---
title: Tutoriel sur l'opérateur ternaire JavaScript et l'instruction If
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-01-25T14:56:28.000Z'
originalURL: https://freecodecamp.org/news/ternary-operator-javascript-if-statement-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/js-ternary.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Tutoriel sur l'opérateur ternaire JavaScript et l'instruction If
seo_desc: 'This tutorial will help you learn how to replace an if/else statement with
  a more concise shorthand syntax called the ternary operator.

  The conditional operator – also known as the ternary operator – is an alternative
  form of the if/else statement th...'
---

Ce tutoriel vous aidera à apprendre comment remplacer une instruction `if/else` par une syntaxe plus concise appelée opérateur ternaire.

L'opérateur conditionnel – également connu sous le nom d'opérateur ternaire – est une forme alternative de l'instruction `if/else` qui vous aide à écrire des blocs de code conditionnels de manière plus concise.

La syntaxe de l'opérateur conditionnel ressemble à ceci :

```js
condition ? expression_si_vrai : expression_si_faux;
```

Tout d'abord, vous devez écrire une _expression conditionnelle_ qui s'évalue en `true` ou `false`. Si l'expression retourne vrai, JavaScript exécutera le code que vous écrivez du côté gauche de l'opérateur deux-points (`:`) ; lorsqu'elle retourne faux, le code du côté droit de l'opérateur deux-points est exécuté.

Pour comprendre comment cela fonctionne, comparons-le avec une instruction `if/else` régulière. Supposons que vous avez un petit programme qui attribue différentes notes d'examen en fonction de votre score :

* Lorsque vous avez un score supérieur à 80, vous attribuez "A" comme note.
* Sinon, vous attribuez "B" comme note.

Voici une façon d'écrire le programme :

```js
let score = 85;
let grade;
if(score >= 80){
    grade = "A";
} else {
    grade = "B";
}

console.log(`Votre note d'examen est ${grade}`);
```

Alternativement, vous pouvez écrire le code ci-dessus en utilisant l'opérateur ternaire comme suit :

```js
let score = 85;
let grade = score >= 80 ? "A" : "B";

console.log(`Votre note d'examen est ${grade}`);
```

Et voilà. La syntaxe abrégée de l'opérateur ternaire semble beaucoup plus concise et plus courte qu'une instruction `if/else` régulière.

Mais que faire si votre code nécessite plusieurs instructions `if/else` ? Que faire si vous ajoutez les notes "C" et "D" à l'évaluation ?

```js
let score = 85;
let grade;
if(score >= 80){
    grade = "A";
} else if (score >= 70) {
    grade = "B";
} else if (score >= 60) {
    grade = "C";
} else {
    grade = "D";
}

console.log(`Votre note d'examen est ${grade}`);
```

Pas de souci ! Vous pouvez écrire plusieurs opérateurs ternaires pour remplacer le code ci-dessus comme ceci :

```js
let score = 85;
let grade = score >= 80 ? "A" 
  : score >= 70 ? "B" 
  : score >= 60 ? "C" 
  : "D";

console.log(`Votre note d'examen est ${grade}`);
```

Cependant, il n'est pas recommandé de remplacer plusieurs instructions `if/else` par plusieurs opérateurs ternaires, car cela rend le code plus difficile à lire à l'avenir. Il est préférable de rester avec soit des instructions `if/else` ou `switch` pour de tels cas.

## Merci d'avoir lu ce tutoriel

Si vous avez apprécié cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous allez réellement avoir l'impression de comprendre ce que vous faites avec JavaScript._

À la prochaine !