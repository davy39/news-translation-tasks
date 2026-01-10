---
title: Portée, Fermetures et Hoisting en JavaScript – Expliqué avec des Exemples de
  Code
subtitle: ''
author: Chidera Humphrey
co_authors: []
series: null
date: '2024-06-26T08:13:12.000Z'
originalURL: https://freecodecamp.org/news/scope-closures-and-hoisting-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/How-to-connect-Firebase-Authentication-with-Golang-app_20240625_101105_0000-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Portée, Fermetures et Hoisting en JavaScript – Expliqué avec des Exemples
  de Code
seo_desc: 'In the dynamic world of JavaScript, understanding the intricacies of scope,
  closures, and hoisting is fundamental for mastering the language and building robust
  applications.

  These concepts, though often misunderstood, play a crucial role in determin...'
---

Dans le monde dynamique de JavaScript, comprendre les subtilités de la portée, des fermetures et du hoisting est fondamental pour maîtriser le langage et construire des applications robustes.

Ces concepts, bien que souvent mal compris, jouent un rôle crucial dans la détermination du comportement des variables et des fonctions dans le code.

La portée dicte l'accessibilité des variables, les fermetures permettent des modèles de programmation puissants, et le hoisting peut conduire à des résultats inattendus s'il n'est pas bien compris.

Dans ce guide complet, nous allons plonger profondément dans les domaines de la portée, des fermetures et du hoisting en JavaScript, démêlant leurs complexités, fournissant des exemples pratiques et offrant les meilleures pratiques pour vous aider dans votre parcours en tant que développeur JavaScript.

Alors, attachez vos ceintures alors que nous entreprenons cette exploration éclairante du trio dynamique de JavaScript.

## Table des Matières

* [Prérequis](#prerequisites)
    
* [Portée en JavaScript](#scope-in-javascript)
    
* [Types de portée en JavaScript](#types-of-scope-in-javascript)
    
* [Fermetures](#closures)
    
* [Hoisting](#hoisting)
    
    * [Hoisting de variable](#variable-hoisting)
        
    * [Hoisting de fonction](#function-hoisting)
        
    * [Hoisting de classe](#class-hoisting)
        
    * [Hoisting d'import](#import-hoisting)
        
* [Meilleures pratiques](#best-practices)
    
* [Conclusion](#conclusion)
    

## Prérequis

Vous devez avoir une compréhension de base du langage JavaScript pour suivre cet article.

## Portée en JavaScript

En programmation, la portée fait référence au contexte dans lequel les variables et les fonctions sont déclarées et accessibles.

La portée détermine la visibilité et le cycle de vie de ces variables et fonctions dans un programme, garantissant qu'elles sont utilisées dans le contexte prévu.

En JavaScript, la portée suit le concept de portée lexicale. Dans la portée lexicale, la visibilité des variables et des fonctions est déterminée par le contexte dans lequel les variables et les fonctions sont définies.

## Types de portée en JavaScript

En JavaScript, il existe trois principaux types de portée :

### Portée globale

Les variables et fonctions définies dans la portée globale peuvent être accessibles par n'importe quelle partie du programme. Les variables et fonctions déclarées dans la portée globale sont dites globales.

```js

let globalScopeVariable = "Je suis dans la portée globale";

  

function logScope(){

console.log(globalScopeVariable)

}

logScope(); // Je suis dans la portée globale

  

for(let i=0; i<3; i++){

console.log(globalScopeVariable);

}

// Je suis dans la portée globale

// Je suis dans la portée globale

// Je suis dans la portée globale

  

if(true){

console.log(globalScopeVariable);

}

// Je suis dans la portée globale

  

console.log(globalScopeVariable); // "Je suis dans la portée globale"
```

Dans le code ci-dessus, la variable `globalScopeVariable` peut être accessible par n'importe quelle partie du programme, qu'elle soit à l'intérieur d'une fonction, d'une boucle, d'instructions conditionnelles ou dans la portée globale elle-même.

Vous pouvez penser à la portée globale comme votre supermarché local – tout le monde y a accès.

**Note** : lors de la création d'applications réelles, il est recommandé de minimiser le nombre de variables qui sont globales. Cela permet de réduire l'imprévisibilité dans votre code qui peut conduire à des bugs.

### Portée de fonction

Lorsque des variables et des fonctions sont déclarées dans des fonctions, les variables et les fonctions sont dans la portée de la fonction.

Ces variables et fonctions ne peuvent être accessibles qu'à l'intérieur de la fonction dans laquelle elles ont été déclarées.

Les variables déclarées dans la portée de fonction sont dites à portée de fonction.

```js

function doubleNum(){

let num = 23;

console.log(num * 2)

}

doubleNum(); // 46

  

console.log(num); // Reference error: "num" n'est pas défini
```

Dans le code ci-dessus, l'enregistrement de `num` entraînera une `Reference error` car `num` ne peut être accessible qu'à l'intérieur de la fonction `doubleNum`.

Vous pouvez penser à la portée de fonction comme un message envoyé à un chat de groupe – seuls les participants du groupe peuvent voir et interagir avec le message.

### Portée de bloc

Les accolades, `{}`, désignent un bloc de code. Les variables déclarées à l'intérieur de ces accolades ne peuvent pas être accessibles à l'extérieur des accolades.

```js

{

let blockScopedVariable = "Je suis à portée de bloc";

console.log(blockScopedVariable); // Je suis à portée de bloc

}

  

console.log(blockScopedVariable); // ReferenceError: blockScopedVariable n'est pas défini
```

Dans le code ci-dessus, `blockScopedVariable` ne peut être accessible qu'à l'intérieur des accolades car elle a été définie à l'intérieur des accolades.

Bien que la portée de bloc semble similaire à la portée de fonction, il y a une petite différence.

La différence clé entre la portée de bloc et la portée de fonction est que la portée de fonction fait référence aux variables définies dans les fonctions, tandis que la portée de bloc fait référence aux variables définies dans une paire d'accolades.

Vous pouvez dire que la portée de fonction est un sous-ensemble de la portée de bloc.

**Note** : les variables déclarées dans une fonction en utilisant `var` ne peuvent pas être accessibles à l'extérieur de cette fonction.

```js

function logScope(){

var x = 4;

}

console.log(x); // ReferenceError: x n'est pas défini
```

## Fermetures

Une fermeture est la combinaison d'une fonction et de sa portée lexicale. En d'autres termes, une fermeture est une fonction définie dans une autre fonction qui se souvient de son environnement lexical.

Se souvenir de son environnement lexical signifie que la fonction de fermeture a accès aux variables déclarées dans la fonction parente, même après que la fonction parente a fini de s'exécuter.

```js

function parentFunction(){

let x = 3;

function childFunction(y){

return x + y

}

return childFunction

}

  

let res = parentFunction();

  
  

console.log(res(6));
```

Dans le code ci-dessus, `childFunction` forme une fermeture à l'intérieur de `parentFunction`. `childFunction` a accès aux variables définies dans l'environnement lexical de `childFunction` même après que `parentFunction` a fini de s'exécuter dans `let res = parentFunction()`. C'est pourquoi `console.log(res(6))` donne `9`.

## Hoisting

Le hoisting en JavaScript fait référence au processus par lequel l'interpréteur JavaScript déplace la déclaration de variables, de fonctions, de classes et d'imports en haut du code avant l'exécution.

Vous pouvez voir le hoisting comme des déclarations étant "soulevées" avant l'exécution du code.

### Hoisting de variable

Seules les variables déclarées en utilisant `var` sont hoistées. Cela est dû au fait que `var` n'est pas à portée de bloc, ce qui signifie que la variable déclarée avec `var` peut être référencée n'importe où dans sa portée indépendamment de la position de la déclaration de la variable.

```js

console.log(x); // undefined

var x = 4;
```

L'exécution du code ci-dessus enregistrera `undefined` dans la console. Cela est dû au fait que seules les déclarations de variables sont hoistées ou 'soulevées' et non les initialisations.

Avant l'exécution du code, le code ressemblera à ceci :

```js

var x;

console.log(x);

x = 4
```

**Astuce** : `var x` est la déclaration de variable. `x = 4` est l'initialisation.

Les variables déclarées avec `let` et `const` ne sont pas hoistées. Cela signifie que le fait de se référer aux variables avant la déclaration entraîne une `ReferenceError`.

```js

console.log(y); // ReferenceError: Impossible d'accéder à "y" avant l'initialisation

let y = 3;
```

### Hoisting de fonction

Les fonctions sont hoistées tout comme les variables déclarées avec `var`.

```js

console.log(addNums(1,3)); // 4

  

function addNums(a,b){

return a + b;

}
```

Lors de l'exécution, le code ressemble à ceci :

```js

function addNums(a,b){

return a + b;

}

  

console.log(addNums(1,3));
```

Cependant, il est important de savoir que seules les déclarations de fonctions sont hoistées. Les expressions de fonctions ne sont pas hoistées.

```js

console.log(addNums(1,3)); // ReferenceError: impossible d'accéder à "addNums" avant l'initialisation

  

const addNums = function (a,b) {

return a + b;

}
```

L'exécution du code ci-dessus entraînera une `ReferenceError`.

### Hoisting de classe

Contrairement à la déclaration de fonction, les déclarations de classe ne sont pas hoistées. Cela signifie que vous ne pouvez pas accéder à une classe avant sa déclaration.

```js

new Car(); // ReferenceError: impossible d'accéder à "Car" avant l'initialisation

class Car{}
```

### Hoisting d'import

Les déclarations d'import sont hoistées. Cela signifie que toutes les méthodes et fonctions d'une valeur importée sont accessibles dans un autre module même avant sa déclaration.

```js
const sum = f.add(2+3);

import f from './library/package'
```

Dans le code ci-dessus, les fonctions et méthodes de `f` sont accessibles même si la déclaration vient plus tard.

## Meilleures pratiques

### Gardez la portée aussi locale que possible

Vous devriez garder votre portée aussi locale que possible.

Lors de la création de variables, vous devriez viser à créer les variables là où vous souhaitez les utiliser. Cela est particulièrement vrai si vous allez utiliser les variables dans une ou quelques parties de votre code.

```js
const num = 3;

function addNum(){
	return 2 + num; // 3
}

function multiplyNum(a){
	return 3 * a;
}
```

Dans le code ci-dessus, `num` est utilisé une seule fois, dans la fonction `addNum`. Il est préférable de déclarer `num` à l'intérieur de la fonction `addNum`.

```js
function addNum(){
	const num = 3;
	return 2 + num;
}

// reste du code
```

Pour une meilleure modularité, vous pouvez passer `num` comme argument à la fonction `addNum`.

```js
function addNum(num){
	return 2 + num
}
addNum(3); //5
```

### Utilisez les fermetures pour protéger les données

En programmation, il arrive que vous souhaitiez protéger certaines variables contre l'accès depuis l'extérieur d'un objet. C'est là que les fermetures peuvent être très utiles.

Utilisez les fermetures pour protéger les données privées des fonctions externes et d'autres parties de votre code.

```js
function encapsulateData(){
	const user = {
		name: 'Chidera',
		age: 23
	}
	return updateUserAge(){
		return data.age++;
	}
}

const updateHandler = encapsulateData();
const updatedAge = updateHandler(); // 24
console.log(user); // undefined
```

Dans le code ci-dessus, `updateAge` augmente l'âge de l'utilisateur sans que `user` soit accessible depuis l'extérieur.

### Déclarez les variables et les fonctions avant de les utiliser

Il est recommandé de toujours déclarer les variables avant de les utiliser. Cela aide à éviter l'imprévisibilité et les bugs indésirables dans votre code.

### Utilisez toujours `let` et `const` pour créer des variables

`let` et `const` sont les méthodes standard de déclaration de variables en JavaScript. Elles éliminent le comportement de code imprévisible qui vient avec l'utilisation de `var`.

Il y a presque aucune raison d'utiliser `var` pour déclarer des variables en JavaScript moderne.

## Conclusion

En résumé, les portées déterminent où une variable peut être accessible.

La portée peut être divisée en trois : globale, locale et de bloc.

Les fermetures sont des fonctions à l'intérieur d'une fonction. Les fonctions de fermeture ont accès aux variables de la fonction parente, même après que la fonction parente a retourné. La fermeture est une partie cruciale de JavaScript asynchrone.

Le hoisting rend les variables accessibles même avant leur création.

N'oubliez pas de vous conformer aux meilleures pratiques lorsque vous travaillez avec les fermetures et le hoisting. Déclarer les variables avant leur utilisation et utiliser les fermetures pour encapsuler les données peut aider à prévenir l'imprévisibilité du code et protéger les données privées.