---
title: Trouver le plus court chemin entre deux points sur un graphe avec l'algorithme
  de Dijkstra
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T21:29:00.000Z'
originalURL: https://freecodecamp.org/news/find-the-shortest-path-between-two-points-on-a-graph-with-dijkstras-algorithm
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df6740569d1a4ca3aa2.jpg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
seo_title: Trouver le plus court chemin entre deux points sur un graphe avec l'algorithme
  de Dijkstra
seo_desc: "Finding the shortest path between two points on a graph is a common problem\
  \ in data structures, especially when dealing with optimization. \nA graph is a\
  \ series of nodes connected by edges. Graphs can be weighted (edges carry values)\
  \ and directional (..."
---

Trouver le plus court chemin entre deux points sur un graphe est un problème courant dans les structures de données, surtout lorsqu'il s'agit d'optimisation. 

Un graphe est une série de nœuds connectés par des arêtes. Les graphes peuvent être pondérés (les arêtes portent des valeurs) et directionnels (les arêtes ont une direction).

Certaines applications de cela sont l'optimisation des trajectoires de vol ou [les 6 degrés de Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon).

## **Algorithme de Dijkstra**

La solution la plus courante pour ce problème est l'algorithme de Dijkstra qui met à jour le plus court chemin entre le nœud actuel et tous ses voisins. 

Après avoir mis à jour la distance de tous les voisins, il se déplace vers le nœud avec la distance la plus faible et répète le processus avec tous les voisins non visités. Ce processus continue jusqu'à ce que tout le graphe ait été visité.

![Image des niveaux de code](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

### Étape 0 :

Notre graphe doit être configuré de manière à pouvoir enregistrer les valeurs requises. Sur toute arête, nous avons la distance entre les deux nœuds qu'elle connecte. Sur tout nœud, nous avons sa distance la plus courte par rapport au nœud de départ. 

Définissons la valeur de chaque nœud à l'infini positif et définissons la valeur du nœud de départ à zéro.

### Étape 1 :

Regardons tous les nœuds directement adjacents au nœud de départ. Les valeurs portées par les arêtes connectant le départ et ces nœuds adjacents sont les distances les plus courtes vers chaque nœud respectif. 

Enregistrons ces distances sur le nœud - en écrasant l'infini - et barrons également les nœuds, ce qui signifie que leur plus court chemin a été trouvé.

### Étape 2 :

Sélectionnons l'un des nœuds dont le plus court chemin a été calculé, nous l'appellerons notre pivot. Regardons les nœuds adjacents à celui-ci (nous les appellerons nos nœuds de destination) et les distances qui les séparent. 

Pour chaque nœud de destination : 

* Si la valeur du pivot plus la valeur de l'arête qui les connecte totalise moins que la valeur du nœud de destination, alors mettez à jour sa valeur, car un nouveau chemin plus court a été trouvé. 
* Si toutes les routes vers ce nœud de destination ont été explorées, il peut être barré.

### Étape 3 :

Répétez l'étape 2 jusqu'à ce que tous les nœuds aient été barrés. Nous avons maintenant un graphe où les valeurs contenues dans chaque nœud seront la distance la plus courte par rapport au nœud de départ.

#### **Plus d'informations :**

[Plus sur l'algorithme de Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[Autres algorithmes de plus court chemin](https://en.wikipedia.org/wiki/Shortest_path_problem#Algorithms)