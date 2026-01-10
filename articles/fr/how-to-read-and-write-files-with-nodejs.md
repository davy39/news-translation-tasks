---
title: Comment lire et écrire des fichiers avec Node.js
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2024-08-19T13:41:36.623Z'
originalURL: https://freecodecamp.org/news/how-to-read-and-write-files-with-nodejs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723804956795/2dbd964a-00c3-4489-819a-393b058ed1fd.png
tags:
- name: Node.js
  slug: nodejs
- name: JavaScript
  slug: javascript
seo_title: Comment lire et écrire des fichiers avec Node.js
seo_desc: Node.js is a powerful JavaScript runtime environment that lets you run JS
  code outside the browser. And a fundamental part of many Node.js applications involves
  reading and writing files – whether that's text, JSON, HTML, or other file formats.
  So yo...
---

Node.js est un environnement d'exécution JavaScript puissant qui vous permet d'exécuter du code JS en dehors du navigateur. Et une partie fondamentale de nombreuses applications Node.js implique la lecture et l'écriture de fichiers – qu'il s'agisse de texte, de JSON, de HTML ou d'autres formats de fichiers. Vous devez donc comprendre comment lire et écrire des fichiers.

Les fichiers sont l'épine dorsale du stockage des données. Node.js fournit un module 'fs' (file system) puissant pour interagir avec ces fichiers de manière transparente. Supposons que je souhaite lire un fichier JSON dans Node.js. Le module fs peut m'aider avec cela.

Dans ce tutoriel, j'expliquerai les fonctionnalités principales de ce module, explorerai diverses techniques pour lire différents types de fichiers et découvrirai quelques bonnes pratiques pour rendre vos opérations de gestion de fichiers plus fluides et plus efficaces.

Tout au long de ce tutoriel, nous couvrirons tout, de l'importation du package à son utilisation pour travailler avec des fichiers de manière asynchrone. Commençons ce voyage d'apprentissage des opérations de fichiers avec Node.js !

### Table des matières

* [Module fs de Node.js](#heading-module-fs-de-nodejs)
    
* [Prérequis](#heading-prerequis)
    
* [Comment lire et écrire des fichiers avec Node.js](#heading-comment-lire-et-ecrire-des-fichiers-avec-nodejs)
    
* [Façons de lire des fichiers dans Node.js](#heading-facons-de-lire-des-fichiers-dans-nodejs)
    
* [Conclusion](#heading-conclusion)
    

## Module `fs` de Node.js

Le module File System (fs) de Node.js est un composant essentiel de l'environnement d'exécution Node.js. Il fournit une variété de fonctionnalités pour interagir avec le système de fichiers de votre ordinateur.

Le module fs vous permet de lire, écrire, mettre à jour, supprimer et gérer des fichiers et des répertoires. Ce module est particulièrement utile pour gérer les opérations liées aux fichiers en modes synchrone et asynchrone.

Décomposons les aspects clés du module :

1. Le module fs, à sa base, fournit une collection d'API pour interagir avec le système de fichiers. Il offre des moyens d'effectuer des activités de base telles que la lecture du contenu des fichiers, l'écriture de données dans des fichiers, la création de répertoires, la suppression de fichiers, et ainsi de suite.
    
2. Le module inclut à la fois des méthodes synchrones et asynchrones pour interagir avec les fichiers. Les méthodes synchrones bloquent l'exécution du programme jusqu'à ce que l'opération soit terminée. Mais les méthodes asynchrones sont idéales pour les scénarios où nous devons effectuer des tâches concurrentes sans interrompre l'exécution de l'ensemble du programme.
    
3. Le module prend également en charge la gestion des répertoires, tels que la création de répertoires, la suppression de répertoires et la liste du contenu des répertoires.
    
4. Le module prend également en charge le travail avec des flux de fichiers, permettant une gestion efficace des grands fichiers en lisant ou en écrivant des données par morceaux sans charger l'intégralité du contenu en mémoire. Il facilite également l'utilisation de tampons pour la gestion des données binaires, ce qui aide pour des activités comme la transformation et la manipulation de données.
    

## Prérequis

Pour continuer avec le tutoriel, je recommande d'avoir les prérequis suivants :

1. **Compréhension de base de JavaScript** : Il est essentiel d'être familier avec JavaScript, car Node.js utilise JavaScript.
    
2. **Node.js installé** : Assurez-vous que Node.js est installé sur votre système. Vous pouvez télécharger et installer Node.js depuis son [site officiel](https://nodejs.org).

    
3. **Éditeur de texte/IDE** : Avoir un éditeur de texte ou un environnement de développement intégré (IDE) installé et prêt à l'emploi.
    

## Comment lire et écrire des fichiers avec Node.js

Examinons un exemple pour comprendre le processus de lecture et d'écriture de fichiers dans Node.js. Nous supposerons un scénario où nous avons deux fichiers – name.json et address.json.

Le contenu du fichier name.json ressemble à ceci :

```json
[

 { "id": 1, "name": "Alice" },

 { "id": 2, "name": "Bob" },

 { "id": 3, "name": "Charlie" }
]
```

Le contenu du fichier address.json ressemble à ceci :

```json
[

 { "id": 1, "address": "123 Main St" },

 { "id": 2, "address": "456 Elm St" },

 { "id": 3, "address": "789 Oak St" }
]
```

Notre objectif est de créer un fichier bio.json qui fusionne les informations d'identification, de nom et d'adresse, créant une structure comme suit :

```json
[
  {
    "id": 1,
    "name": "Alice",
    "address": "123 Main St"
  },
  {
    "id": 2,
    "name": "Bob",
    "address": "456 Elm St"
  },
  {
    "id": 3,
    "name": "Charlie",
    "address": "789 Oak St"
  }
]
```

Construisons l'application !

### Étape 1 : Importer les packages Node.js `path` et `fs`

Commençons par créer un fichier app.js. La première chose que nous ferons est d'importer la bibliothèque fs :

```javascript
const fs = require("fs");
```

### Étape 2 : Lire depuis les fichiers

Ensuite, lisons les données des deux fichiers en utilisant Node.js. Nous créerons une fonction utilitaire qui nous aide à lire ces fichiers facilement dans notre environnement Node.js.

```javascript
async function readJSONFile(filename) {
  try {
    const data = await fs.readFile(filename, "utf8");
    return JSON.parse(data);
  } catch (error) {
    console.error(`Error reading ${filename}: ${error}`);
    return [];
  }
}
```

Puisque nous utilisons des fichiers JSON dans notre exemple, nous avons défini une méthode readJSONFile dans notre code. Il s'agit d'une fonction JavaScript asynchrone qui prend un nom de fichier en entrée et vise à retourner le contenu JSON analysé de ce fichier.

Dans un bloc try, nous tentons de lire le fichier en utilisant fs.readFile dans Node avec le nom de fichier spécifié et le codage "utf8". Si cela réussit, la fonction analyse ensuite le contenu du fichier en JSON en utilisant JSON.parse et le retourne.

Si une erreur se produit lors de la lecture ou de l'analyse, le bloc catch prend le relais. Il enregistre l'erreur avec le nom de fichier et les détails, puis retourne un tableau vide au lieu de l'objet JSON attendu.

### Étape 3 : Implémenter la fonction principale

L'étape suivante consiste à créer une fonction principale où nous utilisons la méthode définie ci-dessus et combinons les données des deux fichiers pour créer un fichier bio.json.

```javascript
async function main() {
  try {
    const names = await readJSONFile("names.json");
    const addresses = await readJSONFile("address.json");

    const bioData = names.map((name) => {
      const matchingAddress = addresses.find(
        (address) => address.id === name.id
      );
      return { ...name, ...matchingAddress };
    });

    await fs.writeFile("bio.json", JSON.stringify(bioData, null, 2));
    console.log("bio.json created successfully!");
  } catch (error) {
    console.error("Error combining data:", error);
  }
}
```

Dans la fonction principale, nous lisons d'abord les deux fichiers JSON nommés `names.json` et `address.json` en utilisant la fonction readJSONFile. Les deux appels readJSONFile utilisent await, donc la fonction attend que les deux fichiers soient lus avant de continuer.

Ensuite, nous itérons à travers chaque `name` en utilisant une map, créant un nouveau `bioData` pour chacun. À l'intérieur de la boucle, il recherche une `address` correspondante dans la collection d'adresses en fonction de l'index en utilisant find.


La recherche compare `name.id` avec chaque `address.id` jusqu'à ce qu'elle trouve une correspondance. Si une correspondance est trouvée, la fonction combine les informations des deux fichiers. Elle utilise l'opérateur de propagation (...) pour fusionner toutes les propriétés des deux objets en un seul nouvel objet `bioData`. Si aucune adresse correspondante n'est trouvée, l'objet `bioData` n'aura que les informations de nom.

Une fois que tous les objets `bioData` sont préparés, la fonction les écrit en tant que nouveau fichier JSON nommé `bio.json` en utilisant `fs.writeFile`. Ce processus d'écriture utilise également await, garantissant que le fichier est créé avant de continuer.


Le bloc try assure une exécution fluide, tandis que le bloc catch prend en charge les erreurs comme les fichiers manquants ou les données incorrectes. Si une erreur se produit, un message d'erreur générique et les détails spécifiques de l'erreur sont enregistrés pour le débogage.

### Code complet

Notre code complet ressemble à ceci :

```javascript
const fs = require("fs").promises;

async function readJSONFile(filename) {
  try {
    const data = await fs.readFile(filename, "utf8");
    return JSON.parse(data);
  } catch (error) {
    console.error(`Error reading ${filename}: ${error}`);
    return [];
  }
}

async function main() {
  try {
    const names = await readJSONFile("names.json");
    const addresses = await readJSONFile("address.json");

    const bioData = names.map((name) => {
      const matchingAddress = addresses.find(
        (address) => address.id === name.id
      );
      return { ...name, ...matchingAddress };
    });

    await fs.writeFile("bio.json", JSON.stringify(bioData, null, 2));
    console.log("bio.json created successfully!");
  } catch (error) {
    console.error("Error combining data:", error);
  }
}

// Execute the main method
main();
```

Nous pouvons exécuter l'application en utilisant la commande suivante :

```bash
node app.js
```

Une fois l'application exécutée, nous voyons les logs suivants dans le terminal si tout se passe bien :

```bash
bio.json created successfully!
```

Cela indique que le fichier bio.json a été créé avec succès. Le contenu du fichier devrait ressembler à ceci :

```json
[
  {
    "id": 1,
    "name": "Alice",
    "address": "123 Main St"
  },
  {
    "id": 2,
    "name": "Bob",
    "address": "456 Elm St"
  },
  {
    "id": 3,
    "name": "Charlie",
    "address": "789 Oak St"
  }
]
```

## Façons de lire des fichiers dans Node.js

Pour lire des fichiers dans Node.js, nous utilisons principalement deux méthodes : `fs.readFile()` et `fs.readFileSync()`. La différence réside dans leur nature synchrone et asynchrone.

### Méthode `fs.readFile()`

La méthode `fs.readFile()` dans Node.js est asynchrone. Elle lit le contenu de l'ensemble du fichier sans bloquer les autres opérations. Cela la rend adaptée aux scénarios où les opérations d'E/S non bloquantes sont essentielles.

En termes simples, la fonction permet à d'autres opérations de continuer pendant que la lecture a lieu. Elle accepte les trois paramètres suivants :

1. path : le chemin vers le fichier à lire.
    
2. encoding : optionnel, spécifie le codage du fichier (par exemple, "utf8"). Par défaut, "utf8" si non fourni.
    
3. fonction de rappel : optionnelle, une fonction à appeler lorsque le fichier est lu. La fonction reçoit trois arguments : error, data et buffer.
    

Regardons un exemple :

```javascript
const fs = require("fs");

fs.readFile("data.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data); // data will be a string containing the content of the file
  }
});
```

### Méthode `fs.readFileSync()`

La méthode `fs.readFileSync()` est synchrone. Elle lit le contenu du fichier de manière synchrone, arrêtant l'exécution ultérieure jusqu'à ce que le fichier soit complètement lu. Cette méthode est bénéfique dans les scénarios où nous nécessitons un traitement synchrone.

Elle ne prend que deux paramètres :

1. path : le chemin vers le fichier à lire
    
2. encoding : optionnel, spécifie le codage du fichier (par exemple, "utf8"). Par défaut, "utf8" si non fourni.
    

Regardons un exemple :

```javascript
const fs = require("fs");

try {
  const data = fs.readFileSync("data.txt", "utf8");
  console.log(data); // data will be a string containing the content of the file
} catch (err) {
  console.error(err);
}
```

### `fs.readFile()` vs `fs.readFileSync()`

Pour comprendre la différence entre les méthodes `readFile` et `readFileSync` de Node.js, nous allons écrire deux programmes et surveiller leur flux d'exécution.

Commençons par la méthode `fs.readFile()`.

```javascript
const fs = require("fs");

fs.readFile("example.txt", "utf8", (err, data) => {
  console.log("Content from readFile:", data);
});

console.log("Completed reading file content asynchronously");
```

Output:

```bash
Completed reading file content asynchronously
Content from readFile: freeCodeCamp is awesome!
```

En raison de la nature asynchrone de `fs.readFile()`, le code après `fs.readFile()` n'attend pas que l'opération de lecture du fichier se termine. Ainsi, le message "Completed reading file content synchronously" est immédiatement enregistré dans la console, montrant que le code suivant continue de s'exécuter sans attendre la fin de la lecture du fichier.

Finalement, lorsque l'opération de lecture du fichier est terminée, la fonction de rappel s'exécute et enregistre le contenu du fichier.

Ensuite, voyons l'exécution de la méthode `fs.readFileSync()`.

```javascript
const fs = require("fs");

const data = fs.readFileSync("data.txt", "utf8");
console.log("Content from readFileSync:", data);

console.log("Completed reading file content synchronously");
```

Output:

```bash
Content from readFileSync: freeCodeCamp is awesome!
Completed reading file content synchronously
```

En revanche, `fs.readFileSync()` lit le fichier data.txt de manière synchrone, bloquant l'exécution du code jusqu'à ce que le fichier soit complètement lu. Par conséquent, le code continue son exécution uniquement après la fin de l'opération de lecture du fichier.

À cause de cela, le message "Completed reading file content synchronously" est enregistré après avoir lu avec succès le contenu du fichier.

Maintenant, nous connaissons la différence entre les deux méthodes. Comprendre cette différence est important car cela impacte le flux du programme, surtout dans les scénarios où le timing et les opérations de blocage sont des considérations critiques dans les applications Node.js.

### Comment lire un fichier texte

Il est assez simple de lire un fichier texte dans Node.js, et nous l'avons fait tout au long du tutoriel. Supposons que nous avons un fichier appelé message.txt avec le contenu suivant :

```plaintext
Learn Node.js with freeCodeCamp
```

Maintenant, nous voulons lire le contenu de ce fichier. Nous pouvons le faire comme ceci :

```javascript
const fs = require("fs");

fs.readFile("message.txt", "utf8", (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
```

La fonction de rappel retourne le contenu du fichier dans une variable data. Puisque nous avons défini le codage sur "utf8", la valeur de data est une chaîne. Nous pouvons donc effectuer des opérations de chaîne sur la variable data.

```javascript
const fs = require("fs");

fs.readFile("message.txt", "utf8", (err, data) => {
  if (err) {
    console.log(err);
  } else {
      let splittedWords = data.split(" ");
      console.log(splittedWords);
  }
});
```

Dans le code ci-dessus, nous divisons la variable data en utilisant un espace. Ainsi, splittedWords sera un tableau de chaînes contenant la valeur suivante :

```javascript
[ 'Learn', 'Node.js', 'with', 'freeCodeCamp' ]
```

### Comment lire des fichiers HTML

La lecture de fichiers HTML suit une approche similaire à la lecture de fichiers texte dans Node.js. Nous pouvons utiliser le module `fs` pour lire des fichiers HTML :

```javascript
const fs = require("fs");

fs.readFile("index.html", "utf8", (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
```

Nous pouvons ensuite utiliser le contenu HTML pour un traitement ultérieur, comme le rendre avec le package `http` de Node.js.

### Comment lire des fichiers par URL

La lecture de fichiers par URL dans Node.js implique des étapes supplémentaires au-delà du module fs natif. Typiquement, nous aurons besoin d'utiliser des modules supplémentaires comme `http` ou `axios` pour récupérer le contenu d'un fichier à partir d'une URL.

```javascript
const fs = require("fs");
const https = require("https");

const file = fs.createWriteStream("data.txt");

https.get(
  "https://example-files.online-convert.com/document/txt/example.txt",
  (response) => {
    var stream = response.pipe(file);

    stream.on("finish", function () {
      console.log("done");
    });
  }
);
```

Tout d'abord, nous configurons un flux writable nommé file, associé au fichier local data.txt. Nous utilisons ensuite le module `https` de Node.js pour effectuer une requête HTTP GET à l'URL spécifiée. La méthode get déclenche une fonction de rappel lorsque nous recevons une réponse du serveur.


À l'intérieur du rappel, le script pipe la réponse directement dans le flux writable. Cette opération dirige efficacement les données reçues du serveur distant vers le fichier local data.txt, téléchargeant et écrivant essentiellement le contenu de manière concurrente.


Enfin, nous configurons un écouteur d'événements pour l'événement "finish" sur le flux. Cet événement se déclenche lorsque toutes les données ont été écrites avec succès dans le fichier. Une fois terminé, le script enregistre "done" dans la console, indiquant le téléchargement et l'écriture réussis du fichier.

### Comment lire un fichier JSON

Nous avons déjà vu comment nous pouvons lire un fichier JSON en utilisant le module fs. Supposons que nous voulons lire notre fichier bio.json créé précédemment. Ses données ressemblent à ceci :

```json
[
  {
    "id": 1,
    "name": "Alice",
    "address": "123 Main St"
  },
  {
    "id": 2,
    "name": "Bob",
    "address": "456 Elm St"
  },
  {
    "id": 3,
    "name": "Charlie",
    "address": "789 Oak St"
  }
]
```

Dans Node.js, nous lisons le JSON comme ceci :

```javascript
const fs = require("fs");

fs.readFile("bio.json", "utf8", (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
```

Avec cela, nos données JSON sont stockées dans la variable data sous forme de chaîne. Si nous le souhaitons, nous pouvons l'utiliser pour un traitement ultérieur. Supposons que nous voulons imprimer les détails de l'utilisateur :

```javascript
const fs = require("fs");

fs.readFile("bio.json", "utf8", (err, data) => {
  if (err) {
    console.log(err);
  } else {
    const users = JSON.parse(data);
    users.forEach((user) => {
      console.log(`${user.name} with ID ${user.id} lives at ${user.address}`);
    });
  }
});
```

Output:

```bash
Alice with ID 1 lives at 123 Main St
Bob with ID 2 lives at 456 Elm St
Charlie with ID 3 lives at 789 Oak St
```

Dans le code ci-dessus, nous analysons d'abord la variable de données de chaîne en JSON et la stockons dans une variable `users`. Nous parcourons ensuite la variable `users` pour enregistrer le message requis.

### `fs.promises`

`fs.promises` fournit un ensemble de fonctions asynchrones pour interagir avec le système de fichiers dans Node.js. Ces fonctions sont basées sur des promesses et offrent un moyen plus lisible et efficace de gérer les opérations asynchrones par rapport aux rappels.

Avec `fs.promises`, nous n'avons pas besoin d'ajouter des rappels imbriqués – ce qui signifie que nous pouvons éviter l'enfer des rappels.

Une opération readFile de base avec `fs.promises` ressemble à ceci :

```javascript
const fs = require("fs").promises;

async function readTextFile() {
  try {
    const data = await fs.readFile("data.txt", "utf8");
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}

readTextFile();
```

## Conclusion

Dans ce tutoriel, nous avons exploré les techniques essentielles pour gérer les fichiers dans Node.js à l'aide du module fs.

De la compréhension de la lecture de fichiers synchrone et asynchrone avec des méthodes comme `fs.readFile()` et `fs.readFileSync()` au traitement de divers formats de fichiers tels que le texte, le HTML, le JSON, et même la lecture de fichiers à partir d'URL, nous avons couvert un ensemble de fonctionnalités. Nous avons également appris à connaître fs.promises, qui est une manière plus élégante de gérer les opérations de fichiers en utilisant des fonctions asynchrones.

### Questions fréquemment posées (FAQ)

#### 1. Comment lire un fichier de manière asynchrone dans Node.js ?

Il existe principalement deux façons de lire un fichier de manière asynchrone dans Node.js : en utilisant `fs.readFile()` et en utilisant `fs.promises`.

La méthode `fs.readFile()` utilise des rappels pour gérer l'opération. Nous fournissons une fonction de rappel qui sera appelée avec les données du fichier (ou une erreur) lorsque la lecture est terminée.

Mais `fs.promises` offre une approche basée sur les promesses. Nous pouvons utiliser la fonction `readFile` avec await pour attendre la fin de la lecture et accéder directement aux données.

#### 2. Comment puis-je vérifier si un fichier existe avant de le lire ou de l'écrire dans Node.js ?

Il existe deux méthodes pour vérifier si un fichier existe : en utilisant `fs.stat` et en utilisant `fs.promises.access`.

La méthode `fs.stat` vérifie de manière synchrone si un fichier existe et retourne des informations à son sujet comme la taille et l'heure d'accès. La méthode `fs.promises.access` vérifie de manière asynchrone si un fichier existe et retourne une promesse qui se résout ou se rejette en fonction de l'existence du fichier.

#### 3. Comment puis-je gérer les erreurs lors de la lecture ou de l'écriture de fichiers dans Node.js ?

Pour gérer les erreurs lors de la lecture ou de l'écriture de fichiers dans Node.js, nous pouvons utiliser des rappels avec erreur en premier ou des promesses avec des blocs try-catch.