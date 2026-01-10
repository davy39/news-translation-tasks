---
title: Les génériques en Go expliqués avec des exemples de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-23T16:49:55.000Z'
originalURL: https://freecodecamp.org/news/generics-in-golang
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6048ce09a7946308b7685b45.jpg
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Les génériques en Go expliqués avec des exemples de code
seo_desc: "By Pramono Winata\nGenerics were proposed a few years ago for Go, and they\
  \ have finally been accepted into the language earlier this year. And they're scheduled\
  \ to be officially released at the end of this year. \nHow will Generics really\
  \ affect Go? Wi..."
---

Par Pramono Winata

Les génériques ont été proposés il y a quelques années pour Go, et ils ont finalement été acceptés dans le langage plus tôt cette année. Et ils sont prévus pour être officiellement publiés à la fin de cette année. 

Comment les génériques vont-ils vraiment affecter Go ? Vont-ils changer la façon dont nous codons ? 

Pour vraiment répondre à ces questions, nous devrons examiner comment fonctionnent les génériques. Heureusement, les développeurs nous ont fourni un [compilateur web](https://go2goplay.golang.org/) où nous pouvons expérimenter nous-mêmes avec les génériques.

## Que changent vraiment les génériques en Go ?

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-316.png)
_Photo par [Unsplash](https://unsplash.com/@anniespratt?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Annie Spratt</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Les génériques permettent à nos fonctions ou structures de données de prendre en charge plusieurs types qui sont définis sous leur forme générique.

Pour vraiment comprendre ce que cela signifie, prenons un exemple très simple.

Supposons que vous deviez créer une fonction qui prend une tranche et l'imprime. Vous pourriez écrire ce type de fonction :

```go
func Print(s []string) {
	for _, v := range s {
		fmt.Print(v)
	}
}
```

Simple, n'est-ce pas ? Et si nous voulons que la tranche soit un entier ? Vous devrez créer une nouvelle méthode pour cela :

```
func Print(s []int) {
	for _, v := range s {
		fmt.Print(v)
	}
}
```

Ces solutions peuvent sembler redondantes, car nous ne changeons que le paramètre. Mais actuellement, c'est ainsi que nous le résolvons en Go sans recourir à une interface.

Et maintenant avec les génériques, ils nous permettront de déclarer nos fonctions comme ceci :

```
func Print[T any](s []T) {
	for _, v := range s {
		fmt.Print(v)
	}
}
```

Dans la fonction ci-dessus, nous déclarons deux choses :

1. Nous avons T, qui est le type du mot-clé `any` (ce mot-clé est spécifiquement défini comme faisant partie d'un générique, ce qui indique n'importe quel type)
2. Et notre paramètre, où nous avons la variable `s` dont le type est une tranche de `T`.

Nous pourrons maintenant appeler notre méthode comme ceci :

```go
func main() {
	Print([]string{"Hello, ", "playground\n"})
	Print([]int{1,2,3})
}

```

Une méthode pour n'importe quel type de variable – sympa, non ?

Ce n'est qu'une des implémentations très basiques pour les génériques. Mais cela semble bien pour l'instant. 

Explorons davantage et voyons jusqu'où les génériques peuvent nous mener.

## Limites des génériques

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-317.png)
_Photo par [Unsplash](https://unsplash.com/@nickeedoo?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Nick Tiemeyer</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Nous avons vu ce que les génériques peuvent faire. Ils nous permettent de spécifier une fonction qui peut prendre en charge n'importe quel type de paramètre.

Mais l'exemple que j'ai donné précédemment était très simple. Il y a des limites à ce que les génériques peuvent faire pour nous. L'impression, par exemple, est assez simple puisque Golang peut imprimer n'importe quel type de variable qui lui est soumis.

Que se passe-t-il si nous voulons faire des choses plus complexes ? Supposons que nous avons défini nos propres méthodes pour une structure et que nous voulons les appeler :

```go
package main

import (
	"fmt"
)

type worker string

func (w worker) Work(){
	fmt.Printf("%s is working\n", w)
}


func DoWork[T any](things []T) {
    for _, v := range things {
        v.Work()
    }
}

func main() {
	var a,b,c worker
	a = "A"
	b = "B"
	c = "C"
	DoWork([]worker{a,b,c})	
}

```

Et vous obtiendrez ceci :

```
type checking failed for main
prog.go2:25:11: v.Work undefined (type bound for T has no method Work)
```

Il échoue à s'exécuter parce que la tranche traitée à l'intérieur de la fonction est de type `any` et elle n'implémente pas la méthode `Work`, ce qui fait qu'elle échoue à s'exécuter.

Nous pouvons en fait la faire fonctionner, cependant, en utilisant une interface :

```go
package main

import (
	"fmt"
)

type Person interface {
    Work()
}

type worker string

func (w worker) Work(){
	fmt.Printf("%s is working\n", w)
}

func DoWork[T Person](things []T) {
    for _, v := range things {
        v.Work()
    }
}

func main() {
	var a,b,c worker
	a = "A"
	b = "B"
	c = "C"
	DoWork([]worker{a,b,c})
}

```

Et cela imprimera ceci :

```
A is working
B is working
C is working
```

Cela fonctionne avec l'interface, mais avoir simplement une interface sans le générique fonctionne bien aussi :

```go
package main

import (
	"fmt"
)

type Person interface {
    Work()
}

type worker string

func (w worker) Work(){
	fmt.Printf("%s is working\n", w)
}

func DoWorkInterface(things []Person) {
    for _, v := range things {
        v.Work()
    }
}

func main() {
	var d,e,f worker
	d = "D"
	e = "E"
	f = "F"
	DoWorkInterface([]Person{d,e,f})
}

```

Cela nous donnera le résultat suivant :

```
D is working
E is working
F is working
```

L'utilisation des génériques ajoutera simplement une logique supplémentaire à notre code. Donc, si l'utilisation de l'interface seule est suffisante, je ne vois aucune raison d'ajouter des génériques au code. 

Les génériques sont encore dans leurs phases de développement très précoces, et ils ont encore leurs limites pour le traitement complexe.

## Jouer avec les contraintes

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-318.png)
_Photo par [Unsplash](https://unsplash.com/@pbrandao?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Paulo Brandao</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Plus tôt, nous avons rencontré le type `any` pour notre contrainte générique. En plus de ce type, il existe plusieurs autres contraintes que nous pouvons utiliser.

L'une des contraintes est `comparable`. Voyons comment cela fonctionne :

```go
func Equal[T comparable](a, b T) bool {
    return a == b
}

func main() {
	Equal("a","a")
}
```

En plus de cela, nous pouvons également essayer de créer notre propre contrainte comme ceci :

```go
package main

import(
	"fmt"
)

type Number interface {
    type int, float64
}

func MultiplyTen[T Number](a T) T{
	return a*10
}

func main() {
	fmt.Println(MultiplyTen(10))
	fmt.Println(MultiplyTen(5.55))
}
```

Et je pense que c'est assez sympa – nous pouvons avoir une fonction pour une expression mathématique simple. Habituellement, nous finissons par créer deux fonctions pour la prendre en charge ou nous utilisons la réflexion pour n'écrire qu'une seule fonction.

Bien que ce soit assez cool, nous devons encore expérimenter beaucoup avec la création de nos propres contraintes. Il est encore trop tôt pour connaître leurs limites. Et nous devons être prudents pour ne pas en abuser et ne l'utiliser que si nous sommes vraiment sûrs qu'il est nécessaire.

## Autres façons d'utiliser les génériques

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-319.png)
_Photo par [Unsplash](https://unsplash.com/@jotaemee?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Marcelo Franchi</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

En plus d'utiliser les génériques comme partie d'une fonction, vous pouvez également les déclarer comme variables comme ceci :

```
type GenericSlice[T any] []T
```

Et vous pouvez utiliser ceci soit comme paramètre dans une fonction, soit créer une méthode à partir de ce type :

```go
func (g GenericSlice[T]) Print() {
	for _, v := range g {
		fmt.Println(v)
	}
}

func Print [T any](g GenericSlice[T]) {
	for _, v := range g {
		fmt.Println(v)
	}
}

func main() {
	g := GenericSlice[int]{1,2,3}
	
	g.Print() //1 2 3
	Print(g) //1 2 3
}
```

L'utilisation varie en fonction de vos besoins. Tout ce que je peux dire, c'est que nous devons encore expérimenter davantage avec les génériques pour voir quels cas d'utilisation fonctionnent le mieux.

## Mon avis sur les génériques

Les génériques sont encore dans leurs phases très précoces (ils ne sont même pas encore sortis !), mais je suis assez impressionné par la façon dont ils sont conçus. Il n'y a pas beaucoup de termes compliqués et de bibliothèques nécessaires pour implémenter les génériques, et cette simplicité est géniale.

Il y a plusieurs cas d'utilisation où je peux déjà voir que l'utilisation des génériques sera meilleure (comme le cas avec la méthode multiply). Une chose que beaucoup de gens semblent confondre est que les génériques pourraient être un remplacement pour l'utilisation des interfaces (à la fois le type interface{} et l'implémentation Interface). 

Mon conseil est de ne pas considérer les génériques comme un remplacement pour quoi que ce soit. Les génériques sont juste un autre outil fourni pour nous dans notre vie de codage. De plus, les génériques peuvent sembler sophistiqués et cool, et vous pourriez vouloir les utiliser dans chaque bloc de votre code. Mais ne les utilisez pas à outrance – seulement lorsque cela est vraiment nécessaire, pas lorsque cela peut convenir.

Et c'est tout. Merci d'avoir lu mon article, et j'espère vraiment que les génériques pourront devenir utiles pour vous.

Enfin, un coup de projecteur à ce [site](https://bitfieldconsulting.com/golang/generics) qui a été une grande référence pour moi lors de la rédaction de cet article. Il explique beaucoup de l'histoire des génériques en Go.

Amusez-vous avec les génériques !