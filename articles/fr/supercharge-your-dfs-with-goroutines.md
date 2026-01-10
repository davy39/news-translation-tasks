---
title: Comment booster votre parcours en profondeur avec des goroutines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-22T01:49:36.000Z'
originalURL: https://freecodecamp.org/news/supercharge-your-dfs-with-goroutines
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Frame-1-1.png
tags:
- name: algorithms
  slug: algorithms
- name: Go Language
  slug: go
- name: Trees
  slug: trees
seo_title: Comment booster votre parcours en profondeur avec des goroutines
seo_desc: 'By Aayush Joglekar

  What is Depth First Search?

  Depth first search is a popular graph traversal algorithm. One application of depth
  first search in real world applications is in site mapping.

  A site map is a list of pages of a web site. They are organ...'
---

Par Aayush Joglekar

## Qu'est-ce que le parcours en profondeur ?

Le parcours en profondeur est un algorithme populaire de parcours de graphes. Une application du parcours en profondeur dans les applications réelles est la cartographie de sites.

Une carte de site est une liste de pages d'un site web. Elles sont organisées de manière hiérarchique et décrivent toute la structure d'un site web à partir d'un nœud racine.

### L'algorithme

La cartographie de site implique de charger un lien racine, d'analyser les liens internes sur la page, puis d'appliquer récursivement le même processus à ces liens. Cela nous donne une structure de données de graphe, mais pour simplifier, nous pouvons supposer qu'il s'agit d'un arbre.

### Le problème

Si nous implémentions l'algorithme de cette manière, le chargement et l'analyse des pages HTML prennent du temps et bloquent tout le processus de parcours.

Supposons qu'une réponse HTTP prenne en moyenne _300ms_ et qu'il y ait 100 pages sur le site à cartographier. 300*100 = 30000ms => 30 secondes. Ainsi, le processus restera inactif pendant 300 secondes.

## Comment pouvons-nous améliorer cela ?

Dans le temps où une page se charge, vous pouvez envoyer plusieurs requêtes HTTP et analyser les pages HTML reçues si vous implémentez une architecture multithread.

Cette méthode concurrente est **7 fois plus rapide** que celle mentionnée précédemment.

L'implémentation de threads peut déclencher l'alarme dans l'esprit de nombreux développeurs. Cependant, Golang vous fournit un ensemble de concepts comme les goroutines, les canaux et les utilitaires de synchronisation pour rendre le travail beaucoup plus facile.

J'ai parlé de cartographie de site plus tôt, cependant, il est beaucoup mieux et plus simple si vous apprenez à programmer un algorithme de parcours en profondeur pour un arbre binaire. Vous pouvez appliquer ce que vous apprendrez dans cet article à beaucoup de choses différentes.

Commençons !

Vous pouvez trouver le code utilisé dans cet article ici sur [GitHub](https://github.com/zerefwayne/article-snippets/tree/master/supercharge-dfs-with-goroutines).

## Installation de l'arbre

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Group-11.png)



### Définition du nœud

Une structure de nœud est le bloc de construction de base de votre arbre binaire. Elle a une donnée, un pointeur vers l'enfant gauche et un pointeur vers l'enfant droit. Pour simuler le délai de traitement d'un nœud, vous devez attribuer un temps de sommeil aléatoire en microsecondes.

```go
type Node struct {
	Data interface{}
	Sleep time.Duration
	Left *Node
	Right *Node
}
```

### Fonction de génération de nœud

`NewNode()` retourne un pointeur vers un nouveau nœud. Sleep est attribué une durée de 0-100 microsecondes.

```go
func NewNode(data interface{}) *Node {

	node := new(Node)

	node.Data = data
	node.Left = nil
	node.Right = nil

	rand.Seed(time.Now().UTC().UnixNano())
	duration := int64(rand.Intn(100))
	node.Sleep = time.Duration(duration) * time.Microsecond

	return node
}
```

Maintenant, vous avez configuré votre arbre et pouvez implémenter le parcours en profondeur et une fonction pour traiter le nœud.

## Parcours en profondeur à thread unique

### ProcessNode()

`ProcessNode()` est une fonction qui sera invoquée lorsque le nœud doit être traité lors d'un parcours.

Normalement, vous imprimeriez ou stockeriez la valeur du nœud. Cependant, pour montrer les avantages des goroutines, vous devrez implémenter une tâche intensive en calcul qui prend environ 1 seconde.

Lors de chaque itération, le nœud dort pendant `n.Sleep` microsecondes et imprime `Node <data> ✅` une fois la tâche terminée.

```go
func (n *Node) ProcessNode() {

	var hello []int

	for i := 0; i < 10000; i++ {
		time.Sleep(n.Sleep)
		hello = append(hello, i)
	}
    
	fmt.Printf("Node %v ✅\n", n.Data)
}
```

### Fonction récursive de parcours en profondeur

Il s'agit d'une fonction de parcours en profondeur à thread unique implémentée via la récursion — elle peut sembler familière à ceux qui l'ont déjà écrite.

```go
func (n *Node) DFS() {

	if n == nil {
		return
	}

	n.Left.DFS()
	n.ProcessNode()
	n.Right.DFS()
}
```

### Implémentation de la fonction main()

Dans la fonction principale, créez un arbre binaire complet qui se compose de 7 nœuds.

Pour voir combien de temps s'est écoulé, initiez `start` puis commencez le DFS à la racine. Une fois terminé, `main()` imprime le temps qui s'est écoulé.

```go
var wg sync.WaitGroup

func main() {

	root := NewNode(1)
	root.Left = NewNode(2)
	root.Right = NewNode(3)
	root.Left.Left = NewNode(4)
	root.Left.Right = NewNode(5)
	root.Right.Left = NewNode(6)
	root.Right.Right = NewNode(7)

	start := time.Now()
	root.DFS()
	fmt.Printf("\nTime elapsed: %v\n\n", time.Since(start))
    
}
```

### Sortie

Il a fallu `8.75s` pour que le parcours en profondeur se termine.

La plupart du temps, le processeur était inactif car chaque nœud était en cours de traitement. Cela a également empêché les autres nœuds de traiter pendant qu'il terminait son temps de sommeil.

Dans le monde réel, cette situation se produit lors des E/S ou des appels HTTP externes.

```
Node 4 ✅
Node 2 ✅
Node 5 ✅
Node 1 ✅
Node 6 ✅
Node 3 ✅
Node 7 ✅

Time elapsed: 8.75086767s
```

## Boostez votre parcours en profondeur avec des goroutines

%[https://tenor.com/bd2iD.gif]

La conversion des fonctions de processus et de parcours en profondeur implique seulement des changements mineurs par rapport à d'autres langages de programmation :

1. Appeler la fonction récursive avec la commande `go`.
2. Maintenir un `waitGroup` qui suit la fonction en cours de traitement afin que le programme ne se termine pas sans que toutes soient terminées.

### DFSParallel()

`wg.Add(1)` : Avant d'entrer dans la récursion, ajoutez la goroutine qui sera démarrée au `waitGroup`.

Vous pouvez également exécuter `wg.Add(3)` puis démarrer les trois goroutines et cela fera le travail. Cependant, cela est plus esthétique et indique clairement ce qui va se passer.

`defer wg.Done()` : diminue le compteur `waitGroup` de 1 lorsque la fonction retourne. Cela indique que la routine est terminée.

`go` : Démarre la fonction dans une nouvelle goroutine.

```go
func (n *Node) DFSParallel() {

	defer wg.Done()

	if n == nil {
		return
	}

	wg.Add(1)
	go n.Left.DFSParallel()

	wg.Add(1)
	go n.ProcessNodeParallel()

	wg.Add(1)
	go n.Right.DFSParallel()
}
```

### ProcessNodeParallel()

Rien de beaucoup à faire ici, il suffit d'ajouter un `defer wg.Done()` après le début de la fonction. Cela informera `waitGroup` que cette goroutine est terminée.

```go
func (n *Node) ProcessNodeParallel() {

	defer wg.Done()

	var hello []int
    
	for i := 0; i < 10000; i++ {
		time.Sleep(n.Sleep)
		hello = append(hello, i)
	}
    
	fmt.Printf("Node %v ✅\n", n.Data)
}
```

### 

### Appel de DFSParallel() dans main()

`GOMAXPROCS` indique au compilateur Go d'exécuter des threads sur tous les cœurs logiques disponibles sur l'ordinateur.

Cela vous aidera à traiter plusieurs nœuds également. Le modèle de conception concurrent implémenté ici montre l'avantage d'avoir plusieurs cœurs sur l'ordinateur. Non seulement le programme peut traiter d'autres nœuds pendant qu'un dort, mais il peut également traiter plusieurs nœuds en même temps.

Vous pouvez démarrer `DFSParallel()` comme une goroutine comme avant et l'ajouter au groupe d'attente.

`wg.Wait()` attend que toutes les goroutines soient terminées. Il attend que le compteur de goroutines soit à 0 puis fait avancer le contrôle.

```go
...
	// Go utilisera le nombre maximum de processeurs disponibles pour traiter les goroutines
	processors := runtime.GOMAXPROCS(runtime.NumCPU())
    
    fmt.Printf("\nTime elapsed: %v\n\n", time.Since(start))

	// Démarre le chronomètre
	start = time.Now()

	// Ajoute une goroutine au WaitGroup
	wg.Add(1)
	// Démarre la goroutine DFS
	go root.DFSParallel()
	// Attend que toutes les goroutines soient terminées
	wg.Wait()

	fmt.Printf("\nProcessors: %v Time elapsed: %v\n", processors, time.Since(start))


}
```

### Sortie

```
Node 7 ✅
Node 4 ✅
Node 2 ✅
Node 6 ✅
Node 5 ✅
Node 1 ✅
Node 3 ✅

Processors: 8 Time elapsed: 1.295332809s
```

Comme prévu, l'algorithme de parcours en profondeur se termine en seulement **1,3 secondes** contre **8,7 secondes** dans l'implémentation précédente.

## Explication

#### Implémentation normale

Les fonctions s'exécutaient en série de manière pré-ordonnée comme vous pourriez vous y attendre. Chaque fonction prenait ~1,1 seconde pour se terminer, ce qui conduisait à un long temps d'exécution.

Cependant, chaque nœud dort pendant ~1 seconde également, pendant laquelle les processeurs restent inactifs car tout s'exécute dans un seul thread.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Group-2.png)
_Graphique du temps d'implémentation normale (axe x en secondes)_

#### Implémentation concurrente

Les fonctions s'exécutaient indépendamment et presque toutes ont commencé à environ ~ 0ème seconde. Elles ont fonctionné pendant 1 seconde et chaque thread s'est terminé.

Cependant, vous pouvez voir que l'ordre n'est pas le même que dans l'implémentation précédente. Cela est dû au fait qu'elles s'exécutent indépendamment et se terminent à des moments différents. Puisqu'elles ont toutes commencé à peu près au même moment, le parcours s'est terminé en environ la durée d'exécution d'une seule fonction.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Group-2--1-.png)
_Implémentation concurrente (axe x en secondes)_

## Conclusion

J'ai trouvé ce résultat assez amazing car il ne m'a pas fallu plus de quelques concepts et 5-6 lignes supplémentaires pour rendre ce programme **7 fois** plus rapide.

Cette technique peut s'avérer être un grand boost pour votre programme Go si vous pouvez identifier des fonctions qui peuvent s'exécuter indépendamment en même temps. Si vos fonctions nécessitent une synchronisation, vous pouvez utiliser des canaux pour accomplir cette tâche.

Vous pouvez trouver le code utilisé dans cet article ici sur [GitHub](https://github.com/zerefwayne/article-snippets/tree/master/supercharge-dfs-with-goroutines).

## Compléments

1. [https://medium.com/rungo/anatomy-of-goroutines-in-go-concurrency-in-go-a4cb9272ff88](https://medium.com/rungo/anatomy-of-goroutines-in-go-concurrency-in-go-a4cb9272ff88)
2. [https://blog.golang.org/defer-panic-and-recover](https://blog.golang.org/defer-panic-and-recover)
3. [https://medium.com/@houzier.saurav/dfs-and-bfs-golang-d5818ec690d3](https://medium.com/@houzier.saurav/dfs-and-bfs-golang-d5818ec690d3)
4. [https://medium.com/rungo/anatomy-of-channels-in-go-concurrency-in-go-1ec336086adb](https://medium.com/rungo/anatomy-of-channels-in-go-concurrency-in-go-1ec336086adb)