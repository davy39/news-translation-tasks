---
title: Comment fonctionnent le Global Execution Context et la Temporal Dead Zone en
  JavaScript ?
subtitle: ''
author: Shejan Mahamud
co_authors: []
series: null
date: '2025-11-05T13:52:17.074Z'
originalURL: https://freecodecamp.org/news/global-execution-context-and-temporal-dead-zone-explained
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762347165225/c7bd75a9-a819-41b6-8a35-4feecfb7cf58.png
tags:
- name: JavaScript
  slug: javascript
- name: optimization
  slug: optimization
seo_title: Comment fonctionnent le Global Execution Context et la Temporal Dead Zone
  en JavaScript ?
seo_desc: 'Have you ever wondered how JavaScript runs your code behind the scenes,
  and how the Global Execution Context actually works? How does hoisting work for
  var, let, and const?

  Consider the code bellow:

  console.log(''My age is'', age)

  console.log(''My name ...'
---

Vous êtes-vous déjà demandé comment JavaScript exécute votre code en coulisses, et comment le Global Execution Context fonctionne réellement ? Comment le Hoisting fonctionne-t-il pour `var`, `let` et `const` ?

Considérez le code ci-dessous :

```javascript
console.log('My age is', age)
console.log('My name is', name)
console.log('My country is', country)

var age = 24
let name = 'Shejan'
const country = 'Bangladesh'
sayHi()
function sayHi() {
  console.log('Hi!')
}
```

Selon vous, quel sera le résultat de ce code ?

La première ligne affichera probablement `undefined`, n'est-ce pas ? Mais qu'en est-il de la deuxième ligne avec `name` ? Cela lèvera une « `ReferenceError`: Cannot access `name` before initialization. » Pourquoi ? Parce que les variables `let` sont hoistées mais restent non initialisées dans la Temporal Dead Zone (TDZ) jusqu'à ce que leur ligne de déclaration soit atteinte.

La troisième ligne avec `country` ne s'exécutera jamais car le code s'arrête à la ligne 2 en raison de la `ReferenceError`. Mais si la ligne 2 n'était pas là, la ligne 3 lèverait la même erreur pour la même raison – `const` reste également dans la TDZ.

Et qu'en est-il de l'appel de fonction `sayHi()` ? Si nous pouvions l'atteindre, il fonctionnerait parfaitement et afficherait "Hi!" car les déclarations de fonction sont entièrement hoistées avec leur corps complet.

La question principale : pourquoi et comment tout cela se produit-il ? Plongeons dans le sujet pour trouver des réponses.

## Voici ce que nous allons aborder :

* [Comment fonctionne le Global Execution Context ?](#heading-comment-fonctionne-le-global-execution-context)
    
* [Phase de création de la mémoire](#heading-phase-de-creation-de-la-memoire)
    
* [Comprendre le logigramme](#heading-comprendre-le-logigramme)
    
* [Qu'est-ce que le Hoisting exactement ?](#heading-quest-ce-que-le-hoisting-exactement)
    
* [Est-ce que seul var est hoisté ?](#heading-est-ce-que-seul-var-est-hoiste)
    
* [Temporal Dead Zone (TDZ) – Qu'est-ce que c'est vraiment ?](#heading-temporal-dead-zone-tdz-quest-ce-que-cest-vraiment)
    
* [Le Hoisting de fonction – La partie la plus intéressante !](#heading-le-hoisting-de-fonction-la-partie-la-plus-interessante)
    
* [Que se passe-t-il pendant la phase mémoire :](#heading-que-se-passe-t-il-pendant-la-phase-memoire)
    

## Comment fonctionne le Global Execution Context ?

Lorsque nous exécutons du code JavaScript, la toute première chose qui se produit est la création d'un **Global Execution Context (GEC)**. C'est le concept fondamental derrière l'exécution de JavaScript ! Ce contexte d'exécution global comporte deux phases importantes :

1. **Memory creation phase** (phase mémoire)
    
2. **Code execution phase** (phase d'exécution)
    

Voyons ce qui se passe dans chaque phase, une par une.

## Phase de création de la mémoire

C'est le temps de préparation. Durant cette phase, le moteur JavaScript parcourt l'intégralité du code une fois (sans l'exécuter) et alloue de la mémoire pour toutes les variables et fonctions.

Mais c'est là que ça devient intéressant :

* Les **Variables** (var, let, const) reçoivent un espace en mémoire.
    
    * `var` se voit attribuer la valeur `undefined`.
        
    * `let` et `const` sont placés en mémoire mais restent non initialisés.
        
    * Les fonctions (déclarations de fonction) sont stockées en mémoire avec leur corps de code complet.
        

Alors, que se passe-t-il dans la phase mémoire pour notre exemple de code ?

```bash
age: undefined
name: <uninitialized>
country: <uninitialized>
sayHi: function() { console.log("Hi!"); }
```

Comme vous pouvez le voir, avant même qu'une seule ligne de code ne soit exécutée, tout est déjà en mémoire ! Ce processus global consistant à lever les variables et les fonctions en mémoire pendant la phase de création de la mémoire est appelé **Hoisting** – et c'est ce qui rend l'exécution de JavaScript si "magique".

### Phase d'exécution du code

Maintenant, l'action commence ! Le moteur JavaScript commence à exécuter le code ligne par ligne.

**Ligne 1 :** `console.log("My age is", age);`

* Cherche `age` en mémoire
    
* Trouve `undefined`
    
* **Résultat :** `My age is undefined`
    

**Ligne 2 :** `console.log("My name is", name);`

* Cherche `name` en mémoire. Constate qu'il existe en mémoire mais n'a pas encore été initialisé (il est dans la Temporal Dead Zone, ou TDZ – nous explorerons ce concept en détail plus tard).
    
* Résultat : `ReferenceError`: Cannot access `name` before initialization.
    

L'exécution du code s'arrête ici ! Les lignes restantes ne seront pas exécutées.

Mais que se passerait-il si les lignes 2 et 3 n'étaient pas là ?

**Ligne 4 :** `var age = 24;`

* La valeur de `age` en mémoire est mise à jour de `undefined` à `24`.
    

**Ligne 5 :** `let name = "Shejan";`

* `name` est maintenant initialisé avec la valeur `"Shejan"`.
    
* À partir de ce point, `name` peut être accédé.
    

**Ligne 6 :** `const country = "Bangladesh";`

* `country` est initialisé avec la valeur `"Bangladesh"`.
    

**Lignes 7-9 :** Appel de fonction

* La fonction `sayHi()` a déjà été chargée avec son corps complet pendant la phase mémoire.
    
* Lorsque `sayHi()` est appelée, le moteur JavaScript crée un nouveau contexte d'exécution spécifiquement pour cette fonction.
    
* Ce nouveau contexte est connu sous le nom de **Function Execution Context (FEC)** – il fonctionne comme un enfant du Global Execution Context.
    

Ce contexte d'exécution de fonction possède également **deux phases**, tout comme le Global Execution Context :

1. **Phase de création de la mémoire :**
    
    * Toutes les variables, paramètres et fonctions imbriquées à l'intérieur de la fonction sont alloués en mémoire.
        
    * Les arguments de la fonction sont assignés.
        
    * Une portée de fonction (scope) est créée et un lien de référence est établi avec l'environnement lexical extérieur (où la fonction a été définie) – ce lien est appelé la **Scope Chain**. La Scope Chain est la manière dont JavaScript résout les noms de variables. C'est comme une chaîne de portées connectées. Lorsque JavaScript cherche une variable à l'intérieur d'une fonction, il vérifie d'abord la propre portée de la fonction. S'il ne l'y trouve pas, il remonte la chaîne pour vérifier la portée parente, puis la portée grand-parente, et ainsi de suite, jusqu'à atteindre la portée globale. Cette chaîne garantit que les fonctions peuvent accéder aux variables de leurs environnements extérieurs.
        
2. **Phase d'exécution du code (Thread) :**
    
    * Maintenant, le corps de la fonction est exécuté ligne par ligne.
        
    * `console.log("Hi!");` s'exécute et affiche **"Hi!"**.
        

Une fois l'exécution de la fonction terminée :

* Ce contexte d'exécution de fonction est retiré de la pile d'appels (Call Stack).
    
* Et le contrôle revient au Global Execution Context.
    

**Note** : Lorsque toute l'exécution du code est terminée, le Global Execution Context est également retiré de la Call Stack.

![Logigramme illustrant le flux de travail du Global Execution Context JavaScript, montrant les deux phases - Phase de création de la mémoire où les variables et fonctions sont allouées, et Phase d'exécution du code où le code s'exécute ligne par ligne, incluant comment le Function Execution Context est créé lors de l'appel des fonctions](https://cdn.hashnode.com/res/hashnode/image/upload/v1761988425883/33792916-eee7-4f87-b365-51a04290aa96.png align="center")

Le logigramme ci-dessus illustre le flux de travail du Global Execution Context JavaScript, montrant les deux phases. Dans la phase de création de la mémoire, les variables et les fonctions sont allouées, et dans la phase d'exécution du code, le code s'exécute ligne par ligne. Il montre également comment le contexte d'exécution de fonction est créé lorsque les fonctions sont appelées.

## Comprendre le logigramme

Le diagramme ci-dessus visualise le parcours complet de l'exécution du code JavaScript du début à la fin.

**Le flux commence** lorsque l'exécution de JavaScript débute et crée immédiatement un Global Execution Context (GEC). Ce contexte se divise ensuite en deux phases distinctes, représentées par un losange dans le diagramme.

**Sur le côté gauche - Phase de création de la mémoire :** Vous pouvez voir trois branches parallèles montrant comment les différents types de déclarations sont gérés :

* Les variables `var` sont allouées avec la valeur `undefined`.
    
* Les variables `let` et `const` sont allouées mais restent non initialisées (dans la Temporal Dead Zone).
    
* Les déclarations de fonction sont entièrement hoistées avec leur corps complet.
    

**Sur le côté droit - Phase d'exécution du code :** JavaScript exécute maintenant le code ligne par ligne. Pendant l'exécution :

* Il accède aux valeurs des variables depuis la mémoire.
    
* Si vous essayez d'accéder à `let` ou `const` avant l'initialisation, vous obtenez une ReferenceError (Temporal Dead Zone).
    
* Si vous accédez à `var` avant l'assignation, vous obtenez `undefined`.
    
* Lorsqu'une fonction est appelée, un nouveau Function Execution Context (FEC) est créé.
    

**Le Function Execution Context (FEC)** (montré dans la branche de droite) fonctionne comme un enfant du GEC et possède ses propres phases de mémoire et d'exécution. Une fois que la fonction a fini de s'exécuter, le FEC est retiré de la Call Stack et le contrôle revient au GEC.

**Enfin**, lorsque toute l'exécution du code est terminée, le GEC lui-même est retiré de la Call Stack, et le programme prend fin.

Cette représentation visuelle vous aide à comprendre que JavaScript ne se contente pas de lire et de lancer votre code - il prépare tout d'abord (Phase Mémoire) puis l'exécute systématiquement (Phase d'Exécution).

## Qu'est-ce que le Hoisting exactement ?

Le Hoisting est le comportement par défaut de JavaScript consistant à déplacer les déclarations de variables et de fonctions en mémoire avant le début de l'exécution du code.

Voyez-le de cette façon : c'est comme si toutes les déclarations se déplaçaient automatiquement tout en haut du code. Bien que le code ne se déplace pas physiquement, l'allocation de mémoire se produit en premier.

## Est-ce que seul `var` est hoisté ?

Cela surprend beaucoup de gens, mais la réponse est non. Il n'y a pas que `var` qui est hoisté ! C'est une idée reçue très répandue chez de nombreux développeurs.

La vérité est que — `let`, `const` et les fonctions — tout est hoisté ! Mais leur comportement est complètement différent. Plongeons dans les détails.

### Que se passe-t-il avec `var` ?

```javascript
console.log(name) // undefined
var name = 'Rahim'
console.log(name) // "Rahim"
```

Les variables déclarées avec `var` :

* Sont hoistées
    
* Sont initialisées avec `undefined`
    
* Existent dans la portée globale ou la portée de fonction
    
* Peuvent être accédées avant la déclaration (ne lève pas d'erreur)
    

### Que se passe-t-il avec `let` ?

```javascript
console.log(name) // ReferenceError: Cannot access 'name' before initialization
let name = 'Rahim'
console.log(name) // "Rahim"
```

Est-ce de la magie ? Non ! En réalité, `let` est bien hoisté, mais il est bloqué dans un état spécial appelé la Temporal Dead Zone !

L'espace est alloué en mémoire, mais il n'est pas initialisé. Donc, si vous essayez d'y accéder avant la déclaration, JavaScript dit : "Hé, la variable existe, mais tu ne peux pas encore l'utiliser !"

### Que se passe-t-il avec `const` ?

```javascript
console.log(age) // ReferenceError: Cannot access 'age' before initialization
const age = 24
console.log(age) // 24
```

Le comportement de `const` est exactement le même que celui de `let` :

* Est hoisté
    
* Reste dans la TDZ jusqu'à la déclaration
    
* Existe dans la portée de bloc
    
* De plus, une fois assigné, il ne peut pas être réassigné
    

## Temporal Dead Zone (TDZ) – Qu'est-ce que c'est vraiment ?

La Temporal Dead Zone est la période ou la zone pendant laquelle une variable existe en mémoire (en raison du hoisting) mais n'a pas encore été initialisée. Pendant ce temps, la variable est essentiellement "morte" – ce qui signifie que vous ne pouvez pas y accéder.

```javascript
// ← La TDZ commence pour x et y
console.log(x) // ReferenceError - toujours dans la TDZ
console.log(y) // ReferenceError - toujours dans la TDZ

// La TDZ continue...
let x = 10 // ← La TDZ de x se termine à cette ligne
const y = 20 // ← La TDZ de y se termine à cette ligne

console.log(x) // 10 - accessible maintenant
console.log(y) // 20 - accessible maintenant
```

Le concept même de la TDZ est de nous forcer à écrire un meilleur code. Utiliser des variables avant de les déclarer est une mauvaise pratique, et la TDZ nous empêche de le faire.

## Le Hoisting de fonction – La partie la plus intéressante !

Le Hoisting avec les fonctions est encore plus intéressant et puissant :

```javascript
greet() // "Hello World!" - Parfait ! Ça fonctionne !

function greet() {
  console.log('Hello World!')
}
```

Comment est-ce possible ? Parce que les déclarations de fonction sont complètement hoistées ! Cela signifie que non seulement le nom, mais tout le corps de la fonction est levé en mémoire. C'est pourquoi elle peut être appelée même avant la déclaration.

Mais attendez ! Toutes les fonctions ne fonctionnent pas de cette manière.

### Avec les expressions de fonction :

```javascript
greet() // TypeError: greet is not a function

var greet = function () {
  console.log('Hello World!')
}
```

Que s'est-il passé ici ? `greet` a été hoisté comme une variable et a reçu la valeur `undefined`. Il n'a pas été hoisté comme une fonction ! Donc, quand vous essayez de l'appeler, vous obtenez une erreur. En d'autres termes, il est hoisté comme une variable (assigné à `undefined`), mais le corps de la fonction n'est pas chargé en mémoire.

### Avec les fonctions fléchées (Arrow Functions) :

```javascript
sayHello() // ReferenceError (si let/const est utilisé)

const sayHello = () => {
  console.log('Hello!')
}
```

Les fonctions fléchées se comportent exactement comme les expressions de fonction. Elles suivent les règles des variables.

Clarifions tout cela avec un exemple complet :

```javascript
console.log(a) // undefined (hoisting de var)
console.log(b) // ReferenceError (TDZ)
console.log(c) // ReferenceError (TDZ)
multiply(2, 3) // 6 (hoisting de fonction)
add(2, 3) // TypeError (expression de fonction)

var a = 10
let b = 20
const c = 30

function multiply(x, y) {
  return x * y
}

var add = function (x, y) {
  return x + y
}
```

## Que se passe-t-il pendant la phase mémoire :

```javascript
a: undefined
b: <uninitialized>
c: <uninitialized>
multiply: function(x, y) { return x * y; }
add: undefined
```

Cet instantané représente l'état de la mémoire avant que tout code ne soit exécuté. Voici ce que signifie chaque ligne :

`a: undefined` - Puisque `a` est déclaré avec `var`, il est hoisté et immédiatement assigné à la valeur `undefined`. C'est pourquoi vous obtenez `undefined` au lieu d'une erreur lorsque vous essayez d'accéder à `a` avant sa ligne de déclaration.

`b: <uninitialized>` - La variable `b` est déclarée avec `let`, elle est donc hoistée et de la mémoire lui est allouée, mais elle reste non initialisée. Elle est dans la Temporal Dead Zone (TDZ). Tenter d'y accéder avant la ligne de déclaration lèvera une `ReferenceError`.

`c: <uninitialized>` - De même, `c` est déclaré avec `const` et suit le même comportement que `let`. Il est hoisté mais reste non initialisé dans la TDZ jusqu'à ce que la ligne de déclaration soit atteinte.

`multiply: function(x, y) { return x * y; }` - Il s'agit d'une déclaration de fonction, elle est donc entièrement hoistée avec son corps complet. La fonction entière est stockée en mémoire et prête à être appelée avant même que le moteur JavaScript n'atteigne sa déclaration dans le code. C'est pourquoi `multiply(2, 3)` fonctionne parfaitement et renvoie `6`.

`add: undefined` - Voici la différence cruciale ! Même si `add` finira par stocker une fonction, il est déclaré en utilisant `var add = function() {...}` (une expression de fonction). Pendant la phase mémoire, seule la variable `add` est hoistée et initialisée avec `undefined`. Le corps réel de la fonction n'est pas assigné avant que la phase d'exécution n'atteigne la ligne 11. C'est pourquoi appeler `add(2, 3)` avant l'assignation lève un `TypeError: add is not a function` – vous essayez essentiellement d'exécuter `undefined()`.

## Conclusion

Comprendre le mécanisme d'exécution de JavaScript est fondamental pour devenir un développeur compétent. Récapitulons les concepts essentiels que nous avons explorés :

**Le Global Execution Context (GEC)** est le fondement de l'exécution de JavaScript. Chaque fois que vous lancez du code JavaScript, le GEC est créé en premier. Il fonctionne en deux phases critiques :

* **Phase de création de la mémoire** : JavaScript se prépare en scannant le code et en allouant de la mémoire pour les variables et les fonctions.
    
* **Phase d'exécution du code** : JavaScript lance votre code ligne par ligne.
    

**Le Hoisting est universel** - pas seulement limité à `var`. Voici comment les différentes déclarations sont hoistées :

* Les variables `var` sont hoistées et initialisées avec `undefined`.
    
* `let` et `const` sont hoistés mais restent non initialisés dans la TDZ.
    
* Les déclarations de fonction sont entièrement hoistées avec leur corps entier.
    
* Les expressions de fonction et les fonctions fléchées suivent les règles de hoisting des variables.
    

**La Temporal Dead Zone (TDZ)** est le mécanisme de sécurité intégré de JavaScript. Elle existe du début de la portée jusqu'à ce que la ligne de déclaration de la variable soit atteinte. La TDZ nous empêche d'accéder aux variables `let` et `const` avant qu'elles ne soient déclarées, encourageant de meilleures pratiques de codage et nous aidant à éviter les bugs.

**Le comportement du hoisting de fonction varie** :

* Les déclarations de fonction peuvent être appelées avant d'apparaître dans le code.
    
* Les expressions de fonction se comportent comme des variables et ne peuvent pas être appelées avant l'assignation.
    
* Les fonctions fléchées suivent les mêmes règles que les expressions de fonction.
    

**Pourquoi est-ce important ?** Comprendre ces concepts vous aide à :

* Prédire comment votre code se comportera avant de le lancer.
    
* Éviter les erreurs courantes comme `ReferenceError` et `TypeError`.
    
* Écrire un code plus propre et plus facile à maintenir.
    
* Déboguer les problèmes plus rapidement lorsqu'ils surviennent.
    
* Prendre des décisions éclairées sur le moment d'utiliser `var`, `let` ou `const`.
    

**Le point clé à retenir** : **JavaScript ne se contente pas d'exécuter votre code - il se prépare d'abord, puis exécute.** La phase mémoire prépare la scène, et la phase d'exécution assure la représentation. Maîtrisez ce processus en deux phases, et vous aurez une compréhension solide du fonctionnement interne de JavaScript.

Vous êtes maintenant équipé des connaissances nécessaires pour écrire un meilleur code JavaScript et comprendre exactement ce qui se passe en coulisses. Continuez à pratiquer ces concepts, et ils deviendront une seconde nature !

Bon codage !