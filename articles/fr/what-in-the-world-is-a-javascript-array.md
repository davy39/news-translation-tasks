---
title: Qu'est-ce qu'un tableau JavaScript au juste ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-01T19:15:47.000Z'
originalURL: https://freecodecamp.org/news/what-in-the-world-is-a-javascript-array
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/kimberly-farmer-lUaaKCUANVI-unsplash.jpg
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce qu'un tableau JavaScript au juste ?
seo_desc: 'By Syk Houdeib

  This article is a beginner''s introduction to JavaScript arrays and data structures.
  It covers why we need them, and how they fit into the front-end context.

  Introduction

  When I first started learning to program, I would regularly encou...'
---

Par Syk Houdeib

Cet article est une introduction pour débutants aux tableaux JavaScript et aux structures de données. Il explique pourquoi nous en avons besoin et comment ils s'intègrent dans le contexte du développement front-end.

## Introduction

Lorsque j'ai commencé à apprendre à programmer, je rencontrais régulièrement des concepts difficiles à situer dans le tableau d'ensemble. Venant d'un milieu non traditionnel, je trouvais des mots comme "structures de données" et "tableaux" souvent difficiles à placer dans un contexte qui avait du sens. Ou pourquoi ils étaient nécessaires pour le développement front-end.

De nos jours, les données et les tableaux font partie de mon quotidien en tant que développeur front-end. Mais je me souviens encore de toute cette confusion initiale. Mon objectif ici est de donner un aperçu de haut niveau conçu pour les personnes n'ayant aucun background en ingénierie. Et de tout placer dans un contexte réaliste.

Dans cet article, nous parlerons de ce qu'est la **donnée** et de la manière dont nous l'**organisons**. Nous examinerons les structures de données en nous concentrant uniquement sur les **tableaux** pour garder les choses claires. Et nous verrons pourquoi nous en avons besoin.

### L'installation

Imaginons que nous travaillons sur une plateforme en ligne qui nous permet de faire nos courses de supermarché depuis un site web. C'est une application concrète des choses dont nous voulons parler ici.

Jetez un œil à [Lola Market](https://lolamarket.com/tienda), où je travaille, pour voir à quoi cela pourrait ressembler.

Notre site web va afficher une liste de produits. Ce sera notre point de départ pour parler des données et de leur organisation dans un contexte qui imite ce que nous faisons tous les jours en front-end.

## Qu'est-ce que la donnée ?

Avant de commencer à parler de la manière dont nous organisons les données, essayons de comprendre ce que signifie la donnée dans notre contexte. Et d'où viennent ces données.

Lorsque vous travaillez dans le domaine numérique, il est utile de se rappeler que tout est donnée. Tout est des bits stockés en binaire.

Maintenant, bien que cela puisse être intéressant, c'est si général que cela ne nous est d'aucune aide. Donc, pour nos besoins, nous allons nous concentrer sur une idée étroite de ce qu'est la donnée. Celle qui est la plus immédiatement pertinente. Jetez un œil à la liste suivante :

![Une liste de produits : Champignons, Steak, Poisson, Aubergines, Lentilles](https://www.freecodecamp.org/news/content/images/2019/08/products-list-1.png)
_Listes de produits_

Cette liste réduite est un exemple du type de produits que vous pouvez trouver sur ce site web que nous construisons. Cette liste est notre donnée : champignons, steak, poisson, aubergines et lentilles.

## D'où viennent ces données ?

Les données peuvent vivre directement dans votre application, dans votre code front-end. Mais plus couramment, elles proviennent d'une source externe. Généralement, ces données sont stockées dans une base de données.

Le front-end fait une requête à la base de données et reçoit ces données en réponse. Une fois qu'elles sont arrivées dans notre application front-end, il est temps pour nous de faire ce que nous devons en faire. Par exemple, afficher le nom du produit sur le site web, le styliser et ajouter les fonctionnalités nécessaires (comme un bouton "ajouter au panier").

Jetez un œil à n'importe quel site de shopping populaire et vous verrez le même schéma. Il aura une liste de produits présentée dans un certain style avec diverses fonctionnalités et d'autres informations à ce sujet.

## Comment organisons-nous les données ?

Nous avons établi que cette liste de produits est notre donnée. Maintenant, nous devons empaqueter cette donnée dans une sorte de conteneur. Cela nous permettra de l'organiser, de la déplacer et d'y accéder plus tard pour faire des choses avec.

L'une des manières les plus courantes d'organiser les données avec lesquelles vous travaillerez fréquemment s'appelle un **tableau**. Voici à quoi ressemble un tableau :

```js
['champignons', 'steak', 'poisson', 'aubergines', 'lentilles']
```

La syntaxe semble assez simple. Vous créez un tableau avec les crochets `[]`. Et vous séparez les éléments individuels avec une virgule `,`. Si vos données sont composées de **chaînes de caractères**, placez chaque élément entre guillemets simples ou doubles `''`. **Chaîne de caractères** signifie grossièrement un ensemble de caractères représentant du texte, comme des mots et des phrases.

Et c'est tout. Vous venez d'organiser vos données dans un seul paquet appelé **tableau**. Et nous pouvons maintenant faire beaucoup de choses avec cela. Vous pouvez penser à un tableau comme un simple conteneur qui nous permet de mettre des données à l'intérieur, de les organiser dans une certaine structure et de nous permettre de faire des choses avec.

Un tableau est un exemple de ce que nous appelons **structures de données**. Ce sont les différentes manières dont nous utilisons pour organiser les données. Il y en a beaucoup, mais les deux plus courantes en front-end sont les tableaux et les objets.

Alors maintenant, que faisons-nous avec cela ?

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-216.png)
_Photo par [Unsplash](https://unsplash.com/@impatrickt?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Patrick Tomasso</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## Pourquoi avons-nous besoin des tableaux ?

Nous avons besoin des tableaux et d'autres structures de données en front-end parce que presque tout ce avec quoi nous traitons est de la donnée. Et cela doit être organisé de manière à ce que nous puissions travailler avec.

Dans notre exemple, une fois que nous recevons le tableau des produits, nous pouvons écrire la logique qui prend chaque produit et affiche son nom sur notre site web. Mais comment sélectionnons-nous chaque élément du tableau et faisons-nous des choses avec ?

Dans l'article ci-dessous, j'explique justement cela. Je prends notre exemple à l'étape suivante et parle de la manière dont les **boucles** entrent en jeu pour commencer à traiter nos données - allez y jeter un œil !

[https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for/](https://www.freecodecamp.org/news/what-in-the-world-is-a-javascript-loop-for/)

## Conclusion

Donc, pour récapituler. Pour notre supermarché en ligne, nous avons un ensemble de produits et c'est notre donnée. Nous avons vu comment nous organisons cette donnée dans des structures de données comme le tableau. Cela est généralement stocké dans une base de données. Nous pouvons ensuite demander cette donnée. Et une fois qu'elle "arrive" dans notre application front-end depuis la base de données, nous pouvons commencer à la traiter et à faire des choses avec. Espérons que cela vous a donné une meilleure idée de pourquoi nous en avons besoin dans notre front-end.

Bien sûr, il y a plus à savoir sur les structures de données que les tableaux composés de chaînes de caractères. Ci-dessous, je vous laisse avec un peu plus d'informations pour élargir votre compréhension. Des choses que vous pourriez vouloir examiner ensuite pour comprendre ces concepts de manière plus complète.

Le premier endroit où je cherche des informations est toujours [MDN](https://developer.mozilla.org). C'est l'une des sources d'informations les plus fiables pour les développeurs.

* **Structures de données** : En plus des tableaux, vous devrez rapidement vous familiariser avec les **objets**. C'est une structure de données encore plus courante. En fait, comprendre les objets est essentiel pour comprendre JavaScript dans son ensemble.
* **Types de données** : Les données avec lesquelles nous avons travaillé ici étaient composées de `chaînes de caractères`. Mais il existe quelques autres types de données comme les `nombres` et les `booléens` (vrai ou faux) que vous devrez comprendre.
* **Requêtes** : Nous avons brièvement mentionné comment nous ferions généralement une requête à notre base de données pour obtenir les données dont nous avons besoin. Travailler avec des API, `fetch()`, faire des requêtes et gérer la réponse est un sujet avancé que vous pouvez laisser pour plus tard. Mais c'est un sujet qui sera essentiel au moment où vous commencerez à passer des entretiens pour un poste de développeur.

### Clôture

Merci d'avoir lu. J'espère que vous avez trouvé cela utile. Et si vous avez aimé, le partager serait grandement apprécié. Si vous avez des questions ou des commentaires, je suis sur [Twitter](https://twitter.com/Syknapse) [@Syknapse](https://twitter.com/Syknapse) et j'adorerais avoir de vos nouvelles.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-157.png)
_Photo par [Claudia](https://twitter.com/__Santaella)_

Je m'appelle Syk et je suis développeur front-end chez [Lola Market](https://twitter.com/Tech_LolaMarket) à Madrid. J'ai changé de carrière pour devenir développeur web depuis un domaine sans rapport, donc j'essaie de créer du contenu pour ceux qui sont sur un chemin similaire. Mes messages directs sont toujours ouverts pour les développeurs web en herbe ayant besoin de soutien. Vous pouvez également lire ma transformation dans [cet article](https://medium.com/free-code-camp/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b).

[https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/](https://www.freecodecamp.org/news/how-i-switched-careers-and-got-a-developer-job-in-10-months-a-true-story-b8895e855a8b/)