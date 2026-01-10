---
title: Algorithme de Prim – Expliqué avec un exemple de pseudocode
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-02-14T22:12:43.000Z'
originalURL: https://freecodecamp.org/news/prims-algorithm-explained-with-pseudocode
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/prim-cover.png
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
seo_title: Algorithme de Prim – Expliqué avec un exemple de pseudocode
seo_desc: 'In Computer Science, Prim’s algorithm helps you find the minimum spanning
  tree of a graph. It is a greedy algorithm – meaning it selects the option available
  at the moment.

  In this article, I’ll show you the pseudocode representation of Prim’s algori...'
---

En informatique, l'algorithme de Prim permet de trouver l'arbre couvrant minimal d'un graphe. C'est un algorithme glouton, ce qui signifie qu'il sélectionne l'option disponible à ce moment-là.

Dans cet article, je vais vous montrer la représentation en pseudocode de l'algorithme de Prim. Mais avant cela, examinons plus en détail ce qu'est l'algorithme de Prim.

## Ce que nous allons couvrir
- [Qu'est-ce que l'algorithme de Prim ?](#heading-quest-ce-que-lalgorithme-de-prim)
- [Comment implémenter l'algorithme de Prim](#heading-comment-implementer-lalgorithme-de-prim)
- [Exemple de pseudocode de l'algorithme de Prim](#heading-exemple-de-pseudocode-de-lalgorithme-de-prim)
- [Comment implémenter l'algorithme de Prim en JavaScript en utilisant le pseudocode](#heading-comment-implementer-lalgorithme-de-prim-en-javascript-en-utilisant-le-pseudocode)
- [Conclusion](#heading-conclusion)

## Qu'est-ce que l'algorithme de Prim ?
L'algorithme de Prim est un type d'algorithme glouton pour trouver l'arbre couvrant minimal (MST) d'un graphe non orienté et pondéré.

Un arbre couvrant minimal (MST) est un sous-ensemble des arêtes d'un graphe qui relie tous les sommets (le point où les côtés se rencontrent) ensemble de sorte que le poids total des arêtes soit minimisé sans former de cycle.

Ainsi, gardez à l'esprit que si vous trouvez le MST d'un graphe avec l'algorithme de Prim, il ne doit y avoir aucun cycle. C'est-à-dire, si A est lié à B et B est lié à C, C ne peut pas être lié à A à nouveau car cela formerait un cycle. J'ai préparé quelques infographies avec des explications qui vous aideront à mieux le comprendre dans les prochaines sections de cet article.

Le poids total des arêtes est également communément appelé `coût`. Et l'un des objectifs de l'algorithme de Prim est d'obtenir l'arbre de coût minimal qui couvre les sommets dans le graphe sans en laisser aucun derrière.

Ainsi, c'est une autre chose à garder à l'esprit : tous les sommets doivent être impliqués dans l'obtention de l'arbre couvrant minimal (MST).

L'algorithme de Prim est également appelé **algorithme de Jarník** car il a été initialement développé par le mathématicien tchèque Vojtěch Jarník en 1930. Il a été redécouvert et publié plus tard par Robert C. Prim en 1957, d'où le nom d'algorithme de Prim.

L'algorithme de Prim fonctionne en commençant par un sommet arbitraire, en ajoutant l'arête de poids minimal qui relie l'arbre à un nouveau sommet, et en répétant ce processus jusqu'à ce que tous les sommets aient été inclus dans l'arbre.

## Comment implémenter l'algorithme de Prim
Pour implémenter l'algorithme de Prim afin de trouver l'arbre couvrant minimal d'un graphe, voici les trois choses à garder à l'esprit :

- tous les sommets du graphe doivent être inclus
- le sommet avec le poids minimal doit être sélectionné en premier. Vous entendrez également certaines personnes appeler ce poids distance, mais continuons à l'appeler poids.
- tous les sommets doivent être connectés
- il ne doit y avoir aucun cycle

Considérez le graphe ci-dessous :
![start-graph](https://www.freecodecamp.org/news/content/images/2023/02/start-graph.png)

Vous devez commencer par choisir un sommet arbitraire comme point de départ et l'ajouter à l'arbre.

Pour l'étape suivante, vous devez sélectionner l'arête avec le poids minimal qui relie un sommet dans l'arbre à un sommet pas encore dans l'arbre, puis ajouter le nouveau sommet à l'arbre.

Choisir `D` comme sommet de départ a donné ceci :
![first-res](https://www.freecodecamp.org/news/content/images/2023/02/first-res.png)

Voici comment cela s'est passé :

- `D` était le point de départ

- le poids minimal suivant connecté à `D` est `2` – la ligne entre `D` et `C`. Donc, je l'ai choisi.

- en regardant le sommet `C`, le poids minimal suivant vers lui est `1` – la ligne entre `C` et `A`. Donc, je l'ai choisi comme suivant
- en regardant `A`, les lignes `2` et `4` sont connectées à lui. Nous ne pouvons pas choisir `4` car il est plus grand que `2` et il nous ramènerait au point de départ `D`. Donc, nous devons choisir `2` – la ligne reliant les sommets `A` et `B`.
- en regardant `B`, la ligne `3` le relie à `C` et la ligne `7` le relie à `E`. Nous ne pouvons pas choisir la ligne `3` car cela formerait un cycle entre `C`, `A` et `B`. Nous devrions également réfléchir à deux fois avant de choisir la ligne 7 car c'est un grand nombre. Il y a une ligne `4` reliant `C` à `G`, donc je l'ai choisie
- Sur le sommet `G`, il y a une connexion à `F` avec la ligne `1` et la ligne `3` à `E`, donc je choisirai le poids minimal qui est `1`
- À ce stade, `E` est le seul sommet non connecté. Il est possible de le connecter car cela ne formera pas de cycle à aucun moment. Donc, je l'ai connecté.

Voici la connexion étape par étape :
![the-steps](https://www.freecodecamp.org/news/content/images/2023/02/the-steps.png)

Encore une fois, voici ce à quoi tous les points ci-dessus mènent :
![first-res-1](https://www.freecodecamp.org/news/content/images/2023/02/first-res-1.png)

Le coût est la somme de tous les poids connectés aux sommets. C'est ainsi que j'ai obtenu 13.

Ce processus continue jusqu'à ce que tous les sommets aient été ajoutés à l'arbre. Il ne laisse aucun d'eux derrière et ne forme aucun cycle.

Vous pouvez faire de n'importe quel sommet le point de départ. Voici le résultat si je commence par le sommet `A` :
![second-res](https://www.freecodecamp.org/news/content/images/2023/02/second-res.png)

Et voici le résultat si je commence par le sommet `C` :
![third-res](https://www.freecodecamp.org/news/content/images/2023/02/third-res.png)

## Exemple de pseudocode de l'algorithme de Prim
Voici un exemple de pseudocode pour l'implémentation de l'algorithme de Prim. J'ai également inclus des commentaires pour que vous puissiez suivre les choses au fur et à mesure qu'elles se produisent :

```py
prim(graph):
    # Initialiser un ensemble vide pour contenir les sommets dans l'arbre couvrant minimal
    mst = empty set

    # Sélectionner le premier sommet pour commencer l'arbre
    startVertex = first vertex in graph
    mst.add(startVertex)

    # Initialiser l'ensemble des arêtes à considérer
    edges = edges connected to startVertex

    # Itérer jusqu'à ce que tous les sommets soient dans l'arbre couvrant minimal
    while mst has fewer vertices than graph:
        # Trouver l'arête minimale dans l'ensemble des arêtes
        minEdge, minWeight = findMinEdge(edges)

        # Ajouter le sommet à l'arbre couvrant minimal
        mst.add(minEdge)

        # Ajouter les arêtes connectées au sommet à l'ensemble des arêtes à considérer
        for edge in edges connected to minEdge:
            if edge is not in mst:
                edges.add(edge)

        # Retirer l'arête minimale de l'ensemble des arêtes à considérer
        edges.remove(minEdge)

    # Retourner l'arbre couvrant minimal sous forme de tableau
    return mst as an array
```

## Comment implémenter l'algorithme de Prim en JavaScript en utilisant le pseudocode
En utilisant ce pseudocode, vous pouvez implémenter l'algorithme de Prim en JavaScript de cette manière :

```js
// Définir un graphe sous forme de liste d'adjacence
const graph = {
  'A': {'B': 4, 'C': 2},
  'B': {'A': 4, 'C': 1, 'D': 5},
  'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
  'D': {'B': 5, 'C': 8, 'E': 2},
  'E': {'C': 10, 'D': 2}
};

// Trouver l'arête minimale dans la liste des arêtes
function findMinEdge(edges) {
  let minEdge = null;
  let minWeight = Infinity;
  for (const [v, weight] of Object.entries(edges)) {
    if (weight < minWeight) {
      minEdge = v;
      minWeight = weight;
    }
  }
  return [minEdge, minWeight];
}

// Trouver l'arbre couvrant minimal en utilisant l'algorithme de Prim
function prim(graph) {
  // Initialiser un ensemble vide pour contenir les sommets dans l'arbre couvrant minimal
  const mst = new Set();

  // Sélectionner le premier sommet pour commencer l'arbre
  const startVertex = Object.keys(graph)[0];
  mst.add(startVertex);

  // Initialiser l'ensemble des arêtes à considérer
  const edges = graph[startVertex];

  // Itérer sur l'objet graphe jusqu'à ce que tous les sommets soient dans l'arbre couvrant minimal
  while (mst.size < Object.keys(graph).length) {
    // Trouver l'arête minimale dans l'ensemble des arêtes
    const [minEdge, minWeight] = findMinEdge(edges);

    // Ajouter le sommet à l'arbre couvrant minimal
    mst.add(minEdge);

    // Ajouter les arêtes connectées au sommet à l'ensemble des arêtes à considérer
    for (const [v, weight] of Object.entries(graph[minEdge])) {
      if (!mst.has(v)) {
        edges[v] = weight;
      }
    }

    // Retirer l'arête minimale de l'ensemble des arêtes à considérer
    delete edges[minEdge];
  }

  // Retourner l'arbre couvrant minimal sous forme de tableau
  return Array.from(mst);
}

// Appeler la fonction prim avec l'objet graphe
const minimumSpanningTree = prim(graph);

// Afficher le résultat dans la console
console.log(minimumSpanningTree);

// Résultat : ['A', 'C', 'B', 'D', 'E']
```

## Conclusion
L'algorithme de Prim est un algorithme amusant et utile utilisé dans la vie quotidienne pour résoudre des problèmes. C'est pourquoi cet article était dédié à vous montrer ce que c'est et un exemple de pseudocode avec lequel vous pouvez l'implémenter dans n'importe quel langage.

Si vous vous demandez à quoi vous pouvez utiliser l'algorithme de Prim, voici quelques-unes de ses applications :
- conception de réseaux de transport
- construction d'arbres phylogénétiques en bioinformatique
- segmentation d'images basée sur la couleur et l'intensité des pixels
- regroupement d'objets similaires dans les algorithmes de clustering

Merci d'avoir lu.