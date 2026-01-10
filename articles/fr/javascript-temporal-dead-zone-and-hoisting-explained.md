---
title: Zone Morte Temporelle (TDZ) et Hoisting en JavaScript – Expliqué avec des Exemples
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2022-01-24T23:10:03.000Z'
originalURL: https://freecodecamp.org/news/javascript-temporal-dead-zone-and-hoisting-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/javascript-temporal-dead-zone-and-hoisting-explained-codesweetly-image-by-bronis-aw-dr--ka-from-pixabay.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Zone Morte Temporelle (TDZ) et Hoisting en JavaScript – Expliqué avec des
  Exemples
seo_desc: 'Temporal Dead Zone and Hoisting are two essential terms in JavaScript.
  But understanding how they work can easily confuse you if you don''t approach them
  properly.

  But don''t fret! This article is here to help you get a good grasp of the two terms.

  So ...'
---

La Zone Morte Temporelle et le Hoisting sont deux termes essentiels en JavaScript. Mais comprendre comment ils fonctionnent peut facilement vous confondre si vous ne les abordez pas correctement.

Mais ne vous inquiétez pas ! Cet article est là pour vous aider à bien comprendre ces deux termes.

Alors détendez-vous, prenez votre tasse de café préférée, et commençons avec la TDZ.

## Qu'est-ce qu'une Zone Morte Temporelle en JavaScript ?

Une **zone morte temporelle (TDZ)** est la partie d'un bloc où une variable est inaccessible jusqu'au moment où l'ordinateur l'initialise complètement avec une valeur.

* Un [bloc](https://www.codesweetly.com/code-block/) est une paire d'accolades (`{...}`) utilisée pour regrouper plusieurs instructions.
* L'[initialisation](https://www.codesweetly.com/declaration-initialization-invocation-in-programming/) se produit lorsque vous attribuez une valeur initiale à une variable.

Supposons que vous essayez d'accéder à une variable avant son initialisation complète. Dans un tel cas, JavaScript lancera une `ReferenceError`.

Ainsi, pour empêcher JavaScript de lancer une telle erreur, vous devez vous souvenir d'accéder à vos variables depuis l'extérieur de la zone morte temporelle.

Mais où exactement commence et se termine la TDZ ? Découvrons-le ci-dessous.

## Où se situe exactement la portée d'une Zone Morte Temporelle ?

La zone morte temporelle d'un bloc commence au début de la portée locale du bloc. Elle se termine lorsque l'ordinateur a complètement initialisé votre variable avec une valeur.

**Voici un exemple :**

```js
{
  // La TDZ de bestFood commence ici (au début de la portée locale de ce bloc)
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  console.log(bestFood); // retourne ReferenceError car la TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  let bestFood = "Riz Frit aux Légumes"; // La TDZ de bestFood se termine ici
  // La TDZ de bestFood n'existe pas ici
  // La TDZ de bestFood n'existe pas ici
  // La TDZ de bestFood n'existe pas ici
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-sjp8hk?file=index.js)

Dans l'extrait ci-dessus, la TDZ du bloc commence à partir de l'accolade ouvrante (`{`) et se termine une fois que l'ordinateur initialise `bestFood` avec la valeur de chaîne `"Riz Frit aux Légumes"`.

Lorsque vous exécutez l'extrait, vous verrez que l'instruction `console.log()` retournera une `ReferenceError`.

JavaScript retournera une `ReferenceError` parce que nous avons utilisé le code `console.log()` pour accéder à `bestFood` avant son initialisation complète. En d'autres termes, nous avons invoqué `bestFood` dans la zone morte temporelle.

Cependant, voici comment vous pouvez accéder à `bestFood` avec succès après son initialisation complète :

```js
{
  // La TDZ commence ici (au début de la portée locale de ce bloc)
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  let bestFood = "Riz Frit aux Légumes"; // La TDZ de bestFood se termine ici
  console.log(bestFood); // retourne "Riz Frit aux Légumes" car la TDZ de bestFood n'existe pas ici
  // La TDZ de bestFood n'existe pas ici
  // La TDZ de bestFood n'existe pas ici
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-utknki?file=index.js)

Maintenant, considérons cet exemple :

```js
{
  // La TDZ commence ici (au début de la portée locale de ce bloc)
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  // La TDZ de bestFood continue ici
  let bestFood; // La TDZ de bestFood se termine ici
  console.log(bestFood); // retourne undefined car la TDZ de bestFood n'existe pas ici
  bestFood = "Riz Frit aux Légumes"; // La TDZ de bestFood n'existe pas ici
  console.log(bestFood); // retourne "Riz Frit aux Légumes" car la TDZ de bestFood n'existe pas ici
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-uyxf4y?file=index.js)

Vous pouvez voir que le premier code `console.log` dans l'extrait ci-dessus a retourné `undefined`.

JavaScript a retourné `undefined` parce que nous n'avons pas attribué de valeur à `bestFood` avant de l'utiliser ([invoquer](https://www.codesweetly.com/declaration-initialization-invocation-in-programming/#what-does-invocation-mean-in-programming)). Ainsi, JavaScript a défini sa valeur par défaut à `undefined`.

Gardez à l'esprit que vous devez spécifier une valeur pour une variable `const` lors de sa [déclaration](https://www.codesweetly.com/declaration-initialization-invocation-in-programming/#what-exactly-does-declaration-mean). À part cette exception, tous les autres principes de la zone morte temporelle des variables `let` s'appliquent également à `const`. Cependant, `var` fonctionne différemment.

## En quoi la TDZ de Var diffère-t-elle des variables Let et Const ?

La principale différence entre la zone morte temporelle d'une variable `var`, `let` et `const` est le moment où leur TDZ se termine.

Par exemple, considérons ce code :

```js
{
  // La TDZ de bestFood commence et se termine ici
  console.log(bestFood); // retourne undefined car la TDZ de bestFood n'existe pas ici
  var bestFood = "Riz Frit aux Légumes"; // La TDZ de bestFood n'existe pas ici
  console.log(bestFood); // retourne "Riz Frit aux Légumes" car la TDZ de bestFood n'existe pas ici
  // La TDZ de bestFood n'existe pas ici
  // La TDZ de bestFood n'existe pas ici
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-gcn7j5?file=index.js)

Lorsque vous exécutez l'extrait ci-dessus, vous verrez que la première instruction `console.log` retournera `undefined`.

L'instruction `console.log` a retourné avec succès une valeur (`undefined`) parce que JavaScript attribue automatiquement `undefined` à une variable `var` hissée.

En d'autres termes, lorsque l'ordinateur hisse une variable `var`, il initialise automatiquement la variable avec la valeur `undefined`.

En revanche, JavaScript n'initialise pas une variable `let` (ou `const`) avec une valeur quelconque lorsqu'il la hisse. Au lieu de cela, la variable reste morte et inaccessible.

Par conséquent, la TDZ d'une variable `let` (ou `const`) se termine lorsque JavaScript l'initialise complètement avec la valeur spécifiée lors de sa déclaration.

Cependant, la TDZ d'une variable `var` se termine immédiatement après son hissage—pas lorsque la variable est complètement initialisée avec la valeur spécifiée lors de sa déclaration.

Mais que signifie exactement "hissage" ? Découvrons-le ci-dessous.

## Que signifie exactement le Hoisting en JavaScript ?

Le **Hoisting** fait référence à JavaScript donnant une priorité plus élevée à la déclaration de variables, de classes et de fonctions lors de l'exécution d'un programme.

Le Hoisting fait en sorte que l'ordinateur traite les déclarations avant tout autre code.

**Note :** Le Hoisting ne signifie pas que JavaScript réorganise ou déplace du code au-dessus d'un autre.

Le Hoisting donne simplement une spécificité plus élevée aux déclarations JavaScript. Ainsi, il fait en sorte que l'ordinateur lise et traite les déclarations en premier avant d'analyser tout autre code dans un programme.

Par exemple, considérons cet extrait :

```js
{
  // Déclarer une variable :
  let bestFood = "Poisson et Frites";

  // Déclarer une autre variable :
  let myBestMeal = function () {
    console.log(bestFood);
    let bestFood = "Riz Frit aux Légumes";
  };

  // Invoquer la fonction myBestMeal :
  myBestMeal();
}

// Le code ci-dessus retournera :
"Uncaught ReferenceError: Cannot access 'bestFood' before initialization"
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ymmkih?file=index.js)

L'extrait ci-dessus a retourné une `ReferenceError` à cause de l'ordre de priorité selon lequel l'ordinateur a exécuté chaque code.

En d'autres termes, les [déclarations](https://www.codesweetly.com/declaration-initialization-invocation-in-programming#what-exactly-does-declaration-mean) du programme ont eu une priorité plus élevée sur les [initialisations](https://www.codesweetly.com/declaration-initialization-invocation-in-programming#what-does-initialization-mean), les [invocations](https://www.codesweetly.com/declaration-initialization-invocation-in-programming#what-does-invocation-mean-in-programming), et les autres codes.

Faisons un tour étape par étape de la manière dont JavaScript a exécuté l'extrait ci-dessus.

## Comment fonctionne le Hoisting en JavaScript étape par étape

Voici une explication de la manière dont JavaScript a exécuté l'extrait précédent.

### 1. JavaScript a analysé la première déclaration `bestFood`

```js
let bestFood // C'est la première déclaration bestFood dans le programme
```

La première déclaration de la variable `bestFood` est le premier code que l'ordinateur a analysé.

Notez qu'après que l'ordinateur a lu la déclaration de la variable `bestFood`, JavaScript a automatiquement gardé la variable dans une _zone morte temporelle_ jusqu'à ce qu'elle soit complètement initialisée.

Par conséquent, toute tentative d'accéder à `bestFood` avant son initialisation complète retournerait une `ReferenceError`.

### 2. L'ordinateur a analysé la déclaration de la variable `myBestMeal`

```js
let myBestMeal
```

La déclaration de la variable `myBestMeal` était le deuxième code que JavaScript a analysé.

Immédiatement après que l'ordinateur a lu la déclaration de la variable `myBestMeal`, JavaScript a automatiquement gardé la variable dans une zone morte temporelle jusqu'à ce qu'elle soit complètement initialisée.

Par conséquent, toute tentative d'accéder à `myBestMeal` avant son initialisation complète retournerait une `ReferenceError`.

### 3. L'ordinateur a initialisé la variable `bestFood`

```js
bestFood = "Poisson et Frites";
```

La troisième étape de l'ordinateur était d'initialiser `bestFood` avec la valeur de chaîne `"Poisson et Frites"`.

Par conséquent, invoquer `bestFood` à ce stade retournerait `"Poisson et Frites"`.

### 4. JavaScript a initialisé la variable `myBestMeal`

```js
myBestMeal = function() {
  console.log(bestFood);
  let bestFood = "Riz Frit aux Légumes";
};
```

Quatrièmement, JavaScript a initialisé `myBestMeal` avec la fonction spécifiée. Ainsi, si vous aviez invoqué `myBestMeal` à ce stade, la fonction aurait retourné.

### 5. L'ordinateur a invoqué la fonction `myBestMeal`

```js
myBestMeal();
```

L'invocation de la fonction `myBestMeal` était la cinquième action de l'ordinateur.

Après l'invocation, l'ordinateur a traité chaque code dans le bloc de la fonction. Cependant, les déclarations avaient une priorité plus élevée sur les autres codes.

### 6. JavaScript a analysé la déclaration `bestFood` de la fonction

```js
let bestFood // C'est la deuxième déclaration bestFood dans le programme
```

La sixième tâche de JavaScript était d'analyser la déclaration de la variable `bestFood` de la fonction.

Après l'analyse, JavaScript a automatiquement gardé la variable dans une zone morte temporelle—jusqu'à son initialisation complète.

Par conséquent, toute tentative d'accéder à `bestFood` avant son initialisation complète retournerait une `ReferenceError`.

### 7. L'ordinateur a analysé l'instruction `console.log` de la fonction

```js
console.log(bestFood);
```

Enfin, l'ordinateur a lu l'instruction `console.log`—qui a ordonné au système de journaliser le contenu de `bestFood` dans la console du navigateur.

Cependant, rappelez-vous que l'ordinateur n'a pas encore complètement initialisé la variable `bestFood` de la fonction. Ainsi, la variable est actuellement dans une zone morte temporelle.

Par conséquent, la tentative du système d'accéder à la variable a retourné une `ReferenceError`.

**Note :** Après que la `ReferenceError` a été retournée, l'ordinateur a arrêté de lire le code de la fonction. Par conséquent, JavaScript n'a pas initialisé la variable `bestFood` de la fonction avec `"Riz Frit aux Légumes"`.

## Conclusion

Voyons le tour d'horizon précédent de notre programme en une seule pièce :

```js
let bestFood // 1. JavaScript a analysé la première déclaration bestFood

let myBestMeal // 2. l'ordinateur a analysé la déclaration de la variable myBestMeal

bestFood = "Poisson et Frites"; // 3. l'ordinateur a initialisé la variable bestFood

myBestMeal = function () {
  console.log(bestFood);
  let bestFood = "Riz Frit aux Légumes";
}; // 4. JavaScript a initialisé la variable myBestMeal

myBestMeal(); // 5. l'ordinateur a invoqué la fonction myBestMeal

let bestFood // 6. JavaScript a analysé la déclaration bestFood de la fonction

console.log(bestFood); // 7. l'ordinateur a analysé l'instruction console.log de la fonction

Uncaught ReferenceError // l'invocation de bestFood a retourné une Erreur
```

Vous pouvez voir que JavaScript a traité les déclarations du programme avant les autres codes.

L'analyse des déclarations avant les autres codes dans un programme est ce que nous appelons "hoisting".

## Aperçu

Cet article a discuté de ce que signifient la zone morte temporelle et le hoisting en JavaScript. Nous avons également utilisé des exemples pour illustrer comment ils fonctionnent tous les deux.

Merci d'avoir lu !

### **Et voici une ressource utile sur ReactJS :**

J'ai écrit un livre sur React !

* Il est adapté aux débutants ✔
* Il contient des extraits de code interactifs ✔
* Il contient des projets évolutifs ✔
* Il contient de nombreux exemples faciles à comprendre ✔

Le livre [React Explained Clearly](https://amzn.to/30iVPIG) est tout ce dont vous avez besoin pour comprendre ReactJS.

[![Livre React Explained Clearly Disponible sur Amazon](https://www.freecodecamp.org/news/content/images/2022/01/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela.jpg)](https://amzn.to/30iVPIG)