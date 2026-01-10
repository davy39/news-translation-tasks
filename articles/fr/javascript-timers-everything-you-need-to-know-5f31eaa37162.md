---
title: 'Minuteries JavaScript : Tout ce que vous devez savoir'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T19:09:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-timers-everything-you-need-to-know-5f31eaa37162
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3MvXyPKEun4xcGZX6ay4PA.png
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Minuteries JavaScript : Tout ce que vous devez savoir'
seo_desc: 'By Samer Buna

  A few weeks ago, I tweeted this interview question:

  _* Answer the question in your head now before you proceed *_

  About half the replies to the Tweet were wrong. The answer is NOT V8 (or other VMs)!!
  While famously known as “JavaScript ...'
---

Par Samer Buna

Il y a quelques semaines, j'ai tweeté cette question d'entretien :

**_*** Répondez à la question dans votre tête maintenant avant de continuer ***_**

*Environ la moitié des réponses au tweet étaient fausses.* La réponse n'est **PAS** V8 (ou d'autres VM) !! Bien que connues sous le nom de "Minuteries JavaScript", les fonctions comme `setTimeout` et `setInterval` ne font pas partie des spécifications ECMAScript ou des implémentations de moteurs JavaScript. Les fonctions de minuterie sont implémentées par les navigateurs et leurs implémentations seront différentes selon les navigateurs. Les minuteries sont également implémentées nativement par le runtime Node.js lui-même.

Dans les navigateurs, les principales fonctions de minuterie font partie de l'interface `Window`, qui comporte quelques autres fonctions et objets. Cette interface rend tous ses éléments disponibles globalement dans le scope principal de JavaScript. C'est pourquoi vous pouvez exécuter `setTimeout` directement dans la console de votre navigateur.

Dans Node, les minuteries font partie de l'objet `global`, qui se comporte de manière similaire à l'interface `Window` du navigateur. Vous pouvez voir le code source des minuteries dans Node [ici](https://github.com/nodejs/node/blob/master/lib/timers.js).

Certains pourraient penser que c'est une mauvaise question d'entretien — pourquoi est-il important de savoir cela ?! En tant que développeur JavaScript, je pense que vous êtes censé savoir cela car si vous ne le savez pas, cela pourrait être un signe que vous ne comprenez pas complètement comment V8 (et d'autres VM) interagit avec les navigateurs et Node.

Faisons quelques exemples et défis sur les fonctions de minuterie, d'accord ?

> **Mise à jour :** Cet article fait maintenant partie de mon "Introduction complète à Node.js".
> Vous pouvez lire la version mise à jour à [ici](https://jscomplete.com/g/js-timers).

### Retarder l'exécution d'une fonction

Les fonctions de minuterie sont des fonctions d'ordre supérieur qui peuvent être utilisées pour retarder ou répéter l'exécution d'autres fonctions (qu'elles reçoivent comme premier argument).

Voici un exemple de retardement :

```js
// exemple1.js
setTimeout(
  () => {
    console.log('Bonjour après 4 secondes');
  },
  4 * 1000
);
```

Cet exemple utilise `setTimeout` pour retarder l'impression du message de salutation de 4 secondes. Le deuxième argument de `setTimeout` est le délai (en ms). C'est pourquoi j'ai multiplié 4 par 1000 pour en faire 4 secondes.

Le premier argument de `setTimeout` est la fonction dont l'exécution sera retardée.

Si vous exécutez le fichier `example1.js` avec la commande `node`, Node attendra 4 secondes puis imprimera le message de salutation (et se terminera après cela).

Notez que le premier argument de `setTimeout` est simplement une référence de fonction. Il ne doit pas nécessairement être une fonction en ligne comme celle de `example1.js`. Voici le même exemple sans utiliser de fonction en ligne :

```js
const func = () => {
  console.log('Bonjour après 4 secondes');
};
setTimeout(func, 4 * 1000);
```

### Passer des arguments

Si la fonction qui utilise `setTimeout` pour retarder son exécution accepte des arguments, nous pouvons utiliser les arguments restants de `setTimeout` lui-même (après les 2 que nous avons appris jusqu'à présent) pour relayer les valeurs des arguments à la fonction retardée.

```js
// Pour : func(arg1, arg2, arg3, ...)
// Nous pouvons utiliser : setTimeout(func, délai, arg1, arg2, arg3, ...)
```

Voici un exemple :

```js
// exemple2.js
const rocks = who => {
  console.log(who + ' rocks');
};
setTimeout(rocks, 2 * 1000, 'Node.js');
```

La fonction `rocks` ci-dessus, qui est retardée de 2 secondes, accepte un argument `who` et l'appel `setTimeout` relaie la valeur "Node.js" comme cet argument `who`.

L'exécution de `example2.js` avec la commande `node` imprimera "Node.js rocks" après 2 secondes.

### Défi des minuteries #1

En utilisant ce que vous avez appris jusqu'à présent sur `setTimeout`, imprimez les 2 messages suivants après leurs délais correspondants.

* Imprimez le message "Bonjour après 4 secondes" après 4 secondes
* Imprimez le message "Bonjour après 8 secondes" après 8 secondes.

**Contraintes :**
Vous ne pouvez définir qu'une seule fonction dans votre solution, y compris les fonctions en ligne. Cela signifie que plusieurs appels `setTimeout` devront utiliser exactement la même fonction.

#### Solution

Voici comment je résoudreais ce défi :

```js
// solution1.js
const theOneFunc = delay => {
  console.log('Bonjour après ' + delay + ' secondes');
};
setTimeout(theOneFunc, 4 * 1000, 4);
setTimeout(theOneFunc, 8 * 1000, 8);
```

J'ai fait en sorte que `theOneFunc` reçoive un argument `delay` et utilisé la valeur de cet argument `delay` dans le message imprimé. De cette façon, la fonction peut imprimer différents messages en fonction de la valeur de délai que nous lui passons.

J'ai ensuite utilisé `theOneFunc` dans deux appels `setTimeout`, l'un qui se déclenche après 4 secondes et l'autre après 8 secondes. Ces deux appels `setTimeout` reçoivent également un **3ème** argument pour représenter l'argument `delay` pour `theOneFunc`.

L'exécution du fichier `solution1.js` avec la commande `node` imprimera les exigences du défi, le premier message après 4 secondes, et le deuxième message après 8 secondes.

### Répéter l'exécution d'une fonction

Et si je vous demandais d'imprimer un message toutes les 4 secondes, pour toujours ?

Bien que vous puissiez mettre `setTimeout` dans une boucle, l'API des minuteries offre également la fonction `setInterval`, qui accomplirait l'exigence de faire quelque chose pour toujours.

Voici un exemple de setInterval :

```js
// exemple3.js
setInterval(
  () => console.log('Bonjour toutes les 3 secondes'),
  3000
);
```

Cet exemple imprimera son message toutes les 3 secondes. L'exécution de `example3.js` avec la commande `node` fera en sorte que Node imprime ce message pour toujours, jusqu'à ce que vous arrêtiez le processus (avec _CTRL+C_).

### Annuler les minuteries

Parce qu'un appel à une fonction de minuterie planifie une action, cette action peut également être annulée avant son exécution.

Un appel à `setTimeout` retourne un identifiant de minuterie et vous pouvez utiliser cet identifiant de minuterie avec un appel `clearTimeout` pour annuler cette minuterie. Voici un exemple :

```js
// exemple4.js
const timerId = setTimeout(
  () => console.log('Vous ne verrez pas celui-ci !'),
  0
);
clearTimeout(timerId);
```

Cette minuterie simple est censée se déclencher après `0` ms (la rendant immédiate), mais elle ne le fera pas car nous capturons la valeur `timerId` et l'annulons immédiatement après avec un appel `clearTimeout`.

Lorsque nous exécutons `example4.js` avec la commande `node`, Node n'imprimera rien et le processus se terminera simplement.

D'ailleurs, dans Node.js, il existe une autre façon de faire `setTimeout` avec `0` ms. L'API des minuteries Node.js a une autre fonction appelée `setImmediate`, et c'est essentiellement la même chose qu'un `setTimeout` avec un délai de `0` ms mais nous n'avons pas à spécifier de délai là :

```js
setImmediate(
  () => console.log('Je suis équivalent à setTimeout avec 0 ms'),
);
```

_La fonction `setImmediate` [n'est pas disponible dans tous les navigateurs](https://developer.mozilla.org/en-US/docs/Web/API/Window/setImmediate). Ne l'utilisez pas pour le code front-end._

Tout comme `clearTimeout`, il existe également une fonction `clearInterval`, qui fait la même chose mais pour les appels `setInerval`, et il existe également un appel `clearImmediate`.

### Un délai de minuterie n'est pas une chose garantie

Dans l'exemple précédent, avez-vous remarqué comment l'exécution de quelque chose avec `setTimeout` après `0` ms ne signifiait pas l'exécuter immédiatement (après la ligne setTimeout), mais plutôt l'exécuter immédiatement après tout le reste dans le script (y compris l'appel clearTimeout) ?

Permettez-moi de clarifier ce point avec un exemple. Voici un simple appel `setTimeout` qui devrait se déclencher après une demi-seconde, mais il ne le fera pas :

```js
// exemple5.js
setTimeout(
  () => console.log('Bonjour après 0,5 secondes. PEUT-ÊTRE !'),
  500,
);
for (let i = 0; i < 1e10; i++) {
  // Bloquer les choses de manière synchrone
}
```

Juste après avoir défini la minuterie dans cet exemple, nous bloquons le runtime de manière synchrone avec une grande boucle `for`. Le `1e10` est `1` avec `10` zéros devant, donc la boucle est une boucle de `10` milliards de ticks (ce qui simule essentiellement un CPU occupé). Node ne peut rien faire pendant que cette boucle tourne.

Cela est bien sûr une très mauvaise chose à faire en pratique, mais cela vous aidera ici à comprendre que le délai `setTimeout` n'est pas une chose garantie, mais plutôt une chose **minimale**. Les `500` ms signifient un délai minimum de `500` ms. En réalité, le script prendra beaucoup plus de temps pour imprimer sa ligne de salutation. Il devra attendre que la boucle de blocage se termine d'abord.

### Défi des minuteries #2

Écrivez un script pour imprimer le message "**Bonjour le monde**" chaque seconde, mais seulement 5 fois. Après 5 fois, le script doit imprimer le message "_Terminé_" et laisser le processus Node se terminer.

**Contraintes :** Vous ne pouvez pas utiliser un appel `setTimeout` pour ce défi.
**Indice :** Vous avez besoin d'un compteur.

#### Solution

Voici comment je résoudreais celui-ci :

```js
let counter = 0;
const intervalId = setInterval(() => {
  console.log('Bonjour le monde');
  counter += 1;
  if (counter === 5) {
    console.log('Terminé');
    clearInterval(intervalId);
  }
}, 1000);
```

J'ai initialisé une valeur `counter` à `0` puis démarré un appel `setInterval` en capturant son id.

La fonction retardée imprimera le message et incrémentera le compteur chaque fois. À l'intérieur de la fonction retardée, une instruction `if` vérifiera si nous en sommes à `5` fois maintenant. Si c'est le cas, elle imprimera "_Terminé_" et effacera l'intervalle en utilisant la constante `intervalId` capturée. Le délai de l'intervalle est de `1000` ms.

### Qui exactement "appele" les fonctions retardées ?

Lorsque vous utilisez le mot-clé `this` de JavaScript à l'intérieur d'une fonction régulière, comme ceci :

```js
function whoCalledMe() {
  console.log('Caller is', this);
}
```

La valeur à l'intérieur du mot-clé `this` représentera l'**appelant** de la fonction. Si vous définissez la fonction ci-dessus à l'intérieur d'un REPL Node, l'appelant sera l'objet `global`. Si vous définissez la fonction à l'intérieur de la console d'un navigateur, l'appelant sera l'objet `window`.

Définissons la fonction comme une propriété sur un objet pour rendre cela un peu plus clair :

```js
const obj = { 
  id: '42',
  whoCalledMe() {
    console.log('Caller is', this);
  }
};
// La référence de la fonction est maintenant : obj.whoCallMe
```

Maintenant, lorsque vous appelez la fonction `obj.whoCallMe` en utilisant sa référence directement, l'appelant sera l'objet `obj` (identifié par son id) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oo6w6C8omvxjxSwK_FJsag.png)

Maintenant, la question est, qui serait l'appelant si nous passons la référence de `obj.whoCallMe` à un appel `setTimetout` ?

```js
// Que va imprimer ceci ??
setTimeout(obj.whoCalledMe, 0);
```

**Qui sera l'appelant dans ce cas ?**

La réponse est différente en fonction de l'endroit où la fonction de minuterie est exécutée. Vous ne pouvez tout simplement pas dépendre de qui est l'appelant dans ce cas. Vous perdez le contrôle de l'appelant car l'implémentation de la minuterie sera celle qui invoquera votre fonction maintenant. Si vous la testez dans un REPL Node, vous obtiendrez un objet `Timetout` comme appelant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*du_RKr4vPNh1irFRPR92EA.png)

Notez que cela n'a d'importance que si vous utilisez le mot-clé `this` de JavaScript à l'intérieur de fonctions régulières. Vous n'avez pas du tout à vous soucier de l'appelant si vous utilisez des fonctions fléchées.

### Défi des minuteries #3

Écrivez un script pour imprimer en continu le message "Bonjour le monde" avec des délais variables. Commencez avec un délai de 1 seconde puis incrémentez le délai de 1 seconde chaque fois. La deuxième fois aura un délai de 2 secondes. La troisième fois aura un délai de 3 secondes, et ainsi de suite.

Incluez le délai dans le message imprimé. La sortie attendue ressemble à ceci :

```
Bonjour le monde. 1
Bonjour le monde. 2
Bonjour le monde. 3
...
```

**Contraintes :** Vous ne pouvez utiliser que `const` pour définir des variables. Vous ne pouvez pas utiliser `let` ou `var`.

#### Solution

Parce que le montant du délai est une variable dans ce défi, nous ne pouvons pas utiliser `setInterval` ici, mais nous pouvons créer manuellement une exécution d'intervalle en utilisant `setTimeout` dans un appel récursif. La première fonction exécutée avec setTimeout créera une autre minuterie, et ainsi de suite.

De plus, parce que nous ne pouvons pas utiliser let/var, nous ne pouvons pas avoir de compteur pour incrémenter le délai dans chaque appel récursif, mais nous pouvons plutôt utiliser les arguments de la fonction récursive pour incrémenter pendant l'appel récursif.

Voici une façon possible de résoudre ce défi :

```js
const greeting = delay =>
  setTimeout(() => {
    console.log('Bonjour le monde. ' + delay);
    greeting(delay + 1);
  }, delay * 1000);
greeting(1);
```

### Défi des minuteries #4

Écrivez un script pour imprimer en continu le message "Bonjour le monde" avec le même concept de délais variables que le défi #3, mais cette fois, en groupes de 5 messages par intervalle de délai principal. Commencez avec un délai de 100 ms pour les 5 premiers messages, puis un délai de 200 ms pour les 5 messages suivants, puis 300 ms, et ainsi de suite.

Voici comment le script doit se comporter :

* Au point 100 ms, le script commencera à imprimer "Bonjour le monde" et le fera 5 fois avec un intervalle de 100 ms. Le 1er message apparaîtra à 100 ms, le 2ème message à 200 ms, et ainsi de suite.
* Après les 5 premiers messages, le script doit incrémenter le délai principal à 200 ms. Donc, le 6ème message sera imprimé à 500 ms + 200 ms (700 ms), le 7ème message sera imprimé à 900 ms, le 8ème message sera imprimé à 1100 ms, et ainsi de suite.
* Après 10 messages, le script doit incrémenter le délai principal à 300 ms. Donc, le 11ème message doit être imprimé à 500 ms + 1000 ms + 300 ms (18000 ms). Le 12ème message doit être imprimé à 21000 ms, et ainsi de suite.
* Continuez le motif pour toujours.

Incluez le délai dans le message imprimé. La sortie attendue ressemble à ceci (sans les commentaires) :

```
Bonjour le monde. 100  // À 100 ms
Bonjour le monde. 100  // À 200 ms
Bonjour le monde. 100  // À 300 ms
Bonjour le monde. 100  // À 400 ms
Bonjour le monde. 100  // À 500 ms
Bonjour le monde. 200  // À 700 ms
Bonjour le monde. 200  // À 900 ms
Bonjour le monde. 200  // À 1100 ms
...
```

**Contraintes :** Vous ne pouvez utiliser que des appels `setInterval` (pas `setTimeout`) et vous ne pouvez utiliser qu'une seule instruction if.

#### Solution

Parce que nous ne pouvons utiliser que des appels `setInterval`, nous aurons également besoin de récursion ici pour incrémenter le délai du prochain appel `setInterval`. De plus, nous avons besoin d'une instruction if pour contrôler cela uniquement après 5 appels de cette fonction récursive.

Voici une solution possible :

```js
let lastIntervalId, counter = 5;
const greeting = delay => {
  if (counter === 5) {
    clearInterval(lastIntervalId);
    lastIntervalId = setInterval(() => {
      console.log('Bonjour le monde. ', delay);
      greeting(delay + 100);
    }, delay);
    counter = 0;
  }
  counter += 1;
};
greeting(100);
```

Merci d'avoir lu.

Si vous commencez tout juste à apprendre Node.js, j'ai récemment publié un [cours de premiers pas sur Pluralsight](https://jscomplete.com/c/nodejs-getting-started), consultez-le :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OoRpYXrRivoSnQTscAjCMw.png)
_[https://jscomplete.com/c/nodejs-getting-started](https://jscomplete.com/c/nodejs-getting-started" rel="noopener" target="_blank" title=")_