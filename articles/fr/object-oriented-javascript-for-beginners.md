---
title: Programmation Orientée Objet en JavaScript pour Débutants
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-05-09T20:36:30.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-javascript-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-lukas-317377.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Programmation Orientée Objet en JavaScript pour Débutants
seo_desc: 'Hi everyone! In this article we''re going to review the main characteristics
  of object oriented programming (OOP) with practical JavaScript examples.

  We will talk about OOP main concepts, why and when it can be useful, and I''ll give
  you plenty of exam...'
---

Bonjour à tous ! Dans cet article, nous allons passer en revue les principales caractéristiques de la programmation orientée objet (POO) avec des exemples pratiques en JavaScript.

Nous parlerons des concepts clés de la POO, de son utilité et de son application, et je vous fournirai de nombreux exemples en utilisant du code JS.

Si vous n'êtes pas familier avec les paradigmes de programmation, je vous recommande de consulter [la brève introduction que j'ai récemment écrite](https://www.freecodecamp.org/news/an-introduction-to-programming-paradigms/) avant de plonger dans celui-ci.

C'est parti !

![Image](https://www.freecodecamp.org/news/content/images/2022/04/160cf1a4201c53b015bfcccb9398e9ab.gif align="left")

## Table des Matières

* [Introduction à la Programmation Orientée Objet](#heading-introduction-a-la-programmation-orientee-objet)
    
* [Comment Créer des Objets – Classes](#heading-comment-creer-des-objets-classes)
    
    * [Quelques points à garder à l'esprit concernant les classes](#heading-quelques-points-a-garder-a-lesprit-concernant-les-classes)
        
* [Les quatre principes de la POO](#heading-les-quatre-principes-de-la-poo)
    
    * [Héritage](#heading-heritage)
        
        * [Quelques points à garder à l'esprit concernant l'héritage](#heading-quelques-points-a-garder-a-lesprit-concernant-lheritage)
            
    * [Encapsulation](#heading-encapsulation)
        
    * [Abstraction](#heading-abstraction)
        
    * [Polymorphisme](#heading-polymorphisme)
        
* [Composition d'Objets](#heading-composition-dobjets)
    
* [Conclusion](#heading-conclusion)
    

# Introduction à la Programmation Orientée Objet

Comme mentionné dans [mon article précédent sur les paradigmes de programmation](https://www.freecodecamp.org/news/an-introduction-to-programming-paradigms/), le concept central de la POO est de **séparer les préoccupations et les responsabilités** en **entités**. 

Les entités sont codées sous forme d'**objets**, et chaque entité regroupera un ensemble donné d'informations (**propriétés**) et d'actions (**méthodes**) qui peuvent être effectuées par l'entité.

La POO est très utile pour les grands projets, car elle facilite la modularité et l'organisation du code.

En implémentant l'abstraction des entités, nous sommes capables de penser au programme de manière similaire à la façon dont notre monde fonctionne, avec différents acteurs qui effectuent certaines actions et interagissent les uns avec les autres.

Pour mieux comprendre comment nous pouvons implémenter la POO, nous allons utiliser un exemple pratique dans lequel nous allons coder un petit jeu vidéo. Nous allons nous concentrer sur la création de personnages et voir comment la POO peut nous aider avec cela. 👽 👾 🤖

# Comment Créer des Objets – Classes

Donc, tout jeu vidéo a besoin de personnages, n'est-ce pas ? Et tous les personnages ont certaines **caractéristiques** (propriétés) comme la couleur, la taille, le nom, et ainsi de suite, et des **capacités** (méthodes) comme sauter, courir, frapper, etc. Les objets sont la structure de données parfaite à utiliser pour stocker ce type d'informations. 👍

Disons que nous avons 3 espèces de personnages différentes disponibles, et que nous voulons créer 6 personnages différents, 2 de chaque espèce.

Une façon de créer nos personnages pourrait être de simplement créer les objets manuellement en utilisant [des littéraux d'objets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer), de cette manière :

```javascript
const alien1 = {
    name: "Ali",
    species: "alien",
    phrase: () => console.log("Je suis Ali l'alien !"),
    fly: () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}
const alien2 = {
    name: "Lien",
    species: "alien",
    sayPhrase: () => console.log("Courez pour sauver vos vies !"),
    fly: () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}
const bug1 = {
    name: "Buggy",
    species: "bug",
    sayPhrase: () => console.log("Votre débogueur ne fonctionne pas avec moi !"),
    hide: () => console.log("Vous ne pouvez pas m'attraper maintenant !")
}
const bug2 = {
    name: "Erik",
    species: "bug",
    sayPhrase: () => console.log("Je bois du déca !"),
    hide: () => console.log("Vous ne pouvez pas m'attraper maintenant !")
}
const Robot1 = {
    name: "Tito",
    species: "robot",
    sayPhrase: () => console.log("Je peux cuisiner, nager et danser !"),
    transform: () => console.log("Optimus prime !")
}
const Robot2 = {
    name: "Terminator",
    species: "robot",
    sayPhrase: () => console.log("Hasta la vista, baby !"),
    transform: () => console.log("Optimus prime !")
}
```

Voyez que tous les personnages ont les propriétés `name` et `species` ainsi que la méthode `sayPhrase`. De plus, chaque espèce a une méthode qui lui est propre (par exemple, les aliens ont la méthode `fly`).

Comme vous pouvez le voir, certaines données sont partagées par tous les personnages, certaines données sont partagées par chaque espèce, et certaines données sont uniques à chaque personnage individuel.

Cette approche fonctionne. Voyez que nous pouvons parfaitement accéder aux propriétés et méthodes comme ceci :

```javascript
console.log(alien1.name) // sortie : "Ali"
console.log(bug2.species) // sortie : "bug"
Robot1.sayPhrase() // sortie : "Je peux cuisiner, nager et danser !"
Robot2.transform() // sortie : "Optimus prime !"
```

Le problème avec cette approche est qu'elle ne s'adapte pas bien du tout et qu'elle est sujette aux erreurs. Imaginez que notre jeu pourrait avoir des centaines de personnages. Nous devrions définir manuellement les propriétés et méthodes pour chacun d'eux !

Pour résoudre ce problème, nous avons besoin d'un moyen programmatique de créer des objets et de définir différentes propriétés et méthodes selon un ensemble de conditions. Et c'est là que les **classes** excellent. 😉

Les classes définissent un modèle pour créer des objets avec des propriétés et méthodes prédéfinies. En créant une classe, vous pouvez ensuite **instancier** (créer) des objets à partir de cette classe, qui hériteront de toutes les propriétés et méthodes que la classe possède.

En refactorisant notre code précédent, nous pouvons créer une classe pour chacune de nos espèces de personnages, comme ceci :

```javascript
class Alien { // Nom de la classe
    // La méthode constructeur prendra un certain nombre de paramètres et assignera ces paramètres comme propriétés à l'objet créé.
    constructor (name, phrase) {
        this.name = name
        this.phrase = phrase
        this.species = "alien"
    }
    // Ce seront les méthodes de l'objet.
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
    sayPhrase = () => console.log(this.phrase)
}

class Bug {
    constructor (name, phrase) {
        this.name = name
        this.phrase = phrase
        this.species = "bug"
    }
    hide = () => console.log("Vous ne pouvez pas m'attraper maintenant !")
    sayPhrase = () => console.log(this.phrase)
}

class Robot {
    constructor (name, phrase) {
        this.name = name
        this.phrase = phrase
        this.species = "robot"
    }
    transform = () => console.log("Optimus prime !")
    sayPhrase = () => console.log(this.phrase)
}
```

Et ensuite nous pouvons instancier nos personnages à partir de ces classes comme ceci :

```javascript
const alien1 = new Alien("Ali", "Je suis Ali l'alien !")
// Nous utilisons le mot-clé "new" suivi du nom de la classe correspondante
// et lui passons les paramètres correspondants selon ce qui a été déclaré dans la fonction constructeur de la classe

const alien2 = new Alien("Lien", "Courez pour sauver vos vies !")
const bug1 = new Bug("Buggy", "Votre débogueur ne fonctionne pas avec moi !")
const bug2 = new Bug("Erik", "Je bois du déca !")
const Robot1 = new Robot("Tito", "Je peux cuisiner, nager et danser !")
const Robot2 = new Robot("Terminator", "Hasta la vista, baby !")
```

Ensuite, nous pouvons accéder aux propriétés et méthodes de chaque objet comme ceci :

```javascript
console.log(alien1.name) // sortie : "Ali"
console.log(bug2.species) // sortie : "bug"
Robot1.sayPhrase() // sortie : "Je peux cuisiner, nager et danser !"
Robot2.transform() // sortie : "Optimus prime !"
```

Ce qui est bien avec cette approche et l'utilisation des classes en général, c'est que nous pouvons utiliser ces "modèles" pour créer de nouveaux objets plus rapidement et plus sûrement que si nous le faisions "manuellement".

De plus, notre code est mieux organisé car nous pouvons clairement identifier où les propriétés et méthodes de chaque objet sont définies (dans la classe). Et cela rend les changements ou adaptations futurs beaucoup plus faciles à implémenter.

### Quelques points à garder à l'esprit concernant les classes :

Suivant [cette définition](https://www.bookstack.cn/read/You-Dont-Know-JS-Get-Started-2nd/spilt.6.833b11649d196dea.md?wd=JS), mise en termes plus formels,

> *"une classe dans un programme est une définition d'un "type" de structure de données personnalisée qui inclut à la fois des données et des comportements qui opèrent sur ces données. Les classes définissent comment une telle structure de données fonctionne, mais les classes ne sont pas elles-mêmes des valeurs concrètes. Pour obtenir une valeur concrète que vous pouvez utiliser dans le programme, une classe doit être instanciée (avec le mot-clé "new") une ou plusieurs fois."*

* Rappelez-vous que les classes ne sont pas des entités ou objets réels. Les classes sont les modèles ou moules que nous allons utiliser pour créer les objets réels.
    
* Les noms de classes sont déclarés avec une majuscule initiale et en camelCase par convention. Le mot-clé class crée une constante, donc il ne peut pas être redéfini par la suite.
    
* Les classes doivent toujours avoir une méthode constructeur qui sera ensuite utilisée pour instancier cette classe. Un constructeur en JavaScript est simplement une fonction qui retourne un objet. La seule chose spéciale à son sujet est que, lorsqu'il est invoqué avec le mot-clé "new", il assigne son prototype comme le prototype de l'objet retourné.
    
* Le mot-clé "this" pointe vers la classe elle-même et est utilisé pour définir les propriétés de la classe au sein de la méthode constructeur.
    
* Les méthodes peuvent être ajoutées en définissant simplement le nom de la fonction et son code d'exécution.
    
* JavaScript est un langage basé sur les prototypes, et au sein de JavaScript, les classes sont utilisées uniquement comme du sucre syntaxique. Cela ne fait pas une énorme différence ici, mais c'est bon à savoir et à garder à l'esprit. Vous pouvez lire [cet article si vous souhaitez en savoir plus sur ce sujet](https://www.freecodecamp.org/news/prototypes-and-inheritance-in-javascript/).
    

# Les Quatre Principes de la POO

La POO est normalement expliquée avec 4 principes clés qui dictent comment les programmes POO fonctionnent. Ce sont **l'héritage, l'encapsulation, l'abstraction et le polymorphisme**. Passons en revue chacun d'eux.

## Héritage

L'héritage est la capacité à **créer des classes basées sur d'autres classes**. Avec l'héritage, nous pouvons définir une **classe parente** (avec certaines propriétés et méthodes), puis des **classes enfants** qui hériteront de la classe parente toutes les propriétés et méthodes qu'elle possède.

Voyons cela avec un exemple. Imaginez que tous les personnages que nous avons définis précédemment seront les ennemis de notre personnage principal. Et en tant qu'ennemis, ils auront tous la propriété "power" et la méthode "attack".

Une façon d'implémenter cela serait simplement d'ajouter les mêmes propriétés et méthodes à toutes les classes que nous avions, comme ceci :

```javascript
...

class Bug {
    constructor (name, phrase, power) {
        this.name = name
        this.phrase = phrase
        this.power = power
        this.species = "bug"
    }
    hide = () => console.log("Vous ne pouvez pas m'attraper maintenant !")
    sayPhrase = () => console.log(this.phrase)
    attack = () => console.log(`J'attaque avec une puissance de ${this.power} !`)
}

class Robot {
    constructor (name, phrase, power) {
        this.name = name
        this.phrase = phrase
        this.power = power
        this.species = "robot"
    }
    transform = () => console.log("Optimus prime !")
    sayPhrase = () => console.log(this.phrase)
    attack = () => console.log(`J'attaque avec une puissance de ${this.power} !`)
}

const bug1 = new Bug("Buggy", "Votre débogueur ne fonctionne pas avec moi !", 10)
const Robot1 = new Robot("Tito", "Je peux cuisiner, nager et danser !", 15)

console.log(bug1.power) // sortie : 10
Robot1.attack() // sortie : "J'attaque avec une puissance de 15 !"
```

Mais vous pouvez voir que nous répétons du code, et ce n'est pas optimal. Une meilleure façon serait de déclarer une classe parente "Enemy" qui est ensuite étendue par toutes les espèces ennemies, comme ceci :

```javascript
class Enemy {
    constructor(power) {
        this.power = power
    }

    attack = () => console.log(`J'attaque avec une puissance de ${this.power} !`)
}


class Alien extends Enemy {
    constructor (name, phrase, power) {
        super(power)
        this.name = name
        this.phrase = phrase
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
    sayPhrase = () => console.log(this.phrase)
}

...
```

Voyez que la classe ennemi ressemble à n'importe quelle autre. Nous utilisons la méthode constructeur pour recevoir des paramètres et les assigner comme propriétés, et les méthodes sont déclarées comme des fonctions simples.

Dans la classe enfant, nous utilisons le mot-clé `extends` pour déclarer la classe parente dont nous voulons hériter. Ensuite, dans la méthode constructeur, nous devons déclarer le paramètre "power" et utiliser la fonction `super` pour indiquer que la propriété est déclarée dans la classe parente.

Lorsque nous instancions de nouveaux objets, nous passons simplement les paramètres comme ils ont été déclarés dans la fonction constructeur correspondante et *voilà !* Nous pouvons maintenant accéder aux propriétés et méthodes déclarées dans la classe parente. 😎

```javascript
const alien1 = new Alien("Ali", "Je suis Ali l'alien !", 10)
const alien2 = new Alien("Lien", "Courez pour sauver vos vies !", 15)

alien1.attack() // sortie : J'attaque avec une puissance de 10 !
console.log(alien2.power) // sortie : 15
```

Maintenant, disons que nous voulons ajouter une nouvelle classe parente qui regroupe tous nos personnages (peu importe s'ils sont ennemis ou non), et que nous voulons définir une propriété de "speed" et une méthode "move". Nous pouvons faire cela comme ceci :

```javascript
class Character {
    constructor (speed) {
        this.speed = speed
    }

    move = () => console.log(`Je me déplace à la vitesse de ${this.speed} !`)
}

class Enemy extends Character {
    constructor(power, speed) {
        super(speed)
        this.power = power
    }

    attack = () => console.log(`J'attaque avec une puissance de ${this.power} !`)
}


class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        super(power, speed)
        this.name = name
        this.phrase = phrase
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
    sayPhrase = () => console.log(this.phrase)
}
```

Tout d'abord, nous déclarons la nouvelle classe parente "Character". Ensuite, nous l'étendons dans la classe Enemy. Et enfin, nous ajoutons le nouveau paramètre "speed" aux fonctions `constructor` et `super` dans notre classe Alien.

Nous instancions en passant les paramètres comme toujours, et *voilà* à nouveau, nous pouvons accéder aux propriétés et méthodes de la classe "grand-parent". 👴

```javascript
const alien1 = new Alien("Ali", "Je suis Ali l'alien !", 10, 50)
const alien2 = new Alien("Lien", "Courez pour sauver vos vies !", 15, 60)

alien1.move() // sortie : "Je me déplace à la vitesse de 50 !"
console.log(alien2.speed) // sortie : 60
```

Maintenant que nous en savons plus sur l'héritage, refactorisons notre code pour éviter autant que possible la répétition de code :

```javascript
class Character {
    constructor (speed) {
        this.speed = speed
    }
    move = () => console.log(`Je me déplace à la vitesse de ${this.speed} !`)
}

class Enemy extends Character {
    constructor(name, phrase, power, speed) {
        super(speed)
        this.name = name
        this.phrase = phrase
        this.power = power
    }
    sayPhrase = () => console.log(this.phrase)
    attack = () => console.log(`J'attaque avec une puissance de ${this.power} !`)
}


class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}

class Bug extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "bug"
    }
    hide = () => console.log("Vous ne pouvez pas m'attraper maintenant !")
}

class Robot extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "robot"
    }
    transform = () => console.log("Optimus prime !")
}


const alien1 = new Alien("Ali", "Je suis Ali l'alien !", 10, 50)
const alien2 = new Alien("Lien", "Courez pour sauver vos vies !", 15, 60)
const bug1 = new Bug("Buggy", "Votre débogueur ne fonctionne pas avec moi !", 25, 100)
const bug2 = new Bug("Erik", "Je bois du déca !", 5, 120)
const Robot1 = new Robot("Tito", "Je peux cuisiner, nager et danser !", 125, 30)
const Robot2 = new Robot("Terminator", "Hasta la vista, baby !", 155, 40)
```

Voyez que nos classes d'espèces sont beaucoup plus petites maintenant, grâce au fait que nous avons déplacé toutes les propriétés et méthodes partagées vers une classe parente commune. C'est le genre d'efficacité que l'héritage peut nous aider à atteindre. 😉

### Quelques points à garder à l'esprit concernant l'héritage :

* Une classe ne peut avoir qu'une seule classe parente dont hériter. Vous ne pouvez pas étendre plusieurs classes, bien qu'il existe des astuces et des moyens de contourner cela.
    
* Vous pouvez étendre la chaîne d'héritage autant que vous le souhaitez, en définissant des classes parent, grand-parent, arrière-grand-parent et ainsi de suite.
    
* Si une classe enfant hérite de propriétés d'une classe parente, elle doit d'abord assigner les propriétés parent en appelant la fonction `super()` avant d'assigner ses propres propriétés.
    

Un exemple :

```javascript
// Cela fonctionne :
class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}

// Cela génère une erreur :
class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        this.species = "alien" // ReferenceError: Must call super constructor in derived class before accessing 'this' or returning from derived constructor
        super(name, phrase, power, speed)
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}
```

* Lors de l'héritage, toutes les méthodes et propriétés parent seront héritées par les enfants. Nous ne pouvons pas décider quoi hériter d'une classe parente (de la même manière que nous ne pouvons pas choisir quelles vertus et défauts nous héritons de nos parents. 😅 Nous reviendrons sur ce point lorsque nous parlerons de composition).
    
* Les classes enfants peuvent remplacer les propriétés et méthodes du parent.
    

Pour donner un exemple, dans notre code précédent, la classe Alien étend la classe Enemy et hérite de la méthode `attack` qui logue `J'attaque avec une puissance de ${this.power} !` :

```javascript
class Enemy extends Character {
    constructor(name, phrase, power, speed) {
        super(speed)
        this.name = name
        this.phrase = phrase
        this.power = power
    }
    sayPhrase = () => console.log(this.phrase)
    attack = () => console.log(`J'attaque avec une puissance de ${this.power} !`)
}


class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}

const alien1 = new Alien("Ali", "Je suis Ali l'alien !", 10, 50)
alien1.attack() // sortie : J'attaque avec une puissance de 10 !
```

Disons que nous voulons que la méthode `attack` fasse une chose différente dans notre classe Alien. Nous pouvons la remplacer en la déclarant à nouveau, comme ceci :

```javascript
class Enemy extends Character {
    constructor(name, phrase, power, speed) {
        super(speed)
        this.name = name
        this.phrase = phrase
        this.power = power
    }
    sayPhrase = () => console.log(this.phrase)
    attack = () => console.log(`J'attaque avec une puissance de ${this.power} !`)
}


class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
    attack = () => console.log("Maintenant je fais une chose différente, HA !") // Remplace la méthode parente.
}

const alien1 = new Alien("Ali", "Je suis Ali l'alien !", 10, 50)
alien1.attack() // sortie : "Maintenant je fais une chose différente, HA !"
```

## Encapsulation

L'encapsulation est un autre concept clé en POO, et il représente la capacité d'un objet à "décider" quelles informations il expose à "l'extérieur" et quelles informations il ne révèle pas. L'encapsulation est mise en œuvre par le biais de **propriétés et méthodes publiques et privées**. 

En JavaScript, toutes les propriétés et méthodes des objets sont publiques par défaut. "Publique" signifie simplement que nous pouvons accéder à une propriété/méthode d'un objet depuis l'extérieur de son propre corps :

```javascript
// Voici notre classe
class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}

// Voici notre objet
const alien1 = new Alien("Ali", "Je suis Ali l'alien !", 10, 50)

// Ici nous accédons à nos propriétés et méthodes publiques
console.log(alien1.name) // sortie : Ali
alien1.sayPhrase() // sortie : "Je suis Ali l'alien !"
```

Pour rendre cela plus clair, voyons à quoi ressemblent les propriétés et méthodes privées.

Disons que nous voulons que notre classe Alien ait une propriété `birthYear`, et utiliser cette propriété pour exécuter une méthode `howOld`, mais nous ne voulons pas que cette propriété soit accessible depuis ailleurs que l'objet lui-même. Nous pourrions l'implémenter comme ceci :

```javascript
class Alien extends Enemy {
    #birthYear // Nous devons d'abord déclarer la propriété privée, en utilisant toujours le symbole '#' au début de son nom.

    constructor (name, phrase, power, speed, birthYear) {
        super(name, phrase, power, speed)
        this.species = "alien"
        this.#birthYear = birthYear // Ensuite, nous assignons sa valeur dans la fonction constructeur
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
    howOld = () => console.log(`Je suis né en ${this.#birthYear}`) // et l'utiliser dans la méthode correspondante.
}
    
// Nous instancions de la même manière que d'habitude
const alien1 = new Alien("Ali", "Je suis Ali l'alien !", 10, 50, 10000)
```

Ensuite, nous pouvons accéder à la méthode `howOld`, comme ceci :

```javascript
alien1.howOld() // sortie : "Je suis né en 10000"
```

Mais si nous essayons d'accéder directement à la propriété, nous obtiendrons une erreur. Et la propriété privée n'apparaîtra pas si nous loggons l'objet.

```javascript
console.log(alien1.#birthYear) // Cela génère une erreur
console.log(alien1) 
// sortie :
// Alien {
//     move: [Function: move],
//     speed: 50,
//     sayPhrase: [Function: sayPhrase],
//     attack: [Function: attack],
//     name: 'Ali',
//     phrase: "Je suis Ali l'alien !",
//     power: 10,
//     fly: [Function: fly],
//     howOld: [Function: howOld],
//     species: 'alien'
//   }
```

L'encapsulation est utile dans les cas où nous avons besoin de certaines propriétés ou méthodes pour le fonctionnement interne de l'objet, mais où nous ne voulons pas exposer cela à l'extérieur. Avoir des propriétés/méthodes privées garantit que nous ne "révélons pas accidentellement" des informations que nous ne voulons pas.

## Abstraction

L'abstraction est un principe qui stipule qu'une classe ne doit représenter que les informations pertinentes pour le contexte du problème. En termes simples, n'exposez à l'extérieur que les propriétés et méthodes que vous allez utiliser. Si ce n'est pas nécessaire, ne l'exposez pas.

Ce principe est étroitement lié à l'encapsulation, car nous pouvons utiliser des propriétés/méthodes publiques et privées pour décider ce qui est exposé et ce qui ne l'est pas.

## Polymorphisme

Ensuite, il y a le polymorphisme (ça sonne vraiment sophistiqué, n'est-ce pas ? Les noms de la POO sont les plus cool... 🤓). Le polymorphisme signifie "plusieurs formes" et est en fait un concept simple. C'est la capacité d'une méthode à retourner différentes valeurs selon certaines conditions.

Par exemple, nous avons vu que la classe Enemy a la méthode `sayPhrase`. Et toutes nos classes d'espèces héritent de la classe Enemy, ce qui signifie qu'elles ont toutes la méthode `sayPhrase` également.

Mais nous pouvons voir que lorsque nous appelons la méthode sur différentes espèces, nous obtenons des résultats différents :

```javascript
const alien2 = new Alien("Lien", "Courez pour sauver vos vies !", 15, 60)
const bug1 = new Bug("Buggy", "Votre débogueur ne fonctionne pas avec moi !", 25, 100)

alien2.sayPhrase() // sortie : "Courez pour sauver vos vies !"
bug1.sayPhrase() // sortie : "Votre débogueur ne fonctionne pas avec moi !"
```

Et c'est parce que nous avons passé à chaque classe un paramètre différent lors de l'instanciation. C'est un type de polymorphisme, **basé sur les paramètres**. 👍

Un autre type de polymorphisme est **basé sur l'héritage**, et cela fait référence au fait que nous avons une classe parente qui définit une méthode et que l'enfant remplace cette méthode pour la modifier d'une certaine manière. L'exemple que nous avons vu précédemment s'applique parfaitement ici également :

```javascript
class Enemy extends Character {
    constructor(name, phrase, power, speed) {
        super(speed)
        this.name = name
        this.phrase = phrase
        this.power = power
    }
    sayPhrase = () => console.log(this.phrase)
    attack = () => console.log(`J'attaque avec une puissance de ${this.power} !`)
}


class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
    attack = () => console.log("Maintenant je fais une chose différente, HA !") // Remplace la méthode parente.
}

const alien1 = new Alien("Ali", "Je suis Ali l'alien !", 10, 50)
alien1.attack() // sortie : "Maintenant je fais une chose différente, HA !"
```

Cette implémentation est polymorphe car si nous commentions la méthode `attack` dans la classe Alien, nous pourrions toujours l'appeler sur l'objet :

```javascript
alien1.attack() // sortie : "J'attaque avec une puissance de 10 !"
```

Nous avons obtenu la même méthode qui peut faire une chose ou une autre en fonction de si elle a été remplacée ou non. Polymorphe. 👍👍

# Composition d'Objets

La [composition d'objets](https://en.wikipedia.org/wiki/Composition_over_inheritance) est une technique qui fonctionne comme une alternative à l'héritage.

Lorsque nous avons parlé d'héritage, nous avons mentionné que les classes enfants héritent toujours de toutes les méthodes et propriétés parent. Eh bien, en utilisant la composition, nous pouvons assigner des propriétés et méthodes aux objets de manière plus flexible que ce que l'héritage permet, de sorte que les objets n'obtiennent que ce dont ils ont besoin et rien d'autre.

Nous pouvons implémenter cela assez simplement, en utilisant des fonctions qui reçoivent l'objet comme paramètre et lui assignent la propriété/méthode souhaitée. Voyons cela dans un exemple.

Disons maintenant que nous voulons ajouter la capacité de voler à nos personnages insectes. Comme nous l'avons vu dans notre code, seuls les aliens ont la méthode `fly`. Donc une option pourrait être de dupliquer exactement la même méthode dans la classe `Bug` :

```javascript
class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}

class Bug extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "bug"
    }
    hide = () => console.log("Vous ne pouvez pas m'attraper maintenant !")
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!") // Nous dupliquons du code =(
}
```

Une autre option serait de déplacer la méthode `fly` vers la classe `Enemy`, afin qu'elle puisse être héritée à la fois par les classes `Alien` et `Bug`. Mais cela rend également la méthode disponible pour les classes qui n'en ont pas besoin, comme `Robot`.

```javascript
class Enemy extends Character {
    constructor(name, phrase, power, speed) {
        super(speed)
        this.name = name
        this.phrase = phrase
        this.power = power
    }
    sayPhrase = () => console.log(this.phrase)
    attack = () => console.log(`J'attaque avec une puissance de ${this.power} !`)
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
}


class Alien extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "alien"
    }
}

class Bug extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "bug"
    }
    hide = () => console.log("Vous ne pouvez pas m'attraper maintenant !")
}

class Robot extends Enemy {
    constructor (name, phrase, power, speed) {
        super(name, phrase, power, speed)
        this.species = "robot"
    }
    transform = () => console.log("Optimus prime !")
	// Je n'ai pas besoin de la méthode fly =(
}
```

Comme vous pouvez le voir, l'héritage pose des problèmes lorsque le plan initial que nous avions pour nos classes change (ce qui, dans le monde réel, est pratiquement toujours le cas). La composition d'objets propose une approche dans laquelle les objets obtiennent des propriétés et méthodes assignées uniquement selon leurs besoins.

Dans notre exemple, nous pourrions créer une fonction et sa seule responsabilité serait d'ajouter la méthode de vol à tout objet qu'elle reçoit comme paramètre :

```javascript
const bug1 = new Bug("Buggy", "Votre débogueur ne fonctionne pas avec moi !", 25, 100)

const addFlyingAbility = obj => {
    obj.fly = () => console.log(`Maintenant ${obj.name} peut voler !`)
}

addFlyingAbility(bug1)
bug1.fly() // sortie : "Maintenant Buggy peut voler !"
```

Et nous pourrions avoir des fonctions très similaires pour chaque pouvoir ou capacité que nous voulons que nos monstres aient.

Comme vous pouvez sûrement le voir, cette approche est beaucoup plus flexible que d'avoir des classes parent avec des propriétés et méthodes fixes à hériter. Chaque fois qu'un objet a besoin d'une méthode, nous appelons simplement la fonction correspondante et c'est tout. 👍

Voici [une belle vidéo qui compare l'héritage avec la composition](https://www.youtube.com/watch?v=wfMtDGfHWpA&t=3s).

# Conclusion

La POO est un paradigme de programmation très puissant qui peut nous aider à aborder de grands projets en créant l'abstraction d'entités. Chaque entité sera responsable de certaines informations et actions, et les entités pourront également interagir les unes avec les autres, tout comme le monde réel fonctionne.

Dans cet article, nous avons appris les classes, l'héritage, l'encapsulation, l'abstraction, le polymorphisme et la composition. Ce sont tous des concepts clés dans le monde de la POO. Et nous avons également vu divers exemples de la manière dont la POO peut être implémentée en JavaScript.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman).

Santé et à la prochaine ! ✉️

![Image](https://www.freecodecamp.org/news/content/images/2022/04/98OvjJ.gif align="left")