---
title: Fonctions d'ordre supérieur en JavaScript – Guide du débutant
subtitle: ''
author: Soham De Roy
co_authors: []
series: null
date: '2022-06-09T19:59:00.000Z'
originalURL: https://freecodecamp.org/news/higher-order-functions-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Blog-8
seo_title: Fonctions d'ordre supérieur en JavaScript – Guide du débutant
---

Freecodecamp-Banner-new.png
tags:
- name: guide des débutants
  slug: guide-des-debutants
- name: JavaScript
  slug: javascript
- name: Développement Web
  slug: developpement-web
seo_title: null
seo_desc: "En JavaScript, les fonctions sont traitées comme des citoyens de première classe. Nous pouvons traiter les fonctions comme des valeurs et les assigner à une autre variable, les passer comme arguments à une autre fonction, ou même les retourner depuis une autre fonction. Cette capacité des fonctions à agir comme des fonctions de première classe est ce qui alimente les fonctions d'ordre supérieur en JavaScript. Une fonction qui prend une autre fonction comme argument ou retourne une fonction est connue comme une fonction d'ordre supérieur. Let's deep dive a bit to see both types of implementation, that is:

- Passing a function as an argument to another function
- Returning a function from another function

![Image](https://www.freecodecamp.org/news/content/images/2022/06/63eec0636ec9b999bf8c5ee5340dd54a_w200.gif)

## Comment passer une fonction comme argument à une autre fonction

Dans cette section, nous verrons comment nous pouvons envoyer une fonction comme argument et finalement comment cela nous aide à écrire un code plus propre.

Considérons le code suivant dans lequel nous voulons créer une fonction qui accepte un tableau comme argument. Elle filtre tous les nombres impairs et retourne tous les nombres filtrés. 

La fonction ressemblera à ceci:

```javascript
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];

function filterOdd(arr) {
  const filteredArr = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 !== 0) {
      filteredArr.push(arr[i]);
    }
  }
  return filteredArr;
}
console.log(filterOdd(arr));

// Output:
// [ 1, 3, 5, 7, 9, 11 ]
```

La fonction ci-dessus retourne le tableau filtré `[ 1, 3, 5, 7, 9, 11 ]` où nous avons tous les nombres impairs, comme prévu.

Maintenant, disons que nous voulons également créer une fonction qui filtre et retourne tous les nombres pairs. Nous pouvons très bien créer la fonction suivante pour y parvenir:

```javascript
function filterEven(arr) {
  const filteredArr = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 == 0) {
      filteredArr.push(arr[i]);
    }
  }
  return filteredArr;
}
console.log(filterEven(arr));

// Output:
// [ 2, 4, 6, 8, 10 ]
```

Encore une fois, comme prévu, nous obtiendrons le résultat souhaité d'un tableau avec tous les nombres pairs `[ 2, 4, 6, 8, 10 ]`. 

Mais remarquez que nous écrivons beaucoup de code dupliqué dans cette approche. Les deux fonctions ci-dessus font beaucoup de choses communes, comme accepter le tableau original, créer un nouveau tableau pour stocker le tableau filtré, parcourir tout le tableau principal, et enfin retourner le tableau filtré. 

La seule différence entre les deux fonctions est la logique qu'elles utilisent pour filtrer le tableau original. 

Pour la fonction `filterOdd`, nous utilisons la logique `arr[i] % 2 !== 0` tandis que dans la fonction `filterEven`, nous utilisons la logique `arr[i] % 2 == 0` pour filtrer le tableau original. 

C'est là que nous pouvons bénéficier de l'utilisation des fonctions d'ordre supérieur. L'intention principale est de créer une fonction pour faire toutes les choses communes que nous avons faites dans les deux fonctions ci-dessus et de passer la partie logique séparément comme argument à cette fonction. Voyons comment nous pouvons implémenter cela.

Créons la fonction qui fait toutes les choses communes que nous avons effectuées dans les fonctions `filterOdd` et `filterEven`. Cela ressemblera à ceci:

```javascript
function filterFunction(arr, callback) {
  const filteredArr = [];
  for (let i = 0; i < arr.length; i++) {
    callback(arr[i]) ? filteredArr.push(arr[i]) : null;
  }
  return filteredArr;
}
```

Ignorez le paramètre `callback` pour l'instant. Remarquez comment dans la nouvelle `filterFunction`, nous avons gardé toutes les étapes communes, c'est-à-dire accepter le tableau original, créer un nouveau tableau pour stocker le tableau filtré, parcourir tout le tableau principal, et enfin retourner le tableau filtré que nous effectuions dans les fonctions `filterOdd` et `filterEven`.

Maintenant, le paramètre `callback` accepte essentiellement la logique qui ne sera rien d'autre qu'une autre fonction contenant la logique de filtrage. Pour filtrer les nombres impairs et pairs, respectivement, voici les fonctions de logique que nous devons écrire:

```javascript
// Fonction contenant la logique pour filtrer les nombres impairs

function isOdd(x) {
  return x % 2 != 0;
}

// Fonction contenant la logique pour filtrer les nombres pairs

function isEven(x) {
  return x % 2 === 0;
}
```

C'est tout! Nous devons maintenant simplement passer le tableau principal, ainsi que la fonction de logique à notre `filterFunction` comme ceci:

```javascript
// Pour filtrer les nombres impairs

filterFunction(arr, isOdd)
// Output de console.log(filterFunction(arr, isOdd)):
// [ 1, 3, 5, 7, 9, 11 ]

// Pour filtrer les nombres pairs

filterFunction(arr, isEven)
// Output de console.log(filterFunction(arr, isEven)):
// [ 2, 4, 6, 8, 10 ]
```

De cette manière, nous passons des fonctions de logique comme `isOdd` ou `isEven` comme arguments à une autre fonction `filterFunction`. 

Nous abstraisons essentiellement la logique de filtrage principale de la fonction principale. Nous pouvons maintenant passer toute autre logique de filtrage comme nous le souhaitons à `filterFunction` sans avoir besoin de la changer.

Par exemple, si nous voulons filtrer un nombre supérieur à 5, nous devons simplement écrire la logique de filtrage suivante:
```javascript
function isGreaterThanFive(x) {
  return x > 5;
}
```

et la passer comme argument à `filterFunction`:

```javascript
filterFunction(arr, isGreaterThanFive)

// Output de console.log(filterFunction(arr, isGreaterThanFive)):
// [ 6, 7, 8, 9, 10, 11 ]
```

Nous pouvons également passer la fonction de logique comme une fonction fléchée et obtenir le même résultat – c'est-à-dire, passer `(x) => x > 5)` à la place de `isGreaterThanFive` nous donnera le même résultat.

```javascript
filterFunction(arr, (x) => x > 5)

// Output de console.log(filterFunction(arr, (x) => x > 5)):
// [ 6, 7, 8, 9, 10, 11 ]
```

### Comment créer des polyfills

Nous savons que JavaScript nous fournit certaines fonctions d'ordre supérieur intégrées comme `map()`, `filter()`, `reduce()` et ainsi de suite. Pouvez-nous recréer notre propre implémentation de ces fonctions? Approfondissons un peu plus.

Nous avons déjà créé notre fonction de filtrage dans la section ci-dessus. Créons un prototype de tableau de notre fonction `filterFunction` afin que nous puissions l'utiliser avec n'importe quel tableau. Cela ressemblera à ceci:

```javascript
Array.prototype.filterFunction = function (callback) {
  const filteredArr = [];
  for (let i = 0; i < this.length; i++) {
    callback(this[i]) ? filteredArr.push(this[i]) : null;
  }
  return filteredArr;
};
```

Dans le code ci-dessus, `this` fait référence au tableau sur lequel le prototype est appelé. Donc si nous écrivons quelque chose comme:

```javascript
const arr = [1, 2, 3, 4, 5]
arr.filterFunction(callbackFn)
```

alors `this` ferait référence au tableau `arr`.

Maintenant, nous pouvons utiliser `filterFunction` tout comme nous utilisons la fonction intégrée `filter()` en JS. Nous pouvons écrire quelque chose comme ceci:

```javascript
arr.filterFunction(isEven)
```

ce qui est similaire à l'appel de la fonction intégrée `filter()`:

```javascript
arr.filter(isEven)
```

Les deux appels de fonction ci-dessus (c'est-à-dire `arr.filterFunction(isEven)` et `arr.filter(isEven)`) nous donneront la même sortie, comme `[ 2, 4, 6, 8, 10 ]`. 

De même, nous pouvons également passer une fonction fléchée dans notre implémentation de prototype comme nous pouvons le faire dans la fonction intégrée `filter()`.

```javascript
// I
arr.filterFunction((x) => x % 2 != 0)
arr.filter((x) => x % 2 != 0)
// les deux donnent la même sortie sur console.log: [ 1, 3, 5, 7, 9, 11 ]

// II
arr.filterFunction((x) => x > 5)
arr.filter((x) => x > 5)
// les deux donnent la même sortie sur console.log: [ 6, 7, 8, 9, 10, 11 ]

```

D'une certaine manière, nous avons écrit un polyfill pour la fonction intégrée `filter()`.

### Chaînage de fonctions

Nous pouvons également implémenter le chaînage de fonctions avec notre implémentation de prototype comme nous pouvons le faire avec la fonction intégrée `filter()`. Filtrons d'abord tous les nombres supérieurs à 5. Ensuite, à partir du résultat, nous filtrerons tous les nombres pairs. Cela ressemblera à ceci:

```javascript
// Utilisation de notre propre implémentation de prototype filterFunction()
arr.filterFunction((x) => x > 5).filterFunction((x) => x % 2 === 0)

// Utilisation de l'implémentation intégrée filter()
arr.filter((x) => x > 5).filter((x) => x % 2 === 0)

// les deux donnent la même sortie sur console.log: [ 6, 8, 10 ]
```

C'est ainsi que nous pouvons utiliser les fonctions d'ordre supérieur en JS pour écrire un code plus modulaire, plus propre et plus maintenable.

Ensuite, voyons comment nous pouvons retourner une fonction depuis une autre fonction.


![Image](https://www.freecodecamp.org/news/content/images/2022/06/lets-move-on-proceed.gif)

## Comment retourner une fonction depuis une autre fonction en JavaScript

Nous pouvons retourner une fonction depuis une autre fonction parce que nous traitons les fonctions en JavaScript comme des valeurs. Voyons cela à travers un exemple:

```javascript
function calculate(operation) {
  switch (operation) {
    case "ADD":
      return function (a, b) {
        console.log(`${a} + ${b} = ${a + b}`);
      };
    case "SUBTRACT":
      return function (a, b) {
        console.log(`${a} - ${b} = ${a - b}`);
      };
  }
}
```
Dans le code ci-dessus, lorsque nous invoquons la fonction `calculate` avec un argument, elle bascule sur cet argument et retourne finalement une fonction anonyme. Donc si nous appelons la fonction `calculate()` et stockons son résultat dans une variable et le journalisons, nous obtiendrons la sortie suivante:

```javascript
const calculateAdd = calculate("ADD");
console.log(calculateAdd);

// Output: 
// [Function (anonymous)]
```

Vous pouvez voir que `calculateAdd` contient une fonction anonyme que la fonction `calculate()` a retournée.

Il y a deux façons d'appeler cette fonction interne que nous allons explorer maintenant.

### Appeler la fonction retournée en utilisant une variable

Dans cette méthode, nous avons stocké la fonction de retour dans une variable comme montré ci-dessus, puis nous avons invoqué la variable pour à son tour invoquer la fonction interne. 

Voyons cela en code:

```javascript
const calculateAdd = calculate("ADD");
calculateAdd(2, 3);
// Output: 2 + 3 = 5


const calculateSubtract = calculate("SUBTRACT");
calculateSubtract(2, 3);
// Output: 2 - 3 = -1
```

Alors, qu'avons-nous fait ici?

* Nous avons appelé la fonction `calculate()` et passé `ADD` comme argument
* Nous avons stocké la fonction anonyme retournée dans la variable `calculateAdd`, et 
* Nous avons invoqué la fonction interne retournée en appelant `calculateAdd()` avec les arguments requis. 

### Appeler la fonction retournée en utilisant des doubles parenthèses

C'est une manière très sophistiquée d'appeler la fonction interne retournée. Nous utilisons des doubles parenthèses `()()` dans cette méthode. 

Voyons cela en code:

```javascript
calculate("ADD")(2, 3);
// Output: 2 + 3 = 5

calculate("SUBTRACT")(2, 3);
// Output: 2 - 3 = -1
```

Vous pouvez penser à cela de manière similaire à notre exemple de chaînage ci-dessus. C'est juste qu'au lieu de chaîner des fonctions, nous chaînons les arguments. 

Les arguments dans les premières parenthèses appartiennent à la fonction externe, tandis que les arguments dans les secondes parenthèses appartiennent à la fonction interne retournée. 

La méthode `calculate()` retourne une fonction comme expliqué précédemment, et c'est cette fonction retournée qui est immédiatement appelée en utilisant les secondes parenthèses. 

Comme je l'ai mentionné ci-dessus, c'est une manière très sophistiquée d'appeler une fonction. Mais une fois que vous en avez l'habitude, cela devient... eh bien, assez naturel.

Un endroit où nous pouvons voir ce type de notation à doubles parenthèses est dans la méthode `connect` de la bibliothèque de gestion d'état `redux`. Vous pouvez en lire plus sur `connect` [ici](https://react-redux.js.org/api/connect).

## Résumé

Dans cet article, nous avons appris: 
- Pourquoi les fonctions sont appelées citoyens de première classe en JS
- Quelles sont les fonctions d'ordre supérieur
- Comment passer une fonction comme argument à une autre fonction 
- Comment créer un prototype de tableau, le chaînage de fonctions, écrire notre propre polyfill pour la méthode filter() intégrée
- Comment retourner une fonction depuis une autre fonction et différentes façons d'appeler la fonction retournée

## Conclusion

Merci d'avoir lu! J'espère vraiment que vous avez trouvé cet article sur les fonctions d'ordre supérieur utile. Restez à l'écoute pour plus de contenu amazing. Peace out! 🖖

## Liens sociaux

- [LinkedIn](https://www.linkedin.com/feed/)
- [Site Web](https://www.sohamderoy.dev/)
- [Site de blog](https://blog.sohamderoy.dev/)

![Image](https://www.freecodecamp.org/news/content/images/2022/06/e2bd7ce3fc5f2783f1e210b015cc5fb1.gif)