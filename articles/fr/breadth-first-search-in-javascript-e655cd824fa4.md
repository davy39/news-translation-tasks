---
title: Recherche en Largeur en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-27T05:14:58.000Z'
originalURL: https://freecodecamp.org/news/breadth-first-search-in-javascript-e655cd824fa4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jbxv9JK2OS55gbMHKV_j0g.jpeg
tags:
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Recherche en Largeur en JavaScript
seo_desc: 'By Jennifer Bland

  In JavaScript programming, data can be stored in data structures like graphs and
  trees. Technically trees are graphs.

  Graph Data Structures

  Graphs evolved from the field of mathematics. They are primarily used to describe
  a model th...'
---

Par Jennifer Bland

En programmation JavaScript, les données peuvent être stockées dans des structures de données comme les graphes et les arbres. Techniquement, les arbres sont des graphes.

### Structures de Données de Graphe

Les graphes proviennent du domaine des mathématiques. Ils sont principalement utilisés pour décrire un modèle qui montre le chemin d'un emplacement à un autre.

Un graphe se compose d'un ensemble de nœuds et d'un ensemble d'arêtes. Une arête est une paire de nœuds qui sont connectés. Un chemin est le terme utilisé pour décrire le déplacement entre des nœuds qui partagent une arête. L'image ci-dessous montre un graphe avec 3 nœuds et 3 arêtes.

![Image](https://cdn-media-1.freecodecamp.org/images/tjwuoz34rL2Ry4bldfjJZwbqwsmQhiJ6RfWL)

### Structure de Données d'Arbre

Une structure de données d'arbre, comme un graphe, est une collection de nœuds. Il y a un nœud racine. Le nœud peut alors avoir des nœuds enfants. Les nœuds enfants peuvent avoir leurs propres nœuds enfants appelés nœuds petits-enfants.

Ce processus se répète jusqu'à ce que toutes les données soient représentées dans la structure de données d'arbre. L'image ci-dessous montre une structure de données d'arbre.

![Image](https://cdn-media-1.freecodecamp.org/images/birsxiv7XJOHl09rsFYM50oIvw3ezByuveng)

Un arbre est un graphe qui n'a pas de cycles (un cycle étant un chemin dans le graphe qui commence et se termine au même sommet). Un nœud enfant ne peut avoir qu'un seul parent. Pour cette raison, les arbres ne sont pas une structure de données récursive.

### Pourquoi Utiliser des Graphes et des Arbres comme Structures de Données ?

En programmation informatique, les arbres sont utilisés tout le temps pour définir des structures de données. Ils sont également utilisés comme base pour des algorithmes afin de résoudre des problèmes.

Les implémentations les plus courantes d'un graphe sont la recherche d'un chemin entre deux nœuds, la recherche du chemin le plus court d'un nœud à un autre et la recherche du chemin le plus court qui visite tous les nœuds.

Le problème du voyageur de commerce est un excellent exemple d'utilisation d'un algorithme d'arbre pour résoudre un problème.

### Recherche de Données

Maintenant que vous comprenez la différence entre les deux structures de données, je vais vous montrer comment vous pouvez rechercher dans vos données.

Les deux méthodes les plus courantes pour rechercher dans un graphe ou un arbre sont la recherche en profondeur et la recherche en largeur.

Que vous utilisiez une recherche en profondeur ou une recherche en largeur doit être déterminé par le type de données contenues dans votre structure de données d'arbre ou de graphe.

### Recherche en Largeur

Voici un exemple d'arbre que nous voulons rechercher en utilisant une recherche en largeur.

![Image](https://cdn-media-1.freecodecamp.org/images/ju4E5iTF4ndvO1EvrfB3slcUdRs0DJAeMji1)

Dans une recherche en largeur, vous commencez par le nœud racine. Vous recherchez ensuite tous leurs nœuds enfants en vous déplaçant de gauche à droite. Une fois que tous les nœuds enfants ont été recherchés, le processus est répété au niveau inférieur du nœud racine.

Ce processus est répété à chaque niveau jusqu'à ce que vous atteigniez la fin de l'arbre ou que vous atteigniez le nœud que vous recherchiez initialement. L'image ci-dessous montre l'ordre dans lequel vous rechercherez un arbre dans une recherche en largeur.

![Image](https://cdn-media-1.freecodecamp.org/images/-6DAOSv8PssZ5GoEXHXWBFY-DVxhDmXbnppf)

Pour implémenter une recherche en largeur, vous avez besoin d'un moyen de garder une trace des nœuds que vous devez rechercher ensuite une fois que vous avez terminé la recherche au niveau actuel.

Pour garder une trace des nœuds qui doivent être recherchés ensuite, vous utiliserez une file d'attente comme étape intermédiaire dans la recherche. Une file d'attente est un tableau FIFO (premier entré, premier sorti).

Pour démontrer comment cela fonctionne, laissez-moi vous guider à travers la recherche du Niveau 1 et du Niveau 2 dans l'image ci-dessus.

Le premier nœud à être recherché est le nœud racine ou le Nœud A. Vous mettriez le Nœud A comme premier élément dans votre file d'attente. Vous répétrez ensuite ces étapes jusqu'à ce que votre file d'attente soit vide.

![Image](https://cdn-media-1.freecodecamp.org/images/X3nfb1wrptBGw2MVwpAlPhWGUXjKnX-hCNPj)

1. Prenez le premier nœud de la file d'attente et voyez s'il correspond à votre élément de recherche.
2. Ajoutez tous les enfants du nœud à la file d'attente temporaire.

Après l'étape 2 de votre recherche, votre file d'attente contiendra maintenant tous les enfants du Nœud A.

![Image](https://cdn-media-1.freecodecamp.org/images/wktEODI9Na9uIyVtxW8nAk4CuG2f41A3F44j)

Nous comparons maintenant le Nœud B pour voir s'il correspond à nos résultats de recherche. S'il ne correspond pas, il est retiré de la file d'attente, ne laissant que le nœud H. Nous ajoutons ensuite les enfants du Nœud B dans la file d'attente.

![Image](https://cdn-media-1.freecodecamp.org/images/SlAqrajhJmA8aRT3cgX28Pz-2YcZJl4n87jk)

Ce processus continue jusqu'à ce que tous les nœuds aient été recherchés ou que vous trouviez le nœud qui correspond à vos critères de recherche.

### Plus d'Articles

Merci d'avoir lu mon article. Si vous l'aimez, veuillez cliquer sur l'icône d'applaudissements ci-dessous afin que d'autres puissent trouver l'article. Voici quelques-uns de mes autres articles qui pourraient vous intéresser :

[Instantiation Patterns in JavaScript](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)
[Why Company Culture is Important to Your Career as a Software Engineer](https://medium.com/@ratracegrad/why-company-culture-is-important-to-your-career-as-a-software-engineer-5a590bc44621)
[Using Node.js & Express.js to save data to MongoDB Database](https://medium.com/@ratracegrad/hitchhikers-guide-to-back-end-development-with-examples-3f97c70e0073)