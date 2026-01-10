---
title: Expressions Infixes VS Expressions Postfixes, et Comment Construire une Meilleure
  Calculatrice JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-05T03:40:19.000Z'
originalURL: https://freecodecamp.org/news/zipline-build-a-smart-javascript-calculator-65e21a8b0b0c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6YO8587U_vTxqVw-OUiqsA.png
tags:
- name: Design
  slug: design
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
seo_title: Expressions Infixes VS Expressions Postfixes, et Comment Construire une
  Meilleure Calculatrice JavaScript
seo_desc: 'By Pramod Sripada

  If you want to make your Simple Calculator a lot smarter, this post is for you.

  You might asking, “What’s wrong with my simple calculator.” Well, it may do all
  the operations correctly, but the sequence in which it does them is prob...'
---

Par Pramod Sripada

Si vous voulez rendre votre Calculatrice Simple beaucoup plus intelligente, cet article est pour vous.

Vous pourriez vous demander, « Qu'est-ce qui ne va pas avec ma calculatrice simple ? » Eh bien, elle peut effectuer toutes les opérations correctement, mais la séquence dans laquelle elle les effectue est probablement incorrecte.

La calculatrice simple ne contient que quatre opérations : addition, soustraction, division et multiplication. Beaucoup d'entre nous ont probablement étudié au lycée la priorité des opérateurs : la division et la multiplication ont la même priorité, et ont une priorité plus élevée que l'addition et la soustraction, qui ont la même priorité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R9O-cK8n4URxuGQPV1Sdfw.png)
_« Veuillez excuser ma chère tante Sally » est un moyen mnémotechnique courant pour se souvenir de l'ordre des opérations (crédit image : [oneyearlease.org](http://www.oneyearlease.org/" rel="noopener" target="_blank" title="))_

Un rappel rapide de la priorité des opérateurs peut être trouvé ici : [http://www.math.utah.edu/online/1010/precedence/](http://www.math.utah.edu/online/1010/precedence/).

La raison pour laquelle je souligne la priorité des opérateurs est qu'une calculatrice simple effectue la plupart des calculs de manière incorrecte. Par exemple, 1+2x3 devrait être égal à 7 selon une calculatrice normale, mais la calculatrice simple donne un résultat de 9.

La raison pour laquelle la calculatrice simple se trompe est qu'elle multiplie simplement les deux opérandes, avec l'opérateur entre eux, et produit le résultat.

Nous ne pouvons pas vraiment blâmer la calculatrice simple. Après tout, elle était censée être simple. Vous pourriez donc commencer à réfléchir à la manière de réorganiser les opérateurs, afin d'obtenir le résultat correct. Oui, vous êtes sur la bonne voie. Pour cela, nous devons connaître deux autres concepts en informatique : les expressions infixes et les expressions postfixes.

En termes simples, les expressions arithmétiques que nous comprenons sont des expressions infixes et les expressions arithmétiques que l'ordinateur comprend sont des expressions postfixes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uB6KUeJDoLWyLUt244Cqsw.png)

Les expressions infixes et postfixes produisent les mêmes résultats. C'est juste que les humains sont habitués à résoudre des expressions infixes, et les ordinateurs sont habitués à résoudre des expressions postfixes.

Une autre caractéristique clé de l'expression postfixe est qu'elle contient des opérateurs succédant aux opérandes selon la priorité, ce qui facilite l'évaluation par l'ordinateur à l'aide de piles, et produit le résultat correct.

À ce stade, vous devez vous demander comment convertir l'expression infixe saisie par votre utilisateur en une expression postfixe. Il existe un algorithme qui convertit une expression infixe en une expression postfixe que l'on peut trouver [**_ici_**](http://csis.pace.edu/~wolf/CS122/infix-postfix.htm).

Voici à quoi ressemble ce processus :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oNj492e1yJgzrFqFS74CYg.png)
_Conversion Infixe en Postfixe_

L'expression postfixe doit être évaluée par un algorithme, que l'on peut trouver [**_ici_**](http://scriptasylum.com/tutorials/infix_postfix/algorithms/postfix-evaluation/). Il est similaire à l'évaluation effectuée par une calculatrice simple, sauf que les opérateurs succèdent aux opérandes dans les expressions postfixes.

En fin de compte, le principal objectif de la conversion d'une expression infixe en une expression postfixe est de préserver la priorité des opérateurs pendant que l'ordinateur évalue l'expression.

Consultez ma calculatrice entièrement fonctionnelle qui incorpore ces principes [**_ici_**](http://codepen.io/pramodvspk/full/RWzxgK/)**_._**