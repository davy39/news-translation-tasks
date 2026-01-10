---
title: 'Node.js : qu''est-ce que c''est, quand et comment l''utiliser, et pourquoi
  vous devriez le faire'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T22:34:04.000Z'
originalURL: https://freecodecamp.org/news/node-js-what-when-where-why-how-ab8424886e2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DF0g7bNW5e2z9XS9N2lAiw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Node.js : qu''est-ce que c''est, quand et comment l''utiliser, et pourquoi
  vous devriez le faire'
seo_desc: 'By Pablo Regen

  You’ve probably read these sentences before…


  Node.js is a JavaScript runtime built on Chrome’s V8 JavaScript engine

  Node.js uses an event-driven, asynchronous non-blocking I/O model

  Node.js operates on a single thread event loop


  … an...'
---

Par Pablo Regen

Vous avez probablement déjà lu ces phrases...

> Node.js est un environnement d'exécution JavaScript basé sur le moteur V8 JavaScript de Chrome

> Node.js utilise un modèle d'E/S asynchrone, non bloquant et piloté par événements

> Node.js fonctionne sur une boucle d'événements à thread unique

... et vous êtes resté perplexe quant à la signification de tout cela. Espérons qu'à la fin de cet article, vous aurez une meilleure compréhension de ces termes ainsi que de ce qu'est Node, comment il fonctionne, et pourquoi et quand il est une bonne idée de l'utiliser.

Commençons par passer en revue la terminologie.

#### E/S (entrée/sortie)

Abréviation de entrée/sortie, **E/S** fait principalement référence à l'interaction du programme avec le disque et le réseau du système. Les exemples d'opérations d'E/S incluent la lecture/écriture de données depuis/vers un disque, l'envoi de requêtes HTTP et la communication avec des bases de données. Elles sont très lentes par rapport à l'accès à la mémoire (RAM) ou au travail effectué sur le CPU.

#### **Synchrone vs Asynchrone**

L'exécution [**synchrone**](https://stackoverflow.com/questions/10570246/what-is-non-blocking-or-asynchronous-i-o-in-node-js) (ou sync) fait généralement référence à un code exécuté en séquence. En programmation synchrone, le programme est exécuté ligne par ligne, une ligne à la fois. Chaque fois qu'une fonction est appelée, l'exécution du programme attend que cette fonction retourne avant de continuer à la ligne de code suivante.

L'exécution **asynchrone** (ou async) fait référence à une exécution qui ne s'effectue pas dans la séquence dans laquelle elle apparaît dans le code. En programmation asynchrone, le programme n'attend pas que la tâche soit terminée et peut passer à la tâche suivante.

Dans l'exemple suivant, l'opération synchrone provoque le déclenchement des alertes en séquence. Dans l'opération asynchrone, bien que alert(2) semble s'exécuter en second, ce n'est pas le cas.

```js
// Synchrone : 1,2,3
alert(1);
alert(2);
alert(3);

// Asynchrone : 1,3,2
alert(1);
setTimeout(() => alert(2), 0);
alert(3);
```

Une opération asynchrone est souvent liée aux E/S, bien que `setTimeout` soit un exemple de quelque chose qui n'est pas une E/S mais reste asynchrone. En général, tout ce qui est lié au calcul est synchrone et tout ce qui est lié à l'entrée/sortie/temporisation est asynchrone. La raison pour laquelle les opérations d'E/S sont effectuées de manière asynchrone est qu'elles sont très lentes et bloqueraient sinon l'exécution ultérieure du code.

#### **Bloquant vs Non-bloquant**

**Bloquant** fait référence à des opérations qui bloquent l'exécution ultérieure jusqu'à ce que cette opération se termine, tandis que **non-bloquant** fait référence à un code qui n'empêche pas l'exécution. Ou comme le dit la documentation de [Node.js](https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/#blocking), le blocage se produit lorsque l'exécution de JavaScript supplémentaire dans le processus Node.js doit attendre qu'une opération non-JavaScript se termine.

Les méthodes bloquantes s'exécutent de manière synchrone tandis que les méthodes non-bloquantes s'exécutent de manière asynchrone.

```js
// Bloquant
const fs = require('fs');
const data = fs.readFileSync('/file.md'); // bloque ici jusqu'à ce que le fichier soit lu
console.log(data);
moreWork(); // s'exécutera après console.log

// Non-bloquant
const fs = require('fs');
fs.readFile('/file.md', (err, data) => {
  if (err) throw err;
  console.log(data);
});
moreWork(); // s'exécutera avant console.log
```

Dans le premier exemple ci-dessus, `console.log` sera appelé avant `moreWork()`. Dans le deuxième exemple, `fs.readFile()` est non-bloquant, donc l'exécution de JavaScript peut continuer et `moreWork()` sera appelé en premier.

Dans Node, non-bloquant fait principalement référence aux opérations d'E/S, et le JavaScript qui présente de mauvaises performances en raison d'une intensité CPU plutôt que d'attendre une opération non-JavaScript, telle que les E/S, n'est généralement pas considéré comme bloquant.

Toutes les méthodes d'E/S de la bibliothèque standard de Node.js fournissent des versions asynchrones, qui sont non-bloquantes, et acceptent des fonctions de rappel. Certaines méthodes ont également des homologues bloquants, dont les noms se terminent par Sync.

Les opérations d'E/S non-bloquantes permettent à un seul processus de servir plusieurs requêtes simultanément. Au lieu que le processus soit bloqué et attende la fin des opérations d'E/S, les opérations d'E/S sont déléguées au système, de sorte que le processus peut exécuter le prochain morceau de code. Les opérations d'E/S non-bloquantes fournissent une fonction de rappel qui est appelée lorsque l'opération est terminée.

#### **Fonctions de rappel (Callbacks)**

Un **callback** est une fonction passée en argument à une autre fonction, qui peut ensuite être invoquée (rappelée) à l'intérieur de la fonction externe pour accomplir une sorte d'action à un moment opportun. L'invocation peut être immédiate (callback synchrone) ou elle peut se produire plus tard (callback asynchrone).

```js
// Callback synchrone
function greetings(callback) {
  callback();
}
greetings(() => { console.log('Bonjour'); });
moreWork(); // s'exécutera après console.log

// Callback asynchrone
const fs = require('fs');
fs.readFile('/file.md', function callback(err, data) { // fs.readFile est une méthode asynchrone fournie par Node
  if (err) throw err;
  console.log(data);
});
moreWork(); // s'exécutera avant console.log
```

Dans le premier exemple, la fonction de rappel est appelée immédiatement à l'intérieur de la fonction externe greetings et enregistre dans la console avant que `moreWork()` ne se poursuive.

Dans le deuxième exemple, fs.readFile (une méthode asynchrone fournie par Node) lit le fichier et, lorsqu'il a terminé, appelle la fonction de rappel avec une erreur ou le contenu du fichier. Pendant ce temps, le programme peut continuer l'exécution du code.

Un callback asynchrone peut être appelé lorsqu'un événement se produit ou lorsqu'une tâche est terminée. Il empêche le blocage en permettant à d'autres codes d'être exécutés en attendant.

[Au lieu](https://github.com/maxogden/art-of-node#callbacks) que le code soit lu de haut en bas de manière procédurale, les programmes asynchrones peuvent exécuter différentes fonctions à différents moments en fonction de l'ordre et de la vitesse auxquels des fonctions précédentes comme les requêtes http ou les lectures du système de fichiers se produisent. Ils sont utilisés lorsque vous ne savez pas quand une opération asynchrone sera terminée.

Vous devriez éviter le [**callback hell**](http://callbackhell.com/), une situation où les callbacks sont imbriqués dans d'autres callbacks à plusieurs niveaux de profondeur, rendant le code difficile à comprendre, maintenir et déboguer.

#### Événements et programmation pilotée par événements

Les **événements** sont des actions générées par l'utilisateur ou le système, comme un clic, un téléchargement de fichier terminé, ou une erreur matérielle ou logicielle.

La **programmation pilotée par événements** est un paradigme de programmation dans lequel le flux du programme est déterminé par des événements. Un programme piloté par événements effectue des actions en réponse à des événements. Lorsqu'un événement se produit, il déclenche une fonction de rappel.

Maintenant, essayons de comprendre Node et voyons comment tout cela se rapporte à lui.

### **Node.js : qu'est-ce que c'est, pourquoi a-t-il été créé et comment fonctionne-t-il ?**

Simplement dit, **Node.js** est une plateforme qui exécute des programmes JavaScript côté serveur qui peuvent communiquer avec des sources d'E/S comme les réseaux et les systèmes de fichiers.

Lorsque [Ryan Dahl](https://www.youtube.com/watch?v=ztspvPYybIY) a créé Node en 2009, il a soutenu que les E/S étaient mal gérées, bloquant l'ensemble du processus en raison de la programmation synchrone.

Les techniques traditionnelles de service web utilisent le modèle de thread, ce qui signifie un thread par requête. Puisque dans une opération d'E/S, la requête passe la plupart du temps à attendre sa complétion, les scénarios d'E/S intensifs entraînent une grande quantité de ressources inutilisées (comme la mémoire) liées à ces threads. Par conséquent, le modèle un thread par requête pour un serveur ne s'adapte pas bien.

Dahl a soutenu que les logiciels devraient être capables de multitâche et a proposé d'éliminer le temps passé à attendre les résultats des E/S. Au lieu du modèle de thread, il a dit que la bonne façon de gérer plusieurs connexions simultanées était d'avoir un thread unique, une boucle d'événements et des E/S non bloquantes. Par exemple, lorsque vous faites une requête à une base de données, au lieu d'attendre la réponse, vous lui donnez un callback afin que votre exécution puisse passer par cette instruction et continuer à faire d'autres choses. Lorsque les résultats reviennent, vous pouvez exécuter le callback.

La [**boucle d'événements**](https://nodejs.org/de/docs/guides/event-loop-timers-and-nexttick/#what-is-the-event-loop) est ce qui permet à Node.js d'effectuer des opérations d'E/S non bloquantes malgré le fait que JavaScript soit mono-thread. La boucle, qui s'exécute sur le même thread que le code JavaScript, prend une tâche du code et l'exécute. Si la tâche est asynchrone ou une opération d'E/S, la boucle la délègue au noyau du système, comme dans le cas des nouvelles connexions au serveur, ou à un pool de threads, comme les opérations liées au système de fichiers. La boucle prend ensuite la tâche suivante et l'exécute.

Puisque la plupart des noyaux modernes sont multi-threads, ils peuvent gérer plusieurs opérations s'exécutant en arrière-plan. Lorsque l'une de ces opérations est terminée (c'est un événement), le noyau informe Node.js afin que le callback approprié (celui qui dépendait de la fin de l'opération) puisse être ajouté à la file d'attente de sondage pour être éventuellement exécuté.

Node suit les opérations asynchrones non terminées, et la boucle d'événements continue de vérifier si elles sont terminées jusqu'à ce que toutes le soient.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vRcV8wd7PQZo7MxKIHdZHg.jpeg)
_La bibliothèque Unicorn Velociraptor fournit un support pour les E/S asynchrones basées sur des boucles d'événements_

Pour accommoder la boucle d'événements à thread unique, Node.js utilise la bibliothèque [**libuv**](https://libuv.org/), qui, à son tour, utilise un **pool de threads** de taille fixe qui gère l'exécution de certaines des opérations d'E/S asynchrones non bloquantes en parallèle. Le thread principal appelle des fonctions qui postent des tâches à la file d'attente de tâches partagée, que les threads du pool de threads tirent et exécutent.

Les fonctions système intrinsèquement non bloquantes telles que le réseau se traduisent par des sockets non bloquants côté noyau, tandis que les fonctions système intrinsèquement bloquantes telles que les E/S de fichiers s'exécutent de manière bloquante sur leurs propres threads. Lorsqu'un thread du pool de threads termine une tâche, il informe le thread principal, qui à son tour, se réveille et exécute le callback enregistré.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pIEFRBvMqxpDipMnqkVprA.jpeg)
_Image de la présentation de Philip Roberts à JSConf EU : [What the heck is the event loop anyway?](https://www.youtube.com/watch?v=8aGhZQkoFbQ" rel="noopener" target="_blank" title=")_

L'image ci-dessus est tirée de la présentation de Philip Roberts à JSConf EU : [What the heck is the event loop anyway?](https://www.youtube.com/watch?v=8aGhZQkoFbQ). Je recommande de regarder la vidéo complète pour avoir une idée générale de la façon dont la boucle d'événements fonctionne.

Le diagramme explique comment la boucle d'événements fonctionne avec le navigateur, mais elle est pratiquement identique pour Node. Au lieu des API web, nous aurions des API Node.

Selon la présentation, la pile d'appels (aka pile d'exécution ou la pile) est une structure de données qui enregistre où nous en sommes dans le programme. Si nous entrons dans une fonction, nous mettons quelque chose sur la pile. Si nous revenons d'une fonction, nous le retirons du sommet de la pile.

Voici comment le code du diagramme est traité lorsque nous l'exécutons :

1. Pousser `main()` sur la pile (le fichier lui-même)
2. Pousser `console.log('Bonjour');` sur la pile, qui s'exécute immédiatement en enregistrant Bonjour dans la console et est retiré de la pile
3. Pousser `setTimeout(cb, 5000)` sur la pile. setTimeout est une API fournie par le navigateur (sur le backend, ce serait une API Node). Lorsque setTimeout est appelé avec la fonction de rappel et les arguments de délai, le navigateur lance un minuteur avec le temps de délai
4. L'appel `setTimeout` est terminé et est retiré de la pile
5. Pousser `console.log('JSConfEU');` sur la pile, qui s'exécute immédiatement en enregistrant JSConfEU dans la console et est retiré de la pile
6. `main()` est retiré de la pile
7. Après 5000 millisecondes, le minuteur de l'API est terminé et le callback est déplacé vers la file d'attente des tâches
8. La boucle d'événements vérifie si la pile est vide car JavaScript, étant mono-thread, ne peut faire qu'une seule chose à la fois (setTimeout n'est pas un temps garanti mais un temps minimum pour l'exécution). Si la pile est vide, elle prend la première chose dans la file d'attente et la pousse sur la pile. Par conséquent, la boucle pousse le callback sur la pile
9. Le callback est exécuté, enregistre là dans la console et est retiré de la pile. Et nous avons terminé

Si vous voulez approfondir les détails sur le fonctionnement de Node.js, libuv, la boucle d'événements et le pool de threads, je vous suggère de consulter les ressources de la section de référence à la fin, en particulier [celle-ci](https://www.youtube.com/watch?v=cCOL7MC4Pl0), [celle-ci](https://www.youtube.com/watch?v=PNa9OMajw9w) et [celle-ci](https://www.youtube.com/watch?v=sGTRmPiXD4Y) ainsi que la [documentation Node](https://nodejs.org/de/docs/guides/event-loop-timers-and-nexttick/#what-is-the-event-loop).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GYkdiL25aLDgkSW0phpAag.jpeg)
_La boucle d'événements. Image de la présentation de Bert Belder : [Everything You Need to Know About Node.js Event Loop](https://www.youtube.com/watch?v=PNa9OMajw9w" rel="noopener" target="_blank" title=")_

### Node.js : **pourquoi et où l'utiliser ?**

Puisque presque aucune fonction dans Node n'effectue directement des E/S, le processus ne bloque jamais (les opérations d'E/S sont déléguées et exécutées de manière asynchrone dans le système), ce qui en fait un bon choix pour développer des systèmes hautement évolutifs.

Grâce à sa boucle d'événements à thread unique et à son modèle d'E/S asynchrone non bloquant, Node.js fonctionne mieux sur des applications intensives en E/S nécessitant vitesse et évolutivité avec de nombreuses connexions simultanées, comme le streaming vidéo et audio, les applications en temps réel, les chats en direct, les applications de jeu, les outils de collaboration ou les logiciels de bourse.

Node.js peut ne pas être le bon choix pour les opérations intensives en CPU. Au lieu de cela, le modèle de thread traditionnel peut mieux performer.

### **npm**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qj1OTPHk-djj2C1Nnkn4VQ.png)

**npm** est le gestionnaire de paquets par défaut pour Node.js et il est installé dans le système lorsque Node.js est installé. Il peut gérer des paquets qui sont des dépendances locales d'un projet particulier, ainsi que des outils JavaScript installés globalement.

[www.npmjs.com](http://www.npmjs.com) héberge des milliers de bibliothèques gratuites à télécharger et à utiliser dans votre programme pour rendre le développement plus rapide et plus efficace. Cependant, puisque n'importe qui peut créer des bibliothèques et qu'il n'y a pas de processus de vérification pour la soumission, vous devez être prudent quant à la qualité, la sécurité ou la malveillance de certaines. npm compte sur les signalements des utilisateurs pour retirer les paquets s'ils violent les politiques, et pour vous aider à décider, il inclut des statistiques comme le nombre de téléchargements et le nombre de paquets dépendants.

### **Comment exécuter du code dans Node.js**

Commencez par installer Node sur votre ordinateur si vous ne l'avez pas déjà. Le moyen le plus simple est de visiter [nodejs.org](https://nodejs.org) et de cliquer pour le télécharger. Sauf si vous voulez ou avez besoin d'avoir accès aux dernières fonctionnalités, téléchargez la version LTS (Long Term Support) pour votre système d'exploitation.

Vous exécutez une application Node à partir du terminal de votre ordinateur. Par exemple, créez un fichier app.js et ajoutez `console.log('Bonjour');` à celui-ci. Dans votre terminal, changez le répertoire pour le dossier où se trouve ce fichier et exécutez `node app.js`. Il enregistrera Bonjour dans la console. ?

### Références

Voici quelques-unes des ressources intéressantes que j'ai consultées lors de la rédaction de l'article.

Présentations de Node.js par son auteur :

* [Présentation originale de Node.js](https://www.youtube.com/watch?v=ztspvPYybIY) par Ryan Dahl à JSConf 2009
* [10 choses que je regrette à propos de Node.js](https://www.youtube.com/watch?v=M3BM9TB-8yA) par Ryan Dahl à JSConf EU 2018

Présentations sur Node, la boucle d'événements et la bibliothèque libuv :

* [What the heck is the event loop anyway?](https://www.youtube.com/watch?v=8aGhZQkoFbQ) par Philip Roberts à JSConf EU
* [Node.js Explained](https://www.youtube.com/watch?v=L0pjVcIsU6A) par Jeff Kunkle
* [In The Loop](https://www.youtube.com/watch?v=cCOL7MC4Pl0) par Jake Archibald à JSConf Asia 2018
* [Everything You Need to Know About Node.js Event Loop](https://www.youtube.com/watch?v=PNa9OMajw9w) par Bert Belder
* [A deep dive into libuv](https://www.youtube.com/watch?v=sGTRmPiXD4Y) par Saul Ibarra Coretge à NodeConf EU 2016

Documents Node :

* [À propos de Node.js](https://nodejs.org/en/about/)
* [The Node.js Event Loop, Timers, and process.nextTick()](https://nodejs.org/de/docs/guides/event-loop-timers-and-nexttick/)
* [Aperçu du bloquant vs non-bloquant](https://nodejs.org/en/docs/guides/blocking-vs-non-blocking/)

Ressources supplémentaires :

* [Art of Node](https://github.com/maxogden/art-of-node) par Max Ogden
* [Callback hell](http://callbackhell.com/) par Max Ogden
* [What is non-blocking or asynchronous I/O in Node.js?](https://stackoverflow.com/questions/10570246/what-is-non-blocking-or-asynchronous-i-o-in-node-js) sur Stack Overflow
* [Event driven programming](https://en.wikipedia.org/wiki/Event-driven_programming) sur Wikipedia
* [Node.js](https://en.wikipedia.org/wiki/Node.js) sur Wikipedia
* [Thread](https://en.wikipedia.org/wiki/Thread_(computing)) sur Wikipedia
* [libuv](https://libuv.org/)

Merci d'avoir lu.