---
title: 'Une variation du problème du sac à dos : comment résoudre le problème de partition
  en sous-ensembles de somme égale en Java'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-10T16:53:32.000Z'
originalURL: https://freecodecamp.org/news/a-variation-on-the-knapsack-problem-how-to-solve-the-partition-equal-subset-sum-problem-in-java-7e0fc047f19b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*u-j8qYS9582smJPe1ZzNcw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Dynamic Programming
  slug: dynamic-programming
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Une variation du problème du sac à dos : comment résoudre le problème
  de partition en sous-ensembles de somme égale en Java'
seo_desc: 'By Fabian Terh

  Previously, I wrote about solving the Knapsack Problem (KP) with dynamic programming.
  You can read about it here.

  Today I want to discuss a variation of KP: the partition equal subset sum problem.
  I first saw this problem on Leetcode —...'
---

Par Fabian Terh

Précédemment, j'ai écrit sur la résolution du problème du sac à dos (KP) avec la programmation dynamique. [Vous pouvez lire à ce sujet ici](https://medium.freecodecamp.org/how-to-solve-the-knapsack-problem-with-dynamic-programming-eb88c706d3cf).

Aujourd'hui, je veux discuter d'une variation du KP : le [problème de partition en sous-ensembles de somme égale](https://leetcode.com/problems/partition-equal-subset-sum/). J'ai d'abord vu ce problème sur Leetcode — c'est ce qui m'a incité à apprendre et à écrire sur le KP.

Voici l'énoncé du problème (reproduit partiellement sans exemples) :

> Étant donné un tableau non vide contenant uniquement des entiers positifs, déterminer si le tableau peut être partitionné en deux sous-ensembles tels que la somme des éléments dans les deux sous-ensembles soit égale.

Pour l'énoncé complet du problème, avec les contraintes et les exemples, consultez le [problème Leetcode](https://leetcode.com/problems/partition-equal-subset-sum/).

### Programmation dynamique

Comme avec le KP, nous allons résoudre ce problème en utilisant la programmation dynamique. Puisque cela est une variation du KP, la logique et la méthodologie sont largement similaires.

### Solution

Nous allons placer notre solution dans une méthode qui retourne un booléen — vrai si le tableau peut être partitionné en sous-ensembles égaux, et faux sinon.

#### Étape 1 : Se prémunir contre une somme impaire du tableau

De manière triviale, si tous les nombres du tableau s'additionnent pour donner une somme impaire, nous pouvons retourner faux. Nous ne procédons que si le tableau s'additionne pour donner une somme paire.

#### Étape 2 : Création du tableau

Ensuite, nous créons le tableau.

Les lignes du tableau représentent l'ensemble des éléments du tableau à considérer, tandis que les colonnes du tableau indiquent la somme que nous voulons atteindre. Les valeurs du tableau sont simplement des valeurs booléennes, indiquant si une somme (colonne) peut être atteinte avec un ensemble d'éléments du tableau (ligne).

Concrètement, la ligne _i_ représente un ensemble d'éléments du tableau des indices 0 à (_i_-1). La raison de ce décalage de 1 est que la ligne 0 représente un ensemble vide d'éléments. Par conséquent, la ligne 1 représente le premier élément du tableau (index 0), la ligne 2 représente les deux premiers éléments du tableau (indices 0-1), et ainsi de suite. Au total, nous créons `n + 1` lignes, y compris 0.

Nous voulons seulement savoir si nous pouvons atteindre exactement la moitié de la somme totale du tableau. Donc, nous n'avons besoin de créer que `totalSum / 2 + 1` colonnes, y compris 0.

#### Étape 3 : Pré-remplissage du tableau

Nous pouvons immédiatement commencer à remplir les entrées pour les cas de base dans notre tableau — la ligne 0 et la colonne 0.

Dans la première ligne, chaque entrée — sauf la première — doit être `false`. Rappelez-vous que la première ligne représente un ensemble vide. Naturellement, nous sommes incapables d'atteindre une somme cible quelconque — le numéro de colonne — sauf 0.

Dans la première colonne, chaque entrée doit être `true`. Nous pouvons toujours, de manière triviale, atteindre une somme cible de 0, indépendamment de l'ensemble des éléments avec lesquels nous devons travailler.

#### Étape 4 : Construction du tableau (le cœur du problème)

Une entrée dans le tableau à la ligne _i_ et à la colonne _j_ est `true` (atteignable) si l'une des trois conditions suivantes est satisfaite :

1. l'entrée à la ligne _i_-1 et à la colonne _j_ est `true`. Rappelez-vous ce que représente le numéro de ligne. Par conséquent, si nous sommes capables d'atteindre une somme particulière avec un sous-ensemble des éléments que nous avons actuellement, nous pouvons également atteindre cette somme avec notre ensemble actuel d'éléments — simplement en n'utilisant pas les éléments supplémentaires. Cela est trivial. Appelons cela `prevRowIsTrue`.
2. L'élément actuel est exactement la somme que nous voulons atteindre. Cela est également trivialement vrai. Appelons cela `isExactMatch`.
3. Si les deux conditions ci-dessus ne sont pas satisfaites, nous avons une dernière façon d'atteindre notre somme cible. Ici, nous utilisons l'élément actuel — l'élément supplémentaire dans l'ensemble des éléments de notre ligne actuelle par rapport à l'ensemble des éléments de la ligne précédente — et vérifions que nous sommes capables d'atteindre le reste de la somme cible. Appelons cela `canArriveAtSum`.

Décomposons la condition 3. Nous ne pouvons utiliser l'élément actuel **que si** il est inférieur à notre somme cible. S'ils sont égaux, la condition 2 serait satisfaite. S'il est plus grand, nous ne pouvons pas l'utiliser. Par conséquent, la première étape consiste à s'assurer que l'élément actuel < somme cible.

Après avoir utilisé notre élément actuel, il nous reste le reste de notre somme cible. Nous vérifions ensuite si cela est atteignable en vérifiant l'entrée correspondante dans la ligne au-dessus.

Comme avec le KP régulier, nous voulons construire progressivement notre tableau de bas en haut. Nous commençons par les cas de base, jusqu'à ce que nous arrivions à notre solution finale.

#### Étape 5 : Retourner la réponse

Nous retournons simplement `return mat[nums.length][totalSum / 2]`.

### Code fonctionnel

Merci d'avoir lu !