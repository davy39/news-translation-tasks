---
title: Structures de données d'index de recherche auto-équilibrées B-Tree expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-24T18:26:00.000Z'
originalURL: https://freecodecamp.org/news/b-tree-self-balancing-search-index-data-structures-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f13740569d1a4ca40b1.jpg
tags:
- name: data analytics
  slug: data-analytics
- name: Trees
  slug: trees
seo_title: Structures de données d'index de recherche auto-équilibrées B-Tree expliquées
seo_desc: "What is a B-Tree?\nB-Tree is a self-balancing search tree. \nIn most of\
  \ the other self-balancing search trees (like AVL and Red Black Trees), it is assumed\
  \ that everything is in main memory. \nTo understand use of B-Trees, we must think\
  \ of huge amount o..."
---

## Qu'est-ce qu'un B-Tree ?

B-Tree est un arbre de recherche auto-équilibré. 

Dans la plupart des autres arbres de recherche auto-équilibrés (comme AVL et les arbres Rouge Noir), on suppose que tout est en mémoire principale. 

Pour comprendre l'utilisation des B-Trees, nous devons penser à une énorme quantité de données qui ne peut pas tenir en mémoire principale. Lorsque le nombre de clés est élevé, les données sont lues depuis le disque sous forme de blocs. Le temps d'accès au disque est très élevé par rapport au temps d'accès à la mémoire principale. 

L'idée principale de l'utilisation des B-Trees est de réduire le nombre d'accès au disque. La plupart des opérations sur l'arbre (recherche, insertion, suppression, max, min, etc) nécessitent O(h) accès au disque où h est la hauteur de l'arbre. B-tree est un arbre large. 

La hauteur des B-Trees est maintenue basse en plaçant un maximum de clés possibles dans un nœud de B-Tree. Généralement, la taille d'un nœud de B-Tree est maintenue égale à la taille du bloc de disque. Puisque h est bas pour B-Tree, le nombre total d'accès au disque pour la plupart des opérations est considérablement réduit par rapport aux arbres binaires de recherche équilibrés comme AVL Tree, Red Black Tree, etc.

Propriétés de B-Tree :

1. Tous les nœuds feuilles sont au même niveau.
2. Un B-Tree est défini par le terme degré minimum 't'. La valeur de t dépend de la taille du bloc de disque.
3. Chaque nœud sauf la racine doit contenir au moins t-1 clés. La racine peut contenir un minimum de 1 clé.
4. Tous les nœuds (y compris la racine) peuvent contenir au plus 2t - 1 clés.
5. Le nombre d'enfants d'un nœud est égal au nombre de clés qu'il contient plus 1.
6. Toutes les clés d'un nœud sont triées par ordre croissant. L'enfant entre deux clés k1 et k2 contient toutes les clés dans la plage de k1 à k2.
7. Le B-Tree grandit et rétrécit à partir de la racine, ce qui est différent de l'arbre binaire de recherche. Les arbres binaires de recherche grandissent vers le bas et rétrécissent également vers le bas.
8. Comme les autres arbres binaires de recherche équilibrés, la complexité temporelle pour rechercher, insérer et supprimer est O(Log(n)).

### Recherche :

La recherche est similaire à la recherche dans un arbre binaire de recherche. Soit k la clé à rechercher. Nous commençons par la racine et parcourons récursivement vers le bas. Pour chaque nœud non-feuille visité, si le nœud contient la clé, nous retournons simplement le nœud. Sinon, nous récursons vers l'enfant approprié (l'enfant qui est juste avant la première clé plus grande) du nœud. Si nous atteignons un nœud feuille et ne trouvons pas k dans le nœud feuille, nous retournons NULL.

### Parcours :

Le parcours est également similaire au parcours Inorder d'un arbre binaire. Nous commençons par l'enfant le plus à gauche, imprimons récursivement l'enfant le plus à gauche, puis répétons le même processus pour les enfants et les clés restants. Enfin, nous imprimons récursivement l'enfant le plus à droite.

### Insertion

Tout d'abord, nous recherchons et déterminons à quel nœud la clé doit appartenir et nous l'y insérons. Ensuite, nous cherchons et corrigeons ces problèmes : Si le nombre de clés est trop élevé (supérieur à t - 1), nous déplaçons la clé du milieu vers le parent du nœud. Nous faisons cela récursivement jusqu'à la racine. Si le nombre de clés dans la racine est trop élevé, alors nous faisons de la clé du milieu la nouvelle racine de l'arbre entier et la connectons au nœud où elle se trouvait auparavant.

### Analyse temporelle pour B-Tree :

Supposons qu'un B-tree ait n éléments et que M soit le nombre maximum d'enfants qu'un nœud peut avoir. Quelle est la profondeur maximale que l'arbre pourrait avoir ? Quelle est la profondeur minimale que l'arbre pourrait avoir ?

* La profondeur dans le pire cas (profondeur maximale) d'un B-tree est : logM/2 n.
* La profondeur dans le meilleur cas (profondeur minimale) d'un B-tree est : logM n.