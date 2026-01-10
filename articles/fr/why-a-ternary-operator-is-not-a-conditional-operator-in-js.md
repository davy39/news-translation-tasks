---
title: Pourquoi un opérateur ternaire n'est pas un opérateur conditionnel en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-17T17:17:44.000Z'
originalURL: https://freecodecamp.org/news/why-a-ternary-operator-is-not-a-conditional-operator-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/17.-ternary-not-conditional.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Pourquoi un opérateur ternaire n'est pas un opérateur conditionnel en JS
seo_desc: "By Dillion Megida\nUntil recently, I called a ternary operator a conditional\
  \ operator in JavaScript. But I just learned that this isn't correct. \nIn this\
  \ tutorial, I will explain how I learned this, and hopefully it teaches you something\
  \ new.\nI have a..."
---

Par Dillion Megida

Jusqu'à récemment, j'appelais un opérateur ternaire un opérateur conditionnel en JavaScript. Mais je viens d'apprendre que ce n'est pas correct.

Dans ce tutoriel, je vais expliquer comment j'ai appris cela, et j'espère que cela vous apprendra quelque chose de nouveau.

J'ai une [version vidéo sur ce sujet](https://youtu.be/vcNlFKzZTq4) que vous pouvez regarder pour compléter votre apprentissage.

## Comment j'ai appris l'opérateur ternaire

J'ai récemment écrit un article sur [l'opérateur ternaire en JavaScript](https://www.freecodecamp.org/news/the-ternary-operator-in-javascript/). Dans cet article, j'ai défini l'opérateur ternaire en commençant comme ceci :

> "L'opérateur ternaire est un opérateur conditionnel..."

Voici une capture d'écran de cette phrase :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-80.png)

**Note :** Je vais apporter quelques mises à jour à cet article lorsque j'aurai terminé celui-ci, alors ne soyez pas surpris si vous ne voyez pas certains des textes que je mentionne ici.

Après avoir publié cet article, [quelqu'un l'a partagé sur Twitter](https://twitter.com/OnlineMDdavid/status/1612935576373673985?s=20&t=87LZfssH26pOK0bJwMBzXw), disant "Merci", et puis [quelqu'un d'autre a fait un commentaire sous le tweet](https://twitter.com/jonrandy/status/1613541257728626691?s=20&t=87LZfssH26pOK0bJwMBzXw) expliquant que "Un opérateur ternaire est un opérateur conditionnel" est une affirmation erronée :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-83.png)

Ces commentaires m'ont fait faire un pas en arrière, et après les avoir lus plusieurs fois, cela avait tout son sens. Merci, Jon !

Je suis ensuite allé en ligne pour rechercher les opérateurs ternaires, et les catégories d'opérateurs en général (qui incluent également les opérateurs **unaires** et **binaires**).

Mes apprentissages de ces commentaires et de mes recherches m'ont conduit à écrire mon récent article sur [les opérateurs unaires, binaires et ternaires en JavaScript](https://www.freecodecamp.org/news/unary-binary-ternary-operators-javascript/), où j'ai expliqué ces catégories et montré quelques exemples d'opérateurs qui relèvent de chaque catégorie. Cela vaut la peine d'y jeter un coup d'œil.

## C'est vrai – un opérateur ternaire n'est pas un opérateur conditionnel

Dans mon article sur les opérateurs unaires, binaires et ternaires, j'ai expliqué que :
* Les opérateurs unaires nécessitent un opérande
* Les opérateurs binaires nécessitent deux opérandes
* Les opérateurs ternaires nécessitent trois opérandes

J'ai également mentionné que ces catégories ne s'appliquent pas seulement à JavaScript, mais aux langages de programmation en général.

Un exemple d'opérateur unaire est `typeof`, qui nécessite seulement un opérande.

Pour les opérateurs binaires, un exemple est l'opérateur arithmétique plus `+` qui nécessite deux opérandes (un avant, et l'autre après l'opérande) pour effectuer l'opération de somme.

Alors que les opérateurs unaires et binaires ont plusieurs exemples, **il n'y a qu'un seul opérateur qui est classé comme opérateur ternaire : l'opérateur conditionnel**. C'est là que vient la confusion.

L'opérateur conditionnel nécessite trois opérandes :

```js
condition ? truthyExpression : falsyExpression
```

`condition` est le premier opérande, `truthyExpression` est le deuxième, et `falsyExpression` est le troisième.

La raison pour laquelle beaucoup de gens (y compris moi-même, jusqu'à récemment) appellent l'opérateur ternaire un opérateur conditionnel, est que l'opérateur conditionnel est le seul opérateur ternaire en JavaScript (et dans certains autres langages également).

Mais une chose à noter ici est que dans certains autres langages de programmation (qui existent actuellement ou existeront à l'avenir), il pourrait y avoir plus d'exemples d'opérateurs ternaires.

Donc le point est que "un opérateur ternaire **n'est pas** un opérateur conditionnel". La meilleure affirmation est : "Un opérateur conditionnel est un opérateur ternaire". Un opérateur conditionnel nécessite trois opérandes, ce qui signifie qu'il relève de la catégorie ternaire.

## Conclusion

Le but de cet article n'est pas de dire "ne dites jamais qu'un opérateur ternaire est un opérateur conditionnel". Vous pouvez toujours dire cela et tous les développeurs comprendront probablement ce que vous dites.

Le but de cet article est de vous montrer que "littéralement", cette affirmation n'est pas correcte, même si elle est largement utilisée.

La meilleure affirmation (que je vais apprendre à dire désormais) est "un opérateur conditionnel est un opérateur ternaire en JavaScript"

Si vous avez appris quelque chose de cet article, veuillez le partager avec les autres :)