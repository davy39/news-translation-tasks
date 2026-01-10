---
title: Recherche en Largeur - Un Guide de Parcours de Graphe BFS avec 3 Exemples Leetcode
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-26T21:16:31.000Z'
originalURL: https://freecodecamp.org/news/breadth-first-search-a-bfs-graph-traversal-guide-with-3-leetcodeexamples
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/graph_theory_design_web_forms_08.png
tags:
- name: algorithms
  slug: algorithms
seo_title: Recherche en Largeur - Un Guide de Parcours de Graphe BFS avec 3 Exemples
  Leetcode
seo_desc: 'By Anamika Ahmed

  Breadth First Search (BFS) is one of the most popular algorithms for searching or
  traversing a tree or graph data structure. In this tutorial, we will learn briefly
  how BFS works and explore a basic pattern that can be used to solve ...'
---

Par Anamika Ahmed

La recherche en largeur (BFS) est l'un des algorithmes les plus populaires pour rechercher ou parcourir une structure de données de type arbre ou graphe. Dans ce tutoriel, nous allons apprendre brièvement comment fonctionne le BFS et explorer un modèle de base qui peut être utilisé pour résoudre certains problèmes de niveau moyen et facile sur Leetcode.

Commençons, d'accord ?

## Qu'est-ce que la Recherche en Largeur ?

Nous savons tous qu'un graphe est un ensemble de sommets et d'arêtes : G={V,E}. Parcourir un graphe signifie visiter chaque sommet et chaque arête *exactement une fois* de manière ordonnée.

Dans le BFS, nous devons parcourir le graphe en largeur ou niveau par niveau. Cela signifie que nous devons d'abord nous déplacer horizontalement et visiter tous les nœuds de la couche actuelle avant de passer à la couche suivante.

Par conséquent, chaque fois que nous devons effectuer un **parcours par niveau**, nous pouvons utiliser la technique BFS.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-154.png)

Dans le BFS, nous commencerions le parcours à partir de 1 (le nœud racine) et visiterions ses nœuds enfants 8, 5 et 2. Nous les stockerions dans l'ordre dans lequel ils ont été visités. Cela nous permettrait de visiter les nœuds enfants de 8 en premier (c'est-à-dire 6, 4 et 3), puis ceux de 5 (c'est-à-dire null), puis ceux de 2 (c'est-à-dire 9) et ainsi de suite.

## Implémentation

Pour implémenter le BFS, une structure de données de type **file d'attente** est utilisée. La file d'attente stocke le nœud et le marque comme 'visité' jusqu'à ce que tous ses sommets adjacents soient marqués.

La file d'attente suit la méthode Premier Entré Premier Sorti (FIFO). Cela signifie que les voisins du nœud seront visités dans l'ordre dans lequel ils ont été insérés.

**Formule magique du BFS :**

1. Ajouter un nœud à la file d'attente
2. Retirer le nœud
3. Récupérer les voisins non visités du nœud retiré, les ajouter à la file d'attente
4. Répéter les étapes 1, 2 et 3 tant que la file d'attente n'est pas vide.

Maintenant, regardons quelques problèmes Leetcode et appliquons ce que nous avons appris.

### [102. Parcours en Largeur d'un Arbre Binaire (Difficulté : Moyenne)](https://leetcode.com/problems/binary-tree-level-order-traversal/)

La question nous demande de parcourir le graphe et d'imprimer les nœuds à chaque niveau dans une liste chaînée. Pour résoudre celui-ci, tout ce que nous avons à faire est d'appliquer notre formule magique !

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-157.png)

Assurez-vous de bien comprendre le code, car c'est le **modèle de base** que nous utiliserons pour résoudre plusieurs problèmes. Alors, passons-le en revue.

Dans le code ci-dessus, nous avons d'abord inséré le nœud racine dans la file d'attente. Tant que la file d'attente n'est pas vide, nous avons retiré ce nœud de la file d'attente et inséré ses enfants gauche et droit dans la file d'attente.

Mais avant cela, nous avons vérifié si chacun de ses enfants est null ou non. Si null, nous aurions obtenu une Null Pointer Exception.

Le processus est répété avec les prochains éléments qui restent dans la file d'attente. La **boucle for** est maintenue pour nous donner la liste des nœuds à chaque niveau dans des listes chaînées séparées.

### [637. Moyenne des Niveaux dans un Arbre Binaire (Difficulté : Facile)](https://leetcode.com/problems/average-of-levels-in-binary-tree/)

Cette question nous demande de trouver la valeur moyenne des nœuds à chaque niveau d'un arbre binaire dans un tableau. Cela suit la même procédure que notre problème précédent avec une petite modification.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-159.png)

Comme vous pouvez le voir, tout ce que nous avons fait est de copier et coller le code du modèle. Ensuite, nous avons simplement placé une variable de somme dans la boucle for qui peut nous donner la somme des valeurs des nœuds à chaque niveau. C'est ce que nous utiliserons pour calculer la moyenne souhaitée.

### [429. Parcours en Largeur d'un Arbre N-aire (Difficulté : Moyenne)](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

Un arbre dans lequel chaque nœud a **au plus** N enfants est appelé un arbre N-aire.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-173.png)

Cela suit exactement la même procédure que le parcours d'un arbre binaire, sauf que dans ce cas, nous insérons tous les enfants d'un nœud dans la file d'attente. Rappelez-vous que lors de la résolution de problèmes liés à un arbre binaire, nous n'avons inséré que les enfants gauche et droit de tout nœud donné dans la file d'attente.

C'est tout ! J'espère que cela vous a aidé à mieux comprendre le BFS et que vous avez apprécié le tutoriel. Veuillez recommander cet article si vous pensez qu'il peut être utile pour quelqu'un d'autre !