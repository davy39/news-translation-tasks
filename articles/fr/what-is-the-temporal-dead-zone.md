---
title: Qu'est-ce que la Zone Morte Temporelle (TDZ) en JavaScript ?
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2020-10-06T22:36:19.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-temporal-dead-zone
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/What-is-the-Temporal-dead-zone_.png
tags:
- name: JavaScript
  slug: javascript
- name: variables
  slug: variables
seo_title: Qu'est-ce que la Zone Morte Temporelle (TDZ) en JavaScript ?
seo_desc: 'I know Temporal Dead Zone sounds like a sci-fi phrase. But it''s helpful
  to understand what the terms and concepts you work with everyday (or want to learn
  about) mean.

  Strap in, because this gets complicated.

  Are you aware that in JavaScript we can a...'
---

Je sais que Zone Morte Temporelle sonne comme une phrase de science-fiction. Mais il est utile de comprendre ce que signifient les termes et concepts avec lesquels vous travaillez quotidiennement (ou que vous souhaitez apprendre).

Attachez vos ceintures, car cela devient compliqué.

Êtes-vous conscient qu'en JavaScript, nous pouvons ajouter `{ }` pour ajouter un niveau de portée où nous le souhaitons ?

Nous pourrions donc toujours faire ce qui suit :

```js
{ { { { { { var folie = true } } } } } }
```

J'ai inclus ce détail pour m'assurer que les exemples à venir soient compréhensibles (car je ne voulais pas supposer que tout le monde le savait).

Avant ES6, il n'y avait pas d'autre moyen de déclarer des variables que `var`. Mais ES6 nous a apporté `let` et `const`.

Les déclarations `let` et `const` sont toutes deux limitées à leur bloc, ce qui signifie qu'elles ne sont accessibles qu'à l'intérieur des `{` `}` qui les entourent. `var`, en revanche, n'a pas cette restriction.

Voici un exemple :

```javascript
let ageBebe = 1;
let estAnniversaire = true;

if (estAnniversaire) {
	let ageBebe = 2; 
}

console.log(ageBebe); // Hmmmm. Cela affiche 1
```

Ce qui précède s'est produit parce que la redéclaration de `ageBebe` à 2 n'est disponible qu'à l'intérieur du bloc `if`. Au-delà, le premier `ageBebe` est utilisé. Pouvez-vous voir qu'il s'agit de deux variables différentes ?

En revanche, la déclaration `var` n'a pas de portée de bloc :

```js
var ageBebe = 1;
var estAnniversaire = true;

if (estAnniversaire) {
	var ageBebe = 2; 
}

console.log(ageBebe); // Ah ! Cela affiche 2
```

La différence finale entre `let` / `const` et `var` est que si vous accédez à `var` avant qu'elle ne soit déclarée, elle est indéfinie. Mais si vous faites de même pour `let` et `const`, elles génèrent une `ReferenceError`.

```javascript
console.log(nombreVar); // undefined
console.log(nombreLet); // Ne s'affiche pas, car cela génère une ReferenceError : nombreLet n'est pas défini

var nombreVar = 1;
let nombreLet = 1;
```

Elles génèrent l'erreur à cause de la Zone Morte Temporelle.

## Explication de la Zone Morte Temporelle

Voici ce qu'est la TDZ : le terme pour décrire l'état où les variables sont inaccessibles. Elles sont dans la portée, mais elles ne sont pas déclarées.

Les variables `let` et `const` existent dans la TDZ à partir du début de leur portée englobante jusqu'à ce qu'elles soient déclarées.

On pourrait aussi dire que les variables existent dans la TDZ à partir de l'endroit où elles sont liées (quand la variable est liée à la portée dans laquelle elle se trouve) jusqu'à ce qu'elles soient déclarées (quand un nom est réservé en mémoire pour cette variable).

```javascript
{
 	// Ceci est la zone morte temporelle pour la variable age !
	// Ceci est la zone morte temporelle pour la variable age !
	// Ceci est la zone morte temporelle pour la variable age !
 	// Ceci est la zone morte temporelle pour la variable age !
	let age = 25; // Ouf, nous y sommes arrivés ! Plus de TDZ
	console.log(age);
}
```

Vous pouvez voir ci-dessus que si j'avais accédé à la variable age avant sa déclaration, cela aurait généré une `ReferenceError`. À cause de la TDZ.

Mais `var` ne fera pas cela. `var` est simplement initialisée par défaut à `undefined` contrairement à l'autre déclaration.

## Quelle est la différence entre déclarer et initialiser ?

Voici un exemple de déclaration d'une variable et d'initialisation d'une variable.

```javascript
function exemplePortee() {

    let age; // 1
    age = 20; // 2
    let mains = 2; // 3
}
```

Déclarer une variable signifie que nous réservons le nom en mémoire dans la portée actuelle. Cela est étiqueté 1 dans les commentaires.

Initialiser une variable consiste à définir la valeur de la variable. Cela est étiqueté 2 dans les commentaires.

Ou vous pourriez toujours faire les deux en une seule ligne. Cela est étiqueté 3 dans les commentaires.

Pour me répéter : les variables `let` et `const` existent dans la TDZ à partir du début de leur portée englobante jusqu'à ce qu'elles soient déclarées.

Donc, dans l'extrait de code ci-dessus, où se trouve la TDZ pour `age` ? De plus, `mains` a-t-elle une TDZ ? Si oui, où commence et où se termine la TDZ pour `mains` ?

<details>
<summary>Vérifiez votre réponse</summary> 
Les variables `mains` et `age` entrent toutes deux dans la TDZ.
<br> <br>
La TDZ pour `mains` se termine lorsqu'elle est déclarée, sur la même ligne où elle est définie à 2. 
<br> <br>  
La TDZ pour `age` se termine lorsqu'elle est déclarée, et le nom réservé en mémoire (à l'étape 2, où j'ai commenté).
</details>

## Pourquoi la TDZ est-elle créée quand elle l'est ?

Revenons à notre premier exemple :

```
{
    // Ceci est la zone morte temporelle pour la variable age !
    // Ceci est la zone morte temporelle pour la variable age !
    // Ceci est la zone morte temporelle pour la variable age !
    // Ceci est la zone morte temporelle pour la variable age !
    let age = 25; // Ouf, nous y sommes arrivés ! Plus de TDZ
    console.log(age);
}
```

Si nous ajoutons un `console.log` à l'intérieur de la TDZ, vous verrez cette erreur :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-5.png)

Pourquoi la TDZ existe-t-elle entre le début de la portée et la déclaration de la variable ? Quelle est la raison spécifique à cela ?

**C'est à cause du hoisting.**

Le moteur JS qui analyse et exécute votre code a deux étapes à effectuer :

1. L'analyse du code en un arbre de syntaxe abstraite/code byte exécutable, et
2. L'exécution au moment de l'exécution.

L'étape 1 est celle où le hoisting se produit, et cela est fait par le moteur JS. Il déplacera essentiellement toutes vos déclarations de variables en haut de leur portée. Un exemple serait :

```js
console.log(variableHoistee); // undefined
var variableHoistee = 1;
```

Pour être clair, ces variables ne se déplacent pas physiquement dans le code. Mais le résultat serait fonctionnellement identique à ce qui suit :

```js
var variableHoistee;

console.log(variableHoistee); // undefined
compteur = 1;
```

La seule différence entre `const` et `let` est que lorsqu'elles sont hoistées, leurs valeurs ne sont pas définies par défaut à `undefined`.

Pour prouver que `let` et `const` sont également hoistées, voici un exemple :

```js
{
    // Les deux variables ci-dessous seront hoistées en haut de leur portée !
	console.log(typeof nonSensQuiNExistePas); // Affiche undefined
	console.log(typeof nom); // Génère une erreur, ne peut pas accéder à 'nom' avant initialisation

	let nom = "Kealan";
}
```

L'extrait de code ci-dessus prouve que `let` est clairement hoistée au-dessus de l'endroit où elle a été déclarée, car le moteur nous alerte du fait. Il sait que `nom` existe (il est déclaré), mais nous ne pouvons pas y accéder avant qu'il ne soit initialisé.

Si cela vous aide à vous souvenir, pensez à cela comme suit.

Lorsque les variables sont hoistées, `var` obtient `undefined` initialisé à sa valeur par défaut dans le processus de hoisting. `let` et `const` sont également hoistées, mais ne sont pas définies à `undefined` lorsqu'elles sont hoistées.

Et c'est la seule raison pour laquelle nous avons la TDZ. Ce qui explique pourquoi cela se produit avec `let` et `const` mais pas avec `var`.

## Plus d'exemples de la TDZ

La TDZ peut également être créée pour les paramètres de fonction par défaut. Donc quelque chose comme ceci :

```js
function creerTDZ(a=b, b) {
}

creerTDZ(undefined, 1); 
```

génère une `ReferenceError`, car l'évaluation de la variable `a` tente d'accéder à la variable `b` avant qu'elle n'ait été analysée par le moteur JS. Les arguments de la fonction sont tous dans la TDZ jusqu'à ce qu'ils soient analysés.

Même quelque chose d'aussi simple que `let testTDZ = testTDZ;` générerait une erreur en raison de la TDZ. Mais `var` ici créerait simplement `testTDZ` et le définirait à `undefined`.

Il y a un dernier exemple [assez avancé](https://github.com/google/traceur-compiler/issues/1382#issuecomment-57182072) d'Erik Arvindson (qui est impliqué dans l'évolution et la maintenance de la spécification ECMAScript) :

```javascript
let a = f(); // 1
const b = 2;
function f() { return b; } // 2, b est dans la TDZ

```

Vous pouvez suivre les numéros commentés.

Dans la première ligne, nous appelons la fonction `f`, puis nous essayons d'accéder à la variable `b` (ce qui génère une `ReferenceError` parce que `b` est dans la TDZ).

## Pourquoi avons-nous la TDZ ?

Le Dr Alex Rauschmayer a un excellent [article](https://2ality.com/2015/10/why-tdz.html) sur _pourquoi_ la TDZ existe, et la raison principale est la suivante :

Cela nous aide à attraper les erreurs.

Essayer d'accéder à une variable avant qu'elle ne soit déclarée est dans le mauvais sens et ne devrait pas être possible.

Cela donne également des sémantiques plus attendues et rationnelles pour `const` (parce que `const` est hoistée, que se passe-t-il si un programmeur essaie de l'utiliser avant qu'elle ne soit déclarée à l'exécution ? Quelle variable devrait-elle contenir au moment où elle est hoistée ?), et c'était la meilleure approche décidée par l'équipe de spécification ECMAScript.

## Comment éviter les problèmes causés par la TDZ

Relativement simple, assurez-vous toujours de définir vos `let` et `const` en haut de votre portée.