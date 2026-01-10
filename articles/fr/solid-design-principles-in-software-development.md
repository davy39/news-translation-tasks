---
title: Principes de conception SOLID en développement logiciel
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-02-16T17:11:16.000Z'
originalURL: https://freecodecamp.org/news/solid-design-principles-in-software-development
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/start-graph--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: solid
  slug: solid
seo_title: Principes de conception SOLID en développement logiciel
seo_desc: "SOLID is a set of five design principles. These principles help software\
  \ developers design robust, testable, extensible, and maintainable object-oriented\
  \ software systems. \nEach of these five design principles solves a particular problem\
  \ that might a..."
---

**SOLID** est un ensemble de cinq principes de conception. Ces principes aident les développeurs de logiciels à concevoir des systèmes logiciels orientés objet robustes, testables, extensibles et maintenables. 

Chacun de ces cinq principes de conception résout un problème particulier qui pourrait survenir lors du développement des systèmes logiciels.

Dans cet article, je vais vous montrer ce que les principes SOLID impliquent, ce que signifie chaque partie de l'acronyme SOLID, et comment les implémenter dans votre code.

## Ce que nous allons couvrir
- [Quels sont les principes de conception SOLID ?](#heading-quest-ce-que-les-principes-de-conception-solid)
  - [Le principe de responsabilité unique (SRP)](#heading-le-principe-de-responsabilite-unique-srp)
  - [Le principe ouvert-fermé (OCP)](#heading-le-principe-ouvert-ferme-ocp)
  - [Le principe de substitution de Liskov (LSP)](#heading-le-principe-de-substitution-de-liskov-lsp)
  - [Le principe de ségrégation des interfaces (ISP)](#heading-le-principe-de-segregation-des-interfaces-isp)
  - [Le principe d'inversion des dépendances (DIP)](#heading-le-principe-dinversion-des-dependances-dip)
- [Conclusion](#heading-conclusion) 


## Quels sont les principes de conception SOLID ?
SOLID est un acronyme qui signifie : 

- Principe de responsabilité unique (SRP)
- Principe ouvert-fermé (OCP)
- Principe de substitution de Liskov (LSP)
- Principe de ségrégation des interfaces (ISP)
- Principe d'inversion des dépendances (DIP)

Dans les sections suivantes, nous examinerons ce que signifie chacun de ces principes en détail.

Les principes de conception SOLID sont une sous-catégorie de nombreux principes introduits par l'informaticien et instructeur américain, Robert C. Martin (alias Uncle Bob) dans un article de 2000.

Le suivi de ces principes peut entraîner une base de code très volumineuse pour un système logiciel. Mais à long terme, l'objectif principal des principes n'est jamais vaincu. C'est-à-dire, aider les développeurs de logiciels à apporter des modifications à leur code sans causer de problèmes majeurs.


### Le principe de responsabilité unique (SRP)
Le principe de responsabilité unique stipule qu'une classe, un module ou une fonction ne doit avoir qu'une seule raison de changer, ce qui signifie qu'elle doit faire une seule chose.

Par exemple, une classe qui affiche le nom d'un animal ne doit pas être la même classe qui affiche le type de son qu'il émet et comment il se nourrit. 

Voici un exemple en JavaScript :
```js
class Animal {
  constructor(name, feedingType, soundMade) {
    this.name = name;
    this.feedingType = feedingType;
    this.soundMade = soundMade;
  }

  nomenclature() {
    console.log(`Le nom de l'animal est ${this.name}`);
  }

  sound() {
    console.log(`${this.name} ${this.soundMade}s`);
  }

  feeding() {
    console.log(`${this.name} est un ${this.feedingType}`);
  }
}

let elephant = new Animal('Elephant', 'herbivore', 'trumpet');
elephant.nomenclature(); // Le nom de l'animal est Elephant
elephant.sound(); // Elephant trumpet
elephant.feeding(); // Elephant est un herbivore
```

Le code ci-dessus viole le principe de responsabilité unique car la classe responsable de l'impression du nom de l'animal montre également le son qu'il émet et son type d'alimentation.

Pour corriger cela, vous devez créer une classe séparée pour les méthodes de son et d'alimentation comme ceci :
```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  nomenclature() {
    console.log(`Le nom de l'animal est ${this.name}`);
  }
}

let animal1 = new Animal('Elephant');
animal1.nomenclature(); // Le nom de l'animal est Elephant

// Classe Sound
class Sound {
  constructor(name, soundMade) {
    this.name = name;
    this.soundMade = soundMade;
  }

  sound() {
    console.log(`${this.name} ${this.soundMade}s`);
  }
}

let animalSound1 = new Sound('Elephant', 'trumpet');
animalSound1.sound(); // Elephant trumpet

// Classe Feeding
class Feeding {
  constructor(name, feedingType) {
    this.name = name;
    this.feedingType = feedingType;
  }

  feeding() {
    console.log(`${this.name} est un ${this.feedingType}`);
  }
}

let animalFeeding1 = new Feeding('Elephant', 'herbivore');
animalFeeding1.feeding(); // Elephant est un herbivore

``` 

De cette manière, chacune des classes ne fait qu'une seule chose :
- la première imprime le nom de l'animal
- la seconde imprime le type de son qu'il émet
- et la troisième imprime son type d'alimentation.

C'est plus de code, mais une meilleure lisibilité et maintenabilité. Un développeur qui n'a pas écrit le code peut le comprendre et voir ce qui se passe plus rapidement que si tout était dans une seule classe.


### Le principe ouvert-fermé (OCP)
Le principe ouvert-fermé stipule que les classes, modules et fonctions doivent être ouverts pour l'extension mais fermés pour la modification.

Ce principe peut sembler se contredire, mais vous pouvez toujours en comprendre le sens dans le code. Cela signifie que vous devriez pouvoir étendre la fonctionnalité d'une classe, d'un module ou d'une fonction en ajoutant plus de code sans modifier le code existant.

Voici un exemple de code qui viole le principe ouvert-fermé en JavaScript :
```js
class Animal {
  constructor(name, age, type) {
    this.name = name;
    this.age = age;
    this.type = type;
  }

  getSpeed() {
    switch (this.type) {
      case 'cheetah':
        console.log('Le guépard court jusqu'à 130 mph');
        break;
      case 'lion':
        console.log('Le lion court jusqu'à 80 mph');
        break;
      case 'elephant':
        console.log('L'éléphant court jusqu'à 40 mph');
        break;
      default:
        throw new Error(`Type d'animal non supporté : ${this.type}`);
    }
  }
}

const animal1 = new Animal('Lion', 4, 'lion');
animal1.getSpeed(); // Le lion court jusqu'à 80 mph
```

Le code ci-dessus viole le principe ouvert-fermé car si vous voulez ajouter un nouveau type d'animal, vous devez modifier le code existant en ajoutant un autre cas à l'instruction switch. 

Normalement, si vous utilisez une instruction `switch`, il est très probable que vous violiez le principe ouvert-fermé.

Voici comment j'ai refactorisé le code pour résoudre le problème : 

```js
class Animal {
  constructor(name, age, speedRate) {
    this.name = name;
    this.age = age;
    this.speedRate = speedRate;
  }

  getSpeed() {
    return this.speedRate.getSpeed();
  }
}

class SpeedRate {
  getSpeed() {}
}

class CheetahSpeedRate extends SpeedRate {
  getSpeed() {
    return 130;
  }
}

class LionSpeedRate extends SpeedRate {
  getSpeed() {
    return 80;
  }
}

class ElephantSpeedRate extends SpeedRate {
  getSpeed() {
    return 40;
  }
}

const cheetah = new Animal('Guépard', 4, new CheetahSpeedRate());
console.log(`${cheetah.name} court jusqu'à ${cheetah.getSpeed()} mph`); // Le guépard court jusqu'à 130 mph

const lion = new Animal('Lion', 5, new LionSpeedRate());
console.log(`${lion.name} court jusqu'à ${lion.getSpeed()} mph`); // Le lion court jusqu'à 80 mph

const elephant = new Animal('Éléphant', 10, new ElephantSpeedRate());
console.log(`${elephant.name} court jusqu'à ${elephant.getSpeed()} mph`); // L'éléphant court jusqu'à 40 mph
```

De cette manière, si vous voulez ajouter un nouveau type d'animal, vous pouvez créer une nouvelle classe qui étend `SpeedRate` et la passer au constructeur Animal sans modifier le code existant. 

Par exemple, j'ai ajouté une nouvelle classe `GoatSpeedRate` comme ceci :

```js
class GoatSpeedRate extends SpeedRate {
  getSpeed() {
    return 35;
  }
}

// Chèvre
const goat = new Animal('Chèvre', 5, new GoatSpeedRate());
console.log(`${goat.name} court jusqu'à ${goat.getSpeed()} mph`); // La chèvre court jusqu'à 35 mph
```

Cela respecte le principe ouvert-fermé.


### Le principe de substitution de Liskov (LSP)
Le principe de substitution de Liskov est l'un des principes les plus importants à respecter en programmation orientée objet (POO). Il a été introduit par l'informaticienne Barbara Liskov en 1987 dans un article qu'elle a co-écrit avec Jeannette Wing.

Le principe stipule que les classes enfants ou sous-classes doivent être substituables à leurs classes parent ou super classes. En d'autres termes, la classe enfant doit pouvoir remplacer la classe parent. Cela a l'avantage de vous faire savoir à quoi vous attendre de votre code.

Voici un exemple de code qui ne viole pas le principe de substitution de Liskov :

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  makeSound() {
    console.log(`${this.name} fait un son`);
  }
}

class Dog extends Animal {
  makeSound() {
    console.log(`${this.name} aboie`);
  }
}

class Cat extends Animal {
  makeSound() {
    console.log(`${this.name} miaule`);
  }
}

function makeAnimalSound(animal) {
  animal.makeSound();
}

const cheetah = new Animal('Guépard');
makeAnimalSound(cheetah); // Le guépard fait un son

const dog = new Dog('Jack');
makeAnimalSound(dog); // Jack aboie

const cat = new Cat('Khloe');
makeAnimalSound(cat); // Khloe miaule
```

Les classes `Dog` et `Cat` peuvent remplacer avec succès la classe parent `Animal`.

D'autre part, voyons comment le code ci-dessous viole le principe de substitution de Liskov :

```js
class Bird extends Animal {
  fly() {
    console.log(`${this.name} bat des ailes`);
  }
}

const parrot = new Bird('Titi le Perroquet');
makeAnimalSound(parrot); // Titi le Perroquet fait un son
parrot.fly(); // Titi le Perroquet bat des ailes
```

La classe `Bird` viole le principe de substitution de Liskov car elle n'implémente pas son propre `makeSound` à partir de la classe parent `Animal`. Au lieu de cela, elle hérite du son générique.

Pour corriger cela, vous devez la faire utiliser la méthode `makeSound` également :

```js
class Bird extends Animal {
  makeSound() {
    console.log(`${this.name} gazouille`);
  }

  fly() {
    console.log(`${this.name} bat des ailes`);
  }
}

const parrot = new Bird('Titi le Perroquet');
makeAnimalSound(parrot); // Titi le Perroquet gazouille
parrot.fly(); // Titi le Perroquet bat des ailes
```


### Le principe de ségrégation des interfaces (ISP)
Le principe de ségrégation des interfaces stipule que les clients ne doivent pas être forcés d'implémenter des interfaces ou des méthodes qu'ils n'utilisent pas. 

Plus précisément, l'ISP suggère que les développeurs de logiciels doivent décomposer les grandes interfaces en interfaces plus petites et plus spécifiques, de sorte que les clients n'aient besoin de dépendre que des interfaces qui sont pertinentes pour eux. Cela peut rendre la base de code plus facile à maintenir.

Ce principe est assez similaire au principe de responsabilité unique (SRP). Mais il ne s'agit pas seulement d'une seule interface faisant une seule chose - il s'agit de décomposer toute la base de code en plusieurs interfaces ou composants.

Pensez à cela comme à la même chose que vous faites en travaillant avec des frameworks et des bibliothèques frontend comme React, Svelte et Vue. Vous décomposez généralement la base de code en composants que vous n'intégrez que lorsque cela est nécessaire. 

Cela signifie que vous créez des composants individuels qui ont une fonctionnalité spécifique à eux. Le composant responsable de l'implémentation du défilement vers le haut, par exemple, ne sera pas celui qui bascule entre le mode clair et sombre, et ainsi de suite.

Voici un exemple de code qui viole le principe de ségrégation des interfaces :

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  eat() {
    console.log(`${this.name} est en train de manger`);
  }

  swim() {
    console.log(`${this.name} est en train de nager`);
  }

  fly() {
    console.log(`${this.name} est en train de voler`);
  }
}

class Fish extends Animal {
  fly() {
    console.error("ERREUR ! Les poissons ne peuvent pas voler");
  }
}

class Bird extends Animal {
  swim() {
    console.error("ERREUR ! Les oiseaux ne peuvent pas nager");
  }
}

const bird = new Bird('Titi le Perroquet');
bird.swim(); // ERREUR ! Les oiseaux ne peuvent pas nager

const fish = new Fish('Neo le Dauphin');
fish.fly(); // ERREUR ! Les poissons ne peuvent pas voler
```

Le code ci-dessus viole le principe de ségrégation des interfaces car la classe `Fish` n'a pas besoin de la méthode `fly`. Un poisson ne peut pas voler. Les oiseaux ne peuvent pas nager non plus, donc la classe `Bird` n'a pas besoin de la méthode `swim`.

De plus, les classes `Bird` et `Fish` étendent toutes deux la classe `Animal`, et cela viole l'ISP puisque la classe `Animal` a des méthodes dont aucune des deux classes n'a besoin. 

L'objectif est de créer des interfaces qui sont adaptées aux besoins spécifiques de chaque classe/fonctionnalité.

Voici comment j'ai corrigé le code pour le conformer au principe de ségrégation des interfaces :

```js
// Définir des interfaces pour différents types d'animaux

class Swimmer {
  constructor(name) {
    this.name = name;
  }

  swim() {
    console.log(`${this.name} est en train de nager`);
  }
}

class Flyer {
  constructor(name) {
    this.name = name;
  }

  fly() {
    console.log(`${this.name} est en train de voler`);
  }
}

// Implémenter des interfaces pour des types spécifiques d'animaux

class Bird extends Flyer {
  constructor(name) {
    super(name);
  }

  eat() {
    console.log(`${this.name} est en train de manger`);
  }
}

class Fish extends Swimmer {
  constructor(name) {
    super(name);
  }

  eat() {
    console.log(`${this.name} est en train de manger`);
  }
}

// Utilisation

const bird = new Bird('Titi le Perroquet');
bird.fly(); // Titi le Perroquet est en train de voler
bird.eat(); // Titi le Perroquet est en train de manger

console.log('\n');

const fish = new Fish('Neo le Dauphin');
fish.swim(); // Neo le Dauphin est en train de nager
fish.eat(); // Neo le Dauphin est en train de manger
``` 

Dans le code ci-dessus, nous avons une classe spécifiquement pour les animaux qui nagent et une autre pour les animaux qui volent. Les classes `Fish` et `Bird` n'étendent que des classes avec des méthodes spécifiques à leurs besoins.

### Le principe d'inversion des dépendances (DIP)
Le principe d'inversion des dépendances consiste à découpler les modules logiciels. C'est-à-dire, les rendre aussi séparés les uns des autres que possible.

Le principe stipule que les modules de haut niveau ne doivent pas dépendre des modules de bas niveau. Au lieu de cela, ils doivent tous deux dépendre des abstractions. De plus, les abstractions ne doivent pas dépendre des détails, mais les détails doivent dépendre des abstractions.

En termes plus simples, cela signifie qu'au lieu d'écrire du code qui repose sur des détails spécifiques de la manière dont le code de bas niveau fonctionne, vous devez écrire du code qui dépend d'abstractions plus générales qui peuvent être implémentées de différentes manières. 

Cela facilite la modification du code de bas niveau sans avoir à changer le code de haut niveau.

Voici un code qui viole le principe d'inversion des dépendances :

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
}

class Dog extends Animal {
  bark() {
    console.log('woof! woof!! woof!!');
  }
}

class Cat extends Animal {
  meow() {
    console.log('meooow!');
  }
}

function printAnimalNames(animals) {
  for (let i = 0; i < animals.length; i++) {
    const animal = animals[i];
    console.log(animal.name);
  }
}

const dog = new Dog('Jack');
const cat = new Cat('Zoey');

const animals = [dog, cat];

printAnimalNames(animals);
```

Le code ci-dessus viole le principe d'inversion des dépendances car la fonction `printAnimalNames` dépend des implémentations concrètes de Dog et Cat. 

Si vous vouliez ajouter un autre animal comme un singe, vous devriez modifier la fonction `printAnimalNames` pour le gérer.

Voici comment le corriger :

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  getName() {
    return this.name;
  }
}

class Dog extends Animal {
  bark() {
    console.log('woof! woof!! woof!!!');
  }
}

class Cat extends Animal {
  meow() {
    console.log('meooow!');
  }
}

function printAnimalNames(animals) {
  for (let i = 0; i < animals.length; i++) {
    const animal = animals[i];
    console.log(animal.getName());
  }
}

const dog = new Dog('Jack');
const cat = new Cat('Zoey');

const animals = [dog, cat, ape];

printAnimalNames(animals);
```

Dans le code ci-dessus, j'ai créé une méthode `getName` à l'intérieur de la classe Animal. Cela fournit une abstraction sur laquelle la fonction `printAnimalNames` peut dépendre. Maintenant, la fonction `printAnimalNames` ne dépend que de la classe `Animal`, et non des implémentations concrètes de `Dog` et `Cat`.

Si vous voulez ajouter une classe Ape, vous pouvez le faire sans modifier la fonction `printAnimalNames` :

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  getName() {
    return this.name;
  }
}

class Dog extends Animal {
  bark() {
    console.log('woof! woof!! woof!!!');
  }
}

class Cat extends Animal {
  meow() {
    console.log('meooow!');
  }
}

// Ajouter la classe Ape
class Ape extends Animal {
  meow() {
    console.log('woo! woo! woo!');
  }
}

function printAnimalNames(animals) {
  for (let i = 0; i < animals.length; i++) {
    const animal = animals[i];
    console.log(animal.getName());
  }
}

const dog = new Dog('Jack'); // Jack
const cat = new Cat('Zoey'); // Zoey

// Utiliser la classe Ape
const ape = new Ape('King Kong'); // King Kong

const animals = [dog, cat, ape];

printAnimalNames(animals);
``` 


## Conclusion
Dans cet article, vous avez appris ce que sont les principes de conception **SOLID**. Nous avons discuté de chaque principe avec un exemple, et nous avons passé en revue les moyens de les implémenter en JavaScript.

J'espère que l'article vous donne une solide compréhension des principes **SOLID**. Vous pouvez voir que les principes de conception SOLID peuvent vous aider à créer un système logiciel exempt de bugs, maintenable, flexible, évolutif et réutilisable.

Merci d'avoir lu.