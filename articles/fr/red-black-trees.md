---
title: 'Arbre Rouge-Noir : Arbres Binaires de Recherche Auto-Équilibrés Expliqués
  avec des Exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-01T18:40:00.000Z'
originalURL: https://freecodecamp.org/news/red-black-trees
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/red-black-tree.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: Computer Science
  slug: computer-science
seo_title: 'Arbre Rouge-Noir : Arbres Binaires de Recherche Auto-Équilibrés Expliqués
  avec des Exemples'
seo_desc: 'What is a Red-Black Tree?

  Red-Black Tree is a type of self-balancing Binary Search Tree (BST). In a Red-Black
  Tree, every node follows these rules:


  Every node has two children, colored either red or black.

  Every tree leaf node is always black.

  Every...'
---

## Qu'est-ce qu'un Arbre Rouge-Noir ?

Un Arbre Rouge-Noir est un type d'Arbre Binaire de Recherche (ABR) auto-équilibré. Dans un Arbre Rouge-Noir, chaque nœud suit ces règles :

1. Chaque nœud a deux enfants, colorés soit en rouge soit en noir.
2. Chaque nœud feuille de l'arbre est toujours noir.
3. Chaque nœud rouge a ses deux enfants colorés en noir.
4. Il n'y a pas deux nœuds rouges adjacents (Un nœud rouge ne peut pas avoir un parent rouge ou un enfant rouge).
5. Chaque chemin de la racine à un nœud feuille de l'arbre a le même nombre de nœuds noirs (appelé "hauteur noire").

![Image](https://www.freecodecamp.org/news/content/images/2020/04/2000px-Fibonacci_Tree_as_Red-Black_Tree.svg.png)

### Insertion dans les Arbres Rouge-Noir

Un nœud est initialement inséré dans un Arbre Rouge-Noir comme dans n'importe quel Arbre Binaire de Recherche. Le nouveau nœud est alors coloré en rouge. Après que le nœud a été inséré, l'arbre doit être validé pour s'assurer qu'aucune des cinq propriétés n'a été violée. Si une propriété a été violée, il y a trois cas potentiels nécessitant soit une rotation à gauche, une rotation à droite, et/ou un recoloriage des nœuds. Les cas dépendent de l'"oncle" du nœud actuel. Plus précisément, si le nœud "oncle" est noir ou rouge. Pour plus d'informations sur l'insertion, les trois cas peuvent être trouvés [ici](https://www.geeksforgeeks.org/red-black-tree-set-2-insert/).

### Arbre Rouge-Noir à Gauche

Un arbre rouge-noir à gauche (LLRB) est un type d'arbre binaire de recherche auto-équilibré. Il s'agit d'une variante de l'arbre rouge-noir et garantit la même complexité asymptotique pour les opérations, mais est conçu pour être plus facile à implémenter.

### Propriétés des Arbres Rouge-Noir à Gauche

Tous les algorithmes d'arbres rouge-noir qui ont été proposés sont caractérisés par un temps de recherche dans le pire des cas limité par un petit multiple constant de log N dans un arbre de N clés, et le comportement observé en pratique est typiquement ce même multiple plus rapide que la limite du pire des cas, proche des nœuds log N optimaux examinés qui seraient observés dans un arbre parfaitement équilibré.

Plus précisément, dans un arbre rouge-noir 2-3 à gauche construit à partir de N clés aléatoires : -> Une recherche réussie aléatoire examine `log2 N` − 0,5 nœuds. -> La hauteur moyenne de l'arbre est d'environ `2 log2 N`