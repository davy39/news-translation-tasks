---
title: JavaScript Créer un Objet – Comment Définir des Objets en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-20T15:06:19.000Z'
originalURL: https://freecodecamp.org/news/javascript-create-object-how-to-define-objects-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/IMG_7192.JPG
tags:
- name: JavaScript
  slug: javascript
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: JavaScript Créer un Objet – Comment Définir des Objets en JS
seo_desc: 'By Cristian Salcescu

  Objects are the main unit of encapsulation in Object-Oriented Programming. In this
  article, I will describe several ways to build objects in JavaScript. They are:


  Object literal

  Object.create()

  Classes

  Factory functions


  Object ...'
---

Par Cristian Salcescu

Les objets sont l'unité principale d'encapsulation en Programmation Orientée Objet. Dans cet article, je vais décrire plusieurs façons de construire des objets en JavaScript. Elles sont :

* Littéral d'objet
* Object.create()
* Classes
* Fonctions de fabrication

## Littéral d'Objet

Tout d'abord, nous devons faire une distinction entre les structures de données et les objets orientés objet. Les structures de données ont des données publiques et aucun comportement. Cela signifie qu'elles n'ont pas de méthodes.

Nous pouvons facilement créer de tels objets en utilisant la syntaxe de littéral d'objet. Cela ressemble à ceci :

```
const product = {
  name: 'apple',
  category: 'fruits',
  price: 1.99
}
  
console.log(product);
```

Les objets en JavaScript sont des collections dynamiques de paires clé-valeur. La clé est toujours une chaîne de caractères et doit être unique dans la collection. La valeur peut être un type primitif, un objet, ou même une fonction.

Nous pouvons accéder à une propriété en utilisant la notation par point ou par crochets.

```
console.log(product.name);
//"apple"

console.log(product["name"]);
//"apple"
```

Voici un exemple où la valeur est un autre objet.

```
const product = {
  name: 'apple',
  category: 'fruits',
  price: 1.99,
  nutrients : {
   carbs: 0.95,
   fats: 0.3,
   protein: 0.2
 }
}
```

La valeur de la propriété `carbs` est un nouvel objet. Voici comment nous pouvons accéder à la propriété `carbs`.

```
console.log(product.nutrients.carbs);
//0.95
```

### Noms de Propriétés Abréviés

Considérons le cas où nous avons les valeurs de nos propriétés stockées dans des variables.

```
const name = 'apple';
const category = 'fruits';
const price = 1.99;
const product = {
  name: name,
  category: category,
  price: price
}
```

JavaScript supporte ce qu'on appelle les noms de propriétés abréviés. Cela nous permet de créer un objet en utilisant simplement le nom de la variable. Il créera une propriété avec le même nom. Le littéral d'objet suivant est équivalent au précédent.

```
const name = 'apple';
const category = 'fruits';
const price = 1.99;
const product = {
  name,
  category,
  price
}
```

## Object.create

Ensuite, voyons comment implémenter des objets avec comportement, des objets orientés objet.

JavaScript a ce qu'on appelle le système de prototype qui permet de partager le comportement entre les objets. L'idée principale est de créer un objet appelé prototype avec un comportement commun et de l'utiliser lors de la création de nouveaux objets.

Le système de prototype nous permet de créer des objets qui héritent du comportement d'autres objets.

Créons un objet prototype qui nous permet d'ajouter des produits et d'obtenir le prix total d'un panier d'achat.

```
const cartPrototype = {
  addProduct: function(product){
    if(!this.products){
     this.products = [product]
    } else {
     this.products.push(product);
    }
  },
  getTotalPrice: function(){
    return this.products.reduce((total, p) => total + p.price, 0);
  }
}
```

Remarquez que cette fois la valeur de la propriété `addProduct` est une fonction. Nous pouvons également écrire l'objet précédent en utilisant une forme plus courte appelée la syntaxe de méthode abréviée.

```
const cartPrototype = {
  addProduct(product){/*code*/},
  getTotalPrice(){/*code*/}
}
```

Le `cartPrototype` est l'objet prototype qui conserve le comportement commun représenté par deux méthodes, `addProduct` et `getTotalPrice`. Il peut être utilisé pour construire d'autres objets héritant de ce comportement.

```
const cart = Object.create(cartPrototype);
cart.addProduct({name: 'orange', price: 1.25});
cart.addProduct({name: 'lemon', price: 1.75});

console.log(cart.getTotalPrice());
//3
```

L'objet `cart` a `cartPrototype` comme prototype. Il hérite du comportement de celui-ci. `cart` a une propriété cachée qui pointe vers l'objet prototype.

Lorsque nous utilisons une méthode sur un objet, cette méthode est d'abord recherchée sur l'objet lui-même plutôt que sur son prototype.

### this

Notez que nous utilisons un mot-clé spécial appelé `this` pour accéder et modifier les données sur l'objet.

Rappelons que les fonctions sont des unités indépendantes de comportement en JavaScript. Elles ne font pas nécessairement partie d'un objet. Lorsqu'elles en font partie, nous devons avoir une référence qui permet à la fonction d'accéder à d'autres membres du même objet. `this` est le contexte de la fonction. Il donne accès à d'autres propriétés.

### Données

Vous vous demandez peut-être pourquoi nous n'avons pas défini et initialisé la propriété `products` sur l'objet prototype lui-même.

Nous ne devrions pas faire cela. Les prototypes doivent être utilisés pour partager le comportement, pas les données. Partager les données conduira à avoir les mêmes produits sur plusieurs objets de panier. Considérez le code ci-dessous :

```
const cartPrototype = {
  products:[],
  addProduct: function(product){
      this.products.push(product);
  },
  getTotalPrice: function(){}
}

const cart1 = Object.create(cartPrototype);
cart1.addProduct({name: 'orange', price: 1.25});
cart1.addProduct({name: 'lemon', price: 1.75});
console.log(cart1.getTotalPrice());
//3

const cart2 = Object.create(cartPrototype);
console.log(cart2.getTotalPrice());
//3
```

Les objets `cart1` et `cart2` héritant du comportement commun de `cartPrototype` partagent également les mêmes données. Nous ne voulons pas cela. Les prototypes doivent être utilisés pour partager le comportement, pas les données.

## Classe

Le système de prototype n'est pas une méthode courante de construction d'objets. Les développeurs sont plus familiers avec la construction d'objets à partir de classes.

La syntaxe de classe permet une manière plus familière de créer des objets partageant un comportement commun. Elle crée toujours le même prototype derrière la scène, mais la syntaxe est plus claire et nous évitons également le problème précédent lié aux données. La classe offre un endroit spécifique pour définir les données distinctes pour chaque objet.

Voici le même objet créé en utilisant la syntaxe de sucre de classe :

```
class Cart{
  constructor(){
    this.products = [];
  }
  
  addProduct(product){
      this.products.push(product);
  }
  
  getTotalPrice(){
    return this.products.reduce((total, p) => total + p.price, 0);
  }
}

const cart = new Cart();
cart.addProduct({name: 'orange', price: 1.25});
cart.addProduct({name: 'lemon', price: 1.75});
console.log(cart.getTotalPrice());
//3

const cart2 = new Cart();
console.log(cart2.getTotalPrice());
//0
```

Remarquez que la classe a une méthode de constructeur qui initialise les données distinctes pour chaque nouvel objet. Les données dans le constructeur ne sont pas partagées entre les instances. Afin de créer une nouvelle instance, nous utilisons le mot-clé `new`.

Je pense que la syntaxe de classe est plus claire et familière pour la plupart des développeurs. Néanmoins, elle fait une chose similaire, elle crée un prototype avec toutes les méthodes et l'utilise pour définir de nouveaux objets. Le prototype peut être accédé avec `Cart.prototype`.

Il s'avère que le système de prototype est suffisamment flexible pour permettre la syntaxe de classe. Ainsi, le système de classe peut être simulé en utilisant le système de prototype.

### Propriétés Privées

La seule chose est que la propriété `products` sur le nouvel objet est publique par défaut.

```
console.log(cart.products);
//[{name: "orange", price: 1.25}
// {name: "lemon", price: 1.75}]
```

Nous pouvons la rendre privée en utilisant le préfixe dièse `#`.

Les propriétés privées sont déclarées avec la syntaxe `#name`. `#` fait partie du nom de la propriété lui-même et doit être utilisé pour déclarer et accéder à la propriété. Voici un exemple de déclaration de `products` comme propriété privée :

```
class Cart{
  #products
  constructor(){
    this.#products = [];
  }
  
  addProduct(product){
    this.#products.push(product);
  }
  
  getTotalPrice(){
    return this.#products.reduce((total, p) => total + p.price, 0);
  }
}

console.log(cart.#products);
//Uncaught SyntaxError: Private field '#products' must be declared in an enclosing class
```

### Fonctions de Fabrication

Une autre option est de créer des objets comme des collections de fermetures.

La fermeture est la capacité d'une fonction à accéder aux variables et paramètres d'une autre fonction même après que la fonction externe a été exécutée. Jetez un coup d'œil à l'objet `cart` construit avec ce qu'on appelle une fonction de fabrication.

```
function Cart() {
  const products = [];
  
  function addProduct(product){
    products.push(product);
  }
  
  function getTotalPrice(){
    return products.reduce((total, p) => total + p.price, 0);
  }
  
  return {
   addProduct,
   getTotalPrice
  }
}

const cart = Cart();
cart.addProduct({name: 'orange', price: 1.25});
cart.addProduct({name: 'lemon', price: 1.75});
console.log(cart.getTotalPrice());
//3
```

`addProduct` et `getTotalPrice` sont deux fonctions internes accédant à la variable `products` de leur parent. Elles ont accès à la variable `products` même après que le parent `Cart` a été exécuté. `addProduct` et `getTotalPrice` sont deux fermetures partageant la même variable privée.

`Cart` est une fonction de fabrication.

Le nouvel objet `cart` créé avec la fonction de fabrication a la variable `products` privée. Elle ne peut pas être accédée de l'extérieur.

```
console.log(cart.products);
//undefined
```

Les fonctions de fabrication n'ont pas besoin du mot-clé `new`, mais vous pouvez l'utiliser si vous le souhaitez. Cela retournera le même objet, que vous l'utilisiez ou non.

## Récapitulatif

Habituellement, nous travaillons avec deux types d'objets, des structures de données qui ont des données publiques et aucun comportement, et des objets orientés objet qui ont des données privées et un comportement public.

Les structures de données peuvent être facilement construites en utilisant la syntaxe de littéral d'objet.

JavaScript offre deux façons innovantes de créer des objets orientés objet. La première consiste à utiliser un objet prototype pour partager le comportement commun. Les objets héritent d'autres objets. Les classes offrent une belle syntaxe de sucre pour créer de tels objets.

L'autre option est de définir des objets comme des collections de fermetures.

**Pour plus d'informations sur les fermetures et les techniques de programmation fonctionnelle, consultez ma série de livres [Functional Programming with JavaScript and React](https://www.amazon.com/gp/product/B08BW8BY1H).**

**Le livre [Functional Programming in JavaScript](https://www.amazon.com/dp/B08CZZ4FQQ) est sur le point de sortir.**