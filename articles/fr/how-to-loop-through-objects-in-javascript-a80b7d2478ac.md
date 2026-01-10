---
title: Comment parcourir les objets en JavaScript
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-06-29T17:25:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-loop-through-objects-in-javascript-a80b7d2478ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_H9NgZvI5oB0dEpzaQLjeg.jpeg
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
seo_title: Comment parcourir les objets en JavaScript
seo_desc: 'Once in a while, you may need to loop through objects in JavaScript. The
  only way to do so before ES6 was with a for...in loop.

  The problem with a for...in loop is that it iterates through properties in the Prototype
  chain. When you loop through an o...'
---

De temps en temps, vous devrez peut-être parcourir des objets en JavaScript. Avant ES6, la seule façon de le faire était avec une boucle `for...in`.

Le problème avec une boucle `for...in` est qu'elle itère à travers les propriétés de la chaîne de prototypes. Lorsque vous parcourez un objet avec la boucle `for...in`, vous devez vérifier si la propriété appartient à l'objet. Vous pouvez le faire avec `hasOwnProperty`.

```js
for (var property in object) {  if (object.hasOwnProperty(property)) {    // Faire des choses ici  }}
```

Nous n'avons plus besoin de nous appuyer sur `for...in` et `hasOwnProperty` maintenant. Il y a une meilleure façon.

### Une meilleure façon de parcourir les objets

La meilleure façon de parcourir les objets est **d'abord de convertir l'objet en un tableau. Ensuite, vous parcourez le tableau.**

Vous pouvez convertir un objet en un tableau avec trois méthodes :

1. `Object.keys`
2. `Object.values`
3. `Object.entries`

#### Object.keys

`Object.keys` crée un tableau qui contient les propriétés d'un objet. Voici un exemple.

```js
const fruits = { apple: 28, orange: 17, pear: 54 };
const keys = Object.keys(fruits);

console.log(keys); // ["apple", "orange", "pear"]
```

#### Object.values

`Object.values` crée un tableau qui contient les valeurs de chaque propriété d'un objet. Voici un exemple :

```js
const fruits = { apple: 28, orange: 17, pear: 54 };
const values = Object.values(fruits);

console.log(values); // [28, 17, 54]
```

#### Object.entries

`Object.entries` crée un tableau de tableaux. Chaque tableau interne contient deux éléments. Le premier élément est la propriété ; le second élément est la valeur.

Voici un exemple :

```js
const fruits = { apple: 28, orange: 17, pear: 54 };
const entries = Object.entries(fruits);

console.log(entries); // [["apple", 28], ["orange", 17], ["pear", 54]]
```

Ma préférée parmi les trois est `Object.entries`, car vous obtenez à la fois la clé et les valeurs des propriétés.

### Parcourir le tableau

Une fois que vous avez converti l'objet en un tableau avec `Object.keys`, `Object.values` ou `Object.entries`, vous pouvez le parcourir comme s'il s'agissait d'un tableau normal.

```js
const fruits = { apple: 28, orange: 17, pear: 54 };
// Parcourir les tableaux créés à partir de Object.keys
const keys = Object.keys(fruits);

for (const key of keys) {  
  console.log(keys);
}

// ["apple", "orange", "pear"]
// ["apple", "orange", "pear"]
// ["apple", "orange", "pear"]
```

Si vous utilisez `Object.entries`, vous pourriez vouloir [déstructurer](https://zellwk.com/blog/es6) le tableau en sa clé et sa propriété.

```
const fruits = { apple: 28, orange: 17, pear: 54 };
const entries = Object.entries(fruits);

for (const [fruit, count] of entries) {
  console.log(`There are ${count} ${fruit}s`);
}

// "There are 28 apples"
// "There are 17 oranges"
// "There are 54 pears"
```

### Conclusion

La meilleure façon de parcourir les objets est d'abord de les convertir en un tableau avec l'une de ces trois méthodes.

1. `Object.keys`
2. `Object.values`
3. `Object.entries`

Ensuite, vous parcourez les résultats comme un tableau normal.

Si cette leçon vous a aidé, vous pourriez apprécier [Learn JavaScript](https://learnjavascript.today/), où vous apprendrez à construire tout ce que vous voulez à partir de zéro. L'inscription pour Learn JavaScript ouvre en juillet 2018 (très bientôt !).

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Looping%20through%20objects%20in%20JavaScript%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/looping-through-js-objects/&hashtags=); vous pourriez aider quelqu'un qui se sentait comme vous avant de lire l'article. Merci.

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/looping-through-js-objects). Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.