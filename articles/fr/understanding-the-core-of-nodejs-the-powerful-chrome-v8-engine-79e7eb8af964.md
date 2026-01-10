---
title: Comprendre comment le moteur V8 de Chrome traduit le JavaScript en code machine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T05:12:25.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-core-of-nodejs-the-powerful-chrome-v8-engine-79e7eb8af964
coverImage: https://cdn-media-1.freecodecamp.org/images/1*T2RkznzWBPFp3JM3L7zx5A.png
tags:
- name: Chromev8
  slug: chromev8
- name: ecmascript
  slug: ecmascript
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: Comprendre comment le moteur V8 de Chrome traduit le JavaScript en code
  machine
seo_desc: 'By Mayank Tripathi

  Before diving deep into the core of Chrome’s V8, first, let’s get our fundamentals
  down. All of our systems consist of microprocessors, the thing that is sitting inside
  your computer right now and allowing you to read this.

  Micropr...'
---

Par Mayank Tripathi

Avant de plonger au cœur du V8 de Chrome, commençons par les bases. Tous nos systèmes sont composés de microprocesseurs, l'élément qui se trouve actuellement dans votre ordinateur et qui vous permet de lire ceci.

Les microprocesseurs sont de minuscules machines qui fonctionnent avec des signaux électriques et qui, en fin de compte, font le travail. Nous donnons des instructions aux microprocesseurs. Ces instructions sont dans le langage que les microprocesseurs peuvent interpréter. Différents microprocesseurs parlent différents langages. Certains des plus courants sont IA-32, x86–64, MIPS et ARM. Ces langages interagissent directement avec le matériel, donc le code écrit dans ces langages est appelé code machine. Le code que nous écrivons sur nos ordinateurs est converti ou compilé en code machine.

Voici à quoi ressemble le code machine :

![Image](https://cdn-media-1.freecodecamp.org/images/1*T2RkznzWBPFp3JM3L7zx5A.png)
_Source : Google_

Il se compose d'instructions qui sont exécutées à un emplacement particulier de la mémoire de votre système à un bas niveau. Vous devez vous estimer heureux de ne pas avoir à écrire tout cela pour exécuter votre programme !

Les langages de haut niveau sont abstraits du langage machine. Dans le niveau d'abstraction ci-dessous, vous pouvez voir à quel point le JavaScript est éloigné du niveau machine. Le C/C++ est relativement beaucoup plus proche du matériel et donc beaucoup plus rapide que les autres langages de haut niveau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hmr87--VeQ_GyZesKYtEeg.png)

Revenons maintenant au moteur V8 : V8 est un puissant moteur Javascript open source fourni par Google. Alors, qu'est-ce qu'un moteur Javascript exactement ? C'est un programme qui convertit le code Javascript en code de bas niveau ou en code machine que les microprocesseurs peuvent comprendre.

Il existe différents moteurs JavaScript, notamment [Rhino](https://en.wikipedia.org/wiki/Rhino_(JavaScript_engine)), [JavaScriptCore](https://en.wikipedia.org/wiki/WebKit#JavaScriptCore) et [SpiderMonkey](https://en.wikipedia.org/wiki/SpiderMonkey_(JavaScript_engine)). Ces moteurs respectent les standards ECMAScript. ECMAScript définit le standard pour le langage de script. JavaScript est basé sur les standards ECMAScript. Ces standards définissent comment le langage doit fonctionner et quelles fonctionnalités il doit avoir. Vous pouvez en apprendre plus sur ECMAScript [ici](https://www.ecma-international.org/publications/standards/Ecma-262.htm).

![Image](https://cdn-media-1.freecodecamp.org/images/1*gZq22sBm1y3eq1NfhEaXeg.png)
_Source : Google_

Le moteur V8 de Chrome :

* Le moteur V8 est écrit en C++ et utilisé dans Chrome et Nodejs.
* Il implémente ECMAScript tel que spécifié dans ECMA-262.
* Le moteur V8 peut fonctionner de manière autonome ; nous pouvons l'intégrer à notre propre programme C++.

Comprenons un peu mieux ce dernier point. V8 peut fonctionner de manière autonome et, en même temps, nous pouvons ajouter notre propre implémentation de fonction en C++ pour ajouter de nouvelles fonctionnalités à JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PA3QZ_7EWgoDGNyJID_7MA.png)

Par exemple : `print('hello world')` n'est pas une instruction valide dans Node.js. Elle donnera une erreur si nous la compilons. Mais nous pouvons ajouter notre propre implémentation de la fonction print en C++ par-dessus V8 qui est open source sur [Github](https://github.com/v8/v8), rendant ainsi la fonction print opérationnelle nativement. Cela permet au JavaScript de comprendre plus que ce que le standard ECMAScript spécifie.

C'est une fonctionnalité puissante car le C++ possède plus de fonctionnalités en tant que langage de programmation par rapport au JavaScript, car il est beaucoup plus proche du matériel, comme pour la gestion des fichiers et des dossiers sur le disque dur.

Le fait de pouvoir écrire du code en C++ et de le rendre disponible pour JavaScript nous permet d'ajouter plus de fonctionnalités à JavaScript.

Node.js en soi est une implémentation C++ d'un moteur V8 permettant la programmation côté serveur et les applications réseau.

Jetons maintenant un coup d'œil à une partie du code open source à l'intérieur du moteur. Pour ce faire, vous devez vous rendre dans le dossier [v8/samples/shell.cc](https://github.com/v8/v8/blob/master/samples/shell.cc).

Ici, vous pouvez voir l'implémentation de différentes fonctions telles que `Print` et `Read`, qui ne sont pas nativement disponibles dans Node.js.

Ci-dessous, vous pouvez voir l'implémentation de la fonction `Print`. Chaque fois que la fonction `print()` est invoquée dans Node.js, elle créera un rappel (callback) et la fonction sera exécutée.

De même, nous pouvons ajouter notre propre implémentation de différentes nouvelles fonctions en C++ à l'intérieur de V8, permettant à Node.js de les comprendre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GtV0dm8WOU4l43oK58SHqg.png)

C'est certainement beaucoup à assimiler pour une simple instruction, et c'est la quantité de travail que le moteur V8 effectue sous le capot.

Vous devriez maintenant avoir une compréhension claire du fonctionnement de Node.js et de ce qu'est réellement le moteur V8 de Chrome.

Merci d'avoir lu cet article. Suivons-nous sur [**Twitter**](https://twitter.com/mayank_408), [**Linkedin**](https://www.linkedin.com/in/mayank-tripathi-a49563126/), [**Github**](https://github.com/mayank408)**,** et [**Facebook**](https://www.facebook.com/profile.php?id=100001106266064).