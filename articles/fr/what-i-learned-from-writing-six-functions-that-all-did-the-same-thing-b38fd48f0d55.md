---
title: Ce que j'ai appris en écrivant six fonctions qui faisaient toutes la même chose
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-30T08:59:34.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-writing-six-functions-that-all-did-the-same-thing-b38fd48f0d55
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BM1TcQvHNMc09jc4GxG-7w.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Ce que j'ai appris en écrivant six fonctions qui faisaient toutes la même
  chose
seo_desc: 'By Jackson Bates

  A couple weeks ago, a camper started an unofficial algorithm competition on Free
  Code Camp’s Forum.

  The challenge seemed simple enough: return the sum of all multiples of 3 or 5 that
  are below a number N, where N is an input paramete...'
---

Par Jackson Bates

Il y a quelques semaines, un campeur a lancé une compétition d'algorithmes non officielle sur le [Forum de Free Code Camp](http://forum.freecodecamp.com/t/javascript-algorithm-challenge-october-9-through-16/44096?u=jacksonbates).

Le défi semblait assez simple : retourner la somme de tous les multiples de 3 ou 5 qui sont inférieurs à un nombre N, où N est un paramètre d'entrée de la fonction.

Mais au lieu de simplement trouver une solution, la compétition de [P1xt](https://www.freecodecamp.org/news/what-i-learned-from-writing-six-functions-that-all-did-the-same-thing-b38fd48f0d55/undefined) exigeait de se concentrer sur l'efficacité. Elle encourageait à écrire ses propres tests et à évaluer les performances de ses solutions.

Voici une analyse de toutes les fonctions que j'ai essayées et testées, y compris mes tests et mes scripts de benchmark. À la fin, je montrerai la fonction qui a surpassé toutes les miennes et m'a appris une leçon précieuse.

### Fonction #1 : Tableau, push, incrément

```javascript
function arrayPushAndIncrement(n) {
	var array = [];
    var result = 0;
    for (var i = 1; i < n; i ++) {
        if (i % 3 == 0 || i % 5 == 0) {
            array.push(i);
        }
    }
    for (var num of array) {
        result += num;
    }
    return result;
}

module.exports = arrayPushAndIncrement; // ceci est nécessaire pour les tests
```

Pour des problèmes comme celui-ci, mon cerveau opte par défaut pour : construire un tableau, puis faire quelque chose avec ce tableau.

Cette fonction crée un tableau et y ajoute tous les nombres qui répondent à notre condition (divisibles par 3 ou 5). Elle parcourt ensuite ce tableau en additionnant toutes les valeurs.

### Configuration des tests

Voici les tests automatisés pour cette fonction, qui utilisent Mocha et Chai, exécutés sur NodeJS.

Si vous souhaitez plus d'informations sur l'installation de Mocha et Chai, j'ai écrit [un guide détaillé](http://forum.freecodecamp.com/t/testing-your-own-code-using-mocha-and-chai-simple-example/44149?u=jacksonbates) sur le forum de Free Code Camp.

J'ai écrit un script de test simple en utilisant les valeurs fournies par [P1xt](https://www.freecodecamp.org/news/what-i-learned-from-writing-six-functions-that-all-did-the-same-thing-b38fd48f0d55/undefined). Remarquez que dans le script ci-dessous, la fonction est incluse en tant que module :

```js
// testMult.js

var should = require( 'chai' ).should();
var arrayPushAndIncrement = require( './arrayPushAndIncrement' );

describe('arrayPushAndIncrement', function() {
    it('should return 23 when passed 10', function() {
    	arrayPushAndIncrement(10).should.equal(23);
    })
    it('should return 78 when passed 20', function() {
    	arrayPushAndIncrement(20).should.equal(78);
    })
    it('should return 2318 when passed 100', function() {
    	arrayPushAndIncrement(100).should.equal(2318);
    })
    it('should return 23331668 when passed 10000', function() {
    	arrayPushAndIncrement(10000).should.equal(23331668);
    })
    it('should return 486804150 when passed 45678', function() {
    	arrayPushAndIncrement(45678).should.equal(486804150);
    })
})
```

Lorsque j'ai exécuté le test avec `mocha testMult.js`, il a retourné ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tmJwwmFxPQevv_kEKOWPRw.png)

Pour toutes les fonctions futures dans cet article, supposez qu'elles ont passé tous les tests. Pour votre propre code, ajoutez des tests pour chaque nouvelle fonction que vous essayez.

### Fonction #2 : Tableau, push, reduce

```javascript
function arrayPushAndReduce(n) {
	var array = [];
    for (var i = 1; i < n; i ++) {
    	if (i % 3 == 0 || i % 5 == 0) {
        	array.push(i);
        }
	}  
    return array.reduce(function(prev, current) {
    	return prev + current;
    });
}

module.exports = arrayPushAndReduce;
```

Cette fonction utilise une approche similaire à la précédente, mais au lieu d'utiliser une boucle `for` pour construire la somme finale, elle utilise la méthode plus élégante `reduce`.

### Configuration des tests de performance

Maintenant que nous avons deux fonctions, nous pouvons comparer leur efficacité. Encore une fois, merci à [P1xt](https://www.freecodecamp.org/news/what-i-learned-from-writing-six-functions-that-all-did-the-same-thing-b38fd48f0d55/undefined) pour avoir fourni ce script dans un précédent fil de forum.

```javascript
// performance.js

var Benchmark = require( 'benchmark' );
var suite = new Benchmark.Suite;

var arrayPushAndIncrement = require( './arrayPushAndIncrement' );
var arrayPushAndReduce = require( './arrayPushAndReduce' );

// ajouter des tests
suite.add( 'arrayPushAndIncrement', function() {
		arrayPushAndIncrement(45678)
    })
    .add( 'arrayPushAndReduce', function() {
    	arrayPushAndReduce(45678)
    })
    // ajouter des écouteurs
    .on( 'cycle', function( event ) {
    	console.log( String( event.target ));
    })
    .on( 'complete', function() {
    	console.log( `Fastest is ${this.filter( 'fastest' ).map( 'name' )}`);
    })
    // exécuter async
    .run({ 'async': true });
```

Si vous exécutez ceci avec `node performance.js`, vous verrez la sortie suivante dans le terminal :

```bash
arrayPushAndIncrement x 270 ops/sec ±11.18% (81 runs sampled)
arrayPushAndReduce x 1,524 ops/sec ±10.79% (89 runs sampled)
Fastest is arrayPushAndReduce
```

Ainsi, l'utilisation de la méthode `reduce` nous a donné une fonction qui était **5 fois plus rapide** !

Si cela n'est pas suffisamment encourageant pour continuer avec plus de fonctions et de tests, je ne sais pas ce qui l'est !

### Fonction #3 : While, Tableau, Reduce

Maintenant, comme je me tourne toujours vers la bonne vieille boucle `for`, j'ai pensé tester une alternative avec une boucle `while` :

```javascript
function whileLoopArrayReduce(n) {
    var array = [];
    while (n >= 1) {
    	n--;
        if (n%3==0||n%5==0) {
        	array.push(n);
        }  
    }  
    return array.reduce(function(prev, current) { 
    	return prev + current;
    });
}

module.exports = whileLoopArrayReduce;
```

Et le résultat ? Un peu plus lent :

```
whileLoopArrayReduce x 1,504 ops/sec ±10.65% (88 runs sampled)
```

### Fonction #4 : While, somme, pas de tableaux

Ainsi, ayant constaté que le type de boucle ne faisait pas une grande différence, je me suis demandé ce qui se passerait si j'utilisais une méthode qui évitait complètement les tableaux :

```js
function whileSum(n) {
    var sum = 0;
    while (n >= 1) {
        n--;
        if (n%3==0||n%5==0) {
            sum += n;
        }
    }  
    return sum;
}

module.exports = whileSum;
```

Dès que j'ai commencé à réfléchir dans cette voie, j'ai réalisé à quel point j'avais tort de _toujours_ me tourner vers les tableaux en premier...

```
whileSum x 7,311 ops/sec ±1.26% (91 runs sampled)
```

Une autre amélioration massive : près de **5 fois plus rapide** à nouveau, et **27 fois plus rapide** que ma fonction originale !

### Fonction #5 : For, somme

Bien sûr, nous savons déjà qu'une boucle for devrait être un peu plus rapide :

```js
function forSum(n) {
    n = n-1;
    var sum = 0;
    for (n; n >= 1 ;n--) {
        (n%3==0||n%5==0) ? sum += n : null;
    }  
    return sum;
}
```

Cela utilise l'opérateur ternaire pour effectuer la vérification de la condition, mais mes tests ont montré qu'une version non ternaire de ceci est la même en termes de performance.

```
forSum x 8,256 ops/sec ±0.24% (91 runs sampled)
```

Donc, un peu plus rapide à nouveau.

Ma fonction finale s'est avérée **28 fois plus rapide** que mon originale.

Je me sentais comme un champion.

J'étais aux anges.

Je me suis reposé sur mes lauriers.

### Entrée des Maths

La semaine a passé et les solutions finales de tout le monde ont été publiées, testées et compilées. La fonction qui a performé le plus rapidement a évité les boucles et a utilisé une formule algébrique pour calculer les nombres :

```javascript
function multSilgarth(N) {
    var threes = Math.floor(--N / 3);  
    var fives = Math.floor(N / 5);
    var fifteen = Math.floor(N / 15);
    return (3 * threes * (threes + 1) + 5 * fives * (fives + 1) - 15 * fifteen * (fifteen + 1)) / 2;
}

module.exports = multSilgarth;
```

Attendez la suite...

```
arrayPushAndIncrement x 279 ops/sec ±0.80% (83 runs sampled)
forSum x 8,256 ops/sec ±0.24% (91 runs sampled)
maths x 79,998,859 ops/sec ±0.81% (88 runs sampled)
Fastest is maths
```

### La plus rapide est maths

Ainsi, la fonction gagnante était environ **9 690 fois plus rapide** que mon meilleur effort, et **275 858 fois plus rapide** que mon effort initial.

Si vous avez besoin de moi, je serai sur Khan Academy à étudier les maths.

Merci à tous ceux qui ont participé et partagé leurs solutions dans l'esprit d'aider les autres campeurs à apprendre de nouvelles méthodes.

Si vous êtes curieux, voici le [compte rendu de P1xt](https://www.freecodecamp.org/news/what-i-learned-from-writing-six-functions-that-all-did-the-same-thing-b38fd48f0d55/undefined) de la compétition, ainsi que toutes les données de test et de benchmark :

[**P1xt/algo-oct-17**](https://github.com/P1xt/algo-oct-17)  
[_algo-oct-17 - JavaScript Algorithm Challenge - October 9 through 16_github.com](https://github.com/P1xt/algo-oct-17)