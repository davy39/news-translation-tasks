---
title: Apprendre Go — de zéro à héros
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-17T21:32:10.000Z'
originalURL: https://freecodecamp.org/news/learning-go-from-zero-to-hero-d2a3223b3d86
coverImage: https://cdn-media-1.freecodecamp.org/images/1*30aoNxlSnaYrLhBT0O1lzw.png
tags:
- name: golang
  slug: golang
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Apprendre Go — de zéro à héros
seo_desc: 'By Milap Neupane

  Let’s start with a small introduction to Go (or Golang). Go was designed by Google
  engineers Robert Griesemer, Rob Pike, and Ken Thompson. It is a statically typed,
  compiled language. The first version was released as open source in ...'
---

Par Milap Neupane

Commençons par une petite introduction à Go (ou Golang). Go a été conçu par les ingénieurs de Google Robert Griesemer, Rob Pike et Ken Thompson. C'est un langage statiquement typé et compilé. La première version a été publiée en open source en mars 2012.

> « Go est un langage de programmation open source qui facilite la création de logiciels simples, fiables et efficaces. » — GoLang

Dans de nombreux langages, il existe de nombreuses façons de résoudre un problème donné. Les programmeurs peuvent passer beaucoup de temps à réfléchir à la meilleure façon de le résoudre.

Go, en revanche, croit en moins de fonctionnalités — avec une seule bonne façon de résoudre le problème.

Cela fait gagner du temps aux développeurs et rend le grand codebase facile à maintenir. Il n'y a pas de fonctionnalités « expressives » comme les maps et les filtres dans Go.

> « Lorsque vous avez des fonctionnalités qui ajoutent de l'expressivité, cela ajoute généralement des coûts. » — Rob Pike

![Image](https://cdn-media-1.freecodecamp.org/images/1*AUiSG5Gqz8MzaGCvGpckGA.png)
_Logo récemment publié de Go : [https://blog.golang.org/go-brand](https://blog.golang.org/go-brand" rel="noopener" target="_blank" title=")_

### Installation

Go est composé de packages. Le package main indique au compilateur Go que le programme est compilé comme un exécutable, plutôt que comme une bibliothèque partagée. C'est le point d'entrée pour une application. Le package main est défini comme suit :

```go
package main
```

Continuons en écrivant un simple exemple "hello world" en créant un fichier `main.go` dans l'espace de travail Go.

#### **Espace de travail**

Un espace de travail dans Go est défini par la variable d'environnement `GOPATH`.

Tout code que vous écrivez doit être écrit à l'intérieur de l'espace de travail. Go recherchera tous les packages à l'intérieur du répertoire `GOPATH`, ou du répertoire `GOROOT`, qui est défini par défaut lors de l'installation de Go. `GOROOT` est le chemin où Go est installé.

Définissez `GOPATH` sur le répertoire souhaité. Pour l'instant, ajoutons-le dans un dossier `~/workspace`.

```
# export env
export GOPATH=~/workspace
# aller dans le répertoire de l'espace de travail
cd ~/workspace
```

Créez le fichier `main.go` avec le code suivant à l'intérieur du dossier de l'espace de travail que nous venons de créer.

#### Hello World !

```go
package main

import (
 "fmt"
)

func main(){
  fmt.Println("Hello World!")
}
```

Dans l'exemple ci-dessus, `fmt` est un package intégré dans Go qui implémente des fonctions pour le formatage des E/S.

Nous importons un package dans Go en utilisant le mot-clé `import`. `func main` est le point d'entrée principal où le code est exécuté. `Println` est une fonction à l'intérieur du package `fmt` qui imprime « hello world » pour nous.

Voyons cela en exécutant ce fichier. Il y a deux façons d'exécuter une commande Go. Comme nous le savons, Go est un langage compilé, donc nous devons d'abord le compiler avant de l'exécuter.

```
> go build main.go
```

Cela crée un fichier binaire exécutable `main` que nous pouvons maintenant exécuter :

```
> ./main 
# Hello World!
```

Il y a une autre façon, plus simple, d'exécuter le programme. La commande `go run` aide à abstraire l'étape de compilation. Vous pouvez simplement exécuter la commande suivante pour exécuter le programme.

```
go run main.go
# Hello World!
```

**_Note_**_: Pour essayer le code mentionné dans ce blog, vous pouvez utiliser [https://play.golang.org](https://play.golang.org/)_

### Variables

Les variables dans Go sont déclarées explicitement. Go est un langage statiquement typé. Cela signifie que le type de variable est vérifié au moment de la déclaration de la variable. Une variable peut être déclarée comme suit :

```go
var a int
```

Dans ce cas, la valeur sera définie sur 0. Utilisez la syntaxe suivante pour déclarer et initialiser une variable avec une valeur différente :

```go
var a = 1
```

Ici, la variable est automatiquement assignée comme un int. Nous pouvons utiliser une définition abrégée pour la déclaration de variable comme suit :

```go
message := "hello world"
```

Nous pouvons également déclarer plusieurs variables sur la même ligne :

```go
var b, c int = 2, 3
```

### Types de données

Comme tout autre langage de programmation, Go supporte diverses structures de données différentes. Explorons-en quelques-unes :

#### **Nombre, Chaîne de caractères et Booléen**

Certains des types de stockage de nombres supportés sont int, int8, int16, int32, int64, uint, uint8, uint16, uint32, uint64, uintptr...

Le type chaîne de caractères stocke une séquence d'octets. Il est représenté et déclaré avec le mot-clé `string`.

Une valeur booléenne est stockée en utilisant le mot-clé `bool`.

Go supporte également les types de données de nombres complexes, qui peuvent être déclarés avec `complex64` et `complex128`.

```go
var a bool = true
var b int = 1
var c string = 'hello world'
var d float32 = 1.222
var x complex128 = cmplx.Sqrt(-5 + 12i)
```

#### **Tableaux, Slices et Maps**

Un tableau est une séquence d'éléments du même type de données. Les tableaux ont une longueur fixe définie à la déclaration, donc ils ne peuvent pas être étendus au-delà de cela. Un tableau est déclaré comme suit :

```go
var a [5]int
```

Les tableaux peuvent également être multidimensionnels. Nous pouvons simplement les créer avec le format suivant :

```go
var multiD [2][3]int
```

Les tableaux sont limitants pour les cas où les valeurs du tableau changent à l'exécution. Les tableaux ne fournissent pas non plus la possibilité d'obtenir un sous-tableau. Pour cela, Go a un type de données appelé slices.

Les slices stockent une séquence d'éléments et peuvent être étendues à tout moment. La déclaration de slice est similaire à la déclaration de tableau — sans la capacité définie :

```go
var b []int
```

Cela crée une slice avec une capacité et une longueur nulles. Les slices peuvent également être définies avec une capacité et une longueur. Nous pouvons utiliser la syntaxe suivante pour cela :

```go
numbers := make([]int,5,10)
```

Ici, la slice a une longueur initiale de 5 et une capacité de 10.

Les slices sont une abstraction d'un tableau. Les slices utilisent un tableau comme structure sous-jacente. Une slice contient trois composants : capacité, longueur et un pointeur vers le tableau sous-jacent comme montré dans le diagramme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*P0lNCO0sQwIYHLEX_mfSOQ.png)
_image src: [https://blog.golang.org/go-slices-usage-and-internals](https://blog.golang.org/go-slices-usage-and-internals" rel="noopener" target="_blank" title=")_

La capacité d'une slice peut être augmentée en utilisant la fonction append ou copy. Une fonction append ajoute une valeur à la fin du tableau et augmente également la capacité si nécessaire.

```go
numbers = append(numbers, 1, 2, 3, 4)
```

Une autre façon d'augmenter la capacité d'une slice est d'utiliser la fonction copy. Créez simplement une autre slice avec une capacité plus grande et copiez la slice originale dans la nouvelle slice créée :

```go
// créer une nouvelle slice
number2 := make([]int, 15)
// copier la slice originale dans la nouvelle slice
copy(number2, number)
```

Nous pouvons créer une sous-slice d'une slice. Cela peut être fait simplement en utilisant la commande suivante :

```go
// initialiser une slice avec 4 len et valeurs
number2 = []int{1,2,3,4}
fmt.Println(numbers) // -> [1 2 3 4]
// créer des sous-slices
slice1 := number2[2:]
fmt.Println(slice1) // -> [3 4]
slice2 := number2[:3]
fmt.Println(slice2) // -> [1 2 3]
slice3 := number2[1:4]
fmt.Println(slice3) // -> [2 3 4]
```

Les maps sont un type de données dans Go, qui mappe les clés aux valeurs. Nous pouvons définir une map en utilisant la commande suivante :

```go
var m map[string]int
```

Ici, `m` est la nouvelle variable de map, qui a ses clés comme `string` et les valeurs sont `integers`. Nous pouvons ajouter des clés et des valeurs facilement à une map :

```go
// ajout de clé/valeur
m['clearity'] = 2
m['simplicity'] = 3
// impression des valeurs
fmt.Println(m['clearity']) // -> 2
fmt.Println(m['simplicity']) // -> 3
```

### **Conversion de type**

Un type de données peut être converti en un autre en utilisant la conversion de type. Regardons une simple conversion de type :

```go
a := 1.1
b := int(a)
fmt.Println(b)
//-> 1
```

Tous les types de données ne peuvent pas être convertis en un autre type. Assurez-vous que le type de données est compatible avec la conversion.

### Instructions conditionnelles

#### if else

Pour les instructions conditionnelles, nous pouvons utiliser les instructions if-else comme montré dans l'exemple ci-dessous. Assurez-vous que les accolades sont sur la même ligne que la condition.

```go
if num := 9; num < 0 {
 fmt.Println(num, "est négatif")
} else if num < 10 {
 fmt.Println(num, "a 1 chiffre")
} else {
 fmt.Println(num, "a plusieurs chiffres")
}
```

#### switch case

Les cas de switch aident à organiser plusieurs instructions conditionnelles. L'exemple suivant montre une instruction switch case simple :

```go
i := 2
switch i {
case 1:
 fmt.Println("un")
case 2:
 fmt.Println("deux")
default:
 fmt.Println("aucun")
}
```

### Boucles

Go a un seul mot-clé pour la boucle. Une seule commande de boucle for aide à réaliser différents types de boucles :

```go
i := 0
sum := 0
for i < 10 {
 sum += 1
  i++
}
fmt.Println(sum)
```

L'exemple ci-dessus est similaire à une boucle while en C. La même instruction for peut être utilisée pour une boucle for normale :

```go
sum := 0
for i := 0; i < 10; i++ {
  sum += i
}
fmt.Println(sum)
```

Boucle infinie en Go :

```go
for {
}
```

### Pointeurs

Go fournit des pointeurs. Les pointeurs sont l'endroit pour stocker l'adresse d'une valeur. Un pointeur est défini par *. Un pointeur est défini selon le type de données. Exemple :

```go
var ap *int

```

Ici, `ap` est le pointeur vers un type entier. L'opérateur `&` peut être utilisé pour obtenir l'adresse d'une variable.

```go
a := 12
ap = &a

```

La valeur pointée par le pointeur peut être accédée en utilisant l'opérateur `*` :

```go
fmt.Println(*ap)
// => 12
```

Les pointeurs sont généralement préférés lors du passage d'une struct comme argument ou lors de la déclaration d'une méthode pour un type défini.

1. Lors du passage de la valeur, la valeur est en fait copiée, ce qui signifie plus de mémoire
2. Avec le pointeur passé, la valeur modifiée par la fonction est réfléchie dans l'appelant de la méthode/fonction.

Exemple :

```go
func increment(i *int) {
  *i++
}
func main() {
  i := 10
  increment(&i)
  fmt.Println(i)
}
//=> 11
```

Note : Lorsque vous essayez l'exemple de code dans le blog, n'oubliez pas de l'inclure avec le package main et d'importer fmt ou d'autres packages lorsque cela est nécessaire, comme montré dans le premier exemple main.go ci-dessus.

### Fonctions

La fonction main définie dans le package main est le point d'entrée pour qu'un programme Go s'exécute. Plus de fonctions peuvent être définies et utilisées. Regardons un exemple simple :

```go
func add(a int, b int) int {
  c := a + b
  return c
}
func main() {
  fmt.Println(add(2, 1))
}
//=> 3
```

Comme nous pouvons le voir dans l'exemple ci-dessus, une fonction Go est définie en utilisant le mot-clé **func** suivi du nom de la fonction. Les **arguments** qu'une fonction prend doivent être définis selon son type de données, et enfin le type de données du retour.

Le retour d'une fonction peut être prédéfini dans la fonction également :

```go
func add(a int, b int) (c int) {
  c = a + b
  return
}
func main() {
  fmt.Println(add(2, 1))
}
//=> 3
```

Ici, c est défini comme la variable de retour. Ainsi, la variable c définie serait automatiquement retournée sans avoir besoin d'être définie à l'instruction return à la fin.

Vous pouvez également retourner plusieurs valeurs de retour à partir d'une seule fonction en séparant les valeurs de retour par une virgule.

```go
func add(a int, b int) (int, string) {
  c := a + b
  return c, "successfully added"
}
func main() {
  sum, message := add(2, 1)
  fmt.Println(message)
  fmt.Println(sum)
}
```

### Méthodes, Structs et Interfaces

Go n'est pas un langage complètement orienté objet, mais avec les structs, les interfaces et les méthodes, il a beaucoup de support et de sensation orientés objet.

#### Struct

Une struct est une collection typée de différents champs. Une struct est utilisée pour regrouper des données ensemble. Par exemple, si nous voulons regrouper des données d'un type Person, nous définissons un attribut de personne qui pourrait inclure le nom, l'âge, le genre. Une struct peut être définie en utilisant la syntaxe suivante :

```go
type person struct {
  name string
  age int
  gender string
}
```

Avec une struct de type personne définie, créons maintenant une personne :

```go
// façon 1 : spécifier l'attribut et la valeur
p = person{name: "Bob", age: 42, gender: "Male"}
// façon 2 : spécifier uniquement la valeur
person{"Bob", 42, "Male"}
```

Nous pouvons facilement accéder à ces données avec un point (.)

```go
p.name
//=> Bob
p.age
//=> 42
p.gender
//=> Male
```

Vous pouvez également accéder aux attributs d'une struct directement avec son pointeur :

```go
pp = &person{name: "Bob", age: 42, gender: "Male"}
pp.name
//=> Bob
```

#### Méthodes

Les méthodes sont un type spécial de fonction avec un _récepteur_. Un récepteur peut être à la fois une valeur ou un pointeur. Créons une méthode appelée describe qui a un type de récepteur person que nous avons créé dans l'exemple ci-dessus :

```go
package main
import "fmt"

// définition de la struct
type person struct {
  name   string
  age    int
  gender string
}

// définition de la méthode
func (p *person) describe() {
  fmt.Printf("%v a %v ans.", p.name, p.age)
}
func (p *person) setAge(age int) {
  p.age = age
}

func (p person) setName(name string) {
  p.name = name
}

func main() {
  pp := &person{name: "Bob", age: 42, gender: "Male"}
  pp.describe()
  // => Bob a 42 ans
  pp.setAge(45)
  fmt.Println(pp.age)
  //=> 45
  pp.setName("Hari")
  fmt.Println(pp.name)
  //=> Bob
}
```

Comme nous pouvons le voir dans l'exemple ci-dessus, la méthode peut maintenant être appelée en utilisant un opérateur point comme `pp.describe`. Notez que le récepteur est un pointeur. Avec le pointeur, nous passons une référence à la valeur, donc si nous apportons des modifications dans la méthode, cela sera reflété dans le récepteur pp. Cela ne crée pas non plus de nouvelle copie de l'objet, ce qui économise de la mémoire.

Notez que dans l'exemple ci-dessus, la valeur de l'âge est modifiée, tandis que la valeur du nom n'est pas modifiée car la méthode setName est du type récepteur tandis que setAge est du type pointeur.

#### Interfaces

Les interfaces Go sont une collection de méthodes. Les interfaces aident à regrouper les propriétés d'un type. Prenons l'exemple d'une interface animal :

```go
type animal interface {
  description() string
}
```

Ici, animal est un type d'interface. Créons maintenant 2 types d'animaux différents qui implémentent le type d'interface animal :

```go
package main

import (
  "fmt"
)

type animal interface {
  description() string
}

type cat struct {
  Type  string
  Sound string
}

type snake struct {
  Type      string
  Poisonous bool
}

func (s snake) description() string {
  return fmt.Sprintf("Poisonous: %v", s.Poisonous)
}

func (c cat) description() string {
  return fmt.Sprintf("Sound: %v", c.Sound)
}

func main() {
  var a animal
  a = snake{Poisonous: true}
  fmt.Println(a.description())
  a = cat{Sound: "Meow!!!"}
  fmt.Println(a.description())
}

//=> Poisonous: true
//=> Sound: Meow!!!
```

Dans la fonction main, nous créons une variable `a` de type animal. Nous assignons un type snake et un type cat à l'animal et utilisons Println pour imprimer a.description. Puisque nous avons implémenté la méthode describe dans les deux types (cat et snake) de différentes manières, nous obtenons la description de l'animal imprimée.

### Packages

Nous écrivons tout le code en Go dans un package. Le package **main** est le point d'entrée pour l'exécution du programme. Il existe de nombreux packages intégrés dans Go. Le plus célèbre que nous avons utilisé est le package **fmt**.

> « Les packages Go sont le mécanisme principal pour programmer en grand que Go fournit et ils rendent possible de diviser un grand projet en petits morceaux. »

> — Robert Griesemer

#### Installation d'un package

```
go get <package-url-github>
// exemple
go get github.com/satori/go.uuid
```

Les packages que nous avons installés sont enregistrés à l'intérieur de la variable d'environnement GOPATH qui est notre répertoire de travail. Vous pouvez voir les packages en allant dans le dossier pkg à l'intérieur de notre répertoire de travail `cd $GOPATH/pkg`.

#### Création d'un package personnalisé

Commençons par créer un dossier custom_package :

```
> mkdir custom_package
> cd custom_package
```

Pour créer un package personnalisé, nous devons d'abord créer un dossier avec le nom du package dont nous avons besoin. Disons que nous construisons un package `person`. Pour cela, créons un dossier nommé `person` à l'intérieur du dossier `custom_package` :

```
> mkdir person
> cd person
```

Créons maintenant un fichier person.go à l'intérieur de ce dossier.

```go
package person
func Description(name string) string {
  return "Le nom de la personne est : " + name
}
func secretName(name string) string {
  return "Ne pas partager"
}
```

Nous devons maintenant installer le package afin qu'il puisse être importé et utilisé. Alors installons-le :

```
> go install
```

Maintenant, retournons dans le dossier custom_package et créons un fichier main.go

```go
package main
import(
  "custom_package/person"
  "fmt"
)
func main(){ 
  p := person.Description("Milap")
  fmt.Println(p)
}
// => Le nom de la personne est : Milap
```

Ici, nous pouvons maintenant importer le package `person` que nous avons créé et utiliser la fonction Description. Notez que la fonction `secretName` que nous avons créée dans le package ne sera pas accessible. Dans Go, le nom de la méthode commençant par une lettre minuscule sera privé.

#### **Documentation des packages**

Go a un support intégré pour la documentation des packages. Exécutez la commande suivante pour générer la documentation :

```
godoc person Description
```

Cela générera la documentation pour la fonction Description à l'intérieur de notre package person. Pour voir la documentation, exécutez un serveur web en utilisant la commande suivante :

```
godoc -http=":8080"
```

Maintenant, allez à l'URL [http://localhost:8080/pkg/](http://localhost:6060/pkg/) et voyez la documentation du package que nous venons de créer.

#### Certains packages intégrés dans Go

**fmt**

Le package implémente des fonctions d'E/S formatées. Nous avons déjà utilisé le package pour imprimer sur stdout.

**json**

Un autre package utile dans Go est le package json. Cela aide à encoder/décoder le JSON. Prenons un exemple pour encoder/décoder du json :

Encoder

```go
package main

import (
  "fmt"
  "encoding/json"
)

func main(){
  mapA := map[string]int{"apple": 5, "lettuce": 7}
  mapB, _ := json.Marshal(mapA)
  fmt.Println(string(mapB))
}
```

Décoder

```go
package main

import (
  "fmt"
  "encoding/json"
)

type response struct {
  PageNumber int `json:"page"`
  Fruits []string `json:"fruits"`
}

func main(){
  str := `{"page": 1, "fruits": ["apple", "peach"]}`
  res := response{}
  json.Unmarshal([]byte(str), &res)
  fmt.Println(res.PageNumber)
}
//=> 1
```

Lors du décodage de l'octet json en utilisant unmarshal, le premier argument est l'octet json et le second argument est l'adresse de la struct de type réponse où nous voulons que le json soit mappé. Notez que le `json:"page"` mappe la clé page à la clé PageNumber dans la struct.

### Gestion des erreurs

Les erreurs sont le résultat indésirable et inattendu d'un programme. Supposons que nous faisons un appel d'API à un service externe. Cet appel d'API peut réussir ou échouer. Une erreur dans un programme Go peut être reconnue lorsqu'un type d'erreur est présent. Regardons l'exemple :

```go
resp, err := http.Get("http://example.com/")

```

Ici, l'appel d'API à l'objet d'erreur peut réussir ou échouer. Nous pouvons vérifier si l'erreur est nil ou présente et gérer la réponse en conséquence :

```go
package main

import (
  "fmt"
  "net/http"
)

func main(){
  resp, err := http.Get("http://example.com/")
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(resp)
}
```

#### Retourner une erreur personnalisée à partir d'une fonction

Lorsque nous écrivons une fonction à nous, il y a des cas où nous avons des erreurs. Ces erreurs peuvent être retournées à l'aide de l'objet d'erreur :

```go
func Increment(n int) (int, error) {
  if n < 0 {
    // retourner l'objet d'erreur
    return nil, errors.New("math: cannot process negative number")
  }
  return (n + 1), nil
}
func main() {
  num := 5
 
  if inc, err := Increment(num); err != nil {
    fmt.Printf("Failed Number: %v, error message: %v", num, err)
  }else {
    fmt.Printf("Incremented Number: %v", inc)
  }
}
```

La plupart des packages qui sont construits en Go, ou des packages externes que nous utilisons, ont un mécanisme de gestion des erreurs. Donc toute fonction que nous appelons pourrait avoir des erreurs possibles. Ces erreurs ne doivent jamais être ignorées et toujours traitées avec grâce à l'endroit où nous appelons ces fonctions, comme nous l'avons fait dans l'exemple ci-dessus.

#### Panic

Panic est quelque chose qui n'est pas géré et qui est soudainement rencontré lors de l'exécution d'un programme. Dans Go, panic n'est pas la façon idéale de gérer les exceptions dans un programme. Il est recommandé d'utiliser un objet d'erreur à la place. Lorsqu'une panic se produit, l'exécution du programme est interrompue. La chose qui est exécutée après une panic est le defer.

```go
//Go
package main

import "fmt"

func main() {
    f()
    fmt.Println("Retour normal de f.")
}

func f() {
    defer func() {
        if r := recover(); r != nil {
            fmt.Println("Recovered in f", r)
        }
    }()
    fmt.Println("Appel de g.")
    g(0)
    fmt.Println("Retour normal de g.")
}

func g(i int) {
    if i > 3 {
        fmt.Println("Panicking!")
        panic(fmt.Sprintf("%v", i))
    }
    defer fmt.Println("Defer in g", i)
    fmt.Println("Printing in g", i)
    g(i + 1)
}
```

#### Defer

Defer est quelque chose qui sera toujours exécuté à la fin d'une fonction.

Dans l'exemple ci-dessus, nous interrompons l'exécution du programme en utilisant panic(). Comme vous le remarquez, il y a une instruction defer qui fera exécuter le programme la ligne à la fin de l'exécution du programme. Defer peut également être utilisé lorsque nous avons besoin que quelque chose soit exécuté à la fin de la fonction, par exemple la fermeture d'un fichier.

### Concurrence

Go est construit avec la concurrence à l'esprit. La concurrence dans Go peut être atteinte par des Go routines qui sont des threads légers.

**Go routine**

Les Go routines sont des fonctions qui peuvent s'exécuter en parallèle ou simultanément avec une autre fonction. La création d'une Go routine est très simple. Simplement en ajoutant un mot-clé Go devant une fonction, nous pouvons la faire exécuter en parallèle. Les Go routines sont très légères, donc nous pouvons en créer des milliers. Regardons un exemple simple :

```go
package main
import (
  "fmt"
  "time"
)
func main() {
  go c()
  fmt.Println("Je suis main")
  time.Sleep(time.Second * 2)
}
func c() {
  time.Sleep(time.Second * 2)
  fmt.Println("Je suis concurrent")
}
//=> Je suis main
//=> Je suis concurrent
```

Comme vous pouvez le voir dans l'exemple ci-dessus, la fonction c est une Go routine qui s'exécute en parallèle avec le thread principal Go. Il y a des moments où nous voulons partager des ressources entre plusieurs threads. Go préfère ne pas partager les variables d'un thread avec un autre car cela ajoute une chance de blocage et d'attente de ressources. Il y a une autre façon de partager des ressources entre les Go routines : via les canaux Go.

**Canaux**

Nous pouvons passer des données entre deux Go routines en utilisant des canaux. Lors de la création d'un canal, il est nécessaire de spécifier quel type de données le canal reçoit. Créons un simple canal avec un type de chaîne comme suit :

```go
c := make(chan string)

```

Avec ce canal, nous pouvons envoyer des données de type chaîne. Nous pouvons à la fois envoyer et recevoir des données dans ce canal :

```go
package main

import "fmt"

func main(){
  c := make(chan string)
  go func(){ c <- "hello" }()
  msg := <-c
  fmt.Println(msg)
}
//=>"hello"
```

Les canaux récepteurs attendent jusqu'à ce que l'expéditeur envoie des données au canal.

**Canal unidirectionnel**

Il y a des cas où nous voulons qu'une Go routine reçoive des données via le canal mais n'en envoie pas, et aussi vice versa. Pour cela, nous pouvons également créer un **canal unidirectionnel**. Regardons un exemple simple :

```go
package main

import (
 "fmt"
)

func main() {
 ch := make(chan string)
 
 go sc(ch)
 fmt.Println(<-ch)
}

func sc(ch chan<- string) {
 ch <- "hello"
}
```

Dans l'exemple ci-dessus, `sc` est une Go routine qui ne peut envoyer que des messages au canal mais ne peut pas recevoir de messages.

### Organiser plusieurs canaux pour une Go routine en utilisant select

Il peut y avoir plusieurs canaux qu'une fonction attend. Pour cela, nous pouvons utiliser une instruction select. Regardons un exemple pour plus de clarté :

```go
package main

import (
 "fmt"
 "time"
)

func main() {
 c1 := make(chan string)
 c2 := make(chan string)
 go speed1(c1)
 go speed2(c2)
 fmt.Println("Le premier à arriver est :")
 select {
 case s1 := <-c1:
  fmt.Println(s1)
 case s2 := <-c2:
  fmt.Println(s2)
 }
}

func speed1(ch chan string) {
 time.Sleep(2 * time.Second)
 ch <- "speed 1"
}

func speed2(ch chan string) {
 time.Sleep(1 * time.Second)
 ch <- "speed 2"
}
```

Dans l'exemple ci-dessus, le main attend deux canaux, c1 et c2. Avec l'instruction select case, la fonction main imprime le message envoyé par le canal qu'elle reçoit en premier.

**Canal tamponné**

Vous pouvez créer un canal tamponné dans go. Avec un canal tamponné, les messages envoyés au canal seront bloqués si le tampon est plein. Regardons l'exemple :

```go
package main

import "fmt"

func main(){
  ch := make(chan string, 2)
  ch <- "hello"
  ch <- "world"
  ch <- "!" # message supplémentaire dans le tampon
  fmt.Println(<-ch)
}

# => erreur fatale : toutes les goroutines sont endormies - deadlock !
```

Comme nous le voyons ci-dessus, pas plus de 2 messages ne sont acceptés par un canal.

#### Pourquoi Golang est-il réussi ?

> Simplicité... — Rob-pike

### Super !

Nous avons appris certains des principaux composants et fonctionnalités de Go.

1. Variables, Types de données
2. Tableaux, slices et maps
3. Fonctions
4. Boucles et instructions conditionnelles
5. Pointeurs
6. Packages
7. Méthodes, Structs et Interfaces
8. Gestion des erreurs
9. Concurrence — Go routines et canaux

Félicitations, vous avez maintenant une compréhension décente de Go.

> L'un de mes jours les plus productifs a été de jeter 1 000 lignes de code.

> — Ken Thompson

Ne vous arrêtez pas ici. Continuez à avancer. Pensez à une petite application et commencez à la construire.

[LinkedIn](https://www.linkedin.com/in/milap-neupane-99a4b565/), [Github](http://github.com/milap-neupane), [Twitter](https://twitter.com/_milap)

Également publié sur le blog de Milap Neupane : [Apprendre Go — de zéro à héros](https://milapneupane.com.np/2019/07/06/learning-golang-from-zero-to-hero/)