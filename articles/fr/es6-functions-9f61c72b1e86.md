---
title: 'Fonctions JavaScript ES6 : Les Bonnes Parties'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-20T17:54:26.000Z'
originalURL: https://freecodecamp.org/news/es6-functions-9f61c72b1e86
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nND_xhKn-rWHi8nBShTH-Q.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: 'Fonctions JavaScript ES6 : Les Bonnes Parties'
seo_desc: 'By Bhuvan Malik

  ES6 offers some cool new functional features that make programming in JavaScript
  much more flexible. Let’s talk about some of them — specifically, default parameters,
  rest parameters, and arrow functions.

  Fun tip: you can copy and pas...'
---

Par Bhuvan Malik

ES6 offre quelques nouvelles fonctionnalités fonctionnelles sympas qui rendent la programmation en JavaScript beaucoup plus flexible. Parlons de certaines d'entre elles — spécifiquement, les paramètres par défaut, les paramètres rest et les fonctions fléchées.

**Astuce amusante** : vous pouvez copier et coller n'importe lequel de ces exemples/code dans [Babel REPL](https://babeljs.io/repl/) et vous pouvez voir comment le code ES6 est transpilé en ES5.

![Image](https://cdn-media-1.freecodecamp.org/images/NIpmekw9kO1zjEdmWmnWAvnmoFQ8Eh96Jcgk)

### **Valeurs de Paramètres par Défaut**

Les fonctions JavaScript ont une caractéristique unique qui permet de passer n'importe quel nombre de paramètres lors de l'appel de la fonction (paramètres réels) indépendamment du nombre de paramètres présents dans la définition de la fonction (paramètres formels). Il est donc nécessaire d'inclure des paramètres par défaut au cas où quelqu'un oublierait d'en passer un.

#### **Comment les paramètres par défaut seraient implémentés en ES5**

Ce qui précède semble correct lorsque nous l'exécutons. `number2` n'a pas été passé et nous avons vérifié cela en utilisant l'opérateur '||' pour retourner le second opérande si le premier est falsy. Ainsi, '10' a été assigné comme valeur par défaut puisque `number2` est indéfini.

Il y a cependant un problème. Que se passe-t-il si quelqu'un passe '0' comme second argument ? ⚠

L'approche ci-dessus échouerait car notre valeur par défaut '10' serait assignée au lieu de la valeur passée, comme '0'. Pourquoi ? Parce que '0' est évalué comme falsy !

Améliorons le code ci-dessus, d'accord ?

Agh ! C'est trop de code. Pas cool du tout. Voyons comment ES6 le fait.

#### **Paramètres par défaut en ES6**

```
function counts(number1 = 5, number2 = 10) {  // faire quelque chose ici}
```

`number1` et `number2` se voient assigner des valeurs par défaut de '5' et '10' respectivement.  
Eh bien oui, c'est à peu près tout. Court et doux. Pas de code supplémentaire pour vérifier un paramètre manquant. Cela rend le corps de la fonction agréable et court. ?

NOTE : Lorsqu'une valeur de `undefined` est passée pour un paramètre avec un argument par défaut, comme prévu, la valeur passée est **invalide** et la **valeur du paramètre par défaut est assignée**. Mais si `null` est passé, il est considéré comme **valide** et le **paramètre par défaut n'est pas utilisé** et null est assigné à ce paramètre.

Une caractéristique intéressante des paramètres par défaut est que le paramètre par défaut n'a pas nécessairement à être une valeur primitive, et nous pouvons également exécuter une fonction pour récupérer la valeur du paramètre par défaut. Voici un exemple :

Les paramètres précédents peuvent également être des paramètres par défaut pour les paramètres qui les suivent comme ceci :

```
function multiply(first, second = first) {  // faire quelque chose ici}
```

Mais l'inverse générera une erreur. C'est-à-dire, si le second paramètre est assigné comme valeur par défaut pour le premier paramètre, cela entraîne une erreur car le second paramètre n'est pas encore défini lors de son assignation au premier paramètre.

```
function add(first = second, second) {  return first + second;}console.log(add(undefined, 1)); // génère une erreur
```

### Paramètres Rest

> Un paramètre _rest_ est simplement un paramètre nommé qui est précédé de trois points (•). Ce paramètre nommé devient un tableau qui contient le reste des paramètres (c'est-à-dire à part les paramètres nommés) passés lors de l'appel de la fonction.

Gardez simplement à l'esprit qu'il ne peut y avoir qu'un seul paramètre _rest_, et qu'il doit être le dernier paramètre. Nous ne pouvons pas avoir un paramètre nommé après un paramètre rest.  
Voici un exemple :

Comme vous pouvez le voir, nous avons utilisé le paramètre rest pour obtenir toutes les clés/propriétés à extraire de l'objet passé, qui est le premier paramètre.

La différence entre un paramètre rest et l'objet 'arguments' est que ce dernier contient tous les paramètres réels passés lors de l'appel de la fonction, tandis que le 'paramètre rest' ne contient que les paramètres qui ne sont pas des paramètres nommés et sont passés lors de l'appel de la fonction.

### Fonctions Fléchées ➡

![Image](https://cdn-media-1.freecodecamp.org/images/9n5l6egKPj2FuvrmoTHpTfNcS0jRzOa-0Ap5)

Les fonctions fléchées, ou « fat arrow functions », introduisent une nouvelle syntaxe pour définir des fonctions qui est très concise. Nous pouvons éviter de taper des mots-clés comme `function`, `return` et même les accolades `{ }` et les parenthèses `()`.

#### Syntaxe

La syntaxe se décline en différentes variantes, selon notre utilisation. Toutes les variations ont un point **commun**, c'est-à-dire qu'elles commencent par les **arguments**, suivis de **la** **flèche** (`=>`), suivis du **corps de la fonction**.

Les arguments et le corps peuvent prendre différentes formes. Voici l'exemple le plus basique :

```
let mirror = value => value;
```

```
// équivalent à :
```

```
let mirror = function(value) {  return value;};
```

L'exemple ci-dessus prend un seul argument « value » (avant la flèche) et retourne simplement cet argument (`=> value`). Comme vous pouvez le voir, **il n'y a que la valeur de retour, donc pas besoin du mot-clé return ou d'accolades pour envelopper le corps de la fonction**.

Puisqu'il n'y a qu'**un seul argument**, il n'y a **pas besoin de parenthèses** « ( ) » non plus.

Voici un exemple avec plus d'un argument pour vous aider à comprendre cela :

```
let add = (no1, no2) => no1 + no2;
```

```
// équivalent à :
```

```
let add = function(no1, no2) {  return no1 + no2;};
```

S'il n'y a pas d'arguments du tout, vous devez inclure des parenthèses vides comme ci-dessous :

```
let getMessage = () => 'Hello World';
```

```
// équivalent à :
```

```
let getMessage = function() {  return 'Hello World';}
```

Pour un corps de fonction avec juste une instruction return, les accolades sont **optionnelles**.  
Pour un corps de fonction ayant plus qu'une simple instruction return, vous devez envelopper le corps dans des accolades comme pour les fonctions traditionnelles.

Voici une simple fonction de calcul avec deux opérations — addition et soustraction. Son corps doit être enveloppé dans des accolades :

```
let calculate = (no1, no2, operation) => {    let result;    switch (operation) {        case 'add':            result = no1 + no2;            break;        case 'subtract':            result = no1 - no2;            break;    }    return result;};
```

Maintenant, que se passe-t-il si nous voulons une fonction qui retourne simplement un objet ? Le compilateur sera confus quant à savoir si les accolades sont celles de l'objet (`()=>{id: number}`) ou les accolades du corps de la fonction.

La solution est d'envelopper l'objet dans des parenthèses. Voici comment :

```
let getTempItem = number => ({ id: number});
```

```
// effectivement équivalent à :
```

```
let getTempItem = function(number) {    return {        id: number    };};
```

Regardons le dernier exemple. Dans celui-ci, nous utiliserons la fonction filter sur un tableau d'exemple de nombres pour retourner tous les nombres supérieurs à 5 000 :

```
// avec fonction fléchéelet result = sampleArray.filter(element => element > 5000);
```

```
// sans fonction fléchéelet result = sampleArray.filter(function(element) {  return element > 5000;});
```

Nous pouvons voir combien moins de code est nécessaire par rapport aux fonctions traditionnelles.

Quelques points à garder à l'esprit concernant les fonctions fléchées :

* Elles ne peuvent pas être appelées avec _new_, ne peuvent pas être utilisées comme constructeurs (et donc n'ont pas de prototype non plus)
* Les fonctions fléchées ont leur propre portée, mais elles n'ont pas de 'this' qui leur est propre.
* Aucun objet _arguments_ n'est disponible. Vous **pouvez utiliser** les paramètres rest cependant.

Puisque JavaScript traite les fonctions comme des citoyens de première classe, les fonctions fléchées rendent l'écriture de code fonctionnel comme les expressions lambda et le currying beaucoup plus facile.

> « Les fonctions fléchées étaient comme du carburant de fusée pour l'explosion de la programmation fonctionnelle en JavaScript. » — Eric Elliott

Eh bien, voilà ! Peut-être est-il temps pour vous de commencer à utiliser ces fonctionnalités.

Les fonctionnalités ES6 comme celles-ci sont un bol d'air frais, et les développeurs adorent les utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/fRbQopusRfJej7QpnRe6umezaPKn-cWs6vgO)

Voici le [lien](https://medium.com/@bhuvanmalik/what-is-variable-hoisting-differentiating-between-var-let-and-const-in-es6-f1a70bb43d) vers mon précédent article sur les déclarations de variables et le hoisting !  
J'espère que cela vous motive à prendre ES6 à bras-le-corps si vous ne l'avez pas déjà fait !

Paix ✌️️