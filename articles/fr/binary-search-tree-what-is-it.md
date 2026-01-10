---
title: Structure de données de l'arbre de recherche binaire expliquée avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-22T22:29:00.000Z'
originalURL: https://freecodecamp.org/news/binary-search-tree-what-is-it
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e86740569d1a4ca3d95.jpg
tags:
- name: binary search
  slug: binary-search
- name: data structures
  slug: data-structures
seo_title: Structure de données de l'arbre de recherche binaire expliquée avec des
  exemples
seo_desc: 'A tree is a data structure composed of nodes that has the following characteristics:


  Each tree has a root node (at the top) having some value.

  The root node has zero or more child nodes.

  Each child node has zero or more child nodes, and so on. This ...'
---

Un arbre est une structure de données composée de nœuds qui a les caractéristiques suivantes :

1. Chaque arbre a un nœud racine (en haut) ayant une certaine valeur.
2. Le nœud racine a zéro ou plusieurs nœuds enfants.
3. Chaque nœud enfant a zéro ou plusieurs nœuds enfants, et ainsi de suite. Cela crée un sous-arbre dans l'arbre. Chaque nœud a son propre sous-arbre composé de ses enfants et de leurs enfants, etc. Cela signifie que chaque nœud peut être un arbre à part entière.

Un arbre de recherche binaire (BST) ajoute ces deux caractéristiques :

1. Chaque nœud a un maximum de deux enfants.
2. Pour chaque nœud, les valeurs de ses nœuds descendants gauches sont inférieures à celle du nœud actuel, qui à son tour est inférieure aux nœuds descendants droits (le cas échéant).

Le BST est construit sur l'idée de l'algorithme de [recherche binaire](https://guide.freecodecamp.org/algorithms/search-algorithms/binary-search), qui permet une recherche, une insertion et une suppression rapides des nœuds. La manière dont ils sont configurés signifie que, en moyenne, chaque comparaison permet aux opérations de sauter environ la moitié de l'arbre, de sorte que chaque recherche, insertion ou suppression prend un temps proportionnel au logarithme du nombre d'éléments stockés dans l'arbre, `O(log n)`.

Cependant, parfois le pire des cas peut se produire, lorsque l'arbre n'est pas équilibré et que la complexité temporelle est `O(n)` pour ces trois fonctions. C'est pourquoi les arbres auto-équilibrants (AVL, rouge-noir, etc.) sont beaucoup plus efficaces que le BST de base.

**Exemple de scénario du pire cas :** Cela peut se produire lorsque vous continuez à ajouter des nœuds qui sont _toujours_ plus grands que le nœud précédent (son parent), la même chose peut se produire lorsque vous ajoutez toujours des nœuds avec des valeurs inférieures à celles de leurs parents.

## **Opérations de base sur un BST**

* Créer : crée un arbre vide.
* Insérer : insère un nœud dans l'arbre.
* Rechercher : recherche un nœud dans l'arbre.
* Supprimer : supprime un nœud de l'arbre.

### Créer

Initialement, un arbre vide sans aucun nœud est créé. La variable/identifiant qui doit pointer vers le nœud racine est initialisée avec une valeur `NULL`.

### Rechercher

Vous commencez toujours à rechercher dans l'arbre au niveau du nœud racine et vous descendez à partir de là. Vous comparez les données de chaque nœud avec celles que vous recherchez. Si le nœud comparé ne correspond pas, vous passez soit au nœud enfant droit, soit au nœud enfant gauche, selon le résultat de la comparaison suivante : Si le nœud que vous recherchez est inférieur à celui avec lequel vous le compariez, vous passez à l'enfant gauche, sinon (s'il est plus grand) vous allez à l'enfant droit. Pourquoi ? Parce que le BST est structuré (selon sa définition), que l'enfant droit est toujours plus grand que le parent et l'enfant gauche est toujours plus petit.

### Insérer

C'est très similaire à la fonction de recherche. Vous commencez à nouveau à la racine de l'arbre et vous descendez de manière récursive, à la recherche du bon endroit pour insérer notre nouveau nœud, de la même manière que celle expliquée dans la fonction de recherche. Si un nœud avec la même valeur est déjà dans l'arbre, vous pouvez choisir d'insérer le duplicata ou non. Certains arbres permettent les duplicatas, d'autres non. Cela dépend de l'implémentation spécifique.

### Supprimer

Il y a 3 cas qui peuvent se produire lorsque vous essayez de supprimer un nœud. S'il a,

1. Aucun sous-arbre (aucun enfant) : Celui-ci est le plus facile. Vous pouvez simplement supprimer le nœud, sans aucune action supplémentaire requise.
2. Un sous-arbre (un enfant) : Vous devez vous assurer que, après la suppression du nœud, son enfant est ensuite connecté au parent du nœud supprimé.
3. Deux sous-arbres (deux enfants) : Vous devez trouver et remplacer le nœud que vous souhaitez supprimer par son successeur (le nœud le plus à gauche dans le sous-arbre droit).

La complexité temporelle pour créer un arbre est `O(1)`. La complexité temporelle pour rechercher, insérer ou supprimer un nœud dépend de la hauteur de l'arbre `h`, donc le pire cas est `O(h)`.

### Prédécesseur d'un nœud

Les prédécesseurs peuvent être décrits comme le nœud qui viendrait juste avant le nœud où vous vous trouvez actuellement. Pour trouver le prédécesseur du nœud actuel, regardez le nœud feuille le plus à droite/le plus grand dans le sous-arbre gauche.

### Successeur d'un nœud

Les successeurs peuvent être décrits comme le nœud qui viendrait juste après le nœud où vous vous trouvez actuellement. Pour trouver le successeur du nœud actuel, regardez le nœud feuille le plus à gauche/le plus petit dans le sous-arbre droit.

## **Types spéciaux de BT**

* Tas
* Arbre rouge-noir
* Arbre B
* Arbre Splay
* Arbre N-aire
* Trie (Arbre Radix)

## Runtime

### **Structure de données : Tableau**

* Performance dans le pire des cas : `O(log n)`
* Performance dans le meilleur des cas : `O(1)`
* Performance moyenne : `O(log n)`
* Complexité spatiale dans le pire des cas : `O(1)`

Où `n` est le nombre de nœuds dans le BST.

## Implémentation de BST

Voici une définition pour un nœud BST ayant certaines données, référençant ses nœuds enfants gauche et droit.

```c
struct node {
   int data;
   struct node *leftChild;
   struct node *rightChild;
};
```

### Opération de recherche

Lorsque vous devez rechercher un élément, commencez la recherche à partir du nœud racine. Ensuite, si les données sont inférieures à la valeur de la clé, recherchez l'élément dans le sous-arbre gauche. Sinon, recherchez l'élément dans le sous-arbre droit. Suivez le même algorithme pour chaque nœud.

```c
struct node* search(int data){
   struct node *current = root;
   printf("Visiting elements: ");
	
   while(current->data != data){
	
      if(current != NULL) {
         printf("%d ",current->data);
			
         //aller à l'arbre gauche
         if(current->data > data){
            current = current->leftChild;
         }//sinon aller à l'arbre droit
         else {                
            current = current->rightChild;
         }
			
         //non trouvé
         if(current == NULL){
            return NULL;
         }
      }			
   }
   return current;
}
```

### Opération d'insertion

Lorsque vous devez insérer un élément, localisez d'abord son emplacement approprié. Commencez la recherche à partir du nœud racine, puis si les données sont inférieures à la valeur de la clé, recherchez l'emplacement vide dans le sous-arbre gauche et insérez les données. Sinon, recherchez l'emplacement vide dans le sous-arbre droit et insérez les données.

```c
void insert(int data) {
   struct node *tempNode = (struct node*) malloc(sizeof(struct node));
   struct node *current;
   struct node *parent;

   tempNode->data = data;
   tempNode->leftChild = NULL;
   tempNode->rightChild = NULL;

   //si l'arbre est vide
   if(root == NULL) {
      root = tempNode;
   } else {
      current = root;
      parent = NULL;

      while(1) {                
         parent = current;
			
         //aller à gauche de l'arbre
         if(data < parent->data) {
            current = current->leftChild;                
            //insérer à gauche
				
            if(current == NULL) {
               parent->leftChild = tempNode;
               return;
            }
         }//aller à droite de l'arbre
         else {
            current = current->rightChild;
            
            //insérer à droite
            if(current == NULL) {
               parent->rightChild = tempNode;
               return;
            }
         }
      }            
   }
}        
```

Les arbres de recherche binaire (BST) nous donnent également un accès rapide aux prédécesseurs et successeurs. Les prédécesseurs peuvent être décrits comme le nœud qui viendrait juste avant le nœud où vous vous trouvez actuellement.

* Pour trouver le prédécesseur du nœud actuel, regardez le nœud feuille le plus à droite/le plus grand dans le sous-arbre gauche. Les successeurs peuvent être décrits comme le nœud qui viendrait juste après le nœud où vous vous trouvez actuellement.
* Pour trouver le successeur du nœud actuel, regardez le nœud feuille le plus à gauche/le plus petit dans le sous-arbre droit.

## Examinons quelques procédures opérant sur les arbres.

Puisque les arbres sont définis de manière récursive, il est très courant d'écrire des routines qui opèrent sur les arbres et qui sont elles-mêmes récursives.

Ainsi, par exemple, si nous voulons calculer la hauteur d'un arbre, c'est-à-dire la hauteur d'un nœud racine, nous pouvons procéder de manière récursive, en parcourant l'arbre. Nous pouvons donc dire :

* Par exemple, si nous avons un arbre nil, alors sa hauteur est de 0.
* Sinon, nous sommes à 1 plus le maximum de l'arbre enfant gauche et de l'arbre enfant droit.

Ainsi, si nous regardons une feuille par exemple, cette hauteur serait de 1 car la hauteur de l'enfant gauche est nil, est 0, et la hauteur de l'enfant droit nil est également 0. Donc le max de cela est 0, puis 1 plus 0.

### Algorithme Height(tree)

```text
if tree = nil:
return 0
return 1 + Max(Height(tree.left),Height(tree.right))
```

### Voici le code en C++

```text
int maxDepth(struct node* node)
{
    if (node==NULL)
        return 0;
   else
   {
       int rDepth = maxDepth(node->right);
       int lDepth = maxDepth(node->left);

       if (lDepth > rDepth)
       {
           return(lDepth+1);
       }
       else
       {
            return(rDepth+1);
       }
   }
}  
```

Nous pourrions également examiner le calcul de la taille d'un arbre, c'est-à-dire le nombre de nœuds.

* Encore une fois, si nous avons un arbre nil, nous avons zéro nœud.

Sinon, nous avons le nombre de nœuds dans l'enfant gauche plus 1 pour nous-mêmes plus le nombre de nœuds dans l'enfant droit. Donc 1 plus la taille de l'arbre gauche plus la taille de l'arbre droit.

### Algorithme Size(tree)

```text
if tree = nil
return 0
return 1 + Size(tree.left) + Size(tree.right)
```

### Voici le code en C++

```text
int treeSize(struct node* node)
{
    if (node==NULL)
        return 0;
    else
        return 1+(treeSize(node->left) + treeSize(node->right));
}
```

### **Vidéos pertinentes sur la chaîne YouTube freeCodeCamp**

* [Binary Search Tree](https://youtu.be/5cU1ILGy6dM)
* [Binary Search Tree: Traversal and Height](https://youtu.be/Aagf3RyK3Lw)

## Voici les types courants d'arbres binaires :

Arbre binaire complet/Arbre binaire strict : Un arbre binaire est complet ou strict si chaque nœud a exactement 0 ou 2 enfants.

```text
           18
       /       \  
     15         30  
    /  \        /  \
  40    50    100   40
```

Dans un arbre binaire complet, le nombre de nœuds feuilles est égal au nombre de nœuds internes plus un.

Arbre binaire complet : Un arbre binaire est un arbre binaire complet si tous les niveaux sont complètement remplis, sauf éventuellement le dernier niveau, et le dernier niveau a toutes les clés aussi à gauche que possible.

```text
           18
       /       \  
     15         30  
    /  \        /  \
  40    50    100   40
 /  \   /
8   7  9 
```