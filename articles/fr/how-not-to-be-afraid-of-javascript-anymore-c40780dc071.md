---
title: Comment ne plus avoir peur de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-24T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-not-to-be-afraid-of-javascript-anymore-c40780dc071
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OQO-Q5kH6KyxOGXf.jpg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment ne plus avoir peur de JavaScript
seo_desc: 'By Neil Kakkar

  Things to know to be a great Javascript developer

  Have you been there before? Where Javascript just doesn’t seem to work. Where the
  functions you write don’t do what you expect them to? Where this just doesn’t make
  sense? What is this?...'
---

Par Neil Kakkar

#### Ce qu'il faut savoir pour devenir un excellent développeur JavaScript

Vous est-il déjà arrivé de vous retrouver dans une situation où JavaScript ne semble tout simplement pas fonctionner ? Où les fonctions que vous écrivez ne font pas ce que vous attendez d'elles ? Où `this` n'a tout simplement pas de sens ? Qu'est-ce que `this` ? C'est `this`.

Cela m'est arrivé. Alors, j'ai écrit cet article. Il couvre tout, des fermetures et des classes aux objets et à l'élévation.

Cela m'a aidé à devenir un meilleur développeur. J'espère qu'il vous aidera aussi.

### Modèle de données

#### Les types

Restez avec moi. Je fais cela parce qu'il y a deux types peu connus que je veux que vous connaissiez : Symboles et Nombres.

De plus, la différence entre undefined et null échappe à beaucoup.

* [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)
* [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
* [Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
* [Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
* [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
* [Symbol](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)
* [undefined](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined) et [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)

#### Nombres

Tous les nombres en JS sont des "valeurs en double précision 64 bits au format IEEE 754". Communément appelés floats, ce qui signifie qu'il n'y a pas de concept d'entier. Vos entiers sont stockés sous forme de floats.

Pour convertir des chaînes en nombres : utilisez `parseInt('123', 10)`. Le deuxième argument est la base. Ainsi, lorsque vous traitez des binaires, vous pourriez faire :

```js
> parseInt('101',2)
5
```

De même, `parseFloat('number')` existe pour les nombres à virgule flottante. La base ici est toujours 10.

#### Symboles

Le seul but de ce type de données est d'identifier les propriétés des objets. Le protocole d'itération et Regex sont les exemples les plus populaires utilisant les Symboles. Nous couvrirons le protocole d'itération dans la prochaine partie !

Vous pouvez en créer un via `Symbol()`. Chaque appel génère un nouveau symbole. Ainsi,

```js
console.log(Symbol(42) === Symbol(42)) // false
```

Les Symboles peuvent persister à travers les fichiers en JavaScript. En ce sens, ils sont différents des variables globales.

Il existe un registre de symboles globaux qui stocke tous les symboles rencontrés. Pour ajouter un Symbole au registre, utilisez `Symbol.for()`, et pour récupérer le symbole utilisez `Symbol.keyFor()`.

Plus d'informations sur les Symboles voir [ici](https://developer.mozilla.org/en-US/docs/Glossary/Symbol).

#### Undefined et Null

Pourquoi la distinction entre undefined et null ?

Par convention, Null indique une valeur délibérément inexistante. Et undefined est une valeur non initialisée.

Par exemple, disons que vous avez un champ qui stocke un ID s'il existe. Dans ce cas, au lieu d'utiliser une valeur magique comme "NOT_EXISTS", vous pouvez utiliser null. S'il est censé exister mais n'est pas là pour le moment, vous pouvez le montrer via undefined.

### Variables et portées

#### Avant ES2015

`var` était le seul moyen de définir des variables.

De plus, nous avions seulement deux portées : [**global**](https://developer.mozilla.org/en-US/docs/Glossary/global_scope) et **fonction** scope. Les variables déclarées à l'intérieur d'une fonction deviennent locales à cette fonction. Tout ce qui est en dehors de la portée de la fonction ne pouvait pas y accéder.

Ainsi, elles avaient une portée de fonction.

#### Après ES2015

ES2015 a introduit deux nouvelles façons de définir des variables :

* `let`
* `const`

Avec elles est venu le concept de **bloc** scope. Un bloc est tout ce qui se trouve entre deux accolades `{..}`

ES2015 est rétrocompatible, donc vous pouvez toujours utiliser var, bien que leur utilisation soit déconseillée.

```js
var x = 1;
{
  var x = 2;
}
console.log(x) // SORTIE : 2, car le bloc ne signifie rien pour var.
let x = 1;
{
  let x = 2;
}
console.log(x) // SORTIE : 1
```

#### Élévation de variable

JavaScript a une idée particulière avec `var` appelée élévation.

```js
function something() {
  console.log(name);
  let name = 'neil';
  console.log(name);
}
```

Pouvez-vous deviner ce qui se passerait ci-dessus ?

Je dis une `ReferenceError` : nous utilisons la variable name avant qu'elle ne soit définie. Cela a du sens, c'est ce qui se passe.

Cependant, si j'utilisais `var` au lieu de `let`, je n'aurais pas d'erreur.

```js
function something() {
  console.log(name); // SORTIE : undefined
  var name = 'neil';
  console.log(name); // SORTIE : neil
}
```

Qu'est-ce qui se passe en coulisses ?

```js
function something() {
  var name; // élévation de variable

  console.log(name); // SORTIE : undefined
  name = 'neil';
  console.log(name); // SORTIE : neil
}
```

C'est une autre raison pour laquelle l'utilisation de `var` est déconseillée. Cela peut conduire à des bugs intéressants.

### Logique de court-circuit : && et ||

Avec JavaScript, quelque chose de particulier se passe avec les opérations logiques. (Et en Python aussi.)

Quelque chose qui vous permet de faire des trucs obscurs comme ceci :

```js
// o est un objet
var name = o && o.name;
```

Que pensez-vous que `name` est ? Si l'objet, `o` est null ou undefined, `name` est null ou undefined.

Si `o` est défini mais que `o.name` est undefined, `name` est undefined.

Si `o` est défini, `o.name` est défini, alors `name = o.name`.

Nous utilisions un opérateur de logique booléenne, n'est-ce pas ? Comment est-ce possible alors ?  
La réponse est le court-circuit et la vérité.

#### Vérité

Une valeur est vraie si elle évalue à true dans un contexte Booléen. Toutes les valeurs sont vraies sauf les valeurs fausses suivantes :

* `false`
* `0`
* `""`
* `null`
* `undefined`
* `NaN`

Note : ce qui signifie que `{}` et `[]` sont vrais !

Un truc habituel pour convertir quelque chose en sa valeur vraie : `!!`

`!` convertit en not — la valeur fausse — et `!` à nouveau la convertit en true/false.

#### Court-circuit

L'idée est que les opérateurs booléens retournent la valeur finale qui rend l'instruction vraie ou fausse, et non si l'instruction est vraie ou fausse. Comme nous l'avons vu ci-dessus, pour la convertir en valeur vraie, vous pouvez utiliser `!!`.

Le court-circuit se produit lorsque l'expression booléenne n'est pas évaluée complètement. Par exemple,

`null && ...`

Peu importe ce que `...` est. `null` est faux, donc cette expression retournerait `null`.

Même cas avec `[] || ...`. `[]` est vrai, donc cette expression retournerait `[]`, indépendamment de ce que `...` est.

### Objets

Un Objet en JavaScript est une collection de paires nom-valeur. Si vous venez de [Comment ne plus avoir peur de Python](https://neilkakkar.com/How-not-to-be-afraid-of-Python-anymore.html), ne confondez pas l'Objet Python avec l'Objet JavaScript.

L'équivalence la plus proche de l'`Object` JavaScript est le `dict` Python.

Pour les types disponibles dans un Objet, nom : `string` ou `Symbol` valeur : N'importe quoi.

Les `Arrays` sont un type spécial d'objet. Ils ont une propriété magique : length (et une chaîne de prototypes différente. Voir ci-dessous.) La longueur du tableau est une de plus que l'index le plus élevé. Cela est mutable, ce qui signifie que vous pouvez faire des trucs bizarres avec (non recommandé) :

```js
const funkyArray = [];
funkyArray['0'] = 'abcd';
funkyArray['length'] = 3

> console.log(funkyArray);
(3) ["abcd", empty × 2]

> funkyArray[4] = 'x';
> console.log(funkyArray);
(5) ["abcd", empty × 3, "x"]
```

Remarquez l'utilisation de nombres et de chaînes comme index de tableau. Les nombres fonctionnent parce que les Objets appellent implicitement `toString()` sur le nom.

Itérer sur les tableaux et les objets, en utilisant des constructions comme `for...of`, `for...in` et `forEach` est quelque chose que je laisserai pour la prochaine partie. (Plus, un bug intéressant lorsque vous utilisez des objets comme maps en JavaScript !)

#### Objet global

Un objet global est un [objet](https://developer.mozilla.org/en-US/docs/Glossary/object) qui existe toujours dans la portée globale. En JavaScript, il y a toujours un objet global défini. Dans un navigateur web, lorsque les scripts créent des variables globales, elles sont créées comme membres de l'objet global [[1](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html#fn:1)]. L'interface de l'objet global dépend du contexte d'exécution dans lequel le script est en cours d'exécution. Par exemple :

* Dans un navigateur web, tout code que le script ne démarre pas spécifiquement comme une tâche de fond a une Window comme objet global. C'est la grande majorité du code JavaScript sur le Web.
* Le code s'exécutant dans un Worker a un objet WorkerGlobalScope comme objet global.
* Les scripts s'exécutant sous Node.js ont un objet appelé global comme objet global. [[2](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html#fn:2)]

### Fonctions

En JavaScript, les fonctions sont des objets de première classe. Elles peuvent avoir des propriétés et des méthodes comme tout autre objet. Elles peuvent être passées à d'autres fonctions comme paramètres (méta-récursion !). La manière dont les fonctions diffèrent des objets est qu'elles sont appelables.

Toutes les fonctions étendent l'objet [**Function**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function). Cet objet n'a pas de propriétés ou de méthodes pré-définies, mais en hérite certaines de `Function.prototype`. (Cela deviendra clair dans la section prototype ci-dessous). De plus, cet objet `Function` est un constructeur pour les fonctions. Vous pouvez créer des fonctions d'au moins 4 manières :

```js
function functionDeclaration() {};
var anonymousFunctionExpression = function() {};
var namedFunctionExpression = function named() {};
var arrowFunctionExpression = () => {};
var constructorFunction = new Function(...args, functionBody); // functionBody est une chaîne
```

L'instruction return peut retourner une valeur à tout moment, mettant fin à la fonction. JavaScript retourne undefined s'il ne voit pas d'instruction return (ou un return vide sans valeur).

Tous les arguments définis pour la fonction vont dans la variable arguments. La valeur par défaut pour tous les arguments est `undefined`.

Avez-vous déjà vu les trois points en JavaScript auparavant ? `...` . Comme celui que j'ai utilisé ci-dessus dans `constructorFunction` ? Ils m'ont déconcerté la première fois que je les ai vus. Ils font partie de la syntaxe en JavaScript. Ce n'est pas du pseudocode (comme je l'ai d'abord pensé).

Ils sont la syntaxe des paramètres `rest` et `spread`.

Ils sont opposés l'un de l'autre. `spread` étale les arguments, `rest` les rassemble.

Voici un exemple : Excusez la fonction mal conçue — qui n'a pas besoin que les arguments soient nommés — mais je fais un point.

```js
const average = function( val1, val2, val3, ...otherValues) { // rest
  console.log(otherValues);
  let sum = 0;
  for (let i = 0; i < arguments.length; i++) { 
    sum += arguments[i];
  }
  return sum / arguments.length;
}
let values = [1, 2, 3, 4, 5, 6]
const averageValue = average(...values); // spread
```

Qu'est-ce qui se passe ici ? `otherValues` utilise la syntaxe rest pour collecter un nombre infini d'arguments passés à average. Le `console.log()` imprimerait `[4, 5, 6]` ci-dessus.

`values` utilise la syntaxe spread pour convertir le tableau en arguments simples. Cela fonctionne de telle sorte que derrière les scènes, ce qui suit est équivalent à ce qui précède.

```
const averageValue = average(1,2,3,4,5,6)
```

Une autre chose à noter est que les valeurs d'argument par défaut sont évaluées chaque fois que la fonction est appelée, contrairement à Python où cela ne se produit qu'une seule fois.

Il existe 3 fonctions prototype intéressantes disponibles pour les objets fonction. Ce sont `apply()`, `bind()` et `call()`. Les A,B,C de JavaScript.

Avec l'avènement de la syntaxe spread et rest, `apply()` et `call()` ne sont plus différents.

`apply()` appelle une fonction avec un tableau d'args ; `call()` appelle une fonction avec des valeurs individuelles.

Le bit cool est qu'ils vous permettent d'appeler la fonction avec un objet `this` personnalisé.

Nous parlerons plus de `apply()` et `bind()` une fois que nous aurons couvert l'objet `this`.

#### Fonctions anonymes et internes

```js
const avg = function () {
  let sum = 0;
  for (let i = 0, argLength = arguments.length; i < argLength; i++) { // la variable arguments est un tableau contenant tous les args passés à la fonction.
    sum += arguments[i];
  }
  return sum / arguments.length; // argLength n'est pas disponible ici
};
```

Les expressions `function avg()` et `var avg = function ()` sont sémantiquement équivalentes.

Cependant, il y a une distinction entre le nom de la fonction (ici anonyme — donc n'existe pas) et la variable à laquelle la fonction est assignée.

Le nom de la fonction ne peut pas être changé, tandis que la variable à laquelle la fonction est assignée peut être réassignée. Le nom de la fonction ne peut être utilisé que dans le corps de la fonction. Tenter de l'utiliser en dehors du corps de la fonction entraîne une erreur (ou undefined si le nom de la fonction a été précédemment déclaré via une instruction var).

Cette idée de fonctions passant comme variables donne naissance à un pouvoir énorme. Par exemple, vous pouvez cacher des variables locales :

```js
var a = 1;
var b = 2;
(function() {
  var b = 3; // variable locale cachée
  a += b;
})();
a; // 4
b; // 2
```

L'expression ci-dessus est appelée une IIFE (Immediately invoked function expression) — où vous créez une fonction et l'appelez immédiatement.

De plus, nous pouvons imbriquer des fonctions les unes dans les autres ! Ce sont ce qu'on appelle les **fonctions internes**. La chose importante à garder à l'esprit : les fonctions internes ont accès aux variables définies dans les fonctions parent, mais pas l'inverse. C'est un résultat direct des fermetures, que nous couvrirons bientôt.

Cela vous permet de créer des fonctions comme :

```js
let joiner = function(separator) {    // La fonction externe définit le séparateur
    return function(left, right) {      
        return left + " " + separator + " " + right;    // La fonction interne a accès au séparateur
    }    // Cela expose la fonction interne au monde extérieur
}
let and = joiner("and");
and("red", "green"); // Il n'y a aucun moyen de changer le séparateur pour AND maintenant ; sauf en réassignant la variable de fonction.
// red and green
const or = joiner("or"); // Il n'y a aucun moyen de changer le séparateur pour OR maintenant.
or("black", "white"); 
// black or white
```

#### Élévation de fonction

> _Avec les déclarations de fonction, les définitions de fonction sont élevées en haut de la portée._  
> _Avec les expressions de fonction, les définitions de fonction ne sont pas élevées_.

D'accord, vous pourriez être confus quant à la différence entre les termes. Je l'étais.

```js
function declaredFunction() { // ceci est la déclaration de fonction
    // ce qui vient ici est la définition de fonction
}
let functionExpression = function() { // ceci est une expression de fonction
    // ce qui vient ici est la définition de fonction
}
```

### Classes et la Chaîne de Prototypes

JavaScript utilise des fonctions comme classes. L'instruction de classe récemment introduite est du sucre syntaxique sur les fonctions.

Puisque toutes les données en JavaScript sont un `Object`, il est logique que nos fonctions — qui sont un constructeur de classe — retourneront un `Object`.

Ainsi, étant donné toutes les bases que nous connaissons sur les fonctions et les objets, nous pouvons faire quelque chose comme ceci pour créer une classe pour, disons _(réfléchit vraiment fort pour trouver un exemple non trivial, utile et relatif...)_  
...   
...   
..   
.  
Une interface de tweet ! Cela semble amusant.

Imaginez que vous construisez votre propre front-end pour afficher des tweets, en parlant à l'API Twitter pour obtenir des données pour les tweets.

```js
function Tweet(id, username, content, parent = null) {
  return {
    id, // JavaScript convertit implicitement ceci en id: id
    username,
    content,
    getUrl: function() {
      return 'https://twitter.com/' + this.username + '/' + this.id;
    },
    isComment: function() {
      return parent !== null;
    }
  };
}
var t = Tweet(1, '@neilkakkar', 'Comment ne plus avoir peur de JS'); 
// Rappelez-vous, nous pouvons remplir n'importe quel nombre d'args
// le reste est undefined ou par défaut
// Tous les args sont dans la variable arguments
t.getUrl(); // "https://twitter.com/@neilkakkar/1"
t.isComment(); // "false"
```

Le mot-clé `[this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)` fait référence à l'objet courant. En utilisant la notation par points, this devient l'objet sur lequel le point a été appliqué. Sinon, c'est l'objet global.

Une note de MDN :

> Dans la plupart des cas, la valeur de this est déterminée par la manière dont une fonction est appelée. Elle ne peut pas être définie par assignation pendant l'exécution, et elle peut être différente à chaque fois que la fonction est appelée. ES5 a introduit la méthode `[bind()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)` pour définir la valeur de `this` d'une fonction indépendamment de la manière dont elle est appelée, et ES2015 a introduit les fonctions fléchées qui ne fournissent pas leur propre liaison this (elle conserve la valeur `this` du contexte lexical englobant).

Cela (jeu de mots intentionnel) est une cause fréquente d'erreurs. Par exemple :

```js
const t = Tweet(1, '@neilkakkar', 'Comment ne plus avoir peur de JS');
const urlFetcher = t.getUrl; // assignation de la fonction
urlFetcher(); // https://twitter.com/undefined/undefined
```

Lorsque nous appelons `urlFetcher()` seul, sans utiliser `t.getUrl()`, `this` est lié à l'objet global. Puisqu'il n'y a pas de variables globales appelées `username` ou `id`, nous obtenons `undefined` pour chacune.

Nous pouvons tirer parti du mot-clé `this` pour améliorer notre fonction Tweet. L'idée est, au lieu de créer un objet et de le retourner, nous attendons un nouvel objet (référencé par `this`) et modifions ses propriétés.

```js
function Tweet(id, username, content, parent = null) {
  this.id = id;
  this.username = username;
  this.content = content;
  this.getUrl = function() {
      return 'https://twitter.com/' + this.username + '/' + this.id;
  };
  this.isComment = function() {
      return parent !== null;
    }
  };
}
var t = new Tweet(1, '@neilkakkar', 'Comment ne plus avoir peur de JS');
```

Le mot-clé [new](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new) crée un tout nouvel objet vide, puis appelle la fonction spécifiée, avec `this` défini sur le nouvel objet. Notre fonction modifiée ne retourne pas de valeur mais modifie simplement l'objet `this`. `new` retourne également l'objet `this`, une fois la fonction appelée sur lui. C'est ce que nous voulions. `new` fait aussi quelques trucs supplémentaires que nous voulons — comme configurer la chaîne de prototypes — mais nous y viendrons dans un peu.

De telles fonctions, conçues pour être appelées par `new`, sont appelées **fonctions constructeur**. Par convention, ces fonctions sont en majuscules (comme un rappel pour les appeler avec `new`).

Puisque nous obtenons un nouvel objet chaque fois que nous appelons `Tweet`, nous avons deux objets fonction (`getUrl` et `isComment`) créés chaque fois que nous appelons `Tweet`. Une meilleure façon est d'écrire ces fonctions en dehors de la portée du constructeur — et de passer une référence.

Si vous venez d'un contexte OOP, même cela pourrait ne pas sembler suffisant. Vous ne voulez pas que cette fonction soit utilisée ailleurs que pour cet objet `Tweet`. Vous ne voulez pas salir votre liste de fonctions globales. C'est là que l'"héritage" de JavaScript entre en jeu.

### Prototype

`Tweet.prototype` est un objet partagé par toutes les instances de `Tweet`. Il fait partie d'une chaîne de recherche (qui a un nom spécial, "chaîne de prototypes") : chaque fois que vous accédez à une propriété de `Tweet` qui n'est pas définie, JavaScript vérifiera `Tweet.prototype` pour voir si cette propriété existe là.

En conséquence, tout ce qui est assigné à `Tweet.prototype` devient disponible pour toutes les instances de ce constructeur via l'objet `this`.

> Chaque objet a une propriété privée (`__proto__`) qui contient un lien vers un autre objet appelé son prototype. Ce prototype objet a un prototype à lui-même, et ainsi de suite jusqu'à ce qu'un objet soit atteint avec null comme prototype. Par définition, null n'a pas de prototype, et agit comme le dernier lien dans cette chaîne de prototypes.

C'est un outil incroyablement puissant. JavaScript vous permet de modifier le prototype de quelque chose à tout moment dans votre programme, ce qui signifie que vous pouvez ajouter des méthodes supplémentaires aux objets existants à l'exécution (sans avoir à rappeler le constructeur).

```js
var t = new Tweet(1, '@neilkakkar', 'Comment ne plus avoir peur de JS');
t.getComments(); // TypeError à la ligne 1 : t.getComments n'est pas une fonction
Tweet.prototype.getComments = function() {
  // exemple d'appel d'API à l'API Twitter - disons qu'elle existe en tant qu'objet twitterService
  return twitterService.getComments(this.id);
};
t.getComments(); // "[ 'C'est un article incroyable, merci !' , 'J'adore ça' ]" 
// commentaires fictifs
```

#### function.prototype vs __proto__

Vous avez probablement vu les deux utilisés de manière interchangeable. Ils ne sont pas les mêmes. Clarifions cela.

Le `function.prototype` est un constructeur pour `__proto__`.

`__proto__` est l'objet prototype réel disponible sur les objets.

Ainsi, `function.prototype` n'est disponible que pour les fonctions constructeur. Vous ne pouvez pas accéder au prototype pour un tweet en tant que `t.prototype`, vous devrez utiliser `t.__proto__`.

Mais pour définir le prototype, vous utiliseriez `Tweet.prototype.getComments()` comme dans l'exemple ci-dessus.

#### Un rappel de ce que nous avons fait avec les fonctions et les classes

* Les classes sont des fonctions. Nous avons commencé avec une fonction qui créait un nouvel objet ( `return {...}`- en utilisant la syntaxe littérale d'objet), puis ajoutait des propriétés (les données de classe) et enfin le retournait.
* Ensuite viennent les fonctions constructeur. Celles-ci supposent qu'il y a un objet vide donné (initialisé via `new`) et ajoutent simplement les propriétés.
* Ensuite vient la chaîne de prototypes, pour les méthodes qui seraient utilisées par tous les objets de la `classe`

En coulisses, c'est ainsi que les choses fonctionnent lorsque vous utilisez le mot-clé `class`.

### Le mot-clé New et Apply

Nous pouvons maintenant explorer ce qui se passe en coulisses avec `new` et revisiter `apply()` à partir du prototype de fonction. Nous avons déjà vu `bind()`.

La fonction de `new` est de créer un objet, de le passer à la fonction constructeur (où cet objet est disponible en tant que `this`), et de configurer la chaîne de prototypes.

`apply()` prend un objet (la valeur `this`) et un tableau d'arguments à appeler sur cet objet.

En mettant ces deux ensemble, nous obtenons une implémentation triviale de new.

```js
function newNew(constructorFunction, ...args) {
  const thisObject = {}; // créer un objet en utilisant la syntaxe littérale d'objet
  constructorFunction.apply(thisObject, args); // appelle constructorFunction avec this défini sur thisObject et avec les args donnés
  // la configuration de la chaîne de prototypes est délicate. Besoin d'un nouveau prototype pour constructorFunction
  // pas le prototype du constructeur de fonction
  return thisObject;
}
```

### Fermetures

Vous vous souvenez de la fonction joiner ?

```js
let joiner = function(separator) {    // La fonction externe définit le séparateur
    return function(left, right) {      
        return left + " " + separator + " " + right;    // La fonction interne a accès au séparateur
    }    // Cela expose la fonction interne au monde extérieur
}
let and = joiner("and");
and("red", "green"); // Il n'y a aucun moyen de changer le séparateur pour AND maintenant ; sauf en réassignant la variable de fonction.
// red and green
const or = joiner("or"); // Il n'y a aucun moyen de changer le séparateur pour OR maintenant.
or("black", "white"); 
// black or white
```

Une fonction définie à l'intérieur d'une autre fonction a accès aux variables de la fonction externe. Une fois que la fonction externe retourne, le bon sens dicterait que ses variables locales n'existent plus.

Mais elles existent — sinon, les fonctions joiner ne fonctionneraient pas. De plus, il y a deux copies différentes des variables locales de `joiner()` — une dans laquelle `separator` est `and` et l'autre où `separator` est `or`. Comment cela fonctionne-t-il ?

#### Objet de portée

Chaque fois que JavaScript exécute une fonction, il crée un objet de 'portée' pour contenir les variables locales créées dans cette fonction. L'objet de portée est initialisé avec les variables passées en tant que paramètres de fonction. Cela est similaire à l'objet global — lorsque de nouvelles variables 'apparaissent', elles sont ajoutées à l'objet de portée.

Deux points clés :

* un tout nouvel objet de portée est créé chaque fois qu'une fonction commence à s'exécuter
* contrairement à l'objet global, ces objets de portée ne peuvent pas être directement accessibles à partir de votre code JavaScript. Il n'y a aucun mécanisme pour itérer sur les propriétés de l'objet de portée actuel.

Ainsi, lorsque `joiner()` est appelé, un objet de portée est créé avec une propriété : `separator`, qui est l'argument passé à `joiner()`. `joiner()` retourne ensuite la fonction créée.

Normalement, le ramasse-miettes de JavaScript nettoierait l'objet de portée créé pour `joiner()` à ce stade, mais la fonction retournée maintient une référence à cet objet de portée. En conséquence, l'objet de portée ne sera pas ramassé jusqu'à ce qu'il n'y ait plus de références à l'objet de fonction que `joiner()` a retourné.

Les objets de portée forment une chaîne appelée la chaîne de portée, similaire à la chaîne de prototypes.

> _Une fermeture est la combinaison d'une fonction et de l'objet de portée dans lequel elle a été créée. Les fermetures vous permettent de sauvegarder l'état — en tant que tel, elles peuvent souvent être utilisées à la place des objets_

Ainsi, vous créez une fermeture chaque fois que vous créez une fonction à l'intérieur d'une autre fonction.

#### Performance

Pour terminer cette section, parlons un peu de performance. Pour optimiser les performances, supprimez les fermetures non nécessaires. Rappelez-vous, la référence vit jusqu'à ce que l'objet de portée soit nécessaire, contenant toutes les variables locales et les arguments de fonction.

```js
function f(i) {
    var o = { };  // Un grand objet
    var a = [ ];  // Un grand tableau
    // `a` et `o` sont des variables locales et seront donc ajoutés à l'objet de fermeture.
    //...
    //...
    // un cas d'utilisation pour a et o
    var c = [ 1, 2, 3 ].filter(item => a.indexOf(item) > -1 || o[item]);
    a = undefined;  // Nettoyer avant la fermeture
    o = undefined;  // Nettoyer avant la fermeture
    return function () { // fermeture créée
           return ++i; // nous n'avions besoin de rien sauf i pour cette fonction,
           // donc il est logique de supprimer tout le reste de la fermeture.
    };
}
```

### Modèle d'exécution

![Image](https://cdn-media-1.freecodecamp.org/images/lSYVzm-RGiVEPonCG-ku2EQuT7aMJ2ENqzP6)
_[Source](https://www.zeolearn.com/magazine/understanding-the-javascript-event-loop" rel="noopener" target="_blank" title=")_

Comment JavaScript s'exécute-t-il ?

Ce gif montre les différents composants et comment ils interagissent ensemble. Passons-les en revue.

#### Pile d'appels

Chaque appel de fonction est un cadre sur la pile.

Cette pile d'appels est une pile d'appels de fonctions à exécuter dans l'ordre. (Vous voyez pourquoi on l'appelle une pile ?)

Le cadre contient les arguments de la fonction et les variables locales. C'est là que l'objet de portée, et donc la fermeture, est défini !

Les fonctions sont retirées de la pile lorsqu'elles retournent.

Chaque script commence avec un `main()` sur la pile, en tant que fonction contenant toutes les autres fonctions du script.

#### Tas

Chaque objet que vous créez a besoin d'un endroit en mémoire pour vivre. Cet endroit est le tas : une grande région de mémoire non structurée.

Si vous venez du monde C++, le tas est l'endroit où les choses vont lorsqu'elles sont construites en utilisant `new` en C++.

#### API Web et Événements

Les API Web sont des fonctions de bas niveau présentes dans l'environnement d'exécution JavaScript pour interagir avec le système d'exploitation. Elles sont implémentées par le navigateur / hôte. Par exemple : `setTimeout()`.

Elles sont appelées depuis la pile et commencent le traitement. La fonction retourne à ce stade (retirant ainsi le cadre de la pile). C'est ce qui donne à JavaScript la caractéristique asynchrone. Presque toutes ses API de base sont non bloquantes.

Jetez un coup d'œil au GIF ci-dessus — et cette partie deviendra plus claire.

Ces API génèrent un message. Cela pourrait être un appel d'API pour `fetch` des données, auquel cas le message est les données. Cela pourrait être `setTimeout()`, où le message est vide. Cela pourrait être un événement sur un bouton DOM comme `onClick`, où le message est l'information stockée dans le bouton.

Les API envoient ces messages à la file d'attente de rappel. Ils ont une fonction de rappel qui est attachée au message. Ce rappel est reçu depuis la pile d'appels (quelque chose que nous fournissons lorsque nous appelons l'API).

> _Dans les navigateurs web, les messages sont ajoutés chaque fois qu'un événement se produit et qu'il y a un écouteur d'événement attaché. Si aucun écouteur n'est présent, l'événement est perdu. Ainsi, un clic sur un élément avec un gestionnaire d'événement de clic ajoutera un message — de même avec tout autre événement._

#### File d'attente de rappel

C'est une file d'attente contenant toutes les tâches qui ont terminé le traitement. Elle a une file d'attente de messages avec des fonctions de rappel pour chaque message.

Pour traiter un message, la fonction de rappel est appelée avec le message comme entrée — mais la file d'attente ne peut pas faire cela, c'est juste une file d'attente de messages. Ce traitement est réalisé via la Boucle d'Événements.

**Fun-fact** : Cette file d'attente est communément connue sous le nom de file d'attente de macrotâches. Il y a une petite file d'attente de microtâches qui se cache derrière aussi. Pas beaucoup de gens savent cela — mais cela entre en jeu lors de la gestion des Promesses. Une histoire pour un futur article, peut-être ? (Wow, JS est énorme, n'est-ce pas ?)

#### Boucle d'Événements

Pour appeler les rappels dans la file d'attente de rappel, nous devons les ramener sur la pile d'appels. C'est la seule façon d'appeler une fonction.

La Boucle d'Événements gère ce bit. C'est une boucle en cours d'exécution qui vérifie si la pile d'appels est vide à chaque boucle.

Une fois la pile d'appels vide, la boucle d'événements prend le premier élément de la file d'attente de rappel et transfère le rappel à la pile d'appels.

#### Exécution à complétion

Dans la boucle d'événements, chaque message s'exécute jusqu'à complétion. Cela signifie qu'aucun nouveau message n'est ajouté à la pile d'appels pendant que le message actuel est en cours d'exécution.

#### Rappel du Modèle d'Exécution

D'accord, nous avons couvert beaucoup de choses ici. Du code suit, mais avant cela, je veux m'assurer que les choses sont claires.

1. Une fois que vous exécutez un script, la fonction `main()` est ajoutée à la pile d'appels.
2. Lorsque des fonctions sont appelées depuis le script, elles sont ajoutées à la pile d'appels. Retirées lorsqu'elles sont retournées.
3. Les objets de portée sont ajoutés avec les fonctions à la pile d'appels.
4. Certaines fonctions peuvent également avoir un composant de traitement — qui est géré par les API. Ces API retournent un message et un rappel.
5. Les messages sont ajoutés à la file d'attente de rappel.
6. La boucle d'événements transfère les messages de la file d'attente de rappel à la pile d'appels uniquement lorsque la pile d'appels est vide (c'est-à-dire que `main()` est également retirée)
7. Chaque message s'exécute jusqu'à complétion (conséquence directe des nouveaux messages étant ajoutés uniquement lorsque la pile est vide)

Avec ce rappel en tête, appliquons-le. `setTimeout( callback, t)` est une fonction (API) comme défini ci-dessus, qui prend un rappel et ajoute un message à la file d'attente de rappel après `t` secondes.

Alors, quel serait l'ordre d'impression ci-dessous ?

```js
console.log('1');
setTimeout( () => console.log(2), 0) // t = 0;
console.log('3');
```

...

..

.

Si vous avez deviné `1 2 3`, passons en revue l'exemple.

Initialement, nous avons `main()` sur la pile d'appels. Ensuite, nous parcourons le script.

Nous voyons `console.log(1)` — cela se met sur la pile d'appels, imprime `1` et est retiré.

Nous voyons `setTimeout()` — cela se met sur la pile d'appels, passe à l'API Web et est retiré.

En même temps, puisque le délai était de 0 secondes, le rappel est passé à la file d'attente de rappel.

Nous voyons `console.log(3)` — cela se met sur la pile d'appels, imprime `3` et est retiré.

Le script se termine, donc `main()` est retiré.

Maintenant, la pile d'appels est vide, donc le rappel `setTimeout()` est transféré à la pile d'appels.

C'est-à-dire que nous avons `() => console.log(2)` sur la pile d'appels. Cela est appelé avec le message nul.

Ainsi, l'ordre est `1 3 2`.

C'est le piège du délai zéro — une idée pratique pour vous rappeler comment fonctionne la boucle d'événements.

Cela semble être un bon endroit pour s'arrêter pour l'instant. J'espère que cet article vous a aidé à commencer à mieux comprendre JavaScript ! :)

Références :

[1] [Réintroduction à Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)  
[2] [Docs généraux MDN](https://developer.mozilla.org/en-US/)

[Voici la Partie 2](https://neilkakkar.com/js-part-2.html) sur mon blog.

Autres histoires de cette série :

[Comment ne plus avoir peur de GIT](https://neilkakkar.com/How-not-to-be-afraid-of-GIT-anymore.html)

[Comment ne plus avoir peur de Vim](https://neilkakkar.com/How-not-to-be-afraid-of-Vim-anymore.html)

[Comment ne plus avoir peur de Python](https://neilkakkar.com/How-not-to-be-afraid-of-Python-anymore.html)

Lisez plus de mes articles sur [neilkakkar.com](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html).