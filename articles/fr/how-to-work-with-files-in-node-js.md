---
title: Comment travailler avec des fichiers dans Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-11T21:16:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-files-in-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/working-with-files.png
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: Comment travailler avec des fichiers dans Node.js
seo_desc: 'By Oluwatise Okuwobi

  JavaScript is a popular programming language among web developers. But when it was
  first released, only front end developers enjoyed all of the fun it had to offer,
  since you couldn''t run JavaScript outside the browser.

  But then ...'
---

Par Oluwatise Okuwobi

JavaScript est un langage de programmation populaire parmi les développeurs web. Mais lorsqu'il a été publié pour la première fois, seuls les développeurs front-end profitaient de tout le plaisir qu'il offrait, car vous ne pouviez pas exécuter JavaScript en dehors du navigateur.

Mais en 2009, la première version de Node.js a été publiée. Node est un environnement d'exécution JavaScript qui vous permet d'exécuter du code JS en dehors du navigateur, et il a donné aux développeurs back-end la joie d'utiliser JavaScript également.

Aujourd'hui, Node.js alimente le développement JavaScript back-end et est la 6ème technologie la plus utilisée parmi les programmeurs.

En tant que développeur back-end, vous devrez comprendre comment travailler efficacement avec les fichiers et les traiter dans Node.js. Et c'est ce que nous allons discuter ici.

## Avant de commencer à écrire du code...

Parlons des prérequis. Avez-vous besoin d'une quantité extensive de connaissances Node pour suivre cet article ? Non. Mais vous devriez comprendre une bonne quantité de JavaScript pour profiter pleinement de ce guide.

De plus, vous devez installer Node sur votre ordinateur si ce n'est pas déjà fait. Le processus d'installation est facile – tout ce que vous avez à faire est de télécharger [Node.js depuis le site officiel](https://nodejs.org/en/download) et de suivre les instructions d'installation et vous êtes prêt à partir.

## Le système de fichiers Node.js

Node agit comme un serveur de fichiers. Avec le module Node, vous pouvez travailler avec des fichiers sur vos ordinateurs et effectuer diverses opérations. Lorsque vous construisez une application web, vous pourriez vouloir télécharger des images, un CV, des vidéos ou des documents sur le serveur. Eh bien, le système de fichiers Node a la capacité de faire tout cela et plus encore.

Puisque ce guide est adapté aux débutants, je vais d'abord expliquer ce que sont les modules Node en général avant de parler plus en détail du système de fichiers.

### Qu'est-ce que les modules Node ?

Au cas où vous ne seriez pas familier avec le terme, les modules Node sont simplement du code JavaScript réutilisable. Vous pouvez facilement importer des modules tout au long de votre projet. Le but des modules est de s'assurer que vous ne répétez pas constamment le même code tout au long d'un projet.

Il existe plusieurs types de modules Node – modules locaux, modules intégrés et modules tiers. Dans ce guide, nous nous concentrerons sur les modules intégrés.

Voici une liste des modules intégrés de Node :

* fs
* http
* url
* os
* path

Le fs est le module du système de fichiers dans Node. Tout devient clair maintenant, n'est-ce pas ? Il existe une bibliothèque complète de modules Node. Si vous voulez en savoir plus à leur sujet, vous devriez lire davantage sur [les modules Node et comment vous pouvez les utiliser](https://www.freecodecamp.org/news/what-are-node-modules/). Continuons !

## Comment travailler avec le module `fs` de Node

Le module `fs` vous permet d'effectuer plusieurs opérations impliquant des fichiers et des dossiers. Avec le module `fs`, vous pouvez :

* lire des fichiers
* créer des fichiers
* mettre à jour des fichiers
* supprimer des fichiers
* renommer des fichiers

Pour commencer dans ce monde de gestion de fichiers, nous allons d'abord créer un dossier. Ensuite, nous créerons un fichier JavaScript pour l'instant. Ouvrez le fichier JS avec VS Code ou tout autre éditeur de texte que vous préférez, et écrivons du code.

### Comment lire des fichiers

Pour lire les fichiers directement depuis votre ordinateur, vous devrez utiliser la méthode `fs.readFile()`. Pour que cela fonctionne, vous devrez créer le fichier que vous souhaitez lire. Supposons qu'il s'agit d'un fichier txt avec le contenu `hello world`. Appelons-le dummyText.txt.

Il existe plusieurs façons de lire un fichier avec Node – soit en utilisant le module `http`, qui lira votre fichier sur le localhost, soit en utilisant des promesses. Je vais vous montrer les deux, et laquelle est préférable.

Commençons par utiliser le module `http`. Ouvrez votre fichier JS, appelons-le `readfile.js`, et ajoutez le code suivant :

```
const http = require('http'); 
const fs = require('fs');

http.createServer(function (req, res) { 
   fs.readFile('dummyText.txt', function(err, data) { 
      res.writeHead(200, {'Content-type': 'text/html'}); 
      res.write(data);           
      return res.end(); 
    }); 
 }).listen(8080);
```

Enregistrez le code, puis ouvrez `cmd` dans le répertoire du fichier et exécutez Node readfile.js :

 `C:\Users\nodefilesystem>node readfile.js`

Visitez https://localhost:8080 pour voir vos résultats. Vous devriez voir le contenu du texte factice sur votre navigateur.

Maintenant, recréons cela avec des promesses. La méthode des promesses est un style de programmation plus moderne, car nous incorporerons la nouvelle syntaxe _async_ et _await_. Lisons notre fichier en utilisant des promesses.

```
// import promises 
const { readFile } = require('fs/promises'); 

async function readThisFile('./dummytext.txt') { 
  try { 
    const data = await readFile('/dummytext.txt');
    console.log(data.toString()); 
  } catch (error) { 
    console.error(`Got an error trying to read the file: {error.message}`); 
  } 
 }
```

Expliquons le code. Nous avons importé le module des promesses Node en utilisant le système de fichiers. Nous avons utilisé `fs/Promises` pour traiter nos fichiers avec des promesses.

Nous avons utilisé la méthode `readFile` pour traiter notre fichier que nous voulons lire. En utilisant des promesses, nous pouvons lire nos fichiers de manière asynchrone. À l'intérieur de la méthode `readFile`, nous avons le chemin vers notre `dummytext` que nous voulons lire, puis retourner le contenu du fichier.

Nous avons également utilisé une méthode de gestion des erreurs try-catch pour nous assurer que nous pouvons contrôler correctement ce que le message d'erreur indique. Donc, s'il y a quelque chose qui ne va pas avec le code avant la ligne catch, il affichera "Got an error trying to read the file", au lieu d'un message d'erreur désordonné.

La gestion des erreurs empêchera également le programme de s'arrêter lorsqu'il détecte une erreur. Avec notre code, le programme peut toujours reprendre même s'il est interrompu.

Si vous voulez en savoir plus sur cela, voici une excellente ressource de freeCodeCamp sur [la gestion des erreurs en JavaScript](https://www.freecodecamp.org/news/error-handling-and-try-catch-throw/).

### Comment créer des fichiers

Maintenant que nous sommes familiers avec la méthode des promesses pour travailler avec le système de fichiers, nous allons l'utiliser tout au long du reste du guide. Maintenant que nous savons comment lire le contenu d'un fichier existant, que diriez-vous d'apprendre à les créer ?

Pour créer un fichier, nous pouvons utiliser l'une des trois méthodes : `appendFile()`, `open()`, et `writeFile()`.

Ouvrons notre éditeur de texte et commençons par `appendFile()` :

```
const { appendFile} = require('fs/promises'); 

async function appendToFile('anotherDummyText.txt', 'i love node') { 

  try { 
    await appendFile(fileName, data, { flag: 'w' });                   console.log(`Appended data to ${fileName}`); 
  } catch (error) { 
    console.error(`Got an error trying to append the file: {error.message}`); 
  } 
 }
```

Expliquons un peu plus le code. Nous avons déjà appelé le module, et maintenant nous utilisons la méthode `appendFile` pour écrire dans le fichier que nous avons créé précédemment. Si le programme ne voit aucun fichier avec le nom que nous avons indiqué dans la fonction `appendToFile`, il le créera.

Nous avons également utilisé la méthode de gestion des erreurs try-catch pour nous assurer de contrôler les erreurs.

Ensuite, nous travaillerons avec `WriteFile`. C'est presque le même code, mais avec quelques ajustements :

```
const { writeFile } = require('fs/promises'); 

async function writeToFile('dummyText.txt', 'using write method') { 
   try { 
     await writeFile(fileName, data); 
     console.log(`Wrote data to ${fileName}`); 
   } catch (error) { 
     console.error(`Got an error trying to write the file: ${error.message}`); 
   } 
 }
```

Maintenant, nous utilisons la méthode `writeFile` qui crée le fichier directement et y ajoute les données. Notez également le mot-clé `await`, dont nous avons besoin pour exécuter une promesse JavaScript réussie.

### Comment renommer des fichiers

Une autre partie majeure du travail avec des fichiers consiste à renommer un fichier déjà existant. Voyons comment cela fonctionne :

```
const { rename } = require('fs/promises'); 

async function renameFile('dummytext.txt', 'changedDummyText.txt') { 
   try { 
     await rename(from, to); 
     console.log(`Renamed ${from} to ${to}`); 
   } catch (error) { 
     console.error(`Got an error trying to rename the file: ${error.message}`); 
   } 
 }
```

Comme vous pouvez le voir, notre fonction `async` a pris deux paramètres cette fois, le premier contiendra le nom actuel du document que nous allons changer, et le second contiendra le nouveau nom avec lequel nous travaillons.

Nous avons également changé notre `dummyText.txt` en `changedDummyText.txt`.

### Comment supprimer des fichiers

Pour supprimer un fichier, nous devrons appeler la méthode `unlink`. Cette fois, au lieu d'avoir deux paramètres, nous n'en aurons qu'un seul : le nom, ou le chemin du fichier que vous souhaitez supprimer.

Nous utiliserons toujours notre méthode de gestion des erreurs try-catch pour contrôler nos erreurs, et enregistrer le nom du fichier qui a été supprimé sur la console.

```
const { unlink } = require('fs/promises'); 

async function deleteFile('./dummytext.txt') { 

   try { 
     await unlink(filePath); 
     console.log(`Deleted ${filePath}`); 
   } catch (error) { 
     console.error(`Got an error trying to delete the file: ${error.message}`); 
   } 
 }
```

### Comment mettre à jour des fichiers

Oui, j'ai mentionné que nous allons apprendre comment mettre à jour des fichiers également – mais si vous avez prêté une attention particulière, vous verrez que nous l'avons déjà fait.

Nous avons parlé de `appendFile()`, qui modifie essentiellement les informations clés, et vous permet d'écrire de nouveaux contenus dans le fichier. Nous avons également parlé de `writeFile()`, qui met à jour le contenu d'un fichier également.

## Conclusion

Nous voici, à la fin de ce guide. Récapitulons ce que nous avons appris dans ce tutoriel.

Tout d'abord, nous avons parlé de ce qu'est Node.js, et de l'importance du système de fichiers. Nous avons également appris ce que sont les modules Node. Tout cela est vital pour votre compréhension du reste du tutoriel.

Gardez à l'esprit qu'il existe plus d'opérations que vous pouvez effectuer avec le système de fichiers dans Node. Ce tutoriel n'a couvert que les bases et les fonctions principales. Lisez un peu plus à ce sujet et vous découvrirez beaucoup plus.

Si vous avez aimé cet article, [parlons-en sur Twitter](https://www.twitter.com/tiseysoft). J'adorerais me connecter avec chacun d'entre vous.