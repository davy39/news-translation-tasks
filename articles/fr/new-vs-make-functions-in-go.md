---
title: Les fonctions new() vs make() en Go – Quand utiliser chacune
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2024-01-04T15:44:43.000Z'
originalURL: https://freecodecamp.org/news/new-vs-make-functions-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/pexels-skitterphoto-422844.jpg
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Les fonctions new() vs make() en Go – Quand utiliser chacune
seo_desc: "Go, also known as Golang, is a statically-typed, compiled programming language\
  \ designed for simplicity and efficiency. \nWhen it comes to working with data structures\
  \ like slices, maps, and channels, you'll likely encounter the new() and make()\
  \ functi..."
---

Go, également connu sous le nom de Golang, est un langage de programmation statiquement typé et compilé, conçu pour la simplicité et l'efficacité. 

Lorsqu'il s'agit de travailler avec des structures de données comme les slices, les maps et les channels, vous rencontrerez probablement les fonctions `new()` et `make()`. Bien que les deux soient utilisées pour l'allocation de mémoire, elles servent des objectifs distincts. 

Dans cet article, nous explorerons les différences entre `new()` et `make()` en Go et discuterons de quand utiliser chacune.

## La fonction `new()`

La fonction `new()` en Go est une fonction intégrée qui alloue de la mémoire pour une nouvelle valeur mise à zéro d'un type spécifié et retourne un pointeur vers celle-ci. Elle est principalement utilisée pour initialiser et obtenir un pointeur vers une nouvelle valeur mise à zéro d'un type donné, généralement pour des types de données comme les structs.

Voici un exemple simple :

```go
package main

import "fmt"

type Person struct {
    Name 	string
    Age  	int
    Gender 	string
}

func main() {
    // Utilisation de new() pour allouer de la mémoire pour une struct Person
    p := new(Person)

    // Initialisation des champs
    p.Name = "John Doe"
    p.Age = 30
    p.Gender = "Male"

    fmt.Println(p)
}

```

Dans cet exemple, `new(Person)` alloue de la mémoire pour une nouvelle struct `Person`, et `p` est un pointeur vers la nouvelle valeur mise à zéro.

## La fonction `make()`

En revanche, la fonction `make()` est utilisée pour initialiser les slices, les maps et les channels – des structures de données qui nécessitent une initialisation à l'exécution. Contrairement à `new()`, `make()` retourne une valeur initialisée (non mise à zéro) d'un type spécifié.

Regardons un exemple utilisant une slice :

```go
package main

import "fmt"

func main() {
    // Utilisation de make() pour créer une slice avec une longueur et une capacité spécifiées
    s := make([]int, 10, 15)

    // Initialisation des éléments
    for i := 0; i < 10; i++ {
        s[i] = i + 1
    }

    fmt.Println(s)
}

```

Dans cet exemple, `make([]int, 10, 15)` crée une slice d'entiers avec une longueur de 10 et une capacité de 15. La fonction `make()` garantit que la slice est initialisée avec des valeurs non nulles.

## Quand utiliser `new()` et `make()` en Go

### Utilisez `new()` pour les types de valeur

Lorsqu'il s'agit de types de valeur comme les structs, vous pouvez utiliser `new()` pour allouer de la mémoire pour une nouvelle valeur mise à zéro. Cela convient aux scénarios où vous voulez un pointeur vers une structure initialisée.

```go
p := new(Person)
```

### Utilisez `make()` pour les types de référence :

Pour les slices, les maps et les channels, où l'initialisation implique la configuration de structures de données et de pointeurs internes, utilisez `make()` pour créer une instance initialisée.

```go
s := make([]int, 5, 10)
```

### Pointeur vs. Valeur :

Gardez à l'esprit que `new()` retourne un pointeur, tandis que `make()` retourne une valeur non mise à zéro. Choisissez la méthode appropriée en fonction de vos besoins en pointeur ou en valeur initialisée.

## Conclusion

Comprendre la distinction entre `new()` et `make()` en Go est crucial pour écrire un code propre et efficace. En utilisant la bonne méthode pour les types de données appropriés, vous pouvez garantir une allocation et une initialisation correctes de la mémoire dans vos programmes Go.