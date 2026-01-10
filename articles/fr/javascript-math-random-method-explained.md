---
title: Méthode JavaScript Math.random() Expliquée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-25T21:46:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-math-random-method-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d8c740569d1a4ca3853.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
- name: toothbrush
  slug: toothbrush
seo_title: Méthode JavaScript Math.random() Expliquée
seo_desc: 'Random Method

  The JavaScript Math.random() method is an excellent built-in method for producing
  random numbers. When Math.random() is executed, it returns a random number that
  can be anywhere between 0 and 1. The 0 is included and 1 is excluded.

  Gene...'
---

## **Méthode Random**

La méthode `Math.random()` de JavaScript est une excellente méthode intégrée pour produire des nombres aléatoires. Lorsque `Math.random()` est exécutée, elle retourne un nombre aléatoire qui peut être compris entre 0 et 1. Le 0 est inclus et 1 est exclu.

## Générer un nombre à virgule flottante aléatoire entre 0 et 1

La méthode `Math.random()` retournera un nombre à virgule flottante (décimal) supérieur ou égal à 0 et inférieur à (mais jamais égal à) 1. En d'autres termes, `0 <= x < 1`. Par exemple :

```javascript
console.log(Math.random());
// 0.7069207248635578

console.log(Math.random());
// 0.765046694794209

console.log(Math.random());
// 0.14069121642698246
```

(Bien sûr, les nombres retournés seront différents à chaque fois. Cela sera supposé pour tous les exemples suivants - différents résultats se produiront à chaque passage.)

Pour obtenir un nombre aléatoire dans une plage plus grande, multipliez le résultat de `Math.random()` par un nombre.

## Générer un nombre à virgule flottante aléatoire entre 0 et un maximum spécifié

Habituellement, vous n'avez pas besoin de nombres aléatoires entre 0 et 1 - vous avez besoin de nombres plus grands ou même d'entiers.

Par exemple, si vous voulez un nombre à virgule flottante aléatoire entre 0 et 10, vous pourriez utiliser :

```javascript
var x = Math.random()*10;

console.log(x);
// 4.133793901445541
```

## Générer un nombre à virgule flottante aléatoire dans une plage

Si vous avez besoin d'un nombre à virgule flottante aléatoire qui se situe entre deux nombres spécifiques, vous pourriez faire quelque chose comme ceci :

```javascript
var min = 83.1;
var max = 193.36;

var x = Math.random()*(max - min)+min;

console.log(x);
// 126.94014012699063
```

## Générer un entier aléatoire entre 0 et un maximum

Souvent, vous avez besoin d'entiers. Pour cela, vous devrez utiliser d'autres méthodes de l'objet `Math`, `Math.floor()` (arrondit à l'entier inférieur le plus proche) et `Math.ceil()` (arrondit à l'entier supérieur le plus proche).

Par exemple, si vous devez sélectionner aléatoirement dans un tableau de 10 éléments, vous aurez besoin d'un nombre aléatoire entre 0 et 9 inclus (n'oubliez pas que les tableaux sont indexés à partir de zéro).

```javascript
var x = Math.floor(Math.random()*10);

console.log(x);
// 7
```

(Rappelez-vous que `Math.random()` ne retournera jamais exactement 1, donc `Math.random()*10` ne retournera jamais exactement 10. Cela signifie qu'après l'arrondi à l'entier inférieur, le résultat sera toujours 9 ou moins.)

## Générer un entier aléatoire entre 1 et un maximum

Si vous avez besoin d'un nombre aléatoire avec le nombre minimum étant 1 (par exemple, choisir un jour aléatoire en janvier), vous pourriez utiliser la méthode `Math.ceil()`.

```javascript
var x = Math.ceil(Math.random()*31);

console.log(x);
// 23
```

Une autre façon aurait été d'utiliser la fonction précédente (en utilisant `Math.floor()`) et d'ajouter 1 :

```javascript
var x = Math.floor(Math.random()*31)+1;

console.log(x);
// 17
```

## Générer un entier aléatoire dans une plage

Enfin, occasionnellement, vous avez besoin d'un entier aléatoire entre deux entiers spécifiques. Par exemple, si vous essayez de choisir des billets de tombola et que vous connaissez les numéros les plus bas et les plus élevés :

```javascript
var min = 1718;
var max = 3429;

var x = Math.floor(Math.random()*(max-min+1)+min);

console.log(x);
//2509
```

## À quel point Math.random() est-il aléatoire ?

Il peut être souligné que le nombre retourné par `Math.random()` est un nombre pseudo-aléatoire, car aucun ordinateur ne peut générer un nombre vraiment aléatoire, qui présente une aléatoire sur toutes les échelles et sur toutes les tailles de jeux de données. Cependant, le nombre pseudo-aléatoire généré par `Math.random()` est généralement suffisant pour les besoins de presque tous les programmes que vous pourriez écrire. Le manque de véritable aléatoire ne devient apparent que dans des jeux de nombres astronomiquement grands ou lorsque des décimales d'une précision inhabituelle sont nécessaires.