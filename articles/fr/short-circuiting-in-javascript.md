---
title: Comment fonctionne le court-circuit en JavaScript ?
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-12T18:38:38.000Z'
originalURL: https://freecodecamp.org/news/short-circuiting-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Copy-of-Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post-3-.png
tags:
- name: JavaScript
  slug: javascript
- name: Operators
  slug: operators
seo_title: Comment fonctionne le court-circuit en JavaScript ?
seo_desc: "In JavaScript, understanding truthy and falsy values is fundamental to\
  \ writing efficient and concise code. Combined with the concept of short-circuiting,\
  \ developers can write elegant solutions to common programming challenges. \nIn\
  \ this hands-on guide..."
---

En JavaScript, comprendre les valeurs "truthy" et "falsy" est fondamental pour écrire un code efficace et concis. Combiné avec le concept de court-circuit, les développeurs peuvent écrire des solutions élégantes aux défis de programmation courants. 

Dans ce guide pratique, nous explorerons les valeurs "truthy" et "falsy", et comprendrons les mécanismes du court-circuit en JavaScript.

Vous pouvez obtenir tout le code source à partir d'[ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/javascript-short-circuiting/index.js).

## Table des matières

* [Comprendre les valeurs Truthy et Falsy](#heading-comprendre-les-valeurs-truthy-et-falsy)
* [Qu'est-ce que le court-circuit en JavaScript ?](#heading-quest-ce-que-le-court-circuit-en-javascript)
* [Cas d'utilisation pratiques](#heading-cas-dutilisation-pratiques)
* [Conclusion](#heading-conclusion)

## Comprendre les valeurs Truthy et Falsy

En JavaScript, chaque valeur a une interprétation booléenne inhérente lorsqu'elle est évaluée dans un contexte booléen. Les valeurs qui évaluent à `true` sont considérées comme "truthy", tandis que celles qui évaluent à `false` sont "falsy". 

Explorons quelques exemples :

```javascript
// Valeurs Truthy
if ('Bonjour') {
    console.log('Truthy !'); // Sortie : Truthy !
}

if (42) {
    console.log('Truthy !'); // Sortie : Truthy !
}

if (['pomme', 'banane']) {
    console.log('Truthy !'); // Sortie : Truthy !
}

// Valeurs Falsy
if ('') {
    console.log('Falsy !'); // Ce bloc de code n'est pas exécuté
}

if (0) {
    console.log('Falsy !'); // Ce bloc de code n'est pas exécuté
}

if (null) {
    console.log('Falsy !'); // Ce bloc de code n'est pas exécuté
}

```

Voici une analyse du code ci-dessus :

### Valeurs Truthy

* `'Bonjour'` : Toute chaîne non vide en JavaScript est considérée comme "truthy". Dans ce cas, la chaîne `'Bonjour'` n'est pas vide, donc la condition évalue à true.
* `42` : Tout nombre non nul (positif ou négatif) est considéré comme "truthy". Puisque `42` est un nombre non nul, la condition évalue à true.
* `['pomme', 'banane']` : Les tableaux en JavaScript sont considérés comme "truthy", indépendamment de leur contenu. Puisque le tableau `['pomme', 'banane']` n'est pas vide, la condition évalue à true.

### Valeurs Falsy

`''` (chaîne vide) : Une chaîne vide en JavaScript est considérée comme "falsy". Par conséquent, la condition évalue à false, et le bloc de code à l'intérieur de l'instruction if ne sera pas exécuté.

`0` : Le nombre zéro est considéré comme "falsy" en JavaScript. Par conséquent, la condition évalue à false, et le bloc de code à l'intérieur de l'instruction if ne sera pas exécuté.

`null` : La valeur null est considérée comme "falsy" en JavaScript. Par conséquent, la condition évalue à false, et le bloc de code à l'intérieur de l'instruction if ne sera pas exécuté.

En JavaScript, les valeurs autres que `false`, `0`, `''` (chaîne vide), `null`, `undefined`, et `NaN` sont considérées comme "truthy". Comprendre ces valeurs "truthy" et "falsy" est crucial lors de l'écriture d'instructions conditionnelles et d'opérations logiques en JavaScript.

Comprendre les valeurs "truthy" et "falsy" est crucial car elles jouent un rôle significatif dans les instructions conditionnelles et les opérations logiques.

## Qu'est-ce que le court-circuit en JavaScript ?

Le court-circuit est un comportement exhibé par les opérateurs logiques (`&&`, `||`) où l'évaluation du second opérande est ignorée si le résultat peut être déterminé en évaluant le premier opérande seul. 

Examinons comment fonctionne le court-circuit avec des exemples pratiques :

### L'opérateur `&&`

L'opérateur `&&` retourne le premier opérande "falsy", ou le dernier opérande "truthy" si tous les opérandes sont "truthy".

```javascript
const value = 0;
const result = value && 'Valeur Truthy';
console.log(result); // Sortie : 0

```

Dans cet exemple, `value` évalue à `0`, qui est une valeur "falsy". Puisque le premier opérande est "falsy", l'expression court-circuite, et le résultat est `0`.

```javascript
const value = 'Bonjour';
const result = value && 'Valeur Truthy';
console.log(result); // Sortie : Valeur Truthy

```

Ici, `value` évalue à une chaîne non vide, qui est "truthy". Par conséquent, le second opérande `'Valeur Truthy'` est retourné, car c'est le dernier opérande "truthy".

### L'opérateur `||`

L'opérateur `||` retourne le premier opérande "truthy", ou le dernier opérande "falsy" si tous les opérandes sont "falsy".

```javascript
const name = '';
const displayName = name || 'Invité';
console.log(displayName); // Sortie : Invité

```

Dans cet exemple, `name` évalue à une chaîne vide, qui est "falsy". Par conséquent, l'expression court-circuite, et `'Invité'` est assigné à `displayName`.

```javascript
const name = 'Alice';
const displayName = name || 'Invité';
console.log(displayName); // Sortie : Alice

```

Ici, `name` évalue à une chaîne non vide, qui est "truthy". Par conséquent, le premier opérande `'Alice'` est retourné, car c'est le premier opérande "truthy" rencontré.

## Cas d'utilisation pratiques

### Fournir des valeurs par défaut

Le court-circuit est couramment utilisé pour fournir des valeurs par défaut aux variables.

```javascript
const options = {};
const limit = options.limit || 10;
console.log(limit); // Sortie : 10 (valeur par défaut)

```

Dans cet exemple, `options` est un objet vide. Le code vise à assigner une valeur à `limit` basée sur la propriété `options.limit`. Cependant, puisque `options.limit` n'est pas défini (il est undefined), l'opérateur logique OR (`||`) est utilisé.

L'opérateur logique OR retourne la valeur du premier opérande s'il est "truthy". Si le premier opérande est "falsy" (dans ce cas, `options.limit` est undefined), il retourne la valeur du second opérande (`10` dans ce cas), qui agit comme une valeur par défaut.

Par conséquent, `limit` sera assigné la valeur `10` parce que `options.limit` est "falsy" (undefined).

### Accéder en toute sécurité aux propriétés imbriquées

Le court-circuit peut également être utilisé pour accéder en toute sécurité aux propriétés imbriquées des objets.

```javascript
const user = { address: { city: 'New York' } };
const city = user.address && user.address.city;
console.log(city); // Sortie : New York

```

Dans cet exemple, `user` est un objet contenant un autre objet `address`, qui contient la propriété `city`.

L'expression `user.address && user.address.city` utilise le court-circuit. Elle vérifie si `user.address` existe et, si c'est le cas, elle vérifie ensuite si `user.address.city` existe.

Si `user.address` est "truthy" (s'il existe), JavaScript procède à l'évaluation de `user.address.city`. Si `user.address` est "falsy" (s'il est undefined ou null), JavaScript court-circuite l'évaluation et ne procède pas à l'évaluation de `user.address.city`. 

Cela prévient une potentielle `TypeError` si `user.address` n'est pas défini ou est null.

Puisque `user.address` existe dans ce cas, l'expression évalue à la valeur de `user.address.city`, qui est `'New York'`.

Cette technique assure un accès sécurisé aux propriétés imbriquées et aide à éviter les erreurs d'exécution dans les cas où les objets pourraient ne pas être entièrement peuplés ou structurés comme prévu.

## Conclusion

Le court-circuit peut grandement améliorer votre flux de développement. 

Vous pouvez pratiquer ces concepts dans vos projets pour devenir compétent dans l'utilisation efficace du comportement de court-circuit de JavaScript.

Si vous avez des commentaires, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/introvertedbot) et [Linkedin](https://www.linkedin.com/in/sahil-mahapatra/)