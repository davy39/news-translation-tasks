---
title: Qu'est-ce que Node.js exactement ? Un guide pour les débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-25T23:08:59.000Z'
originalURL: https://freecodecamp.org/news/what-exactly-is-node-guide-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/revised_node.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: Qu'est-ce que Node.js exactement ? Un guide pour les débutants
seo_desc: 'By Amazing Enyichi Agu

  If you''re thinking about doing back-end development using JavaScript, you will
  hear the term ‘Node.js’. Node is often associated with developing powerful web servers.

  But what exactly is Node.js? Is it a JavaScript framework ju...'
---

Par Amazing Enyichi Agu

Si vous envisagez de faire du développement back-end en utilisant JavaScript, vous entendrez le terme « Node.js ». Node est souvent associé au développement de serveurs web puissants.

Mais qu'est-ce que Node.js exactement ? Est-ce un framework JavaScript comme [Angular](https://angular.io/) ? Est-ce un langage de programmation ? Est-ce une bibliothèque JavaScript ? Est-ce un terme générique pour un groupe de technologies ? Ou est-ce simplement un autre mot pour JavaScript ?

Dans cet article, nous plongerons dans le monde de Node.js, en apprenant ce que c'est, pourquoi il a été créé et à quoi il sert. Ce n'est pas un tutoriel basé sur un projet, il vise à introduire les débutants à Node et à son fonctionnement.

Voici les sujets que nous aborderons :

1. Histoire de Node.js
2. Qu'est-ce que Node.js ?
3. Comment fonctionne Node.js ?
4. Modules dans Node.js
5. L'avenir de Node.js

Si apprendre sur les outils logiciels et leur fonctionnement est quelque chose que vous appréciez, alors vous aimerez lire cet article. Sur cette note, commençons.

## Histoire de Node.js

[Brendan Eich](https://en.wikipedia.org/wiki/Brendan_Eich), qui travaillait pour Netscape, a inventé JavaScript en 1995. Mais c'était un langage de programmation qui ne pouvait fonctionner que sur un navigateur.

Les pages web affichaient initialement uniquement des informations statiques. L'invention de JavaScript a comblé le besoin de comportements plus interactifs au sein des pages web. Avec cette invention, les développeurs pouvaient construire des pages web plus dynamiques.

Après que Brendan Eich ait inventé JavaScript, des entreprises ont tenté d'utiliser le langage pour exécuter des serveurs web également ([scripting côté serveur](https://en.wikipedia.org/wiki/Server-side_scripting)). Ces tentatives incluaient [Livewire de Netscape et Active Server Pages de Microsoft](https://dev.to/macargnelutti/server-side-javascript-a-decade-before-node-js-with-netscape-livewire-l72#the-dawn-of-serverside-javascript).

Mais cela n'est jamais devenu une méthode de développement de serveurs web, même si JavaScript continuait à gagner en popularité lorsqu'il était utilisé dans le navigateur.

En 2008, [Google](https://en.wikipedia.org/wiki/Google) a annoncé un nouveau navigateur web appelé [Chrome](https://en.wikipedia.org/wiki/Google_Chrome). Ce navigateur, une fois publié, a révolutionné le monde de la navigation sur Internet. C'est un navigateur optimisé qui exécute JavaScript rapidement et a amélioré l'expérience utilisateur sur le web.

La raison pour laquelle Google Chrome pouvait exécuter le code JavaScript si rapidement était qu'un moteur JavaScript appelé [V8](https://v8.dev) fonctionnait à l'intérieur de Chrome. Ce moteur était responsable de l'acceptation du code JavaScript, de l'optimisation du code, puis de son exécution sur l'ordinateur.

Le moteur était une solution appropriée pour le JavaScript côté client. Google Chrome est devenu le navigateur web leader.

En 2009, un ingénieur logiciel nommé Ryan Dahl a critiqué la manière populaire dont les serveurs back-end étaient exécutés à l'époque. Le logiciel le plus populaire pour construire des serveurs web était le [serveur HTTP Apache](https://httpd.apache.org/). Dahl a soutenu qu'il était limité, en ce sens qu'il ne pouvait pas gérer efficacement un grand nombre de connexions utilisateur en temps réel (10 000 +).

C'était l'une des principales raisons pour lesquelles [Ryan Dahl a développé Node.js](https://www.youtube.com/watch?v=EeYvFl7li9E), un outil qu'il a construit. Node.js utilisait le moteur V8 de Google pour comprendre et exécuter le code JavaScript en dehors du navigateur. C'était un programme dont le but était d'exécuter des serveurs web.

Node.js était une excellente alternative au serveur HTTP Apache traditionnel et a lentement gagné l'acceptation au sein de la communauté des développeurs.

Aujourd'hui, [de nombreuses grandes organisations](https://www.simform.com/blog/companies-using-nodejs/) comme Netflix, la NASA, LinkedIn, Paypal et bien d'autres utilisent Node.js. Ces entreprises exploitent les capacités de Node.js pour construire des applications robustes pour leurs utilisateurs.

De plus, dans la plus récente [enquête des développeurs StackOverflow](https://survey.stackoverflow.co/2022/) au moment de la rédaction de cet article, Node.js était classé comme la technologie la plus populaire dans la catégorie "Frameworks Web et Technologie". Cela montre à quel point Node.js est populaire maintenant.

![Frameworks Web et Technologies les plus populaires](https://www.freecodecamp.org/news/content/images/2023/05/image-105.png)
_Source : [https://survey.stackoverflow.co/2022/#technology-most-popular-technologies](https://survey.stackoverflow.co/2022/#technology-most-popular-technologies)_

Cet article examinera en profondeur ce qui rend Node.js unique et comment il fonctionne. Mais avant cela, nous devons définir exactement ce que c'est.

## Qu'est-ce que Node.js ?

![Le site officiel de Node.js](https://www.freecodecamp.org/news/content/images/2023/05/image-106.png)
_Source : [https://nodejs.org](https://nodejs.org)_

D'après le [site officiel de Node.js](https://nodejs.org), il est indiqué que :

> Node.js est un environnement d'exécution JavaScript open-source et multiplateforme.

Pour définir Node.js, nous devons décomposer la définition en parties. Les termes que nous allons définir sont :

* open-source
* multiplateforme
* Environnement d'exécution

### Que signifie open source ?

Open source est généralement utilisé pour décrire un logiciel dont le public peut examiner et modifier le code source. Cela signifie que n'importe qui peut inspecter le code qui fait fonctionner le programme de la manière dont il le fait.

Un avantage de cela est que les utilisateurs du programme peuvent le comprendre ainsi que ses capacités. De plus, si une personne repère un bug, elle peut contribuer et corriger le bug.

Vous pouvez trouver le [code source](https://github.com/nodejs/node/) de Node sur GitHub, le site web le plus populaire pour afficher le code open source. Node.js a également de nombreux contributeurs, des personnes qui ajoutent des fonctionnalités et corrigent des bugs, sur GitHub. Tout le monde a accès au code source de Node.js et peut même créer sa version personnalisée du programme s'il le souhaite.

### Que signifie multiplateforme ?

Si un programme est multiplateforme, cela signifie que le programme n'est pas limité à un seul système d'exploitation ou à une seule architecture matérielle.

Un programme multiplateforme peut fonctionner sur plusieurs plateformes. Node.js fonctionne sur Windows, Linux, Unix et MacOS, entre autres plateformes. Les développeurs peuvent utiliser Node.js sur de nombreux systèmes d'exploitation.

### Qu'est-ce qu'un environnement d'exécution ?

L'environnement d'exécution d'un langage de programmation est tout environnement où un utilisateur peut exécuter du code écrit dans ce langage. Cet environnement fournit tous les outils et ressources nécessaires à l'exécution du code. Node.js est un environnement d'exécution JavaScript.

Outre Node.js, un autre exemple d'environnement d'exécution JavaScript est un navigateur web. Un navigateur possède généralement toutes les ressources nécessaires pour exécuter du code JavaScript [côté client](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Understanding_client-side_tools).

Dans le navigateur, nous pouvons utiliser JavaScript pour interagir avec les éléments de balisage et ajuster le style. Le navigateur exécute rapidement le code, car c'est un environnement d'exécution.

D'après les trois termes définis ci-dessus, vous pouvez voir que Node.js n'est pas un framework JavaScript comme Angular. Node.js n'est pas un langage de programmation, ce n'est pas une bibliothèque JavaScript, ni un nom générique pour un groupe de technologies. Ce n'est pas non plus un autre nom pour JavaScript.

Node.js est un programme logiciel qui peut exécuter du code JavaScript. Plus précisément, Node.js est un environnement d'exécution JavaScript. C'est un environnement développé pour rendre possible l'utilisation de code JavaScript pour le scripting côté serveur.

## Comment fonctionne Node.js ?

Node.js a été écrit principalement en C/C++. En tant que programme censé exécuter des serveurs web, Node.js doit constamment interagir avec le système d'exploitation d'un appareil.

La construction de Node.js avec un langage de bas niveau comme le C a facilité l'accès du logiciel aux ressources du système d'exploitation et leur utilisation pour exécuter des instructions.

Mais il y a beaucoup plus de complexités impliquées dans le fonctionnement de Node.js. Node.js exécute des serveurs web rapides et efficaces, mais comment exactement fait-il cela ? Cette section explique le processus que Node.js utilise pour atteindre son efficacité.

Il y a trois composants principaux que nous devons comprendre pour voir comment Node.js fonctionne. Ces composants sont :

* Moteur V8
* Libuv
* Boucle d'événements

Nous allons plonger dans les détails et expliquer chacun de ces composants, et comment ils constituent Node.js.

### Qu'est-ce que le moteur V8 ?

Le moteur V8 est le moteur JavaScript qui interprète et exécute le code JavaScript dans le navigateur Chrome. Certains autres navigateurs utilisent un moteur différent, par exemple, [Firefox utilise SpiderMonkey](https://spidermonkey.dev/), et [Safari utilise JavaScriptCore](https://developer.apple.com/documentation/javascriptcore). Sans le moteur JavaScript, un ordinateur ne peut pas comprendre JavaScript.

Le moteur V8 contient un tas de mémoire et une pile d'appels. Ce sont les éléments de base du moteur V8. Ils aident à gérer l'exécution du code JavaScript.

Le tas de mémoire est le stockage de données du moteur V8. Chaque fois que nous créons une variable qui contient un objet ou une fonction en JavaScript, le moteur enregistre cette valeur dans le tas de mémoire. Pour simplifier, c'est similaire à un sac à dos qui stocke des fournitures pour un randonneur.

Chaque fois que le moteur exécute du code et rencontre l'une de ces variables, il recherche la valeur réelle dans le tas de mémoire, tout comme chaque fois qu'un randonneur a froid et veut allumer un feu, il peut chercher dans son sac à dos un briquet.

Il y a beaucoup plus de profondeur à comprendre le tas de mémoire. La gestion de la mémoire en JavaScript est un sujet qui prend plus de temps à expliquer car le processus réel est très complexe. Pour en savoir plus sur le tas de mémoire, [consultez cette ressource](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_management).

La pile d'appels est un autre élément de base du moteur V8. C'est une structure de données qui gère l'ordre des fonctions à exécuter. Chaque fois que le programme appelle une fonction, la fonction est placée sur la pile d'appels et ne peut quitter la pile que lorsque le moteur a traité cette fonction.

JavaScript est un langage à thread unique, ce qui signifie qu'il ne peut exécuter qu'une seule instruction à la fois. Puisque la pile d'appels contient l'ordre des instructions à exécuter, cela signifie que le moteur JavaScript n'a qu'un seul ordre, une seule pile d'appels. Lisez plus sur [le thread unique et la pile d'appels ici](https://www.geeksforgeeks.org/why-javascript-is-a-single-thread-language-that-can-be-non-blocking/).

![Illustration du moteur V8](https://www.freecodecamp.org/news/content/images/2023/05/v8.png)
_Illustration du moteur V8_

### Qu'est-ce que Libuv ?

Outre le moteur V8, un autre composant très important de Node.js est [Libuv](https://libuv.org/). Libuv est une bibliothèque C utilisée pour effectuer des opérations d'**entrée/sortie (I/O)**.

Les opérations d'I/O concernent l'envoi de requêtes à l'ordinateur et la réception de réponses. Ces opérations incluent la lecture et l'écriture de fichiers, la réalisation de requêtes réseau, etc.

![Le site web de Libuv](https://www.freecodecamp.org/news/content/images/2023/05/image-107.png)
_Source : [https://libuv.org](https://libuv.org)_

D'après le site officiel de Libuv, ils déclarent que :

> Libuv est une bibliothèque de support multiplateforme avec un accent sur l'I/O asynchrone.

Cela signifie que Libuv est multiplateforme (peut fonctionner sur n'importe quel système d'exploitation) et se concentre sur l'I/O asynchrone.

L'ordinateur a tendance à prendre du temps pour traiter les instructions d'I/O, mais Libuv, la bibliothèque que Node.js utilise pour interagir avec l'ordinateur, se concentre sur l'I/O asynchrone. Elle peut gérer plus d'une opération d'I/O à la fois.

C'est ce qui permet à Node.js de traiter les instructions d'I/O efficacement malgré le fait qu'il soit à thread unique. C'est tout grâce à Libuv. Libuv sait comment gérer les requêtes de manière asynchrone, minimisant ainsi les retards. Mais comment exactement le moteur JavaScript utilise-t-il Libuv ?

Chaque fois que nous passons un script à Node.js, le moteur analyse le code et commence à le traiter. La pile d'appels contient les fonctions appelées et suit le programme. Si le moteur V8 rencontre une opération d'I/O, il transmet cette opération à Libuv. Libuv exécute ensuite l'opération d'I/O.

Notez que Libuv est une bibliothèque C. Comment utilisons-nous le code JavaScript pour exécuter des instructions C ? Il existe des **liaisons** qui relient les fonctions JavaScript à leur implémentation réelle dans Libuv. Ces liaisons permettent d'utiliser le code JavaScript pour les instructions d'I/O.

Node.js utilise Libuv pour l'implémentation réelle mais expose des [interfaces de programmation d'applications (API)](https://www.freecodecamp.org/news/apis-for-beginners/). Ainsi, nous pouvons maintenant utiliser une API Node.js (qui ressemble à une fonction JavaScript) pour initier une opération d'I/O.

Une chose intéressante à noter est qu'il est vrai que JavaScript est un langage à thread unique, mais Libuv, la bibliothèque de bas niveau utilisée par Node.js, peut utiliser un pool de threads (plusieurs threads) lors de l'exécution d'instructions dans le système d'exploitation.

Maintenant, vous n'avez pas à vous soucier de ces threads lorsque vous utilisez Node.js. Libuv sait comment les gérer efficacement. Vous devez simplement utiliser les API Node.js fournies pour écrire les instructions.

![Illustration du runtime Node.js](https://www.freecodecamp.org/news/content/images/2023/05/node.js.png)
_Illustration du runtime Node.js_

Libuv a été initialement créé pour Node.js, mais différents langages de programmation ont maintenant des liaisons pour celui-ci. [Julia](https://julialang.org/) et [Luvit (environnement d'exécution basé sur Lua)](https://luvit.io/) ont les liaisons intégrées comme Node.js, mais d'autres langages ont des bibliothèques qui fournissent ces liaisons. Un exemple est [uvloop en Python](https://pypi.org/project/uvloop/), parmi [d'autres](https://github.com/libuv/libuv/blob/v1.x/LINKS.md).

### Qu'est-ce qu'une boucle d'événements ?

[La boucle d'événements dans Node.js](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick) est une partie très importante du processus. D'après le nom, nous pouvons voir qu'il s'agit d'une boucle. La boucle commence à s'exécuter lorsque Node.js commence à exécuter un programme. Dans cette section, nous examinerons ce que fait la boucle d'événements.

Lorsque nous exécutons notre programme JavaScript qui contient du code asynchrone (comme des instructions d'I/O ou des actions basées sur un minuteur), Node.js les gère en utilisant les API Node.js. Les fonctions asynchrones ont généralement des instructions à exécuter après que la fonction a terminé le traitement. Ces instructions sont placées dans une **file d'attente de rappels**.

La file d'attente de rappels fonctionne avec l'approche **Premier Entré Premier Sorti (FIFO)**. Cela signifie que la première instruction (rappel) à entrer dans la file d'attente est la première à être appelée.

Lorsque la boucle d'événements s'exécute, elle vérifie si la pile d'appels est vide. Si la pile d'appels n'est pas vide, elle permet au processus en cours de continuer. Mais si la pile d'appels est vide, elle envoie la première instruction de la file d'attente de rappels au moteur JavaScript. Le moteur place ensuite cette instruction (fonction) sur la pile d'appels et l'exécute. Cela est très similaire à [comment la boucle d'événements fonctionne dans le navigateur](https://www.freecodecamp.org/news/javascript-asynchronous-operations-in-the-browser/#event-loops).

Ainsi, la boucle d'événements exécute les rappels des instructions asynchrones en utilisant le moteur JavaScript V8 dans Node.js. Et c'est une boucle, ce qui signifie que chaque fois qu'elle s'exécute, elle vérifie la pile d'appels pour savoir si elle va retirer le rappel le plus avancé et l'envoyer au moteur JavaScript.

![Illustration complète du runtime Node.js](https://www.freecodecamp.org/news/content/images/2023/05/node.js--1-.png)
_Illustration complète du runtime Node.js_

On dit que Node.js a une architecture pilotée par les événements. Cela signifie que Node.js est construit autour de l'écoute des événements et de la réaction à ceux-ci de manière rapide lorsqu'ils se produisent. Ces événements peuvent être des événements de minuteur, des événements réseau, etc.

Node.js répond à ces événements en utilisant une boucle d'événements pour charger les rappels d'événements dans le moteur après qu'un événement a été déclenché. C'est pour cette raison que Node.js est excellent pour le transfert de données en temps réel dans les applications.

## Modules dans Node.js

Une grande partie de la fonctionnalité de Node.js est contenue dans des modules qui accompagnent le logiciel. Ces modules sont destinés à diviser les éléments de base des programmes en morceaux gérables comme des blocs Lego. Avec cela en place, nous n'avons qu'à importer les modules dont nous avons besoin pour nos programmes.

Par exemple, le morceau de code ci-dessous importe un module intégré appelé `fs`.

```javascript
const fs = require('node:fs')

```

Mais il existe d'autres façons d'utiliser des modules dans Node.js. En plus des modules intégrés, nous pouvons également utiliser des modules (ou packages) construits par d'autres développeurs.

**[Node Package Manager (NPM)](https://www.npmjs.com/)** est une application logicielle qui accompagne Node.js. Il gère tous les modules tiers disponibles dans Node.js. Chaque fois que vous avez besoin d'un package tiers, vous l'installez à partir de NPM en utilisant la commande `npm install`.

![Page d'accueil du site web de NPM](https://www.freecodecamp.org/news/content/images/2023/05/npm.jpg)
_Source : https://npmjs.com_

Pour importer un module que vous avez installé à partir de NPM, cela ressemblerait à ceci :

```javascript
const newModule = require('newModule')
```

## L'avenir de Node.js

Node.js a maintenant une grande communauté de développeurs. Il compte des milliers de [contributeurs sur GitHub](https://github.com/nodejs/node/graphs/contributors) et est utilisé par certaines des plus grandes entreprises aujourd'hui. Mais à quoi ressemble l'avenir pour Node.js ?

Node.js a bien évolué depuis sa création en 2009. Il a été initialement conçu pour le développement back-end, mais il peut faire beaucoup plus maintenant. Vous pouvez utiliser Node.js pour développer des applications de bureau, des applications web front-end, des applications mobiles et des outils en ligne de commande. Les développeurs continueront à l'utiliser pour de plus en plus de ces applications.

Ryan Dahl, l'inventeur de Node.js, a [annoncé un nouveau runtime JavaScript](https://en.wikipedia.org/wiki/Deno_(software)#History) en 2018 appelé [Deno](https://deno.com). Il a dévoilé ce runtime qu'il a co-créé lors d'une conférence intitulée « 10 choses que je regrette à propos de Node.js ».

Deno est un environnement d'exécution JavaScript basé sur le moteur V8 de Google Chrome mais écrit en Rust. Deno n'est pas seulement un environnement d'exécution pour JavaScript mais aussi pour [TypeScript](https://www.typescriptlang.org/).

Ryan Dahl a créé Deno parce qu'il a décidé qu'il avait pris certaines mauvaises décisions concernant le plan original de Node.js. Il voulait prendre de meilleures décisions architecturales pour un environnement d'exécution JavaScript pour les serveurs web. Le résultat fut Deno.

![Page d'accueil du site web de Deno](https://www.freecodecamp.org/news/content/images/2023/05/image-112.png)
_Source : [https://deno.com](https://deno.com)_

Mais Deno n'a pas encore connu une adoption massive dans la communauté des développeurs. C'est encore une technologie relativement nouvelle et a besoin de plus de temps pour gagner du terrain.

De plus, la [Fondation OpenJS](https://openjsf.org/), qui est l'organisation qui gère, développe et maintient activement Node.js, a corrigé certains des bugs et amélioré l'efficacité ultime de Node.js. Plus de projets sont construits sur l'architecture de Node.js, et cela sera probablement le cas pour l'avenir prévisible.

## Conclusion

Dans cet article, vous avez appris beaucoup de choses et pouvez maintenant répondre avec confiance à la question « Qu'est-ce que Node.js exactement ? ».

Nous avons commencé par passer en revue l'histoire de Node.js, puis nous avons correctement défini Node.js. Après cela, nous avons élaboré sur le fonctionnement de Node.js, en expliquant des composants tels que le moteur V8, Libuv et la boucle d'événements.

Après cela, nous avons parlé des modules dans Node.js et de NPM. Enfin, nous avons examiné ce que l'avenir pourrait réserver à Node.js, et nous avons conclu qu'il alimentera probablement encore plus d'applications.

Si vous souhaitez apprendre à utiliser Node.js pour construire des applications, freeCodeCamp dispose d'une [playlist de tutoriels](https://www.youtube.com/playlist?list=PLWKjhJtqVAbmGQoa3vFjeRbRADAOC9drk) entièrement dédiée à cela. Il existe une abondance de ressources pour apprendre la technologie sur Internet, et d'autres sont à venir.

Bonne chance pour la construction de votre prochaine application, et à la prochaine.

PS : Suivez-moi sur [Twitter](https://twitter.com/enyichiA) et [LinkedIn](https://linkedin.com/in/enyichiaagu).