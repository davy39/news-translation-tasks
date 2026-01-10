---
title: JavaScript String to Date – Analyse de Date en JS
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2022-06-29T15:46:32.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-to-date-date-parsing-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/Javascript-String-to-Date-01-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript String to Date – Analyse de Date en JS
seo_desc: 'Dates are a pretty fundamental concept. We use them all the time. And computers
  use them all the time. But parsing dates using JavaScript can be a little...well,
  interesting.

  In this article, we''ll:


  Discuss date formatting

  Turn a wee ol'' string into...'
---

Les dates sont un concept assez fondamental. Nous les utilisons tout le temps. Et les ordinateurs les utilisent tout le temps. Mais l'analyse des dates en utilisant JavaScript peut être un peu... eh bien, intéressante.

Dans cet article, nous allons :

1. Discuter du formatage des dates
2. Transformer une petite chaîne en un objet date approprié en utilisant JavaScript.
3. Analyser un objet date en un nombre
4. Montrer une méthode alternative pour utiliser des arguments au lieu de chaînes pour créer un objet date.

Les dates sont délicates, mais elles sont aussi incroyablement utiles. Et une fois que vous passez un peu de temps à revoir les bases, votre confiance grandira.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/date.gif)

## Quel est le Format de Date en JavaScript ?

ISO 8601, bien sûr ! C'est le nom de la norme internationale pour communiquer les données de date et d'heure. Nous devons utiliser ce format lorsque nous traitons des dates en JavaScript.

Voici à quoi ressemble ce format. Vous le connaissez déjà – il combine simplement une date et une heure en une seule grande pièce d'information avec laquelle JavaScript peut se familiariser.

```javascript
// AAAA-MM-JJTHH:mm:ss.sssZ
// Une chaîne de date au format ISO 8601
```

## Comment Utiliser le Constructeur `new Date()` en JavaScript

`new Date()` est le constructeur pour créer une nouvelle date en JavaScript. Choc ! 😂

![Image](https://www.freecodecamp.org/news/content/images/2022/06/shocker.gif)

Si vous ne passez rien dans le nouveau constructeur de date, il vous donnera un objet date de la **date et de l'heure actuelles**.

```javascript
new Date()

// Jeu 23 juin 2022 20:35:51 GMT-0400 (Heure avancée de l'Est)
```

Notez qu'un objet date peut, et devrait souvent, contenir une heure jusqu'à la milliseconde en plus du mois, du jour et de l'année.

### Comment Créer une Nouvelle Date Avec une Chaîne

Vous pouvez passer une chaîne de date dans `new Date()` pour créer un objet date.

Vous n'avez pas à spécifier une heure lors de la création d'un objet date.

`new Date('2022-06-13')` est parfaitement valide. Cependant, lorsque vous journalisez cette nouvelle date, vous verrez qu'une heure sera automatiquement attribuée même si nous n'en avons pas déclaré une.

```javascript
let uneDate = new Date('2022-06-13')

// Dim 12 juin 2022 20:00:00 GMT-0400 (Heure avancée de l'Est)
```

Cela peut créer des schismes dans la matrice, et il est préférable d'inclure une date complète. Par exemple, puisque l'heure locale du système est utilisée pour interpréter la date, selon l'endroit où se trouve votre ordinateur dans le monde, vous pourriez obtenir des résultats différents à partir de la même date non spécifique.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/glitch.gif)

Donc, lorsque vous passez une chaîne dans `new Date()`, utilisez une date complète avec heures:minutes.millisecondes.

Un **T** majuscule sépare le composant jour du composant heure comme montré ci-dessous :

```javascript
new Date('2022-05-14T07:06:05.123')

// Sam 14 mai 2022 07:06:05 GMT-0400 (Heure avancée de l'Est)
```

### Comment Créer une Nouvelle Date Avec un Nombre

Vous pouvez également passer un nombre dans un constructeur `new Date()`. Plus d'informations sur ce que représentent les nombres ci-dessous – mais `new Date(1656033105000)`, par exemple, retournera une date légitime :

```javascript
console.log(Date(1656033105000))

// Jeu juin 2022 21:12:06 GMT-0400 (Heure avancée de l'Est)
```

### Comment Créer une Nouvelle Date Avec des Arguments

Plus d'informations sur cela également ci-dessous... Vous pouvez passer jusqu'à sept arguments dans `new Date()`, créant ainsi une méthode plus simple pour représenter une date et une heure au constructeur Date.

```javascript
new Date(2022,03,14,07,33,245)

// Jeu 14 avr 2022 07:37:05 GMT-0400 (Heure avancée de l'Est)
```

## Qu'est-ce que Date.parse() ?

Donc, une chose intéressante se produit si vous utilisez la méthode parse sur un objet date. Elle génère un énorme nombre.

`Date.parse()` nous indique le nombre de millisecondes écoulées depuis le 1er janvier 1970. Cela est utile lorsque vous comparez plusieurs dates. Il est plus facile de comparer et de mesurer les différences entre les dates lorsqu'elles sont converties en nombres plutôt qu'en chaînes.

```javascript
let uneAutreDate = new Date(2012,07,12,12,00,234)

Date.parse(uneAutreDate)

// 1344787434000
```

## Lequel est le Meilleur – Dates Créées Avec des Arguments ou des Chaînes ?

Lorsque vous datez, apprenez à bien argumenter pour un succès à long terme. Lorsque vous utilisez des dates en JavaScript, utilisez des arguments plutôt que des chaînes pour un succès à long terme.

`new Date(2022, 00, 12, 8, 01, 33, 456)`

Cela peut être un peu plus facile que de créer une date en utilisant une chaîne. Les arguments sont simplement entrés dans l'ordre décroissant en commençant par l'année et en terminant par les millisecondes.

La seule partie délicate ici : le mois est indexé à zéro. Donc, janvier est 00.

```javascript
new Date(2022,00,12,8,01,33,456)

// Mer 12 janv 2022 08:01:33 GMT-0500 (Heure normale de l'Est)
```

## Comment Approfondir les Dates en JavaScript

Cela ne fait qu'effleurer la surface de l'objet Date. Consultez [MDN pour une plongée en profondeur](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date). Comme pour toutes choses, il y a un trésor d'informations là-bas.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/deep.gif)

Vous avez maintenant les bases. Allez les mettre en pratique. Vous savez maintenant comment créer un objet date en JavaScript avec `new Date()`. Vous pouvez obtenir la date et l'heure actuelles en ne passant rien dans le constructeur, ou vous pouvez passer une chaîne, un nombre ou des arguments.

## Merci d'avoir lu

Merci d'avoir lu ! J'écris sur le design et le développement ici : [https://blog.eamonncottrell.com/](https://blog.eamonncottrell.com/)

Et vous pouvez me trouver sur [Twitter](https://twitter.com/EamonnCottrell) et [LinkedIn](https://www.linkedin.com/in/eamonncottrell/).

Passez une excellente journée !

![Image](https://www.freecodecamp.org/news/content/images/2022/06/thank-you.gif)