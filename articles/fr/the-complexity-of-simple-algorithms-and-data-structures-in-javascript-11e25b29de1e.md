---
title: La complexité des algorithmes simples et des structures de données en JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:02:28.000Z'
originalURL: https://freecodecamp.org/news/the-complexity-of-simple-algorithms-and-data-structures-in-javascript-11e25b29de1e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1bB3zrN0WrNC6ErArRF6cQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: La complexité des algorithmes simples et des structures de données en JS
seo_desc: 'By Yung L. Leung

  In the previous article “A Step Towards Computing as a Science: Simple Algorithms
  & Data Structures in JS,” we discussed simple algorithms (linear & binary searches;
  bubble, selection & insertion sorts) & data structures (array & key...'
---

Par Yung L. Leung

Dans l'article précédent « [Un pas vers l'informatique en tant que science : algorithmes simples et structures de données en JS](https://medium.com/@yunglleung1/a-step-towards-computing-as-a-science-algorithms-data-structures-4c0e2d6ae79a) », nous avons discuté des algorithmes simples (recherches linéaire et binaire ; tris à bulles, par sélection et par insertion) et des structures de données (tableaux et objets à paires clé-valeur). Ici, je continue avec le concept de complexité et son application à ces algorithmes et structures de données.

### **Complexité**

La **complexité** est un facteur impliqué dans un processus complexe. En ce qui concerne les algorithmes et les structures de données, cela peut être le **temps** ou l'**espace** (c'est-à-dire la mémoire informatique) nécessaire pour effectuer une tâche spécifique (recherche, tri ou accès aux données) sur une structure de données donnée. L'efficacité de l'exécution d'une tâche dépend du nombre d'opérations nécessaires pour accomplir cette tâche.

**Sortir les poubelles** peut nécessiter 3 étapes (attacher un sac poubelle, le sortir et le jeter dans une benne). **Sortir les poubelles** peut être simple, mais si vous sortez les poubelles après une longue semaine de rénovation, vous pourriez vous retrouver incapable d'accomplir la tâche en raison d'un **manque d'espace** dans la benne.

**Passer l'aspirateur dans une pièce** peut nécessiter de nombreuses étapes répétitives (l'allumer, passer répétitivement la tête de l'aspirateur sur le sol et l'éteindre). Plus une pièce est grande, plus vous devrez passer la tête de l'aspirateur sur son sol. Ainsi, plus le **temps** sera long pour passer l'aspirateur dans la pièce.

![Image](https://cdn-media-1.freecodecamp.org/images/L12QMT1j9D8t1gr3hUD5nE72YpEsgo3DPowC)

Il existe donc une relation causale directe entre le nombre d'opérations effectuées et le nombre d'éléments sur lesquels elles sont effectuées. Avoir beaucoup de déchets (éléments) nécessite de les sortir plusieurs fois. Cela peut entraîner un problème de **complexité spatiale**. Avoir une grande surface (éléments) nécessite de passer la tête de l'aspirateur sur le sol de nombreuses fois. Cela peut entraîner un problème de **complexité temporelle**.

Que vous **sortiez les poubelles** ou que vous **passiez l'aspirateur dans une pièce**, vous pourriez dire que le **nombre d'opérations (O)** augmente exactement avec le **nombre d'éléments (n)**. Si j'ai 1 sac poubelle, je dois sortir les poubelles une fois. Si j'avais 2 sacs poubelles, je dois effectuer la même tâche deux fois, en supposant que vous ne pouvez pas physiquement soulever plus d'un sac à la fois. Ainsi, le Big-O de ces corvées est O = n ou O = fonction(n) ou **O(n)**. Il s'agit d'une complexité linéaire (une ligne droite avec une correspondance de 1 opération : 1 élément). Ainsi, 30 opérations sont effectuées sur 30 éléments (ligne jaune sur le graphique).

Cela est similaire à ce qui se passe lorsque l'on considère les algorithmes et les structures de données.

### Recherches

#### Recherche linéaire

![Image](https://cdn-media-1.freecodecamp.org/images/CMLgOmQiGx-An2R8TeY3yghPSmQzfHc4KCsa)
_[source](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif" rel="noopener" target="_blank" title=")_

Le **meilleur cas** pour rechercher un élément dans une liste ordonnée, un après l'autre, est une constante **O(1)**, en supposant qu'il s'agit du premier élément de votre liste. Ainsi, si l'élément que vous recherchez est toujours listé en premier, quelle que soit la taille de votre liste, vous trouverez votre élément instantanément. La complexité de votre recherche est constante avec la taille de la liste. Le **cas moyen au pire cas** de ce type de recherche est une complexité linéaire ou **O(n)**. En d'autres termes, pour n éléments, je dois chercher n fois avant de trouver mon élément, d'où la recherche linéaire.

#### Recherche binaire

![Image](https://cdn-media-1.freecodecamp.org/images/BdVrmbkpWAEROeZzJh-WwglcO3ZvE92aE7Co)
_[source](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif" rel="noopener" target="_blank" title=")_

Pour une recherche binaire, le **meilleur cas** est O(1), ce qui signifie que l'élément de votre recherche est situé au point médian. Le **pire cas et le cas moyen** est le logarithme en base 2 de n ou :

![Image](https://cdn-media-1.freecodecamp.org/images/O4yQ5gMCaNxd9A8fGyTmZRoJlZmUvw2aPxmi)

Le logarithme ou log est une façon d'exprimer un exposant pour une base donnée. Ainsi, s'il y avait 16 éléments (n = 16), il faudrait, dans le pire des cas, 4 étapes pour trouver le nombre 15 (exposant = 4).

![Image](https://cdn-media-1.freecodecamp.org/images/DSYpZXtP0NNN0Poj2wNYEE-n6wQhuekHm8KY)

Ou simplement : **O(log n)**

![Image](https://cdn-media-1.freecodecamp.org/images/xWIc5wqomKmecGODTG4drhWSHdirPt9D9lSE)

### Tris

#### Tri à bulles

![Image](https://cdn-media-1.freecodecamp.org/images/0aAaHJbR5Nb4u4NCSWXn2pomchbOh9ThVPUm)
_[source](https://upload.wikimedia.org/wikipedia/commons/5/54/Sorting_bubblesort_anim.gif" rel="noopener" target="_blank" title=")_

Dans le tri à bulles, chaque élément est comparé au reste de la collection pour déterminer la valeur la plus élevée à faire remonter. Pour cette raison, en **moyenne au pire cas**, sa complexité est **O(n²)**. Imaginez une boucle imbriquée dans une autre boucle.

![Image](https://cdn-media-1.freecodecamp.org/images/02WXe7k1k0y-OFHvIwKyyUh0vNZNs0FUVp-G)

Ainsi, pour chaque élément, vous le comparez au reste de votre collection. Cela revient à 16 comparaisons (ou opérations) pour 4 éléments (4² = 16). Le **meilleur cas** est si votre collection est presque triée, à l'exception d'un seul élément. Cela nécessiterait un seul tour de comparaisons. C'est-à-dire que quatre comparaisons sont nécessaires pour faire remonter un membre d'une collection de quatre éléments, ce qui correspond à une complexité de **O(n)**.

#### Tri par sélection

![Image](https://cdn-media-1.freecodecamp.org/images/3HuokiI2FYWnn70N50fhDf-9LrLBLu3Xdcfk)
_[source](https://codepumpkin.com/selection-sort-algorithms/" rel="noopener" target="_blank" title=")_

Contrairement au **tri à bulles**, au lieu de faire remonter la valeur la plus élevée, le **tri par sélection** sélectionne la valeur la plus faible pour la permuter aux premières positions. Mais, parce qu'il nécessite de comparer chaque élément au reste de la collection, il a également une complexité de **O(n²)**.

#### Tri par insertion

![Image](https://cdn-media-1.freecodecamp.org/images/3tfg-fQ3pfT9czmGkS8p41nLAavr2XlPuxVK)
_[source](https://gfycat.com/densebaggyibis" rel="noopener" target="_blank" title=")_

Contrairement aux tris **à bulles** et **par sélection**, le **tri par insertion** insère l'élément à sa position correcte. Mais, comme les tris précédents, cela nécessite également de comparer chaque élément au reste de la collection, donc il a une complexité **moyenne au pire cas** de **O(n²)**. Comme le **tri à bulles**, s'il ne reste qu'un seul élément à trier, il ne nécessite qu'un seul tour de comparaisons pour insérer l'élément à sa position correcte. C'est-à-dire qu'il a la complexité du **meilleur cas** de **O(n)**.

### Structures de données

#### Tableaux

![Image](https://cdn-media-1.freecodecamp.org/images/5UN4-lEeiZ5sR3wLv3S0t5RU0bKU4ixbPTB7)

Parce qu'il faut une seule étape pour accéder à un élément d'un tableau via son index, ou ajouter/supprimer un élément à la fin d'un tableau, la complexité pour **accéder**, **ajouter** ou **supprimer** une valeur dans un tableau est **O(1)**. Alors que la **recherche linéaire** dans un tableau via son index, comme vu précédemment, a une complexité de **O(n)**.

De plus, parce qu'un **déplacement** ou un **ajout** d'une valeur au début ou à la fin d'un tableau nécessite une **réindexation** de chaque élément qui le suit (c'est-à-dire, supprimer un élément à l'index 0 nécessite de relabeliser l'élément à l'index 1 comme index 0, et ainsi de suite), ils ont une complexité de **O(n)**. La réétiquetage est effectuée du début à la fin du tableau.

#### Objets à paires clé-valeur

![Image](https://cdn-media-1.freecodecamp.org/images/uSM26U11UIi7pAVC9TOM0Ku20YXoAE7C2UCD)
_[source](https://cdn.shopify.com/s/files/1/1147/6518/products/safeandvaultstore-sdbx9-safe-deposit-boxes_large.jpg?v=1495593363" rel="noopener" target="_blank" title=")_

**Accéder**, **insérer** ou **supprimer** une valeur en utilisant une clé est instantané, et donc, ils ont une complexité de **O(1)**. Rechercher dans chaque « boîte de dépôt » un élément spécifique en utilisant toutes les clés disponibles est essentiellement une **recherche linéaire**. Et donc, elle a une complexité de **O(n)**.

### Conclusion

La **complexité** est plus qu'un simple sujet pour discuter des algorithmes et des structures de données établis. Si elle est utilisée judicieusement, elle peut être un outil utile pour évaluer l'efficacité du travail que vous faites et du code que vous créez pour résoudre vos problèmes.

### **Référence :**

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)