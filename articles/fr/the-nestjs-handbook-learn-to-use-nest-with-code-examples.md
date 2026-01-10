---
title: Le guide de NestJS – Apprenez à utiliser Nest avec des exemples de code
date: '2025-06-13T20:13:49.159Z'
author: German Cocca
authorURL: https://www.freecodecamp.org/news/author/GerCocca/
originalURL: https://freecodecamp.org/news/the-nestjs-handbook-learn-to-use-nest-with-code-examples
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1749830137752/799b050a-f884-4043-9db1-fe2bb860d297.png
tags:
- name: nestjs
  slug: nestjs
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_desc: NestJS is a progressive Node.js framework for building efficient, reliable,
  and scalable server-side applications. Combining the best ideas from OOP (Object-Oriented
  Programming), FP (Functional Programming), and FRP (Functional Reactive Programming)...
---


NestJS est un framework Node.js progressif pour la création d'applications côté serveur efficaces, fiables et évolutives (scalables). Combinant les meilleures idées de la POO (Programmation Orientée Objet), de la PF (Programmation Fonctionnelle) et de la PRF (Programmation Réactive Fonctionnelle), il vous offre une plateforme complète et structurée au-dessus d'Express (ou Fastify).

<!-- more -->

Si vous venez d'Angular, vous vous sentirez immédiatement à l'aise avec sa structure module/contrôleur/service et son puissant système d'injection de dépendances.

Dans cet article, nous aborderons à la fois la **théorie** – pourquoi NestJS existe, comment il est structuré et quand l'utiliser – et la **pratique**, avec des extraits de code concis démontrant comment initialiser un projet, définir des routes, injecter des dépendances, et plus encore. Commençons par comprendre ce qu'est NestJS et d'où il vient.

## Table des matières

1.  [Qu'est-ce que NestJS ?][1]
    
    -   [1.1 Histoire et philosophie][2]
2.  [Pourquoi choisir NestJS ?][3]
    
    -   [2.1 Avantages et cas d'utilisation][4]
        
    -   [2.2 Comparaison avec d'autres frameworks][5]
        
3.  [Prise en main][6]
    
    -   [3.1 Installation de la CLI][7]
        
    -   [3.2 Créer votre premier projet][8]
        
    -   [3.3 Aperçu de la structure du projet][9]
        
4.  [Les blocs de construction fondamentaux de NestJS][10]
    
    -   [4.1 Modules][11]
        
    -   [4.2 Contrôleurs][12]
        
    -   [4.3 Providers (Services)][13]
        
5.  [Injection de dépendances][14]
    
    -   [5.1 Comment fonctionne l'injection de dépendances dans NestJS][15]
        
    -   [5.2 Providers personnalisés et Factory Providers][16]
        
6.  [Routage et Middleware][17]
    
    -   [6.1 Définir des routes][18]
        
    -   [6.2 Appliquer des middlewares][19]
        
7.  [Cycle de vie des requêtes et Pipes][20]
    
    -   [7.1 Que sont les Pipes ?][21]
        
    -   [7.2 Pipes intégrés vs personnalisés][22]
        
8.  [Guards et Autorisation][23]
    
    -   [8.1 Implémenter des Guards][24]
        
    -   [8.2 Contrôle d'accès basé sur les rôles (RBAC)][25]
        
9.  [Filtres d'exception][26]
    
    -   [9.1 Gérer les erreurs avec élégance][27]
        
    -   [9.2 Créer des filtres personnalisés][28]
        
10.  [Intercepteurs et Journalisation (Logging)][29]
    
    -   [10.1 Transformer les réponses][30]
        
    -   [10.2 Journalisation et métriques de performance][31]
        
11.  [Intégration de bases de données][32]
    
    -   [11.1 TypeORM avec NestJS][33]
        
    -   [11.2 Mongoose (MongoDB)][34]
        
    -   [11.3 Prisma][35]
        
12.  [Gestion de la configuration][36]
    
    -   [12.1 Module @nestjs/config][37]
        
    -   [12.2 Variables d'environnement][38]
        
13.  [Authentification][39]
    
    -   [13.1 Stratégie JWT][40]
        
    -   [13.2 OAuth2 / Connexion via réseaux sociaux][41]
        
14.  [Conclusion et ressources complémentaires][42]
    
    -   [Résumé][43]
        
    -   [Documentation officielle et liens communautaires][44]
        

## 1\. Qu'est-ce que NestJS ?

NestJS est un framework pour construire des applications côté serveur en Node.js. Il est écrit en TypeScript (mais supporte également le JavaScript pur). À la base, il :

-   **Encapsule** une bibliothèque de serveur HTTP mature (Express ou Fastify)
    
-   **Standardise** l'architecture de l'application autour des modules, contrôleurs et providers
    
-   **Exploite** le système de types de TypeScript pour la sécurité à la compilation et des API claires
    
-   **Offre** un support intégré pour des éléments tels que la validation, la configuration et les tests
    

Plutôt que d'assembler des middlewares à la main, NestJS encourage une approche déclarative et par couches. Vous définissez des **modules** pour regrouper les fonctionnalités liées, des **contrôleurs** pour gérer les requêtes entrantes, et des **providers** (souvent appelés "services") pour votre logique métier. En coulisses, NestJS résout les dépendances via un conteneur IoC (Inversion of Control), vous permettant de vous concentrer sur l'écriture de classes propres et réutilisables.

Pour démarrer un projet, exécutez les commandes suivantes :

```
# Installer la CLI Nest globalement
npm install -g @nestjs/cli

# Créer un nouveau projet appelé 'my-app'
nest new my-app

cd my-app
npm run start:dev
```

Une fois lancé, vous disposez d'un serveur HTTP prêt à l'emploi avec rechargement à chaud (hot reloading), typage strict et une structure de dossiers cohérente.

### 1.1 Histoire et philosophie

NestJS est apparu pour la première fois en 2017, créé par Kamil Myśliwiec. Son objectif était d'apporter les modèles architecturaux d'Angular au monde du backend, en offrant :

1.  **Cohérence :** Une manière unique et structurée d'organiser les applications.
    
2.  **Évolutivité :** Des frontières claires (modules) facilitent la croissance des équipes et des bases de code.
    
3.  **Testabilité :** Support intégré pour Jest et une séparation claire des préoccupations.
    
4.  **Extensibilité :** Un système de modules pluggables facilite l'intégration d'ORMs, WebSockets, GraphQL, microservices, et plus encore.
    

Sous le capot, NestJS adopte ces principes :

-   **Modularité :** Tout réside dans un module (`AppModule`, `UsersModule`, etc.), qui peut importer d'autres modules ou exporter des providers.
    
-   **Injection de dépendances :** Les services peuvent être injectés dans les contrôleurs (et même dans d'autres services), ce qui favorise un couplage faible.
    
-   **Décorateurs et métadonnées :** Avec les décorateurs TypeScript (`@Module()`, `@Controller()`, `@Injectable()`), NestJS lit les métadonnées au moment de l'exécution pour tout lier ensemble.
    

Voici un petit exemple montrant l'interaction de ces éléments :

```
// users.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class UsersService {
  private users = [{ id: 1, name: 'Alice' }];
  findAll() {
    return this.users;
  }
}

// users.controller.ts
import { Controller, Get } from '@nestjs/common';
import { UsersService } from './users.service';

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get()
  getUsers() {
    return this.usersService.findAll();
  }
}

// users.module.ts
import { Module } from '@nestjs/common';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';

@Module({
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}
```

-   Le décorateur `@Module` regroupe le contrôleur et le service.
    
-   Le contrôleur injecte le service via son constructeur.
    
-   Une simple route `GET /users` renvoie un tableau d'objets utilisateurs.
    

Une fois ces bases posées, nous explorerons dans la section suivante **pourquoi choisir NestJS**, en le comparant à d'autres frameworks Node populaires et en soulignant les cas d'utilisation courants.

## 2\. Pourquoi choisir NestJS ?

NestJS n'est pas simplement un framework Node.js de plus – il apporte une approche structurée de niveau entreprise pour construire des services backend. Dans cette section, nous aborderons les avantages et les cas d'utilisation réels, puis nous comparerons NestJS à d'autres frameworks Node populaires.

### 2.1 Avantages et cas d'utilisation

1.  **Modèles architecturaux solides**
    
    -   **Modularité :** Vous divisez votre application en modules ciblés (`AuthModule`, `ProductsModule`, etc.), chacun responsable d'une partie des fonctionnalités.
        
    -   **Séparation des préoccupations :** Les contrôleurs gèrent le HTTP, les services encapsulent la logique métier, les modules lient le tout.
        
    -   **Évolutivité :** La croissance des équipes se calque naturellement sur les modules — les nouvelles fonctionnalités touchent rarement le code existant.
        
2.  **Injection de dépendances (DI) intégrée**
    
    -   La DI rend les tests et le remplacement des implémentations triviaux.
        
    -   Vous pouvez facilement mocker un service dans un test unitaire :
        

```
    // products.controller.spec.ts
    import { Test, TestingModule } from '@nestjs/testing';
    import { ProductsController } from './products.controller';
    import { ProductsService } from './products.service';

    describe('ProductsController', () => {
      let controller: ProductsController;
      const mockService = { findAll: () => ['apple', 'banana'] };

      beforeEach(async () => {
        const module: TestingModule = await Test.createTestingModule({
          controllers: [ProductsController],
          providers: [
            { provide: ProductsService, useValue: mockService },
          ],
        }).compile();

        controller = module.get<ProductsController>(ProductsController);
      });

      it('returns a list of products', () => {
        expect(controller.getAll()).toEqual(['apple', 'banana']);
      });
    });
```

3.  **Priorité au TypeScript**
    
    -   Sécurité de typage complète à la compilation.
        
    -   Exploitez les interfaces et les décorateurs (`@Body()`, `@Param()`) pour valider et transformer les données.
        
4.  **Écosystème riche et extensibilité**
    
    -   Intégrations officielles pour WebSockets, GraphQL, microservices (RabbitMQ, Kafka), et plus encore.
        
    -   Des centaines de modules communautaires (par exemple `@nestjs/swagger` pour la documentation OpenAPI).
        
5.  **Outillage de production**
    
    -   La CLI génère du code de base (`nest g module`, `nest g service`).
        
    -   Support du hot-reload en développement (`npm run start:dev`).
        
    -   Configuration de test intégrée avec Jest.
        

**Cas d'utilisation réels :**

-   **API d'entreprise** avec des frontières de modules strictes et du RBAC.
    
-   **Architectures de microservices**, où chaque service est une application NestJS autonome.
    
-   **Applications en temps réel** (chat, tableaux de bord en direct) utilisant les passerelles WebSocket de Nest.
    
-   **Backends GraphQL** avec des schémas "code-first".
    
-   **Systèmes pilotés par événements** se connectant à des courtiers de messages (message brokers).
    

### 2.2 Comparaison avec d'autres frameworks

| Fonctionnalité | Express | Koa | NestJS |
| --- | --- | --- | --- |
| **Architecture** | Minimale, non restrictive | Minimale, basée sur les middlewares | Structurée (modules/contrôleurs/services) |
| **Injection de dépendances** | Liaison manuelle | Liaison manuelle | Intégrée, reflect-metadata |
| **Support TypeScript** | Via DefinitelyTyped | Via DefinitelyTyped | Natif, décorateurs |
| **Outils CLI** | Aucun (tiers) | Aucun | `@nestjs/cli` génère du code |
| **Tests** | Configuré par l'utilisateur | Configuré par l'utilisateur | Jest + DI facilite le mocking |
| **Écosystème** | Bibliothèques de middlewares | Bibliothèques de middlewares | Modules officiels microservices, GraphQL, Swagger |
| **Courbe d'apprentissage** | Faible | Faible | Moyenne (apprentissage des idiomes Nest) |

-   **Express** est excellent si vous voulez un minimum de couches et un contrôle total, mais vous finirez par tout faire à la main (DI, validation, structure de dossiers).
    
-   **Koa** offre une approche middleware plus moderne, mais vous laisse toujours les décisions architecturales.
    
-   **NestJS** fournit la solution complète : structure, DI, validation, tests et intégrations officielles, ce qui est idéal si vous privilégiez la **cohérence**, la **sécurité de typage** et les **bonnes pratiques prêtes à l'emploi**.
    

**Quand choisir NestJS :**

NestJS est idéal pour divers cas d'utilisation. Il est particulièrement efficace si vous construisez une API à grande échelle ou une suite de microservices, si vous voulez une architecture solide dès le premier jour, et si vous préférez TypeScript et la DI pour garder le code testable et maintenable.

Avec ces avantages en tête, vous constaterez que NestJS peut accélérer considérablement le développement, en particulier sur les projets nécessitant une structure robuste et des limites claires.

Dans la section suivante, nous verrons comment démarrer : installation de la CLI, création d'un projet et exploration de la structure des dossiers générée.

## 3\. Prise en main

Passons aux bases : installation de la CLI, création d'un nouveau projet et exploration de la structure de dossiers par défaut.

### 3.1 Installation de la CLI

Nest est livré avec un outil de ligne de commande officiel qui vous aide à générer des modules, des contrôleurs, des services, et plus encore. Sous le capot, il utilise des templates Yeoman pour maintenir la cohérence.

```
# Installer la CLI globalement (nécessite npm ≥ 6)
npm install -g @nestjs/cli
```

Une fois installé, vous pouvez exécuter `nest --help` pour voir les commandes disponibles :

```
nest --help
Usage: nest <command> [options]

Commands:
  new <name>       Scaffold a new project
  generate|g <schematic> [options]  Generate artifacts (modules, controllers, ...)
  build            Build project with webpack
  ...

Options:
  -v, --version    Show version number
  -h, --help       Show help
```

### 3.2 Créer votre premier projet

La création d'une nouvelle application se fait en une seule commande. La CLI vous demandera si vous souhaitez utiliser npm ou yarn, et si vous voulez activer les paramètres TypeScript stricts.

```
# Créer une nouvelle application Nest dans le dossier "my-nest-app"
nest new my-nest-app
```

Après avoir répondu aux invites, vous aurez :

```
cd my-nest-app
npm run start:dev
```

Cela lance un serveur de développement sur [`http://localhost:3000`][45] avec rechargement automatique lors des modifications de fichiers.

### 3.3 Aperçu de la structure du projet

Par défaut, vous verrez quelque chose comme :

```
my-nest-app/
├── src/
│   ├── app.controller.ts      # exemple de contrôleur
│   ├── app.controller.spec.ts # test unitaire pour le contrôleur
│   ├── app.module.ts          # module racine de l'application
│   ├── app.service.ts         # exemple de provider
│   └── main.ts                # point d'entrée (bootstrap de Nest)
├── test/                      # tests de bout en bout (e2e)
├── node_modules/
├── package.json
├── tsconfig.json
└── nest-cli.json             # configuration de la CLI
```

-   **src/main.ts**  
    Le script de démarrage ("bootstrap"). Il crée une instance d'application Nest et commence à écouter sur un port :
    
    ```
      import { NestFactory } from '@nestjs/core';
      import { AppModule } from './app.module';
    
      async function bootstrap() {
        const app = await NestFactory.create(AppModule);
        await app.listen(3000);
        console.log(`🚀 Application is running on: ${await app.getUrl()}`);
      }
      bootstrap();
    ```
    
-   **src/app.module.ts**  
    Le module racine. Il lie les contrôleurs et les providers :
    
    ```
      import { Module } from '@nestjs/common';
      import { AppController } from './app.controller';
      import { AppService } from './app.service';
    
      @Module({
        imports: [],                 // autres modules à importer
        controllers: [AppController],
        providers: [AppService],
      })
      export class AppModule {}
    ```
    
-   **src/app.controller.ts / app.service.ts**  
    Un exemple simple qui montre l'injection de dépendances en action :
    
    ```
      // app.controller.ts
      import { Controller, Get } from '@nestjs/common';
      import { AppService } from './app.service';
    
      @Controller()
      export class AppController {
        constructor(private readonly appService: AppService) {}
    
        @Get()
        getHello(): string {
          return this.appService.getHello();
        }
      }
    
      // app.service.ts
      import { Injectable } from '@nestjs/common';
    
      @Injectable()
      export class AppService {
        getHello(): string {
          return 'Hello, NestJS!';
        }
      }
    ```
    

Avec cette base en place, vous disposez d'une application NestJS minimale mais entièrement fonctionnelle. À partir de là, vous pouvez générer de nouveaux modules, contrôleurs et services :

```
# Générer un nouveau module, contrôleur et service pour "tasks"
nest g module tasks
nest g controller tasks
nest g service tasks
```

Chaque commande déposera un nouveau fichier `.ts` dans le dossier approprié et mettra à jour les métadonnées de votre module. Dans la section suivante, nous approfondirons les blocs de construction de Nest tels que les modules, les contrôleurs et les providers.

## 4\. Les blocs de construction fondamentaux de NestJS

Au cœur de chaque application NestJS se trouvent trois piliers : les **Modules**, les **Contrôleurs** et les **Providers** (souvent appelés Services). Voyons ce que chacun fait et comment ils s'assemblent en théorie et en pratique.

### 4.1 Modules

Un **Module** est une frontière logique – un conteneur qui regroupe des composants liés (contrôleurs, providers et même d'autres modules). Chaque application NestJS possède au moins un module racine (généralement `AppModule`), et vous créez des modules de fonctionnalités (`UsersModule`, `AuthModule`, etc.) pour organiser le code par domaine.

#### Décorateur @Module()

-   `imports` : autres modules à utiliser
    
-   `controllers` : contrôleurs qui gèrent les requêtes entrantes
    
-   `providers` : services ou valeurs disponibles via DI
    
-   `exports` : providers qui doivent être visibles pour les modules importateurs
    

**Voici un exemple :**

```
// cats.module.ts
import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

@Module({
  imports: [],            // ex: TypeOrmModule.forFeature([Cat])
  controllers: [CatsController],
  providers: [CatsService],
  exports: [CatsService], // rend CatsService disponible pour d'autres modules
})
export class CatsModule {}
```

Puis dans votre module racine :

```
// app.module.ts
import { Module } from '@nestjs/common';
import { CatsModule } from './cats/cats.module';

@Module({
  imports: [CatsModule],
})
export class AppModule {}
```

Désormais, tout ce qui injecte `CatsService` se résoudra vers celui défini dans `CatsModule`.

### 4.2 Contrôleurs

Un **Contrôleur** mappe les requêtes HTTP entrantes aux méthodes de gestion (handlers). Il est responsable de l'extraction des données de la requête (paramètres de requête, corps, en-têtes) et du renvoi d'une réponse. Les contrôleurs doivent rester légers – en déléguant la logique métier aux providers.

-   **@Controller(path?)** : Définit un préfixe de route
    
-   **@Get, @Post, @Put, @Delete, etc.** : Définissent des routes au niveau des méthodes
    
-   **@Param(), @Query(), @Body(), @Headers(), @Req(), @Res()** : Décorateurs pour extraire les détails de la requête
    

**Voici un exemple :**

```
// cats.controller.ts
import { Controller, Get, Post, Body, Param } from '@nestjs/common';
import { CatsService } from './cats.service';
import { CreateCatDto } from './dto/create-cat.dto';

@Controller('cats')                  // préfixe : /cats
export class CatsController {
  constructor(private readonly catsService: CatsService) {}

  @Get()
  findAll() {
    return this.catsService.findAll();  // GET /cats
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.catsService.findOne(+id);  // GET /cats/1
  }

  @Post()
  create(@Body() createCatDto: CreateCatDto) {
    return this.catsService.create(createCatDto);  // POST /cats
  }
}
```

```
// dto/create-cat.dto.ts
export class CreateCatDto {
  readonly name: string;
  readonly age: number;
  readonly breed?: string;
}
```

### 4.3 Providers (Services)

Les **Providers** sont des classes annotées avec `@Injectable()` qui contiennent votre logique métier ou l'accès aux données. Tout ce que vous voulez injecter ailleurs doit être un provider. Vous pouvez fournir des valeurs simples, des fonctions d'usine (factories) ou des classes.

-   **@Injectable()** : Marque une classe comme disponible pour la DI
    
-   **Scope** : Par défaut, c'est un singleton, mais vous pouvez changer pour un scope de requête (request) ou transitoire (transient)
    
-   **Providers personnalisés** : Utilisez `useClass`, `useValue`, `useFactory` ou `useExisting` pour plus de contrôle
    

**Voici un exemple :**

```
// cats.service.ts
import { Injectable, NotFoundException } from '@nestjs/common';
import { CreateCatDto } from './dto/create-cat.dto';

@Injectable()
export class CatsService {
  private cats = [];

  create(dto: CreateCatDto) {
    const newCat = { id: Date.now(), ...dto };
    this.cats.push(newCat);
    return newCat;
  }

  findAll() {
    return this.cats;
  }

  findOne(id: number) {
    const cat = this.cats.find(c => c.id === id);
    if (!cat) {
      throw new NotFoundException(`Cat #${id} not found`);
    }
    return cat;
  }
}
```

**Injecter une valeur personnalisée :**

```
// logger.provider.ts
export const LOGGER = {
  provide: 'LOGGER',
  useValue: console,
};

// app.module.ts
import { Module } from '@nestjs/common';
import { LOGGER } from './logger.provider';

@Module({
  providers: [LOGGER],
  exports: [LOGGER],
})
export class AppModule {}
```

```
// some.service.ts
import { Inject, Injectable } from '@nestjs/common';

@Injectable()
export class SomeService {
  constructor(@Inject('LOGGER') private readonly logger: Console) {}

  logMessage(msg: string) {
    this.logger.log(`Custom log: ${msg}`);
  }
}
```

Avec les modules reliant les contrôleurs et les providers, NestJS vous offre une base évolutive et testable. Dans la section suivante, nous explorerons l'**Injection de dépendances** en profondeur – comment elle fonctionne sous le capot et comment créer des providers personnalisés et des injections basées sur des factories.

## 5\. Injection de dépendances

Le système d'injection de dépendances (DI) intégré de Nest est au cœur de la manière dont les composants (contrôleurs, services, etc.) communiquent entre eux de manière faiblement couplée et testable.

### 5.1 Comment fonctionne l'injection de dépendances dans NestJS

Lorsque votre application démarre, Nest construit un **conteneur IoC basé sur les modules**. Chaque provider `@Injectable()` est enregistré dans le conteneur sous un jeton (token) (par défaut, sa classe). Lorsqu'une classe déclare une dépendance dans son constructeur, Nest recherche ce jeton et injecte l'instance correspondante.

-   **Scope Singleton** : Une instance par application (par défaut)
    
-   **Scope Request** : Nouvelle instance par requête entrante
    
-   **Scope Transient** : Nouvelle instance à chaque injection
    

**Voici un exemple :**

```
// cats.service.ts
@Injectable()
export class CatsService {
  // ...
}

// cats.controller.ts
@Controller('cats')
export class CatsController {
  constructor(private readonly catsService: CatsService) {}
  // Nest voit CatsService dans le constructeur,
  // trouve son instance singleton et l'injecte.
}
```

_En coulisses_, Nest collecte les métadonnées des décorateurs (`@Injectable()`, `@Controller()`) et construit un graphe de providers. Lorsque vous appelez `NestFactory.create(AppModule)`, il résout ce graphe et lie tout ensemble.

### 5.2 Providers personnalisés et Factory Providers

Parfois, vous devez injecter des valeurs qui ne sont pas des classes (API, constantes) ou exécuter une logique au moment de l'enregistrement. Nest vous permet de définir des **providers personnalisés** en utilisant la syntaxe `provide`.

#### `useValue`

Injecter une valeur simple ou un objet :

```
// config.constant.ts
export const APP_NAME = {
  provide: 'APP_NAME',
  useValue: 'MyAwesomeApp',
};

// app.module.ts
@Module({
  providers: [APP_NAME],
  exports: ['APP_NAME'],
})
export class AppModule {}

// some.service.ts
@Injectable()
export class SomeService {
  constructor(@Inject('APP_NAME') private readonly name: string) {}

  whoAmI() {
    return `Running in ${this.name}`;
  }
}
```

#### `useClass`

Changer facilement d'implémentation (utile pour les tests ou les feature flags) :

```
// logger.interface.ts
export interface Logger {
  log(msg: string): void;
}

// console-logger.ts
@Injectable()
export class ConsoleLogger implements Logger {
  log(msg: string) { console.log(msg); }
}

// file-logger.ts
@Injectable()
export class FileLogger implements Logger {
  log(msg: string) { /* écrire dans un fichier */ }
}

// app.module.ts
@Module({
  providers: [
    { provide: 'Logger', useClass: FileLogger }, 
  ],
})
export class AppModule {}

// any.service.ts
@Injectable()
export class AnyService {
  constructor(@Inject('Logger') private readonly logger: Logger) {}
}
```

#### `useFactory`

Exécuter une logique d'usine arbitraire (par exemple, initialisation asynchrone, configuration dynamique) :

```
// database.provider.ts
export const DATABASE = {
  provide: 'DATABASE',
  useFactory: async (configService: ConfigService) => {
    const opts = configService.getDbOptions();
    const connection = await createConnection(opts);
    return connection;
  },
  inject: [ConfigService],
};

// app.module.ts
@Module({
  imports: [ConfigModule],
  providers: [DATABASE],
  exports: ['DATABASE'],
})
export class AppModule {}

// users.service.ts
@Injectable()
export class UsersService {
  constructor(@Inject('DATABASE') private readonly db: Connection) {}
}
```

Avec les providers personnalisés et le pattern factory, vous pouvez intégrer des bibliothèques externes, basculer entre les implémentations ou effectuer une configuration asynchrone – tout en conservant la structure claire et testable fournie par NestJS.

Dans la section suivante, nous examinerons le **Routage et le Middleware**, en montrant comment définir des gestionnaires de routes, appliquer des middlewares globaux ou par route, et étendre votre pipeline HTTP.

## 6\. Routage et Middleware

Le routage dans NestJS est construit sur vos contrôleurs et décorateurs, tandis que le middleware vous permet d'intervenir dans le pipeline requête/réponse pour des préoccupations transversales telles que la journalisation, les vérifications d'authentification ou le CORS.

### 6.1 Définir des routes

D'abord, un peu de théorie :

-   **@Controller(path?)** définit un préfixe d'URL pour toutes les routes de cette classe.
    
-   **@Get, @Post, @Put, @Delete, etc.** définissent les gestionnaires de méthodes HTTP.
    
-   **@Param(), @Query(), @Body(), @Headers(), @Req(), @Res()** extraient des parties de la requête entrante.
    

Vous pouvez combiner les décorateurs de route et les décorateurs de paramètres pour construire des points de terminaison (endpoints) expressifs et typés.

**Voici un exemple :**

```
// products.controller.ts
import { Controller, Get, Post, Param, Query, Body } from '@nestjs/common';
import { ProductsService } from './products.service';
import { CreateProductDto } from './dto/create-product.dto';

@Controller('products')                // toutes les routes ici commencent par /products
export class ProductsController {
  constructor(private readonly productsService: ProductsService) {}

  @Get()                              // GET /products
  findAll(
    @Query('limit') limit = '10',     // query optionnelle ?limit=20
  ) {
    return this.productsService.findAll(+limit);
  }

  @Get(':id')                         // GET /products/123
  findOne(@Param('id') id: string) {
    return this.productsService.findOne(+id);
  }

  @Post()                             // POST /products
  create(@Body() dto: CreateProductDto) {
    return this.productsService.create(dto);
  }
}
```

Vous pouvez également imbriquer des contrôleurs en important un module de fonctionnalité, et utiliser **@Patch**, **@Put**, **@Delete**, **@Head**, etc. pour une couverture RESTful complète.

### 6.2 Appliquer des middlewares

Les **Middlewares** sont des fonctions qui s'exécutent _avant_ que vos routes ne traitent une requête. Ils sont utiles pour la journalisation, l'analyse du corps de la requête (bien que Nest en fournisse par défaut), les guards d'authentification à bas niveau, la limitation de débit (rate limiting), etc.

Vous pouvez les implémenter soit sous forme de middleware fonctionnel, soit sous forme de classe implémentant `NestMiddleware`.

**Voici un exemple (Middleware fonctionnel) :**

```
// logger.middleware.ts
import { Request, Response, NextFunction } from 'express';

export function logger(req: Request, res: Response, next: NextFunction) {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
}

// app.module.ts
import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { logger } from './logger.middleware';
import { ProductsModule } from './products/products.module';

@Module({
  imports: [ProductsModule],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(logger)                 // appliquer logger
      .forRoutes('products');        // uniquement pour les routes /products
  }
}
```

**Et voici un autre exemple (Middleware basé sur une classe) :**

```
// auth.middleware.ts
import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';

@Injectable()
export class AuthMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    if (!req.headers.authorization) {
      return res.status(401).send('Unauthorized');
    }
    // valider le token...
    next();
  }
}

// security.module.ts
import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { AuthMiddleware } from './auth.middleware';
import { UsersController } from './users.controller';

@Module({
  controllers: [UsersController],
})
export class SecurityModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(AuthMiddleware)
      .forRoutes(UsersController);    // appliquer à toutes les routes de UsersController
  }
}
```

**Astuce :** Un middleware global peut être appliqué dans votre fichier `main.ts` avant l'appel `app.listen()` via `app.use(logger)` si vous le souhaitez sur _chaque_ requête.

Une fois le routage et le middleware configurés, vous avez un contrôle total sur la façon dont les requêtes circulent dans votre application. Prochaine étape, nous plongerons dans le **Cycle de vie des requêtes et les Pipes**, en explorant comment les transformations de données et les validations se produisent lors de chaque requête.

## 7\. Cycle de vie des requêtes et Pipes

NestJS traite chaque requête entrante à travers un "cycle de vie" d'étapes défini – routage vers le bon gestionnaire, application des **pipes**, **guards**, **intercepteurs**, et enfin invocation de votre méthode de contrôleur. Les **Pipes** se situent entre la requête entrante et votre gestionnaire, transformant ou validant les données avant qu'elles n'atteignent votre logique métier.

### 7.1 Que sont les Pipes ?

Un **Pipe** est une classe annotée avec `@Injectable()` qui implémente l'interface `PipeTransform`. Il possède une seule méthode :

```
transform(value: any, metadata: ArgumentMetadata): any
```

-   **Transformation** : Convertir les données d'entrée (par exemple, une chaîne `"123"`) vers le type souhaité (`number` `123`).
    
-   **Validation** : Vérifier que les données entrantes respectent certaines règles et lever une exception (généralement une `BadRequestException`) si ce n'est pas le cas.
    

Par défaut, les pipes s'exécutent **après** les middlewares et **avant** les guards/intercepteurs, pour chaque paramètre décoré (`@Body()`, `@Param()`, etc.).

**Voici comment cela fonctionne :**  
Nest est livré avec un pipe de validation global très pratique qui s'intègre à class-validator :

```
// main.ts
import { ValidationPipe } from '@nestjs/common';
import { NestFactory }    from '@nestjs/core';
import { AppModule }      from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // Valider automatiquement et supprimer les propriétés inconnues
  app.useGlobalPipes(new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true }));
  await app.listen(3000);
}
bootstrap();
```

Une fois en place, tout DTO annoté avec des décorateurs de validation sera vérifié avant l'exécution de votre gestionnaire :

```
// dto/create-user.dto.ts
import { IsEmail, IsString, MinLength } from 'class-validator';

export class CreateUserDto {
  @IsEmail()           // doit être un email valide
  email: string;

  @IsString()          // doit être une chaîne
  @MinLength(8)        // au moins 8 caractères
  password: string;
}

// users.controller.ts
@Post()
createUser(@Body() dto: CreateUserDto) {
  // Si body.email n'est pas un email, ou si le mot de passe est trop court,
  // Nest lève une erreur 400 Bad Request avec les détails.
  return this.usersService.create(dto);
}
```

### 7.2 Pipes intégrés vs personnalisés

#### Pipes intégrés

Nest fournit plusieurs pipes prêts à l'emploi :

-   **ValidationPipe** : S'intègre à `class-validator` pour la validation des DTO (montré ci-dessus).
    
-   **ParseIntPipe** : Convertit un paramètre de route en `number` ou lève une `BadRequestException`.
    
-   **ParseBoolPipe**, **ParseUUIDPipe**, **ParseFloatPipe**, etc.
    

```
@Get(':id')
getById(@Param('id', ParseIntPipe) id: number) {
  // id est garanti d'être un nombre ici
  return this.itemsService.findOne(id);
}
```

#### Pipes personnalisés

Vous pouvez écrire les vôtres pour gérer n'importe quelle logique de transformation ou de validation :

```
import { PipeTransform, Injectable, BadRequestException } from '@nestjs/common';

@Injectable()
export class ParsePositiveIntPipe implements PipeTransform<string, number> {
  transform(value: string): number {
    const val = parseInt(value, 10);
    if (isNaN(val) || val <= 0) {
      throw new BadRequestException(`"${value}" is not a positive integer`);
    }
    return val;
  }
}
```

Utilisez-le comme un pipe intégré :

```
@Get('order/:orderId')
getOrder(
  @Param('orderId', ParsePositiveIntPipe) orderId: number
) {
  // orderId est un entier positif validé
  return this.ordersService.findById(orderId);
}
```

Avec les pipes, vous vous assurez que chaque donnée entrant dans vos gestionnaires est correctement typée et valide, gardant votre logique métier propre et ciblée. Dans la section suivante, nous explorerons les **Guards et l'Autorisation** pour contrôler l'accès à vos points de terminaison.

## 8\. Guards et Autorisation

Les Guards interviennent dans le cycle de vie de la requête **après** les pipes et **avant** les intercepteurs/contrôleurs. Ils déterminent si une requête donnée doit être autorisée à se poursuivre en fonction d'une logique personnalisée. C'est idéal pour l'authentification, les vérifications de rôles ou les feature flags.

### 8.1 Implémenter des Guards

Un **Guard** est une classe qui implémente l'interface `CanActivate`, avec une seule méthode :

```
canActivate(context: ExecutionContext): boolean | Promise<boolean> | Observable<boolean>;
```

-   **ExecutionContext** vous donne accès à la requête/réponse sous-jacente et aux métadonnées de la route.
    
-   Si `canActivate` renvoie `true`, la requête continue. Renvoyer `false` ou lever une exception (par exemple, `UnauthorizedException`) la bloque.
    

Vous enregistrez les guards soit **globalement**, au niveau du **contrôleur**, ou sur des **routes individuelles** avec le décorateur `@UseGuards()`.

**Voici comment fonctionnent les guards :**

1.  **Création d'un guard d'authentification simple :**

```
// auth.guard.ts
import { Injectable, CanActivate, ExecutionContext, UnauthorizedException } from '@nestjs/common';

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(context: ExecutionContext): boolean {
    const req = context.switchToHttp().getRequest();
    const authHeader = req.headers.authorization;
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      throw new UnauthorizedException('Missing or invalid authorization header');
    }
    // Vérification basique du token (remplacez par une vraie validation)
    const token = authHeader.split(' ')[1];
    if (token !== 'valid-token') {
      throw new UnauthorizedException('Invalid token');
    }
    // Attacher les infos utilisateur si nécessaire :
    req.user = { id: 1, name: 'Alice' };
    return true;
  }
}
```

2.  **Appliquer le guard**

-   **Globalement** (dans `main.ts`) :
    
    ```
      import { NestFactory } from '@nestjs/core';
      import { AppModule } from './app.module';
      import { AuthGuard } from './auth.guard';
    
      async function bootstrap() {
        const app = await NestFactory.create(AppModule);
        // chaque requête entrante passe par AuthGuard
        app.useGlobalGuards(new AuthGuard());
        await app.listen(3000);
      }
      bootstrap();
    ```
    
-   **Au niveau du contrôleur** :
    
    ```
      import { Controller, Get, UseGuards } from '@nestjs/common';
      import { AuthGuard } from './auth.guard';
    
      @Controller('profile')
      @UseGuards(AuthGuard)       // s'applique à toutes les routes de ce contrôleur
      export class ProfileController {
        @Get()
        getProfile(@Req() req) {
          return req.user;
        }
      }
    ```
    
-   **Au niveau de la route** :
    
    ```
      @Get('admin')
      @UseGuards(AdminGuard, AuthGuard)  // chaîner plusieurs guards
      getAdminData() { /* ... */ }
    ```
    

### 8.2 Contrôle d'accès basé sur les rôles (RBAC)

Au-delà de la simple authentification, vous avez souvent besoin d'**autorisation** – s'assurer qu'un utilisateur possède le bon rôle ou la bonne permission. Vous pouvez construire un guard qui lit les métadonnées (par exemple, les rôles requis) et vérifie les droits de l'utilisateur.

**Voici comment cela fonctionne :**

1.  **Définir un décorateur de rôles :**

```
// roles.decorator.ts
import { SetMetadata } from '@nestjs/common';
export const Roles = (...roles: string[]) => SetMetadata('roles', roles);
```

2.  **Créer un guard de rôles :**

```
// roles.guard.ts
import { Injectable, CanActivate, ExecutionContext, ForbiddenException } from '@nestjs/common';
import { Reflector } from '@nestjs/core';

@Injectable()
export class RolesGuard implements CanActivate {
  constructor(private reflector: Reflector) {}

  canActivate(context: ExecutionContext): boolean {
    const requiredRoles = this.reflector.get<string[]>('roles', context.getHandler());
    if (!requiredRoles) {
      return true; // pas de métadonnées de rôles => route ouverte
    }
    const { user } = context.switchToHttp().getRequest();
    const hasRole = requiredRoles.some(role => user.roles?.includes(role));
    if (!hasRole) {
      throw new ForbiddenException('You do not have permission (roles)');
    }
    return true;
  }
}
```

3.  **Appliquer les métadonnées de rôles et le guard :**

```
@Controller('projects')
@UseGuards(AuthGuard, RolesGuard)
export class ProjectsController {
  @Get()
  @Roles('user', 'admin')         // la route nécessite soit 'user' soit 'admin'
  findAll() { /* ... */ }

  @Post()
  @Roles('admin')                 // seul 'admin' peut créer
  create() { /* ... */ }
}
```

Avec cette configuration :

-   `AuthGuard` s'assure que la requête est authentifiée et remplit `req.user`.
    
-   `RolesGuard` lit les métadonnées `@Roles()` pour appliquer l'accès basé sur les rôles.
    

Les guards vous offrent un moyen puissant et déclaratif d'appliquer des politiques de sécurité et d'autorisation. Dans la section suivante, nous aborderons les **Filtres d'exception** – comment intercepter et formater les erreurs de manière centralisée, gardant vos contrôleurs propres.

## 9\. Filtres d'exception

Les filtres d'exception vous permettent de centraliser la gestion des erreurs, en transformant les exceptions levées en réponses HTTP cohérentes ou dans d'autres formats. Vous pouvez compter sur le comportement intégré de Nest pour de nombreux cas, mais les filtres personnalisés vous donnent le contrôle sur la journalisation, la forme de la réponse ou la gestion des erreurs non HTTP.

### 9.1 Gérer les erreurs avec élégance

Par défaut, si un contrôleur ou un service lève une `HttpException` (ou l'une des exceptions intégrées de Nest comme `NotFoundException`, `BadRequestException`, etc.), Nest l'intercepte et envoie une réponse HTTP appropriée avec un code d'état et un corps JSON contenant `statusCode`, `message` et `error`.

Si une erreur inattendue (par exemple, une erreur d'exécution) survient, Nest utilise son filtre d'exception par défaut pour renvoyer une erreur 500 Internal Server Error avec un message générique.

Les contrôleurs/services doivent lever des exceptions plutôt que de renvoyer manuellement des codes d'erreur, afin que le framework puisse formater le tout de manière cohérente.

**Voici comment cela fonctionne :**

```
// users.service.ts
import { Injectable, NotFoundException } from '@nestjs/common';

@Injectable()
export class UsersService {
  private users = [{ id: 1, name: 'Alice' }];

  findOne(id: number) {
    const user = this.users.find(u => u.id === id);
    if (!user) {
      // produit un 404 avec le JSON { statusCode: 404, message: 'User #2 not found', error: 'Not Found' }
      throw new NotFoundException(`User #${id} not found`);
    }
    return user;
  }
}
```

```
// users.controller.ts
import { Controller, Get, Param, ParseIntPipe } from '@nestjs/common';

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  @Get(':id')
  getUser(@Param('id', ParseIntPipe) id: number) {
    return this.usersService.findOne(id);
  }
}
```

Si `findOne` lève une exception, le filtre par défaut de Nest envoie une erreur JSON structurée. Pour les erreurs inattendues (comme un `Error` lancé), Nest l'enveloppe dans une réponse 500.

### 9.2 Créer des filtres personnalisés

Vous pouvez implémenter l'interface `ExceptionFilter` ou étendre `BaseExceptionFilter`. Utilisez simplement le décorateur `@Catch()` pour cibler des types d'exceptions spécifiques (ou laissez vide pour tout intercepter).

Dans `catch(exception, host)`, vous pouvez extraire le contexte (requête/réponse HTTP) et façonner votre réponse (par exemple, ajouter des métadonnées, des champs personnalisés ou une enveloppe uniforme). Vous pouvez également journaliser les exceptions ou les signaler à des systèmes externes ici.

Vous pouvez appliquer des filtres **globalement**, à un contrôleur ou à une route individuelle.

**Voici comment cela fonctionne :**

1.  **Filtre de journalisation simple**  
    Intercepter toutes les exceptions, journaliser les détails, puis déléguer au comportement par défaut :
    
    ```
     // logging-exception.filter.ts
     import {
       ExceptionFilter,
       Catch,
       ArgumentsHost,
       HttpException,
       HttpStatus,
       Logger,
     } from '@nestjs/common';
     import { BaseExceptionFilter } from '@nestjs/core';
    
     @Catch() // pas d'arguments = intercepte chaque exception
     export class LoggingExceptionFilter extends BaseExceptionFilter {
       private readonly logger = new Logger(LoggingExceptionFilter.name);
    
       catch(exception: unknown, host: ArgumentsHost) {
         const ctx = host.switchToHttp();
         const req = ctx.getRequest<Request>();
         const res = ctx.getResponse();
    
         // Journaliser la pile ou le message
         if (exception instanceof Error) {
           this.logger.error(`Error on ${req.method} ${req.url}`, exception.stack);
         } else {
           this.logger.error(`Unknown exception on ${req.method} ${req.url}`);
         }
    
         // Déléguer au filtre par défaut pour les exceptions HTTP ou 500 générique
         super.catch(exception, host);
       }
     }
    ```
    
    **Appliquer globalement** dans `main.ts` :
    
    ```
     async function bootstrap() {
       const app = await NestFactory.create(AppModule);
       app.useGlobalFilters(new LoggingExceptionFilter(app.get(HttpAdapterHost)));
       await app.listen(3000);
     }
    ```
    
    (Si vous étendez `BaseExceptionFilter`, passez le host de l'adaptateur au constructeur ou au super selon les besoins.)
    
2.  **Forme de réponse personnalisée**  
    Supposons que vous vouliez que toutes les erreurs renvoient `{ success: false, error: { code, message } }` :
    
    ```
     // custom-response.filter.ts
     import {
       ExceptionFilter,
       Catch,
       ArgumentsHost,
       HttpException,
       HttpStatus,
     } from '@nestjs/common';
    
     @Catch()
     export class CustomResponseFilter implements ExceptionFilter {
       catch(exception: unknown, host: ArgumentsHost) {
         const ctx = host.switchToHttp();
         const response = ctx.getResponse();
         const request = ctx.getRequest<Request>();
    
         let status: number;
         let message: string | object;
    
         if (exception instanceof HttpException) {
           status = exception.getStatus();
           const res = exception.getResponse();
           // res peut être une chaîne ou un objet
           message = typeof res === 'string' ? { message: res } : res;
         } else {
           status = HttpStatus.INTERNAL_SERVER_ERROR;
           message = { message: 'Internal server error' };
         }
    
         response.status(status).json({
           success: false,
           error: {
             statusCode: status,
             ...(
               typeof message === 'object'
                 ? message
                 : { message }
             ),
           },
           timestamp: new Date().toISOString(),
           path: request.url,
         });
       }
     }
    ```
    
    **Appliquer au niveau du contrôleur ou de la route** :
    
    ```
     @Controller('orders')
     @UseFilters(CustomResponseFilter)
     export class OrdersController {
       // ...
     }
    ```
    
3.  **Intercepter des exceptions spécifiques**  
    Si vous avez une classe d'exception personnalisée :
    
    ```
     export class PaymentFailedException extends HttpException {
       constructor(details: string) {
         super({ message: 'Payment failed', details }, HttpStatus.PAYMENT_REQUIRED);
       }
     }
    ```
    
    Vous pouvez écrire un filtre qui n'intercepte que cela :
    
    ```
     @Catch(PaymentFailedException)
     export class PaymentFailedFilter implements ExceptionFilter {
       catch(exception: PaymentFailedException, host: ArgumentsHost) {
         const ctx = host.switchToHttp();
         const res = ctx.getResponse();
         const status = exception.getStatus();
         const { message, details } = exception.getResponse() as any;
         res.status(status).json({
           error: {
             message,
             details,
           },
           help: 'Please verify your payment method and retry.',
         });
       }
     }
    ```
    
    Puis l'appliquer uniquement là où les paiements ont lieu :
    
    ```
     @Post('charge')
     @UseFilters(PaymentFailedFilter)
     charge() {
       // ...
     }
    ```
    

Avec les filtres d'exception en place, vous garantissez un contrat d'erreur cohérent, une journalisation ou un signalement centralisé, et une gestion sur mesure des différents types d'erreurs. Prochaine étape : **Intercepteurs et Journalisation**, où nous verrons comment transformer les réponses, mesurer les performances et intervenir autour de l'exécution des méthodes.

## 10\. Intercepteurs et Journalisation (Logging)

Les intercepteurs enveloppent l'exécution des méthodes, vous permettant de transformer les réponses, de lier une logique supplémentaire avant/après les appels de méthode ou de mesurer les performances. Ils sont idéaux pour les préoccupations transversales comme la journalisation, la mise en forme des réponses, la mise en cache ou les métriques de temps.

### 10.1 Transformer les réponses

Un **Intercepteur** implémente l'interface `NestInterceptor` avec une méthode `intercept(context, next)`.

À l'intérieur de `intercept`, vous appelez généralement `next.handle()` qui renvoie un `Observable` du résultat du gestionnaire. Vous pouvez ensuite appliquer des opérateurs RxJS (comme `map`) pour modifier les données avant qu'elles ne soient envoyées au client.

Les utilisations courantes consistent à envelopper toutes les réponses dans une enveloppe uniforme, à filtrer certains champs ou à ajouter des métadonnées.

**Voici comment cela fonctionne :**

1.  **Enveloppe de réponse basique**  
    Supposons que vous vouliez que chaque réponse réussie soit `{ success: true, data: <original> }`.
    
    ```
     // response.interceptor.ts
     import {
       Injectable,
       NestInterceptor,
       ExecutionContext,
       CallHandler,
     } from '@nestjs/common';
     import { Observable } from 'rxjs';
     import { map } from 'rxjs/operators';
    
     @Injectable()
     export class ResponseInterceptor implements NestInterceptor {
       intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
         return next.handle().pipe(
           map(data => ({
             success: true,
             data,
           })),
         );
       }
     }
    ```
    
    **Appliquer globalement** dans `main.ts` :
    
    ```
     import { NestFactory } from '@nestjs/core';
     import { AppModule } from './app.module';
     import { ResponseInterceptor } from './common/response.interceptor';
    
     async function bootstrap() {
       const app = await NestFactory.create(AppModule);
       app.useGlobalInterceptors(new ResponseInterceptor());
       await app.listen(3000);
     }
     bootstrap();
    ```
    
    Désormais, si une méthode de contrôleur renvoie `{ id: 1, name: 'Alice' }`, le client verra :
    
    ```
     {
       "success": true,
       "data": { "id": 1, "name": "Alice" }
     }
    ```
    
2.  **Filtrer les champs sensibles**  
    Vous pourriez vouloir supprimer des champs comme `password` avant d'envoyer un objet utilisateur :
    
    ```
     // sanitize.interceptor.ts
     import {
       Injectable,
       NestInterceptor,
       ExecutionContext,
       CallHandler,
     } from '@nestjs/common';
     import { Observable } from 'rxjs';
     import { map } from 'rxjs/operators';
    
     @Injectable()
     export class SanitizeInterceptor implements NestInterceptor {
       intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
         return next.handle().pipe(
           map(data => {
             if (data && typeof data === 'object') {
               const { password, ...rest } = data;
               return rest;
             }
             return data;
           }),
         );
       }
     }
    ```
    
    **Appliquer au niveau du contrôleur ou de la route** :
    
    ```
     @Controller('users')
     @UseInterceptors(SanitizeInterceptor)
     export class UsersController {
       @Get(':id')
       getUser(@Param('id') id: string) {
         // renvoie un objet utilisateur avec un champ password en interne,
         // mais l'intercepteur le supprime avant l'envoi au client
         return this.usersService.findOne(+id);
       }
     }
    ```
    
3.  **Sérialisation avec** `class-transformer`  
    Si vous utilisez des classes avec des décorateurs, vous pouvez intégrer `class-transformer` :
    
    ```
     // user.entity.ts
     import { Exclude, Expose } from 'class-transformer';
    
     export class User {
       id: number;
       name: string;
    
       @Exclude()
       password: string;
    
       @Expose()
       get displayName(): string {
         return `${this.name} (#${this.id})`;
       }
     }
    ```
    
    ```
     // class-transform.interceptor.ts
     import {
       Injectable,
       NestInterceptor,
       ExecutionContext,
       CallHandler,
     } from '@nestjs/common';
     import { plainToInstance } from 'class-transformer';
     import { Observable } from 'rxjs';
     import { map } from 'rxjs/operators';
    
     @Injectable()
     export class ClassTransformInterceptor<T> implements NestInterceptor {
       constructor(private dto: new (...args: any[]) => T) {}
    
       intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
         return next.handle().pipe(
           map(data => {
             return plainToInstance(this.dto, data, {
               excludeExtraneousValues: true,
             });
           }),
         );
       }
     }
    ```
    
    **Appliquer avec un DTO** :
    
    ```
     @Controller('users')
     export class UsersController {
       @Get(':id')
       @UseInterceptors(new ClassTransformInterceptor(User))
       getUser(@Param('id') id: string) {
         // le service renvoie un objet simple ; l'intercepteur le transforme en instance de User
         return this.usersService.findOne(+id);
       }
     }
    ```
    

### 10.2 Journalisation et métriques de performance

Les intercepteurs peuvent également mesurer le temps d'exécution ou journaliser les détails de la requête/réponse. Vous capturez les horodatages avant et après `next.handle()`, en journalisant la différence. Cela aide à surveiller les points de terminaison lents. Combiné avec un framework de journalisation ou le `Logger` de Nest, vous pouvez standardiser les logs.

**Voici comment cela fonctionne :**

1.  **Intercepteur de temps**  
    Journalise le temps mis par chaque gestionnaire de requête :
    
    ```
     // logging.interceptor.ts
     import {
       Injectable,
       NestInterceptor,
       ExecutionContext,
       CallHandler,
       Logger,
     } from '@nestjs/common';
     import { Observable } from 'rxjs';
     import { tap } from 'rxjs/operators';
    
     @Injectable()
     export class LoggingInterceptor implements NestInterceptor {
       private readonly logger = new Logger(LoggingInterceptor.name);
    
       intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
         const req = context.switchToHttp().getRequest();
         const method = req.method;
         const url = req.url;
         const now = Date.now();
         return next.handle().pipe(
           tap(() => {
             const elapsed = Date.now() - now;
             this.logger.log(`${method} ${url} - ${elapsed}ms`);
           }),
         );
       }
     }
    ```
    
    **Appliquer globalement** :
    
    ```
     async function bootstrap() {
       const app = await NestFactory.create(AppModule);
       app.useGlobalInterceptors(new LoggingInterceptor());
       await app.listen(3000);
     }
    ```
    
    Désormais, chaque requête journalise quelque chose comme :
    
    ```
     [LoggingInterceptor] GET /users/1 - 35ms
    ```
    
2.  **Journalisation détaillée requête/réponse**  
    Pour plus de détails, journalisez le corps de la requête ou la taille de la réponse (attention aux données sensibles) :
    
    ```
     // detailed-logging.interceptor.ts
     import {
       Injectable,
       NestInterceptor,
       ExecutionContext,
       CallHandler,
       Logger,
     } from '@nestjs/common';
     import { Observable } from 'rxjs';
     import { tap, map } from 'rxjs/operators';
    
     @Injectable()
     export class DetailedLoggingInterceptor implements NestInterceptor {
       private readonly logger = new Logger('HTTP');
    
       intercept(context: ExecutionContext, next: CallHandler): Observable<any> {
         const ctx = context.switchToHttp();
         const req = ctx.getRequest<Request>();
         const { method, url, body } = req;
         const now = Date.now();
    
         this.logger.log(`Incoming ${method} ${url} - body: ${JSON.stringify(body)}`);
    
         return next.handle().pipe(
           map(data => {
             const elapsed = Date.now() - now;
             this.logger.log(`Response ${method} ${url} - ${elapsed}ms - data: ${JSON.stringify(data)}`);
             return data;
           }),
         );
       }
     }
    ```
    
    **Appliquer conditionnellement** : peut-être uniquement en développement :
    
    ```
     if (process.env.NODE_ENV !== 'production') {
       app.useGlobalInterceptors(new DetailedLoggingInterceptor());
     }
    ```
    
3.  **Combinaison avec les guards/pipes**  
    Puisque les intercepteurs s'exécutent après les guards et avant l'envoi de la réponse, le temps de journalisation capture l'intégralité du gestionnaire, y compris les appels de service, mais après la validation/autorisation. Cela garantit que vous ne mesurez que les requêtes autorisées et les flux de données valides.
    

Les intercepteurs offrent un moyen flexible d'envelopper vos gestionnaires avec un comportement supplémentaire : transformation des sorties, assainissement des données, chronométrage de l'exécution ou ajout d'en-têtes. Dans la section suivante, nous explorerons l'**Intégration de bases de données** pour voir comment intégrer votre couche de données dans Nest.

## 11\. Intégration de bases de données

Dans de nombreuses applications réelles, la persistance des données est essentielle. NestJS offre un support de premier ordre et des intégrations pour plusieurs technologies de base de données. Dans cette section, nous couvrons trois approches courantes :

-   **TypeORM avec NestJS** (bases de données relationnelles, style Active Record/Data Mapper)
    
-   **Mongoose (MongoDB)** (magasin de documents NoSQL)
    
-   **Prisma** (générateur de requêtes typé / alternative ORM)
    

Pour chacune, nous expliquerons la théorie – quand et pourquoi la choisir – et montrerons des exemples pratiques concis de configuration et d'utilisation dans un contexte NestJS.

### 11.1 TypeORM avec NestJS

TypeORM est un ORM populaire pour Node.js qui supporte plusieurs bases de données relationnelles (PostgreSQL, MySQL, SQLite, SQL Server, etc.), offrant à la fois les modèles Active Record et Data Mapper.

Dans NestJS, le package `@nestjs/typeorm` enveloppe TypeORM pour fournir :

-   **Gestion automatique de la connexion** via `TypeOrmModule.forRoot()`
    
-   **Repositories/entités scopés par module** via `TypeOrmModule.forFeature()`
    
-   **Injection de dépendances** pour les repositories et le `DataSource`/`Connection`
    
-   **Décorateurs d'entités** (`@Entity()`, `@Column()`, etc.) pour la définition du schéma
    
-   **Migrations** et fonctionnalités avancées via la CLI TypeORM ou l'utilisation programmatique
    

#### Quand choisir TypeORM

TypeORM est utile dans plusieurs scénarios. Utilisez-le lorsque vos données sont relationnelles et que vous voulez un ORM complet avec des décorateurs et des migrations intégrées. C'est également excellent si vous préférez travailler avec des classes/entités et les mapper automatiquement aux tables. Et c'est un excellent choix si vous appréciez les fonctionnalités intégrées telles que les relations eager/lazy, les cascades, les générateurs de requêtes et les patterns repository.

#### Voici comment l'utiliser :

1.  **Installer les dépendances :**
    
    ```
     npm install --save @nestjs/typeorm typeorm reflect-metadata
     # Installez également le pilote de base de données ; ex pour Postgres :
     npm install --save pg
    ```
    
2.  **Configurer le module racine :**
    
    Dans `app.module.ts`, importez `TypeOrmModule.forRoot()` avec les options de connexion. Celles-ci peuvent provenir de variables d'environnement (abordées plus tard dans Gestion de la configuration).
    
    ```
     // src/app.module.ts
     import { Module } from '@nestjs/common';
     import { TypeOrmModule } from '@nestjs/typeorm';
     import { UsersModule } from './users/users.module';
    
     @Module({
       imports: [
         TypeOrmModule.forRoot({
           type: 'postgres',
           host: process.env.DB_HOST || 'localhost',
           port: +process.env.DB_PORT || 5432,
           username: process.env.DB_USER || 'postgres',
           password: process.env.DB_PASS || 'password',
           database: process.env.DB_NAME || 'mydb',
           entities: [__dirname + '/**/*.entity{.ts,.js}'],
           synchronize: false, // recommandé à false en production ; utilisez les migrations
           // logging: true,
         }),
         UsersModule,
         // ...autres modules
       ],
     })
     export class AppModule {}
    ```
    
    -   `synchronize: true` peut auto-synchroniser le schéma en développement, mais en production, préférez les migrations.
        
    -   Les entités sont chargées automatiquement via glob. Assurez-vous que le chemin correspond à la sortie compilée.
        
3.  **Définir une entité :**
    
    Créez une classe d'entité avec des décorateurs :
    
    ```
     // src/users/user.entity.ts
     import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, UpdateDateColumn } from 'typeorm';
    
     @Entity({ name: 'users' })
     export class User {
       @PrimaryGeneratedColumn()
       id: number;
    
       @Column({ unique: true })
       email: string;
    
       @Column()
       password: string;
    
       @Column({ nullable: true })
       name?: string;
    
       @CreateDateColumn()
       createdAt: Date;
    
       @UpdateDateColumn()
       updatedAt: Date;
     }
    ```
    
4.  **Configurer le module de fonctionnalité :**
    
    ```
     // src/users/users.module.ts
     import { Module } from '@nestjs/common';
     import { TypeOrmModule } from '@nestjs/typeorm';
     import { UsersService } from './users.service';
     import { UsersController } from './users.controller';
     import { User } from './user.entity';
    
     @Module({
       imports: [TypeOrmModule.forFeature([User])],
       providers: [UsersService],
       controllers: [UsersController],
       exports: [UsersService], // si d'autres modules ont besoin de UsersService
     })
     export class UsersModule {}
    ```
    
5.  **Injecter le repository :**
    
    Dans le service, injectez le `Repository<User>` :
    
    ```
     // src/users/users.service.ts
     import { Injectable, NotFoundException } from '@nestjs/common';
     import { InjectRepository } from '@nestjs/typeorm';
     import { Repository } from 'typeorm';
     import { User } from './user.entity';
     import { CreateUserDto } from './dto/create-user.dto';
    
     @Injectable()
     export class UsersService {
       constructor(
         @InjectRepository(User)
         private readonly userRepository: Repository<User>,
       ) {}
    
       async create(dto: CreateUserDto): Promise<User> {
         const user = this.userRepository.create(dto); // mappe les champs DTO à l'entité
         return this.userRepository.save(user);
       }
    
       async findAll(): Promise<User[]> {
         return this.userRepository.find();
       }
    
       async findOne(id: number): Promise<User> {
         const user = await this.userRepository.findOne({ where: { id } });
         if (!user) {
           throw new NotFoundException(`User #${id} not found`);
         }
         return user;
       }
    
       async update(id: number, dto: Partial<CreateUserDto>): Promise<User> {
         const user = await this.findOne(id);
         Object.assign(user, dto);
         return this.userRepository.save(user);
       }
    
       async remove(id: number): Promise<void> {
         await this.userRepository.delete(id);
       }
     }
    ```
    
6.  **Utilisation dans le contrôleur :**
    
    ```
     // src/users/users.controller.ts
     import { Controller, Get, Post, Body, Param, ParseIntPipe, Put, Delete } from '@nestjs/common';
     import { UsersService } from './users.service';
     import { CreateUserDto } from './dto/create-user.dto';
    
     @Controller('users')
     export class UsersController {
       constructor(private readonly usersService: UsersService) {}
    
       @Post()
       create(@Body() dto: CreateUserDto) {
         return this.usersService.create(dto);
       }
    
       @Get()
       findAll() {
         return this.usersService.findAll();
       }
    
       @Get(':id')
       findOne(@Param('id', ParseIntPipe) id: number) {
         return this.usersService.findOne(id);
       }
    
       @Put(':id')
       update(
         @Param('id', ParseIntPipe) id: number,
         @Body() dto: Partial<CreateUserDto>,
       ) {
         return this.usersService.update(id, dto);
       }
    
       @Delete(':id')
       remove(@Param('id', ParseIntPipe) id: number) {
         return this.usersService.remove(id);
       }
     }
    ```
    
7.  **Migrations (optionnel mais recommandé)**
    
    -   Utilisez la CLI TypeORM ou les migrations programmatiques.
        
    -   Configurez un `ormconfig` séparé ou fournissez les options dans le code.
        
    -   Générez et exécutez des migrations pour faire évoluer le schéma sans perte de données.
        

### 11.2 Mongoose (MongoDB)

Mongoose est un ODM (Object Document Mapper) largement utilisé pour MongoDB. Dans NestJS, `@nestjs/mongoose` intègre Mongoose pour :

-   Définir des **schémas** via des classes et des décorateurs (`@Schema()`, `@Prop()`)
    
-   Enregistrer les modèles dans les modules avec `MongooseModule.forFeature()`
    
-   Gérer la connexion MongoDB avec `MongooseModule.forRoot()`
    
-   Injecter des instances de **Model** Mongoose dans les services
    
-   Travailler avec des documents de manière typée (avec des interfaces/types)
    
-   Exploiter des fonctionnalités telles que les hooks, les virtuals et la validation au niveau du schéma
    

#### Quand choisir Mongoose

Mongoose est un bon choix si vous avez besoin d'un magasin NoSQL orienté document, sans schéma ou avec schéma. C'est également excellent si vos formes de données peuvent varier, ou si vous préférez le schéma flexible de MongoDB. Et c'est utile si vous voulez des fonctionnalités comme des hooks middleware dans le schéma (pre/post save), des virtuals, etc.

#### Voici comment l'utiliser :

1.  **Installer les dépendances :**
    
    ```
     npm install --save @nestjs/mongoose mongoose
    ```
    
2.  **Configurer le module racine :**
    
    ```
     // src/app.module.ts
     import { Module } from '@nestjs/common';
     import { MongooseModule } from '@nestjs/mongoose';
     import { CatsModule } from './cats/cats.module';
    
     @Module({
       imports: [
         MongooseModule.forRoot(process.env.MONGO_URI || 'mongodb://localhost/nest'),
         CatsModule,
         // ...autres modules
       ],
     })
     export class AppModule {}
    ```
    
3.  **Définir un schéma et un document :**
    
    Utilisez des décorateurs et des interfaces :
    
    ```
     // src/cats/schemas/cat.schema.ts
     import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
     import { Document } from 'mongoose';
    
     @Schema({ timestamps: true })
     export class Cat extends Document {
       @Prop({ required: true })
       name: string;
    
       @Prop()
       age: number;
    
       @Prop()
       breed: string;
     }
    
     export const CatSchema = SchemaFactory.createForClass(Cat);
    ```
    
    -   Étendre `Document` donne au document Mongoose ses méthodes et propriétés.
        
    -   `timestamps: true` ajoute automatiquement `createdAt` et `updatedAt`.
        
    -   Vous pouvez ajouter des hooks :
        
        ```
          CatSchema.pre<Cat>('save', function (next) {
            // ex : modifier des données ou journaliser avant la sauvegarde
            next();
          });
        ```
        
4.  **Configurer le module de fonctionnalité :**
    
    ```
     // src/cats/cats.module.ts
     import { Module } from '@nestjs/common';
     import { MongooseModule } from '@nestjs/mongoose';
     import { CatsService } from './cats.service';
     import { CatsController } from './cats.controller';
     import { Cat, CatSchema } from './schemas/cat.schema';
    
     @Module({
       imports: [
         MongooseModule.forFeature([{ name: Cat.name, schema: CatSchema }]),
       ],
       controllers: [CatsController],
       providers: [CatsService],
     })
     export class CatsModule {}
    ```
    
5.  **Injecter le modèle :**
    
    Dans le service, injectez `Model<Cat>` :
    
    ```
     // src/cats/cats.service.ts
     import { Injectable, NotFoundException } from '@nestjs/common';
     import { InjectModel } from '@nestjs/mongoose';
     import { Model } from 'mongoose';
     import { Cat } from './schemas/cat.schema';
     import { CreateCatDto } from './dto/create-cat.dto';
     import { UpdateCatDto } from './dto/update-cat.dto';
    
     @Injectable()
     export class CatsService {
       constructor(
         @InjectModel(Cat.name) private readonly catModel: Model<Cat>,
       ) {}
    
       async create(dto: CreateCatDto): Promise<Cat> {
         const created = new this.catModel(dto);
         return created.save();
       }
    
       async findAll(): Promise<Cat[]> {
         return this.catModel.find().exec();
       }
    
       async findOne(id: string): Promise<Cat> {
         const cat = await this.catModel.findById(id).exec();
         if (!cat) {
           throw new NotFoundException(`Cat ${id} not found`);
         }
         return cat;
       }
    
       async update(id: string, dto: UpdateCatDto): Promise<Cat> {
         const updated = await this.catModel
           .findByIdAndUpdate(id, dto, { new: true })
           .exec();
         if (!updated) {
           throw new NotFoundException(`Cat ${id} not found`);
         }
         return updated;
       }
    
       async remove(id: string): Promise<void> {
         const res = await this.catModel.findByIdAndDelete(id).exec();
         if (!res) {
           throw new NotFoundException(`Cat ${id} not found`);
         }
       }
     }
    ```
    
6.  **Utilisation dans le contrôleur :**
    
    ```
     // src/cats/cats.controller.ts
     import { Controller, Get, Post, Body, Param, Put, Delete } from '@nestjs/common';
     import { CatsService } from './cats.service';
     import { CreateCatDto } from './dto/create-cat.dto';
     import { UpdateCatDto } from './dto/update-cat.dto';
    
     @Controller('cats')
     export class CatsController {
       constructor(private readonly catsService: CatsService) {}
    
       @Post()
       create(@Body() dto: CreateCatDto) {
         return this.catsService.create(dto);
       }
    
       @Get()
       findAll() {
         return this.catsService.findAll();
       }
    
       @Get(':id')
       findOne(@Param('id') id: string) {
         return this.catsService.findOne(id);
       }
    
       @Put(':id')
       update(
         @Param('id') id: string,
         @Body() dto: UpdateCatDto,
       ) {
         return this.catsService.update(id, dto);
       }
    
       @Delete(':id')
       remove(@Param('id') id: string) {
         return this.catsService.remove(id);
       }
     }
    ```
    
7.  **Fonctionnalités Mongoose avancées**
    
    -   **Virtuals** : définir des propriétés calculées non stockées en base.
        
    -   **Index** : via les options de schéma ou `@Prop({ index: true })`.
        
    -   **Populate** : référencer d'autres collections avec `@Prop({ type: Types.ObjectId, ref: 'OtherModel' })`.
        
    -   **Transactions** : utiliser les sessions MongoDB pour des opérations atomiques multi-documents.
        

### 11.3 Prisma

Prisma est un ORM/générateur de requêtes moderne qui génère un client typé basé sur une définition de schéma. Il supporte les bases de données relationnelles (PostgreSQL, MySQL, SQLite, SQL Server, etc.).

Voici quelques-unes de ses caractéristiques clés :

-   **Requêtes typées** : Les définitions TypeScript générées automatiquement évitent de nombreuses erreurs d'exécution.
    
-   **Schéma Prisma** : Un fichier déclaratif `.prisma` pour définir les modèles, les relations et les enums.
    
-   **Migrations** : `prisma migrate` pour faire évoluer le schéma.
    
-   **Performance** : Générateur de requêtes léger sans surcharge importante à l'exécution.
    
-   **Flexibilité** : Supporte les requêtes brutes (raw queries) si nécessaire.
    

#### Quand choisir Prisma

Prisma est un excellent choix si vous préférez une approche "schema-first" avec un DSL clair et un client typé généré automatiquement. C'est également excellent si vous voulez des fonctionnalités modernes comme des migrations efficaces, une inférence de type riche et une expérience de développement simple. Et c'est un choix solide si vous n'avez pas besoin du pattern Active Record. À la place, vous utilisez le client Prisma dans les services.

#### Voici comment cela fonctionne :

1.  **Installer les dépendances et initialiser :**
    
    ```
     npm install @prisma/client
     npm install -D prisma
     npx prisma init
    ```
    
    Cela crée un fichier `prisma/schema.prisma` et un fichier `.env` avec `DATABASE_URL`.
    
2.  **Définir le schéma :**
    
    Dans `prisma/schema.prisma` :
    
    ```
     datasource db {
       provider = "postgresql"
       url      = env("DATABASE_URL")
     }
    
     generator client {
       provider = "prisma-client-js"
     }
    
     model User {
       id        Int      @id @default(autoincrement())
       email     String   @unique
       name      String?
       posts     Post[]
       createdAt DateTime @default(now())
       updatedAt DateTime @updatedAt
     }
    
     model Post {
       id        Int      @id @default(autoincrement())
       title     String
       content   String?
       author    User     @relation(fields: [authorId], references: [id])
       authorId  Int
       published Boolean  @default(false)
       createdAt DateTime @default(now())
       updatedAt DateTime @updatedAt
     }
    ```
    
3.  **Exécuter les migrations et générer le client :**
    
    ```
     npx prisma migrate dev --name init
     npx prisma generate
    ```
    
    Cela met à jour le schéma de la base de données et régénère le client TypeScript.
    
4.  **Créer un PrismaService dans NestJS :**
    
    Un pattern courant consiste à envelopper le `PrismaClient` dans un service injectable, gérant les hooks de cycle de vie.
    
    ```
     // src/prisma/prisma.service.ts
     import { Injectable, OnModuleInit, OnModuleDestroy } from '@nestjs/common';
     import { PrismaClient } from '@prisma/client';
    
     @Injectable()
     export class PrismaService extends PrismaClient implements OnModuleInit, OnModuleDestroy {
       async onModuleInit() {
         await this.$connect();
       }
    
       async onModuleDestroy() {
         await this.$disconnect();
       }
     }
    ```
    
5.  **Enregistrer PrismaService dans un module :**
    
    ```
     // src/prisma/prisma.module.ts
     import { Module } from '@nestjs/common';
     import { PrismaService } from './prisma.service';
    
     @Module({
       providers: [PrismaService],
       exports: [PrismaService],
     })
     export class PrismaModule {}
    ```
    
    Importez ensuite `PrismaModule` dans tout module de fonctionnalité nécessitant un accès à la base de données.
    
6.  **Utilisation dans un service de fonctionnalité :**
    
    ```
     // src/users/users.service.ts
     import { Injectable } from '@nestjs/common';
     import { PrismaService } from '../prisma/prisma.service';
     import { CreateUserDto } from './dto/create-user.dto';
    
     @Injectable()
     export class UsersService {
       constructor(private readonly prisma: PrismaService) {}
    
       async create(dto: CreateUserDto) {
         return this.prisma.user.create({ data: dto });
       }
    
       async findAll() {
         return this.prisma.user.findMany();
       }
    
       async findOne(id: number) {
         return this.prisma.user.findUnique({ where: { id } });
       }
    
       async update(id: number, dto: Partial<CreateUserDto>) {
         return this.prisma.user.update({
           where: { id },
           data: dto,
         });
       }
    
       async remove(id: number) {
         await this.prisma.user.delete({ where: { id } });
         return { deleted: true };
       }
     }
    ```
    
    Note : Les champs DTO doivent s'aligner sur les types du schéma Prisma. Les méthodes du client Prisma renvoient des résultats typés.
    
7.  **Injecter dans le contrôleur :**
    
    ```
     // src/users/users.controller.ts
     import { Controller, Get, Post, Body, Param, ParseIntPipe, Put, Delete } from '@nestjs/common';
     import { UsersService } from './users.service';
     import { CreateUserDto } from './dto/create-user.dto';
    
     @Controller('users')
     export class UsersController {
       constructor(private readonly usersService: UsersService) {}
    
       @Post()
       create(@Body() dto: CreateUserDto) {
         return this.usersService.create(dto);
       }
    
       @Get()
       findAll() {
         return this.usersService.findAll();
       }
    
       @Get(':id')
       findOne(@Param('id', ParseIntPipe) id: number) {
         return this.usersService.findOne(id);
       }
    
       @Put(':id')
       update(
         @Param('id', ParseIntPipe) id: number,
         @Body() dto: Partial<CreateUserDto>,
       ) {
         return this.usersService.update(id, dto);
       }
    
       @Delete(':id')
       remove(@Param('id', ParseIntPipe) id: number) {
         return this.usersService.remove(id);
       }
     }
    ```
    
8.  **Utilisation avancée de Prisma**
    
    -   **Relations et écritures imbriquées** : par exemple, créer un post avec un auteur imbriqué (connect/create).
        
    -   **Transactions** : `this.prisma.$transaction([...])` pour des opérations atomiques.
        
    -   **Requêtes brutes** : `this.prisma.$queryRaw` si nécessaire.
        
    -   **Middleware** : Prisma supporte les middlewares côté client.
        
    -   **Optimisation des performances** : sélectionner uniquement les champs nécessaires, utiliser les patterns de pagination.
        

Avec ces trois approches, vous pouvez choisir la stratégie d'intégration de base de données qui correspond le mieux aux besoins de votre application :

-   **TypeORM** pour un ORM complet avec support des décorateurs et des migrations dans les bases de données relationnelles.
    
-   **Mongoose** pour des schémas de documents flexibles dans MongoDB.
    
-   **Prisma** pour une alternative moderne de générateur de requêtes/ORM typé avec une excellente ergonomie pour le développeur.
    

Dans la section suivante, nous aborderons la **Gestion de la configuration** – comment gérer les variables d'environnement et les modules de configuration dans NestJS.

## 12\. Gestion de la configuration

Gérer proprement la configuration est crucial pour que les applications se comportent correctement selon les environnements (développement, staging, production). NestJS fournit le module `@nestjs/config` pour centraliser le chargement, la validation et l'injection de la configuration.

### 12.1 Module @nestjs/config

Le module `@nestjs/config` est un utilitaire puissant pour gérer les paramètres de configuration de l'application. Voici quelques-unes de ses caractéristiques clés :

-   **Configuration centralisée** : Au lieu de disperser `process.env` dans tout votre code, il utilise un service dédié qui charge et valide la configuration une seule fois au démarrage.
    
-   **Indépendant de l'environnement** : Il charge les variables à partir de fichiers `.env`, de variables d'environnement ou d'autres sources, avec un support pour différents fichiers par environnement.
    
-   **Validation** : Il intègre un schéma (par exemple via Joi) pour garantir que les variables requises sont présentes et correctement typées, échouant rapidement en cas de mauvaise configuration.
    
-   **Namespacing de configuration** : Il organise les paramètres liés en groupes logiques (par exemple, base de données, auth, API tierces) via des usines de configuration (factories).
    
-   **Injection** : Il injecte un `ConfigService` pour lire les valeurs de configuration dans les services ou les modules, avec une sécurité de typage lors de l'utilisation d'enveloppes typées personnalisées.
    

#### Voici comment cela fonctionne :

1.  **Installer le package**
    
    ```
     npm install @nestjs/config
     npm install joi    # si vous prévoyez de valider via des schémas Joi
    ```
    
2.  **Importer et initialiser ConfigModule**
    
    Dans votre module racine (`AppModule`), importez `ConfigModule.forRoot()`. Options typiques :
    
    ```
     // src/app.module.ts
     import { Module } from '@nestjs/common';
     import { ConfigModule } from '@nestjs/config';
     import configuration from './config/configuration';
     import { validationSchema } from './config/validation';
    
     @Module({
       imports: [
         ConfigModule.forRoot({
           // Charger .env automatiquement ; spécifier envFilePath si personnalisé :
           isGlobal: true,           // rend ConfigService disponible dans toute l'app
           envFilePath: ['.env.development.local', '.env.development', '.env'], 
           load: [configuration],    // optionnel : charger des usines de config personnalisées
           validationSchema,         // optionnel : schéma Joi pour valider les vars d'env
           validationOptions: {
             allowUnknown: true,
             abortEarly: true,
           },
         }),
         // ...autres modules
       ],
     })
     export class AppModule {}
    ```
    
    -   `isGlobal: true` évite d'importer `ConfigModule` dans chaque module de fonctionnalité.
        
    -   `envFilePath` : un tableau vous permet d'essayer plusieurs fichiers (par exemple, des surcharges locales avant le défaut).
        
    -   `load` : tableau de fonctions renvoyant des objets de config partiels – voir l'étape suivante.
        
    -   `validationSchema` : un schéma Joi garantissant que les variables requises existent et sont du bon type/format.
        
3.  **Définir une usine de configuration**
    
    Organisez les paramètres liés dans un objet typé :
    
    ```
     // src/config/configuration.ts
     export default () => ({
       port: parseInt(process.env.PORT, 10) || 3000,
       database: {
         host: process.env.DB_HOST,
         port: parseInt(process.env.DB_PORT, 10) || 5432,
         user: process.env.DB_USER,
         pass: process.env.DB_PASS,
         name: process.env.DB_NAME,
       },
       jwt: {
         secret: process.env.JWT_SECRET,
         expiresIn: process.env.JWT_EXPIRES_IN || '1h',
       },
       // ajouter d'autres namespaces si besoin
     });
    ```
    
4.  **Valider les variables d'environnement**
    
    Utilisation de Joi pour la validation :
    
    ```
     // src/config/validation.ts
     import * as Joi from 'joi';
    
     export const validationSchema = Joi.object({
       NODE_ENV: Joi.string()
         .valid('development', 'production', 'test', 'staging')
         .default('development'),
       PORT: Joi.number().default(3000),
       DB_HOST: Joi.string().required(),
       DB_PORT: Joi.number().default(5432),
       DB_USER: Joi.string().required(),
       DB_PASS: Joi.string().required(),
       DB_NAME: Joi.string().required(),
       JWT_SECRET: Joi.string().min(32).required(),
       JWT_EXPIRES_IN: Joi.string().default('1h'),
       // ajouter d'autres variables...
     });
    ```
    
    Si la validation échoue au démarrage, l'application s'arrêtera avec des détails, empêchant les déploiements mal configurés.
    
5.  **Injecter ConfigService**
    
    Partout où vous avez besoin de config, injectez `ConfigService` :
    
    ```
     // src/some/some.service.ts
     import { Injectable } from '@nestjs/common';
     import { ConfigService } from '@nestjs/config';
    
     @Injectable()
     export class SomeService {
       constructor(private readonly configService: ConfigService) {}
    
       getDbConfig() {
         const host = this.configService.get<string>('database.host');
         const port = this.configService.get<number>('database.port');
         // Utiliser ces valeurs pour configurer un client de base de données, etc.
         return { host, port };
       }
     }
    ```
    
    -   Utilisez la notation par points pour la config imbriquée : par exemple, `'jwt.secret'`.
        
    -   Vous pouvez également lire les variables d'environnement brutes via `configService.get<string>('DB_HOST')` si nécessaire, mais préférer une config structurée est plus clair.
        
6.  **Enveloppe typée pour ConfigService (optionnel)**
    
    Pour un typage plus fort, créez une interface correspondant à votre configuration et une enveloppe :
    
    ```
     // src/config/config.interface.ts
     export interface AppConfig {
       port: number;
       database: {
         host: string;
         port: number;
         user: string;
         pass: string;
         name: string;
       };
       jwt: {
         secret: string;
         expiresIn: string;
       };
     }
    ```
    
    ```
     // src/config/typed-config.service.ts
     import { Injectable } from '@nestjs/common';
     import { ConfigService } from '@nestjs/config';
     import { AppConfig } from './config.interface';
    
     @Injectable()
     export class TypedConfigService {
       constructor(private readonly configService: ConfigService) {}
    
       get appConfig(): AppConfig {
         return {
           port: this.configService.get<number>('port'),
           database: {
             host: this.configService.get<string>('database.host'),
             port: this.configService.get<number>('database.port'),
             user: this.configService.get<string>('database.user'),
             pass: this.configService.get<string>('database.pass'),
             name: this.configService.get<string>('database.name'),
           },
           jwt: {
             secret: this.configService.get<string>('jwt.secret'),
             expiresIn: this.configService.get<string>('jwt.expiresIn'),
           },
         };
       }
     }
    ```
    
    Enregistrez `TypedConfigService` dans un module si vous préférez l'injecter au lieu du `ConfigService` brut.
    
7.  **Enregistrement de module dynamique utilisant la config**
    
    De nombreux modules Nest acceptent des options dynamiques. Par exemple, TypeORM :
    
    ```
     // src/database/database.module.ts
     import { Module } from '@nestjs/common';
     import { TypeOrmModule } from '@nestjs/typeorm';
     import { ConfigService } from '@nestjs/config';
    
     @Module({
       imports: [
         TypeOrmModule.forRootAsync({
           inject: [ConfigService],
           useFactory: (config: ConfigService) => ({
             type: 'postgres',
             host: config.get<string>('database.host'),
             port: config.get<number>('database.port'),
             username: config.get<string>('database.user'),
             password: config.get<string>('database.pass'),
             database: config.get<string>('database.name'),
             entities: [__dirname + '/../**/*.entity{.ts,.js}'],
             synchronize: config.get('NODE_ENV') !== 'production',
           }),
         }),
       ],
     })
     export class DatabaseModule {}
    ```
    
    L'utilisation de `forRootAsync` avec `useFactory` garantit que la config est chargée avant l'initialisation du module.
    

### 12.2 Variables d'environnement

Les variables d'environnement servent de pont entre le code et son environnement d'exécution, vous permettant de découpler la configuration (comme les URL de base de données, les clés API ou les feature flags) de votre source.

En vous appuyant sur les variables d'environnement, vous garantissez que le même bundle d'application peut s'exécuter en toute sécurité en développement, staging et production – chacun fournissant ses propres paramètres sensibles ou spécifiques à l'environnement sans changer le code. Voici comment cela fonctionne :

-   **Principe de l'application 12-Factor** : Stocke la config dans l'environnement. Évite de coder en dur des secrets ou des paramètres spécifiques à l'environnement dans le code.
    
-   **Séparation des préoccupations** : Le code reste le même d'un environnement à l'autre. Le comportement est piloté par des variables d'environnement ou des fichiers de config.
    
-   **Sécurité** : Garde les secrets (clés API, mots de passe de base de données) hors du contrôle de version. Utilise des variables d'environnement ou des coffres-forts sécurisés.
    
-   **Surcharges et préséance** : Vous pouvez avoir plusieurs fichiers `.env` (par exemple `.env`, `.env.local`, `.env.production`) ou des variables fournies par la CI/CD. Cela contrôle l'ordre de chargement.
    
-   **Valeurs par défaut et replis** : Fournit des valeurs par défaut raisonnables dans le code ou les usines de config afin que l'application puisse s'exécuter en développement sans nécessiter chaque variable.
    

#### Voici comment les utiliser :

1.  **Fichiers .env**
    
    -   Créez un fichier `.env` à la racine du projet avec des paires clé-valeur :
        
        ```
          PORT=3000
          DB_HOST=localhost
          DB_PORT=5432
          DB_USER=postgres
          DB_PASS=secret
          DB_NAME=mydb
          JWT_SECRET=supersecretjwtkey
          JWT_EXPIRES_IN=2h
        ```
        
    -   Créez éventuellement `.env.development`, `.env.test`, `.env.production`, et chargez-les en fonction de `NODE_ENV`.
        
    -   Assurez-vous que les fichiers `.env` sont dans `.gitignore` pour éviter de committer des secrets.
        
2.  **Ordre de chargement**
    
    -   Avec `@nestjs/config`, spécifiez `envFilePath` sous forme de tableau, par exemple :
        
        ```
          ConfigModule.forRoot({
            envFilePath: [
              `.env.${process.env.NODE_ENV}.local`,
              `.env.${process.env.NODE_ENV}`,
              `.env`,
            ],
            isGlobal: true,
          });
        ```
        
    -   Cela essaie `.env.development.local`, puis `.env.development`, puis `.env`. La CI/CD peut définir des variables d'environnement réelles qui surchargent les valeurs des fichiers.
        
3.  **Accéder aux variables d'environnement brutes**
    
    -   Bien que la config structurée soit préférable, vous avez parfois besoin d'un accès direct :
        
        ```
          const raw = process.env.SOME_VAR;
        ```
        
    -   Évitez de disperser `process.env` à plusieurs endroits. Préférez lire une seule fois dans l'usine de configuration et injecter via `ConfigService`.
        
4.  **Valeurs par défaut**
    
    -   Dans l'usine de configuration ou lors de la lecture via `ConfigService`, fournissez des valeurs par défaut :
        
        ```
          const port = configService.get<number>('PORT', 3000);
        ```
        
        ou dans l'usine :
        
        ```
          port: parseInt(process.env.PORT, 10) || 3000
        ```
        
5.  **Coercition de type**
    
    -   Les variables d'environnement sont des chaînes par défaut. Convertissez-les en nombres ou en booléens selon les besoins :
        
        ```
          const isProd = configService.get<string>('NODE_ENV') === 'production';
          const enableFeature = configService.get<string>('FEATURE_FLAG') === 'true';
          const timeout = parseInt(configService.get<string>('TIMEOUT_MS'), 10) || 5000;
        ```
        
6.  **Gestion des secrets**
    
    -   Pour les données sensibles en production, envisagez d'utiliser des gestionnaires de secrets (AWS Secrets Manager, Vault) au lieu de simples fichiers `.env`. Dans ce cas, chargez les secrets au démarrage (par exemple via un provider personnalisé ou une factory) et fusionnez-les dans la configuration.
        
    -   Exemple : dans `useFactory`, récupérez les secrets de manière asynchrone et renvoyez un objet de config les incluant.
        
7.  **Changements de configuration au runtime**
    
    -   Généralement, les configurations sont statiques au démarrage. Si vous devez recharger la config sans redémarrer, implémentez un mécanisme personnalisé (par exemple, lire périodiquement à partir d'une base de données ou d'un service de config distant). Injectez un service qui récupère et met en cache les valeurs, mais notez que cela s'écarte des principes 12-factor.
8.  **Validation en production**
    
    -   Validez toujours les variables d'environnement requises au démarrage afin que les mauvaises configurations échouent tôt. Utilisez `validationSchema` avec Joi ou un autre validateur.
        
    -   Exemple d'erreur : si `JWT_SECRET` est manquant ou trop court, l'application doit refuser de démarrer, en journalisant une erreur claire.
        

Avec une configuration gérée via `@nestjs/config` et des variables d'environnement, votre application NestJS peut s'adapter de manière transparente d'un environnement à l'autre, garder les secrets en sécurité et éviter les changements de code spécifiques à l'environnement. Dans la section suivante, nous aborderons les stratégies d'**Authentification** (JWT, OAuth2/connexion via réseaux sociaux).

## 13\. Authentification

Gérer l'authentification de manière sécurisée est une exigence courante. Dans NestJS, vous utilisez généralement des stratégies **Passport** aux côtés du module **@nestjs/jwt** pour les flux basés sur JWT, ou des stratégies OAuth2 pour la connexion via réseaux sociaux.

Ici, nous couvrirons deux approches courantes :

-   **Stratégie JWT** : authentification par jeton pour les API.
    
-   **OAuth2 / Connexion via réseaux sociaux** : intégration de fournisseurs comme Google ou GitHub.
    

### 13.1 Stratégie JWT

Les JSON Web Tokens (JWT) sont un moyen compact et sûr pour les URL de représenter des revendications (claims) entre deux parties. Dans un contexte d'authentification, le serveur émet un jeton signé contenant l'identité de l'utilisateur et éventuellement d'autres revendications, tandis que le client stocke et envoie ce jeton lors des requêtes ultérieures (généralement dans l'en-tête `Authorization: Bearer <token>`).

Parce que le jeton est signé (et éventuellement chiffré), le serveur peut vérifier son intégrité et son authenticité sans avoir besoin de maintenir un état de session en mémoire ou dans une base de données. Cette nature sans état (stateless) simplifie la mise à l'échelle et découple les services.

Les jetons incluent une expiration (`exp`) afin qu'ils deviennent automatiquement invalides après un certain temps. Pour des sessions plus longues, vous pouvez ajouter un pattern de jeton de rafraîchissement (refresh token) par-dessus.

Dans NestJS, nous exploitons `@nestjs/jwt` pour signer et vérifier les jetons et `@nestjs/passport` avec `passport-jwt` pour intégrer un guard qui vérifie les jetons entrants. Voici comment cela fonctionne :

-   **JWT (JSON Web Token)** : un jeton signé contenant des revendications (par exemple, l'ID utilisateur) que les clients envoient dans l'en-tête `Authorization`.
    
-   **Stateless** : le serveur vérifie la signature du jeton sans stocker l'état de la session.
    
-   **Expiration** : intègre une expiration (`exp`) pour que les jetons expirent automatiquement ; utilise éventuellement des jetons de rafraîchissement pour les sessions de longue durée.
    
-   Dans NestJS, vous utilisez `@nestjs/jwt` pour signer/vérifier les jetons et `@nestjs/passport` avec `passport-jwt` pour implémenter le guard.
    

#### Voici comment l'utiliser :

1.  **Installer les dépendances**
    
    ```
     npm install @nestjs/jwt passport-jwt @nestjs/passport passport
    ```
    
2.  **Configuration**
    
    Utilisez `ConfigService` (de la section précédente) pour charger les secrets et la durée de vie (TTL) :
    
    ```
     // src/auth/auth.config.ts
     export default () => ({
       jwt: {
         secret: process.env.JWT_SECRET || 'default-secret',
         expiresIn: process.env.JWT_EXPIRES_IN || '1h',
       },
     });
    ```
    
    Assurez-vous que `ConfigModule.forRoot({ load: [authConfig], isGlobal: true, validationSchema: ... })` est configuré dans `AppModule`.
    
3.  **Configuration d'AuthModule**
    
    ```
     // src/auth/auth.module.ts
     import { Module } from '@nestjs/common';
     import { JwtModule } from '@nestjs/jwt';
     import { PassportModule } from '@nestjs/passport';
     import { ConfigService, ConfigModule } from '@nestjs/config';
     import { JwtStrategy } from './jwt.strategy';
     import { AuthService } from './auth.service';
     import { UsersModule } from '../users/users.module'; // suppose un UsersService
    
     @Module({
       imports: [
         UsersModule,
         PassportModule.register({ defaultStrategy: 'jwt' }),
         JwtModule.registerAsync({
           imports: [ConfigModule],
           inject: [ConfigService],
           useFactory: (config: ConfigService) => ({
             secret: config.get<string>('jwt.secret'),
             signOptions: { expiresIn: config.get<string>('jwt.expiresIn') },
           }),
         }),
       ],
       providers: [AuthService, JwtStrategy],
       exports: [AuthService],
     })
     export class AuthModule {}
    ```
    
4.  **AuthService**
    
    Responsable de la validation des identifiants et de l'émission des jetons :
    
    ```
     // src/auth/auth.service.ts
     import { Injectable, UnauthorizedException } from '@nestjs/common';
     import { JwtService } from '@nestjs/jwt';
     import { UsersService } from '../users/users.service';
     import * as bcrypt from 'bcrypt';
    
     @Injectable()
     export class AuthService {
       constructor(
         private readonly usersService: UsersService,
         private readonly jwtService: JwtService,
       ) {}
    
       // Valider les identifiants utilisateur (email/mot de passe)
       async validateUser(email: string, pass: string) {
         const user = await this.usersService.findByEmail(email);
         if (user && (await bcrypt.compare(pass, user.password))) {
           // exclure le mot de passe avant de renvoyer
           const { password, ...result } = user;
           return result;
         }
         return null;
       }
    
       // Appelé après le succès de validateUser
       async login(user: any) {
         const payload = { sub: user.id, email: user.email };
         return {
           access_token: this.jwtService.sign(payload),
         };
       }
     }
    ```
    
5.  **JwtStrategy**
    
    ```
     // src/auth/jwt.strategy.ts
     import { Injectable } from '@nestjs/common';
     import { PassportStrategy } from '@nestjs/passport';
     import { ExtractJwt, Strategy } from 'passport-jwt';
     import { ConfigService } from '@nestjs/config';
    
     @Injectable()
     export class JwtStrategy extends PassportStrategy(Strategy) {
       constructor(private readonly configService: ConfigService) {
         super({
           jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
           ignoreExpiration: false,
           secretOrKey: configService.get<string>('jwt.secret'),
         });
       }
    
       async validate(payload: any) {
         // payload.sub est l'ID utilisateur
         return { userId: payload.sub, email: payload.email };
         // la valeur renvoyée est assignée à req.user
       }
     }
    ```
    
6.  **Contrôleur Auth**
    
    Exposer le point de terminaison de connexion :
    
    ```
     // src/auth/auth.controller.ts
     import { Controller, Post, Body, Request, UseGuards } from '@nestjs/common';
     import { AuthService } from './auth.service';
     import { LocalAuthGuard } from './local-auth.guard'; // optionnel si utilisation de la stratégie locale
    
     @Controller('auth')
     export class AuthController {
       constructor(private readonly authService: AuthService) {}
    
       // Exemple : utilisation d'une stratégie locale pour email/mot de passe
       @UseGuards(LocalAuthGuard)
       @Post('login')
       async login(@Request() req) {
         // LocalAuthGuard attache l'utilisateur à req.user
         return this.authService.login(req.user);
       }
    
       // Alternativement, implémenter la logique de connexion directement :
       @Post('login-basic')
       async loginBasic(@Body() body: { email: string; password: string }) {
         const user = await this.authService.validateUser(body.email, body.password);
         if (!user) {
           throw new UnauthorizedException('Invalid credentials');
         }
         return this.authService.login(user);
       }
     }
    ```
    
    -   **LocalAuthGuard** utiliserait une `LocalStrategy` pour valider les identifiants via Passport.
7.  **Protéger les routes**
    
    Utilisez le **JwtAuthGuard** :
    
    ```
     // src/auth/jwt-auth.guard.ts
     import { Injectable } from '@nestjs/common';
     import { AuthGuard } from '@nestjs/passport';
    
     @Injectable()
     export class JwtAuthGuard extends AuthGuard('jwt') {}
    ```
    
    Appliquer aux contrôleurs ou aux routes :
    
    ```
     // src/profile/profile.controller.ts
     import { Controller, Get, UseGuards, Request } from '@nestjs/common';
     import { JwtAuthGuard } from '../auth/jwt-auth.guard';
    
     @Controller('profile')
     export class ProfileController {
       @UseGuards(JwtAuthGuard)
       @Get()
       getProfile(@Request() req) {
         return req.user; // { userId, email }
       }
     }
    ```
    
8.  **Jetons de rafraîchissement (optionnel)**
    
    -   Émettre un jeton de rafraîchissement (expiration plus longue) et le stocker (par exemple en base de données ou sous forme de cookie HTTP-only).
        
    -   Créer un point de terminaison séparé pour émettre un nouveau jeton d'accès lorsque celui-ci expire.
        
    -   Vérifier la validité du jeton de rafraîchissement (par exemple, comparer le jeton stocké ou une version hachée).
        
    -   Les détails d'implémentation varient – tenez compte des meilleures pratiques de sécurité (rotation des jetons, révocation lors de la déconnexion).
        

### 13.2 OAuth2 / Connexion via réseaux sociaux

La connexion sociale via OAuth2 permet aux utilisateurs de s'authentifier auprès de fournisseurs tiers (Google, GitHub, Facebook, etc.) sans créer de mot de passe séparé pour votre service.

Dans le cadre du flux de code d'autorisation (Authorization Code Flow), l'utilisateur est redirigé vers l'écran de consentement du fournisseur. Après avoir accordé la permission, le fournisseur redirige vers votre application avec un code temporaire. Le backend échange ce code contre des jetons d'accès (et éventuellement de rafraîchissement), récupère le profil de l'utilisateur, puis vous pouvez lier ou créer un enregistrement utilisateur local. Enfin, vous émettez généralement votre propre JWT (ou session) afin que le client puisse appeler vos API sécurisées.

Garder les ID/secrets client OAuth dans des variables d'environnement (via `ConfigService`) garantit sécurité et flexibilité. Voici comment cela fonctionne :

-   **OAuth2 Authorization Code Flow** : Redirige l'utilisateur vers l'écran de consentement du fournisseur. Le fournisseur redirige en retour avec un code. Le backend échange le code contre des jetons et récupère les infos utilisateur.
    
-   Côté serveur (NestJS), vous utilisez des stratégies Passport (par exemple `passport-google-oauth20`, `passport-github2`).
    
-   Après avoir obtenu le profil utilisateur du fournisseur, vous recherchez ou créez un enregistrement utilisateur local correspondant, puis vous émettez votre propre JWT ou session.
    
-   Gardez les secrets (ID client/secret) dans des variables d'environnement et chargez-les via `ConfigService`.
    

#### Voici comment l'utiliser :

1.  **Installer les dépendances**
    
    ```
     npm install @nestjs/passport passport passport-google-oauth20
     # ou passport-facebook, passport-github2, etc.
    ```
    
2.  **Configuration**
    
    Ajoutez les identifiants OAuth à l'environnement et au `ConfigModule` :
    
    ```
     GOOGLE_CLIENT_ID=votre-id-client-google
     GOOGLE_CLIENT_SECRET=votre-secret-client-google
     GOOGLE_CALLBACK_URL=http://localhost:3000/auth/google/callback
    ```
    
3.  **Stratégie OAuth**
    
    Exemple : Google
    
    ```
     // src/auth/google.strategy.ts
     import { Injectable } from '@nestjs/common';
     import { PassportStrategy } from '@nestjs/passport';
     import { Strategy, VerifyCallback } from 'passport-google-oauth20';
     import { ConfigService } from '@nestjs/config';
     import { AuthService } from './auth.service';
    
     @Injectable()
     export class GoogleStrategy extends PassportStrategy(Strategy, 'google') {
       constructor(configService: ConfigService, private readonly authService: AuthService) {
         super({
           clientID: configService.get<string>('GOOGLE_CLIENT_ID'),
           clientSecret: configService.get<string>('GOOGLE_CLIENT_SECRET'),
           callbackURL: configService.get<string>('GOOGLE_CALLBACK_URL'),
           scope: ['email', 'profile'],
         });
       }
    
       async validate(accessToken: string, refreshToken: string, profile: any, done: VerifyCallback): Promise<any> {
         const { id, emails, displayName } = profile;
         const email = emails && emails[0]?.value;
         // Déléguer à AuthService pour trouver ou créer l'utilisateur local
         const user = await this.authService.validateOAuthLogin('google', id, email, displayName);
         done(null, user);
       }
     }
    ```
    
    Dans `AuthService` :
    
    ```
     // src/auth/auth.service.ts (ajouter la méthode)
     async validateOAuthLogin(provider: string, providerId: string, email: string, name?: string) {
       // Trouver l'utilisateur existant par provider+providerId ou email
       let user = await this.usersService.findByProvider(provider, providerId);
       if (!user) {
         // Optionnel : vérifier par email ; si existe, lier les comptes ; sinon créer un nouveau
         user = await this.usersService.createOAuthUser({ provider, providerId, email, name });
       }
       // Émettre un JWT ou renvoyer l'objet utilisateur ; ici nous renvoyons le payload minimal pour la connexion
       return user;
     }
    ```
    
4.  **Points de terminaison AuthController**
    
    ```
     // src/auth/auth.controller.ts
     import { Controller, Get, Req, UseGuards } from '@nestjs/common';
     import { AuthGuard } from '@nestjs/passport';
     import { AuthService } from './auth.service';
    
     @Controller('auth')
     export class AuthController {
       constructor(private readonly authService: AuthService) {}
    
       @Get('google')
       @UseGuards(AuthGuard('google'))
       async googleAuth(@Req() req) {
         // Initie le flux Google OAuth2
       }
    
       @Get('google/callback')
       @UseGuards(AuthGuard('google'))
       async googleAuthRedirect(@Req() req) {
         // Google redirige ici après consentement ; req.user défini par GoogleStrategy.validate
         const user = req.user;
         // Émettre un JWT ou définir un cookie, puis rediriger ou renvoyer le jeton
         const jwt = await this.authService.login(user);
         // Ex : rediriger avec le jeton en tant que query, ou définir un cookie :
         // res.redirect(`http://frontend-app.com?token=${jwt.access_token}`);
         return { access_token: jwt.access_token };
       }
     }
    ```
    
    -   Le premier point de terminaison (`/auth/google`) déclenche la redirection vers Google.
        
    -   Le point de terminaison de rappel (callback) gère la réponse, puis émet votre JWT.
        
5.  **Session vs Stateless**
    
    -   De nombreux exemples utilisent des sessions et le support de session de `@nestjs/passport`, mais pour les API, vous ignorez souvent les sessions : Passport invoque toujours `validate`, renvoie l'utilisateur, et vous émettez le JWT immédiatement.
        
    -   Assurez-vous de désactiver les sessions dans l'enregistrement de `PassportModule` : `PassportModule.register({ session: false })`.
        
6.  **Fournisseurs multiples**
    
    -   Répétez la configuration de la stratégie pour chaque fournisseur (par exemple `GitHubStrategy`).
        
    -   Dans `validateOAuthLogin`, gérez le paramètre `provider` pour distinguer la logique.
        
    -   Vous pouvez stocker dans votre entité utilisateur des champs comme `googleId`, `githubId`, etc., ou une table séparée pour les comptes OAuth.
        
7.  **Protéger les routes après connexion**
    
    -   Les clients utilisent le JWT émis dans `Authorization: Bearer <token>` pour accéder aux points de terminaison protégés via `JwtAuthGuard`.
        
    -   Si vous préférez les sessions/cookies, configurez Nest pour utiliser les sessions et les fonctionnalités de session de Passport, mais pour les SPA ou les clients mobiles, le JWT est courant.
        
8.  **Considérations frontend**
    
    -   Les URI de redirection doivent correspondre à celles configurées dans la console du fournisseur OAuth.
        
    -   Après avoir reçu le JWT, stockez-le de manière sécurisée (par exemple, cookie HTTP-only ou stockage sécurisé côté client).
        
    -   Gérer l'expiration des jetons : combinez éventuellement les jetons de rafraîchissement OAuth ou votre propre flux de jetons de rafraîchissement.
        

Avec les stratégies JWT et OAuth2 configurées, votre backend NestJS peut supporter des points de terminaison sécurisés, des flux d'inscription/connexion et des connexions sociales.

## Conclusion et ressources complémentaires

### Résumé

Nous avons parcouru les aspects clés de la construction d'une application NestJS : ses modèles architecturaux, ses blocs de construction fondamentaux (modules, contrôleurs, providers), l'injection de dépendances, le routage et le middleware, le cycle de vie des requêtes avec les pipes, les guards, les filtres d'exception, les intercepteurs, les options d'intégration de base de données (TypeORM, Mongoose, Prisma), la gestion de la configuration et les stratégies d'authentification (JWT, OAuth2).

NestJS fournit un framework structuré, axé sur TypeScript, qui accélère le développement de backends évolutifs et maintenables. En exploitant son système de modules et ses intégrations intégrées, vous bénéficiez dès le départ de la cohérence, de la testabilité et d'une séparation claire des préoccupations.

Que vous choisissiez une base de données relationnelle via TypeORM, un magasin de documents avec Mongoose ou le client typé de Prisma, vous pouvez les brancher dans le conteneur DI de Nest et le module de configuration. Les flux d'authentification – basés sur JWT ou via connexion sociale – s'intègrent naturellement grâce à l'intégration Passport de Nest.

Dans l'ensemble, NestJS est particulièrement adapté aux API, aux microservices, aux applications en temps réel et aux backends d'entreprise où la maintenabilité et l'expérience développeur sont primordiales.

### Documentation officielle et liens communautaires

-   **Documentation officielle de NestJS** : Guide complet et référence API pour toutes les fonctionnalités de base.
    
    -   https://docs.nestjs.com
-   **Dépôt GitHub** : Code source, suivi des problèmes et contributions de la communauté.
    
    -   [https://github.com/nestjs/nest][46]

[1]: #heading-1-qu-est-ce-que-nestjs
[2]: #heading-1-1-histoire-et-philosophie
[3]: #heading-2-pourquoi-choisir-nestjs
[4]: #heading-2-1-avantages-et-cas-d-utilisation
[5]: #heading-2-2-comparaison-avec-d-autres-frameworks
[6]: #heading-3-prise-en-main
[7]: #heading-3-1-installation-de-la-cli
[8]: #heading-3-2-creer-votre-premier-projet
[9]: #heading-3-3-apercu-de-la-structure-du-projet
[10]: #heading-4-les-blocs-de-construction-fondamentaux-de-nestjs
[11]: #heading-4-1-modules
[12]: #heading-4-2-controleurs
[13]: #heading-4-3-providers-services
[14]: #heading-5-injection-de-dependances
[15]: #heading-5-1-comment-fonctionne-l-injection-de-dependances-dans-nestjs
[16]: #heading-5-2-providers-personnalises-et-factory-providers
[17]: #heading-6-routage-et-middleware
[18]: #heading-6-1-definir-des-routes
[19]: #heading-6-2-appliquer-des-middlewares
[20]: #heading-7-cycle-de-vie-des-requetes-et-pipes
[21]: #heading-7-1-que-sont-les-pipes
[22]: #heading-7-2-pipes-integres-vs-personnalises
[23]: #heading-8-guards-et-autorisation
[24]: #heading-8-1-implementer-des-guards
[25]: #heading-8-2-controle-d-acces-base-sur-les-roles-rbac
[26]: #heading-9-filtres-d-exception
[27]: #heading-9-1-gerer-les-erreurs-avec-elegance
[28]: #heading-9-2-creer-des-filtres-personnalises
[29]: #heading-10-intercepteurs-et-journalisation-logging
[30]: #heading-10-1-transformer-les-reponses
[31]: #heading-10-2-journalisation-et-metriques-de-performance
[32]: #heading-11-integration-de-bases-de-donnees
[33]: #heading-11-1-typeorm-avec-nestjs
[34]: #heading-11-2-mongoose-mongodb
[35]: #heading-11-3-prisma
[36]: #heading-12-gestion-de-la-configuration
[37]: #heading-12-1-module-nestjsconfig
[38]: #heading-12-2-variables-d-environnement
[39]: #heading-13-authentification
[40]: #heading-13-1-strategie-jwt
[41]: #heading-13-2-oauth2-connexion-via-reseaux-sociaux
[42]: #heading-14-conclusion-et-ressources-complementaires
[43]: #heading-resume
[44]: #heading-documentation-officielle-et-liens-communautaires
[45]: http://localhost:3000
[46]: https://github.com/nestjs/nest