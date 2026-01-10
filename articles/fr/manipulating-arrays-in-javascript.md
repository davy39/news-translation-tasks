---
title: Comment manipuler les tableaux en JavaScript
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-06-13T12:51:09.000Z'
originalURL: https://freecodecamp.org/news/manipulating-arrays-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_EK3RyHqvMS-ZIy9UyNMxTA--1-.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: arrays
  slug: arrays
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
seo_title: Comment manipuler les tableaux en JavaScript
seo_desc: 'An important part of any programming language. Most times we need to do
  several operations on arrays, hence this article.

  In this article, I would show you various methods of manipulating arrays in JavaScript
  [^^]

  What are Arrays in JavaScript?

  Befor...'
---

Une partie importante de tout langage de programmation. La plupart du temps, nous devons effectuer plusieurs opérations sur les tableaux, d'où cet article.

Dans cet article, je vais vous montrer diverses méthodes pour manipuler les tableaux en JavaScript 😊

### Qu'est-ce qu'un tableau en JavaScript ?

Avant de continuer, vous devez comprendre ce que signifient vraiment les tableaux.

> *En JavaScript, un tableau est une variable utilisée pour stocker différents types de données. Il stocke essentiellement différents éléments dans une seule boîte et peut être consulté plus tard avec la variable.*

Déclarer un tableau :

```javascript
let myBox = [];   // Déclaration initiale d'un tableau en JS
```

Les tableaux peuvent contenir plusieurs types de données

```javascript
let myBox = ['hello', 1, 2, 3, true, 'hi'];
```

Les tableaux peuvent être manipulés en utilisant plusieurs actions connues sous le nom de **méthodes**. Certaines de ces méthodes nous permettent d'ajouter, de supprimer, de modifier et de faire beaucoup plus avec les tableaux.

Je vais vous en montrer quelques-unes dans cet article, c'est parti :)

> *NB : J'ai utilisé les* ***fonctions fléchées*** *dans cet article. Si vous ne savez pas ce que cela signifie, vous devriez lire [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions). La fonction fléchée est une **fonctionnalité ES6**.

### toString()

La méthode JavaScript `toString()` convertit un tableau en une chaîne séparée par une virgule.

```javascript
let colors = ['green', 'yellow', 'blue'];

console.log(colors.toString()); // green,yellow,blue
```

### join()

La méthode JavaScript `join()` combine tous les éléments d'un tableau en une chaîne.

Elle est similaire à la méthode `toString()`, mais ici vous pouvez spécifier le séparateur au lieu de la virgule par défaut.

```javascript
let colors = ['green', 'yellow', 'blue'];

console.log(colors.join('-')); // green-yellow-blue
```

### concat

Cette méthode combine deux tableaux ensemble ou ajoute plus d'éléments à un tableau et retourne un nouveau tableau.

```javascript
let firstNumbers = [1, 2, 3];
let secondNumbers = [4, 5, 6];
let merged = firstNumbers.concat(secondNumbers);
console.log(merged); // [1, 2, 3, 4, 5, 6]
```

### push()

Cette méthode ajoute des éléments à la fin d'un tableau et **modifie** le tableau original.

```javascript
let browsers = ['chrome', 'firefox', 'edge'];
browsers.push('safari', 'opera mini');
console.log(browsers); 
// ["chrome", "firefox", "edge", "safari", "opera mini"]
```

### pop()

Cette méthode supprime le dernier élément d'un tableau et **le retourne**.

```javascript
let browsers = ['chrome', 'firefox', 'edge'];
browsers.pop(); // "edge"
console.log(browsers); // ["chrome", "firefox"]
```

### shift()

Cette méthode supprime le premier élément d'un tableau et **le retourne**.

```javascript
let browsers = ['chrome', 'firefox', 'edge'];
browsers.shift(); // "chrome"
console.log(browsers); // ["firefox", "edge"]
```

### unshift()

Cette méthode ajoute un ou plusieurs éléments au début d'un tableau et **modifie** le tableau original.

```javascript
let browsers = ['chrome', 'firefox', 'edge'];
browsers.unshift('safari');
console.log(browsers); //  ["safari", "chrome", "firefox", "edge"]
```

> *Vous pouvez également ajouter plusieurs éléments à la fois*

### splice()

Cette méthode **modifie** un tableau en ajoutant, supprimant et insérant des éléments.

La syntaxe est :

```python
array.splice(index[, deleteCount, element1, ..., elementN])
```

* `**Index**` ici est le point de départ pour supprimer des éléments dans le tableau
  
* `**deleteCount**` est le nombre d'éléments à supprimer à partir de cet index
  
* `**element1, ..., elementN**` est ou sont les éléments à ajouter
  

***Supprimer des éléments***

> *après avoir exécuté* ***splice()*** *, il retourne le tableau avec les éléments supprimés et les supprime du tableau original.*

```javascript
let colors = ['green', 'yellow', 'blue', 'purple'];
colors.splice(0, 3);
console.log(colors); // ["purple"]
// supprime ["green", "yellow", "blue"]
```

> ***NB*** : Le deleteCount n'inclut pas le dernier index dans la plage.

Si le deuxième paramètre n'est pas déclaré, chaque élément à partir de l'index donné sera supprimé du tableau :

```javascript
let colors = ['green', 'yellow', 'blue', 'purple'];
colors.splice(3);
console.log(colors); // ["green", "yellow", "blue"]
// supprime ['purple']
```

Dans l'exemple suivant, nous allons supprimer 3 éléments du tableau et les remplacer par d'autres éléments :

```javascript
let schedule = ['I', 'have', 'a', 'meeting', 'tommorrow'];
// supprime les 4 premiers éléments et les remplace par d'autres
schedule.splice(0, 4, 'we', 'are', 'going', 'to', 'swim');
console.log(schedule); 
// ["we", "are", "going", "to", "swim", "tommorrow"]
```

***Ajouter des éléments***

Pour ajouter des éléments, nous devons définir le `deleteCount` à zéro

```javascript
let schedule = ['I', 'have', 'a', 'meeting', 'with'];
// ajoute 3 nouveaux éléments au tableau
schedule.splice(5, 0, 'some', 'clients', 'tommorrow');
console.log(schedule); 
// ["I", "have", "a", "meeting", "with", "some", "clients", "tommorrow"]
```

### slice()

> *Cette méthode est similaire à* `splice()` *mais très différente. Elle retourne des sous-tableaux au lieu de sous-chaînes.*

Cette méthode **copie** une partie donnée d'un tableau et retourne cette partie copiée en tant que nouveau tableau. **Elle ne modifie pas le tableau original.**

La syntaxe est :

```python
array.slice(start, end)
```

Voici un exemple de base :

```javascript
let numbers = [1, 2, 3, 4]
numbers.slice(0, 3)
// retourne [1, 2, 3]
console.log(numbers) // retourne le tableau original
```

La meilleure façon d'utiliser `slice()` est de l'assigner à une nouvelle variable.

```javascript
let message = 'congratulations'
const abbrv = message.slice(0, 7) + 's!'; 
console.log(abbrv) // retourne "congrats!"
```

### split()

Cette méthode est utilisée pour les **chaînes**. Elle divise une chaîne en sous-chaînes et les retourne sous forme de tableau.

Voici la syntaxe : string.split(separator, limit);

* Le `**separator**` ici définit comment diviser une chaîne, soit par une virgule.
  
* Le `**limit**` détermine le nombre de divisions à effectuer
  

```javascript
let firstName = 'Bolaji';
// retourne la chaîne sous forme de tableau
firstName.split() // ["Bolaji"]
```

un autre exemple :

```javascript
let firstName = 'hello, my name is bolaji, I am a dev.';
firstName.split(',', 2); // ["hello", " my name is bolaji"]
```

> ***NB*** : *Si nous déclarons un tableau vide, comme ceci* `firstName.split('');` *alors chaque élément de la chaîne sera divisé en sous-chaînes* :

```javascript
let firstName = 'Bolaji';
firstName.split('') // ["B", "o", "l", "a", "j", "i"]
```

### indexOf()

Cette méthode recherche un élément dans un tableau et retourne **l'index** où il a été trouvé, sinon elle retourne `-1`

```javascript
let fruits = ['apple', 'orange', false, 3]
fruits.indexOf('orange'); // retourne 1
fruits.indexOf(3); // retourne 3
friuts.indexOf(null); // retourne -1 (non trouvé)
```

### lastIndexOf()

Cette méthode fonctionne de la même manière que **indexOf()** sauf qu'elle travaille de droite à gauche. Elle retourne le dernier index où l'élément a été trouvé

```javascript
let fruits = ['apple', 'orange', false, 3, 'apple']
fruits.lastIndexOf('apple'); // retourne 4
```

### filter()

Cette méthode crée un nouveau tableau si les éléments d'un tableau passent une certaine condition.

La syntaxe est :

```javascript
let results = array.filter(function(item, index, array) {
  // retourne true si l'élément passe le filtre
});
```

Exemple :

Vérifie les utilisateurs du Nigeria

```javascript
const countryCode = ['+234', '+144', '+233', '+234'];
const nigerian = countryCode.filter( code => code === '+234');
console.log(nigerian); // ["+234", "+234"]
```

### map()

Cette méthode crée un nouveau tableau en manipulant les valeurs d'un tableau.

Exemple :

Affiche les noms d'utilisateurs sur une page. (Affichage de base de la liste d'amis)

```javascript
const userNames = ['tina', 'danny', 'mark', 'bolaji'];
const display = userNames.map(item => {
return '<li>' + item + '</li>';
})
const render = '<ul>' + display.join('') + '</ul>';
document.write(render);
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*obuBZKFb5vKmUP7D4TX2XA.png align="left")

un autre exemple :

```javascript
// ajoute un signe dollar aux nombres
const numbers = [10, 3, 4, 6];
const dollars = numbers.map( number => '$' + number);
console.log(dollars);
// ['$10', '$3', '$4', '$6'];
```

### reduce()

Cette méthode est utile pour calculer des totaux.

**reduce()** est utilisé pour calculer une seule valeur basée sur un tableau.

```js
let value = array.reduce(function(previousValue, item, index, array) {
  // ...
}, initial);
```

exemple :

> *Pour parcourir un tableau et additionner tous les nombres du tableau, nous pouvons utiliser la boucle for of.*

```js
const numbers = [100, 300, 500, 70];
let sum = 0;
for (let n of numbers) {
sum += n;
}
console.log(sum);
```

Voici comment faire la même chose avec `reduce()`

```js
const numbers = [100, 300, 500, 70];
const sum = numbers.reduce((accummulator, value) =>
accummulator + value
, 0);
console.log(sum); // 970
```

> *Si vous omettez la valeur initiale, le total commencera par défaut à partir du premier élément du tableau.*

```js
const numbers = [100, 300, 500, 70];
const sum = numbers.reduce((accummulator, value) => accummulator + value);
console.log(sum); // retourne toujours 970
```

L'extrait suivant montre comment la méthode **reduce()** fonctionne avec les quatre arguments.

**source : MDN Docs**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cbd9qR_vy71qZjEQCFpCLQ.png align="left")

Plus d'informations sur la méthode **reduce()** et diverses façons de l'utiliser peuvent être trouvées [ici](https://medium.freecodecamp.org/reduce-f47a7da511a9) et [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce).

### forEach()

Cette méthode est utile pour itérer à travers un tableau.

Elle applique une fonction à tous les éléments d'un tableau

```js
const colors = ['green', 'yellow', 'blue'];
colors.forEach((item, index) => console.log(index, item));
// retourne l'index et chaque élément du tableau
// 0 "green"
// 1 "yellow"
// 2 "blue"
```

l'itération peut être faite sans passer l'argument index

```js
const colors = ['green', 'yellow', 'blue'];
colors.forEach((item) => console.log(item));
// retourne chaque élément du tableau
// "green"
// "yellow"
// "blue"
```

### every()

Cette méthode vérifie si tous les éléments d'un tableau passent la condition spécifiée et retourne `true` si c'est le cas, sinon `false`.

> *vérifie si tous les nombres sont positifs*

```js
const numbers = [1, -1, 2, 3];
let allPositive = numbers.every((value) => {
return value >= 0;
})
console.log(allPositive); // retournerait false
```

### some()

Cette méthode vérifie si un élément (un ou plusieurs) d'un tableau passe la condition spécifiée et retourne true si c'est le cas, sinon false.

> *vérifie si au moins un nombre est positif*

```js
const numbers = [1, -1, 2, 3];
let atLeastOnePositive = numbers.some((value) => {
return value >= 0;
})
console.log(atLeastOnePositive); // retournerait true
```

### includes()

Cette méthode vérifie si un tableau contient un certain élément. Elle est similaire à `.some()`, mais au lieu de chercher une condition spécifique à passer, elle vérifie si le tableau contient un élément spécifique.

```js
let users = ['paddy', 'zaddy', 'faddy', 'baddy'];
users.includes('baddy'); // retourne true
```

Si l'élément n'est pas trouvé, il retourne `false`

---

Il existe plus de méthodes de tableau, ceci n'est qu'une partie d'entre elles. De plus, il existe de nombreuses autres actions qui peuvent être effectuées sur les tableaux, essayez de consulter la documentation MDN [ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/) pour des informations plus approfondies.

### Résumé

* **toString()** convertit un tableau en une chaîne séparée par une virgule.
  
* **join()** combine tous les éléments d'un tableau en une chaîne.
  
* **concat** combine deux tableaux ensemble ou ajoute plus d'éléments à un tableau et retourne un nouveau tableau.
  
* **push()** ajoute un ou plusieurs éléments à la fin d'un tableau et **modifie** le tableau original.
  
* **pop()** supprime le dernier élément d'un tableau et **le retourne**
  
* **shift()** supprime le premier élément d'un tableau et **le retourne**
  
* **unshift()** ajoute un ou plusieurs éléments au début d'un tableau et **modifie** le tableau original.
  
* **splice()** **modifie** un tableau en ajoutant, supprimant et insérant des éléments.
  
* **slice()** copie une partie donnée d'un tableau et retourne cette partie copiée en tant que nouveau tableau. **Elle ne modifie pas le tableau original.**
  
* **split()** divise une chaîne en sous-chaînes et les retourne sous forme de tableau.
  
* **indexOf()** recherche un élément dans un tableau et retourne **l'index** où il a été trouvé, sinon il retourne `-1`
  
* **lastIndexOf()** recherche un élément de droite à gauche et retourne le dernier index où l'élément a été trouvé.
  
* **filter()** crée un nouveau tableau si les éléments d'un tableau passent une certaine condition.
  
* **map()** crée un nouveau tableau en manipulant les valeurs d'un tableau.
  
* **reduce()** calcule une seule valeur basée sur un tableau.
  
* **forEach()** itère à travers un tableau, il applique une fonction à tous les éléments d'un tableau
  
* **every()** vérifie si tous les éléments d'un tableau passent la condition spécifiée et retourne true si c'est le cas, sinon false.
  
* **some()** vérifie si un élément (un ou plusieurs) d'un tableau passe la condition spécifiée et retourne true si c'est le cas, sinon false.
  
* **includes()** vérifie si un tableau contient un certain élément.
  

---

Concluons ici ; les tableaux sont puissants et l'utilisation de méthodes pour les manipuler crée les algorithmes que les applications du monde réel utilisent.

Créons une petite fonction, une qui convertit un titre de publication en urlSlug.

> ***URL slug*** est l'adresse exacte d'une page ou d'une publication spécifique sur votre site.

Lorsque vous écrivez un article sur **Freecodecamp News** ou toute autre plateforme d'écriture, votre titre de publication est automatiquement converti en un slug avec les espaces blancs supprimés, les caractères convertis en minuscules et chaque mot du titre séparé par un trait d'union.

Voici une fonction de base qui fait cela en utilisant certaines des méthodes que nous venons d'apprendre.

```js
const url = 'https://bolajiayodeji.com/'
const urlSlug = (postTitle) => {
let postUrl = postTitle.toLowerCase().split(' ');
let postSlug = `${url}` + postUrl.join('-');
return postSlug;
}
let postTitle = 'Introduction to Chrome Lighthouse'
console.log(urlSlug(postTitle));
// https://bolajiayodeji.com/introduction-to-chrome-lighthouse
```

dans `postUrl`, nous convertissons la chaîne en minuscules puis nous utilisons la méthode **split()** pour convertir la chaîne en sous-chaînes et la retourner dans un tableau

```python
["introduction", "to", "chrome", "lighthouse"]
```

dans `post slug` nous joignons le tableau retourné avec un trait d'union puis nous le concaténons à la chaîne de catégorie et à l'`url` principale.

```js
let postSlug = `${url}` + postUrl.join('-');
postUrl.join('-') // introduction-to-chrome-lighthouse
```

C'est tout, assez simple, non ? :)

---

Si vous commencez tout juste avec JavaScript, vous devriez consulter ce dépôt [ici](https://github.com/BolajiAyodeji/js-code-snippets), je compile une liste d'extraits de code JavaScript de base allant de

* Tableaux
  
* Contrôle de flux
  
* Fonctions
  
* Objets
  
* Opérateurs
  

N'oubliez pas de mettre une étoile et de partager ! :)

PS : Cet article a été publié pour la première fois sur mon blog [ici](https://www.bolajiayodeji.com/manipulating-arrays-in-javascript/)