---
title: Fonctions pures vs impures en programmation fonctionnelle – Quelle est la différence
  ?
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2021-08-09T21:06:46.000Z'
originalURL: https://freecodecamp.org/news/pure-function-vs-impure-function
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pure-function-vs-impure-function-codesweetly.png
tags:
- name: Functional Programming
  slug: functional-programming
seo_title: Fonctions pures vs impures en programmation fonctionnelle – Quelle est
  la différence ?
seo_desc: 'Pure functions and impure functions are two programming terms you will
  often see in functional programming.

  One core difference between these two types of functions is whether or not they
  have side effects.

  In this article, you will learn what side e...'
---

Les fonctions pures et les fonctions impures sont deux termes de programmation que vous verrez souvent en programmation fonctionnelle.

Une différence fondamentale entre ces deux types de fonctions est qu'elles ont ou non des effets de bord.

Dans cet article, vous apprendrez ce que sont les effets de bord et nous discuterons des différences entre les fonctions pures et impures.

Sans plus attendre, commençons par les effets de bord.

## Qu'est-ce qu'un effet de bord ?

Un **effet de bord** se produit dans un programme chaque fois que vous utilisez du _code externe_ dans votre fonction — ce qui, par conséquent, impacte la capacité de la fonction à accomplir sa tâche.

Alors, que signifie exactement cela ? Voyons cela avec quelques exemples.

### Exemple d'effet de bord 1 : Comment ajouter une ancienne valeur à une nouvelle

```js
let oldDigit = 5;

function addNumber(newValue) {
  return oldDigit += newValue;
}
```

Dans l'extrait ci-dessus, l'utilisation de `oldDigit` dans la fonction donne à `addNumber()` les effets de bord suivants :

#### Premier effet de bord : Dépendance à oldDigit

Le fait que `addNumber()` dépende de `oldDigit` pour accomplir ses tâches signifie que chaque fois que `oldDigit` n'est pas disponible (ou `undefined`), `addNumber()` retournera une erreur.

#### Deuxième effet de bord : Modifie le code externe

Comme `addNumber()` est programmée pour muter l'[état](https://www.codesweetly.com/state-in-programming/) de `oldDigit`, cela implique que `addNumber()` a un effet de bord de manipulation de certains codes externes.

#### Troisième : Devient une fonction non déterministe

L'utilisation de code externe dans `addNumber()` en fait une fonction non déterministe — car vous ne pouvez jamais déterminer sa sortie en la lisant uniquement.

En d'autres termes, pour être sûr de la valeur de retour de `addNumber()`, vous devez considérer d'autres facteurs externes — tels que l'état actuel de `oldDigit`.

Par conséquent, `addNumber()` n'est pas indépendante — elle a toujours des attaches.

### Exemple d'effet de bord 2 : Comment imprimer du texte dans votre console

```js
function printName() {
  console.log("Mon nom est Oluwatobi Sofela.");
}
```

Dans l'extrait ci-dessus, l'utilisation de `console.log()` dans `printName()` donne à la fonction des effets de bord.

#### Comment console.log provoque-t-il des effets de bord dans une fonction ?

Un `console.log()` provoque des effets de bord dans une fonction parce qu'il affecte l'état du code externe — c'est-à-dire, l'état de l'[objet console](https://developer.mozilla.org/en-US/docs/Web/API/console).

En d'autres termes, `console.log()` instructe l'ordinateur de modifier l'état de l'objet `console`.

Ainsi, lorsque vous l'utilisez dans une fonction, cela amène cette fonction à :

1. Être dépendante de l'objet `console` pour accomplir son travail efficacement.
2. Modifier l'état d'un code externe (c'est-à-dire, l'état de l'objet `console`).
3. Devenir non déterministe — car vous devez maintenant considérer l'état de la `console` pour être sûr de la sortie de la fonction.

Par conséquent, chaque fois que vous utilisez du _code externe_ dans votre fonction, ce code provoquera des **effets de bord**.

Alors, comment les effets de bord se rapportent-ils aux fonctions pures et impures ?

Découvrons-le en regardant la définition d'une fonction pure et son alternative impure.

## Qu'est-ce qu'une fonction impure ?

Maintenant que nous savons ce que sont les effets de bord dans les fonctions, nous pouvons parler des fonctions impures (et pures).

Tout d'abord, une **fonction impure** est une fonction qui contient un ou plusieurs effets de bord.

Considérez le code JavaScript ci-dessous :

```js
const myNames = ["Oluwatobi", "Sofela"];

function updateMyName(newName) {
  myNames.push(newName);
  return myNames;
}
```

Dans l'extrait ci-dessus, `updateMyName()` est une fonction impure parce qu'elle contient du code (`myNames`) qui mute un état [externe](https://www.codesweetly.com/state-in-programming/) — ce qui donne à `updateMyName()` quelques effets de bord.

## Qu'est-ce qu'une fonction pure ?

Une **fonction pure** est une fonction sans aucun effet de bord.

Considérez le code JavaScript ci-dessous :

```js
function updateMyName(newName) {
   const myNames = ["Oluwatobi", "Sofela"];
   myNames[myNames.length] = newName;
   return myNames;
}
```

Dans l'extrait ci-dessus, remarquez que `updateMyName()` ne dépend d'aucun code externe pour accomplir ses tâches. Cela en fait une _fonction pure_.

Là où c'est possible, vous devriez utiliser des fonctions pures dans vos applications. Discutons de quelques avantages que vous obtenez en faisant cela.

## Avantages des fonctions pures

Voici quelques avantages des fonctions pures.

### Les fonctions pures sont indépendantes

Les fonctions pures n'affectent aucun état externe, et elles ne sont pas non plus affectées par du code externe.

En d'autres termes, toutes les données externes qu'une fonction pure utilise sont reçues en tant que paramètres — elles ne sont pas _utilisées explicitement en interne_.

Par conséquent, ce que vous voyez à l'intérieur est ce que vous obtenez — il n'y a absolument aucune attache.

Ainsi, vous n'avez pas besoin de chercher des conditions externes (états) qui pourraient impacter le fonctionnement efficace de votre fonction pure, car toutes les activités se passent à l'intérieur.

### Les fonctions pures sont plus faciles à lire

Les fonctions pures sont plus faciles à lire et à déboguer que leurs alternatives impures.

Les fonctions pures sont si lisibles parce qu'elles dépendent uniquement d'elles-mêmes — elles n'affectent pas et ne sont pas impactées par des états externes.

## Choses importantes à savoir sur les fonctions pures

Gardez ces trois informations essentielles à l'esprit chaque fois que vous choisissez d'utiliser des fonctions pures.

### Vous pouvez cloner un état externe dans une fonction pure

Cloner un état externe dans une fonction pure ne rend pas la fonction impure.

La duplication d'état est simplement une opération de copier-coller qui ne laisse aucune attache entre la source et son clone.

**Exemple :**

```js
const myBio = ["Oluwatobi", "Sofela"];

function updateMyBio(newBio, array) {
  const clonedBio = [...array];
  clonedBio[clonedBio.length] = newBio;
  return clonedBio;
}

console.log(updateMyBio("codesweetly.com", myBio));
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-blhtpi?file=script.js)

Dans l'extrait ci-dessus, `updateMyBio()` a utilisé l'[opérateur de décomposition](https://www.codesweetly.com/spread-operator/) pour dupliquer l'état de `myBio` dans `clonedBio`. Cependant, c'est toujours une fonction pure parce qu'elle ne dépend pas de `myBio` et ne modifie aucun code externe.

Au lieu de cela, c'est une fonction exclusivement déterministe programmée pour utiliser la version clonée de son paramètre de tableau.

### Évitez les mutations de code dans les fonctions pures

Techniquement, vous pouvez muter des variables définies localement dans la portée d'une fonction pure. Cependant, il est préférable d'éviter de le faire.

Par exemple, considérons le code ci-dessous :

```js
const compBio = ["code", "sweetly"];

function updateCompBio(newBio, array) {
  const clonedBio = [...array];
  clonedBio[clonedBio.length] = newBio;
  return clonedBio;
}

console.log(updateCompBio(".com", compBio));
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-dprdlf?file=script.js)

Dans l'extrait ci-dessus, `updateCompBio()` est une fonction pure qui utilise `clonedBio[clonedBio.length] = newBio` pour altérer son état local.

Bien qu'une telle opération ne rende pas `updateCompBio()` impure, ce n'est pas la meilleure pratique.

La manière recommandée d'écrire une fonction pure est de la faire recevoir _toutes_ ses valeurs en tant que paramètres comme suit :

```js
const compBio = ["code", "sweetly"];

function updateCompBio(newBio, array) {
  return [...array, newBio];
}

console.log(updateCompBio(".com", compBio));
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-gyl8sy?file=script.js)

Remarquez à quel point notre code est maintenant propre et portable. C'est un avantage de faire en sorte que votre fonction pure reçoive toutes ses valeurs en tant que paramètres. En faisant cela, vous trouverez également plus facile de déboguer votre code.

### La même entrée retournera toujours la même sortie

Un trait vital des fonctions pures est qu'elles retourneront toujours la même valeur avec le même ensemble d'entrées — peu importe le nombre de fois que vous les invoquez.

## Conclusion

Votre fonction est **pure** si elle ne contient aucun code externe. Sinon, elle est **impure** si elle inclut un ou plusieurs effets de bord.

Dans cet article, nous avons discuté de ce que sont les fonctions pures et impures, et nous avons appris les avantages que l'utilisation de fonctions pures peut apporter à votre code.

Merci d'avoir lu !