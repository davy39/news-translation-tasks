---
title: Tout ce que vous devez savoir pour comprendre le Prototype de JavaScript
subtitle: ''
author: Shirshendu Bhowmick
co_authors: []
series: null
date: '2019-04-03T22:16:46.000Z'
originalURL: https://freecodecamp.org/news/all-you-need-to-know-to-understand-javascripts-prototype-a2bff2d28f03
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bgfErxHxXBw-Ccm4OMu7_w.png
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
seo_title: Tout ce que vous devez savoir pour comprendre le Prototype de JavaScript
seo_desc: 'Most of the time, JavaScript’s prototype confuses people who have just
  started to learn JavaScript — especially if they’re from a C++ or Java background.

  In JavaScript, inheritance works a bit differently compared to C++ or Java. JavaScript
  inheritan...'
---

La plupart du temps, le prototype de JavaScript confond les personnes qui viennent de commencer à apprendre JavaScript — surtout si elles viennent d'un milieu C++ ou Java.

En JavaScript, l'héritage fonctionne un peu différemment par rapport à C++ ou Java. L'héritage JavaScript est plus largement connu sous le nom d'« héritage prototypal ».

Les choses deviennent plus difficiles à comprendre lorsque vous rencontrez également `class` en JavaScript. La nouvelle syntaxe `class` ressemble à C++ ou Java, mais en réalité, elle fonctionne différemment.

Dans cet article, nous allons essayer de comprendre l'« héritage prototypal » en JavaScript. Nous examinons également la nouvelle syntaxe basée sur les `class` et essayons de comprendre ce qu'elle est réellement. Alors commençons.

Tout d'abord, nous allons commencer avec l'ancienne école JavaScript fonction et prototype.

#### Comprendre le besoin de prototype

Si vous avez déjà travaillé avec des tableaux JavaScript, des objets ou des chaînes, vous avez remarqué qu'il y a quelques méthodes disponibles par défaut.

Par exemple :

```
var arr = [1,2,3,4];arr.reverse(); // retourne [4,3,2,1]
```

```
var obj = {id: 1, value: "Some value"};obj.hasOwnProperty('id'); // retourne true
```

```
var str = "Hello World";str.indexOf('W'); // retourne 6
```

Vous êtes-vous déjà demandé d'où viennent ces méthodes ? Vous n'avez pas défini ces méthodes vous-même.

Pouvez-vous définir vos propres méthodes comme ceci ? Vous pourriez dire que vous pouvez de cette manière :

```
var arr = [1,2,3,4];arr.test = function() {    return 'Hi';}arr.test(); // retournera 'Hi'
```

Cela fonctionnera, mais seulement pour cette variable appelée `arr`. Supposons que nous ayons une autre variable appelée `arr2`, alors `arr2.test()` lancera une erreur « TypeError: arr2.test n'est pas une fonction ».

Alors, comment ces méthodes deviennent-elles disponibles pour chaque instance de tableau/chaîne/objet ? Pouvez-vous créer vos propres méthodes avec le même comportement ? La réponse est oui. Vous devez le faire de la bonne manière. Pour vous aider, voici le prototype de JavaScript.

Voyons d'abord d'où viennent ces fonctions. Considérez l'extrait de code ci-dessous :

```
var arr1 = [1,2,3,4];var arr2 = Array(1,2,3,4);
```

Nous avons créé deux tableaux de deux manières différentes : `arr1` avec des littéraux de tableau et `arr2` avec la fonction constructeur `Array`. Les deux sont équivalents l'un à l'autre avec quelques différences qui n'ont pas d'importance pour cet article.

Maintenant, en ce qui concerne la fonction constructeur `Array` — c'est une fonction constructeur prédéfinie en JavaScript. Si vous ouvrez les outils de développement Chrome et allez dans la console et tapez `console.log(Array.prototype)` et appuyez sur `enter`, vous verrez quelque chose comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/LgPwy0jWfYBMdxUPmjdTAtDVZmyBkYFE-x8s)
_Fig: 1_

Là, vous verrez toutes les méthodes dont nous nous demandions. Donc maintenant nous savons d'où viennent ces fonctions. N'hésitez pas à essayer avec `String.prototype` et `Object.prototype`.

Créons notre propre fonction constructeur simple :

```
var foo = function(name) { this.myName = name; this.tellMyName = function() {   console.log(this.myName); }}
```

```
var fooObj1 = new foo('James');fooObj1.tellMyName(); // imprimera Jamesvar fooObj2 = new foo('Mike');fooObj2.tellMyName(); // imprimera Mike
```

Pouvez-vous identifier un problème fondamental avec le code ci-dessus ? Le problème est que nous gaspillons de la mémoire avec l'approche ci-dessus. Notez que la méthode `tellMyName` est la même pour chaque instance de `foo`. Chaque fois que nous créons une instance de `foo`, la méthode `tellMyName` finit par prendre de la place dans la mémoire du système. Si `tellMyName` est la même pour toutes les instances, il est préférable de la garder à un seul endroit et de faire en sorte que toutes nos instances y fassent référence. Voyons comment faire cela.

```
var foo = function(name) { this.myName = name;}
```

```
foo.prototype.tellMyName = function() {   console.log(this.myName);}
```

```
var fooObj1 = new foo('James');fooObj1.tellMyName(); // imprimera Jamesvar fooObj2 = new foo('Mike');fooObj2.tellMyName(); // imprimera Mike
```

Vérifions la différence avec l'approche ci-dessus et l'approche précédente. Avec l'approche ci-dessus, si vous `console.dir()` les instances, vous verrez quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/cCfrooHWD8qhcTEt6sqlXGI6hNVo-MT00Icv)
_Fig: 2_

Notez que comme propriété des instances, nous n'avons que `myname`. `tellMyName` est défini sous `__proto__`. Je reviendrai sur ce `__proto__` plus tard. Plus important encore, notez que la comparaison de `tellMyName` des deux instances évalue à vrai. La comparaison de fonctions en JavaScript évalue vrai uniquement si leurs références sont les mêmes. Cela prouve que `tellMyName` ne consomme pas de mémoire supplémentaire pour plusieurs instances.

Voyons la même chose avec l'approche précédente :

![Image](https://cdn-media-1.freecodecamp.org/images/ZNgTtP4W2av-lJDUoRDdf7DmuWtnGumvbFUe)
_Fig: 3_

Notez que cette fois `tellMyName` est défini comme une propriété des instances. Il n'est plus sous ce `__proto__`. Notez également que cette fois, la comparaison des fonctions évalue à faux. Cela est dû au fait qu'elles se trouvent à deux emplacements mémoire différents et que leurs références sont différentes.

J'espère qu'à présent vous comprenez la nécessité du `prototype`.

Maintenant, regardons quelques détails supplémentaires sur le prototype.

Chaque fonction JavaScript aura une propriété `prototype` qui est de type objet. Vous pouvez définir vos propres propriétés sous `prototype`. Lorsque vous utiliserez la fonction comme fonction constructeur, toutes les instances en hériteront des propriétés de l'objet `prototype`.

Maintenant, venons-en à cette propriété `__proto__` que vous avez vue ci-dessus. Le `__proto__` est simplement une référence à l'objet prototype dont l'instance a hérité. Cela semble compliqué ? En réalité, ce n'est pas si compliqué. Visualisons cela avec un exemple.

Considérez le code ci-dessous. Nous savons déjà que la création d'un Array avec des littéraux de tableau héritera des propriétés de `Array.prototype`.

```
var arr = [1, 2, 3, 4];
```

Ce que je viens de dire ci-dessus est « Le `__proto__` est simplement une référence à l'objet prototype dont l'instance a hérité ». Donc `arr.__proto__` devrait être le même que `Array.prototype`. Vérifions cela.

![Image](https://cdn-media-1.freecodecamp.org/images/j8gJ-ryF1SW3bo7IWNnJoreG3Hp5vy1ZSIbx)
_Fig: 4_

Maintenant, nous ne devrions pas accéder à l'objet prototype avec `__proto__`. Selon MDN, l'utilisation de `__proto__` est fortement déconseillée et peut ne pas être supportée dans tous les navigateurs. La bonne façon de faire cela est :

```
var arr = [1, 2, 3, 4];var prototypeOfArr = Object.getPrototypeOf(arr);prototypeOfArr === Array.prototype;prototypeOfArr === arr.__proto__;
```

![Image](https://cdn-media-1.freecodecamp.org/images/WJ6FyFSXejZFU4QONss9YDsZqDLX64UWRYwM)
_Fig: 5_

La dernière ligne de l'extrait de code ci-dessus montre que `__proto__` et `Object.getPrototypeOf` retournent la même chose.

Maintenant, il est temps de faire une pause. Prenez un café ou ce que vous aimez et essayez les exemples ci-dessus par vous-même. Une fois que vous êtes prêt, revenez à cet article et nous continuerons.

#### Chaînage de prototypes et héritage

Dans la Fig: 2 ci-dessus, avez-vous remarqué qu'il y a un autre `__proto__` à l'intérieur du premier objet `__proto__` ? Si ce n'est pas le cas, faites défiler un peu vers le haut jusqu'à la Fig: 2. Jetez un coup d'œil et revenez ici. Nous allons maintenant discuter de ce que c'est réellement. Cela est connu sous le nom de chaînage de prototypes.

En JavaScript, nous réalisons l'héritage avec l'aide du chaînage de prototypes.

Considérez cet exemple : Nous comprenons tous le terme « Véhicule ». Un bus pourrait être appelé un véhicule. Une voiture pourrait être appelée un véhicule. Une moto pourrait être appelée un véhicule. Bus, voiture et moto ont quelques propriétés communes, c'est pourquoi ils sont appelés véhicules. Par exemple, ils peuvent se déplacer d'un endroit à un autre. Ils ont des roues. Ils ont des klaxons, etc.

Encore une fois, bus, voiture et moto peuvent être de différents types, par exemple Mercedes, BMW, Honda, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/LmR5EM367CwHz0BXh8o9jBeAPjbIjmfYjFNz)
_Fig: 6_

Dans l'illustration ci-dessus, Bus hérite de certaines propriétés de véhicule, et Mercedes Benz Bus hérite de certaines propriétés de bus. Il en va de même pour Car et MotorBike.

Établissons cette relation en JavaScript.

Tout d'abord, supposons quelques points pour simplifier :

1. Tous les bus ont 6 roues
2. Les procédures d'accélération et de freinage sont différentes pour les bus, les voitures et les motos, mais les mêmes pour tous les bus, toutes les voitures et toutes les motos.
3. Tous les véhicules peuvent klaxonner.

```
function Vehicle(vehicleType) {  //Constructeur de véhicule    this.vehicleType = vehicleType;}
```

```
Vehicle.prototype.blowHorn = function () {    console.log('Honk! Honk! Honk!'); // Tous les véhicules peuvent klaxonner}
```

```
function Bus(make) { // Constructeur de Bus  Vehicle.call(this, "Bus");      this.make = make}
```

```
Bus.prototype = Object.create(Vehicle.prototype); // Faire en sorte que le constructeur Bus hérite des propriétés de l'objet Prototype Vehicle
```

```
Bus.prototype.noOfWheels = 6; // Supposons que tous les bus ont 6 roues
```

```
Bus.prototype.accelerator = function() {    console.log('Accélération du Bus'); //Accélérateur de Bus}
```

```
Bus.prototype.brake = function() {    console.log('Freinage du Bus'); // Frein de Bus}
```

```
function Car(make) {  Vehicle.call(this, "Car");  this.make = make;}
```

```
Car.prototype = Object.create(Vehicle.prototype);
```

```
Car.prototype.noOfWheels = 4;
```

```
Car.prototype.accelerator = function() {    console.log('Accélération de la Voiture');}
```

```
Car.prototype.brake = function() {    console.log('Freinage de la Voiture');}
```

```
function MotorBike(make) {  Vehicle.call(this, "MotorBike");  this.make = make;}
```

```
MotorBike.prototype = Object.create(Vehicle.prototype);
```

```
MotorBike.prototype.noOfWheels = 2;
```

```
MotorBike.prototype.accelerator = function() {    console.log('Accélération de la Moto');}
```

```
MotorBike.prototype.brake = function() {    console.log('Freinage de la Moto');}
```

```
var myBus = new Bus('Mercedes');var myCar = new Car('BMW');var myMotorBike = new MotorBike('Honda');
```

Permettez-moi d'expliquer l'extrait de code ci-dessus.

Nous avons un constructeur `Vehicle` qui attend un type de véhicule. Comme tous les véhicules peuvent klaxonner, nous avons une propriété `blowHorn` dans le prototype de `Vehicle`.

Comme `Bus` est un véhicule, il héritera des propriétés de l'objet `Vehicle`.

Nous avons supposé que tous les bus auront 6 roues et auront les mêmes procédures d'accélération et de freinage. Nous avons donc `noOfWheels`, `accelerator` et `brake` définis dans le prototype de `Bus`.

Une logique similaire s'applique pour Car et MotorBike.

Allons dans les outils de développement Chrome -> Console et exécutons notre code.

Après exécution, nous aurons 3 objets `myBus`, `myCar` et `myMotorBike`.

Tapez `console.dir(mybus)` dans la console et appuyez sur `enter`. Utilisez l'icône triangle pour l'expanser et vous verrez quelque chose comme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1ST6FxGCAEigEAayuqNpwlUByhTlg3jDm4GR)
_Fig: 7_

Sous `myBus`, nous avons les propriétés `make` et `vehicleType`. Remarquez que la valeur de `__proto__` est le prototype de `Bus`. Toutes les propriétés de son prototype sont disponibles ici : `accelerator`, `brake`, `noOfWheels`.

Maintenant, jetez un coup d'œil au premier objet `__proto__`. Cet objet a un autre objet `__proto__` comme propriété.

Sous lequel nous avons les propriétés `blowHorn` et `constructor`.

```
Bus.prototype = Object.create(Vehicle.prototype);
```

Souvenez-vous de la ligne ci-dessus ? `Object.create(Vehicle.prototype)` créera un objet vide dont le prototype est `Vehicle.prototype`. Nous définissons cet objet comme prototype de `Bus`. Pour `Vehicle.prototype`, nous n'avons pas spécifié de prototype, donc par défaut il hérite de `Object.prototype`.

Regardons la magie ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/VD2RXaotYkPxWd3opcuthx8dX1olyo66LN1Z)
_Fig: 8_

Nous pouvons accéder à la propriété `make` car c'est la propre propriété de `myBus`.

Nous pouvons accéder à la propriété `brake` à partir du prototype de `myBus`.

Nous pouvons accéder à la propriété `blowHorn` à partir du prototype du prototype de `myBus`.

Nous pouvons accéder à la propriété `hasOwnProperty` à partir du prototype du prototype du prototype de `myBus`. :)

Cela s'appelle le chaînage de prototypes. Chaque fois que vous accédez à une propriété d'un objet en JavaScript, il vérifie d'abord si la propriété est disponible à l'intérieur de l'objet. Si ce n'est pas le cas, il vérifie son objet prototype. Si elle s'y trouve, alors bien, vous obtenez la valeur de la propriété. Sinon, il vérifiera si la propriété existe dans le prototype du prototype, si ce n'est pas le cas, alors à nouveau dans le prototype du prototype du prototype, et ainsi de suite.

Alors, combien de temps va-t-il vérifier de cette manière ? Il s'arrêtera si la propriété est trouvée à un moment donné ou si la valeur de `__proto__` à un moment donné est `null` ou `undefined`. Ensuite, il lancera une erreur pour vous notifier qu'il n'a pas pu trouver la propriété que vous cherchiez.

C'est ainsi que fonctionne l'héritage en JavaScript avec l'aide du chaînage de prototypes.

N'hésitez pas à essayer l'exemple ci-dessus avec `myCar` et `myMotorBike`.

Comme nous le savons, en JavaScript, tout est un objet. Vous constaterez que pour chaque instance, la chaîne de prototypes se termine par `Object.prototype`.

L'exception à la règle ci-dessus est si vous créez un objet avec `Object.create(null)`

```
var obj = Object.create(null)
```

Avec le code ci-dessus, `obj` sera un objet vide sans aucun prototype.

![Image](https://cdn-media-1.freecodecamp.org/images/7NnMhJUMOYgjrMLyRW7HWIcJP4bNE0FvCtI7)
_Fig: 9_

Pour plus d'informations sur `Object.create`, consultez la documentation sur MDN.

Pouvez-vous changer l'objet prototype d'un objet existant ? Oui, avec `Object.setPrototypeOf()` vous pouvez. Consultez la documentation sur MDN.

Voulez-vous vérifier si une propriété est la propre propriété de l'objet ? Vous savez déjà comment faire. `Object.hasOwnProperty` vous dira si la propriété provient de l'objet lui-même ou de sa chaîne de prototypes. Consultez sa documentation sur MDN.

Notez que `__proto__` est également appelé `[[Prototype]]`.

Maintenant, il est temps pour une autre pause. Une fois que vous êtes prêt, revenez à cet article. Nous continuerons ensuite et je promets que c'est la dernière partie.

#### Comprendre les Classes en JavaScript

Selon MDN :

> Les classes JavaScript, introduites dans ECMAScript 2015, sont principalement du sucre syntaxique sur l'héritage basé sur les prototypes existants de JavaScript. La syntaxe de classe _ne_ introduit _pas_ un nouveau modèle d'héritage orienté objet à JavaScript.

Les classes en JavaScript fourniront une meilleure syntaxe pour atteindre ce que nous avons fait ci-dessus de manière beaucoup plus propre. Jetons un coup d'œil à la syntaxe des classes d'abord.

```
class Myclass {  constructor(name) {    this.name = name;  }    tellMyName() {    console.log(this.name)  }}
```

```
const myObj = new Myclass("John");
```

La méthode `constructor` est un type spécial de méthode. Elle sera automatiquement exécutée chaque fois que vous créez une instance de cette classe. À l'intérieur du corps de votre classe. Une seule occurrence de `constructor` est possible.

Les méthodes que vous définirez à l'intérieur du corps de la classe seront déplacées vers l'objet prototype.

Si vous voulez une propriété à l'intérieur de l'instance, vous pouvez la définir dans le constructeur, comme nous l'avons fait avec `this.name = name`.

Jetons un coup d'œil à notre `myObj`.

![Image](https://cdn-media-1.freecodecamp.org/images/8YV1-cTjvrf4za0emIjWqvDfmmonmA1287vp)
_Fig: 10_

Notez que nous avons la propriété `name` à l'intérieur de l'instance qui est `myObj` et la méthode `tellMyName` est dans le prototype.

Considérez l'extrait de code ci-dessous :

```
class Myclass {  constructor(firstName) {    this.name = firstName;  }    tellMyName() {    console.log(this.name)  }  lastName = "lewis";}
```

```
const myObj = new Myclass("John");
```

Voyons le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/dY8-i7joXX5hzVuLXbgN4vUENWqoParuuoJW)
_Fig: 11_

Voyez que `lastName` est déplacé dans l'instance au lieu du prototype. Seules les méthodes que vous déclarez à l'intérieur du corps de la classe seront déplacées vers le prototype. Il y a une exception cependant.

Considérez l'extrait de code ci-dessous :

```
class Myclass {  constructor(firstName) {    this.name = firstName;  }    tellMyName = () => {    console.log(this.name)  }  lastName = "lewis";}
```

```
const myObj = new Myclass("John");
```

Résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/GIb2hzCV7C92-Z9L1oEHpr-tJgAFytgrQsdN)
_Fig: 12_

Notez que `tellMyName` est maintenant une fonction fléchée, et elle a été déplacée vers l'instance au lieu du prototype. Donc rappelez-vous que les fonctions fléchées seront toujours déplacées vers l'instance, alors utilisez-les avec précaution.

Jetons un coup d'œil aux propriétés statiques de classe :

```
class Myclass {  static welcome() {    console.log("Hello World");  }}
```

```
Myclass.welcome();const myObj = new Myclass();myObj.welcome();
```

Résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/CpztRyj49N2Wss0c6-o2bqAa3x5dWA3blyC4)
_Fig: 13_

Les propriétés statiques sont quelque chose que vous pouvez accéder sans créer une instance de la classe. D'autre part, l'instance n'aura pas accès aux propriétés statiques d'une classe.

Alors, est-ce que la propriété statique est un nouveau concept qui est disponible uniquement avec la classe et pas dans l'ancien JavaScript ? Non, elle est également présente dans l'ancien JavaScript. L'ancienne méthode pour obtenir une propriété statique est :

```
function Myclass() {}Myclass.welcome = function() {  console.log("Hello World");}
```

Maintenant, jetons un coup d'œil à la manière dont nous pouvons réaliser l'héritage avec des classes.

```
class Vehicle {  constructor(type) {    this.vehicleType= type;  }  blowHorn() {    console.log("Honk! Honk! Honk!");  }}
```

```
class Bus extends Vehicle {  constructor(make) {    super("Bus");    this.make = make;   }  accelerator() {    console.log('Accélération du Bus');  }  brake() {    console.log('Freinage du Bus');  }}
```

```
Bus.prototype.noOfWheels = 6;
```

```
const myBus = new Bus("Mercedes");
```

Nous héritons d'autres classes en utilisant le mot-clé `extends`.

`super()` exécutera simplement le constructeur de la classe parente. Si vous héritez d'autres classes et que vous utilisez le constructeur dans votre classe enfant, alors vous devez appeler `super()` à l'intérieur du constructeur de votre classe enfant, sinon cela lancera une erreur.

Nous savons déjà que si nous définissons une propriété autre qu'une fonction normale dans le corps de la classe, elle sera déplacée vers l'instance au lieu du prototype. Nous définissons donc `noOfWheel` sur `Bus.prototype`.

À l'intérieur du corps de votre classe, si vous voulez exécuter la méthode de la classe parente, vous pouvez le faire en utilisant `super.parentClassMethod()`.

Résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/cSH-VN7BReS2g5-2FkoDEY0dC6DxpeLrG4DD)
_Fig: 14_

Le résultat ci-dessus ressemble à notre approche basée sur les fonctions précédente dans la Fig: 7.

#### Conclusion

Alors, devriez-vous utiliser la nouvelle syntaxe de classe ou l'ancienne syntaxe basée sur les constructeurs ? Je suppose qu'il n'y a pas de réponse définitive à cette question. Cela dépend de votre cas d'utilisation.

Dans cet article, pour la partie sur les classes, j'ai simplement démontré comment vous pouvez réaliser l'héritage prototypal avec les classes. Il y a plus à savoir sur les classes JavaScript, mais cela dépasse le cadre de cet article. Consultez la documentation des classes sur MDN. Ou j'essaierai d'écrire un article entier sur les classes à un moment donné.

Si cet article vous a aidé à comprendre les prototypes, j'apprécierais si vous pouviez applaudir un peu.

Si vous voulez que j'écrive sur un autre sujet, faites-le moi savoir dans les réponses.

Vous pouvez également me contacter sur [LinkedIn](https://www.linkedin.com/in/shirshendubhowmick/).

#### Merci d'avoir lu. :)