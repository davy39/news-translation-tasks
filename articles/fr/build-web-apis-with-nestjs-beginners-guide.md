---
title: Conclusion
date: '2020-06-15T23:12:08.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/build-web-apis-with-nestjs-beginners-guide
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/1_75rW-2GHINvKPaoPbtGo6w-1.png
tags:
- name: api
  slug: api
- name: node js
  slug: node-js
- name: postgres
  slug: postgres
- name: TypeScript
  slug: typescript
seo_desc: "By Victor Onwuzor\nNestJS is an MVC framework for building efficient, scalable\
  \ Node.js server-side applications. \nIt is built with and fully supports TypeScript\
  \ (yet still enables developers to code in pure JavaScript). It also combines elements\
  \ of Ob..."
---


Par Victor Onwuzor

<!-- more -->

NestJS est un framework MVC pour construire des applications côté serveur [Node.js][1] efficaces et évolutives.

Il est construit avec et supporte entièrement [TypeScript][2] (tout en permettant aux développeurs de coder en JavaScript pur). Il combine également des éléments de Programmation Orientée Objet, de Programmation Fonctionnelle et de Programmation Fonctionnelle Réactive.

L'un des principaux avantages de Nest est qu'il fournit une architecture d'application prête à l'emploi qui permet aux développeurs et aux équipes de créer des applications hautement testables, évolutives, faiblement couplées et faciles à maintenir.

## Ce que nous allons construire

Dans cet article, je vais vous accompagner dans vos premiers pas avec Nest. Nous allons construire un Mini Blog qui est une application API Web RESTful.

Cette simple application de Mini Blog couvrira :

-   La configuration de Sequelize et d'une base de données Postgres
-   L'authentification avec Passport (Connexion et Inscription)
-   La validation des entrées utilisateur
-   La protection des routes avec JWT
-   La création, la lecture, la mise à jour et la suppression d'un article de blog (CRUD)

## Prérequis

Une connaissance de TypeScript et de JavaScript est très importante pour suivre ce tutoriel. Une expérience avec Angular est un plus, mais ne vous inquiétez pas – cet article expliquera chaque concept que vous devez connaître sur Nest.

Vous devrez installer [Postman][3], car nous l'utiliserons pour tester nos points de terminaison (endpoints) d'API. Assurez-vous également d'avoir [Node.js][4] (>= 8.9.0) installé sur votre machine. [Enfin, vous pouvez trouver un lien vers le dépôt GitHub du projet final ici][5].

## Blocs de construction

Avant de commencer, nous allons discuter de certaines abstractions/concepts qui vous aideront à savoir où placer la logique métier spécifique d'un projet à l'autre.

Nest est très similaire à Angular – donc si vous êtes familier avec les concepts d'Angular, cela vous semblera très simple.

Néanmoins, je vais supposer que vous n'avez aucune connaissance de ces concepts et je vais vous les expliquer.

### Contrôleur

Le contrôleur est responsable de l'écoute des requêtes qui arrivent dans votre application. Il formule ensuite les réponses qui en sortent.

Par exemple, lorsque vous effectuez un appel API vers `/posts`, le contrôleur gérera cette requête et renverra la réponse appropriée que vous avez spécifiée.

```
import { Controller, Get } from '@nestjs/common';

@Controller('posts')
export class PostsController {
    @Get()
    findAll(): string {
        return 'This action returns all posts';
    }

    @Get(:id)
    findOne(@Param('id') id: number): string {
        return 'This action returns one post';
    }
}
```

Il s'agit simplement d'une déclaration de classe de base en TypeScript/JavaScript avec un décorateur `@Controller`. Tous les contrôleurs Nest doivent avoir ce décorateur qui est **requis** pour définir un contrôleur de base dans Nest.

Nest vous permet de spécifier vos routes en tant que paramètre dans le décorateur `@Controller()`. Cela vous aide à regrouper un ensemble de routes liées et minimise la répétition de code. Toute requête vers `/posts` sera gérée par ce contrôleur.

Au niveau des méthodes de classe, vous pouvez spécifier quelle méthode doit gérer les requêtes HTTP `GET`, `POST`, `DELETE`, `PUT/PATCH`.

Dans notre exemple, la méthode `findAll()` avec le décorateur `@Get()` gère toutes les requêtes HTTP `GET` pour obtenir tous les articles de blog. Tandis que la méthode `findOne()` avec le décorateur `@Get(':id')` gérera une requête `GET /posts/1`.

### Providers

Les providers ont été conçus pour abstraire toute forme de complexité et de logique dans une classe séparée. Un provider peut être un service, un repository, une factory ou un helper.

Les providers sont des classes TypeScript/JavaScript simples avec un décorateur `@Injectable()` précédant leur déclaration. Tout comme les services dans Angular, vous pouvez créer et injecter des providers dans d'autres contrôleurs ou d'autres providers également.

Un bon cas d'utilisation pour un provider de service est de créer un `PostService` qui abstrait toute communication avec la base de données dans ce service. Cela permet de garder le `PostsController` propre et concis.

```
import { Injectable } from '@nestjs/common';
import { Post } from './interfaces/post.interface';

@Injectable()
export class PostsService {
    private readonly posts: Post[] = [];

    create(post: Post) {
        this.posts.push(post);
    }

    findAll(): Post[] {
        return this.posts;
    }
}
```

```
export interface Post {
    title: string;
    body: string;
}
```

Il s'agit simplement d'une classe TypeScript simple avec un décorateur `@Injectable()` (c'est ainsi que Nest sait qu'il s'agit d'un provider). `Post` est juste une interface pour la vérification de type.

Ici, nous utilisons une structure de données simple pour stocker les données. Dans un projet réel, ce service communiquerait avec la base de données.

### Modules

Un module est une classe JavaScript/TypeScript avec le décorateur `@Module()`.  
Le décorateur `@Module()` fournit des métadonnées que Nest utilise pour organiser l'architecture de l'application.

Les modules sont un aspect très important de Nest et chaque application doit fournir au moins un module : le module racine de l'application. Le module racine est le point de départ que Nest utilise pour construire le graphe de l'application.

Le service de post, le contrôleur, l'entité post et tout ce qui concerne les posts doivent être regroupés dans un module (`PostsModule`). Ci-dessous, nous avons défini le `PostsModule`.

```
import { Module } from '@nestjs/common';
import { PostsController } from './posts.controller';
import { PostsService } from './posts.service';

@Module({
    controllers: [PostsController],
    providers: [PostsService],
})
export class PostsModule {}
```

Ensuite, nous importons ce module dans le module racine `AppModule` :

```
import { Module } from '@nestjs/common';
import { PostsModule } from './posts/posts.module';

@Module({
    imports: [PostsModule],
})
export class AppModule {}
```

Le décorateur `@Module()` prend un seul objet dont les propriétés décrivent le module :

-   `**imports:**` Autres modules qui sont nécessaires à ce module.
-   `**exports:**` Par défaut, les modules encapsulent les providers. Il est impossible d'injecter des providers qui ne font pas directement partie du module actuel ou qui ne sont pas exportés des modules importés. Pour rendre les providers du module actuel disponibles pour d'autres modules de l'application, ils doivent être exportés ici. Nous pouvons également exporter les modules que nous avons importés.
-   `**controllers:**` L'ensemble des contrôleurs définis dans ce module qui doivent être instanciés.
-   `**providers:**` En termes simples, tous nos services et providers au sein du module seront ici.

### Intercepteur

Un intercepteur est un ensemble spécialisé de middlewares qui vous permet d'examiner la requête qui entre dans l'application. Vous pouvez examiner la requête soit avant qu'elle n'atteigne le contrôleur, soit après que le contrôleur a terminé la requête avant qu'elle ne parvienne au côté client sous forme de réponse. Vous pouvez manipuler les données lors de leur sortie dans l'intercepteur.

### Guard

Le Guard est également un type spécial de middleware qui est utilisé principalement pour l'authentification et l'autorisation. Il renvoie uniquement une valeur booléenne true ou false.

Les Guards ont une **responsabilité unique** : ils déterminent si une requête donnée sera gérée par le gestionnaire de route ou non, en fonction de certaines conditions (comme les permissions, les rôles, les ACL, etc.) présentes au moment de l'exécution.

Un Guard doit également implémenter l'interface `CanActivate`.

### Pipe

Les Pipes sont également un type spécial de middleware qui se situe entre le client et le contrôleur. Ils sont principalement utilisés pour la validation et la transformation des données avant qu'elles n'arrivent au contrôleur.

### DTO (Data Transfer Object)

Le Data Transfer Object est un objet qui définit comment les données seront envoyées sur le réseau. Ils sont également utilisés pour la validation et la vérification de type.

### Interfaces

Les interfaces TypeScript ne sont utilisées que pour la vérification de type et ne sont pas compilées en code JavaScript.

## Installation

Installez la CLI NestJs. Nest est livré avec une CLI géniale qui facilite l'initialisation d'une application Nest. Dans votre terminal ou invite de commande, exécutez :

`npm i -g @nestjs/cli`

Maintenant, Nest est installé globalement sur votre machine.

Sur votre terminal, déplacez-vous (cd) dans le répertoire où vous souhaitez créer votre application et exécutez les commandes suivantes :

`nest new nest-blog-api`  
`cd nest-blog-api`  
`npm run start:dev`

Naviguez vers `[http://localhost:3000](http://localhost:3000/)` sur l'un de vos navigateurs. Vous devriez voir `Hello World`. Bravo ! Vous avez créé votre première application Nest. Continuons.

**NOTE : Au moment d'écrire ces lignes, si l'exécution de** `**npm run start:dev**` **renvoie une erreur, changez votre** `**typescript:3.4.2**` **dans votre fichier** `**package.json**` **en** `**typescript:3.7.2**`**, puis supprimez le dossier** `**node_modules**` **et le fichier** `**package-lock.json**` **et relancez** `**npm i**`**.**

Votre structure de dossiers devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_qLCtw-62xXAdTHXPy2JAMg.png) _Structure des dossiers Nest_

## Configuration de Sequelize et de la base de données

Nous allons commencer par installer les dépendances suivantes. Assurez-vous que votre terminal est actuellement dans le répertoire racine de votre projet. Exécutez ensuite les commandes suivantes :

`npm install -g sequelize npm install --save sequelize sequelize-typescript pg-hstore pg npm install --save-dev @types/sequelize npm install dotenv --save`

Maintenant, créez un module de base de données. Exécutez `nest generate module /core/database`.

### Interface de base de données

À l'intérieur du dossier database, créez un dossier `interfaces`, puis créez un fichier `dbConfig.interface.ts` à l'intérieur. Ceci est pour l'interface de configuration de la base de données.

Chacun des environnements de base de données doit avoir optionnellement les propriétés suivantes. Copiez et collez le code suivant :

```
export interface IDatabaseConfigAttributes {
    username?: string;
    password?: string;
    database?: string;
    host?: string;
    port?: number | string;
    dialect?: string;
    urlDatabase?: string;
}

export interface IDatabaseConfig {
    development: IDatabaseConfigAttributes;
    test: IDatabaseConfigAttributes;
    production: IDatabaseConfigAttributes;
}
```

### Configuration de la base de données

Maintenant, créons une configuration d'environnement de base de données. À l'intérieur du dossier database, créez un fichier `database.config.ts`. Copiez et collez le code ci-dessous :

```
import * as dotenv from 'dotenv';
import { IDatabaseConfig } from './interfaces/dbConfig.interface';

dotenv.config();

export const databaseConfig: IDatabaseConfig = {
    development: {
        username: process.env.DB_USER,
        password: process.env.DB_PASS,
        database: process.env.DB_NAME_DEVELOPMENT,
        host: process.env.DB_HOST,
        port: process.env.DB_PORT,
        dialect: process.env.DB_DIALECT,
    },
    test: {
        username: process.env.DB_USER,
        password: process.env.DB_PASS,
        database: process.env.DB_NAME_TEST,
        host: process.env.DB_HOST,
        port: process.env.DB_PORT,
        dialect: process.env.DB_DIALECT,
    },
    production: {
        username: process.env.DB_USER,
        password: process.env.DB_PASS,
        database: process.env.DB_NAME_PRODUCTION,
        host: process.env.DB_HOST,
        dialect: process.env.DB_DIALECT,
    },
};
```

L'environnement déterminera quelle configuration doit être utilisée.

### Fichier .env

Dans le dossier racine de notre projet, créez les fichiers `.env` et `.env.sample`. Copiez et collez le code suivant dans les deux fichiers :

```
DB_HOST=localhost
DB_PORT=5432
DB_USER=database_user_name
DB_PASS=database_password
DB_DIALECT=postgres
DB_NAME_TEST=test_database_name
DB_NAME_DEVELOPMENT=development_database_name
DB_NAME_PRODUCTION=production_database_name
JWTKEY=random_secret_key
TOKEN_EXPIRATION=48h
BEARER=Bearer
```

Remplissez les valeurs avec les informations correctes – uniquement dans le fichier `.env` – et assurez-vous qu'il est ajouté au fichier `.gitignore` pour éviter de le pousser en ligne. Le fichier `.env.sample` est destiné à ceux qui souhaitent télécharger votre projet et l'utiliser, vous pouvez donc le pousser en ligne.

**CONSEILS : Votre nom d'utilisateur, votre mot de passe et le nom de la base de données doivent être ceux que vous utilisez pour configurer votre Postgres. Créez une base de données Postgres avec le nom de votre base de données.**

Nest fournit un package `@nestjs/config` prêt à l'emploi pour aider à charger notre fichier `.env`. Pour l'utiliser, nous installons d'abord la dépendance requise.

Exécutez `npm i --save @nestjs/config`.

Importez le `@nestjs/config` dans votre module racine d'application :

```
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';

@Module({
    imports: [
        ConfigModule.forRoot({ isGlobal: true }),
    ]
})
export class AppModule { }
```

Définir `ConfigModule.forRoot({ isGlobal: true })` sur `isGlobal: true` rendra les propriétés du `.env` disponibles dans toute l'application.

### Provider de base de données

Créons un provider de base de données. À l'intérieur du dossier database, créez un fichier appelé `database.providers.ts`.

Le répertoire core contiendra toutes nos configurations de base, partagées, modules, pipes, guards et middlewares.

Dans le fichier `database.providers.ts`, copiez et collez ce code :

```
import { Sequelize } from 'sequelize-typescript';
import { SEQUELIZE, DEVELOPMENT, TEST, PRODUCTION } from '../constants';
import { databaseConfig } from './database.config';

export const databaseProviders = [{
    provide: SEQUELIZE,
    useFactory: async () => {
        let config;
        switch (process.env.NODE_ENV) {
        case DEVELOPMENT:
           config = databaseConfig.development;
           break;
        case TEST:
           config = databaseConfig.test;
           break;
        case PRODUCTION:
           config = databaseConfig.production;
           break;
        default:
           config = databaseConfig.development;
        }
        const sequelize = new Sequelize(config);
        sequelize.addModels(['models goes here']);
        await sequelize.sync();
        return sequelize;
    },
}];
```

Ici, l'application décide dans quel environnement nous fonctionnons actuellement, puis choisit la configuration d'environnement correspondante.

Tous nos modèles seront ajoutés à la fonction `sequelize.addModels([User, Post])`. Actuellement, il n'y a pas de modèles.

**Bonne pratique** : Il est judicieux de conserver toutes les valeurs de chaînes de caractères dans un fichier de constantes et de l'exporter pour éviter les fautes d'orthographe. Vous aurez également un endroit unique pour modifier les choses.

À l'intérieur du dossier core, créez un dossier `constants` et à l'intérieur, créez un fichier `index.ts`. Collez le code suivant :

```
export const SEQUELIZE = 'SEQUELIZE';
export const DEVELOPMENT = 'development';
export const TEST = 'test';
export const PRODUCTION = 'production';
```

Ajoutons le provider de base de données à notre module de base de données. Copiez et collez ce code :

```
import { Module } from '@nestjs/common';
import { databaseProviders } from './database.providers';

@Module({
    providers: [...databaseProviders],
    exports: [...databaseProviders],
})
export class DatabaseModule { }
```

Nous avons exporté le provider de base de données `exports: [...databaseProviders]` pour le rendre **accessible** au reste de l'application qui en a besoin.

Maintenant, importons le module de base de données dans notre module racine d'application pour le rendre disponible à tous nos services.

```
import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { DatabaseModule } from './core/database/database.module';

@Module({
    imports: [
        ConfigModule.forRoot({ isGlobal: true }),
        DatabaseModule,
    ]
})
export class AppModule { }
```

### Définir un préfixe de point de terminaison (endpoint) global

Nous pourrions vouloir que tous nos points de terminaison d'API commencent par `api/v1` pour la gestion des versions. Nous ne voulons pas avoir à ajouter ce préfixe à tous nos contrôleurs. Heureusement, Nest permet de définir un préfixe global.

Dans le fichier `main.ts`, ajoutez `app.setGlobalPrefix('api/v1');`

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
    const app = await NestFactory.create(AppModule);
    // global prefix
    app.setGlobalPrefix('api/v1');
    await app.listen(3000);
}
bootstrap();
```

## Module Utilisateur

Ajoutons un module User pour gérer toutes les opérations liées aux utilisateurs et pour garder une trace de qui crée quel article.

Exécutez `nest generate module /modules/users`.  
Cela ajoutera automatiquement ce module à notre module racine `AppModule`.

### Générer le Service Utilisateur

Exécutez `nest generate service /modules/users`.  
Cela ajoutera automatiquement ce service au module Users.

### Configurer le modèle de schéma de base de données utilisateur

À l'intérieur de `modules/users`, créez un fichier appelé `user.entity.ts`, puis copiez et collez ce code :

```
import { Table, Column, Model, DataType } from 'sequelize-typescript';

@Table
export class User extends Model<User> {
    @Column({
        type: DataType.STRING,
        allowNull: false,
    })
    name: string;

    @Column({
        type: DataType.STRING,
        unique: true,
        allowNull: false,
    })
    email: string;

    @Column({
        type: DataType.STRING,
        allowNull: false,
    })
    password: string;

    @Column({
        type: DataType.ENUM,
        values: ['male', 'female'],
        allowNull: false,
    })
    gender: string;
}
```

Ici, nous spécifions ce que contiendra notre table User. Le décorateur `@Column()` fournit des informations sur chaque colonne de la table. La table User aura les colonnes `name`, `email`, `password` et `gender`. Nous avons importé tous les décorateurs Sequelize de `sequelize-typescript`. Pour en savoir plus sur [Sequelize et TypeScript, consultez ceci][6].

### DTO Utilisateur

Créons notre schéma DTO (**Data Transfer Object**) User. À l'intérieur du dossier users, créez un dossier `dto`. Ensuite, créez un fichier `user.dto.ts` à l'intérieur. Collez le code suivant :

```
export class UserDto {
    readonly name: string;
    readonly email: string;
    readonly password: string;
    readonly gender: string;
}
```

### Provider de Repository Utilisateur

Maintenant, créez un provider de **Repository** User. À l'intérieur du dossier users, créez un fichier `users.providers.ts`. Ce provider est utilisé pour communiquer avec la base de données.

```
import { User } from './user.entity';
import { USER_REPOSITORY } from '../../core/constants';

export const usersProviders = [{
    provide: USER_REPOSITORY,
    useValue: User,
}];
```

Ajoutez cet `export` `const USER_REPOSITORY = 'USER_REPOSITORY';` au fichier de constantes `index.ts`.

Ajoutez également le provider d'utilisateur au module User. Notez que nous avons ajouté le `UsersService` à notre tableau `exports`. C'est parce que nous en aurons besoin en dehors du module User.

```
import { Module } from '@nestjs/common';
import { UsersService } from './users.service';
import { usersProviders } from './users.providers';

@Module({
    providers: [UsersService, ...usersProviders],
    exports: [UsersService],
})
export class UsersModule {}
```

Encapsulons les opérations utilisateur à l'intérieur du `UsersService`. Copiez et collez le code suivant :

```
import { Injectable, Inject } from '@nestjs/common';
import { User } from './user.entity';
import { UserDto } from './dto/user.dto';
import { USER_REPOSITORY } from '../../core/constants';

@Injectable()
export class UsersService {

    constructor(@Inject(USER_REPOSITORY) private readonly userRepository: typeof User) { }

    async create(user: UserDto): Promise<User> {
        return await this.userRepository.create<User>(user);
    }

    async findOneByEmail(email: string): Promise<User> {
        return await this.userRepository.findOne<User>({ where: { email } });
    }

    async findOneById(id: number): Promise<User> {
        return await this.userRepository.findOne<User>({ where: { id } });
    }
}
```

Ici, nous avons injecté le repository utilisateur pour communiquer avec la base de données.

-   `create(user: UserDto)` : Cette méthode crée un nouvel utilisateur dans la table des utilisateurs et renvoie l'objet utilisateur nouvellement créé.
-   `findOneByEmail(email: string)` : Cette méthode est utilisée pour rechercher un utilisateur dans la table des utilisateurs par email et renvoie l'utilisateur.
-   `findOneById(id: number)` : Cette méthode est utilisée pour rechercher un utilisateur dans la table des utilisateurs par l'ID utilisateur et renvoie l'utilisateur.

Nous utiliserons ces méthodes plus tard.

Enfin, ajoutons le modèle User au fichier `database.providers.ts` dans `sequelize.addModels([User]);`.

```
import { Sequelize } from 'sequelize-typescript';
import { SEQUELIZE, DEVELOPMENT, TEST, PRODUCTION } from '../constants';
import { databaseConfig } from './database.config';
import { User } from '../../modules/users/user.entity';

export const databaseProviders = [{
    provide: SEQUELIZE,
    useFactory: async () => {
        let config;
        switch (process.env.NODE_ENV) {
            case DEVELOPMENT:
                config = databaseConfig.development;
                break;
            case TEST:
                config = databaseConfig.test;
                break;
            case PRODUCTION:
                config = databaseConfig.production;
                break;
            default:
                config = databaseConfig.development;
        }
        const sequelize = new Sequelize(config);
        sequelize.addModels([User]);
        await sequelize.sync();
        return sequelize;
    },
}];
```

## Module d'authentification (Auth)

### Générer le module Auth

Ce module gérera l'authentification des utilisateurs (Connexion et Inscription).  
Exécutez `nest generate module /modules/auth`.  
Cela ajoutera automatiquement ce module à notre module racine `AppModule`.

### Générer le service Auth

Exécutez `nest generate service /modules/auth`.  
Cela ajoutera automatiquement ce service au module Auth.

### Générer le contrôleur Auth

Exécutez `nest g co /modules/auth`.  
Cela ajoutera automatiquement ce contrôleur au module Auth.  
**Note :** `**g**` **est un alias pour** `**generate**` **et** `**co**` **pour** `**controller**`**.**

Nous utiliserons [Passport][7] pour gérer notre authentification. Il est simple d'intégrer cette bibliothèque à une application **Nest** en utilisant le module `@nestjs/passport`.

Nous allons implémenter deux stratégies d'authentification pour cette application :

-   **Stratégie Passport locale :** Cette stratégie sera utilisée pour connecter les utilisateurs. Elle vérifiera si l'email/nom d'utilisateur et le mot de passe fournis par l'utilisateur sont valides ou non. Si les identifiants de l'utilisateur sont valides, elle renverra un token et l'objet utilisateur, sinon, elle lèvera une exception.
-   **Stratégie Passport JWT :** Cette stratégie sera utilisée pour protéger les ressources sécurisées. Seuls les utilisateurs authentifiés avec un token valide pourront accéder à ces ressources ou points de terminaison.

### Stratégie Passport locale

Exécutez  
`npm install --save @nestjs/passport passport passport-local`  
`npm install --save-dev @types/passport-local`  
`npm install bcrypt --save`

À l'intérieur du dossier auth, créez un fichier `local.strategy.ts` et ajoutez le code suivant :

```
import { Strategy } from 'passport-local';
import { PassportStrategy } from '@nestjs/passport';
import { Injectable, UnauthorizedException } from '@nestjs/common';
import { AuthService } from './auth.service';

@Injectable()
export class LocalStrategy extends PassportStrategy(Strategy) {
    constructor(private readonly authService: AuthService) {
        super();
    }

    async validate(username: string, password: string): Promise<any>{
        const user = await this.authService.validateUser(username, password);

        if (!user) {
         throw new UnauthorizedException('Invalid user credentials');
        }
        return user;
    }
}
```

Ici, nous importons `Strategy`, `PassportStrategy` et `AuthService`. Nous étendons le `PassportStrategy` pour créer la `LocalStrategy`. Dans notre cas d'utilisation avec passport-local, il n'y a pas d'options de configuration, donc notre constructeur appelle simplement `super()` sans objet d'options.

Nous devons implémenter la méthode `validate()`. Pour la stratégie locale, Passport attend une méthode `validate()` avec la signature suivante : `validate(username: string, password:string): any`.

La majeure partie du travail de validation est effectuée dans notre `AuthService` (avec l'aide de notre `UsersService`), donc cette méthode est assez simple.

Nous appelons la méthode `validateUser()` dans le `AuthService` (que nous n'avons pas encore écrite), qui vérifie si l'utilisateur existe et si le mot de passe est correct. `authService.validateUser()` renvoie null s'il n'est pas valide ou l'objet utilisateur s'il est valide.

Si un utilisateur est trouvé et que les identifiants sont valides, l'utilisateur est renvoyé afin que Passport puisse terminer ses tâches (par exemple, créer la propriété `user` sur l'objet `Request`), et le pipeline de gestion des requêtes peut continuer. S'il n'est pas trouvé, nous levons une exception et laissons notre [couche d'exceptions][8] la gérer.

Maintenant, ajoutez le `PassportModule`, `UsersModule` et `LocalStrategy` à notre `AuthModule`.

```
import { Module } from '@nestjs/common';
import { PassportModule } from '@nestjs/passport';
import { AuthService } from './auth.service';
import { AuthController } from './auth.controller';
import { UsersModule } from '../users/users.module';
import { LocalStrategy } from './local.strategy';

@Module({
    imports: [
        PassportModule,
        UsersModule,
    ],
    providers: [
        AuthService,
        LocalStrategy,
    ],
    controllers: [AuthController],
})
export class AuthModule {}
```

### AuthService

Implémentons la méthode `validateUser()`.

```
import { Injectable } from '@nestjs/common';
import * as bcrypt from 'bcrypt';
import { UsersService } from '../users/users.service';

@Injectable()
export class AuthService {
    constructor(private readonly userService: UsersService) { }

    async validateUser(username: string, pass: string) {
        // find if user exist with this email
        const user = await this.userService.findOneByEmail(username);
        if (!user) {
            return null;
        }

        // find if user password match
        const match = await this.comparePassword(pass, user.password);
        if (!match) {
            return null;
        }

        // tslint:disable-next-line: no-string-literal
        const { password, ...result } = user['dataValues'];
        return result;
    }

    private async comparePassword(enteredPassword, dbPassword) {
        const match = await bcrypt.compare(enteredPassword, dbPassword);
        return match;
    }
}
```

Ici, nous vérifions si l'utilisateur existe avec l'email fourni. Ensuite, nous vérifions si le mot de passe dans la base de données correspond à ce que l'utilisateur a fourni. Si l'un de ces contrôles échoue, nous renvoyons `null`, sinon, nous renvoyons l'objet utilisateur.

`comparePassword(enteredPassword, dbPassword) :` Cette méthode privée compare le mot de passe saisi par l'utilisateur et le mot de passe de l'utilisateur en base de données et renvoie un booléen. Si le mot de passe correspond, elle renvoie true. Sinon, elle renvoie false.

### Stratégie Passport JWT

Exécutez  
`npm install @nestjs/jwt passport-jwt`  
`npm install @types/passport-jwt --save-dev`

À l'intérieur du dossier auth, créez un fichier `jwt.strategy.ts` et ajoutez le code suivant :

```
import { ExtractJwt, Strategy } from 'passport-jwt';
import { PassportStrategy } from '@nestjs/passport';
import { Injectable, UnauthorizedException } from '@nestjs/common';
import { UsersService } from '../users/users.service';

@Injectable()
export class JwtStrategy extends PassportStrategy(Strategy) {
    constructor(private readonly userService: UsersService) {
        super({
             jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
             ignoreExpiration: false,
             secretOrKey: process.env.JWTKEY,
        });
    }

    async validate(payload: any) {
        // check if user in the token actually exist
        const user = await this.userService.findOneById(payload.id);
        if (!user) {
            throw new UnauthorizedException('You are not authorized to perform the operation');
        }
        return payload;
    }
}
```

Ici, nous étendons `PassportStrategy`. À l'intérieur du `super()`, nous avons ajouté un objet d'options. Dans notre cas, ces options sont :

-   `jwtFromRequest :` fournit la méthode par laquelle le JWT sera extrait de la `Request`. Nous utiliserons l'approche standard consistant à fournir un token bearer dans l'en-tête Authorization de nos requêtes API.
-   `ignoreExpiration` : pour être explicite, nous choisissons le réglage par défaut `false`, qui délègue la responsabilité de s'assurer qu'un JWT n'a pas expiré au module Passport. Cela signifie que si notre route reçoit un JWT expiré, la requête sera refusée et une réponse `401 Unauthorized` sera envoyée. Passport gère cela automatiquement pour nous de manière pratique.
-   `secretOrKey` : C'est notre clé secrète pour le token. Elle utilisera la clé secrète de notre fichier `.env`.
-   La méthode `validate(payload: any)` : Pour la stratégie JWT, Passport vérifie d'abord la signature du JWT et décode le JSON. Il invoque ensuite notre méthode `validate()` en passant le JSON décodé comme paramètre unique. Basé sur le fonctionnement de la signature JWT, nous sommes garantis de recevoir un token valide que nous avons précédemment signé et délivré à un utilisateur valide. Nous confirmons si l'utilisateur existe avec l'ID du payload utilisateur. Si l'utilisateur existe, nous renvoyons l'objet utilisateur, et Passport l'attachera comme propriété sur l'objet `Request`. Si l'utilisateur n'existe pas, nous levons une exception.

Maintenant, ajoutez la `JwtStrategy` et le `JwtModule` au `AuthModule` :

```
import { Module } from '@nestjs/common';
import { PassportModule } from '@nestjs/passport';
import { JwtModule } from '@nestjs/jwt';
import { AuthService } from './auth.service';
import { AuthController } from './auth.controller';
import { UsersModule } from '../users/users.module';
import { LocalStrategy } from './local.strategy';
import { JwtStrategy } from './jwt.strategy';

@Module({
    imports: [
        PassportModule,
        UsersModule,
        JwtModule.register({
            secret: process.env.JWTKEY,
            signOptions: { expiresIn: process.env.TOKEN_EXPIRATION },
        }),
    ],
    providers: [
        AuthService,
        LocalStrategy,
        JwtStrategy
    ],
    controllers: [AuthController],
})
export class AuthModule { }
```

Nous configurons le `JwtModule` en utilisant `register()`, en passant un objet de configuration.

Ajoutons d'autres méthodes dont nous aurons besoin pour connecter et créer un nouvel utilisateur dans `AuthService` :

```
import { Injectable } from '@nestjs/common';
import * as bcrypt from 'bcrypt';
import { JwtService } from '@nestjs/jwt';
import { UsersService } from '../users/users.service';

@Injectable()
export class AuthService {
    constructor(
        private readonly userService: UsersService,
        private readonly jwtService: JwtService,
    ) { }

    async validateUser(username: string, pass: string) {
        // find if user exist with this email
        const user = await this.userService.findOneByEmail(username);
        if (!user) {
            return null;
        }

        // find if user password match
        const match = await this.comparePassword(pass, user.password);
        if (!match) {
            return null;
        }

        // tslint:disable-next-line: no-string-literal
        const { password, ...result } = user['dataValues'];
        return result;
    }

    public async login(user) {
        const token = await this.generateToken(user);
        return { user, token };
    }

    public async create(user) {
        // hash the password
        const pass = await this.hashPassword(user.password);

        // create the user
        const newUser = await this.userService.create({ ...user, password: pass });

        // tslint:disable-next-line: no-string-literal
        const { password, ...result } = newUser['dataValues'];

        // generate token
        const token = await this.generateToken(result);

        // return the user and the token
        return { user: result, token };
    }

    private async generateToken(user) {
        const token = await this.jwtService.signAsync(user);
        return token;
    }

    private async hashPassword(password) {
        const hash = await bcrypt.hash(password, 10);
        return hash;
    }

    private async comparePassword(enteredPassword, dbPassword) {
        const match = await bcrypt.compare(enteredPassword, dbPassword);
        return match;
    }
}
```

Importez et injectez `JwtService`.

-   `login(user) :` Cette méthode est utilisée pour connecter l'utilisateur. Elle prend les informations de l'utilisateur, génère un token avec celles-ci, puis renvoie le token et l'objet utilisateur.
-   `create(user) :` Cette méthode est utilisée pour créer un nouvel utilisateur. Elle prend les informations de l'utilisateur, hache le mot de passe, enregistre l'utilisateur dans la base de données, supprime le mot de passe de l'utilisateur nouvellement renvoyé, génère un token avec l'objet utilisateur, puis renvoie le token et l'objet utilisateur.
-   `generateToken(user) :` Cette méthode privée génère un token puis le renvoie.
-   `hashPassword(password) :` Cette méthode privée hache le mot de passe de l'utilisateur et renvoie le mot de passe haché.

Nous utiliserons toutes ces fonctions plus tard.

### AuthController

Maintenant, créons nos méthodes `signup` et `login` :

```
import { Controller, Body, Post, UseGuards, Request } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { AuthService } from './auth.service';
import { UserDto } from '../users/dto/user.dto';

@Controller('auth')
export class AuthController {
    constructor(private authService: AuthService) {}

    @UseGuards(AuthGuard('local'))
    @Post('login')
    async login(@Request() req) {
        return await this.authService.login(req.user);
    }

    @Post('signup')
    async signUp(@Body() user: UserDto) {
        return await this.authService.create(user);
    }
}
```

Lorsque nous appelons le point de terminaison POST `api/v1/auth/login`, cela appellera `@UseGuards(AuthGuard('local'))`. Cela prendra l'email/nom d'utilisateur et le mot de passe, puis exécutera la méthode `validate` sur notre classe de stratégie locale. Le `login(@Request() req)` générera un token JWT et le renverra.

Le point de terminaison POST `api/v1/auth/signup` appellera la méthode `this.authService.create(user)`, créera l'utilisateur et renverra un token JWT.

### Essayons cela...

Ouvrez votre application Postman et assurez-vous qu'elle fonctionne. Envoyez une requête POST à `http://localhost:3000/api/v1/auth/signup` et saisissez vos données de corps (body) pour créer un utilisateur. Vous devriez recevoir un token et l'objet utilisateur en retour.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_FA6_FCcCIJqTw9o37MwaAA.png)

Maintenant que nous avons un utilisateur, connectons-le. Envoyez une requête POST à `http://localhost:3000/api/v1/auth/login` et saisissez uniquement votre nom d'utilisateur et votre mot de passe. Vous devriez recevoir un token et l'objet utilisateur en retour.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_kDI2NMatZQjvcdHzpDNLAA.png)

## Validation

Remarquez que nous ne validons aucune des entrées de l'utilisateur. Ajoutons maintenant la validation à notre application.

Exécutez `npm i class-validator class-transformer --save`.

À l'intérieur du dossier core, créez un dossier pipes puis créez le fichier `validate.pipe.ts`. Copiez et collez le code suivant :

```
import { Injectable, ArgumentMetadata, BadRequestException, ValidationPipe, UnprocessableEntityException } from '@nestjs/common';

@Injectable()
export class ValidateInputPipe extends ValidationPipe {
   public async transform(value, metadata: ArgumentMetadata) {
      try {
        return await super.transform(value, metadata);
      } catch (e) {
         if (e instanceof BadRequestException) {
            throw new UnprocessableEntityException(this.handleError(e.message.message));
         }
      }
   }

   private handleError(errors) {
        return errors.map(error => error.constraints);
   }
}
```

Auto-validons tous nos points de terminaison avec `dto` en liant `ValidateInputPipe` au niveau de l'application. Dans le fichier `main.ts`, ajoutez ceci :

```
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { ValidateInputPipe } from './core/pipes/validate.pipe';

async function bootstrap() {
    const app = await NestFactory.create(AppModule);
    // global endpoints prefix
    app.setGlobalPrefix('api/v1');
    // handle all user input validation globally
    app.useGlobalPipes(new ValidateInputPipe());
    await app.listen(3000);
}
bootstrap();
```

Maintenant, mettons à jour notre fichier `dto` utilisateur :

```
import { IsNotEmpty, MinLength, IsEmail, IsEnum } from 'class-validator';

enum Gender {
    MALE = 'male',
    FEMALE = 'female',
}

export class UserDto {
    @IsNotEmpty()
    readonly name: string;

    @IsNotEmpty()
    @IsEmail()
    readonly email: string;

    @IsNotEmpty()
    @MinLength(6)
    readonly password: string;

    @IsNotEmpty()
    @IsEnum(Gender, {
        message: 'gender must be either male or female',
    })
    readonly gender: Gender;
}
```

Ici, nous importons ces décorateurs de `class-validator`.

-   `@IsNotEmpty() :` garantit que le champ n'est pas vide.
-   `@IsEmail() :` vérifie si l'email saisi est une adresse email valide.
-   `@MinLength(6) :` garantit que le mot de passe ne fait pas moins de six caractères.
-   `@IsEnum :` garantit que seule la valeur spécifiée est autorisée (dans ce cas, male et female).

[class-validator][9] possède des tonnes de décorateurs de validation – n'hésitez pas à les consulter.

**Testons notre validation...**

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_IM9erua1RbvCkQv1yq4hGQ.png)

Sans passer de valeur, j'ai obtenu l'erreur de validation suivante. Notre validation fonctionne maintenant. Cette validation est automatique pour tous les points de terminaison avec un DTO (Data Transfer Object).

### Compte utilisateur unique

Ajoutons un guard qui empêche les utilisateurs de s'inscrire deux fois avec le même email, puisque l'email est unique au niveau du schéma.

À l'intérieur du dossier core, créez un dossier guards, puis créez un fichier `doesUserExist.guard.ts`. Copiez et collez le code suivant :

```
import { CanActivate, ExecutionContext, Injectable, ForbiddenException } from '@nestjs/common';
import { Observable } from 'rxjs';
import { UsersService } from '../../modules/users/users.service';

@Injectable()
export class DoesUserExist implements CanActivate {
    constructor(private readonly userService: UsersService) {}

    canActivate(
      context: ExecutionContext,
    ): boolean | Promise<boolean> | Observable<boolean> {
        const request = context.switchToHttp().getRequest();
        return this.validateRequest(request);
    }

    async validateRequest(request) {
        const userExist = await this.userService.findOneByEmail(request.body.email);
        if (userExist) {
            throw new ForbiddenException('This email already exist');
        }
        return true;
    }
}
```

Maintenant, ajoutons ce guard à notre méthode signup dans `AuthController` :

```

import { Controller, Body, Post, UseGuards, Request } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { AuthService } from './auth.service';
import { UserDto } from '../users/dto/user.dto';
import { DoesUserExist } from '../../core/guards/doesUserExist.guard';

@Controller('auth')
export class AuthController {
    constructor(private authService: AuthService) { }

    @UseGuards(AuthGuard('local'))
    @Post('login')
    async login(@Request() req) {
        return await this.authService.login(req.user);
    }

    @UseGuards(DoesUserExist)
    @Post('signup')
    async signUp(@Body() user: UserDto) {
        return await this.authService.create(user);
    }
}
```

Essayons de créer un utilisateur avec un email qui existe déjà dans notre base de données :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_HuAT1HbVfu4EXWxMBD5QQQ.png)

## Module d'article (Post)

Exécutez `nest g module /modules/posts`.  
Cela ajoutera automatiquement ce module à notre module racine `AppModule`.

### Générer le service Post

Exécutez `nest g service /modules/posts`.  
Cela ajoutera automatiquement ce service au module Post.

### Générer le contrôleur Post

Exécutez `nest g co /modules/posts`.  
Cela ajoutera automatiquement ce contrôleur au module Post.

### Entité Post

Créez un fichier `post.entity.ts` à l'intérieur du dossier posts. Copiez et collez le code suivant :

```
import { Table, Column, Model, DataType, ForeignKey, BelongsTo } from 'sequelize-typescript';
import { User } from '../users/user.entity';

@Table
export class Post extends Model<Post> {
    @Column({
        type: DataType.STRING,
        allowNull: false,
    })
    title: string;

    @Column({
        type: DataType.TEXT,
        allowNull: false,
    })
    body: string;

    @ForeignKey(() => User)
    @Column({
        type: DataType.INTEGER,
        allowNull: false,
    })
    userId: number;

    @BelongsTo(() => User)
    user: User;
}
```

La seule nouveauté ici est le `@ForeignKey(() => User)` spécifiant que la colonne `userId` est l'ID de la table User et `@BelongsTo(() => User)` spécifiant la relation entre la table Post et la table User.

### DTO Post (Data Transfer Object)

À l'intérieur du dossier posts, créez un dossier `dto` puis créez un fichier `post.dto.ts` à l'intérieur. Copiez et collez le code suivant :

```
import { IsNotEmpty, MinLength } from 'class-validator';

export class PostDto {
    @IsNotEmpty()
    @MinLength(4)
    readonly title: string;

    @IsNotEmpty()
    readonly body: string;
}
```

Ici, notre objet de corps de post doit avoir un titre et un corps, et la longueur du titre ne doit pas être inférieure à 4.

### Provider Post

Créez un fichier `posts.providers.ts` à l'intérieur du dossier posts. Copiez et collez le code suivant :

```
import { Post } from './post.entity';
import { POST_REPOSITORY } from '../../core/constants';

export const postsProviders = [{
    provide: POST_REPOSITORY,
    useValue: Post,
}];
```

Ajoutez cet `export` `const POST_REPOSITORY = 'POST_REPOSITORY';` au fichier de constantes `index.ts`.

Ajoutez notre provider Post à notre fichier de module Post :

```
import { Module } from '@nestjs/common';
import { PostsService } from './posts.service';
import { PostsController } from './posts.controller';
import { postsProviders } from './posts.providers';

@Module({
    providers: [PostsService, ...postsProviders],
    controllers: [PostsController],
})
export class PostsModule { }
```

Maintenant, ajoutons notre entité Post à notre provider de base de données. Importez l'entité Post à l'intérieur du fichier `database.providers.ts`, et ajoutez le Post à cette méthode :

`sequelize.addModels([User, Post]);`

### Méthodes du service Post

Copiez et collez ce qui suit à l'intérieur du fichier de service Post :

```
import { Injectable, Inject } from '@nestjs/common';
import { Post } from './post.entity';
import { PostDto } from './dto/post.dto';
import { User } from '../users/user.entity';
import { POST_REPOSITORY } from '../../core/constants';

@Injectable()
export class PostsService {
    constructor(@Inject(POST_REPOSITORY) private readonly postRepository: typeof Post) { }

    async create(post: PostDto, userId): Promise<Post> {
        return await this.postRepository.create<Post>({ ...post, userId });
    }

    async findAll(): Promise<Post[]> {
        return await this.postRepository.findAll<Post>({
            include: [{ model: User, attributes: { exclude: ['password'] } }],
        });
    }

    async findOne(id): Promise<Post> {
        return await this.postRepository.findOne({
            where: { id },
            include: [{ model: User, attributes: { exclude: ['password'] } }],
        });
    }

    async delete(id, userId) {
        return await this.postRepository.destroy({ where: { id, userId } });
    }

    async update(id, data, userId) {
        const [numberOfAffectedRows, [updatedPost]] = await this.postRepository.update({ ...data }, { where: { id, userId }, returning: true });

        return { numberOfAffectedRows, updatedPost };
    }
}
```

Ici, nous injectons notre repository Post pour communiquer avec notre base de données.

-   `create(post: PostDto, userId) :` Accepte l'objet post et l'ID de l'utilisateur qui crée le post. Il ajoute le post à la base de données et renvoie le Post nouvellement créé. Le `PostDto` est utilisé pour la validation.
-   `findAll() :` Récupère tous les posts de la base de données et inclut (chargement immédiat/eager load) l'utilisateur qui l'a créé tout en excluant le mot de passe de l'utilisateur.
-   `findOne(id) :` Trouve et renvoie le post avec l'ID spécifié. Il inclut également l'utilisateur créateur en excluant son mot de passe.
-   `delete(id, userId) :` Supprime le post de la base de données avec l'ID et le `userId`. Seul l'utilisateur qui a créé le post peut le supprimer. Cela renvoie le nombre de lignes affectées.
-   `update(id, data, userId) :` Met à jour un post existant où `id` est l'ID du post, `data` sont les données à mettre à jour, et `userId` est l'ID du créateur original. Cela renvoie le nombre de lignes mises à jour et l'objet nouvellement mis à jour.

### Méthodes du contrôleur Post

Copiez et collez ce qui suit à l'intérieur du fichier du contrôleur Post :

```
import { Controller, Get, Post, Put, Delete, Param, Body, NotFoundException, UseGuards, Request } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { PostsService } from './posts.service';
import { Post as PostEntity } from './post.entity';
import { PostDto } from './dto/post.dto';

@Controller('posts')
export class PostsController {
    constructor(private readonly postService: PostsService) { }

    @Get()
    async findAll() {
        // get all posts in the db
        return await this.postService.findAll();
    }

    @Get(':id')
    async findOne(@Param('id') id: number): Promise<PostEntity> {
        // find the post with this id
        const post = await this.postService.findOne(id);

        // if the post doesn't exit in the db, throw a 404 error
        if (!post) {
            throw new NotFoundException('This Post doesn\'t exist');
        }

        // if post exist, return the post
        return post;
    }

    @UseGuards(AuthGuard('jwt'))
    @Post()
    async create(@Body() post: PostDto, @Request() req): Promise<PostEntity> {
        // create a new post and return the newly created post
        return await this.postService.create(post, req.user.id);
    }

    @UseGuards(AuthGuard('jwt'))
    @Put(':id')
    async update(@Param('id') id: number, @Body() post: PostDto, @Request() req): Promise<PostEntity> {
        // get the number of row affected and the updated post
        const { numberOfAffectedRows, updatedPost } = await this.postService.update(id, post, req.user.id);

        // if the number of row affected is zero, 
        // it means the post doesn't exist in our db
        if (numberOfAffectedRows === 0) {
            throw new NotFoundException('This Post doesn\'t exist');
        }

        // return the updated post
        return updatedPost;
    }

    @UseGuards(AuthGuard('jwt'))
    @Delete(':id')
    async remove(@Param('id') id: number, @Request() req) {
        // delete the post with this id
        const deleted = await this.postService.delete(id, req.user.id);

        // if the number of row affected is zero, 
        // then the post doesn't exist in our db
        if (deleted === 0) {
            throw new NotFoundException('This Post doesn\'t exist');
        }

        // return success message
        return 'Successfully deleted';
    }
}
```

La majeure partie des fonctionnalités d'opération CRUD est effectuée dans notre `PostService`.

-   `findAll() :` Gère la requête `GET` vers le point de terminaison `api/v1/posts`. Elle renvoie tous les posts de notre base de données.
-   `findOne(@Param('id') id: number) :` Gère la requête `GET` vers le point de terminaison `api/v1/posts/1` pour obtenir un seul post, où 1 est l'ID du post. Elle lève une erreur 404 si elle ne trouve pas le post et renvoie l'objet post si elle le trouve.
-   `create(@Body() post: PostDto, @Request() req) :` Gère la requête `POST` vers le point de terminaison `api/v1/posts` pour créer un nouveau post.
-   `@UseGuards(AuthGuard('jwt'))` est utilisé pour protéger la route (souvenez-vous de notre stratégie JWT). Seuls les utilisateurs connectés peuvent créer un post.
-   `update(@Param('id') id: number, @Body() post: PostDto, @Request() req) :` Gère la requête `PUT` vers le point de terminaison `api/v1/posts` pour mettre à jour un post existant. C'est également une route protégée. Si le `numberOfAffectedRows` est égal à zéro, cela signifie qu'aucun post avec cet ID n'a été trouvé.
-   `remove(@Param('id') id: number, @Request() req) :` Gère la requête `DELETE` pour supprimer un post existant.

## Testons nos opérations CRUD...

### Créer un article

Connectez-vous et ajoutez votre token car la route de création de post est protégée.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_qXyUFopQW72cMaHa0uTVOw.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_oxqCFmCNaMH4I8FBR1TD-A.png) _Création d'un article._

### Lire un seul article

Cette route n'est pas protégée, elle peut donc être consultée sans token.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_CQzE4J82K9Tmc0OsclMyQw.png) _Récupération d'un seul article_

Lecture de tous les articles

Cette route n'est pas non plus protégée, elle est donc accessible sans token.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_7D47fSupbbgASbqbpX2jEA.png) _Récupération de tous les articles_

### Mettre à jour un seul article

Cette route est protégée, nous avons donc besoin d'un token et seul le créateur peut le mettre à jour.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1__yN5JvnyoisPNmRASfLnJw.png) _Mise à jour d'un seul article_

### Supprimer un article

Cette route est protégée, nous avons donc besoin d'un token et seul le créateur peut le supprimer.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1_qLmCLDKCvn_YOxeBGyx_3w.png) _Suppression d'un article_

# **Conclusion**

Nest.js vous offre une manière plus structurée de construire vos applications côté serveur avec Node.

Pour plus d'informations, consultez le [site officiel de NestJS ici][10].

Enfin, j'espère que cet article vous a été utile ! Le [lien vers le dépôt GitHub du projet final est ici][11].

Vous pouvez me contacter sur [LinkedIn][12] et [Twitter][13].

[1]: https://nodejs.org/
[2]: http://www.typescriptlang.org/
[3]: https://www.postman.com/
[4]: https://nodejs.org/
[5]: https://github.com/onwuvic/nest-blog-api
[6]: https://github.com/RobinBuschmann/sequelize-typescript#readme
[7]: https://github.com/jaredhanson/passport
[8]: https://docs.nestjs.com/exception-filters
[9]: https://github.com/typestack/class-validator
[10]: https://nestjs.com/
[11]: https://github.com/onwuvic/nest-blog-api
[12]: https://www.linkedin.com/in/victoronwuzor/
[13]: https://twitter.com/victoronwuzor