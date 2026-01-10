---
title: 'Une Introduction en Douceur aux Structures de Données : Comment Fonctionnent
  les Graphes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-06T17:14:24.000Z'
originalURL: https://freecodecamp.org/news/a-gentle-introduction-to-data-structures-how-graphs-work-a223d9ef8837
coverImage: https://cdn-media-1.freecodecamp.org/images/1*W6BXpuuOB_WcoO4-CmJQKg.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Une Introduction en Douceur aux Structures de Données : Comment Fonctionnent
  les Graphes'
seo_desc: 'By Michael Olorunnisola

  So who wants to work at Google, Facebook, or maybe LinkedIn? Beyond their grueling
  interview process, one thing all these companies have in common is their heavy reliance
  on the graph data structure.

  After learning a bit about...'
---

Par Michael Olorunnisola

Alors, qui veut travailler chez Google, Facebook, ou peut-être LinkedIn ? Au-delà de leur processus d'entretien éprouvant, une chose que toutes ces entreprises ont en commun est leur forte dépendance à la structure de données de graphe.

Après avoir appris un peu sur les graphes, vous comprendrez pourquoi. À la fin de cet article, vous vous sentirez plus à l'aise pour plonger dans [Cracking the Coding Interview](http://amzn.to/2gZdc67) — ou un livre similaire de préparation aux entretiens — et pour résoudre quelques problèmes pratiques d'algorithmes de parcours de réseau.

### Comment Fonctionnent les Graphes

Les graphes sont une structure de données puissante et polyvalente qui permet facilement de représenter des relations réelles entre différents types de données (nœuds). Il y a deux parties principales dans un graphe :

![Image](https://cdn-media-1.freecodecamp.org/images/3MPRx8M27DX95wWbfufQ7MSAWytADyK1Nrwu)

* Les sommets (nœuds) où les données sont stockées, c'est-à-dire les nombres dans l'image à gauche
* Les arêtes (connexions) qui relient les nœuds, c'est-à-dire les lignes entre les nombres dans l'image

Les graphes peuvent être **non orientés** ou **orientés**. En utilisant le graphe ci-dessus comme exemple — et en traitant les arêtes comme des relations quotidiennes — voici la différence :

**Graphe non orienté :** Si 6 était un ami de 4, 4 serait également un ami de 6. La relation existe dans les deux sens.

**Graphe orienté :** si 6 avait un crush sur 4, cela ne signifie pas nécessairement que 4 doit avoir un crush sur 6. L'amour est difficile ?. Les relations sont basées sur la direction des arêtes. Cela peut être une relation à sens unique ou une relation à double sens, mais cela doit être explicitement indiqué.

Voici quelques opérations courantes que vous pouvez effectuer sur les graphes :

**Ajouts**

* `addNode` : ajoute des sommets à votre graphe
* `addEdge` : crée des arêtes entre deux sommets donnés dans votre graphe

**Suppressions**

* `removeNode` : supprime des sommets de votre graphe
* `removeEdge` : supprime des arêtes entre deux sommets donnés dans votre graphe

**Recherche**

* `contains` : vérifie si votre graphe contient une valeur donnée
* `hasEdge` : vérifie si une connexion existe entre deux nœuds donnés dans votre graphe

En plus de cela, les graphes peuvent être pondérés ou non pondérés. Cela signifie simplement qu'il y a une certaine valeur ou coût associé aux arêtes entre les sommets. Le meilleur exemple de cela serait Google Maps.

![Image](https://cdn-media-1.freecodecamp.org/images/uR-17IhxwS15IIbSWiL0m6c9rK7uVUugbsLE)

Comme vous pouvez le voir, il y a deux itinéraires suggérés entre Mumbai et Delhi. Mais comment un algorithme de graphe de Google saurait-il que celui en bleu est la meilleure option ? Simple. Vous donnez aux différents itinéraires (arêtes) des poids équivalents à leurs distances. Sachant cela, l'algorithme peut déduire qu'un chemin est 50 km plus court que l'autre, et probablement plus rapide.

Bien sûr, il y a d'autres facteurs pondérés comme les retards et les limites de vitesse. Mais le concept reste le même. Les graphes pondérés vous permettent de choisir le chemin le plus rapide, ou le chemin de moindre résistance (voir [Algorithme de Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)).

Comme vous pouvez le voir à partir de ces exemples, les graphes peuvent montrer presque tout type de relation avec juste des données et des arêtes. C'est pourquoi les graphes sont devenus si largement utilisés par des entreprises comme LinkedIn, Google et Facebook. Lisez simplement cet article de [Facebook](https://www.facebook.com/notes/facebook-engineering/tao-the-power-of-the-graph/10151525983993920/) sur pourquoi ils ont fait la transition en 2007 des bases de données relationnelles aux bases de données de graphes.

Maintenant que vous avez une compréhension de base de ce que sont les graphes, explorons quelques exemples.

**Cas d'Utilisation Exemples :**

* Représenter un réseau social
* Représenter des cartes
* Tuer des questions d'entretien

Ce dernier point vous appartient. Si vous vous préparez pour un entretien de codage, j'ai inclus quelques ressources supplémentaires utiles à la fin de cet article.

En attendant, essayons de créer un réseau social.

### Construire un réseau social en utilisant des graphes

Puisque Facebook a presque un monopole sur ce réseau social, que diriez-vous de créer un réseau social privé pour les développeurs ? DevBook ! Bien sûr, nous pourrions garder les choses simples et simplement créer un groupe Facebook à la place... Mais étant des développeurs de première classe qui aiment un bon défi, prenons un moment de fierté pour jeter "KISS" par la fenêtre.

![Image](https://cdn-media-1.freecodecamp.org/images/WKXkqq13eX18mxYrA0CKS6EhHS0jhwX8PsLg)

Tout d'abord, vous créez le stockage pour votre graphe. Vous réalisez qu'il y a probablement plusieurs façons de représenter une structure de données de graphe, mais pour l'instant, vous décidez d'utiliser une liste qui stockera chaque développeur unique comme une clé et toutes leurs connexions comme leurs valeurs associées. Après avoir effectué une recherche rapide sur Google, vous réalisez que vous créez une liste d'adjacence.

Vous préférez suivre un modèle fonctionnel, donc vous décidez de prendre la route ci-dessous :

```
let MakeGraph = () => {   // Fonction qui créera nos graphes  let graph = {};  return graph;}
```

```
let devBook = MakeGraph();  // Notre graphe représentant notre site
```

Maintenant que vous avez la représentation du graphe, vous devez créer un moyen d'ajouter des développeurs au graphe lorsqu'ils s'inscrivent, et de stocker toutes les connexions futures qu'ils pourraient avoir.

Vous décidez de faire des utilisateurs des clés sur l'objet, et d'utiliser un objet avec une propriété edges pour garder une liste de leurs connexions.

```
let MakeGraph = () => {     let graph = {};
```

```
  graph.addVertex = (node) => {       // ajouter des membres en tant que sommets ici     //  stocker leurs connexions en tant que propriétés sur un objet edges        graph[node] = {edges:{}};  }
```

```
  return graph;}
```

```
let devBook = MakeGraph();  
```

```
devBook.addVertex('James Gosling');devBook.addVertex('Guido Rossum');devBook.addVertex('Linus Torvalds');devBook.addVertex('Michael Olorunnisola');
```

```
// Votre graphe ressemblera maintenant à ceci :
```

```
{ addVertex: [Function],  'James Gosling': { edges: {} },  'Guido Rossum': { edges: {} },  'Linus Torvalds': { edges: {} },  'Michael Olorunnisola': { edges: {} } }
```

Notez qu'en pratique, vous voudriez stocker des enregistrements avec des identifiants d'utilisateur uniques au lieu de noms qui ne pourraient pas être écrasés par d'autres utilisateurs avec le même nom, mais j'ai utilisé les noms de programmeurs célèbres (plus le mien) pour ajouter de la saveur.

Maintenant, vous pouvez construire une méthode `contains` pour vérifier si un utilisateur a déjà été stocké sur votre graphe, et empêcher l'écrasement de toutes les relations qui sont créées à mesure que le site grandit.

```
let MakeGraph = () => {   let graph = {};
```

```
  graph.contains = (node)=> { // vous pouvez vérifier si un utilisateur existe    return !!graph[node];  }
```

```
  graph.addVertex = (node) => {     if(!graph.contains(node)){ // appeler contains pour empêcher l'écrasement      graph[node] = {edges:{}};    }  }
```

```
return graph;}
```

Super ! Maintenant que vous avez un bon ensemble d'utilisateurs uniques, vous voulez leur permettre de se connecter les uns aux autres en créant des amitiés (arêtes). Ces arêtes ne seront pas dirigées, car vous réalisez que les amitiés ne fonctionnent pas vraiment de cette manière.

```
let MakeGraph = () => {   let graph = {};
```

```
  graph.contains = (node)=> {    return !!graph[node];  }
```

```
  graph.addVertex = (node) => {      if(!graph.contains(node)){      graph[node] = {edges:{}};    }  }
```

```
  graph.addEdge = (startNode, endNode) => {    // Seulement si les deux nœuds existent    // Ajouter chaque nœud à la liste des arêtes de l'autre
```

```
    if(graph.contains(startNode) && graph.contains(endNode)){      graph[startNode].edges[endNode] = true;      graph[endNode].edges[startNode] = true;    }  } 
```

```
  return graph;}
```

```
let devBook = MakeGraph();  // Notre graphe représentant notre site
```

```
devBook.addVertex('James Gosling');devBook.addVertex('Guido Rossum');devBook.addVertex('Linus Torvalds');devBook.addVertex('Michael Olorunnisola');
```

```
// Nous allons ajouter les arêtes ici !
```

```
devBook.addEdge('James Gosling', 'Guido Rossum');devBook.addEdge('Linus Torvalds', 'Michael Olorunnisola');
```

```
// Maintenant notre devBook ressemblera à ceci :
```

```
{ contains: [Function],  addVertex: [Function],  addEdge: [Function],  'James Gosling': { edges: { 'Guido Rossum': true } },  'Guido Rossum': { edges: { 'James Gosling': true } },  'Linus Torvalds': { edges: { 'Michael Olorunnisola': true } },  'Michael Olorunnisola': { edges: { 'Linus Torvalds': true } } }
```

C'est absolument fantastique, mais à un moment donné, Linus vous contacte et dit : "Je n'ai aucune idée de qui est ce Michael. J'ai supposé qu'il était Michael Tiemann, mais j'ai finalement essayé de lire son nom de famille."

Actuellement, vous n'avez pas de moyen de supprimer une relation, alors vous vous plongez directement dans le code pour créer une méthode `removeEdge` afin de permettre à Linus de garder sa liste d'amis précise.

```
let MakeGraph = () => {   let graph = {};
```

```
  graph.contains = (node)=> {    return !!graph[node];  }
```

```
  graph.addVertex = (node) => {      if(!graph.contains(node)){      graph[node] = {edges:{}};    }  }
```

```
  graph.addEdge = (startNode, endNode) => {    if(graph.contains(startNode) && graph.contains(endNode)){      graph[startNode].edges[endNode] = true;      graph[endNode].edges[startNode] = true;    }  }    graph.removeEdge = (startNode, endNode) => {    if(graph.contains(startNode) && graph.contains(endNode)){      delete graph[startNode].edges[endNode]      delete graph[endNode].edges[startNode]    }  }
```

```
  return graph;}
```

```
devBook.removeEdge('Linus Torvalds', 'Michael Olorunnisola');
```

```
// Relation supprimée !
```

```
{ contains: [Function],  addVertex: [Function],  addEdge: [Function],  removeEdge: [Function],  'James Gosling': { edges: { 'Guido Rossum': true } },  'Guido Rossum': { edges: { 'James Gosling': true } },  'Linus Torvalds': { edges: {} },  'Michael Olorunnisola': { edges: {} } }
```

Super ! Malheureusement, Linus dit qu'il voulait juste essayer le site, mais qu'il est trop ermite pour être sur un site comme celui-ci. Il veut vraiment supprimer son compte, mais ne peut pas actuellement car vous n'avez pas encore ajouté de méthode de suppression de nœud.

```
let MakeGraph = () => {   let graph = {};
```

```
  graph.contains = (node)=> {    return !!graph[node];  }
```

```
  graph.addVertex = (node) => {      if(!graph.contains(node)){      graph[node] = {edges:{}};    }  }
```

```
  graph.removeVertex = (node) => {    if(graph.contains(node)) {    // Nous devons supprimer toutes les arêtes existantes du nœud      for(let connectedNode in graph[node].edges) {        graph.removeEdge(node, connectedNode);      }      delete graph[node];    }
```

```
  }
```

```
  graph.addEdge = (startNode, endNode) => {    if(graph.contains(startNode) && graph.contains(endNode)){      graph[startNode].edges[endNode] = true;      graph[endNode].edges[startNode] = true;    }  }    graph.removeEdge = (startNode, endNode) => {    if(graph.contains(startNode) && graph.contains(endNode)){      delete graph[startNode].edges[endNode]      delete graph[endNode].edges[startNode]    }  }
```

```
return graph;}
```

```
// Maintenant nous pouvons supprimer des utilisateurs !
```

```
devBook.removeVertex('Linus Torvalds');
```

Excellent travail ! Bien que vous ayez perdu un utilisateur potentiellement précieux, vous avez été en mesure de mettre en œuvre un système de graphe de base pour garder une trace de tous vos utilisateurs et de leurs amitiés.

Si vous remarquez, nous n'avons pas implémenté la méthode `hasEdge`, mais je pense que vous avez assez d'informations pour essayer ! N'hésitez pas à inclure votre implémentation dans les commentaires ci-dessous ?.

### Une analyse de la complexité temporelle des méthodes de graphe en tant que liste d'adjacence

Voici notre code à nouveau :

```
let MakeGraph = () => {   let graph = {};
```

```
  graph.contains = (node)=> {    return !!graph[node];  }
```

```
  graph.addVertex = (node) => {      if(!graph.contains(node)){      graph[node] = {edges:{}};    }  }
```

```
  graph.removeVertex = (node) => {    if(graph.contains(node)) {      for(let connectedNode in graph[node].edges) {        graph.removeEdge(node, connectedNode);      }      delete graph[node];    }  }
```

```
  graph.addEdge = (startNode, endNode) => {    if(graph.contains(startNode) && graph.contains(endNode)){      graph[startNode].edges[endNode] = true;      graph[endNode].edges[startNode] = true;    }  }    graph.removeEdge = (startNode, endNode) => {    if(graph.contains(startNode) && graph.contains(endNode)){      delete graph[startNode].edges[endNode]      delete graph[endNode].edges[startNode]    }  }
```

```
  return graph;}
```

`addNode` est **O(1)** : Vous créez simplement une propriété sur un objet, donc c'est un temps constant.

`addEdge` est **O(1)** : Puisque vous utilisez un objet pour représenter votre graphe, c'est une opération en temps constant puisque vos nœuds et arêtes sont représentés comme des propriétés.

`removeNode` est **O(n)** : Si un nœud a des arêtes, vous devrez itérer sur toutes ses arêtes existantes pour supprimer son existence en tant qu'arête sur ses nœuds connectés.

`removeEdge` est **O(1)** : Puisque vos nœuds sont des propriétés sur votre graphe, vous pouvez y accéder en temps constant et simplement supprimer les arêtes qui sont également accessibles en temps constant.

`contains` est **O(1)** : En tant que propriété sur votre graphe, c'est une recherche en temps constant pour un nœud.

`hasEdge` est **O(1)** : Les deux nœuds seraient des propriétés sur votre graphe, donc ce serait une recherche en temps constant.

### Temps pour un rapide récapitulatif

Graphes :

1. ne sont qu'une combinaison de sommets et d'arêtes représentant des données et des relations
2. ont des méthodes `addNode`, `addEdge`, `removeNode` et `removeEdge` pour gérer leur contenu
3. ont une méthode `contains` et une méthode `hasEdge` pour vous aider à suivre l'état de leur état

### Lectures Complémentaires

Dire qu'il y a beaucoup plus à dire sur la structure de données de graphe serait un énorme euphémisme.

Vous auriez pu représenter les arêtes comme un tableau au lieu d'objets, ou le graphe entier comme un tableau 2-d ([matrice d'adjacence](https://en.wikipedia.org/wiki/Adjacency_matrix)). Vous auriez même pu représenter le graphe uniquement par leurs arêtes dans un tableau ([liste d'arêtes](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs)).

Comme pour tout en programmation, il y a des compromis associés à chaque représentation et il est définitivement utile d'apprendre ce qu'ils sont.

Les graphes sont de loin ma structure de données préférée et aussi l'une des plus polyvalentes, mais ce n'est que mon humble opinion. ([Ceux d'entre vous qui aiment les arbres sont vraiment des amateurs de graphes déguisés](http://freefeast.info/difference-between/difference-between-trees-and-graphs-trees-vs-graphs/) ?).

Peut-être que je peux vous convaincre de les aimer autant que moi, alors voici quelques ressources supplémentaires pour vous documenter :

* Cet [article Wikipedia](https://en.wikibooks.org/wiki/Data_Structures/Graphs) fait un excellent travail non seulement en couvrant les différentes représentations d'un graphe, mais aussi en vous introduisant à certains des algorithmes souvent associés aux graphes.
* Pour ceux d'entre vous qui utilisent Python, voici une [implémentation de graphe](https://www.python.org/doc/essays/graphs/) de l'équipe Python !
* [TutorialsPoint](https://www.tutorialspoint.com/data_structures_algorithms/graph_data_structure.htm) fait un très bon travail en plongeant dans la manière d'implémenter deux des algorithmes : [Recherche en Profondeur](https://www.youtube.com/watch?v=fI6X6IBkzcw) et [Recherche en Largeur](https://www.youtube.com/watch?v=pyNl0ESkH24). Vous pourriez être confronté à ces algorithmes de graphe lors d'entretiens.
* Keith Woods fait un excellent travail en expliquant comment implémenter un moteur de recommandation avec une structure de données de graphe [ici](https://medium.com/@keithwhor/using-graph-theory-to-build-a-simple-recommendation-engine-in-javascript-ec43394b35a3#.8qp8ly4tv). Définitivement à lire, car il implémente beaucoup des concepts que nous n'avons pas abordés ici.
* Pour ceux d'entre vous qui sont familiers avec les bases de données relationnelles comme MySQL — il y a une base de données de graphes [Neo4j](https://neo4j.com/), que j'adore absolument, qui non seulement utilise une syntaxe similaire à SQL, mais a une interface utilisateur graphique géniale [interface utilisateur graphique](https://youtu.be/Go3P73-KV30?t=2253).