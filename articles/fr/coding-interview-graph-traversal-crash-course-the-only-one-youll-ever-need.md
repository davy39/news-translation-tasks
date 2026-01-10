---
title: Cours accéléré sur le parcours de graphes pour les entretiens de codage – Le
  seul dont vous aurez jamais besoin
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-09-09T17:24:25.000Z'
originalURL: https://freecodecamp.org/news/coding-interview-graph-traversal-crash-course-the-only-one-youll-ever-need
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Coding-Interview-Series-1-.png
tags:
- name: algorithms
  slug: algorithms
- name: coding interview
  slug: coding-interview
seo_title: Cours accéléré sur le parcours de graphes pour les entretiens de codage
  – Le seul dont vous aurez jamais besoin
seo_desc: 'Are you preparing for coding interviews? I designed a crash course series
  to help you out.

  I''m Lynn, a software engineer and a recent graduate from the University of Chicago.
  This is the third course in my Coding Interview Crash Course Series. Feel f...'
---

Vous préparez-vous pour des entretiens de codage ? J'ai conçu une série de cours accélérés pour vous aider.

Je m'appelle Lynn, je suis ingénieure logicielle et diplômée récente de l'Université de Chicago. Il s'agit du troisième cours de ma série de cours accélérés sur les entretiens de codage. N'hésitez pas à consulter [ma chaîne YouTube, Lynn's DevLab](https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw), pour rester informé de cette série.

Ce cours accéléré porte sur le **parcours de graphes**. Si vous voulez plonger directement dans le sujet, vous pouvez trouver le cours ici (et lié en bas de cet article). Si vous voulez plus d'informations, continuez votre lecture. 😊

%[https://youtu.be/d31vGF-Z69c]

## Introduction

Nous allons couvrir deux techniques courantes de parcours de graphes : la **recherche en profondeur (DFS)** et la **recherche en largeur (BFS)**.

Nous allons d'abord apprendre comment elles fonctionnent et comment les implémenter en code. Ensuite, nous verrons les algorithmes en action en résolvant un problème LeetCode ainsi qu'en examinant comment j'ai appliqué le parcours de graphes lors de l'implémentation d'un algorithme pour mon jeu, [**Clicky Galaxy**](https://github.com/RuolinZheng08/unity-clicky-galaxy) (également mon premier jeu en Unity lorsque j'apprenais Unity 😉).

![Image](https://www.freecodecamp.org/news/content/images/2021/08/clicky.gif align="left")

*Clicky Galaxy, un jeu que j'ai créé en apprenant Unity*

## Plan du cours

[Cette vidéo de cours](https://youtu.be/d31vGF-Z69c) dure 1 heure et comprend :

* Une description de haut niveau des graphes, DFS et BFS

* Implémentation de DFS

* Implémentation de BFS

* Comment trouver un chemin entre un nœud source et un nœud de destination

* Démo LeetCode : 785. Le graphe est-il bipartite ?

* Démo Clicky Galaxy et parcours de graphes en Unity C# 🚀

Les graphes sont un sujet d'entretien préféré parmi les grandes entreprises technologiques comme Google, Microsoft et Facebook. Plus important encore, c'est aussi amusant et utile en ingénierie logicielle pratique comme le développement de jeux. Travaillons ensemble sur ce sujet dans mon cours !

## Définition d'un graphe

Nous utiliserons le graphe suivant pour montrer le chemin de parcours pour les deux algorithmes de parcours.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screen-Shot-2021-08-21-at-08.41.06.png align="left")

Nous pouvons représenter le graphe en mappant chaque nœud à sa liste de voisins, comme montré dans cet extrait Python :

```python
graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}
```

## Comment utiliser la recherche en profondeur (DFS)

Comme son nom l'indique, DFS privilégie la profondeur dans sa recherche.

Pour un nœud donné (par exemple 1), après avoir visité l'un de ses voisins (par exemple 0), au lieu de visiter immédiatement le reste des voisins (nœuds 2, 3 et 4), il met en cache ces voisins et reprend immédiatement sa visite sur les voisins de 0. Ce n'est que lorsqu'il a épuisé la profondeur qu'il revient à ces voisins mis en cache.

### Implémentation itérative

```python
def dfs(graph, start):
  visited, stack = set(), [start]
  while stack:
    node = stack.pop()
    if not node in visited:
        # effectuer certaines opérations sur le nœud
        # par exemple, nous affichons le nœud
        print('Visite de', node)
    visited.add(node)
    for neighbor in graph[node]:
      if not neighbor in visited:
        stack.append(neighbor)
  return visited
```

Dans ce modèle, les lignes commentées sont l'endroit où nous pouvons effectuer certaines opérations sur le nœud : par exemple, afficher sa valeur, vérifier l'égalité, etc.

Nous gardons une trace d'un ensemble nommé **visited** pour éviter de visiter le même nœud plusieurs fois où il y a un cycle dans le graphe, comme dans notre exemple de graphe ci-dessus.

L'exécution de ce code sur le graphe que nous avons défini ci-dessus donne le résultat suivant :

```python
Visite de 0
Visite de 4
Visite de 3
Visite de 2
Visite de 1
```

## Comment utiliser la recherche en largeur (BFS)

BFS privilégie la largeur dans sa recherche. Pour un nœud donné, il visite tous ses voisins immédiats avant de passer aux voisins des voisins.

### Implémentation itérative

```python
def bfs(graph, start):
  visited, queue = set(), deque([start])
  while queue:
    node = queue.popleft()
    if not node in visited:
        # effectuer certaines opérations sur le nœud
        print('Visite de', node)
    visited.add(node)
    for neighbor in graph[node]:
      if not neighbor in visited:
          queue.append(neighbor)
  return visited
```

L'exécution de ce code sur le graphe que nous avons défini ci-dessus donne le résultat suivant :

```python
Visite de 0
Visite de 1
Visite de 4
Visite de 2
Visite de 3
```

## Comment trouver un chemin entre une source et une destination

Maintenant que nous avons vu comment utiliser DFS et BFS pour parcourir l'ensemble du graphe et afficher tout l'historique de parcours, nous pouvons apporter quelques petites modifications aux modèles pour trouver un **chemin** entre deux nœuds quelconques du graphe (si un tel chemin existe).

Dans un graphe où chaque arête a le même poids, BFS est équivalent à l'**algorithme du plus court chemin de Dijkstra**. Il trouve le chemin le plus court (chemin avec le moins de nœuds) entre un nœud source et un nœud de destination. Il s'agit d'une propriété intéressante que la recherche de chemin avec DFS n'a pas.

Voici comment nous adaptons le modèle DFS pour retourner un chemin donné un nœud **src** et un nœud **dst** :

```python
def dfs_path(graph, src, dst):
  stack = [(src, [src])]
  visited = set()
  while stack:
    node, path = stack.pop()
    if node in visited:
      continue
    if node == dst:
      return path
    visited.add(node)
    for neighbor in graph[node]:
      stack.append((neighbor, path + [neighbor]))
  return None
```

De même pour BFS :

```python
def bfs_path(graph, src, dst):
  visited, queue = set(), deque([[src]])
  while queue:
    path = queue.popleft()
    node = path[-1]
    if node in visited:
      continue
    if node == dst:
      return path
    for neighbor in graph[node]:
      queue.append(path + [neighbor])
  return None
```

## Résolvons un problème LeetCode !

Appliquons maintenant ce que nous avons appris sur le parcours de graphes pour résoudre un problème sur [LeetCode, 785. Le graphe est-il bipartite ?](https://leetcode.com/problems/is-graph-bipartite/)

Selon [cet article](https://www.geeksforgeeks.org/bipartite-graph/), un algorithme BFS modifié est tout ce dont nous avons besoin :

> Voici un algorithme simple pour déterminer si un graphe donné est bipartite ou non en utilisant la recherche en largeur (BFS).
>
> 1. Assigner la couleur ROUGE au sommet source (le mettre dans l'ensemble U).
>
> 2. Colorier tous les voisins avec la couleur BLEUE (les mettre dans l'ensemble V).
>
> 3. Colorier tous les voisins des voisins avec la couleur ROUGE (les mettre dans l'ensemble U).
>
> 4. De cette manière, assigner une couleur à tous les sommets de sorte qu'elle satisfasse toutes les contraintes du problème de coloration à m voies où m = 2.
>
> 5. Lors de l'assignation des couleurs, si nous trouvons un voisin qui est coloré avec la même couleur que le sommet actuel, alors le graphe ne peut pas être coloré avec 2 sommets (ou le graphe n'est pas bipartite)
>

En insérant notre modèle, la solution est aussi simple que ce qui suit. Consultez [ma vidéo](https://youtu.be/d31vGF-Z69c) pour une explication ligne par ligne.

```python
RED = 0
BLUE = 1
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return False
        queue, visited = deque([]), set()
        for v in range(len(graph)):
            if v in visited:
                continue
            queue.append(v)
            node_colors = {v: RED}
            while queue:
                node = queue.popleft()
                visited.add(node)
                my_color = node_colors[node]
                for neighbor in graph[node]:
                    if neighbor in node_colors and node_colors[neighbor] == my_color:
                        return False
                    if not neighbor in visited:
                        queue.append(neighbor)
                    node_colors[neighbor] = RED if my_color == BLUE else BLUE

        return True
```

## Parcours de graphes en action : Clicky Galaxy, un jeu que j'ai créé

Une autre démonstration amusante sur le parcours de graphes : Clicky Galaxy 🚀, un jeu de type "match-three" que j'ai créé lorsque j'apprenais Unity.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/clicky.png align="left")

Dans le jeu, vous déplacez une planète vers une cellule vide et vous marquez des points lorsque trois planètes identiques ou plus sont alignées horizontalement ou verticalement. Une planète ne peut se déplacer que horizontalement ou verticalement, et son chemin de déplacement ne peut pas être obstrué par d'autres planètes.

J'ai appliqué le parcours de graphes pour vérifier s'il existe un chemin valide entre la planète sur laquelle le joueur a cliqué et la cellule de destination afin de déterminer si la planète peut se déplacer vers cette cellule.

Chaque cellule de la grille est un nœud et a quatre voisins immédiats : haut, bas, gauche et droite. Comme je veux trouver un chemin court entre la source et la destination (si un chemin existe), la **recherche de chemin BFS** est idéale pour mon cas d'utilisation.

Voici à quoi ressemble mon code en C#. J'ai utilisé un helper nommé **GetNeighbors** pour obtenir les quatre voisins immédiats, en ignorant ceux qui sont hors limites.

```csharp
List<Vector2Int> BreadthFirstSearch(Vector2Int srcIndices, Vector2Int dstIndices) {
    // identifier un chemin de srcIndices à dstIndices, peut être null
    // le chemin inclut src et dst
    HashSet<Vector2Int> visited = new HashSet<Vector2Int>();
    Queue<List<Vector2Int>> pathQueue = new Queue<List<Vector2Int>>();

    List<Vector2Int> startPath = new List<Vector2Int>();
    startPath.Add(srcIndices);
    pathQueue.Enqueue(startPath);

    while (pathQueue.Count > 0) {
        List<Vector2Int> path = pathQueue.Dequeue();
        Vector2Int node = path[path.Count - 1];
        if (visited.Contains(node)) {
            continue;
        }
        if (node == dstIndices) { // terminé
            return path;
        }
        visited.Add(node);
        List<Vector2Int> neighbors = GetNeighbors(node);
        foreach (Vector2Int neighbor in neighbors) {
            Sprite sprite = GetSpriteAtIndices(neighbor.x, neighbor.y);
            if (sprite == null) { // peut visiter ceci ensuite
                List<Vector2Int> newPath = new List<Vector2Int>(path);
                newPath.Add(neighbor);
                pathQueue.Enqueue(newPath);
            }
        }
    }

    return null;
}

List<Vector2Int> GetNeighbors(Vector2Int indices) {
    // retourner les quatre voisins immédiats, gauche, droite, haut, bas
    List<Vector2Int> neighbors = new List<Vector2Int>();
    if (indices.x >= 0 && indices.x < gridDimension && indices.y >= 0 && indices.y < gridDimension) {
        if (indices.y >= 1) {
            neighbors.Add(new Vector2Int(indices.x, indices.y - 1));
        }
        if (indices.y < gridDimension - 1) {
            neighbors.Add(new Vector2Int(indices.x, indices.y + 1));
        }
        if (indices.x >= 1) {
            neighbors.Add(new Vector2Int(indices.x - 1, indices.y));
        }
        if (indices.x < gridDimension - 1) {
            neighbors.Add(new Vector2Int(indices.x + 1, indices.y));
        }
    }
    return neighbors;
}
```

Et mon jeu s'est vraiment bien assemblé avec cet algorithme !

![Image](https://www.freecodecamp.org/news/content/images/2021/08/clicky-1.gif align="left")

## Réflexions finales

Dans ce cours accéléré, nous avons appris les deux algorithmes de parcours de graphes, DFS et BFS. Nous les avons vus en implémentation d'abord, puis en action dans un problème LeetCode ainsi que dans mon jeu.

Si vous avez aimé les graphes, réfléchissez à la manière dont ils se rapportent aux arbres. Alerte spoiler ! Le parcours pré-ordre dans les arbres est essentiellement DFS dans les graphes et le parcours niveau par niveau dans les arbres est essentiellement BFS dans les graphes. 🤓

Essayez de comprendre cela par vous-même ou regardez [mon cours accéléré sur le parcours d'arbres](https://youtu.be/uaeCfsCcYWo) pour un rappel. Faites-moi confiance, les algorithmes peuvent être amusants ! 😃

## Ressources

Regardez le cours ici :

%[https://youtu.be/d31vGF-Z69c]

Accédez au modèle de code sur mon GitHub :

%[https://gist.github.com/RuolinZheng08/a86a3940a23d653bae4d5c399c06639e]

Découvrez Clicky Galaxy sur mon GitHub :

%[https://github.com/RuolinZheng08/unity-clicky-galaxy]

Restez à jour avec toute la série de cours accélérés :

%[https://youtube.com/playlist?list=PLKcjA7XxXuvSsE-_heuBxIvzWcx4IKfXD]

Et enfin, n'hésitez pas à vous abonner à ma chaîne YouTube pour plus de contenu comme celui-ci :)

%[https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw]