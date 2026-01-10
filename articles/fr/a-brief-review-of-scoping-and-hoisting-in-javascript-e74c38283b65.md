---
title: Une brève revue de la Portée et du Hoisting en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-10T18:43:19.000Z'
originalURL: https://freecodecamp.org/news/a-brief-review-of-scoping-and-hoisting-in-javascript-e74c38283b65
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZyXTRpRSpg2rfqmzJgpJmw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une brève revue de la Portée et du Hoisting en JavaScript
seo_desc: 'By Tiago Romero Garcia

  I bet that any JavaScript developer would want a better understanding of the concepts
  of Scoping and Hoisting. They can silently produce these dreaded unexplainable problems,
  also known as side-effects.

  In a nutshell, scoping a...'
---

Par Tiago Romero Garcia

Je parie que tout développeur JavaScript voudrait une meilleure compréhension des concepts de Portée et de Hoisting. Ils peuvent silencieusement produire ces problèmes inexplicables redoutés, également connus sous le nom d'effets secondaires.

En résumé, la portée et le hoisting affectent la manière dont le code que nous écrivons traitera nos déclarations (telles que var, `let`, `const` et `function`).

Commençons notre récapitulation avec le premier d'entre eux : `var`.

### Travailler avec var

Lorsque vous utilisez `var` pour déclarer vos variables, la fonction parente où vous déclarez vos vars est votre seul délimiteur de portée de facto. Ainsi, la fonction parente crée et maintient la portée pour toutes les variables locales déclarées en son sein.

En d'autres termes, à l'intérieur de la fonction parente, les variables locales naissent, elles font leur travail et lorsque l'exécution de la fonction se termine, elles disparaissent également (sauf si elles sont passées à une autre fonction qui survit à la fonction parente).

C'est la définition de la **Portée Locale**. À l'opposé de la **Portée Globale**, lorsque les variables sont déclarées à l'extérieur de votre fonction. Elles sont accessibles par tout le monde et partout. Elles sont omniprésentes comme l'air que nous respirons, ou comme l'objet `window` dans le navigateur.

Par conséquent, d'autres blocs de code comme les conditionnelles et les boucles (telles que `if`, `for`, `while`, `switch` et `try`) ne délimitent pas la portée, contrairement à la plupart des autres langages.

Ainsi, toute déclaration `var` à l'intérieur de ces blocs sera dans la portée de leur fonction parente qui contient ce bloc.

Non seulement cela, mais pendant l'exécution, chaque déclaration `var` trouvée à l'intérieur de ces blocs de code est déplacée au début de sa fonction parente (sa portée). C'est la définition du **Hoisting**.

Par conséquent, vous ne devriez pas déclarer une variable `var` dans un bloc et penser que cette `var` ne fuit pas à l'extérieur, car elle pourrait l'être !

Voici un exemple :

```
function stepSum() {  var total = 0;
```

```
  for (var i = 0; i < arguments.length; i++) {    var parameter = arguments[i];     total += parameter;    console.log(`${i}) adding ${parameter}`);  }
```

```
  // outside the loop, we can still access vars i and parameter  // even though the were declared within the for loop  console.log(`i=${i}, parameter=${parameter}`);  return total;}
```

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

La sortie est :

```
0) adding 31) adding 22) adding 1i=3, parameter=1total=6
```

Ici, nous pouvons observer que les variables `i` et `parameter` fuient, puisque elles peuvent toutes deux être accessibles depuis la fonction parente. C'est parce qu'elles ont été remontées là, comme si elles avaient été déclarées comme ceci :

```
function stepSum() {  var total = 0;  var i;  var parameter;
```

```
  for (i = 0; i < arguments.length; i++) {    parameter = arguments[i];     total += parameter;    console.log(`${i}) adding ${parameter}`);  }
```

```
  console.log(`i=${i}, parameter=${parameter}`);  return total;}
```

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

Pour éviter toute confusion, il est courant de déclarer les variables dans les premières lignes de la fonction parente. Cela est fait pour éviter de fausses attentes pour toute variable `var` qui pourrait être déclarée quelque part dans la fonction mais qui aurait pu contenir une valeur avant cela.

C'est une source de confusion pour les programmeurs venant de langages avec une portée de bloc (comme C ou Java). Ils déclarent généralement leurs variables au moment où ils sont sur le point de les utiliser pour la première fois.

#### Problèmes avec `var`

Considérons cet extrait de code. Il est similaire au précédent, sauf qu'il calcule chaque somme de manière asynchrone :

```
function stepSum() {  var total = 0;
```

```
  for (var i = 0; i < arguments.length; i++) {    var parameter = arguments[i];
```

```
    setTimeout(function() {      total += parameter;      console.log(`${i}) adding ${parameter}, total=${total}`);    }, i*1000);  }}
```

```
stepSum(3, 2, 1);
```

La sortie est :

```
3) adding 1, total=13) adding 1, total=23) adding 1, total=3
```

Pourquoi cela s'est-il produit ? Il additionne simplement le dernier paramètre 1, trois fois. Et aussi le compteur d'étape est toujours à 3, alors que nous nous attendrions à voir 1, 2 et 3. Qu'est-ce qui ne va pas ici ?

La réponse est la suivante : les variables `i` et `parameter` ont été remontées au début de la fonction `stepSum`, et maintenant elles sont disponibles pour toute la fonction parente. De plus, `parameter` est en fait défini une seule fois, puis il est réaffecté à chaque itération de la boucle for.

Étant donné que nous utilisons des appels `setTimeout` ici, nous pouvons nous attendre à ce que lorsque cette fonction s'exécute pour la première fois (après une seconde), la fonction `stepSum` sera déjà terminée. Ainsi, `parameter` s'est retrouvé avec la valeur de sa dernière affectation, qui provient de la dernière itération de la boucle for, lorsqu'il a été défini à 1. La même chose avec `i` se terminant avec la valeur 3.

C'est pourquoi ces valeurs sont récupérées lorsque les 3 appels `setTimeout` sont finalement exécutés.

Comment pouvons-nous corriger cela ? Simplement en faisant bon usage de la portée et du hoisting. Nous pouvons fournir une nouvelle portée de fonction pour protéger `i` et `parameter` d'être réaffectés. Cela crée une portée locale juste pour eux. Peut-être en utilisant autre chose que var qui peut également nous donner une portée locale dans un bloc, comme nous pouvons le voir ensuite.

### Travailler avec let et const

ES2015 a introduit `let` et `const` qui sont des variables qui respectent la portée de bloc. Cela signifie qu'elles sont sûres à déclarer dans un bloc et ne fuiront pas à l'extérieur, comme le montre l'exemple suivant :

```
function stepSum() {  let total = 0;
```

```
  for (let i = 0; i < arguments.length; i++) {    const parameter = arguments[i];     total += parameter;    console.log(`${i}) adding ${parameter}`);  }
```

```
  // outside the loop, we can no longer access i and parameter  console.log(`i=${i}, parameter=${parameter}`);  return total;}
```

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

La sortie est :

```
0) adding 31) adding 22) adding 1Uncaught ReferenceError: i is not defined  at stepSum (<anonymous>:10:20)  at <anonymous>:13:1
```

D'accord, maintenant que nous avons appris à prévenir les fuites et à protéger les variables dans une portée de bloc, essayons-les !

Revenons au problème `setTimeout` ci-dessus, nous pouvons maintenant utiliser `let` et `const` pour résoudre notre problème :

```
function stepSum() {  let total = 0;
```

```
  for (let i = 0; i < arguments.length; i++) {    const parameter = arguments[i];
```

```
    setTimeout(function() {      total += parameter;     console.log(`${i}) adding ${parameter}, total=${total}`);    }, i*1000);  }}
```

```
stepSum(3, 2, 1);
```

Voilà, maintenant la sortie est ce à quoi nous nous attendons :

```
0) adding 3, total=31) adding 2, total=52) adding 1, total=6
```

Gardez à l'esprit que nous avons créé une paire de variables `i` et `parameter` pour chaque itération de la boucle for. Comparez cela à avant où nous avions un seul `i` et `parameter` réécrits à chaque fois. Cela compte un peu pour la consommation de mémoire.

Enfin, puisque nous avons également créé la fonction de rappel `setTimeout` dans la même portée, elles coexisteront avec les valeurs protégées de `i` et `parameter`. La portée de bloc restera préservée même après que `stepSum` ait terminé son exécution.

### Travailler avec les fonctions

Voici quelque chose de remarquable : déclarer une `function` est différent de déclarer une `var` et de lui assigner une fonction.

Par exemple, voici un exemple de déclaration d'une `function` après son utilisation, pour comprendre comment fonctionne le hoisting. Ceci est un JavaScript valide :

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

```
function stepSum(...args) {  let total = 0;
```

```
  args.forEach((parameter, i) => {     total += parameter;    console.log(`${i}) adding ${parameter}`);  });
```

```
  return total;}
```

La sortie est :

```
0) adding 31) adding 22) adding 1total=6
```

Pourquoi cela a-t-il fonctionné ? Parce que la fonction `stepSum` a été complètement remontée avant d'être utilisée.

Cependant, la déclarer comme une `var` provoque une erreur :

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

```
var stepSum = function(...args) {  let total = 0;
```

```
  args.forEach((parameter, i) => {     total += parameter;    console.log(`${i}) adding ${parameter}`);  });
```

```
  return total;}
```

La sortie est :

```
Uncaught TypeError: stepSum is not a function  at <anonymous>:1:22
```

Pourquoi cela a-t-il échoué ?

La différence ici est que lorsque une `function` est remontée, son corps est également remonté. Comparé à lorsque une `var` est remontée, seule sa déclaration est remontée mais pas son assignation. Ainsi, le code ci-dessus aurait été similaire à ceci, où nous tentons d'utiliser `stepSum` avant que la fonction ne lui soit assignée.

```
var stepSum;console.log(`total=${stepSum(3, 2, 1)}`);
```

```
stepSum = function(...args) {  let total = 0;
```

```
  args.forEach((parameter, i) => {     total += parameter;    console.log(`${i}) adding ${parameter}`);  });
```

```
  return total;}
```

### Prêt pour un défi ?

Maintenant que vous comprenez cela, je voudrais vous laisser un défi pour que vous puissiez expliquer ce qui se passe avec le code ci-dessous :

```
function stepSum(...args) {  let total = 0;
```

```
  args.forEach((parameter, i) => {     total += parameter;    console.log(`${i}) adding ${parameter}`);    return;    function total() {}  });
```

```
  return total;}
```

```
console.log(`total=${stepSum(3, 2, 1)}`);
```

La sortie est :

```
0) adding 31) adding 22) adding 1total=0
```

Pourquoi le 0 ?? Je vous invite à laisser votre explication dans la section des commentaires ci-dessous :)

### En savoir plus

Pour plus de scénarios intéressants sur la portée et le hoisting, je vous suggère de lire cet article clarifiant :

[**JavaScript Scoping and Hoisting**](http://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html)  
[_This method is actually quite flexible, and can be used anywhere you need a temporary scope, not just within blockwww.adequatelygood.com](http://www.adequatelygood.com/JavaScript-Scoping-and-Hoisting.html)

Et après cela, vous pouvez tester vos connaissances avec quelques questions d'entretien :

[**Function Hoisting & Hoisting Interview Questions**](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)  
[_This is a part 2 for my previous article on Variable Hoisting titled A guide to JavaScript variable hoisting ? withm_edium.freecodecamp.org](https://medium.freecodecamp.org/function-hoisting-hoisting-interview-questions-b6f91dbc2be8)

Cet article a été publié à l'origine (version pré-ES2015) le 4 février 2014 sous le titre [Javascript Hoisting](https://coderwall.com/p/jj635w/javascript-hoisting--2).