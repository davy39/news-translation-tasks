---
title: Programmation Orientée Objet en JavaScript
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2023-02-09T02:04:37.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Frame-389.png
tags:
- name: JavaScript
  slug: javascript
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Programmation Orientée Objet en JavaScript
seo_desc: 'Object-Oriented Programming is a programming style based on classes and
  objects. These group data (properties) and methods (actions) inside a box.

  OOP was developed to make code more flexible and easier to maintain.

  JavaScript is prototype-based proc...'
---

La Programmation Orientée Objet est un style de programmation basé sur les classes et les objets. Ceux-ci regroupent les données (propriétés) et les méthodes (actions) dans une boîte.

L'OOP a été développé pour rendre le code plus flexible et plus facile à maintenir.

JavaScript est un langage procédural basé sur les prototypes, ce qui signifie qu'il supporte à la fois la programmation fonctionnelle et orientée objet.

# Que sont les Classes et les Objets en JavaScript ?

## Qu'est-ce qu'une Classe ?

Vous pouvez penser à une classe comme à un plan de construction d'une maison. Une classe n'est pas un objet du monde réel, mais nous pouvons créer des objets à partir d'une classe. C'est comme un modèle pour un objet.

Nous pouvons créer des classes en utilisant le mot-clé `class` qui est un mot-clé réservé en JavaScript. Les classes peuvent avoir leurs propres propriétés et méthodes. Nous étudierons comment créer une classe en détail sous peu. Ceci n'est qu'un aperçu de haut niveau d'une classe.

Prenons un exemple. Ci-dessous se trouve un plan de construction pour une maison (comme une classe).

![Image](https://www.freecodecamp.org/news/content/images/2023/02/blueprint.jpg align="left")

*Plan de construction d'une maison (Classe)*

## Qu'est-ce qu'un Objet ?

Un objet est une instance d'une classe. Maintenant, avec l'aide de la classe maison, nous pouvons construire une maison. Nous pouvons construire plusieurs maisons avec l'aide de la même classe maison.

### Exemple de Classes et Objets en Action

Prenons un exemple simple pour comprendre comment fonctionnent les classes et les objets.

L'exemple ci-dessous n'a rien à voir avec la syntaxe JavaScript. Il s'agit simplement d'expliquer les classes et les objets. Nous étudierons la syntaxe de l'OOP en JavaScript un peu plus tard.

Considérons une classe Étudiant. Un étudiant peut avoir des propriétés comme nom, âge, niveau, et ainsi de suite, et des fonctions comme étudier, jouer, et faire les devoirs.

```javascript
class Student{
 // Données (Propriétés)
 Name
 Age
 Standard
    
 // Méthodes (Action)
 study(){
 // Étudier
 }
    
 Play(){
 // Jouer
 }
    
 doHomeWork(){
 // Faire les devoirs
 }
    
}
```

Avec l'aide de la classe ci-dessus, nous pouvons avoir plusieurs étudiants ou instances.

**Voici les infos pour** `**Student - 01**`**:**

```javascript
// Étudiant 1
{
Name = "John"
Age = 15
Standard = 9
    
study(){
 // Étudier
 }
    
 Play(){
 // Jouer
 }
    
 doHomeWork(){
 // Faire les devoirs
 }
    
}
```

**Voici les infos pour** `**Student - 02**`**:**

```javascript
// Étudiant 2
{
Name = "Gorge"
Age = 18
Standard = 12
    
study(){
 // Étudier
 }
    
 Play(){
 // Jouer
 }
    
 doHomeWork(){
 // Faire les devoirs
 }
    
}
```

# Comment Concevoir une Classe en Réalité ?

Il n'y a pas de réponse parfaite à cette question. Mais nous pouvons obtenir de l'aide de certains principes OOP lors de la conception de nos classes.

Il y a 4 principes principaux en OOP, et ils sont :

* Abstraction
    
* Encapsulation
    
* Héritage
    
* Polymorphisme
    

Nous allons approfondir ces concepts en JavaScript ci-dessous. Mais d'abord, obtenons un aperçu de haut niveau de ces concepts pour mieux les comprendre.

## Que Signifie l'Abstraction en OOP ?

L'abstraction signifie cacher certains détails qui n'ont pas d'importance pour l'utilisateur et ne montrer que les fonctionnalités ou fonctions essentielles.

Par exemple, prenons un téléphone portable. Nous ne montrons pas de détails comme `verifyTemperature()`, `verifyVolt()`, `frontCamOn()`, `frontCamOff()` et ainsi de suite. Au lieu de cela, nous fournissons des fonctionnalités essentielles qui importent à l'utilisateur comme camera(), volumeBtn(), et autres.

## Que Signifie l'Encapsulation en OOP ?

L'encapsulation signifie garder les propriétés et méthodes privées à l'intérieur d'une classe, de sorte qu'elles ne soient pas accessibles depuis l'extérieur de cette classe.

Cela empêchera le code qui est à l'extérieur de la classe de manipuler accidentellement les méthodes et propriétés internes.

## Que Signifie l'Héritage en OOP ?

L'héritage rend toutes les propriétés et méthodes disponibles pour une classe enfant. Cela nous permet de réutiliser la logique commune et de modéliser des relations du monde réel. Nous discuterons de l'héritage dans une section ultérieure de cet article avec un exemple pratique.

## Que Signifie le Polymorphisme en OOP ?

Le polymorphisme signifie avoir différentes formes et multiples. Nous pouvons écraser une méthode héritée d'une classe parente.

```javascript
// Ce n'est pas la syntaxe réelle de JavaScript
class User{
email 
password

login(providedPassword){
	// Connexion de l'utilisateur
}
    
checkMessage(){
// Vérifier tout nouveau message
}
}
```

```javascript
// Ce n'est pas la syntaxe réelle de JavaScript
class Admin inherit user{
email // Propriété héritée
password // Propriété héritée
permissions // Propriété propre

// Méthode héritée
login(providedPassword){
	// Connexion différente de l'utilisateur
}

// Méthode héritée
checkMessage(){
// Vérifier tout nouveau message
}

// Méthode propre
chechStats(){
// Vérifier les statistiques
}
}
```

La méthode Login dans Admin est différente de la classe héritée `user`.

# Programmation Orientée Objet en JavaScript

Nous avons maintenant discuté des bases de l'OOP. Mais l'OOP en JavaScript est un peu différent. Nous avons un objet lié à un prototype. Les prototypes contiennent toutes les méthodes et ces méthodes sont accessibles à tous les objets liés à ce prototype. Cela s'appelle **l'Héritage Prototypal** (ou **Délégation Prototypale**).

## Qu'est-ce que l'Héritage Prototypal en JavaScript ?

Vous avez probablement déjà utilisé l'Héritage Prototypal sans le savoir – par exemple, si vous avez utilisé des méthodes sur des tableaux comme push(), pop(), map() et ainsi de suite (qui sont disponibles sur tous les tableaux).

Si nous allons à la [documentation officielle](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map), nous verrons Array.prototype.map() car Array.prototype est un prototype de tous les objets de tableau que nous créons en JavaScript. C'est un exemple d'héritage prototypal que nous allons apprendre à implémenter.

Tout comme Array.prototype, nous allons créer nos propres prototypes et cela vous aidera à comprendre JavaScript de fond en comble.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ss.png align="left")

*Prototype d'un tableau*

## Comment Implémenter l'Héritage Prototypal en JavaScript

Il y a trois principales façons d'implémenter l'Héritage Prototypal en JavaScript :

### Utilisation des Fonctions Constructeurs

Nous pouvons créer des objets à partir d'une fonction. Avec l'aide d'une fonction constructeur, les objets intégrés comme les tableaux, les ensembles, et autres sont en fait implémentés.

En JavaScript, un constructeur est appelé lorsqu'un objet est créé en utilisant le mot-clé `new`. Le but d'un constructeur est de créer un nouvel objet et de définir ses valeurs pour toute propriété d'objet existante.

### Utilisation des Classes ES6

Les classes sont une alternative à la syntaxe des fonctions constructeurs pour implémenter l'héritage prototypal. Nous appelons également les classes `syntactic sugar`.

Derrière les scènes, les classes fonctionnent exactement comme les fonctions constructeurs. Avant ES6, JavaScript n'avait pas de concepts de classes. Pour simuler une classe, vous utilisez souvent le [modèle de constructeur ou de prototype](https://www.javascripttutorial.net/javascript-constructor-prototype/).

### Utilisation de Object.create()

C'est la manière la plus simple de lier un objet à un objet prototype. C'est une méthode utilisée pour créer un nouvel objet avec l'objet prototype spécifié et les propriétés.

La méthode object.create() retourne un nouvel objet avec l'objet prototype spécifié et les propriétés.

Examinons cela plus en détail maintenant :

## Comment Implémenter l'Héritage Prototypal avec les Fonctions Constructeurs en JavaScript

Nous allons utiliser une fonction pour créer un héritage prototypal. Nous allons commencer par implémenter une expression de fonction User. N'oubliez pas de toujours commencer le nom d'une fonction constructeur par une majuscule (convention standard).

```javascript
function User(name){
    this.name = name;

    // ne créez jamais de fonction à l'intérieur d'une fonction constructeur
    this.printName = function(){
        console.log(this.name);
    }
    
    console.log(this);
}


let kedar = new User("kedar")
```

**Sortie**

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ss2-2.png align="left")

*Prototype utilisant une fonction constructeur*

Nous avons créé une fonction constructeur dans l'exemple ci-dessus. Mais qu'est-ce que le mot-clé `new` ? Avec l'aide du mot-clé new, nous pouvons créer une instance de ce constructeur.

Lorsque nous créons une instance de l'objet constructeur, un objet vide est créé ({}). Cet objet vide ({}) est ensuite lié au prototype.

Nous ne devrions jamais créer une fonction à l'intérieur d'une fonction constructeur. Parce que chaque fois qu'une instance est créée, une nouvelle fonction est créée avec elle que nous avons créée à l'intérieur de la fonction constructeur. Cela créera des problèmes majeurs de performance.

La solution à ce problème est les prototypes. Nous pouvons définir une fonction sur le prototype d'un objet directement. Ainsi, l'objet créé en utilisant cette fonction constructeur aura accès à cette fonction.

**Exemple :**

```javascript
function User(name){
    this.name = name;
    
    console.log(this);
}

User.prototype.printName = function(){
	console.log(this.name)
}


let kedar = new User("kedar")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ss3-2.png align="left")

*Prototype utilisant une fonction constructeur*

Dans la sortie ci-dessus, vous pouvez voir la méthode `printName()` dans le prototype de la fonction constructeur User. C'est la manière préférée de créer une fonction dans une fonction constructeur pour optimiser les performances.

Ainsi, tous les objets créés par cette fonction constructeur auront accès à la fonction printName().

Nous pouvons accéder à ces fonctions avec objectName.functionName() comme ceci :

```javascript
function User(name){
    this.name = name;
    
    console.log(this);
}

User.prototype.printName = function(){
	console.log(this.name)
}


let kedar = new User("kedar")
kedar.printName()
```

Nous pouvons accéder au prototype de la fonction constructeur avec la syntaxe suivante :

```javascript
console.log(User.__proto__)
```

Le prototype de l'objet est le même que le prototype de la fonction constructeur. Vous ne me croyez pas ? Vérifiez ceci :

```javascript
console.log(kedar.__proto__ === User.prototype) 
// Vrai

console.log(User.prototype.isPrototypeOf(kedar))
// Vrai
```

Le prototype de User est le prototype utilisé par son objet et n'appartient pas à User.

```javascript
console.log(User.prototype.isPrototypeOf(User))
// Faux
```

Nous pouvons également lier une variable à un prototype :

```javascript
User.prototype.species = "Homo Sapiens"
```

Maintenant, cette variable appartient au prototype et non à l'objet. Nous pouvons vérifier cela en utilisant `hasOwnProperty()`.

### Héritage Prototypal des Objets Intégrés

Nous avons de nombreuses méthodes disponibles à utiliser sur les tableaux. Comment cela fonctionne-t-il ?

La réponse est l'héritage prototypal. Lorsque nous créons un nouveau tableau, il hérite chaque fois de Array.prototype. C'est ainsi que nous avons accès à toutes ces différentes méthodes.

```javascript
const arr = [1,2,3,4,5]
console.log(arr)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ss5-2.png align="left")

*Prototype d'un tableau*

Nous pouvons également attacher notre propre méthode à Array.prototype afin que chaque fois que nous créons un nouveau tableau, nous aurons accès à cette méthode.

```javascript
const arr = [1,2,4,4,5,5]

Array.prototype.unique = function(){
    return [...new Set(this)]
}

console.log(arr.unique());
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ss6-2.png align="left")

*Prototype d'un tableau avec la méthode unique() personnalisée ajoutée au prototype.*

## Comment Implémenter l'Héritage Prototypal avec les Classes ES6 en JavaScript

Nous pouvons implémenter l'OOP en utilisant des classes, mais derrière les scènes, il utilise l'héritage prototypal. Cette méthode a été introduite pour faciliter la compréhension des personnes venant d'autres langages comme C++ et Java.

Nous allons implémenter les classes User de l'exemple précédent :

```javascript
// Expression de classe
class User = class{

}

// Déclaration de classe
class User{

}
```

Dans l'exemple ci-dessus, nous pouvons voir qu'il y a 2 façons d'implémenter une classe en JavaScript. Vous pouvez choisir l'une ou l'autre selon votre préférence.

À l'intérieur de la classe, la première chose que nous devons faire est d'ajouter une méthode constructeur. Le constructeur peut également prendre des arguments.

```javascript
class User{
	constructor(name){
    	this.name = name
    }
    
    printName(){
        console.log(this.name);
    }
}

const kedar = new User("kedar")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ss7-1.png align="left")

*Prototype utilisant une classe ES6*

Rappelez-vous que chaque fois que nous créons un objet d'une classe, un constructeur est invoqué en premier. S'il n'y a pas de constructeur, le constructeur par défaut est invoqué, qui ne fait rien.

### 3 choses à retenir sur les classes

* Les classes ne sont pas hissed (si vous ne savez pas ce qu'est le hissing, [lisez ce guide](https://www.freecodecamp.org/news/javascript-execution-context-and-hoisting/))
    
* Les classes sont des citoyens de première classe (Si un langage de programmation a la capacité de passer une fonction comme argument – de traiter les fonctions comme des valeurs et de retourner des fonctions – il est dit que le langage a des fonctions de première classe et ces fonctions sont appelées citoyens de première classe)
    
* Les classes sont exécutées en mode strict. (Si vous ne savez pas ce qu'est le mode strict, [lisez ce guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode))
    

### Que sont les Setters et Getters ?

Ce sont des méthodes simples des classes qui obtiennent et définissent une valeur. Mais de l'extérieur, elles ressemblent à des méthodes simples. Regardons l'exemple ci-dessous.

```javascript
class User{
	constructor(name){
    	this._name = name
    }

    get getName(){
        console.log(this._name)
    }

    set setName(newName){
        this._name = newName
    }
}

const kedar = new User("kedar")
kedar.setName = "John"
kedar.getName
```

Dans l'exemple ci-dessus, vous pouvez voir le getter `getName` qui enregistre un nom. Les setters sont utilisés pour définir la valeur d'une propriété existante. Lorsque nous définissons un nom en utilisant un setter, nous devons utiliser (_) avant le nom de la propriété par convention.

### Comment Utiliser les Méthodes Statiques

Les méthodes statiques sont liées à une classe et non aux instances de classe ou à l'objet de la classe. Nous pouvons accéder aux méthodes statiques uniquement via les classes et non via l'objet de cette classe.

```javascript
class User{
	constructor(name){
    	this._name = name
    }

    static anonymous(){
        console.log("anonymous");
    }
}

const kedar = new User("kedar")
kedar.anonymous() // erreur
User.anonymous() // "anonymous"
```

Nous pouvons créer directement des méthodes statiques à l'intérieur des classes en utilisant le mot-clé static avant le nom de la méthode. Dans l'exemple ci-dessus, notez que nous pouvons uniquement appeler la méthode statique sur une classe et non sur un objet de classe.

Il y a une autre façon d'implémenter une méthode statique :

```c
class User{
	constructor(name){
    	this._name = name
    }
}

User.anonymous = function(){
	console.log("anonymous");
}

const kedar = new User("kedar")
kedar.anonymous() // erreur
User.anonymous() // "anonymous"
```

## Comment Implémenter l'Héritage Prototypal avec Object.create() en JavaScript

[La méthode statique `Object.create()` crée un nouvel objet, en utilisant un objet existant comme prototype de l'objet nouvellement créé.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

```javascript
const User = {
    init(name){
        this.name = name
    },
    
    printName(){
        console.log(this.name);
    }
}

let kedar = Object.create(User)
kedar.init("kedar")
kedar.printName()
```

Le nouvel objet créé héritera de toutes les propriétés de l'objet prototype. Vous pouvez spécifier un deuxième paramètre pour ajouter de nouvelles propriétés à l'objet, que le prototype n'avait pas :

```javascript
const newObject = Object.create(prototype, newProperties)
```

```javascript
const User = {
    
    printName(){
        console.log(this.name);
    }
}

let properties = {
    name: {
    	value:"John"
    }
    
}

let John = Object.create(User,properties)
John.printName()
```

## Comment Fonctionne l'Héritage en JavaScript

L'héritage vous permet de définir une classe/un objet qui prend toute la fonctionnalité d'une classe/un objet parent et vous permet d'en ajouter plus. En utilisant l'héritage de classe, une classe/un objet peut hériter de toutes les méthodes et propriétés d'une autre classe. C'est une fonctionnalité utile qui permet la réutilisation du code.

Maintenant, nous allons examiner l'héritage dans la fonction constructeur, les classes ES6 et Object.create().

### Fonction Constructeur

Comprenons l'héritage des fonctions constructeurs par l'exemple. Si vous ne savez pas comment fonctionne l'héritage à un niveau élevé, consultez la section où nous avons discuté de "Comment concevons-nous réellement une classe".

**Exemple :**

```javascript
const User = function(name, password){
    
    this.name = name
    this.password = password
}

User.prototype.printName = function(){
    console.log(this.name);
}

const Admin = function(name, password){
    this.name = name
    this.password = password
}

Admin.prototype.Stats = function(){
    console.log("Stats");
}

const kedar = new Admin("kedar", 12345)
kedar.Stats()
```

Dans le code ci-dessus, nous avons 2 fonctions constructeurs, et elles ont quelques similitudes. Pourtant, nous l'avons écrit deux fois, ce qui viole le principe DRY (Don't Repeat Yourself). Pour éviter de répéter le même code, nous utilisons l'héritage.

```javascript
const User = function(name, password){
    
    this.name = name
    this.password = password
}

User.prototype.printName = function(){
    console.log(this.name);
}

const Admin = function(name, password, course){
    User.call(this, name, password)
    this.course = course
}

Admin.prototype = Object.create(User.prototype)

Admin.prototype.Stats = function(){
    console.log("Stats");
}

const kedar = new Admin("kedar", 12345, "JavaScript")
kedar.printName()
```

Dans le code ci-dessus, d'abord dans la fonction Admin (enfant), nous avons attaché `this` à User (parent) et l'avons appelé avec des paramètres. Une fois que nous avons fait cela, nous avons pu accéder aux champs name et password. Mais nous n'avons pas pu accéder aux méthodes de la fonction parente. Parce que nous devons connecter le prototype de User et Admin.

Pour cela, juste après la fonction enfant, nous avons pointé le prototype Admin vers le prototype User, ce qui nous a donné accès aux méthodes de la fonction parente (User).

Assurez-vous de pointer le prototype de l'enfant (Admin) vers la fonction parente (User) immédiatement après la fonction enfant (Admin). Parce qu'il retourne un objet vide et supprime toutes les méthodes de la fonction enfant (Admin). Donc, créez toujours les méthodes de la fonction enfant (Admin) après avoir pointé le prototype de l'enfant (Admin) vers le prototype de la fonction parente (User).

Maintenant, voyons à quoi ressemble notre chaîne de prototypes :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ss8-1.png align="left")

*Héritage de prototype utilisant une fonction constructeur*

Au bas, il y a un prototype d'objet. Après cela, nous pouvons voir qu'il y a un prototype User et en haut, nous voyons un prototype Admin.

### ES6

Il est super simple d'implémenter l'héritage en utilisant la syntaxe ES6. Mais rappelez-vous que ES6 utilise des fonctions constructeurs pour implémenter l'héritage derrière les scènes.

```javascript
class User{
    constructor(name, password){
        this.name = name
        this.password  =password
    }

    printName(){
        console.log(this.name);
    }
}

class Admin extends User{
    constructor(name, password, course){
        super(name, password)
        this.course = course
    }

    Stats(){
        console.log("Stats");
    }
}

const kedar = new Admin("kedar", 123456, "JavaScript")
kedar.printName()
```

Ainsi, nous avons 2 classes, User et Admin. Lorsque nous voulons hériter, nous ajoutons simplement `extends` et la classe dont nous voulons hériter devant la classe enfant, similaire à la syntaxe montrée dans le code ci-dessus.

Lorsque nous avons terminé, dans le constructeur de la classe enfant, nous appelons la méthode `super()` pour passer un argument à la classe parente, ce qui est requis. C'est ainsi que nous pouvons implémenter l'héritage en JavaScript en utilisant la syntaxe ES6.

Nous pouvons également `écraser` la méthode parente en implémentant une méthode avec le même nom dans la classe enfant.

```javascript
class User{
    constructor(name, password){
        this.name = name
        this.password  =password
    }

    printName(){
        console.log(this.name);
    }
}

class Admin extends User{
    constructor(name, password, course){
        super(name, password)
        this.course = course
    }

    Stats(){
        console.log("Stats");
    }
    
    printName(){
    	console.log("Child class " + this.name)
    }
}

const kedar = new Admin("kedar", 123456, "JavaScript")
kedar.printName()
```

### Object.create()

L'implémentation de l'héritage dans Object.create() est simple. Consultez le code ci-dessous :

```javascript
const User = {
    printName(){
        console.log(this.name);
    },

    init(name, password){
        this.name = name
        this.password = password
    }
}

const Admin = Object.create(User)
Admin.init = function(name, password, course){
    User.init.call(this, name, password)
    this.course = course
}

Admin.stats = function(){
    console.log("Stats");
}

const kedar = Object.create(Admin)
kedar.init("kedar", 123456)
kedar.printName()
kedar.stats()
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ss9-1.png align="left")

*Héritage de prototype utilisant Object.create()*

Tout d'abord, nous avons créé une fonction User. Ensuite, nous avons créé un Admin pointant vers User avec l'aide de `Object.create()`. Avec l'aide de la méthode `Admin.init()`, nous avons appelé la méthode `init()` de User et passé des valeurs à la fonction parente.

## Comment Fonctionne l'Encapsulation en JavaScript

Ci-dessus, nous avons examiné ce que signifie l'encapsulation à un niveau très élevé. Maintenant, nous allons examiner un exemple pour l'expliquer plus en détail.

L'encapsulation peut être définie comme *the packing of data and functions into one component.* Cela est également connu sous le nom de regroupement ou de bundling, et signifie simplement rassembler les données et les méthodes qui opèrent sur les données. Cela peut être une fonction, une classe ou un objet.

L'encapsulation permet de *contrôler l'accès à ce composant.* Lorsque nous avons les données et les méthodes associées dans une seule unité, nous pouvons contrôler comment elles sont accessibles depuis l'extérieur de l'unité. Ce processus est appelé Encapsulation\*\*.\*\*

### Propriétés Protégées

```javascript
class User{
    constructor(name, password){
        this._name = name
        this._password = password
    }
}

const kedar = new User("kedar", 123456)
console.log(kedar._password);
```

Un membre protégé est accessible au sein de la classe et de tout objet qui en hérite. Une valeur protégée est partagée à travers toutes les couches de la chaîne de prototypes.

Nous avons utilisé (_) dans `this._name`, qui est une propriété protégée. Nous pouvons toujours accéder à cette propriété en dehors de la classe. Ce n'est qu'une convention que les programmeurs utilisent.

Si nous savons qu'il y a (_) dans un nom de propriété, nous ne devons pas manipuler cette propriété depuis l'extérieur de la classe.

```javascript
class User{
    constructor(name, password){
        this._name = name
        this._password = password
    }
    
    get getName(){
    	console.log(this._name)
    }
}

const kedar = new User("kedar", 123456)
kedar.getName
```

### Propriétés Privées

```javascript
class User{
    constructor(name, password){
        this.#name = name
        this._password = password
    }
    
    get getName(){
    	console.log(this._name)
    }
}

const kedar = new User("kedar", 123456)
console.log(kedar.#name);
```

Pour implémenter une propriété vraiment privée en JavaScript, nous devons utiliser (#) avant le nom de la propriété ou de la méthode. Ces propriétés et méthodes privées ne seront pas accessibles depuis l'extérieur de la classe, ce qui les rendra vraiment privées.

Cela aidera à restreindre l'accès aux propriétés depuis l'extérieur de la classe. Si nous voulons accéder à une propriété depuis l'extérieur, nous devons créer une méthode qui imprimera uniquement les propriétés sans donner accès à la modification de la valeur de cette propriété.

```javascript
class User{
    #name

    constructor(name, password){
        this.#name = name
        this._password = password
    }
    
    #printName(){
        console.log(this.#name);
    }

    PrintFromPrivateMethod(){
        this.#printName()
    }
}

const kedar = new User("kedar", 123456)
kedar.PrintFromPrivateMethod()
```

## **Conclusion**

J'espère que vous comprenez maintenant comment fonctionne l'OOP en JavaScript. Merci d'avoir lu !

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)
    
* [Instagram](https://www.instagram.com/kedar_98/)