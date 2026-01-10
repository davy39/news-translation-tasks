---
title: Qu'est-ce qu'une fonction de rappel (Callback) en JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-14T23:50:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-callback-function-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9eb0740569d1a4ca3e8d.jpg
tags:
- name: callbacks
  slug: callbacks
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce qu'une fonction de rappel (Callback) en JavaScript ?
seo_desc: 'This article gives a brief introduction to the concept and usage of callback
  functions in the JavaScript programming language.

  Functions are Objects

  The first thing we need to know is that in Javascript, functions are first-class
  objects. As such, we...'
---

Cet article donne une brève introduction au concept et à l'utilisation des fonctions de rappel (callback) dans le langage de programmation JavaScript.

## **Les fonctions sont des objets**

La première chose que nous devons savoir est qu'en JavaScript, les fonctions sont des objets de première classe. Ainsi, nous pouvons travailler avec elles de la même manière que nous travaillons avec d'autres objets, comme les assigner à des variables et les passer en tant qu'arguments à d'autres fonctions. Cela est important, car c'est cette dernière technique qui nous permet d'étendre la fonctionnalité dans nos applications.

## **Fonctions de rappel (Callback)**

Une **fonction de rappel** est une fonction qui est passée _en tant qu'argument_ à une autre fonction, pour être "rappelée" plus tard. Une fonction qui accepte d'autres fonctions comme arguments est appelée une **fonction d'ordre supérieur**, qui contient la logique pour _quand_ la fonction de rappel est exécutée. C'est la combinaison de ces deux éléments qui nous permet d'étendre notre fonctionnalité.

Pour illustrer les fonctions de rappel, commençons par un exemple simple :

```javascript
function createQuote(quote, callback){ 
  var myQuote = "Comme je le dis toujours, " + quote;
  callback(myQuote); // 2
}

function logQuote(quote){
  console.log(quote);
}

createQuote("mangez vos légumes !", logQuote); // 1

// Résultat dans la console :
// Comme je le dis toujours, mangez vos légumes !
```

Dans l'exemple ci-dessus, `createQuote` est la fonction d'ordre supérieur, qui accepte deux arguments, le second étant la fonction de rappel. La fonction `logQuote` est utilisée comme notre fonction de rappel. Lorsque nous exécutons la fonction `createQuote` _(1)_, remarquez que nous n'ajoutons _pas_ de parenthèses à `logQuote` lorsque nous la passons en tant qu'argument. Cela est dû au fait que nous ne voulons pas exécuter notre fonction de rappel immédiatement, nous voulons simplement passer la définition de la fonction à la fonction d'ordre supérieur afin qu'elle puisse être exécutée plus tard.

De plus, nous devons nous assurer que si la fonction de rappel que nous passons attend des arguments, nous fournissons ces arguments lors de l'exécution de la fonction de rappel _(2)_. Dans l'exemple ci-dessus, ce serait l'instruction `callback(myQuote);` puisque nous savons que `logQuote` attend qu'une citation soit passée.

En outre, nous pouvons passer des fonctions anonymes comme fonctions de rappel. L'appel suivant à `createQuote` aurait le même résultat que l'exemple ci-dessus :

```javascript
createQuote("mangez vos légumes !", function(quote){ 
  console.log(quote); 
});
```

Accessoirement, vous n'êtes _pas obligé_ d'utiliser le mot "callback" comme nom de votre argument, JavaScript a simplement besoin de savoir que c'est le nom correct de l'argument. Basé sur l'exemple ci-dessus, la fonction ci-dessous se comportera de manière exactement identique.

```javascript
function createQuote(quote, functionToCall) { 
  var myQuote = "Comme je le dis toujours, " + quote;
  functionToCall(myQuote);
}
```

## **Pourquoi utiliser les fonctions de rappel ?**

La plupart du temps, nous créons des programmes et des applications qui fonctionnent de manière **synchrone**. En d'autres termes, certaines de nos opérations ne commencent que lorsque les précédentes ont été complétées. Souvent, lorsque nous demandons des données à d'autres sources, comme une API externe, nous ne savons pas toujours _quand_ nos données seront renvoyées. Dans ces cas, nous voulons attendre la réponse, mais nous ne voulons pas toujours que notre application entière s'arrête pendant que nos données sont en cours de récupération. Ces situations sont celles où les fonctions de rappel sont utiles.

Prenons un exemple qui simule une requête vers un serveur :

```javascript
function serverRequest(query, callback){
  setTimeout(function(){
    var response = query + "plein !";
    callback(response);
  },5000);
}

function getResults(results){
  console.log("Réponse du serveur : " + results);
}

serverRequest("Le verre est à moitié ", getResults);

// Résultat dans la console après un délai de 5 secondes :
// Réponse du serveur : Le verre est à moitié plein !
```

Dans l'exemple ci-dessus, nous faisons une requête simulée à un serveur. Après 5 secondes, la réponse est modifiée et ensuite notre fonction de rappel `getResults` est exécutée. Pour voir cela en action, vous pouvez copier/coller le code ci-dessus dans l'outil de développement de votre navigateur et l'exécuter.

De plus, si vous êtes déjà familier avec `setTimeout`, alors vous avez utilisé des fonctions de rappel tout du long. L'argument de fonction anonyme passé dans l'appel de la fonction `setTimeout` de l'exemple ci-dessus est également une fonction de rappel ! Ainsi, la fonction de rappel originale de l'exemple est en fait exécutée par une autre fonction de rappel. Faites attention à ne pas imbriquer trop de fonctions de rappel si vous pouvez l'éviter, car cela peut conduire à ce qu'on appelle "l'enfer des callbacks" ! Comme le nom l'indique, ce n'est pas une joie à gérer.