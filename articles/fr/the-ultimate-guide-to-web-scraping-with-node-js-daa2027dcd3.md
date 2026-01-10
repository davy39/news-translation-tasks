---
title: Le Guide Ultime du Web Scraping avec Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T00:32:03.000Z'
originalURL: https://freecodecamp.org/news/the-ultimate-guide-to-web-scraping-with-node-js-daa2027dcd3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KkVKtysvgh2hIVRI1Irk-Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: web scraping
  slug: web-scraping
seo_title: Le Guide Ultime du Web Scraping avec Node.js
seo_desc: 'By Daniel Ni

  So what’s web scraping anyway? It involves automating away the laborious task of
  collecting information from websites.

  There are a lot of use cases for web scraping: you might want to collect prices
  from various e-commerce sites for a pr...'
---

Par Daniel Ni

Alors, qu'est-ce que le web scraping ? Il s'agit d'automatiser la tâche fastidieuse de collecte d'informations à partir de sites web.

Il existe de nombreux cas d'utilisation pour le web scraping : vous pourriez vouloir collecter des prix à partir de divers sites e-commerce pour un site de comparaison de prix. Ou peut-être avez-vous besoin des horaires de vol et des listes d'hôtels/AirBNB pour un site de voyage. Peut-être souhaitez-vous collecter des emails à partir de divers annuaires pour des leads commerciaux, ou utiliser des données d'Internet pour entraîner des modèles de machine learning/IA. Ou vous pourriez même vouloir construire un moteur de recherche comme Google !

Commencer avec le web scraping est facile, et le processus peut être divisé en deux parties principales :

* l'acquisition des données à l'aide d'une bibliothèque de requêtes HTML ou d'un navigateur headless,
* et l'analyse des données pour obtenir les informations exactes que vous souhaitez.

Ce guide vous guidera à travers le processus avec le module Node.js populaire [request-promise](https://github.com/request/request-promise), [CheerioJS](https://github.com/cheeriojs/cheerio), et [Puppeteer](https://github.com/GoogleChrome/puppeteer). En travaillant à travers les exemples de ce guide, vous apprendrez tous les conseils et astuces dont vous avez besoin pour devenir un pro de la collecte de toutes les données dont vous avez besoin avec Node.js !

Nous allons recueillir une liste de tous les noms et dates de naissance des présidents des États-Unis à partir de Wikipedia et les titres de tous les posts sur la page d'accueil de Reddit.

D'abord, installons les bibliothèques que nous allons utiliser dans ce guide (Puppeteer prendra un certain temps à installer car il doit également télécharger Chromium).

### Faire votre première requête

<script src="https://gist.github.com/scraperapi/416fa822eb16e93222b0a836514ca99a.js"></script>

Ensuite, ouvrons un nouveau fichier texte (nommez le fichier potusScraper.js), et écrivons une fonction rapide pour obtenir le HTML de la page Wikipedia "Liste des Présidents".

<script src="https://gist.github.com/scraperapi/10273ecc0a32cf9110cfcb2e443b4a14.js"></script>

Sortie :

<script src="https://gist.github.com/scraperapi/140aa0442cf8cc276bf72ce8f4722702.js"></script>

### Utiliser Chrome DevTools

Super, nous avons obtenu le HTML brut de la page web ! Mais maintenant, nous devons donner un sens à ce gros bloc de texte. Pour cela, nous allons utiliser Chrome DevTools pour nous permettre de rechercher facilement dans le HTML d'une page web.

L'utilisation de Chrome DevTools est facile : ouvrez simplement Google Chrome, et faites un clic droit sur l'élément que vous souhaitez scraper (dans ce cas, je fais un clic droit sur George Washington, car nous voulons obtenir les liens vers toutes les pages Wikipedia individuelles des présidents) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gLKhu_EO-cDqYna1P9WL_w.png)

Maintenant, cliquez simplement sur inspecter, et Chrome ouvrira son panneau DevTools, vous permettant d'inspecter facilement le code source HTML de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HSUjFgji22vjwvGi2uZe1A.png)

### Analyser le HTML avec Cheerio.js

Génial, Chrome DevTools nous montre maintenant le motif exact que nous devons rechercher dans le code (une balise "big" avec un hyperlien à l'intérieur). Utilisons Cheerio.js pour analyser le HTML que nous avons reçu précédemment afin de retourner une liste de liens vers les pages Wikipedia individuelles des présidents des États-Unis.

<script src="https://gist.github.com/scraperapi/104d72fcbcdc2b86af9f44dadca1cde4.js"></script>

Sortie :

<script src="https://gist.github.com/scraperapi/6bf511c579433289b8e7abd426ef0534.js"></script>

Nous vérifions qu'il y a exactement 45 éléments retournés (le nombre de présidents des États-Unis), ce qui signifie qu'il n'y a pas d'autres balises "big" cachées ailleurs sur la page. Maintenant, nous pouvons passer en revue et obtenir une liste de liens vers les 45 pages Wikipedia présidentielles en les obtenant à partir de la section "attribs" de chaque élément.

<script src="https://gist.github.com/scraperapi/63be1711b6b7d2ee771095777791d049.js"></script>

Sortie :

<script src="https://gist.github.com/scraperapi/5be18aa131e2a224f13f79b9d47b830b.js"></script>

Maintenant, nous avons une liste de toutes les 45 pages Wikipedia présidentielles. Créons un nouveau fichier (nommé potusParse.js), qui contiendra une fonction pour prendre une page Wikipedia présidentielle et retourner le nom et la date de naissance du président. Tout d'abord, obtenons le HTML brut de la page Wikipedia de George Washington.

<script src="https://gist.github.com/scraperapi/6bafd36cf3ba6aa12ce7eb6d45063d6a.js"></script>

Sortie :

<script src="https://gist.github.com/scraperapi/76c56e2c587809f8b776061627dc2db3.js"></script>

Utilisons une fois de plus Chrome DevTools pour trouver la syntaxe du code que nous voulons analyser, afin que nous puissions extraire le nom et la date de naissance avec Cheerio.js.

![Image](https://cdn-media-1.freecodecamp.org/images/1*exzZbuIwfrCcbTM2rr9_bw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*yth6AmHpywM77n0wEprpiA.png)

Nous voyons donc que le nom est dans une classe appelée "firstHeading" et que la date de naissance est dans une classe appelée "bday". Modifions notre code pour utiliser Cheerio.js afin d'extraire ces deux classes.

<script src="https://gist.github.com/scraperapi/51d70b35c6b45459038439e5fa118fbc.js"></script>

Sortie :

<script src="https://gist.github.com/scraperapi/459c6bdf3fd4b6c9252dccbff4dd06db.js"></script>

### Mettre le tout ensemble

Parfait ! Maintenant, enveloppons cela dans une fonction et exportons-la depuis ce module.

<script src="https://gist.github.com/scraperapi/a24369f8f0b1bb805874e3f1229b9fa3.js"></script>

Maintenant, retournons à notre fichier original potusScraper.js et importons le module potusParse.js. Nous allons ensuite l'appliquer à la liste de wikiUrls que nous avons recueillie précédemment.

<script src="https://gist.github.com/scraperapi/b46842acda7e87d5bce57175974ba11c.js"></script>

Sortie :

<script src="https://gist.github.com/scraperapi/c1f85d62704d4837c9c20fb9f11a9ecd.js"></script>

### Rendre les Pages JavaScript

Voilà ! Une liste des noms et dates de naissance de tous les 45 présidents des États-Unis. L'utilisation du seul module request-promise et de Cheerio.js devrait vous permettre de scraper la grande majorité des sites sur Internet.

Récemment, cependant, de nombreux sites ont commencé à utiliser JavaScript pour générer du contenu dynamique sur leurs sites web. Cela pose un problème pour request-promise et d'autres bibliothèques de requêtes HTTP similaires (comme axios et fetch), car elles n'obtiennent que la réponse de la requête initiale, mais elles ne peuvent pas exécuter le JavaScript comme le fait un navigateur web.

Ainsi, pour scraper les sites qui nécessitent l'exécution de JavaScript, nous avons besoin d'une autre solution. Dans notre prochain exemple, nous allons obtenir les titres de tous les posts sur la page d'accueil de Reddit. Voyons ce qui se passe lorsque nous essayons d'utiliser request-promise comme nous l'avons fait dans l'exemple précédent.

Sortie :

<script src="https://gist.github.com/scraperapi/1767e286bca624f1bc0aff8b35983b06.js"></script>

Voici à quoi ressemble la sortie :

<script src="https://gist.github.com/scraperapi/a5cb4b9d8d18878ddeefa7e6cfd21ba6.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/1*mKzPVGRR4CFKMwQw5y_YnQ.png)

Hmmm... ce n'est pas tout à fait ce que nous voulons. C'est parce que l'obtention du contenu réel nécessite d'exécuter le JavaScript sur la page ! Avec Puppeteer, ce n'est pas un problème.

Puppeteer est un module extrêmement populaire apporté par l'équipe Google Chrome qui vous permet de contrôler un navigateur headless. Cela est parfait pour scraper de manière programmatique les pages qui nécessitent l'exécution de JavaScript. Obtenons le HTML de la page d'accueil de Reddit en utilisant Puppeteer au lieu de request-promise.

<script src="https://gist.github.com/scraperapi/d29dc43d7f00451c43b8056f716b07b6.js"></script>

Sortie :

<script src="https://gist.github.com/scraperapi/1c05f2d36c9a34f93d1c78ff754c105b.js"></script>

Super ! La page est remplie avec le bon contenu !

![Image](https://cdn-media-1.freecodecamp.org/images/1*N5HtAiijcMEB_fBQvPd7Ow.png)

Maintenant, nous pouvons utiliser Chrome DevTools comme nous l'avons fait dans l'exemple précédent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tHSgjPMvn3M26N2f7Q2B1Q.png)

Il semble que Reddit place les titres à l'intérieur des balises "h2". Utilisons Cheerio.js pour extraire les balises h2 de la page.

<script src="https://gist.github.com/scraperapi/8902791ba6f4b95a7aacebc5ef1348b8.js"></script>

Sortie :

<script src="https://gist.github.com/scraperapi/636185affefd429503e349f2e1616df2.js"></script>
<style>
.gist { width: 100% !important; overflow:auto; }
</style>


### Ressources supplémentaires

Et voici la liste ! À ce stade, vous devriez vous sentir à l'aise pour écrire votre premier scraper web afin de collecter des données à partir de n'importe quel site web. Voici quelques ressources supplémentaires que vous pourriez trouver utiles lors de votre voyage de web scraping :

* [Liste des services de proxy pour le web scraping](https://www.scraperapi.com/blog/the-10-best-rotating-proxy-services-for-web-scraping)
* [Liste des outils pratiques pour le web scraping](https://www.scraperapi.com/blog/the-10-best-web-scraping-tools)
* [Liste des conseils pour le web scraping](https://www.scraperapi.com/blog/5-tips-for-web-scraping)
* [Comparaison des proxies pour le web scraping](https://www.scraperapi.com/blog/free-shared-dedicated-datacenter-residential-rotating-proxies-for-web-scraping)
* [Documentation de Cheerio](https://github.com/cheeriojs/cheerio)
* [Documentation de Puppeteer](https://github.com/GoogleChrome/puppeteer)