---
title: Générateurs ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-27T13:01:22.000Z'
originalURL: https://freecodecamp.org/news/es6-generators-47a9c5290569
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tBXQMulrsKL21K66SVQ5jA.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Générateurs ES6
seo_desc: 'By Sanket Meghani

  Generators are one of the key features introduced in ES6. Contrary to normal functions
  which can only be entered at the beginning of the function, Generators are functions
  which can be exited and re-entered later with their context ...'
---

Par Sanket Meghani

Les générateurs sont l'une des principales fonctionnalités introduites dans ES6. Contrairement aux fonctions normales qui ne peuvent être appelées qu'au début de la fonction, les générateurs sont des fonctions qui peuvent être quittées et réintégrées plus tard avec leur contexte (liaisons de variables) sauvegardé entre les réentrées. En d'autres termes, une fonction générateur pourrait retourner une valeur à mi-chemin et reprendre son exécution à partir de ce point plus tard.

Un générateur peut être défini en utilisant le mot-clé function suivi d'un astérisque.

La différence entre l'appel d'une fonction normale et d'une fonction itérative est que l'appel d'une fonction générateur n'exécute pas immédiatement la fonction générateur. Elle retourne plutôt un objet itérateur pour le générateur. Pour exécuter le corps du générateur, nous devons appeler la méthode next() sur l'itérateur retourné.

```
let generator = myFirstGenerator(5);let output = generator.next();
```

Lorsque la méthode next() de l'itérateur est appelée, le corps de la fonction générateur est exécuté jusqu'à la première expression yield. L'expression yield spécifie la valeur à retourner. Dans l'exemple ci-dessus, l'appel à generator.next() exécuterait la première instruction console.log() et retournerait la sortie de (a + 5). La méthode next() retourne un objet avec la structure suivante.

```
{    value: 10, //Valeur de retour de l'expression yield. C'est-à-dire 5 + 5    done: false //Indique si le générateur a retourné sa dernière valeur}
```

Nous pouvons imprimer la valeur retournée par yield en utilisant la propriété value de l'objet retourné.

```
let generator = myFirstGenerator(5);let output = generator.next(); //output = {value: 10, done: false}
```

```
console.log('Output is: ', output.value); //Output is: 10
```

L'appel à next() à nouveau sur l'itérateur reprendra l'exécution du générateur à partir de la dernière expression yield jusqu'à ce qu'une autre expression yield ou une instruction return soit rencontrée.

```
output = generator.next(10); //output = {value: 15, done: true}
```

Dans notre exemple, l'appel à generator.next(10) reprendra l'exécution du générateur à la ligne 4 avec la valeur de la dernière expression yield étant 10 (c'est-à-dire la valeur passée à next()). Ainsi, la ligne 4 sera évaluée comme b = 5 + 10, ce qui donnera b = 15. À la ligne 7, elle retourne la valeur de b et, comme il s'agit de la dernière instruction return (c'est-à-dire qu'il n'y a plus de yield), done est défini sur true.

L'appel à la méthode next() avec un argument reprendra l'exécution de la fonction générateur, en remplaçant l'instruction yield où l'exécution a été suspendue par l'argument de next().

```
output = generator.next(15); //output = {value: 20, done: true}
```

L'appel à generator.next(15) reprendra l'exécution du générateur à la ligne 4 avec la valeur de la dernière expression yield remplacée par 15. Ainsi, la ligne 4 sera évaluée comme b = 5 + 15, ce qui donnera b = 20.

Nous pouvons utiliser yield* pour déléguer à une autre fonction générateur.

### **Postface**

Il est assez intrigant de savoir comment cette nouvelle fonctionnalité pourrait être utilisée en pratique. [Redux-saga](http://yelouafi.github.io/redux-saga/) utilise des fonctions générateurs pour faciliter l'écriture de flux asynchrones. Nous n'avons fait qu'effleurer la surface et il y a beaucoup plus à découvrir. J'adorerais entendre vos commentaires, suggestions ou questions sur les générateurs ES6 et leurs cas d'utilisation :).