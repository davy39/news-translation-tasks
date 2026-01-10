---
title: Comment créer une API Todo dans Deno et Oak
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-29T11:33:00.000Z'
originalURL: https://freecodecamp.org/news/create-a-todo-api-in-deno-written-by-a-guy-coming-from-node
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ab6740569d1a4ca273d.jpg
tags:
- name: '2020'
  slug: '2020'
- name: code
  slug: code
- name: Deno
  slug: deno
- name: JavaScript
  slug: javascript
- name: Middleware
  slug: middleware
- name: REST API
  slug: rest-api
- name: TypeScript
  slug: typescript
seo_title: Comment créer une API Todo dans Deno et Oak
seo_desc: "By Adeel Imran\nI am a JavaScript/Node developer who secretly likes (actually,\
  \ loves and adores) Deno. I have been a huge fan of Deno ever since it was announced\
  \ and I've been wanting to play with it. \nThis tutorial focuses on creating a set\
  \ of REST A..."
---

Par Adeel Imran

Je suis un développeur JavaScript/Node qui aime secrètement (en fait, aime et adore) Deno. Je suis un grand fan de Deno depuis son annonce et j'avais envie de m'amuser avec. 

Ce tutoriel se concentre sur la création d'un ensemble d'API REST pour une application Todo. Gardez à l'esprit que je n'ai pas abordé la base de données ici – je couvrirai cela [dans un autre article](https://www.freecodecamp.org/news/how-to-use-mysql-in-deno-oak/).

À tout moment, si vous vous sentez perdu ou souhaitez vérifier une référence, voici le code source complet de ce tutoriel : **[Chapitre 1 : Oak](https://github.com/adeelibr/deno-playground/tree/master/chapter_1:oak).**

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-171.png)
_Photo par [Unsplash](https://unsplash.com/@bernardtheclerk?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Bernard de Clerk</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

### Ce que nous allons couvrir

* Créer un serveur de base
* Créer 5 API (routes/contrôleur)
* Créer un middleware pour journaliser les requêtes API au fur et à mesure qu'elles sont faites dans la console
* Créer un middleware non trouvé (404) lorsque l'utilisateur tente d'accéder à une API inconnue

### Ce dont nous aurons besoin

* Une version installée de Deno (ne vous inquiétez pas, je vais vous guider)
* Une petite connaissance de Typescript
* Ce serait génial si vous avez déjà travaillé avec Node/Express (ne vous inquiétez pas si ce n'est pas le cas – ce tutoriel est très basique)

## Commençons

Tout d'abord, installons Deno. Je suis sur un ordinateur Mac, donc j'utilise brew. Ouvrez simplement votre terminal et tapez :

```
$ brew install deno
```

Mais si vous utilisez un système d'exploitation différent, rendez-vous sur [**deno.land installation**](https://deno.land/#installation)**.** Ils ont de nombreuses façons d'installer facilement Deno sur votre machine.

Une fois installé, fermez le terminal, ouvrez-en un nouveau et tapez :

```
$ deno --version
```

Cela devrait afficher quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-28-at-22.34.24.png)
_exécution de la commande "deno --version" pour voir quelle version de deno est installée_

Super ! Avec cela, nous avons presque terminé 10 % de ce tutoriel. 

Passons à l'étape suivante et créons l'API backend pour notre application Todo.

### Configuration du projet

Avant de continuer, voici le code source complet de ce tutoriel : **[Chapitre 1 : Oak](https://github.com/adeelibr/deno-playground/tree/master/chapter_1:oak).**

Commençons :

* Créez un nouveau dossier et appelez-le **chapter_1:oak** (mais vous pouvez l'appeler comme vous voulez)
* Une fois le dossier créé, faites simplement un `cd` dans votre nouveau projet. Créez un fichier appelé **server.ts** et écrivez le code suivant :

```server.ts
import { Application } from "https://deno.land/x/oak/mod.ts";

const app = new Application();
const port: number = 8080;

console.log('running on port ', port);
await app.listen({ port });
```

Exécutons ce fichier. Ouvrez votre terminal et dans le dossier racine de votre projet, tapez :

```
$ deno run --allow-net server.ts
```

Je vais parler de ce que fait le drapeau `--allow-net`, mais pour l'instant, suivez-moi ?.

Vous devriez obtenir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-28-at-22.33.28.png)

Ce que nous avons fait jusqu'à présent, c'est créer un serveur qui écoute sur le port 8080. Il ne fait pas grand-chose pour l'instant, à part pouvoir s'exécuter sur le port 8080.

Si vous avez déjà utilisé JavaScript, une chose que vous avez peut-être remarquée est que nous importons les packages d'une manière différente. Nous devons faire quelque chose comme :

```
import { Application } from "https://deno.land/x/oak/mod.ts";

```

Lorsque vous exécutez `deno run ---allow-net <file_name>` dans votre terminal, Deno regardera toutes vos importations et les installera localement sur votre machine si elles ne sont pas déjà présentes. 

La première fois que vous exécutez cela, il ira à cette URL `https://deno.land/x/oak/mod.ts` et installera le package `oak`. Oak est essentiellement un framework Deno pour écrire des API. Il le placera quelque part localement dans votre cache.

Dans la ligne suivante, nous faisons ceci :

```
const app = new Application();

```

Cela crée une nouvelle instance de notre application, et ce sera la base de tout ce que vous ferez dans ce tutoriel. Vous pouvez ajouter des routes à l'instance de l'application, attacher des middlewares comme la journalisation des API, écrire une page 404 non trouvée, et ainsi de suite.

Ensuite, nous écrivons :

```
const port: number = 8080;
// const port = 8080; // => peut aussi s'écrire comme ceci
```

Les deux sont identiques et font la même chose. La seule différence est que l'écriture de `const port: number = 8080` indique à Typescript que la variable `port` est de type number.

Si vous écriviez `const port: number = "8080"`, cela générerait une erreur dans votre terminal, car port est de type `number`. Mais nous essayons de lui assigner une `string` de valeur "8080". 

Si vous souhaitez en savoir plus sur les différents types de types (jeu de mots intentionnel), consultez ce guide très facile et basique sur [**Basic types by Typescript**](https://www.typescriptlang.org/docs/handbook/basic-types.html). Jetez-y un coup d'œil rapide pendant 2-3 minutes et revenez ici.

Et à la fin, nous avons :

```
console.log('running on port ', port);
await app.listen({ port });
```

Nous affichons simplement ici le numéro de port dans la console et demandons à Deno d'écouter le port, qui est 8080.

Il ne fait pas grand-chose pour l'instant. Faisons-lui faire quelque chose de basique, comme afficher un message _JSON_ dans votre navigateur lorsque vous allez sur http:localhost:8080_._

Ajoutez ce qui suit à votre fichier **server.ts** :

```server.ts
import { Application, Router } from "https://deno.land/x/oak/mod.ts";

const app = new Application();
const port: number = 8080;

const router = new Router();
router.get("/", ({ response }: { response: any }) => {
  response.body = {
    message: "hello world",
  };
});
app.use(router.routes());
app.use(router.allowedMethods());

console.log('running on port ', port);
await app.listen({ port });
```

La nouvelle chose ajoutée ici est que nous importons également `Router` avec `Application` depuis `oak` à la ligne 1.

Ensuite, ce que nous faisons est :

```
const router = new Router();
router.get("/", ({ response }: { response: any }) => {
  response.body = {
    message: "hello world",
  };
});
app.use(router.routes());
app.use(router.allowedMethods());
```

Nous créons une nouvelle instance de routeur en faisant `const router = new Router()` puis nous créons une nouvelle route appelée `/` qui est de type `get`.

Décomposons cela :

```
router.get("/", ({ response }: { response: any }) => {
  response.body = {
    message: "hello world",
  };
});
```

`router.get` prend 2 paramètres. Le premier est la route que nous avons définie sur `/` et le second est une fonction. La fonction elle-même prend un argument qui est un objet. Ce que je fais ici est de [déstructurer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) l'objet et d'obtenir seulement `response`.

Ensuite, je fais une vérification de type sur `response` similaire à ce que j'ai fait avec `const port: number = 8080;`. Tout ce que je fais est `{ response }: { response: any }` qui indique à TypeScript ici que le `response` que j'ai déstructuré peut être de type `any`.

`any` vous aide à éviter la vérification de type dans TypeScript. Vous pouvez en lire plus à ce sujet [ici](https://www.typescriptlang.org/docs/handbook/basic-types.html#any).

Ensuite, tout ce que je fais est de prendre cet objet `response` et de définir `response.body.message = "hello world";`.

```
response.body = {
  message: "hello world",
};
```

Dernier point mais non des moindres, nous ajoutons simplement ces deux lignes :

```
app.use(router.routes());
app.use(router.allowedMethods());
```

Cela indique à Deno d'inclure toutes les routes de notre routeur (actuellement nous n'en avons qu'une) et la ligne suivante indique à Deno d'autoriser toutes les méthodes pour cette route(s) comme `GET, POST, PUT, DELETE`.

Et maintenant nous avons terminé. ✅ Exécutons cela et voyons ce que nous avons :

```
$ deno run --allow-net server.ts
```

La propriété `---allow-net` indique à Deno que cette application donne à l'utilisateur la permission d'accéder à son contenu via le port ouvert.

Maintenant, ouvrez votre navigateur préféré et allez sur `http://localhost:8080`. Vous verrez quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-28-at-23.11.08.png)
_Résultat de l'exécution de localhost:8080 sur votre navigateur_

Honêtement, la partie la plus difficile est faite. Conceptuellement, nous en sommes à 60 %.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/images.jpeg)
_Maître Yoda approuve_

Super.

Une dernière chose avant de commencer avec notre API Todo. Remplaçons :

```
console.log('running on port ', port);
await app.listen({ port });
```

par :

```server.ts
app.addEventListener("listen", ({ secure, hostname, port }) => {
  const protocol = secure ? "https://" : "http://";
  const url = `${protocol}${hostname ?? "localhost"}:${port}`;
  console.log(`Listening on: ${port}`);
});

await app.listen({ port });
```

Le code que nous avions avant n'était pas très précis, car nous affichions simplement un message dans la console puis attendions que l'application commence à écouter sur un port.

Avec la version ultérieure, nous attendons que l'application commence à écouter sur `port` et nous pouvons écouter en ajoutant un écouteur d'événements à notre instance `app` avec ce qui suit : `app_.addEventListener_("listen", ({ secure, hostname, port }) => {}`. 

Le premier paramètre est l'événement que nous voulons écouter (qui est `listen` ?) et le second paramètre est un objet que nous déstructurons en `{ secure, hostname, port }`. Secure est un booléen, hostname est une chaîne, et port est un nombre.

Maintenant, lorsque nous démarrons notre application, elle n'affichera le message dans la console que lorsque l'application commence réellement à écouter sur le port.

Nous pouvons aller un peu plus loin et le rendre plus coloré. Ajoutons un nouveau module en haut du fichier dans `server.ts` :

```
import { green, yellow } from "https://deno.land/std@0.53.0/fmt/colors.ts";

```

Et ensuite, à l'intérieur de notre méthode d'écouteur d'événements, nous pouvons remplacer :

```
console.log(`Listening on: ${port}`);

```

par :

```
console.log(`${yellow("Listening on:")} ${green(url)}`);
```

Maintenant, lorsque nous faisons :

```
$ deno run --allow-net server.ts
```

il affichera ceci dans notre console :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-28-at-23.34.29.png)
_Cool, maintenant nous avons une console colorée._

Si vous êtes bloqué quelque part, vous pouvez simplement aller au code source de ce tutoriel [**ici**](https://github.com/adeelibr/deno-playground/tree/master/chapter_1:oak).

Créons maintenant les routes de notre API Todo.

* Créez un nouveau dossier dans votre dossier racine appelé `routes` et à l'intérieur de ce dossier, créez un fichier appelé `todo.ts`
* En même temps, dans votre dossier racine, créez un nouveau dossier appelé `controllers` et à l'intérieur de ce dossier, créez un fichier appelé `todo.ts`

Commençons par le fichier `controllers/todo.ts` :

```controllers/todo.ts
export default {
  getAllTodos: () => {},
  createTodo: async () => {},
  getTodoById: () => {},
  updateTodoById: async () => {},
  deleteTodoById: () => {},
};
```

Nous exportons simplement un objet ici avec quelques fonctions nommées qui sont vides (pour l'instant).

Ensuite, allez dans votre fichier `routes/todo.ts` et tapez ceci :

```routes/todo.ts
import { Router } from "https://deno.land/x/oak/mod.ts";

const router = new Router();
// controller
import todoController from "../controllers/todo.ts";

router
  .get("/todos", todoController.getAllTodos)
  .post("/todos", todoController.createTodo)
  .get("/todos/:id", todoController.getTodoById)
  .put("/todos/:id", todoController.updateTodoById)
  .delete("/todos/:id", todoController.deleteTodoById);

export default router;
```

Cela peut sembler familier aux personnes qui ont travaillé avec Node et Express. 

Tout ce que nous faisons ici est d'importer `Route` depuis `oak` puis de configurer une nouvelle instance de Router en faisant `const router = new Router();`.

Ensuite, nous importons nos contrôleurs en faisant :

```
import todoController from "../controllers/todo.ts";

```

Une chose à remarquer ici dans Deno est que chaque fois que nous importons un fichier local dans notre projet Deno, nous devons fournir l'extension du fichier. Cela est dû au fait que Deno ne sait pas si le fichier importé est un fichier `.js` ou `.ts`.

Ensuite, nous définissons simplement toutes nos routes selon les conventions REST :

```routes/todo.ts
router
  .get("/todos", todoController.getAllTodos)
  .post("/todos", todoController.createTodo)
  .get("/todos/:id", todoController.getTodoById)
  .put("/todos/:id", todoController.updateTodoById)
  .delete("/todos/:id", todoController.deleteTodoById);
```

Le code ci-dessus se traduira par notre définition d'API comme ceci :

|TYPE|API ROUTE|   |   |   |
|---|---|---|---|---|
|GET|/todos|   |   |   |
|GET|/todos/:id|   |   |   |
|POST|/todos|   |   |   |
|PUT|/todos/:id|   |   |   |
|DELETE|/todos/:id|   |   |   |

et à la fin, nous exportons simplement notre routeur en faisant `_export_ _default_ router;`.

Nous avons terminé avec la création de notre structure de routes. (Maintenant, chaque route ne fait rien car nos contrôleurs sont vides, nous ajouterons des fonctionnalités à ceux-ci dans un instant.)

Voici la dernière pièce du puzzle avant de commencer à ajouter des fonctionnalités à chaque contrôleur de route. Nous devons attacher ce `router` à notre instance `app`.

Alors, rendez-vous dans le fichier `server.ts` et faites ce qui suit :

* Ajoutez ceci tout en haut :

```
// routes
import todoRouter from "./routes/todo.ts";
```

* Supprimez ce morceau de code :

```
const router = new Router();
router.get("/", ({ response }: { response: any }) => {
  response.body = {
    message: "hello world",
  };
});
app.use(router.routes());
app.use(router.allowedMethods());
```

* Remplacez-le par :

```
app.use(todoRouter.routes());
app.use(todoRouter.allowedMethods());
```

C'est tout – nous avons terminé. Votre fichier `server.ts` devrait maintenant ressembler à ceci :

```server.ts
import { Application } from "https://deno.land/x/oak/mod.ts";
import { green, yellow } from "https://deno.land/std@0.53.0/fmt/colors.ts";

// routes
import todoRouter from "./routes/todo.ts";

const app = new Application();
const port: number = 8080;

app.use(todoRouter.routes());
app.use(todoRouter.allowedMethods());

app.addEventListener("listen", ({ secure, hostname, port }) => {
  const protocol = secure ? "https://" : "http://";
  const url = `${protocol}${hostname ?? "localhost"}:${port}`;
  console.log(
    `${yellow("Listening on:")} ${green(url)}`,
  );
});

await app.listen({ port });

```

Si vous avez été bloqué quelque part en suivant cela, rendez-vous simplement au code source de ce tutoriel **[ici](https://github.com/adeelibr/deno-playground/tree/master/chapter_1:oak).**

Super, maintenant nous avons nos routes sans fonctionnalité pour le moment. Ajoutons donc cette fonctionnalité dans nos contrôleurs.

Mais avant de faire cela, nous devons créer 2 fichiers supplémentaires (minuscules).

* Dans votre dossier racine, créez un nouveau dossier appelé `interfaces` et à l'intérieur de ce dossier, créez un fichier appelé `Todo.ts` (assurez-vous que Todo est en majuscule, car cela ne donnera aucune erreur de syntaxe ici si vous ne le faites pas – ce sont juste des conventions.)
* Également dans votre dossier racine, créez un nouveau dossier appelé `stubs` et à l'intérieur de ce dossier, créez un fichier appelé `todos.ts`

Créons une interface dans notre fichier `interfaces/Todo.ts`. Ajoutez simplement le code suivant :

```interfaces/todo.ts
export default interface Todo {
  id: string,
  todo: string,
  isCompleted: boolean,
}
```

Qu'est-ce qu'une interface ?

L'une des choses principales dans TypeScript est de vérifier la forme que la valeur a. Similaire à `const port: number = 8080` ou `{ response }: { response : any }`, nous pouvons également vérifier le type d'un objet. 

Dans TypeScript, les interfaces remplissent le rôle de nommer ces types, et sont un moyen puissant de **définir des contrats au sein** de votre code ainsi que des **contrats avec le code extérieur** à votre projet. 

Voici un autre exemple d'interface :

```ts
// Nous avons une interface
interface LabeledValue {
  label: string;
}

// l'argument passé à cette fonction labeledObj est 
// de type LabeledValue (interface)
function printLabel(labeledObj: LabeledValue) {
  console.log(labeledObj.label);
}

let myObj = {label: "Size 10 Object"};
printLabel(myObj);
```

Espérons que cet exemple vous donne un peu plus d'informations sur les interfaces. Si vous souhaitez des informations plus détaillées, consultez la documentation sur [interfaces ici](https://www.typescriptlang.org/docs/handbook/interfaces.html).

Maintenant que notre interface est prête, créons des données fictives (puisque nous n'avons pas de base de données réelle pour ce tutoriel).

Créons d'abord une liste fictive de todos dans notre fichier `stubs/todos.ts`. Ajoutez simplement ce qui suit :

```stubs/todos.ts
import { v4 } from "https://deno.land/std/uuid/mod.ts";
// interface
import Todo from '../interfaces/Todo.ts';

let todos: Todo[] = [
  {
    id: v4.generate(),
    todo: 'walk dog',
    isCompleted: true,
  },
  {
    id: v4.generate(),
    todo: 'eat food',
    isCompleted: false,
  },
];

export default todos;
```

* Deux choses à remarquer ici : nous ajoutons un nouveau package et utilisons sa méthode `v4` en faisant `_import_ { v4 } _from_ "https://deno.land/std/uuid/mod.ts";`. Ensuite, chaque fois que nous utilisons `v4.generate()`, il créera une nouvelle chaîne aléatoire d'`id`.  
  
L'`id` ne peut pas être un `number`, seulement une `string` car dans notre interface `Todo`, nous avons défini `id` comme une chaîne.
* L'autre chose à se concentrer ici est `let _todos_: _Todo_[]` = []. Cela indique essentiellement à Deno que notre tableau todos est de type `Todo` (ce qui est génial, notre compilateur sait maintenant _automatiquement_ que chaque élément de notre tableau ne peut avoir que `{**id**: _string_, **todo**: _string_ & **isCompleted**: _boolean_}` il n'acceptera aucune autre clé).

Si vous souhaitez en savoir plus sur les `interfaces` dans TypeScript, consultez cette documentation détaillée et incroyable sur les interfaces **[ici](https://www.typescriptlang.org/docs/handbook/interfaces.html).**

Super. Si vous êtes arrivé jusqu'ici, donnez-vous une tape dans le dos. Bon travail à tous.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/download-1.jpeg)
_The Rock apprécie tous les efforts que vous faites_

## Travaillons sur nos contrôleurs

Dans votre fichier `controllers/todo.ts` :

```controllers/todos.ts
export default {
  getAllTodos: () => {},
  createTodo: async () => {},
  getTodoById: () => {},
  updateTodoById: async () => {},
  deleteTodoById: () => {},
};

```

Écrivons le contrôleur pour `getAllTodos` :

```controllers/todos.ts
// stubs
import todos from "../stubs/todos.ts";

export default {
  /**
   * @description Get all todos
   * @route GET /todos
   */
  getAllTodos: ({ response }: { response: any }) => {
    response.status = 200;
    response.body = {
      success: true,
      data: todos,
    };
  },
  createTodo: async () => {},
  getTodoById: () => {},
  updateTodoById: async () => {},
  deleteTodoById: () => {},
};

```

Avant de commencer ce bloc de code, laissez-moi expliquer que chaque contrôleur a un argument – appelons-le `context`.

Nous pouvons donc déstructurer `_getAllTodos_: (context) => {}` en :

```
getAllTodos: ({ request, response, params }) => {}
```

Et puisque nous utilisons `typescript`, nous devons ajouter une vérification de type à toutes ces variables :

```
getAllTodos: (
  { request, response, params }: { 
    request: any, 
    response: any, 
    params: { id: string },
  },
) => {}
```

Nous avons donc ajouté des vérifications de type à tous les 3 `{ request, response, params }`

* `request` est ce que l'utilisateur nous envoie (des informations comme les en-têtes et les données JSON)
* `response` est ce que nous renvoyons à l'utilisateur dans la réponse de l'API
* `params` est ce que nous définissons dans nos routes de routeur, c'est-à-dire :

```ts
.get("/todos/:id", ({ params}: { params: { id: string } }) => {})
```

Donc le `:id` dans `/todos/:id` est le param. Les params sont un moyen d'obtenir des informations à partir de l'URL. Dans cet exemple, nous savons que nous avons un `/:id`. Donc lorsque l'utilisateur tente d'accéder à cette API (c'est-à-dire, `/todos/756`) **756** est essentiellement le param **:id**. Puisqu'il est dans l'URL, nous savons qu'il est de type `string`.

Maintenant que nous avons nos définitions de base définies, revenons à notre contrôleur todos :

```controllers/todos.ts
// stubs
import todos from "../stubs/todos.ts";

export default {
  /**
   * @description Get all todos
   * @route GET /todos
   */
  getAllTodos: ({ response }: { response: any }) => {
    response.status = 200;
    response.body = {
      success: true,
      data: todos,
    };
  },
  createTodo: async () => {},
  getTodoById: () => {},
  updateTodoById: async () => {},
  deleteTodoById: () => {},
};

```

Pour `getAllTodos`, nous avons seulement besoin de `response`. Si vous vous souvenez, `response` est ce qui est nécessaire pour envoyer des données à l'utilisateur.

Pour les personnes venant d'un environnement Node et Express, une grande différence ici est que nous n'avons pas besoin de `return` l'objet de réponse. Deno le fait pour nous automatiquement.

Tout ce que nous avons à faire est de définir `response.status` qui dans ce cas est `200`.

Plus d'informations sur les statuts de réponse [**ici**](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)**.**

L'autre chose que nous définissons est le `response.body` qui dans ce cas est un objet :

```ts
{
  success: true,
  data: todos
}
```

Je vais lancer mon serveur :

```
$ deno run --allow-net server.ts
```

> **Révision :** La propriété `---allow-net` indique à Deno que cette application donne à l'utilisateur la permission d'accéder à son contenu via le port ouvert.

Une fois votre serveur en cours d'exécution, vous pouvez accéder à l'API `GET /todos`. J'utilise `postman` qui est une extension Google Chrome et peut être téléchargé [ici](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop//%40).

Vous pouvez utiliser n'importe quel client rest que vous aimez. J'aime utiliser `postman` parce que je pense qu'il est très facile.

Dans Postman, ouvrez un nouvel onglet. Définissez la requête sur le type `GET` et dans la barre `URL`, tapez `http://localhost:8080/todos`. Appuyez sur `Send` et voici ce que vous voyez :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-02.01.11.png)
_Réponse de l'API GET /todos_

Cool ! 1 API terminée, 4 de plus à faire. ??

Si vous vous sentez bloqué quelque part, jetez un coup d'œil au code source directement [**ici**](https://github.com/adeelibr/deno-playground/tree/master/chapter_1:oak)**.**

Passons à notre prochain contrôleur :

```controllers/todos.ts
import { v4 } from "https://deno.land/std/uuid/mod.ts";
// interfaces
import Todo from "../interfaces/Todo.ts";
// stubs
import todos from "../stubs/todos.ts";

export default {
  getAllTodos: () => {},
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

    // if everything is fine then perform
    // operation and return todos with the
    // new data added.
    let newTodo: Todo = {
      id: v4.generate(),
      todo: body.value.todo,
      isCompleted: false,
    };
    let data = [...todos, newTodo];
    response.body = {
      success: true,
      data,
    };
  },
  getTodoById: () => {},
  updateTodoById: async () => {},
  deleteTodoById: () => {},
};

```

Puisque nous allons ajouter un nouveau Todo à notre liste, j'ai importé 2 modules dans le fichier du contrôleur.

* `import { v4 } from `[https://deno.land/std/uuid/mod.ts](https://deno.land/std/uuid/mod.ts)`;` cela sera utilisé pour créer un nouvel identifiant unique pour le todo en cours de création
* `import Todo from "../interfaces/Todo.ts";` cela sera utilisé pour s'assurer que le nouveau todo qui est créé suit la même structure.

Notre contrôleur `createTodo` est `async`, ce qui signifie qu'il y a des promesses utilisées à l'intérieur du contrôleur. 

Décomposons-le en parties plus petites :

```ts
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

Tout d'abord, nous obtenons le contenu du corps JSON que l'utilisateur nous a envoyé. Ensuite, nous utilisons la méthode intégrée `request.hasBody` de `oak` pour vérifier si l'utilisateur a même envoyé un contenu. Si ce n'est pas le cas, nous pouvons faire `if (!request_._hasBody) {}` à l'intérieur de ce bloc `if`. 

Nous définissons le statut sur `400` (400 signifie que l'utilisateur a fait quelque chose qu'il n'était pas censé faire) et le corps est défini sur `{success: false, message: "no data provided }`. Ensuite, nous ajoutons simplement `return;` pour nous assurer qu'aucun code supplémentaire ci-dessous n'est exécuté.

Ensuite, nous faisons ceci :

```
// if everything is fine then perform
// operation and return todos with the
// new data added.
let newTodo: Todo = {
  id: v4.generate(),
  todo: body.value.todo,
  isCompleted: false,
};
let data = [...todos, newTodo];
response.body = {
  success: true,
  data,
};
```

Nous créons un nouveau todo en faisant ceci :

```
let newTodo: Todo = {
  id: v4.generate(),
  todo: body.value.todo,
  isCompleted: false,
};
```

`let newTodo: Todo = {}` garantit que `newTodo` suit la même structure que le reste des todos. Nous attribuons ensuite un identifiant aléatoire en utilisant `v4.generate()`, définissons todo sur `body.value.todo` et `isCompleted` sur `false`.

La chose à remarquer ici est que toutes les données que l'utilisateur nous envoie, nous pouvons y accéder à partir de `body.value` dans `oak`.

Ensuite, nous faisons ce qui suit :

```
let data = [...todos, newTodo];
response.body = {
  success: true,
  data,
};
```

Ajoutez le `newTodo` à notre liste actuelle de todos et définissez simplement le corps sur `{success: true & data: data`.

Et nous avons terminé ✅ avec ce contrôleur également.

Redémarrons notre serveur :

```
$ deno run --allow-net server.ts
```

Dans mon postman, j'ouvre un nouvel onglet. Je définis la requête sur le type `POST` et dans la barre `URL`, je tape `http://localhost:8080/todos`. Ensuite, je clique sur `Send` et voici ce que vous voyez :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-02.24.00.png)
_J'envoie une requête vide et j'obtiens un code d'erreur de statut 400 ainsi qu'un message d'erreur_

Ensuite, j'envoie un contenu dans le corps de la charge utile de la requête et j'essaie à nouveau :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-02.24.15.png)
_Super, POST /todos avec le contenu du corps { todo: "eat a lamma" } est un succès & nous pouvons voir le contenu ajouté à notre liste de todos actuelle_

Cool, nous pouvons voir que notre API fonctionne comme prévu.

Deux API terminées, trois de plus à faire. 

Nous y sommes presque. La majeure partie du travail difficile est faite. ☺️ ? ? ?

Passons à notre troisième API :

```controllers/todos.ts
import { v4 } from "https://deno.land/std/uuid/mod.ts";
// interfaces
import Todo from "../interfaces/Todo.ts";
// stubs
import todos from "../stubs/todos.ts";

export default {
  getAllTodos: () => {},
  createTodo: async () => {},
  /**
   * @description Get todo by id
   * @route GET todos/:id
   */
  getTodoById: (
    { params, response }: { params: { id: string }; response: any },
  ) => {
    const todo: Todo | undefined = todos.find((t) => {
      return t.id === params.id;
    });
    if (!todo) {
      response.status = 404;
      response.body = {
        success: false,
        message: "No todo found",
      };
      return;
    }

    // If todo is found
    response.status = 200;
    response.body = {
      success: true,
      data: todo,
    };
  },
  updateTodoById: async () => {},
  deleteTodoById: () => {},
};

```

Parlons de notre contrôleur pour `GET todos/:id`. Cela nous permettra d'obtenir un todo par ID.

Décomposons cela en parties plus petites et discutons-en :

```
const todo: Todo | undefined = todos.find((t) => t.id === params.id);
if (!todo) {
  response.status = 404;
  response.body = {
    success: false,
    message: "No todo found",
  };
  return;
}
```

Dans la première partie, nous définissons une nouvelle `const todo` et définissons son type soit `Todo` soit `undefined`. Donc `todo` sera soit un objet avec la forme de l'interface `Todo`, soit il sera `undefined` – il ne peut pas être autre chose.

Nous utilisons ensuite `_todos.find_((_t_)` => _t.id_ === _params.id_); [Array.find()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find) pour trouver le `todo` avec l'id fourni dans `params.id`. Si cela correspond, nous obtenons un `Todo` avec la forme `todo`, sinon `undefined`.

Si `todo` est undefined, cela signifie que ce bloc `if` sera exécuté :

```
if (!todo) {
  response.status = 404;
  response.body = {
    success: false,
    message: "No todo found",
  };
  return;
}
```

Ici, nous définissons simplement le statut sur `404` qui signifie `non trouvé` ainsi que notre réponse d'échec standard ou `{ status, message }`

Cool, non ? ?

Ensuite, nous faisons simplement ceci :

```
// If todo is found
response.status = 200;
response.body = {
  success: true,
  data: todo,
};
```

Définissons une réponse de succès `200` et dans le corps de notre réponse, nous définissons `success: true & data: todo`.

Testons cela dans notre postman.

Redémarrons notre serveur :

```
$ deno run --allow-net server.ts
```

Dans mon postman, j'ouvre un nouvel onglet. Je définis la requête sur le type `GET` et dans la barre `URL`, je tape `http://localhost:8080/todos/:id`, puis je clique sur `Send`.

Puisque nous générons des ID aléatoirement, obtenez d'abord tous les todos en appelant l'API get all todos. Ensuite, à partir de n'importe quel todo, obtenez l'un de ses ID pour tester cette nouvelle API.  
Chaque fois que vous redémarrez cette application Deno, de nouveaux ID seront générés.

Allons-y :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-02.40.52.png)
_statut 404, cas où aucun enregistrement n'est trouvé_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-02.41.36.png)
_Fournissez un ID connu et il renvoie le todo associé à cet ID ainsi que le statut 200_

Si vous devez vous référer au code source original de ce tutoriel, allez [**ici**](https://github.com/adeelibr/deno-playground/tree/master/chapter_1:oak).

Super, 3 API terminées, 2 de plus à faire.

```controllers/todos.ts
import { v4 } from "https://deno.land/std/uuid/mod.ts";
// interfaces
import Todo from "../interfaces/Todo.ts";
// stubs
import todos from "../stubs/todos.ts";

export default {
  getAllTodos: () => {},
  createTodo: async () => {},
  getTodoById: () => {},
  /**
   * @description Update todo by id
   * @route PUT todos/:id
   */
  updateTodoById: async (
    { params, request, response }: {
      params: { id: string },
      request: any,
      response: any,
    },
  ) => {
    const todo: Todo | undefined = todos.find((t) => t.id === params.id);
    if (!todo) {
      response.status = 404;
      response.body = {
        success: false,
        message: "No todo found",
      };
      return;
    }

    // if todo found then update todo
    const body = await request.body();
    const updatedData: { todo?: string; isCompleted?: boolean } = body.value;
    let newTodos = todos.map((t) => {
      return t.id === params.id ? { ...t, ...updatedData } : t;
    });
    response.status = 200;
    response.body = {
      success: true,
      data: newTodos,
    };
  },
  deleteTodoById: () => {},
};

```

Parlons de notre contrôleur pour `PUT todos/:id`. Cela mettra à jour un todo par ID.

Décomposons cela en parties plus petites :

```
const todo: Todo | undefined = todos.find((t) => t.id === params.id);
if (!todo) {
  response.status = 404;
  response.body = {
    success: false,
    message: "No todo found",
  };
  return;
}
```

C'est quelque chose que nous avons fait exactement de la même manière avec le contrôleur précédent, donc je ne vais pas entrer dans les détails ici.

Conseil pro ici : Vous pouvez, si vous le souhaitez, faire de ce morceau de code un bloc de code générique et l'utiliser dans les deux contrôleurs.

Ensuite, nous faisons ceci :

```
// if todo found then update todo
const body = await request.body();
const updatedData: { todo?: string; isCompleted?: boolean } = body.value;
let newTodos = todos.map((t) => {
  return t.id === params.id ? { ...t, ...updatedData } : t;
});
response.status = 200;
response.body = {
  success: true,
  data: newTodos,
};
```

Le morceau de code dont je veux parler ici est le suivant :

```
const updatedData: { todo?: string; isCompleted?: boolean } = body.value;
let newTodos = todos.map((t) => {
  return t.id === params.id ? { ...t, ...updatedData } : t;
});
```

Tout d'abord, nous faisons `const updatedData = body.value` puis nous ajoutons une vérification de type à `updatedData` comme suit :

```
updatedData: { todo?: string; isCompleted?: boolean }
```

Ce morceau de code indique à TS que `updatedData` est un objet qui peut `avoir/pas avoir` _todo: string et_ aussi peut `avoir/pas avoir` _isCompleted: boolean._

Ensuite, nous mappons simplement tous les todos comme ceci :

```
let newTodos = todos.map((t) => {
  return t.id === params.id ? { ...t, ...updatedData } : t;
});
```

Et où `params.id` correspond à `t.id`, nous ajoutons simplement tout à cet objet que nous obtenons de l'utilisateur.

Nous avons également terminé avec cette API. 

Redémarrons notre serveur :

```
$ deno run --allow-net server.ts
```

Ouvrez un nouvel onglet dans Postman. Définissez la requête sur `PUT` et dans la barre `URL`, tapez `http://localhost:8080/todos/:id`, puis cliquez sur `Send` :

Puisque nous générons des ID aléatoirement, obtenez d'abord tous les todos en appelant l'API get all todos. Ensuite, à partir de n'importe quel todo, obtenez l'un de ses ID pour tester cette nouvelle API.  
Chaque fois que vous redémarrez cette application Deno, de nouveaux ID seront générés.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-02.59.39.png)
_statut 404 retourné et message d'erreur aucun todo trouvé donné_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-03.00.21.png)
_Fournir un ID connu, mettre à jour le contenu du todo dans le corps. Il a retourné le todo mis à jour ainsi que tous les autres todos_

C'est incroyable – quatre API terminées et une seule de plus à faire.

```controllers/todos.ts
import { v4 } from "https://deno.land/std/uuid/mod.ts";
// interfaces
import Todo from "../interfaces/Todo.ts";
// stubs
import todos from "../stubs/todos.ts";

export default {
  getAllTodos: () => {},
  createTodo: async () => {},
  getTodoById: () => {},
  updateTodoById: async () => {},
  /**
   * @description Delete todo by id
   * @route DELETE todos/:id
   */
  deleteTodoById: (
    { params, response }: { params: { id: string }; response: any },
  ) => {
    const allTodos = todos.filter((t) => t.id !== params.id);

    // remove the todo w.r.t id and return
    // remaining todos
    response.status = 200;
    response.body = {
      success: true,
      data: allTodos,
    };
  },
};

```

Parlons de notre contrôleur pour `Delete todos/:id`, cela supprimera un todo par ID.

Nous exécutons simplement un filtre sur tous les todos :

```
const allTodos = todos.filter((t) => t.id !== params.id);

```

Supprimez le `todo.id` qui correspond à `params.id` et retournez le reste.

Ensuite, nous faisons ceci :

```
// remove the todo w.r.t id and return
// remaining todos
response.status = 200;
response.body = {
  success: true,
  data: allTodos,
};
```

Retournez simplement tous les todos restants qui n'ont pas le même todo.id.

Redémarrons notre serveur :

```
$ deno run --allow-net server.ts
```

Ouvrez un nouvel onglet dans Postman. Cette fois, définissez la requête sur `DELETE` et dans la barre `URL`, tapez `http://localhost:8080/todos/:id` et cliquez sur `Send`.

Puisque nous générons des ID aléatoirement, obtenez d'abord tous les todos en appelant l'API get all todos. Ensuite, à partir de n'importe quel todo, obtenez l'un de ses ID pour tester cette nouvelle API.  
Chaque fois que vous redémarrez cette application Deno, de nouveaux ID seront générés.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-03.07.54.png)

Avec cela, nous avons terminé avec les cinq API.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/75bdf06df3fd6ddd9d3311d8cb2be029.jpg)

---

Maintenant, il ne nous reste plus que deux choses à faire :

* Ajouter un middleware de route non trouvé afin que lorsque l'utilisateur tente d'accéder à une route inconnue, il renvoie une erreur.
* Ajouter un logger API qui affiche dans la console le temps de réponse qu'il a fallu pour renvoyer les données d'un point de terminaison API.

## Création d'un middleware de route pour les routes introuvables

Dans votre dossier racine, créez un nouveau dossier appelé `middlewares`. À l'intérieur de ce dossier, créez un fichier appelé `notFound.ts` et à l'intérieur de ce fichier, ajoutez ce code :

```middlwares/notfound.ts
export default ({ response }: { response: any }) => {
  response.status = 404;
  response.body = {
    success: false,
    message: "404 - Not found.",
  };
};

```

Ici, nous ne faisons rien de nouveau – c'est très similaire à la structure de nos contrôleurs. Nous retournons simplement un statut `404` (qui signifie non trouvé) avec un objet JSON pour `{ success, message }`.

Ensuite, allez dans votre fichier `server.ts` et ajoutez le contenu suivant :

* Ajoutez cette importation quelque part en haut :

```server.ts
// not found
import notFound from './middlewares/notFound.ts';
```

* Et juste en dessous de votre `app.use(todoRouter.allowedMethods())`, ajoutez cette ligne comme ceci :

```server.ts
app.use(todoRouter.routes());
app.use(todoRouter.allowedMethods());

// 404 page
app.use(notFound);
```

L'ordre d'exécution est important ici : chaque fois que nous essayons d'accéder à un point de terminaison d'API, il correspondra d'abord aux routes de notre `todoRouter`. Si aucune n'est trouvée, il exécutera alors `app_.use_(notFound);`. 

Vérifions si cela fonctionne.

Redémarrez le serveur :

```
$ deno run --allow-net server.ts
```

Ouvrez un nouvel onglet dans Postman. Définissez la requête sur `GET` et dans la barre `URL`, tapez `http://localhost:8080/something-unknown`, puis cliquez sur `Send`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-12.28.10.png)

Nous avons maintenant un middleware de route que nous avons placé à la fin de nos routes dans `server.ts` en tant que `app_.use_(notFound);`. Si aucune route ne correspond, ce middleware s'exécutera et renverra un code de statut `404` (qui signifie non trouvé). Ensuite, nous envoyons simplement un message de réponse comme toujours qui est `{success, message}`.

**Conseil pro :** Nous avons décidé que `{success, message}` est ce que nous renvoyons dans les scénarios d'échec et `{success, data}` est ce que nous renvoyons à l'utilisateur dans les scénarios de succès. Nous pouvons même faire de ces objets/formes des interfaces et les ajouter à notre projet pour garantir la cohérence et la vérification de type sécurisée.

Cool, nous avons terminé avec l'un de nos middlewares – ajoutons l'autre middleware pour journaliser nos API dans la console.

**Rappel :** Si vous êtes bloqué quelque part, vous pouvez utiliser le [code source ici](https://github.com/adeelibr/deno-playground/tree/master/chapter_1:oak).

## Journalisation des API dans la console

Dans votre dossier `middlewares`, créez un nouveau fichier appelé `logger.ts` et entrez le code suivant :

```middlewares/logger.ts
import {
  green,
  cyan,
  white,
  bgRed,
} from "https://deno.land/std@0.53.0/fmt/colors.ts";

const X_RESPONSE_TIME: string = "X-Response-Time";

export default {
  logger: async (
    { response, request }: { response: any, request: any },
    next: Function,
  ) => {
    await next();
    const responseTime = response.headers.get(X_RESPONSE_TIME);
    console.log(`${green(request.method)} ${cyan(request.url.pathname)}`);
    console.log(`${bgRed(white(String(responseTime)))}`);
  },
  responseTime: async (
    { response }: { response: any },
    next: Function,
  ) => {
    const start = Date.now();
    await next();
    const ms: number = Date.now() - start;
    response.headers.set(X_RESPONSE_TIME, `${ms}ms`)
  },
};

```

Dans votre fichier `server.ts`, ajoutez ce code :

* Importez ceci quelque part en haut :

```server.ts
// logger
import logger from './middlewares/logger.ts';
```

* Juste au-dessus de votre code `todoRouter`, ajoutez ces middlewares comme ceci :

```
// order of execution is important;
app.use(logger.logger);
app.use(logger.responseTime);

app.use(todoRouter.routes());
app.use(todoRouter.allowedMethods());
```

Maintenant, discutons de ce que nous venons de faire.

Parlons du fichier `logger.ts` et décomposons-le en morceaux :

```ts
import {
  green,
  cyan,
  white,
  bgRed,
} from "https://deno.land/std@0.53.0/fmt/colors.ts";
```

J'importe certaines couleurs de console et couleurs d'arrière-plan de console que je souhaite utiliser dans la journalisation des API.

Cela est similaire à ce que nous avons fait dans notre `eventListener` dans notre fichier `server.ts`. Nous utiliserons des couleurs dans notre console pour journaliser les requêtes API.

Ensuite, je définis `const X_RESPONSE_TIME: string = "X-Response-Time";`. C'est l'en-tête que nous allons injecter dans nos requêtes API lorsqu'elles arrivent sur notre serveur. Je l'appelle `X_RESPONSE_TIME` et sa valeur est `X-Response-Time`. Je vais démontrer son utilisation dans un instant.

Ensuite, nous exportons simplement un objet comme ceci :

```middlewares/logger.ts
export default {
	logger: async ({ response, request }, next) {}
	responseTime: async ({ response }, next) {}
};
```

Et ensuite, nous l'utilisons simplement à l'intérieur de notre fichier `server.ts` comme ceci :

```server.ts
// order of execution is important;
app.use(logger.logger);
app.use(logger.responseTime);
```

Discutons maintenant de ce qui se passe dans notre code de middleware de journalisation et discutons de son style d'exécution en utilisant `next()` :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-12.51.36.png)
_Exécution de l'ordre du middleware de journalisation lorsque l'API GET /todos est appelée._

La seule différence ici et dans les contrôleurs que nous avions avant est l'utilisation de la fonction `next()`. Cette fonction nous aide à sauter d'un contrôleur à l'autre comme montré dans l'image ci-dessous.

Donc dans :

```middlewares/logger.ts
export default {
  logger: async (
    { response, request }: { response: any, request: any },
    next: Function,
  ) => {
    await next();
    const responseTime = response.headers.get(X_RESPONSE_TIME);
    console.log(`${green(request.method)} ${cyan(request.url.pathname)}`);
    console.log(`${bgRed(white(String(responseTime)))}`);
  },
  responseTime: async (
    { response }: { response: any },
    next: Function,
  ) => {
    const start = Date.now();
    await next();
    const ms: number = Date.now() - start;
    response.headers.set(X_RESPONSE_TIME, `${ms}ms`)
  },
};
```

Gardez à l'esprit que c'est ce que nous avons dans notre fichier `server.ts` :

```server.ts
// order of execution is important;
app.use(logger.logger);
app.use(logger.responseTime);

app.use(todoRouter.routes());
app.use(todoRouter.allowedMethods());
```

L'ordre d'exécution est le suivant :

* logger.logger middleware
* logger.responseTime middleware
* todoRouter controller (quel que soit le chemin appelé par l'utilisateur, pour les besoins de l'explication, je suppose que l'utilisateur a appelé l'API `GET /todos` pour obtenir tous les todos.)

Il exécutera d'abord le middleware logger.logger qui est celui-ci :

```middlewares/logger.ts
logger: async (
    { response, request }: { response: any, request: any },
    next: Function,
  ) => {
    await next();
    const responseTime = response.headers.get(X_RESPONSE_TIME);
    console.log(`${green(request.method)} ${cyan(request.url.pathname)}`);
    console.log(`${bgRed(white(String(responseTime)))}`);
  },
```

Il entrera dans cette fonction et immédiatement lorsqu'il lira `await next()`, il passera rapidement au middleware suivant qui est `responseTime` :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-12.51.36-1.png)
_Partage de l'image ci-dessus à nouveau pour révision._

À l'intérieur de `responseTime`, il n'exécute que deux lignes qui sont (regardez l'ordre d'exécution 2 dans l'image ci-dessus) :

```middlewares/logger.ts
const start = Date.now();
await next();
```

avant de sauter au contrôleur `getAllTodos`. Une fois qu'il entre dans `getAllTodos`, il exécutera tout le code à l'intérieur de ce contrôleur. 

Puisque dans ce contrôleur nous n'utilisons pas `next()`, il renverra simplement le flux de logique à `responseTime` controller. Là, il exécutera ce qui suit :

```middlewares/logger.ts
const ms: number = Date.now() - start;
response.headers.set(X_RESPONSE_TIME, `${ms}ms`)
```

Maintenant, en gardant à l'esprit l'ordre d'exécution qui est `2, 3, 4` (regardez l'image ci-dessus).

Voici ce qui se passe :

* Nous capturons les données dans `ms` en faisant `const` _`start`_ `=` _`Date.now`_`();`. Ensuite, nous appelons immédiatement `next()` qui va au contrôleur `getAllTodos` et exécute tout le code. Ensuite, il revient dans le contrôleur `responseTime`.
* Nous soustrayons ensuite cette date `start` avec la date à ce moment-là en faisant `const _ms_: _number_ = _Date.now_()` - _start_; `ms`. Ici, il renverra un nombre qui est essentiellement la différence en millisecondes qui nous indiquera tout le temps qu'il a fallu à Deno pour exécuter notre contrôleur `getAllTodos`.

Partage de l'image une fois de plus pour révision :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-12.51.36-2.png)

* Ensuite, nous définissons simplement les en-têtes dans notre `response` comme ceci :

```
response.headers.set(X_RESPONSE_TIME, `${ms}ms`)
```

Ce qui définit simplement la valeur de l'en-tête `X-Response-Time` aux millisecondes qu'il a fallu à Deno pour exécuter notre API.

* Ensuite, de l'ordre d'exécution `4`, nous revenons à l'ordre d'exécution `5` (jetez un coup d'œil à l'image ci-dessus pour référence).

Ici, nous faisons simplement :

```middlwares/logger.ts
const responseTime = response.headers.get(X_RESPONSE_TIME);
console.log(`${green(request.method)} ${cyan(request.url.pathname)}`);
console.log(`${bgRed(white(String(responseTime)))}`);
```

* Nous obtenons le temps que nous avons passé dans le `X-Response-Time`
* Ensuite, nous prenons ce temps et l'affichons simplement en couleur dans la console.

`request.method` nous indique la méthode utilisée pour appeler notre API, c'est-à-dire `GET, PUT etc` tandis que `request.url.pathname` nous indiquera le chemin de l'API que l'utilisateur a utilisé, c'est-à-dire `/todos`

Vérifions si cela fonctionne.

Redémarrez le serveur :

```
$ deno run --allow-net server.ts
```

Ouvrez un nouvel onglet dans Postman. Définissez la requête sur `GET`, tapez `http://localhost:8080/todos`, et cliquez sur `Send`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-13.17.13.png)

Appuyez sur l'API plusieurs fois dans Postman. Ensuite, lorsque vous revenez à la console, vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-29-at-13.21.03.png)
_API étant journalisée dans notre console_

C'est tout – nous avons terminé.

Si vous vous sentez toujours bloqué, jetez un coup d'œil au code source complet de ce tutoriel ici : [github.com/adeelibr/deno-playground/tree/master/chapter_1:oak](https://github.com/adeelibr/deno-playground/tree/master/chapter_1:oak)

J'espère que vous avez trouvé cet article utile et qu'il a pu vous aider à apprendre quelque chose aujourd'hui.

Si vous l'avez aimé, n'hésitez pas à le partager sur les réseaux sociaux. Si vous souhaitez en discuter, contactez-moi sur [Twitter](https://twitter.com/adeelibr).