---
title: Comprendre en profondeur le Currying en 7 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T11:45:00.000Z'
originalURL: https://freecodecamp.org/news/deeply-understand-currying-in-7-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/snape-currying-in-7-minutes.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Ramda
  slug: ramda
- name: React
  slug: react
seo_title: Comprendre en profondeur le Currying en 7 minutes
seo_desc: 'By Yazeed Bzadough

  Eric Elliott’s exceptional Composing Software series is initially what got me excited
  about functional programming. It''s a must-read.

  At one point in the series, he mentioned currying. Both computer science and mathematics
  agree on...'
---

Par Yazeed Bzadough

La série exceptionnelle [Composing Software](https://medium.com/javascript-scene/the-rise-and-fall-and-rise-of-functional-programming-composable-software-c2d91b424c8c) d'Eric Elliott est ce qui m'a initialement excité au sujet de la programmation fonctionnelle. C'est une lecture incontournable.

À un moment donné dans la série, il a mentionné le _currying_. L'informatique et les mathématiques s'accordent sur la définition :

> Le currying transforme les fonctions à plusieurs arguments en fonctions unaires (à un seul argument).

Les fonctions curryfiées prennent de nombreux arguments **un à la fois**. Donc, si vous avez

```js
greet = (greeting, first, last) => `${greeting}, ${first} ${last}`;

greet('Hello', 'Bruce', 'Wayne'); // Hello, Bruce Wayne
```

Le currying de `greet` vous donne

```js
curriedGreet = curry(greet);

curriedGreet('Hello')('Bruce')('Wayne'); // Hello, Bruce Wayne
```

Cette fonction à 3 arguments a été transformée en trois fonctions unaires. Au fur et à mesure que vous fournissez un paramètre, une nouvelle fonction apparaît, attendant le suivant.

![dog-properly-currying-a-function-1](https://www.freecodecamp.org/news/content/images/2019/07/dog-properly-currying-a-function-1.jpeg)

## Correctement ?

Je dis "correctement curryfié" car certaines fonctions `curry` sont plus flexibles dans leur utilisation. Le currying est génial en théorie, mais invoquer une fonction pour chaque argument devient fatigant en JavaScript.

La fonction `curry` de [Ramda](https://ramdajs.com/) vous permet d'invoquer `curriedGreet` comme ceci :

```js
// greet nécessite 3 params : (greeting, first, last)

// ceux-ci retournent tous une fonction cherchant (first, last)
curriedGreet('Hello');
curriedGreet('Hello')();
curriedGreet()('Hello')()();

// ceux-ci retournent tous une fonction cherchant (last)
curriedGreet('Hello')('Bruce');
curriedGreet('Hello', 'Bruce');
curriedGreet('Hello')()('Bruce')();

// ceux-ci retournent une salutation, puisque les 3 params ont été fournis
curriedGreet('Hello')('Bruce')('Wayne');
curriedGreet('Hello', 'Bruce', 'Wayne');
curriedGreet('Hello', 'Bruce')()()('Wayne');
```

Remarquez que vous pouvez choisir de donner plusieurs arguments en une seule fois. Cette implémentation est plus utile lors de l'écriture de code.

Et comme démontré ci-dessus, vous pouvez invoquer cette fonction indéfiniment sans paramètres et elle retournera toujours une fonction qui attend les paramètres restants.

## Comment est-ce possible ?

M. Elliot a partagé une implémentation de `curry` très similaire à celle de Ramda. Voici le code, ou comme il l'a aptement appelé, un sortilège magique :

```js
const curry = (f, arr = []) => (...args) =>
  ((a) => (a.length === f.length ? f(...a) : curry(f, a)))([...arr, ...args]);
```

## Euh... ?

![that-code-is-hard-to-read-cmm](https://www.freecodecamp.org/news/content/images/2019/07/that-code-is-hard-to-read-cmm.jpeg)

Oui, je sais... C'est incroyablement concis, alors refactorisons et apprécions-le ensemble.

## Cette version fonctionne de la même manière

J'ai également ajouté des instructions `debugger` pour l'examiner dans les outils de développement Chrome.

```js
curry = (originalFunction, initialParams = []) => {
  debugger;

  return (...nextParams) => {
    debugger;

    const curriedFunction = (params) => {
      debugger;

      if (params.length === originalFunction.length) {
        return originalFunction(...params);
      }

      return curry(originalFunction, params);
    };

    return curriedFunction([...initialParams, ...nextParams]);
  };
};
```

Ouvrez vos [Outils de développement](https://developers.google.com/web/tools/chrome-devtools/) et suivez le guide !

## C'est parti !

Collez `greet` et `curry` dans votre console. Ensuite, entrez `curriedGreet = curry(greet)` et commencez la folie.

### Pause à la ligne 2

![](https://cdn-media-1.freecodecamp.org/images/1*8_q3YkOu6fDzIEMY65lqUg.png)

En inspectant nos deux paramètres, nous voyons que `originalFunction` est `greet` et que `initialParams` est par défaut un tableau vide car nous ne l'avons pas fourni. Passez au point d'arrêt suivant et, oh attendez... c'est tout.

Oui ! `curry(greet)` retourne simplement une nouvelle fonction qui attend 3 paramètres supplémentaires. Tapez `curriedGreet` dans la console pour voir ce que je veux dire.

Lorsque vous avez fini de jouer avec cela, devenons un peu plus fous et faisons `sayHello = curriedGreet('Hello')`.

### Pause à la ligne 4

![](https://cdn-media-1.freecodecamp.org/images/1*FXCJQi5Numlbis5d_bGsjw.png)

Avant de continuer, tapez `originalFunction` et `initialParams` dans votre console. Remarquez que nous pouvons toujours accéder à ces 2 paramètres même si nous sommes dans une fonction complètement nouvelle ? C'est parce que les fonctions retournées par les fonctions parent bénéficient de la portée de leur parent.

#### Héritage dans la vraie vie

Après qu'une fonction parent a disparu, elle laisse ses paramètres pour que ses enfants les utilisent. Un peu comme l'héritage dans le sens de la vraie vie.

`curry` a initialement reçu `originalFunction` et `initialParams`, puis a retourné une fonction "enfant". Ces 2 variables n'ont pas encore été [éliminées](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management) car peut-être que cet enfant en a besoin. S'il n'en a pas besoin, _alors_ cette portée est nettoyée car lorsque personne ne vous référence, c'est à ce moment-là que vous mourez vraiment.

### OK, retour à la ligne 4...

![](https://cdn-media-1.freecodecamp.org/images/1*_TFVnxtqgisi1i0q_K3dUQ.png)

Inspectez `nextParams` et voyez que c'est `['Hello']`... un tableau ? Mais je pensais que nous avions dit `curriedGreet('Hello')`, pas `curriedGreet(['Hello'])` !

Correct : nous avons invoqué `curriedGreet` avec `'Hello'`, mais grâce à la [syntaxe rest](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator#Rest_syntax_%28parameters%29), nous avons _transformé_ `'Hello'` en `['Hello']`.

### POURQUOI ?!

`curry` est une fonction générale qui peut recevoir 1, 10 ou 10 000 000 de paramètres, donc elle a besoin d'un moyen de référencer tous ces paramètres. L'utilisation de la syntaxe rest de cette manière capture chaque paramètre dans un seul tableau, rendant le travail de `curry` beaucoup plus facile.

Passons au prochain `debugger`.

### Ligne 6 maintenant, mais attendez.

Vous avez peut-être remarqué que la ligne 12 s'est en fait exécutée avant l'instruction `debugger` de la ligne 6. Si ce n'est pas le cas, regardez de plus près. Notre programme définit une fonction appelée `curriedFunction` à la ligne 5, l'utilise à la ligne 12, et _ensuite_ nous atteignons cette instruction `debugger` à la ligne 6. Et avec quoi `curriedFunction` est-elle invoquée ?

```js
[...initialParams, ...nextParams];
```

Yuuuup. Regardez `params` à la ligne 5 et vous verrez `['Hello']`. `initialParams` et `nextParams` étaient tous deux des tableaux, donc nous les avons aplatis et combinés en un seul tableau en utilisant l'opérateur de propagation pratique [spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator#Syntax).

C'est là que les bonnes choses se passent.

![](https://cdn-media-1.freecodecamp.org/images/1*pM31i2QVNxVUiqj9aZzVvg.png)

La ligne 7 dit "Si `params` et `originalFunction` ont la même longueur, appelez `greet` avec nos paramètres et nous avons terminé." Ce qui me rappelle...

### Les fonctions JavaScript ont aussi des longueurs

C'est ainsi que `curry` fait sa magie ! C'est ainsi qu'il décide s'il doit demander plus de paramètres ou non.

En JavaScript, la propriété `.length` d'une fonction vous indique _combien d'arguments elle attend_.

```js
greet.length; // 3

iTakeOneParam = (a) => {};
iTakeTwoParams = (a, b) => {};

iTakeOneParam.length; // 1
iTakeTwoParams.length; // 2
```

Si nos paramètres fournis et attendus correspondent, tout va bien, il suffit de les transmettre à la fonction originale et de terminer le travail !

### C'est génial ?

Mais dans notre cas, les paramètres et la longueur de la fonction ne sont _pas_ les mêmes. Nous n'avons fourni que `'Hello'`, donc `params.length` est 1, et `originalFunction.length` est 3 car `greet` attend 3 paramètres : `greeting, first, last`.

### Alors, que se passe-t-il ensuite ?

Eh bien, puisque cette instruction `if` évalue à `false`, le code passera à la ligne 10 et réinvoquera notre fonction maître `curry`. Elle reçoit à nouveau `greet` et cette fois, `'Hello'`, et recommence toute la folie.

C'est de la [récursion](https://developer.mozilla.org/en-US/docs/Glossary/Recursion), mes amis.

`curry` est essentiellement une boucle infinie de fonctions auto-appelantes, affamées de paramètres, qui ne se reposeront pas jusqu'à ce que leur invité soit rassasié. L'hospitalité à son meilleur.

![](https://cdn-media-1.freecodecamp.org/images/1*AZKiupYSanV5iJSQWrtUwg.png)

### Retour à la ligne 2

Les mêmes paramètres qu'avant, sauf que `initialParams` est `['Hello']` cette fois. Passez à nouveau pour sortir du cycle. Tapez notre nouvelle variable dans la console, `sayHello`. C'est une autre fonction, attendant toujours plus de paramètres, mais nous nous rapprochons...

Augmentons la chaleur avec `sayHelloToJohn = sayHello('John')`.

Nous sommes à nouveau à l'intérieur de la ligne 4, et `nextParams` est `['John']`. Passez au prochain debugger à la ligne 6 et inspectez `params` : c'est `['Hello', 'John']` ! ?

![](https://cdn-media-1.freecodecamp.org/images/1*pej6yZ-vGvA2T9LgIIc-vg.png)

### Pourquoi, pourquoi, pourquoi ?

Parce que, rappelez-vous, la ligne 12 dit "Hey `curriedFunction`, il m'a donné `'Hello'` la dernière fois et `'John'` cette fois. Prends-les tous les deux dans ce tableau `[...initialParams, ...nextParams]`."

![](https://cdn-media-1.freecodecamp.org/images/1*Ljvk2BMLxIsbJ09idgStdg.png)

Maintenant, `curriedFunction` compare à nouveau la `length` de ces `params` à `originalFunction`, et puisque `2 < 3`, nous passons à la ligne 10 et appelons `curry` une fois de plus ! Et bien sûr, nous transmettons `greet` et nos 2 params, `['Hello', 'John']`

![](https://cdn-media-1.freecodecamp.org/images/1*EYv9jdo2id8tynbTI5SXYQ.png)

Nous sommes si proches, terminons cela et récupérons la salutation complète !

`sayHelloToJohnDoe = sayHelloToJohn('Doe')`

Je pense que nous savons ce qui se passe ensuite.

![](https://cdn-media-1.freecodecamp.org/images/1*tMJvls2j9eAjrCGykVN84g.png)![](https://cdn-media-1.freecodecamp.org/images/1*NHm1TMo8Tjk7jQVlGGa9zQ.png)![](https://cdn-media-1.freecodecamp.org/images/1*eTwjEYLKGCGJoqdP4Xe9hA.png)

## Le travail est terminé

`greet` a obtenu ses paramètres, `curry` a arrêté de boucler, et nous avons reçu notre salutation : `Hello, John Doe`.

Jouez un peu plus avec cette fonction. Essayez de fournir plusieurs paramètres ou aucun en une seule fois, devenez aussi fou que vous le souhaitez. Voyez combien de fois `curry` doit recourir avant de retourner la sortie attendue.

```js
curriedGreet('Hello', 'John', 'Doe');
curriedGreet('Hello', 'John')('Doe');
curriedGreet()()('Hello')()('John')()()()()('Doe');
```

Un grand merci à [Eric Elliott](https://medium.com/@_ericelliott) pour m'avoir introduit à cela, et encore plus de remerciements à vous pour avoir apprécié `curry` avec moi. À la prochaine fois !

_Pour plus de contenu comme celui-ci, consultez <a href="https://yazeedb.com">yazeedb.com</a> !_