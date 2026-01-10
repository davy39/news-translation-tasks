---
title: Quand utiliser une déclaration de fonction vs. une expression de fonction
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-19T15:44:14.000Z'
originalURL: https://freecodecamp.org/news/when-to-use-a-function-declarations-vs-a-function-expression-70f15152a0a0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i6ZBOiPaCeOTkUWhrb4TRw.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Quand utiliser une déclaration de fonction vs. une expression de fonction
seo_desc: 'By Amber Wilkie

  Tech Jargon Series

  It’s likely you already know how to write functions in both these ways. function
  doStuff() {} and () => {} are characters we type all day. But how are they different
  and why use one over the other?

  Note: Examples ar...'
---

Par Amber Wilkie

#### Série de Jargon Technique

Il est probable que vous sachiez déjà comment écrire des fonctions de ces deux manières. `function doStuff() {}` et `() => {}` sont des caractères que nous tapons toute la journée. Mais en quoi sont-ils différents et pourquoi utiliser l'un plutôt que l'autre ?

**Note :** Les exemples sont donnés en JavaScript. _V_os _K_m _P_euvent _V_arier avec d'autres langages.

![Image](https://cdn-media-1.freecodecamp.org/images/qAG2vEw9KwotPTqwyfiaoNL9HMdE7l5VkayJ)

### La première différence : un nom

Lorsque vous créez une fonction avec un _nom_, il s'agit d'une **déclaration de fonction**. Le nom peut être omis dans les **expressions de fonction**, rendant cette fonction "anonyme".

**Déclaration de fonction :**

```
function doStuff() {};
```

**Expression de fonction :**

```
const doStuff = function() {}
```

Nous voyons souvent des fonctions anonymes utilisées avec la syntaxe ES6 comme suit :

```
const doStuff = () => {}
```

### Hoisting

Le hoisting fait référence à la disponibilité des fonctions et des variables "en haut" de votre code, par opposition à seulement après leur création. Les objets sont initialisés au moment de la compilation et disponibles n'importe où dans votre fichier.

**Les déclarations de fonction sont hoistées mais les expressions de fonction ne le sont pas.**

C'est facile à comprendre avec un exemple :

```
doStuff();
```

```
function doStuff() {};
```

Ce qui précède ne génère pas d'erreur, mais ceci en générerait une :

```
doStuff();
```

```
const doStuff = () => {};
```

### Le cas des expressions de fonction

Il pourrait sembler que les déclarations de fonction, avec leurs puissantes propriétés de hoisting, vont surpasser les expressions de fonction en termes d'utilité. Mais choisir l'une plutôt que l'autre nécessite de réfléchir à **quand et où la fonction est nécessaire**. Basiquement, qui a besoin de la connaître ?

Les expressions de fonction sont invoquées pour **éviter de polluer la portée globale**. Au lieu que votre programme soit conscient de nombreuses fonctions différentes, lorsque vous les gardez anonymes, elles sont utilisées et oubliées immédiatement.

#### IIFE

Le nom — **immediately invoked function expressions** — dit à peu près tout ici. Lorsqu'une fonction est créée au même moment où elle est appelée, vous pouvez utiliser une IIFE, qui ressemble à ceci :

```
(function() => {})()
```

ou :

```
(() => {})()
```

Pour un examen approfondi des IIFE, consultez [cet article complet](https://mariusschulz.com/blog/use-cases-for-javascripts-iifes).

#### Callbacks

Une fonction passée à une autre fonction est souvent appelée un "callback" en JavaScript. Voici un exemple :

```
function mapAction(item) {
  // faire des choses à un élément
}
array.map(mapAction)
```

```
array.map(mapAction)
```

Le problème ici est que `mapAction` sera disponible pour toute votre application — il n'y a pas besoin de cela. Si ce callback est une expression de fonction, il ne sera pas disponible en dehors de la fonction qui l'utilise :

```js
array.map(item => { // faire des choses à un élément })
```

ou

```js
const mapAction = function(item) {
  // faire des choses à un élément
}
array.map(mapAction)
```

```
array.map(mapAction)
```

bien que `mapAction` sera disponible pour le code _en dessous_ de son initialisation.

### Résumé

En bref, utilisez les déclarations de fonction lorsque vous souhaitez créer une fonction dans la portée globale et la rendre disponible dans tout votre code. Utilisez les expressions de fonction pour limiter où la fonction est disponible, garder votre portée globale légère et maintenir une syntaxe propre.

### Références

* [Déclaration de fonction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function), docs MDN.
* [Expression de fonction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/function), docs MDN.
* [Hoisting](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting), glossaire MDN.

### La Série de Jargon Technique

Il y a tant de phrases qui sont lancées lors des meetups et conférences tech, en supposant que tout le monde est déjà familiarisé avec le jargon. Je ne suis souvent pas familiarisé avec le jargon. Il est courant que les développeurs fassent semblant d'être surpris que je manque d'une pièce de connaissance.

La vérité est que je ne connais souvent tout simplement pas le bon mot pour cela. En tant qu'humains, mais surtout en tant qu'humains développeurs, nous aimons écarter ceux qui ne "parlent pas le langage", donc cette série vise à obtenir une compréhension solide des concepts de programmation que l'on "devrait connaître".

Il s'agit du deuxième article de la série. Le premier était [higher-order functions](https://medium.freecodecamp.org/higher-order-functions-what-they-are-and-a-react-example-1d2579faf101). Restez à l'affût pour plus d'articles alors que je vais à des meetups et conférences et fais semblant de savoir de quoi parlent mes collègues tech, mais dois ensuite rentrer chez moi et le chercher sur Google.