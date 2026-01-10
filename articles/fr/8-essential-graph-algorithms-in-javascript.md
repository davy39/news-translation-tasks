---
title: Comment implémenter 8 algorithmes de graphe essentiels en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-17T23:49:50.000Z'
originalURL: https://freecodecamp.org/news/8-essential-graph-algorithms-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a33740569d1a4ca242b.jpg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
seo_title: Comment implémenter 8 algorithmes de graphe essentiels en JavaScript
seo_desc: "By Girish Ramloul\nIn this article, I will implement 8 graph algorithms\
  \ that explore the search and combinatorial problems (traversals, shortest path\
  \ and matching) of graphs in JavaScript. \nThe problems are borrowed from the book,\
  \ Elements of Programm..."
---

Par Girish Ramloul

Dans cet article, je vais implémenter **8 algorithmes de graphe** qui explorent les problèmes de recherche et de combinatoire (parcours, chemin le plus court et appariement) des graphes en JavaScript. 

Les problèmes sont empruntés au livre, [Elements of Programming Interviews in Java](https://www.google.com/books/edition/Elements_of_Programming_Interviews_in_Ja/ux3PCwAAQBAJ?hl=en&gbpv=0). Les solutions dans le livre sont codées en Java, Python ou C++ selon la version du livre que vous possédez. 

Bien que la logique derrière la modélisation des problèmes soit indépendante du langage, les extraits de code que je fournis dans cet article utilisent certaines particularités de JavaScript. 

Chaque solution à chaque problème est divisée en 3 sections : un aperçu de la solution, le pseudocode, et enfin le code réel en JavaScript.

Pour tester le code et voir ce qu'il est censé faire, vous pouvez utiliser [les outils de développement de Chrome](https://developers.google.com/web/tools/chrome-devtools/javascript/snippets) pour exécuter les extraits de code sur le navigateur lui-même ou utiliser NodeJS pour les exécuter depuis la ligne de commande.

## Implémentation de graphe

Les 2 représentations les plus couramment utilisées des [graphes](https://www.geeksforgeeks.org/graph-and-its-representations/) sont la liste d'adjacence et la matrice d'adjacence. 

Les problèmes que je vais résoudre concernent des graphes clairsemés (peu d'arêtes), et les opérations sur les sommets dans l'approche de la liste d'adjacence prennent un temps constant (ajout d'un sommet, O(1)) et linéaire (suppression d'un sommet, O(V+E)). Je vais donc m'en tenir à cette implémentation pour la plupart.

Réalisons cela avec une implémentation simple de **graphe non orienté et non pondéré** en utilisant une **liste d'adjacence**. Nous allons maintenir un objet (adjacencyList) qui contiendra tous les sommets de notre graphe comme clés. Les valeurs seront un tableau de tous les sommets adjacents. Dans l'exemple ci-dessous, le sommet 1 est connecté aux sommets 2 et 4, donc adjacencyList: { 1 : [ 2, 4 ] } et ainsi de suite pour les autres sommets. 

Pour construire le graphe, nous avons deux fonctions : **addVertex** et **addEdge**. addVertex est utilisé pour ajouter un sommet à la liste. addEdge est utilisé pour connecter les sommets en ajoutant les sommets voisins aux tableaux source et destination puisque ce est un graphe non orienté. Pour faire un graphe orienté, nous pouvons simplement supprimer les lignes 14–16 et 18 dans le code ci-dessous.

Avant de supprimer un sommet, nous devons parcourir le tableau des sommets voisins et supprimer toutes les connexions possibles à ce sommet.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image_1_graphs.jpg)
_Un graphe non orienté et non pondéré implémenté en utilisant une liste d'adjacence_

```javascript
class Graph {
  constructor() {
    this.adjacencyList = {};
  }
  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) {
      this.adjacencyList[vertex] = [];
    }
  }
  addEdge(source, destination) {
    if (!this.adjacencyList[source]) {
      this.addVertex(source);
    }
    if (!this.adjacencyList[destination]) {
      this.addVertex(destination);
    }
    this.adjacencyList[source].push(destination);
    this.adjacencyList[destination].push(source);
  }
  removeEdge(source, destination) {
    this.adjacencyList[source] = this.adjacencyList[source].filter(vertex => vertex !== destination);
    this.adjacencyList[destination] = this.adjacencyList[destination].filter(vertex => vertex !== source);
  }
  removeVertex(vertex) {
    while (this.adjacencyList[vertex]) {
      const adjacentVertex = this.adjacencyList[vertex].pop();
      this.removeEdge(vertex, adjacentVertex);
    }
    delete this.adjacencyList[vertex];
  }  
}
```

## Parcours de graphe

En nous basant sur notre implémentation de graphes dans la section précédente, nous allons implémenter les parcours de graphe : recherche en largeur d'abord et recherche en profondeur d'abord.

### Recherche en largeur d'abord

BFS visite les nœuds **un niveau à la fois**. Pour éviter de visiter le même nœud plus d'une fois, nous allons maintenir un objet **visited**. 

Puisque nous devons traiter les nœuds dans un ordre Premier Entré Premier Sorti, une file est un bon candidat pour la structure de données à utiliser. La complexité temporelle est O(V+E).

```
function BFS
   Initialiser une file vide, un tableau 'result' vide et une carte 'visited' vide
   Ajouter le sommet de départ à la file et à la carte visited
   Tant que la file n'est pas vide :
     - Désenfiler et stocker le sommet actuel
     - Pousser le sommet actuel dans le tableau result
     - Parcourir la liste d'adjacence du sommet actuel :
       - Pour chaque sommet adjacent, si le sommet n'est pas visité :
         - Ajouter le sommet à la carte visited
         - Enfiler le sommet
   Retourner le tableau result
```

### Recherche en profondeur d'abord

DFS visite les nœuds en profondeur. Puisque nous devons traiter les nœuds dans un ordre Dernier Entré Premier Sorti, nous allons utiliser une **pile**. 

En partant d'un sommet, nous allons pousser les sommets voisins dans notre pile. Chaque fois qu'un sommet est dépilé, il est marqué comme visité dans notre objet visited. Ses sommets voisins sont poussés dans la pile. Puisque nous dépilons toujours un nouveau sommet adjacent, notre algorithme explorera toujours **un nouveau niveau**. 

Nous pouvons également utiliser les appels de pile intrinsèques pour implémenter DFS de manière récursive. La logique est la même.

La complexité temporelle est la même que BFS, O(V+E).

```
function DFS
   Initialiser une pile vide, un tableau 'result' vide et une carte 'visited' vide
   Ajouter le sommet de départ à la pile et à la carte visited
   Tant que la pile n'est pas vide :
     - Dépiler et stocker le sommet actuel
     - Pousser le sommet actuel dans le tableau result
     - Parcourir la liste d'adjacence du sommet actuel :
       - Pour chaque sommet adjacent, si le sommet n'est pas visité :
         - Ajouter le sommet à la carte visited
         - Empiler le sommet
   Retourner le tableau result
```

```javascript
Graph.prototype.bfs = function(start) {
    const queue = [start];
    const result = [];
    const visited = {};
    visited[start] = true;
    let currentVertex;
    while (queue.length) {
      currentVertex = queue.shift();
      result.push(currentVertex);
      this.adjacencyList[currentVertex].forEach(neighbor => {
        if (!visited[neighbor]) {
          visited[neighbor] = true;
          queue.push(neighbor);
        }
      });
    }
    return result;
}
Graph.prototype.dfsRecursive = function(start) {
    const result = [];
    const visited = {};
    const adjacencyList = this.adjacencyList;
    (function dfs(vertex){
      if (!vertex) return null;
      visited[vertex] = true;
      result.push(vertex);
      adjacencyList[vertex].forEach(neighbor => {
          if (!visited[neighbor]) {
            return dfs(neighbor);
          }
      })
    })(start);
    return result;
}
Graph.prototype.dfsIterative = function(start) {
    const result = [];
    const stack = [start];
    const visited = {};
    visited[start] = true;
    let currentVertex;
    while (stack.length) {
      currentVertex = stack.pop();
      result.push(currentVertex);
      this.adjacencyList[currentVertex].forEach(neighbor => {
        if (!visited[neighbor]) {
          visited[neighbor] = true;
          stack.push(neighbor);
        }
      });
    }
    return result;
}
```

## Recherche dans un labyrinthe

Énoncé du problème :

> Étant donné un tableau 2D d'entrées noires et blanches représentant un labyrinthe avec des points d'entrée et de sortie désignés, trouver un chemin de l'entrée à la sortie, si un tel chemin existe. – Aziz, Adnan, et al. _Elements of Programming Interviews_

Nous allons représenter les entrées blanches avec des 0 et les entrées noires avec des 1. Les entrées blanches représentent les zones ouvertes et les entrées noires les murs. Les points d'entrée et de sortie sont représentés par un tableau, l'index 0 et l'index 1 remplis avec les indices de ligne et de colonne, respectivement.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-05-30-at-7.40.29-PM.png)
_Labyrinthe représenté par un tableau 2D_

Solution :

* Pour se déplacer vers une position différente, nous allons coder en dur les quatre mouvements possibles dans le **tableau des directions** (droite, bas, gauche et haut ; pas de mouvements diagonaux) :

```
[ [0,1], [1,0], [0,-1], [-1,0] ]
```

* Pour garder une trace des cellules que nous avons déjà visitées, nous allons **remplacer** les entrées blanches (**0**) par des entrées noires (**1**). Nous utilisons essentiellement **DFS** de manière récursive pour parcourir le labyrinthe. Le cas de base, qui mettra fin à la récursion, est soit nous avons **atteint notre point de sortie et retournons vrai** soit nous avons **visité chaque entrée blanche et retournons faux**.
* Une autre chose importante à garder à l'esprit est de s'assurer que nous sommes **dans les limites du labyrinthe** tout le temps et que nous ne **procéderons** que si nous sommes **à une entrée blanche**. La **fonction isFeasible** s'en chargera.
* Complexité temporelle : O(V+E)

Pseudocode :

```
function hasPath
   Commencer au point d'entrée
   Tant que le point de sortie n'est pas atteint
     1. Se déplacer vers la cellule du haut
     2. Vérifier si la position est faisable (cellule blanche et dans les limites)
     3. Marquer la cellule comme visitée (la transformer en cellule noire)
     4. Répéter les étapes 1-3 pour les trois autres directions
```

```js
var hasPath = function(maze, start, destination) {
    maze[start[0]][start[1]] = 1;
    return searchMazeHelper(maze, start, destination);
};
function searchMazeHelper(maze, current, end) { // dfs
    if (current[0] == end[0] && current[1] == end[1]) {
        return true;
    }
    let neighborIndices, neighbor;
    // Indices : 0->haut,1->droite, 2->bas, 3->gauche 
    let directions = [ [0,1] , [1,0] , [0,-1] , [-1,0] ];
    for (const direction of directions) {
        neighborIndices = [current[0]+direction[0], current[1]+direction[1]];
        if (isFeasible(maze, neighborIndices)) {
            maze[neighborIndices[0]][neighborIndices[1]] = 1;
            if (searchMazeHelper(maze, neighborIndices, end)) {
                return true;
            }
        }
    }
    return false;
}
function isFeasible(maze, indices) {
    let x = indices[0], y = indices[1];
    return x >= 0 && x < maze.length && y >= 0 && y < maze[x].length && maze[x][y] === 0;
}
var maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
hasPath(maze, [0,4], [3,2]);
```

## Peindre une matrice booléenne

Énoncé du problème :

> _Implémenter une routine qui prend un tableau booléen A de taille n X m ainsi qu'une entrée (x, y) et inverse la couleur de la région associée à (x, y). –_ Aziz, Adnan, et al. _Elements of Programming Interviews_

Les 2 couleurs seront représentées par des 0 et des 1. 

Dans l'exemple ci-dessous, nous commençons au centre du tableau ([1,1]). Notez que depuis cette position, nous ne pouvons atteindre que la matrice triangulaire supérieure gauche. La position la plus à droite et la plus basse ne peut pas être atteinte ([2,2]). Par conséquent, à la fin du processus, c'est la seule couleur qui n'est pas inversée.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/imgonline-com-ua-twotoone-H6wQUCSVtaaILRR.jpg)
_Tableau booléen n x m avant et après l'inversion des couleurs_

Solution :

* Comme dans la question précédente, nous allons coder un tableau pour définir les 4 mouvements possibles.
* Nous allons utiliser BFS pour parcourir le graphe.
* Nous allons modifier légèrement la fonction isFeasible. Elle vérifiera toujours si la nouvelle position est dans les limites de la matrice. L'autre exigence est que la nouvelle position soit colorée de la même couleur que la position précédente. Si la nouvelle position répond aux exigences, sa couleur est inversée.
* Complexité temporelle : O(mn)

Pseudocode :

```
function flipColor
   Commencer aux coordonnées passées et stocker la couleur
   Initialiser la file
   Ajouter la position de départ à la file
   Tant que la file n'est pas vide :
     - Désenfiler et stocker la position actuelle
     - Se déplacer vers la cellule du haut
       1. Vérifier si la cellule est faisable
       2. Si faisable,
          - Inverser la couleur
          - Enfiler la cellule
       3. Répéter les étapes 1-2 pour les trois autres directions
```

```js
function flipColor(image, x, y) {
    let directions = [ [0,1] , [1,0] , [0,-1] , [-1,0] ];
    let color = image[x][y];
    let queue = [];
    image[x][y] = Number(!color);
    queue.push([x,y]);
    let currentPosition, neighbor;
    while (queue.length) {
        currentPosition = queue.shift();
        for (const direction of directions) {
            neighbor = [currentPosition[0]+direction[0], currentPosition[1]+direction[1]];
            if (isFeasible(image, neighbor, color)) {
                image[neighbor[0]][neighbor[1]] = Number(!color);
                queue.push([neighbor[0], neighbor[1]]);
            }
        }
    }
    return image;
}
function isFeasible(image, indices, color) {
    let x = indices[0], y = indices[1];
    return x >= 0 && x < image.length && y >= 0 && y < image[x].length && image[x][y] == color;
}
var image = [[1,1,1],[1,1,0],[1,0,1]];
flipColor(image,1,1);
```

## Calculer les régions enfermées

Énoncé du problème :

> _Soit A un tableau 2D dont les entrées sont soit W soit B. Écrire un programme qui prend A, et remplace tous les W qui ne peuvent pas atteindre la frontière par un B. –_ Aziz, Adnan, et al. _Elements of Programming Interviews_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1-Yjky-DB8p7ABUk3n37GXRA.png)
_Les grilles avant et après avoir été enfermées_

Solution :

* Au lieu de parcourir toutes les entrées pour trouver les entrées W enfermées, il est plus optimal de **commencer avec les entrées W de la frontière**, parcourir le graphe et **marquer les entrées W connectées**. Ces entrées marquées sont garanties de **ne pas être enfermées** puisqu'elles sont connectées à une entrée W sur la bordure du tableau. Ce prétraitement est essentiellement le **complément** de ce que le programme doit accomplir.
* Ensuite, A est parcouru à nouveau et les entrées W **non marquées** (qui seront les enfermées) sont changées en entrées **B**.
* Nous allons garder une trace des entrées W marquées et non marquées en utilisant un tableau booléen de mêmes dimensions que A. Une entrée marquée sera définie à vrai.
* Complexité temporelle : O(mn)

Pseudocode :

```
function fillSurroundedRegions
   1. Initialiser un tableau 'visited' de même longueur que le tableau d'entrée
      pré-rempli avec des valeurs 'false'
   2. Commencer avec les entrées de la frontière
   3. Si l'entrée de la frontière est une entrée W et non marquée :
         Appeler la fonction markBoundaryRegion
   4. Parcourir A et changer l'entrée W non visitée en B
function markBoundaryRegion
   Commencer avec une entrée W de la frontière
   Parcourir la grille en utilisant BFS
   Marquer les entrées faisables comme true
```

```js
function fillSurroundedRegions(board) {
    if (!board.length) {
        return;
    }
    const numRows = board.length, numCols = board[0].length;
    let visited = [];
    for (let i=0; i<numRows; i++) {
        visited.push(new Array(numCols).fill(false, 0, numCols));
    }
    for (let i=0; i<board.length; i++) {
        if (board[i][0] == 'W' && !visited[i][0]) {
            markBoundaryRegion(i, 0, board, visited);
        }
        if (board[i][board.length-1] == 'W' && !visited[i][board.length-1]) {
            markBoundaryRegion(i, board.length-1, board, visited);
        }
    }
    for (let j=0; j<board[0].length; j++) {
        if (board[0][j] == 'W' && !visited[0][j]) {
            markBoundaryRegion(0, j, board, visited);
        }
        if (board[board.length-1][j] == 'W' && !visited[board.length-1][j]) {
            markBoundaryRegion(board.length-1, j, board, visited);
        }
    }
    for (let i=1; i<board.length-1; i++) {
        for (let j=1; j<board.length-1; j++) {
            if (board[i][j] == 'W' && !visited[i][j]) {
                board[i][j] = 'B';
            }
        }
    }
    return board;
}
function markBoundaryRegion(i, j, board, visited) {
    let directions = [ [0,1] , [1,0] , [0,-1] , [-1,0] ];
    const queue = [];
    queue.push([i,j]);
    visited[i][j] = true;
    let currentPosition, neighbor;
    while (queue.length) {
        currentPosition = queue.shift();
        for (const direction of directions) {
            neighbor = [i+direction[0], j+direction[1]];
            if (isFeasible(board,visited,neighbor)) {
                visited[neighbor[0]][neighbor[1]] = true;
                queue.push(neighbor);
            }
        }
    }
}
function isFeasible(board, visited, neighbor) {
    let x = neighbor[0], y = neighbor[1];
    return x >= 0 && x < board.length && y >= 0 && y < board[x].length && board[x][y] == 'W';
}
var board = [['B','B','B','B'],['W','B','W','B'],['B','W','W','B'],['B','B','B','B']];
fillSurroundedRegions(board);
```

## Détection de blocage (Cycle dans un graphe orienté)

Énoncé du problème :

> _Un algorithme de détection de blocage utilise un graphe « wait-for » pour suivre les autres processus qu'un processus bloque actuellement. Dans un graphe wait-for, les processus sont représentés comme des nœuds, et une arête d'un processus P à 0 implique que 0 détient une ressource dont P a besoin et ainsi P attend que 0 libère son verrou sur cette ressource. Un cycle dans ce graphe implique la possibilité d'un blocage. Cela motive le problème suivant._  
> _Écrire un programme qui prend en entrée un graphe orienté et vérifie si le graphe contient un cycle. –_ Aziz, Adnan, et al. _Elements of Programming Interviews_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1-Gn3M8mF6rHb2vu4z4d36_Q.gif)
_Exemple d'un graphe wait-for (a)_

Dans le graphe wait-for ci-dessus, notre **programme de détection de blocage** détectera au moins un **cycle** et retournera vrai.

Pour cet algorithme, nous allons utiliser une implémentation légèrement différente du **graphe orienté** pour explorer d'autres structures de données. Nous l'implémentons toujours en utilisant la **liste d'adjacence** mais au lieu d'un objet (map), nous allons stocker les sommets dans un **tableau**. 

Les **processus** seront modélisés comme des **sommets** commençant par le **0ème processus**. La **dépendance** entre les processus sera modélisée comme des **arêtes** entre les sommets. Les **arêtes** (sommets adjacents) seront stockées dans une **liste chaînée**, à son tour stockée à l'index qui correspond au numéro de processus.

```js
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}
class LinkedList {
    constructor() {
        this.head = null;
    }
    insertAtHead(data) {
        let temp = new Node(data);
        temp.next = this.head;
        this.head = temp;
        return this;
    }
    getHead() {
        return this.head;
    }
}
class Graph {
    constructor(vertices) {
        this.vertices = vertices;
        this.list = [];
        for (let i=0; i<vertices; i++) {
            let temp = new LinkedList();
            this.list.push(temp);
        }
    }
    addEdge(source, destination) {
        if (source < this.vertices && destination < this.vertices) {
            this.list[source].insertAtHead(destination);
        }
        return this;
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1-ml99O-kqmyAxL73GdeAnqQ.png)
_Implémentation du graphe wait-for (a)_

Solution :

* Chaque sommet sera assigné **3 couleurs différentes** : blanc, gris et noir. Initialement, tous les sommets seront colorés en **blanc**. Lorsqu'un sommet est en cours de traitement, il sera coloré en **gris** et après traitement en **noir**.
* Utiliser la recherche en profondeur (DFS) pour parcourir le graphe.
* Si il y a une arête d'un sommet gris vers un autre sommet gris, nous avons découvert une **arête de retour** (une boucle auto-référentielle ou une arête qui se connecte à l'un de ses ancêtres), donc un **cycle** est détecté.
* Complexité temporelle : O(V+E)

Pseudocode :

```
function isDeadlocked
   Colorier tous les sommets en blanc
   Exécuter DFS sur les sommets
     1. Marquer le nœud actuel en gris
     2. Si le sommet adjacent est gris, retourner vrai
     3. Marquer le nœud actuel en noir
   Retourner faux
```

```js
const Colors = {
    WHITE: 'white', 
    GRAY: 'gray', 
    BLACK: 'black'
}
Object.freeze(Colors);
function isDeadlocked(g) {
    let color = [];
    for (let i=0; i<g.vertices; i++) {
        color[i] = Colors.WHITE;
    }
    for (let i=0; i<g.vertices; i++) {
        if (color[i] == Colors.WHITE) {
             if (detectCycle(g, i, color)) {
                return true;
             }   
        }
    }
    return false;
};
function detectCycle(g, currentVertex, color) {
    color[currentVertex] = Colors.GRAY;
    let neighbor;
    let nextNode = g.list[currentVertex].getHead();
    while (nextNode !== null) {
        neighbor = nextNode.data;
        if (color[neighbor] == Colors.GRAY) {
            return true;
        }
        if (color[neighbor] == Colors.WHITE && detectCycle(g, neighbor, color)) {
            return true;
        }
    }
    color[currentVertex] = Colors.BLACK;
    return false;
}
let g = new Graph(3);
g.addEdge(0,1);
g.addEdge(0,2);
isDeadlocked(g);
```

## Cloner un graphe

Énoncé du problème :

> _Considérons un type de sommet pour un graphe orienté dans lequel il y a deux champs : une étiquette entière et une liste de références à d'autres sommets. Concevez un algorithme qui prend une référence à un sommet u, et crée une copie du graphe sur les sommets accessibles depuis u. Retournez la copie de u. –_ Aziz, Adnan, et al. _Elements of Programming Interviews_

Solution :

* Maintenir une **carte** qui **associe le sommet original à son homologue**. Copier les arêtes.
* Utiliser BFS pour visiter les sommets adjacents (arêtes).
* Complexité temporelle : O(n), où n est le nombre total de nœuds.

Pseudocode :

```
function cloneGraph
   Initialiser une carte vide
   Exécuter BFS
   Ajouter le sommet original comme clé et le clone comme valeur à la carte
   Copier les arêtes si les sommets existent dans la carte
   Retourner le clone
```

```js
class GraphVertex {
    constructor(value) {
        this.value = value;
        this.edges = [];
    }
}
function cloneGraph(g) {
    if (g == null) {
        return null;
    }
    let vertexMap = {};
    let queue = [g];
    vertexMap[g] = new GraphVertex(g.value);
    while (queue.length) {
        let currentVertex = queue.shift();
        currentVertex.edges.forEach(v => {
            if (!vertexMap[v]) {
                vertexMap[v] = new GraphVertex(v.value);
                queue.push(v);
            }
            vertexMap[currentVertex].edges.push(vertexMap[v]);
        });
    }
    return vertexMap[g];
}
let n1 = new GraphVertex(1);
let n2 = new GraphVertex(2);
let n3 = new GraphVertex(3);
let n4 = new GraphVertex(4);
n1.edges.push(n2, n4);
n2.edges.push(n1, n3);
n3.edges.push(n2, n4);
n4.edges.push(n1, n3);
cloneGraph(n1);
```

## Établir des connexions filaires

Énoncé du problème :

> _Concevoir un algorithme qui prend un ensemble de broches et un ensemble de fils connectant des paires de broches, et détermine s'il est possible de placer certaines broches sur la moitié gauche d'un PCB, et le reste sur la moitié droite, de sorte que chaque fil soit entre les moitiés gauche et droite. Retourner une telle division, si elle existe. –_ Aziz, Adnan, et al. _Elements of Programming Interviews_

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1-Ye3P_VA_65-B708FzPCpTg.png)
_Un exemple d'une telle division_

Solution :

* Modéliser l'ensemble comme un graphe. Les broches sont représentées par les sommets et les fils qui les connectent sont les arêtes. Nous allons implémenter le graphe en utilisant une [liste d'arêtes](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).

L'appariement décrit dans l'énoncé du problème est possible seulement si les sommets (broches) peuvent être divisés en « 2 ensembles indépendants, U et V tels que chaque arête (u,v) relie soit un sommet de U à V soit un sommet de V à U. » ([Source](https://www.geeksforgeeks.org/bipartite-graph/)) Un tel graphe est connu comme un **graphe biparti**.

Pour vérifier si le graphe est biparti, nous allons utiliser la technique de **coloration de graphe**. Puisque nous avons besoin de deux ensembles de broches, nous devons vérifier si le graphe est 2-colorable (que nous allons représenter comme 0 et 1). 

Initialement, tous les sommets sont non colorés (-1). Si des sommets adjacents se voient attribuer les mêmes couleurs, alors le graphe n'est pas biparti. Il n'est pas possible d'attribuer deux couleurs alternativement à un graphe avec un cycle de longueur impaire en utilisant seulement 2 couleurs, donc nous pouvons colorier le graphe de manière gloutonne.

Étape supplémentaire : Nous allons gérer le cas d'un graphe qui n'est pas connecté. La boucle externe s'en charge en itérant sur tous les sommets.

* Complexité temporelle : O(V+E)

Pseudocode :

```
function isBipartite
   1. Initialiser un tableau pour stocker les sommets non colorés
   2. Itérer à travers tous les sommets un par un
   3. Attribuer une couleur (0) au sommet source
   4. Utiliser DFS pour atteindre les sommets adjacents
   5. Attribuer aux voisins une couleur différente (1 - couleur actuelle)
   6. Répéter les étapes 3 à 5 tant que cela satisfait la contrainte des deux couleurs
   7. Si un voisin a la même couleur que le sommet actuel, rompre la boucle et retourner faux
```

```js
function isBipartite(graph) {
    let color = [];
    for (let i=0; i<graph.length; i++) {
        color[i] = -1;
    }
    for (let i=0; i<graph.length; i++) {
        if (color[i] == -1) {
            let stack = [];
            stack.push(i);
            color[i] = 0;
            let node;
            while (stack.length) {
                node = stack.pop();
                for (const neighbor of graph[node]) {
                    if (color[neighbor] == -1) {
                        stack.push(neighbor);
                        color[neighbor] = 1 - color[node];
                    }
                    else if (color[neighbor] == color[node]) {
                        return false;
                    }
                }
            }
        }
    }
    return true;
}
isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]);
```

## Transformer une chaîne en une autre

Énoncé du problème :

> _Étant donné un dictionnaire D et deux chaînes s et f, écrire un programme pour déterminer si s produit t. Supposons que tous les caractères sont des alphabets minuscules. Si s produit f, sortir la longueur d'une séquence de production la plus courte ; sinon, sortir -1. –_ Aziz, Adnan, et al. _Elements of Programming Interviews_

Par exemple, si le dictionnaire D est ["hot", "dot", "dog", "lot", "log", "cog"], s est "hit" et t est "cog", la longueur de la séquence de production la plus courte est 5.  
"hit" -> "hot" -> "dot" -> "dog" -> "cog"

Solution :

* Représenter les **chaînes** comme des **sommets** dans un graphe non orienté et non pondéré, avec une **arête** entre 2 sommets si les chaînes correspondantes diffèrent d'**un caractère** au plus. Nous allons implémenter une fonction (compareStrings) qui calcule la différence de caractères entre deux chaînes.
* En nous appuyant sur l'exemple précédent, les sommets dans notre graphe seront

```
{hit, hot, dot, dog, lot, log, cog}
```

* Les arêtes représentées par l'approche de la liste d'adjacence que nous avons discutée dans la section 0. Implémentation de graphe, seront :

```
{
    "hit": ["hot"],
    "hot": ["dot", "lot"],
    "dot": ["hot", "dog", "lot"],
    "dog": ["dot", "lot", "cog"],
    "lot": ["hot", "dot", "log"],
    "log": ["dog", "lot", "cog"],
    "cog": ["dog", "log"]
}
```

* Une fois que nous avons fini de construire le graphe, le problème se réduit à trouver le chemin le plus court d'un nœud de départ à un nœud d'arrivée. Cela peut être calculé naturellement en utilisant la **recherche en largeur d'abord**.
* Complexité temporelle : O(M x M x N), où M est la longueur de chaque mot et N est le nombre total de mots dans le dictionnaire.

Pseudocode :

```
function compareStrings
   Comparer deux chaînes caractère par caractère
   Retourner combien de caractères diffèrent
function transformString
   1. Construire le graphe en utilisant la fonction compareStrings. Ajouter des arêtes si et seulement si les deux chaînes diffèrent d'un caractère
   2. Exécuter BFS et incrémenter la longueur
   3. Retourner la longueur de la séquence de production
```

```js
function transformString(beginWord, endWord, wordList) {
    let graph = buildGraph(wordList, beginWord);
    if (!graph.has(endWord)) return 0;
    let queue = [beginWord];
    let visited = {};
    visited[beginWord] = true;
    let count = 1;
    while (queue.length) {
        let size = queue.length;
        for (let i=0; i<size; i++) {
            let currentWord = queue.shift();
            if (currentWord === endWord) {
                return count;
            }
            graph.get(currentWord).forEach( neighbor => {
                if (!visited[neighbor]) {
                    queue.push(neighbor);
                    visited[neighbor] = true;
                }
            })
        }
        count++;
    }
    return 0;
};

function compareStrings (str1, str2) {
    let diff = 0;
    for (let i=0; i<str1.length; i++) {
        if (str1[i] !== str2[i]) diff++
    }
    return diff;
}

function buildGraph(wordList, beginWord) {
    let graph = new Map();
    wordList.forEach( (word) => {
        graph.set(word, []);
        wordList.forEach( (nextWord) => {
            if (compareStrings(word, nextWord) == 1) {
                graph.get(word).push(nextWord);
            }
        })
    })
    if (!graph.has(beginWord)) {
        graph.set(beginWord, []);
        wordList.forEach( (nextWord) => {
            if (compareStrings(beginWord, nextWord) == 1) {
                graph.get(beginWord).push(nextWord);
            }
        })
    }
    return graph;
}
```

## Où aller à partir de là ?

Espérons qu'à la fin de cet article, vous avez réalisé que la partie la plus difficile des problèmes de graphe est d'identifier comment modéliser les problèmes sous forme de graphes. À partir de là, vous pouvez utiliser/modifier les deux parcours de graphe pour obtenir la sortie attendue.

D'autres algorithmes de graphe qu'il est bon d'avoir dans votre boîte à outils sont :

* Ordonnancement topologique
* Algorithmes de chemin le plus court (Dijkstra et Floyd Warshall)
* Algorithmes d'arbres couvrant minimaux (Prim et Kruskal)

Si vous avez trouvé cet article utile, envisagez de [m'offrir un café](https://www.buymeacoffee.com/girish). Cela me tiendra éveillé lorsque je travaillerai sur un tutoriel vidéo de cet article :)                                        

### Références :

Aziz, Adnan, et al. Elements of Programming Interviews. 2nd ed., CreateSpace Independent Publishing Platform, 2012.