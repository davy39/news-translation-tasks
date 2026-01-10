---
title: Comment utiliser Puppeteer avec Node.js
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2022-07-18T16:41:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-puppeteer-with-nodejs
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pup.jpg
tags:
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: puppeteer
  slug: puppeteer
- name: Testing
  slug: testing
seo_title: Comment utiliser Puppeteer avec Node.js
seo_desc: 'Puppeteer is a JavaScript library that allows you to script and interact
  with browser windows.

  In this guide, we''ll explore the basics of using Puppeteer with Node.js so you
  can start automating your tests.

  Prerequisites


  Basic understanding of Node....'
---

Puppeteer est une bibliothèque JavaScript qui vous permet de scripter et d'interagir avec les fenêtres du navigateur.

Dans ce guide, nous explorerons les bases de l'utilisation de Puppeteer avec Node.js afin que vous puissiez commencer à automatiser vos tests.

### Prérequis

* Compréhension de base de Node.js
* Compréhension de base de Puppeteer
* Un IDE approprié tel que VS Code

### Ce que vous allez apprendre

* Qu'est-ce que Puppeteer ?
* Qu'est-ce que Node.js ?
* Comment configurer votre premier test avec Puppeteer
* Comment exécuter des tests Chrome headless sur un serveur CI

## **Qu'est-ce que Puppeteer ?**

Puppeteer est une bibliothèque Node.js développée par Google qui vous permet de contrôler Chrome headless via le protocole DevTools.

C'est un outil pour automatiser les tests dans votre application en utilisant Chrome headless ou des appareils Chromebit, sans nécessiter d'extensions de navigateur comme Selenium Webdriver ou PhantomJS.

Puppeteer vous permet d'automatiser les tests de vos applications web. Avec lui, vous pouvez exécuter des tests dans le navigateur et voir les résultats en temps réel dans votre terminal.

Puppeteer utilise le protocole WebDriver pour se connecter au navigateur et simuler l'interaction de l'utilisateur avec les éléments HTML ou les pages.

## **Qu'est-ce que Node.js ?**

Node.js est un environnement d'exécution JavaScript open-source construit sur le moteur V8 de Chrome qui fonctionne sur les systèmes d'exploitation Linux, Mac OS X et Windows. Il a été publié pour la première fois en 2009 par Ryan Dahl, qui était l'un de ses contributeurs originaux (avec l'aide de Douglas Crockford).

Node.js est devenu extrêmement populaire au fil des ans en tant que partie essentielle de nombreux projets de développement logiciel. Il possède des capacités étendues lorsqu'il s'agit de coder certaines tâches comme les applications côté serveur ou les protocoles de réseau pair-à-pair comme Websockets.

### Comment configurer Node.js et Puppeteer

Tout d'abord, créez un répertoire dans lequel vous allez travailler en cliquant avec le bouton droit sur l'emplacement préféré et en choisissant nouveau dossier. Vous pouvez également utiliser la commande `mkdir dir-name` dans votre terminal.

Ensuite, créez un fichier `app.js` dans votre dossier et ajoutez le code `node.js` comme montré ci-dessous :

```js
const puppeteer = require('puppeteer');

(async () => {
	const browser = await puppeteer.launch();
	const page = await browser.newPage();
	await page.goto('https://www.freecodecamp.org/');
	
	await browser.close();
})();


```

Le code ci-dessus crée une instance du navigateur qui permet à Puppeteer de se lancer. Assurons-nous de bien comprendre le code ci-dessus :

* `browser.newPage()` crée une nouvelle page
* `page.goto()` fournit l'URL à `browser.newPage()`
* `browser.close()` ferme le processus en cours

Maintenant, ouvrez votre terminal et utilisez `cd` pour accéder au dossier. Ensuite, exécutez `npm init` pour créer un fichier `package.json`.

Appuyez sur Entrée, puis tapez oui si on vous demande 'est-ce correct'.

Votre sortie ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-182.png)
_package.json_

Suivez les instructions de configuration pour installer les dépendances que nous utiliserons dans notre projet.

## **Comment configurer votre premier test avec Puppeteer**

Pour utiliser Puppeteer avec Node.js, vous devrez installer plusieurs packages et configurer quelques variables d'environnement. Cette partie vous guidera à travers les étapes à suivre pour utiliser Puppeteer dans vos tests :

* Télécharger et installer [Node.js](https://nodejs.org/)
* Installer [Puppeteer](https://www.npmjs.com/package/puppeteer)
* Installer [Mocha](https://www.npmjs.com/package/mocha)
* Installer [Chai](https://www.npmjs.com/package/chai)
* Installer [Selenium Webdriver](https://www.npmjs.com/package/selenium-webdriver)

Vous n'avez besoin de compléter la dernière étape que si vous souhaitez exécuter des tests sur un navigateur réel au lieu de simplement tester contre des scripts de pilote web.

Si c'est votre cas, alors allez-y et installez le module selenium-web driver à partir du gestionnaire de packages npm en tapant `npm i selenium-webdriver --save`.

L'installation des dépendances générera `node_modules` et un fichier `package-lock.json` comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-183.png)
_package-lock.json_

Les captures d'écran sont un excellent moyen de capturer des informations dans votre navigateur. Eh bien, Puppeteer vous couvre !

Pour prendre une capture d'écran de la page web vers laquelle vous avez navigué, ajoutez l'extrait de code ci-dessous :

```js
  await page.screenshot({path: 'example.png'});

```

Pour exécuter l'application :

```bash
cd puppeter-tut
cd src

```

Ensuite, tapez la commande suivante dans votre terminal :

```bash
node app.js
```

Vous pouvez également créer un PDF en ajoutant le snippet suivant dans votre code :

```js
    await page.pdf({ path: 'example.pdf' });
```

L'extrait de code ci-dessus nous donnera la sortie montrée ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-188.png)

## Comment tester votre configuration

Pour tester votre configuration, créez un dossier `test` dans votre code, puis ajoutez `example.test.js`.

Votre fichier doit contenir le code suivant :

```js
const puppeteer = require('puppeteer')

describe("Ma première configuration de test",()=>{
     it("Page d'accueil",async()=>{
    const browser = await puppeteer.launch({headless:false})
     });
});
```

Exécutez votre test en utilisant `npm run test`. Après avoir exécuté votre test, vous obtiendrez la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-187.png)

Voici un [lien GitHub vers le code source du tutoriel](https://github.com/gatwirival/puppeteer-tut.git).

## Comment utiliser une instance de navigateur avec Puppeteer

En tant que développeur web, vous pouvez utiliser Puppeteer pour exécuter des scripts dans le navigateur Chrome headless et accéder à l'objet window. Cela est utile lors du test d'applications qui nécessitent l'accès à des ressources web comme localStorage ou les cookies.

Pour utiliser une instance de navigateur avec Puppeteer, vous devez simplement passer `{ headless: false }` à la méthode launch. Elle est asynchrone, donc elle ne bloquera pas le thread principal et ne rendra pas votre application non réactive.

Le meilleur aspect de cette méthode est que, une fois lancée, elle ne doit être utilisée qu'une seule fois. Sinon, vous obtiendrez une erreur en essayant d'accéder à une page web depuis Puppeteer à nouveau.

**Voici un exemple :**

```js
let browser; (async() => { if(!browser) browser = await puppeteer.launch({headless: false}); 
```

## **Conclusion**

Donc, voilà ! Maintenant, vous savez comment commencer avec Puppeteer et Node.js.

J'espère que ce guide vous a aidé à vous familiariser avec l'outil et ses capacités. N'hésitez pas à me contacter si vous avez des questions ou des suggestions.

