---
title: Le manuel Golang – Un guide pour débutants pour apprendre Go
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2023-05-25T18:11:18.000Z'
originalURL: https://freecodecamp.org/news/learn-golang-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738338718817/f95f88be-48a2-49ca-8d84-2bb09c65165f.png
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Le manuel Golang – Un guide pour débutants pour apprendre Go
seo_desc: 'The Go programming language has been exploding in popularity. Tons of companies
  are using Go to build scalable, modern, backend infrastructure.

  If you''re looking to learn a new programming language, Go is a great choice. It''s
  fast, lightweight, has a...'
---

Le langage de programmation Go a connu une explosion de popularité. De nombreuses entreprises utilisent Go pour construire des infrastructures backend modernes et scalables.

Si vous cherchez à apprendre un nouveau langage de programmation, Go est un *excellent* choix. Il est rapide, léger, dispose d'une communauté open source incroyable et est en fait assez facile à prendre en main.

Ceci est un manuel entièrement gratuit basé sur du texte. Si vous voulez commencer, il suffit de faire défiler vers le bas et de commencer à lire ! Cela dit, il existe deux autres options pour suivre le cours.

1. Essayez la version interactive de ce [cours Golang](https://boot.dev/learn/learn-golang) sur [Boot.dev](https://boot.dev/), complète avec des défis de codage et des projets

2. Regardez la vidéo de ce cours sur la chaîne YouTube de FreeCodeCamp (intégrée ci-dessous)

%[https://www.youtube.com/watch?v=un6ZyFkqFKo]

## Table des matières

1. [Pourquoi apprendre Go ?](#heading-chapter-1-pourquoi-apprendre-go)

2. [Comment compiler du code Go](#heading-chapter-2-comment-compiler-du-code-go)

3. [Variables en Go](#heading-chapter-3-variables-en-go)

4. [Fonctions en Go](#heading-chapter-4-fonctions-en-go)

5. [Structs en Go](#heading-chapter-5-structs-en-go)

6. [Interfaces en Go](#heading-chapter-6-interfaces-en-go)

7. [Erreurs en Go](#heading-chapter-7-erreurs-en-go)

8. [Boucles en Go](#heading-chapter-8-boucles-en-go)

9. [Tableaux et Slices en Go](#heading-chapter-9-tableaux-et-slices-en-go)

10. [Maps en Go](#heading-chapter-10-maps-en-go)

11. [Fonctions avancées en Go](#heading-chapter-11-fonctions-avancees-en-go)

12. [Pointeurs en Go](#heading-chapter-12-pointeurs-en-go)

13. [Environnement de développement local en Go](#heading-chapter-13-environnement-de-developpement-local-en-go)

14. [Canaux en Go](#heading-chapter-14-canaux-en-go)

15. [Mutexes en Go](#heading-chapter-15-mutexes-en-go)

16. [Génériques en Go](#heading-chapter-16-generiques-en-go)

## Chapitre 1 – Pourquoi apprendre Go ?

**Go est rapide, simple et productif.** Go est l'un des langages de programmation les plus rapides, surpassant JavaScript, Python et Ruby dans la plupart des benchmarks.

Cependant, le code Go ne s'exécute pas aussi vite que ses homologues compilés Rust et C. Cela dit, il se *compile* beaucoup plus rapidement qu'eux, ce qui rend l'expérience du développeur super productive. Malheureusement, il n'y a pas de combats à l'épée dans les équipes Go...

![Image](https://www.freecodecamp.org/news/content/images/2023/05/compiling.png align="left")

*Bande dessinée par* [*xkcd*](https://xkcd.com/303/)

Go a connu une croissance folle dans l'industrie du [développement backend](https://blog.boot.dev/backend/become-backend-developer/), donc si vous êtes intéressé par un [emploi en tant que développeur backend](https://blog.boot.dev/backend/backend-job-description/), [Go peut être un excellent choix](https://blog.boot.dev/golang/become-golang-backend-dev/) de technologie à ajouter à votre ceinture à outils.

### Comment télécharger et installer la chaîne d'outils Go

Je recommande généralement l'une des deux méthodes :

* [Téléchargement officiel](https://golang.org/doc/install)

* [Téléchargeur Webi](https://webinstall.dev/golang/)

Assurez-vous d'utiliser au moins la version `1.20`. Vous pouvez vérifier cela après l'installation en tapant :

```bash
go version
```

### Une note sur la structure d'un programme Go

Nous passerons en revue tout cela plus en détail plus tard, mais pour satisfaire votre curiosité pour l'instant, voici quelques détails sur le code :

```go
package main

import "fmt"

func main() {
	fmt.Println("hello world")
}
```

1. `package main` indique au compilateur Go que nous voulons que ce code soit compilé et exécuté en tant que programme autonome, par opposition à une bibliothèque importée par d'autres programmes.

2. `import fmt` importe le package `fmt` (formattage). Le package de formattage existe dans la bibliothèque standard de Go et nous permet de faire des choses comme imprimer du texte sur la console.

3. `func main()` définit la fonction `main`. `main` est le nom de la fonction qui sert de point d'entrée pour un programme Go.

Enregistrez le code ci-dessus dans un fichier appelé `main.go`, exécutez `go build`, puis exécutez l'exécutable résultant.

```bash
go build -o out
./out
```

Vous pouvez également utiliser le [Go playground](https://boot.dev/playground/go) de Bootdev pour essayer tous les extraits de ce cours directement depuis votre navigateur.

## Chapitre 2 – Comment compiler du code Go

### Que signifie être compilé ?

Les ordinateurs ont besoin de code machine – ils ne comprennent pas l'anglais ni même Go. Nous devons convertir notre code de haut niveau (Go) en langage machine, qui n'est en fait qu'un ensemble d'instructions qu'un matériel spécifique peut comprendre. Dans votre cas, votre CPU.

Le travail du compilateur Go est de prendre le code Go et de produire du code machine. Sur Windows, ce serait un fichier `.exe`. Sur Mac ou Linux, ce serait n'importe quel fichier exécutable.

Les ordinateurs ne savent pas comment faire quoi que ce soit à moins que nous, en tant que programmeurs, leur disions quoi faire. Malheureusement, les ordinateurs ne comprennent pas le langage humain. En fait, ils ne comprennent même pas les programmes informatiques non compilés.

Par exemple, le code :

```go
package main

import "fmt"

func main(){
  fmt.Println("hello world")
}
```

ne signifie *rien* pour un ordinateur.

### Les ordinateurs ont besoin de code machine

Le [CPU](https://en.wikipedia.org/wiki/Central_processing_unit) d'un ordinateur ne comprend que son propre *ensemble d'instructions*, que nous appelons "code machine". Les instructions sont des opérations mathématiques de base comme l'addition, la soustraction, la multiplication, et la capacité de sauvegarder des données temporairement.

Par exemple, un [processeur ARM](https://en.wikipedia.org/wiki/ARM_architecture) utilise l'instruction *ADD* lorsqu'il est fourni avec le nombre `0100` en binaire.

### Go, C, Rust, et ainsi de suite

Go, C et Rust sont tous des langages où le code est d'abord converti en code machine par le compilateur avant d'être exécuté.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/code-compiler-machine-code.png align="left")

### Compilé vs Interprété

%[https://www.youtube.com/watch?v=1CSPb2q94KQ]

Les programmes compilés peuvent être exécutés sans accès au code source original, et sans accès à un compilateur.

Par exemple, lorsque votre navigateur exécute le code que vous écrivez dans ce cours, il n'utilise pas le code original, juste le résultat compilé. Notez comment cela est différent des langages interprétés comme Python et JavaScript.

Avec Python et JavaScript, le code est interprété à l'exécution par un programme séparé connu sous le nom d'"interpréteur". Distribuer du code pour que les utilisateurs l'exécutent peut être fastidieux car ils doivent avoir un interpréteur installé, et ils doivent avoir accès au code source original.

### Exemples de langages compilés

* Go

* C

* C++

* Rust

### Exemples de langages interprétés

* JavaScript

* Python

* Ruby

![Image](https://www.freecodecamp.org/news/content/images/2023/05/ovHaWmS.jpg align="left")

*Illustration des langages compilés vs interprétés*

### Go est fortement typé

Go impose un typage fort et statique, ce qui signifie que les variables ne peuvent avoir qu'un seul type. Une variable `string` comme "hello world" ne peut pas être changée en `int`, comme le nombre `3`.

L'un des plus grands avantages du typage fort est que les erreurs peuvent être attrapées au moment de la "compilation". En d'autres termes, les bugs sont plus facilement attrapés à l'avance car ils sont détectés lorsque le code est compilé avant même qu'il ne s'exécute.

Contrastez cela avec la plupart des langages interprétés, où les types de variables sont dynamiques. Le typage dynamique peut conduire à des bugs subtils qui sont difficiles à détecter. Avec les langages interprétés, le code *doit* être exécuté (parfois en production si vous avez de la malchance 😨) pour attraper les erreurs de syntaxe et de type.

Par exemple, le code suivant échouera à la compilation car les chaînes de caractères et les entiers ne peuvent pas être additionnés ensemble :

```go
func main() {
	var username string = "wagslane"
	var password int = 20947382822

	// ne pas éditer en dessous de cette ligne
	fmt.Println("Authorization: Basic", username+":"+password)
}
```

### Les programmes Go sont légers

%[https://www.youtube.com/watch?v=L1nDnWUbs6k]

Les programmes Go sont assez légers. Chaque programme inclut une petite quantité de code "supplémentaire" qui est inclus dans le binaire exécutable. Ce code supplémentaire est appelé le [Go Runtime](https://go.dev/doc/faq#runtime). L'un des objectifs du runtime Go est de nettoyer la mémoire inutilisée à l'exécution.

En d'autres termes, le compilateur Go inclut une petite quantité de logique supplémentaire dans chaque programme Go pour faciliter l'écriture de code efficace en mémoire pour les développeurs.

En règle générale, les programmes Java utilisent *plus* de mémoire que les programmes Go comparables car Go n'utilise pas une machine virtuelle entière pour exécuter ses programmes, juste un petit runtime. Le runtime Go est suffisamment petit pour être inclus directement dans le code machine compilé de chaque programme Go.

D'autre part, les programmes Rust et C++ utilisent légèrement *moins* de mémoire que les programmes Go car plus de contrôle est donné au développeur pour optimiser l'utilisation de la mémoire du programme. Le runtime Go gère cela automatiquement pour nous.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/1_Ggs-bJxobwZmrbfuoWGpFw.png align="left")

*Graphique montrant la comparaison de l'utilisation de la mémoire inactive entre Java (162MB), Go (.86MB) et Rust (.36MB)*

Dans le graphique ci-dessus, [Dexter Darwich compare l'utilisation de la mémoire](https://medium.com/@dexterdarwich/comparison-between-java-go-and-rust-fdb21bd5fb7c) de trois programmes *très* simples écrits en Java, Go et Rust. Comme vous pouvez le voir, Go et Rust utilisent *très* peu de mémoire par rapport à Java.

## Chapitre 3 – Variables en Go

Les types de variables de base de Go sont :

```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias pour uint8

rune // alias pour int32
     // représente un point de code Unicode

float32 float64

complex64 complex128
```

Nous avons parlé des `string` et des `int` précédemment, et ces deux types devraient être assez explicites.

Un `bool` est une variable booléenne, ce qui signifie qu'elle a une valeur de `true` ou `false`. Les types à virgule flottante (`float32` et `float64`) sont utilisés pour les nombres qui ne sont pas des entiers – c'est-à-dire qu'ils ont des chiffres à droite de la virgule décimale, comme `3.14159`. Le type `float32` utilise 32 bits de précision, tandis que le type `float64` utilise 64 bits pour pouvoir stocker plus de chiffres de manière plus précise.

Ne vous inquiétez pas trop des intrications des autres types pour l'instant. Nous les couvrirons plus en détail au fur et à mesure de notre progression.

### Comment déclarer une variable

Les variables sont déclarées en utilisant le mot-clé `var`. Par exemple, pour déclarer une variable appelée `number` de type `int`, vous écririez :

```go
var number int
```

Pour déclarer une variable appelée `pi` pour qu'elle soit de type `float64` avec une valeur de `3.14159`, vous écririez :

```go
var pi float64 = 3.14159
```

La valeur d'une variable initialisée sans affectation sera sa [valeur zéro](https://tour.golang.org/basics/12).

### Déclaration de variable courte

À l'intérieur d'une fonction (même la fonction principale), l'instruction d'affectation courte `:=` peut être utilisée à la place d'une déclaration `var`. L'opérateur `:=` infère le type de la nouvelle variable en fonction de la valeur.

```go
var empty string
```

Est la même chose que :

```go
empty := ""
```

```go
numCars := 10 // inféré comme étant un entier

temperature := 0.0 // temperature est inféré comme étant une valeur à virgule flottante car il a un point décimal

var isFunny = true // isFunny est inféré comme étant un booléen
```

En dehors d'une fonction (dans la [portée globale/du package](https://dave.cheney.net/2017/06/11/go-without-package-scoped-variables)), chaque instruction commence par un mot-clé (`var`, `func`, et ainsi de suite) et donc la construction `:=` n'est pas disponible.

### Inférence de type

Pour déclarer une variable sans spécifier un type explicite (soit en utilisant la syntaxe `:=` ou `var = expression`), le type de la variable est *inféré* à partir de la valeur du côté droit.

Lorsque le côté droit de la déclaration est typé, la nouvelle variable est de ce même type :

```go
var i int
j := i // j est aussi un int
```

Cependant, lorsque le côté droit est une valeur littérale (une constante numérique non typée comme `42` ou `3.14`), la nouvelle variable sera un `int`, `float64`, ou `complex128` selon sa précision :

```go
i := 42           // int
f := 3.14         // float64
g := 0.867 + 0.5i // complex128
```

### Déclarations sur la même ligne

Nous pouvons déclarer plusieurs variables sur la même ligne :

```go
mileage, company := 80276, "Tesla"

// est la même chose que

mileage := 80276
company := "Tesla"
```

### Tailles des types

Les entiers, [uints](https://www.cs.utah.edu/~germain/PPS/Topics/unsigned_integer.html#:~:text=Unsigned%20Integers,negative%20\(zero%20or%20positive\).), [floats](https://techterms.com/definition/floatingpoint), et [complex](https://www.cloudhadoop.com/2018/12/golang-tutorials-complex-types-numbers.html#:~:text=Golang%20Complex%20Type%20Numbers,complex%20number%20is%2012.8i.) les nombres ont tous des tailles de type.

```go
int  int8  int16  int32  int64 // nombres entiers

uint uint8 uint16 uint32 uint64 uintptr // nombres entiers positifs

float32 float64 // nombres décimaux

complex64 complex128 // nombres imaginaires (rares)
```

La taille (8, 16, 32, 64, 128, et ainsi de suite) indique combien de bits en mémoire seront utilisés pour stocker la variable. Les types `int` et `uint` par défaut sont simplement des alias qui font référence à leurs tailles respectives de 32 ou 64 bits selon l'environnement de l'utilisateur.

Les tailles standard qui [devraient être utilisées](https://blog.boot.dev/golang/default-native-types-golang/) sauf si vous avez un besoin spécifique sont :

* `int`

* `uint`

* `float64`

* `complex128`

Certains types peuvent être convertis de la manière suivante :

```go
temperatureInt := 88
temperatureFloat := float64(temperatureInt)
```

La conversion d'un float en entier de cette manière [tronque](https://techterms.com/definition/truncate) la partie à virgule flottante.

### **Quel type devrais-je utiliser ?**

Avec autant de types pour ce qui est essentiellement juste un nombre, les développeurs venant de langages qui n'ont qu'un seul type de `Number` (comme JavaScript) peuvent trouver les choix intimidants.

Un problème survient lorsque nous avons un `uint16`, et que la fonction que nous essayons de lui passer prend un `int`. Nous sommes obligés d'écrire du code rempli de casts de type comme `int(myUint16)`.

Ce style de développement peut être lent et ennuyeux à lire. Lorsque les développeurs Go s'éloignent du type "par défaut" pour une famille de types donnée, le code peut devenir désordonné rapidement.

Sauf si vous avez une bonne raison de le faire, restez avec les types suivants :

* `bool`

* `string`

* `int`

* `uint`

* `byte`

* `rune`

* `float64`

* `complex128`

### Constantes

Les constantes sont déclarées comme des variables mais utilisent le mot-clé `const`. Les constantes ne peuvent pas utiliser la syntaxe de déclaration courte `:=`.

Les constantes peuvent être des caractères, des chaînes de caractères, des valeurs booléennes ou numériques. Elles *ne peuvent pas* être des types plus complexes comme les slices, les maps et les structs, que je vais expliquer plus tard.

Comme le nom l'indique, la valeur d'une constante ne peut pas être changée après avoir été déclarée.

[Les constantes *doivent* être connues au moment de la compilation](https://blog.boot.dev/clean-code/constants-in-go-vs-javascript-and-when-to-use-them/). Le plus souvent, elles seront déclarées avec une valeur statique :

```go
const myInt = 15
```

Cependant, les constantes *peuvent être calculées* tant que le calcul peut se faire au moment de la compilation. Par exemple, ceci est valide :

```go
const firstName = "Lane"
const lastName = "Wagner"
const fullName = firstName + " " + lastName
```

Cela dit, vous ne pouvez pas déclarer une constante qui ne peut être calculée qu'à l'exécution.

### Comment formater les chaînes de caractères en Go

Go suit la [tradition printf](https://cplusplus.com/reference/cstdio/printf/) du langage C. À mon avis, le formatage/interpolation des chaînes de caractères en Go est actuellement *moins* élégant qu'en JavaScript et Python.

* [fmt.Printf](https://pkg.go.dev/fmt#Printf) – Imprime une chaîne de caractères formatée sur la [sortie standard](https://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr)

* [fmt.Sprintf()](https://pkg.go.dev/fmt#Sprintf) – Retourne la chaîne de caractères formatée

### Exemples

Ces verbes de formatage fonctionnent à la fois avec `fmt.Printf` et `fmt.Sprintf`.

#### `%v` - Interpoler la représentation par défaut

Le variant `%v` imprime la représentation de la syntaxe Go d'une valeur. Vous pouvez généralement utiliser ceci si vous n'êtes pas sûr de quoi utiliser d'autre. Cela dit, il est préférable d'utiliser le variant spécifique au type si vous le pouvez.

```go
s := fmt.Sprintf("I am %v years old", 10)
// I am 10 years old

s := fmt.Sprintf("I am %v years old", "way too many")
// I am way too many years old
```

#### `%s` - Interpoler une chaîne de caractères

```go
s := fmt.Sprintf("I am %s years old", "way too many")
// I am way too many years old
```

#### `%d` - Interpoler un entier en forme décimale

```go
s := fmt.Sprintf("I am %d years old", 10)
// I am 10 years old
```

#### `%f` - Interpoler un décimal

```go
s := fmt.Sprintf("I am %f years old", 10.523)
// I am 10.523000 years old

// Le ".2" arrondit le nombre à 2 décimales
s := fmt.Sprintf("I am %.2f years old", 10.523)
// I am 10.53 years old
```

Si vous êtes intéressé par toutes les options de formatage, n'hésitez pas à consulter la documentation du package `fmt` [ici](https://pkg.go.dev/fmt#hdr-Printing).

### Conditionnelles

Les instructions `if` en Go n'utilisent pas de parenthèses autour de la condition :

```go
if height > 4 {
    fmt.Println("You are tall enough!")
}
```

`else if` et `else` sont supportés comme vous pourriez vous y attendre :

```go
if height > 6 {
    fmt.Println("You are super tall!")
} else if height > 4 {
    fmt.Println("You are tall enough!")
} else {
    fmt.Println("You are not tall enough!")
}
```

### L'instruction initiale d'un bloc if

Une conditionnelle `if` peut avoir une instruction "initiale". Les variables créées dans l'instruction initiale ne sont définies que dans la portée du corps de l'`if`.

```go
if INITIAL_STATEMENT; CONDITION {
}
```

Ce n'est qu'un peu de sucre syntaxique que Go offre pour raccourcir le code dans certains cas. Par exemple, au lieu d'écrire :

```go
length := getLength(email)
if length < 1 {
    fmt.Println("Email is invalid")
}
```

Nous pouvons faire :

```go
if length := getLength(email); length < 1 {
    fmt.Println("Email is invalid")
}
```

Non seulement ce code est un peu plus court, mais il supprime également `length` de la portée parente. C'est pratique car nous n'en avons pas besoin là-bas – nous avons seulement besoin d'y accéder lors de la vérification d'une condition.

## Chapitre 4 – Fonctions en Go

Les fonctions en Go peuvent prendre zéro ou plusieurs arguments.

Pour rendre le code Go plus facile à lire, le type de variable vient *après* le nom de la variable.

Par exemple, la fonction suivante :

```go
func sub(x int, y int) int {
  return x-y
}
```

Accepte deux paramètres entiers et retourne un autre entier.

Ici, `func sub(x int, y int) int` est connu comme la "signature de la fonction".

### Paramètres multiples

Lorsque plusieurs arguments sont du même type, le type n'a besoin d'être déclaré qu'après le dernier, en supposant qu'ils sont dans l'ordre.

Par exemple :

```go
func add(x, y int) int {
  return x + y
}
```

S'ils ne sont pas dans l'ordre, ils doivent être définis séparément.

### Syntaxe de déclaration de fonction

Les développeurs se demandent souvent pourquoi la syntaxe de déclaration en Go est différente de la tradition établie dans la famille de langages C.

#### Syntaxe de style C

Le langage C décrit les types avec une expression incluant le nom à déclarer, et indique de quel type sera cette expression.

```c
int y;
```

Le code ci-dessus déclare `y` comme un `int`. En général, le type va à gauche et l'expression à droite.

Intéressamment, les créateurs du langage Go ont convenu que le style C de déclaration des types dans les signatures devient confus très rapidement – jetez un coup d'œil à ce cauchemar.

```c
int (*fp)(int (*ff)(int x, int y), int b)
```

#### Syntaxe de style Go

Les déclarations de Go sont claires, vous les lisez simplement de gauche à droite, comme vous le feriez en anglais.

```go
x int
p *int
a [3]int
```

C'est bien pour des signatures plus complexes, car cela les rend plus faciles à lire.

```go
f func(func(int,int) int, int) int
```

### Comment passer des variables par valeur

Les variables en Go sont passées par valeur (sauf pour quelques types de données que nous n'avons pas encore couverts). "Passer par valeur" signifie que lorsqu'une variable est passée dans une fonction, cette fonction reçoit une *copie* de la variable. La fonction est incapable de muter les données originales de l'appelant.

```go
func main(){
    x := 5
    increment(x)

    fmt.Println(x)
    // imprime toujours 5,
    // car la fonction increment
    // a reçu une copie de x
}

func increment(x int){
    x++
}
```

### Comment ignorer les valeurs de retour

Une fonction peut retourner une valeur dont l'appelant ne se soucie pas. Nous pouvons explicitement ignorer les variables en utilisant un underscore : `_`

Par exemple :

```go
func getPoint() (x int, y int) {
  return 3, 4
}

// ignorer la valeur y
x, _ := getPoint()
```

Même si `getPoint()` retourne deux valeurs, nous pouvons capturer la première et ignorer la seconde.

#### Pourquoi ignorer une valeur de retour ?

Il pourrait y avoir de nombreuses raisons. Par exemple, peut-être qu'une fonction appelée `getCircle` retourne le point central et le rayon, mais vous avez vraiment seulement besoin du rayon pour votre calcul. Dans ce cas, vous ignoreriez la variable du point central.

C'est crucial à comprendre car le compilateur Go générera une erreur si vous avez des déclarations de variables inutilisées dans votre code, donc vous *devez* ignorer tout ce que vous n'avez pas l'intention d'utiliser.

### Valeurs de retour nommées

Les valeurs de retour peuvent être nommées, et si elles le sont, alors elles sont traitées de la même manière que si elles étaient de nouvelles variables définies en haut de la fonction.

Les valeurs de retour nommées sont mieux considérées comme un moyen de documenter le but des valeurs retournées.

Selon le [tour de go](https://tour.golang.org/) :

> "Une instruction return sans arguments retourne les valeurs de retour nommées. Cela est connu comme un return "nu". Les instructions return nues doivent être utilisées uniquement dans les fonctions courtes. Elles peuvent nuire à la lisibilité dans les fonctions plus longues."

```go
func getCoords() (x, y int){
  // x et y sont initialisés avec des valeurs zéro

  return // retourne automatiquement x et y
}
```

Est la même chose que :

```go
func getCoords() (int, int){
  var x int
  var y int
  return x, y
}
```

Dans le premier exemple, `x` et `y` sont les valeurs de retour. À la fin de la fonction, nous pourrions simplement écrire `return` pour retourner les valeurs de ces deux variables, plutôt que d'écrire `return x,y`.

### Retours explicites

Même si une fonction a des valeurs de retour nommées, nous pouvons toujours retourner explicitement des valeurs si nous le voulons.

```go
func getCoords() (x, y int){
  return x, y // ceci est explicite
}
```

En utilisant ce modèle explicite, nous pouvons même écraser les valeurs de retour :

```go
func getCoords() (x, y int){
  return 5, 6 // ceci est explicite, x et y ne sont PAS retournés
}
```

Sinon, si nous voulons retourner les valeurs définies dans la signature de la fonction, nous pouvons simplement utiliser un `return` nu (retour vide) :

```go
func getCoords() (x, y int){
  return // retourne implicitement x et y
}
```

### Les avantages des retours nommés

1. #### Bon pour la documentation (compréhension)

Les paramètres de retour nommés sont excellents pour documenter une fonction. Nous savons ce que la fonction retourne directement à partir de sa signature, pas besoin de commentaire.

Les paramètres de retour nommés sont particulièrement importants dans les fonctions plus longues avec de nombreuses valeurs de retour.

```go
func calculator(a, b int) (mul, div int, err error) {
    if b == 0 {
      return 0, 0, errors.New("Can't divide by zero")
    }
    mul = a * b
    div = a / b
    return mul, div, nil
}
```

Ce qui est plus facile à comprendre que :

```go
func calculator(a, b int) (int, int, error) {
    if b == 0 {
      return 0, 0, errors.New("Can't divide by zero")
    }
    mul := a * b
    div := a / b
    return mul, div, nil
}
```

Nous connaissons *la signification* de chaque valeur de retour simplement en regardant la signature de la fonction : `func calculator(a, b int) (mul, div int, err error)`

#### Moins de code (parfois)

S'il y a plusieurs instructions de retour dans une fonction, vous n'avez pas besoin d'écrire toutes les valeurs de retour à chaque fois, bien que vous devriez probablement le faire.

Lorsque vous choisissez d'omettre les valeurs de retour, cela s'appelle un retour *nu*. Les retours nus ne doivent être utilisés que dans des fonctions courtes et simples.

### Retours anticipés

Go prend en charge la capacité de retourner tôt d'une fonction. C'est une fonctionnalité puissante qui peut nettoyer le code, surtout lorsqu'elle est utilisée comme [clauses de garde](https://blog.boot.dev/clean-code/guard-clauses/).

Les clauses de garde exploitent la capacité de `return` tôt d'une fonction (ou `continue` à travers une boucle) pour rendre les conditionnelles imbriquées unidimensionnelles. Au lieu d'utiliser des chaînes if/else, nous retournons simplement tôt de la fonction à la fin de chaque bloc conditionnel.

```go
func divide(dividend, divisor int) (int, error) {
	if divisor == 0 {
		return 0, errors.New("Can't divide by zero")
	}
	return dividend/divisor, nil
}
```

La gestion des erreurs en Go encourage naturellement les développeurs à utiliser des clauses de garde. Lorsque j'ai commencé à écrire plus de JavaScript, j'ai été déçu de voir combien de conditionnelles imbriquées existaient dans le code sur lequel je travaillais.

Prenons un exemple exagéré de logique conditionnelle imbriquée :

```go
func getInsuranceAmount(status insuranceStatus) int {
  amount := 0
  if !status.hasInsurance(){
    amount = 1
  } else {
    if status.isTotaled(){
      amount = 10000
    } else {
      if status.isDented(){
        amount = 160
        if status.isBigDent(){
          amount = 270
        }
      } else {
        amount = 0
      }
    }
  }
  return amount
}
```

Cela pourrait être écrit avec des clauses de garde à la place :

```go
func getInsuranceAmount(status insuranceStatus) int {
  if !status.hasInsurance(){
    return 1
  }
  if status.isTotaled(){
    return 10000
  }
  if !status.isDented(){
    return 0
  }
  if status.isBigDent(){
    return 270
  }
  return 160
}
```

L'exemple ci-dessus est beaucoup plus facile à lire et à comprendre. Lorsque vous écrivez du code, il est important d'essayer de réduire la charge cognitive du lecteur en réduisant le nombre d'entités auxquelles il doit penser à un moment donné.

Dans le premier exemple, si le développeur essaie de comprendre *quand* 270 est retourné, il doit penser à chaque branche de l'arbre logique et essayer de se souvenir des cas qui comptent et de ceux qui ne comptent pas.

Avec la structure unidimensionnelle offerte par les clauses de garde, c'est aussi simple que de passer par chaque cas dans l'ordre.

## Chapitre 5 – Structs en Go

Nous utilisons des structs en Go pour représenter des données structurées. Il est souvent pratique de regrouper différents types de variables ensemble. Par exemple, si nous voulons représenter une voiture, nous pourrions faire ce qui suit :

```go
type car struct {
  Make string
  Model string
  Height int
  Width int
}
```

Cela crée un nouveau type de struct appelé `car`. Toutes les voitures ont un `Make`, `Model`, `Height` et `Width`.

En Go, vous utiliserez souvent une struct pour représenter des informations que vous auriez utilisées un dictionnaire en Python, ou un littéral d'objet en JavaScript.

### Structs imbriquées en Go

Les structs peuvent être imbriquées pour représenter des entités plus complexes :

```go
type car struct {
  Make string
  Model string
  Height int
  Width int
  FrontWheel Wheel
  BackWheel Wheel
}

type Wheel struct {
  Radius int
  Material string
}
```

Les champs d'une struct peuvent être accédés en utilisant l'opérateur point `.`.

```go
myCar := car{}
myCar.FrontWheel.Radius = 5
```

### Structs anonymes

Une [struct anonyme](https://blog.boot.dev/golang/anonymous-structs-golang/) est comme une struct régulière, mais elle est définie sans nom et ne peut donc pas être référencée ailleurs dans le code.

Pour créer une struct anonyme, il suffit d'instancier l'instance immédiatement en utilisant une deuxième paire d'accolades après avoir déclaré le type :

```go
myCar := struct {
  Make string
  Model string
} {
  Make: "tesla",
  Model: "model 3"
}
```

Vous pouvez même imbriquer des structs anonymes en tant que champs dans d'autres structs :

```go
type car struct {
  Make string
  Model string
  Height int
  Width int
  // Wheel est un champ contenant une struct anonyme
  Wheel struct {
    Radius int
    Material string
  }
}
```

#### Quand devriez-vous utiliser une struct anonyme ?

En général, *préférez les structs nommées*. Les structs nommées rendent votre code plus facile à lire et à comprendre, et elles ont l'effet secondaire agréable d'être réutilisables. J'utilise parfois des structs anonymes lorsque je sais que je n'aurai plus jamais besoin d'utiliser une struct. Par exemple, parfois j'en utilise une pour créer la forme de certaines données JSON dans les gestionnaires HTTP.

Si une struct est destinée à être utilisée une seule fois, alors il est logique de la déclarer de manière à ce que les développeurs plus tard ne soient pas tentés de l'utiliser à nouveau par accident.

Vous pouvez lire plus sur les [structs anonymes ici](https://blog.boot.dev/golang/anonymous-structs-golang/) si vous êtes curieux.

### Structs intégrées

Go n'est pas un langage [orienté objet](https://boot.dev/learn/learn-object-oriented-programming). Mais les structs intégrées fournissent une sorte d'*héritage de données uniquement* qui peut être utile à certains moments.

Gardez à l'esprit, Go ne supporte pas les classes ou l'héritage au sens complet. Les structs intégrées sont juste un moyen d'élever et de partager des champs entre les définitions de structs.

```go
type car struct {
  make string
  model string
}

type truck struct {
  // "car" est intégré, donc la définition d'un
  // "truck" contient maintenant également tous
  // les champs de la struct car
  car
  bedSize int
}
```

#### Intégré vs imbriqué

* Les champs d'une struct intégrée sont accédés au niveau supérieur, contrairement aux structs imbriquées.

* Les champs promus peuvent être accédés comme des champs normaux sauf qu'ils ne peuvent pas être utilisés dans les [littéraux composites](https://golang.org/ref/spec#Composite_literals)

```go
lanesTruck := truck{
  bedSize: 10,
  car: car{
    make: "toyota",
    model: "camry",
  },
}

fmt.Println(lanesTruck.bedSize)

// les champs intégrés sont promus au niveau supérieur
// au lieu de lanesTruck.car.make
fmt.Println(lanesTruck.make)
fmt.Println(lanesTruck.model)
```

### Méthodes de struct

Bien que Go ne soit **pas** orienté objet, il supporte les méthodes qui peuvent être définies sur des structs. Les méthodes sont simplement des fonctions qui ont un récepteur. Un récepteur est un paramètre spécial qui se place syntaxiquement *avant* le nom de la fonction.

```go
type rect struct {
  width int
  height int
}

// area a un récepteur de (r rect)
func (r rect) area() int {
  return r.width * r.height
}

r := rect{
  width: 5,
  height: 10,
}

fmt.Println(r.area())
// imprime 50
```

Un récepteur est juste un type spécial de paramètre de fonction. Les récepteurs sont importants car ils nous permettront, comme vous l'apprendrez dans les exercices à venir, de définir des interfaces que nos structs (et autres types) peuvent implémenter.

## Chapitre 6 – Interfaces en Go

Les [interfaces](https://blog.boot.dev/golang/golang-interfaces/) sont des collections de signatures de méthodes. Un type "implémente" une interface s'il a toutes les méthodes de l'interface donnée définies sur lui.

Dans l'exemple suivant, une "forme" doit pouvoir retourner sa surface et son périmètre. Les deux `rect` et `circle` remplissent l'interface.

```go
type shape interface {
  area() float64
  perimeter() float64
}

type rect struct {
    width, height float64
}
func (r rect) area() float64 {
    return r.width * r.height
}
func (r rect) perimeter() float64 {
    return 2*r.width + 2*r.height
}

type circle struct {
    radius float64
}
func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}
func (c circle) perimeter() float64 {
    return 2 * math.Pi * c.radius
}
```

Lorsque qu'un type implémente une interface, il peut alors être utilisé comme le type de l'interface.

Les interfaces sont implémentées *implicitement*.

Un type ne déclare jamais qu'il implémente une interface donnée. Si une interface existe et qu'un type a les méthodes appropriées définies, alors le type remplit automatiquement cette interface.

### Interfaces multiples

Un type peut implémenter n'importe quel nombre d'interfaces en Go. Par exemple, l'interface vide, `interface{}`, est *toujours* implémentée par chaque type car elle n'a pas d'exigences.

### Nommer les arguments des interfaces

Considérez l'interface suivante :

```go
type Copier interface {
  Copy(string, string) int
}
```

Sur la base du code seul, pouvez-vous déduire *quels* types de chaînes de caractères vous devriez passer dans la fonction `Copy` ?

Nous savons que la signature de la fonction attend 2 types de chaînes de caractères, mais quels sont-ils ? Des noms de fichiers ? Des URLs ? Des données de chaînes de caractères brutes ? À ce sujet, qu'est-ce que cet `int` qui est retourné ?

Ajoutons quelques arguments et données de retour nommés pour que ce soit plus clair.

```go
type Copier interface {
  Copy(sourceFile string, destinationFile string) (bytesCopied int)
}
```

Beaucoup mieux. Nous pouvons voir quelles sont les attentes maintenant. Le premier argument est le `sourceFile`, le deuxième argument est le `destinationFile`, et `bytesCopied`, un entier, est retourné.

### Assertions de type en Go

Lorsque vous travaillez avec des interfaces en Go, de temps en temps vous aurez besoin d'accéder au type sous-jacent d'une valeur d'interface. Vous pouvez convertir une interface en son type sous-jacent en utilisant une *assertion de type*.

```go
type shape interface {
	area() float64
}

type circle struct {
	radius float64
}

// "c" est un nouveau cercle converti à partir de "s"
// qui est une instance d'une forme.
// "ok" est un booléen qui est vrai si s était un cercle
// ou faux si s n'est pas un cercle
c, ok := s.(circle)
if !ok {
	// s n'était pas un cercle
	log.Fatal("s is not a circle")
}

radius := c.radius
```

### Switch de type en Go

Un *switch de type* facilite l'exécution de plusieurs assertions de type en série.

Un switch de type est similaire à une instruction switch normale, mais les cas spécifient des *types* au lieu de *valeurs*.

```go
func printNumericValue(num interface{}) {
	switch v := num.(type) {
	case int:
		fmt.Printf("%T\n", v)
	case string:
		fmt.Printf("%T\n", v)
	default:
		fmt.Printf("%T\n", v)
	}
}

func main() {
	printNumericValue(1)
	// imprime "int"

	printNumericValue("1")
	// imprime "string"

	printNumericValue(struct{}{})
	// imprime "struct {}"
}
```

`fmt.Printf("%T\n", v)` imprime le *type* d'une variable.

### Interfaces propres

Écrire des interfaces propres est *difficile*. Franchement, chaque fois que vous traitez avec des abstractions dans le code, le simple peut devenir complexe très rapidement si vous n'êtes pas prudent. Passons en revue quelques [règles de base pour garder les interfaces propres](https://blog.boot.dev/golang/golang-interfaces/).

#### 1. Gardez les interfaces petites

Si il n'y a qu'un seul conseil que vous retenez de cet article, faites en sorte que ce soit celui-ci : gardez les interfaces petites ! Les interfaces sont destinées à définir le comportement minimal nécessaire pour représenter précisément une idée ou un concept.

Voici un exemple du package HTTP standard d'une interface plus grande qui est un bon exemple de définition de comportement minimal :

```go
type File interface {
    io.Closer
    io.Reader
    io.Seeker
    Readdir(count int) ([]os.FileInfo, error)
    Stat() (os.FileInfo, error)
}
```

Tout type qui satisfait les comportements de l'interface peut être considéré par le package HTTP comme un *File*. C'est pratique car le package HTTP n'a pas besoin de savoir s'il traite avec un fichier sur disque, un tampon réseau, ou un simple `[]byte`.

#### 2. Les interfaces ne devraient avoir aucune connaissance des types satisfaisants

Une interface devrait définir ce qui est nécessaire pour que d'autres types soient classés comme membre de cette interface. Elles ne devraient pas être conscientes des types qui se trouvent satisfaire l'interface au moment de la conception.

Par exemple, supposons que nous construisons une interface pour décrire les composants nécessaires pour définir une voiture.

```go
type car interface {
	Color() string
	Speed() int
	IsFiretruck() bool
}
```

`Color()` et `Speed()` ont parfaitement du sens, ce sont des méthodes limitées à la portée d'une voiture. `IsFiretruck()` est un anti-pattern. Nous forçons toutes les voitures à déclarer si elles sont des camions de pompiers ou non. Pour que ce pattern ait un quelconque sens, nous aurions besoin d'une liste entière de sous-types possibles. `IsPickup()`, `IsSedan()`, `IsTank()`... où cela s'arrête-t-il ??

Au lieu de cela, le développeur aurait dû s'appuyer sur la fonctionnalité native de l'assertion de type pour dériver le type sous-jacent lorsqu'une instance de l'interface voiture est donnée. Ou, si une sous-interface est nécessaire, elle peut être définie comme :

```go
type firetruck interface {
	car
	HoseLength() int
}
```

Qui hérite des méthodes requises de `car` et ajoute une méthode requise supplémentaire pour faire de la `car` un `firetruck`.

#### 3. Les interfaces ne sont pas des classes

* Les interfaces ne sont pas des classes, elles sont plus légères.

* Les interfaces n'ont pas de constructeurs ou de destructeurs qui nécessitent que des données soient créées ou détruites.

* Les interfaces ne sont pas hiérarchiques par nature, bien qu'il existe un sucre syntaxique pour créer des interfaces qui se trouvent être des sur-ensembles d'autres interfaces.

* Les interfaces définissent des signatures de fonctions, mais pas le comportement sous-jacent. Faire une interface n'assécherait souvent pas votre code en ce qui concerne les méthodes de struct. Par exemple, si cinq types satisfont l'interface `fmt.Stringer`, ils ont tous besoin de leur propre version de la fonction `String()`.

## Chapitre 7 – Erreurs en Go

%[https://www.youtube.com/watch?v=Nf17bnV2Tlw]

Les programmes Go expriment les erreurs avec des valeurs `error`. Une Erreur est tout type qui implémente l'interface simple intégrée [error interface](https://blog.golang.org/error-handling-and-go) :

```go
type error interface {
    Error() string
}
```

Lorsque quelque chose peut mal se passer dans une fonction, cette fonction doit retourner un `error` comme dernière valeur de retour. Tout code qui appelle une fonction qui peut retourner un `error` doit gérer les erreurs en testant si l'erreur est `nil`.

```go
// Atoi convertit un nombre sous forme de chaîne en un entier
i, err := strconv.Atoi("42b")
if err != nil {
    fmt.Println("couldn't convert:", err)
    // parce que "42b" n'est pas un entier valide, nous imprimons :
    // couldn't convert: strconv.Atoi: parsing "42b": invalid syntax
    // Note:
    // 'parsing "42b": invalid syntax' est retourné par la méthode .Error()
    return
}
// si nous arrivons ici, alors
// i a été converti avec succès
```

Une erreur `nil` indique un succès. Une erreur non-nil indique un échec.

### L'interface d'erreur

Parce que les erreurs sont juste des interfaces, vous pouvez construire vos propres types personnalisés qui implémentent l'interface `error`. Voici un exemple de struct `userError` qui implémente l'interface `error` :

```go
type userError struct {
    name string
}

func (e userError) Error() string {
    return fmt.Sprintf("%v has a problem with their account", e.name)
}
```

Il peut ensuite être utilisé comme une erreur :

```go
func sendSMS(msg, userName string) error {
    if !canSendToUser(userName) {
        return userError{name: userName}
    }
    ...
}
```

Les programmes Go expriment les erreurs avec des valeurs `error`. Les valeurs d'erreur sont tout type qui implémente l'interface simple intégrée [error interface](https://blog.golang.org/error-handling-and-go).

Gardez à l'esprit que la manière dont Go gère les erreurs est assez unique. La plupart des langages traitent les erreurs comme quelque chose de spécial et de différent. Par exemple, Python lève des types d'exception et JavaScript lance et attrape des erreurs.

En Go, une `error` est juste une autre valeur que nous gérons comme n'importe quelle autre valeur – cependant, comme nous le voulons ! Il n'y a pas de mots-clés spéciaux pour les gérer.

### Le package errors

La bibliothèque standard de Go fournit un package "errors" qui facilite la gestion des erreurs.

Lisez la godoc pour la fonction [errors.New()](https://pkg.go.dev/errors#New), mais voici un exemple simple :

```go
var err error = errors.New("something went wrong")
```

## Chapitre 8 – Boucles en Go

La [boucle de base en Go](https://blog.boot.dev/golang/golang-for-loop/) est écrite en syntaxe standard de type C :

```go
for INITIAL; CONDITION; AFTER{
  // faire quelque chose
}
```

`INITIAL` est exécuté une fois au début de la boucle et peut créer des variables dans la portée de la boucle.

`CONDITION` est vérifiée avant chaque itération. Si la condition n'est pas remplie, la boucle se rompt.

`AFTER` est exécuté après chaque itération.

Par exemple :

```go
for i := 0; i < 10; i++ {
  fmt.Println(i)
}
// Imprime de 0 à 9
```

### Comment omettre les conditions

Les boucles en Go peuvent omettre des sections d'une boucle for. Par exemple, la `CONDITION` (partie du milieu) peut être omise, ce qui fait que la boucle s'exécute indéfiniment.

```go
for INITIAL; ; AFTER {
  // faire quelque chose indéfiniment
}
```

### Pas de boucles while en Go

La plupart des langages de programmation ont un concept de boucle `while`. Parce que Go permet l'omission de sections d'une boucle `for`, une boucle `while` est simplement une boucle `for` qui n'a qu'une CONDITION.

```go
for CONDITION {
  // faire des choses tant que CONDITION est vraie
}
```

Par exemple :

```go
plantHeight := 1
for plantHeight < 5 {
  fmt.Println("still growing! current height:", plantHeight)
  plantHeight++
}
fmt.Println("plant has grown to ", plantHeight, "inches")
```

Ce qui imprime :

```python
still growing! current height: 1
still growing! current height: 2
still growing! current height: 3
still growing! current height: 4
plant has grown to 5 inches
```

### Continuer à travers une boucle

Le mot-clé `continue` arrête l'itération actuelle d'une boucle et passe à l'itération suivante. `continue` est un moyen puissant d'utiliser le motif de "clause de garde" au sein des boucles.

```go
for i := 0; i < 10; i++ {
  if i % 2 == 0 {
    continue
  }
  fmt.Println(i)
}
// 1
// 3
// 5
// 7
// 9
```

### Sortir d'une boucle

Le mot-clé `break` arrête l'itération actuelle d'une boucle et quitte la boucle.

```go
for i := 0; i < 10; i++ {
  if i == 5 {
    break
  }
  fmt.Println(i)
}
// 0
// 1
// 2
// 3
// 4
```

## Chapitre 9 – Tableaux et Slices en Go

%[https://www.youtube.com/watch?v=NFF2usIBX-U]

### Tableaux

Les tableaux sont des groupes de variables de même type de taille fixe.

Le type `[n]T` est un tableau de n valeurs de type `T`.

Pour déclarer un tableau de 10 entiers :

```go
var myInts [10]int
```

ou pour déclarer un littéral initialisé :

```go
primes := [6]int{2, 3, 5, 7, 11, 13}
```

### Slices

*99 fois sur 100* vous utiliserez un slice au lieu d'un tableau lorsque vous travaillerez avec des listes ordonnées.

Les tableaux sont de taille fixe. Une fois que vous avez créé un tableau comme `[10]int`, vous ne pouvez pas ajouter un 11ème élément.

Un slice est une vue *dynamiquement dimensionnée*, *flexible* des éléments d'un tableau.

Les slices ont **toujours** un tableau sous-jacent, bien qu'il ne soit pas toujours spécifié explicitement. Pour créer explicitement un slice sur un tableau, nous pouvons faire :

```go
primes := [6]int{2, 3, 5, 7, 11, 13}
mySlice := primes[1:4]
// mySlice = {3, 5, 7}
```

La syntaxe est :

```python
arrayname[lowIndex:highIndex]
arrayname[lowIndex:]
arrayname[:highIndex]
arrayname[:]
```

Où `lowIndex` est inclusif et `highIndex` est exclusif

Soit `lowIndex` ou `highIndex` ou les deux peuvent être omis pour utiliser le tableau entier de ce côté.

### Comment créer de nouveaux Slices en Go

La plupart du temps, nous n'avons pas besoin de penser au tableau sous-jacent d'un slice. Nous pouvons créer un nouveau slice en utilisant la fonction `make` :

```go
// func make([]T, len, cap) []T
mySlice := make([]int, 5, 10)

// l'argument de capacité est généralement omis et par défaut égal à la longueur
mySlice := make([]int, 5)
```

Les slices créés avec `make` seront remplis avec la valeur zéro du type.

Si nous voulons créer un slice avec un ensemble spécifique de valeurs, nous pouvons utiliser un littéral de slice :

```go
mySlice := []string{"I", "love", "go"}
```

Notez que les crochets du tableau *ne contiennent pas* un `3`. S'ils le faisaient, vous auriez un *tableau* au lieu d'un slice.

#### Longueur

La longueur d'un slice est simplement le nombre d'éléments qu'il contient. Elle est accessible en utilisant la fonction intégrée `len()` :

```go
mySlice := []string{"I", "love", "go"}
fmt.Println(len(mySlice)) // 3
```

#### Capacité

La capacité d'un slice est le nombre d'éléments dans le tableau sous-jacent, en comptant à partir du premier élément du slice. Elle est accessible en utilisant la fonction intégrée `cap()` :

```go
mySlice := []string{"I", "love", "go"}
fmt.Println(cap(mySlice)) // 3
```

En général, sauf si vous optimisez de manière excessive l'utilisation de la mémoire de votre programme, vous n'avez pas besoin de vous soucier de la capacité d'un slice car il grandira automatiquement si nécessaire.

### Fonctions variadiques

De nombreuses fonctions, en particulier celles de la bibliothèque standard, peuvent prendre un nombre arbitraire d'arguments *finaux*. Cela est accompli en utilisant la syntaxe "..." dans la signature de la fonction.

Une fonction variadique reçoit les arguments variadiques sous forme de slice.

```go
func concat(strs ...string) string {
    final := ""
    // strs est juste un slice de chaînes de caractères
    for str := range strs {
        final += str
    }
    return final
}

func main() {
    final := concat("Hello ", "there ", "friend!")
    fmt.Println(total)
    // Sortie : Hello there friend!
}
```

Les fonctions familières [fmt.Println()](https://pkg.go.dev/fmt#Println) et [fmt.Sprintf()](https://pkg.go.dev/fmt#Sprintf) sont variadiques ! `fmt.Println()` imprime chaque élément avec des espaces [délimiteurs](https://www.dictionary.com/browse/delimited) et une nouvelle ligne à la fin.

```go
func Println(a ...interface{}) (n int, err error)
```

#### Opérateur de propagation

L'opérateur de propagation nous permet de passer un slice *dans* une fonction variadique. L'opérateur de propagation se compose de trois points suivant le slice dans l'appel de fonction.

```go
func printStrings(strings ...string) {
	for i := 0; i < len(strings); i++ {
		fmt.Println(strings[i])
	}
}

func main() {
    names := []string{"bob", "sue", "alice"}
    printStrings(names...)
}
```

### Comment ajouter à un Slice

La fonction intégrée append est utilisée pour ajouter dynamiquement des éléments à un slice :

```go
func append(slice []Type, elems ...Type) []Type
```

Si le tableau sous-jacent n'est pas assez grand, `append()` créera un nouveau tableau sous-jacent et pointera le slice vers celui-ci.

Remarquez que `append()` est variadique. Les exemples suivants sont tous valides :

```go
slice = append(slice, oneThing)
slice = append(slice, firstThing, secondThing)
slice = append(slice, anotherSlice...)
```

### Comment parcourir un Slice en Go

Go fournit un sucre syntaxique pour itérer facilement sur les éléments d'un slice :

```go
for INDEX, ELEMENT := range SLICE {
}
```

Par exemple :

```go
fruits := []string{"apple", "banana", "grape"}
for i, fruit := range fruits {
    fmt.Println(i, fruit)
}
// 0 apple
// 1 banana
// 2 grape
```

## Chapitre 10 – Maps en Go

Les Maps sont similaires aux objets JavaScript, aux dictionnaires Python et aux hashes Ruby. Les Maps sont une structure de données qui fournit une correspondance clé->valeur.

La valeur zéro d'une map est `nil`.

Nous pouvons [créer une map](https://blog.boot.dev/golang/golang-make-maps-and-slices/) en utilisant un littéral ou en utilisant la fonction `make()` :

```go
ages := make(map[string]int)
ages["John"] = 37
ages["Mary"] = 24
ages["Mary"] = 21 // écrase 24
```

```go
ages = map[string]int{
  "John": 37,
  "Mary": 21,
}
```

La fonction `len()` fonctionne sur une map – elle retourne le nombre total de paires clé/valeur.

```go
ages = map[string]int{
  "John": 37,
  "Mary": 21,
}
fmt.Println(len(ages)) // 2
```

### Mutations de Map

#### Insérer un élément

```go
m[key] = elem
```

#### Obtenir un élément

```go
elem = m[key]
```

#### Supprimer un élément

```go
delete(m, key)
```

#### Vérifier si une clé existe

```go
elem, ok := m[key]
```

Si `key` est dans `m`, alors `ok` est `true`. Sinon, `ok` est `false`.

Si `key` n'est pas dans la map, alors `elem` est la valeur zéro pour le type d'élément de la map.

### Types de clés de Map valides

N'importe quel type peut être utilisé comme *valeur* dans une map, mais les *clés* sont plus restrictives.

Vous pouvez en lire plus dans la section suivante du [blog officiel de Go](https://go.dev/blog/maps).

Comme mentionné précédemment, **les clés de map peuvent être de n'importe quel type qui est comparable**. La spécification du langage définit cela précisément, mais en bref, les types comparables sont les booléens, numériques, chaînes de caractères, pointeurs, canaux, et types d'interface, et les structs ou tableaux qui contiennent uniquement ces types.

Notamment absents de la liste sont les slices, maps, et fonctions. Ces types ne peuvent pas être comparés en utilisant ==, et ne peuvent pas être utilisés comme clés de map.

Il est évident que les chaînes de caractères, les entiers, et autres types de base devraient être disponibles comme clés de map, mais peut-être inattendus sont les clés de struct. Les structs peuvent être utilisées pour indexer les données par plusieurs dimensions.

Par exemple, cette map de maps pourrait être utilisée pour compter les hits de pages web par pays :

```go
hits := make(map[string]map[string]int)
```

C'est une map de string vers (map de string vers int). Chaque clé de la map externe est le chemin vers une page web avec sa propre map interne. Chaque clé de la map interne est un code de pays à deux lettres. Cette expression récupère le nombre de fois qu'un Australien a chargé la page de documentation :

```go
n := hits["/doc/"]["au"]
```

Malheureusement, cette approche devient encombrante lors de l'ajout de données, car pour toute clé externe donnée, vous devez vérifier si la map interne existe, et la créer si nécessaire :

```go
func add(m map[string]map[string]int, path, country string) {
    mm, ok := m[path]
    if !ok {
        mm = make(map[string]int)
        m[path] = mm
    }
    mm[country]++
}
add(hits, "/doc/", "au")
```

D'autre part, une conception qui utilise une seule map avec une clé de struct élimine toute cette complexité :

```go
type Key struct {
    Path, Country string
}
hits := make(map[Key]int)
```

Lorsque qu'une personne vietnamienne visite la page d'accueil, l'incrémentation (et éventuellement la création) du compteur approprié est une ligne de code :

```go
hits[Key{"/", "vn"}]++
```

Et il est tout aussi simple de voir combien de Suisses ont lu la spécification :

```go
n := hits[Key{"/ref/spec", "ch"}]
```

### Maps imbriquées

Les maps peuvent contenir des maps, créant une structure imbriquée. Par exemple :

```go
map[string]map[string]int
map[rune]map[string]int
map[int]map[string]map[string]int
```

## Chapitre 11 – Fonctions avancées en Go

### Fonctions de première classe et d'ordre supérieur

Un langage de programmation est dit avoir des "fonctions de première classe" lorsque les fonctions dans ce langage sont traitées comme n'importe quelle autre variable.

Par exemple, dans un tel langage, une fonction peut être passée comme argument à d'autres fonctions, peut être retournée par une autre fonction, et peut être assignée comme valeur à une variable.

Une fonction qui retourne une fonction ou accepte une fonction en entrée est appelée une fonction d'ordre supérieur.

Go prend en charge les fonctions de [première classe](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function) et d'ordre supérieur. Une autre façon de penser à cela est qu'une fonction est juste un autre type – tout comme les `int`, les `string` et les `bool`.

Par exemple, pour accepter une fonction comme paramètre :

```go
func add(x, y int) int {
  return x + y
}

func mul(x, y int) int {
  return x * y
}

// aggregate applique la fonction mathématique donnée aux trois premières entrées
func aggregate(a, b, c int, arithmetic func(int, int) int) int {
  return arithmetic(arithmetic(a, b), c)
}

func main(){
  fmt.Println(aggregate(2,3,4, add))
  // imprime 9
  fmt.Println(aggregate(2,3,4, mul))
  // imprime 24
}
```

### Currying de fonctions en Go

Le currying de fonctions est la pratique d'écrire une fonction qui prend une fonction (ou des fonctions) en entrée, et retourne une nouvelle fonction.

Par exemple :

```go
func main() {
  squareFunc := selfMath(multiply)
  doubleFunc := selfMath(add)
  
  fmt.Println(squareFunc(5))
  // imprime 25

  fmt.Println(doubleFunc(5))
  // imprime 10
}

func multiply(x, y int) int {
  return x * y
}

func add(x, y int) int {
  return x + y
}

func selfMath(mathFunc func(int, int) int) func (int) int {
  return func(x int) int {
    return mathFunc(x, x)
  }
}
```

Dans l'exemple ci-dessus, la fonction `selfMath` prend une fonction en tant que paramètre et retourne une fonction qui elle-même retourne la valeur de l'exécution de cette fonction d'entrée sur son paramètre.

### Mot-clé Defer

Le mot-clé `defer` est une fonctionnalité assez unique de Go. Il permet à une fonction d'être exécutée automatiquement *juste avant* que sa fonction englobante ne retourne.

Les arguments de l'appel différé sont évalués immédiatement, mais l'appel de la fonction n'est pas exécuté tant que la fonction environnante ne retourne pas.

Les [fonctions différées](https://blog.boot.dev/golang/defer-golang/) sont généralement utilisées pour fermer les connexions de base de données, les gestionnaires de fichiers et autres.

Par exemple :

```go
// CopyFile copie un fichier de srcName vers dstName sur le système de fichiers local.
func CopyFile(dstName, srcName string) (written int64, err error) {

  // Ouvrir le fichier source
  src, err := os.Open(srcName)
  if err != nil {
    return
  }
  // Fermer le fichier source lorsque la fonction CopyFile retourne
  defer src.Close()

  // Créer le fichier de destination
  dst, err := os.Create(dstName)
  if err != nil {
    return
  }
  // Fermer le fichier de destination lorsque la fonction CopyFile retourne
  defer dst.Close()

  return io.Copy(dst, src)
}
```

Dans l'exemple ci-dessus, la fonction `src.Close()` n'est pas appelée tant que la fonction `CopyFile` n'a pas été appelée mais immédiatement avant que la fonction `CopyFile` ne retourne.

Defer est un excellent moyen de **s'assurer** que quelque chose se passe à la fin d'une fonction, même s'il y a plusieurs instructions de retour.

### Fermetures

Une fermeture est une fonction qui référence des variables en dehors de son propre corps de fonction. La fonction peut accéder et *assigner* aux variables référencées.

Dans cet exemple, la fonction `concatter()` retourne une fonction qui a référence à une valeur *enfermée* `doc`. Chaque appel successif à `harryPotterAggregator` mute cette même variable `doc`.

```go
func concatter() func(string) string {
	doc := ""
	return func(word string) string {
		doc += word + " "
		return doc
	}
}

func main() {
	harryPotterAggregator := concatter()
	harryPotterAggregator("Mr.")
	harryPotterAggregator("and")
	harryPotterAggregator("Mrs.")
	harryPotterAggregator("Dursley")
	harryPotterAggregator("of")
	harryPotterAggregator("number")
	harryPotterAggregator("four,")
	harryPotterAggregator("Privet")

	fmt.Println(harryPotterAggregator("Drive"))
	// Mr. and Mrs. Dursley of number four, Privet Drive
}
```

### Fonctions anonymes

Les fonctions anonymes sont conformes à leur forme en ce sens qu'elles n'ont *pas de nom*. Nous les avons utilisées tout au long de ce chapitre, mais nous n'en avons pas vraiment parlé jusqu'à présent.

Les fonctions anonymes sont utiles lors de la définition d'une fonction qui ne sera utilisée qu'une seule fois ou pour créer une [fermeture](https://en.wikipedia.org/wiki/Closure_\(computer_programming\)) rapide.

```go
// doMath accepte une fonction qui convertit un int en un autre
// et un slice d'ints. Elle retourne un slice d'ints qui ont été
// convertis par la fonction passée en paramètre.
func doMath(f func(int) int, nums []int) []int {
	var results []int
	for _, n := range nums {
		results = append(results, f(n))
	}
	return results
}

func main() {
	nums := []int{1, 2, 3, 4, 5}
	
    // Ici, nous définissons une fonction anonyme qui double un int
    // et la passons à doMath
	allNumsDoubled := doMath(func(x int) int {
	    return x + x
	}, nums)
	
	fmt.Println(allNumsDoubled)
    // imprime:
    // [2 4 6 8 10]
}
```

## Chapitre 12 – Pointeurs en Go

%[https://www.youtube.com/watch?v=MhQw9FNWVMQ]

Comme nous l'avons appris, une variable est un emplacement nommé en mémoire qui stocke une valeur. Nous pouvons manipuler la valeur d'une variable en lui assignant une nouvelle valeur ou en effectuant des opérations sur celle-ci. Lorsque nous assignons une valeur à une variable, nous stockons cette valeur à un emplacement spécifique en mémoire.

```go
x := 42
// "x" est le nom d'un emplacement en mémoire. Cet emplacement stocke la valeur entière 42
```

#### Un pointeur est une variable

Un pointeur est une variable qui stocke l'*adresse mémoire* d'une autre variable. Cela signifie qu'un pointeur "pointe vers" l'*emplacement* où les données sont stockées *ET NON* les données elles-mêmes.

La syntaxe `*` définit un pointeur :

```go
var p *int
```

L'opérateur `&` génère un pointeur vers son opérande.

```go
myString := "hello"
myStringPtr = &myString
```

#### Pourquoi les pointeurs sont-ils utiles ?

Les pointeurs nous permettent de manipuler les données en mémoire directement, sans faire de copies ou dupliquer les données. Cela peut rendre les programmes plus efficaces et nous permettre de faire des choses qui seraient difficiles ou impossibles sans eux.

### Syntaxe des pointeurs

La syntaxe `*` définit un pointeur :

```go
var p *int
```

La valeur zéro d'un pointeur est `nil`

L'opérateur `&` génère un pointeur vers son opérande :

```go
myString := "hello"
myStringPtr = &myString
```

Le `*` déréférence un pointeur pour accéder à la valeur :

```go
fmt.Println(*myStringPtr) // lit myString à travers le pointeur
*myStringPtr = "world"    // définit myString à travers le pointeur
```

Contrairement à C, Go n'a pas d'[arithmétique de pointeurs](https://www.tutorialspoint.com/cprogramming/c_pointer_arithmetic.htm)

#### Juste parce que vous pouvez ne signifie pas que vous devriez

Nous faisons cet exercice pour comprendre que les pointeurs **peuvent** être utilisés de cette manière. Cela dit, les pointeurs peuvent être *très* dangereux. Il est généralement préférable que vos fonctions acceptent des non-pointeurs et retournent de nouvelles valeurs plutôt que de muter les entrées de pointeurs.

### Pointeurs nuls

Encore une fois, les pointeurs peuvent être très dangereux.

Si un pointeur ne pointe vers rien (la valeur zéro du type pointeur), alors le déréférencer provoquera une erreur d'exécution (une [panique](https://gobyexample.com/panic)) qui fera planter le programme.

En général, chaque fois que vous travaillez avec des pointeurs, vous devriez vérifier s'il est `nil` avant d'essayer de le déréférencer.

### Récepteurs de méthode de pointeur

Un type de récepteur sur une méthode peut être un pointeur.

Les méthodes avec des récepteurs de pointeur peuvent modifier la valeur vers laquelle le récepteur pointe. Puisque les méthodes ont souvent besoin de modifier leur récepteur, les récepteurs de pointeur sont *plus courants* que les récepteurs de valeur.

#### Récepteur de pointeur

```go
type car struct {
	color string
}

func (c *car) setColor(color string) {
	c.color = color
}

func main() {
	c := car{
		color: "white",
	}
	c.setColor("blue")
	fmt.Println(c.color)
	// imprime "blue"
}
```

#### Récepteur non pointeur

```go
type car struct {
	color string
}

func (c car) setColor(color string) {
	c.color = color
}

func main() {
	c := car{
		color: "white",
	}
	c.setColor("blue")
	fmt.Println(c.color)
	// imprime "white"
}
```

Les méthodes avec des récepteurs de pointeur n'exigent pas qu'un pointeur soit utilisé pour appeler la méthode. Le pointeur sera automatiquement dérivé de la valeur.

```go
type circle struct {
	x int
	y int
    radius int
}

func (c *circle) grow(){
    c.radius *= 2
}

func main(){
    c := circle{
        x: 1,
        y: 2,
        radius: 4,
    }

    // notez que c n'est pas un pointeur dans la fonction appelante
    // mais la méthode obtient toujours accès à un pointeur vers c
    c.grow()
    fmt.Println(c.radius)
    // imprime 8
}
```

## Chapitre 13 – Environnement de développement local en Go

### Paquets

Assurez-vous d'avoir [Go installé](https://go.dev/doc/install) sur votre machine locale.

Chaque programme Go est composé de paquets.

Vous avez probablement remarqué le `package main` en haut de tous les programmes que vous avez écrits.

Un paquet nommé "main" a un point d'entrée à la fonction `main()`. Un paquet `main` est compilé en un programme exécutable.

Un paquet de n'importe quel autre nom est un "paquet de bibliothèque". Les bibliothèques n'ont pas de point d'entrée. Les bibliothèques exportent simplement des fonctionnalités qui peuvent être utilisées par d'autres paquets. Par exemple :

```go
package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
}
```

Ce programme est un exécutable. C'est un paquet "main" et *importe* depuis les paquets de bibliothèque `fmt` et `math/rand`.

### Noms de paquets

#### Convention de nommage

Par *convention*, le nom d'un paquet est le même que le dernier élément de son chemin d'importation. Par exemple, le paquet `math/rand` comprend des fichiers qui commencent par :

```go
package rand
```

Cela dit, les noms de paquets ne sont *pas obligés* de correspondre à leur chemin d'importation. Par exemple, je pourrais écrire un nouveau paquet avec le chemin `github.com/mailio/rand` et nommer le paquet `random` :

```go
package random
```

Bien que ce qui précède soit possible, cela est déconseillé pour des raisons de cohérence.

#### Un paquet / répertoire

Un répertoire de code Go peut avoir **au plus** un paquet. Tous les fichiers `.go` dans un seul répertoire doivent tous appartenir au même paquet. Sinon, une erreur sera générée par le compilateur. Cela est vrai pour les paquets main et les paquets de bibliothèque.

### Modules Go

Les programmes Go sont organisés en *paquets*. Un paquet est un répertoire de code Go qui est tout compilé ensemble. Les fonctions, types, variables et constantes définis dans un fichier source sont visibles pour **tous les autres fichiers sources au sein du même paquet (répertoire)**.

Un *dépôt* contient un ou plusieurs *modules*. Un module est une collection de paquets Go qui sont publiés ensemble.

#### Un dépôt Go contient généralement un seul module, situé à la racine du dépôt.

Un fichier nommé `go.mod` à la racine d'un projet déclare le module. Il contient :

* Le chemin du module

* La version du langage Go que votre projet nécessite

* Optionnellement, toute dépendance de paquet externe que votre projet a

Le chemin du module est simplement le préfixe du chemin d'importation pour tous les paquets au sein du module. Voici un exemple de fichier `go.mod` :

```python
module github.com/bootdotdev/exampleproject

go 1.20

require github.com/google/examplepackage v1.3.0
```

Le chemin de chaque module sert non seulement de préfixe de chemin d'importation pour les paquets au sein de celui-ci, mais *indique également où la commande go doit chercher pour le télécharger*.

Par exemple, pour télécharger le module `golang.org/x/tools`, la commande go consulterait le dépôt situé à [https://golang.org/x/tools](https://golang.org/x/tools).

> Un "chemin d'importation" est une chaîne utilisée pour importer un paquet. Le chemin d'importation d'un paquet est son chemin de module joint à son sous-répertoire au sein du module. Par exemple, le module `github.com/google/go-cmp` contient un paquet dans le répertoire `cmp/`. Le chemin d'importation de ce paquet est `github.com/google/go-cmp/cmp`. Les paquets de la bibliothèque standard n'ont pas de préfixe de chemin de module. – Paraphrasé de l'[organisation du code](https://golang.org/doc/code#Organization) de Golang.org

#### Dois-je mettre mon paquet sur GitHub ?

Vous n'avez pas besoin de publier votre code dans un dépôt distant avant de pouvoir le construire. Un module peut être défini localement sans appartenir à un dépôt. Mais c'est une bonne habitude de garder une copie de tous vos projets sur un serveur distant, comme GitHub.

### Comment configurer votre machine

Votre machine contiendra de nombreux dépôts de *contrôle de version* (gérés par Git, par exemple).

Chaque dépôt contient un ou plusieurs *paquets*, mais sera typiquement un seul *module*.

Chaque paquet se compose d'un ou plusieurs *fichiers source Go* dans un seul répertoire.

Le chemin vers le répertoire d'un paquet détermine son *chemin d'importation* et d'où il peut être téléchargé si vous décidez de l'héberger sur un système de contrôle de version distant comme Github ou Gitlab.

#### Une note sur GOPATH

La variable d'environnement $GOPATH sera définie par défaut quelque part sur votre machine (généralement dans le répertoire personnel, `~/go`). Puisque nous travaillerons dans la nouvelle configuration "Go modules", vous *n'avez pas besoin de vous en soucier*. Si vous lisez quelque chose en ligne sur la configuration de votre GOPATH, cette documentation est probablement obsolète.

De nos jours, vous devriez éviter de travailler dans le répertoire `$GOPATH/src`. Encore une fois, c'est l'ancienne façon de faire les choses et peut causer des problèmes inattendus, donc mieux vaut simplement l'éviter.

#### Accéder à votre espace de travail

Naviguez vers un emplacement sur votre machine où vous souhaitez stocker du code. Par exemple, je stocke tout mon code dans `~/workspace`, puis je l'organise en sous-dossiers en fonction de l'emplacement distant. Par exemple,

`~/workspace/github.com/wagslane/go-password-validator` = [https://github.com/wagslane/go-password-validator](https://github.com/wagslane/go-password-validator)

Cela dit, vous pouvez mettre votre code où vous voulez.

### Comment écrire votre premier programme Go local

Une fois dans votre espace de travail personnel, créez un nouveau répertoire et entrez-y :

```bash
mkdir hellogo
cd hellogo
```

À l'intérieur du répertoire, déclarez le nom de votre module :

```bash
go mod init {REMOTE}/{USERNAME}/hellogo
```

Où `{REMOTE}` est votre fournisseur de source distant préféré (c'est-à-dire `github.com`) et `{USERNAME}` est votre nom d'utilisateur Git. Si vous n'utilisez pas encore de fournisseur distant, utilisez simplement `example.com/username/hellogo`

Imprimez votre fichier `go.mod` :

```bash
cat go.mod
```

### La commande Go Run

À l'intérieur de `hellogo`, créez un nouveau fichier appelé `main.go`.

Par convention, le fichier dans le package `main` qui contient la fonction `main()` est appelé `main.go`.

Collez le code suivant dans votre fichier :

```go
package main

import "fmt"

func main() {
	fmt.Println("hello world")
}
```

#### Exécuter le code

```bash
go run main.go
```

La commande `go run` est utilisée pour compiler et exécuter rapidement un package Go. Le binaire compilé n'est *pas* enregistré dans votre répertoire de travail. Utilisez `go build` à la place pour compiler des exécutables de production.

Je n'utilise que rarement `go run` sauf pour faire rapidement des tests ou du débogage.

#### Lecture complémentaire

Exécutez `go help run` dans votre shell et lisez les instructions.

### La commande Go Build

`go build` compile le code go en un programme exécutable.

#### Construire un exécutable

Assurez-vous d'être dans votre dépôt hellogo, puis exécutez :

```bash
go build
```

Exécutez le nouveau programme :

```bash
./hellogo
```

### Go Install

#### Construire un exécutable

Assurez-vous d'être dans votre dépôt `hellogo`, puis exécutez :

```bash
go install
```

Naviguez hors de votre répertoire de projet :

```bash
cd ../
```

Go a installé le programme `hellogo` globalement. Exécutez-le avec :

```bash
hellogo
```

#### Astuce concernant "not found"

Si vous obtenez une erreur concernant "hellogo not found", cela signifie que vous n'avez probablement pas configuré correctement votre environnement Go. Plus précisément, `go install` ajoute votre binaire à votre répertoire `GOBIN`, mais celui-ci peut ne pas être dans votre `PATH`.

Vous pouvez en lire plus à ce sujet ici dans la [documentation de go install](https://pkg.go.dev/cmd/go#hdr-Compile_and_install_packages_and_dependencies).

### Comment créer un package Go personnalisé

Écrivons un package à importer et à utiliser dans `hellogo`.

Créez un répertoire frère au même niveau que le répertoire `hellogo` :

```bash
mkdir mystrings
cd mystrings
```

Initialisez un module :

```bash
go mod init {REMOTE}/{USERNAME}/mystrings
```

Ensuite, créez un nouveau fichier `mystrings.go` dans ce répertoire et collez le code suivant :

```go
// par convention, nous nommons notre package de la même manière que le répertoire
package mystrings

// Reverse inverse une chaîne de gauche à droite
// Remarquez que nous devons mettre en majuscule la première lettre de la fonction
// Si nous ne le faisons pas, nous ne pourrons pas accéder à cette fonction en dehors du
// package mystrings
func Reverse(s string) string {
  result := ""
  for _, v := range s {
    result = string(v) + result
  }
  return result
}
```

Notez qu'il n'y a pas de `main.go` ou de `func main()` dans ce package.

`go build` ne construira pas un exécutable à partir d'un package de bibliothèque. Cependant, `go build` compilera toujours le package et le sauvegardera dans notre cache de construction local. Il est utile pour vérifier les erreurs de compilation.

Exécutez :

```bash
go build
```

### Comment publier des packages distants en Go

Apprenons à utiliser un package open-source disponible en ligne.

#### Une note sur la manière de publier des modules

Soyez conscient que l'utilisation du mot-clé "replace" comme nous l'avons fait dans la dernière tâche *n'est pas conseillée*, mais peut être utile pour démarrer rapidement. La bonne manière de créer et de dépendre des modules est de les publier dans un dépôt distant. Lorsque vous faites cela, le mot-clé "replace" peut être supprimé du `go.mod` :

#### Mauvais

Cela fonctionne pour le développement local uniquement

```go
module github.com/wagslane/hellogo

go 1.20

replace github.com/wagslane/mystrings v0.0.0 => ../mystrings

require (
	github.com/wagslane/mystrings v0.0.0
)
```

#### Bon

Cela fonctionne si nous publions nos modules dans un emplacement distant comme Github comme nous le devrions.

```go
module github.com/wagslane/hellogo

go 1.20

require (
	github.com/wagslane/mystrings v0.0.0
)
```

### Bonnes pratiques avec les packages Go

J'ai souvent vu, et j'ai été responsable de, jeter du code dans des packages sans trop réfléchir. J'ai rapidement tracé une ligne dans le sable et j'ai commencé à mettre du code dans différents dossiers (qui en Go sont différents packages par définition) juste pour la facilité de recherche.

Apprendre à construire correctement des packages petits et réutilisables peut faire passer votre carrière Go au niveau supérieur.

#### 1. Masquer la logique interne

Si vous êtes familier avec les piliers de la POO, c'est une pratique d'*encapsulation*.

Souvent, une application aura une logique complexe qui nécessite beaucoup de code. Dans presque tous les cas, la logique dont l'application se soucie peut être exposée via une API, et la plupart du travail sale peut être gardé au sein d'un package.

Par exemple, imaginez que nous construisons une application qui doit classifier des images. Nous pourrions construire un package :

```go
package classifier

// ClassifyImage classe les images comme "hotdog" ou "not hotdog"
func ClassifyImage(image []byte) (imageType string) {
	return hasHotdogColors(image) && hasHotdogShape(image)
}

func hasHotdogShape(image []byte) bool {
	// logique interne dont l'application n'a pas besoin de connaître
	return true
}

func hasHotdogColors(image []byte) bool {
	// logique interne dont l'application n'a pas besoin de connaître
	return true
}
```

Nous créons une API en exposant uniquement la ou les fonctions dont l'application a besoin de connaître. Toute autre logique est non exportée pour maintenir une séparation claire des préoccupations. L'application n'a pas besoin de savoir comment classifier une image, juste le résultat de la classification.

#### 2. Ne changez pas les API

Les fonctions non exportées au sein d'un package peuvent et doivent changer souvent pour les tests, le refactoring et la correction de bugs.

Une bibliothèque bien conçue aura une API stable afin que les utilisateurs ne reçoivent pas de changements cassants à chaque mise à jour de la version du package. En Go, cela signifie ne pas changer les signatures des fonctions exportées.

#### 3. N'exportez pas de fonctions depuis le package main

Un package `main` n'est pas une bibliothèque, il n'y a pas besoin d'exporter des fonctions depuis celui-ci.

#### 4. Les packages ne devraient pas connaître leurs dépendants

Peut-être l'une des règles les plus importantes et les plus enfreintes est qu'un package ne devrait rien savoir de ses dépendants. En d'autres termes, un package ne devrait jamais avoir de connaissance spécifique sur une application particulière qui l'utilise.

#### Lecture complémentaire

Vous pouvez optionnellement [lire plus ici](https://blog.boot.dev/golang/how-to-separate-library-packages-in-go/) si vous êtes intéressé.

## Chapitre 14 – Canaux en Go

### Concurrence

%[https://www.youtube.com/watch?v=snK5wn00Lhw]

La concurrence est la capacité à effectuer plusieurs tâches en même temps. Typiquement, notre code est exécuté ligne par ligne, l'une après l'autre. Cela s'appelle l'exécution *séquentielle* ou l'exécution *synchrone*.

![concurrency](https://i.imgur.com/1pQKFgw.png align="left")

Si l'ordinateur sur lequel nous exécutons notre code dispose de plusieurs cœurs, nous pouvons même exécuter plusieurs tâches *exactement* en même temps. Si nous exécutons sur un seul cœur, un seul code exécute du code *presque* en même temps en basculant entre les tâches très rapidement. Dans les deux cas, le code que nous écrivons a la même apparence en Go et tire parti des ressources disponibles.

#### Comment fonctionne la concurrence en Go ?

Go a été conçu pour être concurrent, ce qui est un trait *assez* unique à Go. Il excelle dans l'exécution de nombreuses tâches simultanément et en toute sécurité en utilisant une syntaxe simple.

Il n'existe pas de langage de programmation populaire où le lancement d'une exécution concurrente est aussi élégant, du moins à mon avis.

La concurrence est aussi simple que d'utiliser le mot-clé `go` lors de l'appel d'une fonction :

```go
go doSomething()
```

Dans l'exemple ci-dessus, `doSomething()` sera exécuté de manière concurrente avec le reste du code dans la fonction. Le mot-clé `go` est utilisé pour lancer une nouvelle [goroutine](https://gobyexample.com/goroutines).

### Canaux en Go

Les canaux sont une file d'attente typée et thread-safe. Les canaux permettent à différentes goroutines de communiquer entre elles.

#### Créer un canal

Comme les maps et les slices, les canaux doivent être créés *avant* utilisation. Ils utilisent également le même mot-clé `make` :

```go
ch := make(chan int)
```

#### Envoyer des données à un canal

```go
ch <- 69
```

L'opérateur `<-` est appelé l'*opérateur de canal*. Les données circulent dans la direction de la flèche. Cette opération va *bloquer* jusqu'à ce qu'une autre goroutine soit prête à recevoir la valeur.

#### Recevoir des données d'un canal

```go
v := <-ch
```

Cela lit et supprime une valeur du canal et la sauvegarde dans la variable `v`. Cette opération va *bloquer* jusqu'à ce qu'il y ait une valeur dans le canal à lire.

#### Blocage et interblocages

Un [interblocage](https://yourbasic.org/golang/detect-deadlock/#:~:text=yourbasic.org%2Fgolang,look%20at%20this%20simple%20example.) est lorsque qu'un groupe de goroutines sont toutes bloquées de sorte qu'aucune d'entre elles ne peut continuer. C'est un bug courant auquel vous devez faire attention dans la programmation concurrente.

### Jetons

Les structs vides sont souvent utilisées comme `jetons` dans les programmes Go. Dans ce contexte, un jeton est une valeur [unaire](https://en.wikipedia.org/wiki/Unary_operation). En d'autres termes, nous ne nous soucions pas *de ce qui* est passé à travers le canal. Nous nous soucions *quand* et *si* il est passé.

Nous pouvons bloquer et attendre jusqu'à ce que *quelque chose* soit envoyé sur un canal en utilisant la syntaxe suivante

```go
<-ch
```

Cela bloquera jusqu'à ce qu'il retire un seul élément du canal, puis continuera, en rejetant l'élément.

### Canaux tamponnés

Les canaux peuvent éventuellement être tamponnés.

#### Comment créer un canal avec un tampon

Vous pouvez fournir une longueur de tampon comme deuxième argument à `make()` pour créer un canal tamponné :

```go
ch := make(chan int, 100)
```

L'envoi sur un canal tamponné ne bloque que lorsque le tampon est *plein*.

La réception bloque uniquement lorsque le tampon est *vide*.

### Comment fermer les canaux

Les canaux peuvent être explicitement fermés par un *expéditeur* :

```go
ch := make(chan int)

// faire quelques choses avec le canal

close(ch)
```

#### Comment vérifier si un canal est fermé

De manière similaire à la valeur `ok` lors de l'accès aux données dans une `map`, les récepteurs peuvent vérifier la valeur `ok` lors de la réception d'un canal pour tester si un canal a été fermé.

```go
v, ok := <-ch
```

ok est `false` si le canal est vide et fermé.

#### Ne pas envoyer sur un canal fermé

Envoyer sur un canal fermé provoquera une panique. Une panique sur la goroutine principale provoquera le plantage de l'ensemble du programme, et une panique dans toute autre goroutine provoquera le plantage de *cette goroutine*.

La fermeture n'est pas nécessaire. Il n'y a rien de mal à laisser les canaux ouverts, ils seront toujours collectés par le garbage collector s'ils ne sont pas utilisés. Vous devriez fermer les canaux pour indiquer explicitement à un récepteur que rien d'autre ne va venir.

### Parcourir un canal

De manière similaire aux slices et aux maps, les canaux peuvent être parcourus.

```go
for item := range ch {
    // item est la prochaine valeur reçue du canal
}
```

Cet exemple recevra des valeurs sur le canal (en bloquant à chaque itération s'il n'y a rien de nouveau) et ne sortira que lorsque le canal sera fermé.

### Sélectionner à partir d'un canal

Parfois, nous avons une seule goroutine écoutant plusieurs canaux et voulons traiter les données dans l'ordre où elles arrivent à travers chaque canal.

Une instruction `select` est utilisée pour écouter plusieurs canaux en même temps. Elle est similaire à une instruction `switch` mais pour les canaux.

```go
select {
  case i, ok := <- chInts:
    fmt.Println(i)
  case s, ok := <- chStrings:
    fmt.Println(s)
}
```

Le premier canal avec une valeur prête à être reçue se déclenchera et son corps s'exécutera. Si plusieurs canaux sont prêts en même temps, l'un est choisi aléatoirement. La variable `ok` dans l'exemple ci-dessus fait référence au fait que le canal a été fermé ou non par l'expéditeur.

### Sélection par défaut

Le cas `default` dans une instruction `select` s'exécute *immédiatement* si aucun autre canal n'a de valeur prête. Un cas `default` empêche l'instruction `select` de bloquer.

```go
select {
  case v := <-ch:
    // utiliser v
  default:
    // recevoir de ch bloquerait
    // donc faire autre chose
}
```

## Chapitre 15 – Mutexes en Go

Les [Mutexes](https://blog.boot.dev/golang/golang-mutex/) nous permettent de *verrouiller* l'accès aux données. Cela garantit que nous pouvons contrôler quelles goroutines peuvent accéder à certaines données à quel moment.

La bibliothèque standard de Go fournit une implémentation intégrée d'un mutex avec le type [sync.Mutex](https://pkg.go.dev/sync#Mutex) et ses deux méthodes :

* [.Lock()](https://golang.org/pkg/sync/#Mutex.Lock)

* [.Unlock()](https://golang.org/pkg/sync/#Mutex.Unlock)

Nous pouvons protéger un bloc de code en l'entourant d'un appel à `Lock` et `Unlock` comme montré dans la méthode `protected()` ci-dessous.

Il est bon de structurer le code protégé au sein d'une fonction afin que `defer` puisse être utilisé pour s'assurer que nous n'oublions jamais de déverrouiller le mutex.

```go
func protected(){
    mux.Lock()
    defer mux.Unlock()
    // le reste de la fonction est protégé
    // tout autre appel à `mux.Lock()` sera bloqué
}
```

Les Mutexes sont puissants. Comme la plupart des choses puissantes, ils peuvent aussi causer de nombreux bugs s'ils sont utilisés sans précaution.

#### Les Maps ne sont pas thread-safe

Les Maps ne sont **pas** sûres pour une utilisation concurrente ! Si vous avez plusieurs goroutines accédant à la même map, et qu'au moins l'une d'entre elles écrit dans la map, vous devez verrouiller vos maps avec un mutex.

### Pourquoi s'appelle-t-il un Mutex ?

Mutex est l'abréviation de [exclusion mutuelle](https://en.wikipedia.org/wiki/Mutual_exclusion), et le nom conventionnel pour la structure de données qui la fournit est "mutex", souvent abrégé en "mux".

Il est appelé "exclusion mutuelle" parce qu'un mutex *exclut* différents threads (ou goroutines) d'accéder aux mêmes données en même temps.

### Pourquoi utiliser des mutexes ?

Le problème principal que les mutexes nous aident à éviter est le *problème de lecture/écriture concurrente*. Ce problème survient lorsqu'un thread écrit dans une variable tandis qu'un autre thread lit cette même variable *en même temps*.

Lorsque cela se produit, un programme Go paniquera car le lecteur pourrait lire de mauvaises données pendant qu'elles sont mutées en place.

![mutex](https://i.imgur.com/NGBnMXe.png align="left")

### Exemple de Mutex

```go
package main

import (
	"fmt"
)

func main() {
	m := map[int]int{}
	go writeLoop(m)
	go readLoop(m)

	// empêcher le programme de se terminer, doit être tué
	block := make(chan struct{})
	<-block
}

func writeLoop(m map[int]int) {
	for {
		for i := 0; i < 100; i++ {
			m[i] = i
		}
	}
}

func readLoop(m map[int]int) {
	for {
		for k, v := range m {
			fmt.Println(k, "-", v)
		}
	}
}
```

L'exemple ci-dessus crée une map, puis démarre deux goroutines qui ont chacune accès à la map. Une goroutine modifie en continu les valeurs stockées dans la map, tandis que l'autre imprime les valeurs qu'elle trouve dans la map.

Si nous exécutons le programme sur une machine multi-cœur, nous obtenons le message d'erreur suivant : `fatal error: concurrent map iteration and map write`

En Go, il n'est pas sûr de lire et d'écrire dans une map en même temps.

### Les Mutexes à la rescousse

```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	m := map[int]int{}

	mux := &sync.Mutex{}

	go writeLoop(m, mux)
	go readLoop(m, mux)

	// empêcher le programme de se terminer, doit être tué
	block := make(chan struct{})
	<-block
}

func writeLoop(m map[int]int, mux *sync.Mutex) {
	for {
		for i := 0; i < 100; i++ {
			mux.Lock()
			m[i] = i
			mux.Unlock()
		}
	}
}

func readLoop(m map[int]int, mux *sync.Mutex) {
	for {
		mux.Lock()
		for k, v := range m {
			fmt.Println(k, "-", v)
		}
		mux.Unlock()
	}
}
```

Dans cet exemple, nous avons ajouté un `sync.Mutex{}` et l'avons nommé `mux`. Dans la boucle d'écriture, la méthode `Lock()` est appelée avant l'écriture, puis la méthode `Unlock()` est appelée lorsque nous avons terminé. Cette séquence Lock/Unlock garantit qu'aucun autre thread ne peut `Lock()` le mutex pendant que *nous* l'avons verrouillé – tout autre thread tentant de `Lock()` sera bloqué et attendra jusqu'à ce que nous `Unlock()`.

Dans le lecteur, nous `Lock()` avant d'itérer sur la map, et de même `Unlock()` lorsque nous avons terminé. Maintenant, les threads partagent la mémoire en toute sécurité !

### RWMutex

La bibliothèque standard expose également un [sync.RWMutex](https://golang.org/pkg/sync/#RWMutex)

En plus de ces méthodes :

* [Lock()](https://golang.org/pkg/sync/#Mutex.Lock)

* [Unlock()](https://golang.org/pkg/sync/#Mutex.Unlock)

Le `sync.RWMutex` a également ces méthodes :

* [RLock()](https://golang.org/pkg/sync/#RWMutex.RLock)

* [RUnlock()](https://golang.org/pkg/sync/#RWMutex.RUnlock)

Le `sync.RWMutex` peut aider avec les performances si nous avons un processus intensif en lecture. De nombreuses goroutines peuvent lire en toute sécurité depuis la map en même temps (plusieurs appels `Rlock()` peuvent se produire simultanément). Cependant, une seule goroutine peut détenir un `Lock()` et tous les `RLock()` seront également exclus.

## Chapitre 16 – Génériques en Go

Comme nous l'avons mentionné, Go ne *supporte* pas les classes. Pendant longtemps, cela signifiait que le code Go ne pouvait pas être facilement réutilisé dans de nombreuses circonstances.

Par exemple, imaginez un code qui divise un slice en 2 parties égales. Le code qui divise le slice ne se soucie pas vraiment des *valeurs* stockées dans le slice. Malheureusement en Go, nous devrions l'écrire plusieurs fois pour chaque type, ce qui est très peu [DRY](https://blog.boot.dev/clean-code/dry-code/).

```go
func splitIntSlice(s []int) ([]int, []int) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
```

```go
func splitStringSlice(s []string) ([]string, []string) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
```

Dans Go 1.20 cependant, le support des [génériques](https://blog.boot.dev/golang/how-to-use-golangs-generics/) a été publié, résolvant efficacement ce problème !

#### Paramètres de type

En termes simples, les génériques nous permettent d'utiliser des variables pour faire référence à des types spécifiques. C'est une fonctionnalité incroyable car elle nous permet d'écrire des fonctions abstraites qui réduisent considérablement la duplication de code.

```go
func splitAnySlice[T any](s []T) ([]T, []T) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
```

Dans l'exemple ci-dessus, `T` est le nom du paramètre de type pour la fonction `splitAnySlice`, et nous avons dit qu'il doit correspondre à la contrainte `any`, ce qui signifie qu'il peut être n'importe quoi. Cela a du sens car le corps de la fonction *ne se soucie pas* des types de choses stockées dans le slice.

```go
firstInts, secondInts := splitAnySlice([]int{0, 1, 2, 3})
fmt.Println(firstInts, secondInts)
```

### Pourquoi les génériques ?

#### Les génériques réduisent le code répétitif

Vous devriez vous soucier des génériques car ils signifient que vous n'avez pas à écrire autant de code ! Il peut être frustrant d'écrire la même logique encore et encore, juste parce que vous avez des types de données sous-jacents légèrement différents.

#### Les génériques sont utilisés plus souvent dans les bibliothèques et les packages

Les génériques donnent aux développeurs Go un moyen élégant d'écrire des packages utilitaires incroyables. Bien que vous verrez et utiliserez des génériques dans le code d'application, je pense qu'il sera beaucoup plus courant de voir des génériques utilisés dans les bibliothèques et les packages. Les bibliothèques et les packages contiennent du code importable destiné à être utilisé dans *de nombreuses* applications, il est donc logique de les écrire de manière plus abstraite. Les génériques sont souvent le moyen de le faire !

#### Pourquoi a-t-il fallu si longtemps pour obtenir des génériques ?

Go met l'accent sur la simplicité. En d'autres termes, Go a délibérément laissé de côté de nombreuses fonctionnalités pour fournir sa meilleure fonctionnalité : être simple et facile à utiliser.

Selon les [données historiques des enquêtes Go](https://go.dev/blog/survey2020-results), le manque de génériques dans Go a toujours été classé comme l'un des trois plus grands problèmes du langage. À un certain point, les inconvénients associés au manque d'une fonctionnalité comme les génériques justifient l'ajout de complexité au langage.

### Contraintes en Go

Parfois, vous avez besoin que la logique dans votre fonction générique sache *quelque chose* sur les types sur lesquels elle opère. L'exemple que nous avons utilisé dans le premier exercice n'avait pas besoin de savoir *quoi que ce soit* sur les types dans le slice, donc nous avons utilisé la contrainte intégrée `any` :

```go
func splitAnySlice[T any](s []T) ([]T, []T) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
```

Les contraintes sont simplement des interfaces qui nous permettent d'écrire des génériques qui n'opèrent que dans la contrainte d'un type d'interface donné. Dans l'exemple ci-dessus, la contrainte `any` est la même que l'interface vide car elle signifie que le type en question peut être *n'importe quoi*.

#### Comment créer une contrainte personnalisée

Prenons l'exemple d'une fonction `concat`. Elle prend un slice de valeurs et concatène les valeurs en une chaîne de caractères. Cela devrait fonctionner avec *n'importe quel type qui peut se représenter comme une chaîne de caractères*, même si ce n'est pas une chaîne de caractères sous le capot.

Par exemple, une struct `user` peut avoir une méthode `.String()` qui retourne une chaîne de caractères avec le nom et l'âge de l'utilisateur.

```go
type stringer interface {
    String() string
}

func concat[T stringer](vals []T) string {
    result := ""
    for _, val := range vals {
        // c'est ici que la méthode .String()
        // est utilisée. C'est pourquoi nous avons besoin d'une contrainte plus spécifique
        // au lieu de la contrainte any
        result += val.String()
    }
    return result
}
```

### Liste de types d'interface

Lorsque les génériques ont été publiés, une nouvelle façon d'écrire des interfaces a également été publiée en même temps !

Nous pouvons maintenant simplement lister un ensemble de types pour obtenir une nouvelle interface/contrainte.

```go
// Ordered est une contrainte de type qui correspond à tout type ordonné.
// Un type ordonné est celui qui supporte les opérateurs <, <=, >, et >=.
type Ordered interface {
    ~int | ~int8 | ~int16 | ~int32 | ~int64 |
        ~uint | ~uint8 | ~uint16 | ~uint32 | ~uint64 | ~uintptr |
        ~float32 | ~float64 |
        ~string
}
```

### Comment nommer les types génériques

Regardons à nouveau cet exemple simple :

```go
func splitAnySlice[T any](s []T) ([]T, []T) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
```

Rappelez-vous, `T` est juste un nom de variable. Nous aurions pu nommer le paramètre de type *n'importe quoi*. `T` se trouve être une convention assez courante pour une variable de type, similaire à la façon dont `i` est une convention pour les variables d'index dans les boucles.

Ceci est tout aussi valide :

```go
func splitAnySlice[MyAnyType any](s []MyAnyType) ([]MyAnyType, []MyAnyType) {
    mid := len(s)/2
    return s[:mid], s[mid:]
}
```

## **Félicitations pour être arrivé à la fin !**

Si vous êtes intéressé par les exercices de codage interactifs et les quiz de ce cours, vous pouvez consulter le [cours Learn Go](https://boot.dev/learn/learn-golang) sur [Boot.dev](https://boot.dev/).

Ce cours fait partie de mon [parcours complet de carrière de développeur backend](https://boot.dev/tracks/backend), composé d'autres cours et projets si vous êtes intéressé à les consulter.

Si vous voulez voir les autres contenus que je crée liés au développement web, consultez certains de mes liens ci-dessous :

* [Podcast de Lane : Backend Banter](https://backendbanter.fm/)

* [Lane sur Twitter](https://twitter.com/wagslane)

* [Lane sur YouTube](https://youtube.com/@bootdotdev)