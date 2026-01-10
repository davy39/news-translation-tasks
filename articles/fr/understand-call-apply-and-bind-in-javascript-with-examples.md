---
title: Comment utiliser les fonctions Call, Apply et Bind en JavaScript – avec des
  exemples de code
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2022-06-20T18:25:02.000Z'
originalURL: https://freecodecamp.org/news/understand-call-apply-and-bind-in-javascript-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Screenshot-2022-06-14-at-8.53.33-PM-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les fonctions Call, Apply et Bind en JavaScript – avec
  des exemples de code
seo_desc: 'In this article, I am going to explain how to use call, apply, and bind
  in JavaScript with simple examples.

  We will also implement an example that showcases how you can create your own map
  function with the apply function.

  Without further ado, let''s ...'
---

Dans cet article, je vais expliquer comment utiliser call, apply et bind en JavaScript avec des exemples simples.

Nous allons également implémenter un exemple qui montre comment vous pouvez créer votre propre fonction map avec la fonction apply.

Sans plus attendre, commençons.

## Table des matières

* [Prérequis](#heading-prerequisites)
    
* [Définitions](#heading-definitions)
    
* [Comment utiliser la fonction call en JavaScript](#heading-how-to-use-the-call-function-in-javascript)
    
* [Comment utiliser la fonction apply en JavaScript](#heading-how-to-use-the-apply-function-in-javascript)
    
* [Comment utiliser la fonction bind en JavaScript](#heading-how-to-use-the-bind-function-in-javascript)
    
* [Comment créer votre propre fonction map](#heading-how-to-create-your-own-map-function)
    
* [Résumé](#heading-summary)
    

## Prérequis

Voici quelques-unes des choses que vous devriez comprendre pour tirer le meilleur parti de cet article :

* [Fonctions](https://www.freecodecamp.org/news/what-is-a-function-javascript-function-examples/)
    
* [Prototypes de fonction](https://www.freecodecamp.org/news/all-you-need-to-know-to-understand-javascripts-prototype-a2bff2d28f03/)
    
* [Mot-clé This](https://www.freecodecamp.org/news/what-is-this-in-javascript/)
    

## Définitions

Examinons de plus près les fonctions que nous allons étudier ici pour comprendre ce qu'elles font.

**Call** est une fonction qui vous aide à changer le contexte de la fonction invoquée. En termes simples, elle vous aide à remplacer la valeur de `this` à l'intérieur d'une fonction par la valeur que vous souhaitez.

**Apply** est très similaire à la fonction `call`. La seule différence est que dans `apply`, vous pouvez passer un tableau comme liste d'arguments.

**Bind** est une fonction qui vous aide à créer une autre fonction que vous pouvez exécuter plus tard avec le nouveau contexte de `this` qui est fourni.

Maintenant, nous allons examiner quelques exemples de base des fonctions call, apply et bind. Ensuite, nous examinerons un exemple où nous construirons notre propre fonction similaire à la fonction map.

## Comment utiliser la fonction Call en JavaScript

`call` est une fonction que vous utilisez pour changer la valeur de `this` à l'intérieur d'une fonction et l'exécuter avec les arguments fournis.

Voici la syntaxe de la fonction `call` :

```javascript

func.call(thisObj, args1, args2, ...)
```

Où,

* **func** est une fonction qui doit être invoquée avec un objet `this` différent
    
* **thisObj** est un objet ou une valeur qui doit être remplacée par le mot-clé `this` présent à l'intérieur de la fonction `func`
    
* **args1, args2** sont des arguments qui sont passés à la fonction invoquée avec l'objet `this` modifié.
    

Notez que si vous invoquez une fonction sans aucun argument `thisObj`, alors JavaScript considère cette propriété comme un objet global.

Maintenant que nous avons un peu de contexte sur ce qu'est la fonction `call`, commençons par la comprendre plus en détail avec quelques exemples.

### Comment appeler une fonction avec différents contextes en JS

Considérons l'exemple ci-dessous. Il se compose de 3 classes – `Car`, `Brand1` et `Brand2`.

```javascript
function Car(type, fuelType){
	this.type = type;
	this.fuelType = fuelType;
}

function setBrand(brand){
	Car.call(this, "convertible", "petrol");
	this.brand = brand;
	console.log(`Car details = `, this);
}

function definePrice(price){
	Car.call(this, "convertible", "diesel");
	this.price = price;
	console.log(`Car details = `, this);
}

const newBrand = new setBrand('Brand1');
const newCarPrice = new definePrice(100000);
```

Si vous regardez attentivement, vous pouvez voir que nous utilisons la fonction `call` pour invoquer la fonction `Car` à deux reprises. Tout d'abord, dans `setBrand` puis dans `definePrice`.

Dans ces deux fonctions, nous invoquons la fonction `Car` avec l'objet `this` représentant les fonctions elles-mêmes. Par exemple, à l'intérieur de `setBrand`, nous appelons la fonction `Car` avec l'objet `this` appartenant à son contexte. Le cas est similaire pour `definePrice`.

Voici une courte vidéo illustrant cela : [https://www.canva.com/design/DAFD4b369JM/watch](https://www.canva.com/design/DAFD4b369JM/watch)

### Comment appeler une fonction sans arguments en JS

Considérons l'exemple ci-dessous :

```javascript
const newEntity = (obj) => console.log(obj);

function mountEntity(){
	this.entity = newEntity;
	console.log(`Entity ${this.entity} is mounted on ${this}`);
}

mountEntity.call();
```

Dans cet exemple, nous avons invoqué la fonction `mountEntity` sans argument `thisObj`. Dans de tels cas, JavaScript fait référence à l'objet global.

## Comment utiliser la fonction Apply en JavaScript

La fonction `Apply` est très similaire à la fonction `Call`. La seule différence entre `call` et `apply` est la différence dans la manière dont les arguments sont passés.

Dans `apply`, les arguments que vous pouvez passer en tant que littéral de tableau ou un nouvel objet de tableau.

Voici la syntaxe de la fonction `apply` :

```javascript
func.apply(thisObj, argumentsArray);
```

Où,

* **func** est une fonction qui doit être invoquée avec un objet `this` différent
    
* **thisObj** est un objet ou une valeur qui doit être remplacée par le mot-clé `this` présent à l'intérieur de la fonction `func`
    
* **argumentsArray** peut être un tableau d'arguments, un objet de tableau ou le mot-clé [arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) lui-même.
    

Comme vous pouvez le voir ci-dessus, la fonction `apply` a différents types de syntaxes.

La première syntaxe est simple. Vous pouvez passer un tableau d'arguments comme ci-dessous :

```javascript
func.apply(thisObj, [args1, args2, ...]);
```

La deuxième syntaxe est celle où nous pouvons lui passer le nouvel objet de tableau :

```javascript
func.apply(thisObj, new Array(args1, args2));
```

La troisième syntaxe est celle où nous pouvons passer le mot-clé arguments :

```javascript
func.apply(thisObj, arguments);
```

[arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments) est un objet spécial disponible à l'intérieur d'une fonction. Il contient les valeurs des arguments qui sont passés à une fonction. Vous pouvez utiliser ce mot-clé avec la fonction `apply` pour prendre un nombre quelconque d'arguments arbitraires.

Le meilleur aspect de `apply` est que nous n'avons pas besoin de nous soucier du nombre d'arguments qui sont passés à la fonction invoquée. Grâce à sa nature dynamique et polyvalente, vous pouvez l'utiliser dans des situations compliquées.

Examinons le même exemple que ci-dessus, mais cette fois nous utiliserons la fonction `apply`.

```javascript
function Car(type, fuelType){
	this.type = type;
	this.fuelType = fuelType;
}

function setBrand(brand){
	Car.apply(this, ["convertible", "petrol"]); // Syntaxe avec littéral de tableau
	this.brand = brand;
	console.log(`Car details = `, this);
}

function definePrice(price){
	Car.apply(this, new Array("convertible", "diesel")); // Syntaxe avec construction d'objet de tableau
	this.price = price;
	console.log(`Car details = `, this);
}

const newBrand = new setBrand('Brand1');
const newCarPrice = new definePrice(100000);
```

Et voici un exemple qui montre comment utiliser le mot-clé `arguments` :

```javascript
function addUp(){
		// Utilisation des arguments pour capturer le nombre arbitraire d'entrées
    const args = Array.from(arguments); 
    this.x = args.reduce((prev, curr) => prev + curr, 0);
    console.log("this.x = ", this.x);
}

function driverFunc(){
    const obj = {
        inps: [1,2,3,4,5,6]
    }
    addUp.apply(obj, obj.inps);
}

driverFunc();
```

## Comment utiliser la fonction Bind en JavaScript

La fonction `bind` crée une copie d'une fonction avec une nouvelle valeur pour le `this` présent à l'intérieur de la fonction appelante.

Voici la syntaxe de la fonction `bind` :

```javascript
func.bind(thisObj, arg1, arg2, ..., argN);
```

Où,

* **func** est une fonction qui doit être invoquée avec un objet `this` différent
    
* **thisObj** est un objet ou une valeur qui doit être remplacée par le mot-clé `this` présent à l'intérieur de la fonction `func`
    
* **arg1, arg2…argN** – vous pouvez passer 1 argument à la fonction appelante ou plus, similaire à la fonction `call`.
    

La fonction `bind` retourne ensuite une nouvelle fonction qui contient un nouveau contexte pour la variable `this` présente à l'intérieur de la fonction appelante :

```javascript
func(arg1, arg2);
```

Maintenant, cette fonction `func` peut être exécutée plus tard avec les arguments.

Regardons un exemple classique de comment utiliser une fonction `bind` avec l'aide d'un composant React basé sur une classe :

```jsx
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 1
    };
  }
  handleCode() {
    console.log("HANDLE CODE THIS = ", this.state);
  }
  render() {
    return <button onClick={this.handleCode}>Click Me</button>;
  }
}
```

Considérons le composant App ci-dessus. Il constitue les éléments suivants :

* `constructor` est une fonction qui est appelée lorsqu'une classe est instanciée avec un mot-clé `new`.
    
* `render` est une fonction qui exécute/rend le code JSX.
    
* `handleCode` est une méthode de classe qui journalise l'état du composant.
    

Si nous cliquons sur le bouton `Click Me`, nous recevrons une erreur indiquant : `Cannot read properties of undefined (reading 'state')`.

Vous vous êtes peut-être demandé pourquoi ce problème se produit ? 🤔🤔

Vous pourriez vous attendre à pouvoir accéder à l'état de la classe puisque `handleCode` est une méthode de classe. Mais voici le piège :

* `this` à l'intérieur de `handleCode` n'est pas le même que celui de la classe.
    
* À l'intérieur d'une classe, `this` est un objet régulier qui a des méthodes de classe non statiques comme propriétés. Mais `this` à l'intérieur de `handleCode` fera référence à un contexte différent.
    
* Pour être honnête, la valeur de `this` dans ce scénario dépend de l'endroit d'où la fonction est appelée. Si vous voyez, `handleCode` est appelé sur l'événement `onClick`.
    
* Mais à ce stade, nous obtiendrons `undefined` pour le contexte de `this` présent à l'intérieur de la fonction `handleCode`.
    
* Nous essayons d'appeler la propriété `state` d'une valeur indéfinie. Par conséquent, cela conduit à l'erreur ci-dessus.
    

Nous pouvons corriger cela en fournissant le bon contexte de `this` à l'intérieur de la méthode `handleCode`. Vous pouvez faire cela avec la méthode `bind`.

```jsx
class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      counter: 1
    };
   this.handleCode = this.handleCode.bind(this); // lie cette fonction
  }
  handleCode() {
    console.log("HANDLE CODE THIS = ", this.state);
  }
  render() {
    return <button onClick={this.handleCode}>Click Me</button>;
  }
}
```

Le `bind` créera une nouvelle fonction et la stockera à l'intérieur de l'objet `this` avec une nouvelle propriété en tant que `handleCode`. `Bind` s'assurera que le contexte `this` de la classe est appliqué au `this` présent à l'intérieur de la fonction `handleCode`.

## Comment créer votre propre fonction `map`

Maintenant que nous avons toutes les choses nécessaires, commençons par créer notre propre fonction `map`. Commençons par comprendre les choses dont nous aurons besoin pour construire notre propre fonction `map`.

Voici la syntaxe de la fonction `map` :

```javascript
arr.map(func)
```

Où,

* **arr** est un tableau sur lequel la map est appelée.
    
* **func** est la fonction qui doit s'exécuter sur chaque élément d'un tableau.
    

La fonctionnalité de base d'une fonction `map` est simple :

C'est une fonction qui parcourt chaque élément d'un tableau et applique la fonction qui est passée en argument. Le type de retour d'une map est à nouveau un tableau avec `func` appliqué à chaque élément.

Maintenant que nous comprenons les exigences, nous pouvons passer à la création de notre propre fonction `map`. Voici le code de notre nouvelle fonction `map` :

```javascript
function newMap(func){
  let destArr = [];
  const srcArrLen = this.length;
  for(let i = 0; i < srcArrLen; i++){
    destArr.push(func.call(this, this[i]));
  }

  return destArr;
}
```

Comprenons la fonction ci-dessus bit par bit :

* Cette fonction accepte un argument appelé `func`. Ce n'est rien d'autre qu'une fonction qui doit être appelée sur chaque élément d'un tableau.
    
* Les autres parties du code sont assez explicites. Nous nous concentrerons sur la ligne suivante : `destArr.push(func.call(this, this[i]));`
    
* Cette ligne fait deux choses :
    

1. Pousse les changements dans le `destArr`
    
2. Exécute la `func` à l'aide de la méthode `call`. Ici, la méthode `call` (comme expliqué dans les sections précédentes) exécutera la méthode `func` avec une nouvelle valeur pour l'objet `this` présent à l'intérieur de la méthode `func`.
    

Maintenant, regardons comment nous allons exécuter notre fonction `newMap`. L'approche ci-dessous d'ajout d'une nouvelle méthode au type de données primitif existant n'est pas recommandée, mais nous le ferons pour les besoins de cet article.

**NOTE :** ne suivez pas l'approche ci-dessous dans votre code de production. Cela peut endommager le code existant.

```javascript
Object.defineProperty(Array.prototype, 'newMap', {
  value: newMap
});
```

Avec `defineProperty`, nous créons une nouvelle propriété à l'intérieur de `Array.prototype`.

Une fois cela fait, nous sommes prêts à exécuter notre nouvelle fonction map sur un tableau.

```javascript
const arr = [1,2,3];
const newArr = arr.newMap(item => item + 1);
console.log(newArr);
```

## Résumé

Cet article vous a montré ce que les fonctions call, apply et bind peuvent faire via des exemples.

Pour parler brièvement de ces fonctions :

* Call, apply et bind sont les fonctions qui vous aident à changer le contexte du mot-clé `this` présent à l'intérieur de la fonction invoquée.
    
* Nous avons vu comment chaque fonction peut être appelée de différentes manières – par exemple, avec `apply`, vous pouvez exécuter une fonction avec un tableau d'arguments, et avec la fonction `call`, vous pouvez exécuter la même chose, mais les arguments sont répartis via des virgules.
    
* Ces fonctions sont vraiment utiles dans les composants basés sur des classes de React.
    

Merci d'avoir lu !

Suivez-moi sur [Twitter](https://twitter.com/keurplkar), [GitHub](https://github.com/keyurparalkar) et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).