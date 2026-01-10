---
title: 'Web scraping pour les développeurs web : un résumé concis'
subtitle: ''
author: David Karolyi
co_authors: []
series: null
date: '2019-02-13T17:59:30.000Z'
originalURL: https://freecodecamp.org/news/web-scraping-for-web-developers-a-concise-summary-3af3d0ca4069
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QYXgeKvQq5M0lMGMRFXJvA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: web scraping
  slug: web-scraping
seo_title: 'Web scraping pour les développeurs web : un résumé concis'
seo_desc: 'Knowing one approach to web scraping may solve your problem in the short
  term, but all methods have their own strengths and weaknesses. Being aware of this
  can save you time and help you to solve a task more efficiently.

  Numerous resources exist, whi...'
---

Connaître une approche du web scraping peut résoudre votre problème à court terme, mais toutes les méthodes ont leurs propres forces et faiblesses. Être conscient de cela peut vous faire gagner du temps et vous aider à résoudre une tâche plus efficacement.

De nombreuses ressources existent, qui vous montreront une seule technique pour extraire des données d'une page web. La réalité est que plusieurs solutions et outils peuvent être utilisés pour cela.

Quelles sont vos options pour extraire des données d'une page web de manière programmatique ?

Quels sont les avantages et les inconvénients de chaque approche ?

Comment utiliser les services cloud pour augmenter le degré d'automatisation ?

**Ce guide vise à répondre à ces questions.**

Je suppose que vous avez une compréhension de base des navigateurs en général, des requêtes **HTTP**, du **DOM** (Document Object Model), du **HTML**, des sélecteurs **CSS** et du **JavaScript asynchrone**.

Si ces termes vous semblent inconnus, je vous suggère de vérifier ces sujets avant de continuer la lecture. Les exemples sont implémentés en Node.js, mais vous pouvez transférer la théorie dans d'autres langages si nécessaire.

### Contenu statique

#### Source HTML

Commençons par l'approche la plus simple.

Si vous prévoyez de scraper une page web, c'est la première méthode à essayer. Elle nécessite une quantité négligeable de puissance de calcul et le moins de temps pour être implémentée.

Cependant, cela **ne fonctionne que si le code source HTML contient les données** que vous ciblez. Pour vérifier cela dans Chrome, faites un clic droit sur la page et choisissez _Afficher le code source de la page_. Vous devriez maintenant voir le code source HTML.

Il est important de noter ici que vous ne verrez pas le même code en utilisant l'outil d'inspection de Chrome, car il montre la structure HTML liée à l'état actuel de la page, qui n'est pas nécessairement la même que le document HTML source que vous pouvez obtenir du serveur.

Une fois que vous avez trouvé les données ici, écrivez un [sélecteur CSS](https://www.w3schools.com/cssref/css_selectors.asp) appartenant à l'élément enveloppant, pour avoir une référence plus tard.

Pour l'implémenter, vous pouvez envoyer une requête HTTP GET à l'URL de la page et vous obtiendrez le code source HTML en retour.

Dans **Node**, vous pouvez utiliser un outil appelé [CheerioJS](https://github.com/cheeriojs/cheerio) pour analyser ce HTML brut et extraire les données en utilisant un sélecteur. Le code ressemble à quelque chose comme ceci :

```js
const fetch = require('node-fetch');
const cheerio = require('cheerio');

const url = 'https://example.com/';
const selector = '.example';

fetch(url)
  .then(res => res.text())
  .then(html => {
    const $ = cheerio.load(html);
    const data = $(selector);
    console.log(data.text());
  });
```

### Contenu dynamique

Dans de nombreux cas, vous ne pouvez pas accéder aux informations à partir du code HTML brut, car le DOM a été manipulé par un certain JavaScript, exécuté en arrière-plan. Un exemple typique de cela est une SPA (Single Page Application), où le document HTML contient une quantité minimale d'informations, et le JavaScript le remplit à l'exécution.

Dans cette situation, une solution consiste à construire le DOM et à exécuter les scripts situés dans le code source HTML, tout comme le fait un navigateur. Après cela, les données peuvent être extraites de cet objet avec des sélecteurs.

#### Navigateurs sans tête

Cela peut être réalisé en utilisant un navigateur sans tête. Un navigateur sans tête est presque la même chose que celui que vous utilisez probablement tous les jours, mais sans interface utilisateur. Il fonctionne en arrière-plan et vous pouvez le contrôler de manière programmatique au lieu de cliquer avec votre souris et de taper avec un clavier.

Un choix populaire pour un navigateur sans tête est [Puppeteer](https://github.com/GoogleChrome/puppeteer). Il s'agit d'une bibliothèque Node facile à utiliser qui fournit une API de haut niveau pour contrôler Chrome en mode sans tête. Il peut être configuré pour fonctionner en mode non sans tête, ce qui est pratique pendant le développement. Le code suivant fait la même chose qu'avant, mais il fonctionnera également avec des pages dynamiques :

```js
const puppeteer = require('puppeteer');

async function getData(url, selector){
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);
  const data = await page.evaluate(selector => {
    return document.querySelector(selector).innerText;
  }, selector);
  await browser.close();
  return data;
}

const url = 'https://example.com';
const selector = '.example';
getData(url,selector)
  .then(result => console.log(result));
```

Bien sûr, vous pouvez faire des choses plus intéressantes avec Puppeteer, il vaut donc la peine de consulter la [documentation](https://pptr.dev/). Voici un extrait de code qui navigue vers une URL, prend une capture d'écran et l'enregistre :

```js
const puppeteer = require('puppeteer');

async function takeScreenshot(url,path){
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);
  await page.screenshot({path: path});
  await browser.close();
}

const url = 'https://example.com';
const path = 'example.png';
takeScreenshot(url, path);
```

Comme vous pouvez l'imaginer, l'exécution d'un navigateur nécessite beaucoup plus de puissance de calcul que l'envoi d'une simple requête GET et l'analyse de la réponse. Par conséquent, l'exécution est relativement coûteuse et lente. Non seulement cela, mais l'inclusion d'un navigateur en tant que dépendance rend le package de déploiement massif.

En revanche, cette méthode est très flexible. Vous pouvez l'utiliser pour naviguer autour des pages, simuler des clics, des mouvements de souris et des événements de clavier, remplir des formulaires, prendre des captures d'écran ou générer des PDF de pages, exécuter des commandes dans la console, sélectionner des éléments pour extraire leur contenu textuel. Basiquement, tout ce qui peut être fait manuellement dans un navigateur peut être fait.

#### Construire uniquement le DOM

Vous pouvez penser qu'il est un peu excessif de simuler un navigateur complet juste pour construire un DOM. En fait, c'est le cas, au moins dans certaines circonstances.

Il existe une bibliothèque Node, appelée [Jsdom](https://github.com/jsdom/jsdom), qui analysera le HTML que vous lui passez, tout comme le fait un navigateur. Cependant, ce n'est pas un navigateur, mais **un outil pour construire un DOM à partir d'un code source HTML donné**, tout en exécutant également le code JavaScript contenu dans ce HTML.

Grâce à cette abstraction, Jsdom est capable de fonctionner plus rapidement qu'un navigateur sans tête. Si c'est plus rapide, pourquoi ne pas l'utiliser à la place des navigateurs sans tête tout le temps ?

Citation de la documentation :

> Les gens ont souvent des problèmes avec le chargement asynchrone de scripts lors de l'utilisation de jsdom. De nombreuses pages chargent des scripts de manière asynchrone, mais il n'y a aucun moyen de savoir quand ils ont terminé de le faire, et donc quand c'est un bon moment pour exécuter votre code et inspecter la structure DOM résultante. C'est une limitation fondamentale.

>  Cela peut être contourné en vérifiant périodiquement la présence d'un élément spécifique.

Cette solution est montrée dans l'exemple. Il vérifie toutes les 100 ms si l'élément est apparu ou s'il a expiré (après 2 secondes).

Il lance également souvent des messages d'erreur désagréables lorsqu'une fonctionnalité du navigateur dans la page n'est pas implémentée par Jsdom, comme : « Erreur : Non implémenté : window.alert » ou « Erreur : Non implémenté : window.scrollTo ». Ce problème peut également être résolu avec quelques solutions de contournement ([consoles virtuelles](https://github.com/jsdom/jsdom#virtual-consoles)).

En général, c'est une API de niveau inférieur à Puppeteer, vous devez donc implémenter certaines choses vous-même.

Ces choses le rendent un peu plus compliqué à utiliser, comme vous le verrez dans l'exemple. Puppeteer résout tous ces problèmes pour vous en arrière-plan et le rend extrêmement facile à utiliser. Jsdom, pour ce travail supplémentaire, offrira une solution rapide et légère.

Voyons le même exemple qu'auparavant, mais avec Jsdom :

```js
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

async function getData(url,selector,timeout) {
  const virtualConsole = new jsdom.VirtualConsole();
  virtualConsole.sendTo(console, { omitJSDOMErrors: true });
  const dom = await JSDOM.fromURL(url, {
    runScripts: "dangerously",
    resources: "usable",
    virtualConsole
  });
  const data = await new Promise((res,rej)=>{
    const started = Date.now();
    const timer = setInterval(() => {
      const element = dom.window.document.querySelector(selector)
      if (element) {
        res(element.textContent);
        clearInterval(timer);
      }
      else if(Date.now()-started > timeout){
        rej("Timed out");
        clearInterval(timer);
      }
    }, 100);
  });
  dom.window.close();
  return data;
}

const url = "https://example.com/";
const selector = ".example";
getData(url,selector,2000).then(result => console.log(result));
```

#### Ingénierie inverse

Jsdom est une solution rapide et légère, mais il est possible d'aller encore plus loin pour simplifier les choses.

Avons-nous même besoin de simuler le DOM ?

En général, la page web que vous souhaitez scraper est composée du même HTML, du même JavaScript, des mêmes technologies que vous connaissez déjà. Donc, **si vous trouvez ce morceau de code à partir duquel les données ciblées ont été dérivées, vous pouvez répéter la même opération afin d'obtenir le même résultat.**

Si nous **sur-simplifions** les choses, les données que vous recherchez peuvent être :

* partie du code source HTML (comme nous l'avons vu dans le premier paragraphe),
* partie d'un fichier statique, référencé dans le document HTML (par exemple une chaîne dans un fichier JavaScript),
* une réponse à une requête réseau (par exemple, un certain code JavaScript a envoyé une requête AJAX à un serveur, qui a répondu avec une chaîne JSON).

**Toutes ces sources de données peuvent être accessibles avec des requêtes réseau.** De notre perspective, peu importe si la page web utilise HTTP, WebSockets ou tout autre protocole de communication, car tous sont reproductibles en théorie.

Une fois que vous avez localisé la ressource hébergeant les données, vous pouvez envoyer une requête réseau similaire au même serveur que la page originale. En résultat, vous obtenez la réponse, contenant les données ciblées, qui peuvent être facilement extraites avec des expressions régulières, des méthodes de chaîne, JSON.parse, etc.

En termes simples, vous pouvez simplement prendre la ressource où se trouvent les données, au lieu de traiter et de charger tout le contenu. De cette manière, le problème, montré dans les exemples précédents, peut être résolu avec une seule requête HTTP au lieu de contrôler un navigateur ou un objet JavaScript complexe.

Cette solution semble facile en théorie, mais la plupart du temps, elle peut être **vraiment chronophage** à réaliser et nécessite une certaine expérience de travail avec les pages web et les serveurs.

Un point de départ possible pour la recherche est d'observer le trafic réseau. Un excellent outil pour cela est l'onglet [Network dans Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/network-performance/). Vous verrez toutes les requêtes sortantes avec les réponses (y compris les fichiers statiques, les requêtes AJAX, etc.), vous pouvez donc les parcourir et rechercher les données.

Cela peut être encore plus lent si la réponse est modifiée par un certain code avant d'être rendue à l'écran. Dans ce cas, vous devez trouver ce morceau de code et comprendre ce qui se passe.

Comme vous le voyez, cette solution peut nécessiter beaucoup plus de travail que les méthodes présentées jusqu'à présent. D'un autre côté, une fois implémentée, elle offre les meilleures performances.

Ce graphique montre le temps d'exécution requis et la taille du package comparé à Jsdom et Puppeteer :

![Image](https://cdn-media-1.freecodecamp.org/images/1*36D8phqv-iUx6SVmrqhJcQ.jpeg)

Ces résultats ne sont pas basés sur des mesures précises et peuvent varier dans chaque situation, mais montrent bien la différence approximative entre ces techniques.

### Intégration des services cloud

Supposons que vous avez implémenté l'une des solutions listées jusqu'à présent. Une façon d'exécuter votre script est d'allumer votre ordinateur, d'ouvrir un terminal et de l'exécuter manuellement.

Cela peut devenir rapidement ennuyeux et inefficace, il serait donc préférable de pouvoir simplement télécharger le script sur un serveur et de l'exécuter régulièrement en fonction de sa configuration.

Cela peut être fait en exécutant un serveur réel et en configurant certaines règles sur le moment d'exécuter le script. Les serveurs excellent lorsque vous continuez à observer un élément dans une page. Dans d'autres cas, une fonction cloud est probablement une solution plus simple.

Les fonctions cloud sont essentiellement des conteneurs destinés à exécuter le code téléchargé lorsqu'un événement déclencheur se produit. Cela signifie que vous n'avez pas à gérer les serveurs, c'est fait automatiquement par le fournisseur cloud de votre choix.

Un déclencheur possible peut être un calendrier, une requête réseau et de nombreux autres événements. Vous pouvez sauvegarder les données collectées dans une base de données, les écrire dans une [feuille Google](https://developers.google.com/sheets/api/) ou les envoyer dans un [email](https://www.w3schools.com/nodejs/nodejs_email.asp). Tout dépend de votre créativité.

Les fournisseurs cloud populaires sont [Amazon Web Services](https://aws.amazon.com)(AWS), [Google Cloud Platform](https://cloud.google.com/)(GCP) et [Microsoft Azure](https://azure.microsoft.com) et tous ont un service de fonction :

* [AWS Lambda](https://aws.amazon.com/lambda/)
* [GCP Cloud Functions](https://cloud.google.com/functions/)
* [Azure Functions](https://azure.microsoft.com/services/functions/)

Ils offrent une certaine quantité d'utilisation gratuite chaque mois, que votre seul script ne dépassera probablement pas, sauf dans des cas extrêmes, mais **veuillez vérifier les prix avant utilisation**.

Si vous utilisez Puppeteer, les _Cloud Functions_ de Google sont la solution la plus simple. La taille du package zippé de Chrome sans tête (~130 Mo) dépasse la limite de taille zippée maximale d'AWS Lambda (50 Mo). Il existe quelques techniques pour le faire fonctionner avec Lambda, mais les fonctions GCP [supportent Chrome sans tête par défaut](https://cloud.google.com/blog/products/gcp/introducing-headless-chrome-support-in-cloud-functions-and-app-engine), vous devez simplement inclure Puppeteer comme dépendance dans _package.json_.

Si vous souhaitez en savoir plus sur les fonctions cloud en général, faites des recherches sur les architectures serverless. De nombreux guides ont déjà été écrits sur ce sujet et la plupart des fournisseurs ont une documentation facile à suivre.

### Résumé

Je sais que chaque sujet était un peu compressé. Vous ne pouvez probablement pas implémenter chaque solution avec cette seule connaissance, mais avec la documentation et quelques recherches personnalisées, cela ne devrait pas poser de problème.

Espérons que maintenant vous avez une vue d'ensemble de haut niveau des techniques utilisées pour collecter des données sur le web, afin que vous puissiez approfondir chaque sujet en conséquence.