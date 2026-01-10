---
title: Comment commencer avec NodeJS – un guide pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-02T18:25:47.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/e5aa6e1c-fe02-4e17-bdb1-1622b97831e6.jpg
tags:
- name: 'Back end development '
  slug: back-end-development
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: node js
  slug: node-js
seo_title: Comment commencer avec NodeJS – un guide pour débutants
seo_desc: "By Krish Jaiswal\nHello folks! \U0001F44B Recently, I have been learning\
  \ about Node.js. So I decided to share my learnings with you here. \U0001F468‍\U0001F4BB\
  \nIn this tutorial, we'll take a high-level look at Node.js – what it is, and what\
  \ you can do with it. \nWe will be co..."
---

Par Krish Jaiswal

Salut à tous ! 👋 Récemmment, j'ai appris Node.js. J'ai donc décidé de partager mes apprentissages avec vous ici. 👨‍💻

Dans ce tutoriel, nous allons examiner Node.js de haut niveau – ce qu'il est et ce que vous pouvez faire avec. 

Nous allons couvrir tous les concepts importants de Node avec des exemples pratiques et de nombreux extraits de code. Cela vous donnera les connaissances de base nécessaires pour commencer le développement backend avec NodeJS.

Cet article est largement inspiré du **Cours complet NodeJS et Express** sur freeCodeCamp enseigné par John Smilga. Vous pouvez [le consulter ici si vous le souhaitez](https://www.freecodecamp.org/news/free-8-hour-node-express-course/).

## Voici ce que nous allons couvrir dans ce guide :

* [Qu'est-ce que NodeJS ?](#heading-quest-ce-que-node)
* [Variables globales](#heading-variables-globales)
* [Modules](#heading-modules-dans-nodejs)
* [Note courte sur `module.exports`](#heading-note-courte-sur-moduleexports)
* [Types de modules](#heading-types-de-modules-dans-node)
* [Programmation pilotée par événements](#heading-programmation-pilotee-par-evenements)
* [Création de notre premier serveur](#heading-creons-un-serveur)
* [Servons quelque chose d'intéressant !](https://www.freecodecamp.org/news/p/af44b49e-dac0-4ba4-abe6-32ad97ee5afe/Let's%20Serve%20Something%20Interesting)
* [Conclusion](#heading-conclusion)

# Qu'est-ce que Node ?

Node est un environnement dans lequel vous pouvez exécuter du code JavaScript "**En dehors du navigateur web**". Node est comme : "Hey tout le monde, vous me donnez votre code JS et je l'exécute 😊". Il utilise le moteur V8 de Google pour convertir le code JavaScript en code machine.

Puisque Node exécute du code JavaScript en dehors du navigateur web, cela signifie qu'il n'a pas accès à certaines fonctionnalités disponibles uniquement dans le navigateur, comme le DOM ou l'objet `window` ou même le `localStorage`.

Cela signifie qu'à tout moment dans votre code, vous ne pouvez pas taper `document.querySelector()` ou `alert()` car ceux-ci produiront des erreurs (c'est ce qui est montré dans l'image ci-dessous). 

**À retenir :** Node est destiné à la programmation côté serveur, tandis que ces fonctionnalités de navigateur sont destinées à la programmation côté client.

![Node ne connaît pas les API du navigateur](https://www.freecodecamp.org/news/content/images/2023/05/image-135.png)

Les développeurs front-end, ne soyez pas tristes 😢 – il y a plus ! Node vous fournit de nombreuses API et modules avec lesquels vous pouvez effectuer diverses opérations comme la gestion de fichiers, la création de serveurs, et bien plus encore. Avant de plonger dans NodeJS, commençons par l'installer sur notre machine.

## Comment installer NodeJS

L'installation de NodeJS est simple. Si vous avez déjà Node installé sur votre machine, vous pouvez sauter cette section. Sinon, suivez les instructions.

Voici les étapes pour télécharger NodeJS sur votre machine :

1. Rendez-vous sur [https://nodejs.org/](https://nodejs.org/)
2. Téléchargez la version LTS de NodeJS pour votre système d'exploitation
3. Exécutez l'installateur et suivez l'assistant d'installation. Répondez simplement Oui à toutes les questions.
4. Une fois l'installation terminée, ouvrez une nouvelle fenêtre de terminal ou d'invite de commande et exécutez la commande suivante pour vérifier que NodeJS est installé correctement : `node -v`. Si vous voyez la version de NodeJS imprimée dans votre terminal, félicitations ! Vous avez maintenant installé NodeJS sur votre machine.

**Remarque :** Si vous rencontrez des problèmes lors du processus d'installation, vous pouvez consulter la documentation officielle de NodeJS pour des instructions plus détaillées et des conseils de dépannage.

# Variables globales

Commençons cet article en apprenant quelques variables présentes dans NodeJS appelées variables globales. Ce sont essentiellement des variables qui stockent certaines données et peuvent être accessibles de n'importe où dans votre code – peu importe à quel point le code est imbriqué.

Vous devriez connaître ces variables globales couramment utilisées : 

* `__dirname` : Cette variable stocke le chemin vers le répertoire de travail actuel.
* `__filename` : Cette variable stocke le chemin vers le fichier de travail actuel.

Utilisons-les et voyons quelle valeur elles contiennent. Pour cela, créons un nouveau dossier appelé `NodeJSTut` sur votre `Bureau` et ouvrons-le avec votre éditeur de texte préféré (dans ce tutoriel, nous utiliserons VS Code). Créez un nouveau fichier appelé `app.js` et ouvrez un nouveau terminal intégré de VS Code. 

Collez le code suivant dans le fichier `app.js` et enregistrez-le :

```javascript
// Variable globale __dirname
console.log(__dirname);

// Variable globale __filename
console.log(__filename);
```

Pour exécuter ce code avec Node, tapez la commande suivante dans le terminal et appuyez sur Entrée : `node app.js`. Vous verrez le chemin absolu vers le répertoire de travail actuel et le chemin vers le fichier actuel imprimé dans le terminal. Voici à quoi ressemble la sortie dans mon cas :

```text
C:\Desktop\NodeJSTut
C:\Desktop\NodeJSTut\app.js
```

Vous pouvez créer vos propres variables globales qui peuvent être accessibles de n'importe où dans votre code. Vous pouvez le faire comme ceci :

```javascript
// Définir une variable globale dans NodeJS
global.myVariable = 'Hello World';

// Accéder à la variable globale
console.log(myVariable); // Sortie : Hello World

```

# Modules dans NodeJS

Dans Node.js, un module est essentiellement un bloc de code réutilisable qui peut être utilisé pour effectuer un ensemble spécifique de tâches ou fournir une fonctionnalité spécifique. Un module peut contenir des variables, des fonctions, des classes, des objets, ou tout autre code qui peut être utilisé pour accomplir une tâche ou un ensemble de tâches particulier.

Le but principal de l'utilisation des modules dans Node.js est d'aider à organiser le code en morceaux plus petits et plus faciles à gérer. Un module peut ensuite être importé à tout moment et utilisé de manière flexible, ce qui aide à créer des composants de code réutilisables qui peuvent être partagés entre plusieurs projets.

Pour comprendre cela, considérons cet exemple : Supposons que vous avez défini de nombreuses fonctions dans votre code qui fonctionnent avec un grand volume de données JSON. 

Perte de sommeil et augmentation des niveaux d'anxiété sont des effets secondaires courants de garder tout cela (fonctions + données + une autre logique) dans un seul fichier.

Alors vous, en tant que programmeur intelligent, avez pensé à faire un fichier séparé pour les données JSON et un fichier séparé pour stocker toutes les fonctions. Maintenant, vous pouvez simplement importer les données et les fonctions quand vous voulez et les utiliser en conséquence. Cette méthode augmente l'efficacité car la taille de votre fichier est considérablement réduite. C'est le concept des modules !

Voyons comment nous pouvons créer nos propres modules. Pour cela, nous allons écrire du code où nous allons définir une fonction appelée `sayHello()` dans un fichier appelé `hello.js`. Cette fonction acceptera un `name` comme paramètre et imprimera simplement un message de salutation dans la console.

Nous allons ensuite l'importer dans un autre fichier appelé `app.js` et l'utiliser là. N'est-ce pas intéressant 😊 ? Vérifions le code :

Voici le code dans le fichier `hello.js` :

```javascript
function sayHello(name){
    console.log(`Hello ${name}`);
}

module.exports = sayHello
```

Voici le code dans le fichier `app.js` :

```javascript
const sayHello = require('./hello.js');

sayHello('John');
sayHello('Peter');
sayHello('Rohit');
```

Le fichier `hello.js` peut être appelé le `module` dans ce cas. Chaque module a un objet appelé `exports` qui doit contenir toutes les choses que vous voulez exporter de ce module comme des variables ou des fonctions. Dans notre cas, nous définissons une fonction dans le fichier `hello.js` et l'exportons directement.

Le fichier `app.js` importe la fonction `sayHello()` de `hello.js` et la stocke dans la variable `sayHello`. Pour importer quelque chose d'un module, nous utilisons la méthode `require()` qui accepte le chemin vers le module. Maintenant, nous pouvons simplement invoquer la variable et passer un nom comme paramètre. L'exécution du code dans le fichier `app.js` produira la sortie suivante :

```javascript
Hello John
Hello Peter
Hello Rohit
```

# Note courte sur `module.exports`

Dans la section précédente de l'article, nous avons vu comment utiliser `module.exports`, mais j'ai pensé qu'il était important de comprendre comment il fonctionne un peu plus en détail. Par conséquent, cette section de l'article est comme un mini-tutoriel où nous verrons comment nous pouvons exporter une variable/fonction ainsi que plusieurs variables et fonctions en utilisant `module.exports`. Alors, commençons :

`module.exports` est un objet spécial dans NodeJS qui vous permet d'exporter des fonctions, des objets ou des valeurs d'un module, afin que d'autres modules puissent y accéder et les utiliser. Voici un exemple de la façon d'utiliser `module.exports` pour exporter une fonction d'un module :

```javascript
// myModule.js

function myFunction() {
  console.log('Hello from myFunction!');
}

module.exports = myFunction;
```

Dans cet exemple, nous définissons une fonction `myFunction` puis nous l'exportons en utilisant `module.exports`. D'autres modules peuvent maintenant nécessiter ce module et utiliser la fonction exportée :

```javascript
// app.js

const myFunction = require('./myModule');

myFunction(); // logs 'Hello from myFunction!'
```

Tout semble bien maintenant et la vie est belle. Mais le problème survient lorsque nous devons exporter plusieurs fonctions et variables d'un seul fichier. Le point est que lorsque vous utilisez `module.exports` plusieurs fois dans un seul module, il remplacera la valeur précédemment assignée par la nouvelle. Considérez ce code :

```javascript
// module.js

function myFunction() {
  console.log('Hello from myFunction!');
}

function myFunction2() {
  console.log('Hello from myFunction2!');
}

// Première exportation
module.exports = myFunction;

// Deuxième exportation
module.exports = myFunction2;
```

Dans cet exemple, nous exportons d'abord `myFunction()`. Mais nous remplaçons ensuite `module.exports` par une nouvelle fonction - `myFunction2()`. Par conséquent, seule la deuxième instruction d'exportation prendra effet, et la fonction `myFunction()` ne sera pas exportée.

Ce problème peut être résolu si vous attribuez `module.exports` à un objet qui contient toutes les fonctions que vous souhaitez exporter, comme ceci :

```javascript
// myModule.js

function myFunction1() {
  console.log('Hello from myFunction1!');
}

function myFunction2() {
  console.log('Hello from myFunction2!');
}

module.exports = {
  foo: 'bar',
  myFunction1: myFunction1,
  myFunction2: myFunction2
};
```

Dans cet exemple, nous exportons un objet avec trois propriétés : `foo`, `myFunction1`, et `myFunction2`. D'autres modules peuvent nécessiter ce module et accéder à ces propriétés :

```javascript
// app.js

const myModule = require('./myModule');

console.log(myModule.foo); // logs 'bar'
myModule.myFunction1(); // logs 'Hello from myFunction1!'
myModule.myFunction2(); // logs 'Hello from myFunction2!'
```

Pour résumer, vous pouvez utiliser `module.exports` autant de fois que vous le souhaitez dans votre code NodeJS, mais vous devez être conscient que chaque nouvelle attribution remplacera la précédente. Vous devez utiliser un objet pour regrouper plusieurs exportations ensemble.

# Types de modules dans Node

Il existe 2 types de modules dans NodeJS :

* **Modules intégrés** : Ce sont des modules inclus dans Node par défaut, vous pouvez donc les utiliser sans installation. Vous devez simplement les importer et commencer.
* **Modules externes** : Ce sont des modules créés par d'autres développeurs qui ne sont pas inclus par défaut. Vous devez donc les installer avant de les utiliser.

Voici une image des modules intégrés populaires dans NodeJS et ce que vous pouvez faire avec eux :

![Représentation tabulaire des différents modules intégrés dans NodeJS](https://www.freecodecamp.org/news/content/images/2023/05/image-137-1.png)

Passons en revue chacun de ces modules plus en détail pour en apprendre davantage sur ce qu'ils font.

## Le module OS

Le module OS (comme son nom l'indique) vous fournit des méthodes/fonctions avec lesquelles vous pouvez obtenir des informations sur votre système d'exploitation.

Pour utiliser ce module, la première étape est de l'importer comme ceci :

```javascript
const os = require('os');

```

Voici comment vous pouvez utiliser le module OS pour obtenir des informations sur le système d'exploitation :👋

```javascript
const os = require('os')

// os.uptime()
const systemUptime = os.uptime();

// os.userInfo()
const userInfo = os.userInfo();

// Nous allons stocker d'autres informations sur mon WindowsOS dans cet objet :
const otherInfo = {
    name: os.type(),
    release: os.release(),
    totalMem: os.totalmem(),
    freeMem: os.freemem(),
}

// Vérifions les résultats :
console.log(systemUptime);
console.log(userInfo);
console.log(otherInfo);
```

Voici la sortie du code ci-dessus : 

Notez que la sortie montre des informations sur le système d'exploitation Windows qui s'exécute sur mon système. La sortie pourrait être différente de la vôtre.

```text
521105
{
	uid: -1,
	gid: -1,
	username: 'krish',
	homedir: 'C:\\Users\\krish',
	shell: null
}
{
	name: 'Windows_NT',
	release: '10.0.22621',
	totalMem: 8215212032,
	freeMem: 1082208256
}
```

Analysons le code et la sortie ci-dessus :

* `os.uptime()` indique le temps de fonctionnement du système en secondes. Cette fonction retourne le nombre de secondes pendant lesquelles le système a fonctionné depuis son dernier redémarrage. Si vous regardez la première ligne de la sortie : `521105` est le nombre de secondes pendant lesquelles mon système a fonctionné depuis son dernier redémarrage. Bien sûr, ce sera différent pour vous.
* `os.userInfo()` donne des informations sur l'utilisateur actuel. Cette fonction retourne un objet avec des informations sur l'utilisateur actuel, y compris l'ID de l'utilisateur, l'ID du groupe, le nom d'utilisateur, le répertoire personnel et le shell par défaut. Voici la décomposition de la sortie dans mon cas :

```javascript
    {
        uid: -1,
        gid: -1,
        username: 'krish',
        homedir: 'C:\\Users\\krish',
        shell: null
    }

```

L'`uid` et le `gid` sont définis sur `-1` dans Windows, car Windows n'a pas le concept d'IDs d'utilisateur comme les systèmes basés sur Unix. Le `username` de mon OS est `krish` et le répertoire personnel est `'C:\\Users\\krish'`. Le `shell` est défini sur `null` car le concept d'un shell par défaut n'existe pas sur Windows. Windows a un programme d'interpréteur de commandes par défaut appelé Invite de commandes (cmd.exe), qui exécute des commandes et gère le système.

Les autres méthodes liées au module OS comme `os.type()`, `os.release()` et ainsi de suite, que vous avez vues dans le code ci-dessus, ont été utilisées dans l'objet `otherInfo`. Voici une décomposition de ce que font ces méthodes :

* `os.type()` - Indique le nom du système d'exploitation
* `os.release()` - Indique la version de publication du système d'exploitation
* `os.totalMem()` - Indique la quantité totale de mémoire disponible en octets
* `os.freeMem()` - Indique la quantité totale de mémoire libre disponible en octets

Voici les informations que les méthodes ci-dessus affichent sur mon OS :

```javascript
{
	name: 'WindowsNT', // Nom de mon OS
	release: '10.0.22621', // Version de publication de mon OS
	totalMem: 8215212032, // Mémoire totale disponible en octets (~ 8 Go)
 	freeMem: 1082208256 // Mémoire libre disponible en octets (~ 1 Go) 
}
```

## Le module PATH

Le module PATH est utile lorsque vous travaillez avec des chemins de fichiers et de répertoires. Il vous fournit diverses méthodes avec lesquelles vous pouvez :

* Joindre des segments de chemin ensemble
* Dire si un chemin est absolu ou non
* Obtenir la dernière portion/segment d'un chemin
* Obtenir l'extension de fichier à partir d'un chemin, et bien plus encore !

Vous pouvez voir le module PATH en action dans le code ci-dessous.

Code :

```javascript
// Importer le module 'path' en utilisant la méthode 'require()' :
const path = require('path')

// Attribuer un chemin à la variable myPath
const myPath = '/mnt/c/Desktop/NodeJSTut/app.js'

const pathInfo = {
    fileName: path.basename(myPath),
    folderName: path.dirname(myPath),
    fileExtension: path.extname(myPath),
    absoluteOrNot: path.isAbsolute(myPath),
    detailInfo: path.parse(myPath),
}

// Voyons les résultats :
console.log(pathInfo);
```

Sortie :

```text
{
  fileName: 'app.js',
  folderName: '/mnt/c/Desktop/NodeJSTut',
  fileExtension: '.js',
  absoluteOrNot: true,
  detailInfo: {
    root: '/',
    dir: '/mnt/c/Desktop/NodeJSTut',
    base: 'app.js',
    ext: '.js',
    name: 'app'
  }
}
```

Analysons en détail le code et sa sortie ci-dessus :

La première et la plus importante étape pour travailler avec le module `path` est de l'importer dans le fichier `app.js` en utilisant la méthode `require()`. 

Ensuite, nous attribuons un chemin d'un fichier à une variable appelée `myPath`. Cela peut être un chemin vers n'importe quel fichier aléatoire. Dans le but de comprendre le module `path`, j'ai choisi celui-ci : `/mnt/c/Desktop/NodeJSTut/app.js`.

En utilisant la variable `myPath`, nous allons comprendre le module `path` en détail. Vérifions les fonctions que ce module a à offrir et ce que nous pouvons faire avec :

* `path.basename(myPath)` : La fonction `basename()` accepte un chemin et retourne la dernière partie de ce chemin. Dans notre cas, la dernière partie de `myPath` est : `app.js`.
* `path.dirname(myPath)` : La fonction `dirname()` sélectionne la dernière partie du chemin fourni et retourne le chemin vers son répertoire parent. Dans notre cas, puisque la dernière partie de `myPath` est `app.js`. La fonction `dirname()` retourne le chemin vers le répertoire parent de `app.js` (le dossier dans lequel se trouve le fichier `app.js`), c'est-à-dire, `/mnt/c/Desktop/NodeJSTut`. On peut aussi penser que : la fonction `dirname()` exclut simplement la dernière partie du chemin fourni et retourne le chemin restant.
* `path.extname(myPath)` : Cette fonction vérifie s'il y a une extension sur la dernière partie du chemin fourni et elle retourne l'extension du fichier (si elle existe), sinon elle retourne une chaîne vide : `''`. Dans notre cas, puisque la dernière partie est `app.js` et qu'une extension de fichier existe, nous obtenons `'.js'` comme sortie.
* `path.isAbsolute(myPath)` : Cela indique si le chemin fourni est absolu ou non. Sur les systèmes basés sur Unix (comme macOS et Linux), un chemin absolu commence toujours par une barre oblique (`/`). Sur les systèmes Windows, un chemin absolu peut commencer par une lettre de lecteur (comme `C:`) suivie d'un deux-points (`:`), ou par deux barres obliques inverses (`\\`). Puisque la valeur stockée dans la variable `myPath` commence par `/`, donc `isAbsolute()` retourne `true`.  
  
Cependant, si vous changez simplement la variable `myPath` en ceci : `Desktop/NodeJSTut/app.js` (en la convertissant en un chemin relatif), `isAbsolute()` retourne `false`.
* `path.parse(myPath)` : Cette fonction accepte un chemin et retourne un objet qui contient une décomposition détaillée du chemin fourni. Voici ce qu'elle retourne lorsque nous fournissons la variable `myPath` :  
1. `root` : La racine du chemin (dans ce cas, `/`).  
2. `dir` : Le répertoire du fichier (dans ce cas, `/mnt/c/Desktop/NodeJSTut`).  
3. `base` : Le nom de base du fichier (dans ce cas, `app.js`).  
4. `ext` : L'extension du fichier (dans ce cas, `.js`).  
5. `name` : Le nom de base du fichier, sans l'extension (dans ce cas, `app`).

Avant de continuer avec les autres fonctions du module `path`, nous devons comprendre quelque chose appelé **séparateur de chemin et la structure de chemin**. 

Vous avez dû voir que le chemin vers un même fichier semble différent dans différents systèmes d'exploitation. Par exemple, considérons le chemin vers un fichier nommé `example.txt` situé dans un dossier appelé `Documents` sur le bureau d'un utilisateur Windows :

```text
C:\Users\username\Desktop\Documents\example.txt
```

D'autre part, le chemin du fichier vers le même fichier pour un utilisateur sur un système macOS serait comme ceci :

```text
/Users/username/Desktop/Documents/example.txt
```

2 différences sont à noter ici :

1. **Différence dans les séparateurs de chemin :** Dans Windows, les chemins de fichiers utilisent la barre oblique inverse (`\`) comme séparateur entre les répertoires, tandis que dans macOS/Linux (qui est un système basé sur Unix), les chemins de fichiers utilisent la barre oblique (`/`) comme séparateur.
2. **Différence dans le répertoire racine des fichiers de l'utilisateur :** Sur Windows, le répertoire racine pour les fichiers d'un utilisateur se trouve généralement à `C:\Users\username`, tandis que sur macOS et Linux, il se trouve à `/Users/username/`. Bien que cela soit vrai pour la plupart des systèmes Windows, macOS et Linux, il peut y avoir quelques variations dans l'emplacement exact du répertoire personnel de l'utilisateur en fonction de la configuration du système.

Avec cela à l'esprit, continuons et comprenons quelques autres fonctions fournies par le module `path` :

* `path.sep` : `sep` est une variable qui contient le séparateur de chemin spécifique au système. Pour une machine Windows : `console.log(path.sep)` imprime `\` dans la console tandis que dans le cas de macOS ou Linux, `path.sep` retourne une barre oblique (`/`).
* `path.join(<paths>)` : La fonction `path.join()` accepte des chemins sous forme de chaînes. Elle joint ensuite ces chemins en utilisant le séparateur de chemin spécifique au système et retourne le chemin joint. Par exemple, considérons ce code :

```javascript
console.log(path.join('grandParentFolder', 'parentFolder', 'child.txt'))
```

Le code ci-dessus imprime différents résultats pour différents systèmes d'exploitation.   
Dans Windows, il donnera cette sortie : `grandParentFolder\parentFolder\child.txt` tandis que dans macOS/Linux, il donnera cette sortie : `grandParentFolder/parentFolder/child.txt`. Notez que la différence est seulement dans les séparateurs de chemin - barre oblique inverse et barre oblique.

* `path.resolve(<paths>)` : Cette fonction fonctionne de manière similaire à `path.join()`. La fonction `path.resolve()` joint simplement les différents chemins fournis en utilisant le séparateur de chemin spécifique au système, puis ajoute la sortie finale au chemin absolu du répertoire de travail actuel. 

Supposons que vous êtes un utilisateur Windows et que le chemin absolu vers votre répertoire de travail actuel est le suivant : `C:\Desktop\NodeJSTut`, si vous exécutez ce code :

```javascript
console.log(path.resolve('grandParentFolder', 'parentFolder', 'child.txt'));
```

 Vous verrez la sortie suivante dans la console :

```text
C:\Desktop\NodeJSTut\grandParentFolder\parentFolder\child.txt
```

Le même principe s'applique à un utilisateur macOS ou Linux. Il s'agit simplement de la différence dans le chemin absolu du répertoire de travail actuel et le séparateur de chemin.

## Le module FS

Ce module vous aide avec les opérations de gestion de fichiers telles que :

* Lire un fichier (de manière synchrone ou asynchrone)
* Écrire dans un fichier (de manière synchrone ou asynchrone)
* Supprimer un fichier
* Lire le contenu d'un répertoire
* Renommer un fichier
* Surveiller les changements dans un fichier, et bien plus encore

Effectuons certaines de ces tâches pour voir le module `fs` (File System) en action ci-dessous :

### Comment créer un répertoire en utilisant `fs.mkdir()`

La fonction `fs.mkdir()` dans Node.js est utilisée pour créer un nouveau répertoire. Elle prend deux arguments : le chemin du répertoire à créer et une fonction de rappel facultative qui est exécutée lorsque l'opération est terminée.

* **path** : Ici, path fait référence à l'emplacement où vous souhaitez créer un nouveau dossier. Cela peut être un chemin absolu ou relatif. Dans mon cas, le chemin vers le répertoire de travail actuel (le dossier dans lequel je me trouve), est : `C:\Desktop\NodeJSTut`. Donc, créons un dossier dans le répertoire `NodeJSTut` appelé `myFolder`.
* **fonction de rappel** : Le but de la fonction de rappel est de notifier que le processus de création du répertoire est terminé. Cela est nécessaire car la fonction `fs.mkdir()` est asynchrone, ce qui signifie qu'elle ne bloque pas l'exécution du reste du code pendant que l'opération est en cours. Au lieu de cela, elle retourne immédiatement le contrôle à la fonction de rappel, lui permettant de continuer à exécuter d'autres tâches. Une fois que le répertoire a été créé, la fonction de rappel est appelée avec un objet d'erreur (le cas échéant) et toute autre donnée pertinente liée à l'opération. Dans le code ci-dessous, nous l'utilisons simplement pour afficher un message de succès dans la console ou toute erreur.

```javascript
// Importer le module fs
const fs = require('fs');

// Répertoire de travail actuel : C:\Desktop\NodeJSTut
// Création d'un nouveau répertoire appelé ./myFolder :

fs.mkdir('./myFolder', (err) => {
    if(err){
    	console.log(err);
    } else{
    	console.log('Dossier créé avec succès');
    }
})
```

Après avoir exécuté le code ci-dessus, vous verrez un nouveau dossier appelé `myFolder` créé dans le répertoire `NodeJSTut`.

### Comment créer et écrire dans un fichier de manière asynchrone en utilisant `fs.writeFile()`

Après la création réussie du répertoire `myFolder`, il est temps de créer un fichier et d'y écrire quelque chose en utilisant le module `fs`. 

Il existe essentiellement 2 façons de faire cela :

* **Approche synchrone** : Dans cette approche, nous créons un fichier et écrivons les données de manière bloquante, ce qui signifie que NodeJS attend que la création et l'opération d'écriture soient terminées avant de passer à la ligne de code suivante. Si une erreur se produit pendant ce processus, elle lance une exception qui doit être capturée en utilisant `try...catch`.
* **Approche asynchrone** : Dans cette approche, nous créons et écrivons des données dans un fichier de manière non bloquante, ce qui signifie que NodeJS n'attend pas que l'opération d'écriture soit terminée avant de passer à la ligne de code suivante. Au lieu de cela, il prend une fonction de rappel qui est appelée une fois que l'ensemble du processus est terminé. Si une erreur se produit pendant l'opération d'écriture, l'objet d'erreur est passé à la fonction de rappel.

Dans ce tutoriel, nous allons utiliser la fonction `fs.writeFile()` qui suit l'approche asynchrone.

`writeFile()` est une méthode fournie par le module `fs` (file system) dans Node.js. Elle est utilisée pour écrire des données dans un fichier de manière asynchrone. La méthode prend trois arguments :

1. Le **chemin** du fichier dans lequel écrire (y compris le nom du fichier et l'extension)
2. Les **données** à écrire dans le fichier (sous forme de chaîne ou de buffer)
3. Une fonction de rappel **facultative** qui est appelée une fois que l'opération d'écriture est terminée ou qu'une erreur se produit pendant l'opération d'écriture.

Lorsque `writeFile()` est appelée, Node.js crée un nouveau fichier ou écrase un fichier existant à l'emplacement **chemin** spécifié. Il écrit ensuite les **données** fournies dans le fichier et le ferme. Puisque la méthode est asynchrone, l'opération d'écriture ne bloque pas la boucle d'événements, permettant à d'autres opérations d'être effectuées en attendant. 

Voici le code où nous créons un nouveau fichier appelé `myFile.txt` dans le répertoire `myFolder` et écrivons ces `data` dedans : `Hi,this is newFile.txt`.

```javascript
const fs = require('fs');

const data = "Hi,this is newFile.txt";

fs.writeFile('./myFolder/myFile.txt', data, (err)=> {
    if(err){
        console.log(err);
        return;
    } else {
    	console.log('Écriture dans le fichier réussie !');
    }
})
```

Puisque `newFile.txt` n'existait pas auparavant, la fonction `writeFile()` a donc créé ce fichier pour nous sur le chemin fourni et a ensuite écrit la valeur dans la variable `data` dans le fichier. Supposons que ce fichier existe déjà. Dans ce cas, `writeFile()` ouvrira simplement le fichier, effacera tout le texte existant présent et écrira ensuite les données dedans.

Le problème avec ce code est : lorsque vous exécutez le même code plusieurs fois, il efface les données précédentes déjà présentes dans `newFile.txt` et écrit les données dedans. 

Au cas où vous ne souhaitez pas que les données originales soient supprimées et souhaitez simplement que les nouvelles données soient ajoutées/ajoutées à la fin du fichier, vous devez apporter une petite modification au code ci-dessus en ajoutant cet "objet d'options" : `{flag: 'a'}` comme troisième paramètre à `writeFile()` – comme ceci :

```javascript
const fs = require('fs');

const data = 'Hi,this is newFile.txt';

fs.writeFile('./myFolder/myFile.txt', data, {flag: 'a'}, (err) => {
    if(err){
        console.log(err);
        return;
    } else {
    	console.log('Écriture dans le fichier réussie !');
    }
})
```

Une fois que vous exécutez le code ci-dessus encore et encore, vous verrez que le fichier `myFile.txt` contient la valeur de la variable `data` écrite plusieurs fois. Cela est dû au fait que l'objet (3ème paramètre) : `{flag: 'a'}` indique à la méthode `writeFile()` d'ajouter les `data` à la fin du fichier au lieu d'effacer les données précédentes présentes.

### Comment lire un fichier de manière asynchrone en utilisant `fs.readFile()`

Après avoir créé et écrit dans le fichier, il est temps d'apprendre comment lire les données présentes dans le fichier en utilisant le module `fs`.

Il y a à nouveau 2 façons de faire cela : l'approche synchrone et l'approche asynchrone (comme la fonction précédente). Ici, nous allons utiliser la fonction `readFile()` fournie par le module `fs` qui effectue l'opération de lecture de manière asynchrone.

La fonction `readFile()` prend 3 paramètres :

1. Le **chemin** vers le fichier qui doit être lu.
2. L'**encodage** du fichier.
3. La **fonction de rappel** qui est exécutée une fois l'opération de lecture terminée ou si une erreur se produit pendant l'opération de lecture. Elle accepte 2 paramètres : le premier paramètre stocke les données du fichier (si l'opération de lecture est réussie) et le second paramètre stocke l'objet d'erreur (si l'opération de lecture échoue en raison d'une erreur).

La fonction `readFile()` est très intuitive et une fois appelée, elle lit les données présentes dans le fichier fourni selon l'encodage donné. Si l'opération de lecture est réussie, elle retourne les données à la fonction de rappel et si ce n'est pas le cas, elle retournera l'erreur survenue.

Dans le code ci-dessous, nous lisons le contenu du fichier - `myFile.txt` que nous avions créé en apprenant la fonction précédente et nous enregistrons les données qui y sont stockées dans la console.

```javascript
const fs = require('fs');

fs.readFile('./myFolder/myFile.txt', {encoding: 'utf-8'}, (err, data) => {
    if(err){
    	console.log(err);
        return;
    } else {
    	console.log('Fichier lu avec succès ! Voici les données');
        console.log(data);
    }
})
```

Il est à noter ici que la propriété `encoding` est définie sur `'utf-8'`. À ce stade, certains d'entre vous ne connaissent peut-être pas la propriété d'encodage, alors comprenons-la un peu plus en détail :

Le paramètre `encoding` dans la méthode `fs.readFile()` de Node.js est utilisé pour spécifier l'encodage de caractères utilisé pour interpréter les données du fichier. Par défaut, si aucun paramètre `encoding` n'est fourni, la méthode retourne un buffer brut.

Si la méthode `readFile()` est appelée sans fournir de paramètre `encoding`, vous verrez un résultat similaire à celui-ci imprimé dans la console :

```javascript
<Buffer 54 68 69 73 20 69 73 20 73 6f 6d 65 20 64 61 74 61 20 69 6e 20 61 20 66 69 6c 65>

```

Ce buffer brut est difficile à lire et à interpréter car il représente le contenu du fichier sous forme binaire. Pour convertir le buffer en une chaîne lisible, vous pouvez spécifier un paramètre `encoding` lors de l'appel de `readFile()`. 

Dans notre cas, nous avons spécifié l'encodage `'utf8'` comme deuxième paramètre de la méthode `readFile()`. Cela indique à Node.js d'interpréter le contenu du fichier comme une chaîne en utilisant l'encodage de caractères UTF-8, ainsi vous voyez les données originales imprimées dans la console. D'autres encodages courants qui peuvent être utilisés avec `readFile()` incluent :

* `'ascii'` : Interpréter le contenu du fichier comme du texte encodé en ASCII.
* `'utf16le'` : Interpréter le contenu du fichier comme du texte Unicode 16 bits en ordre d'octets little-endian.
* `'latin1'` : Interpréter le contenu du fichier comme du texte encodé en ISO-8859-1 (également connu sous le nom de Latin-1).

### Lire et écrire dans un fichier de manière synchrone

Jusqu'à présent, vous avez appris comment configurer des serveurs web mais nous n'avons rien construit d'intéressant. Ajoutons donc un peu de plaisir à nos vies.

Dans la dernière section de ce tutoriel, nous allons servir cette barre de navigation :

![GIF animé de la barre de navigation que nous allons servir depuis notre serveur](https://cdn.hashnode.com/res/hashnode/image/upload/v1680026253758/29c08d70-df1b-4dbf-ae30-552b41cba12b.gif)

Puisque ce n'est pas un tutoriel lié au front-end, nous ne construirons pas cette barre de navigation à partir de zéro. Au lieu de cela, vous pouvez vous rendre sur ce dépôt GitHub et copier le contenu du répertoire `navbar-app` et le configurer localement : [Dépôt GitHub de John Smilga](https://github.com/john-smilga/node-express-course/tree/main/02-express-tutorial/navbar-app). L'idée est de :

1. Configurer le dossier `navbar-app` localement
2. Utiliser le module `fs` pour lire le contenu des fichiers HTML, CSS, JS et le Logo
3. Utiliser le module `http` pour rendre les fichiers lorsque quelqu'un essaie d'accéder à la route `/` ou à la page d'accueil. Alors, commençons :

Dans le code ci-dessous, nous utilisons la méthode `readFileSync()` du module `fs` pour lire le contenu des fichiers HTML, CSS, JS et le Logo. 

Notez que nous allons servir le contenu du fichier et non le fichier lui-même. Donc `readFileSync()` entre en jeu.

Ensuite, nous servons le contenu du fichier HTML (stocké dans la variable `homePage`) en utilisant la méthode `res.write()`. N'oubliez pas de définir le `content-type` comme `text/html` car nous servons du contenu HTML. Nous avons également configuré des réponses pour la route `/about` et également une page 404.

```javascript
const http = require('http');
const fs = require('fs');

// Obtenir le contenu des fichiers HTML, CSS, JS et Logo
const homePage = fs.readFileSync('./navbar-app/index.html');
const homeStyles = fs.readFileSync('./navbar-app/style.css');
const homeLogo = fs.readFileSync('./navbar-app/logo.svg');
const homeLogic = fs.readFileSync('./navbar-app/browser-app.js');

// Création du serveur
const server = http.createServer((req, res) => {
    const url = req.url;
    if(url === '/'){
    	res.writeHead(200, {'content-type': 'text/html'});
        res.write(homePage);
        res.end();
    } else if(url === '/about'){
    	res.writeHead(200, {'content-type': 'text/html'});
        res.write(<h1>Page À Propos</h1>);
        res.end();
    } else{
    	res.writeHead(200, {'content-type': 'text/html'});
        res.write(<h1>404, Ressource Non Trouvée</h1>);
        res.end();
    }
})

server.listen(5000, () => {
	console.log('Serveur à l'écoute sur le port 5000');
})
```

Lorsque vous exécutez ce code en utilisant la commande `node app.js`, vous verrez ces réponses envoyées par le serveur pour les routes suivantes :

![Image des différentes réponses HTML que le serveur envoie lors de la visite de différentes URL. Ici, nous voyons seulement la structure HTML de la barre de navigation, le CSS, le Logo et le JS sont manquants](https://www.freecodecamp.org/news/content/images/2023/05/c5892af9-1fff-49b4-af43-2c6db6053b9d.png)

Nous voyons que les autres routes fonctionnent bien, mais la page d'accueil ne ressemble pas à ce que nous attendions. Le problème est que nous ne voyons que la structure HTML de la barre de navigation affichée et non les autres éléments comme le CSS, le logo et le JavaScript.

Voyons quel est le bug. Nous pouvons vérifier quelles requêtes sont faites par le navigateur web au serveur en modifiant le code ci-dessus comme ceci :

```javascript
// ... code ci-dessus
const server = http.createServer((req, res) => {
    const url = req.url;
    console.log(url);
    
    // ... reste du code
})
```

Ici, nous imprimons simplement l'`url` de la requête faite par le client au serveur.

Une fois que nous actualisons la page, nous voyons que initialement le navigateur demande la page d'accueil et fait une requête GET avec l'URL `/`. Ensuite, il fait 3 autres requêtes :

* `/style.css` – demandant le fichier CSS
* `/browser-app.js` – demandant le fichier JS
* `/logo.svg` – demandant le logo

![Une image de la console montrant la propriété req.url des différentes requêtes : /, /style.css, /browser-app.js et /logo.svg](https://www.freecodecamp.org/news/content/images/2023/05/image-2.png)

**De cela, nous pouvons déduire comment fonctionnent les navigateurs.**

Le navigateur fait une requête pour le contenu du chemin `/` et le serveur envoie simplement le contenu HTML. Une fois que le navigateur reçoit le contenu HTML, il l'interprète et commence à afficher les éléments. Pendant l'analyse du HTML, si le navigateur rencontre une ressource supplémentaire comme une page CSS ou JS, il fera une requête au serveur pour la même chose.

Puisque nous n'envoyons pas le CSS, le JS et le Logo dans la réponse, nous ne les voyons pas à l'écran. Nous pouvons corriger cela en ajoutant quelques `if()` supplémentaires dans le code et en envoyant ces ressources que le navigateur demande et BOOM – ce bug est corrigé.

```javascript
const http = require('http');
const fs = require('fs');

// Obtenir le contenu des fichiers HTML, CSS, JS et Logo
const homePage = fs.readFileSync('./navbar-app/index.html');
const homeStyles = fs.readFileSync('./navbar-app/style.css');
const homeLogo = fs.readFileSync('./navbar-app/logo.svg');
const homeLogic = fs.readFileSync('./navbar-app/browser-app.js');

// Création du serveur
const server = http.createServer((req, res) => {
    const url = req.url;
    if(url === '/'){
    	res.writeHead(200, {'content-type': 'text/html'});
        res.write(homePage);
        res.end();
    } else if(url === '/style.css'){
    	res.writeHead(200, {'content-type': 'text/css'});
        res.write(homeStyles);
        res.end();
    } else if(url === '/browser-app.js'){
    	res.writeHead(200, {'content-type': 'text/javascript'});
        res.write(homeLogic);
        res.end();
    } else if(url === '/logo.svg'){
        res.writeHead(200, {'content-type': 'image/svg+xml'});
        res.write(homeLogo);
        res.end();
    } else if(url === '/about'){
    	res.writeHead(200, {'content-type': 'text/html'});
        res.write(<h1>Page À Propos</h1>);
        res.end();
    } else{
    	res.writeHead(200, {'content-type': 'text/html'});
        res.write(<h1>404, Ressource Non Trouvée</h1>);
        res.end();
    }
})

server.listen(5000, () => {
	console.log('Serveur à l'écoute sur le port 5000');
})
```

Maintenant, nous pouvons voir le HTML, le CSS, le Logo et la fonctionnalité JS présents :

![Image de la barre de navigation servie par le serveur](https://www.freecodecamp.org/news/content/images/2023/05/somerandomImage--1-.png)

# Conclusion

Avec cela, nous arrivons à la fin de ce tutoriel 😊 – J'espère que vous l'avez aimé et que vous avez appris beaucoup de choses sur Node. 

Partagez vos apprentissages de ce guide sur Twitter et LinkedIn (#LearnInPublic) et suivez freeCodeCamp pour plus d'articles de codage informatifs comme celui-ci.

Connectez-vous avec moi sur Twitter : [Twitter - Krish4856](https://twitter.com/Krish4856), DMs ouverts. 

À la prochaine 👋 💖 ✨