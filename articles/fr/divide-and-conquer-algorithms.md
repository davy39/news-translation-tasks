---
title: 'Algorithme Diviser pour Régner : Signification et Explications avec Exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-26T18:30:00.000Z'
originalURL: https://freecodecamp.org/news/divide-and-conquer-algorithms
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f04740569d1a4ca4062.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: 'Algorithme Diviser pour Régner : Signification et Explications avec Exemples'
seo_desc: 'What are Divide and Conquer Algorithms? (And no, it''s not "Divide and
  Concur")

  Divide and Conquer is an algorithmic paradigm (sometimes mistakenly called "Divide
  and Concur" - a funny and apt name), similar to Greedy and Dynamic Programming.
  A typica...'
---

## Qu'est-ce que les algorithmes Diviser pour Régner ? (Et non, ce n'est pas "Diviser et Conquérir")

Diviser pour Régner est un paradigme algorithmique (parfois appelé à tort "Diviser et Conquérir" - un nom amusant et approprié), similaire aux algorithmes Gloutons et à la Programmation Dynamique. Un algorithme typique Diviser pour Régner résout un problème en utilisant les trois étapes suivantes.

1. **Diviser** : Diviser le problème donné en sous-problèmes de même type. Cette étape consiste à diviser le problème en sous-problèmes plus petits. Les sous-problèmes doivent représenter une partie du problème original. Cette étape utilise généralement une approche récursive pour diviser le problème jusqu'à ce qu'aucun sous-problème ne soit plus divisible. À ce stade, les sous-problèmes deviennent atomiques par nature mais représentent toujours une partie du problème réel.
2. **Régner** : Résoudre récursivement ces sous-problèmes. Cette étape reçoit de nombreux sous-problèmes plus petits à résoudre. Généralement, à ce niveau, les problèmes sont considérés comme "résolus" par eux-mêmes.
3. **Combiner** : Combiner les réponses de manière appropriée. Lorsque les sous-problèmes plus petits sont résolus, cette étape les combine récursivement jusqu'à ce qu'ils forment une solution du problème original. Cette approche algorithmique fonctionne de manière récursive, et les étapes de conquête et de fusion sont si proches qu'elles semblent ne faire qu'une.

Cette méthode nous permet généralement de réduire considérablement la complexité temporelle.

Par exemple, le Tri Bulle utilise une complexité de `O(n^2)`, tandis que le tri rapide (une application de Diviser pour Régner) réduit la complexité temporelle à `O(nlog(n))`. La Recherche Linéaire a une complexité temporelle de `O(n)`, tandis que la Recherche Binaire (une application de Diviser pour Régner) réduit la complexité temporelle à `O(log(n))`.

Voici quelques algorithmes standards qui relèvent de la catégorie des algorithmes Diviser pour Régner.

**Recherche Binaire** est un algorithme de recherche. À chaque étape, l'algorithme compare l'élément d'entrée (x) avec la valeur de l'élément du milieu dans le tableau. Si les valeurs correspondent, il retourne l'index du milieu. Sinon, si x est inférieur à l'élément du milieu, l'algorithme récurse sur la partie gauche de l'élément du milieu, sinon il récurse sur la partie droite de l'élément du milieu.

**Tri Rapide** est un algorithme de tri. L'algorithme choisit un élément pivot, réorganise les éléments du tableau de telle sorte que tous les éléments plus petits que le pivot se déplacent à gauche du pivot, et tous les éléments plus grands se déplacent à droite. Enfin, l'algorithme trie récursivement les sous-tableaux à gauche et à droite de l'élément pivot.

**Tri Fusion** est également un algorithme de tri. L'algorithme divise le tableau en deux moitiés, les trie récursivement, et fusionne finalement les deux moitiés triées. La complexité temporelle de cet algorithme est `O(nLogn)`, qu'il s'agisse du meilleur cas, du cas moyen ou du pire cas. Sa complexité temporelle peut être facilement comprise à partir de l'équation de récurrence : `T(n) = 2T(n/2) + n`.

**Paire de Points la Plus Proche** Le problème consiste à trouver la paire de points la plus proche dans un ensemble de points dans le plan x-y. Le problème peut être résolu en temps `O(n^2)` en calculant les distances de chaque paire de points et en comparant les distances pour trouver le minimum. L'algorithme Diviser pour Régner résout le problème en temps `O(nLogn)`.

**Algorithme de Strassen** est un algorithme efficace pour multiplier deux matrices. Une méthode simple pour multiplier deux matrices nécessite 3 boucles imbriquées et est `O(n^3)`. L'algorithme de Strassen multiplie deux matrices en temps `O(n^2.8974)`.

**Algorithme de Transformée de Fourier Rapide (FFT) de Cooley-Tukey** est l'algorithme le plus courant pour la FFT. Il s'agit d'un algorithme Diviser pour Régner qui fonctionne en temps `O(nlogn)`.

**Algorithme de Karatsuba** était le premier algorithme de multiplication asymptotiquement plus rapide que l'algorithme quadratique "scolaire". Il réduit la multiplication de deux nombres à n chiffres à au plus n^1.585 (ce qui est une approximation du logarithme de 3 en base 2) produits de chiffres uniques. Il est donc plus rapide que l'algorithme classique, qui nécessite n^2 produits de chiffres uniques.

### Diviser pour Régner (D & C) vs Programmation Dynamique (PD)

Les deux paradigmes (D & C et PD) divisent le problème donné en sous-problèmes et résolvent les sous-problèmes. Comment choisir l'un d'eux pour un problème donné ? Diviser pour Régner doit être utilisé lorsque les mêmes sous-problèmes ne sont pas évalués plusieurs fois. Sinon, la Programmation Dynamique ou la Mémoisation doit être utilisée.

Par exemple, la Recherche Binaire est un algorithme Diviser pour Régner, nous n'évaluons jamais les mêmes sous-problèmes à nouveau. En revanche, pour calculer le n-ième nombre de Fibonacci, la Programmation Dynamique doit être préférée.