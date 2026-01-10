---
title: Comment construire une API RESTful avec AdonisJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-29T20:37:35.000Z'
originalURL: https://freecodecamp.org/news/build-a-restful-api-with-adonisjs
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-sevenstorm-juhaszimrus-443383.jpg
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: REST API
  slug: rest-api
seo_title: Comment construire une API RESTful avec AdonisJS
seo_desc: 'By Solomon Eseme

  As a developer, it''s important to understand how APIs work. APIs have helped bridged
  the gap between the frontend and backend. They also let you separate parts of large
  codebases and take advantage of a microservices architecture.

  Th...'
---

Par Solomon Eseme

En tant que développeur, il est important de comprendre comment fonctionnent les API. Les API ont aidé à combler le fossé entre le frontend et le backend. Elles permettent également de séparer des parties de grandes bases de code et de tirer parti d'une architecture de microservices.

Cette séparation des préoccupations fait de l'apprentissage et de la construction d'API RESTful une compétence très demandée pour tout ingénieur logiciel, en particulier les développeurs backend.

Dans ce tutoriel, nous allons explorer les détails de la construction d'API RESTful avec AdonisJS 5. Vous apprendrez comment construire correctement le processus d'authentification et d'autorisation dans le framework AdonisJS 5.

AdonisJS est le Laravel de JavaScript et c'est une compétence très demandée. Donc, apprendre à construire votre première API REST avec lui sera un changement de jeu. 

Vous pouvez lire le [Guide ultime d'AdonisJS 5](https://masteringbackend.com/posts/adonisjs-tutorial-the-ultimate-guide) pour en apprendre davantage à ce sujet.

# Ce que vous allez apprendre :

1. Comment configurer AdonisJS
2. Comment créer la base de données
3. Comment configurer l'autorisation et l'authentification
4. Comment créer le modèle Todo
5. Comment créer le contrôleur Todo
6. Comment créer les routes de points de terminaison
7. Comment tester l'API Todo
8. Conclusion

# Comment configurer AdonisJS 5

La configuration d'AdonisJS est devenue plus facile à mesure que le framework a gagné en popularité ces derniers temps.

Si vous travaillez déjà avec des frameworks JavaScript, vous devriez avoir Node.js installé. Si ce n'est pas le cas, vous pouvez installer la dernière version de Node.js à partir de la [documentation officielle](https://nodejs.org/en/).

Assurez-vous d'installer la version requise de Node.js qui installera également la bonne version de NPM. AdonisJS 5 nécessite Node.js version 12 et NPM version 6 et supérieure.

Si vous avez installé et configuré Node.js et NPM correctement sur votre machine locale en suivant les étapes de la documentation, vous pouvez créer un nouveau projet AdonisJS 5 en exécutant cette commande :

```bash
npm init adonis-ts-app@latest adonisjs-test-app
```

La commande demandera la structure du projet. Sélectionnez simplement API Server et continuez avec les autres options par défaut comme indiqué ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/api_select.png)
_Capture d'écran montrant l'option API à sélectionner_

Enfin, après l'installation réussie, ouvrez le dossier avec n'importe quel éditeur de texte et exécutez la commande suivante pour démarrer et inspecter le projet pour les nouveaux changements :

```bash
cd <NOM_DU_PROJET>

node ace serve --watch
```

Si tout est réussi sans erreurs, ouvrez votre navigateur avec l'URL générée. Voici une capture d'écran de la page d'accueil.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/adonisjs.png)
_Capture d'écran de la page de prévisualisation de l'API AdonisJS_

# Comment créer la base de données

Maintenant que nous avons installé Adonis avec succès, passons à la construction d'une API d'application Todo pour apprendre les détails de la création d'une API RESTful avec AdonisJS.

Nous commencerons par créer et alimenter la base de données avec des schémas et structures de base de données appropriés qui représenteront le stockage des données de l'application Todo.

Tout d'abord, nous devons créer une nouvelle base de données MySQL. Vous pouvez utiliser l'un de ces clients de base de données pour créer et gérer votre base de données.

Ensuite, nous installerons et configurerons AdonisJS Lucid. C'est un ORM puissant pour AdonisJS que vous utilisez pour accéder et manipuler des bases de données sans écrire une seule requête SQL.

Installons Lucid en utilisant cette commande :

```bash
npm install @adonisjs/lucid
```

Pour configurer le package nouvellement installé avec le projet et la base de données nouvellement créée, exécutez cette commande :

```bash
node ace invoke @adonisjs/lucid
```

La commande présentera différentes options de base de données. Sélectionnez MySQL/MariaDB, et enfin, sélectionnez `In the Terminal` pour les instructions. 

Lisez les instructions et mettez à jour votre fichier `.env` en conséquence avec les bonnes informations d'identification de la base de données comme indiqué ci-dessous :

```bash
DB_CONNECTION=mysql
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER= //UTILISATEUR_DB
MYSQL_PASSWORD= //MOT_DE_PASSE_DB
MYSQL_DB_NAME= //NOM_DB
```

Si vous rencontrez cette erreur — `Client does not support authentication protocol requested by server;` — lors du test de votre API Todo, suivez ces étapes pour la résoudre :

```bash
npm install mysql2
```

Ouvrez le fichier `config/database.ts` et mettez à jour le champ `client` en `mysql2`. Cela devrait corriger le bug et vous serez prêt pour le développement et les tests.

AdonisJS 5 rend le développement d'API RESTful très facile. Avec un seul package, vous pouvez configurer un flux complet d'authentification et d'autorisation. 

Dans la section suivante, nous allons couvrir comment protéger notre API avec l'authentification et l'autorisation.

# Comment configurer l'autorisation et l'authentification

Pour configurer l'authentification et l'autorisation, installez le package Auth d'AdonisJS et configurez votre processus d'authentification et d'autorisation.

Vous pouvez installer le package Auth en utilisant la commande suivante :

```
npm install @adonisjs/auth@alpha
```

Ensuite, appelez la commande `invoke` pour configurer le package Auth nouvellement installé en utilisant la commande suivante :

```
node ace invoke @adonisjs/auth
```

Lorsque vous appelez la commande invoke, elle vous guidera à travers un processus de configuration pour le package Auth. Suivez les étapes ci-dessous pour configurer le processus d'authentification par jeton API pour l'application Todo :

1. Choisissez `Lucid` et `API Token` puisque nous construisons des API.
2. Tapez `User` comme modèle pour votre authentification.
3. Appuyez sur `Y` pour créer une nouvelle migration d'utilisateur.
4. Choisissez `Database` comme fournisseur.
5. Appuyez sur `Y` pour créer une migration `api_token`.

Après avoir suivi les étapes avec succès, vous devriez avoir 2 migrations générées dans votre dossier `database/migrations`. Vous pouvez ouvrir la migration `xxxx_users.ts` pour mettre à jour les informations selon les besoins de votre application.

Voici un exemple de notre migration d'utilisateur pour cette démonstration.

```typescript
import BaseSchema from '@ioc:Adonis/Lucid/Schema'

export default class UsersSchema extends BaseSchema {
  protected tableName = 'users'

  public async up () {
    this.schema.createTable(this.tableName, (table) => {
      table.increments('id').primary()
      table.string('name', 255).notNullable()
      table.string('email', 255).notNullable()
      table.string('password', 180).notNullable()
      table.string('remember_me_token').nullable()
      table.timestamps(true)
    })
  }

  public async down () {
    this.schema.dropTable(this.tableName)
  }
}
```

Enfin, nous allons ajouter le middleware `auth` dans le fichier `start/kernel.ts`. Cela vérifiera toujours chaque requête pour s'assurer qu'elle est correctement authentifiée.

```typescript
Server.middleware.registerNamed({
auth: 'App/Middleware/Auth',
})
```

Après avoir configuré l'authentification et l'autorisation, nous devons créer plus de migrations pour l'application Todo. 

Dans la section suivante, nous créerons plus de migrations et alimenterons les données dans l'application Todo pour les tests.

# Comment créer des migrations

Ensuite, nous allons créer les migrations restantes pour le modèle Todo en suivant les étapes décrites ci-dessous.

Pour créer une nouvelle migration, tapez la commande suivante :

```
node ace make:migration todos
```

Après avoir exécuté la commande, ouvrez le nouveau fichier dans `database/migrations/xxxx_todos.ts` et collez le code suivant.

```
import BaseSchema from "@ioc:Adonis/Lucid/Schema";

export default class Todos extends BaseSchema {
	protected tableName = "todos";
    
	public async up() {
        this.schema.createTable(this.tableName, (table) => {
            table.increments("id");
            table.string("title", 255).notNullable();
            table.string("desc", 255).notNullable();
            table.boolean("done").default(false);
            table.timestamps(true);
		});
	}
    
	public async down() {
		this.schema.dropTable(this.tableName);
	}
}
```

Pour l'instant, nous gardons cela simple sans définir de contraintes de base de données. Enfin, nous exécuterons les migrations pour générer et créer les tables de la base de données comme spécifié dans les migrations. Assurez-vous d'arrêter le serveur et de le redémarrer avant d'exécuter la migration :

```
node ace serve --watch
// Puis
node ace migration:run
```

Vous pouvez configurer des seeders de base de données pour générer des données fictives ou [cloner mon dépôt](https://github.com/Kaperskyguru/adonisjs-todo-app) puisque nous avons déjà configuré cela.

# Comment créer le modèle Todo

Pour communiquer avec la base de données, nous devons définir un modèle de base de données en utilisant l'ORM Lucid que nous avons installé précédemment. Cela nous permet de manipuler la base de données sans écrire une seule requête SQL.

Nous créerons différents modèles pour chaque schéma de base de données que nous avons créé. Mais nous n'avons que 2 schémas de base de données qui sont pertinents pour notre application Todo.

Nous utiliserons la commande suivante pour générer les modèles de base de données pour les schémas utilisateurs et todos :

```
node ace make:model User
node ace make:model Todo
```

Après avoir généré les modèles, nous ouvrirons chaque modèle et configurerons les données et les colonnes représentant les colonnes de la base de données, respectivement. Regardons le snippet de code pour le modèle User.

```typescript
import { DateTime } from "luxon";
import Hash from "@ioc:Adonis/Core/Hash";
import {
  column,
  beforeSave,
  BaseModel,
  hasMany,
  HasMany,
} from "@ioc:Adonis/Lucid/Orm";
import Todo from "App/Models/Todo";

export default class User extends BaseModel {
  @column({ isPrimary: true })
  public id: number;

  @column()
  public name: string;

  @column()
  public email: string;

  @column({ serializeAs: null })
  public password: string;

  @column()
  public rememberMeToken?: string;

  @column.dateTime({ autoCreate: true })
  public createdAt: DateTime;

  @column.dateTime({ autoCreate: true, autoUpdate: true })
  public updatedAt: DateTime;

  @hasMany(() => Todo)
  public todos: HasMany<typeof Todo>;

  @beforeSave()
  public static async hashPassword(user: User) {
    if (user.$dirty.password) {
      user.password = await Hash.make(user.password);
    }
  }
}
```

## Revue de code

Passons en revue les détails du code ci-dessus :

### Étape 1 : Importer les packages

Tout d'abord, nous importons les bibliothèques et fichiers requis ci-dessus. Ensuite, nous créons une classe User et mappons chaque colonne de la base de données au modèle User nouvellement créé. Cela nous permet de communiquer avec notre base de données en appelant les colonnes comme propriétés d'objet en utilisant les annotations définies par AdonisJS.

### Étape 2 : La méthode HashPassword

Enfin, nous avons défini les colonnes de la base de données et créé le crochet hashPassword pour qu'il soit appelé automatiquement avant d'enregistrer des données dans la base de données.

```ts
@beforeSave()
    public static async hashPassword(user: User) {
        if (user.$dirty.password) {
        	user.password = await Hash.make(user.password);
        }
    }
```

Maintenant que nous avons créé ces modèles individuels et les avons configurés en conséquence, dans la section suivante, nous créerons des contrôleurs AdonisJS. Ceux-ci interagiront avec les modèles pour créer, récupérer, mettre à jour et supprimer des todos de la base de données.

# Comment créer le contrôleur Todo

Pour manipuler la base de données en utilisant le modèle lorsqu'une requête est envoyée à l'API de l'application Todo, nous créerons un contrôleur pour intercepter chaque requête dirigée vers les Todos. 

Le contrôleur manipulera le Modèle avec la logique métier appropriée et servira la requête avec une réponse appropriée.

## Comment créer le contrôleur Auth

Dans AdonisJS, nous pouvons générer des contrôleurs en utilisant la commande suivante. Tout d'abord, nous générerons le contrôleur Auth pour gérer la logique métier de l'authentification et de l'autorisation.

```
node ace make:controller Auth
```

Ensuite, ouvrez le fichier nouvellement créé dans `app/Controllers/Http/AuthController.ts` et collez le code suivant :

```
import { HttpContextContract } from "@ioc:Adonis/Core/HttpContext";
import User from "App/Models/User";
export default class AuthController {
public async login({ request, auth }: HttpContextContract) {

    const email = request.input("email");
    const password = request.input("password");
    
    const token = await auth.use("api").attempt(email, password, {
        expiresIn: "10 days",
        });
        return token.toJSON();
    }
    
    public async register({ request, auth }: HttpContextContract) {
    
        const email = request.input("email");
        const password = request.input("password");
        const name = request.input("name");
        
        /**
        * Créer un nouvel utilisateur
        */
        
        const user = new User();
        user.email = email;
        user.password = password;
        user.name = name;
        await user.save();
        
        const token = await auth.use("api").login(user, {
        	expiresIn: "10 days",
        });
        
        return token.toJSON();
    }
}
```

## Revue de code

### Étape 1 : Importer les packages

Tout d'abord, nous avons importé les bibliothèques et fichiers requis. Deuxièmement, nous avons créé deux méthodes importantes à l'intérieur de la classe `AuthController`.

```
import { HttpContextContract } from "@ioc:Adonis/Core/HttpContext";
import User from "App/Models/User";
```

### Étape 2 : La méthode Login

La première méthode est la méthode Login qui gère la logique métier pour connecter un utilisateur avec succès en vérifiant si un utilisateur particulier avec l'email et le mot de passe existe dans la base de données.

```
public async login({ request, auth }: HttpContextContract) {

    const email = request.input("email");
    const password = request.input("password");
    
    const token = await auth.use("api").attempt(email, password, {
    	expiresIn: "10 days",
    });
    
    return token.toJSON();
}
```

### Étape 3 : La méthode Register

La deuxième méthode est la méthode Register que nous utilisons pour créer un nouvel utilisateur dans la base de données. Après avoir créé un nouvel utilisateur avec succès, la méthode register connectera automatiquement l'utilisateur.

```
public async register({ request, auth }: HttpContextContract) {

const email = request.input("email");
const password = request.input("password");
const name = request.input("name");

/**
* Créer un nouvel utilisateur
*/

const user = new User();
user.email = email;
user.password = password;
user.name = name;
await user.save();

const token = await auth.use("api").login(user, {
	expiresIn: "10 days",
});

return token.toJSON();
}
```

### Comment créer le contrôleur Todo

Ensuite, nous créerons le contrôleur Todo pour gérer la logique métier de l'application Todo. Tapez la commande suivante pour créer un `TodoController` :

```
node ace make:controller Todo
```

Ensuite, ouvrez le fichier `TodosController.ts` à l'intérieur du dossier `app/Controllers/Http` et ajoutez le code suivant :

```
import { HttpContextContract } from "@ioc:Adonis/Core/HttpContext";
import Todo from "App/Models/Todo";

export default class TodosController {

    public async index({ request}: HttpContextContract)
    {
    const todos = await Todo.query();
    return todos
    }
    
    public async show({ request, params}: HttpContextContract)
    {
        try {
            const todo = await Todo.find(params.id);
            if(todo){
            return todo
        }
        } catch (error) {
        	console.log(error)
        }
    }
    
    public async update({ auth, request, params}: HttpContextContract)
    {
        const todo = await Todo.find(params.id);
        if (todo) {
            todo.title = request.input('title');
            todo.content = request.input('desc');
            todo.done = request.input('done')
            
            if (await todo.save()) {
            	return todo
        	}
        	return; // 422
        }
        return; // 401
    }
    
    public async store({ auth request, response}: HttpContextContract)
    {
        const user = await auth.authenticate();
        const todo = new Todo();
        todo.title = request.input('title');
        todo.desc = request.input('desc');
        await todo.save(todo)
        return todo
    }
    
    public async destroy({response, auth, request, params}: HttpContextContract)
    {
        const user = await auth.authenticate();
        const todo = await Todo.query().where('id', params.id).delete();
        return response.json({message:"Supprimé avec succès"})
    }
}
```

## Revue de code

Passons en revue les détails du code.

### Étape 1 : Importer les packages

Tout d'abord, nous avons importé les bibliothèques et fichiers requis et créé la classe `TodosController`. Ensuite, nous avons créé 5 méthodes différentes à l'intérieur de la classe qui correspondent aux opérations CRUD (Create, Read, Update, Delete). Ces méthodes, que nous discuterons ensuite, sont `index`, `show`, `update`, `store` et `destroy`.

### Étape 2 : La méthode Index

La première méthode est la méthode `index` qui retourne toutes les listes de todos créées par l'utilisateur. Vous pouvez également configurer la méthode index pour utiliser la pagination si la liste de todos est trop grande pour être retournée en une seule fois.

```
public async index({ request}: HttpContextContract)
{
    const todos = await Todo.query();
    return todos
}
```

### Étape 3 : La méthode Show

La deuxième méthode est la méthode `show` que vous utilisez pour récupérer une seule liste de todos en fournissant l'ID du Todo dans la requête.

```
public async show({ request, params}: HttpContextContract)
{
    try {
    	const todo = await Todo.find(params.id);
        if(todo){
        	return todo
        }
    } catch (error) {
    	console.log(error)
    }
}
```

### Étape 4 : La méthode Update

La troisième méthode est la méthode `update` que vous utilisez pour mettre à jour la valeur de chaque colonne dans le schéma Todo. Comme le suggère le nom, vous pouvez changer n'importe quelle colonne spécifique dans la base de données en passant les nouvelles données dans la requête.

```
public async update({ auth, request, params}: HttpContextContract)
{
    const todo = await Todo.find(params.id);
    if (todo) {
        todo.title = request.input('title');
        todo.content = request.input('desc');
        todo.done = request.input('done')
        if (await todo.save()) {
        return todo
    }
    return; // 422
    }
    return; // 401
}
```

### Étape 5 : La méthode Store

La quatrième méthode est la méthode `store` que vous utilisez pour créer un nouveau Todo dans la base de données. En appelant la méthode et en fournissant les informations requises, un nouveau Todo sera créé.

```
public async store({ auth request, response}: HttpContextContract)
{
    const user = await auth.authenticate();
    const todo = new Todo();
    todo.title = request.input('title');
    todo.desc = request.input('desc');
    await todo.save(todo)
    return todo
}
```

### Étape 6 : La méthode Destroy

Enfin, la cinquième méthode est la méthode `destroy`. Vous utilisez cette méthode pour supprimer un seul Todo de la base de données. Elle nécessite l'ID du Todo pour la suppression.

```
public async destroy({response, auth, request, params}: HttpContextContract)
{
    const user = await auth.authenticate();
    const todo = await Todo.query().where('id', params.id).delete();
    return response.json({message:"Supprimé avec succès"})
}
```

Jusqu'à présent, nous avons créé la logique métier de l'API Todo à l'intérieur du contrôleur et utilisé le modèle pour manipuler la base de données. Vous pouvez cloner le dépôt à ce stade pour mieux comprendre ou suivre le tutoriel. 

Dans la section suivante, nous créerons tous les points de terminaison que l'application frontend utilisera pour accéder au contrôleur.

# Comment créer les routes de points de terminaison

Pour exposer notre logique métier au frontend ou aux utilisateurs, nous devons créer différents points de terminaison pour accéder aux différentes méthodes du `TodosController`. 

Pour ce faire, ouvrez le fichier `route.ts` à l'intérieur du dossier `start` et ajoutez le code suivant :

```
//......

Route.group(() => {

    Route.post("register", "AuthController.register");
    Route.post("login", "AuthController.login");
    
        Route.group(() => {
        Route.get("todos", "TodosController.index");
        Route.get("todos/:id", "TodosController.show");
        Route.put("todos/update", "TodosController.update");
        Route.post("todos", "TodosController.store");
        }).middleware("auth:api");
        
}).prefix("api");

//......
```

Maintenant que nous avons créé différents points de terminaison pour notre API Todo, redémarrons le serveur et testons l'API Todo.

# Comment tester l'API Todo

Lorsque vous testez votre point de terminaison en utilisant n'importe quel client HTTP (comme [Postman](https://www.postman.com/)), si vous rencontrez une erreur disant `Cannot find module 'phc-argon2'`, exécutez simplement la commande suivante pour installer le package :

```
npm install phc-argon2
```

Tout d'abord, testons le point de terminaison de l'API Todo sans authentification et voyons l'erreur qu'il générera car nous n'avons pas activé le package Auth.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/unnamed--2-.png)
_Capture d'écran du test de l'API sans authentification_

Mais si nous nous connectons en utilisant le point de terminaison `/api/login` ou nous inscrivons en utilisant le point de terminaison `/api/register` pour récupérer notre jeton API, nous obtenons ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/unnamed--3-.png)
_Capture d'écran de la réponse avec le jeton après une connexion réussie_

Maintenant, nous pouvons accéder aux points de terminaison protégés après avoir inséré le jeton comme valeur d'en-tête d'autorisation du client HTTP.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/unnamed--4-.png)
_Capture d'écran de l'ajout du jeton API pour l'authentification_

Maintenant, nous pouvons accéder à nos points de terminaison protégés :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/giphy.gif)
_Capture d'écran de l'aperçu réussi de l'API_

Si tout fonctionne correctement, félicitations ! Vous avez créé avec succès votre première API RESTful avec AdonisJS 5.

# Conclusion

Dans ce tutoriel, vous avez appris comment construire des API RESTful avec AdonisJS 5, et comment construire correctement le processus d'authentification et d'autorisation dans le framework AdonisJS 5.

Nous avons discuté de différents concepts, de la création de bases de données, de migrations et de modèles, à la création de contrôleurs et de points de terminaison pour accéder à l'API Todo.

Faites-moi savoir ce que vous construisez - j'adorerais le savoir ! Vous pouvez également me suivre sur [Twitter](https://twitter.com/kaperskyguru), [LinkedIn](https://www.linkedin.com/in/solomoneseme/), et [mon blog](https://masteringbackend.com?source=freecodecamp).