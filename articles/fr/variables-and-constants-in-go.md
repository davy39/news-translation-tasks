---
title: Qu'est-ce que les Variables et les Constantes en Go ? Expliqué avec des Exemples
subtitle: ''
author: Temitope Oyedele
co_authors: []
series: null
date: '2024-08-19T07:26:50.337Z'
originalURL: https://freecodecamp.org/news/variables-and-constants-in-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724052347929/f54eba57-fa4b-4b81-821e-41826d592933.jpeg
tags:
- name: Go
  slug: go-cjffccfnf0024tjs1mcwab09t
- name: beginner
  slug: beginner
seo_title: Qu'est-ce que les Variables et les Constantes en Go ? Expliqué avec des
  Exemples
seo_desc: 'Variables and constants are fundamental concepts in most programming languages.
  They are the building blocks for storing and managing data.

  In this article, we''ll take a look at how variables and constant work in Go.

  Table of contents:


  What are Vari...'
---

Les variables et les constantes sont des concepts fondamentaux dans la plupart des langages de programmation. Elles sont les éléments de base pour stocker et gérer des données.

Dans cet article, nous allons examiner comment les variables et les constantes fonctionnent en Go.

## Table des matières :

* [Qu'est-ce que les Variables ?](#heading-quest-ce-que-les-variables)
    
* [Comment Créer une Variable](#heading-comment-creer-une-variable-en-go)
    
* [Déclaration Explicite](#heading-declaration-explicite)
    
* [Déclaration de Variable en Notation Courte](#heading-declaration-de-variable-en-notation-courte)
    
* [Déclarations de Variables Multiples](#heading-declarations-de-variables-multiples)
    
* [Valeurs Zéro](#heading-valeurs-zero)
    
* [Qu'est-ce qu'une Portée de Variable](#heading-quest-ce-quune-porte-de-variable)
    
* [Conventions de Nommage en Go](#heading-conventions-de-nommage-en-go)
    
* [Qu'est-ce que les Constantes en Go](#heading-quest-ce-que-les-constantes-en-go)
    
* [Comment Déclarer des Constantes en Go](#heading-comment-declarer-des-constantes-en-go)
    
* [Types de Constantes en Go](#heading-types-de-constantes-en-go)
    
* [C'est tout pour aujourd'hui](#heading-cest-tout-pour-aujourdhui)
    

## Qu'est-ce que les Variables ?

Une variable est un emplacement de stockage identifié par un nom (ou identifiant) qui contient une valeur. Cette valeur peut changer (ou varier) pendant l'exécution d'un programme. C'est pourquoi on l'appelle une variable.

Par exemple :

```go
myName := "temitope"

fmt.Println(myName)

myName := "oyedele"

fmt.Println(myName)
```

Nous avons créé une variable avec un identifiant `myName` qui contient une valeur de chaîne de caractères.

Si vous l'avez remarqué, nous avons changé la valeur en une autre chaîne, et nous pouvons le faire plusieurs fois car les variables sont autorisées à le faire.

Les variables vous permettent de stocker des données, qui peuvent être de différents types, tels que des entiers, des nombres à virgule flottante, des chaînes de caractères ou des objets.

## Comment Créer une Variable en Go

Il existe deux façons principales de créer une variable en Go : la déclaration explicite et la déclaration en notation courte.

### Déclaration Explicite

C'est la manière traditionnelle de créer une variable en Go. Elle fonctionne en utilisant le mot-clé `var` et en déclarant le type de la variable, rendant votre code plus lisible et clair.

```go
package main

import "fmt"

func main() {

	var age int = 25

	var name string = "Temitope"

	var height float64 = 5.7

	fmt.Println(age, name, height)

}
```

Vous pouvez voir que, pour chaque variable, nous avons déclaré son type de données avant de lui attribuer une valeur.

```plaintext
output:
25 Temitope 5.7
```

Le mot-clé `var` et le type de données peuvent également être utilisés sans avoir de valeur initiale :

```go
package main

import "fmt"

func main() {
	var age int
	var name string
	var height float64

	age = 25
	name = "Temitope"
	height = 5.7

	fmt.Println(age, name, height)
}
```

De cette manière, les variables sont déclarées d'abord sans valeur initiale. Elles se voient ensuite attribuer des valeurs plus tard dans le code. Vous aurez toujours la même sortie que la première.

### Déclaration de Variable en Notation Courte

La syntaxe de déclaration de variable en notation courte (`:=`) est une manière plus concise de déclarer des variables. Cette méthode vous permet de déclarer et d'initialiser une variable en une seule ligne sans indiquer explicitement son type, car le type est déduit de la valeur attribuée.

```go
package main

import "fmt"

func main() {

	age := 25

	name := "Temitope"

	height := 5.7

	fmt.Println(age, name, height)

}
```

Ici, chaque variable a été déclarée avec sa valeur, Go déduisant le type de données. Par exemple, `age` a été déclaré et initialisé avec une valeur de 25, et Go a déduit son type comme `int`. `name` a été déclaré avec la valeur "Temitope", et Go a déduit son type comme `string`. Enfin, `height` a été déclaré avec 5.7, et Go a déduit son type comme `float64`.

```plaintext
output:
25 Temitope 5.7
```

L'un des inconvénients de la déclaration de variable en notation courte est que vous ne pouvez l'utiliser qu'à l'intérieur d'une fonction.

## Déclarations de Variables Multiples

Vous pouvez déclarer et initialiser plusieurs variables sur la même ligne en séparant chaque variable par une virgule. Cette approche est simple et directe. Elle est couramment utilisée lorsque les variables sont liées ou lorsque vous souhaitez les initialiser ensemble. Par exemple :

```go
package main

import "fmt"

func main() {

	var age, height int = 25, 180

	var name, city string = "Temitope", "New York"

	fmt.Println(age, height)

	fmt.Println(name, city)
}
```

Ici, les variables `age` et `height` sont toutes deux déclarées comme des entiers et initialisées avec les valeurs 25 et 180, respectivement. Les variables `name` et `city` sont également toutes deux déclarées comme des chaînes de caractères et initialisées avec "Temitope" et "New York" :

```plaintext
Output:
25 180
Temitope New York
```

Vous pouvez également déclarer plusieurs variables dans un bloc comme suit :

```go
package main

import "fmt"

func main() {

	var (
		age int = 25

		name string = "Temitope"

		height int = 180

		city string = "New York"
	)

	fmt.Println(age, name, height, city)

}
```

Ici, les variables `age`, `name`, `height` et `city` sont déclarées dans un seul bloc var, chaque variable ayant sa propre ligne.

```plaintext
Output:
25 Temitope 180 New York
```

### Valeurs Zéro

Lorsque des variables sont déclarées sans être initialisées, elles reçoivent des valeurs zéro par défaut. Ces valeurs diffèrent selon le type de variable. Voici un exemple de la manière dont vous pouvez déclarer des valeurs par défaut :

```go
package main

import "fmt"

func main() {

	var intValue int

	var floatValue float64

	var boolValue bool

	var stringValue string

	var ptrValue *int

	var sliceValue []int

	var mapValue map[string]int

	fmt.Println("Valeurs zéro :")

	fmt.Println("int:", intValue)

	fmt.Println("float64:", floatValue)

	fmt.Println("bool:", boolValue)

	fmt.Println("string:", stringValue)

	fmt.Println("pointer:", ptrValue)

	fmt.Println("slice:", sliceValue)

	fmt.Println("map:", mapValue)

}
```

Dans le code ci-dessus, voici ce qui va se passer :

* L'entier `intValue` recevra la valeur zéro 0.
    
* Le nombre à virgule flottante `floatValue` recevra la valeur zéro 0.
    
* Le booléen `boolValue` recevra la valeur zéro `false`.
    
* La chaîne de caractères `stringValue` recevra la valeur zéro "" (chaîne vide).
    
* Le pointeur `ptrValue`, la tranche `sliceValue` et la carte `mapValue` recevront tous la valeur zéro `nil`.
    

Output:

```plaintext
Output:
Valeurs zéro :
int: 0
float64: 0
bool: false
string: 
pointer: <nil>
slice: []
map: map[]
```

### Qu'est-ce qu'une Portée de Variable ?

Les variables peuvent être déclarées soit globalement, soit localement. La portée d'une variable détermine où elle peut être accessible et modifiée dans votre code.

Les variables globales sont déclarées en dehors de toute fonction, généralement en haut d'un fichier, et elles peuvent être accessibles par toute fonction dans le même package. Voici un exemple :

```go
package main

import "fmt"

var globalCounter int = 0

func incrementCounter() {

	globalCounter++

}

func main() {

	fmt.Println("Compteur Initial :", globalCounter)

	incrementCounter()

	fmt.Println("Après Incrémentation :", globalCounter)

}
```

Dans l'exemple ci-dessus, `globalCounter` est la variable globale, et elle est accessible à la fois par la fonction `incrementCounter` et la fonction `main`.

De plus, la valeur de `globalCounter` persiste à travers les appels de fonction. Cela signifie que tout changement qui lui est apporté dans une fonction affecte sa valeur dans d'autres parties du programme.

Les variables locales, en revanche, sont déclarées dans une fonction ou un bloc et ne sont accessibles que dans cette fonction ou ce bloc spécifique. Elles sont créées lorsque la fonction ou le bloc est exécuté et détruites une fois qu'il est terminé. Par exemple :

```go
package main

import "fmt"

func incrementCounter() {

	localCounter := 0

	localCounter++

	fmt.Println("Compteur Local :", localCounter)

}

func main() {

	incrementCounter()

	incrementCounter()

}
```

Dans le code ci-dessus, nous avons `localCounter` comme variable locale à l'intérieur de la fonction `incrementCounter`. Chaque fois que `incrementCounter` est appelée, un nouveau `localCounter` est créé, initialisé à 0, et incrémenté.

La valeur de `localCounter` ne persiste pas entre les appels de fonction, donc elle ne peut pas affecter une partie quelconque d'un programme lorsqu'un changement est apporté à la fonction.

## Conventions de Nommage en Go

Le nommage approprié des variables est crucial pour écrire un code propre, lisible et maintenable. Go a des conventions et des règles spécifiques pour le nommage des variables. En voici quelques-unes :

* **Utilisez des noms descriptifs :** Utilisez des noms qui décrivent clairement le but ou le contenu de la variable. Par exemple, au lieu d'utiliser des noms vagues comme x ou y, utilisez des noms comme `age`, `totalPrice`, ou `userName` qui indiquent clairement ce que la variable représente.
    
* **Utilisez le CamelCase pour les Noms à Plusieurs Mots :** En Go, il est courant d'utiliser le CamelCase pour les noms de variables composés de plusieurs mots. Le premier mot est en minuscule, et la première lettre de chaque mot suivant est en majuscule.
    
* **Évitez d'Utiliser des Underscores :** Contrairement à certains autres langages, Go préfère le CamelCase à l'utilisation de underscores pour séparer les mots dans les noms de variables. Restez avec le CamelCase pour adhérer au style idiomatique de Go.
    
* **Utilisez des Noms Courts pour les Variables de Courte Durée :** Pour les variables de courte durée, telles que les compteurs de boucle ou les indices, il est acceptable d'utiliser des noms courts comme i, j, ou k.
    

## Qu'est-ce que les Constantes en Go ?

Les constantes sont des valeurs immuables définies au moment de la compilation qui ne peuvent pas être modifiées pendant l'exécution du programme. Elles sont utiles pour définir des valeurs connues à l'avance et qui resteront les mêmes.

Imaginez que vous construisez une boutique en ligne où les frais de livraison standard sont toujours de 10 $. Vous pouvez les déclarer comme une constante, afin de pouvoir l'utiliser dans tout votre programme chaque fois que des frais de livraison doivent être appliqués. Si les tarifs de livraison changent, vous n'avez besoin de mettre à jour la valeur qu'à un seul endroit.

## Comment Déclarer des Constantes en Go

Vous pouvez déclarer des constantes en utilisant le mot-clé `const`, suivi du nom, du type (facultatif si la valeur implique le type) et de la valeur de la constante. Voici comment :

```go
package main

import "fmt"

func main() {

	const pi float64 = 3.14159

	const greeting string = "Hello, World!"

	fmt.Println("Pi:", pi)

	fmt.Println("Greeting:", greeting)

}
```

Si vous essayez de changer une constante après sa déclaration, vous obtiendrez une erreur de compilation.

## Types de Constantes en Go

Les constantes peuvent être catégorisées comme typées ou non typées. Les deux types de constantes servent le même but. Elles fournissent des valeurs fixes et immuables dans tout le programme. Cependant, elles diffèrent dans la manière dont Go gère leurs types et dans leur flexibilité lorsqu'elles sont utilisées.

Les constantes non typées ne se voient pas attribuer un type sauf si elles sont utilisées dans un contexte qui nécessite un type. Lorsque vous déclarez une constante non typée, Go déduira le type au moment où la constante est utilisée. Cela rend les constantes non typées plus flexibles car elles peuvent être utilisées dans divers contextes sans nécessiter de conversion de type.

```go
package main

import "fmt"

const gravity = 9.81

func main() {

	var height int = 10

	var acceleration float64 = gravity * float64(height)

	fmt.Println("Acceleration:", acceleration)

}
```

Ici, `gravity` est la constante non typée. Cela signifie que Go peut déduire son type en fonction de son utilisation. Lorsque `gravity` est utilisée dans un calcul avec un `float64`, Go la traitera automatiquement comme un `float64`.

Contrairement aux constantes non typées, les constantes typées ont un type explicitement déclaré. Cela signifie qu'elles ne peuvent être utilisées que dans des contextes qui correspondent à ce type ou peuvent être converties en un type compatible. Les constantes typées sont plus strictes, garantissant que la valeur est toujours traitée comme le type spécifique avec lequel elle a été déclarée.

```go
package main

import "fmt"

const speedOfLight int = 299792458

func main() {

	var distance int = speedOfLight * 2

	fmt.Println("Distance:", distance)

}
```

Ici, `speedOfLight` est la constante typée avec le type `int`.

Elle ne peut être utilisée que dans des opérations avec d'autres valeurs `int` ou convertie explicitement en un type différent.

## C'est tout pour aujourd'hui

Dans cet article, nous avons examiné ce que sont les variables et les constantes et comment les déclarer en Go.

Les variables et les constantes sont des outils critiques en programmation. Elles permettent aux développeurs de gérer et de manipuler efficacement les données. Lorsque vous comprenez comment les utiliser, vous pouvez améliorer la qualité de votre code.

Veuillez partager si vous avez trouvé cela utile.