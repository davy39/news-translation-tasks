---
title: Comment configurer TypeORM DataSource dans votre projet NestJS
subtitle: ''
author: Alaran Ayobami
co_authors: []
series: null
date: '2024-04-25T11:22:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-typeorm-datasource-nestjs-app
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/hq720-1-1.jpg
tags:
- name: nestjs
  slug: nestjs
- name: TypeScript
  slug: typescript
seo_title: Comment configurer TypeORM DataSource dans votre projet NestJS
seo_desc: 'Hey there! 👋 Ever since I started working with NestJS, I''ve been looking
  for a reliable way to manage my database with TypeORM. Today, I''ll share my journey
  and the steps I took to get it all set up.

  Alright, before we dive in, let''s try to understa...'
---

Salut à tous ! 👋 Depuis que j'ai commencé à travailler avec NestJS, je cherchais un moyen fiable de gérer ma base de données avec TypeORM. Aujourd'hui, je vais partager mon parcours et les étapes que j'ai suivies pour tout configurer.

Très bien, avant de plonger dans le vif du sujet, essayons de comprendre ce que sont TypeORM et NestJS.

### Table des matières :

* [Qu'est-ce que TypeORM ?](#heading-quest-ce-que-typeorm)
* [Qu'est-ce que NestJS ?](#heading-quest-ce-que-nestjs)
* [Prérequis du tutoriel](#heading-prerequis-du-tutoriel)
* [Comment configurer un projet NestJS](#heading-comment-configurer-un-projet-nestjs)
* [Comment configurer TypeORM DataSource pour la persistance des données](#heading-comment-configurer-typeorm-datasource-pour-la-persistance-des-donnees)
* [Étendre le dépôt DataSource pour des méthodes personnalisées](#heading-etendre-le-depot-datasource-pour-des-methodes-personnalisees)
* [Conclusion](#heading-conclusion)
* [Ressources](#heading-ressources)

## Qu'est-ce que TypeORM ?

TypeORM est un outil de [mappage objet-relationnel (ORM)](https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/) qui simplifie le travail avec les bases de données dans les applications Node.js et TypeScript. Il prend en charge diverses bases de données comme MySQL, PostgreSQL, SQLite, et plus encore, permettant aux développeurs d'utiliser des concepts de programmation orientée objet au lieu de traiter avec des requêtes SQL de bas niveau. 

TypeORM fournit également des fonctionnalités comme les migrations de schéma, la construction de requêtes et la gestion des relations entre les tables.

## Qu'est-ce que NestJS ?

NestJS est un framework Node.js progressif conçu pour construire des applications côté serveur efficaces, fiables et évolutives. Il tire parti des fonctionnalités de TypeScript pour permettre aux développeurs d'écrire du code structuré et maintenable. 

NestJS adopte un modèle d'architecture modulaire, permettant d'organiser le code en modules, contrôleurs, services et fournisseurs. Il fournit un support intégré pour des fonctionnalités comme l'injection de dépendances, les middlewares et GraphQL, ce qui en fait un choix populaire pour construire des applications web modernes et des API. 

De plus, NestJS s'intègre parfaitement avec d'autres bibliothèques et frameworks, y compris TypeORM, pour rationaliser les flux de travail de développement. Sous le capot, il utilise un framework de serveur HTTP robuste comme Express (par défaut) et peut être configuré pour utiliser d'autres frameworks de serveur HTTP Node.js. 

Très bien, c'est beaucoup, n'est-ce pas ? Eh bien, avant de continuer, essayons de décomposer la phrase, 'NestJS est un framework Node.js progressif', ce qui signifie simplement que NestJS tire parti des dernières fonctionnalités du langage JavaScript et des frameworks serveur, offrant ainsi une flexibilité aux développeurs pour écrire du code dans le langage le plus adapté à leurs projets.[(Source)](https://docs.nestjs.com/)

## Prérequis du tutoriel

- Node.js. Au moins la version 18
- npm. Au moins la version 8
- Postgresql. [Télécharger ici](https://www.postgresql.org/download/) 
- Familiarité de base avec Typescirpt et Nestjs
- Pgadmin 4. [Télécharger ici](https://www.pgadmin.org/download)

## Comment configurer un projet NestJS

Exécutez les commandes suivantes pour installer votre projet NestJS :

```bash
npm i -g @nestjs/cli # installer nestj cli globalement
nest new simple-crm # démarrer un nouveau projet nestjs
```

Après l'installation, exécutez le serveur de développement :

```bash
npm run start:dev # démarrer l'application en mode surveillance
```

Maintenant, testons notre projet pour voir si le `nest-cli` a correctement configuré tout le code de base, en envoyant une requête get à l'URL racine /

![init_test](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_18-1.png)
_init_test_



Super ! Notre projet est opérationnel.

### Comment configurer TypeORM DataSource pour la persistance des données

```bash
npm install --save @nestjs/typeorm typeorm # pilotes nestjs typeorm
npm install --save pg # pilote typeorm postgressql
```

Créons la base de données pour le projet à partir de l'interface Pgadmin 4

Ouvrez l'interface Pgadmin 4 et cliquez avec le bouton droit sur l'onglet Bases de données pour créer une nouvelle base de données, comme ceci 👍.

![create_db-1](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_18-2.png)
_create_db-1_

![create_db-2](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_18-3.png)
_create_db-2_

Confirmez que votre base de données a été créée avec succès.

![confirm_db](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_18-4.png)
_confirm_db_

Super, il est temps d'ajouter la base de données à notre application NestJS en utilisant TypeORM.

Créez un nouveau dossier, **datasource** dans le dossier **src/** de votre application, comme ceci 👍

![datasource_folder](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_18-5.png)
_confirm_folder_

Créez un nouveau fichier **typeorm.module.ts**, dans le dossier **datasource**, et ajoutez le code suivant :

```typescript 
import { DataSource } from 'typeorm';
import { Global, Module } from '@nestjs/common';

@Global() // rend le module disponible globalement pour d'autres modules une fois importé dans les modules de l'application
@Module({
  imports: [],
  providers: [
    {
      provide: DataSource, // ajoute la datasource en tant que fournisseur
      inject: [],
      useFactory: async () => {
        // utilisation de la fonction factory pour créer l'instance de datasource
        try {
          const dataSource = new DataSource({
            type: 'postgres',
            host: 'localhost',
            port: 5432,
            username: 'ayo',
            password: 'haywon',
            database: 'simple-crm_db',
            synchronize: true,
            entities: [`${__dirname}/../**/**.entity{.ts,.js}`], // cela chargera automatiquement tous les fichiers d'entité dans le dossier src
          });
          await dataSource.initialize(); // initialise la source de données
          console.log('Base de données connectée avec succès');
          return dataSource;
        } catch (error) {
          console.log('Erreur de connexion à la base de données');
          throw error;
        }
      },
    },
  ],
  exports: [DataSource],
})
export class TypeOrmModule {}

```

Ajoutez le module TypeORM au tableau des imports du module App, comme ceci 👍

```typescript
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { TypeOrmModule } from './datasource/typeorm.module';

@Module({
  imports: [TypeOrmModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

```

Ensuite, enregistrez et confirmez à partir de votre console si la base de données a été connectée avec succès.

![db_conn_success](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_19-1.png)
_show_db_success_conn_

Si vous voyez que la base de données est connectée avec succès, bon travail ! Sinon, revenez aux étapes précédentes pour voir si vous avez suivi les configurations correctement.

Maintenant, nous pouvons continuer à utiliser notre service `datasource` en tirant parti de TypeORM.

Créons le module `users`, le contrôleur, le fournisseur et l'entité pour interagir avec notre base de données nouvellement connectée.

```bash
nest g module users && nest g service users && nest g controller users
```

La commande ci-dessus générera le module `users`, le service et le contrôleur et mettra à jour le **app.module.ts** avec le module `users`.

Ajoutez le code suivant à l'intérieur du fichier **users.entity.ts** et redémarrez votre serveur de développement pour créer la table `user` dans la base de données.

```typescript
import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity('user')
export class UserEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ unique: true })
  username: string;

  @Column()
  password: string;
}

```

Vérifiez votre interface Pgadmin 4 et confirmez que TypeORM a automatiquement chargé le `UserEntity` et créé la table `user` dans votre base de données, comme ceci 👍.

![confirm_user_table](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_19-2.png)
_confirm_user_table_

Vous devrez peut-être actualiser la base de données si vous ne la voyez pas au premier abord.

Maintenant, implémentons notre premier gestionnaire de service `users`, ajoutez le code suivant à votre fichier **users.service.ts** :

```typescript
import {
  HttpException,
  HttpStatus,
  Injectable,
  InternalServerErrorException,
  Logger,
} from '@nestjs/common';
import { DataSource } from 'typeorm';
import { UserEntity } from './users.entity';

export interface CreateUser {
  username: string;
  password: string;
}

@Injectable()
export class UsersService {
  private userRepository;
  private logger = new Logger();
  //   injecter le fournisseur Datasource
  constructor(private dataSource: DataSource) {
    // obtenir le dépôt de la table des utilisateurs pour interagir avec la base de données
    this.userRepository = this.dataSource.getRepository(UserEntity);
  }
  //  créer un gestionnaire pour créer un nouvel utilisateur et l'enregistrer dans la base de données
  async createUser(createUser: CreateUser): Promise<UserEntity> {
    try {
      const user = await this.userRepository.create(createUser);
      return await this.userRepository.save(user);
    } catch (err) {
      if (err.code == 23505) {
        this.logger.error(err.message, err.stack);
        throw new HttpException('Le nom d\'utilisateur existe déjà', HttpStatus.CONFLICT);
      }
      this.logger.error(err.message, err.stack);
      throw new InternalServerErrorException(
        'Quelque chose s\'est mal passé, réessayez !',
      );
    }
  }
}

```

Nous avons ajouté la méthode `createUser` pour gérer la création d'un utilisateur lorsqu'une requête POST est envoyée avec le corps de requête requis au contrôleur d'extrémité qui utilise la méthode de service `createUser`. 

La fonction prend un objet `createUser` comme argument de type interface `CreateUser`. Habituellement, cela devrait être un DTO (Data Transfer Object) pour la structure de type de données et la validation, mais comme cela est hors du cadre de ce tutoriel, nous utilisons l'interface uniquement pour la forme des données. 

Nous avons appelé la méthode `create` du `userRepository` puis assigné son retour à la variable `user` pour contenir le nouvel objet utilisateur créé. Nous avons ensuite appelé la méthode `save` pour enregistrer l'objet dans la base de données.

Maintenant, utilisons le gestionnaire de service `createUser` dans notre contrôleur `users` qui gère la requête POST pour créer un nouvel utilisateur.

```typescript
import { Body, Controller, Post } from '@nestjs/common';
import { CreateUser, UsersService } from './users.service';

@Controller('users')
export class UsersController {
  constructor(private userService: UsersService) {}

  @Post('/create')
  //   gère la requête post à l'extrémité /users/create pour créer un nouvel utilisateur
  async signUp(@Body() user: CreateUser) {
    return await this.userService.createUser(user);
  }
}


```

Testez la nouvelle extrémité créée, en envoyant une requête POST à `http://localhost:3000/users/create` avec le nom d'utilisateur et le mot de passe comme corps de la requête.

![test_user_create](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_19-3.png)
_test_user_create_endpoint_

Très bien, vérifions la base de données juste pour être sûr que tout est là, car nous avons déjà obtenu un code de statut de réponse 201 qui devrait suffire pour savoir que notre application interagit correctement avec notre base de données en utilisant le DataSource TypeORM.

![confirm_user_db](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_19-4.png)
_confirm_user_db_

### Étendre le dépôt DataSource pour des méthodes personnalisées

Que vous cherchiez à optimiser les requêtes de base de données, à introduire de nouvelles opérations de manipulation de données ou à intégrer des services tiers, l'extension du dépôt DataSource avec des méthodes personnalisées peut être un changement de jeu pour interagir avec la base de données de manière transparente. 

Ici, nous allons explorer les avantages des méthodes personnalisées et fournir un guide étape par étape pour les implémenter dans vos applications NestJS. Alors, plongeons et déverrouillons tout le potentiel du dépôt DataSource !

Certains des avantages de base des méthodes personnalisées du dépôt sont :

**Fonctionnalité sur mesure :** Les méthodes personnalisées permettent aux développeurs d'introduire des fonctionnalités spécifiques qui ne sont pas disponibles dans le dépôt DataSource standard. En adaptant le dépôt DataSource avec des méthodes personnalisées, les développeurs peuvent répondre à des cas d'utilisation uniques, des opérations de manipulation de données et d'agrégation, ou des optimisations qui sont essentielles pour les exigences de leur projet.

**Performance optimisée :** Les méthodes personnalisées peuvent être conçues pour optimiser les requêtes de base de données, la récupération de données et les opérations de manipulation de données, conduisant à une performance et une efficacité améliorées. En tirant parti des méthodes personnalisées, les développeurs peuvent implémenter des algorithmes optimisés, des mécanismes de mise en cache ou des optimisations de requêtes adaptés aux besoins et caractéristiques spécifiques de leurs applications.

**Amélioration de la réutilisabilité et de la maintenabilité du code :** Les méthodes personnalisées favorisent la réutilisabilité du code en encapsulant une logique, des algorithmes ou des opérations spécifiques dans des composants réutilisables. En modularisant les méthodes personnalisées, les développeurs peuvent maintenir un code plus propre, plus organisé et plus maintenable, ce qui facilite la gestion, le débogage et l'amélioration du dépôt DataSource à long terme.

D'accord, c'est tout, passons à l'action. Nous avons donc une application CRM simple qui a à voir avec la gestion des utilisateurs. Ajoutons une méthode de dépôt personnalisée qui peut nous aider à filtrer les utilisateurs par nom d'utilisateur.

Pour implémenter cela, créons notre module `datasource` et notre service `datasource`. Nous allons créer ces fichiers pour nous aligner avec les principes de modularité du modèle architectural NestJS.

Créez les fichiers à l'intérieur de votre dossier **datasource** précédemment créé et ajoutez le code suivant :

```typescript
// datasource.module.ts
import { Module } from '@nestjs/common';
import { TypeOrmModule } from './typeorm.module';
import { DataSourceService } from './datasource.service';

@Module({
  imports: [TypeOrmModule],
  providers: [DataSourceService],
  exports: [DataSourceService],
})
export class DataSourceModule {}

```

```typescript
// datasource.service.ts
import { Injectable } from '@nestjs/common';
import { UserEntity } from 'src/users/users.entity';
import { DataSource } from 'typeorm';

export interface UsernameQuery {
  username: string;
}

@Injectable()
export class DataSourceService {
  constructor(private dataSource: DataSource) {}

  //   étendre userRepository pour ajouter des méthodes personnalisées
  userCustomRepository = this.dataSource.getRepository(UserEntity).extend({
    async filterUser(usernameQuery: UsernameQuery): Promise<UserEntity[]> {
      const { username } = usernameQuery;
      console.log(username);
      // initialiser un constructeur de requêtes pour le userrepository
      const query = this.createQueryBuilder('user');
      //   filtrer l'utilisateur où le nom d'utilisateur est comme le nom d'utilisateur passé
      query.where('(LOWER(user.username) LIKE LOWER(:username))', {
        username: `%${username}%`,
      });
      return await query.getMany();
    },
  });
}

```

À partir du code **datasource.service.ts** ci-dessus, nous avons étendu le `UserRepository`, en appelant la méthode `getRepository` sur le service `dataSource` et en passant `UserEntity` comme argument pour obtenir le dépôt pour la table particulière.

Ensuite, nous avons appelé la méthode `extend` sur le `userRepository` que nous avons obtenu de notre `getRepository` pour ajouter notre méthode personnalisée. Dans notre méthode `extend`, nous avons passé un objet qui contiendra toutes nos méthodes personnalisées pour le dépôt personnalisé que nous avons assigné au `userCustomRepository`. Ici, nous avons simplement ajouté une seule méthode personnalisée à notre dépôt d'utilisateurs personnalisé qui est `filterUser`. Elle exécute une requête de filtre sur la table des utilisateurs par le nom d'utilisateur fourni.

Puisque notre `DataSourseService` est injectable, nous pouvons l'injecter dans notre `UserService` et consommer la méthode `filterUser` nouvellement créée après avoir ajouté le `DataSourceModule` au tableau des imports du module utilisateur comme ceci 👍

```typescript
// users.module.ts
import { Module } from '@nestjs/common';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';
import { DataSourceModule } from 'src/datasource/datasource.module';

@Module({
  imports: [DataSourceModule], // ajouter le DataSourceModule au tableau d'importation 
  providers: [UsersService],
  controllers: [UsersController],
})
export class UsersModule {}

```

Consommons la méthode de filtre de `CustomUserRepository` dans notre `UserService` pour filtrer les utilisateurs par tout nom d'utilisateur passé comme argument de notre requête lors de l'envoi de la requête.

```typescript
// users.service.ts
import {
  HttpException,
  HttpStatus,
  Injectable,
  InternalServerErrorException,
  Logger,
} from '@nestjs/common';
import { DataSource } from 'typeorm';
import { UserEntity } from './users.entity';
import {
  DataSourceService,
  UsernameQuery,
} from 'src/datasource/datasource.service';

export interface CreateUser {
  username: string;
  password: string;
}

@Injectable()
export class UsersService {
  private userRepository;
  private customUserRepository;
  private logger = new Logger();
  //   injecter le fournisseur Datasource
  constructor(
    private dataSource: DataSource,
    private dataSourceService: DataSourceService, // injecter notre service datasource
  ) {
    // obtenir le dépôt de la table des utilisateurs pour interagir avec la base de données
    this.userRepository = this.dataSource.getRepository(UserEntity);
    // assigner le userCustomRepository du dataSourceService au customUserRepository de la classe
    this.customUserRepository = this.dataSourceService.userCustomRepository;
  }
  //  créer un gestionnaire pour créer un nouvel utilisateur et l'enregistrer dans la base de données
  async createUser(createUser: CreateUser): Promise<UserEntity> {
    try {
      const user = await this.userRepository.create(createUser);
      return await this.userRepository.save(user);
    } catch (err) {
      if (err.code == 23505) {
        this.logger.error(err.message, err.stack);
        throw new HttpException('Le nom d\'utilisateur existe déjà', HttpStatus.CONFLICT);
      }
      this.logger.error(err.message, err.stack);
      throw new InternalServerErrorException(
        'Quelque chose s\'est mal passé, réessayez !',
      );
    }
  }
  // le gestionnaire filterByUsername du service utilisateur
  async filterByUsername(usernameQuery: UsernameQuery): Promise<UserEntity[]> {
    try {
    // appel de la méthode personnalisée filterUser du customUserRepository
      return await this.customUserRepository.filterUser(usernameQuery);
    } catch (err) {
      this.logger.error(err.message, err.stack);
      throw new InternalServerErrorException(
        'Quelque chose s\'est mal passé, réessayez !',
      );
    }
  }
}

```

À partir du code ci-dessus, nous avons injecté notre service `DataSourceService` personnalisé en ajoutant ce qui suit au constructeur de la classe `private dataSourceService: DataSourceService,`.

Le service `filterByUsername` gère la requête que nous consommons dans notre méthode personnalisée `filterUser` `await _this_.customUserRepository.filterUser(usernameQuery);`, qui retournera une promesse.

Maintenant, utilisons ce gestionnaire de service dans notre contrôleur utilisateur pour filtrer les utilisateurs par leur nom d'utilisateur.

```typescript
// users.controller.ts
import { Body, Controller, Get, Post, Query } from '@nestjs/common';
import { CreateUser, UsersService } from './users.service';
import { UserEntity } from './users.entity';
import { UsernameQuery } from 'src/datasource/datasource.service';

@Controller('users')
export class UsersController {
  constructor(private userService: UsersService) {}

  @Post('/create')
  //   gère la requête post à l'extrémité /users/create pour créer un nouvel utilisateur
  async signUp(@Body() user: CreateUser): Promise<UserEntity> {
    return await this.userService.createUser(user);
  }

  @Get('') // gestionnaire de requête get qui retourne les résultats filtrés de la table des utilisateurs
  async filterUser(
    @Query() usernameQuery: UsernameQuery // extrait le paramètre de requête username de l'URL de l'extrémité,
  ): Promise<UserEntity[]> {
    return await this.userService.filterByUsername(usernameQuery);
  }
}

```

Testons notre extrémité de filtre,

![test-filter](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot_2024_04_19-5.png)
_test_filter_endpoint_

Ici, nous avons obtenu une liste avec un objet utilisateur dont le nom d'utilisateur est similaire au nom d'utilisateur que nous avons passé en tant que requête.

## Conclusion

Voilà ! C'est tout, vous êtes maintenant prêt à commencer à travailler avec NestJS, TypeORM et DataSource.

Merci d'avoir lu !

Si vous l'avez trouvé utile, veuillez le partager avec vos amis et collègues ! Restez à l'écoute pour plus de contenu instructif, et continuons à apprendre et à grandir ensemble. À la construction de solutions plus intelligentes et plus efficaces avec NestJS !

### Ressources

* [Page de documentation NestJS](https://docs.nestjs.com/) 
* [Page de documentation TypeORM](https://typeorm.io/)
* [Cours complet sur NestJS](https://www.youtube.com/watch?v=sFnAHC9lLaw&t=935s)

### Liens de contact

* [Twitter](https://twitter.com/ayobamialaran)
* [LinkedIn](https://www.linkedin.com/in/ayobami-alaran/)
* [GitHub](https://github.com/Ayobami6)