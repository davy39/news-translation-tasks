---
title: Qu'est-ce que les pointeurs en Go ? Un guide pour les développeurs JavaScript
subtitle: ''
author: Brian Barrow
co_authors: []
series: null
date: '2023-04-24T22:07:19.000Z'
originalURL: https://freecodecamp.org/news/what-are-pointers-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/kaleb-tapp-J59wWPn09BE-unsplash.jpg
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que les pointeurs en Go ? Un guide pour les développeurs JavaScript
seo_desc: 'Coming from a language like JavaScript, pointers can be kind of confusing
  at first. Here I will break it down so that they are easier to understand.

  What Are Pointers in Go?

  Just like in JavaScript, Go has variables which are locations in memory that...'
---

Venant d'un langage comme JavaScript, les pointeurs peuvent être un peu déroutants au début. Ici, je vais les décomposer pour qu'ils soient plus faciles à comprendre.

## Qu'est-ce que les pointeurs en Go ?

Tout comme en JavaScript, Go a des variables qui sont des emplacements en mémoire stockant une valeur.

Dans les deux langages, cette valeur peut être manipulée en lui assignant une nouvelle valeur ou en effectuant des opérations dessus. Peu importe ce que vous faites avec cette variable, elle est toujours stockée à un endroit spécifique en mémoire.

Les pointeurs sont un autre type de variable. Au lieu de stocker une valeur que vous allez utiliser, ils stockent l'_adresse mémoire_ d'une autre variable. Il "pointe vers" l'emplacement de la variable.

**Ce n'est pas les données réelles de cette variable**. C'est juste l'adresse de la variable vers laquelle il pointe.

### Syntaxe des pointeurs

Un pointeur est défini en utilisant la syntaxe `*`. Donc, pour déclarer une variable de pointeur, le code ressemblerait à ceci :

```go
var x *int
```

Cela définit `x` comme un pointeur vers une valeur `int`.

Si vous voulez définir une variable comme un pointeur vers une autre valeur, vous l'initialisez avec l'opérateur `&`.

```go
normalInt := 5
// pointerInt est défini comme un pointeur vers normalInt
pointerInt = &normalInt

normalString := "hello world"
// pointerString est défini comme un pointeur vers normalString
pointerString = &normalString
```

Afin d'accéder à la valeur sous-jacente du pointeur, nous utilisons l'opérateur `*`.

```go
fmt.Println(*pointerInt) // lit pointerInt à travers le pointeur
*pointerInt = 10 // définit pointerInt à travers le pointeur
```

Voici un dessin qui illustre le concept de pointeurs :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Pasted-image-20230421202803.png)

### Attention aux pointeurs `nil`

Lors de la déréférencement d'un pointeur, s'il n'a pas été pointé vers quoi que ce soit, le programme va paniquer. Il est bon de vérifier si un pointeur est `nil` avant d'essayer de le déréférencer.

### Pourquoi les pointeurs ?

Lorsque une fonction prend un argument, la valeur de l'argument est copiée dans la fonction. La fonction peut alors manipuler la copie de la variable.

En utilisant des pointeurs, nous pouvons créer des programmes plus efficaces. Cela nous permet de manipuler les données auxquelles le pointeur fait référence sans les copier plusieurs fois dans le programme.

Bien que cela améliore l'efficacité du programme, vous devez être prudent lorsque vous les utilisez. Il est parfaitement acceptable d'utiliser des variables normales comme arguments pour les fonctions et de retourner de nouvelles valeurs depuis les fonctions.

Un endroit où les pointeurs sont utiles est avec les récepteurs.

### Récepteurs de pointeurs

Au lieu de recevoir juste une valeur, les méthodes peuvent recevoir un pointeur. Cela permet à la méthode de modifier la valeur vers laquelle le récepteur pointe. Puisque les méthodes ont souvent besoin de modifier leur récepteur, les récepteurs de pointeurs sont plus courants que les récepteurs de valeurs.

```go
type ball struct {
	color string
}

func (b *ball) setColor(color string) {
	b.color = color
}

func main() {
	b := ball{
		color: "white",
	}
	b.setColor("blue")
	fmt.Println(b.color)
	// imprime "blue"
}
```

Sans le récepteur de pointeur, `setColor` ne pourrait pas modifier la valeur `color` de la balle.

```go
type ball struct {
	color string
}

func (b ball) setColor(color string) {
	b.color = color
}

func main() {
	b := ball{
		color: "white",
	}
	b.setColor("blue")
	fmt.Println(b.color)
	// imprime "white"
}
```

## Conclusion

Les pointeurs sont un concept essentiel en programmation Go. Bien qu'ils puissent être déroutants au début, ils sont un outil important pour créer des programmes efficaces.

Espérons que cette brève explication aidera à clarifier toute confusion.