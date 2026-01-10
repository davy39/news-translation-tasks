---
title: Comment fonctionne l'opérateur de coalescence nulle en JavaScript
subtitle: ''
author: Yogesh Chavan
co_authors: []
series: null
date: '2020-12-22T17:41:22.000Z'
originalURL: https://freecodecamp.org/news/nullish-coalescing-operator-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/nullish-2.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment fonctionne l'opérateur de coalescence nulle en JavaScript
seo_desc: "ES11 has added a nullish coalescing operator which is denoted by double\
  \ question marks, like this: ??. \nIn this article, we will explore why it's so\
  \ useful and how to use it.\nLet's get started.\nBackground Information\nIn JavaScript,\
  \ there is a short-c..."
---

ES11 a ajouté un opérateur de coalescence nulle qui est représenté par deux points d'interrogation, comme ceci : `??`.

Dans cet article, nous allons explorer pourquoi il est si utile et comment l'utiliser.

Commençons.

## Informations de base

En JavaScript, il existe un opérateur logique OR de court-circuit `||`.

> L'opérateur || retourne la première valeur `truthy`.

Les valeurs suivantes sont les `six seules` valeurs considérées comme `falsy` en JavaScript.

* false
* undefined
* null
* ""(chaîne vide)
* NaN
* 0

Donc, si quelque chose n'est pas dans la liste ci-dessus, il sera considéré comme une valeur `truthy`.

Les valeurs `Truthy` et `Falsy` sont des valeurs non booléennes qui sont converties en `true` ou `false` lors de certaines opérations.

```js
const value1 = 1;
const value2 = 23;

const result = value1 || value2; 

console.log(result); // 1
```

Comme l'opérateur || retourne la première valeur `truthy`, dans le code ci-dessus, le `result` sera la valeur stockée dans `value1` qui est `1`.

Si `value1` est `null`, `undefined`, `vide` ou toute autre valeur `falsy`, alors l'opérande suivant après l'opérateur || sera évalué et ce sera le résultat de l'expression totale.

```js
const value1 = 0;
const value2 = 23;
const value3 = "Hello";

const result = value1 || value2 || value3; 

console.log(result); // 23
```

Ici, parce que `value1` est 0, `value2` sera vérifié. Comme c'est une valeur truthy, le résultat de toute l'expression sera `value2`.

> Le problème avec l'opérateur || est qu'il ne distingue pas entre `false`, `0`, une chaîne vide `""`, `NaN`, `null` et `undefined`. Ils sont tous considérés comme des valeurs `falsy`.

Si l'un de ceux-ci est le premier opérande de ||, alors nous obtiendrons le deuxième opérande comme résultat.

## Pourquoi JavaScript avait besoin de l'opérateur de coalescence nulle

L'opérateur || fonctionne très bien, mais parfois nous voulons que l'expression suivante soit évaluée uniquement lorsque le premier opérande est soit `null` soit `undefined`.

Par conséquent, ES11 a ajouté l'opérateur de coalescence nulle.

Dans l'expression `x ?? y`,

* Si x est soit `null` soit `undefined` **alors seulement** le résultat sera `y`.
* Si x **n'est pas** `null` ou `undefined`, alors le résultat sera `x`.

Cela rendra les vérifications conditionnelles et le débogage du code une tâche facile.

## Essayez vous-même

```js
let result = undefined ?? "Hello";
console.log(result); // Hello

result = null ?? true; 
console.log(result); // true

result = false ?? true;
console.log(result); // false

result = 45 ?? true; 
console.log(result); // 45

result = "" ?? true; 
console.log(result); // ""

result = NaN ?? true; 
console.log(result); // NaN

result = 4 > 5 ?? true; 
console.log(result); // false car 4 > 5 évalue à false

result = 4 < 5 ?? true;
console.log(result); // true car 4 < 5 évalue à true

result = [1, 2, 3] ?? true;
console.log(result); // [1, 2, 3]

```

Donc, d'après tous les exemples ci-dessus, il est clair que le résultat de l'opération `x ?? y` est `y` uniquement lorsque `x` est soit `undefined` soit `null`.

Dans tous les autres cas, le résultat de l'opération sera toujours `x`.

## Conclusion

Comme vous l'avez vu, l'opérateur de coalescence nulle est vraiment utile lorsque vous ne vous souciez que de la valeur `null` ou `undefined` pour une variable.

À partir de ES6, il y a de nombreuses additions utiles à JavaScript comme

* La destructuration ES6
* La syntaxe d'import et d'export
* Les fonctions fléchées
* Les promesses
* Async/await
* L'opérateur de chaînage optionnel

et bien plus encore.

Vous pouvez tout apprendre sur toutes les fonctionnalités ES6+ en détail dans le livre [Mastering Modern JavaScript](https://modernjavascript.yogeshchavan.dev/).

Vous pouvez [obtenir le livre Mastering Modern JavaScript à 40% de réduction](https://modernjavascript.yogeshchavan.dev/).

**Abonnez-vous à ma [newsletter hebdomadaire](https://yogeshchavan.dev/) pour rejoindre plus de 1000 autres abonnés et recevoir des conseils, astuces, articles et offres de réduction directement dans votre boîte de réception.**