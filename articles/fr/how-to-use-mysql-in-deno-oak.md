---
title: Comment utiliser MySQL avec Deno et Oak
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-07T16:40:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-mysql-in-deno-oak
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a78740569d1a4ca25d2.jpg
tags:
- name: Deno
  slug: deno
- name: MySQL
  slug: mysql
- name: Tutorial
  slug: tutorial
seo_title: Comment utiliser MySQL avec Deno et Oak
seo_desc: "By Adeel Imran\nI recently wrote about how to make a Todo API in Deno +\
  \ Oak (without using a database). You can find the repo under chapter_1:oak on GitHub.\
  \ \nThis tutorial picks up where the other left off, and I'll go over how to integrate\
  \ MySQL into..."
---

Par Adeel Imran

J'ai récemment écrit un article sur la création d'une **[API Todo dans Deno + Oak (sans utiliser de base de données)](https://www.freecodecamp.org/news/create-a-todo-api-in-deno-written-by-a-guy-coming-from-node/)**. Vous pouvez trouver le dépôt sous **[chapter_1:oak](https://github.com/adeelibr/deno-playground/tree/master/chapter_1:oak)** sur GitHub. 

Ce tutoriel reprend là où l'autre s'est arrêté, et je vais expliquer comment intégrer MySQL dans un projet Deno et Oak.

Si à un moment donné vous souhaitez voir l'intégralité du code source utilisé dans ce tutoriel, il est disponible à l'adresse [**chapter_2:mysql**](https://github.com/adeelibr/deno-playground/tree/master/chapter_2:mysql). N'hésitez pas à lui donner une étoile sur GitHub si vous l'aimez.

Je suppose que vous avez déjà terminé le dernier tutoriel mentionné ci-dessus. Si ce n'est pas le cas, consultez-le [ici](https://www.freecodecamp.org/news/create-a-todo-api-in-deno-written-by-a-guy-coming-from-node/) et revenez lorsque vous aurez terminé.

Avant de commencer, assurez-vous d'avoir un client MySQL installé et en cours d'exécution :

* Serveur communautaire MySQL [[Télécharger ici](https://dev.mysql.com/downloads/mysql/)]
* MySQL Workbench [[Télécharger ici](https://dev.mysql.com/downloads/workbench/)]

J'ai écrit un petit guide pour les utilisateurs de Mac OS sur la configuration de MySQL car j'ai également eu des difficultés avec cela. Consultez-le [ici](https://github.com/adeelibr/deno-playground/blob/master/guidelines/setting-up-mysql-mac-os-catalina.md).

Si vous êtes sur une machine Windows, vous pouvez utiliser les mêmes outils ou vous pouvez également utiliser [XAMPP](https://www.apachefriends.org/index.html) pour avoir une instance MySQL en cours d'exécution dans votre tableau de bord.

Une fois que vous avez une instance MySQL en cours d'exécution, nous pouvons commencer notre tutoriel.

## Commençons

En supposant que vous venez de cet article, [**Todo API in Deno + Oak (without using a database)**](https://www.freecodecamp.org/news/create-a-todo-api-in-deno-written-by-a-guy-coming-from-node/), nous allons faire ce qui suit :

* Créer une connexion à une base de données MySQL
* Écrire un petit script qui réinitialise la base de données chaque fois que nous démarrons notre serveur Deno
* Effectuer des opérations CRUD sur une table
* Ajouter la fonctionnalité CRUD à nos contrôleurs d'API

Une dernière chose – voici l'intégralité de la différence de commit qui a été faite dans le chapitre 1 pour ajouter MySQL au projet ([code source montrant les nouvelles additions faites à partir du chapitre 1](https://github.com/adeelibr/deno-playground/pull/1/commits/5b63b51ebcadededcfec452fe6877a0bd0f1f83f)).

Dans le dossier racine de votre projet – le mien s'appelle _`chapter_2:mysql`_, bien que le vôtre puisse s'appeler comme vous le souhaitez – créez un dossier appelé **db**. À l'intérieur de ce dossier, créez un fichier appelé **config.ts** et ajoutez le contenu suivant :

```db/config.ts
export const DATABASE: string = "deno";
export const TABLE = {
  TODO: "todo",
};

```

Rien de compliqué ici, nous définissons simplement le nom de notre base de données ainsi qu'un objet pour les tables, puis nous l'exportons. Notre projet aura une base de données appelée "deno" et à l'intérieur de cette base de données, nous n'aurons qu'une seule table appelée "todo".

Ensuite, à l'intérieur du dossier **db**, créez un autre fichier appelé **client.ts** et ajoutez le contenu suivant :

```db/client.ts
import { Client } from "https://deno.land/x/mysql/mod.ts";
// config
import { DATABASE, TABLE } from "./config.ts";

const client = await new Client();

client.connect({
  hostname: "127.0.0.1",
  username: "root",
  password: "",
  db: "",
});

export default client;

```

Plusieurs choses se passent ici. 

Nous importons `Client` de la bibliothèque `mysql`. `Client` nous aidera à nous connecter à notre base de données et à effectuer des opérations dans la base de données.

```db/client.ts
client.connect({
  hostname: "127.0.0.1",
  username: "root",
  password: "",
  db: "",
});
```

`Client` fournit une méthode appelée `connect` qui prend un objet où nous pouvons fournir le `hostname`, `username`, `password`, et `db`. Avec ces informations, il peut établir une connexion à notre instance MySQL.

Assurez-vous que votre `username` n'a pas de `password`, car cela entrera en conflit avec la connexion à la bibliothèque MySQL de Deno. Si vous ne savez pas comment faire cela, [lisez ce tutoriel](https://github.com/adeelibr/deno-playground/blob/master/guidelines/setting-up-mysql-mac-os-catalina.md#set-your-mysql-password-to-empty) que j'ai écrit.

J'ai laissé le champ `database` vide ici car je veux le sélectionner manuellement plus tard dans mon script.

Ajoutons un script qui initialisera une base de données appelée "deno", la sélectionnera, et à l'intérieur de cette base de données, créera une table appelée "todo".

À l'intérieur du fichier `db/client.ts`, ajoutons quelques nouvelles additions :

```db/client.ts
import { Client } from "https://deno.land/x/mysql/mod.ts";
// config
import { DATABASE, TABLE } from "./config.ts";

const client = await new Client();

client.connect({
  hostname: "127.0.0.1",
  username: "root",
  password: "",
  db: "",
});

const run = async () => {
  // create database (if not created before)
  await client.execute(`CREATE DATABASE IF NOT EXISTS ${DATABASE}`);
  // select db
  await client.execute(`USE ${DATABASE}`);

  // delete table if it exists before
  await client.execute(`DROP TABLE IF EXISTS ${TABLE.TODO}`);
  // create table
  await client.execute(`
    CREATE TABLE ${TABLE.TODO} (
        id int(11) NOT NULL AUTO_INCREMENT,
        todo varchar(100) NOT NULL,
        isCompleted boolean NOT NULL default false,
        PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  `);
};

run();

export default client;

```

Ici, nous importons `DATABASE` et `TABLE` de notre fichier de configuration, puis nous utilisons ces valeurs dans une nouvelle fonction appelée `run()`.

Décomposons cette fonction `run()`. J'ai ajouté des commentaires dans le fichier pour vous aider à comprendre le flux de travail :

```db/client.ts
const run = async () => {
  // create database (if not created before)
  await client.execute(`CREATE DATABASE IF NOT EXISTS ${DATABASE}`);
  // select db
  await client.execute(`USE ${DATABASE}`);

  // delete table if it exists before
  await client.execute(`DROP TABLE IF EXISTS ${TABLE.TODO}`);
  // create table
  await client.execute(`
    CREATE TABLE ${TABLE.TODO} (
        id int(11) NOT NULL AUTO_INCREMENT,
        todo varchar(100) NOT NULL,
        isCompleted boolean NOT NULL default false,
        PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
  `);
};

run();
```

* Créer une base de données appelée `deno`. Si elle existe déjà, ne rien faire.
* Ensuite, sélectionner la base de données à utiliser, qui s'appelle `deno`
* Supprimer la table à l'intérieur de `deno` appelée `todo` si elle existe déjà. 
* Ensuite, créer une nouvelle table à l'intérieur de la base de données `deno`, l'appeler `todo`, et définir sa structure : elle aura un `id` unique auto-incrémenté qui sera un entier, un autre champ appelé `todo` qui sera une chaîne de caractères, et enfin un champ appelé `isCompleted` qui est un booléen. J'ai également défini `id` comme ma clé primaire.

La raison pour laquelle j'ai écrit ce script est que je ne veux pas avoir d'informations supplémentaires dans l'instance MySQL. Chaque fois que le script s'exécute, il réinitialise simplement tout.

Vous n'êtes pas obligé d'ajouter ce script. Mais si vous ne le faites pas, vous devrez alors créer manuellement une base de données et la table.

De plus, consultez la documentation de la bibliothèque MySQL de Deno sur la [création de base de données](https://deno.land/x/mysql/#create-database) et sur la [création de table](https://deno.land/x/mysql/#create-table).

En revenant à notre agenda, nous venons d'accomplir deux choses sur les quatre mentionnées en haut de l'article :

* Créer une connexion à une base de données MySQL
* Écrire un petit script qui réinitialise la base de données chaque fois que nous démarrons notre serveur Deno

Cela représente déjà 50 % du tutoriel. Malheureusement, nous ne pouvons pas voir grand-chose se passer pour le moment. Ajoutons rapidement quelques fonctionnalités pour voir cela fonctionner.

## Effectuer des opérations CRUD sur une table et ajouter la fonctionnalité à nos contrôleurs d'API

Nous devons d'abord mettre à jour notre interface Todo. Allez dans le fichier `interfaces/Todo.ts` et ajoutez ce qui suit :

```interfaces/todo.ts
export default interface Todo {
  id?: number,
  todo?: string,
  isCompleted?: boolean,
}

```

Ce que fait ce `?`, c'est qu'il rend la clé dans l'objet optionnelle. Je l'ai fait parce que plus tard, j'utiliserai différentes fonctions pour passer des objets avec seulement un `id`, `todo`, `isCompleted`, ou tous à la fois.

Si vous souhaitez en savoir plus sur les propriétés optionnelles dans TypeScript, consultez leur documentation [ici](https://www.typescriptlang.org/docs/handbook/interfaces.html#optional-properties).

Ensuite, créez un nouveau dossier appelé **models** et à l'intérieur de ce dossier, créez un fichier appelé **todo.ts**. Ajoutez le contenu suivant au fichier :

```models/todo.ts
import client from "../db/client.ts";
// config
import { TABLE } from "../db/config.ts";
// Interface
import Todo from "../interfaces/Todo.ts";

export default {
  /**
   * Takes in the id params & checks if the todo item exists
   * in the database
   * @param id
   * @returns boolean to tell if an entry of todo exits in table
   */
  doesExistById: async ({ id }: Todo) => {},
  /**
   * Will return all the entries in the todo column
   * @returns array of todos
   */
  getAll: async () => {},
  /**
   * Takes in the id params & returns the todo item found
   * against it.
   * @param id
   * @returns object of todo item
   */
  getById: async ({ id }: Todo) => {},
  /**
   * Adds a new todo item to todo table
   * @param todo
   * @param isCompleted
   */
  add: async (
    { todo, isCompleted }: Todo,
  ) => {},
  /**
   * Updates the content of a single todo item
   * @param id
   * @param todo
   * @param isCompleted
   * @returns integer (count of effect rows)
   */
  updateById: async ({ id, todo, isCompleted }: Todo) => {},
  /**
   * Deletes a todo by ID
   * @param id
   * @returns integer (count of effect rows)
   */
  deleteById: async ({ id }: Todo) => {},
};

```

Pour l'instant, les fonctions sont vides, mais ce n'est pas grave. Nous les remplirons une par une.

Ensuite, allez dans le fichier `controllers/todo.ts` et assurez-vous d'ajouter ce qui suit :

```
// interfaces
import Todo from "../interfaces/Todo.ts";
// models
import TodoModel from "../models/todo.ts";

export default {
  /**
   * @description Get all todos
   * @route GET /todos
   */
  getAllTodos: async ({ response }: { response: any }) => {},
  /**
   * @description Add a new todo
   * @route POST /todos
   */
  createTodo: async (
    { request, response }: { request: any; response: any },
  ) => {},
  /**
   * @description Get todo by id
   * @route GET todos/:id
   */
  getTodoById: async (
    { params, response }: { params: { id: string }; response: any },
  ) => {},
  /**
   * @description Update todo by id
   * @route PUT todos/:id
   */
  updateTodoById: async (
    { params, request, response }: {
      params: { id: string };
      request: any;
      response: any;
    },
  ) => {},
  /**
   * @description Delete todo by id
   * @route DELETE todos/:id
   */
  deleteTodoById: async (
    { params, response }: { params: { id: string }; response: any },
  ) => {},
};

```

Ici, nous avons également des fonctions vides. Commençons à les remplir.

### [Get] toutes les todos API

À l'intérieur de `models/todo.ts`, ajoutez une définition pour une fonction appelée `getAll` :

```models/todo.ts
import client from "../db/client.ts";
// config
import { TABLE } from "../db/config.ts";
// Interface
import Todo from "../interfaces/Todo.ts";

export default {
   /**
   * Will return all the entries in the todo column
   * @returns array of todos
   */
  getAll: async () => {
    return await client.query(`SELECT * FROM ${TABLE.TODO}`);
  },
}
```

Le `Client` expose également une autre méthode à part `connect` (nous avons utilisé une méthode "connect" dans le fichier `db/client.ts`) et c'est `query`. La méthode `client.query` nous permet d'exécuter des requêtes MySQL directement depuis notre code Deno tel quel.

Ensuite, allez dans `controllers/todo.ts` et ajoutez une définition pour `getAllTodos` :

```controllers/todo.ts
// interfaces
import Todo from "../interfaces/Todo.ts";
// models
import TodoModel from "../models/todo.ts";

export default {
  /**
   * @description Get all todos
   * @route GET /todos
   */
  getAllTodos: async ({ response }: { response: any }) => {
    try {
      const data = await TodoModel.getAll();
      response.status = 200;
      response.body = {
        success: true,
        data,
      };
    } catch (error) {
      response.status = 400;
      response.body = {
        success: false,
        message: `Error: ${error}`,
      };
    }
  },
}
```

Tout ce que nous faisons est d'importer `TodoModel` et d'utiliser sa méthode appelée `getAll`, que nous venons de définir. Comme elle retourne une promesse, nous l'avons enveloppée dans async/await. 

La méthode `TodoModel.getAll()` nous retournera un tableau que nous retournons simplement à `response.body` avec `status` défini sur `200`.

Si la promesse échoue ou s'il y a une autre erreur, nous allons simplement dans notre bloc catch et retournons un statut de 400 avec `success` défini sur false. Nous définissons également le `message` sur ce que nous obtenons du bloc catch.

C'est tout, nous avons terminé. Maintenant, lançons notre terminal. 

Assurez-vous que votre instance MySQL est en cours d'exécution. Dans votre terminal, tapez :

```
$ deno run --allow-net server.ts 
```

Votre terminal devrait ressembler à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-04-at-23.29.19.png)
_C'est ainsi que ma console apparaît lorsque je démarre le serveur_

Ma console me dit deux choses ici.

1. Que mon serveur API Deno est en cours d'exécution sur le port 8080
2. Que mon instance MySQL est en cours d'exécution sur `127.0.0.1`, qui est `localhost`

Testons notre API. J'utilise [Postman](https://www.postman.com/) ici, mais vous pouvez utiliser votre client API préféré.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-04-at-23.31.07.png)
_exécution de [GET] localhost:8080/todos => Retournera toutes les todos_

Pour l'instant, il ne retourne que des données vides. Mais une fois que nous aurons ajouté des données à notre table `todo`, il retournera ces todos ici.

Super. Une API de moins et quatre autres à faire.

### [Post] ajouter une todo API

Dans le fichier `models/todo.ts`, ajoutez la définition suivante pour la fonction `add()` :

```
export default {
   /**
   * Adds a new todo item to todo table
   * @param todo
   * @param isCompleted
   */
  add: async (
    { todo, isCompleted }: Todo,
  ) => {
    return await client.query(
      `INSERT INTO ${TABLE.TODO}(todo, isCompleted) values(?, ?)`,
      [
        todo,
        isCompleted,
      ],
    );
  },
}
```

La fonction add prend un objet comme argument, qui contient deux éléments : `todo` et `isCompleted`.

Ainsi, `_add_: _async_ ({ todo, isCompleted }: Todo) => {}` peut également s'écrire `({todo, isCompleted}: {todo:string, isCompleted:boolean})`. Mais puisque nous avons déjà une interface définie dans notre fichier `interfaces/Todo.ts` qui est

```
export default interface Todo {
  id?: number,
  todo?: string,
  isCompleted?: boolean,
}

```

nous pouvons simplement écrire ceci comme `_add_: _async_ ({ todo, isCompleted }: Todo) => {}`. Cela indique à TypeScript que cette fonction a deux arguments, `todo`, qui est une chaîne de caractères, et `isCompleted`, qui est un booléen.

Si vous souhaitez en savoir plus sur les interfaces, TypeScript dispose d'un excellent document à ce sujet que vous pouvez trouver [ici](https://www.typescriptlang.org/docs/handbook/interfaces.html).

À l'intérieur de notre fonction, nous avons ce qui suit :

```
return await client.query(
  `INSERT INTO ${TABLE.TODO}(todo, isCompleted) values(?, ?)`,
  [
    todo,
    isCompleted,
  ],
);
```

Cette requête peut être décomposée en deux parties :

* `INSERT INTO ${TABLE_._TODO}(todo, isCompleted) values(?, ?)`. Les deux points d'interrogation ici désignent une utilisation de variables à l'intérieur de cette requête.
* L'autre partie, `[todo, isCompleted]`, est les variables qui iront dans la _première partie_ de la requête et seront remplacées par `(?, ?)`
* `Table.Todo` est simplement une chaîne de caractères provenant du fichier `db/config.ts` où la valeur `Table.Todo` est "`todo`"

Ensuite, à l'intérieur de notre fichier `controllers/todo.ts`, allez à la définition de la fonction `createTodo()` :

```
export default {
   /**
   * @description Add a new todo
   * @route POST /todos
   */
  createTodo: async (
    { request, response }: { request: any; response: any },
  ) => {
    const body = await request.body();
    if (!request.hasBody) {
      response.status = 400;
      response.body = {
        success: false,
        message: "No data provided",
      };
      return;
    }

    try {
      await TodoModel.add(
        { todo: body.value.todo, isCompleted: false },
      );
      response.body = {
        success: true,
        message: "The record was added successfully",
      };
    } catch (error) {
      response.status = 400;
      response.body = {
        success: false,
        message: `Error: ${error}`,
      };
    }
  },
}
```

Décomposons cela en deux parties :

**Partie 1**

```
const body = await request.body();
if (!request.hasBody) {
  response.status = 400;
  response.body = {
    success: false,
    message: "No data provided",
  };
  return;
}
```

Tout ce que nous faisons ici est de vérifier si l'utilisateur envoie des données dans le corps. Si ce n'est pas le cas, nous retournons un statut `400` et dans le corps, nous retournons `success: false` et `message: <erromessage-string>`.

**Partie 2**

```
try {
  await TodoModel.add(
    { todo: body.value.todo, isCompleted: false },
  );
  response.body = {
    success: true,
    message: "The record was added successfully",
  };
} catch (error) {
  response.status = 400;
  response.body = {
    success: false,
    message: `Error: ${error}`,
  };
}
```

S'il n'y a pas d'erreur, la fonction `TodoModel.add()` est appelée et retourne simplement un statut de `200` et un message de confirmation à l'utilisateur.

Sinon, elle retourne simplement une erreur similaire à celle que nous avons faite dans l'API précédente.

Maintenant, nous avons terminé. Lancez votre terminal et assurez-vous que votre instance MySQL est en cours d'exécution. Dans votre terminal, tapez :

```
$ deno run --allow-net server.ts 
```

Allez sur [Postman](https://www.postman.com/) et exécutez la route de l'API pour ce contrôleur :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-04-at-23.55.02.png)
_exécution de [POST] localhost:8080/todos => Ajoutera un nouvel élément todo_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-04-at-23.57.06.png)
_exécution de [POST] localhost:8080/todos => Retournera toutes les todos, remarquez comment le nouvel élément ajouté est également retourné_

C'est génial, nous avons maintenant deux API fonctionnelles. Il en reste trois autres à faire.

### [GET] todo par id API

Dans votre fichier `models/todo.ts`, ajoutez une définition pour ces deux fonctions, `doesExistById()` et `getById()` :

```
export default {
   /**
   * Takes in the id params & checks if the todo item exists
   * in the database
   * @param id
   * @returns boolean to tell if an entry of todo exits in table
   */
  doesExistById: async ({ id }: Todo) => {
    const [result] = await client.query(
      `SELECT COUNT(*) count FROM ${TABLE.TODO} WHERE id = ? LIMIT 1`,
      [id],
    );
    return result.count > 0;
  },
  /**
   * Takes in the id params & returns the todo item found
   * against it.
   * @param id
   * @returns object of todo item
   */
  getById: async ({ id }: Todo) => {
    return await client.query(
      `SELECT * FROM ${TABLE.TODO} WHERE id = ?`,
      [id],
    );
  },
}
```

Parlons de chaque fonction une par une :

* `doesExistById` prend un `id` et retourne un `boolean` indiquant si une todo particulière existe dans la base de données ou non.

Décomposons cette fonction :

```
const [result] = await client.query(
  `SELECT COUNT(*) count FROM ${TABLE.TODO} WHERE id = ? LIMIT 1`,
  [id],
);
return result.count > 0;
```

Nous vérifions simplement le compte ici dans la table contre un id de todo particulier. Si le compte est supérieur à zéro, nous retournons `true`. Sinon, nous retournons `false`.

* `getById` retourne l'élément todo contre un id particulier :

```
return await client.query(
  `SELECT * FROM ${TABLE.TODO} WHERE id = ?`,
  [id],
);
```

Nous exécutons simplement une requête MySQL ici pour obtenir une todo par id et retournons le résultat tel quel.

Ensuite, allez dans votre fichier `controllers/todo.ts` et ajoutez une définition pour une méthode de contrôleur `getTodoById` :

```
export default {
   /**
   * @description Get todo by id
   * @route GET todos/:id
   */
  getTodoById: async (
    { params, response }: { params: { id: string }; response: any },
  ) => {
    try {
      const isAvailable = await TodoModel.doesExistById(
        { id: Number(params.id) },
      );

      if (!isAvailable) {
        response.status = 404;
        response.body = {
          success: false,
          message: "No todo found",
        };
        return;
      }

      const todo = await TodoModel.getById({ id: Number(params.id) });
      response.status = 200;
      response.body = {
        success: true,
        data: todo,
      };
    } catch (error) {
      response.status = 400;
      response.body = {
        success: false,
        message: `Error: ${error}`,
      };
    }
  },
}
```

Décomposons cela en deux parties plus petites :

```
const isAvailable = await TodoModel.doesExistById(
  { id: Number(params.id) },
);

if (!isAvailable) {
  response.status = 404;
  response.body = {
    success: false,
    message: "No todo found",
  };
  return;
}
```

Tout d'abord, nous vérifions si la todo existe dans la base de données contre un id en utilisant cette méthode :

```
const isAvailable = await TodoModel.doesExistById(
  { id: Number(params.id) },
);
```

Ici, nous devons convertir `params.id` en un `Number` car notre interface todo n'accepte que `id` comme un nombre. Ensuite, nous passons simplement `params.id` à la méthode `doesExistById`. Cette méthode retournera un booléen.

Ensuite, nous vérifions simplement si la todo n'est pas disponible et retournons une méthode `404` avec notre réponse standard comme avec les points de terminaison précédents :

```
if (!isAvailable) {
  response.status = 404;
  response.body = {
    success: false,
    message: "No todo found",
  };
  return;
}
```

Ensuite, nous avons :

```
try {
const todo: Todo = await TodoModel.getById({ id: Number(params.id) });
response.status = 200;
response.body = {
  success: true,
  data: todo,
};
} catch (error) {
response.status = 400;
response.body = {
  success: false,
  message: `Error: ${error}`,
};
```

Cela est similaire à ce que nous faisions dans nos API précédentes. Ici, nous obtenons simplement des données de la base de données, définissons la variable `todo`, puis retournons la réponse. Si une erreur survient, nous retournons simplement un message d'erreur standard dans le bloc catch à l'utilisateur.

Maintenant, lancez votre terminal et assurez-vous que votre instance MySQL est en cours d'exécution. Dans votre terminal, tapez :

```
$ deno run --allow-net server.ts 
```

Allez sur [Postman](https://www.postman.com/) et exécutez la route de l'API pour ce contrôleur.

N'oubliez pas que chaque fois que nous redémarrons notre serveur, nous réinitialisons la base de données. Si vous ne souhaitez pas ce comportement, vous pouvez simplement commenter la fonction `run` dans le fichier `db/client.ts`.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-07-at-17.09.32.png)
_exécution de [POST] localhost:8080/todos => Ajoutera un nouvel élément todo_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-07-at-17.10.13.png)
_exécution de [POST] localhost:8080/todos => Retournera toutes les todos_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-07-at-17.11.03.png)
_exécution de [GET] localhost:8080/todos/:id => retournera la todo pour cet id si trouvé_

![running [GET] localhost:8080/todos/:id => will return the todo for that id if found](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-07-at-17.16.06.png)
_exécution de [GET] localhost:8080/todos/&lt;unknown-id&gt; => retourne le statut 404 avec un message d'erreur non trouvé_

Jusqu'à présent, nous avons fait des API pour :

* Obtenir toutes les todos
* Créer une nouvelle todo
* Obtenir une todo par ID

Et voici les API restantes :

* Mettre à jour une todo par ID
* Supprimer une todo par ID

### [PUT] mettre à jour une todo par id API

Créons d'abord un modèle pour cette API. Allez dans notre fichier `models/todo.ts` et ajoutez une définition pour une fonction `updateById` :

```
**
 * Met à jour le contenu d'un seul élément todo
 * @param id
 * @param todo
 * @param isCompleted
 * @returns integer (nombre de lignes affectées)
 */
updateById: async ({ id, todo, isCompleted }: Todo) => {
  const result = await client.query(
    `UPDATE ${TABLE.TODO} SET todo=?, isCompleted=? WHERE id=?`,
    [
      todo,
      isCompleted,
      id,
    ],
  );
  // retourne le nombre de lignes mises à jour
  return result.affectedRows;
},
```

La fonction `updateById` prend 3 paramètres : `id`, `todo`, et `isCompleted`.

Nous exécutons simplement une requête MySQL à l'intérieur de cette fonction :

```
onst result = await client.query(
  `UPDATE ${TABLE.TODO} SET todo=?, isCompleted=? WHERE id=?`,
  [
    todo,
    isCompleted,
    id,
  ],
);
```

Cela met à jour le `todo` et le `isCompleted` d'un seul élément todo par un `id` spécifique.

Ensuite, nous retournons un compte des lignes mises à jour par cette requête en faisant :

```
  // retourne le nombre de lignes mises à jour
  return result.affectedRows;
```

Le compte sera soit 0 soit 1, mais jamais plus que 1. Cela est dû au fait que nous avons des ID uniques dans notre base de données – plusieurs todos avec le même ID ne peuvent pas exister.

Ensuite, allez dans notre fichier `controllers/todo.ts` et ajoutez une définition pour une fonction `updateTodoById` :

```
updateTodoById: async (
  { params, request, response }: {
    params: { id: string };
    request: any;
    response: any;
  },
) => {
  try {
    const isAvailable = await TodoModel.doesExistById(
      { id: Number(params.id) },
    );
    if (!isAvailable) {
      response.status = 404;
      response.body = {
        success: false,
        message: "No todo found",
      };
      return;
    }

    // si todo trouvé alors mettre à jour todo
    const body = await request.body();
    const updatedRows = await TodoModel.updateById({
      id: Number(params.id),
      ...body.value,
    });
    response.status = 200;
    response.body = {
      success: true,
      message: `Successfully updated ${updatedRows} row(s)`,
    };
  } catch (error) {
    response.status = 400;
    response.body = {
      success: false,
      message: `Error: ${error}`,
    };
  }
},
```

Cela est presque identique à nos API précédentes que nous avons écrites. La partie qui est nouvelle ici est celle-ci :

```
// si todo trouvé alors mettre à jour todo
const body = await request.body();
const updatedRows = await TodoModel.updateById({
  id: Number(params.id),
  ...body.value,
});
```

Nous obtenons simplement le corps que l'utilisateur nous envoie en JSON et passons le corps à notre fonction `TodoModel.updateById`.

Nous devons convertir l'`id` en un nombre pour nous conformer à notre interface Todo.

La requête est exécutée et retourne le nombre de lignes mises à jour. À partir de là, nous le retournons simplement dans notre réponse. Si une erreur survient, elle va dans le bloc catch où nous retournons notre message de réponse standard.

Lançons cela et voyons si cela fonctionne. Assurez-vous que votre instance MySQL est en cours d'exécution et exécutez ce qui suit à partir de votre terminal :

```
$ deno run --allow-net server.ts 
```

Allez sur [Postman](https://www.postman.com/) et exécutez la route de l'API pour ce contrôleur :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-07-at-17.42.02.png)
_exécution de [PUT] localhost:8080/todos/:id => mettra à jour le contenu de cette todo par l'id donné_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-07-at-17.43.13.png)
_exécution de [GET] localhost:8080/todos/ => retournera toutes les todos, voyez comment la todo que vous avez mise à jour est également affichée ici._

### [DELETE] todo par id API

Dans votre fichier `models/todo.ts`, créez une fonction appelée `deleteById` :

```
/**
 * Supprime une todo par ID
 * @param id
 * @returns integer (nombre de lignes affectées)
 */
deleteById: async ({ id }: Todo) => {
  const result = await client.query(
    `DELETE FROM ${TABLE.TODO} WHERE id = ?`,
    [id],
  );
  // retourne le nombre de lignes mises à jour
  return result.affectedRows;
},
```

Ici, nous passons simplement un `id` comme paramètre, puis utilisons la requête MySQL delete. Nous retournons ensuite le compte des lignes mises à jour. Le compte mis à jour sera soit 0 soit 1 car l'ID de chaque todo est unique.

Ensuite, allez dans votre fichier `controllers/todo.ts` et définissez une méthode `deleteByTodoId` :

```
/**
 * @description Supprimer une todo par id
 * @route DELETE todos/:id
 */
deleteTodoById: async (
  { params, response }: { params: { id: string }; response: any },
) => {
  try {
    const updatedRows = await TodoModel.deleteById({
      id: Number(params.id),
    });
    response.status = 200;
    response.body = {
      success: true,
      message: `Successfully updated ${updatedRows} row(s)`,
    };
  } catch (error) {
    response.status = 400;
    response.body = {
      success: false,
      message: `Error: ${error}`,
    };
  }
},
```

Cela est assez simple. Nous passons le `params.id` à notre méthode `TodoModel.deleteById` et retournons le nombre de lignes mises à jour avec cette requête.

Si quelque chose ne va pas, une erreur est lancée dans le bloc catch qui retourne notre réponse d'erreur standard.

Vérifions cela.

Assurez-vous que votre instance MySQL est en cours d'exécution. Dans votre terminal, tapez :

```
$ deno run --allow-net server.ts 
```

Allez sur [Postman](https://www.postman.com/) et exécutez la route de l'API pour ce contrôleur :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-07-at-18.23.04.png)
_exécution de [GET] localhost:8080/todos/ => retournera toutes les todos_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-07-at-18.23.11.png)
_exécution de [DELETE] localhost:8080/todos/:id => supprimera une todo par ID_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-07-at-18.23.44.png)
_exécution de [GET] localhost:8080/todos/ => retournera toutes les todos, voyez comment la todo avec "id" n'est plus ici_

Avec cela, nous avons terminé notre tutoriel Deno + Oak + MySQL.

L'intégralité du code source est disponible ici : [https://github.com/adeelibr/deno-playground](https://github.com/adeelibr/deno-playground). Si vous trouvez un problème, faites-le moi savoir. Ou n'hésitez pas à faire une pull request et je vous créditerai dans le dépôt.

Si vous avez trouvé ce tutoriel utile, veuillez le partager. Et comme toujours, je suis disponible sur [Twitter sous @adeelibr](https://twitter.com/adeelibr). J'adorerais avoir vos commentaires à ce sujet.