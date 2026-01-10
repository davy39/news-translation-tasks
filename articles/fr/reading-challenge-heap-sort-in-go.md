---
title: Comment implémenter Heap-Sort dans la bibliothèque standard de Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-12T04:00:00.000Z'
originalURL: https://freecodecamp.org/news/reading-challenge-heap-sort-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/heap_cars.jpeg
tags:
- name: Go Language
  slug: go
- name: General Programming
  slug: programming
seo_title: Comment implémenter Heap-Sort dans la bibliothèque standard de Go
seo_desc: 'By Ehud Tamir

  Heap-sort is a beautiful sorting algorithm. It uses a max-heap to sort a sequence
  of numbers or other elements with a defined order relation. In this article we’ll
  deep-dive into the Go standard library heap-sort implementation.

  Max-hea...'
---

Par Ehud Tamir

Heap-sort est un bel algorithme de tri. Il utilise un max-heap pour trier une séquence de nombres ou d'autres éléments avec une relation d'ordre définie. Dans cet article, nous allons plonger en profondeur dans l'implémentation de **heap-sort de la bibliothèque standard de Go**.

# Max-heap

D'abord, un bref rappel sur les [**binary max-heaps**](https://en.wikipedia.org/wiki/Heap_(data_structure)). Un max-heap est un conteneur qui fournit son élément maximum en temps O(1), ajoute un élément en O(log n), et supprime l'**élément maximum** en O(log n).

Les max-heaps sont des arbres binaires **presque complets**, où **chaque nœud est supérieur ou égal à ses enfants**. Je me référerai à ce dernier comme **la propriété de heap** tout au long de l'article.

Ensemble, ces deux propriétés définissent un max-heap :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-117.png)
_Un Max heap. Par Ermishin — Travail personnel, CC BY-SA 3.0, [https://commons.wikimedia.org/w/index.php?curid=12251273](https://commons.wikimedia.org/w/index.php?curid=12251273)_

Dans les algorithmes de heap, un max-heap est représenté comme un tableau. Dans la représentation de tableau, les enfants du nœud à l'index `i` sont situés aux indices `2*i+1` et `2*i+2`. Ce tableau de Wikipedia montre la représentation de tableau :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-118.png)
_Max-heap représenté comme un tableau. Par Maxiantor — Travail personnel, CC BY-SA 4.0, [https://commons.wikimedia.org/w/index.php?curid=55590553](https://commons.wikimedia.org/w/index.php?curid=55590553)_

## Construire un heap

Un tableau peut être converti en un max-heap en temps O(n). Incroyable, n'est-ce pas ? Voici l'algorithme :

1. Traitez le tableau d'entrée comme un heap. Il ne satisfait pas encore la propriété de heap.
2. Parcourez les nœuds du heap en commençant par le niveau avant-dernier du heap — c'est un niveau au-dessus des feuilles — en remontant vers la racine.
3. Pour chaque nœud rencontré, propagez-le vers le bas dans le heap, jusqu'à ce qu'il soit plus grand que ses deux enfants. Lors de la propagation vers le bas, échangez toujours avec l'enfant le plus grand.

C'est tout ! Vous avez terminé !

Pourquoi cela fonctionne-t-il ? Je vais essayer de vous convaincre avec cette preuve approximative (n'hésitez pas à sauter cette partie) :

* Prenez un nœud d'arbre `x`. Parce que nous parcourons le heap de l'arrière vers l'avant, lorsque nous l'atteignons, les sous-arbres enracinés dans ses deux enfants satisfont déjà la propriété de heap.
* Si `x` est plus grand que ses deux enfants, nous avons terminé.
* Sinon, nous échangeons `x` avec son plus grand enfant. Cela fait que la nouvelle racine du sous-arbre est plus grande que ses deux enfants.
* Si `x` ne satisfait pas la propriété de heap dans son nouveau sous-arbre, le processus sera répété jusqu'à ce qu'il le fasse ou devienne une feuille, auquel cas il n'aura plus d'enfants.

Cela est vrai pour tous les nœuds du heap, y compris la racine.

# Algorithme Heap-sort

Maintenant, le plat principal — heap-sort.

Heap-sort fonctionne en 2 étapes :

1. Construit un max-heap à partir du tableau d'entrée en utilisant l'algorithme que j'ai montré ci-dessus. Cela prend O(n) temps
2. Extrait les éléments du heap dans le tableau de sortie, le remplissant de l'arrière vers l'avant. Chaque suppression de l'élément maximum du heap prend O(log n) temps, ce qui s'accumule à O(n * log n) pour l'ensemble du conteneur.

Une propriété intéressante de l'implémentation Go est qu'elle utilise le tableau d'entrée pour stocker la sortie, évitant ainsi le besoin d'allouer O(n) mémoire pour la sortie.

# Implémentation de Heap-sort

La bibliothèque de tri Go prend en charge toute collection qui est **indexée par des entiers**, a une **relation d'ordre définie** sur ses éléments, et **prend en charge l'échange** d'éléments entre deux indices :

```go
type Interface interface {
	// Len est le nombre d'éléments dans la collection.
	Len() int
	// Less indique si l'élément avec
	// l'index i doit être trié avant l'élément avec l'index j.
	Less(i, j int) bool
	// Swap échange les éléments avec les index i et j.
	Swap(i, j int)
}
```

Naturellement, tout conteneur contigu de nombres peut satisfaire cette interface.

Maintenant, examinons le corps de `heapSort()` :

```go
func heapSort(data Interface, a, b int) {
	first := a
	lo := 0
	hi := b - a

	// Construire un heap avec le plus grand élément en haut.
	for i := (hi - 1) / 2; i >= 0; i-- {
		siftDown(data, i, hi, first)
	}

	// Extraire les éléments, du plus grand au plus petit, à la fin des données.
	for i := hi - 1; i >= 0; i-- {
		data.Swap(first, first+i)
		siftDown(data, lo, i, first)
	}
}
```

La signature de la fonction est un peu cryptique, mais les trois premières lignes clarifient les choses :

* `a` et `b` sont des indices dans `data`. `heapSort(data, a, b)` trie `data` dans la plage semi-ouverte `[a, b)`.
* `first` est une copie de `a`.
* `lo` et `high` sont des indices normalisés par `a` — `lo` commence toujours à zéro, et `hi` à la taille de l'entrée.

Ensuite, le code construit le max-heap :

```go
// Construire un heap avec le plus grand élément en haut.
for i := (hi - 1) / 2; i >= 0; i-- {
  siftDown(data, i, hi, first)
}
```

Comme nous l'avons vu précédemment, le code parcourt le heap à partir d'un niveau au-dessus des feuilles et utilise `siftDown()` pour propager l'élément actuel vers le bas jusqu'à ce qu'il satisfasse la propriété de heap. Je vais entrer dans les détails de `siftDown()` ci-dessous.

À ce stade, `data` est un max-heap.

Ensuite, nous extrayons tous les éléments pour créer le tableau trié :

```go
// Extraire les éléments, du plus grand au plus petit, à la fin des données.
for i := hi - 1; i >= 0; i-- {
  data.Swap(first, first+i)
  siftDown(data, lo, i, first)
}
```

Dans cette boucle, `i` est le dernier index dans le heap. À chaque itération :

* Le maximum du heap `first` est échangé avec le dernier élément du heap.
* La propriété de heap est restaurée en propageant le nouveau `first` vers le bas jusqu'à ce qu'il satisfasse la propriété de heap.
* La taille du heap `i` est réduite de un.

En d'autres termes, nous remplissons le tableau de l'arrière vers l'avant, en commençant par le plus grand élément, jusqu'au 2ème élément en taille, jusqu'au plus petit élément. Le résultat est l'entrée triée.

## Maintenir la propriété de heap

Tout au long de l'article, j'ai mentionné l'utilisation de `siftDown()` pour maintenir la propriété de heap. Voyons comment cela fonctionne :

```go
// siftDown implémente la propriété de heap sur data[lo, hi).
// first est un décalage dans le tableau où se trouve la racine du heap.
func siftDown(data Interface, lo, hi, first int) {
	root := lo
	for {
		child := 2*root + 1
		if child >= hi {
			break
		}
		if child+1 < hi && data.Less(first+child, first+child+1) {
			child++
		}
		if !data.Less(first+root, first+child) {
			return
		}
		data.Swap(first+root, first+child)
		root = child
	}
}
```

Ce code propage l'élément dans `root` tout au long de l'arbre jusqu'à ce qu'il soit plus grand que ses deux enfants. Lors de la descente d'un niveau, l'élément sera échangé avec son enfant le plus grand. Cela est fait pour s'assurer que le nouveau nœud parent est plus grand que ses deux enfants :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-119.png)
_Le parent '3' est échangé avec le plus grand enfant '10'_

Les premières lignes calculent l'index du premier enfant et vérifient qu'il existe :

```go
child := 2*root + 1
if child >= hi {
  break
}

```

`child >= hi` signifie que le `root` actuel est une feuille, donc l'algorithme s'arrête.

Ensuite, nous choisissons le plus grand des deux enfants :

```go
if child+1 < hi && data.Less(first+child, first+child+1) {
  child++
}
```

Puisque les enfants de tout nœud sont côte à côte dans le tableau, `child++` sélectionne le deuxième enfant.

Ensuite, nous vérifions si le parent est effectivement plus petit que l'enfant :

```go
if !data.Less(first+root, first+child) {
  return
}
```

Si le parent est plus grand que son plus grand enfant, nous avons terminé, donc nous retournons.

Enfin, si le parent est plus petit que l'enfant, nous échangeons les deux éléments et incrémentons `root` pour préparer la prochaine itération :

```go
data.Swap(first+root, first+child)
root = child
```

# Conclusion

Ceci est le troisième article où je lis un morceau de code inconnu et essaie de l'expliquer. J'aime ce genre d'expérience car cela m'apprend à lire du code et à communiquer à ce sujet. Veuillez laisser vos commentaires et retours ci-dessous !