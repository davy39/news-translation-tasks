---
title: Une introduction à la programmation orientée objet en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T17:05:04.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-object-oriented-programming-in-javascript-8900124e316a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KmFzveXeGZNH5kdepynd4A.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une introduction à la programmation orientée objet en JavaScript
seo_desc: 'By Rainer Hahnekamp

  This article is for students of JavaScript that don’t have any prior knowledge in
  object-oriented programming (OOP). I focus on the parts of OOP that are only relevant
  for JavaScript and not OOP in general. I skip polymorphism bec...'
---

Par Rainer Hahnekamp

_Cet article s'adresse aux étudiants en JavaScript qui n'ont aucune connaissance préalable en programmation orientée objet (POO). Je me concentre sur les parties de la POO qui sont uniquement pertinentes pour JavaScript et non sur la POO en général. Je saute le polymorphisme car il convient mieux à un langage à typage statique._

### Pourquoi devez-vous connaître cela ?

Avez-vous choisi JavaScript comme premier langage de programmation ? Souhaitez-vous devenir un développeur de premier plan qui travaille sur des systèmes d'entreprise géants couvrant cent mille lignes de code ou plus ?

À moins d'apprendre à adopter pleinement la programmation orientée objet, vous serez bien et véritablement perdu.

### Différents états d'esprit

Au football, vous pouvez jouer en défense sûre, vous pouvez jouer avec des balles hautes depuis les côtés ou vous pouvez attaquer comme s'il n'y avait pas de lendemain. Toutes ces stratégies ont le même objectif : gagner le match.

Il en va de même pour les paradigmes de programmation. Il existe différentes façons d'aborder un problème et de concevoir une solution.

La programmation orientée objet, ou POO, est LE paradigme pour le développement d'applications modernes. Elle est soutenue par des langages majeurs comme Java, C# ou JavaScript.

### Le paradigme orienté objet

Du point de vue de la POO, une application est une collection d'« objets » qui communiquent entre eux. Nous basons ces objets sur des choses du monde réel, comme des produits en inventaire ou des dossiers d'employés. Les objets contiennent des données et exécutent une certaine logique basée sur leurs données. Par conséquent, le code POO est très facile à comprendre. Ce qui est moins facile, c'est de décider comment diviser une application en ces petits objets en premier lieu.

Si vous étiez comme moi lorsque je l'ai entendu pour la première fois, vous n'avez aucune idée de ce que cela signifie réellement — tout cela semble très abstrait. Se sentir ainsi est absolument normal. Il est plus important que vous ayez entendu l'idée, que vous vous en souveniez et que vous essayiez d'appliquer la POO dans votre code. Avec le temps, vous gagnerez en expérience et alignerez davantage votre code avec ce concept théorique.

**Leçon** : La POO basée sur des objets du monde réel permet à quiconque de lire votre code et de comprendre ce qui se passe.

### L'objet comme pièce centrale

![Image](https://cdn-media-1.freecodecamp.org/images/E-8djcwlqdOvRJ0Dl9kHAlUINOI1ooUBnjAK)

Un exemple simple vous aidera à voir comment JavaScript implémente les principes fondamentaux de la POO. Considérons un cas d'utilisation de shopping dans lequel vous mettez des produits dans votre panier, puis calculez le prix total que vous devez payer. Si vous prenez vos connaissances en JavaScript et codez le cas d'utilisation sans POO, cela ressemblerait à ceci :

```
const bread = {name: 'Bread', price: 1};const water = {name: 'Water', price: 0.25};
```

```
const basket = [];basket.push(bread);basket.push(bread);basket.push(water);basket.push(water);basket.push(water);
```

```
const total = basket  .map(product => product.price)  .reduce((a, b) => a + b, 0);
```

```
console.log('one has to pay in total: ' + total);
```

La perspective POO facilite l'écriture de meilleur code car nous pensons aux objets comme nous les rencontrerions dans le monde réel. Comme notre cas d'utilisation contient un panier de produits, nous avons déjà deux types d'objets — l'objet panier et les objets produits.

La version POO du cas d'utilisation de shopping pourrait être écrite comme suit :

```
const bread = new Product('bread', 1);const water = new Product('water', .25)const basket = new Basket();basket.addProduct(2, bread);basket.addProduct(3, water);basket.printShoppingInfo();
```

Comme vous pouvez le voir dans la première ligne, nous créons un nouvel objet en utilisant le mot-clé `new` suivi du nom de ce qu'on appelle une classe (décrite ci-dessous). Cela retourne un objet que nous stockons dans la variable bread. Nous répétons cela pour la variable water et prenons un chemin similaire pour créer une variable basket. Après avoir ajouté ces produits à votre panier, vous imprimez enfin le montant total que vous devez payer.

La différence entre les deux extraits de code est évidente. La version POO se lit presque comme des phrases anglaises réelles et vous pouvez facilement comprendre ce qui se passe.

**Leçon** : Un objet modélisé sur des choses du monde réel se compose de données et de fonctions.

### Classe comme modèle

![Image](https://cdn-media-1.freecodecamp.org/images/auocIypgaJDNSym46KgEptmlE6FW3xFaxLPL)

Nous utilisons des classes en POO comme modèles pour créer des objets. Un objet est une « instance d'une classe » et l'« instanciation » est la création d'un objet basé sur une classe. Le code est défini dans la classe mais ne peut pas s'exécuter sauf s'il est dans un objet vivant.

Vous pouvez considérer les classes comme les plans pour une voiture. Ils définissent les propriétés de la voiture comme le couple et la puissance, les fonctions internes telles que les rapports air-carburant et les méthodes accessibles publiquement comme l'allumage. Ce n'est que lorsqu'une usine instancie la voiture, cependant, que vous pouvez tourner la clé et conduire.

Dans notre cas d'utilisation, nous utilisons la classe Product pour instancier deux objets, bread et water. Bien sûr, ces objets ont besoin de code que vous devez fournir dans les classes. Cela se passe comme suit :

```
function Product(_name, _price) {  const name = _name;  const price = _price;
```

```
this.getName = function() {    return name;  };
```

```
this.getPrice = function() {    return price;  };}
```

```
function Basket() {  const products = [];
```

```
this.addProduct = function(amount, product) {    products.push(...Array(amount).fill(product));  };
```

```
this.calcTotal = function() {    return products      .map(product => product.getPrice())      .reduce((a, b) => a + b, 0);  };
```

```
this.printShoppingInfo = function() {    console.log('one has to pay in total: ' + this.calcTotal());  };}
```

Une classe en JavaScript ressemble à une fonction, mais vous l'utilisez différemment. Le nom de la fonction est le nom de la classe et est en majuscule. Puisqu'elle ne retourne rien, nous n'appelons pas la fonction de la manière habituelle comme `const basket = Product('bread', 1);`. Au lieu de cela, nous ajoutons le mot-clé new comme `const basket = new Product('bread', 1);`.

Le code à l'intérieur de la fonction est le constructeur. Ce code s'exécute chaque fois qu'un objet est instancié. Product a les paramètres `_name` et `_price`. Chaque nouvel objet stocke ces valeurs à l'intérieur.

De plus, nous pouvons définir des fonctions que l'objet fournira. Nous définissons ces fonctions en préfixant le mot-clé this qui les rend accessibles depuis l'extérieur (voir Encapsulation). Remarquez que les fonctions ont un accès complet aux propriétés.

La classe Basket n'a pas besoin d'arguments pour créer un nouvel objet. L'instanciation d'un nouvel objet Basket génère simplement une liste vide de produits que le programme peut remplir ensuite.

**Leçon** : Une classe est un modèle pour générer des objets pendant l'exécution.

### Encapsulation

![Image](https://cdn-media-1.freecodecamp.org/images/mZ820W4kli-j2xEfcLDh6iCenZ6llKyD1eG5)

Vous pouvez rencontrer une autre version de la façon de déclarer une classe :

```
function Product(name, price) {  this.name = name;  this.price = price;}
```

Faites attention à l'assignation des propriétés à la variable `this`. À première vue, cela semble être une meilleure version car elle ne nécessite plus les méthodes getter (getName & getPrice) et est donc plus courte.

Malheureusement, vous avez maintenant donné un accès complet aux propriétés depuis l'extérieur. Donc, tout le monde pourrait y accéder et les modifier :

```
const bread = new Product('bread', 1);bread.price = -10;
```

C'est quelque chose que vous ne voulez pas car cela rend l'application plus difficile à maintenir. Que se passerait-il si vous ajoutiez un code de validation pour empêcher, par exemple, les prix inférieurs à zéro ? Tout code qui accède directement à la propriété price contournerait la validation. Cela pourrait introduire des erreurs qui seraient difficiles à tracer. Le code qui utilise les méthodes getter de l'objet, en revanche, est garanti de passer par la validation du prix de l'objet.

Les objets doivent avoir un contrôle exclusif sur leurs données. En d'autres termes, les objets « encapsulent » leurs données et empêchent les autres objets d'accéder directement aux données. Le seul moyen d'accéder aux données est indirect via les fonctions écrites dans les objets.

Les données et le traitement (aka logique) appartiennent ensemble. Cela est particulièrement vrai lorsqu'il s'agit d'applications plus grandes où il est très important que le traitement des données soit restreint à des endroits spécifiquement définis.

Bien fait, la POO produit une modularité par conception, le saint graal du développement logiciel. Elle éloigne le code spaghetti redouté où tout est étroitement couplé et vous ne savez pas ce qui se passe lorsque vous changez un petit morceau de code.

Dans notre cas, les objets de la classe Product ne vous permettent pas de changer le prix ou le nom après leur initialisation. Les instances de Product sont en lecture seule.

**Leçon** : L'encapsulation empêche l'accès aux données sauf par les fonctions de l'objet.

### Héritage

![Image](https://cdn-media-1.freecodecamp.org/images/5tlMVYYAPXe7tTT4qhcQY9iwRKAT2PSPKOOB)

L'héritage vous permet de créer une nouvelle classe en étendant une classe existante avec des propriétés et des fonctions supplémentaires. La nouvelle classe « hérite » de toutes les caractéristiques de sa classe parente, évitant ainsi la création de nouveau code à partir de zéro. De plus, toute modification apportée à la classe parente sera automatiquement disponible pour la classe enfant. Cela rend les mises à jour beaucoup plus faciles.

Supposons que nous avons une nouvelle classe appelée Book qui a un nom, un prix et un auteur. Avec l'héritage, vous pouvez dire qu'un Book est identique à un Product mais avec la propriété author supplémentaire. Nous disons que Product est la superclasse de Book et Book est une sous-classe de Product :

```
function Book(_name, _price, _author) {  Product.call(this, _name, _price);  const author = _author;    this.getAuthor = function() {    return author;  }}
```

Remarquez l'argument supplémentaire `Product.call` avec `this` comme premier argument. Veuillez noter : Bien que book fournisse les méthodes getter, il n'a toujours pas d'accès direct aux propriétés name et price. Book doit appeler ces données depuis la classe Product.

Vous pouvez maintenant ajouter un objet book au panier sans aucun problème :

```
const faust = new Book('faust', 12.5, 'Goethe');basket.addProduct(1, faust);
```

Basket attend un objet de type Product. Puisque book hérite de Product via Book, il est également un Product.

**Leçon** : Les sous-classes peuvent hériter des propriétés et des fonctions des superclasses tout en ajoutant des propriétés et des fonctions qui leur sont propres.

### JavaScript et POO

Vous trouverez trois paradigmes de programmation différents utilisés pour créer des applications JavaScript. Il s'agit de la programmation basée sur les prototypes, de la programmation orientée objet et de la programmation orientée fonctionnelle.

La raison en est l'histoire de JavaScript. À l'origine, il était basé sur les prototypes. JavaScript n'était pas destiné à être un langage pour les grandes applications.

Contrairement au plan de ses fondateurs, les développeurs ont de plus en plus utilisé JavaScript pour des applications plus grandes. La POO a été greffée sur la technique originale basée sur les prototypes.

L'approche basée sur les prototypes est montrée ci-dessous. Elle est considérée comme la « méthode classique et par défaut » pour construire des classes. Malheureusement, elle ne supporte pas l'encapsulation.

Même si le support de la POO par JavaScript n'est pas au même niveau que d'autres langages comme Java, il évolue encore. La sortie de la version ES6 a ajouté un mot-clé `class` dédié que nous pouvons utiliser. En interne, il sert le même but que la propriété prototype, mais il réduit la taille du code. Cependant, les classes ES6 manquent toujours de propriétés privées, ce qui explique pourquoi je suis resté fidèle à la « vieille méthode ».

Pour l'exhaustivité, voici comment nous écririons Product, Basket et Book avec les classes ES6 et aussi avec l'approche prototype (classique et par défaut). Veuillez noter que ces versions ne fournissent pas d'encapsulation :

```
// Version ES6
```

```
class Product {  constructor(name, price) {    this.name = name;    this.price = price;  }}
```

```
class Book extends Product {  constructor(name, price, author) {    super(name, price);    this.author = author;  }}
```

```
class Basket {  constructor() {    this.products = [];  }
```

```
  addProduct(amount, product) {    this.products.push(Array(amount).fill(product));  }
```

```
  calcTotal() {    return this.products      .map(product => product.price)      .reduce((a, b) => a + b, 0);  }
```

```
  printShoppingInfo() {    console.log('one has to pay in total: ' + this.calcTotal());  }}
```

```
const bread = new Product('bread', 1);const water = new Product('water', 0.25);const faust = new Book('faust', 12.5, 'Goethe');
```

```
const basket = new Basket();basket.addProduct(2, bread);basket.addProduct(3, water);basket.addProduct(1, faust);basket.printShoppingInfo();
```

```
// Version Prototypefunction Product(name, price) {  this.name = name;  this.price = price;}function Book(name, price, author) {  Product.call(this, name, price);  this.author = author;}Book.prototype = Object.create(Product.prototype);Book.prototype.constructor = Book;function Basket() {  this.products = [];}Basket.prototype.addProduct = function(amount, product) {  this.products.push(...Array(amount).fill(product));};Basket.prototype.calcTotal = function() {  return this.products    .map(product => product.price)    .reduce((a, b) => a + b, 0);};Basket.prototype.printShoppingInfo = function() {  console.log('one has to pay in total: ' + this.calcTotal());};
```

**Leçon** : La POO a été ajoutée à JavaScript plus tard dans son développement.

### Résumé

En tant que nouveau programmeur apprenant JavaScript, il faudra du temps pour apprécier pleinement la programmation orientée objet. Les choses importantes à comprendre à ce stade précoce sont les principes sur lesquels repose le paradigme POO et les avantages qu'ils offrent :

* Les objets modélisés sur des choses du monde réel sont la pièce centrale de toute application basée sur la POO.
* L'encapsulation protège les données contre les accès non contrôlés.
* Les objets ont des fonctions qui opèrent sur les données que les objets contiennent.
* Les classes sont les modèles utilisés pour instancier des objets.
* L'héritage est un outil puissant pour éviter la redondance.
* La POO est plus verbeuse mais plus facile à lire que d'autres paradigmes de codage.
* Puisque la POO est venue plus tard dans le développement de JavaScript, vous pouvez rencontrer un ancien code qui utilise des techniques de programmation basées sur les prototypes ou fonctionnelles.

### Lectures complémentaires

* [https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS)
* [http://voidcanvas.com/es6-private-variables/](http://voidcanvas.com/es6-private-variables/)
* [https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65)
* [https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance)
* [https://en.wikipedia.org/wiki/Object-oriented_programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
* [https://en.wikipedia.org/wiki/Object-oriented_programming](https://en.wikipedia.org/wiki/Object-oriented_programming)