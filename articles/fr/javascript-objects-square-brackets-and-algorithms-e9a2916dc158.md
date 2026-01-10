---
title: Objets JavaScript, crochets et algorithmes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-10T20:58:59.000Z'
originalURL: https://freecodecamp.org/news/javascript-objects-square-brackets-and-algorithms-e9a2916dc158
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UNpp95VAxeCcyKy8z6w_oA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: software development
  slug: software-development
seo_title: Objets JavaScript, crochets et algorithmes
seo_desc: 'By Dmitri Grabov

  One of the most powerful aspects of JavaScript is being able to dynamically refer
  to properties of objects. In this article we will look at how this works and what
  advantages this might give us. We will take a quick look at some of t...'
---

Par Dmitri Grabov

L'un des aspects les plus puissants de JavaScript est la possibilité de faire référence dynamiquement aux propriétés des objets. Dans cet article, nous allons examiner comment cela fonctionne et quels avantages cela peut nous apporter. Nous allons jeter un rapide coup d'œil à certaines des structures de données utilisées en informatique. De plus, nous allons examiner quelque chose appelé la notation Big O, qui est utilisée pour décrire la performance d'un algorithme.

### Introduction aux objets

Commençons par créer un objet simple représentant une voiture. Chaque objet a quelque chose appelé des `propriétés`. Une propriété est une variable qui appartient à un objet. Notre objet voiture aura trois propriétés : `make`, `model` et `color`.

Voyons à quoi cela pourrait ressembler :

```
const car = {  make: 'Ford',  model: 'Fiesta',  color: 'Red'};
```

Nous pouvons faire référence aux propriétés individuelles d'un objet en utilisant la notation par point. Par exemple, si nous voulons savoir quelle est la couleur de notre voiture, nous pouvons utiliser la notation par point comme ceci `car.color`.

Nous pourrions même l'afficher en utilisant `console.log` :

```
console.log(car.color); //sortie : Red
```

Une autre façon de faire référence à une propriété est d'utiliser la notation par crochets :

```
console.log(car['color']); //sortie : Red
```

Dans l'exemple ci-dessus, nous utilisons le nom de la propriété sous forme de chaîne de caractères à l'intérieur des crochets pour obtenir la valeur correspondant à ce nom de propriété. L'avantage de la notation par crochets est que nous pouvons également utiliser des variables pour obtenir des propriétés de manière dynamique.

C'est-à-dire, plutôt que de coder en dur un nom de propriété spécifique, nous pouvons le spécifier sous forme de chaîne de caractères dans une variable :

```
const propertyName = 'color';const console.log(car[propertyName]); //sortie : Red
```

### Utilisation de la recherche dynamique avec la notation par crochets

Examinons un exemple où nous pouvons utiliser cela. Supposons que nous gérons un restaurant et que nous voulons pouvoir obtenir les prix des articles de notre menu. Une façon de faire cela est d'utiliser des instructions `if/else`.

Écrivons une fonction qui acceptera un nom d'article et retournera un prix :

```
function getPrice(itemName){  if(itemName === 'burger') {    return 10;  } else if(itemName === 'fries') {    return 3;  } else if(itemName === 'coleslaw') {    return 4;  } else if(itemName === 'coke') {    return 2;  } else if(itemName === 'beer') {    return 5;  }}
```

Bien que l'approche ci-dessus fonctionne, elle n'est pas idéale. Nous avons codé en dur le menu dans notre code. Maintenant, si notre menu change, nous devrons réécrire notre code et le redéployer. De plus, nous pourrions avoir un long menu et devoir écrire tout ce code serait fastidieux.

Une meilleure approche serait de séparer nos données et notre logique. Les données contiendront notre menu et la logique recherchera les prix à partir de ce menu.

Nous pouvons représenter le `menu` sous forme d'objet où le nom de la propriété, également appelé clé, correspond à une valeur.

Dans ce cas, la clé sera le nom de l'article et la valeur sera le prix de l'article :

```
const menu = {  burger: 10,  fries: 3,  coleslaw: 4,  coke: 2,  beer: 5};
```

En utilisant la notation par crochets, nous pouvons créer une fonction qui acceptera deux arguments :

* un objet menu
* une chaîne avec le nom de l'article

et retournera le prix de cet article :

```
const menu = {  burger: 10,  fries: 3,  coleslaw: 4,  coke: 2,  beer: 5};
```

```
function getPrice(itemName, menu){  const itemPrice = menu[itemName];  return itemPrice;}
```

```
const priceOfBurger = getPrice('burger', menu);console.log(priceOfBurger); // sortie : 10
```

L'avantage de cette approche est que nous avons séparé nos données de notre logique. Dans cet exemple, les données résident dans notre code, mais elles pourraient tout aussi bien provenir d'une base de données ou d'une API. Elles ne sont plus étroitement couplées avec notre logique de recherche qui convertit le nom de l'article en prix de l'article.

### Structures de données et algorithmes

Une map en termes d'informatique est une structure de données qui est une collection de paires clé/valeur où chaque clé correspond à une valeur correspondante. Nous pouvons l'utiliser pour rechercher une valeur qui correspond à une clé spécifique. C'est ce que nous faisons dans l'exemple précédent. Nous avons une clé qui est un nom d'article et nous pouvons rechercher le prix correspondant de cet article en utilisant notre objet menu. Nous utilisons un objet pour implémenter une structure de données de map.

Examinons un exemple de pourquoi nous pourrions vouloir utiliser une map. Supposons que nous gérons une librairie et que nous avons une liste de livres. Chaque livre a un identifiant unique appelé International Standard Book Number (ISBN), qui est un nombre à 13 chiffres. Nous stockons nos livres dans un tableau et voulons pouvoir les rechercher en utilisant l'ISBN.

Une façon de faire cela est de parcourir le tableau, de vérifier la valeur ISBN de chaque livre et, si elle correspond, de le retourner :

```
const books = [{  isbn: '978-0099540946',  author: 'Mikhail Bulgakov',  title: 'Master and Margarita'}, {  isbn: '978-0596517748',  author: 'Douglas Crockford',  title: 'JavaScript: The Good Parts'}, {  isbn: '978-1593275846',  author: 'Marijn Haverbeke',  title: 'Eloquent JavaScript'}];
```

```
function getBookByIsbn(isbn, books){  for(let i = 0; i < books.length; i++){    if(books[i].isbn === isbn) {      return books[i];    }  }}
```

```
const myBook = getBookByIsbn('978-1593275846', books);
```

Cela fonctionne bien dans cet exemple puisque nous n'avons que trois livres (c'est une petite librairie). Cependant, si nous étions Amazon, parcourir des millions de livres pourrait être très lent et coûteux en termes de calcul.

La [notation Big O](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation/) est utilisée en informatique pour décrire la performance d'un algorithme. Par exemple, si _n_ est le nombre de livres dans notre collection, le coût de l'utilisation de l'itération pour rechercher un livre dans le pire des cas (le livre que nous recherchons est le dernier de la liste) sera _O(n)_. Cela signifie que si le nombre de livres dans notre collection double, le coût de recherche d'un livre en utilisant l'itération doublera également.

Examinons comment nous pouvons rendre notre algorithme plus efficace en utilisant une structure de données différente.

Comme discuté, une map peut être utilisée pour rechercher la valeur qui correspond à une clé. Nous pouvons structurer nos données sous forme de map au lieu d'un tableau en utilisant un objet.

La clé sera l'ISBN et la valeur sera l'objet livre correspondant :

```
const books = {  '978-0099540946':{    isbn: '978-0099540946',    author: 'Mikhail Bulgakov',    title: 'Master and Margarita'  },  '978-0596517748': {    isbn: '978-0596517748',    author: 'Douglas Crockford',    title: 'JavaScript: The Good Parts'  },  '978-1593275846': {    isbn: '978-1593275846',    author: 'Marijn Haverbeke',    title: 'Eloquent JavaScript'  }};
```

```
function getBookByIsbn(isbn, books){  return books[isbn];}
```

```
const myBook = getBookByIsbn('978-1593275846', books);
```

Au lieu d'utiliser l'itération, nous pouvons maintenant utiliser une simple recherche de map par ISBN pour obtenir notre valeur. Nous n'avons plus besoin de vérifier la valeur ISBN pour chaque objet. Nous obtenons la valeur directement à partir de la map en utilisant la clé.

En termes de performance, une recherche de map offrira une énorme amélioration par rapport à l'itération. Cela est dû au fait que la recherche de map a un coût constant en termes de calcul. Cela peut être écrit en utilisant la notation Big O comme _O(1)_. Il n'a pas d'importance si nous avons trois ou trois millions de livres, nous pouvons obtenir le livre que nous voulons tout aussi rapidement en effectuant une recherche de map en utilisant la clé ISBN.

### Récapitulatif

* Nous avons vu que nous pouvons accéder aux valeurs des propriétés d'objet en utilisant la notation par point et la notation par crochets
* Nous avons appris comment nous pouvons rechercher dynamiquement les valeurs des propriétés en utilisant des variables avec la notation par crochets
* Nous avons également appris qu'une structure de données de map associe des clés à des valeurs. Nous pouvons utiliser des clés pour rechercher directement des valeurs dans une map que nous implémentons en utilisant un objet.
* Nous avons jeté un premier coup d'œil à la manière dont la performance des algorithmes est décrite en utilisant la notation _Big O_. De plus, nous avons vu comment nous pouvons améliorer la performance d'une recherche en convertissant un tableau d'objets en une map et en utilisant une recherche directe plutôt qu'une itération.

Vous voulez tester vos nouvelles compétences ? Essayez l'exercice [Crash Override](https://www.codewars.com/kata/crash-override/javascript) sur Codewars.

Vous voulez apprendre à écrire des applications web en utilisant JavaScript ? Je dirige [Constructor Labs](http://constructorlabs.com/), un bootcamp de codage [JavaScript](http://constructorlabs.com/course) de 12 semaines à Londres. Les technologies enseignées incluent **HTML**, **CSS**, **JavaScript**, **React**, **Redux**, **Node** et **Postgres**. Tout ce dont vous avez besoin pour créer une application web complète à partir de zéro et obtenir votre premier emploi dans l'industrie. Les frais sont de £3,000 et la prochaine cohorte commence le 29 mai. [Les candidatures sont ouvertes maintenant](http://constructorlabs.com/admission).