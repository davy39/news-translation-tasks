---
title: Comment utiliser les callbacks et les fonctions d'ordre supérieur en JavaScript
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2024-01-12T18:07:08.000Z'
originalURL: https://freecodecamp.org/news/callbacks-higher-order-functions-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/higher-order-callbacks.png
tags:
- name: callbacks
  slug: callbacks
- name: functions
  slug: functions
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les callbacks et les fonctions d'ordre supérieur en JavaScript
seo_desc: The way functions are treated and used in JavaScript is quite interesting.
  They are very flexible – we can assign functions as a value to a variable, return
  them as a value from another function, and pass them as an argument to another function.
  We c...
---

La manière dont les fonctions sont traitées et utilisées en JavaScript est assez intéressante. Elles sont très flexibles – nous pouvons assigner des fonctions comme valeur à une variable, les retourner comme valeur d'une autre fonction, et les passer comme argument à une autre fonction. Nous pouvons faire tout cela parce que JavaScript traite les fonctions comme des **citoyens de première classe**.

Dans cet article, je vais expliquer ce que sont les fonctions d'ordre supérieur et les callbacks, et comment elles fonctionnent en JavaScript.

## Les fonctions comme citoyens de première classe en JavaScript

Les fonctions sont définies comme des [citoyens de première classe](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function) ou objets de première classe en JavaScript parce que les fonctions sont traitées comme des variables.

Cela signifie que les fonctions en JavaScript peuvent être :

* Passées comme argument à une autre fonction.
* Assignées comme valeur à une variable.
* Retournées comme valeur d'une fonction.

Il est essentiel de comprendre comment les fonctions sont traitées en JavaScript, car elles servent de base pour comprendre les fonctions d'ordre supérieur et les callbacks en JavaScript et comment elles fonctionnent.

## Qu'est-ce que les fonctions d'ordre supérieur ?

Les fonctions d'ordre supérieur sont des fonctions qui prennent des fonctions comme arguments et retournent également une fonction comme valeur.

Il existe de nombreuses fonctions d'ordre supérieur intégrées fournies en JavaScript. Nous allons examiner certaines d'entre elles et tirer parti de la manière dont les fonctions sont traitées comme des citoyens de première classe. Nous allons également créer nos propres fonctions d'ordre supérieur.

Tout d'abord, examinons quelques exemples de fonctions d'ordre supérieur intégrées.

### Méthodes de tableau

Les méthodes de tableau sont généralement la première introduction des fonctions d'ordre supérieur qu'un développeur aura lors de l'apprentissage de JavaScript. Celles-ci incluent, sans s'y limiter, les méthodes de tableau `map`, `filter`, `forEach`, `find`, `findIndex`, `some`, et `every` fournies par JavaScript.

Ces méthodes ou fonctions de tableau ont beaucoup en commun, mais l'une des caractéristiques les plus courantes est qu'elles acceptent toutes une fonction comme argument. Voici un extrait de code qui démontre comment la méthode de tableau `forEach` fonctionne :

```javascript
const people = [
  { firstName: "Jack", year: 1988 },
  { name: "Kait", year: 1986 },
  { name: "Irv", year: 1970 },
  { name: "Lux", year: 2015 },
];

people.forEach(function (person) {
  console.log(person);
});

// Sortie : Affiche chaque objet personne dans le tableau
```

À partir de l'exemple de code ci-dessus, nous pouvons voir que la méthode `forEach` accepte une fonction comme argument qu'elle appelle à chaque itération sur le tableau. Par conséquent, la méthode de tableau `forEach` est une fonction d'ordre supérieur.

### Événements de temporisation

Un autre ensemble de fonctions d'ordre supérieur intégrées couramment utilisées sont les fonctions `setInterval` et `setTimeout`, connues sous le nom d'événements de temporisation en JavaScript.

Chaque fonction accepte une fonction comme l'un de ses arguments et l'utilise pour créer un événement temporisé.

Regardez l'exemple de code ci-dessous pour voir comment `setTimeout` fonctionne :

```javascript
setTimeout(function () {
  console.log("Ceci est une fonction d'ordre supérieur");
}, 1000);

// Sortie : "Ceci est une fonction d'ordre supérieur" après 1000ms / 1 seconde
```

L'extrait de code ci-dessus est l'exemple le plus basique de comment une fonction `setTimeout` fonctionne. Elle accepte une fonction et une durée en millisecondes et exécute la fonction après que la durée fournie se soit écoulée.

Dans l'exemple ci-dessus, `Ceci est une fonction d'ordre supérieur` est imprimé dans la console après 1000 ms, ou une seconde.

```javascript
setInterval(function () {
  console.log("Ceci est une fonction d'ordre supérieur");
}, 1000);

// Sortie : "Ceci est une fonction d'ordre supérieur" toutes les 1000ms / 1 seconde
```

La fonction `setInterval` est similaire à la fonction `setTimeout`, tout comme les méthodes de tableau – bien qu'elle fonctionne différemment. Mais nous pouvons voir un schéma commun : elle accepte également une fonction comme l'un de ses paramètres.

Contrairement à `setTimeout` (qui exécute la fonction après que la durée fournie se soit écoulée), `setInterval` exécute la fonction encore et encore toutes les 1000ms ou 1 seconde.

### Comment créer et utiliser une fonction d'ordre supérieur

Les fonctions d'ordre supérieur ne sont pas limitées à celles intégrées fournies par JavaScript.

Puisque les fonctions en JavaScript sont traitées comme des objets de première classe, nous pouvons tirer parti de ce comportement et construire des fonctions hautement performantes et réutilisables.

Dans les exemples ci-dessous, nous allons construire quelques fonctions. Elles accepteront le nom d'un client et une salutation, puis imprimeront ces informations dans la console.

Tout d'abord, voici une fonction simple qui fait ces deux choses :

```js
function greetCustomer(firstName, lastName, salutation) {
  const fullName = `${firstName} ${lastName}`;

  console.log(`${salutation} ${fullName}`);
}

greetCustomer("Franklin", "Okolie", "Bonjour");

// Sortie : "Bonjour Franklin Okolie"
```

`greetCustomer` accepte 3 arguments : un prénom, un nom de famille et une salutation. Ensuite, elle imprime une salutation au client dans la console.

Mais il y a un problème avec cette fonction – elle fait deux choses : composer le nom complet du client et aussi imprimer la salutation.

Ce n'est pas une bonne pratique, car les fonctions doivent faire une seule chose et bien la faire. Nous allons donc refactoriser notre code.

Une autre fonction devrait composer le nom du client afin que la fonction `greetCustomer` n'ait qu'à imprimer la salutation dans la console. Écrivons donc une fonction qui gère cela :

```js
function composeName(firstName, lastName) {
  const fullName = `${firstName} ${lastName}`;

  return fullName;
}
```

Maintenant que nous avons une fonction qui combine le prénom et le nom de famille du client, nous pouvons utiliser cette fonction dans `greetCustomer` :

```js
function greetCustomer(composerFunc, firstName, lastName, salutation) {
  const fullName = composerFunc(firstName, lastName);

  console.log(`${salutation} ${fullName}`);
}

greetCustomer(composeName, "Franklin", "Okolie", "Bonjour");

// Sortie : "Bonjour Franklin Okolie"
```

Maintenant, cela semble plus propre, et chaque fonction fait une seule chose. La fonction `greetCustomer` accepte maintenant 4 arguments, et puisque l'un de ces arguments est une fonction, c'est maintenant une fonction d'ordre supérieur.

Vous vous êtes peut-être demandé plus tôt, comment une fonction est invoquée à l'intérieur d'une autre fonction, et pourquoi ?

Maintenant, nous allons plonger profondément dans l'invocation de fonction et répondre à ces deux questions.

### Retourner une fonction comme valeur

Rappelez-vous que les fonctions d'ordre supérieur prennent soit une fonction comme paramètre et/ou retournent une fonction comme valeur.

Refactorisons la fonction `greetCustomer` pour utiliser moins d'arguments et retourner une fonction :

```js
function getGreetingsDetails(composerFunc, salutation) {
  return function greetCustomer(firstName, lastName) {
    const fullName = composerFunc(firstName, lastName);

    console.log(`${salutation} ${fullName}`);
  };
}
```

La dernière version de `greetCustomer` acceptait trop d'arguments. Quatre arguments, ce n'est pas beaucoup, mais ce serait toujours frustrant si vous mélangiez l'ordre des arguments. En général, moins vous avez d'arguments, mieux c'est.

Dans l'exemple ci-dessus, nous avons une fonction appelée `getGreetingDetails` qui accepte `composerFunc` et `salutation` au nom de la fonction interne `greetCustomer`. Elle retourne ensuite la fonction interne `greetCustomer`, qui elle-même accepte `firstName` et `lastName` comme arguments.

En faisant cela, `greetCustomer` a moins d'arguments au total.

Et avec cela, voyons comment utiliser la fonction `getGreetingDetails` :

```js
const greet = getGreetingsDetails(composeName, "Bonne année !");

greet("Quincy", "Larson");

// Sortie : "Bonne année Quincy Larson"
```

Maintenant, faites un pas en arrière et admirez cette belle abstraction. Magnifique ! Nous avons utilisé la magie des fonctions d'ordre supérieur pour simplifier la fonction `greetCustomer`.

Passons en revue comment tout fonctionne. La fonction d'ordre supérieur nommée `getGreetingDetails` prend deux arguments : une fonction pour composer le prénom et le nom de famille du client, et une salutation. Ensuite, elle retourne une fonction nommée `greetCustomer` qui accepte le prénom et le nom de famille d'un client comme arguments.

La fonction `greetCustomer` retournée utilise également l'argument accepté par `getGreetingDetails` pour exécuter certaines actions.

À ce stade, vous vous demandez probablement, comment une fonction retournée peut-elle utiliser les arguments fournis à une fonction parente ? Surtout étant donné le fonctionnement du contexte d'exécution des fonctions. C'est possible grâce aux [closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures). Apprenons-en plus à leur sujet maintenant.

### Explication des closures

Une closure est une fonction qui a accès à la variable dans la portée où elle a été créée, même après que la portée n'existe plus dans le contexte d'exécution. C'est l'un des mécanismes sous-jacents des callbacks, car les callbacks peuvent encore référencer et utiliser des variables créées dans une fonction externe après que cette fonction externe ait été fermée.

Prenons un exemple rapide :

```js
function getTwoNumbers(num1, num2) {
  return function add() {
    const total = num1 + num2;
    console.log(total);
  };
}

const addNumbers = getTwoNumbers(5, 2);

addNumbers();

//Sortie: 7;
```

Le code de cet exemple définit une fonction appelée `getTwoNumbers` et vous montre comment fonctionnent les closures. Explorons-le plus en détail :

1. `getTwoNumbers` est définie comme une fonction qui prend deux paramètres, `num1` et `num2`.
2. À l'intérieur de `getTwoNumbers`, elle retourne une autre fonction, qui est une fonction interne nommée `add`.
3. La fonction `add`, lorsqu'elle est invoquée, calcule la somme de `num1` et `num2` et enregistre le résultat dans la console.
4. En dehors de la fonction `getTwoNumbers`, nous créons une variable appelée `addNumbers` et lui assignons le résultat de l'invocation de `getTwoNumbers(5, 2)`. Cela établit effectivement une closure où `addNumbers` "se souvient" maintenant des valeurs `5` et `2` comme `num1` et `num2`.
5. Enfin, nous appelons `addNumbers()` pour exécuter la fonction interne `add`. Puisque `addNumbers` est une closure, elle a toujours accès aux valeurs `num1` et `num2`, qui ont été définies à `5` et `2`, respectivement. Elle calcule leur somme et enregistre `7` dans la console.

Si vous souhaitez en savoir plus sur les [closures, lisez plus ici](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures).

Retour à notre fonction d'ordre supérieur. La fonction retournée `greetCustomer` est retournée comme une valeur que nous stockons dans une variable nommée `greet`.

Faire cela fait de la variable `greet` elle-même une fonction, ce qui signifie que nous pouvons l'invoquer comme une fonction et passer des arguments pour un prénom et un nom de famille.

Et voilà. Ces concepts peuvent être un peu complexes à saisir au début, mais une fois que vous les maîtrisez, ils ne vous quittent plus.

Je vous encourage à relire les sections précédentes, à jouer avec le code dans votre éditeur, et à comprendre comment tout fonctionne ensemble.

Maintenant que vous avez une compréhension approfondie de comment les fonctions d'ordre supérieur fonctionnent, parlons des fonctions de callback.

## Qu'est-ce que les fonctions de callback ?

Une fonction de callback est une fonction qui est passée à une autre fonction comme argument.

Encore une fois, l'un des facteurs déterminants des fonctions comme citoyens de première classe est leur capacité à être passées comme argument à une autre fonction. Cela s'appelle **l'acte de passer des callbacks**.

Revenons en arrière et examinons les événements de temporisation que nous avons discutés précédemment lorsque nous apprenions les fonctions intégrées fournies en JavaScript. Voici à nouveau la fonction `setTimeout` :

```js
setTimeout(function () {
  console.log("Ceci est une fonction d'ordre supérieur");
}, 1000);

// Sortie : "Ceci est une fonction d'ordre supérieur" après 1000ms / 1 seconde
```

Nous avons établi que la fonction `setTimeout` est une fonction d'ordre supérieur parce qu'elle accepte une autre fonction comme argument.

La fonction qui est passée comme argument à la fonction `setTimeout` est appelée une fonction de callback. Cela est dû au fait qu'elle est invoquée ou exécutée à l'intérieur de la fonction d'ordre supérieur dans laquelle elle est passée.

Pour mieux comprendre les fonctions de callback, examinons à nouveau la fonction `greetCustomer` de plus tôt :

```js
// CECI EST UNE FONCTION DE CALLBACK
// ELLE EST PASSÉE COMME ARGUMENT À UNE FONCTION

function composeName(firstName, lastName) {
  const fullName = `${firstName} ${lastName}`;

  return fullName;
}

// CECI EST UNE FONCTION D'ORDRE SUPÉRIEUR
// ELLE ACCEPTE UNE FONCTION COMME ARGUMENT

function greetCustomer(composerFunc, firstName, lastName, salutation) {
  const fullName = composerFunc(firstName, lastName);

  console.log(`${salutation} ${fullName}`);
}

greetCustomer(composeName, "Franklin", "Okolie", "Bonjour");

// Sortie : "Bonjour Franklin Okolie"
```

La fonction `composeName` est une fonction de callback qui est passée comme argument à la fonction `greetCustomer`, une fonction d'ordre supérieur, et elle est exécutée à l'intérieur de cette fonction.

## La différence entre les fonctions d'ordre supérieur et les fonctions de callback

Il est important que nous comprenions la différence entre ces deux termes afin de pouvoir communiquer plus clairement avec les coéquipiers et lors des entretiens techniques :

* **Fonction d'ordre supérieur** : Une fonction qui accepte une fonction comme argument et/ou retourne une fonction comme valeur.
* **Fonction de callback** : Une fonction qui est passée comme argument à une autre fonction.

### Un sac et un livre

Pour mieux comprendre ces termes, je vais partager une simple analogie.

Imaginez que vous avez un sac et un livre. Vous transportez le livre dans votre sac pendant que vous assistez à une réunion, allez en classe, allez à l'église, etc.

Dans ce scénario, le sac accepte votre livre pour le transporter, et le retourne également lorsque vous voulez l'utiliser. Donc le sac est comme une fonction d'ordre supérieur.

Le livre est gardé à l'intérieur du sac jusqu'à ce qu'il soit prêt à être utilisé, donc il est comme une fonction de callback.

### Carburant et réservoir de carburant

Examinons une autre analogie ; le carburant et un réservoir de carburant.

Pour faire le plein d'une voiture, nous devons verser le carburant à travers le réservoir de carburant, le réservoir de carburant reçoit le carburant – tout comme une fonction d'ordre supérieur.

Le carburant est versé dans le réservoir de carburant – comme une fonction de callback.

J'espère que ces analogies aident à simplifier davantage les fonctions d'ordre supérieur et les fonctions de callback et la différence entre elles.

## Conclusion

Comme vous pouvez le voir, les fonctions en JavaScript sont très flexibles et peuvent être utilisées de nombreuses manières utiles. Cette flexibilité a également conduit à deux termes techniques courants en JavaScript, les fonctions d'ordre supérieur et les fonctions de callback.

Si vous souhaitez en savoir plus sur ces sujets, consultez la documentation MDN sur les fonctions en tant que [citoyens de première classe](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function), [fonctions d'ordre supérieur](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function), et [fonctions de callback](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function).

J'espère que vous avez appris beaucoup de choses grâce à cet article, et j'espère que vous utiliserez vos nouvelles connaissances pour communiquer vos pensées plus clairement lors des sessions de codage en binôme ou lors des entretiens techniques.

Pour plus de conseils sur JavaScript, suivez-moi sur [Twitter](https://twitter.com/developeraspire).

Merci d'avoir lu ! À la prochaine.