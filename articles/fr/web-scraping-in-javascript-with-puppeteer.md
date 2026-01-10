---
title: Web Scraping en JavaScript – Comment utiliser Puppeteer pour extraire des pages
  web
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2023-01-31T15:26:55.000Z'
originalURL: https://freecodecamp.org/news/web-scraping-in-javascript-with-puppeteer
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/web-scraping-in-javascript-with-puppeteer.png
tags:
- name: JavaScript
  slug: javascript
- name: puppeteer
  slug: puppeteer
- name: web scraping
  slug: web-scraping
seo_title: Web Scraping en JavaScript – Comment utiliser Puppeteer pour extraire des
  pages web
seo_desc: 'Welcome to the world of web scraping! Have you ever needed data from a
  website but found it hard to access it in a structured format? This is where web
  scraping comes in.

  Using scripts, we can extract the data we need from a website for various purpo...'
---

Bienvenue dans le monde du web scraping ! Avez-vous déjà eu besoin de données d'un site web mais trouvé difficile d'y accéder dans un format structuré ? C'est là que le web scraping intervient.

En utilisant des scripts, nous pouvons extraire les données dont nous avons besoin d'un site web pour diverses raisons, telles que la création de bases de données, l'analyse de données, et bien plus encore.

> **Avertissement :** Soyez prudent lorsque vous faites du web scraping. Assurez-vous toujours de scraper des sites qui l'autorisent, et de réaliser cette activité dans les limites éthiques et légales.

JavaScript et Node.js offrent diverses bibliothèques qui facilitent le web scraping. Pour une extraction de données simple, vous pouvez utiliser Axios pour récupérer des réponses d'API ou le HTML d'un site web.

Mais si vous cherchez à effectuer des tâches plus avancées, y compris des automatisations, vous aurez besoin de bibliothèques telles que [Puppeteer](https://pptr.dev/), [Cheerio](https://cheerio.js.org/), ou [Nightmare](https://github.com/segmentio/nightmare) (ne vous inquiétez pas, le nom est nightmare, mais ce n'est pas si difficile à utiliser 😊).

Je vais vous introduire aux bases du web scraping en JavaScript et Node.js en utilisant Puppeteer dans cet article. J'ai structuré l'écriture pour vous montrer quelques bases de la récupération d'informations sur un site web et du clic sur un bouton (par exemple, passer à la page suivante).

À la fin de cette introduction, je recommanderai des moyens de pratiquer et d'en apprendre davantage en améliorant le projet que nous venons de créer.

## Prérequis

Avant de plonger et de scraper notre première page ensemble en utilisant JavaScript, Node.js et le [DOM HTML](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction), je recommande d'avoir une compréhension de base de ces technologies. Cela améliorera votre apprentissage et votre compréhension du sujet.

Plongeons-nous ! 🥳

## Comment initialiser votre premier scraper Puppeteer

Nouveau projet... nouveau dossier ! Tout d'abord, créez le dossier `first-puppeteer-scraper-example` sur votre ordinateur. Il contiendra le code de notre futur scraper.

```shell
mkdir first-puppeteer-scraper-example
```

Maintenant, il est temps d'initialiser votre dépôt Node.js avec un fichier package.json. Il est utile d'ajouter des informations au dépôt et aux packages NPM, tels que la bibliothèque Puppeteer.

```shell
npm init -y
```

Après avoir tapé cette commande, vous devriez trouver ce fichier `package.json` dans l'arborescence de votre dépôt.

```json
{
  "name": "first-puppeteer-scraper-example",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "puppeteer": "^19.6.2"
  },
  "type": "module",
  "devDependencies": {},
  "description": ""
}

```

Avant de continuer, nous devons nous assurer que le projet est configuré pour gérer les fonctionnalités ES6. Pour ce faire, vous pouvez ajouter l'instruction `"types": "module"` à la fin de la configuration.

```json
{
  "name": "first-puppeteer-scraper-example",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "puppeteer": "^19.6.2"
  },
  "type": "module",
  "description": "",
  "types": "module"
}

```

La dernière étape de notre initialisation du scraper est d'installer la bibliothèque Puppeteer. Voici comment faire :

```shell
npm install puppeteer
```

Wow ! Nous y sommes – nous sommes prêts à scraper notre premier site web ensemble. 🤩

## Comment scraper votre première donnée

Dans cet article, nous utiliserons le site [ToScrape](https://toscrape.com/) comme plateforme d'apprentissage. Ce bac à sable en ligne propose deux projets spécialement conçus pour le web scraping, ce qui en fait un excellent point de départ pour apprendre les bases telles que l'extraction de données et la navigation entre les pages.

Pour cette introduction pour débutants, nous nous concentrerons spécifiquement sur le site [Quotes to Scrape](http://quotes.toscrape.com/).

### Comment initialiser le script

À la racine du dépôt du projet, vous pouvez créer un fichier `index.js`. Ce sera le point d'entrée de notre application.

Pour garder les choses simples, notre script se compose d'une fonction chargée de récupérer les citations du site web (`getQuotes`).

Dans le corps de la fonction, nous devrons suivre différentes étapes :

* Démarrer une session Puppeteer avec `puppeteer.launch` (elle instanciera une variable `browser` que nous utiliserons pour manipuler le navigateur)
* Ouvrir une nouvelle page/onglet avec `browser.newPage` (elle instanciera une variable `page` que nous utiliserons pour manipuler la page)
* Changer l'URL de notre nouvelle page pour [`http://quotes.toscrape.com/`](http://quotes.toscrape.com/) avec `page.goto`

Voici la version commentée du script initial :

```javascript
import puppeteer from "puppeteer";

const getQuotes = async () => {
  // Démarrer une session Puppeteer avec :
  // - un navigateur visible (`headless: false` - plus facile à déboguer car vous verrez le navigateur en action)
  // - aucun viewport par défaut (`defaultViewport: null` - la page du site web sera en pleine largeur et hauteur)
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
  });

  // Ouvrir une nouvelle page
  const page = await browser.newPage();

  // Sur cette nouvelle page :
  // - ouvrir le site web "http://quotes.toscrape.com/"
  // - attendre jusqu'à ce que le contenu du dom soit chargé (HTML est prêt)
  await page.goto("http://quotes.toscrape.com/", {
    waitUntil: "domcontentloaded",
  });
};

// Démarrer le scraping
getQuotes();

```

Que pensez-vous de lancer notre scraper et de voir le résultat ? Faisons-le avec la commande ci-dessous :

```shell
node index.js
```

Après avoir fait cela, vous devriez avoir une toute nouvelle application de navigateur démarrée avec une nouvelle page et le site web Quotes to Scrape chargé dessus. Magique, n'est-ce pas ? 🤩

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-353.png)
_Page d'accueil de Quotes to Scrape chargée par notre script initial_

**Note :** Pour cette première itération, nous ne fermons pas le navigateur. Cela signifie que vous devrez fermer le navigateur pour arrêter l'application en cours d'exécution.

### Comment récupérer la première citation

Chaque fois que vous souhaitez scraper un site web, vous devrez manipuler le DOM HTML. Ce que je recommande, c'est d'inspecter la page et de commencer à naviguer dans les différents éléments pour trouver ce dont vous avez besoin.

Dans notre cas, nous suivrons le [principe des petits pas](https://dictionary.cambridge.org/dictionary/english/baby-step) et commencerons par récupérer la première citation, l'auteur et le texte.

Après avoir parcouru le HTML de la page, nous pouvons remarquer qu'une citation est encapsulée dans un élément `<div>` avec un nom de classe `quote` (`class="quote"`). C'est une information importante car le scraping fonctionne avec des [sélecteurs CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors) (par exemple, .quote).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-354.png)
_Inspecteur de navigateur avec la première citation `&lt;div&gt;` sélectionnée_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-355.png)
_Un exemple de la façon dont chaque citation est rendue dans le HTML_

Maintenant que nous avons cette connaissance, nous pouvons retourner à notre fonction `getQuotes` et améliorer notre code pour sélectionner la première citation et extraire ses données.

Nous devrons ajouter ce qui suit après l'instruction `page.goto` :

* Extraire les données de notre HTML de page avec `page.evaluate` (elle exécutera la fonction passée en paramètre dans le contexte de la page et retournera le résultat)
* Obtenir le nœud HTML de la citation avec `document.querySelector` (elle récupérera le premier `<div>` avec le nom de classe `quote` et le retournera)
* Obtenir le texte et l'auteur de la citation à partir du nœud HTML de la citation précédemment extrait avec `quote.querySelector` (elle extraira les éléments avec les noms de classe `text` et `author` sous `<div class="quote">` et les retournera)

Voici la version mise à jour avec des commentaires détaillés :

```javascript
import puppeteer from "puppeteer";

const getQuotes = async () => {
  // Démarrer une session Puppeteer avec :
  // - un navigateur visible (`headless: false` - plus facile à déboguer car vous verrez le navigateur en action)
  // - aucun viewport par défaut (`defaultViewport: null` - la page du site web sera en pleine largeur et hauteur)
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
  });

  // Ouvrir une nouvelle page
  const page = await browser.newPage();

  // Sur cette nouvelle page :
  // - ouvrir le site web "http://quotes.toscrape.com/"
  // - attendre jusqu'à ce que le contenu du dom soit chargé (HTML est prêt)
  await page.goto("http://quotes.toscrape.com/", {
    waitUntil: "domcontentloaded",
  });

  // Obtenir les données de la page
  const quotes = await page.evaluate(() => {
    // Récupérer le premier élément avec la classe "quote"
    const quote = document.querySelector(".quote");

    // Récupérer les sous-éléments de l'élément de citation précédemment récupéré
    // Obtenir le texte affiché et le retourner (`.innerText`)
    const text = quote.querySelector(".text").innerText;
    const author = quote.querySelector(".author").innerText;

    return { text, author };
  });

  // Afficher les citations
  console.log(quotes);

  // Fermer le navigateur
  await browser.close();
};

// Démarrer le scraping
getQuotes();

```

Une chose intéressante à souligner est que le nom de la fonction pour sélectionner un élément est le même que dans l'inspecteur du navigateur. Voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-362.png)
_Après avoir exécuté l'instruction `document.querySelector` dans l'inspecteur du navigateur, nous avons la première citation comme résultat (comme avec Puppeteer)_

Lançons notre script une fois de plus et voyons ce que nous avons comme résultat :

```json
{
  text: "\u201cLe monde tel que nous l'avons créé est un processus de notre pensée. Il ne peut être changé sans changer notre pensée.\u201d",
  author: "Albert Einstein"
}
```

Nous l'avons fait ! Notre premier élément scrapé est ici, directement dans le terminal. Maintenant, développons-le et récupérons toutes les citations de la page actuelle. 🔥

### Comment récupérer toutes les citations de la page actuelle

Maintenant que nous savons comment récupérer une citation, modifions un peu notre code pour obtenir toutes les citations et extraire leurs données une par une.

Précédemment, nous avons utilisé `document.getQuerySelector` pour sélectionner le premier élément correspondant (la première citation). Pour pouvoir récupérer toutes les citations, nous aurons besoin de la fonction `document.querySelectorAll` à la place.

Nous devrons suivre ces étapes pour que cela fonctionne :

* Remplacer `document.getQuerySelector` par `document.querySelectorAll` (elle récupérera tous les éléments `<div>` avec le nom de classe `quote` et les retournera)
* Convertir les éléments récupérés en une liste avec `Array.from(quoteList)` (elle garantira que la liste des citations est itérable)
* Déplacer notre code précédent pour obtenir le texte et l'auteur de la citation à l'intérieur de la boucle et retourner le résultat (elle extraira les éléments avec les noms de classe `text` et `author` sous `<div class="quote">` pour chaque citation)

Voici la mise à jour du code :

```javascript
import puppeteer from "puppeteer";

const getQuotes = async () => {
  // Démarrer une session Puppeteer avec :
  // - un navigateur visible (`headless: false` - plus facile à déboguer car vous verrez le navigateur en action)
  // - aucun viewport par défaut (`defaultViewport: null` - la page du site web sera en pleine largeur et hauteur)
  const browser = await puppeteer.launch({
    headless: false,
    defaultViewport: null,
  });

  // Ouvrir une nouvelle page
  const page = await browser.newPage();

  // Sur cette nouvelle page :
  // - ouvrir le site web "http://quotes.toscrape.com/"
  // - attendre jusqu'à ce que le contenu du dom soit chargé (HTML est prêt)
  await page.goto("http://quotes.toscrape.com/", {
    waitUntil: "domcontentloaded",
  });

  // Obtenir les données de la page
  const quotes = await page.evaluate(() => {
    // Récupérer le premier élément avec la classe "quote"
    // Obtenir le texte affiché et le retourner
    const quoteList = document.querySelectorAll(".quote");

    // Convertir la quoteList en un tableau itérable
    // Pour chaque citation, récupérer le texte et l'auteur
    return Array.from(quoteList).map((quote) => {
      // Récupérer les sous-éléments de l'élément de citation précédemment récupéré
      // Obtenir le texte affiché et le retourner (`.innerText`)
      const text = quote.querySelector(".text").innerText;
      const author = quote.querySelector(".author").innerText;

      return { text, author };
    });
  });

  // Afficher les citations
  console.log(quotes);

  // Fermer le navigateur
  await browser.close();
};

// Démarrer le scraping
getQuotes();

```

En résultat final, si nous exécutons notre script une fois de plus, nous devrions avoir une liste de citations comme résultat. Chaque élément de cette liste devrait avoir une propriété texte et auteur.

```json
[
  {
    text: "\u201cLe monde tel que nous l'avons créé est un processus de notre pensée. Il ne peut être changé sans changer notre pensée.\u201d",
    author: "Albert Einstein"
  },
  {
    text: "\u201cCe sont nos choix, Harry, qui montrent ce que nous sommes vraiment, bien plus que nos capacités.\u201d",
    author: "J.K. Rowling"
  },
  {
    text: "\u201cIl n'y a que deux façons de vivre sa vie. L'une est de croire que rien n'est un miracle. L'autre est de croire que tout est un miracle.\u201d",
    author: "Albert Einstein"
  },
  {
    text: "\u201cLa personne, qu'elle soit un gentleman ou une dame, qui n'a pas de plaisir à lire un bon roman, doit être incroyablement stupide.\u201d",
    author: "Jane Austen"
  },
  {
    text: "\u201cL'imperfection est la beauté, la folie est le génie et il est préférable d'être absolument ridicule que absolument ennuyeux.\u201d",
    author: "Marilyn Monroe"
  },
  {
    text: "\u201cEssayez de ne pas devenir un homme de succès. Devenez plutôt un homme de valeur.\u201d",
    author: "Albert Einstein"
  },
  {
    text: "\u201cIl est préférable d'être haï pour ce que l'on est que d'être aimé pour ce que l'on n'est pas.\u201d",
    author: "André Gide"
  },
  {
    text: "\u201cJe n'ai pas échoué. J'ai simplement trouvé 10 000 façons qui ne fonctionnent pas.\u201d",
    author: "Thomas A. Edison"
  },
  {
    text: "\u201cUne femme est comme un sachet de thé ; on ne sait jamais à quel point elle est forte jusqu'à ce qu'elle soit dans l'eau chaude.\u201d",
    author: "Eleanor Roosevelt"
  },
  {
    text: "\u201cUne journée sans soleil est comme, vous savez, la nuit.\u201d",
    author: "Steve Martin"
  }
]
```

Bon travail ! Toutes les citations de la première page sont maintenant scrapées par notre script. 👍

### Comment passer à la page suivante

Notre script est maintenant capable de récupérer toutes les citations d'une page. Ce qui serait intéressant, c'est de cliquer sur le bouton "Page suivante" en bas de la page et de faire de même sur la deuxième page.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-363.png)
_Bouton "Suivant" en bas de la page Quotes to Scrape_

Retour à notre inspecteur de navigateur, et trouvons comment nous pouvons cibler cet élément en utilisant des sélecteurs CSS.

Comme nous pouvons le remarquer, le bouton suivant est placé sous une liste non ordonnée `<ul>` avec un nom de classe `pager` (`<ul class="pager">`). Cette liste a un élément `<li>` avec un nom de classe `next` (`<li class="next">`). Enfin, il y a une ancre de lien `<a>` qui mène à la deuxième page (`<a href="/page/2/">`).

En CSS, si nous voulons cibler ce lien spécifique, il y a différentes façons de le faire. Nous pouvons faire :

* `.next > a` : mais, c'est risqué car si un autre élément avec `.next` comme élément parent contient un lien, il cliquera dessus.
* `.pager > .next > a` : plus sûr, car nous nous assurons que le lien doit être à l'intérieur de l'élément parent `.pager` sous l'élément `.next`. Il y a un faible risque d'avoir cette hiérarchie plus d'une fois.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-356.png)
_Un exemple de la façon dont le bouton "Suivant" est rendu dans le HTML_

Pour cliquer sur ce bouton, à la fin de notre script après le `console.log(quotes);`, vous pouvez ajouter ce qui suit : `await page.click(".pager > .next > a");`.

Puisque nous fermons maintenant la page du navigateur avec `await browser.close();` après que toutes les instructions soient terminées, vous devez commenter cette instruction pour voir la deuxième page ouverte dans le navigateur du scraper.

C'est temporaire et à des fins de test, mais la fin de notre fonction `getQuotes` devrait ressembler à ceci :

```javascript
  // Afficher les citations
  console.log(quotes);

  // Cliquer sur le bouton "Page suivante"
  await page.click(".pager > .next > a");

  // Fermer le navigateur
  // await browser.close();
```

Après cela, si vous exécutez notre scraper à nouveau, après avoir traité toutes les instructions, votre navigateur devrait s'arrêter sur la deuxième page :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-357.png)
_Deuxième page de Quotes to Scrape chargée après avoir cliqué sur le bouton "Suivant"_

## C'est à vous ! Voici ce que vous pouvez faire ensuite :

Félicitations pour avoir atteint la fin de cette introduction au scraping avec Puppeteer ! 👍

Maintenant, c'est à vous d'améliorer le scraper et de lui faire extraire plus de données du site Quotes to Scrape. Voici une liste d'améliorations potentielles que vous pouvez apporter :

* Naviguer entre toutes les pages en utilisant le bouton "Suivant" et récupérer les citations de toutes les pages.
* Récupérer les tags des citations (chaque citation a une liste de tags).
* Scraper la page "à propos" de l'auteur (en cliquant sur le nom de l'auteur de chaque citation).
* Catégoriser les citations par tags ou auteurs (ce n'est pas 100% lié au scraping lui-même, mais cela peut être une bonne amélioration).

N'hésitez pas à être créatif et à faire tout ce que vous jugez utile 🚀

### Le code du scraper est disponible sur GitHub

Consultez la dernière version de notre scraper sur GitHub ! Vous êtes libre de l'enregistrer, de le fork, ou de l'utiliser comme vous le souhaitez.

=> [First Puppeteer Scraper (example)](https://github.com/gaelgthomas/first-puppeteer-scraper-example)

## Début de scraping réussi : Merci d'avoir lu l'article !

J'espère que cet article vous a donné une introduction précieuse au web scraping en utilisant JavaScript et Puppeteer. Écrire cela a été un plaisir, et j'espère que vous l'avez trouvé informatif et agréable.

[Rejoignez-moi sur Twitter](https://twitter.com/gaelgthomas) pour plus de contenu comme celui-ci. Je partage régulièrement du contenu pour vous aider à développer vos compétences en développement web et serais ravi de vous avoir dans la conversation. Apprenons, grandissons et inspirons-nous mutuellement en cours de route !