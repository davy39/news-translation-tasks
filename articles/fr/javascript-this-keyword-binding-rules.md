---
title: Le mot-clé `this` en JavaScript + 5 règles de liaison clés expliquées pour
  les débutants en JS
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2020-10-23T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-this-keyword-binding-rules
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/cover_freecodecamp.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Le mot-clé `this` en JavaScript + 5 règles de liaison clés expliquées pour
  les débutants en JS
seo_desc: 'JavaScript''s this keyword is one of the hardest aspects of the language
  to grasp. But it is critically important for writing more advanced JavaScript code.

  In JavaScript, the this keyword allows us to:


  Reuse functions in different execution contexts...'
---

Le mot-clé `this` de JavaScript est l'un des aspects les plus difficiles du langage à comprendre. Mais il est extrêmement important pour écrire du code JavaScript plus avancé.

En JavaScript, le mot-clé `this` nous permet de :

* Réutiliser des fonctions dans différents contextes d'exécution. Cela signifie qu'une fonction, une fois définie, peut être invoquée pour différents objets en utilisant le mot-clé `this`.
* Identifier l'objet dans le contexte d'exécution actuel lorsque nous invoquons une méthode.

Le mot-clé `this` est très étroitement associé aux fonctions JavaScript. En ce qui concerne `this`, la chose fondamentale est de comprendre où une fonction est invoquée. Parce que nous ne savons pas ce qu'il y a dans le mot-clé `this` jusqu'à ce que la fonction soit invoquée.

L'utilisation de `this` peut être catégorisée en cinq différents aspects de `liaison`. Dans cet article, nous allons apprendre ces cinq aspects avec des exemples.

# **Tout d'abord, qu'est-ce que la liaison ?**

En JavaScript, un `Environnement Lexical` est l'endroit où votre code est physiquement écrit. Dans l'exemple ci-dessous, la variable name est `lexicalement` à l'intérieur de la fonction `sayName()`.

```js
function sayName() {
  let name = 'someName';
  console.log('The name is, ', name);
}
```

Un `Contexte d'Exécution` fait référence au code qui est actuellement en cours d'exécution et à tout ce qui aide à l'exécuter. Il peut y avoir beaucoup d'environnements lexicaux disponibles, mais celui qui est _actuellement_ en cours d'exécution est géré par le _[Contexte d'Exécution](https://blog.greenroots.info/understanding-javascript-execution-context-like-never-before-ckb8x246k00f56hs1nefzpysq)_.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/lexical.gif)
_Environnement Lexical vs Contexte d'Exécution_

Chacun des Contexte d'Exécution contient un `Enregistrement d'Environnement`. Lorsque le moteur JavaScript exécute le code, les variables et les noms de fonctions sont ajoutés à l'Enregistrement d'Environnement.

Ce phénomène est connu sous le nom de `Liaison` en JavaScript. La `Liaison` aide à associer les identifiants (variables, noms de fonctions) avec le mot-clé `this` pour un `contexte d'exécution`.

Ne vous inquiétez pas si vous trouvez cela un peu difficile à comprendre maintenant. Vous aurez une meilleure compréhension au fur et à mesure que nous avancerons.

# Règle #1 : Comment fonctionne la liaison implicite en JavaScript

La liaison implicite couvre la plupart des cas d'utilisation pour traiter avec le mot-clé `this`.

Lorsque nous invoquons une méthode d'un objet, nous utilisons la notation par point (.) pour y accéder. Dans la liaison implicite, vous devez vérifier l'objet adjacent à la méthode au moment de l'invocation. Cela détermine à quoi `this` est lié.

Regardons un exemple pour mieux comprendre.

```js
let blog = {
    name: 'Tapas',
    address: 'freecodecamp',
    message: function() {
        console.log(`${this.name} blogs on ${this.address}`);
    }
};

blog.message();
```

Ici, `this` est lié à l'objet blog. Nous le savons parce que nous invoquons la méthode `message()` sur l'objet blog. Donc `this.name` va afficher _Tapas_ et `this.address` va afficher _freeCodeCamp_ dans la console.

Regardons un autre exemple pour mieux comprendre ce concept :

```js
 function greeting(obj) {
      obj.logMessage = function() {
          console.log(`${this.name} is ${this.age} years old!`);
      }
  };

  const tom = {
      name: 'Tom',
      age: 7
  };

  const jerry = {
      name: 'jerry',
      age: 3
  };

  greeting(tom);
  greeting(jerry);

  tom.logMessage ();
  jerry.logMessage ();

```

Dans cet exemple, nous avons deux objets, `tom` et `jerry`. Nous avons décoré (amélioré) ces objets en attachant une méthode appelée `logMessage()`.

Remarquez que lorsque nous invoquons `tom.logMessage()`, elle a été invoquée sur l'objet `tom`. Donc `this` est lié à l'objet `tom` et il affiche la valeur _tom_ et 7 (`this.name` est égal à tom et `this.age` est 7 ici). Le même principe s'applique lorsque `jerry.logMessage()` est invoqué.

# Règle #2 : Comment fonctionne la liaison explicite en JavaScript

Nous avons vu que JavaScript crée un environnement pour exécuter le code que nous écrivons. Il prend en charge la création de mémoire pour les variables, les fonctions, les objets, etc., dans la _phase de création_. Enfin, il exécute le code dans la _phase d'exécution_. Cet environnement spécial est appelé le `Contexte d'Exécution`.

Il peut y avoir de nombreux environnements (Contexte d'Exécution) dans une application JavaScript. Chaque contexte d'exécution fonctionne indépendamment des autres.

Mais parfois, nous pouvons vouloir utiliser des éléments d'un contexte d'exécution dans un autre. C'est là que la liaison explicite entre en jeu.

Dans la liaison explicite, nous pouvons appeler une fonction avec un objet lorsque la fonction est en dehors du contexte d'exécution de l'objet.

Il existe trois méthodes très spéciales, `call()`, `apply()` et `bind()`, qui nous aident à réaliser la liaison explicite.

## Comment fonctionne la méthode `call()` en JavaScript

Avec la méthode `call()`, le contexte avec lequel la fonction doit être appelée sera passé en tant que paramètre à `call()`. Voyons comment cela fonctionne avec un exemple :

```js
let getName = function() {
     console.log(this.name);
 }
 
let user = {
   name: 'Tapas',
   address: 'Freecodecamp'  
 };

getName.call(user);
```

Ici, la méthode `call()` est invoquée sur une fonction appelée `getName()`. La fonction `getName()` se contente d'afficher `this.name`. Mais qu'est-ce que `this` ici ? Cela est déterminé par ce qui a été passé à la méthode `call()`.

Ici, `this` sera lié à l'objet user parce que nous avons passé l'utilisateur en tant que paramètre à la méthode `call()`. Donc `this.name` devrait afficher la valeur de la propriété name de l'objet user, c'est-à-dire _Tapas_.

Dans l'exemple ci-dessus, nous avons passé un seul argument à `call()`. Mais nous pouvons aussi passer plusieurs arguments à `call()`, comme ceci :

```js
let getName = function(hobby1, hobby2) {
     console.log(this.name + ' likes ' + hobby1 + ' , ' + hobby2);
 }

let user = {
   name: 'Tapas',
   address: 'Bangalore'  
 };

let hobbies = ['Swimming', 'Blogging'];
 
getName.call(user, hobbies[0], hobbies[1]);
```

Ici, nous avons passé plusieurs arguments à la méthode `call()`. Le premier argument doit être le contexte de l'objet avec lequel la fonction doit être invoquée. Les autres paramètres peuvent être simplement des valeurs à utiliser.

Ici, je passe _Swimming_ et _Blogging_ comme deux paramètres à la fonction `getName()`.

Avez-vous remarqué un point douloureux ici ? Dans le cas d'un `call()`, les arguments doivent être passés un par un – ce qui n'est pas une manière intelligente de faire les choses ! C'est là que notre prochaine méthode, `apply()`, entre en jeu.

## Comment fonctionne la méthode `apply()` en JavaScript

Cette manière fastidieuse de passer des arguments à la méthode `call()` peut être résolue par une autre méthode alternative appelée `apply()`. Elle est exactement la même que `call()` mais permet de passer les arguments de manière plus pratique. Jetez un coup d'œil :

```js
let getName = function(hobby1, hobby2) {
     console.log(this.name + ' likes ' + hobby1 + ' , ' + hobby2);
 }
 
let user = {
   name: 'Tapas',
   address: 'Bangalore'  
 };

let hobbies = ['Swimming', 'Blogging'];
 
getName.apply(user, hobbies);
```

Ici, nous sommes en mesure de passer un tableau d'arguments, ce qui est beaucoup plus pratique que de les passer un par un.

Astuce : Lorsque vous n'avez qu'un seul argument de valeur ou aucun argument de valeur à passer, utilisez `call()`. Lorsque vous avez plusieurs arguments de valeur à passer, utilisez `apply()`.

## Comment fonctionne la méthode `bind()` en JavaScript

La méthode `bind()` est similaire à la méthode `call()` mais avec une différence. Contrairement à la méthode `call()` qui appelle directement la fonction, `bind()` retourne une toute nouvelle fonction et nous pouvons invoquer celle-ci à la place.

```js
let getName = function(hobby1, hobby2) {
     console.log(this.name + ' likes ' + hobby1 + ' , ' + hobby2);
 }

let user = {
   name: 'Tapas',
   address: 'Bangalore'  
 };

let hobbies = ['Swimming', 'Blogging'];
let newFn = getName.bind(user, hobbies[0], hobbies[1]); 

newFn();
```

Ici, `getName.bind()` n'invoque pas directement la fonction `getName()`. Elle retourne une nouvelle fonction, `newFn` et nous pouvons l'invoquer en tant que `newFn()`.

# Règle #3 : La liaison `new` en JavaScript

Un mot-clé `new` est utilisé pour créer un objet à partir de la fonction constructeur.

```js
let Cartoon = function(name, character) {
     this.name = name;
     this.character = character;
     this.log = function() {
         console.log(this.name +  ' is a ' + this.character);
     }
 };
```

Vous pouvez créer des objets en utilisant le mot-clé `new` comme ceci :

```js
 let tom = new Cartoon('Tom', 'Cat');
 let jerry = new Cartoon('Jerry', 'Mouse');
```

Lorsque une fonction est invoquée avec le mot-clé `new`, JavaScript crée un objet `this` interne (comme, this = {}) dans la fonction. Le `this` nouvellement créé se lie à l'objet en cours de création en utilisant le mot-clé `new`.

Cela semble complexe ? D'accord, décomposons cela. Prenons cette ligne,

```js
let tom = new Cartoon('Tom', 'Cat');
```

Ici, la fonction Cartoon est invoquée avec le mot-clé `new`. Donc le `this` créé en interne sera lié au nouvel objet en cours de création ici, qui est _tom_.

# Règle #4 : Liaison de l'objet global en JavaScript

Que pensez-vous de la sortie du code ci-dessous ? À quoi `this` est-il lié ici ?

```js
let sayName = function(name) {
    console.log(this.name);
};

window.name = 'Tapas';
sayName();
```

Si le mot-clé `this` n'est pas résolu avec l'une des liaisons, `implicite`, `explicite` ou `new`, alors `this` est lié à l'objet `window(global)`.

Il y a une exception cependant. Le mode strict de JavaScript ne permet pas cette liaison par défaut.

```js
"use strict";
function myFunction() {
  return this;
}
```

Dans le cas ci-dessus, `this` est `undefined`.

# Règle #5 : Liaison des éléments d'événement HTML en JavaScript

Dans les gestionnaires d'événements HTML, `this` se lie aux éléments HTML qui reçoivent l'événement.

```html
<button onclick="console.log(this)">Click Me!</button>
```

Voici le journal de sortie dans la console lorsque vous cliquez sur le bouton :

```shell
"<button onclick='console.log(this)'>Click Me!</button>"
```

Vous pouvez changer le style du bouton en utilisant le mot-clé `this`, comme ceci :

```html
<button onclick="this.style.color='teal'">Click Me!</button>
```

Mais soyez attentif lorsque vous appelez une fonction au clic du bouton et utilisez `this` à l'intérieur de cette fonction.

```html
<button onclick="changeColor()">Click Me!</button>
```

et le JavaScript :

```js
function changeColor() {
  this.style.color='teal';
}
```

Le code ci-dessus ne fonctionnera pas comme prévu. Comme nous l'avons vu dans la Règle 4, ici `this` sera lié à l'objet global (en mode 'non-strict') où il n'y a pas d'objet _style_ pour définir la couleur.

# En résumé

Pour résumer,

* Dans le cas de la liaison implicite, `this` se lie à l'objet adjacent à l'opérateur point (.) lors de l'invocation de la méthode.
* Dans le cas de la liaison explicite, nous pouvons appeler une fonction avec un objet lorsque la fonction est en dehors du contexte d'exécution de l'objet. Les méthodes `call()`, `apply()` et `bind()` jouent un grand rôle ici.
* Lorsque une fonction est invoquée avec le mot-clé `new`, le mot-clé `this` à l'intérieur de la fonction se lie au nouvel objet en cours de construction.
* Lorsque le mot-clé `this` n'est pas résolu avec l'une des liaisons, `implicite`, `explicite` ou `new`, alors `this` est lié à l'objet `window(global)`. En mode strict de JavaScript, `this` sera undefined.
* Dans les gestionnaires d'événements HTML, `this` se lie aux éléments HTML qui reçoivent l'événement.

Il y a un autre cas où `this` se comporte différemment, comme avec les fonctions fléchées `ES6`. Nous examinerons cela dans un futur article.

J'espère que vous avez trouvé cet article instructif. Vous pourriez également aimer,

* [JavaScript Hoisting Internals](https://blog.greenroots.info/javascript-hoisting-internals-ckbuavl6f00dllas14hl9ckq1)
* [Understanding JavaScript Execution Context like never before](https://blog.greenroots.info/understanding-javascript-execution-context-like-never-before-ckb8x246k00f56hs1nefzpysq)
* [JavaScript Scope Fundamentals with Tom and Jerry](https://blog.greenroots.info/javascript-scope-fundamentals-with-tom-and-jerry-ckcq723h4007vkxs18dxa97ae)
* [Understanding JavaScript Closure with example](https://blog.greenroots.info/understanding-javascript-closure-with-example-ckd17fci5001iw5s1fju4f8r0)

Si cet article vous a été utile, veuillez le partager afin que d'autres puissent le lire également. Vous pouvez me mentionner sur Twitter ([@tapasadhikary](https://twitter.com/tapasadhikary)) avec des commentaires, ou n'hésitez pas à me suivre.