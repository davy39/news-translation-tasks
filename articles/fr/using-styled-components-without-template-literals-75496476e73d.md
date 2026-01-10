---
title: Comment utiliser styled-components sans littéraux de gabarit
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-01T17:12:58.000Z'
originalURL: https://freecodecamp.org/news/using-styled-components-without-template-literals-75496476e73d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*p1TndLk3UsGPBsM7qHPZIw.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: Web Development
  slug: web-development
seo_title: Comment utiliser styled-components sans littéraux de gabarit
seo_desc: 'By Jake Wiesler

  If you’ve used styled-components in the past, you’ve probably seen the default (according
  to the documentation) way of declaring a component using the styled API:

  import styled from ''styled-components''

  const Button = styled.button`  b...'
---

Par Jake Wiesler

Si vous avez utilisé `styled-components` par le passé, vous avez probablement vu la méthode par défaut (selon la documentation) pour déclarer un composant en utilisant l'API `styled` :

```
import styled from 'styled-components'
```

```
const Button = styled.button`  background: palevioletred;   color: #fff;`
```

Rien de surprenant ici. La documentation utilise ce modèle, et si vous avez consulté du matériel sur `styled-components`, vous avez probablement vu la même chose.

Eh bien, ces dernières semaines, j'ai vu un modèle différent dans quelques bibliothèques utilisant `styled-components`, mais je n'ai pas vu beaucoup d'informations à ce sujet. Le voici :

```
const Button = styled('button')([],  'background: palevioletred',  'color: #fff')
```

C'est intéressant, et j'aimerais l'explorer.

### Comment cela fonctionne-t-il ?

Si vous lisez l'article de [Max Stoiber](https://medium.com/@mxstbr) [The magic behind styled-components](https://mxstbr.blog/2016/11/styled-components-magic-explained/), il entre dans certains détails sur le fonctionnement interne de sa populaire bibliothèque CSS. L'API `styled` de `styled-components` repose sur des littéraux de gabarit étiquetés, et c'est probablement la manière dont vous verrez la plupart des gens l'utiliser.

Mais ce n'est pas la seule façon de déclarer des composants en utilisant l'API `styled`. C'est l'idée clé derrière cet article, bien que cela puisse sembler flou pour l'instant. Alors, pour répondre à la question, *comment cela fonctionne-t-il ?*, nous devons d'abord plonger un peu plus profondément dans les littéraux de gabarit étiquetés.

#### Littéraux de gabarit étiquetés

Faisons une distinction importante concernant les littéraux de gabarit par rapport aux littéraux de gabarit étiquetés. *Quelle est la différence ?*

**Les littéraux de gabarit** sont, selon Mozilla :

> « des littéraux de chaîne permettant des expressions intégrées. »

Ces chaînes peuvent être multi-lignes :

```
const multiLiner = `  Regarde Maman,  2 lignes !`
```

Et elles peuvent également contenir des expressions intégrées, ce qui est une autre façon de dire qu'elles supportent les *interpolations* :

```
const food = 'burger'
```

```
const str = 'Mmmm ! C'est un délicieux ${food} !'
```

![Image](https://cdn-media-1.freecodecamp.org/images/O4ksRAAXJa5q98ps0eX3yfffNUlPzyDX6TEF)
_pulp fiction ya dig_

`${ This here }` est une interpolation. Pensez-y comme des espaces réservés pour des expressions JavaScript.

**Les littéraux de gabarit étiquetés**, en revanche, sont simplement des littéraux de gabarit qui sont utilisés pour appeler une fonction au lieu des valeurs séparées par des virgules à l'intérieur des parenthèses :

```
// appel de fonction régulier
```

```
myFunc(1, 2, 3)
```

```
// appel de fonction étiquetée
```

```
myFunc`1, 2, 3`
```

La deuxième version de `myFunc` ci-dessus est connue sous le nom de **fonction étiquetée**.

La manière dont les deux sites d'appel de `myFunc` transmettent leurs paramètres est ce qui les distingue. Vous savez déjà comment un appel de fonction régulier transmet ses paramètres, mais je ne m'attends pas à ce que vous sachiez comment les fonctions étiquetées le font.

Max [résume cela](https://mxstbr.blog/2016/11/styled-components-magic-explained/) extrêmement bien dans son article, et c'est *la* chose que vous devez comprendre sur les littéraux de gabarit étiquetés, alors je vais résumer comment cela fonctionne en utilisant la même fonction qu'il a créée :

```
const logArgs = (...args) => console.log(...args)
```

La fonction ci-dessus utilise les opérateurs _spread...rest_. Les arguments de la fonction sont collectés dans un seul tableau nommé `args` en utilisant la syntaxe `
...args`. Cela est appelé **rest**. Vous pouvez y penser comme « collecter le reste » des arguments dans un tableau nommé `args`. C'est utile lorsque vous ne savez pas combien d'arguments la fonction pourrait avoir.

Son frère, **spread**, se produit lorsque nous enregistrons les arguments dans la console en utilisant `console.log(...args)`. Nous « étalons » littéralement le contenu du tableau `args`.

Ces deux opérateurs nous aident à visualiser exactement ce qui est passé à `logArgs`. Examinons le résultat de cette fonction lorsqu'elle est appelée de les deux manières décrites précédemment :

```
logArgs(1, 2, 3)
```

```
// -> 1
```

```
// -> 2
```

```
// -> 3
```

```
logArgs`1, 2, 3`
```

```
// -> ["1, 2, 3"]
```

Appeler la fonction normalement fait ce à quoi nous nous attendons. Elle étale le tableau `args` en valeurs individuelles, et enregistre chacune dans la console.

Appeler `logArgs` en utilisant un littéral de gabarit étiqueté, en revanche, enregistre un tableau. C'est notre première leçon :

*Les littéraux de gabarit étiquetés passent un tableau de valeurs de chaîne comme premier argument à la fonction étiquetée.*

Les choses deviennent encore plus intéressantes lorsque nous incluons des interpolations :

```
const food = 'burger'
```

```
logArgs`Mmmm ! C'est un délicieux ${food} !`
```

```
// -> ["Mmmm ! C'est un délicieux ", " !"]
```

```
// -> "burger"
```

`logArgs` produit toujours un tableau de valeurs de chaîne comme premier argument, mais si le littéral de gabarit étiqueté a une interpolation, alors l'expression à l'intérieur de l'interpolation est passée comme argument suivant.

Que se passe-t-il lorsqu'il y a plusieurs interpolations ?

```
const food = 'burger'
```

```
const adj = 'tasty'
```

```
logArgs`Mmmm ! C'est un délicieux ${adj} ${food} !`
```

```
// -> ["Mmmm ! C'est un délicieux ", " ", " !"]
```

```
// -> "tasty"
```

```
// -> "burger"
```

Nous pourrions avoir autant d'interpolations que nous le souhaitons, et chacune sera passée en conséquence. C'est la deuxième leçon :

*Si des interpolations existent à l'intérieur des littéraux de gabarit étiquetés, leurs expressions contenues sont passées comme arguments supplémentaires à la fonction étiquetée.*

Voyons comment les littéraux de gabarit étiquetés gèrent les fonctions interpolées :

```
logArgs`Mmmm ! C'est un délicieux ${() => 'burger'}`
```

```
// -> ["Mmmm ! C'est un délicieux", " !"]
```

```
// -> () => "burger"
```

La fonction elle-même est incluse comme argument. C'est l'essence de `styled-components`. En capturant une telle fonction, la bibliothèque peut l'exécuter et faire ce qu'elle doit faire, principalement fusionner la valeur résultante dans les valeurs de chaîne à l'intérieur du tableau.

### Relier nos nouvelles connaissances

Maintenant que nous savons comment fonctionnent les littéraux de gabarit étiquetés, approfondissons notre compréhension de l'API `styled` :

```
const Button = styled.button`  background: ${props => props.primary ? 'red' : 'white'};  color: black;`
```

`styled.button` est une fonction étiquetée. Si nous devions enregistrer les arguments de cette fonction, nous verrions ceci :

```
logArgs`  background: ${props => props.primary ? 'red' : 'white'};  color: black;`
```

```
// -> ["background: ", "; color: black;"]
```

```
// -> props => props.primary ? "red" : "white"
```

Voyez-vous le pouvoir ici ? Ce n'est pas surprenant que `styled-components` soit devenu si populaire en tant que solution CSS-in-JS. Non seulement les littéraux de gabarit étiquetés nous permettent d'écrire du CSS multi-lignes naturellement, mais ils permettent également à la bibliothèque de manipuler les styles à travers ces fonctions interpolées, donnant à nos composants un aspect dynamique.

### Comment fonctionne l'autre modèle ?

Ah, oui. C'est pourquoi vous êtes ici, n'est-ce pas ? Plus tôt, j'ai montré une autre façon d'utiliser l'API `styled` que j'ai vue récemment :

```
const Button = styled('button')([],  'background: palevioletred',  'color: #fff')
```

Tout d'abord, comprenez que `styled.button` et `styled('button')` sont traités de la même manière. Ils sont interchangeables.

Deuxièmement, il n'y a pas d'action de littéral de gabarit étiqueté ici. Mais, puisque nous savons que `styled` les supporte, *nous savons comment il attend ses arguments*. C'est la clé majeure ?.

Rappelez-vous les deux règles :

1. **Les littéraux de gabarit étiquetés passent un tableau de valeurs de chaîne comme premier argument à la fonction étiquetée.**
2. **Si des interpolations existent à l'intérieur des littéraux de gabarit étiquetés, leurs expressions contenues sont passées comme arguments supplémentaires à la fonction étiquetée.**

Ainsi, la fonction étiquetée attend un tableau de valeurs de chaîne comme premier argument, et les expressions interpolées suivent.

Dans le modèle ci-dessus, que je vais nommer *« The Empty Array Pattern »*, les arguments sont :

```
// -> []
```

```
// -> 'background: palevioletred'
```

```
// -> 'color: #fff'
```

Le premier argument est un tableau, et satisfait la règle numéro un. Oui, il n'y a pas de valeurs de chaîne à l'intérieur du tableau, mais c'est tout à fait correct. Les arguments supplémentaires sont des chaînes qui, par définition, sont des expressions qui produisent une valeur, et en tant que telles, elles satisfont la règle numéro deux.

*Nous avons imité le comportement des littéraux de gabarit étiquetés sans les utiliser réellement.*

### Conclusion

À la fin de la journée, les deux modèles produisent la même valeur. Ce que je trouve difficile à découvrir, c'est pourquoi vous voudriez utiliser l'un plutôt que l'autre. Je suppose que je pourrais voir une situation où, en utilisant des littéraux de gabarit étiquetés, vous aviez plusieurs interpolations, et pour la lisibilité du code, vous pourriez choisir le *Empty Array Pattern* à la place :

```
// en tant que littéral de gabarit étiqueté
```

```
const Button = styled.button`  background: ${ props => props.background };  color: ${ props => props.color };`
```

```
// en tant que Empty Array Pattern
```

```
const Button = styed.button([], props => ({  background: props.background,  color: props.color}))
```

J'adorerais entendre les réflexions d'autres personnes ayant de l'expérience avec ces modèles, et quels sont les avantages et les inconvénients de chacun !

C'était un article croisé de [mon propre blog](https://www.jakewiesler.com/blog/using-styled-components-without-template-literals/). ?

Dites bonjour sur [Twitter](https://twitter.com/jakewies) ?