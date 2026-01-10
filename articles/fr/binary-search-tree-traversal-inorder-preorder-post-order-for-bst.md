---
title: Parcours d'un arbre binaire de recherche – Inorder, Preorder, Post Order pour
  BST
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-26T20:01:40.000Z'
originalURL: https://freecodecamp.org/news/binary-search-tree-traversal-inorder-preorder-post-order-for-bst
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/binary-search-tree-traversal.png
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
seo_title: Parcours d'un arbre binaire de recherche – Inorder, Preorder, Post Order
  pour BST
seo_desc: "In this tutorial, you will learn what a binary search tree is, what parts\
  \ make up a tree, and some of the common terms we use when describing parts of a\
  \ tree. \nWe will also see how to traverse a tree using some of the common algorithms\
  \ – all illustra..."
---

Dans ce tutoriel, vous apprendrez ce qu'est un arbre binaire de recherche, quelles parties composent un arbre, et certains des termes courants que nous utilisons pour décrire les parties d'un arbre. 

Nous verrons également comment parcourir un arbre en utilisant certains des algorithmes courants – tous illustrés avec des exemples clairs.

## Qu'est-ce qu'un arbre binaire de recherche ?

Un arbre binaire de recherche est un arbre binaire composé de nœuds. Chaque nœud a une clé signifiant sa valeur. 

La valeur des nœuds dans le sous-arbre gauche est inférieure à la valeur du nœud racine. Et la valeur des nœuds dans le sous-arbre droit est supérieure à la valeur du nœud racine. 

Le nœud racine est le nœud parent des deux sous-arbres.

Le diagramme ci-dessous montre les principales parties d'un arbre binaire :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/binary-tree.png)
_Diagramme d'un arbre binaire de recherche_

Examinons la relation entre les nœuds. 

* `**A**` est le nœud racine. 
* Le sous-arbre gauche commence à **`B`** tandis que le sous-arbre droit commence à **`C`**.
* Le nœud **`A`** a deux nœuds enfants – **`B`** et **`C`**.
* Le nœud **`C`** est le nœud parent de **`F`** et **`G`**. **`F`** et **`G`** sont frères.
* Les nœuds **`F`** et **`G`** sont appelés nœuds **feuilles** car ils n'ont pas d'enfants.
* Le nœud **`B`** est le nœud parent de **`D`** et **`E`**.
* Le nœud **`D`** est le nœud parent de **`H`** et **`I`**.
* **`D`** et **`E`** sont frères ainsi que **`H`** et **`I`**.
* Le nœud **`E`** est un nœud feuille.

Voici donc quelques termes importants que nous venons d'utiliser pour décrire l'arbre ci-dessus :

**Racine :** Le nœud le plus haut dans l'arbre.

**Parent :** Un nœud avec un ou des enfants.

**Enfant :** Un nœud étendu à partir d'un autre nœud (nœud parent).

**Feuille :** Un nœud sans enfant.

## À quoi sert un arbre binaire de recherche ?

Les arbres binaires de recherche nous aident à accélérer notre recherche binaire car nous sommes capables de trouver des éléments plus rapidement. 

Nous pouvons utiliser l'arbre binaire de recherche pour l'ajout et la suppression d'éléments dans un arbre. 

Nous pouvons également représenter des données dans un ordre classé en utilisant un arbre binaire. Et dans certains cas, il peut être utilisé comme un graphique pour représenter une collection d'informations.

Ensuite, nous examinerons certaines techniques utilisées pour parcourir un arbre binaire.

## Qu'est-ce que le parcours d'arbre ?

Parcourir un arbre signifie visiter et sortir la valeur de chaque nœud dans un ordre particulier. Dans ce tutoriel, nous utiliserons les méthodes de parcours d'arbre Inorder, Preorder et Post order.

L'importance majeure du parcours d'arbre est qu'il existe plusieurs façons de réaliser des opérations de parcours contrairement aux structures de données linéaires comme les tableaux, les bitmaps, les matrices où le parcours est fait dans un ordre linéaire.

Chacune de ces méthodes de parcours d'un arbre suit un ordre particulier :

* Pour **Inorder**, vous parcourez depuis le sous-arbre **gauche** vers la **racine** puis vers le sous-arbre **droit**.
* Pour **Preorder**, vous parcourez depuis la **racine** vers le sous-arbre **gauche** puis vers le sous-arbre **droit**.
* Pour **Post order**, vous parcourez depuis le sous-arbre **gauche** vers le sous-arbre **droit** puis vers la **racine**.

Voici une autre façon de représenter les informations ci-dessus :

Inorder => Gauche, Racine, Droit.

Preorder => Racine, Gauche, Droit.

Post order => Gauche, Droit, Racine.

### Comment parcourir un arbre en utilisant le parcours Inorder

Nous allons créer un arbre similaire à celui de la dernière section, mais cette fois les clés des nœuds seront des nombres au lieu de lettres. 

Rappelez-vous que les valeurs des nœuds dans le sous-arbre gauche sont toujours inférieures à la valeur du nœud racine. De plus, les valeurs des nœuds dans le sous-arbre droit sont supérieures à la valeur du nœud racine. 

Voici le diagramme avec lequel nous allons travailler :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ex-binary-search-tree.png)

Rappelez-vous que l'ordre pour le parcours inorder est Gauche, Racine, Droit.

Voici le résultat que nous obtenons après avoir utilisé le parcours inorder :

**D, B, E, A, F, C, G**

Si cela semble un peu complexe pour vous, suivez l'ordre des couleurs dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ex-inorder-traversal.png)
_Parcours Inorder_

### Comment parcourir un arbre en utilisant le parcours Preorder

L'ordre ici est Racine, Gauche, Droit.

En utilisant le même diagramme ci-dessus, nous avons :

**A, B, D, E, C, F, G**

Voici le même diagramme avec différentes couleurs utilisées comme guide :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ex-preorder-traversal.png)
_Parcours Preorder_

### Comment parcourir un arbre en utilisant le parcours Postorder

L'ordre pour le parcours post order est Gauche, Droit, Racine.

Voici le résultat :

**D, E, B, F, G, C, A**

Si vous ne comprenez pas comment nous sommes arrivés à ce résultat, utilisez les couleurs dans l'image ci-dessous comme guide :

![Image](https://www.freecodecamp.org/news/content/images/2022/02/ex-post-order-traversal.png)
_Parcours Postorder_

## Conclusion

Dans ce tutoriel, nous avons appris les bases de ce qu'est un arbre binaire de recherche, quelles sont les différentes parties d'un arbre binaire, et les termes courants associés à un arbre. Nous avons également vu certains des algorithmes que nous pouvons utiliser pour parcourir un arbre.

Merci d'avoir lu !