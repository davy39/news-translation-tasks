---
title: J'ai trouvé un bug dans l'opérateur d'exponentiation de V8
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T14:35:08.000Z'
originalURL: https://freecodecamp.org/news/i-found-a-bug-in-v8s-exponentiation-operator-dcddfa5b8482
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c61X5rQY1EerMPy61Ud-ng.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: J'ai trouvé un bug dans l'opérateur d'exponentiation de V8
seo_desc: 'By Christoph Michel

  I always thought that the new ES6 exponentiation operator [x ** y](https://tc39.github.io/ecma262/#sec-exp-operator-runtime-semantics-evaluation)
  was the same as [Math.pow(x,y)](https://tc39.github.io/ecma262/#sec-math.pow).

  Indee...'
---

Par Christoph Michel

J'ai toujours pensé que le nouvel opérateur d'exponentiation ES6 `[x ** y](https://tc39.github.io/ecma262/#sec-exp-operator-runtime-semantics-evaluation)` était le même que `[Math.pow(x,y)](https://tc39.github.io/ecma262/#sec-math.pow)`.

En effet, c'est ce que dit [la spécification](https://tc39.github.io/ecma262/#sec-math.pow) à propos de `Math.pow` :

> Retourne le résultat de l'application de l'opérateur ** avec la base et l'exposant tels que spécifiés dans 12.6.4.

12.6.4 — *Application de l'opérateur *** indique que le résultat est *dépendant de l'implémentation* — mais il ne devrait toujours pas y avoir de divergence entre `**` et `Math.pow`.

Cependant, l'évaluation de ce qui suit dans le moteur JS V8 actuel (Chrome / Node) donne ceci :

```
console.log('1.35 ** 92', 1.35 ** 92)                   // 978828715394.7672console.log('Math.pow(1.35, 92)', Math.pow(1.35, 92))   // 978828715394.767
```

L'opérateur d'exponentiation `**` retourne une approximation plus précise.

Mais ce n'est pas la seule bizarrerie avec l'opérateur d'exponentiation : essayons d'évaluer la même chose avec des variables ([REPL](https://repl.it/@MrToph/ExponentiationBugs)) — cela ne devrait faire aucune différence :

![Image](https://cdn-media-1.freecodecamp.org/images/THt5NNcrKd1S9dd99OY4jUhPB0nw9wrHiY0K)

```
const exponent = 92;console.log(`1.35 ** exponent`, 1.35 ** exponent)                   // 978828715394.767console.log('1.35 ** 92', 1.35 ** 92)                               // 978828715394.7672console.log(`Math.pow(1.35, exponent)`, Math.pow(1.35, exponent))   // 978828715394.767console.log('Math.pow(1.35, 92)', Math.pow(1.35, 92))               // 978828715394.767
```

Mais cela en fait une : `1.35 ** 92` diffère de `1.35 ** exponent`.

Donc, ce qui semble se passer ici, c'est que le compilateur traite le code JS `1.35 ** 92` qui est déjà [constant folded](https://en.wikipedia.org/wiki/Constant_folding)

Cela a du sens car V8 compile vraiment en code machine.

**V8 améliore les performances en compilant JavaScript en code machine natif avant de l'exécuter, plutôt qu'en exécutant du bytecode ou en l'interprétant.**

V8 fonctionne d'abord en interprétant le code JS avec leur **Ignition Interpreter**. Il effectue une seconde passe avec le **TurboFan compiler** en [optimisant](https://v8project.blogspot.com/2017/05/launching-ignition-and-turbofan.html) le code machine.

![Image](https://cdn-media-1.freecodecamp.org/images/TyMWLEdnZyqL2oDHhD8mWqiYH0vsL6vgjp9J)
_De [Comprendre le bytecode de V8](https://medium.com/dailyjs/understanding-v8s-bytecode-317d46c94775" rel="noopener" target="_blank" title=")_

TurboFan effectue maintenant le **constant folding**. Son algorithme d'exponentiation a une meilleure précision que l'algorithme d'exponentiation du compilateur JIT (Ignition).

Si vous essayez la même chose dans d'autres moteurs JS comme _SpiderMonkey_ de Firefox, le résultat est une valeur cohérente de `978828715394.767` pour tous les calculs.

#### Est-ce un bug ?

Je dirais que oui, bien que ce ne soit pas grave dans mon code. Mais cela ne suit toujours pas la spécification qui dit que `Math.pow` et `**` devraient donner le même résultat.

Si vous transpilez le code avec Babel, `x ** y` est traduit en `Math.pow(x,y)`, ce qui entraîne à nouveau des divergences entre le code transpilé et non transpilé. Comme nous l'avons vu, `Math.pow(1.35, 92)` n'est **pas** optimisé (seuls les **opérateurs** semblent être optimisés par V8). Par conséquent, `1.35 ** 92` donne un résultat différent lorsqu'il est [transpilé en ES5](https://babeljs.io/repl/#?babili=false&browsers=&build=&builtIns=false&spec=false&loose=false&code_lz=IwOgzArABAVDUE4BMQ&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=true&fileSize=false&sourceType=module&lineWrap=false&presets=es2015%2Creact%2Cstage-2&prettier=false&targets=&version=6.26.0&envVersion=).

En utilisant ce bug et en ignorant toute pratique de code propre, nous pouvons écrire une belle fonction pour déterminer si nous exécutons Chrome (sauf si vous transpilez votre code ?) :

```
function isChrome() {    return 1.35 ** 92 !== Math.pow(1.35, 92)}
```

Toujours plus lisible que les chaînes d'agent utilisateur. ?

Publié à l'origine sur [cmichel.io](https://cmichel.io/bugs-in-exponentiation-operator/)

![Image](https://cdn-media-1.freecodecamp.org/images/9APsDGxF26LJJOgAusJLRrMPLw3zBSbLoP8u)