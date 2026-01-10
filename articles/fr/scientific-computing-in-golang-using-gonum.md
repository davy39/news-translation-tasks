---
title: Calcul scientifique en Golang avec le package Gonum
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-04T15:49:21.000Z'
originalURL: https://freecodecamp.org/news/scientific-computing-in-golang-using-gonum
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/freecode_ccexpress.jpeg
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Go Language
  slug: go
- name: golang
  slug: golang
- name: Mathematics
  slug: mathematics
seo_title: Calcul scientifique en Golang avec le package Gonum
seo_desc: 'By Ukeje Chukwuemeriwo Goodness

  In this article, I''ll introduce you to Gonum, a package you can use to perform
  scientific computations in the Go programming language.

  Here''s what we''ll cover in this intermediate tutorial:


  What is Gonum?

  Why use Gonu...'
---

Par Ukeje Chukwuemeriwo Goodness

Dans cet article, je vais vous présenter Gonum, un package que vous pouvez utiliser pour effectuer des calculs scientifiques dans le langage de programmation Go.

### Voici ce que nous allons couvrir dans ce tutoriel intermédiaire :

- Qu'est-ce que Gonum ?
- Pourquoi utiliser Gonum
- Comment installer et configurer Gonum
- Comment effectuer des opérations statistiques en utilisant Gonum
- Comment effectuer des opérations matricielles en utilisant Gonum
- Autres calculs scientifiques supportés par Gonum.


### Prérequis :

- Connaissance de la programmation fonctionnelle en Golang.
- Un IDE Golang avec Go installé (j'utilise Goland et Go 1.17.6, mais vous pouvez utiliser un autre)

## Qu'est-ce que Gonum ?
![Screenshot-from-2022-03-14-05-30-53-1](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-from-2022-03-14-05-30-53-1.png)

[Gonum](https://github.com/gonum/gonum), abréviation de Go Numerical, est un package Golang construit et conçu par [gonum.org](http://gonum.org) pour faciliter les calculs scientifiques dans le langage de programmation Go.

Le package Gonum est similaire à [Numpy](https://numpy.org/) dans le langage de programmation [Python](http://python.org). Numpy offre actuellement plus de fonctionnalités que Gonum, mais les fonctionnalités de Gonum s'améliorent constamment.

Le package Gonum supporte des fonctionnalités pour divers calculs scientifiques comme l'algèbre linéaire, le calcul, les statistiques, les graphes, et bien d'autres.

Dans cet article, nous allons passer en revue diverses fonctions et cas d'utilisation de Gonum.

## Pourquoi utiliser Gonum ?

- La vitesse et la concurrency que Golang offre.
- Les programmes Golang sont plus faciles à maintenir.
- Gonum contient plus d'opérations mathématiques que la bibliothèque standard de Go.
- Gonum est optimisé pour les calculs scientifiques dans divers domaines.

## Comment commencer avec Gonum

Pour commencer avec Gonum, vous devez installer le package depuis [Github](https://github.com/gonum/gonum) sur votre terminal en utilisant la commande :

```go
go get -u gonum.org/v1/gonum/
```

Cette commande devrait afficher un message de succès d'installation. Si ce n'est pas le cas, mettez à jour votre Go vers une version plus récente et réessayez.

## Opérations statistiques avec Gonum

Le package Gonum fournit une bibliothèque pour les calculs statistiques. Cette bibliothèque contient de nombreuses fonctions que vous pouvez consulter [ici](https://pkg.go.dev/gonum.org/v1/gonum@v0.9.3/stat).

Dans ce tutoriel, je vais passer en revue les fonctions rudimentaires de la bibliothèque, spécifiquement pour les mesures de tendance centrale (moyenne, médiane, mode).

Importez la bibliothèque stats dans le package `gonum` comme ceci :

```go
import "gonum.org/v1/gonum/stat"
```

![carbon--1-](https://www.freecodecamp.org/news/content/images/2022/03/carbon--1-.png)

- **Moyenne** : `stat.Mean` retourne la valeur moyenne d'une tranche de type `float64`. Elle prend une tranche et un [poids](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean) qui peut être nil ou une tranche correspondante pour laquelle la tranche est pondérée.

```go
func mean() {
   values := []float64{1, 2, 3, 4, 5, 6}
   weights := []float64{1, 1, 1, 1, 1, 1} //a les mêmes effets que nil
   fmt.Println(stat.Mean(values, weights))
}
```

**Sortie : 3.5**

- **Médiane** : `stat.Quantile`, il n'y a pas de fonction explicite pour la médiane dans gonums/stat. Mais nous pouvons utiliser `stat.Quantile` en passant une tranche triée en important le module `sort`.
    
`stat.Quantile` prend une position, la tranche, un [type de cumulant](https://github.com/gonum/gonum/blob/v0.9.3/stat/stat.go#L1039) et un poids. L'argument de position `p` est un float allant de 0 à 1, et le type de cumulant est `stat.Empirical` ou `stat.LinInterp`. 

Dans ce cas, nous utilisons `stat.Empirical`, qui retourne la valeur à la position spécifiée `p`.
    
    ```go
    import (
    	"gonum.org/v1/gonum/stat"
    	"sort"
    )
    
    func median() {
    	values := []float64{10, 20, 25, 30, 45, 70, 30}
    	sort.Float64s(values) //trie le float
    	fmt.Println(stat.Quantile(0.5, stat.Empirical, values, nil))
    }
    ```
    

**Sortie : 30**

- **Mode** : `stat.Mode`. Tout comme `stat.Mean`, elle prend une tranche de valeurs et une tranche de poids, et retourne l'élément le plus fréquent ainsi que le nombre d'occurrences de l'élément.

```go
func mode() {
   values := []float64{10, 20, 25, 30, 45, 70, 30}
   fmt.Println(stat.Mode(values, nil))
}
```

**Sortie : 30  2**

## Opérations matricielles avec Gonum

Gonum supporte les opérations matricielles dans le [`mat package`](https://pkg.go.dev/gonum.org/v1/gonum/mat). 

```go
import "gonum.org/v1/gonum/mat"
```

### Comment créer une matrice :

`mat.NewDense` est la méthode pour créer une matrice. Elle prend les dimensions de la matrice et les données à passer, qui peuvent être nil (une matrice avec toutes les entités égales à zéro).

`mat.NewDense` retourne un pointeur vers l'objet matrice qui peut être déréférencé.

La matrice nulle sert de matrice pour les exemples dans ce tutoriel.

```go
func null(){
  matrix := mat.NewDense(3, 3, nil)
  fmt.Println(*matrix)
}
```

**Sortie :**

```markdown
{{3 3 [0 0 0 0 0 0 0 0 0] 3} 3 3}
```

### Comment formater la sortie de la matrice

Imprimer une matrice Gonum sans formatage retourne un pointeur vers la matrice dans ce format `{{3 3 [0 0 0 0 0 0 0 0 0] 3} 3 3}`. 

Pour afficher un tableau bidimensionnel, nous utilisons `mat.Formatted` qui prend l'objet matrice, un préfixe et une option de format qui, dans ce cas, nous utilisons `mat.Squeeze`.

```go
func format(matrix mat.Matrix) {
	formatted := mat.Formatted(matrix, mat.Prefix(""), mat.Squeeze())
	fmt.Println(formatted)
}
```

**Sortie :**

```markdown
⎡0  0  0⎤
⎢0  0  0⎥
⎣0  0  0⎦
```

### Comment définir les valeurs de la matrice

Pour entrer une valeur dans une position dans la matrice, nous utilisons `.Set` sur l'objet matrice. `matrix.Set` prend trois arguments ou plus comme suit :

`matrix.Set(rowNumber, columnNumber, element)`.

```go
func input(){
	matrix.Set(1, 2, 3.0)
}
```

**Sortie :**

```markdown
⎡0  0  0⎤
⎢0  0  3⎥
⎣0  0  0⎦
```

### Comment obtenir les valeurs de la matrice

Récupérer les valeurs dans la matrice se fait en utilisant `.At` sur l'objet matrice, qui prend les numéros de ligne et de colonne, respectivement.

Ici, nous récupérons l'élément que nous avons défini dans l'exemple ci-dessus :

```go
func retriever(){
	getElement := matrix.At(1, 2)
	fmt.Println(getElement)
}
```

**Sortie : 3**

### Comment transposer une matrice

Transposer une matrice implique l'échange de lignes et de colonnes dans une matrice de sorte que les lignes soient définies comme colonnes et vice-versa.

La méthode `.T` sur l'objet matrice transpose la matrice.

```go
func transposer(){
	format(null.T())
}
```

Ici, nous transposons la sortie de la matrice de l'exemple défini.

**Sortie :**

```markdown
⎡0  0  0⎤
⎢0  0  0⎥
⎣0  3  0⎦
```

### Déterminant d'une matrice

Vous pouvez évaluer le déterminant d'une matrice en utilisant la méthode `mat.Det` qui prend la matrice et retourne son déterminant.

```go
func determinant(){
	determinant := mat.Det(matrix)
	fmt.Println(determinant)
}
```

**Sortie** : 0


### Comment ajouter des lignes et des colonnes aux matrices

Vous pouvez ajouter une nouvelle ligne ou colonne en utilisant `.SetRow` et `.SetCol`. Ces méthodes prennent un numéro de ligne et une tranche de valeurs de dimension similaire.

Cela met à jour les lignes et les colonnes de la matrice :

```go
values := []float64{1, 2, 3}
matrix.SetCol(0, values)
matrix.SetRow(1, values)
```

**Sortie :**

```markdown
⎡1  0  0⎤
⎢1  2  3⎥
⎣3  0  0⎦
```

## Autres packages Gonum

Gonum a plus de packages pour le calcul scientifique :

- [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.11.0/blas) → fournit des interfaces pour le standard BLAS (**Basic Linear Algebra Subprograms)**
- [diff](https://pkg.go.dev/gonum.org/v1/gonum@v0.11.0/diff/fd) → Fonctions pour le calcul différentiel
- [graph](https://pkg.go.dev/gonum.org/v1/gonum@v0.11.0/graph) → interfaces pour les graphes
- [integrate](https://pkg.go.dev/gonum.org/v1/gonum@v0.11.0/integrate) → Fonctions pour le calcul intégral
- [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.11.0/lapack) → fournit des interfaces pour le standard LAPACK (Linear Algebra Package)
- [mathext](https://pkg.go.dev/gonum.org/v1/gonum@v0.11.0/mathext) → Fonctions mathématiques spéciales qui ne sont pas incluses dans la bibliothèque standard de Go
- [unit](https://pkg.go.dev/gonum.org/v1/gonum@v0.11.0/unit) → Types et constantes pour une utilisation facile des unités SI

## Conclusion

Dans cet article, vous avez appris les calculs scientifiques en Golang en utilisant le package Gonum.

Nous avons discuté des calculs statistiques et matricielles dans Gonum et passé en revue d'autres modules de calcul scientifique dans le package Gonum. 

Travailler avec d'autres modules dans le package Gonum est assez simple et similaire à ceux que nous avons discutés ici.