---
title: Comment commencer à déboguer des applications NodeJS avec ndb
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-14T22:09:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-debugging-nodejs-applications-with-ndb-a37e8747dbba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vd_jfkBVYHNek4GsfTShkQ.jpeg
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment commencer à déboguer des applications NodeJS avec ndb
seo_desc: 'By Geshan Manandhar

  NodeJs was released almost 9 years ago. The default debugging process of NodeJs
  (read Node.js) is quite clumsy. You are likely already aware of the need to add
  --inspect to the node script with node inspector. It is also dependent...'
---

Par Geshan Manandhar

NodeJs a été publié il y a presque 9 ans. Le processus de débogage par défaut de NodeJs (lire Node.js) est assez maladroit. Vous êtes probablement déjà conscient de la nécessité d'ajouter `--inspect` au script node avec l'inspecteur de nœuds. Il dépend également de Chrome. Ensuite, vous devez rechercher la bonne connexion WebSocket, ce qui est difficile, et déboguer en utilisant le débogueur de nœuds de Chrome. Pour être honnête, c'est une vraie corvée.

**Enfin, Google chromelabs a publié ndb**, qu'ils décrivent comme Une expérience de débogage améliorée pour Node.js, activée par Chrome DevTools. Ndb est une bénédiction lors du débogage d'une application Nodejs.

Je vais vous montrer un processus étape par étape pour déboguer une application nodejs avec [ndb](https://github.com/GoogleChromeLabs/ndb). Ci-dessous, vous pouvez voir ndb en action. Alors maintenant, retroussons nos manches et commençons :

![Image](https://cdn-media-1.freecodecamp.org/images/poXxYHbteBuspVOlKzmD9bqdaHtmqqt7F9t6)

### Prérequis

Voici quelques prérequis avant de commencer :

1. Vous avez nodejs installé sur votre système (une évidence, mais cela vaut la peine d'être mentionné)
2. Vous avez une connaissance générale de l'exécution de scripts node et du travail avec des applications nodejs.
3. Vous avez une expérience préalable du débogage avec nodejs ou un autre langage.

Pour le débogage d'applications nodejs, au lieu d'utiliser un autre script, j'utiliserai une application express nodejs complète. Il s'agit d'une application open source que j'ai utilisée pour une démonstration sur le test d'applications nodejs.

### Débogage d'une application express nodejs en tant que démonstration

J'utilise mon API open source [currency API](https://github.com/geshan/currency-api) pour ce guide étape par étape sur le débogage d'une application nodejs. Elle est construite en utilisant le framework ExpressJS. Vous pouvez également consulter l'application en cours d'exécution hébergée sur [Zeit Now](https://currency-api-nodejs.now.sh/api/convert/USD/AUD/2019-01-01) pour voir le taux USD vers AUD du 2019-01-10 comme exemple.

L'idée de l'application est simple. Si le taux de conversion est disponible dans la base de données, il le récupérera depuis la base de données. Sinon, il le récupérera depuis une autre API et l'enverra à l'utilisateur, en enregistrant également le taux dans la base de données en même temps (asynchrone) pour une utilisation ultérieure.

Vous pouvez cloner l'application depuis github et exécuter `npm install` pour la préparer au débogage. Il s'agit d'une application très simple avec la plupart de la logique dans le fichier `exchangeRates.js` [fichier](https://github.com/geshan/currency-api/blob/master/src/exchangeRates.js). Elle dispose également de tests mocha [tests](https://github.com/geshan/currency-api/blob/master/test/exchnageRatesTest.js) car il s'agissait d'une démonstration pour tester une application nodejs.

### 1. Commencer, installer ndb

L'installation de ndb est très facile. Tout ce que vous avez à faire pour commencer à déboguer votre application nodejs est d'installer [ndb](https://github.com/GoogleChromeLabs/ndb#installation). Je vous suggère de l'installer globalement avec :

```
# avec npm
npm install -g ndb
# avec yarn 
yarn global add ndb
```

Vous pouvez également l'installer et l'utiliser localement par application si vous le souhaitez. Une chose que j'ai dû corriger était d'obtenir la dernière version de Chrome, car j'ai vu des problèmes de permissions.

### 2. Exécuter l'application avec ndb (pas node ou nodemon)

Pour déboguer des applications nodejs avec ndb, vous pouvez exécuter directement le script de l'application nodejs avec ndb plutôt qu'avec node. Par exemple, si vous aviez l'habitude de faire `node index.js` ou `nodemon index.js` en développement. Pour déboguer votre application, vous pouvez exécuter :

```
ndb index.js
```

Remarquez que vous n'avez pas besoin de mettre `--inspect`, donc l'expérience est beaucoup plus fluide.

_Vous n'avez pas besoin de vous souvenir d'un port différent ou d'aller dans les outils de développement de Chrome et d'ouvrir une fenêtre d'inspecteur différente pour déboguer. Quel soulagement !_

ndb ouvre un écran comme ci-dessous lorsque vous faites `ndb .` ou `ndb index.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/bf5fWVVRGMvWDXEc-J0xAAvyresEZ04xyw2f)

Veuillez ajouter un point d'arrêt à la ligne 46. Comme vous avez exécuté l'application avec ndb, elle s'exécutera en mode débogage et s'arrêtera au point d'arrêt comme ci-dessous lorsque vous accéderez à `http://localhost:8080/api/convert/USD/AUD/2019-01-01` dans le navigateur. J'ai défini le point d'arrêt sur exchangeRates.js à la ligne 46 dans la capture d'écran ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/AfCAHbcURVEjAF8NNTUwN0jXozpjyvv0RO5u)

ndb vous permet d'exécuter n'importe quel script pour le débogage. Par exemple, je peux exécuter `ndb npm start` et il utilisera l'exécution de nodemon. Cela signifie que je peux déboguer l'application tout en modifiant le code, ce qui est génial.

_Par exemple, il peut être exécuté avec `ndb npm start` pour déboguer cette application express nodejs._

Vous pouvez également déboguer vos tests avec une commande comme `ndb npm test`.

### 3. Déboguons du code

Comme le débogueur fonctionne, je peux placer plus de points d'arrêt ou exécuter le code à ma vitesse et à ma convenance.

_Les raccourcis essentiels sont `F10` pour passer par-dessus l'appel de fonction et `F11` pour entrer dans une fonction._

Le flux de travail de débogage habituel que je suppose que vous connaissez. Ci-dessous, j'ai avancé jusqu'à la ligne 52 :

![Image](https://cdn-media-1.freecodecamp.org/images/wMByQMEy-UYehLe-SxXz-nGM9sDw5zwg-Srd)

### Plus de choses sur le débogage

Comme avec tout autre débogueur, avec ndb vous pouvez :

1. Ajouter des montres
2. Vérifier la trace de la pile d'appels
3. Vérifier le processus

_L'onglet console est également utile si vous voulez exécuter rapidement du code nodejs dans le contexte._

Lisez plus sur ce que vous pouvez faire avec ndb dans le [readme](https://github.com/GoogleChromeLabs/ndb#what-can-i-do) officiel. Ci-dessous, une capture d'écran de la console utile :

![Image](https://cdn-media-1.freecodecamp.org/images/gICkxIsuYHbODz87IhtR979LkdhnHdh05R-z)

### Conclusion (TL;DR)

Déboguer une application nodejs avec ndb est une meilleure expérience pour les développeurs. Pour déboguer l'application express nodejs de l'API de devise avec ndb, vous exécutez les commandes suivantes, à condition d'avoir node > 8 installé :

1. npm install -g ndb
2. git clone [[email protected]](https://geshan.com.np/cdn-cgi/l/email-protection):geshan/currency-api.git
3. cd currency-api
4. npm install
5. ndb npm start
6. Après l'ouverture du débogueur ndb, ajoutez un point d'arrêt à la ligne 46 de src/exchangeRates.js
7. Ensuite, ouvrez `http://localhost:8080/api/convert/USD/AUD/2019-01-01` dans le navigateur
8. Maintenant, comme l'application devrait s'arrêter au point d'arrêt, profitez-en et continuez le débogage.

Si cela fonctionne pour cette application, vous pouvez déboguer n'importe quelle application nodejs avec cette approche.

_Bienvenue dans la nouvelle façon de déboguer les applications nodejs qui est indépendante du navigateur et beaucoup plus fluide que l'expérience par défaut. Améliorez votre jeu de débogage d'applications nodejs._

J'espère que cet article vous a aidé à mieux déboguer votre application nodejs. Si vous avez d'autres choses à partager sur le débogage des applications nodejs ou une meilleure utilisation de ndb, veuillez commenter ci-dessous !

Merci d'avoir lu !

Vous pouvez lire plus de mes articles de blog sur [geshan.com.np](https://geshan.com.np/blog/2019/01/getting-started-with-debugging-nodejs-applications-with-ndb/).