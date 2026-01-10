---
title: Tutoriel sur les fermetures JavaScript – Comment les fermetures et la portée
  lexicale fonctionnent en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-28T18:45:21.000Z'
originalURL: https://freecodecamp.org/news/javascript-closure-lexical-scope
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/tim-evans-Uf-c4u1usFQ-unsplash.jpg
tags:
- name: closure
  slug: closure
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Lexical Scoping
  slug: lexical-scoping
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Tutoriel sur les fermetures JavaScript – Comment les fermetures et la portée
  lexicale fonctionnent en JS
seo_desc: 'By Dave Gray

  In JavaScript, people often confuse closures with lexical scope.

  Lexical scope is an important part of closures, but it is not a closure by itself.

  Closures are an advanced concept that is also a frequent topic of technical interviews.

  Y...'
---

Par Dave Gray

En JavaScript, les gens confondent souvent les fermetures avec la portée lexicale.

La portée lexicale est une partie importante des fermetures, mais ce n'est pas une fermeture en soi.

Les fermetures sont un concept avancé qui est également un sujet fréquent des entretiens techniques.

Vous devriez avoir une compréhension fondamentale des fonctions avant d'essayer de comprendre les fermetures.

Après avoir lu cet article, j'espère vous avoir aidé à apprendre ce qui suit :

* La différence entre la portée lexicale et les fermetures.
* Pourquoi les fermetures nécessitent une portée lexicale.
* Comment donner un exemple de fermeture lors du processus d'entretien.

## Qu'est-ce que la portée lexicale en JavaScript ?

La portée lexicale décrit comment les fonctions imbriquées (également connues sous le nom de "fonctions enfants") ont accès aux variables définies dans les portées parent.

```js
const myFunction = () => {
     let myValue = 2;
     console.log(myValue);

     const childFunction = () => {
          console.log(myValue += 1);
     }

     childFunction();
}

myFunction();
```

Dans cet exemple, `childFunction` a accès à la variable `myValue` qui est définie dans la portée parent de `myFunction`.

La portée lexicale de `childFunction` permet l'accès à la portée parent.

## Qu'est-ce qu'une fermeture en JavaScript ?

[w3Schools.com](https://www.w3schools.com/js/js_function_closures.asp) offre une excellente définition de ce qu'est une fermeture :

> Une fermeture est une fonction ayant accès à la portée parent, même après que la fonction parent a été fermée.

Regardons la première partie de la phrase avant la virgule :

> ...une fonction ayant accès à la portée parent

Cela décrit la portée lexicale !

Mais nous avons besoin de la deuxième partie de la définition pour donner un exemple de fermeture...

> ...même après que la fonction parent a été fermée.

Regardons un exemple de fermeture :

```js
const myFunction = () => {
     let myValue = 2;
     console.log(myValue);

     const childFunction = () => {
          console.log(myValue += 1);
     }

     return childFunction;
}

const result = myFunction();
console.log(result);
result();
result();
result();
```

Copiez le code d'exemple ci-dessus et essayez-le.

_Décortiquons ce qui se passe..._

Dans cette révision, `myFunction` retourne `childFunction` au lieu de l'appeler.

Par conséquent, lorsque `result` est défini égal à `myFunction()`, l'instruction de console à l'intérieur de `myFunction` est enregistrée, mais pas l'instruction à l'intérieur de `childFunction`.

`childFunction` n'est pas appelée à l'action.

Au lieu de cela, elle est retournée et conservée dans `result`.

De plus, nous devons réaliser que `myFunction` a été fermée après avoir été appelée.

La ligne avec `console.log(result)` devrait montrer dans la console que `result` contient maintenant la valeur de fonction anonyme qui était `childFunction`.

Maintenant, lorsque nous appelons `result()`, nous appelons la fonction anonyme qui était assignée à `childFunction`.

En tant qu'enfant de `myFunction`, cette fonction anonyme a accès à la variable `myValue` à l'intérieur de `myFunction` _même après qu'elle a été fermée !_

La fermeture que nous avons créée permet maintenant de continuer à augmenter la valeur de la variable `myValue` chaque fois que nous appelons `result()`.

## Prenez votre temps avec les fermetures

Les fermetures sont considérées comme un concept avancé pour de bonnes raisons.

Même avec une explication étape par étape de ce qu'est une fermeture, ce concept peut prendre du temps à comprendre.

Ne vous précipitez pas pour comprendre et ne soyez pas dur avec vous-même si cela n'a pas de sens au début.

Lorsque vous comprendrez pleinement les fermetures, vous pourriez vous sentir comme [Neo lorsqu'il voit la Matrice](https://www.google.com/search?q=neo+sees+the+matrix&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiG1MaN1rPxAhUNCM0KHQJWCtAQ_AUoAXoECAEQAw&biw=1762&bih=886). Vous verrez de nouvelles possibilités de code et réaliserez qu'elles étaient là tout le temps !

Je vous laisse avec un tutoriel sur les fermetures de [ma chaîne YouTube](https://www.youtube.com/davegrayteachescode). J'approfondis un peu plus et je fournis quelques exemples supplémentaires de fermetures pour construire la discussion dans cet article.

%[https://www.youtube.com/watch?v=1S8SBDhA7HA]