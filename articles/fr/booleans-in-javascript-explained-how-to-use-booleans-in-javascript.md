---
title: Les Booléens en JavaScript Expliqués – Comment utiliser les Booléens en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/booleans-in-javascript-explained-how-to-use-booleans-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d04740569d1a4ca3574.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: toothbrush
  slug: toothbrush
seo_title: Les Booléens en JavaScript Expliqués – Comment utiliser les Booléens en
  JavaScript
seo_desc: 'Boolean

  Booleans are a primitive datatype commonly used in computer programming languages.
  By definition, a boolean has two possible values: true or false.

  In JavaScript, there is often implicit type coercion to boolean. If for example
  you have an if...'
---

## **Boolean**

Les booléens sont un type de données primitif couramment utilisé dans les langages de programmation informatique. Par définition, un booléen a deux valeurs possibles : `true` ou `false`.

En JavaScript, il y a souvent une coercition de type implicite vers un booléen. Par exemple, si vous avez une instruction if qui vérifie une certaine expression, cette expression sera coercée en un booléen :

```javascript
const a = 'une chaîne';
if (a) {
  console.log(a); // affiche 'une chaîne'
}
```

Il n'y a que quelques valeurs qui seront coercées en false :

* false (pas vraiment coercé car il est déjà false)
* null
* undefined
* NaN
* 0
* "" (chaîne vide)

Toutes les autres valeurs seront coercées en true. Lorsqu'une valeur est coercée en un booléen, nous appelons cela soit 'falsy' soit 'truthy'.

Une façon dont la coercition de type est utilisée est avec l'utilisation des opérateurs or (`||`) et and (`&&`) :

```javascript
const a = 'mot';
const b = false;
const c = true;
const d = 0
const e = 1
const f = 2
const g = null

console.log(a || b); // 'mot'
console.log(c || a); // true
console.log(b || a); // 'mot'
console.log(e || f); // 1
console.log(f || e); // 2
console.log(d || g); // null
console.log(g || d); // 0
console.log(a && c); // true
console.log(c && a); // 'mot'
```

Comme vous pouvez le voir, l'opérateur _or_ vérifie le premier opérande. Si celui-ci est true ou truthy, il le retourne immédiatement (c'est pourquoi nous obtenons 'mot' dans le premier cas et true dans le second cas). Si ce n'est pas true ou truthy, il retourne le second opérande (c'est pourquoi nous obtenons 'mot' dans le troisième cas).

Avec l'opérateur and, cela fonctionne de manière similaire, mais pour que 'and' soit true, les deux opérandes doivent être truthy. Il retournera donc toujours le second opérande si les deux sont true/truthy, sinon il retournera false. C'est pourquoi dans le quatrième cas nous obtenons true et dans le dernier cas nous obtenons 'mot'.

## **L'objet Boolean**

Il existe également un objet natif JavaScript qui enveloppe une valeur. La valeur passée en tant que premier paramètre est convertie en une valeur booléenne, si nécessaire. Si la valeur est omise, 0, -0, null, false, NaN, undefined, ou la chaîne vide (""), l'objet a une valeur initiale de false. Toutes les autres valeurs, y compris tout objet ou la chaîne "false", créent un objet avec une valeur initiale de true.

Ne confondez pas les valeurs booléennes primitives true et false avec les valeurs true et false de l'objet Boolean.

## **Plus de détails**

Tout objet dont la valeur n'est pas undefined ou null, y compris un objet Boolean dont la valeur est false, est évalué à true lorsqu'il est passé à une instruction conditionnelle. Si true, cela exécutera la fonction. Par exemple, la condition dans l'instruction if suivante est évaluée à true :

```javascript
const x = new Boolean(false);
if (x) {
  // ce code est exécuté
}
```

Ce comportement ne s'applique pas aux booléens primitifs. Par exemple, la condition dans l'instruction if suivante est évaluée à false :

```javascript
const x = false;
if (x) {
  // ce code n'est pas exécuté
}
```

N'utilisez pas un objet Boolean pour convertir une valeur non booléenne en une valeur booléenne. Utilisez plutôt Boolean comme une fonction pour effectuer cette tâche :

```javascript
const x = Boolean(expression);     // préféré
const x = new Boolean(expression); // ne pas utiliser
```

Si vous spécifiez un objet quelconque, y compris un objet Boolean dont la valeur est false, comme valeur initiale d'un objet Boolean, le nouvel objet Boolean a une valeur de true.

```javascript
const myFalse = new Boolean(false);   // valeur initiale de false
const g = new Boolean(myFalse);       // valeur initiale de true
const myString = new String('Hello'); // objet chaîne
const s = new Boolean(myString);      // valeur initiale de true
```

N'utilisez pas un objet Boolean à la place d'un booléen primitif.