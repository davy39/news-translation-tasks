---
title: 'Arbres de Recherche Binaire : BST Expliqué avec des Exemples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-16T17:58:00.000Z'
originalURL: https://freecodecamp.org/news/binary-search-trees-bst-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f48740569d1a4ca41c4.jpg
tags:
- name: binary search
  slug: binary-search
- name: data structures
  slug: data-structures
- name: Trees
  slug: trees
seo_title: 'Arbres de Recherche Binaire : BST Expliqué avec des Exemples'
seo_desc: 'What is a Binary Search Tree?

  A tree is a data structure composed of nodes that has the following characteristics:


  Each tree has a root node at the top (also known as Parent Node) containing some
  value (can be any datatype).

  The root node has zero o...'
---

## Qu'est-ce qu'un Arbre de Recherche Binaire ?

Un arbre est une structure de données composée de nœuds qui a les caractéristiques suivantes :

1. Chaque arbre a un nœud racine en haut (également connu sous le nom de Nœud Parent) contenant une certaine valeur (peut être de n'importe quel type de données).
2. Le nœud racine a zéro ou plusieurs nœuds enfants.
3. Chaque nœud enfant a zéro ou plusieurs nœuds enfants, et ainsi de suite. Cela crée un sous-arbre dans l'arbre. Chaque nœud a son propre sous-arbre composé de ses enfants et de leurs enfants, etc. Cela signifie que chaque nœud peut être un arbre à lui seul.

Un arbre de recherche binaire (BST) ajoute ces deux caractéristiques :

1. Chaque nœud a un maximum de deux enfants.
2. Pour chaque nœud, les valeurs de ses nœuds descendants gauches sont inférieures à celle du nœud actuel, qui à son tour est inférieure aux nœuds descendants droits (le cas échéant).

Le BST est construit sur l'idée de l'algorithme de [recherche binaire](https://guide.freecodecamp.org/algorithms/search-algorithms/binary-search), qui permet une recherche, une insertion et une suppression rapides des nœuds. La manière dont ils sont configurés signifie que, en moyenne, chaque comparaison permet aux opérations de sauter environ la moitié de l'arbre, de sorte que chaque recherche, insertion ou suppression prend un temps proportionnel au logarithme du nombre d'éléments stockés dans l'arbre, `O(log n)`. Cependant, parfois le pire cas peut se produire, lorsque l'arbre n'est pas équilibré et la complexité temporelle est `O(n)` pour ces trois fonctions. C'est pourquoi les arbres auto-équilibrants (AVL, rouge-noir, etc.) sont beaucoup plus efficaces que le BST de base.

**Exemple de scénario du pire cas :** Cela peut se produire lorsque vous continuez à ajouter des nœuds qui sont _toujours_ plus grands que le nœud précédent (son parent), la même chose peut se produire lorsque vous ajoutez toujours des nœuds avec des valeurs inférieures à celles de leurs parents.

### Opérations de base sur un BST

* Créer : crée un arbre vide.
* Insérer : insère un nœud dans l'arbre.
* Rechercher : recherche un nœud dans l'arbre.
* Supprimer : supprime un nœud de l'arbre.
* Inorder : parcours en ordre de l'arbre.
* Preorder : parcours en préordre de l'arbre.
* Postorder : parcours en postordre de l'arbre.

#### Créer

Initialement, un arbre vide sans aucun nœud est créé. La variable/identifiant qui doit pointer vers le nœud racine est initialisée avec une valeur `NULL`.

#### Rechercher

Vous commencez toujours à rechercher dans l'arbre au niveau du nœud racine et descendez à partir de là. Vous comparez les données de chaque nœud avec celles que vous recherchez. Si le nœud comparé ne correspond pas, vous passez soit au nœud enfant droit, soit au nœud enfant gauche, selon le résultat de la comparaison suivante : Si le nœud que vous recherchez est inférieur à celui avec lequel vous le compariez, vous passez au nœud enfant gauche, sinon (s'il est plus grand), vous allez au nœud enfant droit. Pourquoi ? Parce que le BST est structuré (selon sa définition), de sorte que le nœud enfant droit est toujours plus grand que le parent et le nœud enfant gauche est toujours plus petit.

###### Recherche en largeur (BFS)

La recherche en largeur est un algorithme utilisé pour parcourir un BST. Elle commence au niveau du nœud racine et se déplace de manière latérale (de côté à côté), recherchant le nœud souhaité. Ce type de recherche peut être décrit comme O(n) étant donné que chaque nœud est visité une fois et que la taille de l'arbre est directement corrélée à la longueur de la recherche.

###### Recherche en profondeur (DFS)

Avec une approche de recherche en profondeur, nous commençons par le nœud racine et descendons une seule branche. Si le nœud souhaité est trouvé le long de cette branche, c'est bien, mais sinon, nous continuons vers le haut et recherchons les nœuds non visités. Ce type de recherche a également une notation Big O de O(n).

#### Insérer

C'est très similaire à la fonction de recherche. Vous commencez à nouveau à la racine de l'arbre et descendez de manière récursive, recherchant le bon endroit pour insérer notre nouveau nœud, de la même manière que celle expliquée dans la fonction de recherche. Si un nœud avec la même valeur est déjà dans l'arbre, vous pouvez choisir d'insérer le duplicata ou non. Certains arbres permettent les duplicatas, d'autres non. Cela dépend de l'implémentation.

#### Suppression

Il y a 3 cas qui peuvent se produire lorsque vous essayez de supprimer un nœud. S'il a,

1. Aucun sous-arbre (aucun enfant) : C'est le plus facile. Vous pouvez simplement supprimer le nœud, sans aucune action supplémentaire requise.
2. Un sous-arbre (un enfant) : Vous devez vous assurer que, après la suppression du nœud, son enfant est ensuite connecté au parent du nœud supprimé.
3. Deux sous-arbres (deux enfants) : Vous devez trouver et remplacer le nœud que vous souhaitez supprimer par son successeur en ordre (le nœud le plus à gauche dans le sous-arbre droit).

La complexité temporelle pour créer un arbre est `O(1)`. La complexité temporelle pour rechercher, insérer ou supprimer un nœud dépend de la hauteur de l'arbre `h`, donc le pire cas est `O(h)` en cas d'arbres déséquilibrés.

#### Prédécesseur d'un nœud

Les prédécesseurs peuvent être décrits comme le nœud qui viendrait juste avant le nœud où vous vous trouvez actuellement. Pour trouver le prédécesseur du nœud actuel, regardez le nœud feuille le plus à droite/le plus grand dans le sous-arbre gauche.

#### Successeur d'un nœud

Les successeurs peuvent être décrits comme le nœud qui viendrait juste après le nœud actuel. Pour trouver le successeur du nœud actuel, regardez le nœud feuille le plus à gauche/le plus petit dans le sous-arbre droit.

### Types spéciaux de BT

* Tas
* Arbre rouge-noir
* Arbre B
* Arbre Splay
* Arbre N-aire
* Trie (Arbre Radix)

### Runtime

**Structure de données : BST**

* Performance dans le pire cas : `O(n)`
* Performance dans le meilleur cas : `O(1)`
* Performance moyenne : `O(log n)`
* Complexité spatiale dans le pire cas : `O(1)`

Où `n` est le nombre de nœuds dans le BST. Le pire cas est O(n) puisque le BST peut être déséquilibré.

### Implémentation de BST

Voici une définition pour un nœud BST ayant des données, référençant ses nœuds enfants gauche et droit.

```
struct node {
   int data;
   struct node *leftChild;
   struct node *rightChild;
};

```

#### Opération de Recherche

Lorsque vous devez rechercher un élément, commencez par le nœud racine. Si les données sont inférieures à la valeur de la clé, recherchez l'élément dans le sous-arbre gauche. Sinon, recherchez l'élément dans le sous-arbre droit. Suivez le même algorithme pour chaque nœud.

```
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

#### Opération d'Insertion

Lorsque vous devez insérer un élément, localisez d'abord son emplacement approprié. Commencez par le nœud racine, puis si les données sont inférieures à la valeur de la clé, recherchez l'emplacement vide dans le sous-arbre gauche et insérez les données. Sinon, recherchez l'emplacement vide dans le sous-arbre droit et insérez les données.

```
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

#### Opération de Suppression

```
void deleteNode(struct node* root, int data){

    if (root == NULL) root=tempnode; 

    if (data < root->key) 
        root->left = deleteNode(root->left, key); 
  

    else if (key > root->key) 
        root->right = deleteNode(root->right, key); 

    else
    { 
        if (root->left == NULL) 
        { 
            struct node *temp = root->right; 
            free(root); 
            return temp; 
        } 
        else if (root->right == NULL) 
        { 
            struct node *temp = root->left; 
            free(root); 
            return temp; 
        } 
  
        struct node* temp = minValueNode(root->right); 
 
        root->key = temp->key; 

        root->right = deleteNode(root->right, temp->key); 
    } 
    return root; 

}

```

Les arbres de recherche binaire (BST) nous donnent également un accès rapide aux prédécesseurs et successeurs. Les prédécesseurs peuvent être décrits comme le nœud qui viendrait juste avant le nœud où vous vous trouvez actuellement.

* Pour trouver le prédécesseur du nœud actuel, regardez le nœud feuille le plus à droite/le plus grand dans le sous-arbre gauche. Les successeurs peuvent être décrits comme le nœud qui viendrait juste après le nœud où vous vous trouvez actuellement.
* Pour trouver le successeur du nœud actuel, regardez le nœud feuille le plus à gauche/le plus petit dans le sous-arbre droit.

### Examinons quelques procédures opérant sur les arbres.

Puisque les arbres sont définis de manière récursive, il est très courant d'écrire des routines qui opèrent sur les arbres et qui sont elles-mêmes récursives.

Par exemple, si nous voulons calculer la hauteur d'un arbre, c'est-à-dire la hauteur d'un nœud racine, nous pouvons procéder de manière récursive, en parcourant l'arbre. Nous pouvons donc dire :

* Par exemple, si nous avons un arbre nil, alors sa hauteur est 0.
* Sinon, nous avons 1 plus le maximum de l'arbre enfant gauche et de l'arbre enfant droit.
* Donc, si nous regardons une feuille par exemple, cette hauteur serait 1 parce que la hauteur de l'enfant gauche est nil, est 0, et la hauteur de l'enfant droit nil est également 0. Donc le max de cela est 0, puis 1 plus 0.

#### Algorithme Height(tree)

```
if tree = nil:
    return 0
return 1 + Max(Height(tree.left),Height(tree.right))

```

#### Voici le code en C++

```
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

Nous pourrions également calculer la taille d'un arbre, c'est-à-dire le nombre de nœuds.

* Encore une fois, si nous avons un arbre nil, nous avons zéro nœud.
* Sinon, nous avons le nombre de nœuds dans l'enfant gauche plus 1 pour nous-mêmes plus le nombre de nœuds dans l'enfant droit. Donc 1 plus la taille de l'arbre gauche plus la taille de l'arbre droit.

#### Algorithme Size(tree)

```
if tree = nil
    return 0
return 1 + Size(tree.left) + Size(tree.right)

```

#### Voici le code en C++

```
int treeSize(struct node* node)
{
    if (node==NULL)
        return 0;
    else
        return 1+(treeSize(node->left) + treeSize(node->right));
}

```

#### Parcours

Il existe 3 types de parcours qui sont généralement effectués sur un arbre de recherche binaire. Tous ces parcours ont une manière quelque peu commune de parcourir les nœuds de l'arbre.

##### In-order

Ce parcours commence par le sous-arbre gauche du nœud racine, puis accède au nœud actuel, suivi du sous-arbre droit du nœud actuel. Le code représente également le cas de base, qui dit qu'un arbre vide est également un arbre de recherche binaire.

```
void inOrder(struct node* root) {
        // Cas de base
        if (root == null) {
                return;
        }
        // Parcourez d'abord le sous-arbre gauche.
        inOrder(root.left);
        // Imprimez la valeur du nœud actuel
        printf("%d ", root.data);
        // Parcourez ensuite le sous-arbre droit.
        inOrder(root.right);
}

```

### Pre-order

Ce parcours accède d'abord à la valeur du nœud actuel, puis parcourt les sous-arbres gauche et droit respectivement.

```
void preOrder(struct node* root) {
        if (root == null) {
                return;
        }
        // Imprimez la valeur du nœud actuel
        printf("%d ", root.data);
        // Parcourez d'abord le sous-arbre gauche.
        preOrder(root.left);
        // Parcourez ensuite le sous-arbre droit.
        preOrder(root.right);
}

```

### Post-order

Ce parcours place la valeur de la racine en dernier, et parcourt d'abord les sous-arbres gauche et droit. L'ordre relatif des sous-arbres gauche et droit reste le même. Seule la position de la racine change dans tous les parcours mentionnés ci-dessus.

```
void postOrder(struct node* root) {
        if (root == null) {
                return;
        }
        // Parcourez d'abord le sous-arbre gauche.
        postOrder(root.left);
        // Parcourez ensuite le sous-arbre droit.
        postOrder(root.right);
        // Imprimez la valeur du nœud actuel
        printf("%d ", root.data);
}

```

### Vidéos pertinentes sur la chaîne YouTube freeCodeCamp

%[https://youtu.be/5cU1ILGy6dM]

## Et Arbre de Recherche Binaire : Parcours et Hauteur

%[https://youtu.be/Aagf3RyK3Lw]

### Voici les types courants d'Arbres Binaires :

Arbre Binaire Complet/Arbre Binaire Strict : Un Arbre Binaire est complet ou strict si chaque nœud a exactement 0 ou 2 enfants.

```
          18
         /   \
       /       \  
     15         30  
    /  \       /  \
  40    50   100   40

```

Dans un Arbre Binaire Complet, le nombre de nœuds feuilles est égal au nombre de nœuds internes plus un.

Arbre Binaire Complet : Un Arbre Binaire est un Arbre Binaire Complet si tous les niveaux sont complètement remplis sauf éventuellement le dernier niveau et le dernier niveau a toutes les clés aussi à gauche que possible

```
           18
         /    \
       /        \  
     15         30  
    /  \       /  \
  40    50   100   40
 /  \   /
8    7 9 

```

Arbre Binaire Parfait : Un Arbre Binaire est un Arbre Binaire Parfait dans lequel tous les nœuds internes ont deux enfants et toutes les feuilles sont au même niveau.

```
          18
         /  \
       /      \  
     15        30  
    /  \      /  \
  40    50  100   40

```

### Augmenter un BST

Parfois, nous devons stocker des informations supplémentaires avec les structures de données traditionnelles pour faciliter nos tâches. Par exemple, considérons un scénario où vous devez trouver le ième plus petit nombre dans un ensemble. Vous pouvez utiliser la force brute ici, mais nous pouvons réduire la complexité du problème à `O(lg n)` en augmentant un arbre rouge-noir ou tout arbre auto-équilibrant (où n est le nombre d'éléments dans l'ensemble). Nous pouvons également calculer le rang de n'importe quel élément en temps `O(lg n)`. Considérons un cas où nous augmentons un arbre rouge-noir pour stocker les informations supplémentaires nécessaires. En plus des attributs habituels, nous pouvons stocker le nombre de nœuds internes dans le sous-arbre enraciné à x (taille du sous-arbre enraciné à x y compris le nœud lui-même). Soit x un nœud arbitraire d'un arbre.

`x.size = x.left.size + x.right.size + 1`

Lors de l'augmentation de l'arbre, nous devons garder à l'esprit que nous devons être capables de maintenir les informations augmentées ainsi que d'effectuer d'autres opérations comme l'insertion, la suppression, la mise à jour en temps `O(lg n)`.

Puisque nous savons que la valeur de x.left.size nous donnera le nombre de nœuds qui précèdent x dans le parcours en ordre de l'arbre. Ainsi, `x.left.size + 1` est le rang de x dans le sous-arbre enraciné à x.