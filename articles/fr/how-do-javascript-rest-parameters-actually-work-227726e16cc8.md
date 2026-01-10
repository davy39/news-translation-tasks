---
title: Comment fonctionnent réellement les paramètres rest de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T00:32:29.000Z'
originalURL: https://freecodecamp.org/news/how-do-javascript-rest-parameters-actually-work-227726e16cc8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*10krG9dLp-2JAyOo1TNVPQ.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Comment fonctionnent réellement les paramètres rest de JavaScript
seo_desc: 'By Yazeed Bzadough

  My last article covered spread syntax and Object.assign in detail, but glossed over
  rest parametersin the interest of time. I do, however, feel they deserve a closer
  look.

  Let’s begin at the trusty MDN Docs:


  The rest parameter syn...'
---

Par Yazeed Bzadough

[Mon dernier article](https://medium.com/@yazeedb/how-do-object-assign-and-spread-actually-work-169b53275cb) couvrait en détail la syntaxe **spread** et `Object.assign`, mais passait rapidement sur les **paramètres rest** par manque de temps. Je pense cependant qu'ils méritent un examen plus approfondi.

Commençons par la documentation de confiance [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters) :

> La syntaxe des **paramètres rest** nous permet de représenter un nombre indéfini d'arguments sous la forme d'un tableau.

Cette dernière partie, « sous la forme d'un tableau », est intéressante, car avant les fonctions fléchées d'ES6, nous utilisions l'**objet** `arguments`. Il ressemblait à un tableau (*array-like*), mais n'en était pas réellement un.

Exemple :

```js
function returnArgs() {
  return arguments;
}
```

![](https://cdn-media-1.freecodecamp.org/images/1*Xuhn5NvMtl3Mev2FqL-oug.png)

Nous voyons que `arguments` possède des indices, il est donc possible de boucler dessus :

```js
function loopThruArgs() {
  let i = 0;

  for (i; i < arguments.length; i++) {
    console.log(arguments[i]);
  }
}
```

![](https://cdn-media-1.freecodecamp.org/images/1*jU_wgPi5ILJrOQ7F0J8sUA.png)

Mais ce n'est pas un tableau.

![](https://cdn-media-1.freecodecamp.org/images/1*KNeT3_DX6pQE3TWkjzJiMg.png)

Comparons cela avec une fonction utilisant les paramètres **rest** :

```js
es6Params = (...params) => {
  console.log('Array?', Array.isArray(params));
  return params;
};
```

![](https://cdn-media-1.freecodecamp.org/images/1*cPEtXM-jUWC3oDsCHU2keg.png)

C'est *juste un tableau*, ce qui signifie que nous pouvons utiliser n'importe quelle méthode d'`Array` dessus !

Écrivons une fonction qui **double** et **additionne** chaque paramètre que vous lui donnez.

```js
double = (x) => x * 2;
sum = (x, y) => x + y;

doubleAndSum = (...numbers) => numbers.map(double).reduce(sum, 0);
```

![](https://cdn-media-1.freecodecamp.org/images/1*Hdk9NP-ZGteTef7v5RPBEg.png)

Et vous pouvez nommer autant de paramètres que vous le souhaitez dans votre fonction avant d'utiliser **rest**.

```js
someFunction = (a, b, c, ...others) => {
  console.log(a, b, c, others);
};
```

![](https://cdn-media-1.freecodecamp.org/images/1*NZVvRUAyRffRtcckUIPdLA.png)

Mais il doit être le dernier spécifié, puisqu'il capture le *reste* de vos arguments. ?

![](https://cdn-media-1.freecodecamp.org/images/1*xjYSLt00rbmHdUtBYWUPMg.png)

Je pense que nous savons ce qui se passe sous le capot, mais soyons rigoureux. Allez voir sur [babeljs.io/repl](https://babeljs.io/repl), où vous pouvez écrire du code ES6+ et le faire transpiler en ES5 en temps réel.

![](https://cdn-media-1.freecodecamp.org/images/1*qYBa9yW0izOhXaTfP8IBKw.png)

C'est une petite fonction sympa, développons-la et ajoutons des commentaires.

```js
someFunction = function someFunction() {
  var _len = arguments.length;

  // créer un tableau de la même longueur
  // que l'objet arguments
  var args = Array(_len);
  var i = 0;

  // itérer à travers les arguments
  for (i; i < _len; i++) {
    // les assigner au
    // nouveau tableau
    args[i] = arguments[i];
  }

  // et le retourner
  return args;
};
```

Puisque Babel a écrit une fonction à l'ancienne pour nous, elle peut accéder à l'objet `arguments` ! `arguments` possède des indices et une propriété `.length`, ce qui est tout ce dont nous avons besoin pour en créer un clone parfait.

C'est pourquoi nous pouvons utiliser des méthodes de tableau comme `map`, `filter`, `reduce` sur les paramètres **rest**, car cela crée un clone de `arguments` sous forme de tableau.

Amusez-vous bien avec les paramètres *rest* !