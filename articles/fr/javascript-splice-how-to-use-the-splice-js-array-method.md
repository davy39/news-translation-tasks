---
title: JavaScript Splice – Comment utiliser la méthode de tableau JS .splice()
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-04-23T18:14:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-splice-how-to-use-the-splice-js-array-method
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/JavaScript-splice-method.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: JavaScript Splice – Comment utiliser la méthode de tableau JS .splice()
seo_desc: "The splice() method is a built-in method for JavaScript Array objects.\
  \ It lets you change the content of your array by removing or replacing existing\
  \ elements with new ones. \nThis method modifies the original array and returns\
  \ the removed elements as..."
---

La méthode `splice()` est une méthode intégrée pour les objets Array de JavaScript. Elle vous permet de modifier le contenu de votre tableau en supprimant ou en remplaçant des éléments existants par de nouveaux.

Cette méthode modifie le tableau d'origine et renvoie les éléments supprimés sous la forme d'un nouveau tableau.

Dans ce tutoriel, vous apprendrez comment supprimer, ajouter ou remplacer des éléments d'un tableau à l'aide de la méthode `splice()`. Commençons par la suppression d'éléments d'un tableau.

## Comment supprimer des éléments d'un tableau avec splice()

Par exemple, supposons que vous ayez un tableau nommé `months` mais que vous ayez des noms de jours dans le tableau comme suit :

```js
let months = ["January", "February", "Monday", "Tuesday"];
```

Vous pouvez utiliser la méthode `splice()` pour supprimer les noms de jours du tableau `months` et les ajouter à un nouveau tableau en même temps :

```js
let months = ["January", "February", "Monday", "Tuesday"];
let days = months.splice(2);

console.log(days); // ["Monday", "Tuesday"]
```

La méthode `splice()` nécessite au moins un paramètre, qui est l'index de départ (`start`) où l'opération splice commence. Dans le code ci-dessus, le nombre `2` est passé à la méthode, ce qui signifie que `splice()` commencera à supprimer des éléments à partir de l'index `2`.

Vous pouvez également définir le nombre d'éléments que vous souhaitez supprimer du tableau en passant un deuxième argument numérique connu sous le nom de `removeCount`. Par exemple, pour ne supprimer qu'un seul élément, vous pouvez passer le nombre `1` comme ceci :

```js
let months = ["January", "February", "Monday", "Tuesday"];
let days = months.splice(2, 1);

console.log(days); // ["Monday"]
console.log(months); // ["January", "February", "Tuesday"]
```

Lorsque vous omettez le paramètre `removeCount`, `splice()` supprimera tous les éléments de l'index de départ (`start`) jusqu'à la fin du tableau.

## Comment supprimer et ajouter des éléments d'un tableau avec splice()

La méthode vous permet également d'ajouter de nouveaux éléments juste après l'opération de suppression. Il vous suffit de passer les éléments que vous souhaitez ajouter au tableau après le nombre de suppressions.

La syntaxe complète de la méthode `splice()` est la suivante :

```js
Array.splice(start, removeCount, newItem, newItem, newItem, ...)
```

L'exemple suivant montre comment supprimer "Monday" et "Tuesday" tout en ajoutant "March" et "April" au tableau `months` :

```js
let months = ["January", "February", "Monday", "Tuesday"];
let days = months.splice(2, 2, "March", "April");

console.log(days); // ["Monday", "Tuesday"]
console.log(months); // ["January", "February", "March", "April"]

```

## Comment ajouter de nouveaux éléments à un tableau sans en supprimer

Enfin, vous pouvez ajouter de nouveaux éléments sans en supprimer aucun en passant le nombre `0` au paramètre `removeCount`. Lorsqu'aucun élément n'est supprimé, la méthode splice renvoie un tableau vide. Vous pouvez choisir de stocker le tableau vide renvoyé dans une variable ou non.

L'exemple suivant montre comment ajouter un nouvel élément `"March"` à côté de `"February"` sans supprimer d'éléments. Comme la méthode `splice()` renvoie un tableau vide, vous n'avez pas besoin de stocker le tableau renvoyé :

```js
let months = ["January", "February", "Monday", "Tuesday"];
months.splice(2, 0, "March");

console.log(months); 
// ["January", "February", "March", "Monday", "Tuesday"]
```

## Conclusion

Vous venez d'apprendre comment fonctionne la méthode `splice()`. Beau travail !

La méthode `splice()` est principalement utilisée lorsque vous devez supprimer ou ajouter de nouveaux éléments à un tableau. Dans certaines situations, vous pouvez également l'utiliser pour séparer un tableau qui a un contenu mixte comme dans le cas ci-dessus.

Lorsque vous supprimez `0` élément du tableau, la méthode renvoie simplement un tableau vide. Vous êtes toujours libre d'assigner le tableau renvoyé à une variable ou de l'ignorer.

## **Merci d'avoir lu ce tutoriel**

Si vous avez apprécié cet article et que vous souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre le JavaScript. Il fournit un guide étape par étape qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous aurez réellement l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !