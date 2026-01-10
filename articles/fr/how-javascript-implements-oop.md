---
title: Programmation Orientée Objet en JavaScript – Expliquée avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-13T17:46:51.000Z'
originalURL: https://freecodecamp.org/news/how-javascript-implements-oop
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/OOP-IN-JS-1.png
tags:
- name: JavaScript
  slug: javascript
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Programmation Orientée Objet en JavaScript – Expliquée avec des Exemples
seo_desc: "By Dillion Megida\nJavaScript is not a class-based object-oriented language.\
  \ But it still has ways of using object oriented programming (OOP). \nIn this tutorial,\
  \ I'll explain OOP and show you how to use it.\nAccording to Wikipedia, class-based\
  \ programm..."
---

Par Dillion Megida

JavaScript n'est pas un langage orienté objet basé sur les classes. Mais il dispose toujours de moyens pour utiliser la programmation orientée objet (POO).

Dans ce tutoriel, je vais expliquer la POO et vous montrer comment l'utiliser.

Selon [Wikipedia](https://en.m.wikipedia.org/wiki/Class-based_programming), la programmation basée sur les classes est

> un style de programmation orientée objet (POO) dans lequel l'héritage se fait via la définition de classes d'objets, au lieu que l'héritage se fasse via les objets seuls

Le modèle le plus populaire de la POO est basé sur les classes.

Mais comme je l'ai mentionné, JavaScript n'est pas un langage basé sur les classes – c'est un langage basé sur les prototypes.

Selon la documentation de Mozilla :

> Un langage basé sur les prototypes a la notion d'un objet prototype, un objet utilisé comme modèle à partir duquel obtenir les propriétés initiales pour un nouvel objet.

Jetez un œil à ce code :

```javascript
let names = {
    fname: "Dillion",
    lname: "Megida"
}
console.log(names.fname);
console.log(names.hasOwnProperty("mname"));
// Résultat attendu
// Dillion
// false
```

La variable objet `names` n'a que deux propriétés - `fname` et `lname`. Aucune méthode.

Alors, d'où vient `hasOwnProperty` ?

Eh bien, elle vient du prototype `Object`.

Essayez de logger le contenu de la variable dans la console :

```js
console.log(names);
```

Lorsque vous développez les résultats dans la console, vous obtenez ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/1-1.png)
_console.log(names)_

Remarquez la dernière propriété - `__proto__` ? Essayez de la développer :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/2-1.png)
_La propriété __proto__ de names_

Vous verrez un ensemble de propriétés sous le constructeur `Object`. Toutes ces propriétés proviennent du prototype global `Object`. Si vous regardez de près, vous remarquerez également notre méthode `hasOwnProperty` cachée.

En d'autres termes, tous les objets ont accès au prototype de `Object`. Ils ne possèdent pas ces propriétés, mais ont accès aux propriétés du prototype.

## La propriété `__proto__`

Celle-ci pointe vers l'objet qui est utilisé comme prototype.

C'est la propriété de chaque objet qui lui donne accès à la propriété `Object prototype`.

Chaque objet a cette propriété par défaut, qui fait référence au `Prototype Object`, sauf lorsqu'elle est configurée autrement (c'est-à-dire lorsque le `__proto__` de l'objet pointe vers un autre prototype).

### Modifier la propriété `__proto__`

Cette propriété peut être modifiée en indiquant explicitement qu'elle doit faire référence à un autre prototype. Les méthodes suivantes sont utilisées pour y parvenir :

### `Object.create()`

```javascript
function DogObject(name, age) {
    let dog = Object.create(constructorObject);
    dog.name = name;
    dog.age = age;
    return dog;
}
let constructorObject = {
    speak: function(){
        return "I am a dog"
    }
}
let bingo = DogObject("Bingo", 54);
console.log(bingo);
```

Dans la console, voici ce que vous auriez :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/3-1.png)
_console.log(bingo)_

Remarquez la propriété `__proto__` et la méthode `speak` ?

`Object.create` utilise l'argument passé pour devenir le prototype.

### Mot-clé `new`

```javascript
function DogObject(name, age) {
    this.name = name;
    this.age = age;
}
DogObject.prototype.speak = function() {
    return "I am a dog";
}
let john = new DogObject("John", 45);
```

La propriété `__proto__` de `john` est dirigée vers le prototype de `DogObject`. Mais rappelez-vous, le prototype de `DogObject` est un objet (paire clé-valeur), donc il a également une propriété `__proto__` qui fait référence au prototype global `Object`.

Cette technique est appelée **CHAÎNAGE DE PROTOTYPES**.

**Notez que :** l'approche avec le mot-clé `new` fait la même chose que `Object.create()` mais la rend plus facile car elle fait certaines choses automatiquement pour vous.

### Et donc...

Chaque objet en JavaScript a accès au prototype de `Object` par défaut. S'il est configuré pour utiliser un autre prototype, disons `prototype2`, alors `prototype2` aurait également accès au prototype de l'objet par défaut, et ainsi de suite.

### Combinaison Objet + Fonction

Vous êtes probablement confus par le fait que `DogObject` est une fonction (`function DogObject(){}`) et qu'elle a des propriétés accessibles avec une **notation par points**. Cela est appelé une **combinaison fonction-objet**.

Lorsque les fonctions sont déclarées, par défaut, elles reçoivent de nombreuses propriétés attachées. N'oubliez pas que les fonctions sont également des objets dans les types de données JavaScript.


## Maintenant, la Classe

JavaScript a introduit le mot-clé `class` dans ECMAScript 2015. Il fait ressembler JavaScript à un langage OOP. Mais ce n'est que du sucre syntaxique sur la technique de prototypage existante. Il continue son prototypage en arrière-plan mais fait ressembler le corps extérieur à de l'OOP. Nous allons maintenant voir comment cela est possible.

L'exemple suivant est une utilisation générale d'une `class` en JavaScript :

```javascript
class Animals {
    constructor(name, specie) {
        this.name = name;
        this.specie = specie;
    }
    sing() {
        return `${this.name} can sing`;
    }
    dance() {
        return `${this.name} can dance`;
    }
}
let bingo = new Animals("Bingo", "Hairy");
console.log(bingo);
```

Voici le résultat dans la console :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/5-1.png)
_console.log(bingo)_

Le `__proto__` fait référence au prototype `Animals` (qui à son tour fait référence au prototype `Object`).

À partir de cela, nous pouvons voir que le constructeur définit les principales caractéristiques tandis que tout ce qui est en dehors du constructeur (`sing()` et `dance()`) sont les caractéristiques bonus (**prototypes**).

En arrière-plan, en utilisant l'approche avec le mot-clé `new`, ce qui précède se traduit par :

```javascript
function Animals(name, specie) {
    this.name = name;
    this.specie = specie;
}
Animals.prototype.sing = function(){
    return `${this.name} can sing`;
}
Animals.prototype.dance = function() {
    return `${this.name} can dance`;
}
let Bingo = new Animals("Bingo", "Hairy");
```

## Sous-classes

C'est une fonctionnalité de l'OOP où une classe hérite des caractéristiques d'une classe parente mais possède des caractéristiques supplémentaires que la classe parente n'a pas.

L'idée ici est, par exemple, si vous voulez créer une classe *cats*. Au lieu de créer la classe à partir de zéro - en indiquant les propriétés *name*, *age* et *species* à nouveau, vous hériterez de ces propriétés de la classe parente *animals*.

Cette classe *cats* peut alors avoir des propriétés supplémentaires comme *color of whiskers*.

Voyons comment les sous-classes sont faites avec `class`.

Ici, nous avons besoin d'une classe parente dont la sous-classe hérite. Examinez le code suivant :

```js
class Animals {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    sing() {
        return `${this.name} can sing`;
    }
    dance() {
        return `${this.name} can dance`;
    }
} 
class Cats extends Animals {
    constructor(name, age, whiskerColor) {
        super(name, age);
        this.whiskerColor = whiskerColor;
    }
    whiskers() {
        return `I have ${this.whiskerColor} whiskers`;
    }
}
let clara = new Cats("Clara", 33, "indigo");
```

Avec ce qui précède, nous obtenons les résultats suivants :

```js
console.log(clara.sing());
console.log(clara.whiskers());
// Résultat attendu
// "Clara can sing"
// "I have indigo whiskers"
```

Lorsque vous loggez le contenu de clara dans la console, nous avons :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/6-1.png)
_console.log(clara)_

Vous remarquerez que `clara` a une propriété `__proto__` qui fait référence au constructeur `Cats` et obtient accès à la méthode `whiskers()`. Cette propriété `__proto__` a également une propriété `__proto__` qui fait référence au constructeur `Animals`, obtenant ainsi accès à `sing()` et `dance()`. `name` et `age` sont des propriétés qui existent sur chaque objet créé à partir de celui-ci.

En utilisant l'approche de la méthode `Object.create`, ce qui précède se traduit par :

```js
function Animals(name, age) {
    let newAnimal = Object.create(animalConstructor);
    newAnimal.name = name;
    newAnimal.age = age;
    return newAnimal;
}
let animalConstructor = {
    sing: function() {
        return `${this.name} can sing`;
    },
    dance: function() {
        return `${this.name} can dance`;
    }
}
function Cats(name, age, whiskerColor) {
    let newCat = Animals(name, age);
    Object.setPrototypeOf(newCat, catConstructor);
    newCat.whiskerColor = whiskerColor;
    return newCat;
}
let catConstructor = {
    whiskers() {
        return `I have ${this.whiskerColor} whiskers`;
    }
}
Object.setPrototypeOf(catConstructor, animalConstructor);
const clara = Cats("Clara", 33, "purple");
clara.sing();
clara.whiskers();
// Résultat attendu
// "Clara can sing"
// "I have purple whiskers"
```

`Object.setPrototypeOf` est une méthode qui prend deux arguments - l'objet (premier argument) et le prototype souhaité (deuxième argument).

À partir de ce qui précède, la fonction `Animals` retourne un objet avec `animalConstructor` comme prototype. La fonction `Cats` retourne un objet avec `catConstructor` comme prototype. `catConstructor`, en revanche, reçoit un prototype de `animalConstructor`.

Par conséquent, les animaux ordinaires n'ont accès qu'à `animalConstructor`, mais les chats ont accès à `catConstructor` et à `animalConstructor`.

## Conclusion

JavaScript utilise sa nature de prototype pour accueillir les développeurs OOP dans son écosystème. Il fournit également des moyens faciles de créer des prototypes et d'organiser des données liées.

Les vrais langages OOP n'effectuent pas de prototypage en arrière-plan - notez simplement cela.

Un grand merci au cours de [Will Sentance](https://frontendmasters.com/teachers/will-sentance/) sur Frontend Masters - [JavaScript: The Hard Parts of Object Oriented JavaScript](https://frontendmasters.com/courses/object-oriented-js/). J'ai appris tout ce que vous voyez dans cet article (plus un peu de recherche supplémentaire) grâce à son cours. Vous devriez le consulter.

Vous pouvez me contacter sur Twitter à [iamdillion](https://twitter.com/iamdillion) pour toute question ou contribution.

Merci pour la lecture : )

### Ressources utiles

- [Object-oriented JavaScript for beginners](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)
- [Introduction to Object Oriented Programming in JavaScript](https://www.geeksforgeeks.org/introduction-object-oriented-programming-javascript/)