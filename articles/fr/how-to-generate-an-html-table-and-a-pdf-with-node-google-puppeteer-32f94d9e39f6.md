---
title: Comment générer un tableau HTML et un PDF avec Node & Google Puppeteer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-15T21:53:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-an-html-table-and-a-pdf-with-node-google-puppeteer-32f94d9e39f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vmoUk8zB0XXR2l203rw7fQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment générer un tableau HTML et un PDF avec Node & Google Puppeteer
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@lobosnico?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Nicolas
  Lobos / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  Understandi...'
---

Par Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-244.png)
_Photo par [Unsplash](https://unsplash.com/@lobosnico?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Nicolas Lobos</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Comprendre NodeJS en interne peut être un peu intimidant (je sais que cela a été le cas pour moi). Node est un langage très puissant et il peut faire beaucoup de choses.

Aujourd'hui, je voulais découvrir le pouvoir de l'outil utilitaire intégré de Node appelé [fs](https://nodejs.org/api/fs.html) ([système de fichiers](https://nodejs.org/api/fs.html))

Selon la documentation [fs](https://nodejs.org/api/fs.html) :

> Le module `fs` fournit une API pour interagir avec le système de fichiers de manière étroitement modélisée autour des fonctions POSIX standard.

Ce qui est simplement une manière élégante de dire que le [système de fichiers](https://nodejs.org/api/fs.html) est un moyen dans Node d'interagir avec les fichiers pour les opérations de lecture et d'écriture.

Maintenant, le [système de fichiers](https://nodejs.org/api/fs.html) est un utilitaire énorme dans NodeJS qui possède de nombreuses fonctionnalités sophistiquées. Dans cet article, cependant, je ne discuterai que de 3 :

* Obtenir des informations sur un fichier : **_fs.statSync_**
* Supprimer un fichier : **_fs.unlinkSync_**
* Écrire des données dans un fichier : **_fs.writeFileSync_**

Une autre chose que nous aborderons dans cet article est [Google Puppeteer](https://developers.google.com/web/tools/puppeteer/) qui est cet outil vraiment cool et élégant créé par des gens formidables chez Google.

Alors, qu'est-ce que Puppeteer ? Eh bien, selon la documentation, ils disent :

> Puppeteer est une bibliothèque Node qui fournit une API de haut niveau pour contrôler [headless](https://developers.google.com/web/updates/2017/04/headless-chrome) Chrome ou Chromium via le [DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/). Il peut également être configuré pour utiliser Chrome ou Chromium complet (non headless).

Donc, c'est essentiellement un outil qui vous permet de faire toutes les choses cool liées au navigateur sur le serveur. Comme obtenir des captures d'écran d'un site web, crawler des sites web, et générer du contenu pré-rendu pour des applications à page unique. Vous pouvez même faire des soumissions de formulaires via votre serveur NodeJS.

Encore une fois, Puppeteer est un outil énorme, donc nous couvrirons juste une petite mais très cool fonctionnalité de Puppeteer. Nous verrons comment générer un fichier PDF basé sur notre fichier de tableau HTML généré. Dans le processus, nous apprendrons sur puppeteer.launch() et comprendrons un peu sur page() & pdf().

#### Donc, pour donner un bref aperçu, les choses que nous couvrirons :

* Générer des données fictives (pour les factures) en utilisant un outil en ligne.
* Créer un tableau HTML avec un peu de style avec des données générées, en utilisant un script Node automatisé.
* Apprendre à vérifier si un fichier existe ou non en utilisant fs.statSync
* Apprendre à supprimer un fichier en utilisant fs.unlinkSync
* Apprendre à écrire un fichier en utilisant fs.writeFileSync
* Créer un fichier PDF de ce fichier HTML généré en utilisant Google Puppeteer
* Les transformer en scripts npm, pour être utilisés plus tard ? ?

> De plus, avant de commencer, voici l'ensemble du [code source du tutoriel](https://github.com/adeelibr/understaning-node-fs-and-puppeteer), pour que tout le monde puisse suivre. Vous n'avez pas besoin d'écrire quoi que ce soit, mais vous devriez écrire du code avec ce tutoriel. Cela sera plus utile et vous comprendrez mieux. [**_CODE SOURCE DU TUTORIEL_**](https://github.com/adeelibr/understaning-node-fs-and-puppeteer)

Avant de commencer, assurez-vous d'avoir au moins les éléments suivants installés sur votre machine

* Node version 8.11.2
* Node Package Manager (NPM) version 6.9.0

Vous n'avez pas besoin de le faire, mais vous pouvez également regarder une vidéo d'introduction (ma première vidéo) qui parle des bases de la lecture, de l'écriture et de la suppression d'un fichier dans NodeJS. Cela vous aidera à comprendre ce tutoriel. (Veuillez me donner votre avis). ?

%[https://youtu.be/7tc_lYelc-U]

### Commençons

#### **Étape 1 :**

Dans votre terminal, tapez ce qui suit :

```
npm init -y
```

Cela initialisera un projet vide pour vous.

#### Étape 2 :

Deuxièmement, dans le même dossier, créez un nouveau fichier appelé `data.json` et ajoutez-y des données fictives. Vous pouvez utiliser l'exemple JSON suivant.

Vous pouvez obtenir les données fictives JSON de stub à partir de [**ici**](https://gist.github.com/adeelibr/69d2ca9d40642aaf99721796da0aaa64)**.** Pour générer ces données, j'ai utilisé un outil formidable appelé [https://mockaroo.com/](https://mockaroo.com/) C'est un outil de génération de données en ligne.

Les données JSON que j'utilise ont une structure comme celle-ci :

```js
[
  {},
  {},
  {
   "invoiceId": 1,
   "createdDate": "3/27/2018",
   "dueDate": "5/24/2019",
   "address": "28058 Hazelcrest Center",
   "companyName": "Eayo",
   "invoiceName": "Carbonated Water - Peach",
   "price": 376
  },
  {
   "invoiceId": 2,
   "createdDate": "6/14/2018",
   "dueDate": "11/14/2018",
   "address": "6205 Shopko Court",
   "companyName": "Ozu",
   "invoiceName": "Pasta - Fusili Tri - Coloured",
   "price": 285
  },
  {},
  {}
]
```

> Vous pouvez télécharger le tableau JSON complet pour ce tutoriel à partir de [**ici**](https://gist.github.com/adeelibr/69d2ca9d40642aaf99721796da0aaa64)**.**

#### Étape 3 :

Ensuite, créez un nouveau fichier appelé `buildPaths.js`

```js
const path = require('path');
const buildPaths = {
   buildPathHtml: path.resolve('./build.html'),
   buildPathPdf: path.resolve('./build.pdf')
};
module.exports = buildPaths;
```

Ainsi, `path.resolve` prendra un chemin relatif et nous retournera le chemin absolu de ce répertoire particulier.

Ainsi, `path.resolve('./build.html');` retournera par exemple quelque chose comme ceci :

```
$ C:\\Users\\Adeel\\Desktop\\articles\\tutorial\\build.html
```

#### **Étape 4 :**

Dans le même dossier, créez un fichier appelé `createTable.js` et ajoutez le code suivant :

```js
const fs = require('fs');
// Données JSON
const data = require('./data.json');
// Chemins de construction
const { buildPathHtml } = require('./buildPaths');

/**
 * Prend un objet qui a le modèle suivant
 * @param {Object} item 
 * @model
 * {
 *   "invoiceId": `Number`,
 *   "createdDate": `String`,
 *   "dueDate": `String`,
 *   "address": `String`,
 *   "companyName": `String`,
 *   "invoiceName": `String`,
 *   "price": `Number`,
 * }
 * 
 * @returns {String}
 */
const createRow = (item) => `
  <tr>
    <td>${item.invoiceId}</td>
    <td>${item.invoiceName}</td>
    <td>${item.price}</td>
    <td>${item.createdDate}</td>
    <td>${item.dueDate}</td>
    <td>${item.address}</td>
    <td>${item.companyName}</td>
  </tr>
`;

/**
 * @description Génère un tableau `html` avec toutes les lignes du tableau
 * @param {String} rows
 * @returns {String}
 */
const createTable = (rows) => `
  <table>
    <tr>
        <th>Invoice Id</td>
        <th>Invoice Name</td>
        <th>Price</td>
        <th>Invoice Created</td>
        <th>Due Date</td>
        <th>Vendor Address</td>
        <th>Vendor Name</td>
    </tr>
    ${rows}
  </table>
`;

/**
 * @description Génère une page `html` avec un tableau rempli
 * @param {String} table
 * @returns {String}
 */
const createHtml = (table) => `
  <html>
    <head>
      <style>
        table {
          width: 100%;
        }
        tr {
          text-align: left;
          border: 1px solid black;
        }
        th, td {
          padding: 15px;
        }
        tr:nth-child(odd) {
          background: #CCC
        }
        tr:nth-child(even) {
          background: #FFF
        }
        .no-content {
          background-color: red;
        }
      </style>
    </head>
    <body>
      ${table}
    </body>
  </html>
`;

/**
 * @description cette méthode prend un chemin sous forme de chaîne et retourne vrai/faux
 * selon que le chemin de fichier spécifié existe dans le système ou non.
 * @param {String} filePath 
 * @returns {Boolean}
 */
const doesFileExist = (filePath) => {
	try {
		fs.statSync(filePath); // obtenir les informations du chemin de fichier spécifié.
		return true;
	} catch (error) {
		return false;
	}
};

try {
	/* Vérifie si le fichier pour la construction `html` existe dans le système ou non */
	if (doesFileExist(buildPathHtml)) {
		console.log('Suppression de l'ancien fichier de construction');
		/* Si le fichier existe, supprime le fichier du système */
		fs.unlinkSync(buildPathHtml);
	}
	/* génère des lignes */
	const rows = data.map(createRow).join('');
	/* génère un tableau */
	const table = createTable(rows);
	/* génère du html */
	const html = createHtml(table);
	/* écrit le html généré dans un fichier */
	fs.writeFileSync(buildPathHtml, html);
	console.log('Tableau HTML créé avec succès');
} catch (error) {
	console.log('Erreur lors de la génération du tableau', error);
}
```

Je sais que c'est beaucoup de code, mais divisons-le en morceaux et commençons à le comprendre pièce par pièce.

Allez à la **ligne 106** ([gist github](https://gist.github.com/adeelibr/70936277d38f3c77d3910e417581e98a#file-createtable-js))

Dans notre bloc `try/catch`, nous vérifions d'abord si le fichier de construction pour HTML existe dans le système ou non. C'est le chemin du fichier où notre script NodeJS générera notre HTML.

`if (doesFileExist(buildPathHtml){}` appelle la méthode doesFileExist() qui retourne simplement vrai/faux. Pour cela, nous utilisons

```
fs.statSync(filePath);
```

Cette méthode retourne en réalité des informations sur le fichier comme la taille du fichier, quand le fichier a été créé, etc. Cependant, si nous fournissons un chemin de fichier invalide, cette méthode retourne une erreur nulle. Ce que nous utilisons ici à notre avantage et enveloppons la méthode `fs.statSync()` dans un `try/catch`. Si Node est capable de lire le fichier dans notre bloc try, nous retournons `true` — sinon, il lance une erreur que nous obtenons dans notre bloc catch et retourne `false`.

Si le fichier existe dans le système, nous finissons par supprimer le fichier en utilisant

```
fs.unlinkSync(filePath); // prend un chemin de fichier et le supprime
```

Après avoir supprimé le fichier, nous devons générer des lignes à mettre dans le tableau.

#### Étape 5 :

Donc, d'abord, nous importons `data.json` que nous faisons à la **ligne 3** puis à la **ligne 115**, nous itérons chaque élément en utilisant map(). Vous pouvez en lire plus sur [Array.prototype.map() ici.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

La méthode map prend une méthode `createRow` qui prend un objet à chaque itération et retourne une chaîne qui a un contenu comme ceci :

```html
"<tr>
  <td>invoice id</td>
  <td>invoice name</td>
  <td>invoice price</td>
  <td>invoice created date</td>
  <td>invoice due date</td>
  <td>invoice address</td>
  <td>invoice sender company name</td>
</tr>"
```

> `const row = data.map(createdRow).join('');`

La partie `join('')` est importante ici, car je veux concaténer tout mon tableau en une chaîne.

Un principe presque similaire est utilisé pour générer un tableau à la **ligne 117** puis le tableau html à la **ligne 119.**

#### **Étape 6 :**

La partie importante est celle où nous écrivons dans notre fichier à la **ligne 121** :

```
fs.writeFileSync(buildPathHtml, html); 
```

Il prend 2 paramètres : l'un est le chemin de construction (chaîne) et le contenu html (chaîne) et génère un fichier (s'il n'est pas créé ; et s'il est créé, il écrase le fichier déjà existant).

> Une chose à noter ici, nous n'avons peut-être pas besoin de l'Étape 4, où nous vérifions si le fichier existe et s'il existe, nous le supprimons. Cela est dû au fait que writeFileSync le fait pour nous. Je l'ai simplement ajouté dans le code à des fins d'apprentissage.

#### Étape 7 :

Dans votre terminal, allez dans le chemin du dossier où vous avez le fichier `createTable.js` et tapez

```
$ npm run ./createTable.js
```

Dès que vous exécutez ce script, il créera un nouveau fichier dans le même dossier appelé `build.html` Vous pouvez ouvrir ce fichier dans votre navigateur et il ressemblera à quelque chose comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/lnYaAbNKig8Zhhuqh1QQDnMGFcQ1KNcHAA2I)
_Tableau HTML généré._

> Cool, non ? Jusqu'à présent, tout va bien. _?_

Vous pouvez également ajouter un `script npm` dans votre package.json comme ceci :

```js
"scripts": {
  "build:table": "node ./createTable.js"
},
```

De cette façon, au lieu d'écrire `npm run ./createTable.js`, vous pouvez simplement taper `npm run build:table`.

Prochaine étape : générer un PDF à partir du fichier `HTML` généré.

#### Étape 8 :

Tout d'abord, nous devons installer un outil sophistiqué, alors allez dans votre terminal dans le dossier de votre application et tapez

```
npm install puppeteer
```

#### **Étape 9 :**

Dans le même dossier où vous avez les fichiers `createTable.js`, `buildPaths.js` et `data.json`, créez un nouveau fichier appelé `createPdf.js` et ajoutez-y le contenu suivant :

```js

const fs = require('fs');
const puppeteer = require('puppeteer');
// Chemins de construction
const { buildPathHtml, buildPathPdf } = require('./buildPaths');

const printPdf = async () => {
	console.log('Début : Génération du processus PDF, veuillez patienter ..');
	/** Lance un navigateur headless */
	const browser = await puppeteer.launch();
	/* 1- Crée un nouvel objet newPage(). Il est créé dans le contexte du navigateur par défaut. */
	const page = await browser.newPage();
	/* 2- Ouvrira notre fichier `.html` généré dans la nouvelle instance de Page. */
	await page.goto(buildPathHtml, { waitUntil: 'networkidle0' });
	/* 3- Prend un instantané du PDF */
	const pdf = await page.pdf({
		format: 'A4',
		margin: {
			top: '20px',
			right: '20px',
			bottom: '20px',
			left: '20px'
		}
	});
	/* 4- Nettoyage : ferme le navigateur. */
	await browser.close();
	console.log('Fin : Génération du processus PDF');
	return pdf;
};

const init = async () => {
	try {
		const pdf = await printPdf();
		fs.writeFileSync(buildPathPdf, pdf);
		console.log('Fichier PDF créé avec succès');
	} catch (error) {
		console.log('Erreur lors de la génération du PDF', error);
	}
};

init();
```

Comme nous l'avons fait avec le script `createTable.js`, décomposons cela en morceaux et commençons à comprendre ce script étape par étape.

Commençons par la **[ligne 40](https://gist.github.com/adeelibr/57081ec24b634b4d161e405ae3bf6d78#file-createpdf-js-L40)** ici nous appelons une méthode **_init()_** qui appelle la méthode à la **[ligne 30](https://gist.github.com/adeelibr/57081ec24b634b4d161e405ae3bf6d78#file-createpdf-js-L30).** Une chose à noter est que notre méthode init() est une méthode asynchrone. Lisez-en plus sur cette [fonction asynchrone](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).

D'abord, dans la méthode init(), nous appelons la méthode **_printPdf()_** qui est à nouveau une méthode asynchrone, donc nous devons attendre sa réponse. La méthode printPdf() nous retourne une instance PDF que nous écrivons ensuite dans un fichier à la **[ligne 33](https://gist.github.com/adeelibr/57081ec24b634b4d161e405ae3bf6d78#file-createpdf-js-L33).**

Alors, que fait la méthode `printPdf()` ? Creusons cela.

```js
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto(buildPathHtml, { waitUntil: 'networkidle0' });
const pdf = await page.pdf({
  format: 'A4',
  margin: {
   top: '20px', right: '20px', bottom: '20px', left: '20px'}
});
await browser.close();
return pdf;
```

Nous lançons d'abord une instance de navigateur headless en utilisant Puppeteer en faisant ce qui suit :

```
await puppeteer.launch(); // cela nous retourne un navigateur headless
```

que nous utilisons ensuite pour ouvrir une page web :

```
await browser.newPage(); // ouvre une page vide dans le navigateur headless
```

Une fois que nous avons une page vide ouverte, nous pouvons naviguer vers une page. Puisque notre page web est locale dans notre système, nous faisons simplement

```
page.goto(buildPathHtml, { waitUntil: 'networkidle0' });
```

Ici, `waitUntil: 'networkidle0'` est important, car il indique à Puppeteer d'attendre 500/ms jusqu'à ce qu'il n'y ait plus de connexions réseau.

> **_Note:_** C'est pourquoi nous avons utilisé path.resolve() pour obtenir des chemins absolus, car pour ouvrir la page web avec Puppeteer, nous avons besoin d'un chemin absolu.

Après avoir ouvert une page web dans le navigateur headless sur le serveur, nous enregistrons cette page en tant que PDF :

```
await page.pdf({ });
```

Dès que nous avons une version PDF de la page web, nous devons fermer l'instance du navigateur ouverte par Puppeteer pour économiser des ressources en faisant ceci :

```
await browser.close();
```

& puis nous retournons le `pdf` enregistré, que nous écrivons ensuite dans le fichier.

#### Étape 10 :

Dans votre terminal, tapez

```
$ npm ./createPdf.js
```

Remarque : Avant d'exécuter le script ci-dessus, assurez-vous que vous avez le fichier `build.html` généré par le script `createTable.js`. Cela garantit que nous avons toujours le `build.html` avant d'exécuter le script `createPdf.js`. Dans votre `package.json`, faites ce qui suit.

```
"scripts": {
  "build:table": "node ./createTable.js",
  "prebuild:pdf": "npm run build:table",
  "build:pdf": "node ./createPdf.js"
},
```

Maintenant, si vous exécutez `**$** npm run build:pdf`, il exécutera d'abord le script `createTable.js` puis le script `createPdf.js`. Vous pouvez en lire plus sur les [scripts NPM](https://docs.npmjs.com/misc/scripts) dans leur documentation officielle [docs](https://docs.npmjs.com/misc/scripts).

Lorsque vous exécutez

```
$ npm run build:pdf
```

Il s'exécutera et créera un `build.pdf` qui ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/UOMwXytU2JyC8VlsgaM-wXF-9D9icvPpLlnC)
_Fichier .pdf généré lors de l'exécution du script **createPdf.js**_

Et c'est tout, nous avons terminé.

Vous avez appris les points suivants :

* Comment vérifier si un fichier existe / obtenir des informations sur un fichier (dans Node)
* Comment supprimer un fichier dans Node
* Comment écrire dans un fichier
* Comment utiliser Google Puppeteer pour générer un fichier PDF

Bonne apprentissage, j'adorerais avoir vos commentaires sur cet article. Vous pouvez me joindre sur [**_twitter_**](https://twitter.com/adeelibr) également.