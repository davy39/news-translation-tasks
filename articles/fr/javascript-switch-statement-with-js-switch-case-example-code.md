---
title: L'instruction Switch en JavaScript – Avec un exemple de code de cas Switch
  en JS
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2021-04-09T18:27:57.000Z'
originalURL: https://freecodecamp.org/news/javascript-switch-statement-with-js-switch-case-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/js-switch-statement.png
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: L'instruction Switch en JavaScript – Avec un exemple de code de cas Switch
  en JS
seo_desc: "Creating conditionals to decide what action to perform is one of the most\
  \ fundamental parts of programming in JavaScript. This tutorial will help you learn\
  \ how to create multiple conditionals using the switch keyword. \nHow switch statements\
  \ work in J..."
---

Créer des conditionnelles pour décider de l'action à effectuer est l'une des parties les plus fondamentales de la programmation en JavaScript. Ce tutoriel vous aidera à apprendre comment créer plusieurs conditionnelles en utilisant le mot-clé `switch`.

## Comment fonctionnent les instructions switch en JavaScript

Le mot-clé `switch` de JavaScript est utilisé pour créer plusieurs instructions conditionnelles, vous permettant d'exécuter différents blocs de code en fonction de différentes conditions.

Le code ci-dessous vous montre une instruction `switch` en action :

```js
var score = 20;

switch(age){
    case 10:
        console.log("La valeur du score est 10");
        break;
    case 20:
        console.log("La valeur du score est 20");
        break;
    default:
        console.log("La valeur du score n'est ni 10 ni 20");
}
```

Le code ci-dessus affichera `"La valeur du score est 20"` dans la console. L'instruction switch fonctionne en comparant une `expression` donnée avec les expressions dans chaque clause `case`.

Tout d'abord, vous devez passer une `expression` dans l'instruction `switch`, qui est ensuite enfermée dans une paire de parenthèses `()`. Vous pouvez passer une variable ou une valeur littérale comme montré ci-dessous :

```js
var age = 29;

switch(age){}
// ou
switch(true){}
switch("Une chaîne"){}
switch(5+5){}
```

L'`expression` sera évaluée une fois, puis comparée avec les expressions que vous définissez dans chaque clause `case`, de haut en bas.

Dans l'exemple suivant, l'instruction `switch` évaluera la valeur de la variable `flower` puis la comparera avec chaque clause `case` pour voir si elle retourne `true` :

* Le premier `case` comparera si `flower === "rose"`
* Le deuxième `case` comparera si `flower === "violet"`
* Le troisième `case` comparera si `flower === "sunflower"`
* Lorsque les trois clauses `case` retournent `false`, le cas `default` sera exécuté

```js
var flower = "tulip";

switch (flower){
    case "rose":
        console.log("Les roses sont rouges");
        break;
    case "violet":
        console.log("Les violettes sont bleues");
        break;
    case "sunflower":
        console.log("Les tournesols sont jaunes");
        break;
    default:
        console.log("Veuillez sélectionner une autre fleur");
}
```

Le cas `default` est facultatif, ce qui signifie que vous pouvez simplement parcourir l'instruction `switch` sans générer aucune sortie. Mais il est toujours préférable d'inclure un cas `default` pour savoir que l'instruction `switch` est correctement exécutée par JavaScript.

Vous ne pouvez inclure qu'un seul cas `default` dans une instruction `switch`, sinon JavaScript générera une erreur.

Enfin, vous devez inclure le mot-clé `break` dans le corps de chaque clause `case` pour arrêter l'exécution de l'instruction `switch` une fois qu'un cas correspondant est trouvé. Si vous omettez le mot-clé `break`, JavaScript continuera à évaluer l'expression jusqu'à la dernière clause `case`.

Le code suivant affichera à la fois `"Les roses sont rouges"` et `"Veuillez sélectionner une autre fleur"` parce que le mot-clé `break` est omis des clauses `case`, ce qui fait que JavaScript continue la comparaison de l'expression jusqu'au dernier cas, qui est le cas `default` :

```js
var flower = "rose";

switch (flower){
    case "rose":
        console.log("Les roses sont rouges");
    case "violet":
        console.log("Les violettes sont bleues");
    case "sunflower":
        console.log("Les tournesols sont jaunes");
    default:
        console.log("Veuillez sélectionner une autre fleur");
}
```

Même lorsque l'expression `"rose"` a déjà trouvé une correspondance dans la première clause `case`, JavaScript continue d'exécuter l'instruction `switch` parce qu'il n'y a pas de mot-clé `break`.

*Note : il n'y a pas besoin du mot-clé `break` dans le dernier cas, car l'instruction `switch` sera exécutée complètement à ce moment-là.*

Pour résumer, voici comment fonctionne une instruction `switch` :

* Tout d'abord, vous avez besoin d'une `expression` que vous voulez comparer avec certaines conditionnelles.
* Ensuite, vous écrivez toutes les conditionnelles à comparer avec l'`expression` dans chaque clause `case`, y compris un cas `default` lorsqu'il n'y a pas de `case` correspondant.
* Enfin, écrivez le code que vous voulez exécuter à l'intérieur de chaque `case`, suivi du mot-clé `break` pour empêcher JavaScript de comparer davantage l'`expression` avec les clauses `case`.

Maintenant que vous savez comment fonctionne l'instruction `switch`, apprenons quand vous devez utiliser l'instruction `switch` au lieu d'une instruction `if..else`.

## Quand utiliser l'instruction switch

Les instructions `switch` et `if..else` sont toutes deux utilisées pour créer des conditionnelles. La règle générale est que l'instruction `switch` n'est utilisée que lorsque vous avez une **valeur précise** pour les conditionnelles.

C'est parce qu'une instruction `if..else` peut être utilisée pour comparer une `expression` avec une **valeur imprécise** telle que plus grand que ou plus petit que :

```js
var score = 70;

if(score > 50){
  console.log("Le score est supérieur à 50");
} else {
  console.log("Le score est 50 ou inférieur");
}
```

Mais vous ne pouvez pas utiliser `score > 50` comme condition pour une clause `case`. L'exemple suivant affichera le cas `default` même si `score > 50` :

```js
var score = 70;

switch(score){
    case score > 50:
        console.log("Le score est supérieur à 50");
        break;
    default:
        console.log("Le score est 50 ou inférieur");
}
```

Si vous voulez évaluer une valeur imprécise en utilisant l'instruction `switch`, vous devez créer un contournement en évaluant une expression `true` comme dans le code ci-dessous :

```js
var score = 70;

switch(true){
    case score > 50:
        console.log("Le score est supérieur à 50");
        break;
    default:
        console.log("Le score est 50 ou inférieur");
}
```

Bien que le code ci-dessus fonctionnera, il est préférable d'utiliser une instruction `if..else` car elle est plus lisible.

## **Merci d'avoir lu ce tutoriel**

Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : *Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript.*

À la prochaine !