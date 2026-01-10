---
title: Comment Créer une API Personnalisée à Partir de N'importe Quel Site Web en
  Utilisant Puppeteer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-27T13:33:54.000Z'
originalURL: https://freecodecamp.org/news/create-api-website-using-puppeteer
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/F4C23721-4609-4B8B-A907-36ACDF146287.jpg
tags:
- name: api
  slug: api
- name: node js
  slug: node-js
- name: puppeteer
  slug: puppeteer
- name: Web Development
  slug: web-development
seo_title: Comment Créer une API Personnalisée à Partir de N'importe Quel Site Web
  en Utilisant Puppeteer
seo_desc: 'By Tarique Ejaz

  It often happens that you come across a website and are forced to perform a set
  of actions to finally get some data. You are then faced with a dilemma: how do you
  make this data available in a form which can easily be consumed by your...'
---

Par Tarique Ejaz

Il arrive souvent que vous tombiez sur un site web et que vous soyez obligé d'effectuer une série d'actions pour enfin obtenir certaines données. Vous êtes alors confronté à un dilemme : comment rendre ces données disponibles sous une forme qui peut être facilement consommée par votre application ?

Le scraping vient à la rescousse dans un tel cas. Et choisir le bon outil pour le travail est assez important.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/puppeteer-2-3.png)
_L'API est juste une façon de regarder un site web après tout (Source : XKCD Comics)_

## Puppeteer : Pas Juste Une Autre Bibliothèque de Scraping

[Puppeteer](https://github.com/puppeteer/puppeteer) est une bibliothèque Node.js maintenue par l'équipe Chrome Devtools de Google. Elle exécute essentiellement une instance de Chromium ou Chrome (peut-être le nom le plus reconnaissable) de manière headless (ou configurable) et expose un ensemble d'API de haut niveau.

D'après sa [documentation officielle](https://pptr.dev/), Puppeteer est normalement utilisé pour plusieurs processus qui ne sont pas limités aux suivants :

* Générer des captures d'écran et des PDF
* Explorer une SPA et générer du contenu pré-rendu (c'est-à-dire Server Side Rendering)
* Tester les extensions Chrome
* Tests d'automatisation des interfaces web
* Diagnostic des problèmes de performance grâce à des techniques comme la capture de la trace de la timeline d'un site web

Pour notre cas, nous devons pouvoir accéder à un site web et mapper les données sous une forme qui peut être facilement consommée par notre application.

Cela semble simple ? La mise en œuvre n'est pas non plus si complexe. Commençons.

## Enchaînement du Code

Mon affection pour les produits Amazon me pousse à utiliser l'une de leurs pages de liste de produits comme exemple ici. Nous allons mettre en œuvre notre cas d'utilisation en deux étapes :

* Extraire les données de la page et les mapper sous une forme JSON facilement consommable
* Ajouter une petite touche d'automatisation pour faciliter un peu notre vie

Vous pouvez trouver le code complet dans ce [dépôt](https://github.com/tejazz/article-snippets/tree/master/puppeteer-api).

Nous allons extraire les données de ce lien : [https://www.amazon.in/s?k=Shirts&ref=nb_sb_noss_2](https://www.amazon.in/s?k=Shirts&ref=nb_sb_noss_2) (une liste des chemises les plus recherchées comme montré dans l'image) sous une forme servable par une API.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot--53-.png)
_Amazon Inde - Page de Liste de Chemises_

Avant de commencer à utiliser Puppeteer de manière extensive dans cette section, nous devons comprendre les deux classes principales qu'il fournit.

* **[Browser:](https://pptr.dev/#?product=Puppeteer&version=v3.1.0&show=api-class-browser)** lance une instance de Chrome lorsque nous utilisons `puppeteer.launch` ou `puppeteer.connect`. Cela fonctionne comme une simple émulation de navigateur.
* **[Page:](https://pptr.dev/#?product=Puppeteer&version=v3.1.0&show=api-class-page)** ressemble à un seul onglet d'un navigateur Chrome. Il fournit un ensemble exhaustif de méthodes que vous pouvez utiliser avec une instance de page particulière et est invoqué lorsque nous appelons `browser.newPage`. Tout comme vous pouvez créer plusieurs onglets dans le navigateur, vous pouvez créer plusieurs instances de page en même temps dans Puppeteer.

### Configuration de Puppeteer et Navigation vers l'URL Cible

Nous commençons à configurer Puppeteer en utilisant le module npm fourni. Après avoir installé Puppeteer, nous créons une instance du navigateur et de la classe de page et naviguons vers l'URL cible.

```js
const puppeteer = require('puppeteer');

const url = 'https://www.amazon.in/s?k=Shirts&ref=nb_sb_noss_2';

async function fetchProductList(url) {
    const browser = await puppeteer.launch({ 
        headless: true, // false: permet de voir l'instance de Chrome en action
        defaultViewport: null, // (optionnel) utile uniquement en mode non-headless
    });
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2' });
    ...
}

fetchProductList(url);

```

Nous utilisons `networkidle2` comme valeur pour l'option `waitUntil` lors de la navigation vers l'URL. Cela garantit que l'état de chargement de la page est considéré comme final lorsqu'il n'y a pas plus de 2 connexions en cours d'exécution pendant au moins 500 ms.

> **Note :** Vous n'avez pas besoin d'avoir Chrome ou une instance de celui-ci installée sur votre système pour que Puppeteer fonctionne. Il est déjà livré avec une version légère de celui-ci, intégrée à la bibliothèque.

### Méthodes de Page pour Extraire et Mapper les Données

Le DOM a déjà été chargé dans l'instance de page créée. Nous allons utiliser la méthode `page.evaluate()` pour interroger le DOM.

Avant de commencer, nous devons déterminer les points de données exacts que nous devons extraire. Dans l'exemple actuel, chacun des objets produit ressemblera à quelque chose comme ceci.

```js
{
	brand: 'Nom de la Marque', 
    product: 'Nom du Produit',
    url: 'https://www.amazon.in/url.du.produit.com/',
    image: 'https://www.amazon.in/image.jpg',
    price: '₹599',
}
```

Nous avons défini la structure que nous voulons atteindre. Il est temps de commencer à inspecter le DOM pour les identifiants. Nous vérifions les sélecteurs qui apparaissent tout au long des éléments à mapper. Nous utiliserons principalement `[document.querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)` et `[document.querySelectorAll](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)` pour parcourir le DOM.

```js
...

async function fetchProductList(url) {
	...
    
    await page.waitFor('div[data-cel-widget^="search_result_"]');

    const result = await page.evaluate(() => {
        // compte le nombre total de produits
        let totalSearchResults = Array.from(document.querySelectorAll('div[data-cel-widget^="search_result_"]')).length;

        let productsList = [];

        for (let i = 1; i < totalSearchResults - 1; i++) {
            let product = {
                brand: '',
                product: '',
            };
            let onlyProduct = false;
            let emptyProductMeta = false;
			
            // parcours pour les noms de marque et de produit
            let productNodes = Array.from(document.querySelectorAll(`div[data-cel-widget="search_result_${i}"] .a-size-base-plus.a-color-base`));

            if (productNodes.length === 0) {
                // parcours pour les noms de marque et de produit
				// (au cas où le parcours précédent aurait retourné des éléments vides)
                productNodes = Array.from(document.querySelectorAll(`div[data-cel-widget="search_result_${i}"] .a-size-medium.a-color-base.a-text-normal`));
                productNodes.length > 0 ? onlyProduct = true : emptyProductMeta = true;
            }

            let productsDetails = productNodes.map(el => el.innerText);

            if (!emptyProductMeta) {
                product.brand = onlyProduct ? '' : productsDetails[0];
                product.product = onlyProduct ? productsDetails[0] : productsDetails[1];
            }
			
            // parcours pour l'image du produit
            let rawImage = document.querySelector(`div[data-cel-widget="search_result_${i}"] .s-image`);
            product.image = rawImage ? rawImage.src : '';
			
            // parcours pour l'URL du produit
            let rawUrl = document.querySelector(`div[data-cel-widget="search_result_${i}"] a[target="_blank"].a-link-normal`);
            product.url = rawUrl ? rawUrl.href : '';

            // parcours pour le prix du produit
            let rawPrice = document.querySelector(`div[data-cel-widget="search_result_${i}"] span.a-offscreen`);
            product.price = rawPrice ? rawPrice.innerText : '';

            if (typeof product.product !== 'undefined') {
                !product.product.trim() ? null : productsList = productsList.concat(product);
            }
        }

        return productsList;
    });
    
    ...
}
    
...
```

// parcours pour les noms de marque et de produit

Après avoir investigué le DOM, nous voyons que chaque élément listé est enfermé sous un élément avec le sélecteur `div[data-cel-widget^="search_result_"]`. Ce sélecteur particulier recherche toutes les balises `div` avec l'attribut `data-cel-widget` qui ont une valeur commençant par `search_result_`.

De même, nous mappons les sélecteurs pour les paramètres dont nous avons besoin comme listé. Si vous voulez en savoir plus sur le parcours du DOM, vous pouvez consulter cet article informatif de [Zell](https://zellwk.com/blog/dom-traversals/).

* **nombre total d'éléments listés :** `div[data-cel-widget^="search_result_"]`
* **marque :** `div[data-cel-widget="search_result_${i}"] .a-size-base-plus.a-color-base` (`i` représente le numéro de nœud dans `nombre total d'éléments listés`)
* **produit :** `div[data-cel-widget="search_result_${i}"] .a-size-base-plus.a-color-base` ou `div[data-cel-widget="search_result_${i}"] .a-size-medium.a-color-base.a-text-normal` (`i` représente le numéro de nœud dans `nombre total d'éléments listés`)
* **url :** `div[data-cel-widget="search_result_${i}"] a[target="_blank"].a-link-normal` (`i` représente le numéro de nœud dans `nombre total d'éléments listés`)
* **image :** `div[data-cel-widget="search_result_${i}"] .s-image` (`i` représente le numéro de nœud dans `nombre total d'éléments listés`)
* **prix :** `div[data-cel-widget="search_result_${i}"] span.a-offscreen` (`i` représente le numéro de nœud dans `nombre total d'éléments listés`)

> **Note :** Nous attendons que les éléments nommés avec le sélecteur `div[data-cel-widget^="search_result_"]` soient disponibles sur la page en utilisant la méthode `page.waitFor`.

Une fois la méthode `page.evaluate` invoquée, nous pouvons voir les données dont nous avons besoin enregistrées.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-162.png)
_Cela fonctionne ! Nous avons nos données d'API prêtes à servir ce dont nous avons besoin_

### Ajout d'Automatisation pour Faciliter le Flux

Jusqu'à présent, nous sommes capables de naviguer vers une page, d'extraire les données dont nous avons besoin et de les transformer sous une forme prête pour une API. Cela semble tout à fait correct.

Cependant, considérons un instant un cas où vous devez naviguer vers une URL à partir d'une autre en effectuant certaines actions – et ensuite essayer d'extraire les données dont vous avez besoin.

Cela rendrait-il votre vie un peu plus compliquée ? Pas du tout. Puppeteer peut facilement imiter le comportement de l'utilisateur. Il est temps d'ajouter un peu d'automatisation à notre cas d'utilisation existant.

Contrairement à l'exemple précédent, nous allons à la page d'accueil de `amazon.in` et recherchons 'Shirts'. Cela nous mènera à la page de liste des produits et nous pourrons extraire les données requises du DOM. Facile. Regardons le code.

```js
...

async function fetchProductList(url, searchTerm) {
	...
	await page.goto(url, { waitUntil: 'networkidle2' });

    await page.waitFor('input[name="field-keywords"]');
    await page.evaluate(val => document.querySelector('input[name="field-keywords"]').value = val, searchTerm);

    await page.click('div.nav-search-submit.nav-sprite');
    
    // Logique de parcours du DOM et de mappage des données
	// retourne un tableau productsList
    ...
}

fetchProductList('https://amazon.in', 'Shirts');

```

Nous pouvons voir que nous attendons que la boîte de recherche soit disponible, puis nous ajoutons le `searchTerm` passé en utilisant `page.evaluate`. Nous naviguons ensuite vers la page de liste des produits en émulant l'action de clic sur le bouton 'rechercher' et en exposant le DOM.

La complexité de l'automatisation varie d'un cas d'utilisation à l'autre.

### Quelques Pièges Notables : Un Petit Avertissement

L'API de Puppeteer est assez complète, mais il y a quelques pièges que j'ai rencontrés en travaillant avec elle. N'oubliez pas que tous ces pièges ne sont pas directement liés à Puppeteer, mais tendent à mieux fonctionner avec lui.

* Puppeteer crée une instance de navigateur Chrome comme déjà mentionné. Cependant, il est probable que certains sites web existants bloquent l'accès s'ils suspectent une activité de bot. Il existe un package appelé `[user-agents](https://www.npmjs.com/package/user-agents)` qui peut être utilisé avec Puppeteer pour randomiser l'agent utilisateur du navigateur.

> **Note :** Le scraping d'un site web se situe quelque part dans les zones grises de l'acceptation légale. Je recommande de l'utiliser avec prudence et de vérifier les règles là où vous vivez.

```js
const puppeteer = require('puppeteer');
const userAgent = require('user-agents');

...

const browser = await puppeteer.launch({ headless: true, defaultViewport: null });
const page = await browser.newPage();
await page.setUserAgent(userAgent.toString());

...
```

* Nous avons rencontré `defaultViewport: null` lors du lancement de notre instance Chrome et je l'avais listé comme optionnel. Cela est dû au fait qu'il est utile uniquement lorsque vous visualisez l'instance Chrome en cours de lancement. Il empêche la largeur et la hauteur du site web d'être affectées lors de son rendu.
* Puppeteer n'est pas la solution ultime en matière de performance. Vous, en tant que développeur, devrez l'optimiser pour augmenter son efficacité de performance grâce à des actions comme la limitation des animations sur le site, en permettant uniquement les appels réseau essentiels, etc.
* N'oubliez pas de toujours terminer une session Puppeteer en fermant l'instance du navigateur en utilisant `browser.close`. (J'ai oublié de le faire lors de la première tentative) Cela aide à terminer une session de navigateur en cours d'exécution.
* Certaines opérations JavaScript courantes comme `console.log()` ne fonctionneront pas dans le cadre des méthodes de page. La raison étant que le [contexte de page/contexte de navigateur](https://pptr.dev/#?product=Puppeteer&version=v3.1.0&show=api-class-browsercontext) diffère du contexte de nœud dans lequel votre application est en cours d'exécution.

Ce sont quelques-uns des pièges que j'ai remarqués. Si vous en avez d'autres, n'hésitez pas à me les communiquer. J'adorerais en apprendre davantage.

Terminé ? Exécutons l'application.

## Site Web vers Votre API : Tout Rassembler

L'application est exécutée en mode non-headless afin que vous puissiez voir exactement ce qui se passe. Nous allons automatiser la navigation vers la page de liste des produits à partir de laquelle nous obtenons les données.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ezgif.com-video-to-gif--1-.gif)

Voilà. Vous avez votre propre configuration de données consommables par API à partir du site web de votre choix. Tout ce que vous avez à faire maintenant est de connecter cela avec un framework côté serveur comme [`express`](https://expressjs.com/) et vous êtes prêt à partir.

## Conclusion

Il y a tant de choses que vous pouvez faire avec Puppeteer. Ce n'est qu'un cas d'utilisation particulier. Je vous recommande de passer un peu de temps à lire la documentation officielle. Je vais faire de même.

Puppeteer est utilisé de manière extensive dans certaines des plus grandes organisations pour des tâches d'automatisation comme les tests et le rendu côté serveur, entre autres.

Il n'y a pas de meilleur moment pour commencer avec Puppeteer que maintenant.

Si vous avez des questions ou des commentaires, vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/tarique-ejaz/) ou [Twitter](https://twitter.com/theguynameddate).

En attendant, continuez à coder.