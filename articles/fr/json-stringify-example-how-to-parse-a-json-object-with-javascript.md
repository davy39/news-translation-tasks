---
title: Exemple JSON Stringify – Comment analyser un objet JSON avec JS
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2021-01-05T15:11:00.000Z'
originalURL: https://freecodecamp.org/news/json-stringify-example-how-to-parse-a-json-object-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/602358380a2838549dcc2554.jpg
tags:
- name: JavaScript
  slug: javascript
- name: json
  slug: json
seo_title: Exemple JSON Stringify – Comment analyser un objet JSON avec JS
seo_desc: 'JSON, or JavaScript Object Notation, is all around us. If you''ve ever
  used a web app, there''s a very good chance that it used JSON to structure, store,
  and transmit data between its servers and your device.

  In this article, we''ll briefly go over the ...'
---

JSON, ou JavaScript Object Notation, est partout autour de nous. Si vous avez déjà utilisé une application web, il y a de fortes chances qu'elle ait utilisé JSON pour structurer, stocker et transmettre des données entre ses serveurs et votre appareil.

Dans cet article, nous allons brièvement passer en revue les différences entre JSON et JavaScript, puis nous plonger dans différentes façons d'analyser JSON avec JavaScript dans le navigateur et dans les projets Node.js.

## Différences entre JSON et JavaScript

Bien que JSON ressemble à du JavaScript régulier, il est préférable de considérer JSON comme un format de données, similaire à un fichier texte. Il se trouve que JSON est inspiré de la syntaxe JavaScript, c'est pourquoi ils se ressemblent tant.

Examinons les objets JSON et les tableaux JSON et comparons-les à leurs équivalents JavaScript.

### Objets JSON vs littéraux d'objet JavaScript

Tout d'abord, voici un objet JSON :

```json
{
  "name": "Jane Doe",
  "favorite-game": "Stardew Valley",
  "subscriber": false
}

```

La principale différence entre un objet JSON et un objet JavaScript régulier – également appelé littéral d'objet – réside dans les guillemets. Toutes les clés et les valeurs de type chaîne dans un objet JSON doivent être entourées de guillemets doubles (`"`).

Les littéraux d'objet JavaScript sont un peu plus flexibles. Avec les littéraux d'objet, vous n'avez pas besoin d'entourer les clés et les chaînes de guillemets doubles. Au lieu de cela, vous pourriez utiliser des guillemets simples (`'`), ou ne pas utiliser de guillemets pour les clés.

Voici à quoi pourrait ressembler le code ci-dessus en tant que littéral d'objet JavaScript :

```js
const profile = {
  name: 'Jane Doe',
  'favorite-game': 'Stardew Valley',
  subscriber: false
}

```

Notez que la clé `'favorite-game'` est entourée de guillemets simples. Avec les littéraux d'objet, vous devrez entourer les clés où les mots sont séparés par des tirets (`-`) de guillemets.

Si vous souhaitez éviter les guillemets, vous pourriez réécrire la clé pour utiliser la casse camel (`favoriteGame`) ou séparer les mots avec un trait de soulignement (`favorite_game`) à la place.

### Tableaux JSON vs tableaux JavaScript

Les tableaux JSON fonctionnent à peu près de la même manière que les tableaux en JavaScript, et peuvent contenir des chaînes, des booléens, des nombres et d'autres objets JSON. Par exemple :

```json
[
  {
    "name": "Jane Doe",
    "favorite-game": "Stardew Valley",
    "subscriber": false
  },
  {
    "name": "John Doe",
    "favorite-game": "Dragon Quest XI",
    "subscriber": true
  }
]

```

Voici à quoi cela pourrait ressembler en JavaScript simple :

```js
const profiles = [
  {
    name: 'Jane Doe',
    'favorite-game': 'Stardew Valley',
    subscriber: false
  },
  {
    name: 'John Doe',
    'favorite-game': 'Dragon Quest XI',
    subscriber: true
  }
];

```

## JSON en tant que chaîne

Vous vous demandez peut-être, s'il existe des objets JSON et des tableaux, ne pourriez-vous pas l'utiliser dans votre programme comme un littéral d'objet JavaScript ou un tableau régulier ?

La raison pour laquelle vous ne pouvez pas faire cela est que JSON est vraiment juste une chaîne.

Par exemple, lorsque vous écrivez JSON dans un fichier séparé comme avec `jane-profile.json` ou `profiles.json` ci-dessus, ce fichier contient en réalité du texte sous la forme d'un objet JSON ou d'un tableau, qui ressemble à JavaScript.

Et si vous faites une requête à une API, elle retournera quelque chose comme ceci :

```
{"name":"Jane Doe","favorite-game":"Stardew Valley","subscriber":false}
```

Tout comme avec les fichiers texte, si vous voulez utiliser JSON dans votre projet, vous devrez l'analyser ou le transformer en quelque chose que votre langage de programmation peut comprendre. Par exemple, l'analyse d'un objet JSON en Python créera un dictionnaire.

Avec cette compréhension, regardons différentes façons d'analyser JSON en JavaScript.

## Comment analyser JSON dans le navigateur

Si vous travaillez avec JSON dans le navigateur, vous recevez ou envoyez probablement des données via une API.

Examinons quelques exemples.

### Comment analyser JSON avec `fetch`

La manière la plus simple d'obtenir des données à partir d'une API est avec `fetch`, qui inclut la méthode `.json()` pour analyser les réponses JSON en un littéral d'objet JavaScript ou un tableau utilisable automatiquement.

Voici un code qui utilise `fetch` pour faire une requête `GET` pour une blague à thème développeur à partir de l'API gratuite [Chuck Norris Jokes API](https://api.chucknorris.io/) :

```js
fetch('https://api.chucknorris.io/jokes/random?category=dev')
  .then(res => res.json()) // la méthode .json() analyse la réponse JSON en un littéral d'objet JS
  .then(data => console.log(data));

```

Si vous exécutez ce code dans le navigateur, vous verrez quelque chose comme ceci journalisé dans la console :

```js
{
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "elgv2wkvt8ioag6xywykbq",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/elgv2wkvt8ioag6xywykbq",
    "value": "Le clavier de Chuck Norris n'a pas de touche Ctrl car rien ne contrôle Chuck Norris."
}

```

Bien que cela ressemble à un objet JSON, c'est vraiment un littéral d'objet JavaScript, et vous pouvez l'utiliser librement dans votre programme.

### Comment stringifier JSON avec `JSON.stringify()`

Mais que faire si vous voulez envoyer des données à une API ?

Par exemple, disons que vous souhaitez envoyer une blague de Chuck Norris à l'API Chuck Norris Jokes afin que d'autres personnes puissent la lire plus tard.

Tout d'abord, vous écriviez votre blague sous forme de littéral d'objet JS :

```js
const newJoke = {
  categories: ['dev'],
  value: "Le clavier de Chuck Norris est entièrement composé de touches Cmd car Chuck Norris est toujours en commande."
};

```

Ensuite, puisque vous envoyez des données à une API, vous devrez transformer votre littéral d'objet `newJoke` en une chaîne JSON.

Heureusement, JavaScript inclut une méthode super utile pour faire exactement cela – `JSON.stringify()` :

```js
const newJoke = {
  categories: ['dev'],
  value: "Le clavier de Chuck Norris est entièrement composé de touches Cmd car Chuck Norris est toujours en commande."
};

console.log(JSON.stringify(newJoke)); // {"categories":["dev"],"value":"Le clavier de Chuck Norris est entièrement composé de touches Cmd car Chuck Norris est toujours en commande."}

console.log(typeof JSON.stringify(newJoke)); // string

```

Bien que nous convertissions un littéral d'objet en une chaîne JSON dans cet exemple, `JSON.stringify()` fonctionne également avec les tableaux.

Enfin, vous devrez simplement envoyer votre blague stringifiée JSON à l'API avec une requête `POST`.

Notez que l'API Chuck Norris Jokes ne possède pas réellement cette fonctionnalité. Mais si c'était le cas, voici à quoi le code pourrait ressembler :

```js
const newJoke = {
  categories: ['dev'],
  value: "Le clavier de Chuck Norris est entièrement composé de touches Cmd car Chuck Norris est toujours en commande."
};

fetch('https://api.chucknorris.io/jokes/submit', { // faux endpoint API
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(newJoke), // transformer le littéral d'objet JS en une chaîne JSON
})
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => {
    console.error(err);
  });
```

Et voilà, vous avez analysé le JSON entrant avec `fetch` et utilisé `JSON.stringify()` pour convertir un littéral d'objet JS en une chaîne JSON.

### Comment travailler avec des fichiers JSON locaux dans le navigateur

Malheureusement, il n'est pas possible (ou conseillé) de charger un fichier JSON local dans le navigateur.

`fetch` générera une erreur si vous essayez de charger un fichier local. Par exemple, disons que vous avez un fichier JSON avec quelques blagues :

```json
[
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "elgv2wkvt8ioag6xywykbq",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/elgv2wkvt8ioag6xywykbq",
    "value": "Le clavier de Chuck Norris n'a pas de touche Ctrl car rien ne contrôle Chuck Norris."
  },
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "ae-78cogr-cb6x9hluwqtw",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/ae-78cogr-cb6x9hluwqtw",
    "value": "Il n'y a pas de touche Échap sur le clavier de Chuck Norris, car personne n'échappe à Chuck Norris."
  }
]

```

Et vous voulez l'analyser et créer une liste de blagues sur une simple page HTML.

Si vous créez une page avec ce qui suit et que vous l'ouvrez dans votre navigateur :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="viewport" content="width=device-width" />
    <title>Fetch Local JSON</title>
  </head>
  <script>
    fetch("./jokes.json", { mode: "no-cors" }) // désactiver CORS car le chemin ne contient pas http(s)
      .then((res) => res.json())
      .then((data) => console.log(data));
  </script>
</html>

```

Vous verrez ceci dans la console :

```
Fetch API cannot load file://<path>/jokes.json. URL scheme "file" is not supported

```

Par défaut, les navigateurs n'autorisent pas l'accès aux fichiers locaux pour des raisons de sécurité. C'est une bonne chose, et vous ne devriez pas essayer de contourner ce comportement.

Au lieu de cela, la meilleure chose à faire est de convertir le fichier JSON local en JavaScript. Heureusement, cela est assez facile puisque la syntaxe JSON est si similaire à JavaScript.

Tout ce que vous avez à faire est de créer un nouveau fichier et de déclarer votre JSON comme une variable :

```js
const jokes = [
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "elgv2wkvt8ioag6xywykbq",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/elgv2wkvt8ioag6xywykbq",
    "value": "Le clavier de Chuck Norris n'a pas de touche Ctrl car rien ne contrôle Chuck Norris."
  },
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "ae-78cogr-cb6x9hluwqtw",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/ae-78cogr-cb6x9hluwqtw",
    "value": "Il n'y a pas de touche Échap sur le clavier de Chuck Norris, car personne n'échappe à Chuck Norris."
  }
]

```

Et l'ajouter à votre page en tant que script séparé :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta name="viewport" content="width=device-width" />
    <title>Fetch Local JSON</title>
  </head>
  <script src="jokes.js"></script>
  <script>
    console.log(jokes);
  </script>
</html>

```

Vous pourrez utiliser le tableau `jokes` librement dans votre code.

Vous pourriez également utiliser les [modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) JavaScript pour faire la même chose, mais cela est un peu en dehors du cadre de cet article.

Mais que faire si vous voulez travailler avec des fichiers JSON locaux et que vous avez Node.js installé ? Regardons comment faire cela maintenant.

## Comment analyser JSON dans Node.js

Node.js est un environnement d'exécution JavaScript qui vous permet d'exécuter JavaScript en dehors du navigateur. Vous pouvez tout lire sur [Node.js ici](https://www.freecodecamp.org/news/the-definitive-node-js-handbook-6912378afc6e/).

Que vous utilisiez Node.js pour exécuter du code localement sur votre ordinateur, ou pour exécuter des applications web entières sur un serveur, il est bon de savoir comment travailler avec JSON.

Pour les exemples suivants, nous utiliserons le même fichier `jokes.json` :

```json
[
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "elgv2wkvt8ioag6xywykbq",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/elgv2wkvt8ioag6xywykbq",
    "value": "Le clavier de Chuck Norris n'a pas de touche Ctrl car rien ne contrôle Chuck Norris."
  },
  {
    "categories": ["dev"],
    "created_at": "2020-01-05 13:42:19.324003",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "ae-78cogr-cb6x9hluwqtw",
    "updated_at": "2020-01-05 13:42:19.324003",
    "url": "https://api.chucknorris.io/jokes/ae-78cogr-cb6x9hluwqtw",
    "value": "Il n'y a pas de touche Échap sur le clavier de Chuck Norris, car personne n'échappe à Chuck Norris."
  }
]

```

### Comment analyser un fichier JSON avec `require()`

Commençons par la méthode la plus simple.

Si vous avez un fichier JSON local, tout ce que vous avez à faire est d'utiliser `require()` pour le charger comme n'importe quel autre module Node.js :

```js
const jokes = require('./jokes.json');

```

Le fichier JSON sera analysé automatiquement pour vous et vous pourrez commencer à l'utiliser dans votre projet :

```js
const jokes = require('./jokes.json');

console.log(jokes[0].value); // "Le clavier de Chuck Norris n'a pas de touche Ctrl car rien ne contrôle Chuck Norris."

```

Notez que cela est synchrone, ce qui signifie que votre programme s'arrêtera jusqu'à ce qu'il analyse le fichier entier avant de continuer. Les très grands fichiers JSON peuvent ralentir votre programme, alors faites simplement attention à cela.

De plus, parce que l'analyse de JSON de cette manière charge l'ensemble dans la mémoire, il est préférable d'utiliser cette méthode pour les fichiers JSON statiques. Si le fichier JSON change pendant que votre programme est en cours d'exécution, vous n'aurez pas accès à ces changements jusqu'à ce que vous redémarriez votre programme et analysiez le fichier JSON mis à jour.

### Comment analyser un fichier JSON avec `fs.readFileSync(`) et `JSON.parse()`

C'est la méthode plus traditionnelle (pour ne pas dire mieux) pour analyser les fichiers JSON dans les projets Node.js – lire le fichier avec le module `fs` (file system), puis analyser avec `JSON.parse()`.

Voyons comment faire cela avec la méthode `fs.readFileSync()`. Tout d'abord, ajoutez le module `fs` à votre projet :

```js
const fs = require('fs');

```

Ensuite, créez une nouvelle variable pour stocker la sortie du fichier `jokes.json` et définissez-la égale à `fs.readFileSync()` :

```js
const fs = require('fs');
const jokesFile = fs.readFileSync();

```

`fs.readFileSync()` prend quelques arguments. Le premier est le chemin vers le fichier que vous voulez lire :

```js
const fs = require('fs');
const jokesFile = fs.readFileSync('./jokes.json');

```

Mais si vous journalisez `jokesFile` dans la console maintenant, vous verrez quelque chose comme ceci :

```
<Buffer 5b 0a 20 20 7b 0a 20 20 20 20 22 63 61 74 65 67 6f 72 69 65 73 22 3a 20 5b 22 64 65 76 22 5d 2c 0a 20 20 20 20 22 63 72 65 61 74 65 64 5f 61 74 22 3a ... 788 more bytes>
```

Cela signifie simplement que le module `fs` lit le fichier, mais il ne connaît pas l'encodage ou le format du fichier. `fs` peut être utilisé pour charger à peu près n'importe quel fichier, et pas seulement ceux basés sur du texte comme JSON, donc nous devons lui dire comment le fichier est encodé.

Pour les fichiers basés sur du texte, l'encodage est généralement `utf8` :

```js
const fs = require('fs');
const jokesFile = fs.readFileSync('./jokes.json', 'utf8');

```

Maintenant, si vous journalisez `jokesFile` dans la console, vous verrez le contenu du fichier.

Mais jusqu'à présent, nous lisons simplement le fichier, et c'est toujours une chaîne. Nous devrons utiliser une autre méthode pour analyser `jokesFile` en un objet JavaScript ou un tableau utilisable.

Pour cela, nous utiliserons `JSON.parse()` :

```js
const fs = require('fs');
const jokesFile = fs.readFileSync('./jokes.json', 'utf8');
const jokes = JSON.parse(jokesFile);

console.log(jokes[0].value); // "Le clavier de Chuck Norris n'a pas de touche Ctrl car rien ne contrôle Chuck Norris."

```

Comme le suggère le nom, `JSON.parse()` prend une chaîne JSON et l'analyse en un littéral d'objet JavaScript ou un tableau.

Comme avec la méthode `require` ci-dessus, `fs.readFileSync()` est une méthode synchrone, ce qui signifie qu'elle pourrait ralentir votre programme si elle lit un grand fichier, JSON ou autre.

De plus, il ne lit le fichier qu'une seule fois et le charge en mémoire. Si le fichier change, vous devrez relire le fichier à un moment donné. Pour faciliter les choses, vous pourriez vouloir créer une fonction simple pour lire les fichiers.

Voici à quoi cela pourrait ressembler :

```js
const fs = require('fs');
const readFile = path => fs.readFileSync(path, 'utf8');

const jokesFile1 = readFile('./jokes.json');
const jokes1 = JSON.parse(jokesFile1);

console.log(jokes1[0].value); // "Le clavier de Chuck Norris n'a pas de touche Ctrl car rien ne contrôle Chuck Norris."

// le fichier jokes.json change à un moment donné

const jokesFile2 = readFile('./jokes.json');
const jokes2 = JSON.parse(jokesFile2);

console.log(jokes2[0].value); // "Le clavier de Chuck Norris est entièrement composé de touches Cmd car Chuck Norris est toujours en commande."
```

### Comment analyser JSON avec `fs.readFile(`) et `JSON.parse()`

La méthode `fs.readFile()` est très similaire à `fs.readFileSync()`, sauf qu'elle fonctionne de manière asynchrone. C'est génial si vous avez un grand fichier à lire et que vous ne voulez pas qu'il bloque le reste de votre code.

Voici un exemple de base :

```js
const fs = require('fs');

fs.readFile('./jokes.json', 'utf8');
```

Jusqu'à présent, cela ressemble à ce que nous avons fait avec `fs.readFileSync()`, sauf que nous ne l'assignons pas à une variable comme `jokesFile`. Parce qu'il est asynchrone, tout code après `fs.readFile()` s'exécutera avant qu'il n'ait fini de lire le fichier.

Au lieu de cela, nous utiliserons une fonction de rappel et analyserons le JSON à l'intérieur :

```js
const fs = require('fs');

fs.readFile('./jokes.json', 'utf8', (err, data) => {
  if (err) console.error(err);
  const jokes = JSON.parse(data);

  console.log(jokes[0].value);
});

console.log("Cela s'exécutera en premier !");
```

Ce qui imprime ce qui suit dans la console :

```
Cela s'exécutera en premier !
Le clavier de Chuck Norris n'a pas de touche Ctrl car rien ne contrôle Chuck Norris.

```

Comme avec `fs.readFileSync()`, `fs.readFile()` charge le fichier en mémoire, ce qui signifie que vous devrez relire le fichier s'il change.

De plus, même si `fs.readFile()` est asynchrone, il charge éventuellement l'ensemble du fichier qu'il lit en mémoire. Si vous avez un fichier massif, il peut être préférable de regarder les [flux Node.js](https://www.freecodecamp.org/news/node-js-streams-everything-you-need-to-know-c9141306be93/) à la place.

### Comment stringifier JSON avec `JSON.stringify()` dans Node.js

Enfin, si vous analysez JSON avec Node.js, il y a de fortes chances que vous deviez retourner JSON à un moment donné, peut-être en tant que réponse d'API.

Heureusement, cela fonctionne de la même manière que dans le navigateur – utilisez simplement `JSON.stringify()` pour convertir les littéraux d'objet JavaScript ou les tableaux en une chaîne JSON :

```js
const newJoke = {
  categories: ['dev'],
  value: "Le clavier de Chuck Norris est entièrement composé de touches Cmd car Chuck Norris est toujours en commande."
};

console.log(JSON.stringify(newJoke)); // {"categories":["dev"],"value":"Le clavier de Chuck Norris est entièrement composé de touches Cmd car Chuck Norris est toujours en commande."}

```

Et c'est tout ! Nous avons couvert à peu près tout ce que vous devez savoir sur le travail avec JSON dans le navigateur et dans les projets Node.js.

Maintenant, allez-y et analysez ou stringifiez JSON à votre guise.

Ai-je manqué quelque chose ? Comment analysez-vous JSON dans vos projets ? Faites-le moi savoir sur [Twitter](https://twitter.com/kriskoishigawa).