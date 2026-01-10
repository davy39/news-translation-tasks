---
title: Un Guide Sur La Méthode Reduce En JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-11T04:14:17.000Z'
originalURL: https://freecodecamp.org/news/reduce-f47a7da511a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7Lt21vtHVtY6j0oBWNDd4w.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Un Guide Sur La Méthode Reduce En JavaScript
seo_desc: 'By Josh Pitzalis

  JavaScript’s reduce method is one of the cornerstones of functional programming.
  Let’s explore how it works, when you should use it, and some of the cool things
  it can do.

  A Basic Reduction

  Use it when: You have an array of amounts a...'
---

Par Josh Pitzalis

La méthode **reduce** de JavaScript est l'un des piliers de la programmation fonctionnelle. Explorons comment elle fonctionne, quand l'utiliser et certaines des choses intéressantes qu'elle peut faire.

#### Une Réduction Basique

**Utilisez-la lorsque** : Vous avez un tableau de montants et vous voulez tous les additionner.

```js
const euros = [29.76, 41.85, 46.5];

const sum = euros.reduce((total, amount) => total + amount); 

sum // 118.11
```

Comment l'utiliser :

* Dans cet exemple, Reduce accepte deux paramètres, le total et le montant actuel.
* La méthode reduce parcourt chaque nombre du tableau, comme le ferait une boucle for.
* Lorsque la boucle commence, la valeur totale est le nombre le plus à gauche (29.76) et le montant actuel est celui à côté (41.85).
* Dans cet exemple particulier, nous voulons ajouter le montant actuel au total.
* Le calcul est répété pour chaque montant du tableau, mais à chaque fois, la valeur actuelle change pour le nombre suivant dans le tableau, en se déplaçant vers la droite.
* Lorsque plus aucun nombre ne reste dans le tableau, la méthode retourne la valeur totale.

#### **La Version ES5 De La Méthode Reduce En JavaScript**

Si vous n'avez jamais utilisé la syntaxe ES6 auparavant, ne vous laissez pas intimider par l'exemple ci-dessus. C'est exactement la même chose que d'écrire :

```js
var euros = [29.76, 41.85, 46.5]; 

var sum = euros.reduce( function(total, amount){
  return total + amount
});

sum // 118.11
```

Nous utilisons `const` au lieu de `var` et nous remplaçons le mot `function` par une "flèche grasse" (`=>`) après les paramètres, et nous omettons le mot 'return'.

J'utiliserai la syntaxe ES6 pour le reste des exemples, car elle est plus concise et laisse moins de place aux erreurs.

#### Trouver Une Moyenne Avec La Méthode Reduce En JavaScript

Au lieu de journaliser la somme, vous pourriez diviser la somme par la longueur du tableau avant de retourner une valeur finale.

La façon de faire cela est de tirer parti des autres arguments de la méthode reduce. Le premier de ces arguments est l'_index_. Comme une boucle for, l'index fait référence au nombre de fois que le réducteur a parcouru le tableau. Le dernier argument est le _tableau_ lui-même.

```js
const euros = [29.76, 41.85, 46.5];

const average = euros.reduce((total, amount, index, array) => {
  total += amount;
  if( index === array.length-1) { 
    return total/array.length;
  }else { 
    return total;
  }
});

average // 39.37
```

#### Map Et Filter Comme Réductions

Si vous pouvez utiliser la fonction reduce pour calculer une moyenne, alors vous pouvez l'utiliser de la manière que vous voulez.

Par exemple, vous pourriez doubler le total, ou diviser chaque nombre par deux avant de les additionner, ou utiliser une instruction if à l'intérieur du réducteur pour n'additionner que les nombres supérieurs à 10. Mon propos est que la _Méthode Reduce En JavaScript_ vous donne un mini CodePen où vous pouvez écrire la logique que vous voulez. _Elle_ répétera la logique pour chaque montant du tableau puis retournera une seule valeur.

Le fait est que vous n'avez pas toujours à retourner une seule valeur. Vous pouvez réduire un tableau en un nouveau tableau.

Par exemple, réduisons un tableau de montants en un autre tableau où chaque montant est doublé. Pour cela, nous devons définir la valeur initiale de notre accumulateur à un tableau vide.

La valeur initiale est la valeur du paramètre total lorsque la réduction commence. Vous définissez la valeur initiale en ajoutant une virgule suivie de votre valeur initiale à l'intérieur des parenthèses mais après les accolades (**en gras dans l'exemple ci-dessous**).

```js
const average = euros.reduce((total, amount, index, array) => {
  total += amount
  return total/array.length
}, 0);
```

Dans les exemples précédents, la valeur initiale était zéro, donc je l'ai omise. En omettant la valeur initiale, le _total_ prendra par défaut le premier montant du tableau.

En définissant la valeur initiale à un tableau vide, nous pouvons ensuite pousser chaque _montant_ dans le _total_. Si nous voulons réduire un tableau de valeurs en un autre tableau où chaque valeur est doublée, nous devons pousser le _montant_ * 2. Ensuite, nous retournons le total lorsqu'il n'y a plus de montants à pousser.

```js
const euros = [29.76, 41.85, 46.5];

const doubled = euros.reduce((total, amount) => {
  total.push(amount * 2);
  return total;
}, []);

doubled // [59.52, 83.7, 93]
```

Nous avons créé un nouveau tableau où chaque montant est doublé. Nous pourrions également filtrer les nombres que nous ne voulons pas doubler en ajoutant une instruction if à l'intérieur de notre réducteur.

```js
const euro = [29.76, 41.85, 46.5];

const above30 = euro.reduce((total, amount) => {
  if (amount > 30) {
    total.push(amount);
  }
  return total;
}, []);

above30 // [ 41.85, 46.5 ]
```

Ces opérations sont les méthodes _map_ et _filter_ réécrites comme une méthode reduce.

Pour ces exemples, il serait plus logique d'utiliser map ou filter car ils sont plus simples à utiliser. L'avantage d'utiliser reduce se manifeste lorsque vous voulez mapper et filtrer ensemble et que vous avez beaucoup de données à parcourir.

Si vous enchaînez map et filter ensemble, vous faites le travail deux fois. Vous filtrez chaque valeur puis vous mappez les valeurs restantes. Avec reduce, vous pouvez filtrer puis mapper en une seule passe.

Utilisez map et filter, mais lorsque vous commencez à enchaîner beaucoup de méthodes ensemble, vous savez maintenant qu'il est plus rapide de réduire les données à la place.

#### Créer Un Compteur Avec La Méthode Reduce En JavaScript

**Utilisez-la lorsque** : Vous avez une collection d'objets et vous voulez savoir combien de chaque objet se trouve dans la collection.

```js
const fruitBasket = ['banana', 'cherry', 'orange', 'apple', 'cherry', 'orange', 'apple', 'banana', 'cherry', 'orange', 'fig' ];

const count = fruitBasket.reduce( (tally, fruit) => {
  tally[fruit] = (tally[fruit] || 0) + 1 ;
  return tally;
} , {})

count // { banana: 2, cherry: 3, orange: 3, apple: 2, fig: 1 }
```

Pour compter les objets dans un tableau, notre valeur initiale doit être un objet vide, et non un tableau vide comme dans le dernier exemple.

Puisque nous allons retourner un objet, nous pouvons maintenant stocker des paires clé-valeur dans le total.

```js
fruitBasket.reduce( (tally, fruit) => {
  tally[fruit] = 1;
  return tally;
}, {})
```

Lors de notre première passe, nous voulons que le nom de la première clé soit notre valeur actuelle et nous voulons lui donner une valeur de 1.

Cela nous donne un objet avec tous les fruits comme clés, chacun avec une valeur de 1. Nous voulons que la quantité de chaque fruit augmente s'ils se répètent.

Pour cela, lors de notre deuxième boucle, nous vérifions si notre total contient une clé avec le fruit actuel du réducteur. Si ce n'est pas le cas, nous la créons. Si c'est le cas, nous incrémentons la quantité de un.

```js
fruitBasket.reduce((tally, fruit) => {
  if (!tally[fruit]) {
    tally[fruit] = 1;
  } else {
    tally[fruit] = tally[fruit] + 1;
  }
  return tally;
}, {});
```

J'ai réécrit exactement la même logique de manière plus concise ci-dessus.

#### Aplanir Un Tableau De Tableaux Avec La Méthode Reduce En JavaScript

Nous pouvons utiliser reduce pour aplatir des montants imbriqués en un seul tableau.

Nous définissons la valeur initiale à un tableau vide puis nous concaténons la valeur actuelle au total.

```js
const data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

const flat = data.reduce((total, amount) => {
  return total.concat(amount);
}, []);

flat // [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
```

Plus souvent qu'autrement, les informations sont imbriquées de manière plus compliquée. Par exemple, disons que nous voulons simplement toutes les couleurs dans la variable de données ci-dessous.

```js
const data = [
  {a: 'happy', b: 'robin', c: ['blue','green']}, 
  {a: 'tired', b: 'panther', c: ['green','black','orange','blue']}, 
  {a: 'sad', b: 'goldfish', c: ['green','red']}
];
```

Nous allons parcourir chaque objet et extraire les couleurs. Nous faisons cela en pointant amount.c pour chaque objet du tableau. Nous utilisons ensuite une boucle forEach pour pousser chaque valeur du tableau imbriqué dans notre total.

```js
const colors = data.reduce((total, amount) => {
  amount.c.forEach( color => {
      total.push(color);
  })
  return total;
}, [])

colors //['blue','green','green','black','orange','blue','green','red']
```

Si nous avons besoin uniquement de nombres uniques, nous pouvons vérifier si le nombre existe déjà dans _total_ avant de le pousser.

```js
const uniqueColors = data.reduce((total, amount) => {
  amount.c.forEach( color => {
    if (total.indexOf(color) === -1){
     total.push(color);
    }
  });
  return total;
}, []);

uniqueColors // [ 'blue', 'red', 'green', 'black', 'orange']
```

#### Piping Avec Reduce

Un aspect intéressant de la méthode reduce en JavaScript est que vous pouvez réduire sur des fonctions ainsi que sur des nombres et des chaînes.

Disons que nous avons une collection de fonctions mathématiques simples. Ces fonctions nous permettent d'incrémenter, de décrémenter, de doubler et de diviser par deux un montant.

```js
function increment(input) { return input + 1;}

function decrement(input) { return input — 1; }

function double(input) { return input * 2; }

function halve(input) { return input / 2; }
```

Pour une raison quelconque, nous devons incrémenter, puis doubler, puis décrémenter un montant.

Vous pourriez écrire une fonction qui prend une entrée et retourne (input + 1) * 2 -1. Le problème est que nous savons que nous allons devoir incrémenter le montant trois fois, puis le doubler, puis le décrémenter, et enfin le diviser par deux à un moment donné dans le futur. Nous ne voulons pas avoir à réécrire notre fonction chaque fois, donc nous allons utiliser reduce pour créer un pipeline.

Un pipeline est un terme utilisé pour une liste de fonctions qui transforment une valeur initiale en une valeur finale. Notre pipeline sera constitué de nos trois fonctions dans l'ordre où nous voulons les utiliser.

```js
let pipeline = [increment, double, decrement];
```

Au lieu de réduire un tableau de valeurs, nous réduisons notre pipeline de fonctions. Cela fonctionne parce que nous définissons la valeur initiale comme le montant que nous voulons transformer.

```js
const result = pipeline.reduce(function(total, func) {
  return func(total);
}, 1);

result // 3
```

Parce que le pipeline est un tableau, il peut être facilement modifié. Si nous voulons décrémenter quelque chose trois fois, puis le doubler, le décrémenter et le diviser par deux, nous modifions simplement le pipeline.

```js
var pipeline = [

  increment,
  
  increment,
  
  increment,
  
  double,
  
  decrement,
  
  halve
  
];
```

La fonction reduce reste exactement la même.

#### Erreurs Silencieuses À Éviter

Si vous ne passez pas de valeur initiale, reduce supposera que le premier élément de votre tableau est votre valeur initiale. Cela a bien fonctionné dans les premiers exemples car nous additionnions une liste de nombres.

Si vous essayez de compter des fruits et que vous oubliez la valeur initiale, les choses deviennent étranges. Ne pas entrer de valeur initiale est une erreur facile à faire et l'une des premières choses à vérifier lors du débogage.

Une autre erreur courante est d'oublier de retourner le total. Vous devez retourner quelque chose pour que la fonction reduce fonctionne. Vérifiez toujours et assurez-vous que vous retournez bien la valeur que vous voulez.

**Outils, Conseils & Références**

* Tout dans cet article provient d'une fantastique série de vidéos sur egghead appelée [Introducing Reduce](https://egghead.io/courses/reduce-data-with-javascript). Je donne tout le crédit à [Mykola Bilokonsky](https://twitter.com/mykola) et je lui suis reconnaissant pour tout ce que je sais maintenant sur l'utilisation de la Méthode Reduce En JavaScript. J'ai essayé de réécrire beaucoup de ce qu'il explique avec mes propres mots comme exercice pour mieux comprendre chaque concept. De plus, il est plus facile pour moi de référencer un article, plutôt qu'une vidéo, lorsque j'ai besoin de me rappeler comment faire quelque chose.
* La [documentation MDN Reduce](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) appelle ce que j'ai appelé un _total_ l'`accumulator`. Il est important de le savoir car la plupart des gens l'appelleront un accumulateur si vous en lisez en ligne. Certaines personnes l'appellent `prev` comme dans _valeur précédente_. Tout cela fait référence à la même chose. J'ai trouvé plus facile de penser à un _total_ lorsque j'apprenais reduce.
* Si vous souhaitez pratiquer l'utilisation de reduce, je recommande de vous inscrire à [freeCodeCamp](https://www.freecodecamp.com/) et de compléter autant que possible les [algorithmes intermédiaires](https://www.freecodecamp.com/map-aside#nested-collapseIntermediateAlgorithmScripting) en utilisant reduce.
* Si les variables 'const' dans les extraits d'exemples vous sont nouvelles, j'ai écrit un autre article sur [les variables ES6 et pourquoi vous pourriez vouloir les utiliser](https://medium.com/@joshpitzalis/es6-variables-and-why-you-might-want-to-use-them-fbc84ce27262#.981ejmn1f).
* J'ai également écrit un article intitulé [The Trouble With Loops](https://medium.com/@joshpitzalis/the-trouble-with-loops-f639e3cc52d9#.8xkmhn7z6) qui explique comment utiliser map() et filter() si elles vous sont nouvelles.

Merci d'avoir lu ! Si vous souhaitez être informé lorsque j'écris un nouvel article, veuillez [entrer votre email](https://tinyletter.com/joshpitzalis) ici.

Et si vous avez aimé l'article, veuillez le partager sur les réseaux sociaux pour que d'autres puissent le trouver.