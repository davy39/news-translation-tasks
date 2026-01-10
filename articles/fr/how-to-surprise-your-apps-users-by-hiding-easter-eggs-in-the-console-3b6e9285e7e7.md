---
title: Comment surprendre les utilisateurs de votre application en cachant des Easter
  eggs dans la console
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T00:23:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-surprise-your-apps-users-by-hiding-easter-eggs-in-the-console-3b6e9285e7e7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0B1CuHTa6jjPvRZLDBtUBw.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Comment surprendre les utilisateurs de votre application en cachant des
  Easter eggs dans la console
seo_desc: 'By Ethan Ryan

  I love console.logging(“stuff”).

  I do it throughout my apps, for debugging purposes and feature building purposes,
  and just for the sheer hell of it. It’s fun to log stuff to the console.

  I even use console.warn() and console.error(), a...'
---

Par Ethan Ryan

J'adore console.logging("stuff").

Je le fais partout dans mes applications, à des fins de débogage et de construction de fonctionnalités, et juste pour le plaisir.

J'utilise même `console.warn()` et `console.error()`, et `console.table()` si je me sens audacieux.

J'aime toutes les jolies couleurs qu'ils font dans ma console, et parfois vous voulez que certains messages se distinguent plus que d'autres.

Mais j'ai réalisé en regardant [mon application de générateur d'histoires WordNerds](https://wordnerds.co/) hier que je faisais des logs dans la console en mode production.

Oh-oh spaghetti-ohs.

C'est un non-non. Cela pourrait ralentir le code inutilement, et surtout, cela pourrait compromettre les adresses e-mail de mes utilisateurs ! Je faisais des logs de tous les noms d'utilisateur et adresses e-mail de mes utilisateurs. Pas cool ! Leurs mots de passe sont cryptés bien sûr, mais quand même, ce n'est pas bien. Je ne voudrais pas que des méchants obtiennent un tas d'adresses e-mail de mes utilisateurs et leur envoient des crapolas.

### Supprimer les logs de la console en mode production

Le corriger s'est avéré facile. Bien sûr, j'aurais pu parcourir la base de code et commenter tous mes console.logs(), mais cela aurait été fastidieux, et certains d'entre eux servent des objectifs importants en mode développement.

Heureusement, il existe une méthode plus facile et meilleure.

J'ai d'abord consulté [certaines des solutions](https://stackoverflow.com/questions/8002116/should-i-be-removing-console-log-from-production-code) à ce problème [listées sur StackFlow](https://stackoverflow.com/questions/7500811/how-do-i-disable-console-log-when-i-am-not-debugging), puis j'ai finalement opté pour la première solution listée sur [cet article de blog](https://www.codebyamir.com/blog/suppressing-console-log-messages-in-production).

![Image](https://cdn-media-1.freecodecamp.org/images/jc4ODxkMp1KtvfhpstgQLe-aVYqusFrOAuK8)
_Solution via [www.codebyamir.com](http://www.codebyamir.com" rel="noopener" target="_blank" title=")_

Comme l'ont mentionné certains des commentaires lorsqu'une personne a listé cela comme une solution au problème : "C'est un hack. Vous gaspillez du calcul en production"

![Image](https://cdn-media-1.freecodecamp.org/images/-s1srDkkrRoKPbhbzIx-WFfUHZrAf-Q60tE0)
_"C'est un hack."_

Bon débat ! Je n'étais pas trop inquiet d'appeler une fonction vide plusieurs fois et de gaspiller du calcul en production, alors j'ai opté pour cette solution, car elle est facile à mettre en œuvre et résout mon problème.

Voici comment je l'ai fait, dans le fichier src/index.js :

![Image](https://cdn-media-1.freecodecamp.org/images/DSciz3L5MRihw5jjT7o7rCeWNMz9kQI-mjGf)
_src/index.js file_

Bien sûr, je pourrais le faire dans n'importe quel fichier, comme le composant App, ou mon composant StoryContainer. N'importe où tant que c'était avant que des logs, des avertissements ou des erreurs de console ne soient rendus. Mais il m'a semblé logique de le faire à la racine.

Je l'ai testé en développement en remplaçant 'production' par 'development', et ça a marché ! Plus de messages dans la console.

#### Ajouter des messages dans la console

Mais ensuite, je me suis senti triste :(

Plus de messages dans la console ? Cela semblait si sparse.

Autant avoir QUELQUES messages pour ces curieux, intrépides nerds de mots assez audacieux pour ouvrir la console.

J'en ai donc ajouté un, comme un [Easter egg](https://en.wikipedia.org/wiki/Easter_egg_(media)) caché :

![Image](https://cdn-media-1.freecodecamp.org/images/acJJhS1TezClILOJ2V4Uzb0okV6it-dXBUcw)
_hello everybody!_

Comment ai-je fait cela ? Facile : puisque toutes les appels de mon application à `console.log()`, `console.warn()`, et `console.error()` étaient écrasés par des fonctions vides, j'ai simplement ajouté un `console.info()` ! C'est pratiquement la même chose qu'un `console.log()`. Certaines des différences sont listées, et disputées, [ici](https://stackoverflow.com/questions/25532778/node-js-console-log-vs-console-info).

`hello everybody!` était un peu ennuyeux. J'avais déjà le nom de l'utilisateur connecté de mon application stocké dans l'état, alors pourquoi ne pas personnaliser mon message ?

Et si je personnalise mon message, pourquoi ne pas personnaliser un tas de messages, et en retourner un aléatoirement chaque fois qu'un utilisateur connecté inspecte la console ? Tout le monde aime trouver des Easter eggs !

C'est ce que j'ai décidé de faire, et voici comment je l'ai fait :

![Image](https://cdn-media-1.freecodecamp.org/images/H5wxFxT9YHiehoaeFUKSOIL70eiW-gbACi3e)
_Composant de salutation_

Je rends mon composant Greeting dans mon StoryContainer, de sorte que chaque fois qu'un utilisateur connecté choisit de vérifier la console, il verra l'un de ces messages amicaux !

```js
function getFriendlyMessage(nameString) {
  let messages = [
    `Bonjour ${nameString}, c'est bon de te voir !`,
    `salut ${nameString}`,
    `bonjour ${nameString}, tu as l'air génial aujourd'hui !`,
    `bonjour ${nameString}, toi l'être humain spectaculaire !`,
    `tu as l'air génial aujourd'hui ${nameString} !`,
    `hellllooooooo ${nameString} !`,
    `Hey ${nameString}, comment ça va ?`,
    `Peux-tu garder un secret, ${nameString} ? Tu es mon préféré !`,
    `Rien à voir ici, ${nameString}.`,
    `Félicitations, ${nameString} ! Tu as découvert la console ;)`,
    `je t'ai dit récemment que je t'aime, ${nameString} ?`,
    `je savais que tu trouverais cet Easter egg éventuellement, ${nameString}...`,
  ]
  var randomMessage = messages[Math.floor(Math.random() * messages.length)];
  return randomMessage
}
```

Coder, c'est amusant.

Merci de votre lecture, nerds de mots !