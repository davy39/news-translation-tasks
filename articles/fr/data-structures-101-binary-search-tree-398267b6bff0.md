---
title: 'Structures de Données 101 : Arbre Binaire de Recherche'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-10T16:31:48.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-binary-search-tree-398267b6bff0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*gYtXwdbgInK7hI-u
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Structures de Données 101 : Arbre Binaire de Recherche'
seo_desc: 'By Kevin Turney

  How to combine the efficiency of insertion of a Linked List and the quick search
  of an ordered array.


  _“leafless tree on the hill” by [Unsplash](https://unsplash.com/@fabulu75?utm_source=medium&utm_medium=referral"
  rel="noopener" tar...'
---

Par Kevin Turney

#### Comment combiner l'efficacité d'insertion d'une Liste Chaînée et la recherche rapide d'un tableau ordonné.

![Image](https://cdn-media-1.freecodecamp.org/images/4k66O-44Ze-2G1D19GB4by1CUYiTnQbEzmpo)
_"arbre sans feuilles sur la colline" par [Unsplash](https://unsplash.com/@fabulu75?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Fabrice Villard</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### **Qu'est-ce qu'un Arbre Binaire de Recherche ?**

Commençons par la terminologie de base afin que nous puissions partager le même langage et examiner les concepts connexes. Tout d'abord, quels sont les principes qui définissent un Arbre Binaire de Recherche ?

* À partir de maintenant, j'utiliserai "ABR" pour faire court

Un ABR est considéré comme une structure de données composée de **nœuds**, comme les [**Listes Chaînées**](https://medium.freecodecamp.org/data-structures-101-linked-lists-254c82cf5883)**_._** Ces nœuds sont soit nuls, soit ont des références (liens) vers d'autres nœuds. Ces 'autres' nœuds sont des nœuds enfants, appelés nœud gauche et nœud droit. Les nœuds ont des **valeurs**. Ces valeurs déterminent où ils sont placés dans l'ABR.

De manière similaire à une liste chaînée, chaque nœud est référencé par **un seul** autre nœud, son parent (sauf pour le nœud racine). Nous pouvons donc dire que chaque nœud dans un ABR est en lui-même un ABR. Parce que plus bas dans l'arbre, nous atteignons un autre nœud et ce nœud a un gauche et un droit. Ensuite, selon la direction que nous prenons, ce nœud a un gauche et un droit et ainsi de suite.

1. Le nœud gauche est toujours plus petit que son parent.

2. Le nœud droit est toujours plus grand que son parent.

3. Un ABR est considéré comme équilibré si chaque niveau de l'arbre est entièrement rempli à l'exception du dernier niveau. Au dernier niveau, l'arbre est rempli de gauche à droite.

4. Un ABR Parfait est celui dans lequel il est à la fois plein et complet (tous les nœuds enfants sont au même niveau et chaque nœud a un nœud enfant gauche et un nœud enfant droit).

![Image](https://cdn-media-1.freecodecamp.org/images/2rTqYlcrnWtICedt131tDft0CmkzZaViExJX)

### Pourquoi l'utiliserions-nous ?

Quels sont quelques exemples concrets d'ABR ? Les arbres sont souvent utilisés dans la recherche, la logique de jeu, les tâches d'autocomplétion et les graphiques.

Vitesse. Comme mentionné précédemment, l'ABR est une structure de données ordonnée. Lors de l'insertion, les nœuds sont placés de manière ordonnée. Cet ordre inhérent rend la recherche rapide. Similaire à la recherche binaire (avec un tableau qui est trié), nous réduisons de moitié la quantité de données à trier à chaque passage. Par exemple, supposons que nous cherchons une petite valeur de nœud. À chaque passage, nous continuons à nous déplacer le long du nœud le plus à gauche. Cela élimine automatiquement la moitié des valeurs plus grandes !

De plus, contrairement à un tableau, les données sont stockées par référence. Lorsque nous ajoutons à la structure de données, nous créons un nouveau bloc en mémoire et y établissons un lien. Cela est plus rapide que de créer un nouveau tableau avec plus d'espace et d'insérer ensuite les données du tableau plus petit dans le nouveau, plus grand.

En bref, l'insertion, la suppression et la recherche sont les opérations vedettes pour un ABR.

Maintenant que nous comprenons les principes, les avantages et les composants de base d'un ABR, implémentons-en un en JavaScript.

L'API pour un ABR se compose des éléments suivants : **Insert, Contains, Get Min, Get Max, Remove Node, Check if Full, Is Balanced**, et les types de recherche — **Depth First (preOrder, inOrder, postOrder), Breadth First Search**, et enfin **Get Height**. C'est une grande API, prenez-la une section à la fois.

### **Implémentation**

**Le constructeur**

L'ABR est composé de nœuds, et chaque nœud a une valeur.

```
function Node(value){  this.value = value;  this.left = null;  this.right = null;}
```

Le constructeur ABR est composé d'un nœud racine.

```
function BinarySearchTree() { this.root = null;}
```

```
let bst = new BST();let node = new Node();
```

```
console.log(node, bst); // Node { value: undefined, left: null, right: null } BST { root: null }
```

... jusqu'à présent, tout va bien.

### Insertion

```
BinarySearchTree.prototype.insert = function(value){ let node = new Node(value); if(!this.root) this.root = node; else{    let current = this.root;    while(!!current){       if(node.value < current.value){       if(!current.left){           current.left = node;           break;         }         current = current.left;         }        else if(node.value > current.value){         if(!current.right){            current.right = node;            break;           }          current = current.right;          }         else {          break;           }         }        }    return this; };
```

```
let bst = new BST();bst.insert(25); // BST { root: Node { value: 25, left: null, right: null } }
```

Ajoutons quelques valeurs supplémentaires.

```
bst.insert(40).insert(20).insert(9).insert(32).insert(15).insert(8).insert(27);
```

```
BST { root:  Node { value: 25, left: Node { value: 20, left: [Object], right: null }, right: Node { value: 40, left: [Object], right: null } } }
```

Pour une visualisation sympa [Allez Ici](http://btv.melezinek.cz/binary-search-tree.html)!!

Décortiquons cela.

1. Tout d'abord, nous passons une valeur et créons un nouveau nœud
2. Vérifions s'il y a une racine, sinon, définissons ce nœud nouvellement créé comme nœud racine
3. S'il y a un nœud racine, nous créons une variable déclarée "current", et définissons sa valeur sur le nœud racine
4. Si la valeur du nœud nouvellement créé est plus petite que celle du nœud racine, nous nous déplacerons vers la gauche
5. Nous continuons à comparer cette valeur de nœud aux nœuds de gauche.
6. Si la valeur est suffisamment petite et que nous atteignons un point où il n'y a plus de nœuds de gauche, nous plaçons cet élément ici.
7. Si la valeur du nœud est plus grande, nous répétons les mêmes étapes que ci-dessus sauf que nous nous déplaçons le long de la droite.
8. Nous avons besoin des instructions break car il n'y a pas d'étape de comptage pour terminer la boucle while.

### Contains

C'est une approche assez simple.

```
BinarySearchTree.prototype.contains = function(value){ let current = this.root; while(current){ if(value === current.value) return true; if(value < current.value) current = current.left; if(value > current.value) current = current.right; } return false;};
```

### Get Min et Get Max.

Continuez à parcourir vers la gauche pour la plus petite valeur ou vers la droite pour la plus grande.

```
BinarySearchTree.prototype.getMin = function(node){ if(!node) node = this.root; while(node.left) { node = node.left; } return node.value};
```

```
BinarySearchTree.prototype.getMax = function(node){ if(!node) node = this.root; while(node.right) { node = node.right; } return node.value;};
```

### Suppression

Supprimer un nœud est l'opération la plus délicate, car les nœuds doivent être réorganisés pour maintenir les propriétés d'un ABR. Il y a un cas si un nœud n'a qu'un seul enfant et un cas s'il y a à la fois un nœud gauche et un nœud droit. Nous utilisons la fonction auxiliaire plus grande pour faire le gros du travail.

```
BinarySearchTree.prototype.removeNode = function(node, value){ if(!node){   return null; } if(value === node.value){ // aucun enfant if(!node.left && !node.right) return null; // un enfant et c'est le droit if(!node.left) node.right;// un enfant et c'est le gauche if(!node.right) node.left;  // deux enfants const temp = this.getMin(node.right); node.value = temp; node.right = this.removeNode(node.right, temp); return node; } else if(value < node.value) {     node.left = this.removeNode(node.left, value);     return node; } else  {     node.right = this.removeNode(node.right, value);     return node;   }};
```

```
BinarySearchTree.prototype.remove = function(value){ this.root = this.removeNode(this.root, value);};
```

Cela fonctionne comme suit...

Contrairement à deleteMin et deleteMax, où nous pouvons simplement parcourir tout le chemin vers la gauche ou tout le chemin vers la droite et prendre la dernière valeur, nous devons enlever un nœud et ensuite le remplacer par quelque chose. Cette solution a été développée en 1962 par T. Hibbard. Nous tenons compte du cas où nous pouvons supprimer un nœud avec un seul enfant ou aucun, c'est mineur. Si aucun enfant, pas de problème. Si un enfant est présent, cet enfant monte simplement d'un cran.

Mais avec un nœud prévu pour être supprimé qui a deux enfants, quel enfant prend sa place ? Certes, nous ne pouvons pas déplacer un nœud plus grand vers le bas. Ce que nous faisons donc, c'est le remplacer par son successeur, le prochain pivot. Nous devons trouver le plus petit enfant droit à droite qui est plus grand que l'enfant gauche.

1. Créez une valeur temporaire et stockez le plus petit nœud à sa droite. Ce que cela fait, c'est satisfaire la propriété que les valeurs à gauche sont toujours plus petites et les valeurs à droite sont toujours plus grandes.
2. Réinitialisez la valeur du nœud à cette variable temporaire
3. Supprimez le nœud droit.
4. Ensuite, nous comparons les valeurs à gauche et à droite et déterminons la valeur assignée.

Cela est mieux expliqué avec une image :

![Image](https://cdn-media-1.freecodecamp.org/images/cEcyXZpZvRln6p7jzJq08lOJsORH6yA7Rd0T)

### Recherche

Il existe deux types de recherche, Depth First et Breadth First. Breadth First consiste simplement à s'arrêter à chaque niveau en descendant. Cela ressemble à ceci : nous commençons par la racine, puis l'enfant gauche, puis l'enfant droit. Passez au niveau suivant, enfant gauche puis enfant droit. Imaginez cela comme un mouvement horizontal. Nous employons, je devrais dire simulons, une file d'attente pour aider à ordonner le processus. Nous passons une fonction, car souvent nous voulons opérer sur une valeur.

```
BinarySearchTree.prototype.traverseBreadthFirst = function(fn) { let queue = []; queue.push(this.root); while(!!queue.length) {   let node = queue.shift();   fn(node);   node.left && queue.push(node.left);   node.right && queue.push(node.right);  }}
```

La recherche Depth First implique de descendre l'ABR de manière spécifiée, soit en preOrder, inOrder, ou postOrder. Je vais expliquer les différences sous peu.

Dans l'esprit du code concis, nous avons une fonction traverseDepthFirst de base et nous passons une fonction et une méthode. Encore une fois, la fonction implique que nous voulons faire quelque chose aux valeurs en cours de route, tandis que la méthode est le type de recherche que nous souhaitons effectuer. Dans le traverseDFS, nous avons un repli : la recherche preOrder en place.

Maintenant, comment chacun est-il différent ? Tout d'abord, expliquons inOrder. Cela devrait être auto-explicatif mais ce n'est pas le cas. Voulons-nous dire dans l'ordre d'insertion, dans l'ordre du plus haut au plus bas ou du plus bas au plus haut ? Je voulais simplement que vous considériez ces choses au préalable. Dans ce cas, oui, cela signifie du plus bas au plus haut.

**preOrder** peut être pensé comme **Parent, Enfant Gauche, puis Enfant Droit_._**

**postOrder** comme **Enfant Gauche, Enfant Droit, Parent_._**

```
BinarySearchTree.prototype.traverseDFS = function(fn, method){ let current = this.root; if(!!method) this[method](current, fn); else this._preOrder(current, fn);};
```

```
BinarySearchTree.prototype._inOrder = function(node, fn){ if(!!node){ this._inOrder(node.left, fn); if(!!fn) fn(node); this._inOrder(node.right, fn); }};
```

```
BinarySearchTree.prototype._preOrder = function(node, fn){ if(node){ if(fn) fn(node); this._preOrder(node.left, fn); this._preOrder(node.right, fn); }};
```

```
BinarySearchTree.prototype._postOrder = function(node, fn){ if(!!node){ this._postOrder(node.left, fn); this._postOrder(node.right, fn); if(!!fn) fn(node); }};
```

### **Vérifier si l'ABR est plein**

Rappelons que, plus tôt, un ABR est plein si chaque nœud a zéro ou deux enfants.

```
// un ABR est plein si chaque nœud a zéro ou deux enfants (aucun nœud n'a un enfant)
```

```
BinarySearchTree.prototype.checkIfFull = function(fn){ let result = true; this.traverseBFS = (node) => {   if(!node.left && !node.right) result = false;   else if(node.left && !node.right) result = false;  } return result;};
```

### Obtenir la Hauteur de l'ABR

Que signifie obtenir la hauteur d'un arbre ? Pourquoi est-ce important ? C'est là que la **Complexité Temporelle** (aka Big O) entre en jeu. Les opérations de base sont proportionnelles à la hauteur d'un arbre. Donc, comme nous l'avons suggéré plus tôt, si nous recherchons une valeur particulière, le nombre d'opérations que nous devons effectuer est réduit de moitié à chaque étape.

Cela signifie que si nous avons une miche de pain et que nous la coupons en deux, puis que nous coupons cette moitié en deux, et que nous continuons à faire cela jusqu'à obtenir le morceau de pain exact que nous voulons.

En informatique, cela s'appelle O(log n). Nous commençons avec une taille d'entrée de quelque sorte, et avec le temps, cette taille devient plus petite (un peu en s'aplatissant). Une recherche linéaire droite est notée O(n), car à mesure que la taille d'entrée augmente, le temps nécessaire pour exécuter les opérations augmente également. O(n) conceptuellement est une ligne à 45 degrés commençant à l'origine zéro sur un graphique et se déplaçant vers la droite. L'échelle horizontale représente la taille d'une entrée et l'échelle verticale représente le temps nécessaire pour compléter.

Le temps constant est O(1). Peu importe la taille de l'entrée, grande ou petite, l'opération a lieu dans le même laps de temps. Par exemple, push() et pop() d'un tableau sont en temps constant. La recherche d'une valeur dans une table de hachage est en temps constant.

J'expliquerai plus en détail cela dans un futur article, mais je voulais vous armer de cette connaissance pour l'instant.

**Retour à la hauteur.**

Nous avons une fonction récursive, et notre cas de base est : **'si nous n'avons pas de nœud, alors nous commençons à this.root'_** Cela implique que nous pouvons commencer à des valeurs plus basses dans l'arbre et obtenir des sous-hauteurs d'arbre.

Donc si nous passons this.root pour commencer, nous nous déplaçons récursivement vers le bas de l'arbre et ajoutons les appels de fonction à la pile d'exécution (autres articles ici). Lorsque nous atteignons le bas, la pile est remplie. Ensuite, les appels sont exécutés et nous comparons les hauteurs de la gauche et les hauteurs de la droite et nous incrémentons de un.

```
BinarySearchTree.prototype._getHeights = function(node){ if(!node) return -1; let left = this._getHeights(node.left); let right = this._getHeights(node.right); return Math.max(left, right) + 1;};
```

```
BinarySearchTree.prototype.getHeight = function(node){ if(!node) node = this.root; return this._getHeights(node);};
```

### Enfin, Is Balanced

Ce que nous faisons, c'est vérifier si l'arbre est rempli à chaque niveau, et au dernier niveau, s'il est rempli de gauche à droite.

```
BinarySearchTree.prototype._isBalanced = function(node){ if(!node) return true; let heightLeft = this._getHeights(node.left); let heightRight = this._getHeights(node.right); let diff = Math.abs(heightLeft — heightRight); if(diff > 1) return false; else return this._isBalanced(node.left) &&    this._isBalanced(node.right);};
```

```
BinarySearchTree.prototype.isBalanced = function(node){ if(!node) node = this.root; return this._isBalanced(node);};
```

### Imprimer

Utilisez cela pour visualiser toutes les méthodes que vous voyez, surtout les parcours en profondeur et en largeur.

```
BinarySearchTree.prototype.print = function() { if(!this.root) {   return console.log('Aucun nœud racine trouvé'); } let newline = new Node('|'); let queue = [this.root, newline]; let string = ''; while(queue.length) {   let node = queue.shift();   string += node.value.toString() + ' ';   if(node === newline && queue.length) queue.push(newline);    if(node.left) queue.push(node.left);   if(node.right) queue.push(node.right);  } console.log(string.slice(0, -2).trim());};
```

**Notre ami Console.log!! Amusez-vous et expérimentez.**

```
const binarySearchTree = new BinarySearchTree();binarySearchTree.insert(5);binarySearchTree.insert(3);
```

```
binarySearchTree.insert(7);binarySearchTree.insert(2);binarySearchTree.insert(4);binarySearchTree.insert(4);binarySearchTree.insert(6);binarySearchTree.insert(8);binarySearchTree.print(); // => 5 | 3 7 | 2 4 6 8
```

```
binarySearchTree.contains(4);
```

```
//binarySearchTree.printByLevel(); // => 5 \n 3 7 \n 2 4 6 8console.log('--- DFS inOrder');
```

```
binarySearchTree.traverseDFS(function(node) { console.log(node.value); }, '_inOrder'); // => 2 3 4 5 6 7 8
```

```
console.log('--- DFS preOrder');
```

```
binarySearchTree.traverseDFS(function(node) { console.log(node.value); }, '_preOrder'); // => 5 3 2 4 7 6 8
```

```
console.log('--- DFS postOrder');
```

```
binarySearchTree.traverseDFS(function(node) { console.log(node.value); }, '_postOrder'); // => 2 4 3 6 8 7 5
```

```
console.log('--- BFS');
```

```
binarySearchTree.traverseBFS(function(node) { console.log(node.value); }); // => 5 3 7 2 4 6 8
```

```
console.log('min est 2:', binarySearchTree.getMin()); // => 2
```

```
console.log('max est 8:', binarySearchTree.getMax()); // => 8
```

```
console.log('l\'arbre contient 3 est vrai:', binarySearchTree.contains(3)); // => true
```

```
console.log('l\'arbre contient 9 est faux:', binarySearchTree.contains(9)); // => false
```

```
// console.log('la hauteur de l\'arbre est 2:', binarySearchTree.getHeight()); // => 2
```

```
console.log('l\'arbre est équilibré est vrai:', binarySearchTree.isBalanced(),'ligne 220'); // => true
```

```
binarySearchTree. remove(11); // supprimer un nœud inexistant
```

```
binarySearchTree.print(); // => 5 | 3 7 | 2 4 6 8
```

```
binarySearchTree.remove(5); // supprimer 5, 6 monte
```

```
binarySearchTree.print(); // => 6 | 3 7 | 2 4 8
```

```
console.log(binarySearchTree.checkIfFull(), 'devrait être vrai');
```

```
var fullBSTree = new BinarySearchTree(10);
```

```
fullBSTree.insert(5).insert(20).insert(15).insert(21).insert(16).insert(13);
```

```
console.log(fullBSTree.checkIfFull(), 'devrait être vrai');
```

```
binarySearchTree.remove(7); // supprimer 7, 8 monte
```

```
binarySearchTree.print(); // => 6 | 3 8 | 2 4
```

```
binarySearchTree.remove(8); // supprimer 8, l'arbre devient déséquilibré
```

```
binarySearchTree.print(); // => 6 | 3 | 2 4
```

```
console.log('l\'arbre est équilibré est faux:', binarySearchTree.isBalanced()); // => true
```

```
console.log(binarySearchTree.getHeight(),'la hauteur est 2')
```

```
binarySearchTree.remove(4);
```

```
binarySearchTree.remove(2);
```

```
binarySearchTree.remove(3);
```

```
binarySearchTree.remove(6);
```

```
binarySearchTree.print(); // => 'Aucun nœud racine trouvé'
```

```
//binarySearchTree.printByLevel(); // => 'Aucun nœud racine trouvé'
```

```
console.log('la hauteur de l\'arbre est -1:', binarySearchTree.getHeight()); // => -1
```

```
console.log('l\'arbre est équilibré est vrai:', binarySearchTree.isBalanced()); // => true
```

```
console.log('---');
```

```
binarySearchTree.insert(10);
```

```
console.log('la hauteur de l\'arbre est 0:', binarySearchTree.getHeight()); // => 0
```

```
console.log('l\'arbre est équilibré est vrai:', binarySearchTree.isBalanced()); // => true
```

```
binarySearchTree.insert(6);
```

```
binarySearchTree.insert(14);
```

```
binarySearchTree.insert(4);
```

```
binarySearchTree.insert(8);
```

```
binarySearchTree.insert(12);
```

```
binarySearchTree.insert(16);
```

```
binarySearchTree.insert(3);
```

```
binarySearchTree.insert(5);
```

```
binarySearchTree.insert(7);
```

```
binarySearchTree.insert(9);
```

```
binarySearchTree.insert(11);
```

```
binarySearchTree.insert(13);
```

```
binarySearchTree.insert(15);
```

```
binarySearchTree.insert(17);
```

```
binarySearchTree.print(); // => 10 | 6 14 | 4 8 12 16 | 3 5 7 9 11 13 15 17
```

```
binarySearchTree.remove(10); // supprimer 10, 11 monte
```

```
binarySearchTree.print(); // => 11 | 6 14 | 4 8 12 16 | 3 5 7 9 x 13 15 17
```

```
binarySearchTree.remove(12); // supprimer 12; 13 monte
```

```
binarySearchTree.print(); // => 11 | 6 14 | 4 8 13 16 | 3 5 7 9 x x 15 17
```

```
console.log('l\'arbre est équilibré est vrai:', binarySearchTree.isBalanced()); // => true
```

```
//console.log('l\'arbre est équilibré optimisé est vrai:', binarySearchTree.isBalancedOptimized()); // => true
```

```
binarySearchTree.remove(13); // supprimer 13, 13 n'a pas d'enfants donc rien ne change
```

```
binarySearchTree.print(); // => 11 | 6 14 | 4 8 x 16 | 3 5 7 9 x x 15 17
```

```
console.log('l\'arbre est équilibré est faux:', binarySearchTree.isBalanced()); // => false
```

```
// donne ...5 | 3 7 | 2 4 6 8--- DFS inOrder2345678--- DFS preOrder5324768--- DFS postOrder2436875--- BFS5372468min est 2: 2max est 8: 8l\'arbre contient 3 est vrai: truel\'arbre contient 9 est faux: falsel\'arbre est équilibré est vrai: true ligne 2205 | 3 7 | 2 4 6 86 | 3 7 | 2 4 8true 'devrait être vrai'true 'devrait être vrai'6 | 3 8 | 2 46 | 3 | 2 4l\'arbre est équilibré est faux: false2 'la hauteur est 2'Aucun nœud racine trouvéla hauteur de l\'arbre est -1: -1l\'arbre est équilibré est vrai: true---la hauteur de l\'arbre est 0: 0l\'arbre est équilibré est vrai: true10 | 6 14 | 4 8 12 16 | 3 5 7 9 11 13 15 1711 | 6 14 | 4 8 12 16 | 3 5 7 9 13 15 1711 | 6 14 | 4 8 13 16 | 3 5 7 9 15 17l\'arbre est équilibré est vrai: true11 | 6 14 | 4 8 16 | 3 5 7 9 15 17l\'arbre est équilibré est faux: false
```

### Complexité Temporelle

1. Insertion O(log n)  
2. Suppression O(log n)  
3. Recherche O(log n)

Wow, c'est effectivement beaucoup d'informations. J'espère que les explications étaient aussi claires et aussi introductives que possible. Encore une fois, écrire m'aide à solidifier les concepts et comme l'a dit Richard Feynman, "Quand une personne enseigne, deux apprennent."

### Ressources

Probablement la meilleure ressource pour visualiser, utilisez-la définitivement :

[**Visualisation des Structures de Données**](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)  
[_David Galles Informatique Université de San Francisco_www.cs.usfca.edu](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)[**BinaryTreeVisualiser - Arbre Binaire de Recherche**](http://btv.melezinek.cz/binary-search-tree.html)  
[_Description du site ici_btv.melezinek.cz](http://btv.melezinek.cz/binary-search-tree.html)[**VisuAlgo - Arbre Binaire de Recherche, Arbre AVL**](https://visualgo.net/en/bst?slide=1)  
[_Un Arbre Binaire de Recherche (ABR) est un arbre binaire dans lequel chaque sommet a seulement jusqu'à 2 enfants qui satisfait la propriété ABR..._visualgo.net](https://visualgo.net/en/bst?slide=1)[**Big-O Algorithm Complexity Cheat Sheet (Know Thy Complexities!) @ericdrowell**](http://www.bigocheatsheet.com/)  
[_Salut ! Cette page web couvre les complexités Big-O d'espace et de temps des algorithmes courants utilisés en informatique. Quand..._www.bigocheatsheet.com](http://www.bigocheatsheet.com/)[**Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne**](https://algs4.cs.princeton.edu/home/)  
[_Le manuel Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne passe en revue les algorithmes et les structures de données les plus importants..._algs4.cs.princeton.edu](https://algs4.cs.princeton.edu/home/)[**Binary search tree - Wikipedia**](https://en.wikipedia.org/wiki/Binary_search_tree)  
[_En informatique, les arbres binaires de recherche (ABR), parfois appelés arbres binaires ordonnés ou triés, sont un type particulier..._en.wikipedia.org](https://en.wikipedia.org/wiki/Binary_search_tree)