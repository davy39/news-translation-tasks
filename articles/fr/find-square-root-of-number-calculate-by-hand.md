---
title: Comment trouver la racine carrée d'un nombre et la calculer à la main
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-07T00:03:15.000Z'
originalURL: https://freecodecamp.org/news/find-square-root-of-number-calculate-by-hand
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/5f9c9cba740569d1a4ca33db.jpg
tags:
- name: Math
  slug: math
seo_title: Comment trouver la racine carrée d'un nombre et la calculer à la main
seo_desc: 'By Alexander Arobelidze

  At times, in everyday situations, we may face the task of having to figure the square
  root of a number. What if there is no calculator or a smartphone handy? Can we use
  an old fashioned paper and pencil to do it in a long divi...'
---

Par Alexander Arobelidze

Parfois, dans des situations quotidiennes, nous pouvons être confrontés à la tâche de devoir trouver la racine carrée d'un nombre. Que faire s'il n'y a pas de calculatrice ou de smartphone à portée de main ? Peut-on utiliser un papier et un crayon à l'ancienne pour le faire à la manière d'une division longue ?

Oui, nous pouvons le faire, et il existe plusieurs méthodes différentes. Certaines sont plus complexes que d'autres. Certaines fournissent des résultats plus précis. 

Celle que je veux partager avec vous en est une. Pour rendre cet article plus convivial pour le lecteur, chaque étape est accompagnée d'illustrations.

## ÉTAPE 1 : Séparer les chiffres en paires 

![Image](https://www.freecodecamp.org/news/content/images/2020/01/step1Alt.png)

Pour commencer, organisons l'espace de travail. Nous diviserons l'espace en trois parties. Ensuite, séparons les chiffres du nombre en paires en allant de droite à gauche. 

Par exemple, le nombre 7,469.17 devient **74**  **69.**  **17**. Ou dans le cas d'un nombre avec un nombre impair de chiffres comme 19,036, nous commencerons par **1**  **90**  **36**. 

Dans notre cas ici, 2,025 devient **20**  **25**.

## ÉTAPE 2 : Trouver le plus grand entier

![Image](https://www.freecodecamp.org/news/content/images/2020/01/step2.png)

Ensuite, nous devons trouver le plus grand entier (i) dont le carré est inférieur ou égal au nombre le plus à gauche. 

Dans notre exemple actuel, le nombre le plus à gauche est 20. Puisque 4² = 16 <= 20 et 5² = 25 > 20, l'entier en question est 4. Déposons 4 dans le coin supérieur droit et 4² = 16 dans le coin inférieur droit.

## ÉTAPE 3 : Maintenant, soustrayez cet entier 

![Image](https://www.freecodecamp.org/news/content/images/2020/01/step3.png)

Maintenant, nous devons soustraire le carré de cet entier (qui est égal à 16) du nombre le plus à gauche (qui est égal à 20). Le résultat est égal à 4 et nous l'écrirons comme indiqué ci-dessus.

## ÉTAPE 4 : Passons à la paire suivante

![Image](https://www.freecodecamp.org/news/content/images/2020/01/step4.png)

Ensuite, passons à la paire suivante dans notre nombre (qui est 25). Nous l'écrivons à côté de la valeur soustraite déjà présente (qui est 4). 

Maintenant, multiplions le nombre dans le coin supérieur droit (qui est également 4) par 2. Cela donne 8 et nous l'écrivons dans le coin inférieur droit suivi de  **_ x _ =**   


## ÉTAPE 5 : Trouver la bonne correspondance

![Image](https://www.freecodecamp.org/news/content/images/2020/01/step5.png)

Il est temps de remplir chaque espace vide avec le même entier (i). Il doit s'agir du plus grand entier possible qui permet au produit d'être inférieur ou égal au nombre de gauche. 

Par exemple, si nous choisissons le nombre 6, le premier nombre devient 86 (8 et 6) et nous devons également le multiplier par 6. Le résultat 516 est supérieur à 425, donc nous descendons et essayons 5. Le nombre 8 et le nombre 5 nous donnent 85. 85 fois 5 donne 425, ce qui est exactement ce dont nous avons besoin. 

Écrivez 5 à côté de 4 dans le coin supérieur droit. C'est le deuxième chiffre de la racine.

## ÉTAPE 6 : Soustraire à nouveau

![Image](https://www.freecodecamp.org/news/content/images/2020/01/step6.png)

Soustraire le produit que nous avons calculé (qui est 425) du nombre actuel à gauche (également 425). Le résultat est zéro, ce qui signifie que la tâche est terminée. 

**Note :** J'ai choisi un carré parfait (2025 = 45 x 45) exprès. De cette façon, j'ai pu montrer les règles pour résoudre les problèmes de racine carrée. 

En réalité, les nombres se composent de nombreux chiffres, y compris ceux après la virgule. Dans ce cas, nous répétons les étapes 4, 5 et 6 jusqu'à ce que nous atteignions la précision souhaitée. 

L'exemple suivant explique ce que je veux dire.

## EXEMPLE : Nous creusons plus profond...

Cette fois, le nombre se compose d'un nombre impair de chiffres, y compris ceux après la virgule.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/EX1.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/01/EX2.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/01/EX3.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/01/EX4.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/01/EX5.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/01/EX6.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/01/EX7.png)

Comme nous l'avons vu dans cet exemple, le processus peut se répéter plusieurs fois pour atteindre un niveau de précision souhaité.