---
title: 'Apprendre ES6 à la manière cool Partie III : Littéraux de gabarit, Opérateurs
  de propagation et Générateurs !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-14T08:50:52.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294
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
seo_title: 'Apprendre ES6 à la manière cool Partie III : Littéraux de gabarit, Opérateurs
  de propagation et Générateurs !'
seo_desc: 'By Mariya Diminsky

  Welcome to Part III of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  Let’s adventure further into ES6 and cover three super valuable concepts:


  Template Literals

  Spread Operators

  Generat...'
---

Par Mariya Diminsky

Bienvenue dans la Partie III de **Apprendre ES6 à la manière cool**, une série créée pour vous aider à comprendre facilement ES6 (ECMAScript 6) !

Aventurez-vous plus loin dans ES6 et couvrez trois concepts super précieux :

* Littéraux de gabarit
* Opérateurs de propagation
* Générateurs

#### Littéraux de gabarit

Avantages :

* Interpolation facile des expressions et appels de méthodes ! Voir les exemples ci-dessous.
* Inclure des informations complexes dans le format que vous voulez est simple !
* Vous n'avez pas à vous soucier des multiples marques de citation, des multi-lignes, des espaces, ou de l'utilisation du signe "+" non plus ! Seules deux backticks reconnaissent toutes les informations à l'intérieur d'elles ! Youpi !

Attention :

* Communément appelés "Template Strings", car c'était leur nom dans les éditions précédentes de la spécification ES2015 / ES6.
* Les variables et paramètres doivent être enveloppés dans un signe dollar et des accolades, c'est-à-dire _placeholder_ ${EXAMPLE}.
* Le signe plus, "+", à l'intérieur d'un littéral de gabarit agit littéralement comme une opération mathématique, pas une concaténation s'il est aussi à l'intérieur de ${}. Voir les exemples ci-dessous pour plus d'explications.

#### Migration vers la syntaxe des littéraux de gabarit

Après avoir passé en revue les avantages et les éléments à connaître, notez ces exemples et étudiez les différences subtiles avec l'utilisation des littéraux de gabarit :

```js
// #1
// Avant :
function sayHi(petSquirrelName) { console.log('Greetings ' + petSquirrelName + '!'); }
sayHi('Brigadier Sir Nutkins II'); // => Greetings Brigadier Sir Nutkins II!

// Après :
function sayHi(petSquirrelName) { console.log(`Greetings ${petSquirrelName}!`); }
sayHi('Brigadier Sir Nutkins II'); // => Greetings Brigadier Sir Nutkins II!

// #2
// Avant :
console.log('first text string \n' + 'second text string'); 
// => first text string 
// => second text string

// Après :
console.log(`first text string 
second text string`); 
// => first text string 
// => second text string

// #3
// Avant :
var num1 = 5;
var num2 = 10;
console.log('She is ' + (num1 + num2) +  ' years old and\nnot ' + (2 * num1 + num2) + '.');
// => She is 15 years old and
// => not 20.

// Après :
var num1 = 5;
var num2 = 10;
console.log(`She is ${num1 + num2} years old and\nnot ${2 * num1 + num2}.`);
// => She is 15 years old and
// => not 20.

// #4 
// Avant :
var num1 = 12;
var num2 = 8;
console.log('The number of JS MVC frameworks is ' + (2 * (num1 + num2)) + ' and not ' + (10 * (num1 + num2)) + '.');
//=> The number of JS frameworks is 40 and not 200.

// Après :
var num1 = 12;
var num2 = 8;
console.log(`The number of JS MVC frameworks is ${2 * (num1 + num2)} and not ${10 * (num1 + num2)}.`);
//=> The number of JS frameworks is 40 and not 200.

// #5
// Le ${} fonctionne bien avec tout type d'expression, y compris les appels de méthode :
// Avant :
var registeredOffender = {name: 'Bunny BurgerKins'};
console.log((registeredOffender.name.toUpperCase()) + ' you have been arrested for the possession of illegal carrot bits!');
// => BUNNY BURGERKINS you have been arrested for the possession of illegal carrot bits!

// Après :
var registeredOffender = {name: 'Bunny BurgerKins'};
console.log(`${registeredOffender.name.toUpperCase()} you have been arrested for the possession of illegal carrot bits!`);
// => BUNNY BURGERKINS you have been arrested for the possession of illegal carrot bits!
```

Regardons une manière encore plus complexe d'utiliser les littéraux de gabarit ! Voyez à quel point il est facile d'inclure toutes ces informations sans se soucier de tous les signes "+", des espaces, de la logique mathématique et du placement des guillemets ! Cela peut être _si_ pratique ! Notez également que vous devrez inclure un autre signe dollar, à l'extérieur du placeholder, si vous imprimez des prix :

```js
function bunnyBailMoneyReceipt(bunnyName, bailoutCash) {
  var bunnyTip = 100;
  
  console.log(
    `
    Greetings ${bunnyName.toUpperCase()}, you have been bailed out!
    
      Total: $${bailoutCash}
      Tip: $${bunnyTip}
      ------------
      Grand Total: $${bailoutCash + bunnyTip}
    
    We hope you a pleasant carrot nip-free day!  
    
  `
  );

}

bunnyBailMoneyReceipt('Bunny Burgerkins', 200);

// Entrez le code ci-dessus dans votre console pour obtenir ce résultat :
/* 
  Greetings BUNNY BURGERKINS, you have been bailed out!
    
      Total: $200
      Tip: $100
      ------------
      Grand Total: $300
    
    We hope you a pleasant carrot nip-free day! 
*/
```

Wow, c'est tellement plus simple !! C'est si excitant... Ahh !!

![Image](https://cdn-media-1.freecodecamp.org/images/PLbJ5KyPdRVJmbS-4MXy5XC5eZ5EcHtDw6f4)

#### Opérateurs de propagation

Si vous avez plusieurs arguments dans un tableau que vous voulez insérer dans un appel de fonction, ou plusieurs tableaux et/ou éléments de tableau que vous voulez insérer dans un autre tableau de manière transparente, utilisez les opérateurs de propagation !

Avantages :

* Concatène facilement les tableaux à l'intérieur d'autres tableaux.
* Placez les tableaux où vous voulez à l'intérieur de ce tableau.
* Ajoute facilement des arguments dans l'appel de fonction.
* Juste 3 points '...' avant le nom du tableau.
* Similaire à _function.apply_ mais peut être utilisé avec le mot-clé _new_, tandis que _function.apply_ ne le peut pas.

Regardons une situation où nous voudrions ajouter plusieurs tableaux dans un autre tableau principal sans utiliser l'opérateur de propagation :

```js
var squirrelNames = ['Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom'];
var bunnyNames = ['Lady FluffButt', 'Brigadier Giant'];
var animalNames = ['Lady Butt', squirrelNames, 'Juicy Biscuiteer', bunnyNames];

animalNames;
// => ['Lady Butt', ['Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom'], 'Juicy Biscuiteer', ['Lady FluffButt', 'Brigadier Giant']]

// Pour aplatir ce tableau, nous avons besoin d'une autre étape :
var flattened = [].concat.apply([], animalNames);
flattened;
// => ['Lady Butt', 'Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom', 'Juicy Biscuiteer', 'Lady FluffButt', 'Brigadier Giant']

```

Avec l'opérateur de propagation, vos tableaux sont automatiquement insérés et concaténés où vous le souhaitez. Pas besoin d'étapes supplémentaires :

```js
var squirrelNames = ['Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom'];
var bunnyNames = ['Lady FluffButt', 'Brigadier Giant'];
var animalNames = ['Lady Butt', ...squirrelNames, 'Juicy Biscuiteer', ...bunnyNames];

animalNames;
// => ['Lady Butt', 'Lady Nutkins', 'Squirrely McSquirrel', 'Sergeant Squirrelbottom', 'Juicy Biscuiteer', 'Lady FluffButt', 'Brigadier Giant']

```

Un autre exemple utile :

```js
var values = [25, 50, 75, 100]

// Ceci :
console.log(Math.max(25, 50, 75, 100)); // => 100

// Est la même chose que ceci :
console.log(Math.max(...values)); // => 100

/* 
  NOTE: Math.max() ne fonctionne généralement pas pour les tableaux sauf si vous l'écrivez comme :
        Math.max.apply(null, values), mais avec les opérateurs de propagation, vous pouvez simplement l'insérer
        et voilà ! Pas besoin de la partie .apply() ! Youpi ! :)
*/
```

#### Potentiellement plus utile que .apply()

Et si vous avez plusieurs arguments à placer à l'intérieur d'une fonction ? Vous pourriez utiliser le bon vieux _Function.prototype.apply_ :

```js
function myFunction(x, y, z) {
  console.log(x + y + z)
};
var args = [0, 1, 2];
myFunction.apply(null, args);
// => 3
```

Ou utiliser l'opérateur de propagation :

```js
function myFunction(x, y, z) {
  console.log(x + y + z);
}
var args = [0, 1, 2];
myFunction(...args);
// => 3
```

En ES5, il n'est pas possible de composer le mot-clé _new_ avec la méthode _apply_. Depuis l'introduction de la syntaxe de l'opérateur de propagation, vous pouvez maintenant !

```js
var dateFields = readDateFields(database);
var d = new Date(...dateFields);
```

#### Générateurs

Avantages :

* Vous permet de mettre en pause des fonctions pour les reprendre plus tard.
* Plus facile de créer des fonctions asynchrones.
* Utilisé couramment avec _setTimeout()_ ou _setInterval()_ pour chronométrer des événements asynchrones.

À savoir :

* Vous savez que vous regardez un générateur si vous voyez * et le mot _yield_.
* Vous devez appeler la fonction chaque fois pour que la fonction suivante à l'intérieur soit appelée, sinon elle ne s'exécutera pas, sauf si elle est dans un _setInterval()_.
* Le résultat sort naturellement sous forme d'objet, ajoutez ._value_ pour obtenir la valeur uniquement.
* L'objet vient avec une propriété _done_ qui est définie sur false jusqu'à ce que toutes les expressions _yield_ soient imprimées.
* Les générateurs se terminent soit lorsque toutes les fonctions/valeurs ont été appelées, soit si une instruction _return_ est présente.

Exemple :

```js
function* callMe() {
  yield '1';
  yield '...and a 2';
  yield '...and a 3';
  return;
  yield 'this won’t print';
}

var anAction = callMe();

console.log(anAction.next());
//=> { value: '1', done: false }

console.log(anAction.next());
//=> { value: '...and a 2', done: false }

console.log(anAction.next());
//=> { value: '...and a 3', done: false }

console.log(anAction.next());
//=> { value: 'undefined', done: true }

console.log(anAction.next());
//=> { value: 'undefined', done: true }

// NOTE: Pour obtenir uniquement la valeur, utilisez anAction.next().value, sinon l'objet entier sera imprimé.

```

Les générateurs sont super utiles lorsqu'il s'agit d'appels de fonctions asynchrones. Supposons que vous avez 3 fonctions différentes que vous avez stockées dans un tableau et que vous voulez appeler chacune l'une après l'autre après un certain temps :

```js
// Bunny doit faire les courses pour l'anniversaire de son ami.
var groceries = '';

// Créons trois fonctions qui doivent être appelées pour Bunny.
var buyCarrots = function () {
  groceries += 'carrots';
}

var buyGrass = function () {
  groceries += ', grass';
}

var buyApples = function () {
  groceries += ', and apples';
}

// Bunny est pressée, vous devez donc acheter les courses dans un certain temps !
// Voici un exemple de quand vous utiliseriez un minuteur avec un générateur.
// D'abord, stockez les fonctions dans un tableau :
var buyGroceries = [buyCarrots, buyGrass, buyApples];

// Ensuite, parcourez le tableau dans un générateur :
// Il y a quelques problèmes avec forEach, recréez ceci en utilisant une boucle for.
function* loopThrough(arr) {
  for(var i=0; i<arr.length; i++) {
    yield arr[i]();
  }
}

// ajoutez le tableau des trois fonctions à la fonction loopThrough.
var functions = loopThrough(buyGroceries);

// Enfin, définissez le temps que vous voulez pause avant l'appel de la fonction suivante
// en utilisant la méthode setInterval (appelle une fonction/expression après un temps défini).
var timedGroceryHunt = setInterval(function() {
  var functionCall = functions.next();
  if(!functionCall.done) {
    console.log(`Bunny bought ${groceries}!`);
  }else {
    clearInterval(timedGroceryHunt);
    console.log(`Thank you! Bunny bought all the ${groceries} in time thanks to your help!`);
  }
}, 1000);

// Entrez ce code dans votre console pour le tester !
// après 1 seconde : => Bunny bought carrots!
// après 1 seconde : => Bunny bought carrots, grass!
// après 1 seconde : => Bunny bought carrots, grass, and apples!
// après 1 seconde : => Thank you! Bunny bought all the carrots, grass, and apples in time thanks to your help!

```

Cela peut également être accompli via une _promise_ (une opération qui n'a pas encore été complétée, mais qui est attendue dans le futur). Les développeurs utilisent parfois des promesses et des générateurs ensemble dans leur code, il est donc bon de connaître les deux.

Félicitations ! Vous avez réussi à traverser **Apprendre ES6 à la manière cool** Partie III et vous avez maintenant acquis trois concepts super précieux ! Vous pouvez maintenant vous rafraîchir la mémoire et faire un usage efficace des littéraux de gabarit, des opérateurs de propagation et des générateurs dans votre code. Youpi ! Allez-y !

Cependant, vous pourriez vouloir attendre car il y a encore des problèmes de navigateur avec ES6 et il est important d'utiliser des compilateurs comme _Babel_ ou un bundler de modules comme _Webpack_ avant de publier votre code. Tous ces sujets seront discutés dans les futures éditions de **Apprendre ES6 à la manière cool ! Merci d'avoir lu** **❤**

Gardez votre sagesse à jour en aimant et en suivant car plus de **Apprendre ES6 à la manière cool** arrive bientôt sur Medium !

**[Partie I : const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Partie II : Fonctions (fléchées) => et mot-clé 'this'](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Partie III : Littéraux de gabarit, Opérateurs de propagation et Générateurs !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Partie IV : Paramètres par défaut, Affectation par décomposition, et une nouvelle méthode ES6 !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Partie V : Classes, Transpilation du code ES6 et plus de ressources !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

Vous pouvez également me trouver sur github ❤ [https://github.com/Mashadim](https://github.com/Mashadim)