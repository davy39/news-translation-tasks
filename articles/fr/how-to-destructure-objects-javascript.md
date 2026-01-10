---
title: Comment déstructurer des objets en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-21T16:47:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-destructure-objects-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/code--f7df1e--3-.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment déstructurer des objets en JavaScript
seo_desc: "By Madison Kanna\nSince ECMAScript 6 (or ES6 for short), you can descructure\
  \ objects in JavaScript. As a JavaScript developer, you’ll likely destructure objects\
  \ as part of your daily work. \nLet's learn about why we use destructuring, and\
  \ then we'll le..."
---

Par Madison Kanna

Depuis ECMAScript 6 (ou ES6 en abrégé), vous pouvez déstructurer des objets en JavaScript. En tant que développeur JavaScript, vous déstructurerez probablement des objets dans le cadre de votre travail quotidien. 

Apprenons pourquoi nous utilisons la déstructuration, puis nous apprendrons comment déstructurer des objets JavaScript.

<h1>Pourquoi déstructurer un objet ?</h1>

Passons en revue un exemple pour nous aider à comprendre pourquoi nous voudrions déstructurer un objet en premier lieu. Créons un objet avec le nom de `pet` :

```javascript
const pet = {
  name: 'Captain',
  food: 'Kibble',
  color: 'Black'
};
```

Disons que nous voulons simplement imprimer la nourriture de l'animal. Nous pourrions le faire comme ceci :

```
console.log(pet.food);
```

Cela afficherait `kibble` dans la console. Cependant, il est fastidieux d'écrire `pet.name` chaque fois que nous avons besoin de la valeur de la nourriture. Avant ES6, les développeurs JavaScript faisaient donc ceci :

```
const food = pet.food;
```

Ici, nous déclarons une variable nommée `food` et nous disons de pointer cette variable vers la valeur stockée dans `pet.food`, qui est `kibble`. Nous pouvons démontrer que nous avons fait cela en ajoutant cette ligne de code :

```js
console.log(food); // sortie : kibble
```

Cependant, disons que nous voulons faire de même avec le reste de nos propriétés dans l'objet `pet` :

```js
const name = pet.name;
const food = pet.food;
const color = pet.color;
```

Cela commence à devenir verbeux. C'est là que la **déstructuration** entre en jeu.

<h1>Comment déstructurer un objet en JavaScript</h1>

Au lieu d'écrire `const food = pet.food`, nous pouvons utiliser la déstructuration et simplement écrire : 

```
const { food } = pet;
```

Maintenant, si nous imprimons à nouveau `food`, nous pouvons voir que nous avons créé la variable `food` :

```js
console.log(food); // sortie : kibble
```

En utilisant la déstructuration, notre code est maintenant plus concis et sec. C'est pourquoi les développeurs JavaScript ont commencé à utiliser la déstructuration une fois qu'elle a été introduite dans ES6. 

Faisons une pause un instant et regardons à nouveau cette ligne : 

```
const { food } = pet;
```

Que se passe-t-il ici ?

Rappelez-vous, dans un objet JavaScript, une **propriété** est une paire clé/valeur. La clé est une chaîne de caractères, et la valeur peut être de n'importe quel type de données. Dans l'objet `pet`, l'une des clés est `food`, et sa valeur correspondante est `kibble`.  

Lorsque nous enveloppons notre variable `food` dans des crochets, nous cherchons à l'intérieur de notre objet `pet` une propriété avec le même nom. Nous créons une nouvelle variable avec le nom `food`, et nous définissons sa valeur à `kibble`, la valeur correspondante de cette clé.

Si vous souhaitez déstructurer plusieurs propriétés et leurs clés à partir d'un objet, vous pouvez le faire comme ceci :

```
const { name, food, color } = pet;
```

Maintenant, si vous imprimez ces variables, vous verrez qu'elles existent toutes :

```js
console.log(name, food, color) // sortie : captain chewtoy black
```

Dans cet article, nous avons appris comment déstructurer des objets et pourquoi nous le ferions. Nous avons également appris comment déstructurer plusieurs propriétés à partir d'un objet.

Merci d'avoir lu !

**Si vous avez aimé cet article, rejoignez mon [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f), où nous relevons des défis de codage ensemble chaque dimanche et nous soutenons mutuellement alors que nous apprenons de nouvelles technologies.**

**Si vous avez des commentaires ou des questions sur cet article, ou trouvez-moi sur Twitter [@madisonkanna](https://twitter.com/Madisonkanna).**