---
title: L'itération en Golang – Comment boucler sur les structures de données en Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-26T22:44:22.000Z'
originalURL: https://freecodecamp.org/news/iteration-in-golang
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/How-to-perform-iteration-in-Golang-1.png
tags:
- name: data structures
  slug: data-structures
- name: Go Language
  slug: go
- name: golang
  slug: golang
- name: Loops
  slug: loops
seo_title: L'itération en Golang – Comment boucler sur les structures de données en
  Go
seo_desc: 'By Ubaydah Abdulwasiu

  In programming, iteration (commonly known as looping) is a process where a step
  is repeated n number of times until a specific condition is met.

  Just like every other programming language, Golang has a way of iterating through
  d...'
---

Par Ubaydah Abdulwasiu

En programmation, l'itération (communément appelée boucle) est un processus où une étape est répétée n fois jusqu'à ce qu'une condition spécifique soit remplie.

Comme tout autre langage de programmation, Golang permet d'itérer à travers différentes structures et types de données tels que les structs, les maps, les tableaux (arrays), les chaînes de caractères (strings), et ainsi de suite.

Dans cet article, vous apprendrez :

* Comment boucler sur les tableaux
* Comment boucler sur les chaînes de caractères
* Comment boucler sur les maps
* Comment boucler sur les structs

## Comment boucler sur les tableaux et les slices en Go

Les tableaux sont des structures de données puissantes qui stockent des types de données similaires. Vous pouvez identifier et accéder aux éléments qu'ils contiennent par leur index.

En Golang, vous pouvez boucler sur un tableau en utilisant une boucle `for` en initialisant une variable i à 0 et en incrémentant la variable jusqu'à ce qu'elle atteigne la longueur du tableau.

La syntaxe est présentée ci-dessous :

```go
for i := 0; i < len(arr); i++ {
    // effectuer une opération
}
```

À titre d'exemple, bouclons sur un tableau d'entiers :

```go
package main

import (
	"fmt"
)

func main() {
	numbers := []int{7, 9, 1, 2, 4, 5}

	for i := 0; i < len(numbers); i++ {
		fmt.Println(numbers[i])

	}
}
```

Dans le code ci-dessus, nous avons défini un tableau d'entiers nommé `numbers` et nous avons bouclé dessus en initialisant une variable `i`. Nous avons ensuite affiché la valeur de chaque index du tableau tout en incrémentant `i`.

Le code ci-dessus affiche ce qui suit :

```
7
9
1
2
4
5
```

Nous pouvons également boucler sur un tableau en utilisant le mot-clé `range` qui itère sur toute la longueur d'un tableau. 

La syntaxe est présentée ci-dessous :

```go
for index, arr := range arr {
  // effectuer une opération	
}
```

Par exemple :

```go
package main

import (
	"fmt"
)

func main() {
	arr := []string{"a", "b", "c", "d", "e", "f"}

	for index, a := range arr {
		fmt.Println(index, a)
	}

}
```

Dans le code ci-dessus, nous avons défini un tableau de chaînes de caractères et bouclé à la fois sur son index et sa valeur en utilisant le mot-clé `for..range`. 

Le `for...range` a une syntaxe plus simple et est plus facile à comprendre. Vous l'utilisez pour itérer sur différentes structures de données comme les tableaux, les chaînes de caractères, les maps, les slices, et ainsi de suite. 

Ceci affiche ce qui suit : 

```
0 a
1 b
2 c
3 d
4 e
5 f
```

Si nous voulions ignorer l'index et simplement afficher les éléments du tableau, il suffirait de remplacer la variable `index` par un underscore.

Par exemple :

```go 
package main

import (
	"fmt"
)

func main() {
	arr := []string{"a", "b", "c", "d", "e", "f"}

	for _, a := range arr {
		fmt.Println(a)
	}

}
```

Dans le code ci-dessus, nous avons modifié l'exemple précédent et remplacé la variable `index` par un underscore. Nous avons fait cela pour ignorer l'index et afficher les éléments du tableau à la place.

Ceci affiche ce qui suit :

```
a
b
c
d
e
f
```

## Comment boucler sur les chaînes de caractères en Go

Les chaînes de caractères en programmation sont immuables – cela signifie que vous ne pouvez pas les modifier après les avoir créées. Ce sont des séquences ordonnées d'un ou plusieurs caractères (comme des lettres, des chiffres ou des symboles) qui peuvent être soit une constante, soit une variable.

En Golang, les [strings](https://golangbot.com/strings/) sont différentes des autres langages comme Python ou JavaScript. Elles sont représentées comme une [séquence d'octets UTF-8](https://naveenr.net/unicode-character-set-and-utf-8-utf-16-utf-32-encoding/) et chaque élément d'une chaîne représente un octet.

Vous bouclez sur les chaînes de caractères en utilisant la boucle `for...range` ou en utilisant une boucle classique. 

Par exemple :

```go
package main

import (
	"fmt"
)

func main() {
	word := "Ab$du"

	for index, a := range word {
		fmt.Println(index, string(a))
	}
}
```

Dans le code ci-dessus, nous avons défini une chaîne contenant différents caractères et bouclé sur ses entrées. Les chaînes sont représentées par des octets en Golang, c'est pourquoi nous avons dû convertir chaque valeur vers le type `string` lors de leur affichage. 

Ceci affiche :

```
0 A
1 b
2 $
3 d
4 u
```

Si nous n'avions pas converti chaque entrée en chaîne, Golang afficherait la représentation en octets à la place.

Par exemple :

```go
package main

import (
	"fmt"
)

func main() {
	word := "Ab$du"

	for index, a := range word {
		fmt.Println(index, a)
	}
}
```

Ceci affiche :

```
0 65
1 98
2 36
3 100
4 117
```

Nous pouvons également itérer à travers la chaîne en utilisant une boucle `for` classique.

```go
package main

import (
	"fmt"
)

func main() {
	word := "ab$du"

	for i := 0; i < len(word); i++ {
		fmt.Println(i, string(word[i]))
	}
}
```

## Comment boucler sur les maps en Go

En Golang, une map est une structure de données qui stocke des éléments sous forme de paires clé-valeur, où les clés sont utilisées pour identifier chaque valeur dans une map. C'est similaire aux dictionnaires et aux hashmaps dans d'autres langages comme Python et Java.

Vous pouvez itérer à travers une `map` en Golang en utilisant l'instruction `for...range` où elle récupère la clé et sa valeur correspondante. 

Par exemple :

```go
package main

import (
	"fmt"
)

func main() {
	books := map[string]int{
		"maths":     5,
		"biology":   9,
		"chemistry": 6,
		"physics":   3,
	}
	for key, val := range books {
		fmt.Println(key, val)
	}
}
```

Dans le code ci-dessus, nous avons défini une map stockant les détails d'une librairie avec le type `string` comme clé et le type `int` comme valeur. Nous avons ensuite bouclé sur ses clés et valeurs en utilisant le mot-clé `for..range`. 

L'itération à travers une map en Golang n'a pas d'ordre spécifié, et nous ne devrions pas nous attendre à ce que les clés soient renvoyées dans l'ordre où nous les avons définies lors de la boucle.

Ce code affiche :

```
physics 3
maths 5
biology 9
chemistry 6
```

Si nous ne voulons pas spécifier les valeurs et renvoyer uniquement les clés à la place, nous ne définissons simplement pas de variable de valeur et définissons uniquement une variable de clé.

Par exemple :

```go
package main

import (
	"fmt"
)

func main() {
	books := map[string]int{
		"maths":     5,
		"biology":   9,
		"chemistry": 6,
		"physics":   3,
	}
	for key := range books {
		fmt.Println(key)
	}
}
```

Ceci affiche ce qui suit :

```
maths
biology
chemistry
physics
```

De même, si nous ne sommes pas intéressés par les clés d'une map, nous utilisons un underscore pour ignorer les clés et définissons une variable pour la valeur.

Par exemple :

```go
package main

import (
	"fmt"
)

func main() {
	books := map[string]int{
		"maths":     5,
		"biology":   9,
		"chemistry": 6,
		"physics":   3,
	}
	for _, val := range books {
		fmt.Println(val)
	}
}
```

Ceci affiche :

```
5
9
6
3
```

## Comment boucler sur les structs en Go

Une struct est une structure de données en Golang que vous utilisez pour combiner différents types de données en un seul. Contrairement à un tableau, une struct peut contenir des entiers, des chaînes, des booléens et plus encore – le tout au même endroit.

Contrairement à une map, où nous pouvons facilement boucler sur ses clés et valeurs, boucler sur une struct en Golang nécessite l'utilisation d'un package appelé `reflect`. Cela vous permet de manipuler un objet avec un type arbitraire.

Par exemple, créons une struct et bouclons dessus :

```go
package main

import (
	"fmt"
	"reflect"
)

type Person struct {
	Name   string
	Age    int
	Gender string
	Single bool
}

func main() {
	ubay := Person{
		Name:   "John",
		Gender: "Female",
		Age:    17,
		Single: false,
	}
	values := reflect.ValueOf(ubay)
	types := values.Type()
	for i := 0; i < values.NumField(); i++ {
		fmt.Println(types.Field(i).Index[0], types.Field(i).Name, values.Field(i))
	}
}
```

Ceci affiche :

```
0 Name John
1 Age 17
2 Gender Female
3 Single false
```

Dans le code ci-dessus, nous avons défini une `struct` nommée `Person` avec différents attributs et créé une nouvelle instance de la `struct`. Nous avons ensuite utilisé le package `reflect` pour obtenir les valeurs de la `struct` et son `type`.  

En utilisant la boucle `for` classique, nous avons incrémenté la variable initialisée `i` jusqu'à ce qu'elle atteigne la longueur de la struct. 

Nous utilisons la méthode `NumField` pour obtenir le nombre total de champs dans la struct. La méthode `types.Field(i).Index` renvoie l'index de chaque clé dans une struct. La méthode `types.Field(i).Name` renvoie le nom du champ pour chaque clé de la struct. Et `values.Field(i)` renvoie la valeur pour chaque clé de la struct.

Vous pouvez en apprendre davantage sur le package reflect dans cet article :

%[https://medium.com/capital-one-tech/learning-to-use-go-reflection-822a0aed74b7]

## Conclusion 

Dans cet article, nous avons exploré comment effectuer des itérations sur différents types de données en Golang. 

Bien que vous puissiez boucler sur les tableaux, les maps et les chaînes de caractères à l'aide d'une boucle `for` ou `for..range`, les structs nécessitent un package supplémentaire appelé `reflect` pour boucler sur leurs clés et valeurs.

J'espère que cet article vous aidera à mieux comprendre l'itération en Golang.

Merci de votre lecture.