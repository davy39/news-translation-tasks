---
title: Feuille de révision pour les entretiens JavaScript – Réussissez vos entretiens
  de codage avec ces concepts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-07T15:43:17.000Z'
originalURL: https://freecodecamp.org/news/javascript-interview-prep-cheatsheet
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/JS-Interview--2-.png
tags:
- name: coding interview
  slug: coding-interview
- name: Interview tips
  slug: interview-tips
- name: JavaScript
  slug: javascript
seo_title: Feuille de révision pour les entretiens JavaScript – Réussissez vos entretiens
  de codage avec ces concepts
seo_desc: 'By rajat gupta

  I''ve carefully gone through over 50 resources, I''ve been through 10 JavaScript
  interviews, and I''ve landed a job at a unicorn startup.

  And throughout this entire process, I started to see a pattern in the most frequently
  asked JS inter...'
---

Par Rajat Gupta

J'ai soigneusement examiné plus de **50** ressources, j'ai passé **10** entretiens JavaScript et j'ai obtenu un **emploi** dans une startup licorne.

Et tout au long de ce processus, j'ai commencé à voir un *modèle* dans les questions d'entretien JS les plus fréquemment posées.

Dans cet article, j'ai essayé de lister les concepts qui couvriront **80%** de tout bon entretien JS.

Donc, si vous vous préparez pour votre prochain entretien JS, voici la feuille de révision parfaite pour vous pour réviser et solidifier vos compétences. Passez en revue ceci et vous serez prêt à tout casser. 🚀

## 📝 Prérequis
* Connaissance de base du web et de la programmation
* Familiarité avec HTML/CSS et JavaScript (surtout la syntaxe ES6+)

## Table des matières 📜
* [Bases de JavaScript](#heading-installation) – Variables JS et Méthodes de Tableau
* [Programmation Fonctionnelle en JavaScript](#heading-programmation-fonctionnelle-en-javascript) – Portée, Fermetures et Hissage
* [Objets en JavaScript](#heading-objets-en-javascript) – Prototypes et "this"
* [JavaScript Asynchrone](#heading-javascript-asynchrone) – Boucles d'Événements, Minuteries et Promesses
* [Concepts Avancés de JavaScript à Connaître](#heading-concepts-avances-de-javascript-a-connaitre) - Async/defer, Polyfills, Débogage et Throttling
* [Stockage en JavaScript](#heading-stockage-en-javascript)

**Avertissement :** L'accent ici sera largement mis sur la couverture des concepts pertinents pour l'entretien et non sur la création d'un livret complet pour apprendre le langage. Traitez cela davantage comme une feuille de révision.

Si vous souhaitez approfondir et apprendre plus de concepts JS, consultez le [programme de freeCodeCamp](https://www.freecodecamp.org/learn/).

Cela étant dit - c'est parti !

## Bases de JavaScript 👨‍💻

Commençons par quelques concepts de base que tout développeur JS doit connaître.

### Variables en JavaScript 📥

Les variables sont les éléments de base de tout langage de programmation. Vous les utilisez pour stocker des valeurs. Une variable peut être un nombre, une chaîne et bien d'autres types.

Maintenant, JS est un langage *faiblement typé*. Vous n'avez pas à préciser le type de variable. Vous pouvez simplement la déclarer, et JS la déterminera lui-même.

Maintenant, en JavaScript, nous avons **3** façons de déclarer des variables : `var`, `let` et `const`.

Voici les principales différences :

![-wnr0JLxh](https://www.freecodecamp.org/news/content/images/2021/06/-wnr0JLxh.png)

Essayons de les comprendre à travers des exemples.

Nous aborderons la portée plus tard. Pour l'instant, concentrons-nous sur les autres différences.

```javascript
var a = 3
var a = 4

console.log(a) // 4 car les variables var peuvent être redéclarées + mises à jour

let b = 3
let b = 4

console.log(b) // Erreur de syntaxe car les variables let ne peuvent pas être redéclarées

// Si nous faisons simplement cela, cela fonctionnera car elles peuvent être mises à jour
b = 4

const c = 3
const c = 4

console.log(c) // Erreur de syntaxe car les variables const ne peuvent pas être redéclarées ou mises à jour

const d

// Cela va-t-il générer une erreur ? Passez en revue le tableau et essayez de trouver la réponse.
```

**Note :** En JavaScript, mettre un point-virgule après la fin de l'instruction est facultatif. Je vais le sauter ici pour des raisons de lisibilité.

### == vs === en JavaScript

Comparons quelques variables. Il y a deux façons de le faire.

`==` vérifie uniquement la valeur

`===` vérifie la valeur + le type

```javascript

let a = 5 // nombre
let b = '5' // chaîne

console.log(a == b) // vrai

console.log(a === b) // faux

```

### Tableaux en JavaScript

Maintenant que nous connaissons un peu les variables, passons aux tableaux et aux méthodes de tableau.

Si nous avons déclaré beaucoup de variables, il est logique de les stocker quelque part. Sinon, il sera difficile de garder une trace de toutes. Les tableaux sont un moyen de stocker une variable.

```javascript

let a = 4
const b = 5
var c = 'bonjour'

const tableau = [a, b, c]

// ou vous pouvez simplement faire directement

const arr = [4,5,'bonjour']
```

Mais stocker des variables dans un tableau est un peu ennuyeux. Nous pouvons faire plus de *choses* avec ce tableau (comme accéder à ces variables ou changer l'ordre dans lequel elles sont stockées ou comment elles sont stockées).

Pour cela, JS a beaucoup de méthodes. Regardons quelques-unes maintenant.

## Méthodes de Tableau JavaScript 🏃‍♂️


Les méthodes de tableau les plus fréquemment utilisées en JS sont : `map`, `filter`, `find`, `reduce` et `forEach`.

Couvrons `map`, `filter` et `forEach`. Vous pouvez explorer plus dans [cet article utile](https://www.freecodecamp.org/news/complete-introduction-to-the-most-useful-javascript-array-methods/).

### La méthode de tableau `map`

`map` crée une nouvelle copie du tableau original. Nous l'utilisons lorsque nous voulons faire quelque chose avec les éléments du tableau original mais ne voulons pas le changer.

`map` itère sur le tableau original et prend une fonction de rappel (que nous aborderons plus tard) comme argument. Dans la fonction de rappel, nous lui disons quoi faire avec les éléments.

```javascript
const a = [1,2,3,4,5]

// Créer un nouveau tableau qui multiplie chaque élément par 2

const d = a.map(function(item){ return item*2 })

console.log(d) // [2,4,6,8,10]
```


### La méthode de tableau `filter`

`filter` crée un nouveau tableau avec les éléments qui répondent à la ou aux conditions données.

Regardons un exemple. J'ai utilisé des [fonctions fléchées](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) ici. Si vous êtes un peu mal à l'aise avec les fonctions, vous pouvez couvrir la section suivante en premier et revenir.

```javascript
// Retourner les mots avec plus de 6 lettres
const mots = ['react', 'script', 'entretien', 'style', 'javascript']

const ans = mots.filter((mot) => mot.length > 6)

console.log(ans) // ['entretien', 'javascript']
```

Essayez de faire les exercices vous-même d'abord pour tester vos connaissances. Si vous trouvez des solutions différentes ou meilleures, faites-le moi savoir !

Généralement, une suite à cela : pouvez-vous le faire sans la méthode de tableau ?


```javascript
let newArr = []

for (let i = 0; i < mots.length; i++) {
  if (mots[i].length > 6) {
    newArr.push(mots[i])
  }
}
console.log(newArr)
```


### La méthode de tableau `forEach`

`forEach` est très similaire à `map` mais a deux différences clés :

Tout d'abord, `map` retourne un nouveau tableau, mais `forEach` ne le fait pas.

```javascript
// Retourner un nouveau tableau où les nombres pairs sont multipliés par 2
let arr = [1, 2, 3, 4, 5, 6, 7]

function consoleEven(arr) {
  let data = arr.map((num) => (num % 2 === 0 ? num * 2 : num * 1))
  
  console.log(data)  // [1,  4, 3, 8, 5, 12, 7]
}


// ? est l'opérateur ternaire. Si la condition est vraie - la première instruction est retournée sinon la deuxième.


consoleEven(arr)
```

```javascript

function consoleEven(arr) {
  let data = arr.forEach((num) => (num % 2 === 0 ? num * 2 : num * 1))
  console.log(data) // undefined
}

consoleEven(arr)
```

Et deuxièmement, vous pouvez faire du chaînage de méthodes dans `map` mais pas dans `forEach`.

```javascript

// Convertir le nouveau tableau en original

function consoleEven(arr) {
  let data = arr
    .map((num) => (num % 2 === 0 ? num * 2 : num * 1))
    .map((item) => (item % 2 === 0 ? item / 2 : item / 1))
    
  console.log(data)
}

consoleEven(arr)
```

**Note :** `map` et `forEach` ne mutent pas (changent) le tableau original.

## Programmation Fonctionnelle en JavaScript 🛠️

Nous avons déjà utilisé des fonctions ci-dessus. Couvrons-les plus en détail maintenant.

Tout comme nous avons utilisé des variables pour stocker des valeurs, nous pouvons utiliser des fonctions pour stocker un morceau de code que nous pouvons réutiliser.

Vous pouvez créer une fonction de deux manières :

```javascript
function a(){
 console.log('Je suis une fonction normale');
 }
 
const b = () => {
console.log('Je suis une fonction fléchée')
}

// Elles sont essentiellement les mêmes mais avec quelques différences que nous aborderons au fur et à mesure de ce tutoriel.

// Nous pouvons passer des variables comme arguments

const c = (name) => {
console.log(`Mon nom est ${name}`)
}

// `` les littéraux de gabarit sont un nouvel ajout au langage. Très utiles pour le formatage de chaînes. Les valeurs sont accessibles en utilisant ${} à l'intérieur.


// Nous pouvons même passer des fonctions comme arguments à une fonction. Nous verrons plus sur cela lorsque nous essaierons de comprendre les fermetures.

const greet = () =>  {
    const prefix = 'Mr'
    return (name) => {
        console.log(`${prefix} ${name}, bienvenue !`)
    }
}

console.log(greet()('Jack'))
```

Maintenant, couvrons quelques concepts importants liés aux fonctions.

### Portée des Fonctions en JavaScript 🔍

La portée détermine d'où les variables sont accessibles.

Il existe trois types de portée :

* Globale (déclaration en dehors de toute fonction)
* Fonction (déclaration à l'intérieur d'une fonction)
* Bloc (déclaration à l'intérieur d'un bloc)

Rappelez-vous que `var` est globalement portée alors que `let` et `const` sont portées par bloc. Comprenons cela maintenant.

```javascript

var a = 5 // nous pouvons accéder à ce a n'importe où

function adder(){
    let b = 7
    console.log(a + b)
 }
 
console.log(adder())

console.log(b) // Erreur car b n'est pas accessible en dehors de la fonction

{
const c = 10
console.log(c) // 10
}

console.log(c) // Erreur car c n'est pas accessible en dehors du bloc
```

### Fermetures en JavaScript (❗important) 🔑

Nous avons déjà utilisé une fermeture sans même nous en rendre compte. Dans l'exemple ci-dessous, `prefix` est une variable fermée.

```
const greet = () =>  {
    const prefix = 'Mr'
    return (name) => {
        console.log(`${prefix} ${name}, bienvenue !`)
    }
}

console.log(greet()('Jack'))
```

Cette section contiendra beaucoup de mots fantaisistes, alors restez avec moi. Nous les couvrirons un par un.

MDN dit :

> Une fonction regroupée avec son environnement lexical forme une fermeture.

D'accord, qu'est-ce qu'un environnement lexical ?

C'est essentiellement l'état environnant – la **mémoire locale** ainsi que l'environnement lexical de son parent.

Quoi ? 🤯 Je sais que c'est un peu déroutant. Comprenons-le avec un exemple simple.

```javascript
function x() {
  var a = 7
  function y() {
    console.log(a)
  }
  return y
}

var z = x()
console.log(z) // [Function: y]
z()
```

Lorsque x est invoqué, y est retourné. Maintenant, y attend d'être exécuté. Un peu comme un pistolet chargé attendant d'être tiré ! 🔫

Donc, lorsque nous invoquons enfin z, y est invoqué. Maintenant, y doit logger `a` alors il essaie d'abord de le trouver 🔍 dans la **mémoire locale** mais il n'est pas là. Il va à sa fonction parente. Il trouve `a` là.

Voilà ! Vous l'avez - [c'est une fermeture](https://www.freecodecamp.org/news/closures-in-javascript/).

Même lorsque les fonctions sont retournées (dans le cas ci-dessus y), elles se souviennent encore de leur portée lexicale (d'où elles viennent)

Citation totalement non liée pour le fun 🕺:

> Ils peuvent oublier ce que vous avez dit - mais ils n'oublieront jamais comment vous les avez fait sentir - Carl W. Buehner

Je jure que le reste de l'article est légitime 😆 Continuez à lire.

### Avantages des Fermetures en JavaScript 😎

- Currying

```javascript
let add = function (x) {
  return function (y) {
    console.log(x + y)
  }
}

let addByTwo = add(2)
addByTwo(3)
```

- Masquage de Données/Encapsulation

Supposons que vous voulez créer une application de compteur. Chaque fois que vous l'appelez, le compte augmente de 1. Mais vous ne voulez pas exposer la variable en dehors de la fonction. Comment faire ?

Vous l'avez deviné – les fermetures !

```javascript
function Counter() {
  var count = 0
  this.incrementCount = function () {
    count++
    console.log(count)
  }
}

console.log(count) // Erreur : count n'est pas défini
var adder = new Counter()
adder.incrementCount() // 1
```

Ne vous inquiétez pas pour `this` et `new`. Nous avons une section entière qui leur est consacrée ci-dessous.

### Inconvénients des Fermetures en JavaScript 😅

- La surconsommation de mémoire ou les fuites de mémoire peuvent se produire.

Par exemple, la variable fermée ne sera pas collectée par le garbage collector. Cela est dû au fait que, même si la fonction externe a été exécutée, la fonction interne retournée a toujours une référence à la variable fermée.

**Note :** La collecte des déchets supprime essentiellement les variables inutilisées de la mémoire automatiquement.


### Hissage en JavaScript 🚩


C'est le comportement par défaut de JavaScript qui consiste à déplacer les déclarations en haut du programme.

- La déclaration `var` est hissée et initialisée avec `undefined`.
- Les déclarations `let` et `const` sont hissées mais non initialisées.
- Les définitions de `function` sont également hissées et stockées telles quelles.

Regardons un exemple :

```javascript
function consoleNum() {
  console.log(num)
  var num = 10
}

consoleNum() // undefined

// Pourquoi pas d'erreur ?

// Voici comment le runtime voit cela
{
  var num
  console.log(num)
  num = 9
}

// Si au lieu de var -> let, cela donnera une erreur car les valeurs let ne sont pas initialisées
```

Ouf ! J'ai terminé avec les fonctions ici, mais si vous voulez plus [regardez ce discours incroyable d'Anjana Vakil](https://youtu.be/e-5obm1G_FY) sur la programmation fonctionnelle.

## Objets en JavaScript 📂

Tout comme les tableaux, les objets sont un moyen de stocker des données. Nous le faisons à l'aide de paires clé-valeur.

```javascript

    const developer = {
        name: "Raj",
        age: 22
        }
```

`name` est la `clé` et `Raj` est la `valeur`. Les clés sont généralement le nom des propriétés de l'objet.

Nous pouvons stocker toutes sortes de données comme des fonctions à l'intérieur d'un objet. Vous pouvez explorer plus ici sur le [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object).

### Qu'est-ce que `this` en JavaScript ?

Maintenant, travailler avec des objets est différent en JS que dans d'autres langages de programmation populaires comme C++. Et pour bien comprendre cela, nous avons besoin d'une bonne compréhension du mot-clé `this`.

Essayons de le comprendre étape par étape.

Dans un programme, parfois, nous avons besoin d'un moyen de pointer vers des choses. Comme dire que cette fonction ici appartient à cet objet. `this` nous aide à obtenir ce contexte.

Vous comprendrez mieux ce que je dis lorsque nous regarderons quelques exemples.

Pour l'instant, pensez à `this` comme quelque chose qui fournit un contexte. Et rappelez-vous cette chose importante : sa valeur dépend de la manière et de l'endroit où il est appelé.

Je sais, je sais. Beaucoup de `this` 😬. Passons en revue tout cela lentement.

Démarrez un nouveau programme et loggez simplement `this`.

```javascript

console.log(this)

```

Il pointera vers l'objet window.

Maintenant, prenons un exemple avec un objet :

```javascript
function myFunc() {
    console.log(this)
  }
 
const obj = {
  bool: true,
  myFunc: myFunc,
}

obj.myFunc()
```

Maintenant, `this` pointera vers l'objet. Alors, que se passe-t-il ici ?

Dans le premier exemple, nous n'avions rien à gauche du `.` donc il a pris par défaut l'objet `window`. Mais dans cet exemple, nous avons l'objet `obj`.

Si vous faites :

```javascript

myFunc() // window

```

Nous obtenons à nouveau l'objet `window`. Donc, nous pouvons voir que la valeur de `this` dépend de la manière et de l'endroit où nous faisons l'appel.

Ce que nous venons de faire ci-dessus s'appelle **Implicit Binding**. La valeur de `this` a été liée à l'objet.

Il y a une autre façon d'utiliser `this`. **Explicit binding** est lorsque vous forcez une fonction à utiliser un certain objet comme son `this`.

Comprenons pourquoi nous avons besoin d'un explicit binding à travers un exemple.

```javascript

const student_1 =  {
    name: 'Randall',
    displayName_1: function displayName() {
        console.log(this.name)
    }
}
const student_2 =  {
    name: 'Raj',
    displayName_2: function displayName() {
        console.log(this.name)
    }
}

student_1.displayName_1()
student_2.displayName_2()

```

Nous utilisons `this` correctement, mais pouvez-vous voir le problème avec le code ci-dessus ?

Nous répétons du code. Et l'un des principes de la bonne programmation est de garder votre code DRY ! (Don't Repeat Yourself)

Alors, débarrassons-nous de `displayName_2` et faisons simplement :

```javascript

student_1.displayName_1.call(student_2) // Raj

```

`call` a forcé `displayName_1` à utiliser le deuxième objet comme son `this`.

Il y a beaucoup d'autres façons de faire cela.

![call-bind-apply.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1622489263380/UwpR9Rscv.png)

Essayez de résoudre le problème donné vous-même.

```javascript
const myData = {
  name: 'Rajat',
  city: 'Delhi',
  displayStay: function () {
    console.log(this.name, 'vit à', this.city)
  },
}
myData.displayStay()

// créez un objet yourData et essayez d'utiliser displayStay
const yourData = {
 name: 'nom',
 city: 'ville'
}


// réponse
myData.displayStay.call(yourData)
```


Enfin, rappelez-vous que j'ai dit qu'il y avait des différences entre les fonctions fléchées et les fonctions régulières.

Le cas de `this` en est une.

Pour une fonction fléchée, la valeur dépend de la portée lexicale – c'est-à-dire, la fonction externe où la fonction fléchée est déclarée.

Donc, si nous faisons de `displayName()` ci-dessus une fonction fléchée, rien ne fonctionnera.

Les fonctions fléchées héritent essentiellement du contexte du parent qui dans le cas ci-dessus est la `window`.


### Prototypes et Héritage Prototypal en JavaScript 👨‍👩‍👧‍👦

> Chaque fois que nous créons quelque chose (comme un objet ou une fonction) en JavaScript, le moteur JS attache automatiquement cette chose avec certaines propriétés et méthodes.

Tout cela vient via les `prototypes`.

`__proto__` est l'objet où JS met tout.

Regardons quelques exemples. Lancez vos consoles !

```javascript
let arr = ['Rajat', 'Raj']
console.log(arr.__proto__.forEach)
console.log(arr.__proto__) // même que Array.prototype
console.log(arr.__proto__.__proto__) // même que Object.prototype
console.log(arr.__proto__.__proto__.__proto__) // null
```

Tout cela s'appelle une `chaîne de prototypes`.

Nous pouvons faire la même chose avec les objets et les fonctions également.

Nous trouverons toujours `Object.prototype` en coulisses. C'est pourquoi vous avez peut-être entendu dire que tout en JS est un objet. 🤯


### Qu'est-ce que l'Héritage Prototypal en JavaScript ?


```javascript
let object = {
  name: 'Rajat',
  city: 'Delhi',
  getIntro: function () {
    console.log(`${this.name}, ${this.city}`)
  },
}

let object2 = {
  name: 'Aditya',
}
```

**Note :** Ne modifiez pas les prototypes de cette manière. C'est juste pour la compréhension. [Voici la bonne façon de le faire](https://javascript.plainenglish.io/how-prototypal-inheritance-works-in-javascript-and-how-to-convert-it-to-class-based-inheritance-632e31e6350d).

```javascript
object2.__proto__ = object
```

En faisant cela, `object2` obtient l'accès aux propriétés de l'objet. Donc, maintenant nous pouvons faire :

```javascript
console.log(object2.city)
```

C'est l'**héritage prototypal**.

## JavaScript Asynchrone ⚡

Donc, JS est un langage *monothread*. Les choses se passent une à la fois. Ce n'est qu'après qu'une chose est faite que nous pouvons passer à la suivante.

Mais cela crée des problèmes dans le monde réel, surtout lorsque nous travaillons avec des navigateurs.

Par exemple, lorsque nous devons récupérer des données du web - souvent, nous ne savons pas combien de temps cela prendra pour les obtenir. Et si nous serons en mesure d'obtenir les données avec succès.

Pour aider à cela, le JavaScript asynchrone entre en jeu.

Et le concept le plus important à comprendre est la boucle d'événements.

### Boucles d'Événements en JavaScript ➡️

Au lieu de fournir une explication à moitié cuite ici, je recommande vivement de regarder cette vidéo de Philip Roberts si vous ne l'avez pas déjà fait :

[Apprenez tout sur les boucles d'événements en JS ici](https://youtu.be/8aGhZQkoFbQ).


### Minuteries en JavaScript – setTimeout, setInterval, clearInterval ⏳

J'espère que vous avez regardé la vidéo. Elle a mentionné les minuteries. Parlons-en plus maintenant. Ce sont des questions très fréquemment posées lors des entretiens.

La méthode `setTimeout()` appelle une fonction ou évalue une expression après un nombre spécifié de millisecondes.

`setInterval()` fait de même pour des intervalles spécifiés.

```javascript

setTimeout(() => {
    console.log('Ici - Je suis après 2 secondes')
}, 2000);

const timer = setInterval(() => {
    console.log('Je continuerai à revenir jusqu'à ce que vous me supprimiez')
}, 2000);

```

Vous utilisez `clearInterval()` pour arrêter la minuterie.

```
clearInterval(timer)
```

Passons en revue quelques questions qui utilisent ces concepts.

```javascript
  console.log('Bonjour')
  setTimeout(() => {
    console.log('lovely')
  }, 0)
  console.log('lecteur')

  // sortie
  Bonjour
  lecteur
  lovely
```

En voici un légèrement plus trompeur :

```javascript
  for (var i = 1; i <= 5; i++) {
    setTimeout(function () {
      console.log(i)
    }, i * 1000)
  }

// sortie
6
6
6
6
6
```

Et voici une brève explication de ce qui se passe là : lorsque `setTimeout` revient dans le tableau, toute la boucle a été exécutée et la valeur de `i` est devenue 6,

Maintenant, supposons que nous voulons que le résultat soit 1 2 3 4 5 – que faisons-nous ?

Au lieu de `var` ➡️ utilisez `let`.

Pourquoi cela fonctionnera-t-il ?

`var` est globalement portée mais `let` est localement portée. Donc pour `let`, un nouveau `i` est créé pour chaque itération.


### Promesses en JavaScript (❗important) 🤯

Les promesses sont au cœur du JavaScript asynchrone.

> L'objet Promise représente l'achèvement éventuel (ou l'échec) d'une opération asynchrone et sa valeur résultante.

Une promesse peut être dans l'un de ces trois états :

- En attente : état initial, ni remplie ni rejetée
- Remplie : l'opération a été complétée avec succès
- Rejetée : l'opération a échoué

```javascript
const promise = new Promise((resolve, reject) => {
  let value = true
  if (value) {
    resolve('hey value est vrai')
  } else {
    reject('il y a eu une erreur, value est faux')
  }
})

promise
  .then((x) => {
    console.log(x)
  })
  .catch((err) => console.log(err))
```

**Note :** `resolve` et `reject` sont juste des noms conventionnels. Appelez-le pizza🍕 si vous voulez.

Au lieu de `then/catch`, nous pouvons aussi utiliser `async/await` :

```javascript
async function asyncCall() {
  const result = await promise
  console.log(result)
}

asyncCall()
```

L'un des avantages des promesses est qu'elles ont une syntaxe beaucoup plus propre. Avant d'avoir les promesses, nous pouvions facilement nous retrouver dans [l'enfer des callbacks](http://callbackhell.com/) 🌫️

## Concepts Avancés de JavaScript à Connaître

### 📊 Polyfills en JavaScript

> Un polyfill est un morceau de code (généralement JavaScript sur le Web) utilisé pour fournir des fonctionnalités modernes sur des navigateurs plus anciens qui ne les supportent pas nativement. [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill)

- Implémentons-le pour `map` :

```javascript
// this - tableau
// this[i] - valeur actuelle
Array.prototype.myMap = function (cb) {
  var arr = []
  for (var i = 0; i < this.length; i++) {
    arr.push(cb(this[i], i, this))
  }
  return arr
}

const arr = [1, 2, 3]
console.log(arr.myMap((a) => a * 2)) // [2, 4, 6]
```

Remarquez comment nous utilisons `this`. Ici, nous avons essentiellement créé un nouveau tableau et y ajoutons des valeurs.


### Async et defer en JavaScript ✅

Ces concepts sont fréquemment demandés lors des entretiens par de grandes entreprises comme Amazon, Walmart et Flipkart. 🏢

Pour comprendre `async` et `defer`, nous devons avoir une idée de la manière dont les navigateurs rendent une page web. D'abord, ils analysent le HTML et le CSS. Ensuite, les arbres DOM sont créés. À partir de ceux-ci, un arbre de rendu est créé. Enfin, à partir de l'arbre de rendu - une mise en page est créée et la peinture se produit.

Pour un regard plus détaillé, consultez [cette vidéo](https://youtu.be/SmE4OwHztCc).

Async et defer sont des attributs `boolean` qui peuvent être chargés avec les balises de script. Ils sont utiles pour charger des scripts externes dans votre page web.

Comprenons avec l'aide d'images.

![18-async-defer.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1621781371965/PciAdUTCL.png)
![19-async-defer.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1621781403795/VgIYFtP5T.png)
![20-async.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1621781415787/mJEkxqe_i.png)
![21-defer.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1621781428927/2nUaI8fjr.png)

S'il y a plusieurs scripts qui dépendent les uns des autres, utilisez `defer`. Les scripts defer sont exécutés dans l'ordre où ils sont définis.

Si vous voulez charger un script externe qui ne dépend pas de l'exécution d'autres scripts, utilisez `async`.

**Note :** L'attribut async ne garantit pas l'ordre d'exécution des scripts.


### Débogage en JavaScript ⛷️‍♂️

Le débogage est un autre sujet préféré des recruteurs.

Comprenons-le en créant une barre de recherche.

**Démo :** https://codesandbox.io/s/debounce-input-field-o5gml

Créez un simple champ de saisie dans `index.html` comme ceci :

```javascript
<input type='text' id='text' />
```

Maintenant, dans `index.js`. N'oubliez pas de l'ajouter à `index.html` d'abord :

```javascript
const getData = (e) => {
  console.log(e.target.value)
}
const inputField = document.getElementById('text')

const debounce = function (fn, delay) {
  let timer
  return function () {
    let context = this
    clearTimeout(timer)
    timer = setTimeout(() => {
      fn.apply(context, arguments)
    }, delay)
  }
}

inputField.addEventListener('keyup', debounce(getData, 300))
```

Tout d'abord, nous avons sélectionné l'entrée et ajouté un `écouteur d'événement`. Ensuite, nous avons créé une fonction de débogage qui prend une fonction de rappel et un délai.

Maintenant, à l'intérieur de la fonction de débogage, nous créons une minuterie en utilisant `setTimeout`. Maintenant, le travail de cette minuterie est de s'assurer que le prochain appel pour `getData` n'a lieu qu'après 300 ms. C'est ce qu'est le débogage.

De plus, nous utilisons `clearTimeout` pour le supprimer. Ne voulons pas qu'il y en ait trop qui traînent en occupant de l'espace mémoire !

Ouf ! Beaucoup de théorie. Faisons un défi amusant. Vous devez avoir vu le compte à rebours avant qu'un jeu ne commence (il va comme 10, 9, 8, .... avec un certain délai entre les deux). Essayez d'écrire un programme pour cela.

Voici comment vous le feriez :

```javascript
let count = 10

for (let i = 0; i < 10; i++) {
  function timer(i) {
    setTimeout(() => {
      console.log(count)
      count--
    }, i * 500)
  }
  timer(i)
}
```

Avez-vous pu le résoudre ? L'avez-vous fait différemment ? Faites-moi savoir votre solution.


### Throttling en JavaScript 🏃

Prenons un exemple. Supposons que lors de chaque événement de redimensionnement de fenêtre, nous appelons une fonction coûteuse. Maintenant, nous voulons que la fonction coûteuse ne soit exécutée qu'une seule fois dans l'intervalle de temps donné. C'est ce qu'est le throttling.

Créez un `index.html` et un `index.js` avec le code suivant :

```javascript
const expensive = () => {
  console.log('expensive')
}

const throttle = (fn, limit) => {
  let context = this
  let flag = true
  return function () {
    if (flag) {
      fn.apply(context, arguments)
      flag = false
    }
    setTimeout(() => {
      flag = true
    }, limit)
  }
}
const func = throttle(expensive, 2000)
window.addEventListener('resize', func)
```

Presque la même chose que le débogage. La différence clé est la variable `flag`. Seulement, lorsque c'est vrai, nous invoquons la fonction de rappel. Et elle est définie sur `true` à l'intérieur du `setTimeout`. Donc la valeur est `true` seulement après la limite de temps souhaitée.

### Donc, quelle est la différence entre debounce et throttling❓

Prenons l'exemple de la barre de recherche 🔍 ci-dessus. Lorsque nous faisons le débogage du champ de saisie, nous disons de ne récupérer les données que lorsque la différence entre deux événements `keyup` est d'au moins 300 ms.

Dans le cas du throttling, nous faisons un appel de fonction seulement après une certaine période de temps.

Supposons que vous recherchez une encyclopédie dans la barre de recherche. Le premier appel est fait sur `e` et il nous a fallu 300 ms pour atteindre `p`. Le prochain appel sera fait alors seulement. Tous les événements entre les deux seront ignorés.

Donc, pour résumer, le débogage est lorsque la différence entre deux événements `keyup` est de 300 ms. Et le throttling est lorsque la différence entre deux appels de fonction est de 300 ms. En gros, la fonction est appelée après un certain intervalle de temps.

## Stockage en JavaScript 📦

Enfin, un petit mais important sujet pour conclure.

**localStorage :** Les données persistent même après la fermeture de votre session

**sessionStorage :** Vous perdez vos données lorsque votre session est terminée, comme lorsque vous fermez le navigateur sur l'onglet.


```javascript
// sauvegarder
localStorage.setItem('key', 'value')
// obtenir les données sauvegardées
let data = localStorage.getItem('key')
// supprimer les données sauvegardées
localStorage.removeItem('key')
// Même chose pour sessionStorage
```

Et nous avons terminé ! 🏁 J'espère que vous vous sentez plus confiant pour votre prochain entretien JS maintenant. Je vous souhaite tout le meilleur.

Si vous avez des questions / suggestions / commentaires, vous pouvez me contacter sur Twitter : [https://twitter.com/rajatetc](https://twitter.com/rajatetc).

## 📋 Références Principales
- [MDN Docs](https://developer.mozilla.org/en-US/)
- [Akshay Saini](https://www.youtube.com/channel/UC3N9i_KvKZYP4F84FPIzgPQ)
- [Coding Addict](https://www.youtube.com/channel/UCMZFwxv5l-XtKi693qMJptA)
- [Javascript_Interviews](https://www.instagram.com/javascript_interviews/)