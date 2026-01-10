---
title: Qu'est-ce qu'une Fonction ? Exemples de Fonctions en JavaScript
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-07T23:46:55.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-function-javascript-function-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/blake-connally-B3l0g6HLxr8-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce qu'une Fonction ? Exemples de Fonctions en JavaScript
seo_desc: 'Functions are one of the main parts of computer programs.

  They are widely used and are one of JavaScript''s fundamental building blocks.

  In this article, we''ll go over the definition of functions and why they are so
  important. I''ll also show you how t...'
---

Les fonctions sont l'une des principales parties des programmes informatiques.

Elles sont largement utilisées et constituent l'un des éléments fondamentaux de JavaScript.

Dans cet article, nous allons passer en revue la définition des fonctions et pourquoi elles sont si importantes. Je vais également vous montrer comment commencer à écrire des fonctions en JavaScript.

Plongeons-nous dans le sujet !

## Qu'est-ce qu'une fonction en JavaScript ?

Une fonction est un bloc de code qui encapsule un comportement isolé et autonome que l'ordinateur doit exécuter.

Les fonctions sont un ensemble d'instructions organisées qui correspondent à une certaine tâche ou à une fonctionnalité spécifique qu'un utilisateur souhaite implémenter dans son programme pour atteindre un résultat souhaité.

Le code à l'intérieur d'une fonction ne s'exécute que lorsqu'il est nécessaire, c'est-à-dire uniquement lorsqu'il est *appelé*.

Les fonctions sont une partie importante et utile de la programmation car elles créent un code réutilisable.

Au lieu de copier, coller et répéter le même code dans différentes parties de votre programme, vous pouvez écrire ce code en un seul endroit en utilisant une fonction. Ensuite, vous pouvez l'utiliser encore et encore chaque fois que vous en avez besoin.

Cela aide également lorsque vous souhaitez apporter des modifications à votre programme ou le déboguer et essayer de corriger une erreur.

Au lieu de chercher les différentes parties où votre code pourrait se trouver, vous n'avez qu'à regarder un seul endroit particulier, ce qui rend votre code plus lisible.

## Comment déclarer des fonctions en JavaScript

La syntaxe générale pour créer une fonction en JavaScript ressemble à ceci :

```Javascript
function nom(paramètre1, paramètre2, ...) {
    // les instructions de code à exécuter
}
```

Décomposons cela :

- Vous déclarez une fonction avec le mot-clé `function`.
- Ensuite, vous donnez un nom de votre choix à la fonction. Les noms de fonctions en JavaScript sont sensibles à la casse et une convention et meilleure pratique est d'utiliser le `camelCase`.
- Le nom de la fonction est suivi d'une paire de parenthèses ouvrante et fermante.

Les fonctions peuvent prendre des données en acceptant des *entrées*. Ces entrées sont enfermées dans les parenthèses et sont appelées *paramètres*.

Les paramètres agissent comme des variables de remplacement locales pour les valeurs qui seront passées à la fonction en tant qu'entrées lorsque la fonction est appelée. Ils sont entièrement optionnels et s'il y en a plus d'un, vous les séparez par une virgule.
- Enfin, viennent les accolades, et à l'intérieur, le corps principal de la fonction avec les instructions de code à exécuter lorsque la fonction est appelée. C'est ici que les entrées de la fonction sont traitées.

### Comment déclarer et appeler une fonction simple en JavaScript

```javascript

function salutation() {
  console.log('Bonjour le Monde !');
}
```

Ci-dessus, nous avons créé une fonction appelée `salutation`.

Cette fonction est très basique et vous ne pouvez pas faire grand-chose avec elle. Elle ne prend aucune entrée et la seule chose qui se passe est que le texte `Bonjour le Monde !` est imprimé dans la console.

Définir une fonction en soi ne fait pas s'exécuter le code à l'intérieur du corps de la fonction. Pour que le code soit exécuté, et afin de voir ce message dans la console, la fonction doit être appelée. Cela s'appelle également une *invocation de fonction*.

Pour appeler une fonction qui n'accepte pas d'entrées, vous écrivez simplement le nom de la fonction suivi de parenthèses et d'un point-virgule à la fin.

```javascript
salutation();

//sortie
//Bonjour le Monde !
```

Maintenant, vous pouvez réutiliser cette fonction plusieurs fois en appelant simplement la fonction elle-même plusieurs fois. Cela vous aide à éviter de répéter le code :

```javascript
salutation();
salutation();
salutation();

//sortie
// Bonjour le Monde !
// Bonjour le Monde !
// Bonjour le Monde !
```


### Comment déclarer et appeler des fonctions avec des paramètres en JavaScript

Nous pouvons modifier l'exemple précédent pour accepter des entrées. Nous allons le faire avec des paramètres, comme mentionné précédemment.

Les paramètres sont des valeurs que vous passez à la fonction lorsque la fonction est *déclarée*.

```javascript
function salutation(nom) {
  console.log('Bonjour ' + nom + ' !' );
}
```

La fonction nommée `salutation` accepte maintenant un paramètre, `nom`. Cette chaîne est concaténée (`+`) avec la chaîne `Bonjour ` et un point d'exclamation à la fin.

Lors de l'appel de fonctions qui acceptent des paramètres, vous devez passer des arguments.

Les arguments sont des valeurs que vous fournissez lors de l'appel de la fonction et ils correspondent aux paramètres qui ont été passés dans la ligne de déclaration de la fonction.

Par exemple :

```javascript
salutation('Jenny');
//Sortie
// Bonjour Jenny !
```

L'argument est la valeur `Jenny` et vous pouvez le considérer comme `nom = 'Jenny'`. `nom`, le paramètre, est la variable de remplacement, et `Jenny` est la valeur que vous passez lorsque vous appelez la fonction.

Les fonctions peuvent accepter plus d'un paramètre et peuvent également retourner des données à l'utilisateur du programme :


```javascript
function additionnerNombres(num1, num2) {
    return num1 + num2;
}
```

Le code ci-dessus a créé une fonction nommée `additionnerNombres` qui prend deux paramètres – `num1` et `num2`, séparés par une virgule.

De la même manière que les fonctions ont des entrées, elles ont également des *sorties*.

La fonction *retourne* comme sortie la somme de `num1` et `num2`. Cela signifie qu'elle traite les deux paramètres, effectue le calcul demandé et retourne la valeur finale comme résultat à l'utilisateur.

Lorsque la fonction est appelée, deux arguments doivent être passés puisque la fonction accepte deux paramètres :

```javascript
additionnerNombres(10, 20);
//Sortie
// 30
// pensez à cela comme num1 = 10 et num2 = 20
```

Chaque fois que la fonction est appelée, vous pouvez passer différents arguments :

```javascript
additionnerNombres(2, 2);
// 4
additionnerNombres(3, 15);
//18
```

### Portée des variables dans les fonctions JavaScript

La portée des variables fait référence à la *visibilité* des variables pour différentes parties du programme.

Une variable définie *à l'extérieur* et *avant* un bloc de fonction a une portée globale et peut être accessible depuis l'intérieur d'une fonction :

```javascript
const num = 7;

function maFonction() {
  console.log(num);
}

//Accéder à la variable avec une portée globale depuis n'importe quel endroit dans le programme :
console.log(num);
//Sortie
//7

//Appeler la fonction avec la variable ayant une portée globale
maFonction();
//Sortie
// 7
```

Mais si cette variable était définie *à l'intérieur* de la fonction, elle aurait une portée locale et serait limitée et visible uniquement dans la fonction où elle a été définie.

Vous ne pouvez pas y accéder depuis l'extérieur de la fonction :

```javascript
function maFonction() {
  const num = 7;
  console.log(num);
}

// Essayer d'accéder à la variable avec une portée locale depuis l'extérieur de la portée de la fonction :
console.log(num);
//Sortie :
//Uncaught ReferenceError: num is not defined

//Appeler la fonction avec la variable définie à l'intérieur de la fonction :
maFonction();
//Sortie
//7
```

### Expressions de fonction

Vous pouvez également créer des fonctions en utilisant des expressions.

Ces fonctions sont créées à l'intérieur d'une expression au lieu d'être créées avec une déclaration de fonction comme vous l'avez vu jusqu'à présent.

```javascript
const nom = function(premierNom) {
  return 'Bonjour ' + premierNom ;
  }
```

Ici, nous utilisons la variable `nom` pour stocker la fonction.

Pour appeler la fonction, vous utilisez le nom de la variable comme ceci :

```javascript
console.log(nom('Jenny'));
//Sortie
//"Bonjour Jenny"
```

Ce type de fonction est également appelé une fonction anonyme car elles n'ont pas besoin de nom.

Les différences entre une fonction nommée et une fonction anonyme sont listées ci-dessous :

```javascript

//nommée
function nom(premierNom) {
    console.log('Bonjour ' + premierNom);
 }
 
nom('Jenny');
 
//anonyme
const nom = function(premierNom) {
  return 'Bonjour ' + premierNom ;
  }
 console.log(nom('Jenny'));
```

Les variables dans les fonctions anonymes peuvent également être utilisées comme valeurs pour d'autres variables :

```javascript
const nom = function(premierNom) {
  return 'Bonjour ' + premierNom ;
  }
  
const monNom = nom('Timmy');
console.log(monNom);
//Sortie
//"Bonjour Timmy"
```

## Conclusion

Et voilà ! Cela marque la fin de notre introduction aux fonctions JavaScript et à certaines des façons de les créer.

Si vous souhaitez en apprendre davantage, les [fonctions fléchées](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) sont un nouveau moyen plus efficace de créer des fonctions en JavaScript et elles ont été introduites avec ES6.

Si vous souhaitez commencer à apprendre les fondamentaux de JavaScript de manière interactive et acquérir une compréhension approfondie du langage tout en construisant des projets, freeCodeCamp propose une certification gratuite [JavaScript Algorithms and Data Structures Certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/).

Merci d'avoir lu et bon apprentissage !