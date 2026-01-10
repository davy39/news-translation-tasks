---
title: Fall-Through dans les instructions Switch en JavaScript – Expliqué avec des
  exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-02T17:42:59.000Z'
originalURL: https://freecodecamp.org/news/fall-through-in-javascript-switch-statements
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/14.-fall-through-2.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Fall-Through dans les instructions Switch en JavaScript – Expliqué avec
  des exemples
seo_desc: 'By Dillion Megida

  Switch statements in JavaScript have a behavior called fall-through which can cause
  unexpected results. I will explain what this behavior is, how to avoid it, and use
  cases for it.

  Switch statements allow you to create conditional s...'
---

Par Dillion Megida

Les instructions switch en JavaScript ont un comportement appelé **fall-through** qui peut causer des résultats inattendus. Je vais expliquer ce qu'est ce comportement, comment l'éviter et ses cas d'utilisation.

Les instructions switch vous permettent de créer des instructions conditionnelles en JavaScript. Vous avez une expression conditionnelle, et selon la valeur retournée par cette expression, vous pouvez avoir différents cas. Le cas qui correspond à cette expression sera exécuté.

Examinons le comportement de fall-through des instructions switch.

## Qu'est-ce que ce comportement de Fall-through ?

Jetez un œil à cet exemple d'instruction switch :

```js
const expression = 10 - 5

switch (expression) {
  case 1:
    console.log("Le résultat est 1")
    break

  case 5:
    console.log("Le résultat est 5")
    break

  case 10:
    console.log("Le résultat est 10")
    break

  default:
    console.log("Le résultat n'existe pas")
}

// Le résultat est 5
```

Ici, nous avons l'expression : `10 - 5`. En utilisant l'opérateur `switch`, nous basculons entre différents `case`s, dont l'un correspond à la valeur retournée par l'expression.

Dans l'exemple, `case 5` correspond à l'expression, donc le code `console.log("Le résultat est 5")` dans ce cas sera exécuté.

Comme vous pouvez le voir, le résultat enregistré est "Le résultat est 5".

Si notre expression était `10 - 1`, le résultat serait 9. Puisqu'il n'y a pas de cas pour cette valeur, le cas `default` sera exécuté et le résultat enregistré sera :

```js
// Le résultat n'existe pas
```

Une instruction commune que vous trouvez dans tous les cas est l'instruction `break`. Que se passerait-il si cette instruction n'était pas dans ces cas ? Voyons ce qui se passe :

```js
const expression = 10 - 5

switch (expression) {
  case 1:
    console.log("Le résultat est 1")

  case 5:
    console.log("Le résultat est 5")

  case 10:
    console.log("Le résultat est 10")

  default:
    console.log("Le résultat n'existe pas")
}

// Le résultat est 5
// Le résultat est 10
// Le résultat n'existe pas
```

Qu'est-ce que vous remarquez ?

Le cas 5, le cas 10 et le cas par défaut sont exécutés. C'est le **comportement de fall-through** en action.

Lorsque vous avez des `case`s et une expression, l'instruction `switch` trouve le premier cas qui correspond à l'expression. Elle commence par le premier cas, `case 1`. Ce cas ne correspond pas, donc l'instruction `switch` continue sa recherche. Ensuite, elle trouve `case 5`. Ce cas correspond à l'expression.

Lorsque l'instruction `switch` trouve ce premier cas qui correspond à l'expression, elle effectue un fall-through où elle exécute les cas restants après le cas correspondant. Peu importe si les cas restants correspondent à l'expression ou non, ils seront exécutés.

J'ai une [version vidéo expliquant ce comportement](https://youtu.be/huQAwJIkYwk) que vous pouvez consulter.

Vous vous demandez probablement "quel est l'avantage de ce comportement ?". Nous allons examiner cela plus tard dans cet article.

## Le mot-clé Break dans les instructions Switch

Le mot-clé `break`, comme vous l'avez vu dans le premier exemple, est un moyen d'informer l'instruction `switch` de **ne pas continuer ; s'arrêter ici**. Sans cette instruction, un fall-through se produit, ce qui signifie que le cas qui correspond à l'expression sera exécuté, ainsi que tous les autres cas qui suivent.

Supposons que nous avons un `break` dans notre `case 10` :

```js
const expression = 10 - 5

switch (expression) {
  case 1:
    console.log("Le résultat est 1")

  case 5:
    console.log("Le résultat est 5")

  case 10:
    console.log("Le résultat est 10")
    break

  default:
    console.log("Le résultat n'existe pas")
}

// Le résultat est 5
// Le résultat est 10
```

D'après les logs, qu'est-ce que vous remarquez ici ? Le cas 5, le cas correspondant, est exécuté. Nous avons "Le résultat est 5" enregistré. Il n'y a pas d'instruction `break`, donc `switch` continue avec les cas qui suivent.

Le cas 10, le cas suivant après le cas 5, est exécuté. Nous avons "Le résultat est 10" enregistré. Ensuite, l'instruction `switch` rencontre un `break` qui est son signal pour s'arrêter. Par conséquent, les cas restants ne sont pas exécutés.

Maintenant, vous voyez pourquoi nous avions un `break` dans chaque cas :

```js
const expression = 10 - 5

switch (expression) {
  case 1:
    console.log("Le résultat est 1")
    break

  case 5:
    console.log("Le résultat est 5")
    break

  case 10:
    console.log("Le résultat est 10")
    break

  default:
    console.log("Le résultat n'existe pas")
}

// Le résultat est 5
```

Sa pertinence est que nous pouvons exécuter uniquement le cas qui correspond à notre expression.

## Le cas par défaut a-t-il besoin d'un Break ?

Dans notre exemple, chaque cas a un `break`, mais le cas `default` n'en a pas. Le cas par défaut en a-t-il besoin ? Eh bien, cela dépend de l'emplacement où le cas par défaut est placé.

Dans notre exemple, le cas `default` est le dernier. Lorsque ce cas est exécuté (car il n'y a pas de cas correspondant pour l'expression), un fall-through est attendu car il n'y a pas d'instruction `break`.

Mais comme le cas par défaut arrive en dernier, il n'y a pas d'autre cas qui le suit dans lequel l'instruction `switch` pourrait continuer.

Mais supposons que nous avions un ordre différent pour le cas `default` :

```js
const expression = 10 - 1

switch (expression) {
  case 1:
    console.log("Le résultat est 1")

  default:
    console.log("Le résultat n'existe pas")

  case 5:
    console.log("Le résultat est 5")

  case 10:
    console.log("Le résultat est 10")
}

// Le résultat n'existe pas
// Le résultat est 5
// Le résultat est 10
```

Ici, l'expression est `10 - 1`, et nous avons supprimé tous les `break`s. Le cas `default` est le deuxième dans l'instruction `switch`. Qu'est-ce que vous remarquez dans les logs ?

Comme il n'y a pas de cas qui correspond à l'expression, le cas `default` est exécuté. Mais ce cas n'a pas de `break` et il y a d'autres cas en dessous. Donc, les cas (5 et 10) après le cas `default` sont également exécutés.

C'est pourquoi j'ai déclaré que cela dépend de l'emplacement où le cas `default` est placé. Dans cet exemple, il serait important d'ajouter un `break` à `default`. Ensuite, nous pouvons sauter un `break` dans le cas 10, car c'est le dernier cas :

```js
const expression = 10 - 1

switch (expression) {
  case 1:
    console.log("Le résultat est 1")
    break

  default:
    console.log("Le résultat n'existe pas")
    break

  case 5:
    console.log("Le résultat est 5")
    break

  case 10:
    console.log("Le résultat est 10")
}

// Le résultat n'existe pas
```

## Avantages du comportement de Fall-through

Ce comportement peut sembler être un bug, mais ce n'en est pas un. Il a son avantage. Vous pouvez tirer parti de ce comportement pour regrouper des cas liés. Voici un exemple :

```js
const expression = 10 - 2

switch (expression) {
  case 2:
    console.log("Le résultat est inférieur à 8")
    break;

  case 5:
    console.log("Le résultat est inférieur à 8")
    break;

  case 8:
    console.log("Le résultat est 8")
    break;

  default:
    console.log("Le résultat n'existe pas")
}

// Le résultat est 8
```

Ici, nous avons une condition de `10 - 2`. Le cas 8 correspond à cette expression, donc nous avons "Le résultat est 8" dans la console.

Si nous changeons la condition en `10 - 8`, le cas 2 correspondra à l'expression, et nous aurons "Le résultat est inférieur à 8" dans la console.

Si nous changeons la condition en `10 - 5`, le cas 5 correspondra à l'expression, et nous aurons "Le résultat est inférieur à 8" dans la console.

Remarquez que le code pour ce cas est similaire au cas 2 ? Alors, au lieu de les écrire séparément, nous pouvons les regrouper.

Voici comment :

```js
const expression = 10 - 5

switch (expression) {
  case 2:

  case 5:
    console.log("Le résultat est inférieur à 8")
    break;

  case 8:
    console.log("Le résultat est 8")
    break;

  default:
    console.log("Le résultat n'existe pas")
}

// Le résultat est inférieur à 8
```

En supprimant le code et le mot-clé `break` du cas 2, nous sommes en mesure de combiner le cas 2 et le cas 5. Avec une condition de `10 - 5`, le cas 5 correspond, et nous avons "Le résultat est inférieur à 8" dans la console.

Avec une condition de `10 - 8`, le cas 2 correspondra. Il n'y a pas de code dans le cas 2, donc rien ne sera exécuté. De plus, il n'y a pas de `break`, donc un fall-through se produit, ce qui signifie que le cas suivant, le cas 5, sera exécuté.

Après l'exécution, nous avons "Le résultat est inférieur à 8" imprimé dans la console. L'instruction `switch` rencontre un mot-clé `break` ici, donc elle sait s'arrêter.

Nous avons été en mesure de regrouper le cas 2 et le cas 5, puisqu'ils sont liés, en tirant parti du comportement de fall-through. Il existe de nombreux scénarios où vous pouvez utiliser ce comportement.

## Conclusion

Dans cet article, nous avons examiné le comportement de fall-through dans les instructions switch. Ce comportement implique l'exécution d'autres cas après le cas correspondant d'une expression. Il se produit par défaut, mais peut être évité avec le mot-clé `break` comme nous l'avons vu dans différents exemples.

Nous avons également vu l'avantage de ce comportement, car il aide à regrouper des cas liés.

Lorsque j'ai commencé à apprendre JavaScript, j'ai appris à toujours utiliser `break` dans mes cas switch, mais je n'ai jamais vraiment compris pourquoi. Je pensais que c'était juste la syntaxe des instructions switch.

Mais seulement après un certain temps, j'ai compris ce que faisait l'instruction `break` – empêcher les fall-throughs.

Peut-être avez-vous une histoire similaire, ou non, mais j'espère que cet article vous apprend quelque chose sur les instructions switch. Veuillez le partager si vous l'avez trouvé utile.