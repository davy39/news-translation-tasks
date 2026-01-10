---
title: Une introduction rapide à pipe() et compose() en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-10T02:30:12.000Z'
originalURL: https://freecodecamp.org/news/pipe-and-compose-in-javascript-5b04004ac937
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FKEc-DbmFn54VPLQmCOLRA.jpeg
tags:
- name: composition
  slug: composition
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Une introduction rapide à pipe() et compose() en JavaScript
seo_desc: 'By Yazeed Bzadough

  Functional programming’s been quite the eye-opening journey for me. This post, and
  posts like it, are an attempt to share my insights and perspectives as I trek new
  functional programming lands.

  Ramda’s been my go-to FP library bec...'
---

Par Yazeed Bzadough

La programmation fonctionnelle a été un véritable voyage révélateur pour moi. Cet article, et d'autres similaires, sont une tentative de partager mes insights et perspectives alors que j'explore de nouvelles terres de la programmation fonctionnelle.

[Ramda](http://ramdajs.com/) a été ma bibliothèque FP de prédilection grâce à la facilité avec laquelle elle permet de faire de la programmation fonctionnelle en JavaScript. Je la recommande vivement.

### Pipe

Le concept de `pipe` est simple — il combine `n` fonctions. C'est un pipe qui coule de gauche à droite, appelant chaque fonction avec la sortie de la précédente.

Écrivons une fonction qui retourne le `name` de quelqu'un.

```js
getName = (person) => person.name;

getName({ name: 'Buckethead' });
// 'Buckethead'
```

Écrivons une fonction qui met les chaînes de caractères en majuscules.

```js
uppercase = (string) => string.toUpperCase();

uppercase('Buckethead');
// 'BUCKETHEAD'
```

Donc, si nous voulions obtenir et capitaliser le `name` de `person`, nous pourrions faire ceci :

```js
name = getName({ name: 'Buckethead' });
uppercase(name);

// 'BUCKETHEAD'
```

C'est bien, mais éliminons cette variable intermédiaire `name`.

```js
uppercase(getName({ name: 'Buckethead' }));
```

Mieux, mais je n'aime pas cette imbrication. Cela peut devenir trop encombré. Et si nous voulons ajouter une fonction qui obtient les 6 premiers caractères d'une chaîne ?

```js
get6Characters = (string) => string.substring(0, 6);

get6Characters('Buckethead');
// 'Bucket'
```

Résultant en :

```js
get6Characters(uppercase(getName({ name: 'Buckethead' })));

// 'BUCKET';
```

Devenons un peu fous et ajoutons une fonction pour inverser les chaînes.

```js
reverse = (string) =>
  string
    .split('')
    .reverse()
    .join('');

reverse('Buckethead');
// 'daehtekcuB'
```

Maintenant nous avons :

```js
reverse(get6Characters(uppercase(getName({ name: 'Buckethead' }))));
// 'TEKCUB'
```

Cela peut devenir un peu... trop.

### Pipe à la rescousse !

Au lieu d'entasser des fonctions dans des fonctions ou de créer un tas de variables intermédiaires, utilisons `pipe` pour tout !

```js
pipe(
  getName,
  uppercase,
  get6Characters,
  reverse
)({ name: 'Buckethead' });
// 'TEKCUB'
```

De l'art pur. C'est comme une liste de tâches !

Parcourons cela étape par étape.

À des fins de démonstration, j'utiliserai une implémentation de `pipe` issue d'un des [articles sur la programmation fonctionnelle](https://medium.com/javascript-scene/reduce-composing-software-fe22f0c39a1d) de [Eric Elliott](https://medium.com/@_ericelliott).

```js
pipe = (...fns) => (x) => fns.reduce((v, f) => f(v), x);
```

J'adore cette petite ligne de code.

En utilisant les paramètres _rest_, [voir mon article à ce sujet](https://medium.com/@yazeedb/how-do-javascript-rest-parameters-actually-work-227726e16cc8), nous pouvons utiliser `pipe` avec `n` fonctions. Chaque fonction prend la sortie de la précédente et tout est _réduit_ en une seule valeur.

Et vous pouvez l'utiliser exactement comme nous l'avons fait ci-dessus.

```js
pipe(
  getName,
  uppercase,
  get6Characters,
  reverse
)({ name: 'Buckethead' });
// 'TEKCUB'
```

Je vais développer `pipe` et ajouter quelques instructions de débogage, et nous allons passer ligne par ligne.

```js
pipe = (...functions) => (value) => {
  debugger;

  return functions.reduce((currentValue, currentFunction) => {
    debugger;

    return currentFunction(currentValue);
  }, value);
};
```

![](https://cdn-media-1.freecodecamp.org/images/1*jqrKgVeO-raAUJjuN-adug.png)

Appelez `pipe` avec notre exemple et laissez les merveilles se déployer.

![](https://cdn-media-1.freecodecamp.org/images/1*rqi22p06rTtc2m0k1yHrRw.png)

Regardez les variables locales. `functions` est un tableau des 4 fonctions, et `value` est `{ name: 'Buckethead' }`.

Puisque nous avons utilisé les paramètres _rest_, `pipe` permet d'utiliser n'importe quel nombre de fonctions. Il va simplement boucler et appeler chacune d'elles.

![](https://cdn-media-1.freecodecamp.org/images/1*UjM5plW8s--8chfQQg3cMg.png)

Au prochain débogueur, nous sommes à l'intérieur de `reduce`. C'est ici que `currentValue` est passé à `currentFunction` et retourné.

Nous voyons que le résultat est `'Buckethead'` parce que `currentFunction` retourne la propriété `.name` de n'importe quel objet. Cela sera retourné dans `reduce`, ce qui signifie que cela devient le nouveau `currentValue` la prochaine fois. Appuyons sur le prochain débogueur et voyons.

![](https://cdn-media-1.freecodecamp.org/images/1*sEcE5tBFSpCzJZrKz8mmEQ.png)

Maintenant, `currentValue` est `'Buckethead'` parce que c'est ce qui a été retourné la dernière fois. `currentFunction` est `uppercase`, donc `'BUCKETHEAD'` sera le prochain `currentValue`.

![](https://cdn-media-1.freecodecamp.org/images/1*Va6taGFU8dSyhz1wLVMWMQ.png)

Même idée, prenez les 6 premiers caractères de `'BUCKETHEAD'` et passez-les à la fonction suivante.

![](https://cdn-media-1.freecodecamp.org/images/1*YaI1oxsZW5qZZUC146DYoQ.png)

`reverse('BUCKET')`

![](https://cdn-media-1.freecodecamp.org/images/1*moIMQxr82r2Z8IuXwuZfKQ.png)

Et c'est terminé !

### Et compose() ?

C'est simplement `pipe` dans l'autre direction.

Donc, si vous vouliez le même résultat que notre `pipe` ci-dessus, vous feriez l'inverse.

```js
compose(
  reverse,
  get6Characters,
  uppercase,
  getName
)({ name: 'Buckethead' });
```

Remarquez comment `getName` est le dernier dans la chaîne et `reverse` est le premier ?

Voici une implémentation rapide de `compose`, encore une fois grâce au magique [Eric Elliott](https://medium.com/@_ericelliott), issue [du même article](https://medium.com/javascript-scene/reduce-composing-software-fe22f0c39a1d).

```js
compose = (...fns) => (x) => fns.reduceRight((v, f) => f(v), x);
```

Je vous laisse le soin de développer cette fonction avec des `debugger`s comme exercice. Amusez-vous avec, utilisez-la, appréciez-la. Et surtout, amusez-vous !