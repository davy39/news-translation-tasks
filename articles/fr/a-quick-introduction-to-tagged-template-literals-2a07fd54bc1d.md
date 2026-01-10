---
title: Une introduction rapide aux littéraux de gabarit étiquetés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T18:19:34.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-tagged-template-literals-2a07fd54bc1d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iuk6ay4N9W42ACJg7BCjiQ.png
tags:
- name: CSS
  slug: css
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Une introduction rapide aux littéraux de gabarit étiquetés
seo_desc: 'By Michael Ozoemena

  In this article, I’m going to be talking about what “tagged template literals” are
  and some places where I’ve seen them being used.

  What are “tagged template literals”?

  Tagged template literals were enabled by a new technology int...'
---

Par Michael Ozoemena

Dans cet article, je vais parler de ce que sont les « littéraux de gabarit étiquetés » et de quelques endroits où je les ai vus être utilisés.

#### Qu'est-ce que les « littéraux de gabarit étiquetés » ?

Les littéraux de gabarit étiquetés ont été rendus possibles par une nouvelle technologie introduite dans ES6, appelée « littéraux de gabarit ». Il s'agit simplement d'une syntaxe qui permet l'interpolation de chaînes de caractères en JavaScript. Avant l'arrivée des `littéraux de gabarit`, les développeurs JavaScript devaient effectuer des concaténations de chaînes de caractères peu élégantes.

Les `littéraux de gabarit étiquetés` vous offrent la possibilité d'analyser les littéraux de gabarit de la manière que vous souhaitez. Ils fonctionnent en combinant des fonctions avec des `littéraux de gabarit`. Il y a deux parties dans un `littéral de gabarit étiqueté`, la première étant la `fonction d'étiquette` et la seconde, le `littéral de gabarit`.

```
const coolVariable = "Cool Value";
```

```
const anotherCoolVariable = "Another Cool Value";
```

```
randomTagFunctionName`${coolVariable} in a tagged template literal with ${anotherCoolVariable} just sitting there`
```

Maintenant, le premier paramètre dans la `fonction d'étiquette` est une variable contenant un tableau de chaînes de caractères dans le littéral de gabarit :

```
function randomTagFunctionName(firstParameter) {
```

```
console.log(firstParameter);     // ["", " in a tagged template literal with ", " just sitting there"]
```

```
}
```

Et tous les autres paramètres suivants contiendront les valeurs passées au littéral de gabarit :

```
function randomTagFunctionName(firstParameter, secondParameter, thirdParameter) {
```

```
console.log(secondParameter);   // "Cool Value"
```

```
console.log(thirdParameter);   // "Another Cool Value"
```

```
}
```

En tirant parti de l'opérateur Rest d'ES6, nous pouvons redéfinir notre fonction comme ceci :

```
function randomTagFunctionName(firstParameter, ...otherParameters) {
```

```
console.log(otherParameters);   // ["Cool Value", "Another Cool Value"]
```

```
}
```

#### Littéraux de gabarit étiquetés dans Styled-Components.

Maintenant que vous comprenez ce que sont les littéraux de gabarit étiquetés, discutons d'une application de ceux-ci dans le monde réel.

Styled-Components est une bibliothèque JavaScript qui vous permet de créer et d'attacher des styles CSS à vos composants React et React Native. Voici à quoi cela ressemble :

```
const Button = styled.button`  color: red;`
```

Dans l'exemple ci-dessus, Button n'est pas seulement une variable, c'est un composant. Cela signifie que vous pouvez le mélanger avec d'autres composants et sa sortie est un élément de bouton HTML.

C'est un cas d'utilisation très excitant pour les littéraux de gabarit étiquetés car cela vous permet d'avoir un CSS scopé d'une manière qui garde votre fichier de composant propre et vous donne l'impression d'écrire du CSS dans une feuille de style régulière. Sans les littéraux de gabarit étiquetés, nous devrions représenter ce style comme un objet JavaScript comme ceci :

```
const Button = styled.button({  color: 'red'})
```

Un autre cas d'utilisation est avec la bibliothèque [graphql-tag](https://github.com/apollographql/graphql-tag) utilisée dans **Apollo GraphQL**. Je ne pense pas qu'il soit possible de ne pas utiliser la bibliothèque `graphql-tag` lorsque l'on travaille avec Apollo GraphQL (si c'est le cas, faites-le moi savoir !).

#### En conclusion.

Je pense qu'il est formidable d'apprendre de nouvelles technologies et encore mieux de regarder comment les autres les ont utilisées pour résoudre des problèmes. Si vous avez d'autres cas d'utilisation réels pour les littéraux de gabarit étiquetés, faites-le moi savoir.

PS : « Real-World » signifie également vos projets secondaires ou vos exemples de code `codesandbox`.