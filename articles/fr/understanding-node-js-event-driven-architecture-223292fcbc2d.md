---
title: Comprendre l'architecture orientée événements de Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-08T05:27:40.000Z'
originalURL: https://freecodecamp.org/news/understanding-node-js-event-driven-architecture-223292fcbc2d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Nozl2qd0SV8Uya2CEkF_mg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comprendre l'architecture orientée événements de Node.js
seo_desc: 'By Samer Buna


  Update: This article is now part of my book “Node.js Beyond The Basics”.

  Read the updated version of this content and more about Node at jscomplete.com/node-beyond-basics.


  Most of Node’s objects — like HTTP requests, responses, and st...'
---

Par Samer Buna

> **Mise à jour :** Cet article fait maintenant partie de mon livre « Node.js Beyond The Basics ».

> Lisez la version mise à jour de ce contenu et plus sur Node à l'adresse [**jscomplete.com/node-beyond-basics**](https://jscomplete.com/g/node-events).

La plupart des objets de Node — comme les requêtes HTTP, les réponses et les flux — implémentent le module `EventEmitter` afin de pouvoir fournir un moyen d'émettre et d'écouter des événements.

![Image](https://cdn-media-1.freecodecamp.org/images/1*74K5OhiYt7WTR0WuVGeNLQ.png)

La forme la plus simple de la nature orientée événements est le style de rappel de certaines des fonctions Node.js populaires — par exemple, `fs.readFile`. Dans cette analogie, l'événement sera déclenché une fois (quand Node est prêt à appeler le rappel) et le rappel agit comme le gestionnaire d'événements.

Explorons d'abord cette forme de base.

#### Appelez-moi quand vous êtes prêt, Node !

La manière originale dont Node gérait les événements asynchrones était avec des rappels. C'était il y a longtemps, avant que JavaScript ne dispose d'une prise en charge native des promesses et de la fonctionnalité async/await.

Les rappels sont essentiellement des fonctions que vous passez à d'autres fonctions. Cela est possible en JavaScript car les fonctions sont des objets de première classe.

Il est important de comprendre que les rappels n'indiquent pas un appel asynchrone dans le code. Une fonction peut appeler le rappel à la fois de manière synchrone et asynchrone.

Par exemple, voici une fonction hôte `fileSize` qui accepte une fonction de rappel `cb` et peut invoquer cette fonction de rappel à la fois de manière synchrone et asynchrone en fonction d'une condition :

```js
function fileSize (fileName, cb) {
  if (typeof fileName !== 'string') {
    return cb(new TypeError('argument should be string')); // Synchrone
  }
  fs.stat(fileName, (err, stats) => {
    if (err) { return cb(err); } // Asynchrone
    cb(null, stats.size); // Asynchrone
  });
}
```

Notez que cela est une mauvaise pratique qui conduit à des erreurs inattendues. Concevez les fonctions hôtes pour consommer les rappels soit toujours de manière synchrone, soit toujours de manière asynchrone.

Explorons un exemple simple d'une fonction Node asynchrone typique qui est écrite avec un style de rappel :

```js
const readFileAsArray = function(file, cb) {
  fs.readFile(file, function(err, data) {
    if (err) {
      return cb(err);
    }
    const lines = data.toString().trim().split('\n');
    cb(null, lines);
  });
};
```

`readFileAsArray` prend un chemin de fichier et une fonction de rappel. Il lit le contenu du fichier, le divise en un tableau de lignes et appelle la fonction de rappel avec ce tableau.

Voici un exemple d'utilisation. Supposons que nous avons le fichier `numbers.txt` dans le même répertoire avec un contenu comme ceci :

```
10
11
12
13
14
15
```

Si nous avons une tâche pour compter les nombres impairs dans ce fichier, nous pouvons utiliser `readFileAsArray` pour simplifier le code :

```js
readFileAsArray('./numbers.txt', (err, lines) => {
  if (err) throw err;
  const numbers = lines.map(Number);
  const oddNumbers = numbers.filter(n => n%2 === 1);
  console.log('Nombre de nombres impairs :', oddNumbers.length);
});
```

Le code lit le contenu des nombres dans un tableau de chaînes, les analyse en tant que nombres et compte les nombres impairs.

Le style de rappel de Node est utilisé ici de manière pure. Le rappel a un argument `err` en premier qui est nullable et nous passons le rappel comme dernier argument pour la fonction hôte. Vous devriez toujours faire cela dans vos fonctions car les utilisateurs supposeront probablement cela. Faites en sorte que la fonction hôte reçoive le rappel comme son dernier argument et faites en sorte que le rappel attende un objet d'erreur comme premier argument.

#### L'alternative moderne de JavaScript aux rappels

En JavaScript moderne, nous avons des objets de promesse. Les promesses peuvent être une alternative aux rappels pour les API asynchrones. Au lieu de passer un rappel comme argument et de gérer l'erreur au même endroit, un objet de promesse nous permet de gérer les cas de succès et d'erreur séparément et il nous permet également d'enchaîner plusieurs appels asynchrones au lieu de les imbriquer.

Si la fonction `readFileAsArray` prend en charge les promesses, nous pouvons l'utiliser comme suit :

```js
readFileAsArray('./numbers.txt')
  .then(lines => {
    const numbers = lines.map(Number);
    const oddNumbers = numbers.filter(n => n%2 === 1);
    console.log('Nombre de nombres impairs :', oddNumbers.length);
  })
  .catch(console.error);
```

Au lieu de passer une fonction de rappel, nous avons appelé une fonction `.then` sur la valeur de retour de la fonction hôte. Cette fonction `.then` nous donne généralement accès au même tableau de lignes que nous obtenons dans la version de rappel, et nous pouvons effectuer notre traitement dessus comme avant. Pour gérer les erreurs, nous ajoutons un appel `.catch` sur le résultat et cela nous donne accès à une erreur lorsqu'elle se produit.

Rendre la fonction hôte compatible avec une interface de promesse est plus facile en JavaScript moderne grâce au nouvel objet Promise. Voici la fonction `readFileAsArray` modifiée pour prendre en charge une interface de promesse en plus de l'interface de rappel qu'elle prend déjà en charge :

```js
const readFileAsArray = function(file, cb = () => {}) {
  return new Promise((resolve, reject) => {
    fs.readFile(file, function(err, data) {
      if (err) {
        reject(err);
        return cb(err);
      }
      const lines = data.toString().trim().split('\n');
      resolve(lines);
      cb(null, lines);
    });
  });
};
```

Nous faisons donc en sorte que la fonction retourne un objet Promise, qui enveloppe l'appel asynchrone `fs.readFile`. L'objet promise expose deux arguments, une fonction `resolve` et une fonction `reject`.

Chaque fois que nous voulons invoquer le rappel avec une erreur, nous utilisons également la fonction `reject` de la promesse, et chaque fois que nous voulons invoquer le rappel avec des données, nous utilisons également la fonction `resolve` de la promesse.

La seule autre chose que nous avons dû faire dans ce cas est d'avoir une valeur par défaut pour cet argument de rappel au cas où le code est utilisé avec l'interface de promesse. Nous pouvons utiliser une fonction vide par défaut simple dans l'argument pour ce cas : `() =>` {}.

#### Consommer des promesses avec async/await

L'ajout d'une interface de promesse rend votre code beaucoup plus facile à utiliser lorsqu'il y a besoin de boucler sur une fonction asynchrone. Avec les rappels, les choses deviennent désordonnées.

Les promesses améliorent cela un peu, et les générateurs de fonctions améliorent cela un peu plus. Cela dit, une alternative plus récente pour travailler avec du code asynchrone est d'utiliser la fonction `async`, qui nous permet de traiter le code asynchrone comme s'il était synchrone, le rendant ainsi beaucoup plus lisible dans l'ensemble.

Voici comment nous pouvons consommer la fonction `readFileAsArray` avec async/await :

```
async function countOdd () {
  try {
    const lines = await readFileAsArray('./numbers');
    const numbers = lines.map(Number);
    const oddCount = numbers.filter(n => n%2 === 1).length;
    console.log('Nombre de nombres impairs :', oddCount);
  } catch(err) {
    console.error(err);
  }
}
countOdd();
```

Nous créons d'abord une fonction asynchrone, qui est simplement une fonction normale avec le mot `async` avant elle. À l'intérieur de la fonction asynchrone, nous appelons la fonction `readFileAsArray` comme si elle retournait la variable lines, et pour que cela fonctionne, nous utilisons le mot-clé `await`. Après cela, nous continuons le code comme si l'appel `readFileAsArray` était synchrone.

Pour faire fonctionner les choses, nous exécutons la fonction asynchrone. C'est très simple et plus lisible. Pour travailler avec les erreurs, nous devons envelopper l'appel asynchrone dans une instruction `try`/`catch`.

Avec cette fonctionnalité async/await, nous n'avons pas eu à utiliser d'API spéciale (comme .then et .catch). Nous avons simplement étiqueté les fonctions différemment et utilisé du JavaScript pur pour le code.

Nous pouvons utiliser la fonctionnalité async/await avec n'importe quelle fonction qui prend en charge une interface de promesse. Cependant, nous ne pouvons pas l'utiliser avec des fonctions asynchrones de style rappel (comme setTimeout par exemple).

### Le module EventEmitter

EventEmitter est un module qui facilite la communication entre les objets dans Node. EventEmitter est au cœur de l'architecture asynchrone orientée événements de Node. De nombreux modules intégrés de Node héritent de EventEmitter.

Le concept est simple : les objets émetteurs émettent des événements nommés qui provoquent l'appel des écouteurs précédemment enregistrés. Ainsi, un objet émetteur a essentiellement deux caractéristiques principales :

* Émettre des événements nommés.
* Enregistrer et désenregistrer des fonctions d'écoute.

Pour travailler avec EventEmitter, nous créons simplement une classe qui étend EventEmitter.

```
class MyEmitter extends EventEmitter {}
```

Les objets émetteurs sont ce que nous instancions à partir des classes basées sur EventEmitter :

```
const myEmitter = new MyEmitter();
```

À tout moment dans le cycle de vie de ces objets émetteurs, nous pouvons utiliser la fonction emit pour émettre n'importe quel événement nommé que nous voulons.

```
myEmitter.emit('something-happened');
```

Émettre un événement est le signal que certaines conditions se sont produites. Cette condition concerne généralement un changement d'état dans l'objet émetteur.

Nous pouvons ajouter des fonctions d'écoute en utilisant la méthode `on`, et ces fonctions d'écoute seront exécutées chaque fois que l'objet émetteur émet leur événement nommé associé.

#### Événements ≠ Asynchronisme

Examinons un exemple :

```js
const EventEmitter = require('events');

class WithLog extends EventEmitter {
  execute(taskFunc) {
    console.log('Avant l\'exécution');
    this.emit('begin');
    taskFunc();
    this.emit('end');
    console.log('Après l\'exécution');
  }
}

const withLog = new WithLog();

withLog.on('begin', () => console.log('Sur le point d\'exécuter'));
withLog.on('end', () => console.log('Terminé avec l\'exécution'));

withLog.execute(() => console.log('*** Exécution de la tâche ***'));
```

La classe `WithLog` est un émetteur d'événements. Elle définit une fonction d'instance `execute`. Cette fonction `execute` reçoit un argument, une fonction de tâche, et enveloppe son exécution avec des instructions de journalisation. Elle déclenche des événements avant et après l'exécution.

Pour voir la séquence de ce qui va se passer ici, nous enregistrons des écouteurs sur les deux événements nommés et exécutons enfin une tâche d'exemple pour déclencher les choses.

Voici le résultat de cela :

```js
Avant l'exécution
Sur le point d'exécuter
*** Exécution de la tâche ***
Terminé avec l'exécution
Après l'exécution
```

Ce que je veux que vous remarquiez à propos de la sortie ci-dessus, c'est que tout se passe de manière synchrone. Il n'y a rien d'asynchrone dans ce code.

* Nous obtenons la ligne « Avant l'exécution » en premier.
* L'événement nommé `begin` provoque ensuite la ligne « Sur le point d'exécuter ».
* La ligne d'exécution réelle produit ensuite la ligne « *** Exécution de la tâche *** ».
* L'événement nommé `end` provoque ensuite la ligne « Terminé avec l'exécution »
* Nous obtenons la ligne « Après l'exécution » en dernier.

Tout comme les anciens rappels, ne supposez pas que les événements signifient un code synchrone ou asynchrone.

Cela est important, car si nous passons une fonction `taskFunc` asynchrone à `execute`, les événements émis ne seront plus précis.

Nous pouvons simuler le cas avec un appel `setImmediate` :

```js
// ...

withLog.execute(() => {
  setImmediate(() => {
    console.log('*** Exécution de la tâche ***')
  });
});
```

Maintenant, la sortie serait :

```
Avant l'exécution
Sur le point d'exécuter
Terminé avec l'exécution
Après l'exécution
*** Exécution de la tâche ***
```

Cela est incorrect. Les lignes après l'appel asynchrone, qui ont provoqué les appels « Terminé avec l'exécution » et « Après l'exécution », ne sont plus précises.

Pour émettre un événement après qu'une fonction asynchrone soit terminée, nous devrons combiner les rappels (ou les promesses) avec cette communication basée sur les événements. L'exemple ci-dessous le démontre.

Un avantage de l'utilisation des événements au lieu des rappels réguliers est que nous pouvons réagir au même signal plusieurs fois en définissant plusieurs écouteurs. Pour accomplir la même chose avec les rappels, nous devons écrire plus de logique à l'intérieur du seul rappel disponible. Les événements sont un excellent moyen pour les applications de permettre à plusieurs plugins externes de construire des fonctionnalités sur le cœur de l'application. Vous pouvez les considérer comme des points d'accroche pour permettre de personnaliser l'histoire autour d'un changement d'état.

#### Événements asynchrones

Convertissons l'exemple d'échantillon synchrone en quelque chose d'asynchrone et un peu plus utile.

```js
const fs = require('fs');
const EventEmitter = require('events');

class WithTime extends EventEmitter {
  execute(asyncFunc, ...args) {
    this.emit('begin');
    console.time('execute');
    asyncFunc(...args, (err, data) => {
      if (err) {
        return this.emit('error', err);
      }

      this.emit('data', data);
      console.timeEnd('execute');
      this.emit('end');
    });
  }
}

const withTime = new WithTime();

withTime.on('begin', () => console.log('Sur le point d\'exécuter'));
withTime.on('end', () => console.log('Terminé avec l\'exécution'));

withTime.execute(fs.readFile, __filename);
```

La classe `WithTime` exécute une `asyncFunc` et rapporte le temps que prend cette `asyncFunc` en utilisant les appels `console.time` et `console.timeEnd`. Elle émet la bonne séquence d'événements avant et après l'exécution. Et émet également des événements d'erreur/données pour travailler avec les signaux habituels des appels asynchrones.

Nous testons un émetteur `withTime` en lui passant un appel `fs.readFile`, qui est une fonction asynchrone. Au lieu de gérer les données de fichier avec un rappel, nous pouvons maintenant écouter l'événement de données.

Lorsque nous exécutons ce code, nous obtenons la bonne séquence d'événements, comme prévu, et nous obtenons un temps rapporté pour l'exécution, ce qui est utile :

```
Sur le point d'exécuter
execute: 4.507ms
Terminé avec l'exécution
```

Remarquez comment nous avons dû combiner un rappel avec un émetteur d'événements pour accomplir cela. Si la `asynFunc` prenait également en charge les promesses, nous pourrions utiliser la fonctionnalité async/await pour faire la même chose :

```js
class WithTime extends EventEmitter {
  async execute(asyncFunc, ...args) {
    this.emit('begin');
    try {
      console.time('execute');
      const data = await asyncFunc(...args);
      this.emit('data', data);
      console.timeEnd('execute');
      this.emit('end');
    } catch(err) {
      this.emit('error', err);
    }
  }
}
```

Je ne sais pas pour vous, mais cela est beaucoup plus lisible pour moi que le code basé sur les rappels ou toute ligne .then/.catch. La fonctionnalité async/await nous rapproche autant que possible du langage JavaScript lui-même, ce que je pense être une grande victoire.

#### Arguments et erreurs des événements

Dans l'exemple précédent, il y avait deux événements qui ont été émis avec des arguments supplémentaires.

L'événement d'erreur est émis avec un objet d'erreur.

```
this.emit('error', err);
```

L'événement de données est émis avec un objet de données.

```
this.emit('data', data);
```

Nous pouvons utiliser autant d'arguments que nous le souhaitons après l'événement nommé, et tous ces arguments seront disponibles à l'intérieur des fonctions d'écoute que nous enregistrons pour ces événements nommés.

Par exemple, pour travailler avec l'événement de données, la fonction d'écoute que nous enregistrons aura accès à l'argument de données qui a été passé à l'événement émis et cet objet de données est exactement ce que la `asyncFunc` expose.

```js
withTime.on('data', (data) => {
  // faire quelque chose avec les données
});
```

L'événement `error` est généralement un événement spécial. Dans notre exemple basé sur les rappels, si nous ne gérons pas l'événement d'erreur avec un écouteur, le processus node va en fait quitter.

Pour démontrer cela, faites un autre appel à la méthode execute avec un mauvais argument :

```js
class WithTime extends EventEmitter {
  execute(asyncFunc, ...args) {
    console.time('execute');
    asyncFunc(...args, (err, data) => {
      if (err) {
        return this.emit('error', err); // Non géré
      }

      console.timeEnd('execute');
    });
  }
}

const withTime = new WithTime();

withTime.execute(fs.readFile, ''); // MAUVAIS APPEL
withTime.execute(fs.readFile, __filename);
```

Le premier appel execute ci-dessus déclenchera une erreur. Le processus node va planter et quitter :

```js
events.js:163
      throw er; // Événement 'error' non géré
      ^
Error: ENOENT: aucun fichier ou répertoire de ce type, open ''
```

Le deuxième appel execute sera affecté par ce plantage et ne sera potentiellement pas exécuté du tout.

Si nous enregistrons un écouteur pour l'événement spécial `error`, le comportement du processus node changera. Par exemple :

```js
withTime.on('error', (err) => {
  // faire quelque chose avec err, par exemple le journaliser quelque part
  console.log(err)
});
```

Si nous faisons ce qui précède, l'erreur du premier appel execute sera signalée mais le processus node ne plantera pas et ne quittera pas. L'autre appel execute se terminera normalement :

```
{ Error: ENOENT: aucun fichier ou répertoire de ce type, open '' errno: -2, code: 'ENOENT', syscall: 'open', path: '' }
execute: 4.276ms
```

Notez que Node se comporte actuellement différemment avec les fonctions basées sur les promesses et se contente d'émettre un avertissement, mais cela changera éventuellement :

```
UnhandledPromiseRejectionWarning: Unhandled promise rejection (rejection id: 1): Error: ENOENT: aucun fichier ou répertoire de ce type, open ''
DeprecationWarning: Unhandled promise rejections are deprecated. In the future, promise rejections that are not handled will terminate the Node.js process with a non-zero exit code.
```

L'autre moyen de gérer les exceptions des erreurs émises est d'enregistrer un écouteur pour l'événement global `uncaughtException` du processus. Cependant, capturer les erreurs globalement avec cet événement est une mauvaise idée.

Le conseil standard concernant `uncaughtException` est de l'éviter, mais si vous devez le faire (par exemple pour signaler ce qui s'est passé ou faire des nettoyages), vous devriez simplement laisser le processus quitter de toute façon :

```js
process.on('uncaughtException', (err) => {
  // quelque chose n'a pas été géré.
  // Faites tout nettoyage et quittez de toute façon !

  console.error(err); // ne faites pas seulement cela.

  // FORCEZ la sortie du processus aussi.
  process.exit(1);
});
```

Cependant, imaginez que plusieurs événements d'erreur se produisent exactement au même moment. Cela signifie que l'écouteur `uncaughtException` ci-dessus sera déclenché plusieurs fois, ce qui pourrait poser problème pour certains codes de nettoyage. Un exemple de cela est lorsque plusieurs appels sont faits à une action d'arrêt de base de données.

Le module `EventEmitter` expose une méthode `once`. Cette méthode signale d'invoquer l'écouteur une seule fois, pas chaque fois que cela se produit. Donc, c'est un cas d'utilisation pratique à utiliser avec uncaughtException car avec la première exception non capturée, nous commencerons à faire le nettoyage et nous savons que nous allons quitter le processus de toute façon.

#### Ordre des écouteurs

Si nous enregistrons plusieurs écouteurs pour le même événement, l'invocation de ces écouteurs se fera dans l'ordre. Le premier écouteur que nous enregistrons est le premier écouteur qui est invoqué.

```js
//  
withTime.on('data', (data) => {
  console.log(`Longueur : ${data.length}`);
});

//  
withTime.on('data', (data) => {
  console.log(`Caractères : ${data.toString().length}`);
});

withTime.execute(fs.readFile, __filename);
```

Le code ci-dessus provoquera l'enregistrement de la ligne « Longueur » avant la ligne « Caractères », car c'est l'ordre dans lequel nous avons défini ces écouteurs.

Si vous devez définir un nouvel écouteur, mais que cet écouteur soit invoqué en premier, vous pouvez utiliser la méthode `prependListener` :

```
//  
withTime.on('data', (data) => {
  console.log(`Longueur : ${data.length}`);
});

//  
withTime.prependListener('data', (data) => {
  console.log(`Caractères : ${data.toString().length}`);
});

withTime.execute(fs.readFile, __filename);
```

Cela provoquera l'enregistrement de la ligne « Caractères » en premier.

Et enfin, si vous devez supprimer un écouteur, vous pouvez utiliser la méthode `removeListener`.

C'est tout ce que j'ai pour ce sujet. Merci d'avoir lu ! À la prochaine !

Apprendre React ou Node ? Consultez mes livres :

* [Learn React.js by Building Games](http://amzn.to/2peYJZj)
* [Node.js Beyond the Basics](http://amzn.to/2FYfYru)