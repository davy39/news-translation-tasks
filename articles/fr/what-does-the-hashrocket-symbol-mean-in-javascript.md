---
title: Que signifie => en JavaScript ? Le symbole égal supérieur à, alias Hashrocket,
  expliqué
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-03-21T22:16:00.000Z'
originalURL: https://freecodecamp.org/news/what-does-the-hashrocket-symbol-mean-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/markus-spiske-AaEQmoufHLk-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Que signifie => en JavaScript ? Le symbole égal supérieur à, alias Hashrocket,
  expliqué
seo_desc: "Prior to the introduction of arrow functions, function expressions in JavaScript\
  \ had a verbose syntax that often made code harder to read and understand. \nAs\
  \ a more concise way of writing function expressions in JavaScript, arrow functions\
  \ were intro..."
---

Avant l'introduction des fonctions fléchées, les expressions de fonction en JavaScript avaient une syntaxe verbeuse qui rendait souvent le code plus difficile à lire et à comprendre. 

Comme moyen plus concis d'écrire des expressions de fonction en JavaScript, les fonctions fléchées ont été introduites dans ECMAScript 6 (ES6). Elles ont rapidement gagné en popularité parmi les développeurs en raison de leur simplicité et de leur lisibilité.

Les fonctions fléchées sont un raccourci pour définir des fonctions en JavaScript, et elles ont une syntaxe unique qui diffère des fonctions traditionnelles. Le symbole => est utilisé pour définir la fonction tandis que le corps de la fonction est entouré d'accolades. Le symbole « => » est connu sous le nom de symbole « égal supérieur à » ou **hashrocket**.

Dans cet article, nous examinerons en profondeur ce que signifie le symbole « **=>** » en JavaScript et comment il est utilisé pour créer des fonctions fléchées. Nous explorerons la syntaxe et la structure des fonctions fléchées, ainsi que leurs avantages. J'espère que vous l'apprécierez.

## Que signifie le symbole « => »

Le symbole « => », également connu sous le nom de symbole égal supérieur à ou **hashrocket**, est une notation raccourcie pour définir des fonctions en JavaScript. Il est utilisé pour créer un nouveau type de fonction appelé fonction fléchée.

Les fonctions fléchées ont une syntaxe plus simple et plus concise que les expressions de fonction traditionnelles. Vous pouvez les utiliser pour définir des fonctions anonymes ou pour passer des fonctions comme arguments à d'autres fonctions.

Voici un exemple basique de l'endroit où le hashrocket est utilisé et de la manière dont il est utilisé.

```js
const square = x => x * x;
```

Le code ci-dessus montre comment le hashrocket est utilisé dans une fonction fléchée qui prend un paramètre et renvoie son carré. 

La fonction fléchée est définie à l'aide du symbole « => », qui possède un paramètre, x. Le corps de la fonction, qui calcule le carré de « x », n'est pas entouré d'accolades et suit l'opérateur fléché. C'est la façon la plus concise d'écrire une fonction fléchée.

Les fonctions fléchées peuvent également avoir plusieurs paramètres entourés de parenthèses et un corps de fonction entouré d'accolades. Voici un exemple d'une fonction fléchée qui prend deux paramètres et renvoie leur somme :

```js
const sum = (a, b) => {
  return a + b;
};

```

Dans le code ci-dessus, la fonction fléchée est définie à l'aide du symbole « **=>** », avec les paramètres « **a** » et « **b** ». Le corps de la fonction, qui calcule la somme de « **a** » et « **b** », est entouré d'accolades et suit le hashrocket.

## Avantages des fonctions fléchées

### Portée lexicale

Les fonctions fléchées en JavaScript ont une portée lexicale (lexical scoping), ce qui signifie qu'elles héritent des variables de leur portée parente. Cette fonctionnalité les rend utiles dans certaines tâches de programmation où vous devez accéder à des variables dans la portée parente.

Voici un exemple simple pour illustrer ce concept :

```js
function outerFunction() {
  var outerVariable = "Hello, ";
  
  function innerFunction(name) {
    var innerVariable = "world!";
    
    var message = () => {
      console.log(outerVariable + name + " " + innerVariable);
    };
    
    return message();
  }
  
  innerFunction("John");
}

outerFunction(); // sortie : "Hello, John world!"
```

Dans cet exemple, nous avons une fonction externe appelée `outerFunction()` qui déclare une variable appelée `outerVariable` et lui assigne la valeur "Hello, ". La fonction externe déclare également une fonction interne appelée `innerFunction(name)`, qui possède sa propre variable `innerVariable` et une fonction fléchée appelée `message()`.

La fonction fléchée `message()` enregistre un message dans la console qui inclut la valeur de `outerVariable`, name (qui est passé comme argument à `innerFunction()`), et `innerVariable`. Lorsque `message()` est appelée, elle a accès à toutes ces variables, même si elles sont définies dans des portées différentes.

Enfin, nous appelons la fonction externe `outerFunction()`, qui à son tour appelle `innerFunction("John")`. Cela entraîne l'enregistrement du message "Hello, John world!" dans la console.

L'exemple montre que la fonction fléchée `message()` a accès aux variables définies dans les fonctions externe et interne, grâce à la **portée lexicale**. Cette fonctionnalité rend les fonctions fléchées utiles pour accéder aux variables dans la portée parente, ce qui peut simplifier le code et le rendre plus lisible.

### Utile pour les callbacks

Les fonctions fléchées sont utiles pour les callbacks. Les fonctions de rappel (callback) sont des fonctions qui sont passées comme arguments à d'autres fonctions. Les fonctions fléchées sont généralement préférées comme fonctions de rappel car elles peuvent être écrites de manière plus concise et plus claire que les expressions de fonction traditionnelles.

Par exemple, considérons ce code qui utilise l'expression de fonction traditionnelle pour filtrer un tableau de nombres :

```js
const numbers = [1, 2, 3, 4, 5];

const filteredNumbers = numbers.filter(function(number) {
  return number % 2 === 0;
});

```

Dans ce code, l'expression de fonction est un peu longue et difficile à lire. Nous pouvons la simplifier en utilisant une fonction fléchée comme illustré ci-dessous.

```js
const numbers = [1, 2, 3, 4, 5];

const filteredNumbers = numbers.filter(number => number % 2 === 0);
```

Dans cette version du code, la fonction fléchée est beaucoup plus courte et plus facile à lire, ce qui en fait un excellent choix pour les callbacks.

## Conclusion

En conclusion, la syntaxe des fonctions fléchées en JavaScript offre un moyen plus concis et plus simple d'écrire des expressions de fonction. Elle simplifie la syntaxe pour les fonctions simples à l'aide du symbole **=>** et facilite la gestion de la portée.

J'espère que cet article vous a été utile. Bon codage !