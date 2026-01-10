---
title: Algorithmes de graphes expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T00:33:00.000Z'
originalURL: https://freecodecamp.org/news/graph-algorithms-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dbe740569d1a4ca3965.jpg
tags:
- name: algorithms
  slug: algorithms
- name: toothbrush
  slug: toothbrush
seo_title: Algorithmes de graphes expliqués
seo_desc: 'What are graph algorithms?

  Graph algorithms are a set of instructions that traverse (visits nodes of a) graph.

  Some algorithms are used to find a specific node or the path between two given nodes.

  Why Graph Algorithms are Important

  Graphs are very us...'
---

## **Qu'est-ce que les algorithmes de graphes ?**

Les algorithmes de graphes sont un ensemble d'instructions qui parcourent (visitent les nœuds d') un graphe.

Certains algorithmes sont utilisés pour trouver un nœud spécifique ou le chemin entre deux nœuds donnés.

### **Pourquoi les algorithmes de graphes sont importants**

Les graphes sont des structures de données très utiles qui peuvent être utilisées pour modéliser divers problèmes. Ces algorithmes ont des applications directes sur les sites de réseaux sociaux, la modélisation de machines à états et bien d'autres cas d'utilisation.

## **Quelques algorithmes de graphes courants**

Dans cet article, nous allons examiner quelques algorithmes de graphes couramment utilisés et fournir une explication et des exemples pour chacun. Alors, commençons.

## **Recherche en largeur (BFS)**

La recherche en largeur est l'un des algorithmes de graphes les plus simples. Il parcourt le graphe en vérifiant d'abord le nœud actuel, puis en l'expansant en ajoutant ses successeurs au niveau suivant. Le processus est répété pour tous les nœuds du niveau actuel avant de passer au niveau suivant. Si la solution est trouvée, la recherche s'arrête.

### **Visualisation**

![Image](https://upload.wikimedia.org/wikipedia/commons/4/46/Animated_BFS.gif)

### **Évaluation**

Complexité spatiale : O(n)

Complexité temporelle dans le pire cas : O(n)

La recherche en largeur est complète sur un ensemble fini de nœuds et optimale si le coût de déplacement d'un nœud à un autre est constant.

### **Code C++ pour l'implémentation de BFS**

```cpp
// Programme pour imprimer le parcours BFS à partir d'un sommet source donné. BFS(int s) parcourt les sommets 
// accessibles depuis s. 
#include<iostream> 
#include <list> 
  
using namespace std; 
  
// Cette classe représente un graphe orienté en utilisant 
// une représentation par liste d'adjacence 
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
    // Marquer tous les sommets comme non visités 
    bool *visited = new bool[V]; 
    for(int i = 0; i < V; i++) 
        visited[i] = false; 
  
    // Créer une file pour BFS 
    list<int> queue; 
  
    // Marquer le nœud actuel comme visité et l'enfiler 
    visited[s] = true; 
    queue.push_back(s); 
  
    // 'i' sera utilisé pour obtenir tous les sommets adjacents 
    // d'un sommet 
    list<int>::iterator i; 
  
    while(!queue.empty()) 
    { 
        // Défiler un sommet de la file et l'imprimer 
        s = queue.front(); 
        cout << s << " "; 
        queue.pop_front(); 
  
        // Obtenir tous les sommets adjacents du sommet défilé 
        // s. Si un sommet adjacent n'a pas été visité, 
        // alors le marquer comme visité et l'enfiler 
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
  
// Programme principal pour tester les méthodes de la classe graphe 
int main() 
{ 
    // Créer un graphe donné dans le diagramme ci-dessus 
    Graph g(4); 
    g.addEdge(0, 1); 
    g.addEdge(0, 2); 
    g.addEdge(1, 2); 
    g.addEdge(2, 0); 
    g.addEdge(2, 3); 
    g.addEdge(3, 3); 
  
    cout << "Voici le parcours en largeur "
         << "(en commençant par le sommet 2) \n"; 
    g.BFS(2); 
  
    return 0; 
}
```

## **Recherche en profondeur (DFS)**

La recherche en profondeur est l'un des algorithmes de graphes les plus simples. Il parcourt le graphe en vérifiant d'abord le nœud actuel, puis en se déplaçant vers l'un de ses successeurs pour répéter le processus. 

Si le nœud actuel n'a pas de successeur à vérifier, nous revenons à son prédécesseur et le processus continue (en se déplaçant vers un autre successeur). Si la solution est trouvée, la recherche s'arrête.

### **Visualisation**

![Image](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif)

### **Implémentation (C++14)**

```c++
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
   adj[v].push_back(v);  // ajoute u à la liste de v (supprimez cette instruction si le graphe est orienté !)
} 
void Graph::dfs(){
   // vecteur visité - pour suivre les nœuds visités pendant DFS
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
   // (uniquement si le voisin n'a pas été visité !)
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
 
   cout << "Voici le parcours en profondeur du graphe fourni"
        << "(en commençant par le sommet 0) : "; 
   g.dfs(); 
   // la sortie serait : 0 1 2 3
   return 0; 
}
```

### **Évaluation**

Complexité spatiale : O(n)

Complexité temporelle dans le pire cas : O(n) La recherche en profondeur est complète sur un ensemble fini de nœuds. Elle fonctionne mieux sur des arbres peu profonds.

### **Implémentation de DFS en C++**

```c++
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

# **Algorithme de Dijkstra**

L'algorithme de Dijkstra est un algorithme de graphe présenté par E.W. Dijkstra. Il trouve le chemin le plus court à partir d'une source unique dans un graphe avec des arêtes non négatives.

Nous créons 2 tableaux : visited et distance, qui enregistrent si un sommet est visité et quelle est la distance minimale depuis le sommet source, respectivement. Le tableau visited est initialement défini comme faux et distance comme infini.

Nous commençons par le sommet source. Soit le sommet actuel u et ses sommets adjacents v. Maintenant, pour chaque v qui est adjacent à u, la distance est mise à jour si elle n'a pas été visitée auparavant et si la distance depuis u est inférieure à sa distance actuelle. Ensuite, nous sélectionnons le sommet suivant avec la distance la plus faible et qui n'a pas été visité.

La file de priorité est souvent utilisée pour répondre à cette dernière exigence dans le temps le plus court possible. Ci-dessous se trouve une implémentation de la même idée utilisant une file de priorité en Java.

```java
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

    // Comparateur pour trier les Pairs dans la file de priorité
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
	    Pair<Integer> x = pq.remove(); // Extraire le sommet avec la distance la plus courte depuis src
	    int u = x.first;
	    visited[u] = true;
	    Iterator<Pair<Integer>> iter = g.adj[u].listIterator();
	    // Itérer sur les voisins de u et mettre à jour leurs distances
	    while(iter.hasNext()) {
		Pair<Integer> y = iter.next();
		int v = y.first;
		int weight = y.second;
		// Vérifier si le sommet v n'est pas visité
		// Si le nouveau chemin à travers u offre un coût moindre, alors mettre à jour le tableau des distances et ajouter à pq
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

## **Algorithme de Floyd-Warshall**

L'algorithme de Floyd-Warshall est un excellent algorithme pour trouver la distance la plus courte entre tous les sommets dans un graphe. C'est un algorithme très concis et a une complexité temporelle de O(V^3) (où V est le nombre de sommets). 

Il peut être utilisé avec des poids négatifs, bien que des cycles de poids négatifs ne doivent pas être présents dans le graphe.

### **Évaluation**

Complexité spatiale : O(V^2)

Complexité temporelle dans le pire cas : O(V^3)

### **Implémentation en Python**

```python
# Une grande valeur comme infini
inf = 1e10 

def floyd_warshall(weights):
    V = len(weights)
    distance_matrix = weights
    for k in range(V):
        next_distance_matrix = [list(row) for row in distance_matrix] # faire une copie de la matrice des distances
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