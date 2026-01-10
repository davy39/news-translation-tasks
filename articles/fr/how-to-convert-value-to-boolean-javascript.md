---
title: Comment convertir une valeur en booléen en JavaScript
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-05-20T18:06:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-value-to-boolean-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Fashion-Sale--Banner--Landscape--.png
tags:
- name: beginner
  slug: beginner
- name: Boolean
  slug: boolean
- name: JavaScript
  slug: javascript
seo_title: Comment convertir une valeur en booléen en JavaScript
seo_desc: 'A boolean is a primitive value that represents either true or false. In
  Boolean contexts, JavaScript utilizes type casting to convert values to true/false.
  There are implicit and explicit methods to convert values into their boolean counterparts.

  Thi...'
---

Un booléen est une [valeur primitive](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) qui représente soit vrai (true) soit faux (false). Dans les contextes booléens, JavaScript utilise la [conversion de type](https://developer.mozilla.org/en-US/docs/Glossary/Type_Conversion) pour convertir les valeurs en true/false. Il existe des méthodes implicites et explicites pour convertir des valeurs en leurs équivalents booléens.

Cet article donne un aperçu des valeurs "truthy" et "falsy" et explique comment convertir des valeurs en booléens en JavaScript.

### Tableau récapitulatif des valeurs "truthy" et "falsy" en JavaScript

```
Boolean(false);         // false
Boolean(undefined);     // false
Boolean(null);          // false
Boolean('');            // false
Boolean(NaN);           // false
Boolean(0);             // false
Boolean(-0);            // false
Boolean(0n);            // false

Boolean(true);          // true
Boolean('hi');          // true
Boolean(1);             // true
Boolean([]);            // true
Boolean([0]);           // true
Boolean([1]);           // true
Boolean({});            // true
Boolean({ a: 1 });      // true
```

Il est préférable de commencer par comprendre quelles valeurs sont interprétées comme "truthy" ou "falsy" par JavaScript. Il est également important de comprendre la [coercition implicite](https://betterprogramming.pub/implicit-and-explicit-coercion-in-javascript-b23d0cb1a750) par rapport à la [coercition explicite](https://www.bookstack.cn/read/TypesGrammar/spilt.3.ch4.md#Explicitly:%20*%20%E2%80%94%3E%20Boolean).

La coercition implicite est initiée par le moteur JavaScript et se produit automatiquement. La coercition explicite est effectuée en convertissant manuellement les valeurs, et JavaScript fournit des méthodes intégrées pour gérer cela.

### L'opérateur `!!`

```javascript
!!value
```

Vous connaissez peut-être déjà `!` comme l'opérateur logique NOT. En utilisant deux de suite (`!!`), le premier `!` force la valeur en booléen et l'inverse. Par exemple, `!true` donnerait false. Le second `!` inverse la valeur précédemment inversée, résultant en la valeur booléenne true.

C'est généralement une méthode préférée, car elle a [de meilleures performances](https://www.measurethat.net/Benchmarks/Show/11127/0/boolean-vs). Un inconvénient potentiel de cette méthode est une perte de lisibilité, principalement si d'autres développeurs ne sont pas familiers avec le fonctionnement de cet opérateur.

```javascript
const value = "truthy string"
!!value // true
```

Voici un exemple décomposé en étapes :

```javascript
const value = "truthy string";

!value; // false
!!value; // true
```

Ci-dessous se trouve une liste d'exemples de sortie avec l'opérateur `!!`.

```javascript
// Valeurs "falsy"

!!'' // false
!!false // false
!!null // false
!!undefined // false
!!0 // false
!!NaN // false


// Valeurs "truthy"

!![] // true
!!"false" // true
!!true // true
!!1 // true
!!{} // true
```

### La fonction `Boolean()`

```javascript
Boolean(value)
```

`Boolean()` est une fonction globale qui convertit la valeur qui lui est passée en booléen.

Vous ne devriez pas utiliser cette fonction avec le mot-clé `new` (`new Boolean`) car cela crée une instance d'un Boolean qui a un type d'objet. Ci-dessous se trouve un exemple de l'utilisation correcte de cette fonction.

```javascript
const value = "truthy string"
Boolean(value) // true
```

## En résumé

Il existe deux méthodes pour convertir une valeur en booléen en JavaScript.

### 1. `!!`

```javascript
!!value

```

### 2. `Boolean()`

```
Boolean(value)

```

```javascript
const finalThoughts = "J'ai vraiment apprécié écrire cet article. Merci pour la lecture !"

!!finalThoughts // true
Boolean(finalThoughts) // true

```