---
title: Comment Construire un Bot de Recherche Simple en 30 Minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-03T20:01:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-search-bot-in-30-minutes-eb56fcedcdb1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pMm3_L9RmFcb0KLJT1SirQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: web scraping
  slug: web-scraping
seo_title: Comment Construire un Bot de Recherche Simple en 30 Minutes
seo_desc: 'By Quinn Langille

  Apartment hunting sucks, especially in Montreal. This guide will show you how to
  build a bot that stays on top of the hunt for you. This way, you’ll never have to
  endlessly refresh your searches again.

  Context

  Unlike other cities, m...'
---

Par Quinn Langille

La recherche d'un appartement est pénible, surtout à Montréal. Ce guide vous montrera comment construire un bot qui reste à l'affût pour vous. Ainsi, vous n'aurez plus jamais à actualiser sans fin vos recherches.

### Contexte

Contrairement à d'autres villes, la plupart des personnes qui louent des appartements à Montréal ont le même terme de bail. Les nouveaux baux commencent en juillet, durent 12 mois et se terminent le 30 juin. Bien que l'on puisse soutenir que cela simplifie beaucoup de choses — comme la disponibilité et les attentes — cela signifie également que la compétition est féroce.

Chaque jour, je me réveillais, actualisais mes 10 pages ouvertes de [Kijiji](https://www.kijiji.ca/) et envoyais des courriels pour demander des informations sur toutes les nouvelles annonces. Je faisais cela à nouveau au déjeuner, au dîner et avant de me coucher. Mon taux de réponse était faible — bien en dessous de 10 %. Lorsque quelqu'un répondait, sa réponse était généralement peu encourageante.

Mon prochain pas a été de relever le défi et de décrocher réellement le téléphone. Appeler a amélioré un peu mes chances. Les propriétaires étaient plus réactifs, et cette fois, il y avait généralement moins de 10 personnes devant moi. Mais définitivement encore plus de 5. Retour à la case départ.

Un jour, en me plaignant à un collègue que tout mon temps était mangé par cette chasse à l'appartement — cela m'a frappé. Je pourrais résoudre ce problème avec mon ordinateur.

En rentrant chez moi, j'ai écrit un petit programme qui surveille les recherches Kijiji pour détecter les changements. Lorsqu'il en voit, il envoie un message texte SMS à mon téléphone avec les informations pertinentes. Le reste de cet article expliquera comment j'ai fait cela.

**Note :** pour ceux qui ne se soucient pas du tutoriel, j'ai mis le scraper Kijiji en tant que dépôt open source [ici](https://github.com/quinnlangille/pad-patrol) : ?

### Construction de Pad-Patrol

Lorsque je suis rentré du travail, j'ai sorti mon ordinateur portable et lancé mon terminal. Je savais que le programme devait être léger, car je vais le faire tourner 24/7 — ou au moins jusqu'à ce que je trouve un appartement. J'ai décidé de simplement construire un script node simple que je pourrais exécuter depuis mon terminal.

#### Installation

En supposant que vous avez `node` et `npm` installés, la première étape — de tout projet node — est d'initialiser npm à l'intérieur du répertoire du projet.

Ensuite, créons un répertoire `src` où notre code résidera.

À l'intérieur du répertoire `src`, créez un fichier `index.js` où notre script ira.

Vous pouvez faire cela comme suit :

```
$ npm init // cela posera quelques questions$ mkdir src$ cd src && touch index.js
```

#### Écriture du script

Lorsque je fais un projet solo, j'ai tendance à improviser — casser des choses et puis les réparer (arguablement la meilleure façon d'apprendre). Je vais essayer de reproduire mon processus de pensée initial avec les instructions suivantes, mais faites-moi savoir si elles semblent désorganisées.

La toute première chose que nous devons faire est de faire une requête réussie à Kijiji. Pour nous assurer que nous pouvons obtenir une réponse appropriée, faisons une requête très basique.

Pour cela, nous devons installer une bibliothèque de requêtes :

```
$ npm install request-promise
```

et ensuite ajouter ce qui suit à `index.js` :

Une fois cela sauvegardé, nous pouvons exécuter `$ node src/index.js` et nous devrions voir un peu de balisage HTML dans notre console. Première étape terminée — Facile !

Parce que nous ne nous soucions que des changements de contenu, créons un simple hash de la réponse. Ainsi, nous pouvons comparer la réponse et comparer les hashs. Dans le cas où nous devons enregistrer nos résultats, cela sera beaucoup moins encombrant que le balisage brut.

Pour cela, nous pouvons utiliser un outil de hachage appelé `checksum` :

```
$ yarn add checksum
```

et ensuite :

Ok, super, cela a fonctionné ! Nos 1500 lignes de HTML ont été réduites à 32 chiffres. Maintenant, enveloppons cela dans une fonction réutilisable :

Le code ci-dessus créera un hash à partir de la valeur récupérée. Ensuite, lors de la récupération suivante, il comparera les hashs originaux et nouveaux.

S'ils sont différents, il retournera `true`. Cela a très bien fonctionné… comme, un peu trop bien. Comme vous le verrez, il retourne `true` à chaque fois ?

Après une inspection plus approfondie de la réponse de la récupération, nous pouvons voir que Kijiji a un horodatage dans l'en-tête. Cela signifie que le hash sera différent à chaque récupération. Il est important de noter que cela se serait également produit en raison des annonces tournantes et d'un tas d'autres contenus dynamiques.

La leçon à tirer de cette négligence est de toujours inspecter soigneusement votre réponse lorsque vous traitez avec une API que vous n'avez pas écrite.

Cela signifie que nous devons accéder à des bits granulaires du balisage, alors installons un package tiers pour aider à analyser la réponse. [Cheerio](https://cheerio.js.org/) est une bibliothèque qui peut ingérer du balisage HTML et le transformer en une API JavaScript accessible. Son but initial était d'aider les développeurs `jQuery` à ne pas utiliser `jQuery`, mais les intentions sont surévaluées.

Pour nous, ce sera un faux ensemble d'outils de développement Chrome !

En tant que prérequis pour utiliser Cheerio de cette manière, nous devons savoir quoi chercher dans notre balisage. Alors ouvrons Chrome et inspectons notre URL.

Si nous inspectons les annonces, nous pouvons voir que toutes les réponses de recherche ont les classes `.search-item` et `.regular-ad`. Parfait !

Nous pouvons les sélectionner avec Cheerio comme suit :

Tout comme nous l'avions prévu, cela génère un tableau d'objets bien organisés. Selon la documentation de Cheerio, tous les attributs d'un élément sont imbriqués dans une clé appelée `attribs`. Si nous retournons aux outils de développement Chrome, nous pouvons voir que chaque annonce a un attribut de données unique appelé ID. Ciblons cela — remplacez le code à l'intérieur de votre fonction `checkURL` par ce qui suit :

```
rp(siteToCheck).then(response => {  const $ = co.load(HTMLresponse);  let apartmentString = "";
```

```
  // utilisez cheerio pour analyser la réponse HTML et trouver tous les résultats de recherche  $(".search-item.regular-ad").each((i, element) => {    console.log(element.attribs["data-ad-id"]);  });});
```

Ok, super, nous obtenons une liste de numéros d'ID uniques. Ces ID sont les seules informations qui nous intéressent sur la page.

Alors retournons à notre plan initial de comparaison des hashs, sauf que nous ne hacherons que les ID uniques :

Parfait ! Cela fonctionne exactement comme prévu. Lorsque quelqu'un publie une nouvelle annonce (ou supprime une ancienne annonce, un inconvénient de la surveillance de l'ordre des ID), nous imprimons `true` dans notre console. Il ne reste plus qu'à configurer notre outil SMS.

#### Envoyer des SMS depuis le Terminal

Cela est en fait beaucoup plus facile que cela en a l'air. Pour cela, nous utiliserons un logiciel tiers appelé [Twilio](https://www.twilio.com/). Il fait beaucoup de choses, mais l'une de ses fonctionnalités principales est d'envoyer des SMS. En bonus, il a aussi une excellente API JavaScript ! Pour terminer le tutoriel, vous aurez besoin de l'un de leurs [compte](https://www.twilio.com/try-twilio)s — un essai gratuit sera plus que suffisant pour jouer — et peut-être même obtenir un nouvel appartement.

Ok, alors pour commencer, nous devons exécuter :

```
$ yarn add twilio
```

à partir de là, dans `index.js`, ajoutons Twilio et définissons une nouvelle fonction appelée `SMS` :

```
const twilio = require(twilio);
```

```
// vous devrez obtenir vos propres identifiants pour celui-ciconst client = new Twilio("accountID", "authKey");
```

```
function SMS({ body, to, from }) {  client.messages    .create({      body,      to,      from    })    .then(() => {      console.log(`? Succès ! Le message a été envoyé à ${to}`);    })    .catch(err => {      console.log(err);    });} 
```

Cette fonction simple prend deux numéros de téléphone (`to` et `from`) et un message (`body`). Au lieu d'enregistrer dans la console le résultat de notre fonction `checkURL`, nous pouvons appeler `SMS` avec le message que nous voulons :

Et voilà ! Chaque fois que notre script voit un changement entre les hashs du site, il enverra un message texte avec l'URL directement sur votre téléphone ?.

### Bonne Chasse !

Le script réel que j'ai construit est un peu plus compliqué que l'exemple ci-dessus — je l'ai mis en tant que dépôt open source sur [GitHub](https://github.com/quinnlangille/pad-patrol).

Éventuellement, j'aimerais y apporter quelques ajouts — le premier étant de le rendre plus générique et pas seulement un scraper Kijiji. Il est assez basique, donc ce sera un excellent premier projet pour les nouveaux contributeurs.

N'hésitez pas à contribuer de la manière que vous jugez appropriée ?

Aussi, au cas où quelqu'un se poserait la question, j'ai signé un bail dimanche dernier. L'appartement que j'ai fini par louer provenait de la toute première mise à jour que pad-patrol m'a envoyée — c'était le destin F328

Je travaille actuellement en tant que développeur logiciel dans une entreprise de mode de luxe à Montréal. Je fais cela depuis environ un an, après avoir terminé un [bootcamp de développement web](https://www.decodemtl.com) l'été dernier. Je passe mon temps libre à apprendre de nouvelles technologies et, jusqu'à il y a quelques jours, à chasser des appartements.