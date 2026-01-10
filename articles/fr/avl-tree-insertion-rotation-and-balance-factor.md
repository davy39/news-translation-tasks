---
title: Insertion, Rotation et Facteur d'Équilibre des Arbres AVL Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-23T23:20:00.000Z'
originalURL: https://freecodecamp.org/news/avl-tree-insertion-rotation-and-balance-factor
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f18740569d1a4ca40ca.jpg
tags:
- name: binary search
  slug: binary-search
seo_title: Insertion, Rotation et Facteur d'Équilibre des Arbres AVL Expliqués
seo_desc: 'What is an AVL Tree?

  An AVL tree is a type of binary search tree. Named after it''s inventors Adelson,
  Velskii, and Landis, AVL trees have the property of dynamic self-balancing in addition
  to all the other properties exhibited by binary search trees....'
---

## Qu'est-ce qu'un Arbre AVL ?

Un arbre AVL est un type d'arbre binaire de recherche. Nommé d'après ses inventeurs Adelson, Velskii et Landis, les arbres AVL ont la propriété d'auto-équilibrage dynamique en plus de toutes les autres propriétés des arbres binaires de recherche.

Un BST (Binary Search Tree) est une structure de données composée de nœuds. Il a les garanties suivantes :

1. Chaque arbre a un nœud racine (en haut)
2. Le nœud racine a zéro, un ou deux nœuds enfants
3. Chaque nœud enfant a zéro, un ou deux nœuds enfants
4. Chaque nœud a jusqu'à deux enfants
5. Pour chaque nœud, ses descendants gauches sont inférieurs au nœud actuel, qui est inférieur aux descendants droits

Les arbres AVL ont une garantie supplémentaire :

1. La différence entre la profondeur des sous-arbres droit et gauche ne peut pas être supérieure à un. Cette différence est appelée le facteur d'équilibre.

Afin de maintenir cette garantie, une implémentation d'un AVL inclura un algorithme pour rééquilibrer l'arbre lorsqu'un élément supplémentaire serait ajouté et perturberait cette garantie.

Les arbres AVL ont un temps de recherche, d'insertion et de suppression dans le pire des cas de `O(log n)`, où `n` est le nombre de nœuds dans l'arbre. La complexité spatiale dans le pire des cas est `O(n)`.

### Processus d'Insertion dans un Arbre AVL

L'insertion dans un arbre AVL est similaire à l'insertion dans un arbre binaire de recherche. Mais après avoir inséré un élément, vous devez corriger les propriétés AVL en utilisant des rotations gauche ou droite :

* S'il y a un déséquilibre dans le sous-arbre droit de l'enfant gauche, effectuez une rotation gauche-droite
* S'il y a un déséquilibre dans le sous-arbre gauche de l'enfant gauche, effectuez une rotation droite
* S'il y a un déséquilibre dans le sous-arbre droit de l'enfant droit, effectuez une rotation gauche
* S'il y a un déséquilibre dans le sous-arbre gauche de l'enfant droit, effectuez une rotation droite-gauche

%[https://www.youtube.com/watch?v=7m94k2Qhg68]

## Rotations des Arbres AVL

Dans les arbres AVL, après chaque opération comme l'insertion et la suppression, le facteur d'équilibre de chaque nœud doit être vérifié. Si chaque nœud satisfait la condition du facteur d'équilibre, alors l'opération peut être conclue. Sinon, l'arbre doit être rééquilibré en utilisant des opérations de rotation.

Il existe quatre rotations et elles sont classées en deux types :

### Rotation Gauche (Rotation LL)

Dans les rotations gauches, chaque nœud se déplace d'une position vers la gauche à partir de la position actuelle.

![Rotation Gauche de l'Arbre AVL](https://raw.githubusercontent.com/HebleV/valet_parking/master/images/avl_left_rotation.jpg)

### Rotation Droite (Rotation RR)

Dans les rotations droites, chaque nœud se déplace d'une position vers la droite à partir de la position actuelle.

![Rotation Droite de l'Arbre AVL](https://raw.githubusercontent.com/HebleV/valet_parking/master/images/avl_right_rotation.jpg)

### Rotation Gauche-Droite (Rotation LR)

Les rotations gauche-droite sont une combinaison d'une rotation gauche unique suivie d'une rotation droite unique.

D'abord, chaque nœud se déplace d'une position vers la gauche, puis d'une position vers la droite à partir de la position actuelle.

### Rotation Droite-Gauche (Rotation RL)

Les rotations droite-gauche sont une combinaison d'une rotation droite unique suivie d'une rotation gauche unique.

D'abord, chaque nœud se déplace d'une position vers la droite, puis d'une position vers la gauche à partir de la position actuelle.

## Application des Arbres AVL

Les arbres AVL sont bénéfiques dans des cas comme une base de données où les insertions et suppressions ne sont pas très fréquentes, mais où vous vérifiez fréquemment les entrées.