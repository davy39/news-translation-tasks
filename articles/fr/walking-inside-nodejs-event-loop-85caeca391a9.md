---
title: Exploration de la Boucle d'Événements de Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-18T17:06:37.000Z'
originalURL: https://freecodecamp.org/news/walking-inside-nodejs-event-loop-85caeca391a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mLzCgaWN0FT9kLGtObzBeA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Exploration de la Boucle d'Événements de Node.js
seo_desc: 'By Oluwaseun Omoyajowo

  NodeJS Event loop is perhaps one of the most misunderstood concepts in node. Unfortunately
  most articles online are not helping. Until a few days ago I also had the wrong
  idea of how Event loop works thanks to Daniel Khan’s art...'
---

Par Oluwaseun Omoyajowo

La boucle d'événements de NodeJS est peut-être l'un des concepts les plus mal compris dans Node. Malheureusement, la plupart des articles en ligne n'aident pas. Jusqu'il y a quelques jours, j'avais aussi une mauvaise idée de comment la boucle d'événements fonctionne, grâce à l'article de Daniel Khan sur [article](https://medium.com/the-node-js-collection/what-you-should-know-to-really-understand-the-node-js-event-loop-and-its-metrics-c4907b19da4c). Daniel a mis en lumière certaines de ces idées fausses et a également expliqué les réalités. Je vais simplement souligner les plus populaires ci-dessous et vous pourrez consulter l'article de Daniel [article](https://medium.com/the-node-js-collection/what-you-should-know-to-really-understand-the-node-js-event-loop-and-its-metrics-c4907b19da4c) après et tout lire en entier.

« La boucle d'événements s'exécute dans un thread séparé dans le code utilisateur. Il y a un thread principal où le code JavaScript de l'utilisateur (code utilisateur) s'exécute et un autre qui exécute la boucle d'événements. Chaque fois qu'une opération asynchrone a lieu, le thread principal transmettra le travail au thread de la boucle d'événements et une fois terminé, le thread de la boucle d'événements informera le thread principal pour exécuter un rappel. » — Cela est FAUX

Cela a été mon idée de la boucle d'événements, donc j'ai décidé de faire des recherches et d'approfondir. Dans cet article, je vais expliquer comment tout se passe avec un exemple général.

Pour commencer, créez un fichier JavaScript et enregistrez-le avec le nom que vous souhaitez, le mien est 'index.js'. Tapez ou copiez et collez les codes suivants à l'intérieur du fichier.

```
const fs = require('fs');
```

```
const setTimeOutlogger = ()=>{    console.log('setTimeout logger');}const setImmediateLogger = ()=>{    console.log('setImmediate logger');}
```

```
//Pour timeout setTimeout(setTimeOutlogger, 1000);
```

```
//Opération d'E/S de fichierfs.readFile('test.txt', 'utf-8',(data)=>{    console.log('Lecture des données 1');});fs.readFile('test.txt', 'utf-8',(data)=>{    console.log('Lecture des données 2');});fs.readFile('test.txt', 'utf-8',(data)=>{    console.log('Lecture des données 3');});fs.readFile('test.txt', 'utf-8',(data)=>{    console.log('Lecture des données 4');});fs.readFile('test.txt', 'utf-8',(data)=>{    console.log('Lecture des données 5');});
```

```
//Pour setImmediatesetImmediate(setImmediateLogger);setImmediate(setImmediateLogger);setImmediate(setImmediateLogger);
```

Créez un fichier texte, 'txt' dans le même répertoire et enregistrez-le avec le nom que vous souhaitez. Le mien est 'test.txt'. À l'intérieur de ce fichier, tapez ce que vous voulez.

Avant d'exécuter le fichier JavaScript, si vous pouvez deviner l'ordre de la sortie de la console, alors *bravo à vous*. Ma sortie :

```
setImmediate logger
setImmediate logger
setImmediate logger
Lecture des données 1
Lecture des données 2
Lecture des données 3
Lecture des données 4
Lecture des données 5
setTimeout logger
```

Il est possible que la vôtre soit différente, selon la taille du fichier que vous lisez et le contenu du fichier 'txt' que vous avez créé.

Alors, que s'est-il passé dans la boucle d'événements lorsque vous avez exécuté le code ?

Lorsque Node.js démarre, il initialise la boucle d'événements, traite le script d'entrée fourni qui peut faire des appels d'API asynchrones, puis commence à traiter la boucle d'événements. Il n'y a qu'un seul thread et c'est le thread sur lequel la boucle d'événements s'exécute. La boucle d'événements fonctionne dans un ordre cyclique, avec différentes phases. L'ordre de fonctionnement de la boucle d'événements est montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/tKMV4TPOjzvtD9z9wH3lzyUWzSnNi-JRZxoe)

Il y a six phases dans la boucle d'événements, mais une fonctionne en interne. Voici un aperçu de chaque phase selon la documentation de Node.js [doc](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/).

* timers : cette phase exécute les rappels planifiés par `setTimeout()` et `setInterval()`.
* I/O callbacks : exécute presque tous les rappels à l'exception des rappels de fermeture, ceux planifiés par les timers, et `setImmediate()`.
* idle, prepare : utilisés uniquement en interne.
* poll : récupère de nouveaux événements d'E/S ; node bloquera ici lorsque cela est approprié.
* check : les rappels `setImmediate()` sont invoqués ici.close callbacks : tels que `socket.on('close')`.

### Timers

Dans notre exemple, nous avons défini `setTimeout` à 1s avant d'invoquer la fonction `timeOutLogger`. C'est la première phase (pas exactement la première, mais dans notre exemple, c'est le cas) de la boucle d'événements. Le timer définit le seuil auquel le rappel sera exécuté.

Il est important de noter que chaque phase a une file d'attente premier entré, premier sorti (FIFO) de rappels à exécuter.

### I/O callbacks

Cette phase exécute les rappels d'erreur système tels que l'erreur de connexion de socket TCP (Transmission Control Protocol) `ECONNREFUSED`. Bien que cette phase soit appelée rappel d'E/S, comprenez que les rappels d'opération d'E/S normaux sont exécutés dans la phase de poll. Je vais approfondir cela ensuite. Dans notre exemple, aucun rappel n'a été mis en file d'attente ici.

### Poll

Cette phase est celle où la plupart du travail est effectué. Selon la documentation de Node.js, la phase de poll fait essentiellement deux choses :

* Exécuter des scripts pour les timers dont le seuil a expiré
* Traiter les événements dans la file d'attente de poll

En suivant notre exemple dans cette phase, il y a actuellement une file d'attente vide puisque `fs.readFile` n'est pas terminé. En attendant, le seuil du timer `**1s**` défini précédemment n'a pas expiré. La boucle d'événements vérifie les rappels mis en file d'attente par `setImmediate()` dans la phase de check. Il y a trois rappels de notre exemple mis en file d'attente par `setImmediate()`. La boucle d'événements entre dans la phase de check.

### Check

Dans la phase de check, la boucle d'événements exécute tous les rappels dans la file d'attente, d'où l'ordre de sortie de la console dans notre exemple.

Après avoir exécuté tous les rappels dans la file d'attente de check et aucun seuil de timer n'a été atteint. Mais il y a des rappels mis en file d'attente dans la phase de poll déjà à partir de fs.readFile**. La boucle d'événements exécute tous les rappels (la boucle d'événements bloque) jusqu'à ce que le maximum soit atteint ou que la file d'attente soit à nouveau vide. Voici le problème, lors de l'exécution des rappels, il est possible que le seuil du timer expire. Et avec un nouveau rappel de timer prêt à être exécuté, le timer devra attendre que les rappels de poll s'exécutent, provoquant des retards supplémentaires. C'est l'une des raisons pour lesquelles il est conseillé de ne pas faire trop de choses à l'intérieur de vos rappels. Après avoir exécuté les rappels de la file d'attente de poll, la boucle d'événements revient immédiatement au timer pour exécuter le rappel.

**Note :** Pour empêcher la phase de poll d'épuiser la boucle d'événements, [libuv](http://libuv.org/) a également un maximum strict (dépendant du système) avant qu'il n'arrête de sonder pour plus d'événements.

### Conclusion

Bien qu'il y ait encore beaucoup de choses qui se passent derrière la scène à l'intérieur des boucles d'événements, j'espère avoir pu vous donner un aperçu de l'intérieur de la boucle d'événements de Node.js. Si vous avez des questions ou souhaitez apporter des corrections, veuillez les écrire dans la réponse. Je répondrai dès que possible ou mettra à jour l'article.

Merci d'avoir lu. Je suis Oluwaseun Omoyajowo, développeur web full-stack freelance. Restons en contact ! [Twitter](https://twitter.com/flickzcode) [LinkedIn](https://www.linkedin.com/in/oluwaseun-omoyajowo-641358110/?lipi=urn%3Ali%3Apage%3Ad_flagship3_notifications%3BESCtLB7XS8aBHaL2eaiW0g%3D%3D&licu=urn%3Ali%3Acontrol%3Ad_flagship3_notifications-nav.settings_view_profile) [Github](https://github.com/flickz) [Facebook](https://facebook.com/sheaflickz)