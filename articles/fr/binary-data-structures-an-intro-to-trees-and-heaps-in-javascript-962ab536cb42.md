---
title: 'Structures de données binaires : une introduction aux arbres et aux tas en
  JavaScript'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-20T21:24:05.000Z'
originalURL: https://freecodecamp.org/news/binary-data-structures-an-intro-to-trees-and-heaps-in-javascript-962ab536cb42
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zrltwsvmiJBwYBZ2g6uiOg.jpeg
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Structures de données binaires : une introduction aux arbres et aux tas
  en JavaScript'
seo_desc: 'By Yung L. Leung

  Linear data structures are simple in direction. A linked list is a list of nodes
  (each containing their own data) that are linked from one node to the next (and
  to the previous, for a doubly linked list). A stack builds upward like a...'
---

Par Yung L. Leung

Les [**structures de données linéaires**](https://medium.freecodecamp.org/linear-data-structures-linked-lists-stacks-queues-a13c7591ad87) sont simples en direction. Une **liste chaînée** est une liste de nœuds (chacun contenant ses propres données) qui sont liés d'un nœud à l'autre (et au précédent, pour une liste doublement chaînée). Une **pile** se construit vers le haut comme une tour de données. Chaque nœud s'empile au-dessus de l'autre et se raccourcit selon un mécanisme **dernier entré, premier sorti (LIFO)**. Une **file d'attente** est une ligne de nœuds qui s'allonge à partir de la fin de la ligne et se raccourcit selon un mécanisme **premier entré, premier sorti (FIFO)**.

Les **structures de données binaires** sont comme une fourche dans une route de données. Les nœuds se construisent comme les branches d'un **arbre** ou un **tas** de rochers.

### Arbres

![Image](https://cdn-media-1.freecodecamp.org/images/pt4Jg1dZ90bHVIsMWmfT0O5bI3FPflW53AGf)
_[source](https://www.rosettacode.org/mw/images/a/a3/Fractal_tree_bbc.gif" rel="noopener" target="_blank" title=")_

Un **arbre binaire de recherche** est composé de nœuds qui se ramifient en pas plus de deux nœuds (binaire). Un nœud parent peut avoir des nœuds enfants gauche et droit. Par convention, les nœuds enfants de gauche contiennent des valeurs inférieures à celles du parent. Alors que les nœuds enfants de droite contiennent des valeurs supérieures (**gauche est inférieur, droite est supérieur**). Tous les arbres commencent par un seul nœud racine.

![Image](https://cdn-media-1.freecodecamp.org/images/msMkP14InEQYWfg8eWglyjdXhZ5SrojngUPm)
_Une racine se ramifie en deux parents de feuilles. Les feuilles (vertes) sont des nœuds sans enfants._

Pour **insérer** une valeur, il faut créer un **nouveau nœud**, comparer sa valeur à la **racine** et à ses valeurs **descendantes**, tout en décidant de rechercher plus à gauche (insertion d'une valeur inférieure) ou plus à droite (insertion d'une valeur supérieure). Une fois qu'une position disponible est trouvée, le nœud est inséré à sa place.

![Image](https://cdn-media-1.freecodecamp.org/images/ZSfQBHy1ZvdXm5A304q1jFMOZpAamWG1F4Ae)
_**Insertion du nœud avec une valeur de 6**_

Pour **trouver** une valeur est similaire à l'insertion d'une valeur. Vous effectuez la recherche d'une valeur stockée et retournez le nœud qui la contient.

![Image](https://cdn-media-1.freecodecamp.org/images/dSrg3P7BVUiquGDvZYHwvCfVW9AgK4HeuaMC)
_**Trouver le nœud avec une valeur de 6**_

Pour effectuer une **recherche en largeur** des valeurs, il faut stocker une valeur racine. Puis procéder avec l'enfant de gauche, puis l'enfant de droite et ainsi de suite.

![Image](https://cdn-media-1.freecodecamp.org/images/MgGzdIJ78U3kLa-qh-AezTkzNYDsCOo4MB6j)
_**La recherche en largeur retourne [3, 1, 5, 0, 2, 4, 6]**_

Pour effectuer une **recherche en profondeur (pré-ordre)** des valeurs, il faut stocker une valeur racine. Puis procéder avec tous les descendants à gauche, avant les descendants à droite.

![Image](https://cdn-media-1.freecodecamp.org/images/VhYpkEBTORBiFDgRHEJAHOpSO5dVTH6h0IBe)
_**La recherche en profondeur pré-ordre retourne [3, 1, 0, 2, 5, 4, 6]**_

Puisque l'**insertion** et la **recherche** d'un nœud d'une certaine valeur sont des processus relativement similaires (l'insertion insère un nœud alors que la recherche retourne un nœud), il n'est pas surprenant que leur complexité soit la même, **O(log n)**.

![Image](https://cdn-media-1.freecodecamp.org/images/3WWlcSbWBhhv7P-lPxF-hbaQ8Kq7vyoqvcKw)
_**n = 3**_

Pour un **arbre binaire de recherche** à 3 nœuds, **trouver** **5** nécessite deux étapes :

* **5** est-il supérieur ou inférieur à 3 ? Procéder vers la droite.
* **5** est-il égal à la valeur recherchée ? Retourner le nœud.

De même, pour **insérer** un nœud avec la valeur 6, deux étapes sont nécessaires :

* **6** est-il supérieur ou inférieur à 3 ? Procéder vers la droite.
* **6** est-il supérieur ou inférieur à 5 ? Insérer du côté droit.

### Tas

![Image](https://cdn-media-1.freecodecamp.org/images/d1JWsgkTF-HSMsfHQw-QJt6OcGDfQBOk8OGe)
_Photo par Nick Tong sur [Unsplash](https://unsplash.com/photos/zjy2yMUGzRU" rel="noopener" target="_blank" title=")_

Un **tas binaire** est une structure pyramidale de nœuds dont les nœuds peuvent s'empiler vers le haut avec des rangées de valeurs décroissantes vers un minimum (**tas binaire minimum**) ou avec des rangées de valeurs croissantes vers un maximum (**tas binaire maximum**). Comme l'arbre, chaque nœud parent peut s'étendre jusqu'à deux nœuds enfants. Contrairement à l'arbre, chaque parent peut contenir une valeur inférieure à celle de ses enfants (**tas binaire minimum**) ou une valeur supérieure (**tas binaire maximum**).

![Image](https://cdn-media-1.freecodecamp.org/images/HE8SQ3qiyd19h6kZOCpp8griQB2cOIXcV4L6)
_Tas binaire maximum_

Pour un **tas binaire maximum**, **insérer** une valeur à la base de la pyramide nécessite de la comparer aux nœuds parents et de **faire remonter** la valeur la plus grande.

![Image](https://cdn-media-1.freecodecamp.org/images/v7W4gtqZZ4vknoz9-Qj28CuXtviStsYYXAS8)
_**Insertion d'un nœud avec une valeur de 6 et le faire remonter.**_

Pour **extraire une valeur maximale**, il faut supprimer la valeur de l'apex et **faire descendre** une valeur de la base de la pyramide. Cela implique de trouver le plus grand des deux nœuds enfants.

![Image](https://cdn-media-1.freecodecamp.org/images/C-UotKFPhKz02WrcwHlP-qf6zyjI9OlPpe64)
_**Extraction du nœud maximum avec la valeur de 6 et faire descendre le nœud avec la valeur de 3.**_

Pour un **tas binaire maximum**, l'**insertion** d'un nœud et l'**extraction** d'un nœud avec la valeur maximale ont toutes deux une complexité de **O(log n)**.

Pour un **tas binaire maximum** à 3 nœuds, l'insertion d'un nœud avec la valeur 6 nécessite deux étapes.

![Image](https://cdn-media-1.freecodecamp.org/images/YHk4cDUnf9vpmrx1IwSnmOqXJ6t0QAsbq7cs)
_**Faire remonter le nouveau nœud avec la valeur 6**_

* Après avoir attaché le nœud de valeur 6 à une nouvelle rangée (sous 4), **6** est-il supérieur ou inférieur à 4 ? Échanger.
* **6** est-il supérieur ou inférieur à 5 ? Échanger.

De même, après la suppression d'un nœud avec une valeur maximale et son remplacement par un nœud de valeur **1**, deux étapes restent.

![Image](https://cdn-media-1.freecodecamp.org/images/37yXpaPzOVAquuqkOYNPPqch6OtMbmf8EW4W)
_**Faire descendre le nœud avec la valeur 1**_

* **1** est-il supérieur ou inférieur à 5 ? Échanger.
* **1** est-il supérieur ou inférieur à 4 ? Échanger.

Merci d'avoir lu !

### Référence :

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)