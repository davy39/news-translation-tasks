---
title: One-liners JavaScript à utiliser dans chaque projet
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-03-10T21:18:03.000Z'
originalURL: https://freecodecamp.org/news/javascript-one-liners-to-use-in-every-project
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/javascript-one-liner.png
tags:
- name: JavaScript
  slug: javascript
seo_title: One-liners JavaScript à utiliser dans chaque projet
seo_desc: 'JavaScript is a powerful language that can do a lot with very little code.

  In some cases, the amount of code you need to write doesn''t exceed more than a
  single line, which is why they are known as one-liners.

  Let''s go through 10 essential one liners...'
---

JavaScript est un langage puissant qui peut faire beaucoup avec très peu de code.

Dans certains cas, la quantité de code que vous devez écrire ne dépasse pas une seule ligne, c'est pourquoi ils sont connus sous le nom de "one-liners".

Parcourons 10 one-liners essentiels qui valent la peine d'être utilisés dans pratiquement tous les projets JavaScript que vous créez.

## 1. Comment mettre une majuscule au texte

```js
const capitalize = (str) => `${str.charAt(0).toUpperCase()}${str.slice(1)}`;
```

Mettre une majuscule aux chaînes de caractères n'est pas une fonctionnalité native de JavaScript.

Pour corriger cela, nous pouvons créer une fonction `capitalize` qui accepte du texte et met la première lettre en majuscule, puis ajoute le reste de la chaîne.

Ce one-liner est utile pour à peu près tout type de texte que vous souhaitez mettre en majuscule. Je l'utilise le plus souvent pour afficher les noms des utilisateurs.

```js
const name = "robert";

capitalize(name) // "Robert";
```

## 2. Comment calculer un pourcentage

```js
const calculatePercent = (value, total) => Math.round((value / total) * 100)
```

Calculer un pourcentage est assez facile et implique simplement quelques calculs mathématiques simples. C'est une tâche essentielle si vous voulez afficher la progression de l'utilisateur, par exemple pour incrémenter une barre de progression.

`calculatePercent` accepte une certaine quantité, la divise par le montant total, puis la multiplie par 100. Enfin, nous utilisons `Math.round()` pour arrondir le résultat à l'entier le plus proche.

```js
const questionsCorrect = 6;
const questionTotal = 11;

calculatePercent(questionsCorrect, questionTotal); // 55
```

## 3. Comment obtenir un élément aléatoire

```js
const getRandomItem = (items) =>  items[Math.floor(Math.random() * items.length)];
```

Obtenir un élément aléatoire d'un tableau est très pratique lorsque vous voulez rendre les choses uniques pour votre utilisateur.

Par exemple, vous pourriez vouloir montrer à vos utilisateurs un message de félicitations basé sur une certaine action. Mais vous ne voulez probablement pas leur montrer le même à chaque fois, car cela deviendrait répétitif et ennuyeux.

`getRandomItem` utilise la fonction `Math.random()`, qui renvoie un décimal entre 0 et 1. Celui-ci est multiplié par la longueur du tableau pour sélectionner un index aléatoire, qui peut ensuite être utilisé pour sélectionner un élément au hasard.

```js
const items = ["Nicely done!", "Good job!", "Good work!", "Correct!"];

getRandomItem(items); // "Good job!"
```

## 4. Comment supprimer les éléments en double

```js
const removeDuplicates = (arr) => [...new Set(arr)];
```

Supprimer les valeurs en double dans un tableau est une tâche essentielle en JavaScript.

Par exemple, vous pourriez ajouter un utilisateur à la liste d'amis d'un autre utilisateur, mais vous ne voulez pas que cet utilisateur soit ajouté ou affiché deux fois.

Cette fonction `removeDuplicates` exploite le constructeur `Set` en JavaScript, qui supprime par défaut toutes les valeurs (primitives) en double. Après cela, nous utilisons l'opérateur de décomposition (spread operator) `...` pour propager ses valeurs dans un nouveau tableau.

```js
const friendList = ["Jeff", "Jane", "Jane", "Rob"];

removeDuplicates(friendList); // ['Jeff', 'Jane', 'Rob']
```

## 5. Comment trier des éléments par une certaine propriété

```js
const sortBy = (arr, key) => arr.sort((a, b) => a[key] > b[key] ? 1 : a[key] < b[key] ? -1 : 0);
```

Une tâche courante lors de l'affichage de données en JavaScript est de les trier en fonction d'une certaine propriété.

Cette fonction `sortBy` utilise la méthode de tri native, compare les éléments du tableau en se basant sur la clé fournie et trie le tableau par ordre croissant.

Où cela serait-il utile ? Si vous récupérez des données qui sont censées être à une certaine position en fonction d'une clé de position, `sortBy` s'assurera que ces éléments sont placés dans le bon ordre.

```js
const lessons = [{ position: 1, name: "Intro" }, { position: 0, name: "Basics" }];

sortBy(lessons, 'position'); 

// {position: 0, name: 'Basics'},
// {position: 1, name: 'Intro'}
```

## 6. Comment vérifier si des tableaux ou objets sont égaux

```js
const isEqual = (a, b) => JSON.stringify(a) === JSON.stringify(b);

```

Il est facile de vérifier l'égalité avec les primitives JavaScript, comme les nombres et les chaînes.

Cependant, vérifier l'égalité entre des tableaux et des objets est un peu plus difficile. Heureusement, il existe une astuce intéressante que vous pouvez utiliser avec `JSON.stringify` pour convertir des tableaux ou des objets en une chaîne JSON. Si tous les éléments correspondent, `isEqual` renverra la valeur true.

C'est très pratique lorsque vous attendez plusieurs entrées de la part d'un utilisateur, par exemple s'il répond à une question et que vous voulez comparer sa réponse à la solution correcte.

```js
isEqual([1, '2'], [1, 2]); // false
isEqual([1, 2], [1, 2]); // true
```

## 7. Comment compter le nombre d'occurrences

```js
const countOccurrences = (arr, value) => arr.reduce((a, v) => (v === value ? a + 1 : a), 0);
```

Un autre one-liner utile basé sur les tableaux consiste à compter le nombre d'occurrences d'un élément dans un tableau. Il utilise la fonction `.reduce()`. Si la valeur est trouvée dans le tableau, elle incrémente un compteur de un.

Un exemple utile pourrait être un sondage pour déterminer pour quoi la plupart des gens ont voté.

```js
const pollResponses = ["Yes", "Yes", "No"];
const response = "Yes";

countOccurrences(pollResponses, response); // 2
```

## 8. Comment attendre un certain laps de temps

```js
const wait = async (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));
```

Dans votre application, vous pourriez vouloir attendre pendant une certaine période. Par exemple, si vous voulez retarder une animation ou si vous attendez la fin d'une opération importante.

Vous pouvez fournir à la fonction `wait` un certain temps d'attente en millisecondes. Comme elle utilise une promesse, vous pouvez utiliser le rappel `then` ou le mot-clé `await` pour vous assurer qu'elle est terminée.

```js
wait(2000).then(() => goToSignupPage());
```

## 9. Comment extraire une propriété d'un tableau d'objets (Pluck)

```js
const pluck = (objs, key) => objs.map((obj) => obj[key]);
```

Si vous avez besoin d'extraire des données d'un tableau d'objets et que vous n'êtes pas intéressé par toutes les données renvoyées, utilisez la fonction `pluck`.

Elle prend un tableau d'objets et une propriété que chacun des objets contient. La fonction parcourt ce tableau et renvoie un tableau contenant uniquement les valeurs de la propriété que nous avons spécifiée.

Par exemple, si nous avons un tableau de données utilisateur, mais que nous voulons le convertir simplement en un tableau de leurs noms, `pluck` peut le faire.

```js
const users = [{ name: "Abe", age: 45 }, { name: "Jennifer", age: 27 }];

pluck(users, 'name'); // ['Abe', 'Jennifer']
```

## 10. Comment insérer un élément à une certaine position

```js
const insert = (arr, index, newItem) => [...arr.slice(0, index), newItem, ...arr.slice(index)];
```

Si nous voulons placer un élément à un endroit précis dans un tableau, nous pouvons utiliser cette fonction spéciale `insert`.

Pour l'utiliser, il nous suffit de passer à `insert` le tableau que nous voulons transformer, l'index où nous voulons insérer l'élément, et l'élément à insérer.

C'est une excellente fonction à utiliser à la place de `.splice()` car elle ne modifie pas le tableau d'origine. Elle crée un nouveau tableau à l'aide de la méthode slice, en découpant le tableau en deux parties autour de l'index spécifié, puis en assemble un nouveau.

```js
const items = [1, 2, 4, 5];

// insérer le nombre 3 à l'index 2 :

insert(items, 2, 3); // [1, 2, 3, 4, 5]
```

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le découvrir par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C’est le cours que j’aurais aimé avoir quand j’ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*