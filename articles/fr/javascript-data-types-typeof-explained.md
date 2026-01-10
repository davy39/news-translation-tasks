---
title: 'Types de données JavaScript : Typeof expliqué'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-23T23:54:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-data-types-typeof-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e80740569d1a4ca3d75.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: 'Types de données JavaScript : Typeof expliqué'
seo_desc: 'typeof is a JavaScript keyword that will return the type of a variable
  when you call it. You can use this to validate function parameters or check if variables
  are defined. There are other uses as well.

  The typeof operator is useful because it is an ...'
---

`typeof` est un mot-clé JavaScript qui retourne le type d'une variable lorsque vous l'appelez. Vous pouvez l'utiliser pour valider les paramètres de fonction ou vérifier si des variables sont définies. Il y a d'autres utilisations également.

L'opérateur `typeof` est utile car c'est un moyen facile de vérifier le type d'une variable dans votre code. Cela est important car JavaScript est un [langage à typage dynamique](https://stackoverflow.com/questions/2690544/what-is-the-difference-between-a-strongly-typed-language-and-a-statically-typed). Cela signifie que vous n'êtes pas obligé d'assigner des types aux variables lorsque vous les créez. Parce qu'une variable n'est pas restreinte de cette manière, son type peut changer pendant l'exécution d'un programme.

Par exemple :

```javascript
var x = 12345; // number
x = 'string'; // string
x = { key: 'value' }; // object
```

Comme vous pouvez le voir dans l'exemple ci-dessus, une variable en JavaScript peut changer de type tout au long de l'exécution d'un programme. Cela peut être difficile à suivre en tant que programmeur, et c'est là que l'opérateur `typeof` est utile.

L'opérateur `typeof` retourne une chaîne qui représente le type actuel d'une variable. Vous l'utilisez en tapant `typeof(variable)` ou `typeof variable`. En revenant à l'exemple précédent, vous pouvez l'utiliser pour vérifier le type de la variable `x` à chaque étape :

```javascript
var x = 12345; 
console.log(typeof x) // number
x = 'string'; 
console.log(typeof x) // string
x = { key: 'value' };
console.log(typeof x) // object
```

Cela peut être utile pour vérifier le type d'une variable dans une fonction et continuer de manière appropriée.

Voici un exemple de fonction qui peut prendre une variable qui est une chaîne ou un nombre :

```javascript
function doSomething(x) {
  if(typeof(x) === 'string') {
    alert('x est une chaîne')
  } else if(typeof(x) === 'number') {
    alert('x est un nombre')
  }
}
```

Une autre façon dont l'opérateur `typeof` peut être utile est de s'assurer qu'une variable est définie avant d'essayer d'y accéder dans votre code. Cela peut aider à prévenir les erreurs dans un programme qui peuvent se produire si vous essayez d'accéder à une variable qui n'est pas définie.

```javascript
function(x){
  if (typeof(x) === 'undefined') {
    console.log('la variable x n\'est pas définie');
    return;
  }
  // continuer avec la fonction ici...
}
```

La sortie de l'opérateur `typeof` peut ne pas toujours être ce à quoi vous vous attendez lorsque vous vérifiez un nombre. Les nombres peuvent devenir la valeur [NaN (Not A Number)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN) pour plusieurs raisons.

```javascript
console.log(typeof NaN); //"number"
```

Peut-être avez-vous essayé de multiplier un nombre avec un objet parce que vous avez oublié d'accéder au nombre à l'intérieur de l'objet.

```javascript
var x = 1;
var y = { number: 2 };
console.log(x * y); // NaN
console.log(typeof (x * y)); // number
```

Lorsque vous vérifiez un nombre, il n'est pas suffisant de vérifier la sortie de `typeof` pour un nombre, puisque `NaN` passe également ce test. Cette fonction vérifie les nombres et n'autorise pas non plus la valeur `NaN` à passer.

```javascript
function isNumber(data) {
  return (typeof data === 'number' && !isNan(data));
}
```

Même si c'est une méthode de validation utile, nous devons être prudents car JavaScript a quelques parties étranges et l'une d'entre elles est le résultat de `typeof` sur certaines instructions. Par exemple, en JavaScript, beaucoup de choses sont simplement des `objects`, donc vous trouverez.

```javascript
var x = [1,2,3,4]; 
console.log(typeof x)  // object

console.log(typeof null)  // object
```