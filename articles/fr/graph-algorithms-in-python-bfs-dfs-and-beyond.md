---
title: 'Algorithmes de Graphes en Python : BFS, DFS et au-delà'
subtitle: ''
author: Oyedele Tioluwani
co_authors: []
series: null
date: '2025-09-03T16:25:04.388Z'
originalURL: https://freecodecamp.org/news/graph-algorithms-in-python-bfs-dfs-and-beyond
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1756916679855/9b173128-ed79-4ae0-8cc8-79fca17662dd.png
tags:
- name: Python
  slug: python
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: graphs
  slug: graphs
seo_title: 'Algorithmes de Graphes en Python : BFS, DFS et au-delà'
seo_desc: 'Have you ever wondered how Google Maps finds the fastest route or how Netflix
  recommends what to watch? Graph algorithms are behind these decisions.

  Graphs, made up of nodes (points) and edges (connections), are one of the most powerful
  data structur...'
---

Vous êtes-vous déjà demandé comment Google Maps trouve l'itinéraire le plus rapide ou comment Netflix recommande ce qu'il faut regarder ? Les algorithmes de graphes sont derrière ces décisions.

Les graphes, composés de nœuds (points) et d'arêtes (connexions), sont l'une des structures de données les plus puissantes en informatique. Ils aident à modéliser les relations de manière efficace, des réseaux sociaux aux systèmes de transport.

Dans ce guide, nous explorerons deux techniques de parcours fondamentales : le parcours en largeur (Breadth-First Search - BFS) et le parcours en profondeur (Depth-First Search - DFS). Ensuite, nous aborderons des algorithmes avancés comme Dijkstra, A\*, Kruskal, Prim et Bellman-Ford.

### Table des matières :

1. [Comprendre les graphes en Python](#heading-comprendre-les-graphes-en-python)
    
2. [Façons de représenter les graphes en Python](#heading-facons-de-representer-les-graphes-en-python)
    
3. [Parcours en largeur (BFS)](#heading-parcours-en-largeur-bfs)
    
4. [Parcours en profondeur (DFS)](#heading-parcours-en-profondeur-dfs)
    
5. [Algorithme de Dijkstra](#heading-algorithme-de-dijkstra)
    
6. [Recherche A\*](#heading-recherche-a-search)
    
7. [Algorithme de Kruskal](#heading-algorithme-de-kruskal)
    
8. [Algorithme de Prim](#heading-algorithme-de-prim)
    
9. [Algorithme de Bellman-Ford](#heading-algorithme-de-bellman-ford)
    
10. [Optimiser les algorithmes de graphes en Python](#heading-optimiser-les-algorithmes-de-graphes-en-python)
    
11. [Points clés à retenir](#heading-points-cles-a-retenir)
    

## Comprendre les graphes en Python

Un graphe se compose de **nœuds (sommets)** et d'**arêtes (relations)**.

Par exemple, dans un réseau social, les personnes sont des nœuds et les amitiés sont des arêtes. Ou dans une feuille de route, les villes sont des nœuds et les routes sont des arêtes.

Il existe différents types de graphes :

* **Orienté** : les arêtes ont une direction (rues à sens unique, planification de tâches).
    
* **Non orienté** : les arêtes vont dans les deux sens (amitiés mutuelles).
    
* **Pondéré** : les arêtes ont des valeurs (distances, coûts).
    
* **Non pondéré** : les arêtes sont égales (itinéraires de métro de base).
    

Maintenant que vous savez ce que sont les graphes, examinons les différentes façons dont ils peuvent être représentés en Python.

## Façons de représenter les graphes en Python

Avant de plonger dans le parcours et la recherche de chemin, il est important de savoir comment les graphes peuvent être représentés. Différents problèmes nécessitent différentes représentations.

### Matrice d'adjacence

Une matrice d'adjacence est un tableau 2D où chaque cellule `(i, j)` indique s'il existe une arête du nœud `i` au nœud `j`.

* Dans un **graphe non pondéré**, `0` signifie aucune arête, et `1` signifie qu'une arête existe.
    
* Dans un **graphe pondéré**, la cellule contient le poids de l'arête.
    

Cela permet de vérifier très rapidement si deux nœuds sont directement connectés (recherche en temps constant), mais cela consomme plus de mémoire pour les grands graphes.

```python
graph = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
```

Ici, la matrice montre un graphe de 3 nœuds entièrement connecté. Par exemple, `graph[0][1] = 1` signifie qu'il y a une arête du nœud 0 au nœud 1.

### Liste d'adjacence

Une liste d'adjacence représente chaque nœud accompagné de la liste des nœuds auxquels il est connecté.

C'est généralement plus efficace pour les graphes creux (où chaque nœud n'est pas connecté à tous les autres). Cela économise de la mémoire car seules les arêtes réelles sont stockées au lieu d'une grille entière.

```python
graph = {
    'A': ['B','C'],
    'B': ['A','C'],
    'C': ['A','B']
}
```

Ici, le nœud `A` se connecte à `B` et `C`, et ainsi de suite. Vérifier les connexions prend un peu plus de temps qu'avec une matrice, mais pour les grands graphes creux, c'est la meilleure option.

### Utilisation de NetworkX

Lorsqu'on travaille sur des applications réelles, écrire ses propres listes et matrices d'adjacence peut devenir fastidieux. C'est là qu'intervient **NetworkX**, une bibliothèque Python qui simplifie la création et l'analyse de graphes.

Avec seulement quelques lignes de code, vous pouvez construire des graphes, les visualiser et exécuter des algorithmes avancés sans réinventer la roue.

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([('A','B'), ('A','C'), ('B','C')])
nx.draw(G, with_labels=True)
plt.show()
```

Ceci construit un graphe en forme de triangle avec les nœuds A, B et C. NetworkX vous permet également d'exécuter facilement des algorithmes tels que les plus courts chemins ou les arbres couvrants sans les coder manuellement.

Maintenant que nous avons vu différentes façons de représenter les graphes, passons aux méthodes de parcours, en commençant par le parcours en largeur (BFS).

## Parcours en largeur (BFS)

L'idée de base du BFS est d'explorer un graphe couche par couche. Il examine tous les voisins d'un nœud de départ avant de passer au niveau suivant. Une file (queue) est utilisée pour suivre ce qui vient ensuite.

Le BFS est particulièrement utile pour :

* Trouver le plus court chemin dans les graphes non pondérés
    
* Détecter les composantes connectées
    
* Explorer des pages web
    

Voici un exemple :

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

bfs(graph, 'A')
```

Voici ce qui se passe dans ce code :

* `graph` est un dictionnaire où chaque nœud correspond à une liste de voisins.
    
* `deque` est utilisé comme une file FIFO pour visiter les nœuds niveau par niveau.
    
* `visited` garde trace des nœuds déjà traités pour éviter les boucles infinies sur les cycles.
    
* Dans la boucle, on extrait un nœud, on l'affiche, puis pour chaque voisin non visité, on le marque comme visité et on l'ajoute à la file.
    

Et voici la sortie :

```python
A B C D E F
```

Maintenant que nous avons vu comment fonctionne le BFS, passons à son homologue : le parcours en profondeur (DFS).

## Parcours en profondeur (DFS)

Le DFS fonctionne différemment du BFS. Au lieu de se déplacer niveau par niveau, il suit un chemin aussi loin que possible avant de revenir en arrière (backtracking). Pensez-y comme à une plongée profonde dans un sentier, puis à un retour pour explorer les autres.

Nous pouvons implémenter le DFS de deux manières :

* **DFS récursif**, qui utilise la pile d'appels de fonction
    
* **DFS itératif**, qui utilise une pile (stack) explicite
    

Le DFS est surtout utile pour :

* La détection de cycles
    
* La résolution de labyrinthes et de puzzles
    
* Le tri topologique
    

Voici un exemple de DFS récursif :

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

graph = {
    'A': ['B','C'],
    'B': ['A','D','E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

dfs_recursive(graph, 'A')
```

* `visited` est un ensemble qui suit les nœuds déjà traités pour éviter les boucles sur les cycles.
    
* À chaque appel, si le `node` n'a pas été vu, il est affiché, marqué comme visité, puis la fonction s'appelle récursivement pour chaque voisin.
    

Ordre de parcours :

```python
A B D E F C
```

Explication : le DFS visite B après A, s'enfonce dans D, puis revient en arrière pour explorer E et F, et visite enfin C.

Et voici un exemple de DFS itératif :

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))

dfs_iterative(graph, 'A')
```

* `visited` suit les nœuds déjà traités.
    
* `stack` est LIFO (dernier entré, premier sorti) – on `pop()` le nœud supérieur, on le traite, puis on ajoute ses voisins.
    
* `reversed(graph[node])` ajoute les voisins en sens inverse pour qu'ils soient visités dans l'ordre original de gauche à droite (imitant le DFS récursif habituel).
    

Voici la sortie :

```python
A B D E F C
```

Une fois le BFS et le DFS expliqués, nous pouvons passer à des algorithmes qui résolvent des problèmes plus complexes, en commençant par l'algorithme de plus court chemin de Dijkstra.

## Algorithme de Dijkstra

L'algorithme de Dijkstra repose sur une règle simple : toujours visiter d'abord le nœud ayant la plus petite distance connue. En répétant cela, il découvre le chemin le plus court d'un nœud de départ vers tous les autres dans un graphe pondéré ne possédant pas d'arêtes négatives.

```python
import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    shortest_path = {node: float('inf') for node in graph}
    shortest_path[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)
        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < shortest_path[neighbor]:
                shortest_path[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return shortest_path

graph = {
    'A': [('B',1), ('C',4)],
    'B': [('A',1), ('C',2), ('D',5)],
    'C': [('A',4), ('B',2), ('D',1)],
    'D': [('B',5), ('C',1)]
}

print(dijkstra(graph, 'A'))
```

Voici ce qui se passe dans ce code :

* `graph` est une liste d'adjacence : chaque nœud correspond à une liste de paires `(voisin, poids)`.
    
* `shortest_path` stocke la meilleure distance connue vers chaque nœud (initialement ∞, 0 pour `start`).
    
* `heap` (file de priorité) contient les nœuds frontières sous la forme `(coût, nœud)`, en extrayant toujours le coût le plus bas en premier.
    
* Pour chaque `node` extrait, il effectue un relâchement d'arêtes : pour chaque `(neighbor, weight)`, calcule `new_cost`. Si `new_cost` est meilleur que `shortest_path[neighbor]`, il le met à jour et ajoute le voisin à la file avec ce coût.
    

Et voici la sortie :

```python
{'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

Ensuite, examinons une extension de cet algorithme : *Recherche A\*.*

## Recherche A\*

A\* fonctionne comme Dijkstra mais ajoute une fonction heuristique qui estime la distance d'un nœud par rapport à l'objectif. Cela le rend plus efficace en guidant la recherche dans la bonne direction.

```python
import heapq

def heuristic(node, goal):
    heuristics = {'A': 4, 'B': 2, 'C': 1, 'D': 0}
    return heuristics.get(node, 0)

def a_star(graph, start, goal):
    g_costs = {node: float('inf') for node in graph}
    g_costs[start] = 0
    came_from = {}

    heap = [(heuristic(start, goal), start)]

    while heap:
        f, node = heapq.heappop(heap)

        if f > g_costs[node] + heuristic(node, goal):
            continue

        if node == goal:
            path = [node]
            while node in came_from:
                node = came_from[node]
                path.append(node)
            return path[::-1], g_costs[path[0]]

        for neighbor, weight in graph[node]:
            new_g = g_costs[node] + weight
            if new_g < g_costs[neighbor]:
                g_costs[neighbor] = new_g
                came_from[neighbor] = node
                heapq.heappush(heap, (new_g + heuristic(neighbor, goal), neighbor))

    return None, float('inf')

graph = {
    'A': [('B',1), ('C',4)],
    'B': [('A',1), ('C',2), ('D',5)],
    'C': [('A',4), ('B',2), ('D',1)],
    'D': []
}

print(a_star(graph, 'A', 'D'))
```

Celui-ci est un peu plus complexe, voici donc l'explication :

* `graph` : liste d'adjacence – chaque nœud correspond à `[(voisin, poids), ...]`.
    
* `heuristic(node, goal)` : renvoie une estimation `h(node)` (plus c'est bas, mieux c'est). L'objectif est passé, mais cette démo utilise un dictionnaire fixe.
    
* `g_costs` : coût le plus bas connu du `start` vers chaque nœud (initialement ∞, 0 pour start).
    
* `heap` : min-heap de `(priorité, nœud)` où `priorité = g + h`.
    
* `came_from` : pointeurs de retour pour reconstruire le chemin une fois l'objectif atteint.
    

Ensuite, dans la boucle principale :

* On extrait le nœud avec la plus petite priorité.
    
* Si c'est l'objectif, on remonte via `came_from` pour construire le chemin et le renvoyer avec `g_costs[goal]`.
    
* Sinon, on relâche les arêtes : pour chaque `(neighbor, weight)`, on calcule `new_cost = g_costs[node] + weight`. Si `new_cost` améliore `g_costs[neighbor]`, on le met à jour, on définit `came_from[neighbor] = node`, et on ajoute `(new_cost + heuristic(neighbor, goal), neighbor)` à la file.
    

Sortie :

```python
(['A', 'B', 'C', 'D'], 4)
```

Ensuite, passons des plus courts chemins aux arbres couvrants. C'est ici qu'intervient l'algorithme de Kruskal.

## Algorithme de Kruskal

L'algorithme de Kruskal construit un arbre couvrant minimal (MST) en triant toutes les arêtes de la plus petite à la plus grande et en les ajoutant une par une, tant qu'elles ne créent pas de cycle. Cela en fait un algorithme glouton car il choisit toujours l'option la moins chère disponible à chaque étape.

L'implémentation utilise une structure de données d'ensembles disjoints (Union-Find) pour vérifier efficacement si l'ajout d'une arête créerait un cycle. Chaque nœud commence dans son propre ensemble, et à mesure que les arêtes sont ajoutées, les ensembles sont fusionnés.

```python
class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, node1, node2):
        r1, r2 = self.find(node1), self.find(node2)
        if r1 != r2:
            if self.rank[r1] > self.rank[r2]:
                self.parent[r2] = r1
            else:
                self.parent[r1] = r2
                if self.rank[r1] == self.rank[r2]:
                    self.rank[r2] += 1

def kruskal(graph):
    edges = sorted(graph, key=lambda x: x[2])
    mst, ds = [], DisjointSet({u for e in graph for u in e[:2]})
    for u,v,w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u,v)
            mst.append((u,v,w))
    return mst

graph = [('A','B',1), ('A','C',4), ('B','C',2), ('B','D',5), ('C','D',1)]
print(kruskal(graph))
```

Sortie :

```python
[('A','B',1), ('C','D',1), ('B','C',2)]
```

Ici, l'MST inclut les arêtes les plus petites qui connectent tous les nœuds sans former de cycles. Maintenant que nous avons vu Kruskal, nous pouvons passer à l'analyse d'un autre algorithme.

## Algorithme de Prim

L'algorithme de Prim trouve également un MST, mais il fait croître l'arbre étape par étape. Il commence avec un nœud et **ajoute à plusieurs reprises l'arête la plus petite** qui connecte l'arbre actuel à un nouveau nœud. Pensez-y comme à l'expansion d'une « île » connectée jusqu'à ce que tous les nœuds soient inclus.

Cette implémentation utilise une **file de priorité (heapq)** pour toujours sélectionner l'arête disponible la plus petite de manière efficace.

```python
import heapq

def prim(graph, start):
    mst, visited = [], {start}
    edges = [(w, start, n) for n,w in graph[start]]
    heapq.heapify(edges)

    while edges:
        w,u,v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u,v,w))
            for n,w in graph[v]:
                if n not in visited:
                    heapq.heappush(edges, (w,v,n))
    return mst

graph = {
    'A':[('B',1),('C',4)],
    'B':[('A',1),('C',2),('D',5)],
    'C':[('A',4),('B',2),('D',1)],
    'D':[('B',5),('C',1)]
}
print(prim(graph,'A'))
```

Sortie :

```python
[('A','B',1), ('B','C',2), ('C','D',1)]
```

Remarquez comment l'algorithme s'étend progressivement à partir du nœud `A`, en choisissant toujours l'arête de poids le plus bas qui connecte un nouveau nœud.

Examinons maintenant un algorithme capable de gérer des graphes avec des arêtes négatives : Bellman-Ford.

## Algorithme de Bellman-Ford

Bellman-Ford est un algorithme de plus court chemin capable de gérer des poids d'arêtes négatifs, contrairement à Dijkstra. Il fonctionne en **relâchant toutes les arêtes de manière répétée** : si le chemin actuel vers un nœud peut être amélioré en passant par un autre nœud, il met à jour la distance. Après `V-1` itérations (où `V` est le nombre de sommets), tous les chemins les plus courts sont garantis d'être trouvés.

Cela le rend légèrement plus lent que Dijkstra mais plus polyvalent. Il peut également détecter des cycles de poids négatifs en vérifiant s'il y a d'autres améliorations possibles après la boucle principale.

```python
def bellman_ford(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    for _ in range(len(graph)-1):
        for u in graph:
            for v,w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist

graph = {
    'A':[('B',4),('C',2)],
    'B':[('C',-1),('D',2)],
    'C':[('D',3)],
    'D':[]
}
print(bellman_ford(graph,'A'))
```

Sortie :

```python
{'A': 0, 'B': 4, 'C': 2, 'D': 5}
```

Ici, le chemin le plus court vers chaque nœud est trouvé, même s'il y a une arête négative (`B → C` avec un poids de -1). S'il y avait eu un cycle négatif, Bellman-Ford l'aurait détecté en remarquant que les distances continuent de s'améliorer après `V-1` itérations.

Les principaux algorithmes ayant été expliqués, passons à quelques conseils pratiques pour rendre ces implémentations plus efficaces en Python.

## Optimiser les algorithmes de graphes en Python

Lorsque les graphes deviennent plus grands, de petits ajustements dans votre code peuvent faire une grande différence. Voici quelques astuces simples mais puissantes pour que tout fonctionne parfaitement.

**1\. Utilisez** `deque` pour le BFS  
Si vous utilisez une liste Python ordinaire comme file, extraire des éléments au début prend de plus en plus de temps à mesure que la liste s'allonge. Avec `collections.deque`, vous obtenez des extractions instantanées (`O(1)`) aux deux extrémités. C'est fait pour ça.

```python
from collections import deque

queue = deque([start])  # extractions et ajouts rapides
```

**2\. Passez à l'itératif pour le DFS**  
Le DFS récursif est élégant, mais Python n'aime pas descendre trop profondément – vous atteindrez une limite de récursion si votre graphe est très grand. La solution ? Écrivez le DFS dans un style itératif avec une pile. Même idée, pas d'erreurs de récursion.

```python
def dfs_iterative(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
```

**3\. Laissez NetworkX faire le gros du travail**  
Pour s'exercer et apprendre, écrire son propre code de graphe est excellent. Mais si vous travaillez sur un problème réel – par exemple analyser un réseau social ou planifier des itinéraires – la bibliothèque NetworkX fait gagner énormément de temps. Elle est fournie avec des versions optimisées de presque tous les algorithmes de graphes courants, ainsi que d'excellents outils de visualisation.

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([('A','B'), ('A','C'), ('B','D'), ('C','D')])

print(nx.shortest_path(G, source='A', target='D'))
```

**Sortie :**

```python
['A', 'B', 'D']
```

Au lieu de vous soucier des files et des piles, vous pouvez laisser NetworkX gérer les détails et vous concentrer sur la signification des résultats.

## Points clés à retenir

* Une matrice d'adjacence est rapide pour les recherches mais consomme beaucoup de mémoire.
    
* Une liste d'adjacence est efficace en termes d'espace pour les graphes creux.
    
* NetworkX facilite grandement l'analyse de graphes pour les projets réels.
    
* Le BFS explore couche par couche, le DFS explore en profondeur avant de revenir en arrière.
    
* Dijkstra et A\* gèrent les plus courts chemins.
    
* Kruskal et Prim construisent des arbres couvrants.
    
* Bellman-Ford fonctionne avec des poids négatifs.
    

## Conclusion

Les graphes sont partout, des cartes aux réseaux sociaux, et les algorithmes présentés ici sont les briques de base pour travailler avec eux. Qu'il s'agisse de trouver des chemins, de construire des arbres couvrants ou de gérer des poids complexes, ces outils ouvrent un large éventail de problèmes que vous pouvez résoudre.

Continuez à expérimenter et essayez des bibliothèques comme NetworkX quand vous serez prêt à entreprendre des projets plus ambitieux.