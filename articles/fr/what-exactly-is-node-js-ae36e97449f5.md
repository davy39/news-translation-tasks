---
title: Qu'est-ce que Node.js exactement ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T13:19:30.000Z'
originalURL: https://freecodecamp.org/news/what-exactly-is-node-js-ae36e97449f5
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cae6a740569d1a4caa649.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que Node.js exactement ?
seo_desc: 'By Priyesh Patel

  Node.js is a JavaScript runtime environment. Sounds great, but what does that mean?
  How does that work?

  The Node.js run-time environment includes everything you need to execute a program
  written in JavaScript.


  If you know Java, here...'
---

Par Priyesh Patel

Node.js est un environnement d'exécution JavaScript. Cela semble génial, mais que signifie cela ? Comment cela fonctionne-t-il ?

L'environnement d'exécution Node.js inclut tout ce dont vous avez besoin pour exécuter un programme écrit en JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/1_sYPllpcAZLHmpuQSRPuO0Q.png)
*Si vous connaissez Java, voici une petite analogie.*

Node.js est né lorsque les développeurs originaux de JavaScript l'ont étendu de quelque chose que vous ne pouviez exécuter que dans le navigateur à quelque chose que vous pouviez exécuter sur votre machine en tant qu'application autonome.

Maintenant, vous pouvez faire beaucoup plus avec JavaScript que simplement rendre les sites web interactifs.

JavaScript a maintenant la capacité de faire des choses que d'autres langages de script comme Python peuvent faire.

Votre JavaScript de navigateur et Node.js s'exécutent sur le moteur d'exécution JavaScript V8. Ce moteur prend votre code JavaScript et le convertit en un code machine plus rapide. Le code machine est un code de bas niveau que l'ordinateur peut exécuter sans avoir besoin de l'interpréter d'abord.

### Pourquoi Node.js ?

Voici une définition formelle telle que donnée sur le site officiel de Node.js [website](https://nodejs.org/en/) :

> Node.js® est un environnement d'exécution JavaScript construit sur le [moteur V8 JavaScript de Chrome](https://developers.google.com/v8/).  
>   
> Node.js utilise un modèle d'E/S piloté par événements et non bloquant qui le rend léger et efficace.  
>   
> L'écosystème de packages de Node.js, [npm](https://www.npmjs.com/), est le plus grand écosystème de bibliothèques open source au monde.

Nous avons déjà discuté de la première ligne de cette définition : « Node.js® est un environnement d'exécution JavaScript construit sur le moteur V8 JavaScript de Chrome. » Maintenant, comprenons les deux autres lignes pour découvrir pourquoi Node.js est si populaire.

I/O fait référence à l'entrée/sortie. Cela peut être n'importe quoi, allant de la lecture/écriture de fichiers locaux à la réalisation d'une requête HTTP vers une API.

L'I/O prend du temps et bloque donc d'autres fonctions.

Considérons un scénario où nous demandons à une base de données backend les détails de user1 et user2, puis les affichons à l'écran/console. La réponse à cette demande prend du temps, mais les deux demandes de données utilisateur peuvent être effectuées indépendamment et en même temps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B_UCsFOPfRDKO8ovHpxphg.png)
*I/O bloquant (à gauche) vs I/O non bloquant (à droite)*

### I/O bloquant

Dans la méthode bloquante, la demande de données de user2 n'est pas initiée tant que les données de user1 ne sont pas imprimées à l'écran.

Si cela était un serveur web, nous devrions démarrer un nouveau thread pour chaque nouvel utilisateur. Mais JavaScript est mono-threadé (pas vraiment, mais il a une boucle d'événements mono-threadée, dont nous parlerons un peu plus tard). Donc cela rendrait JavaScript peu adapté aux tâches multi-threadées.

C'est là qu'intervient la partie non bloquante.

### I/O non bloquant

D'autre part, en utilisant une requête non bloquante, vous pouvez initier une demande de données pour user2 sans attendre la réponse à la demande pour user1. Vous pouvez initier les deux demandes en parallèle.

Ce modèle d'I/O non bloquant élimine le besoin de multi-threading puisque le serveur peut gérer plusieurs requêtes en même temps.

### La boucle d'événements JavaScript

Si vous avez 26 minutes, regardez cette excellente explication vidéo de la boucle d'événements Node :

<iframe width="560" height="315" src="https://www.youtube.com/embed/8aGhZQkoFbQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Sinon, voici une explication rapide étape par étape de la façon dont la boucle d'événements JavaScript fonctionne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BBlPbUjGVtfSPd7BHa1LHw.png)
*Crédits image : Cours d'Andrew Mead [course](https://www.udemy.com/the-complete-nodejs-developer-course-2/" rel="noopener" target="_blank" title=")*

1. Poussez `main()` sur la pile d'appels.
2. Poussez `console.log()` sur la pile d'appels. Cela s'exécute immédiatement et est retiré.
3. Poussez `setTimeout(2000)` sur la pile. `setTimeout(2000)` est une API Node. Lorsque nous l'appelons, nous enregistrons la paire événement-callback. L'événement attendra 2000 millisecondes, puis le callback est la fonction.
4. Après l'avoir enregistré dans les API, `setTimeout(2000)` est retiré de la pile d'appels.
5. Maintenant, le deuxième `setTimeout(0)` est enregistré de la même manière. Nous avons maintenant deux API Node en attente d'exécution.
6. Après avoir attendu 0 secondes, `setTimeout(0)` est déplacé vers la file d'attente de callback, et la même chose se produit avec `setTimeout(2000)`.
7. Dans la file d'attente de callback, les fonctions attendent que la pile d'appels soit vide, car une seule instruction peut être exécutée à la fois. Cela est géré par la boucle d'événements.
8. Le dernier `console.log()` s'exécute, et `main()` est retiré de la pile d'appels.
9. La boucle d'événements voit que la pile d'appels est vide et que la file d'attente de callback ne l'est pas. Elle déplace donc les callbacks (dans l'ordre premier entré, premier sorti) vers la pile d'appels pour exécution.

### npm

![Image](https://cdn-media-1.freecodecamp.org/images/0*A47ZVKudfCOCBbyx.png)

Ce sont des bibliothèques construites par la communauté qui résoudreont la plupart de vos problèmes génériques. npm (Node package manager) dispose de packages que vous pouvez utiliser dans vos applications pour rendre votre développement plus rapide et efficace.

### Require

Require fait trois choses :

* Il charge les modules qui sont fournis avec Node.js comme le système de fichiers et HTTP depuis l'[API Node.js](http://nodejs.org/api/).
* Il charge les bibliothèques tierces comme Express et Mongoose que vous installez depuis npm.
* Il vous permet de charger vos propres fichiers et de modulariser le projet.

Require est une fonction, et elle accepte un paramètre « path » et retourne `module.exports`.

### Modules Node

Un module Node est un bloc de code réutilisable dont l'existence n'impacte pas accidentellement d'autres codes.

Vous pouvez écrire vos propres modules et les utiliser dans diverses applications. Node.js dispose d'un ensemble de modules intégrés que vous pouvez utiliser sans aucune installation supplémentaire.

### V8 turbo-charge JavaScript en exploitant C++

V8 est un moteur d'exécution open source écrit en C++.

JavaScript -> V8(C++) -> Code Machine

V8 implémente un script appelé ECMAScript tel que spécifié dans ECMA-262. ECMAScript a été créé par Ecma International pour standardiser JavaScript.

V8 peut s'exécuter de manière autonome ou peut être intégré dans n'importe quelle application C++. Il dispose de crochets qui vous permettent d'écrire votre propre code C++ que vous pouvez rendre disponible pour JavaScript.

Cela vous permet essentiellement d'ajouter des fonctionnalités à JavaScript en intégrant V8 dans votre code C++ afin que votre code C++ comprenne plus que ce que la norme ECMAScript spécifie autrement.

Modification : Comme cela a été porté à mon attention par [Greg Bulmash](https://www.freecodecamp.org/news/what-exactly-is-node-js-ae36e97449f5/undefined), il existe de nombreux moteurs d'exécution JavaScript différents en plus de V8 par Chrome comme SpiderMonkey par Mozilla, Chakra par Microsoft, etc. Les détails peuvent être trouvés sur [cette page](https://en.wikipedia.org/wiki/JavaScript_engine).

### Événements

Quelque chose qui s'est produit dans notre application et auquel nous pouvons répondre. Il existe deux types d'événements dans Node.

* Événements système : Noyau C++ provenant d'une bibliothèque appelée libuv. (Par exemple, lecture d'un fichier terminée).
* Événements personnalisés : Noyau JavaScript.

### Écrire Hello World en Node.js

Nous devons le faire, n'est-ce pas ?

Créez un fichier app.js et ajoutez ce qui suit :

```javascript
console.log("Hello World!");
```

Ouvrez votre terminal Node, changez le répertoire pour le dossier où le fichier est enregistré et exécutez `node app.js`.

Bam — vous venez d'écrire Hello World en Node.js.

<a href="https://twitter.com/Priyesh_p18?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-count="false">Follow @Priyesh_p18</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Il existe une tonne de ressources que vous pouvez utiliser pour en apprendre davantage sur Node.js, y compris [freeCodeCamp.org](https://www.freecodecamp.org/).