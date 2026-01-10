---
title: Qu'est-ce que le stockage local asynchrone dans Node.js v14 ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-23T22:32:05.000Z'
originalURL: https://freecodecamp.org/news/async-local-storage-nodejs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b7a740569d1a4ca2c15.jpg
tags:
- name: node js
  slug: node-js
seo_title: Qu'est-ce que le stockage local asynchrone dans Node.js v14 ?
seo_desc: "By Mehul Mohan\nNode.js 14 is out now, and with that release, it brings\
  \ in Async Local Storage support. Now you might thing, \"Meh, okay. Local storage\
  \ has been around for awhile,\" but this time, it's different. \nFor starters, this\
  \ is the Node runtime ..."
---

Par Mehul Mohan

Node.js 14 est maintenant disponible, et avec cette version, il introduit la prise en charge du stockage local asynchrone. Vous pourriez penser : "Bof, d'accord. Le stockage local existe depuis un certain temps", mais cette fois, c'est différent. 

Pour commencer, nous parlons ici du runtime Node et non du navigateur. Ainsi, avoir un concept de type "localStorage" comme dans le navigateur n'a pas vraiment de sens pour Node. Et en fait, ce n'est pas non plus le localStorage auquel vous pensez probablement. Alors, qu'est-ce que c'est ?

## Présentation du stockage local asynchrone – Stockage pour les tâches asynchrones

Prenons l'exemple d'un serveur web comme Apache exécutant PHP pour héberger un site web. Lorsque PHP reçoit une requête d'un client, votre serveur web s'assure de lancer un nouveau thread. Il permet à ce thread de gérer toutes les ressources, les variables locales, la pile d'appels de fonctions, etc., pour cette requête particulière. Simple et facile. Mais un problème se pose avec JavaScript.

JavaScript est monothread – cela signifie que vous ne pouvez pas avoir plusieurs threads de JS s'exécutant ensemble sous un même processus parent. Mais ne vous y trompez pas – JS est aussi rapide (voire plus rapide) que des solutions matures comme un backend Java pour gérer les requêtes de serveur web. 

Comment cela se produit-il ? Eh bien, c'est une question pour un autre article. Mais l'important ici est que **Node est monothread**, donc vous ne bénéficiez pas des avantages du **stockage local de thread**. Le stockage local de thread n'est rien d'autre que des variables et des fonctions locales à un thread particulier – dans notre cas, pour gérer un utilisateur particulier sur la page web.

## Pourquoi le monothread est-il un problème ?

Le monothread est un problème dans ce cas car Node continue d'exécuter le code synchrone en une seule fois tant qu'il n'a pas épuisé toutes les opérations synchrones dans la boucle d'événements. Ensuite, il vérifie les événements et les rappels et exécute ce code chaque fois que nécessaire. 

Dans Node, une simple requête HTTP n'est rien d'autre qu'un événement déclenché par la bibliothèque `http` pour que Node gère la requête – d'où son caractère asynchrone. 

Maintenant, supposons que vous souhaitiez associer certaines données à cette opération asynchrone. Comment feriez-vous cela ?

Eh bien, vous pouvez créer une sorte de variable "globale" et y assigner vos données spéciales. Ensuite, lorsqu'une autre requête provient du même utilisateur, vous pouvez utiliser la variable globale pour lire ce que vous aviez stocké précédemment. 

Mais cela échouerait spectaculairement lorsque vous avez plus d'une requête en cours, car Node n'exécuterait pas le code asynchrone en série (bien sûr, c'est la définition de l'asynchrone !). 

Considérons ce code factice (supposons le runtime Node) :

```js
server.listen(1337).on('request', (req) => {
  // une opération synchrone (sauvegarde de l'état)
  // une opération asynchrone
  // une opération asynchrone
})
```

Considérons cette séquence d'événements :

1. L'utilisateur 1 accède au serveur sur le port 1337
2. Node commence à exécuter le code de l'opération synchrone
3. Pendant que Node exécutait ce code synchrone, un autre utilisateur 2 accède au serveur.
4. Node continuerait à exécuter le code synchrone, tandis que la requête pour traiter la deuxième requête HTTP attend dans la file d'attente des tâches.
5. Lorsque Node termine l'opération synchrone et arrive à l'opération asynchrone, il la place dans la file d'attente des tâches, puis commence à traiter la première tâche dans la file d'attente – la deuxième requête HTTP.
6. Cette fois, il exécute ce morceau de code synchrone, mais au nom de la requête de l'utilisateur 2. Lorsque ce code synchrone pour l'utilisateur 2 est terminé, il reprend l'exécution asynchrone de l'utilisateur 1, et ainsi de suite.

Maintenant, que faire si vous souhaitez conserver des données spécifiques à cet utilisateur spécifique chaque fois que le code asynchrone qui lui est propre est appelé ? C'est là que vous utilisez **AsyncStorage – stockage pour les flux asynchrones dans Node.**

Considérons cet exemple directement issu de la documentation officielle :

```js
const http = require('http');
const { AsyncLocalStorage } = require('async_hooks');

const asyncLocalStorage = new AsyncLocalStorage();

function logWithId(msg) {
  const id = asyncLocalStorage.getStore();
  console.log(`${id !== undefined ? id : '-'}:`, msg);
}

let idSeq = 0;
http.createServer((req, res) => {
  asyncLocalStorage.run(idSeq++, () => {
    logWithId('start');
    // Imaginez ici une chaîne d'opérations asynchrones
    setImmediate(() => {
      logWithId('finish');
      res.end();
    });
  });
}).listen(8080);

http.get('http://localhost:8080');
http.get('http://localhost:8080');
// Affiche :
//   0: start
//   1: start
//   0: finish
//   1: finish
```

Cet exemple montre simplement la "persistance" de `idSeq` avec la requête respective. Vous pouvez imaginer comment express remplit l'objet `req.session` avec le bon utilisateur à chaque fois. De manière similaire, il s'agit d'une API de bas niveau utilisant une structure de bas niveau dans Node appelée `async_hooks`, qui est encore expérimentale, mais c'est assez cool à savoir !

## Performance

Avant de tenter de déployer cela en production, méfiez-vous – ce n'est pas quelque chose que je recommanderais vraiment à quiconque de faire si ce n'est absolument nécessaire. Cela est dû au fait que cela entraîne une baisse de performance non négligeable sur votre application. Cela est principalement dû au fait que l'API sous-jacente de `async_hooks` est encore en cours de développement, mais la situation devrait s'améliorer progressivement. 

## Conclusion

C'est à peu près tout ! Une introduction très simple et brève à ce qu'est AsyncStorage dans Node 14 et quelle est l'idée générale de haut niveau pour cela. Si vous souhaitez en savoir plus sur les nouvelles fonctionnalités de Node.js, consultez cette vidéo :

%[https://www.youtube.com/watch?v=osFz798wIaQ]

De plus, si vous êtes un adopteur précoce, essayez [codedamn](https://codedamn.com) – une plateforme pour les développeurs pour apprendre et se connecter. J'ai déployé quelques fonctionnalités sympas là-bas pour vous à essayer ! Restez à l'écoute.

Paix !