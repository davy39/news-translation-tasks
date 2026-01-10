---
title: Algorithmes de Graphes et Structures de Données Expliqués avec des Exemples
  en Java et C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T21:55:00.000Z'
originalURL: https://freecodecamp.org/news/graph-algorithms-and-data-structures-explained-with-java-and-c-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e3e740569d1a4ca3c1f.jpg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: Java
  slug: java
seo_title: Algorithmes de Graphes et Structures de Données Expliqués avec des Exemples
  en Java et C++
seo_desc: 'What is a Graph Algorithm?

  Graph algorithms are a set of instructions that traverse (visits nodes of a) graph.

  Some algorithms are used to find a specific node or the path between two given nodes.

  Why Graph Algorithms are Important

  Graphs are very us...'
---

## Qu'est-ce qu'un Algorithme de Graphe ?

Les algorithmes de graphes sont un ensemble d'instructions qui parcourent (visitent les nœuds d') un graphe.

Certains algorithmes sont utilisés pour trouver un nœud spécifique ou le chemin entre deux nœuds donnés.

### Pourquoi les Algorithmes de Graphes sont Importants

Les graphes sont des structures de données très utiles qui peuvent être utilisées pour modéliser divers problèmes. Ces algorithmes ont des applications directes sur les sites de réseaux sociaux, la modélisation de machines à états et bien plus encore.

### Quelques Algorithmes de Graphes Communs

Certains des algorithmes de graphes les plus courants sont :

* Parcours en Largeur (BFS)
* Parcours en Profondeur (DFS)
* Dijkstra
* Algorithme de Floyd-Warshall

## Algorithme de Bellman Ford

L'algorithme de Bellman Ford est un algorithme de recherche de plus court chemin pour les graphes qui peuvent avoir des poids négatifs. L'algorithme de Bellman Ford est également excellent pour détecter les cycles de poids négatifs, car l'algorithme converge vers une solution optimale en O(V*E) étapes. Si le résultat n'est pas optimal, alors le graphe contient un cycle de poids négatif.

Voici une implémentation en Python :

```
infinity = 1e10

def bellman_ford(graph, start, end):
    num_vertices = graph.get_num_vertices()
    edges = graph.get_edges()

    distance = [infinity for vertex in range(num_vertices)]
    previous = [None for vertex in range(num_vertices)]

    distance[start] = 0
    for i range(end+1):
        for (u, v) in edges:
            if distance[v] > distance[u] + graph.get_weight(u, v):
                distance[v] = distance[u] + graph.get_weight(u, v)
                previous[v] = u

    for (u,v) in edges:
        if distance[v] > distance[u] + graph.get_weight(u, v):
            raise NegativeWeightCycleError()
    return distance, previous
# 'distance' est la distance depuis le départ jusqu'à ce nœud dans le chemin le plus court, utile pour imprimer la distance la plus courte.
# Previous est un tableau qui indique le nœud qui précède le nœud actuel, utile pour imprimer le chemin.

```

## Parcours en Profondeur (DFS)

Le parcours en profondeur est l'un des algorithmes de graphes les plus simples. Il parcourt le graphe en vérifiant d'abord le nœud actuel, puis en se déplaçant vers l'un de ses successeurs pour répéter le processus. Si le nœud actuel n'a pas de successeur à vérifier, nous revenons à son prédécesseur et le processus continue (en se déplaçant vers un autre successeur). Si la solution est trouvée, la recherche s'arrête.

### Visualisation

![Image](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

### Implémentation (C++14)

```
#include <iostream> 
#include <vector> 
#include <queue>  
#include <algorithm>
using namespace std; 
 
class Graph{ 
   int v;    // nombre de sommets 
 
   // pointeur vers un vecteur contenant des listes d'adjacence 
   vector < int > *adj;
public: 
   Graph(int v);  // Constructeur 
 
   // fonction pour ajouter une arête au graphe 
   void add_edge(int v, int w);  
 
   // imprime le parcours dfs à partir d'une source donnée `s` 
   void dfs();
   void dfs_util(int s, vector < bool> &visited);   
}; 
 
Graph::Graph(int v){ 
   this -> v = v; 
   adj = new vector < int >[v]; 
} 
 
void Graph::add_edge(int u, int v){ 
   adj[u].push_back(v); // ajoute v à la liste de u
   adj[v].push_back(v);  // ajoute u à la liste de v (supprimez cette instruction si le graphe est dirigé !)
} 
void Graph::dfs(){
   // vecteur visité - pour suivre les nœuds visités pendant le DFS
   vector < bool > visited(v, false);  // marque tous les nœuds/sommets comme non visités
   for(int i = 0; i < v; i++)
       if(!visited[i])
           dfs_util(i, visited);
} 
// remarquez l'utilisation du passage par référence ici !
void Graph::dfs_util(int s, vector < bool > &visited){ 
   // marque le nœud/sommet actuel comme visité
   visited[s] = true;
    // l'affiche à la sortie standard (écran)
   cout << s << " ";
   
   // parcourt sa liste d'adjacence et appelle récursivement dfs_util pour tous ses voisins !
   // (uniquement si le voisin n'a pas encore été visité !)
   for(vector < int > :: iterator itr = adj[s].begin(); itr != adj[s].end(); itr++)
       if(!visited[*itr])
           dfs_util(*itr, visited); 
} 
 
int main() 
{ 
   // crée un graphe en utilisant la classe Graph que nous avons définie ci-dessus
   Graph g(4); 
   g.add_edge(0, 1); 
   g.add_edge(0, 2); 
   g.add_edge(1, 2); 
   g.add_edge(2, 0); 
   g.add_edge(2, 3); 
   g.add_edge(3, 3); 
 
   cout << "Voici le Parcours en Profondeur du graphe fourni"
        << "(en commençant par le sommet 0): "; 
   g.dfs(); 
   // la sortie serait : 0 1 2 3
   return 0; 
} 

```

### Évaluation

Complexité Spatiale : O(n)

Complexité Temporelle dans le Pire Cas : O(n) Le parcours en profondeur est complet sur un ensemble fini de nœuds. Il fonctionne mieux sur des arbres peu profonds.

### Implémentation du DFS en C++

```
#include<iostream>
#include<vector>
#include<queue>

using namespace std;

struct Graph{
	int v;
	bool **adj;
	public:
		Graph(int vcount);
		void addEdge(int u,int v);
		void deleteEdge(int u,int v);
		vector<int> DFS(int s);
		void DFSUtil(int s,vector<int> &dfs,vector<bool> &visited);
};
Graph::Graph(int vcount){
	this->v = vcount;
	this->adj=new bool*[vcount];
	for(int i=0;i<vcount;i++)
		this->adj[i]=new bool[vcount];
	for(int i=0;i<vcount;i++)
		for(int j=0;j<vcount;j++)
			adj[i][j]=false;
}

void Graph::addEdge(int u,int w){
	this->adj[u][w]=true;
	this->adj[w][u]=true;
}

void Graph::deleteEdge(int u,int w){
	this->adj[u][w]=false;
	this->adj[w][u]=false;
}

void Graph::DFSUtil(int s, vector<int> &dfs, vector<bool> &visited){
	visited[s]=true;
	dfs.push_back(s);
	for(int i=0;i<this->v;i++){
		if(this->adj[s][i]==true && visited[i]==false)
			DFSUtil(i,dfs,visited);
	}
}

vector<int> Graph::DFS(int s){
	vector<bool> visited(this->v);
	vector<int> dfs;
	DFSUtil(s,dfs,visited);
	return dfs;
}

```

## Algorithme de Floyd Warshall

L'algorithme de Floyd Warshall est un excellent algorithme pour trouver la distance la plus courte entre tous les sommets d'un graphe. Il a un algorithme très concis et une complexité temporelle de O(V^3) (où V est le nombre de sommets). Il peut être utilisé avec des poids négatifs, bien que des cycles de poids négatifs ne doivent pas être présents dans le graphe.

### Évaluation

Complexité Spatiale : O(V^2)

Complexité Temporelle dans le Pire Cas : O(V^3)

### Implémentation en Python

```
# Une grande valeur comme infinie
inf = 1e10 

def floyd_warshall(weights):
    V = len(weights)
    distance_matrix = weights
    for k in range(V):
        next_distance_matrix = [list(row) for row in distance_matrix] # faire une copie de la matrice de distance
        for i in range(V):
            for j in range(V):
                # Choisir si le sommet k peut servir de chemin avec une distance plus courte
                next_distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
        distance_matrix = next_distance_matrix # mise à jour
    return distance_matrix

# Un graphe représenté comme matrice d'adjacence
graph = [
    [0, inf, inf, -3],
    [inf, 0, inf, 8],
    [inf, 4, 0, -2],
    [5, inf, 3, 0]
]

print(floyd_warshall(graph))

```

## Parcours en Largeur (BFS)

Le parcours en largeur est l'un des algorithmes de graphes les plus simples. Il parcourt le graphe en vérifiant d'abord le nœud actuel, puis en l'expansant en ajoutant ses successeurs au niveau suivant. Le processus est répété pour tous les nœuds du niveau actuel avant de passer au niveau suivant. Si la solution est trouvée, la recherche s'arrête.

### Visualisation

![Image](https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif)

### Évaluation

Complexité Spatiale : O(n)

Complexité Temporelle dans le Pire Cas : O(n)

Le parcours en largeur est complet sur un ensemble fini de nœuds et optimal si le coût de déplacement d'un nœud à un autre est constant.

### Code C++ pour l'implémentation de BFS

```
// Programme pour imprimer le parcours BFS à partir d'un sommet source donné. BFS(int s) parcourt les sommets 
// accessibles depuis s. 
#include<iostream> 
#include <list> 
  
using namespace std; 
  
// Cette classe représente un graphe dirigé en utilisant 
// la représentation par liste d'adjacence 
class Graph 
{ 
    int V;    // Nombre de sommets 
  
    // Pointeur vers un tableau contenant des listes d'adjacence 
    list<int> *adj;    
public: 
    Graph(int V);  // Constructeur 
  
    // fonction pour ajouter une arête au graphe 
    void addEdge(int v, int w);  
  
    // imprime le parcours BFS à partir d'une source donnée s 
    void BFS(int s);   
}; 
  
Graph::Graph(int V) 
{ 
    this->V = V; 
    adj = new list<int>[V]; 
} 
  
void Graph::addEdge(int v, int w) 
{ 
    adj[v].push_back(w); // Ajoute w à la liste de v. 
} 
  
void Graph::BFS(int s) 
{ 
    // Marque tous les sommets comme non visités 
    bool *visited = new bool[V]; 
    for(int i = 0; i < V; i++) 
        visited[i] = false; 
  
    // Crée une file pour BFS 
    list<int> queue; 
  
    // Marque le nœud actuel comme visité et l'enfile 
    visited[s] = true; 
    queue.push_back(s); 
  
    // 'i' sera utilisé pour obtenir tous les sommets adjacents d'un sommet 
    list<int>::iterator i; 
  
    while(!queue.empty()) 
    { 
        // Défile un sommet de la file et l'imprime 
        s = queue.front(); 
        cout << s << " "; 
        queue.pop_front(); 
  
        // Obtient tous les sommets adjacents du sommet défilé 
        // s. Si un sommet adjacent n'a pas été visité, 
        // alors le marque comme visité et l'enfile 
        for (i = adj[s].begin(); i != adj[s].end(); ++i) 
        { 
            if (!visited[*i]) 
            { 
                visited[*i] = true; 
                queue.push_back(*i); 
            } 
        } 
    } 
} 
  
// Programme pilote pour tester les méthodes de la classe graph 
int main() 
{ 
    // Crée un graphe donné dans le diagramme ci-dessus 
    Graph g(4); 
    g.addEdge(0, 1); 
    g.addEdge(0, 2); 
    g.addEdge(1, 2); 
    g.addEdge(2, 0); 
    g.addEdge(2, 3); 
    g.addEdge(3, 3); 
  
    cout << "Voici le Parcours en Largeur "
         << "(en commençant par le sommet 2) \n"; 
    g.BFS(2); 
  
    return 0; 
}

```

## Algorithme de Dijkstra

L'algorithme de Dijkstra est un algorithme de graphe présenté par E.W. Dijkstra. Il trouve le chemin le plus court à partir d'une source unique dans un graphe avec des arêtes non négatives. (pourquoi ?)

Nous créons 2 tableaux : visited et distance, qui enregistrent si un sommet est visité et quelle est la distance minimale depuis le sommet source, respectivement. Initialement, le tableau visited est défini comme faux et distance comme infini.

Nous commençons par le sommet source. Soit le sommet actuel u et ses sommets adjacents v. Maintenant, pour chaque v qui est adjacent à u, la distance est mise à jour si elle n'a pas été visitée auparavant et si la distance depuis u est inférieure à sa distance actuelle. Ensuite, nous sélectionnons le sommet suivant avec la distance la plus faible et qui n'a pas été visité.

La file de priorité est souvent utilisée pour répondre à cette dernière exigence dans le temps le plus court. Ci-dessous se trouve une implémentation de la même idée utilisant une file de priorité en Java.

```
import java.util.*;
public class Dijkstra {
    class Graph {
	LinkedList<Pair<Integer>> adj[];
	int n; // Nombre de sommets.
	Graph(int n) {
	    this.n = n;
	    adj = new LinkedList[n];
	    for(int i = 0;i<n;i++) adj[i] = new LinkedList<>();
	}
	// ajoute une arête dirigée entre les sommets a et b avec un coût comme poids
	public void addEdgeDirected(int a, int b, int cost) {
	    adj[a].add(new Pair(b, cost));
	}
	public void addEdgeUndirected(int a, int b, int cost) {
	    addEdgeDirected(a, b, cost);
	    addEdgeDirected(b, a, cost);
	}
    }
    class Pair<E> {
	E first;
	E second;
	Pair(E f, E s) {
	    first = f;
	    second = s;
	}
    }

    // Comparateur pour trier les Pairs dans la File de Priorité
    class PairComparator implements Comparator<Pair<Integer>> {
	public int compare(Pair<Integer> a, Pair<Integer> b) {
	    return a.second - b.second;
	}
    }

    // Calcule le chemin le plus court vers chaque sommet depuis la source et retourne la distance
    public int[] dijkstra(Graph g, int src) {
	int distance[] = new int[g.n]; // distance la plus courte de chaque sommet depuis src
	boolean visited[] = new boolean[g.n]; // sommet est visité ou non
	Arrays.fill(distance, Integer.MAX_VALUE);
	Arrays.fill(visited, false);
	PriorityQueue<Pair<Integer>> pq = new PriorityQueue<>(100, new PairComparator());
        pq.add(new Pair<Integer>(src, 0));
	distance[src] = 0;
	while(!pq.isEmpty()) {
	    Pair<Integer> x = pq.remove(); // Extrait le sommet avec la distance la plus courte depuis src
	    int u = x.first;
	    visited[u] = true;
	    Iterator<Pair<Integer>> iter = g.adj[u].listIterator();
	    // Parcourt les voisins de u et met à jour leurs distances
	    while(iter.hasNext()) {
		Pair<Integer> y = iter.next();
		int v = y.first;
		int weight = y.second;
		// Vérifie si le sommet v n'est pas visité
		// Si le nouveau chemin à travers u offre un coût moindre, alors met à jour le tableau des distances et ajoute à pq
		if(!visited[v] && distance[u]+weight<distance[v]) {
		    distance[v] = distance[u]+weight;
		    pq.add(new Pair(v, distance[v]));
		}
	    }
	}
	return distance;
    }

    public static void main(String args[]) {
	Dijkstra d = new Dijkstra();
	Dijkstra.Graph g = d.new Graph(4);
	g.addEdgeUndirected(0, 1, 2);
	g.addEdgeUndirected(1, 2, 1);
	g.addEdgeUndirected(0, 3, 6);
	g.addEdgeUndirected(2, 3, 1);
	g.addEdgeUndirected(1, 3, 3);

	int dist[] = d.dijkstra(g, 0);
	System.out.println(Arrays.toString(dist));
    }
}

```

## Algorithme de Ford Fulkerson

L'algorithme de Ford Fulkerson résout le problème de flux maximum dans un graphe. Il trouve la meilleure organisation du flux à travers les arêtes des graphes de sorte que vous obteniez un flux maximum à l'autre extrémité. La source a un taux d'entrée spécifique et chaque arête a un poids associé qui est la substance maximale qui peut être passée à travers cette arête.

L'algorithme de Ford Fulkerson est également appelé algorithme d'Edmund-Karp car l'algorithme a été fourni en spécification complète par Jack Edmonds et Richard Karp.

Il fonctionne en créant des chemins augmentants, c'est-à-dire des chemins de la source au puits qui ont un flux non nul. Nous passons le flux à travers les chemins et nous mettons à jour les limites. Cela peut conduire à une situation où nous n'avons plus de mouvements possibles. C'est là que la capacité "d'annulation" de cet algorithme joue un grand rôle. En cas de blocage, nous diminuons le flux et ouvrons l'arête pour passer notre substance actuelle.

## Étapes

1. Définir un flux nul pour toutes les arêtes.
2. Tant qu'il existe un chemin de la source au puits, faire :
3. Trouver le poids minimum sur le chemin, soit `limit`.
4. Pour toutes les arêtes (u, v) sur le chemin, faire :
1. Ajouter `limit` au flux de u à v. (Pour le mouvement actuel)
2. Soustraire `limit` du flux de v à u. (Pour l'annulation dans un mouvement ultérieur)

### Évaluation

Complexité Temporelle : `O(V*E^2)`

### Implémentation en Python

```
# Grand nombre comme infinie
inf = 1e10

def maximum_flow(graph, source, sink):
  max_flow = 0
  parent = bfs(graph, source, sink)
  while path:
    limit = inf
    v = sink
    while v != source:
        u = parent[s]
        path_flow = min(limit, graph[u][v])
        v = parent[v]
    max_flow += path_flow

    v = sink
    while v != source:
        u = parent[v]
        graph[u][v] -= path_flow
        graph[v][u] += path_flow
        v = parent[v]

    path = bfs(graph, source, sink)
  return max_flow

```