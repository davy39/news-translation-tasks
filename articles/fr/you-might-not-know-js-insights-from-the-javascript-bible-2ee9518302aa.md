---
title: 'Vous ne connaissez peut-être pas JS : Perspectives de la Bible JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-06T22:18:58.000Z'
originalURL: https://freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N8GoVaCrqVPJWv4H15RdCw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Vous ne connaissez peut-être pas JS : Perspectives de la Bible JavaScript'
seo_desc: 'By Jérémy Bardon

  Did you use some JavaScript to make your web app dynamic? That’s the common usage
  for this language, but there is far more waiting for you.

  After reading the popular book series You Don’t Know JS by Kyle Simpson, I realised
  I didn’t ...'
---

Par Jérémy Bardon

Avez-vous utilisé un peu de JavaScript pour rendre votre application web dynamique ? C'est l'usage courant pour ce langage, mais il y a bien plus qui vous attend.

Après avoir lu la série de livres populaires [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS) de [Kyle](https://www.freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa/undefined) Simpson, j'ai réalisé que je ne connaissais pas JS auparavant. La communauté JavaScript considère cette série comme l'une des références pour le langage. Elle est épaisse mais complète. Cette série est une alliée inestimable (et gratuite) pour vous aider à affûter vos compétences.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6YTkvM9Y-gcw5F6qyA3ngQ.png)
_You Don't Know JS (série de livres)_

Dans cet article, j'ai rassemblé pour vous les perspectives les plus importantes. Des choses simples aux plus difficiles (ce mot-clé et les promesses). Je n'ai pas cité le livre mais j'ai préféré construire mes propres exemples. Considérez cela comme une introduction à la série de livres.

Si vous avez appris JavaScript à l'école comme moi, je parie que vous avez d'abord appris Java. Faites attention, apprendre JavaScript ne consiste pas à imiter Java. Cela ne fonctionne pas comme ça — vous devez l'apprendre comme un nouveau langage.

### LEÇON #1 — Opérateurs logiques

Dans de nombreux langages, les expressions qui implémentent des opérateurs logiques tels que **ET** et **OU** retournent une valeur booléenne. Au lieu de cela, JavaScript retourne l'un des deux opérandes comme expliqué dans cette [note de spécification ECMAScript](https://tc39.github.io/ecma262/#sec-binary-logical-operators).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ihA6bgwRrlMZWxJ8Ghy2mg.png)

Avec les deux opérateurs, il retourne le premier opérande qui arrête l'évaluation. Essayez en définissant `foo` ou `bar` à la valeur booléenne `false`. De plus, si vous n'incluez aucune parenthèse, l'opérateur **ET** a la priorité sur **OU**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BDscE-3cbvZq3xQnbWI_fA.png)

Il évalue d'abord `foo && foo.bar` comme s'il était entre parenthèses. Vous pouvez dire que **ET** a la priorité sur **OU**.

Étant donné que l'opérateur **OU** retourne le premier opérande qui le satisfait, vous pouvez l'utiliser pour définir une valeur par défaut pour les variables vides ou non définies. C'était la manière préférée de définir les [paramètres de fonction par défaut](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters) avant ES6.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0xc6klIypF2zQkJ0dIM3Xw.png)

Un autre cas d'utilisation pour ces opérateurs logiques est d'éviter les blocs `if-else` et les expressions ternaires :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oISc-T9mbTwvdpiom0XyFg.png)

Voici les équivalences pour les expressions ternaires :

* `a || b` est équivalent à `a ? a : b`
* `a && b` est équivalent à `a ? b : a`

### LEÇON #2 — Conversion de type

Outre les fonctions telles que `valueOf`, JavaScript fournit une [conversion de type](https://en.wikipedia.org/wiki/Type_conversion). Il existe une autre manière de convertir les types de variables.

* **Cast** se produit au moment de la compilation et utilise l'opérateur de cast explicite
* **Coercition** se produit à l'exécution et souvent avec une syntaxe implicite

![Image](https://cdn-media-1.freecodecamp.org/images/1*lhxK9yCOl3iB-C8kncEkGg.png)

La coercition implicite est le type de conversion le plus difficile à voir, donc les développeurs évitent souvent de les utiliser. Pourtant, il est bon de connaître quelques coercitions implicites courantes. Voici des exemples pour `String` et `Boolean`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pOJHWmz4DX0PMqB0M-ZSxQ.png)

Un autre opérateur utile mais rarement utilisé est `~`, un équivalent à l'opération `-(x+1)`. Il est utile pour détecter la valeur de sentinelle commune [**sentinel value**](https://en.wikipedia.org/wiki/Sentinel_value) `-1`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MFNIbPhb06Kd507UGSd0vg.png)

### LEÇON #3 — Valeurs fausses

Les conditions sont l'une des structures de base en programmation et nous les utilisons beaucoup. Au fait, la légende dit que les programmes d'intelligence artificielle sont remplis de `if`. Il est important de savoir comment cela se comporte dans n'importe quel langage de programmation.

Les valeurs données à une condition sont soit considérées comme **fausses** soit **vraies**. [La spécification ECMAScript](https://tc39.github.io/ecma262/#table-10) vient avec une liste soignée de valeurs fausses :

* `''` chaîne vide
* `undefined`
* `null`
* `false` valeur booléenne
* `0` valeur numérique
* `-0` valeur numérique
* `NaN` valeur non numérique

Expérimentez vous-même avec le snippet suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*P77vOjTLIb-u1UgVnYK7Wg.png)
_Tester si une valeur est vraie ou fausse_

Toute autre valeur non dans la liste est vraie. Par exemple, faites attention à `{}` (objet littéral vide), `[]` (tableau vide) et `'false'` (chaîne false) qui sont tous `true`.

Combiné avec des opérateurs logiques, vous pouvez appeler une fonction uniquement si une valeur est vraie sans utiliser de `if`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lwDhNrZH9nOtIG5-raaiFg.png)

### LEÇON #4 — Portée et IIFE

La première fois que vous avez écrit du JavaScript, quelqu'un vous a probablement dit d'utiliser la notation suivante parce que _"ça marche mieux"_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*STUXPjN-r6umC3VQwC7EmQ.png)

Cela fait la même chose que de déclarer une fonction régulière puis de l'appeler immédiatement.

Cette notation est une [IIFE](https://en.wikipedia.org/wiki/Immediately-invoked_function_expression), elle signifie **Immediately Invoked Function Expression**. Et elle ne marche pas mieux mais elle prévient les collisions de variables.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z7r-mW31xLOYz7PeBeVuVg.png)

La variable `foo` d'une **balise script** est magiquement attachée à la fenêtre. Assez intéressant quand on sait que les bibliothèques et frameworks définissent leurs propres variables en utilisant la même technique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ibEEEl6V5oXcq7hyh-Z0GA.png)
_Collision de variable sur la variable nommée 'Vue'_

En réalité, la **portée** des variables définies avec le mot-clé `var` n'est pas liée à tous les blocs. Ces blocs sont des parties de code délimitées avec des accolades comme dans les expressions `if` et `for`, par exemple.

Seuls les blocs `function` et `try-catch` peuvent restreindre la portée de `var`. Même les blocs `if-else` et les boucles `for` ne peuvent pas le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jmZGwgpNrrnC3nT2DlKbtg.png)

L'utilisation de IIFE fournit un moyen de cacher les variables de l'extérieur et de restreindre leur portée. Ainsi, personne ne peut altérer la logique métier en changeant les valeurs des variables de la fenêtre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SKPQrd8ekt_cDjGEA5yNWw.png)

ES6 arrive avec les mots-clés `let` et `const`. Les variables utilisant ces mots-clés sont liées aux blocs définis avec des accolades.

### LEÇON #5 — Objet et maps

Les objets aident à rassembler des variables avec le même sujet sous une variable unique. Vous obtenez un objet contenant de nombreuses propriétés. Il existe deux syntaxes pour accéder à une propriété d'objet : la syntaxe par point et par tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PFNO-NyFBTmtIiiHGt3ccg.png)

La syntaxe par tableau semble être la meilleure solution pour créer des maps mais ce n'est pas le cas. Dans cette configuration, les clés doivent être des chaînes. Si ce n'est pas le cas, elles sont coercées en chaîne. Par exemple, tout objet est coercé en clé `[object Object]`.

```js
// À partir d'ici, les exemples sont un peu longs.
// J'utiliserai du code intégré pour que vous puissiez copier/coller et essayer vous-même !

let map = {};
let x = { id: 1 },
    y = { id: 2 };

map[x] = 'foo';
map[y] = 'bar';

console.log(map[x], map[y]); // 'bar', 'bar'
```

À partir d'ici, les exemples sont un peu longs. J'utiliserai des gists pour que vous puissiez copier/coller et essayer vous-même !

En réalité, cette map n'a qu'une seule valeur sous la clé `[object Object]`. D'abord, sa valeur est `'foo'` puis elle devient `'bar'`.

Pour éviter ce problème, utilisez l'objet [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) introduit dans ES6. Pourtant, faites attention, l'opération de recherche pour obtenir une valeur à partir d'une clé utilise une [égalité stricte](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness#Strict_equality_using).

```js
var map = new Map();
map.set(x, 'foo');
map.set(y, 'bar');

console.log(map.get(x), map.get(y)); // 'foo', 'bar'

// undefined, undefined
console.log(map.get({ id: 1 }, map.get({ id: 2 });
```

Ce détail n'a d'importance que pour les variables complexes comme les objets. Parce que deux objets avec le même contenu ne correspondront pas avec une égalité stricte. Vous devez utiliser la variable exacte que vous avez mise comme clé pour récupérer votre valeur de la map.

### LEÇON #6 — Qu'est-ce que `this` ?

Le mot-clé `this` est utilisé dans les langages construits avec des classes. Habituellement, `this` (et son frère `self`) fait référence à l'instance actuelle de la classe utilisée. Sa signification ne change pas beaucoup en [POO](https://en.wikipedia.org/wiki/Object-oriented_programming). Mais, JavaScript n'avait pas de classes avant ES6 (bien qu'il avait toujours le mot-clé `this`).

La valeur de `this` en JavaScript est différente selon le contexte. Pour déterminer sa valeur, vous devez d'abord inspecter le **site d'appel** de la fonction où vous l'utilisez.

```js
function foo () {
   console.log( this.a );
}

// #1: Liaison par défaut
var a = 'bar';

// [site d'appel : global]
foo(); // 'bar' ou undefined (mode strict)
```

Cela semble étrange lorsque vous comparez ce comportement avec les normes POO. Cette première règle n'est pas si importante car la plupart des codes JavaScript utilisent le [mode strict](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode). De plus, grâce à ES6, les développeurs auront tendance à utiliser `let` et `const` au lieu de l'ancien `var`.

C'est la première règle qui est appliquée par défaut pour lier une valeur à `this`. Il y a 4 règles au total. Voici les 3 règles restantes :

```js
// Ce n'est pas facile à comprendre, copiez ce code et faites quelques tests !

// #2: Liaison implicite
const o2 = { a: 'o2', foo };
const o1 = { a: 'o1', o2 };

o1.o2.foo(); // [site d'appel : o2] 'o2'

// #3: Liaison explicite
const o = { a: 'bar' }; 
foo.call(o); // [site d'appel : o] 'bar'

const hardFoo = foo.bind(o); // [site d'appel : o]
hardFoo(); // [site d'appel : o] 'bar'

// #4: Nouvelle liaison
function foo() {
   this.a = 'bar';
}
let result = new foo(); // [site d'appel : new]
console.log(result.a); // 'bar'
```

La dernière **règle de nouvelle liaison** est la première règle que JavaScript essaie d'utiliser. Si cette règle ne s'applique pas, il reviendra aux autres règles : **liaison explicite**, **liaison implicite** et finalement **liaison par défaut**.

La chose la plus importante à retenir :

> this change avec le site d'appel de la fonction, les règles de liaison ont des priorités

Outre ces règles, il y a encore quelques cas particuliers. Cela devient un peu délicat lorsque certaines règles sont ignorées en fonction du site d'appel ou de la valeur de `this`.

```js
// 1- Problème de site d'appel
const o = { a: 'bar', foo };
callback(o.foo); // undefined

function callback(func){
  func(); // [site d'appel : callback]
}

// 2- La liaison par défaut n'est pas une liaison lexicale
var a = 'foo';
function bar(func){
   var a = 'bar'; // Ne remplace pas la valeur globale 'a' pour this
   func();
}
bar(foo); // 'foo'

// 3- this est null ou undefined
var a = 'foo';
foo.call(null); // 'foo' car le 'this' donné est null
```

C'est tout sur la liaison de `this`. Je suis d'accord, ce n'est pas facile à comprendre au premier abord mais après un certain temps, cela s'imprégnera. Vous devez faire l'effort d'apprendre comment cela fonctionne et pratiquer beaucoup.

Pour être honnête, c'est un résumé de l'ensemble du [troisième livre de la série](https://github.com/getify/You-Dont-Know-JS/tree/master/this%20%26%20object%20prototypes). N'hésitez pas à commencer par ce livre et à lire quelques chapitres. [Kyle](https://www.freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa/undefined) Simpson donne bien plus d'exemples et des explications très détaillées.

### LEÇON #7 — Modèle des promesses

Avant ES6, la manière courante de gérer la programmation asynchrone était d'utiliser des callbacks. Vous appelez une fonction qui ne peut pas fournir un résultat immédiatement, donc vous fournissez une fonction qu'elle appellera une fois qu'elle aura terminé.

Les promesses sont liées aux callbacks, mais elles vont les remplacer. Le concept de promesses n'est pas facile à saisir, alors prenez votre temps pour comprendre l'exemple et essayez-les !

#### Des callbacks aux promesses

Tout d'abord, parlons des callbacks. Avez-vous réalisé que les utiliser introduit une [inversion de contrôle](https://en.wikipedia.org/wiki/Inversion_of_control) (IoC) dans l'exécution du programme ? La fonction que vous appelez obtient le contrôle sur l'exécution de votre script.

```js
// Veuillez appeler 'eatPizza' une fois que vous avez terminé votre travail
orderPizza(eatPizza);

function orderPizza(callback) {
   // Vous ne savez pas ce qui se passe ici !
   callback(); // <- J'espère que c'est ça
}

function eatPizza() {
   console.log('Miam');
}
```

Vous mangerez votre pizza une fois qu'elle sera livrée et la commande terminée. Le processus derrière `orderPizza` n'est pas visible pour nous, mais c'est la même chose pour les fonctions des bibliothèques. Il peut appeler `eatPizza` plusieurs fois, pas du tout ou même attendre longtemps.

Avec les promesses, vous pouvez inverser l'IoC des callbacks. La fonction ne demandera pas de callback mais vous donnera une promesse. Ensuite, vous pouvez vous abonner pour être notifié après que la promesse soit résolue (soit avec succès soit avec échec).

```js
let promise = orderPizza(); // <- Pas de callback 

// S'abonne à la promesse
promise.then(eatPizza);     // Promesse tenue
promise.catch(stillHungry); // Promesse rejetée

function orderPizza() {
  return Promise.resolve(); // <- retourne la promesse
}
```

Les fonctions basées sur les callbacks demandent souvent deux callbacks (succès et échec) ou passent un paramètre au seul callback et vous laissent chercher les erreurs.

Avec les promesses, ces deux callbacks changent en `then` et `catch`. Cela correspond au succès et à l'échec mais les termes des promesses sont différents. Une **promesse tenue est un succès** (avec `then`) et une **promesse rejetée est un échec** (avec `catch`).

Selon l'API ou la bibliothèque que vous utilisez pour les promesses, le `catch` peut ne pas être disponible. Au lieu de cela, `then` prend deux fonctions comme arguments, et c'est le même modèle que pour les fonctions basées sur les callbacks.

Dans l'exemple, `orderPizza` retourne une promesse tenue. Habituellement, ce type de fonction asynchrone retourne une promesse en attente ([documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)). Mais, dans la plupart des cas, vous n'aurez pas besoin du constructeur de promesse car `Promise.resolve` et `Promise.reject` suffisent.

Une promesse n'est rien de plus qu'un objet avec une propriété d'état. La fonction que vous appelez change cet état de **en attente** à **tenue** ou **rejetée** une fois qu'elle a terminé son travail.

```js
// Fonction exécutée même s'il n'y a pas de then ou catch
let promise = Promise.resolve('Pizza');

// Ajoute des callbacks plus tard, appelés en fonction du statut de la promesse
promise.then(youEatOneSlice);
promise.then(yourFriendEatOneSlice);
promise.then(result => console.log(result)); // 'Pizza'

// La promesse est un objet (avec au moins une fonction then : c'est un objet thenable)
console.log(promise); // { state: 'fulfilled', value: 'Pizza' }
```

Vous pouvez joindre une valeur à une promesse. Elle est transmise aux callbacks abonnés comme paramètre (`then` et `catch`). Dans cet exemple, il y a deux abonnements sur le callback de réussite. Une fois la promesse tenue, les deux fonctions abonnées se déclenchent dans n'importe quel ordre.

**Pour résumer : il y a encore des callbacks avec les promesses.**

Mais les promesses agissent comme un tiers de confiance. Elles sont [immutables](https://en.wikipedia.org/wiki/Immutable_object) après achèvement et ne peuvent donc pas se résoudre plusieurs fois. De plus, dans la partie suivante, vous verrez qu'il est possible de réagir lorsqu'une promesse est encore en attente depuis longtemps.

Notez que vous pouvez transformer une fonction basée sur les callbacks en une fonction basée sur les promesses avec quelques lignes de code ([voir ce gist](https://gist.github.com/jbardon/dedede64f070de31a26e9d88d3ae0562)). Bien sûr, il y a des bibliothèques. Parfois, c'est aussi inclus dans l'API du langage (TypeScript a une fonction promisify).

#### Tirer parti de l'API Promise

Les callbacks et les promesses doivent tous deux gérer le problème des tâches asynchrones dépendantes. Cela se produit lorsque le résultat d'une première fonction asynchrone est nécessaire pour appeler une deuxième fonction asynchrone. De plus, la troisième fonction asynchrone a besoin du résultat de la deuxième fonction, et ainsi de suite...

Il est important de voir comment gérer correctement cette situation. C'est ce qui conduit à une base de code horrible. Regardez le code suivant, vous devriez être familier avec lui :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bn-bt2dZTNcZySovNCtONw.png)
_Un exemple d'enfer de callbacks_

Vous venez de rencontrer un [enfer de callbacks](https://en.wiktionary.org/wiki/callback_hell). Pour manger une pizza, le chef doit la cuisiner, puis l'emballer et le livreur la livrer à vous. Enfin, vous pouvez manger la pizza livrée.

Chaque étape est asynchrone et a besoin du résultat de l'étape précédente. C'est le point qui vous conduit à écrire du code d'enfer de callbacks. Les promesses peuvent l'éviter car elles peuvent soit retourner d'autres promesses soit des valeurs (emballées dans une promesse).

![Image](https://cdn-media-1.freecodecamp.org/images/1*DfRiJM9wpGaNF_PBzpGxFg.png)
_Chaîne de promesses avec raccourci syntaxique_

Ce snippet semble complexe et simple en même temps. Le code est petit mais il semble que nous ayons mis des choses magiques. Décomposons chaque étape et débarrassons-nous de la syntaxe ES6 pour clarifier :

```js
// Chaîne de promesses détaillée avec ES5, essayez la partie pratique !

const cookPromise = cookPizza();

const packPromise = cookPromise.then(function(pizza) {
    return pack(pizza); // Retourne une promesse stockée dans packPromise
});
  
const deliverPromise = packPromise.then(function (packedPizza) { // valeur de pack(pizza)
    return deliver(packedPizza);
});

deliverPromise.then(function (deliveredPizza) {
    return eat(deliveredPizza);
});

/* Pour vous entraîner */
// - Un exemple pour l'implémentation de cookPizza, pack, deliver et eat
//   Chaque fonction ajoute quelque chose à la chaîne de l'étape précédente
function pack(pizza) { 
    return Promise.resolve(pizza + ' pack');
}

// - Récupérer le résultat de eat et afficher la chaîne finale
//   Devrait être quelque chose comme : 'pizza pack deliver eat'
eatPromise.eat((result) => console.log(result));
```

Maintenant, vous avez la syntaxe courte et la plus verbeuse. Pour mieux comprendre ce morceau de code, vous devriez :

* Implémenter les fonctions `cookPizza`, `pack`, `deliver` et `eat`
* Vérifier que chaque fonction a changé la chaîne en utilisant `eatPromise`
* Refactoriser le code étape par étape pour obtenir la syntaxe courte

Il y a aussi l'usage régulier des promesses. L'[API Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference--/Global_Objects/Promise#Methods) fournit également des helpers pour gérer les conditions d'interaction de concurrence courantes telles que **gate**, **race** et **latch**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kmSMWUqTU_QnI9UYDs2YGw.png)

Dans cet exemple, seul le `then` est utilisé mais `catch` est également disponible. Pour `Promise.all`, il se déclenchera au lieu de `then` si au moins une promesse est rejetée.

Comme expliqué précédemment, vous pouvez utiliser les promesses pour "vérifier et agir lorsqu'une promesse est encore en attente depuis longtemps". C'est le cas d'utilisation courant pour `Promise.race`. Si vous voulez obtenir un exemple complet avec un timeout, consultez [cette partie](https://github.com/getify/You-Dont-Know-JS/blob/master/async%20%26%20performance/ch3.md#never-calling-the-callback) du livre.

#### Aller plus loin avec ES7

Dans certains codes, vous pourriez trouver des [**objets différés**](https://developer.mozilla.org/en-US/docs/Mozilla/JavaScript_code_modules/Promise.jsm/Deferred) pour gérer les promesses. Par exemple, AngularJS le fournit via le [$q service](https://docs.angularjs.org/api/ng/service/$q).

Les utiliser semble plus naturel et compréhensible mais ils ne le sont pas. Vous feriez mieux de prendre votre temps pour apprendre les promesses.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W5e2awkUrPHB2blVePE7rg.png)

Vous pourriez avoir besoin de retourner une promesse et de changer son état plus tard. Avant de choisir cette solution, assurez-vous qu'il n'y a pas d'autres moyens. De toute façon, l'API Promise ne retourne pas d'objets différés.

**N'utilisez pas d'objet différé. Si vous pensez en avoir besoin, repassez sur les promesses**

Mais vous pouvez utiliser le constructeur Promise pour imiter ce comportement. Consultez [ce gist](https://gist.github.com/jbardon/da9faa37cfc8cf31c2726cca1923262c) pour en savoir plus mais souvenez-vous — c'est mauvais !

Enfin, ES7 a introduit une nouvelle manière de gérer les promesses en tirant parti de la [syntaxe des générateurs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*). Elle vous permet de faire en sorte que les fonctions asynchrones ressemblent à des fonctions synchrones régulières.

```js
// Syntaxe ES6
function load() { 
  return Promise.all([foo(), bar()])
    .then(console.log);
}
load();

// Syntaxe ES7
async function load() { 
  let a = await foo();
  
  // Arrive ici une fois que 'foo' est résolu puis appelle 'bar'
  let b = await bar(); 
  console.log(a, b);
}
load();
```

Marquez `load` qui appelle les fonctions asynchrones `foo` et `bar` avec le mot-clé `async`. Et mettez `await` avant les appels asynchrones. Vous pourrez utiliser `load` comme avant, avec un classique `load()`.

Cette syntaxe est attrayante, n'est-ce pas ? Plus de callback et d'enfer de promesses avec une indentation infinie. Mais attendez, vous devriez considérer comment les générateurs fonctionnent pour éviter les problèmes de performances.

Dans l'exemple ci-dessus, `bar` n'est exécuté qu'une fois que la promesse `foo` est résolue. Leur exécution n'est pas parallélisée. Vous obtiendrez le même résultat exact en écrivant quelque chose comme `foo.then(bar)`.

Voici comment le corriger :

```js
async function load() {
   let fooPromise = foo();
   let barPromise = bar();
  
   // foo et bar sont exécutés avant Promise.all
   let results = await Promise.all([fooPromise, barPromise]);
   console.log(results);
}
load();
```

Utilisez `Promise.all`. En fait, `await` signifie que vous voulez exécuter votre fonction étape par étape. D'abord, du début au premier `await`. Une fois que la promesse du premier `await` est résolue, elle reprendra la fonction jusqu'au mot-clé `await` suivant. Ou jusqu'à la fin de la fonction s'il n'y en a plus.

Dans cet exemple, `foo` et `bar` s'exécutent pendant la première étape. La fonction `load` fait une pause sur `Promise.all`. À ce stade, `foo` et `bar` ont déjà commencé leur travail.

C'était une introduction rapide aux promesses avec quelques notes sur les pièges que vous ne voulez pas rencontrer. Cela résume le [cinquième livre de la série](https://github.com/getify/You-Dont-Know-JS/tree/master/async%20%26%20performance) qui décrit en profondeur les modèles asynchrones et les promesses.

Vous pouvez également consulter [cet article](https://medium.com/@pyrolistical/how-to-get-out-of-promise-hell-8c20e0ab0513) de [Ronald Chen](https://www.freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa/undefined). Il rassemble de nombreux anti-modèles de promesses. Cet article vous aidera à échapper à l'enfer des promesses.

### Conclusion

Ce sont les leçons les plus importantes que j'ai apprises en lisant [You Don't Know JS](https://github.com/getify/You-Dont-Know-JS). Cette série de livres a bien plus de leçons et de détails à vous enseigner sur le fonctionnement de JavaScript.

Juste un avertissement : pour moi, c'était parfois difficile à suivre lorsque l'auteur cite la spécification ECMAScript et des exemples longs. Les livres sont longs, c'est sûr, mais aussi très complets. D'ailleurs, j'ai presque abandonné mais finalement, j'ai continué à lire jusqu'à la fin et je peux vous dire — ça en valait la peine.

Ce n'est pas une sorte de publicité pour [Kyle](https://www.freecodecamp.org/news/you-might-not-know-js-insights-from-the-javascript-bible-2ee9518302aa/undefined). J'aime juste cette série et la considère comme une référence. De plus, elle est gratuite à lire et à contribuer à la série via le [dépôt GitHub](https://github.com/getify/You-Dont-Know-JS).

**Si vous avez trouvé cet article utile, veuillez cliquer sur le bouton** ? **plusieurs fois pour aider les autres à trouver l'article et montrer votre soutien !** ?

**N'oubliez pas de me suivre pour être notifié de mes prochains articles** ?

### Consultez mes [Autres](https://www.freecodecamp.org/news/author/jbardon/) Articles

#### ➡ JavaScript

* [Série React pour débutants](https://medium.freecodecamp.org/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44)
* [Comment améliorer vos compétences en JavaScript en écrivant votre propre framework de développement web](https://medium.freecodecamp.org/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190)
* [Erreurs courantes à éviter lors de l'utilisation de Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)

#### ➡ Astuces et conseils

* [Comment maîtriser IntelliJ pour booster votre productivité](https://medium.freecodecamp.org/how-to-master-intellij-to-boost-your-productivity-44b9da20c556)
* [Arrêtez le débogage JavaScript douloureux et adoptez Intellij avec Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [Comment réduire les bundles JavaScript énormes sans effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)