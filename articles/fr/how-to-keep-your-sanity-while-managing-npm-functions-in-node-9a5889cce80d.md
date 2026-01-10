---
title: Comment garder votre santé mentale tout en gérant NPM et les fonctions dans
  Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-12T22:03:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-keep-your-sanity-while-managing-npm-functions-in-node-9a5889cce80d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*h4bO2japPTG77hSqSBf12g.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: General Programming
  slug: programming
seo_title: Comment garder votre santé mentale tout en gérant NPM et les fonctions
  dans Node
seo_desc: 'By Ted Gross

  Introduction

  In my career, I have trolled through hundreds of articles dealing with NodeJS and
  many full examples of NodeJS, either in the typical MEAN stack, or specific examples
  using various NPM modules. An integral part of writing in...'
---

Par Ted Gross

### Introduction

Dans ma carrière, j'ai parcouru des centaines d'articles traitant de NodeJS et de nombreux exemples complets de NodeJS, soit dans la pile MEAN typique, soit des exemples spécifiques utilisant divers modules NPM. Une partie intégrante de l'écriture en NodeJS est l'utilisation de NPM ou Yarn pour installer des bibliothèques qui font certaines choses. Pour donner un exemple que tous les programmeurs Node connaissent, il y a les bibliothèques NPM Express-Passport-JWT-Mongo.

Nous savons tous que la pile ne s'arrêtera pas là. Express nécessitera probablement également l'installation de "body-parser" et "cors", et éventuellement des sous-modules Express NPM. N'oubliez pas Lodash, Underscore, Moment... et la liste s'allonge à l'infini, car il existe des milliers et des milliers de modules NPM à utiliser.

### Maintenir une structure de modules NPM de manière saine

Normalement, lorsque vous examinez des extraits de code ou des systèmes dans une recherche, ou que vous écrivez le vôtre, chaque fichier contiendra les modules nécessaires pour ce fichier spécifique. Les extraits de code suivants sont tirés de vrais extraits de code disponibles sur le net :

* _Veuillez noter pour ces exemples que le 'var' doit être remplacé par 'let' ou 'const' selon ce qui est fait._

```
var express = require('express');var path = require('path');var favicon = require('serve-favicon');var logger = require('morgan');var bodyParser = require('body-parser');
```

Ensuite, un autre fichier peut commencer par :

```
var morgan = require('morgan');var mongoose = require('mongoose');var passport = require('passport');
```

Et un troisième fichier peut commencer par :

```
var mongoose = require('mongoose');var Schema = mongoose.Schema;var bcrypt = require('bcrypt-nodejs');
```

Vous pouvez imaginer le reste des fichiers et il y en a généralement beaucoup, même dans les micro-services, de leur apparence.

Ce qui rend cette pratique encore pire, c'est que vous pouvez trouver 'require' au milieu d'un fichier également. En d'autres termes, le code peut continuer pendant de nombreuses lignes et soudainement le codeur introduira un autre module NPM. Cela arrive généralement avec des codeurs inexpérimentés ou non organisés, pourtant c'est une pratique incroyablement courante et cela cause des ravages dans la compréhension et le débogage du code.

Le problème, comme vous pouvez bien le voir, est cette pléthore de modules NPM, qui tôt ou tard causera un énorme mal de tête dans la maintenance d'un système, surtout au sein d'une équipe de programmeurs, qui doivent savoir ce qui a déjà été installé et est disponible et ce qui ne l'est pas.

Les programmeurs Node sont notoires pour installer, tester et jeter des modules NPM, (je reconnais en faire partie). La question, bien sûr, est de savoir comment maintenir la santé mentale, l'ordre, et surtout le contrôle sur les modules NPM installés et une méthode commune pour les appeler.

Heureusement, Node permet une méthode relativement simple pour traiter ces problèmes. Ce qui suit est une méthode que j'utilise pour les équipes back-end traitant de la pile. Elle garde les choses ordonnées, faciles à trouver, et tout le monde sait ce qui est installé et ce qui ne l'est pas dans le système. Elle permet également des désinstallations propres lorsqu'un module NPM n'est plus nécessaire.

Si vous êtes un programmeur "fonctionnel", en d'autres termes, tout ne doit pas être OOP avec des classes et "this->", ce qui suit peut vous permettre de reconsidérer une toute nouvelle méthode d'utilisation des fonctions et des procédures stockées.

Ma suggestion serait de créer un répertoire sous votre répertoire de projet racine. J'appelle généralement ce répertoire "env", mais vous pouvez l'appeler comme vous le souhaitez. "env" est l'endroit où je garde toutes mes bibliothèques de fonctions et mes procédures stockées, y compris, si utilisé, le fichier d'environnement nécessaire par la bibliothèque NPM "dotenv". (Les variables d'environnement peuvent être stockées n'importe où, elles n'ont pas besoin d'être stockées dans le répertoire racine du projet. Pourtant, une discussion sur les variables d'environnement et "dotenv" est pour un autre article.) En d'autres termes, votre répertoire "env" ne doit contenir que des fichiers qui doivent être requis ou accessibles par des parties des systèmes.

Dans le répertoire "env" hors de la racine, créez un fichier appelé "helperMods.js". (Encore une fois, vous pouvez appeler ce fichier comme vous le souhaitez.) De plus, si votre système va utiliser de nombreux modules NPM, ou ceux utilisés uniquement à des fins de développement (comme "chalk"), vous pouvez vouloir diviser cela en deux ou trois fichiers. Cependant, pour notre exemple simple, nous utiliserons un seul fichier.

```
module.exports = {    request: require("request"), //utilisé pour les requêtes http    fs: require('fs'),    path: require('path'),    chalk: require('chalk'),    moment: require('moment'),    express: require('express'),    session: require('express-session'),    eJWT: require('express-jwt'),    bodyParser: require('body-parser'),    cors: require('cors'),    passport: require('passport'),    passportLocal: require('passport-local'),    crypto: require('crypto'),    dotenv: require('dotenv'),    jwt: require('jsonwebtoken'),    jwtclaims: require('jwt-claims'),    redis: require('redis'),    mongodb: require('mongodb'),    mongoose: require('mongoose'),    assert: require('assert'),    shortid: require('shortid'),    badWords: require('bad-words'),    enum: require('enum'),    errorHandler: require('errorhandler'),    morgan: require('morgan')};
```

Tout d'abord, installez un module NPM que vous souhaitez utiliser, par exemple :

```
npm i jsonwebtoken --s
```

Maintenant, décidez d'un appelant pour ce module. Par exemple, dans le fichier ci-dessus, jsonwebtoken est d'abord défini comme "jwt". Ensuite, requérez le module réel que vous avez installé. Donc, la ligne se lira :

```
jwt: require('jsonwebtoken'),
```

(La virgule à la fin est due au format JSON du fichier.)

Les choses à savoir dans ce fichier sont les suivantes :

1. Gardez vos noms d'appel distincts.

2. Malgré ce que vous voyez ci-dessus, je les alphabétiserais selon les noms d'appel ou l'ordre alphabétique des modules NPM.

3. N'oubliez pas non plus, même s'il s'agit d'un module NodeJS intégré tel que "crypto" (oui, "crypto" fait enfin partie du NodeJS interne) ou "request", vous devez le requérir.

4. En effet, si vous requérez de nombreux modules "natifs", vous pouvez les séparer en fichiers qui peuvent tous être appelés à partir des premières lignes de chaque fichier que vous exécutez.

5. N'oubliez pas, les "espaces de noms" vous protégeront de charger un module deux fois en mémoire. Une fois que vous appelez ce module dans votre requête, même si vous l'appelez à nouveau à partir d'un autre fichier, il n'occupera pas plus de mémoire ou ne la "dupliquera".

Une fois que vous avez configuré votre fichier, la méthode d'appel à partir de n'importe quel fichier est assez facile.

Chaque fichier que vous configurez ou utilisez doit commencer par deux (ou plus) lignes selon les modules que vous devez requérir. Par exemple :

```
"use strict";const helpMods = require("./env/helperMods");
```

Les lignes ci-dessus requerront tous les modules de votre fichier. Il devient alors une méthode simple de les appeler en utilisant la notation par points.

Par exemple, si vous devez appeler le module badWords, votre notation par points ressemblera à ceci :

```
helpMods.badWords.(faites ce qui doit être fait normalement ici)
```

Si vous oubliez helpMods, un IDE comme WebStorm vous lancera une erreur vous avertissant que le module n'a pas été requis, ce qui vous indiquera immédiatement que vous avez oublié la notation par points correcte ou que vous avez oublié d'inclure ce module dans votre fichier d'exportations principal.

### Maintenir les fonctions utilisateur de manière saine

Encore une fois, en regardant de nombreux exemples, vous trouverez des fonctions dans le fichier. Souvent, ces fonctions sont un "one-off", c'est-à-dire spécifiquement utilisées pour une situation très spécifique qui ne se répétera pas. Ou le fera-t-elle ?

En années d'expérience, j'ai appris que une fois qu'une fonction fonctionne correctement, il y a de bonnes chances que vous l'utilisiez à nouveau à partir d'un autre fichier. Peut-être que les paramètres seront différents, ou vous devrez peut-être ajouter aux paramètres qu'elle reçoit (facilement fait avec un bon IDE), mais il y a de bonnes chances que vous l'utilisiez à nouveau.

Pour cette raison, je maintient un ensemble de bibliothèques de fonctions dans le répertoire "env". J'essaie généralement de diviser ces fonctions en structures logiques. Par exemple, toutes les activités CRUD et autres activités de base de données iront dans un fichier de bibliothèque de fonctions. Toutes les fonctions de sécurité iront dans un autre. Ce n'est qu'une suggestion.

Ce que ce type de programmation fait :

* Vous donne, à vous et à votre équipe, le contrôle sur l'environnement.
* Réduit les requêtes de modules spécifiques encore et encore dans chaque fichier.
* Accorde un accès immédiat aux modules NPM dont vous n'auriez peut-être pas pensé avoir besoin dans un fichier.
* Utilise la notation par points standard, sans aucun contour.
* Vous permet de diviser votre structure de la manière que vous jugez appropriée, y compris l'appel de fonctions dans des fichiers de fonctions, etc., de cette manière. Cependant, un fichier de fonction n'est pas écrit dans le même type de structure. Vous devrez requérir :

```
"use strict";const helpMods = require("./env/helperMods");
```

**Et tout autre fichier de module que vous avez décidé.**

Pour cet exemple, nous utiliserons quelques fonctions, séparées dans l'ordre pour notre système. Ensuite, écrivez et définissez toutes les fonctions, avec des rappels, des promesses ou async/await. Appelons le fichier "generalFuncs.js". Chaque fonction a cependant un nom.

```
Function(getExactTime(passed params go in here){/do stuff in here}
```

```
Function(logFile(passed params go in here){//do stuff in here}
```

Ajoutez autant de fonctions que vous le souhaitez à ce fichier. **Donc, à la fin du fichier de fonctions, vous devez écrire :**

```
module.exports = {getExactTime, logfile, HTMLResponse, getRemoteConnect, doesKeyExist, generateUniqueKey, restartAll, createDateFromString};
```

Ce qui précède permettra à ces fonctions d'être disponibles en notation par points dans tout fichier où vous ajoutez ce qui suit :

```
"use strict";const helpMods = require("./env/helperMods");const generalFuncs = require (../env/generalFuncs");
```

Maintenant, lorsque vous utilisez la fonction "getExactTime", vous y accédez comme suit :

```
generalFuncs.getExactTime(whatever is needed goes here);
```

En plus, dans tout bon IDE, vous pourrez voir quelles fonctions ne sont jamais exportées car elles ne seront jamais requises dans aucun système.

### Conclusion

Les méthodes ci-dessus vous permettront de maintenir le contrôle et la compréhension de ce qui est utilisé dans le système. Les fichiers de fonctions permettront le refactoring des fonctions tout au long du processus chaque fois que cela doit être fait. La notation par points vous permettra d'appeler les modules ou les fonctions de manière simple et ordonnée.

Cela ajoute un niveau supplémentaire dans votre structure de répertoires, ce qui peut vous rendre fou en y accédant à partir d'autres sous-répertoires, à moins que vous ne sachiez exactement comment Node gère les structures de répertoires (ce que vous devriez savoir de toute façon). **Si vous préférez ne pas faire cela, vous pouvez les laisser dans votre répertoire racine de l'application.**

Aucun de cela, d'ailleurs, n'interférera avec les versions GitHub ou les contrôles de version. En effet, la vérification, le refactoring et les tests deviendront d'autant plus faciles. Des lignes uniques peuvent être marquées uniquement pour les systèmes de développement, d'autres pour les systèmes de production.

Si vous pouvez vous habituer à ce style de codage, au moins en termes de modules et éventuellement de fonctions, vous trouverez votre code plus propre, plus facile à lire, disponible pour toute l'équipe et plus facile à refactoriser.

________________________________________________________

À propos de l'auteur : Ted Gross a servi en tant que CTO pendant de nombreuses années avec une expertise en technologie de base de données, NodeJS, MongoDB, chiffrement, PHP et OOP. Il a une expertise en technologies de mondes virtuels et en réalité augmentée. Il a également publié de nombreux articles sur des sujets technologiques, notamment sur le Big Data et la théorie du chaos (dans des revues professionnelles et en ligne @ Medium & LinkedIn). [**Il est également l'auteur de fictions littéraires, de livres pour enfants et de divers articles non fictifs**](http://amazon.com/author/tedgross). Son recueil de nouvelles, [_"Ancient Tales, Modern Legends"_](http://www.amazon.com/Ancient-Tales-Modern-Legends-Collection/dp/1469901714) a reçu d'excellentes critiques.

Ted peut être contacté par email : tedwgross@gmail.com ; [Twitter](https://twitter.com/tedwgross) (@tedwgross) ; [LinkedIn](http://il.linkedin.com/in/tedwgross) ; [Medium](https://medium.com/@tedwgross)