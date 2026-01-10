---
title: Comment créer une application en ligne de commande CRUD avec Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-06T15:59:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-command-line-application-with-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-hitesh-choudhary-1261427.jpg
tags:
- name: command line
  slug: command-line
- name: crud
  slug: crud
- name: node js
  slug: node-js
seo_title: Comment créer une application en ligne de commande CRUD avec Node.js
seo_desc: "By Njoku Samson Ebere\nIf you're looking for a tutorial to teach you the\
  \ basics of Nodejs and the command line, you're in the right place.  \nYou can use\
  \ JavaScript to build almost any software (web, mobile, bots, and so on). The reason\
  \ is that compute..."
---

Par Njoku Samson Ebere

Si vous cherchez un tutoriel pour vous apprendre les bases de [Nodejs](https://nodejs.org/en/) et de la ligne de commande, vous êtes au bon endroit.  
  
Vous pouvez utiliser JavaScript pour construire presque n'importe quel logiciel (web, mobile, bots, etc.). La raison est que les ordinateurs ne dépendent plus uniquement des navigateurs pour comprendre le code JavaScript. Consultez cet article pour voir [Comment les ordinateurs comprennent le code JavaScript](https://dev.to/ebereplenty/how-computers-understand-javascript-code-k1n). 

Node.js est utilisé pour exécuter des applications backend écrites en JavaScript.   
  
Je vais vous apprendre à créer une application en ligne de commande qui peut lire, écrire, modifier et supprimer des données en utilisant Node.js. Elle ne nécessitera pas de connexion à des bases de données externes comme MySQL, MongoDB, Postgresql, etc. Voir le projet [ici](https://github.com/EBEREGIT/Nodejs_CLI_app).  
  
À la fin de l'article, vous devriez être capable de configurer un projet Node de base, manipuler des fichiers, utiliser des modules, naviguer dans les promesses, collecter des entrées, etc.

J'ai également ajouté des vidéos pour améliorer votre apprentissage.

## Prérequis

Vous n'avez besoin d'aucune connaissance préalable en programmation pour comprendre ce tutoriel.

%[https://www.youtube.com/watch?v=RQ4b0Ui1-3o&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=2&t=6s]

## Comment l'application terminée fonctionnera

L'application que nous allons construire sera capable de faire ce qui suit :

* Vérifier si une base de données existe
* Récupérer des données de la base de données
* Ajouter de nouvelles données à la base de données
* Mettre à jour la base de données avec de nouvelles données
* Supprimer des données de la base de données

## Comment installer Node et NPM

Veuillez vous rendre sur le [site web de Nodejs](https://nodejs.org/en/) et télécharger la version recommandée pour tous les utilisateurs. Installez-la une fois le téléchargement terminé.

Utilisez la commande suivante pour vérifier si l'installation a réussi :

* Pour Node

```
node -v
```

* Pour npm

```
npm -v
```

L'installation est réussie si chaque commande retourne un numéro de version.

## Comment configurer un projet Node.js

%[https://www.youtube.com/watch?v=8dlICKn-tQw&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=2]

Les étapes suivantes vous aideront à configurer votre projet :  
  
Ouvrez votre terminal ou CMD et créez le répertoire du projet :

```
mkdir node_CLI_app
```

Naviguez dans le répertoire :

```
cd node_CLI_app
```

Initialisez le projet :

```
npm init	
```

Cela posera quelques questions. Appuyez sur la touche Entrée pour chaque invite.   
  
Un nouveau fichier (`package.json`) devrait avoir été ajouté à votre répertoire de projet. Nous utiliserons ce fichier pour ajouter du code externe (module) au projet.  
  
Ajoutez la ligne suivante avant l'accolade fermante (`}`) pour activer l'import ES6 :

```
"type": "module"
```

Cela complète la configuration du projet !

## Comment installer les dépendances

Vous vous souviendrez que le fichier `package.json` sert à ajouter du code externe au projet. Ce code externe est également appelé Dépendances, Modules ou Paquets. Il est écrit par d'autres programmeurs (généralement gratuitement) pour aider les autres à construire des applications plus rapidement. Vous en trouverez beaucoup sur le [site web de npm](https://www.npmjs.com/).  
  
Nous avons besoin de deux (2) paquets pour ce projet : [inquirer](https://www.npmjs.com/package/inquirer) et [uuid](https://www.npmjs.com/package/uuid). Je vais vous montrer comment les installer dans cette section.  
  
L'installation des paquets suit ce modèle :

```
npm install <package_name>
```

Nous pouvons installer plus d'un paquet à la fois en séparant les noms des paquets par un espace :

```
npm install <package_name_1> <package_name_2> <package_name_3>
```

La commande `install` peut être remplacée par `i` pour plus de commodité.  
  
Exécutez donc la commande suivante pour installer les paquets :

```
npm i inquirer uuid
```

Votre fichier package.json devrait avoir les lignes de code suivantes ajoutées une fois l'installation terminée :

```javascript

  "dependencies": {
    "inquirer": "^9.1.4",
    "uuid": "^9.0.0"
  }
```

Les numéros de version peuvent différer, mais ce n'est pas grave.

Vous remarquerez également qu'un fichier (`package.lock.json`) et un dossier (`node_modules`) ont été ajoutés. Vous n'avez pas à vous en soucier. Sachez simplement qu'ils aident à gérer le code externe que nous venons d'ajouter.

Cela complète l'installation des dépendances !

## Comment créer un nouveau fichier à partir du terminal

Vous pouvez créer un fichier à partir du terminal en utilisant la commande suivante :

* Sur Mac :

```
touch <file_name>
```

* Sur Windows :

```
echo.><file_name>
```

Vous pouvez également créer plus d'un fichier à la fois en séparant les fichiers par un espace. C'est ainsi que nous allons générer les fichiers pour ce projet :

```
touch addData.js removeData.js retrieveData.js updateData.js queryDB.js dbFileCheck.js
```

Chacun de ces fichiers jouera un rôle unique dans l'application.

* `addData.js` ajoute des données à la base de données. Il fabrique également le fichier de base de données s'il n'existe pas.
* `removeData.js` supprime les données sélectionnées.
* `retrieveData.js` récupère toutes les données.
* `updateData.js` modifie les données.
* `queryDB.js` vérifie si une base de données existe et exécute une fonction qui lui est passée.
* `dbFileCheck.js` confirme si le fichier de base de données a été créé.

Il y a un autre fichier que nous n'avons pas créé : le fichier de base de données (`db.json`). Nous allons le générer automatiquement en utilisant notre code.

## Comment vérifier si un fichier existe

%[https://www.youtube.com/watch?v=V9dmEXCnY-8&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=3]

Node.js fournit un module intégré pour manipuler les fichiers - [file system](https://nodejs.org/api/fs.html) (fs). L'une des méthodes que contient le module est la méthode `existsSync`. Elle retourne `true` ou `false` selon que le fichier a été créé ou non. Je vais utiliser cela pour vérifier si le fichier `db.json` est dans le projet. Voir le code ci-dessous :

```javascript
  import fs from "fs";
  import { exit } from "process";  
  
  if (fs.existsSync("db.json")) {
    console.log("Le fichier existe !");
    exit(1);
  }
```

La méthode `exit` termine un processus.

C'est ce que nous voulons faire dans le fichier `dbFileCheck.js`. Cependant, nous voulons inverser le résultat en ajoutant un `!` avant la méthode `fs.existsSync` comme ceci :

```javascript
  import fs from "fs";
  import { exit } from "process";  
  
  if (!fs.existsSync("db.json")) {
    console.log("Le fichier n'existe pas !");
    exit(1);
  }
```

Cela sera nécessaire lors de la construction d'autres fonctionnalités comme la mise à jour et la suppression de données. 

Comment ces fichiers vont-ils accéder à ce code ? C'est grâce à une structure modulaire. Cela implique de regrouper ce code et de le rendre accessible via d'autres fichiers du projet. La commande export rend cela possible :

```
import fs from "fs";
import { exit } from "process";

export default function dbFileCheck() {
  if (!fs.existsSync("db.json")) {
    console.log("La base de données est vide. Créez des données !");
    exit(1);
  }
}
```

Le code ci-dessus place le code dans une fonction (`dbFileCheck`) et l'exporte en utilisant la commande `export`. Cette fonction peut maintenant être importée et utilisée dans d'autres fichiers de ce projet.

Notez que le mot-clé `default` est nécessaire pour la première exportation d'un fichier.

## Comment interroger la base de données

Une autre méthode du `file system` est la méthode `readFile`. Elle retourne le contenu de tout fichier qui lui est passé. 

%[https://www.youtube.com/watch?v=ZmckWr9sH-w&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=4]

La méthode `readFile` prend deux paramètres : le fichier à lire et une fonction de rappel qui retourne le résultat de l'opération.  
  
Nous utiliserons le code suivant pour récupérer les données de notre base de données :

```javascript
import fs from "fs";

fs.readFile("db.json", function (err, data) {
  if (err) {
    console.log(err);
  }
  console.log(data.toString());
});
```

Le code ci-dessus importe le module du système de fichiers et tente de lire le fichier de la base de données. S'il y a une erreur, il retournera l'erreur. S'il n'y a pas d'erreurs, il retournera les données obtenues. 

La méthode `.toString()` attachée aux données retournées (`data.toString()`) est parce que les données récupérées sont de type `buffer` par défaut, ce qui n'est pas lisible.

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675074450995_Screenshot+2023-01-30+at+11.25.25.png)
_sortie du buffer_

Ouvrez votre projet dans un éditeur de code et collez ce code dans le fichier `queryDB.js`.  
  
Exécutez la commande ci-dessous pour voir si cela fonctionne :

```
node queryDB
```

La commande ci-dessus exécutera tout le code dans `queryDB.js`. L'extension `.js` est facultative. Elle s'exécutera dans les deux cas.

Le résultat de cette opération sera une erreur car nous n'avons pas le fichier.

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675074558543_Screenshot+2023-01-30+at+11.28.47.png)

Vous pouvez créer le fichier `db.json`, ajouter du contenu et vérifier la sortie.  
  
Mais nous ne voulons pas que notre application essaie de lire le fichier de la base de données s'il n'a pas été généré. Utilisez donc la méthode `existsSync` pour vérifier si le fichier a été créé. Voici comment je l'utilise dans le code ci-dessous :

```javascript
    import fs from "fs";

    if (fs.existsSync("db.json")) {
      fs.readFile("db.json", function (err, data) {
        if (err) {
          console.log(err);
        }
        console.log(data.toString());
      });
    } else {
      console.log("Aucune donnée disponible !");
    }
```

Le code ci-dessus vérifie si le fichier existe en passant le nom du fichier (`db.json`) à la méthode `fs.existsSync`. Si c'est vrai, alors il lit le fichier. Si c'est faux, il retourne une chaîne.

Maintenant que nous avons ce code propre, nous voulons le rendre encore plus robuste.

Puisque nous construisons une application CRUD, nous devons avoir accès et suivre les données retournées. J'ai introduit une nouvelle variable dans le code ci-dessous pour que cela se produise :

```javascript
    import fs from "fs";

    let info = [];
    if (fs.existsSync("db.json")) {
      fs.readFile("db.json", function (err, data) {
        if (err) {
          console.log(err);
        }
        info = JSON.parse(data.toString());
        console.log(info);
      });
    } else {
      console.log("Aucune donnée disponible !");
    }


```

Le code ci-dessus a maintenant une variable, `info`. Elle suit les données retournées. J'ai passé les données à travers la méthode `JSON.parse` pour convertir les données de chaîne en tableau. 

Nous pouvons maintenant manipuler `info` comme nous le jugeons approprié. Nous devons exporter le code et accepter une fonction pour rendre cela possible. Cette fonction prendra la variable `info` comme entrée et l'utilisera comme requis.

```javascript
import fs from "fs";

export default async function queryDB(externalFunction) {
  try {
    let info = [];

    if (fs.existsSync("db.json")) {
      await fs.readFile("db.json", function (err, data) {
        info = JSON.parse(data.toString());
        console.log(info);

        if (err) {
          console.log(err);
          return;
        }

        if (externalFunction && !err) {
          externalFunction(info);
          return;
        }
      });
    } else {
      if (externalFunction) {
        externalFunction(info);
        return;
      }
    }
  } catch (error) {
    console.error(`Quelque chose s'est produit : ${error.message}`);
  }
}
```

Ce code prend une fonction et l'exécute uniquement s'il n'y a pas d'erreurs. Cependant, il y aura une exception - lors de l'ajout de données. Dans ce cas, la base de données sera créée.

Le bloc [`try...catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) aide à détecter les erreurs, et les mots-clés [`async`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) [`await`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) sont utilisés lors de l'exécution de code qui prendra beaucoup de temps à s'exécuter.

Le fichier `queryDB.js` ne retournera plus aucune sortie lorsque nous exécuterons la commande `node queryDB`. Mais ce n'est pas grave. Nous la déclencherons à partir d'autres fichiers.

## Comment ajouter des données à un fichier

Dans cette section, je vais vous apprendre à ajouter des données au magasin. Le fichier pour cette section est le fichier `addData.js`.

%[https://www.youtube.com/watch?v=vi0unBmidkE&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=5]

Nous commencerons par importer tous les modules nécessaires :

```javascript
import inquirer from "inquirer";
import fs from "fs";
import { v4 as uuidv4 } from "uuid";
import queryDB from "./queryDB.js";
```

Ensuite, créez le modèle de base pour la fonction :

```
export default async function addData(info) {
  try {
    
  } catch (error) {
    console.log("Quelque chose s'est mal passé !", error);
  }
}

```

Cela ressemble à ce que nous avons fait auparavant. Tout le code que nous allons écrire ensuite ira dans le bloc `try...`. Le tableau `info` passé dans la fonction provient du fichier `queryDB`.  
  
La première chose à faire dans le bloc `try...` est de collecter les données à stocker. Nous allons utiliser [`inquirer`](https://www.npmjs.com/package/inquirer) pour cela avec le code ci-dessous :

```javascript
const answers = await inquirer.prompt([
      {
        type: "input",
        name: "name",
        message: "Quel est votre nom ?",
      },
      {
        type: "number",
        name: "phone",
        message: "Quel est votre téléphone ?",
      },
      {
        type: "list",
        name: "age",
        message: "Êtes-vous un adulte ?",
        choices: [
          { name: "Y", value: "Adult" },
          { name: "N", value: "Minor" },
        ],
      },
    ]);
```

Le package `inquirer` aide à construire des interfaces de ligne de commande interactives. Il contient une méthode appelée `prompt` utilisée pour demander des entrées. Il prend un tableau de questions au format objet. Chaque objet doit avoir les clés `name`, `type` et `message`. 

La clé `choices` est facultative. Elle est utilisée lorsqu'il y a une liste d'options.

Donc, le code ci-dessus collecte trois (3) entrées (nom, téléphone et âge) et les stocke dans une variable appelée `answers`.

Ensuite, nous attribuons à cet ensemble d'entrées un ID unique en appelant la fonction `uuidv4()` et nous poussons tout dans le tableau `info` :

```javascript
    const data = {
      id: uuidv4(),
      name: answers.name,
      phone: answers.phone,
      age: answers.age,
    };
    info.push(data);
```

Enfin, nous vérifions si le fichier de la base de données existe. Nous mettrons à jour la base de données avec les nouvelles données si le fichier a été créé ou nous le créerons et ajouterons les nouvelles données si c'est faux.

```javascript
    if (fs.existsSync("db.json")) {
      createDetails(info);
    } else {
      fs.appendFile("db.json", "[]", (err) => {
        if (err) {
          console.log("Impossible de créer db.json", err);
          return;
        }
        createDetails(info);
      });
    }
```

La fonction `createDetails` sera utilisée pour écraser les données de la base de données. Je vais la créer dans un instant.  
  
Dans le bloc `else` (si le fichier n'existe pas), j'ai créé le fichier en utilisant la méthode `appendFile` du système de fichiers. Cette méthode est utilisée pour créer un fichier s'il n'est pas déjà là et ajouter ou append des données au bas du fichier. 

J'ajoute `[]` au fichier. Donc le fichier nouvellement créé n'aura que `[]` dedans. J'ai appelé la fonction `createDetails` ensuite pour ajouter les données collectées à partir de la CLI.  
  
Veuillez taper le code suivant pour la fonction createDetails sous la fonction addData. 

```javascript
async function createDetails(info) {
  await fs.writeFile("db.json", JSON.stringify(info), function (err) {
    if (err) {
      console.log(err);
    }
    console.log("sauvegardé !");
  });
}
```

Cette fonction utilise la méthode `writeFile` du système de fichiers pour écraser la base de données avec les données actuelles. J'utilise `JSON.stringify` pour convertir la variable `info` en une chaîne car c'est le format acceptable lors de l'écriture dans un fichier. Cela explique également pourquoi j'ai utilisé `JSON.parse` pour la convertir en type d'origine lorsque je l'ai récupérée dans la section précédente.  
  
`writeFile` est différent de `appendFile` car `writeFile` écrase un fichier tandis que `appendFile` ajoute au contenu existant. Ils sont similaires en ce sens que les deux méthodes créeront le fichier s'il n'a pas été créé.

La dernière chose à faire dans ce fichier est d'invoquer ou d'appeler la fonction. La façon de faire cela est de taper son nom suivi de parenthèses ouvrantes et fermantes comme ceci :

```javascript
addData();
```

Cela pourrait fonctionner correctement, mais cela ne ferait pas ce que nous voulons. Nous devons passer la fonction en tant qu'argument dans `queryDB` comme ceci :

```javascript
queryDB(addData);
```

Maintenant, `addData` pourra communiquer avec la fonction `queryDB`.

## Comment tester le fichier `addData`

Exécutez la commande ci-dessous pour tester si le fichier `addData` fonctionne comme prévu :

```
node addData
```

Il vous demandera des réponses. Remplissez les réponses. Après cela, votre écran devrait ressembler au mien :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675241012883_Screenshot+2023-02-01+at+09.42.57.png)
_sortie addData_

Il devrait également avoir auto-généré un fichier `db.json` avec les données que vous venez d'ajouter.

Et c'est tout pour le fichier `addData` !

## Comment récupérer des données

Cette section montre comment obtenir le contenu de la base de données. Tout ce dont vous avez besoin pour réaliser cette fonctionnalité est le code ci-dessous :

```javascript
import queryDB from "./queryDB.js";

queryDB();
```

Ce que fait le code, c'est importer la fonction `queryDB` et l'invoquer. Collez le code dans le fichier `retrieveData.js` et exécutez le fichier avec :

```
node retrieveData
```

Il retournera une sortie similaire à celle-ci :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675319554801_Screenshot+2023-02-02+at+07.29.43.png)
_sortie retrieveData.js_

Vous pourriez vous demander : pourquoi n'ai-je pas appelé cette fonction dans le fichier `queryDB` ? La raison est que le fichier effectue plus que simplement récupérer des données. Appeler la fonction `queryDB` dans son fichier altérera le résultat des autres fichiers.

## Comment modifier des données

Cette section se concentrera maintenant sur la façon de mettre à jour les données. Le modèle à suivre ici est :

* Collecter l'ID de l'utilisateur.
* Rechercher l'utilisateur.
* Retourner les données de l'utilisateur si l'utilisateur existe, et le définir comme option par défaut.
* Demander les informations mises à jour. La valeur initiale sera conservée si l'utilisateur appuie sur la touche `Entrée`.
* Enfin, écraser la base de données avec les informations mises à jour.

%[https://www.youtube.com/watch?v=UmshAmmU-44&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=6]

Commençons...  
  
Naviguez dans le fichier `updateData.js` et collez le code suivant :

```
import inquirer from "inquirer";
import fs from "fs";
import queryDB from "./queryDB.js";
import dbFileCheck from "./dbFileCheck.js";

export default async function updateData(info) {
  dbFileCheck();

  try {
    
  } catch (error) {
    console.log("Quelque chose s'est mal passé !", error);
  }
}
```

C'est le modèle de base pour la fonction `updateData`. La nouvelle chose ici est la fonction `dbFileCheck` (créée il y a un moment) pour terminer une opération si la base de données n'a pas été créée.   
  
Le reste du code sera à l'intérieur du bloc `try...`.

La première chose est de collecter l'ID de l'utilisateur avec ce code :

```
    const answers = await inquirer.prompt([
      {
        type: "input",
        name: "recordID",
        message: "Entrez l'ID de l'enregistrement",
      },
    ]);
```

La deuxième étape consiste à rechercher l'utilisateur :

```
    let current;

    info.forEach((element) => {
      if (element.id === answers.recordID) {
        current = element;

        updateDetails(current, info);
      }
    });
```

Le code ci-dessus recherche parmi les utilisateurs (`info`) et définit l'utilisateur trouvé sur la variable `current`. Enfin, `updateDetails` est appelé pour collecter les informations mises à jour et écraser la base de données avec les nouvelles données.

### Comment construire la fonction `updateDetails`

Cette partie montrera comment garder une trace des données initiales d'un utilisateur tout en collectant de nouvelles données. Elle mettra à jour la base de données avec les nouvelles données par la suite.  
  
Le code suivant est le modèle de base pour la fonction :

```
async function updateDetails(current, info) {
  try {
    
  } catch (error) {
    console.log("Quelque chose s'est mal passé !", error);
  }
}
```

Ce code va sous l'opération `updateData`.  
  
Le code ci-dessous va dans le bloc `try...`. Il est destiné à collecter les informations mises à jour de l'utilisateur.

```
  const feedbacks = await inquirer.prompt([
      {
        type: "input",
        default: current.name,
        name: "name",
        message: "Quel est votre nom ?",
      },
      {
        type: "number",
        default: current.phone,
        name: "phone",
        message: "Quel est votre téléphone ?",
      },
      {
        type: "list",
        default: current.age,
        name: "age",
        message: "Êtes-vous un adulte ?",
        choices: [
          { name: "Y", value: "Adult" },
          { name: "N", value: "Minor" },
        ],
      },
    ]);
```

La clé `default` est nouvelle. Elle contient une entrée qui sera utilisée si l'utilisateur n'en fournit pas. Elle suit les données actuelles de l'utilisateur pour ce code. Ainsi, l'utilisateur peut appuyer sur le bouton `Entrée` au lieu de saisir à nouveau l'ancienne valeur.  
  
Les détails de l'utilisateur doivent être mis à jour en conséquence en utilisant ce code :

```
    current.name = feedbacks.name;
    current.phone = feedbacks.phone;
    current.age = feedbacks.age;
```

Enfin, écraser la base de données avec la nouvelle valeur :

```
await fs.writeFile("db.json", JSON.stringify(info), function (err) {
      if (err) {
        console.log(err);
      }
      console.log("mis à jour");
    });
```

Appelez la fonction `updateData` pour tout rassembler :

```
queryDB(updateData)
```

### Comment tester le fichier `updateData`

Exécutez la commande ci-dessous pour voir comment la fonction `updateData` se comporte :

```
node updateData
```

Il vous demandera un ID. Entrez l'ID de n'importe quel enregistrement dans la base de données.  
  
Il vous demandera ensuite des informations mises à jour sur l'utilisateur. Remplissez les informations et appuyez sur `Entrée` pour tout détail qui n'a pas besoin d'une mise à jour. Le terminal devrait ressembler à ceci à la fin :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675324018105_Screenshot+2023-02-02+at+08.45.07.png)
_sortie updateData_

Cela conclut le fichier `updateData`. Les enregistrements peuvent maintenant être mis à jour.

## Comment supprimer des données

Une application CRUD ne peut pas être complète sans la partie DELETE. Ce sera le focus ici. Elle empruntera un peu aux sections précédentes. Donc ce ne sera pas trop à comprendre.

%[https://www.youtube.com/watch?v=JptWEtAtOeA&list=PLOvIwkWvHysNC83IAQZrxgkUZgA1k5WZE&index=7]

Vous allez commencer par taper le code suivant dans le fichier `removeData.js` :

```
import inquirer from "inquirer";
import fs from "fs";
import queryDB from "./queryDB.js";
import dbFileCheck from "./dbFileCheck.js";

export default async function removeData(info) {
  dbFileCheck();

  try {
    const answers = await inquirer.prompt([
      {
        type: "input",
        name: "recordID",
        message: "Entrez l'ID de l'enregistrement",
      },
    ]);

    let remnantData = [];
    info.forEach((element) => {
      if (element.id !== answers.recordID) {
        remnantData.push(element);
      }
    });

    fs.writeFile("db.json", JSON.stringify(remnantData), function (err) {
      if (err) {
        console.log(err);
      }
      console.log("Supprimé !");
    });
  } catch (error) {
    console.log("Quelque chose s'est mal passé !", error);
  }
}

```

Tout d'abord, le code ci-dessus collecte un ID.  
  
Ensuite, il utilise l'ID pour rechercher les données de la base de données et ne conserve que les données avec un ID différent dans le tableau `remnantData`.  
  
Enfin, il écrase la base de données avec les données mises à jour.  
  
Appelez la fonction removeData en bas pour tout rassembler comme ceci :

```
queryDB(removeData)
```

Maintenant, essayez de tester le fichier en utilisant cette commande :

```
node removeData
```

Voici ma sortie :

![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1675329363353_Screenshot+2023-02-02+at+10.15.12.png)
_sortie removeData_

## Conclusion

La meilleure façon d'apprendre à programmer est en construisant. Et certains des meilleurs projets à construire sont des applications CRUD car elles couvrent les bases de ce qu'un projet professionnel nécessite. C'est ce que j'ai fait dans ce tutoriel.  
  
Je vous ai appris les bases de Nodejs en construisant une application qui crée, lit, met à jour et supprime des enregistrements. J'ai couvert des concepts tels que la lecture de fichiers, l'écriture dans des fichiers, les boucles, les instructions conditionnelles, les modules et les opérations CLI.  
  
Tous les fichiers de ce tutoriel sont sur [GitHub](https://github.com/EBEREGIT/Nodejs_CLI_app).  
  
Vous avez maintenant toutes les bases nécessaires pour commencer à construire des applications en utilisant Nodejs. Une chose que j'aimerais que vous essayiez est de mettre à jour ou de supprimer plus d'un enregistrement à la fois.

J'ai quelques autres tutoriels sur Nodejs, et je suggère que vous les suiviez dans cet ordre pour développer vos compétences :

* [Comment construire un serveur sécurisé avec Node.js et Express et télécharger des images avec Cloudinary](https://www.freecodecamp.org/news/build-a-secure-server-with-node-and-express/)
* [Comment construire et déployer une application backend avec Express, Postgres, Github et Heroku](https://www.freecodecamp.org/news/how-to-build-a-backend-application/)
* [Comment construire une application d'authentification Full-Stack avec React, Express, MongoDB, Heroku et Netlify](https://www.freecodecamp.org/news/how-to-build-a-fullstack-authentication-system-with-react-express-mongodb-heroku-and-netlify/)

Bonne construction !