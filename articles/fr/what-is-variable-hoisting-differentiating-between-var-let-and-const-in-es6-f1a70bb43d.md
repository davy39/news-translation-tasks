---
title: Un guide sur le hoisting des variables JavaScript ? avec let et const
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-19T17:28:14.000Z'
originalURL: https://freecodecamp.org/news/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0hfm3TfurQboq6KlJrG56g.jpeg
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
seo_title: Un guide sur le hoisting des variables JavaScript ? avec let et const
seo_desc: 'By Bhuvan Malik

  New JavaScript developers often have a hard time understanding the unique behaviour
  of variable/function hoisting.

  Since we’re going to be talking about var, let and const declarations later on,
  it’s important to understand variable h...'
---

Par Bhuvan Malik

Les nouveaux développeurs JavaScript ont souvent du mal à comprendre le comportement unique du _hoisting_ des variables/fonctions.

Puisque nous allons parler des déclarations `var`, `let` et `const` plus tard, il est important de comprendre le _hoisting des variables_ plutôt que le _hoisting des fonctions_. Plongeons-nous dans le sujet !

![Image](https://cdn-media-1.freecodecamp.org/images/qtdiMnLrgBGImBAMbanGKSmux1n-jjX3wOKH)

### **Qu'est-ce que le hoisting des variables ?**

Le moteur JavaScript traite toutes les déclarations de variables utilisant "`_var_`" comme si elles étaient déclarées en haut d'une portée fonctionnelle (si déclarées à l'intérieur d'une fonction) ou d'une portée globale (si déclarées à l'extérieur d'une fonction) indépendamment de l'endroit où la déclaration réelle se produit. Cela est essentiellement le "_hoisting_".

Ainsi, les variables peuvent être disponibles avant leur déclaration.

![Image](https://cdn-media-1.freecodecamp.org/images/kdtsq45xrgSooJlUgu3ArT4FiRvuzItcwqlX)

Voyons cela en action..

```
// SORTIE : undefinedconsole.log(shape);
```

```
var shape = "square";
```

```
// SORTIE : "square"console.log(shape);
```

Si vous venez de langages basés sur C, vous vous attendriez à une erreur lorsque le premier `console.log` est appelé puisque la variable `shape` n'avait pas été définie à ce moment-là. Mais l'interpréteur JavaScript regarde devant et "hoiste" toutes les déclarations de variables en haut, et l'initialisation reste au même endroit.

Voici ce qui se passe en coulisses :

```
// déclaration hoistée en hautvar shape;
```

```
// SORTIE : undefinedconsole.log(shape);
```

```
shape = "square";
```

```
// SORTIE : "square"console.log(shape);
```

Voici un autre exemple cette fois dans une portée fonctionnelle pour clarifier les choses :

```
function getShape(condition) {    // shape existe ici avec une valeur undefined
```

```
    // SORTIE : undefined    console.log(shape);
```

```
    if (condition) {        var shape = "square";        // autre code        return shape;    } else {        // shape existe ici avec une valeur undefined        return false;    }}
```

Vous pouvez voir dans l'exemple ci-dessus comment la déclaration de `shape` est hoistée en haut de la fonction `getShape()`. Cela est dû au fait que les blocs if/else ne créent pas de portée locale comme vu dans d'autres langages. Une portée locale est essentiellement une portée de fonction en JavaScript. Par conséquent, shape est accessible partout en dehors du bloc `if` et dans la fonction avec une valeur 'undefined'.

Ce comportement par défaut de JavaScript a ses avantages et ses inconvénients. Ne pas les comprendre pleinement peut conduire à des bugs subtils mais dangereux dans notre code.

### **Les déclarations de niveau bloc !**

![Image](https://cdn-media-1.freecodecamp.org/images/dboQXJ3XAiw2IMLMsf8tfhv4SeXXnQaE3FOX)

ES6 a introduit des options de portée de niveau bloc pour fournir aux développeurs plus de contrôle et de flexibilité sur le cycle de vie d'une variable.

Les déclarations de niveau bloc sont faites dans des portées de bloc/lexicales qui sont créées à l'intérieur d'un bloc "{ }".

#### Déclarations let

Cette syntaxe est similaire à `var`, il suffit de remplacer `var` par `let` pour déclarer une variable dont la portée est uniquement ce bloc de code.

Placez vos déclarations `let` en haut d'un bloc pour qu'elles soient disponibles dans tout ce bloc.

Par exemple :

```
function getShape(condition) {// shape n'existe pas ici
```

```
// console.log(shape); => ReferenceError: shape is not defined
```

```
if (condition) {        let shape = "square";        // autre code        return shape;    } else {        // shape n'existe pas ici non plus        return false;    }}
```

Remarquez comment shape existe uniquement à l'intérieur du bloc `if`, et lance une erreur lorsqu'on tente d'y accéder en dehors de celui-ci au lieu de sortir `undefined` comme dans notre cas précédent avec les déclarations `var`.

**NOTE** : Si un identifiant a déjà été défini à l'intérieur d'une portée avec `var`, utiliser le même identifiant dans une déclaration `let` à l'intérieur de la même portée lance une erreur.  
De plus, aucune erreur n'est lancée si une déclaration `let` crée une variable avec le même nom qu'une variable dans sa portée externe. (Ce cas est le même avec les déclarations `const` dont nous parlerons bientôt.)

Par exemple :

```
var shape = "square";let shape = "rectangle";
```

```
// SyntaxError: Identifier 'shape' has already been declared
```

et :

```
var shape = "square";if (condition) {    // ne lance pas d'erreur    let shape = "rectangle";    // plus de code }// Pas d'erreur
```

### Déclarations const

La syntaxe de déclaration est similaire à `let` et `var`, le cycle de vie est le même que `let`. Mais vous devez suivre certaines règles.

Les liaisons déclarées en utilisant `const` sont traitées comme des **constantes**, et donc **elles ne peuvent pas être réassignées une fois définies**. En raison de cela, chaque déclaration `const` **doit être initialisée** au moment de la déclaration.

Par exemple :

```
// const valide shape = "triangle";
```

```
// erreur de syntaxe : initialisation manquanteconst color;
```

```
// TypeError: Assignment to constant variableshape = "square"
```

**Cependant**, les propriétés d'un objet peuvent être modifiées !

```
const shape = {    name: "triangle",    sides: 3}
```

```
// FONCTIONNEshape.name = "square";shape.sides = 4;
```

```
// SyntaxError: Invalid shorthand property initializershape = {    name: "hexagon",    sides: 6}
```

Dans l'exemple ci-dessus, nous pouvons voir que seules les propriétés de l'objet `shape` pouvaient être changées parce que nous changeons seulement ce que `shape` contient, pas ce à quoi il est lié.

Nous pouvons résumer en disant que `const` empêche la modification de la liaison dans son ensemble — pas la valeur à laquelle elle est liée.

Note : Les propriétés peuvent être mutées. Donc pour une vraie immutabilité, utilisez Immutable.js ou Mori.

### La Zone Morte Temporelle

Nous savons maintenant que l'accès aux variables `let` ou `const` avant qu'elles ne soient déclarées lancera une `ReferenceError`. Cette période entre l'entrée dans la portée et la déclaration où elles ne peuvent pas être accessibles est appelée la Zone Morte Temporelle.

Notez que "Zone Morte Temporelle" n'est pas formellement mentionnée dans la spécification ECMAScript. C'est juste un terme populaire parmi les programmeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/VGX7QSdndFKi23EHHNbrYUD4LDtTPMwxn4bf)

Je recommande personnellement d'utiliser toujours `const`, car cela conduit à moins de bugs. Je n'ai pas encore rencontré de situation où j'avais besoin d'utiliser `var`.

En règle générale, utilisez `let` uniquement pour les compteurs de boucle ou seulement si vous avez vraiment besoin de réassignment. Ailleurs, utilisez `const`. Personnellement, j'ai abandonné les boucles pour filter(), map() et reduce(). Vous devriez aussi.

**Assurez-vous de consulter la partie 2 sur le Hoisting des Fonctions et les questions d'entretien importantes liées au sujet du hoisting en JS.**

[**Hoisting des Fonctions & Questions d'Entretien sur le Hoisting**](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)  
[_Ceci est une partie 2 de mon article précédent sur le Hoisting des Variables intitulé "Un guide sur le hoisting des variables JavaScript ? avec
…m_edium.freecodecamp.org](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)

Cliquez [ici](https://medium.com/@bhuvanmalik/es6-functions-9f61c72b1e86) pour mon article sur certaines des nouvelles fonctionnalités utiles dans ES6 liées aux fonctions.

À la prochaine. Paix ! ✌️