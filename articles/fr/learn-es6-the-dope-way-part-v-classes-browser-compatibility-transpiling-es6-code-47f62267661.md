---
title: 'Apprendre ES6 à la manière cool Partie V : Classes, Transpilation du code
  ES6 et plus de ressources !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-27T06:02:46.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RuxaPPPrL6K09eF4pFhISw.jpeg
tags:
- name: education
  slug: education
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: 'Apprendre ES6 à la manière cool Partie V : Classes, Transpilation du code
  ES6 et plus de ressources !'
seo_desc: 'By Mariya Diminsky

  Welcome to Part V of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  Today we’ll explore ES6 classes, learn how to compile our code into ES5 for browser
  compatibility and learn about some ...'
---

Par Mariya Diminsky

Bienvenue à la Partie V de **Apprendre ES6 à la manière cool**, une série créée pour vous aider à comprendre facilement ES6 (ECMAScript 6) !

Aujourd'hui, nous explorerons les _classes_ ES6, apprendrons à compiler notre code en ES5 pour la compatibilité avec les navigateurs et découvrirons quelques ressources géniales qui nous aideront à comprendre ES6 en profondeur ! C'est l'heure de l'aventure ! 💖

![Image](https://cdn-media-1.freecodecamp.org/images/1*EwyGlROHPNaLRBejoGqM3g.gif)

#### Classes en ES6

**Avantages :**

* Une manière plus simple de gérer l'héritage par prototype de JavaScript — c'est juste du "sucre syntaxique".
* Vous utilisez toujours le même modèle d'héritage orienté objet.
* Similaire à la syntaxe _class_ en Java, Python, Ruby et PHP.
* Vous fait gagner beaucoup de frappe.

**Attention :**

* Vous ne pouvez invoquer une _class_ que via _new_, pas via un appel de fonction.
* Utilisez _super()_ pour appeler le _constructor_ d'une classe parente.
* Une _class_ ressemble à un objet mais se comporte comme une fonction — parce que c'en est une.
* Les déclarations de _class_ ne sont pas hissées comme le sont les déclarations de fonction.
* Un nom donné à une expression de _class_ est seulement local au corps de la _class_.
* Une _SyntaxError_ sera levée si la classe contient plus d'une occurrence d'une méthode _constructor_.
* Alors que les membres d'un littéral objet sont séparés par des virgules, les virgules sont illégales dans les _classes_ — cela souligne la différence entre eux. Les points-virgules ne sont autorisés que pour la syntaxe future (possiblement ES7), qui peut inclure des propriétés annulées par des points-virgules.
* Dans les _classes dérivées_ (expliqué plus tard), _super()_ doit être appelé en premier, avant que vous puissiez utiliser le mot-clé _this_. Sinon, cela causera une _ReferenceError_.
* Les propriétés _static_ sont des propriétés de la _class_ elle-même. Ainsi, bien qu'elles puissent être héritées et accessibles en appelant directement le nom de la _class_, si vous appelez une instance de la _class_ (et la stockez dans une variable), vous ne pourrez pas y accéder avec cette variable.

#### Créer une Classe

Alors, comment créer une _class_ ? Commençons par revoir comment les objets sont créés en ES5 sans utiliser de _classes_ :

```js
function Bunny(name, age, favoriteFood) {
  this.name = name;
  this.age = age;
  this.favoriteFood = favoriteFood;
}
  
Bunny.prototype.eatFavFood = function () {
  console.log('"Mmmm! Those ' + this.favoriteFood + ' were delicious", said ' + this.name + ', the ' + this.age + ' year old bunny.');
};

var newBunny = new Bunny('Brigadier Fluffkins', 3, 'Raspberry Leaves');
newBunny.eatFavFood();
// "Mmmm! Those Raspberry Leaves were delicious", said Brigadier Fluffkins, the 3 year old bunny.

```

Maintenant, observons la même chose avec les _classes_ ES6 :

```js
class Bunny {
  constructor(name, age, favoriteFood){
    this.name = name;
    this.age = age;
    this.favoriteFood = favoriteFood;
  }
  
  eatFavFood() {
    console.log(`"Mmmm! Those ${this.favoriteFood} were delicious", said ${this.name} the ${this.age} year old bunny.`);
  };
}

let es6Bunny = new Bunny('Brigadier Fluffkins', 3, 'Raspberry Leaves');
es6Bunny.eatFavFood();
// "Mmmm! Those Raspberry Leaves were delicious", said Brigadier Fluffkins the 3 year old bunny.

```

Quelles sont les principales différences ? Clairement, la syntaxe de la _class_ ressemble à un objet, mais rappelez-vous qu'en réalité, c'est toujours une fonction et qu'elle se comporte comme telle. Testons cela nous-mêmes :

```js
typeof Bunny
// function
```

Une autre différence principale est que tout ce que vous voulez stocker doit être dans une méthode _constructor_. Toute méthode de prototype de la _class_ doit être à l'intérieur de cette _class_, mais à l'extérieur du _constructor_, sans écrire '._prototype_', et en utilisant la syntaxe de fonction ES6.

#### Deux Façons de Définir une Classe et l'Héritage de Prototype

Il existe deux principales façons de définir une _class_ — l'exemple ci-dessus est l'une des façons les plus courantes, une déclaration de _class_. Bien qu'une _class_ soit effectivement une fonction et que les déclarations de fonction soient hissées — ce qui signifie que la fonction peut être appelée peu importe si elle est appelée avant d'être déclarée — vous ne pouvez pas hisser une déclaration de _class_. C'est important à retenir :

```js
// Déclaration de fonction normale
// appelée avant d'être déclarée et cela fonctionne.
callMe(); // Testing, Testing.

function callMe() {
  console.log("Testing, Testing.")
}

// Cela est appelé après, comme nous le ferions dans une expression de fonction,
// et cela fonctionne aussi !
callMe() // Testing, Testing.


// Mais avec les classes... Vous ne pouvez pas créer une instance d'une classe 
// avant de l'avoir créée :
let es6Bunny = new Bunny('Brigadier Fluffkins', 3, 'Raspberry Leaves');
es6Bunny.eatFavFood();

class Bunny {
  constructor(name, age, favoriteFood){
    this.name = name;
    this.age = age;
    this.favoriteFood = favoriteFood;
  }
  
  eatFavFood() {
    console.log(`"Mmmm! Those ${this.favoriteFood} were delicious", said ${this.name} the ${this.age} year old bunny.`);
  };
}

// Au lieu de cela, nous obtenons ceci : Uncaught ReferenceError: Bunny is not defined
```

La raison de cette limitation est que les _classes_ peuvent avoir une clause _extends_ — utilisée pour l'héritage — dont la valeur peut être spécifiée plus tard ou peut même dépendre d'une valeur saisie ou d'un calcul. Puisque les expressions peuvent parfois avoir besoin d'être évaluées une autre fois, il est logique que cette évaluation ne soit pas hissée avant que toutes les valeurs ne soient évaluées. Ne pas le faire peut causer des erreurs dans votre code.

Néanmoins, il est possible de stocker une instance d'une _class_ avant qu'elle ne soit créée dans une fonction pour une utilisation ultérieure et de l'évaluer après que la _class_ ait été définie :

```js
function createNewBunny() { new Bunny(); }
createNewBunny(); // ReferenceError

class Bunny {...etc}
createNewBunny(); // Fonctionne !
```

La deuxième façon de définir une classe est une expression de _class_. Comme avec les expressions de fonction, les expressions de _class_ peuvent être nommées ou anonymes. Soyez conscient que ces noms sont seulement locaux au corps de la _class_ et ne peuvent pas être accessibles en dehors de celui-ci :

```js
// anonyme :
const Bunny = class {
  etc...
};
const BunnyBurgerKins = new Bunny();

// nommée
const Bunny = class SurferBunny {
  whatIsMyName() {
    return SurferBunny.name;
  }
};
const BunnyBurgerKins = new Bunny();

console.log(BunnyBurgerKins.whatIsMyName()); // SurferBunny
console.log(SurferBunny.name); // ReferenceError: SurferBunny is not defined
```

Il existe deux types de _classes_ : La _class_ de base — ou la classe parente — et la _class_ dérivée — la sous-classe héritée. Ici, _Bunny_ est la classe de base et _BelgianHare_ est la classe dérivée puisqu'elle a la clause _extends_. Remarquez à quel point la syntaxe pour l'héritage de prototype est simple avec les _classes_ :

```js
class Bunny {
  constructor(name, age, favoriteFood){
    this.name = name;
    this.age = age;
    this.favoriteFood = favoriteFood;
  }
  
  eatFavFood() {
    console.log(`"Mmmm! That ${this.favoriteFood} was delicious", said ${this.name} the ${this.age} year old bunny.`);
  };
}

class BelgianHare extends Bunny {
  constructor(favDrink, favoriteFood, name, age) {
    super(name, age, favoriteFood);
    this.favDrink = favDrink;
  }
  
  drinkFavDrink() {
    console.log(`\"Thank you for the ${this.favDrink} and ${this.favoriteFood}!\", said ${this.name} the happy ${this.age} year old Belgian Hare bunny.`)
  }
}

let newBelgHare = new BelgianHare('Water', 'Grass', 'Donald', 5);
newBelgHare.drinkFavDrink();
// "Thank you for the Water and Grass!", said Donald the happy 5 year old Belgian Hare bunny.
newBelgHare.eatFavFood();
// "Mmmm! That Grass was delicious", said Donald the 5 year old bunny.
```

La fonction _super()_ à l'intérieur de la _class_ dérivée, _BelgianHare_, nous donne accès au _constructor_ dans la _class_ de base, _Bunny_, donc lorsque nous appelons les méthodes de prototype des deux _classes_ (_drinkFavDrink()_ de la _class_ dérivée, et _eatFavFood()_ de la _class_ de base), elles fonctionnent toutes les deux !

#### Compatibilité avec les Navigateurs

Toutes les fonctionnalités ES6 ne sont pas encore entièrement supportées par tous les navigateurs. En attendant, restez à jour en consultant ces sites :

* Voir le tableau de compatibilité : [https://kangax.github.io/compat-table/es6/](https://kangax.github.io/compat-table/es6/)
* Entrez n'importe quelle fonctionnalité ES6 manuellement : [http://caniuse.com/#search=const](http://caniuse.com/#search=const)

#### Transpilation du Code ES6

Puisque tous les navigateurs ne supportent pas toutes les fonctionnalités ES6, vous devez transpiler votre code ES6 dans un compilateur comme _Babel_ ou un bundler de modules comme _Webpack_.

La transpilation signifie simplement prendre du code ES6 et le convertir en ES5 afin qu'il puisse être lu par tous les navigateurs — comme une précaution de sécurité !

Il existe de nombreux outils de transpilation, les plus populaires sont également ceux qui supportent le plus de fonctionnalités ES6 :

* _Babel.js_
* _Closure_
* _Traceur_

Vous pouvez utiliser n'importe lequel de ceux-ci, mais parmi les trois listés, je recommanderais _Babel_ pour les petits projets. Veuillez suivre leurs étapes simples pour installer _Babel_ dans votre projet via _Node_ : [https://babeljs.io/](https://babeljs.io/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YHKpM73vm1u2fvrKgYcYYw.png)

Pour les projets plus importants, je recommande d'utiliser _Webpack_. _Webpack_ fait beaucoup de choses compliquées pour vous, y compris : la transpilation de code, les conversions SAS, la gestion des dépendances, et même le remplacement d'outils tels que _Grunt_, _Gulp_ et _Browserify_. Il existe déjà un tutoriel informatif écrit sur Webpack juste ici [here](https://medium.com/@dabit3/beginner-s-guide-to-webpack-b1f1a3638460#.mu2kgudga).

#### Ressources

Consultez ces ressources pour apprendre et explorer ES6 en profondeur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*h6QrITdqOjVWG9-e3nkLSA.png)

Le Mozilla Developer Network (MDN) est un outil superbe pour apprendre tous les concepts ES6, en fait tout ce qui concerne JavaScript. Par exemple, apprenons-en plus sur les _classes_ : [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)

Babel.js a un article super utile qui résume tous nos points ES6 en un seul : [https://babeljs.io/docs/learn-es2015/](https://babeljs.io/docs/learn-es2015/)

Ce gars est toujours amusant à regarder : [https://www.youtube.com/playlist?list=PL0zVEGEvSaeHJppaRLrqjeTPnCH6vw-sm](https://www.youtube.com/playlist?list=PL0zVEGEvSaeHJppaRLrqjeTPnCH6vw-sm)

Et consultez cette liste exhaustive de ressources d'étude ES6 : [https://github.com/ericdouglas/ES6-Learning](https://github.com/ericdouglas/ES6-Learning)

Il y en a beaucoup, beaucoup plus. Allez de l'avant mon enfant, explore ton internet.

Rappelez-vous, peu importe votre expérience — Google est votre ami.

Félicitations ! Vous avez réussi à traverser **Apprendre ES6 à la manière cool** Partie V et maintenant vous avez appris une manière astucieuse d'utiliser l'héritage de prototype à travers les _classes_ ES6, vous comprenez qu'il est important de _toujours_ transpiler votre code puisque tous les navigateurs ne supportent pas _toutes_ les fonctionnalités de ES6 — soit via _Babel.js_ pour les petits projets ou _Webpack_ pour les projets plus importants.

Gardez votre sagesse à jour en aimant et en suivant. C'est la dernière leçon de la série **Apprendre ES6 à la manière cool** ! Félicitations, vous avez réussi !! Tapez-vous dans le dos, vous avez fait du bon travail !! Je suis si fier de vous ! Hourra !!!

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ecYe92TjNDCisDHLDH_4Q.gif)

**Merci d'avoir lu 💖** Restez à l'écoute pour plus de leçons JavaScript en cours !

**[Partie I : const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Partie II : Fonctions (Flèche) => et mot-clé 'this'](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Partie III : Littéraux de Gabarit, Opérateurs de Décomposition & Générateurs !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Partie IV : Paramètres par Défaut, Affectation par Décomposition, et une nouvelle méthode ES6 !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Partie V : Classes, Transpilation du Code ES6 & Plus de Ressources !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

Vous pouvez également me trouver sur github 💖 [https://github.com/Mashadim](https://github.com/Mashadim)