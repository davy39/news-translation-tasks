---
title: 'Comment déclarer des variables JavaScript : un aperçu de let, const et var'
subtitle: ''
author: Shirshendu Bhowmick
co_authors: []
series: null
date: '2019-03-11T14:49:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-declare-javascript-variables-a-look-at-let-const-and-var-5d801c70c377
coverImage: https://cdn-media-1.freecodecamp.org/images/1*f5NxsWhcLjKe4GYjw74adg.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Comment déclarer des variables JavaScript : un aperçu de let, const et
  var'
seo_desc: With the old JavaScript, we had only one way to declare a variable, and
  that was with var, like var x = 10. It will create a variable called x and assign
  a value 10 to it. Now with modern ES6 JavaScript, we have 3 different ways to declare
  a variable...
---

Avec l'ancien JavaScript, nous avions une seule façon de déclarer une variable, et c'était avec `var`, comme `var x = 10`. Cela créera une variable appelée x et lui assignera la valeur 10. Maintenant, avec le JavaScript moderne ES6, nous avons 3 façons différentes de déclarer une variable : `let`, `const` et `var`. Nous parlerons de `let` et `const` plus tard. Pour l'instant, concentrons-nous sur `var`.

## var

Nous savons déjà comment déclarer une variable avec `var`. Référons-nous maintenant à du code pour bien comprendre `var`.

```js
var x = 20;
function foo() {
    var y = 10;
    console.log(x);
    console.log(y);
}
foo(); // imprimera 20 et 10
console.log(x); // imprimera 20
console.log(y); // lèvera une erreur de référence
```

Ceux qui sont familiers avec le C ou le C++ comprendront pourquoi la sortie est ainsi. Cela est dû au fait que `x` est dans la portée globale et `y` est dans la portée de la fonction foo. Comme la fonction `foo` a accès à la portée globale, depuis l'intérieur de la fonction, nous pouvons accéder à la fois à `x` et `y`. L'impression de `x` se passe également bien car, comme `x` est dans la portée globale, nous pouvons y accéder de partout. Les choses se passent mal lorsque nous essayons d'accéder à `y` depuis la portée globale car `y` est limité à la portée de la fonction uniquement.

Similaire au C ou C++ n'est-ce pas ? Non. Voyons pourquoi.

```js
var x = 20;
function foo() {
    var y = 10;
    {
        var z = 30;
    }
    console.log(x);
    console.log(y);
    console.log(z);
}
foo();
```

Que pensez-vous que la sortie du code sera ? Si vous pensez qu'il y aura une erreur de référence à la ligne `console.log(z)`, alors vous avez raison d'un point de vue C ou C++. Mais avec JavaScript, ce n'est pas le cas. Le code ci-dessus imprimera 20 10 30.

Cela est dû au fait qu'en JavaScript avec `var`, contrairement au C et C++, nous n'avons aucune portée de niveau bloc. Nous n'avons que des portées globale et de niveau fonction. Donc `z` relève de la portée de la fonction foo.

Nous avons maintenant un autre exemple :

```js
var x = 20;
var x = 30;
console.log(x); // cela imprimera 30
```

En C ou C++, si nous déclarons une variable plus d'une fois dans la même portée, nous obtenons une erreur. Mais ce n'est pas le cas avec `var` en JavaScript. Dans l'exemple ci-dessus, il redéfinit simplement `x` et lui assigne une valeur de 30.

Considérons les extraits de code ci-dessous :

```js
function foo() {
    x = 20;
    console.log(x);
}
foo();
console.log(x);
```

Le code ci-dessus imprimera 20 20. Alors, que se passe-t-il ici ? Si vous déclarez une variable n'importe où sans le mot-clé `var`, elle devient une partie de la portée globale. Elle est accessible à la fois de l'intérieur et de l'extérieur de `foo`.

```js
'use strict'
function foo() {
    x = 20;
    console.log(x);
}
foo();
console.log(x);
```

Dans le code ci-dessus, nous utilisons le mode strict. En mode strict, une déclaration de type `x = 20` n'est pas autorisée. Elle lèvera une erreur de référence. Vous devez déclarer une variable en utilisant `var`, `let` ou `const`.

## let

Il est maintenant temps de jeter un coup d'œil à `let`. `let` est le nouveau var dans ES6 mais avec quelques différences.

```js
let x = 20;
function foo() {
    let y = 10;
    {
        let z = 30;
    }
    console.log(x);
    console.log(y);
    console.log(z);
}
foo();
```

Souvenez-vous qu'en JavaScript, `var` n'a aucune portée de niveau bloc ? Maintenant, les portées de niveau bloc sont de retour avec `let`. Si vous exécutez le code ci-dessus, vous obtiendrez une erreur de référence à la ligne `console.log(z)`. La variable `z` déclarée avec `let` est maintenant dans une portée de niveau bloc différente et n'est pas accessible en dehors de cette portée.

```js
let x = 10;
let x = 20; // lèvera une erreur
```

La redéclaration de variables avec `let` n'est pas autorisée.

```js
var x = 10;
let y = 20;
console.log(window.x); // 10
console.log(window.y); // undefined
```

Les variables globales déclarées globalement avec `var` sont ajoutées à l'objet `global`, le `window` dans le cas des navigateurs. Les variables déclarées globalement avec `let` ne sont pas ajoutées à `window` (objet global). Bien qu'elles soient accessibles globalement, c'est comme si elles étaient là mais vous ne pouvez pas les voir.

```js
console.log(x); //undefined
console.log(y); //erreur de référence
var x;
let y;
```

Contrairement à `var`, les variables `let` ne sont pas initialisées avec undefined avant que leurs définitions ne soient évaluées. Si vous essayez d'accéder à la variable avant cela, vous rencontrerez une erreur de référence. Cela est également connu sous le nom de zone morte temporelle. En termes simples, le hoisting est uniquement disponible avec `var`, pas avec `let` et `const`.

## const

`const` signifie constante, elle est très similaire à `let`. Les seules différences sont que sa valeur ne peut pas être changée et qu'elle doit être initialisée là où vous la déclarez.

```js
const x = 20;
console.log(x); // imprimera 20
x = 30 // lèvera une erreur
```

Ce n'est pas que dans le cas des objets `const`, vous pouvez changer la propriété de cet objet — c'est simplement que vous ne pouvez pas réassigner une variable `const`.

```js
const obj = {firstName: "James", lastName: "Bond"}
console.log(obj); // imprimera l'objet obj
obj.firstName = "Ruskin";
console.log(obj); // imprimera l'objet obj, il a un nouveau firstName
obj = {firstName: "James", lastName: "Bond"}; // lèvera une erreur
```

De plus, comme mentionné précédemment, vous devez initialiser une variable `const`, vous ne pouvez pas la laisser non initialisée.

```js
const x; // lèvera une erreur
some other code;
```

C'est tout pour cet article — à plus tard !

## Merci d'avoir lu :)

##