---
title: Principes de la programmation fonctionnelle en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-17T17:20:19.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-principles-in-javascript-1b8fc6c3563f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JyVlvqwsCBYl2FuvPFVRZQ.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Principes de la programmation fonctionnelle en JavaScript
seo_desc: 'By TK

  After a long time learning and working with object-oriented programming, I took
  a step back to think about system complexity.


  “Complexity is anything that makes software hard to understand or to modify." —
  John Outerhout


  Doing some research, ...'
---

Par TK

Après avoir passé beaucoup de temps à apprendre et à travailler avec la programmation orientée objet, j'ai fait un pas en arrière pour réfléchir à la complexité des systèmes.

> « La complexité est tout ce qui rend le logiciel difficile à comprendre ou à modifier. » — John Outerhout

En faisant quelques recherches, j'ai découvert des concepts de programmation fonctionnelle comme l'immuabilité et les fonctions pures. Ces concepts permettent de créer des fonctions sans effets secondaires, ce qui facilite la maintenance des systèmes — avec quelques autres [avantages](https://hackernoon.com/why-functional-programming-matters-c647f56a7691).

Dans cet article, je vais vous en dire plus sur la programmation fonctionnelle et quelques concepts importants, avec beaucoup d'exemples de code en JavaScript.

### Qu'est-ce que la programmation fonctionnelle ?

> La programmation fonctionnelle est un paradigme de programmation — un style de construction de la structure et des éléments des programmes informatiques — qui traite le calcul comme l'évaluation de fonctions mathématiques et évite les changements d'état et les données mutables — [Wikipedia](https://en.wikipedia.org/wiki/Functional_programming)

#### Fonctions pures

![Image](https://cdn-media-1.freecodecamp.org/images/0*FMur6URY7yAVjeuP)
_« goutte d'eau » par [Unsplash](https://unsplash.com/@martinmohan?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Mohan Murugesan</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Le premier concept fondamental que nous apprenons lorsque nous voulons comprendre la programmation fonctionnelle est celui des **fonctions pures**. Mais que signifie réellement ce terme ? Qu'est-ce qui rend une fonction pure ?

Alors, comment savoir si une fonction est `pure` ou non ? Voici une définition très stricte de la pureté :

* Elle retourne le même résultat si on lui donne les mêmes arguments (on parle aussi de fonction `déterministe`)
* Elle ne provoque aucun effet secondaire observable

#### Elle retourne le même résultat si on lui donne les mêmes arguments

Imaginons que nous voulons implémenter une fonction qui calcule l'aire d'un cercle. Une fonction impure recevrait `radius` comme paramètre, puis calculerait `radius * radius * PI` :

```js
let PI = 3.14;

const calculateArea = (radius) => radius * radius * PI;

calculateArea(10); // retourne 314.0
```

Pourquoi cette fonction est-elle impure ? Tout simplement parce qu'elle utilise un objet global qui n'a pas été passé en paramètre à la fonction.

Maintenant, imaginons que des mathématiciens soutiennent que la valeur de `PI` est en réalité `[42](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy#Answer_to_the_Ultimate_Question_of_Life,_the_Universe,_and_Everything_(42))` et changent la valeur de l'objet global.

Notre fonction impure retournera maintenant `10 * 10 * 42` = `4200`. Pour le même paramètre (`radius = 10`), nous avons un résultat différent.

Corrigeons cela !

```js
let PI = 3.14;

const calculateArea = (radius, pi) => radius * radius * pi;

calculateArea(10, PI); // retourne 314.0
```

Maintenant, nous passerons toujours la valeur de `PI` en tant que paramètre à la fonction. Ainsi, nous n'accédons qu'aux paramètres passés à la fonction. Aucun `objet externe`.

* Pour les paramètres `radius = 10` et `PI = 3.14`, nous aurons toujours le même résultat : `314.0`
* Pour les paramètres `radius = 10` et `PI = 42`, nous aurons toujours le même résultat : `4200`

#### Lecture de fichiers

Si notre fonction lit des fichiers externes, ce n'est pas une fonction pure — le contenu du fichier peut changer.

```js
const charactersCounter = (text) => `Nombre de caractères : ${text.length}`;

function analyzeFile(filename) {
  let fileContent = open(filename);
  return charactersCounter(fileContent);
}
```

#### Génération de nombres aléatoires

Toute fonction qui dépend d'un générateur de nombres aléatoires ne peut pas être pure.

```js
function yearEndEvaluation() {
  if (Math.random() > 0.5) {
    return "Vous obtenez une augmentation !";
  } else {
    return "Meilleure chance l'année prochaine !";
  }
}
```

#### Elle ne provoque aucun effet secondaire observable

Des exemples d'effets secondaires observables incluent la modification d'un objet global ou d'un paramètre passé par référence.

Maintenant, nous voulons implémenter une fonction pour recevoir une valeur entière et retourner la valeur augmentée de 1.

```js
let counter = 1;

function increaseCounter(value) {
  counter = value + 1;
}

increaseCounter(counter);
console.log(counter); // 2
```

Nous avons la valeur `counter`. Notre fonction impure reçoit cette valeur et réassigne le compteur avec la valeur augmentée de 1.

```js
let counter = 1;

const increaseCounter = (value) => value + 1;

increaseCounter(counter); // 2
console.log(counter); // 1
```

**Observation** : la mutabilité est découragée en programmation fonctionnelle.

Nous modifions l'objet global. Mais comment la rendre `pure` ? Il suffit de retourner la valeur augmentée de 1.

Voyez que notre fonction pure `increaseCounter` retourne 2, mais la valeur `counter` reste la même. La fonction retourne la valeur incrémentée sans altérer la valeur de la variable.

Si nous suivons ces deux règles simples, il devient plus facile de comprendre nos programmes. Maintenant, chaque fonction est isolée et incapable d'impacter d'autres parties de notre système.

Les fonctions pures sont stables, cohérentes et prévisibles. Étant donné les mêmes paramètres, les fonctions pures retourneront toujours le même résultat. Nous n'avons pas besoin de penser à des situations où le même paramètre donne des résultats différents — car cela n'arrivera jamais.

#### Avantages des fonctions pures

Le code est définitivement plus facile à tester. Nous n'avons pas besoin de simuler quoi que ce soit. Ainsi, nous pouvons tester les fonctions pures avec différents contextes :

* Étant donné un paramètre `A` → s'attendre à ce que la fonction retourne la valeur `B`
* Étant donné un paramètre `C` → s'attendre à ce que la fonction retourne la valeur `D`

Un exemple simple serait une fonction pour recevoir une collection de nombres et s'attendre à ce qu'elle incrémente chaque élément de cette collection.

```js
let list = [1, 2, 3, 4, 5];

const incrementNumbers = (list) => list.map(number => number + 1);
```

Nous recevons le tableau `numbers`, utilisons `map` pour incrémenter chaque nombre et retournons une nouvelle liste de nombres incrémentés.

```js
incrementNumbers(list); // [2, 3, 4, 5, 6]
```

Pour l'`input` `[1, 2, 3, 4, 5]`, l'`output` attendu serait `[2, 3, 4, 5, 6]`.

#### Immuabilité

> Inchangé dans le temps ou incapable d'être changé.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MGlzHgISuw0dXwsf)
_« enseigne lumineuse de changement » par [Unsplash](https://unsplash.com/@rossf?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Ross Findon</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Lorsque les données sont immuables, leur état ne peut pas changer après leur création. Si vous voulez changer un objet immuable, vous ne pouvez pas. Au lieu de cela, vous créez un nouvel objet avec la nouvelle valeur.

En JavaScript, nous utilisons couramment la boucle `for`. Cette instruction `for` suivante a quelques variables mutables.

```js
var values = [1, 2, 3, 4, 5];
var sumOfValues = 0;

for (var i = 0; i < values.length; i++) {
  sumOfValues += values[i];
}

sumOfValues // 15
```

Pour chaque itération, nous changeons l'état de `i` et de `sumOfValue`. Mais comment gérer la mutabilité dans l'itération ? Avec la récursivité.

```js

let list = [1, 2, 3, 4, 5];
let accumulator = 0;

function sum(list, accumulator) {
  if (list.length == 0) {
    return accumulator;
  }

  return sum(list.slice(1), accumulator + list[0]);
}

sum(list, accumulator); // 15
list; // [1, 2, 3, 4, 5]
accumulator; // 0
```

Ainsi, nous avons la fonction `sum` qui reçoit un vecteur de valeurs numériques. La fonction s'appelle elle-même jusqu'à ce que nous obtenions la liste vide ([notre cas de base de récursivité](https://en.wikipedia.org/wiki/Recursion_(computer_science)#Recursive_functions_and_algorithms)). Pour chaque "itération", nous ajouterons la valeur à l'accumulateur `total`.

Avec la récursivité, nous gardons nos variables immuables. Les variables `list` et `accumulator` ne sont pas modifiées. Elles conservent la même valeur.

**Observation** : Nous pouvons utiliser `reduce` pour implémenter cette fonction. Nous aborderons ce sujet dans la section sur les fonctions d'ordre supérieur.

Il est également très courant de construire l'état final d'un objet. Imaginons que nous avons une chaîne de caractères et que nous voulons transformer cette chaîne en un `slug d'URL`.

En programmation orientée objet en Ruby, nous créerions une classe, disons `UrlSlugify`. Et cette classe aurait une méthode `slugify` pour transformer l'entrée de chaîne en un `slug d'URL`.

```js
class UrlSlugify
  attr_reader :text
  
  def initialize(text)
    @text = text
  end

  def slugify!
    text.downcase!
    text.strip!
    text.gsub!(' ', '-')
  end
end

UrlSlugify.new(' I will be a url slug   ').slugify! # "i-will-be-a-url-slug"
```

C'est implémenté !

Ici, nous avons une programmation impérative qui dit exactement ce que nous voulons faire dans chaque processus `slugify` — d'abord en minuscules, puis enlever les espaces blancs inutiles et, enfin, remplacer les espaces blancs restants par des tirets.

Mais nous mutons l'état de l'entrée dans ce processus.

Nous pouvons gérer cette mutation en faisant de la composition de fonctions, ou de l'enchaînement de fonctions. En d'autres termes, le résultat d'une fonction sera utilisé comme entrée pour la fonction suivante, sans modifier la chaîne d'entrée originale.

```js
const string = " I will be a url slug   ";

const slugify = string =>
  string
    .toLowerCase()
    .trim()
    .split(" ")
    .join("-");

slugify(string); // i-will-be-a-url-slug
```

Ici, nous avons :

* `toLowerCase` : convertit la chaîne en minuscules
* `trim` : supprime les espaces blancs des deux extrémités d'une chaîne
* `split` et `join` : remplace toutes les instances de correspondance par un remplacement dans une chaîne donnée

Nous combinons toutes ces 4 fonctions et nous pouvons "slugifier" notre chaîne.

#### Transparence référentielle

![Image](https://cdn-media-1.freecodecamp.org/images/0*K0VAbQjAwmKZb1at)
_« personne tenant des lunettes » par [Unsplash](https://unsplash.com/@joshcala?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Josh Calabrese</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Implémentons une `fonction carré` :

```js
const square = (n) => n * n;
```

Cette fonction pure aura toujours la même sortie, étant donné la même entrée.

```js
square(2); // 4
square(2); // 4
square(2); // 4
// ...
```

Passer `2` comme paramètre de la `fonction carré` retournera toujours 4. Donc maintenant nous pouvons remplacer `square(2)` par 4. Notre fonction est `référentiellement transparente`.

En gros, si une fonction produit constamment le même résultat pour la même entrée, elle est référentiellement transparente.

fonctions pures + données immuables = transparence référentielle

Avec ce concept, une chose intéressante que nous pouvons faire est de [mémoïser](https://en.wikipedia.org/wiki/Memoization) la fonction. Imaginons que nous avons cette fonction :

```js
const sum = (a, b) => a + b;
```

Et nous l'appelons avec ces paramètres :

```js
sum(3, sum(5, 8));
```

La fonction `sum(5, 8)` est égale à `13`. Cette fonction retournera toujours `13`. Donc nous pouvons faire ceci :

```js
sum(3, 13);
```

Et cette expression retournera toujours `16`. Nous pouvons remplacer toute l'expression par une constante numérique et la [mémoïser](https://en.wikipedia.org/wiki/Memoization).

#### Fonctions en tant qu'entités de première classe

![Image](https://cdn-media-1.freecodecamp.org/images/0*K6m1Ftw54Wm6tfFB)
_« première classe » par [Unsplash](https://unsplash.com/@andrewtneel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Andrew Neel</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

L'idée des fonctions en tant qu'entités de première classe est que les fonctions sont également traitées comme des valeurs et utilisées comme des données.

Les fonctions en tant qu'entités de première classe peuvent :

* y faire référence à partir de constantes et de variables
* la passer en tant que paramètre à d'autres fonctions
* la retourner en tant que résultat d'autres fonctions

L'idée est de traiter les fonctions comme des valeurs et de passer des fonctions comme des données. De cette façon, nous pouvons combiner différentes fonctions pour créer de nouvelles fonctions avec de nouveaux comportements.

Imaginons que nous avons une fonction qui additionne deux valeurs puis double la valeur. Quelque chose comme ceci :

```js
const doubleSum = (a, b) => (a + b) * 2;
```

Maintenant, une fonction qui soustrait des valeurs et retourne le double :

```js
const doubleSubtraction = (a, b) => (a - b) * 2;
```

Ces fonctions ont une logique similaire, mais la différence est les fonctions opérateurs. Si nous pouvons traiter les fonctions comme des valeurs et les passer comme arguments, nous pouvons construire une fonction qui reçoit la fonction opérateur et l'utilise à l'intérieur de notre fonction.

```js
const sum = (a, b) => a + b;
const subtraction = (a, b) => a - b;

const doubleOperator = (f, a, b) => f(a, b) * 2;

doubleOperator(sum, 3, 1); // 8
doubleOperator(subtraction, 3, 1); // 4
```

Maintenant, nous avons un argument `f`, et nous l'utilisons pour traiter `a` et `b`. Nous avons passé les fonctions `sum` et `subtraction` pour composer avec la fonction `doubleOperator` et créer un nouveau comportement.

#### Fonctions d'ordre supérieur

Lorsque nous parlons de fonctions d'ordre supérieur, nous parlons d'une fonction qui soit :

* prend une ou plusieurs fonctions comme arguments, ou
* retourne une fonction comme résultat

La fonction `doubleOperator` que nous avons implémentée ci-dessus est une fonction d'ordre supérieur car elle prend une fonction opérateur comme argument et l'utilise.

Vous avez probablement déjà entendu parler de `filter`, `map` et `reduce`. Examinons ceux-ci.

#### Filter

Étant donné une collection, nous voulons filtrer par un attribut. La fonction de filtrage attend une valeur `true` ou `false` pour déterminer si l'élément doit ou non être inclus dans la collection de résultats. Basiquement, si l'expression de rappel est `true`, la fonction de filtrage inclura l'élément dans la collection de résultats. Sinon, elle ne l'inclura pas.

Un exemple simple est lorsque nous avons une collection d'entiers et que nous voulons uniquement les nombres pairs.

#### **Approche impérative**

Une façon impérative de le faire avec JavaScript est de :

* créer un tableau vide `evenNumbers`
* itérer sur le tableau `numbers`
* pousser les nombres pairs dans le tableau `evenNumbers`

```js
var numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var evenNumbers = [];

for (var i = 0; i < numbers.length; i++) {
  if (numbers[i] % 2 == 0) {
    evenNumbers.push(numbers[i]);
  }
}

console.log(evenNumbers); // (6) [0, 2, 4, 6, 8, 10]
```

Nous pouvons également utiliser la fonction d'ordre supérieur `filter` pour recevoir la fonction `even`, et retourner une liste de nombres pairs :

```js
const even = n => n % 2 == 0;
const listOfNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
listOfNumbers.filter(even); // [0, 2, 4, 6, 8, 10]
```

Un problème intéressant que j'ai résolu sur [Hacker Rank FP](https://www.hackerrank.com/domains/fp) Path était le [problème Filter Array](https://www.hackerrank.com/challenges/fp-filter-array/problem). L'idée du problème est de filtrer un tableau donné d'entiers et de ne sortir que les valeurs inférieures à une valeur spécifiée `X`.

Une solution impérative JavaScript à ce problème serait quelque chose comme :

```js
var filterArray = function(x, coll) {
  var resultArray = [];

  for (var i = 0; i < coll.length; i++) {
    if (coll[i] < x) {
      resultArray.push(coll[i]);
    }
  }

  return resultArray;
}

console.log(filterArray(3, [10, 9, 8, 2, 7, 5, 1, 3, 0])); // (3) [2, 1, 0]
```

Nous disons exactement ce que notre fonction doit faire — itérer sur la collection, comparer l'élément courant de la collection avec `x`, et pousser cet élément dans `resultArray` s'il passe la condition.

#### **Approche déclarative**

Mais nous voulons une manière plus déclarative de résoudre ce problème, et utiliser également la fonction d'ordre supérieur `filter`.

Une solution JavaScript déclarative serait quelque chose comme ceci :

```js
function smaller(number) {
  return number < this;
}

function filterArray(x, listOfNumbers) {
  return listOfNumbers.filter(smaller, x);
}

let numbers = [10, 9, 8, 2, 7, 5, 1, 3, 0];

filterArray(3, numbers); // [2, 1, 0]
```

Utiliser `this` dans la fonction `smaller` semble un peu étrange au premier abord, mais est facile à comprendre.

`this` sera le deuxième paramètre dans la fonction `filter`. Dans ce cas, `3` (le `x`) est représenté par `this`. C'est tout.

Nous pouvons également faire cela avec des maps. Imaginons que nous avons une map de personnes avec leur `name` et `age`.

```js
let people = [
  { name: "TK", age: 26 },
  { name: "Kaio", age: 10 },
  { name: "Kazumi", age: 30 }
];
```

Et nous voulons filtrer uniquement les personnes au-dessus d'une valeur d'âge spécifiée, dans cet exemple les personnes qui ont plus de 21 ans.

```js
const olderThan21 = person => person.age > 21;
const overAge = people => people.filter(olderThan21);
overAge(people); // [{ name: 'TK', age: 26 }, { name: 'Kazumi', age: 30 }]
```

Résumé du code :

* nous avons une liste de personnes (avec `name` et `age`).
* nous avons une fonction `olderThan21`. Dans ce cas, pour chaque personne dans le tableau people, nous voulons accéder à l'`age` et voir s'il est plus vieux que 21.
* nous filtrons toutes les personnes sur la base de cette fonction.

#### Map

L'idée de map est de transformer une collection.

> La méthode `map` transforme une collection en appliquant une fonction à tous ses éléments et en construisant une nouvelle collection à partir des valeurs retournées.

Prenons la même collection `people` ci-dessus. Nous ne voulons pas filtrer par "âge supérieur" maintenant. Nous voulons simplement une liste de chaînes, quelque chose comme `TK a 26 ans`. Donc la chaîne finale pourrait être `:name a :age ans` où `:name` et `:age` sont des attributs de chaque élément dans la collection `people`.

En JavaScript impératif, ce serait :

```js
var people = [
  { name: "TK", age: 26 },
  { name: "Kaio", age: 10 },
  { name: "Kazumi", age: 30 }
];

var peopleSentences = [];

for (var i = 0; i < people.length; i++) {
  var sentence = people[i].name + " a " + people[i].age + " ans";
  peopleSentences.push(sentence);
}

console.log(peopleSentences); // ['TK a 26 ans', 'Kaio a 10 ans', 'Kazumi a 30 ans']

```

En JavaScript déclaratif, ce serait :

```js
const makeSentence = (person) => `${person.name} a ${person.age} ans`;

const peopleSentences = (people) => people.map(makeSentence);
  
peopleSentences(people);
// ['TK a 26 ans', 'Kaio a 10 ans', 'Kazumi a 30 ans']
```

L'idée est de transformer un tableau donné en un nouveau tableau.

Un autre problème intéressant de Hacker Rank était le [problème de mise à jour de liste](https://www.hackerrank.com/challenges/fp-update-list/problem). Nous voulons simplement mettre à jour les valeurs d'un tableau donné avec leurs valeurs absolues.

Par exemple, l'entrée `[1, 2, 3, -4, 5]` doit donner la sortie `[1, 2, 3, 4, 5]`. La valeur absolue de `-4` est `4`.

Une solution simple serait une mise à jour en place pour chaque valeur de la collection.

```js
var values = [1, 2, 3, -4, 5];

for (var i = 0; i < values.length; i++) {
  values[i] = Math.abs(values[i]);
}

console.log(values); // [1, 2, 3, 4, 5]
```

Nous utilisons la fonction `Math.abs` pour transformer la valeur en sa valeur absolue, et faisons la mise à jour en place.

Ce n'est **pas** une manière fonctionnelle d'implémenter cette solution.

Premièrement, nous avons appris l'immuabilité. Nous savons à quel point l'immuabilité est importante pour rendre nos fonctions plus cohérentes et prévisibles. L'idée est de construire une nouvelle collection avec toutes les valeurs absolues.

Deuxièmement, pourquoi ne pas utiliser `map` ici pour "transformer" toutes les données ?

Ma première idée était de tester la fonction `Math.abs` pour gérer une seule valeur.

```js
Math.abs(-1); // 1
Math.abs(1); // 1
Math.abs(-2); // 2
Math.abs(2); // 2
```

Nous voulons transformer chaque valeur en une valeur positive (la valeur absolue).

Maintenant que nous savons comment faire l'"absolue" pour une valeur, nous pouvons utiliser cette fonction pour la passer en argument à la fonction `map`. Vous vous souvenez qu'une `fonction d'ordre supérieur` peut recevoir une fonction comme argument et l'utiliser ? Oui, map peut le faire !

```js
let values = [1, 2, 3, -4, 5];

const updateListMap = (values) => values.map(Math.abs);

updateListMap(values); // [1, 2, 3, 4, 5]
```

Waouh. Si beau !

#### Reduce

L'idée de reduce est de recevoir une fonction et une collection, et de retourner une valeur créée en combinant les éléments.

Un exemple courant dont les gens parlent est d'obtenir le montant total d'une commande. Imaginez que vous êtes sur un site de shopping. Vous avez ajouté `Produit 1`, `Produit 2`, `Produit 3` et `Produit 4` à votre panier (commande). Maintenant, nous voulons calculer le montant total du panier.

De manière impérative, nous itérerions la liste des commandes et additionnerions chaque montant de produit au montant total.

```js
var orders = [
  { productTitle: "Produit 1", amount: 10 },
  { productTitle: "Produit 2", amount: 30 },
  { productTitle: "Produit 3", amount: 20 },
  { productTitle: "Produit 4", amount: 60 }
];

var totalAmount = 0;

for (var i = 0; i < orders.length; i++) {
  totalAmount += orders[i].amount;
}

console.log(totalAmount); // 120
```

En utilisant `reduce`, nous pouvons construire une fonction pour gérer la `somme des montants` et la passer comme argument à la fonction `reduce`.

```js
let shoppingCart = [
  { productTitle: "Produit 1", amount: 10 },
  { productTitle: "Produit 2", amount: 30 },
  { productTitle: "Produit 3", amount: 20 },
  { productTitle: "Produit 4", amount: 60 }
];

const sumAmount = (currentTotalAmount, order) => currentTotalAmount + order.amount;

const getTotalAmount = (shoppingCart) => shoppingCart.reduce(sumAmount, 0);

getTotalAmount(shoppingCart); // 120
```

Ici, nous avons `shoppingCart`, la fonction `sumAmount` qui reçoit le `currentTotalAmount` actuel, et l'objet `order` pour les `somme`.

La fonction `getTotalAmount` est utilisée pour `réduire` le `shoppingCart` en utilisant le `sumAmount` et en commençant par `0`.

Une autre façon d'obtenir le montant total est de composer `map` et `reduce`. Que veux-je dire par là ? Nous pouvons utiliser `map` pour transformer le `shoppingCart` en une collection de valeurs `amount`, puis simplement utiliser la fonction `reduce` avec la fonction `sumAmount`.

```js
const getAmount = (order) => order.amount;
const sumAmount = (acc, amount) => acc + amount;

function getTotalAmount(shoppingCart) {
  return shoppingCart
    .map(getAmount)
    .reduce(sumAmount, 0);
}

getTotalAmount(shoppingCart); // 120
```

La fonction `getAmount` reçoit l'objet produit et retourne uniquement la valeur `amount`. Donc ce que nous avons ici est `[10, 30, 20, 60]`. Et ensuite, le `reduce` combine tous les éléments en les additionnant. Magnifique !

Nous avons examiné comment chaque fonction d'ordre supérieur fonctionne. Je veux vous montrer un exemple de la façon dont nous pouvons composer les trois fonctions dans un exemple simple.

En parlant de "panier d'achat", imaginons que nous avons cette liste de produits dans notre commande :

```js
let shoppingCart = [
  { productTitle: "Programmation Fonctionnelle", type: "livres", amount: 10 },
  { productTitle: "Kindle", type: "électronique", amount: 30 },
  { productTitle: "Chaussures", type: "mode", amount: 20 },
  { productTitle: "Clean Code", type: "livres", amount: 60 }
]
```

Nous voulons le montant total de tous les livres dans notre panier. C'est aussi simple que cela. L'algorithme ?

* filtrer par type de livre
* transformer le panier en une collection de montants en utilisant map
* combiner tous les éléments en les additionnant avec reduce

```js
let shoppingCart = [
  { productTitle: "Programmation Fonctionnelle", type: "livres", amount: 10 },
  { productTitle: "Kindle", type: "électronique", amount: 30 },
  { productTitle: "Chaussures", type: "mode", amount: 20 },
  { productTitle: "Clean Code", type: "livres", amount: 60 }
]

const byBooks = (order) => order.type == "livres";
const getAmount = (order) => order.amount;
const sumAmount = (acc, amount) => acc + amount;

function getTotalAmount(shoppingCart) {
  return shoppingCart
    .filter(byBooks)
    .map(getAmount)
    .reduce(sumAmount, 0);
}

getTotalAmount(shoppingCart); // 70
```

Terminé !

#### Ressources

J'ai organisé quelques ressources que j'ai lues et étudiées. Je partage celles que j'ai trouvées vraiment intéressantes. Pour plus de ressources, visitez mon [dépôt GitHub sur la programmation fonctionnelle](https://github.com/LeandroTk/learning-functional-programming)

* [Cours EcmaScript 6 par Wes Bos](https://ES6.io/friend/LEANDRO)
* [JavaScript par OneMonth](https://mbsy.co/lFtbC)
* [Ressources spécifiques à Ruby](https://github.com/LeandroTk/learning-functional-programming/tree/master/ruby)
* [Ressources spécifiques à Javascript](https://github.com/LeandroTk/learning-functional-programming/tree/master/javascript)
* [Ressources spécifiques à Clojure](https://github.com/LeandroTk/learning-functional-programming/tree/master/clojure)
* [Apprendre React en construisant une application](https://alterclass.io/?ref=5ec57f513c1321001703dcd2)

#### Introductions

* [Apprendre la programmation fonctionnelle en JS](https://www.youtube.com/watch?v=e-5obm1G_FY)
* [Introduction à la programmation fonctionnelle avec Python](https://codewords.recurse.com/issues/one/an-introduction-to-functional-programming)
* [Aperçu de la programmation fonctionnelle](https://blog.codeship.com/overview-of-functional-programming)
* [Une introduction rapide au JavaScript fonctionnel](https://hackernoon.com/a-quick-introduction-to-functional-javascript-7e6fe520e7fa)
* [Qu'est-ce que la programmation fonctionnelle ?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0)
* [Jargon de la programmation fonctionnelle](https://github.com/hemanth/functional-programming-jargon)

#### Fonctions pures

* [Qu'est-ce qu'une fonction pure ?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976)
* [Programmation fonctionnelle pure 1](https://www.fpcomplete.com/blog/2017/04/pure-functional-programming)
* [Programmation fonctionnelle pure 2](https://www.fpcomplete.com/blog/2017/05/pure-functional-programming-part-2)

#### Données immuables

* [Structures de données immuables pour la programmation fonctionnelle](https://www.youtube.com/watch?v=Wo0qiGPSV-s)
* [Pourquoi l'état mutable partagé est la racine de tous les maux](http://henrikeichenhardt.blogspot.com/2013/06/why-shared-mutable-state-is-root-of-all.html)

#### Fonctions d'ordre supérieur

* [Eloquent JS : Fonctions d'ordre supérieur](https://eloquentjavascript.net/05_higher_order.html)
* [Fun fun function Filter](https://www.youtube.com/watch?v=BMUiFMZr7vk&t=0s&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84&index=2&ab_channel=FunFunFunction)
* [Fun fun function Map](https://www.youtube.com/watch?v=bCqtb-Z5YGQ&index=2&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84&ab_channel=FunFunFunction)
* [Fun fun function Basic Reduce](https://www.youtube.com/watch?v=Wl98eZpkp-c&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84&index=3&frags=wn&ab_channel=FunFunFunction)
* [Fun fun function Advanced Reduce](https://www.youtube.com/watch?v=1DMolJ2FrNY&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84&index=4&ab_channel=FunFunFunction)
* [Fonctions d'ordre supérieur en Clojure](https://clojure.org/guides/higher_order_functions)
* [Purely Function Filter](https://purelyfunctional.tv/lesson/filter/)
* [Purely Functional Map](https://purelyfunctional.tv/lesson/map/)
* [Purely Functional Reduce](https://purelyfunctional.tv/lesson/reduce/)

#### Programmation déclarative

* [Programmation déclarative vs impérative](https://tylermcginnis.com/imperative-vs-declarative-programming/)

#### C'est tout !

Salut les gens, j'espère que vous avez pris du plaisir à lire cet article, et j'espère que vous avez appris beaucoup ici ! C'était ma tentative de partager ce que j'apprends.

[Voici le dépôt avec tous les codes](https://github.com/tk-notes/fp-in-javascript-article-source-code) de cet article.

Venez apprendre avec moi. Je partage des ressources et mon code dans ce [dépôt d'apprentissage de la programmation fonctionnelle](https://github.com/LeandroTk/learning-functional-programming).

J'ai également écrit un [article sur la programmation fonctionnelle mais en utilisant principalement Clojure](https://medium.freecodecamp.org/an-introduction-to-the-basic-principles-of-functional-programming-a2c2a15c84)

J'espère que vous avez vu quelque chose d'utile pour vous ici. Et à la prochaine fois ! :)

Mon [Twitter](https://twitter.com/LeandroTk_) & [Github](https://github.com/LeandroTk).

TK.