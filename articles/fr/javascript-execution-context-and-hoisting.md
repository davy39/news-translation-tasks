---
title: Le contexte d'exécution et le hoisting en JavaScript expliqués avec des exemples
  de code
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-04-27T22:53:14.000Z'
originalURL: https://freecodecamp.org/news/javascript-execution-context-and-hoisting
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/freeCodeCamp-Cover-4.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
seo_title: Le contexte d'exécution et le hoisting en JavaScript expliqués avec des
  exemples de code
seo_desc: "JavaScript is an easy-to-learn programming language compared to many of\
  \ its counterparts. However, a few basic concepts need a bit more attention if you\
  \ want to understand, debug, and write better code. \nIn this article, we will learn\
  \ about two such ..."
---

JavaScript est un langage de programmation facile à apprendre par rapport à beaucoup de ses homologues. Cependant, quelques concepts de base nécessitent un peu plus d'attention si vous voulez comprendre, déboguer et écrire un meilleur code.

Dans cet article, nous allons découvrir deux de ces concepts :

* Le contexte d'exécution (Execution Context)
* Le Hoisting

En tant que débutant en JavaScript, la compréhension de ces concepts vous aidera à appréhender les mots-clés `this`, `scope` (portée) et `closure` (fermeture) bien plus sereinement. Alors, profitez-en et bonne lecture.

# Contexte d'exécution en JavaScript

En général, un fichier source JavaScript contient plusieurs lignes de code. En tant que développeurs, nous organisons le code en variables, fonctions, structures de données comme les objets et les tableaux, et plus encore.

Un `Environnement lexical` détermine comment et où nous écrivons physiquement notre code. Regardez le code ci-dessous :

```js
function doSomething() {
  var age= 7;
  // Un peu plus de code
 }

```

Dans le code ci-dessus, la variable `age` se trouve lexicalement à l'intérieur de la fonction `doSomething`.

Veuillez noter que notre code ne s'exécute pas tel quel. Il doit être traduit par le compilateur en byte-code compréhensible par l'ordinateur. Le compilateur doit donc mapper ce qui est placé lexicalement et où, de manière significative et valide.

Habituellement, il y aura plus d'un `Environnement lexical` dans votre code. Cependant, tous les environnements ne sont pas exécutés en même temps.

L'environnement qui aide le code à s'exécuter est appelé le `Contexte d'exécution`. C'est le code qui est actuellement en cours d'exécution, ainsi que tout ce qui l'entoure et qui aide à son exécution.

Il peut y avoir de nombreux `Environnement lexical` disponibles, mais celui qui exécute actuellement le code est géré par le `Contexte d'exécution`.

Consultez l'image ci-dessous pour comprendre la différence entre un environnement lexical et un contexte d'exécution :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/lexical.gif)
_Environnement lexical vs Contexte d'exécution_

Alors, que se passe-t-il exactement dans le contexte d'exécution ? Le code est analysé ligne par ligne, génère du byte-code exécutable, alloue de la mémoire et s'exécute.

Reprenons la même fonction que celle vue plus haut. À votre avis, que se passe-t-il lorsque la ligne suivante est exécutée ?

```js
var age = 7;

```

Beaucoup de choses se passent en coulisses. Ce morceau de code source passe par les phases suivantes avant d'être finalement exécuté :

* **Tokenisation :** Dans cette phase, la chaîne de code source est décomposée en plusieurs morceaux significatifs appelés `Tokens`. Par exemple, le code `var age = 7;` se divise en **var**, **age**, **=**, **7** et **;**.
* **Analyse syntaxique (Parsing) :** La phase suivante est le parsing, où un tableau de tokens se transforme en un arbre d'éléments imbriqués compris par la grammaire du langage. Cet arbre est appelé un `AST` (Abstract Syntax Tree).
* **Génération de code :** Dans cette phase, l'AST créé lors de la phase de parsing est transformé en byte-code exécutable. Ce byte-code exécutable est ensuite optimisé par le compilateur JIT (Just-In-Time).

L'image animée ci-dessous montre la transition du code source vers le byte-code exécutable.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/execution_steps.gif)
_Du code source au byte-code exécutable_

Toutes ces étapes se déroulent dans un `Contexte d'exécution`. Le contexte d'exécution est donc l'environnement dans lequel une portion spécifique du code s'exécute.

Il existe deux types de contextes d'exécution :

* Le contexte d'exécution global (GEC - Global Execution Context)
* Le contexte d'exécution de fonction (FEC - Function Execution Context)

Et chacun de ces contextes d'exécution comporte deux phases :

* Phase de création
* Phase d'exécution

Examinons chacune d'elles en détail pour mieux les comprendre.

## Contexte d'exécution global (GEC) en JavaScript

Chaque fois que nous exécutons du code JavaScript, cela crée un contexte d'exécution global (également appelé contexte d'exécution de base). Le contexte d'exécution global comporte deux phases.

### Phase de création

Lors de la phase de création, deux éléments uniques sont créés :

* Un objet global appelé `window` (pour le JavaScript côté client).
* Une variable globale appelée `this`.

Si des variables sont déclarées dans le code, de la mémoire leur est allouée. La variable est initialisée avec une valeur unique appelée `undefined`. Si une `fonction` est présente dans le code, elle est placée directement en mémoire. Nous en apprendrons davantage sur cette partie dans la section `Hoisting` plus loin.

### Phase d'exécution

L'exécution du code commence dans cette phase. C'est ici que l'assignation des valeurs des variables globales a lieu. Veuillez noter qu'aucune fonction n'est invoquée ici, car cela se produit dans le contexte d'exécution de fonction. Nous verrons cela dans un instant.

Comprenons ces deux phases avec quelques exemples.

#### Exemple 1 : Charger un script vide

Créez un fichier JavaScript vide nommé `index.js`. Créez maintenant un fichier HTML avec le contenu suivant :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src='./index.js'></script>
</head>
<body>
    Je charge un script vide
</body>
</html>
```

Notez que nous importons le fichier de script vide dans le fichier HTML à l'aide de la balise `<script>`. 

Chargez le fichier HTML dans le navigateur et ouvrez les Chrome DevTools (généralement avec la touche `F12`) ou l'équivalent pour d'autres navigateurs. Allez dans l'onglet `console`, tapez `window` et appuyez sur entrée. Vous devriez voir l'objet `Window` du navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-102.png)
_L'objet Window_

Maintenant, tapez le mot `this` et appuyez sur entrée. Vous devriez voir la même valeur d'objet `Window` affichée dans la console du navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-103.png)
_Valeur de 'this'_

Super, essayez maintenant de vérifier si window est égal à `this`. Oui, c'est le cas.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-104.png)
_window est égal à 'this'_

Très bien, qu'avons-nous appris ?

* Le contexte d'exécution global est créé lorsque nous chargeons le fichier JavaScript, même s'il est vide.
* Il crée deux éléments spéciaux pour nous lors de sa phase de création : l'objet `window` et `this`.
* Dans le contexte d'exécution global, l'objet `window` et `this` sont identiques.
* Il n'y a rien à exécuter puisque le fichier de script est vide. Rien ne se passe donc dans la phase d'exécution.

#### Exemple 2 : Avec des variables et des fonctions

Voyons maintenant un exemple avec du code dans le fichier JavaScript. Nous allons ajouter une variable (blog) avec une valeur assignée. Nous définirons également une fonction nommée `logBlog`.

```js
var blog = 'freeCodeCamp';

function logBlog() {
  console.log(this.blog); 
}

```

Dans la phase de création :

* L'objet global `window` et la variable `this` sont créés.
* De la mémoire est allouée pour la variable `blog` et la fonction `logBlog`.
* La variable `blog` est initialisée par une valeur spéciale `undefined`. La fonction `logBlog` est placée directement en mémoire.

Dans la phase d'exécution :

* La valeur `freeCodeCamp` est assignée à la variable `blog`.
* Comme nous avons défini la fonction mais ne l'avons pas encore appelée, l'exécution de la fonction n'a pas lieu. Nous appellerons la fonction et verrons ce qui se passe lorsque nous étudierons le contexte d'exécution de fonction.

## Contexte d'exécution de fonction (FEC) en JavaScript

Lorsque nous invoquons une fonction, un contexte d'exécution de fonction est créé. Reprenons le même exemple que précédemment, mais cette fois-ci, nous allons appeler la fonction.

```js
var blog = 'freeCodeCamp';

function logBlog() {
  console.log(this.blog); 
}

// Appelons la fonction
logBlog();
```

Le contexte d'exécution de fonction passe par les mêmes phases : création et exécution.

La phase d'exécution de la fonction a accès à une valeur spéciale appelée `arguments`. Ce sont les arguments passés à la fonction. Dans notre exemple, aucun argument n'est passé.

Veuillez noter que l'objet `window` et la variable `this` créés dans le contexte d'exécution global sont toujours accessibles dans ce contexte.

Lorsqu'une fonction en invoque une autre, un nouveau contexte d'exécution de fonction est créé pour ce nouvel appel. Chacun des contextes d'exécution de fonction détermine la `scope` (portée) des variables utilisées dans les fonctions respectives.

# Hoisting en JavaScript

J'espère que vous avez apprécié d'en apprendre davantage sur le `Contexte d'exécution`. Passons à un autre concept fondamental appelé `Hoisting`. Quand j'ai entendu parler du hoisting pour la première fois, il m'a fallu un certain temps pour réaliser que le nom « Hoisting » pouvait prêter à confusion.

En anglais, le terme « hoisting » signifie soulever quelque chose à l'aide de cordes et de poulies. Ce nom peut vous induire en erreur en vous faisant croire que le moteur JavaScript remonte physiquement les variables et les fonctions lors d'une phase spécifique de l'exécution du code. Ce n'est pas tout à fait ce qui se passe.

Comprenons donc le `Hoisting` en utilisant le concept de `Contexte d'exécution`.

## Hoisting de variable en JavaScript

Regardez l'exemple ci-dessous et devinez le résultat :

```js
console.log(name);
var name;


```

Je suis sûr que vous l'avez déjà deviné. C'est le suivant :

```shell
undefined

```

Cependant, la question est : pourquoi ? Supposons que nous utilisions un code similaire dans un autre langage de programmation. Dans ce cas, nous pourrions obtenir une erreur indiquant que la variable `name` n'est pas déclarée et que nous essayons d'y accéder bien avant cela. La réponse réside dans le contexte d'exécution.

Dans la phase de `création` :

* La mémoire est allouée pour la variable `name`, et
* Une valeur spéciale `undefined` est assignée à la variable.

Dans la phase d' `exécution` :

* L'instruction `console.log(name)` s'exécute.

Ce mécanisme d'allocation de mémoire pour les variables et d'initialisation avec la valeur `undefined` lors de la phase de création du contexte d'exécution est appelé `Hoisting de variable`.

> La valeur spéciale `undefined` signifie qu'une variable est déclarée mais qu'aucune valeur ne lui est assignée.

Si nous assignons une valeur à la variable comme ceci :

```js
name = 'freeCodeCamp';
```

La phase d'exécution assignera cette valeur à la variable.

## Hoisting de fonction en JavaScript

Parlons maintenant du `Hoisting de fonction`. Il suit le même schéma que le `Hoisting de variable`.

La phase de création du contexte d'exécution place la déclaration de la fonction en mémoire, et la phase d'exécution l'exécute. Regardez l'exemple ci-dessous :

```js
// Invoquer la fonction functionA
functionA();

// Déclarer la fonction functionA
function functionA() {
 console.log('Function A');
 // Invoquer la fonction functionB    
 functionB();
}

// Déclarer la fonction functionB
function functionB() {
 console.log('Function B');
}
```

Le résultat est le suivant :

```shell
Function A
Function B
```

* Le contexte d'exécution crée la mémoire pour la fonction et y place l'intégralité de la déclaration de `functionA`.
* Les fonctions créent leur propre contexte d'exécution. La même chose se produit donc également pour `functionB`.
* Ensuite, les fonctions sont exécutées respectivement dans leur contexte d'exécution.

Le fait de placer l'intégralité de la déclaration de la fonction en mémoire lors de la phase de création est appelé `Hoisting de fonction`.

## Quelques règles de base

Maintenant que nous comprenons le concept de `Hoisting`, voyons quelques règles de base :

* Définissez toujours les variables et les fonctions avant de les utiliser dans votre code. Cela réduit les risques d'erreurs surprises et de cauchemars de débogage.
* Le hoisting ne concerne que la déclaration de fonction, pas son initialisation. Voici un exemple d'initialisation de fonction où l'exécution du code s'arrêtera.

```js
logMe();

var logMe = function() {
  console.log('Logging...');
}
```

L'exécution du code s'arrêtera car, avec une initialisation de fonction, la variable `logMe` sera « hoistée » comme une variable, et non comme une fonction. Ainsi, avec le hoisting de variable, l'allocation mémoire se fera avec l'initialisation à `undefined`. C'est la raison pour laquelle nous obtiendrons l'erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-105.png)
_Erreur lors du hoisting d'une initialisation de fonction_

Supposons que nous essayions d'accéder à une variable avant sa déclaration et que nous utilisions les mots-clés `let` et `const` pour la déclarer plus tard. Dans ce cas, elles seront « hoistées » mais ne se verront pas assigner la valeur par défaut `undefined`. L'accès à de telles variables entraînera une `ReferenceError`. Voici un exemple :

```js
console.log(name);
let name;
```

Cela générera l'erreur :

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-106.png)
_Erreur avec le hoisting d'une variable déclarée avec les mots-clés let et const_

Le même code s'exécuterait sans problème si nous utilisions `var` au lieu de `let` et `const`. Cette erreur est un mécanisme de protection du langage JavaScript, car comme nous l'avons déjà mentionné, un hoisting accidentel peut causer des problèmes inutiles.

# Avant de terminer...

J'espère que vous avez trouvé cet article instructif et qu'il vous aide à mieux comprendre les concepts de `Contexte d'exécution` et de `Hoisting`. J'écrirai bientôt un article sur la `Scope` (portée) et la `Closure` (fermeture) basé sur ces concepts. Restez à l'écoute.

Restons en contact. Vous me trouverez actif sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). N'hésitez pas à me suivre.

Vous aimerez peut-être aussi ces articles :

* [Le mot-clé `this` en JavaScript + 5 règles de liaison clés expliquées pour les débutants en JS](https://www.freecodecamp.org/news/javascript-this-keyword-binding-rules/)
* [Comment apprendre quelque chose de nouveau chaque jour en tant que développeur de logiciels](https://www.freecodecamp.org/news/learn-something-new-every-day-as-a-software-developer/)
* [Mes astuces JavaScript préférées](https://blog.greenroots.info/my-favorite-javascript-tips-and-tricks-ckd60i4cq011em8s16uobcelc)
* [Explique-moi comme si j'avais cinq ans : que sont les symboles ES6 ?](https://blog.greenroots.info/explain-me-like-i-am-five-what-are-es6-symbols-ckeuz5sb8001qafs14of305dw)
* [16 dépôts GitHub de projets secondaires que vous pourriez trouver utiles](https://blog.greenroots.info/16-side-project-github-repositories-you-may-find-useful-ckk50hic406quhls1dui2d6sd)