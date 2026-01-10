---
title: Apprendre les fermetures JavaScript avec des exemples de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-29T15:30:09.000Z'
originalURL: https://freecodecamp.org/news/lets-learn-javascript-closures-66feb44f6a44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bSMhqCAGeHAqbPS6qQMe5Q.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
seo_title: Apprendre les fermetures JavaScript avec des exemples de code
seo_desc: 'By Preethi Kasireddy

  Closures are a fundamental JavaScript concept that every serious programmer should
  know inside and out.

  The Internet is packed with great explanations of “what” closures are, but few deep-dive
  into the “why” side of things.

  I fin...'
---

Par Preethi Kasireddy

Les fermetures sont un concept fondamental de JavaScript que tout programmeur sérieux devrait maîtriser.

Internet regorge d'excellentes explications sur "ce que" sont les fermetures, mais peu approfondissent le "pourquoi".

Je pense que comprendre les rouages donne aux développeurs une meilleure maîtrise de leurs outils, donc cet article sera dédié aux détails de _comment_ et _pourquoi_ les fermetures fonctionnent comme elles le font.

Espérons que vous repartirez mieux équipé pour tirer parti des fermetures dans votre travail quotidien. Commençons !

# **Qu'est-ce qu'une fermeture ?**

Les fermetures sont une propriété extrêmement puissante de JavaScript (et de la plupart des langages de programmation). Selon la définition de [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures) :

_Les fermetures sont des **fonctions** qui **référencent** des variables indépendantes **(libres)**. En d'autres termes, la fonction définie dans la fermeture "se souvient" de l'environnement dans lequel elle a été créée._

Note : Les variables libres sont des variables qui ne sont ni déclarées localement ni passées en paramètre.

Regardons quelques exemples :

## **Exemple 1 :**

```js
function numberGenerator() {
  // Variable locale "libre" qui se retrouve dans la fermeture
  var num = 1;
  function checkNumber() { 
    console.log(num);
  }
  num++;
  return checkNumber;
}

var number = numberGenerator();
number(); // 2
```

Dans l'exemple ci-dessus, la fonction numberGenerator crée une variable locale "libre" **num** (un nombre) et **checkNumber** (une fonction qui affiche **num** dans la console).

La fonction **checkNumber** n'a aucune variable locale propre — cependant, elle a accès aux variables de la fonction externe, **numberGenerator**, grâce à une fermeture.

Par conséquent, elle peut utiliser la variable **num** déclarée dans **numberGenerator** pour l'afficher dans la console _même après_ que **numberGenerator** a retourné.

## **Exemple 2 :**

Dans cet exemple, nous démontrons qu'une fermeture contient toutes les variables locales déclarées dans la fonction externe.

```js
function sayHello() {
  var say = function() { console.log(hello); }
  // Variable locale qui se retrouve dans la fermeture
  var hello = 'Hello, world!';
  return say;
}
var sayHelloClosure = sayHello(); 
sayHelloClosure(); // 'Hello, world!'
```

Remarquez comment la variable **hello** est définie _après_ la fonction anonyme — mais peut toujours accéder à la variable **hello**. Cela est dû au fait que la variable **hello** a déjà été définie dans la "portée" de la fonction au moment de sa création, la rendant disponible lorsque la fonction anonyme est finalement exécutée.

(Ne vous inquiétez pas, j'expliquerai ce que signifie "portée" plus tard dans l'article. Pour l'instant, suivez simplement !)

## **Comprendre le niveau supérieur**

Ces exemples ont illustré "ce que" sont les fermetures à un niveau élevé. Le thème général est le suivant : _nous avons accès aux variables définies dans la ou les fonctions englobantes même après que la fonction englobante qui définit ces variables a retourné._

Clairement, quelque chose se passe en arrière-plan qui permet à ces variables de rester accessibles longtemps après que la fonction englobante qui les a définies a retourné.

Pour comprendre comment cela est possible, nous devons aborder quelques concepts connexes — en commençant à 3000 mètres d'altitude et en redescendant lentement vers le monde des fermetures. Commençons par le _contexte_ global dans lequel une fonction est exécutée, connu sous le nom de "Contexte d'exécution".

# **Contexte d'exécution**

Le contexte d'exécution est un concept abstrait utilisé par la spécification ECMAScript pour suivre l'évaluation du code à l'exécution. Cela peut être le contexte global dans lequel votre code est exécuté pour la première fois ou lorsque le flux d'exécution entre dans le corps d'une fonction.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-147.png)

À tout moment, il ne peut y avoir qu'un seul contexte d'exécution en cours. C'est pourquoi JavaScript est "mono-thread", ce qui signifie qu'une seule commande peut être traitée à la fois.

Typiquement, les navigateurs maintiennent ce contexte d'exécution à l'aide d'une "pile". Une pile est une structure de données Last In First Out (LIFO), ce qui signifie que la dernière chose que vous avez poussée sur la pile est la première à en être retirée. (C'est parce que nous ne pouvons insérer ou supprimer des éléments qu'au sommet de la pile.)

Le contexte d'exécution actuel ou "en cours" est toujours l'élément du haut de la pile. Il est retiré du sommet lorsque le code dans le contexte d'exécution en cours a été complètement évalué, permettant à l'élément suivant du haut de prendre le relais en tant que contexte d'exécution en cours.

De plus, simplement parce qu'un contexte d'exécution est en cours ne signifie pas qu'il doit terminer son exécution avant qu'un autre contexte d'exécution puisse s'exécuter.

Il arrive que le contexte d'exécution en cours soit suspendu et qu'un autre contexte d'exécution devienne le contexte d'exécution en cours. Le contexte d'exécution suspendu peut alors, à un moment ultérieur, reprendre là où il s'était arrêté.

Chaque fois qu'un contexte d'exécution est remplacé par un autre de cette manière, un nouveau contexte d'exécution est créé et poussé sur la pile, devenant le contexte d'exécution actuel.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-148.png)

Pour un exemple pratique de ce concept en action dans le navigateur, voir l'exemple ci-dessous :

```js
var x = 10;
function foo(a) {
  var b = 20;

  function bar(c) {
    var d = 30;
    return boop(x + a + b + c + d);
  }

  function boop(e) {
    return e * -1;
  }

  return bar;
}

var moar = foo(5); // Fermeture
/*
  La fonction ci-dessous exécute la fonction bar qui a été retournée
  lorsque nous avons exécuté la fonction foo dans la ligne ci-dessus. La fonction bar
  invoque boop, moment auquel bar est suspendue et boop est poussée
  au sommet de la pile d'appels (voir la capture d'écran ci-dessous)
*/
moar(15);
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-149.png)

Ensuite, lorsque **boop** retourne, elle est retirée de la pile et **bar** reprend :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-150.png)

Lorsque nous avons une série de contextes d'exécution s'exécutant les uns après les autres — souvent suspendus au milieu puis repris plus tard — nous avons besoin d'un moyen de suivre l'état afin de gérer l'ordre et l'exécution de ces contextes.

Et c'est en effet le cas. Selon la spécification ECMAScript, chaque contexte d'exécution possède divers composants d'état utilisés pour suivre les progrès du code dans chaque contexte. Ceux-ci incluent :

* **État d'évaluation du code** : Tout état nécessaire pour effectuer, suspendre et reprendre l'évaluation du code associé à ce contexte d'exécution
* **Fonction** : L'objet fonction que le contexte d'exécution évalue (ou null si le contexte évalué est un _script_ ou un _module_)
* **Royaume** : Un ensemble d'objets internes, un environnement global ECMAScript, tout le code ECMAScript chargé dans la portée de cet environnement global, et d'autres états et ressources associés
* **Environnement lexical** : Utilisé pour résoudre les références d'identifiants faites par le code dans ce contexte d'exécution.
* **Environnement de variable** : Environnement lexical dont l'EnvironmentRecord contient les liaisons créées par les VariableStatements dans ce contexte d'exécution.

Si cela vous semble trop confus, ne vous inquiétez pas. Parmi toutes ces variables, la variable Environnement Lexical est celle qui nous intéresse le plus car elle indique explicitement qu'elle résout les "références d'identifiants" faites par le code dans ce contexte d'exécution.

Vous pouvez penser aux "identifiants" comme des variables. Puisque notre objectif initial était de comprendre comment il est possible d'accéder magiquement aux variables même après qu'une fonction (ou "contexte") a retourné, l'Environnement Lexical semble être quelque chose que nous devrions approfondir !

**_Note_** : _Techniquement, l'Environnement de Variable et l'Environnement Lexical sont tous deux utilisés pour implémenter les fermetures. Mais pour simplifier, nous les généraliserons en un "Environnement". Pour une explication détaillée sur la différence entre l'Environnement Lexical et l'Environnement de Variable, voir l'excellent_ [_article_](http://www.2ality.com/2011/04/ecmascript-5-spec-lexicalenvironment.html) _du Dr. Alex Rauschmayer._

# **Environnement Lexical**

Par définition :

> _Un Environnement Lexical est un type de spécification utilisé pour définir l'association des Identifiants à des variables et fonctions spécifiques basées sur la structure de nidification lexicale du code ECMAScript. Un Environnement Lexical se compose d'un Environment Record et d'une référence éventuellement nulle à un Environnement Lexical externe. Habituellement, un Environnement Lexical est associé à une structure syntaxique spécifique du code ECMAScript telle qu'une FunctionDeclaration, une BlockStatement, ou une clause Catch d'une TryStatement et un nouvel Environnement Lexical est créé chaque fois que ce code est évalué. —_ [_ECMAScript-262/6.0_](http://www.ecma-international.org/ecma-262/6.0/#sec-lexical-environments)

Décomposons cela.

* **"Utilisé pour définir l'association des Identifiants"** : Le but d'un Environnement Lexical est de gérer les données (c'est-à-dire les identifiants) dans le code. En d'autres termes, il donne un sens aux identifiants. Par exemple, si nous avions une ligne de code "_console.log(x / 10)_", il est sans signification d'avoir une variable (ou "identifiant") **x** sans quelque chose qui donne un sens à cette variable. L'Environnement Lexical fournit ce sens (ou "association") via son Environment Record (voir ci-dessous).
* **"L'Environnement Lexical se compose d'un Environment Record"** : Un Environment Record est une manière sophistiquée de dire qu'il conserve un enregistrement de tous les identifiants et leurs liaisons qui existent dans un Environnement Lexical. Chaque Environnement Lexical a son propre Environment Record.
* **"Structure de nidification lexicale"** : C'est la partie intéressante, qui dit essentiellement qu'un environnement interne référence l'environnement externe qui l'entoure, et que cet environnement externe peut avoir son propre environnement externe. Par conséquent, un environnement peut servir d'environnement externe pour plus d'un environnement interne. L'environnement global est le seul Environnement Lexical qui n'a pas d'environnement externe. Le langage ici est trompeur, alors utilisons une métaphore et pensons aux environnements lexicaux comme aux couches d'un oignon : l'environnement global est la couche la plus externe de l'oignon ; chaque couche suivante en dessous est imbriquée à l'intérieur.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-151.png)

Abstraitement, l'environnement ressemble à ceci en pseudocode :

```js
LexicalEnvironment = {
  EnvironmentRecord: {
  // Les liaisons d'identifiants vont ici
  },
  
  // Référence à l'environnement externe
  outer: < >
};
```

* **"Un nouvel Environnement Lexical est créé chaque fois que ce code est évalué"** : Chaque fois qu'une fonction externe englobante est appelée, un nouvel environnement lexical est créé. C'est important — nous reviendrons sur ce point à la fin. _(Note de côté : une fonction n'est pas la seule façon de créer un Environnement Lexical. D'autres incluent une instruction de bloc ou une clause catch. Pour simplifier, je me concentrerai sur les environnements créés par des fonctions tout au long de cet article)_

En bref, chaque contexte d'exécution a un Environnement Lexical. Cet Environnement Lexical contient des variables et leurs valeurs associées, et a également une référence à son environnement externe.

L'Environnement Lexical peut être l'environnement global, un environnement de module (qui contient les liaisons pour les déclarations de niveau supérieur d'un Module), ou un environnement de fonction (environnement créé en raison de l'invocation d'une fonction).

# **Chaîne de portée**

Sur la base de la définition ci-dessus, nous savons qu'un environnement a accès à l'environnement de son parent, et que l'environnement parent a accès à l'environnement de son parent, et ainsi de suite. Cet ensemble d'identifiants auxquels chaque environnement a accès est appelé "portée". Nous pouvons imbriquer ces portées dans une chaîne hiérarchique d'environnements connue sous le nom de "chaîne de portée".

Regardons un exemple de cette structure d'imbrication :

```js
var x = 10;

function foo() {
  var y = 20; // variable libre
  function bar() {
    var z = 15; // variable libre
    return x + y + z;
  }
  return bar;
}
```

Comme vous pouvez le voir, **bar** est imbriqué dans **foo**. Pour vous aider à visualiser l'imbrication, voir le diagramme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-152.png)

Nous reviendrons sur cet exemple plus tard dans l'article.

Cette chaîne de portée, ou chaîne d'environnements associée à une fonction, est enregistrée dans l'objet fonction au moment de sa création. En d'autres termes, elle est définie statiquement par l'emplacement dans le code source. (C'est aussi ce qu'on appelle le "scoping lexical".)

Faisons un petit détour pour comprendre la différence entre "portée dynamique" et "portée statique", ce qui aidera à clarifier pourquoi la portée statique (ou portée lexicale) est nécessaire pour avoir des fermetures.

# **Détour : Portée dynamique vs. Portée statique**

Les langages à portée dynamique ont des "implémentations basées sur la pile", ce qui signifie que les variables locales et les arguments des fonctions sont stockés sur une pile. Par conséquent, l'état d'exécution de la pile du programme détermine à quelle variable vous faites référence.

D'autre part, la portée statique est lorsque les variables référencées dans un contexte sont enregistrées au _moment de la création_. En d'autres termes, la structure du code source du programme détermine à quelles variables vous faites référence.

À ce stade, vous vous demandez peut-être comment la portée dynamique et la portée statique sont différentes. Voici deux exemples pour illustrer :

## **Exemple 1 :**

```js
var x = 10;

function foo() {
  var y = x + 5;
  return y;
}
 
function bar() {
  var x = 2;
  return foo();
}
 
function main() {
  foo(); // Portée statique : 15 ; Portée dynamique : 15
  bar(); // Portée statique : 15 ; Portée dynamique : 7
  return 0;
}
```

Nous voyons ci-dessus que la portée statique et la portée dynamique retournent des valeurs différentes lorsque la fonction bar est invoquée.

Avec la portée statique, la valeur de retour de **bar** est basée sur la valeur de **x** au moment de la création de **foo**. Cela est dû à la structure statique et lexicale du code source, ce qui fait que **x** est 10 et le résultat est 15.

La portée dynamique, en revanche, nous donne une pile de définitions de variables suivies à l'exécution — de sorte que le **x** que nous utilisons dépend de ce qui est exactement dans la portée et a été défini dynamiquement à l'exécution. L'exécution de la fonction **bar** pousse x = 2 au sommet de la pile, faisant retourner 7 à **foo**.

## **Exemple 2 :**

```js
var myVar = 100;
 
function foo() {
  console.log(myVar);
}
 
foo(); // Portée statique : 100 ; Portée dynamique : 100
 
(function () {
  var myVar = 50;
  foo(); // Portée statique : 100 ; Portée dynamique : 50
})();

// Fonction d'ordre supérieur
(function (arg) {
  var myVar = 1500;
  arg();  // Portée statique : 100 ; Portée dynamique : 1500
})(foo);
```

De même, dans l'exemple de portée dynamique ci-dessus, la variable **myVar** est résolue en utilisant la valeur de **myVar** à l'endroit où la fonction est appelée. La portée statique, en revanche, résout **myVar** à la variable qui a été enregistrée dans la portée des deux fonctions IIFE _au moment de la création_.

Comme vous pouvez le voir, la portée dynamique conduit souvent à une certaine ambiguïté. Il n'est pas exactement clair à quelle portée la variable libre sera résolue.

# **Fermetures**

Certaines de ces informations peuvent vous sembler hors sujet, mais nous avons en fait couvert tout ce que nous devons savoir pour comprendre les fermetures :

_Toute fonction a un contexte d'exécution, qui comprend un environnement qui donne un sens aux variables de cette fonction et une référence à l'environnement de son parent. Une référence à l'environnement du parent rend toutes les variables de la portée du parent disponibles pour toutes les fonctions internes, indépendamment du fait que la ou les fonctions internes soient invoquées à l'extérieur ou à l'intérieur de la portée dans laquelle elles ont été créées._

_Il semble donc que la fonction "se souvienne" de cet environnement (ou portée) car la fonction a littéralement une référence à cet environnement (et aux variables définies dans cet environnement) !_

Revenons à l'exemple de structure imbriquée :

```js
var x = 10;

function foo() {
  var y = 20; // variable libre
  function bar() {
    var z = 15; // variable libre
    return x + y + z;
  }
  return bar;
}

var test = foo();

test(); // 45
```

Sur la base de notre compréhension du fonctionnement des environnements, nous pouvons dire que les définitions d'environnement pour l'exemple ci-dessus ressemblent à ceci (notez que ceci est du pseudocode) :

```js
GlobalEnvironment = {
  EnvironmentRecord: { 
    // identifiants intégrés
    Array: '<func>',
    Object: '<func>',
    // etc..
    
    // identifiants personnalisés
    x: 10
  },
  outer: null
};
 
fooEnvironment = {
  EnvironmentRecord: {
    y: 20,
    bar: '<func>'
  }
  outer: GlobalEnvironment
};

barEnvironment = {
  EnvironmentRecord: {
    z: 15
  }
  outer: fooEnvironment
};
```

Lorsque nous invoquons la fonction **test**, nous obtenons 45, qui est la valeur de retour de l'invocation de la fonction **bar** (parce que **foo** a retourné **bar**). **bar** a accès à la variable libre **y** même après que la fonction **foo** a retourné parce que **bar** a une référence à **y** par le biais de son environnement externe, qui est l'environnement de **foo** ! **bar** a également accès à la variable globale **x** parce que l'environnement de **foo** a accès à l'environnement global. Cela s'appelle la _"recherche dans la chaîne de portée"_.

Revenant à notre discussion sur la portée dynamique vs la portée statique : pour que les fermetures soient implémentées, nous ne pouvons pas utiliser la portée dynamique via une pile dynamique pour stocker nos variables.

La raison est que cela signifierait que lorsque une fonction retourne, les variables seraient retirées de la pile et ne seraient plus disponibles — ce qui contredit notre définition initiale d'une fermeture.

Ce qui se passe à la place, c'est que les données de fermeture du contexte parent sont sauvegardées dans ce qu'on appelle le "tas", ce qui permet aux données de persister après que l'appel de fonction qui les a créées retourne (c'est-à-dire même après que le contexte d'exécution est retiré de la pile d'appels d'exécution).

Cela a du sens ? Bien ! Maintenant que nous comprenons les rouages à un niveau abstrait, regardons quelques exemples supplémentaires :

## **Exemple 1 :**

Un exemple/malentendu canonique est lorsqu'il y a une boucle for et que nous essayons d'associer la variable de compteur dans la boucle for à une fonction dans la boucle for :

```js
var result = [];
 
for (var i = 0; i < 5; i++) {
  result[i] = function () {
    console.log(i);
  };
}

result[0](); // 5, attendu 0
result[1](); // 5, attendu 1
result[2](); // 5, attendu 2
result[3](); // 5, attendu 3
result[4](); // 5, attendu 4
```

En revenant à ce que nous venons d'apprendre, il devient super facile de repérer l'erreur ici ! Abstraitement, voici à quoi ressemble l'environnement au moment où la boucle for se termine :

```js
environment: {
  EnvironmentRecord: {
    result: [...],
    i: 5
  },
  outer: null,
}
```

L'hypothèse incorrecte ici était que la portée est différente pour les cinq fonctions dans le tableau result. Au lieu de cela, ce qui se passe réellement est que l'environnement (ou contexte/portée) est le même pour les cinq fonctions dans le tableau result. Par conséquent, chaque fois que la variable **i** est incrémentée, elle met à jour la portée — qui est partagée par toutes les fonctions. C'est pourquoi l'une des 5 fonctions essayant d'accéder à **i** retourne 5 (i est égal à 5 lorsque la boucle for se termine).

Une façon de corriger cela est de créer un contexte englobant supplémentaire pour chaque fonction afin qu'elles obtiennent chacune leur propre contexte d'exécution/portée :

```js
var result = [];
 
for (var i = 0; i < 5; i++) {
  result[i] = (function inner(x) {
    // contexte englobant supplémentaire
    return function() {
      console.log(x);
    }
  })(i);
}

result[0](); // 0, attendu 0
result[1](); // 1, attendu 1
result[2](); // 2, attendu 2
result[3](); // 3, attendu 3
result[4](); // 4, attendu 4
```

Hourra ! C'est corrigé :)

Une autre approche, plutôt astucieuse, consiste à utiliser **let** au lieu de **var**, puisque **let** est limité à la portée du bloc et qu'une nouvelle liaison d'identifiant est créée pour chaque itération dans la boucle for :

```js
var result = [];
 
for (let i = 0; i < 5; i++) {
  result[i] = function () {
    console.log(i);
  };
}

result[0](); // 0, attendu 0
result[1](); // 1, attendu 1
result[2](); // 2, attendu 2
result[3](); // 3, attendu 3
result[4](); // 4, attendu 4
```

Tada ! :)

## **Exemple 2 :**

Dans cet exemple, nous montrerons comment chaque _appel_ à une fonction crée une nouvelle fermeture séparée :

```js
function iCantThinkOfAName(num, obj) {
  // Cette variable de tableau, ainsi que les 2 paramètres passés,
  // sont 'capturés' par la fonction imbriquée 'doSomething'
  var array = [1, 2, 3];
  function doSomething(i) {
    num += i;
    array.push(num);
    console.log('num: ' + num);
    console.log('array: ' + array);
    console.log('obj.value: ' + obj.value);
  }
  
  return doSomething;
}

var referenceObject = { value: 10 };
var foo = iCantThinkOfAName(2, referenceObject); // fermeture #1
var bar = iCantThinkOfAName(6, referenceObject); // fermeture #2

foo(2);
/*
  num: 4
  array: 1,2,3,4
  obj.value: 10
*/

bar(2);
/*
  num: 8
  array: 1,2,3,8
  obj.value: 10
*/

referenceObject.value++;

foo(4);
/*
  num: 8
  array: 1,2,3,4,8
  obj.value: 11
*/

bar(4);
/*
  num: 12
  array: 1,2,3,8,12
  obj.value: 11
*/
```

Dans cet exemple, nous pouvons voir que chaque appel à la fonction **iCantThinkOfAName** crée une nouvelle fermeture, à savoir **foo** et **bar**. Les invocations ultérieures à l'une ou l'autre des fonctions de fermeture mettent à jour les variables de fermeture au sein de cette fermeture elle-même, démontrant que les variables dans _chaque_ fermeture continuent d'être utilisables par la fonction **doSomething** de **iCantThinkOfAName** longtemps après que **iCantThinkOfAName** retourne.

## **Exemple 3 :**

```js
function mysteriousCalculator(a, b) {
	var mysteriousVariable = 3;
	return {
		add: function() {
			var result = a + b + mysteriousVariable;
			return toFixedTwoPlaces(result);
		},
		
		subtract: function() {
			var result = a - b - mysteriousVariable;
			return toFixedTwoPlaces(result);
		}
	}
}

function toFixedTwoPlaces(value) {
	return value.toFixed(2);
}

var myCalculator = mysteriousCalculator(10.01, 2.01);
myCalculator.add() // 15.02
myCalculator.subtract() // 5.00
```

Ce que nous pouvons observer, c'est que **mysteriousCalculator** est dans la portée globale, et il retourne deux fonctions. Abstraitement, les environnements pour l'exemple ci-dessus ressemblent à ceci :

```js
GlobalEnvironment = {
  EnvironmentRecord: { 
    // identifiants intégrés
    Array: '<func>',
    Object: '<func>',
    // etc...

    // identifiants personnalisés
    mysteriousCalculator: '<func>',
    toFixedTwoPlaces: '<func>',
  },
  outer: null,
};
 
mysteriousCalculatorEnvironment = {
  EnvironmentRecord: {
    a: 10.01,
    b: 2.01,
    mysteriousVariable: 3,
  }
  outer: GlobalEnvironment,
};

addEnvironment = {
  EnvironmentRecord: {
    result: 15.02
  }
  outer: mysteriousCalculatorEnvironment,
};

subtractEnvironment = {
  EnvironmentRecord: {
    result: 5.00
  }
  outer: mysteriousCalculatorEnvironment,
};
```

Parce que nos fonctions **add** et **subtract** ont une référence à l'environnement de la fonction **mysteriousCalculator**, elles sont capables d'utiliser les variables de cet environnement pour calculer le résultat.

## **Exemple 4 :**

Un dernier exemple pour démontrer une utilisation importante des fermetures : maintenir une référence privée à une variable dans la portée externe.

```js
function secretPassword() {
  var password = 'xh38sk';
  return {
    guessPassword: function(guess) {
      if (guess === password) {
        return true;
      } else {
        return false;
      }
    }
  }
}

var passwordGame = secretPassword();
passwordGame.guessPassword('heyisthisit?'); // false
passwordGame.guessPassword('xh38sk'); // true
```

C'est une technique très puissante — elle donne à la fonction de fermeture **guessPassword** un accès exclusif à la variable **password**, tout en rendant impossible l'accès au **password** depuis l'extérieur.

# **TL;DR**

* Le contexte d'exécution est un concept abstrait utilisé par la spécification ECMAScript pour suivre l'évaluation du code à l'exécution. À tout moment, il ne peut y avoir qu'un seul contexte d'exécution qui exécute du code.
* Chaque contexte d'exécution a un Environnement Lexical. Cet Environnement Lexical contient des liaisons d'identifiants (c'est-à-dire des variables et leurs valeurs associées), et a également une référence à son environnement externe.
* L'ensemble des identifiants auxquels chaque environnement a accès est appelé "portée". Nous pouvons imbriquer ces portées dans une chaîne hiérarchique d'environnements, connue sous le nom de "chaîne de portée".
* Chaque fonction a un contexte d'exécution, qui comprend un Environnement Lexical qui donne un sens aux variables de cette fonction et une référence à l'environnement de son parent. Et ainsi, il semble que la fonction "se souvienne" de cet environnement (ou portée) car la fonction a littéralement une référence à cet environnement. C'est une fermeture.
* Une fermeture est créée chaque fois qu'une fonction externe englobante est appelée. En d'autres termes, la fonction interne n'a pas besoin de retourner pour qu'une fermeture soit créée.
* La portée d'une fermeture en JavaScript est lexicale, ce qui signifie qu'elle est définie statiquement par son emplacement dans le code source.
* Les fermetures ont de nombreux cas d'utilisation pratiques. Un cas d'utilisation important est de maintenir une référence privée à une variable dans la portée externe.

# **Remarques de clôt(ure)**

J'espère que cet article a été utile et vous a donné un modèle mental de la façon dont les fermetures sont implémentées en JavaScript. Comme vous pouvez le voir, comprendre les rouages de leur fonctionnement facilite grandement la détection des fermetures — sans parler de l'économie de nombreux maux de tête lorsqu'il est temps de déboguer.

PS : Je suis humain et je fais des erreurs — donc si vous trouvez des erreurs, j'adorerais que vous me le fassiez savoir !

## **Lectures complémentaires**

Pour des raisons de brièveté, j'ai omis quelques sujets qui pourraient intéresser certains lecteurs. Voici quelques liens que je voulais partager :

* **Qu'est-ce que le VariableEnvironment dans un contexte d'exécution ?** Le Dr. Axel Rauschmayer fait un travail phénoménal en l'expliquant, donc je vous laisse avec un lien vers son article de blog : [http://www.2ality.com/2011/04/ecmascript-5-spec-lexicalenvironment.html](http://www.2ality.com/2011/04/ecmascript-5-spec-lexicalenvironment.html)
* **Quels sont les différents types d'Environment Records ?** Lisez la spécification ici : [http://www.ecma-international.org/ecma-262/6.0/#sec-environment-records](http://www.ecma-international.org/ecma-262/6.0/#sec-environment-records)
* **Excellent article de MDN sur les fermetures** : [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* D'autres ? Veuillez suggérer et je les ajouterai !