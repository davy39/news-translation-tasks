---
title: Insertion dans un tableau JavaScript - Comment ajouter à un tableau avec les
  fonctions Push, Unshift et Concat
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-25T21:36:59.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-insert-how-to-add-to-an-array-with-the-push-unshift-and-concat-functions
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Hello--my-name-is-Matthew.-Nice-to-meet-you..png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: Web Development
  slug: web-development
seo_title: Insertion dans un tableau JavaScript - Comment ajouter à un tableau avec
  les fonctions Push, Unshift et Concat
seo_desc: "By Nehemiah Kivelevitz\nJavaScript arrays are easily one of my favorite\
  \ data types. They are dynamic, easy to use, and offer a whole bunch of built-in\
  \ methods we can take advantage of. \nHowever, the more options you have the more\
  \ confusing it can be t..."
---

Par Nehemiah Kivelevitz

Les tableaux JavaScript sont facilement l'un de mes types de données préférés. Ils sont dynamiques, faciles à utiliser et offrent toute une série de méthodes intégrées dont nous pouvons tirer parti. 

Cependant, plus vous avez d'options, plus il peut être difficile de décider laquelle utiliser. 

Dans cet article, je souhaite discuter de certaines méthodes courantes pour ajouter un élément à un tableau JavaScript.

### Voici un Scrim interactif sur comment ajouter à un tableau 

<iframe src="https://scrimba.com/scrim/cLwq7WCZ?pl=pd9ZLcW&embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>


## La méthode Push

La première et probablement la méthode de tableau JavaScript la plus courante que vous rencontrerez est _push()_. La méthode push() est utilisée pour ajouter un élément à la fin d'un tableau. 

Supposons que vous avez un tableau d'éléments, chaque élément étant une chaîne représentant une tâche que vous devez accomplir. Il serait logique d'ajouter les nouveaux éléments à la fin du tableau afin que nous puissions terminer nos tâches précédentes en premier. 

Regardons l'exemple sous forme de code :

```javascript
const arr = ['Premier élément', 'Deuxième élément', 'Troisième élément'];

arr.push('Quatrième élément');

console.log(arr); // ['Premier élément', 'Deuxième élément', 'Troisième élément', 'Quatrième élément']
```

Très bien, push nous a donc donné une syntaxe simple et agréable pour ajouter un élément à la fin de notre tableau. 

Supposons que nous voulions ajouter deux ou trois éléments à la fois à notre liste, que ferions-nous alors ? Il s'avère que _push()_ peut accepter plusieurs éléments à ajouter en une seule fois. 

```javascript
const arr = ['Premier élément', 'Deuxième élément', 'Troisième élément'];

arr.push('Quatrième élément', 'Cinquième élément');

console.log(arr); // ['Premier élément', 'Deuxième élément', 'Troisième élément', 'Quatrième élément', 'Cinquième élément']
```

Maintenant que nous avons ajouté quelques tâches supplémentaires à notre tableau, nous pourrions vouloir savoir combien d'éléments se trouvent actuellement dans notre tableau pour déterminer si nous avons trop à faire. 

Heureusement, _push()_ a une valeur de retour avec la longueur du tableau après que nos élément(s) ont été ajoutés.

```javascript
const arr = ['Premier élément', 'Deuxième élément', 'Troisième élément'];

const arrLength = arr.push('Quatrième élément', 'Cinquième élément');

console.log(arrLength); // 5 
console.log(arr); // ['Premier élément', 'Deuxième élément', 'Troisième élément', 'Quatrième élément', 'Cinquième élément']
```

## La méthode Unshift

Toutes les tâches ne sont pas créées égales. Vous pourriez rencontrer un scénario dans lequel vous ajoutez des tâches à votre tableau et soudainement vous tombez sur une tâche plus urgente que les autres. 

Il est temps de présenter notre ami _unshift()_ qui nous permet d'ajouter des éléments au début de notre tableau. 

```javascript
const arr = ['Premier élément', 'Deuxième élément', 'Troisième élément'];

const arrLength = arr.unshift('Élément urgent 1', 'Élément urgent 2');

console.log(arrLength); // 5 
console.log(arr); // ['Élément urgent 1', 'Élément urgent 2', 'Premier élément', 'Deuxième élément', 'Troisième élément']
```

Vous pouvez remarquer dans l'exemple ci-dessus que, tout comme la méthode _push()_, _unshift()_ retourne la nouvelle longueur du tableau pour que nous puissions l'utiliser. Elle nous donne également la possibilité d'ajouter plus d'un élément à la fois. 

## La méthode Concat

Abréviation de concatenate (lier ensemble), la méthode _concat()_ est utilisée pour joindre deux (ou plus) tableaux ensemble. 

Si vous vous souvenez de ce qui précède, les méthodes _unshift()_ et _push()_ retournent la longueur du nouveau tableau. _concat()_, en revanche, retournera un tableau complètement nouveau. 

C'est une distinction très importante et rend _concat()_ extrêmement utile lorsque vous traitez avec des tableaux que vous ne voulez pas muter (comme les tableaux stockés dans l'état React).

Voici à quoi pourrait ressembler un cas assez basique et simple :

```javascript
const arr1 = ['?', '?'];
const arr2 = ['?', '?'];

const arr3 = arr1.concat(arr2);

console.log(arr3); // ["?", "?", "?", "?"] 

```

Supposons que vous avez plusieurs tableaux que vous souhaitez joindre ensemble. Pas de problème, _concat()_ est là pour sauver la journée !

```javascript
const arr1 = ['?', '?'];
const arr2 = ['?', '?'];
const arr3 = ['?', '?'];

const arr4 = arr1.concat(arr2,arr3);

console.log(arr4); // ["?", "?", "?", "?", "?", "?"]

```

### Voici un scrim interactif pour vous aider à mieux comprendre cela :

<iframe src="https://scrimba.com/scrim/cZa9DZsz?pl=pd9ZLcW&embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

### Clonage avec Concat

Vous souvenez-vous quand j'ai dit que _concat()_ peut être utile lorsque vous ne voulez pas muter votre tableau existant ? Regardons comment nous pouvons utiliser ce concept pour copier le contenu d'un tableau dans un nouveau tableau.

```javascript
const arr1 = ["?", "?", "?", "?", "?", "?"];

const arr2 = [].concat(arr1);

arr2.push("?");

console.log(arr1) //["?", "?", "?", "?", "?", "?"]
console.log(arr2) //["?", "?", "?", "?", "?", "?", "?"]
```

Super ! Nous pouvons essentiellement "cloner" un tableau en utilisant _concat()_. 

Mais il y a un petit "piège" dans ce processus de clonage. Le nouveau tableau est une "copie superficielle" du tableau copié. Cela signifie que tout objet est **copié par référence** et non l'objet réel. 

Regardons un exemple pour expliquer cette idée plus clairement.

```javascript
const arr1 = [{food:"?"}, {food:"?"}, {food:"?"}]

const arr2 = [].concat(arr1);

// change à la fois arr1 et arr2
arr2[1].food = "!";
// change seulement arr2
arr2.push({food:"*"})

console.log(arr1) // [ { food: '?' }, { food: '!' }, { food: '?' } ]

console.log(arr2) // [ { food: '?' }, { food: '!' }, { food: '?' }, { food: '*' } ] 
```

Même si nous n'avons pas **directement** apporté de modifications à notre tableau original, le tableau a finalement été affecté par les modifications que nous avons apportées à notre tableau cloné ! 

Il existe plusieurs façons différentes de faire correctement un "clonage profond" d'un tableau, mais je vous laisse cela comme devoir. 

## TL;DR

Lorsque vous voulez ajouter un élément à la fin de votre tableau, utilisez _push()_. Si vous devez ajouter un élément au début de votre tableau, essayez _unshift()_. Et vous pouvez ajouter des tableaux ensemble en utilisant _concat()_. 

Il existe certainement de nombreuses autres options pour ajouter des éléments à un tableau, et je vous invite à aller découvrir d'autres méthodes de tableau ! 

N'hésitez pas à me contacter sur [Twitter](https://twitter.com/nehemiahkiv) et faites-moi savoir votre méthode de tableau préférée pour ajouter des éléments à un tableau.