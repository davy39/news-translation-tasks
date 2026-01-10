---
title: Concepts clés de Golang à apprendre en tant que développeur Go débutant
date: '2024-11-12T20:06:42.584Z'
author: Temitope Oyedele
authorURL: https://www.freecodecamp.org/news/author/Koded001/
originalURL: https://freecodecamp.org/news/key-golang-concepts-for-beginner-go-devs
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731435098075/7fee649f-911d-4537-a613-1fa12824a011.png
tags:
- name: golang
  slug: golang
- name: Beginner Developers
  slug: beginners
- name: Web Development
  slug: web-development
- name: backend
  slug: backend
seo_desc: 'Learning new programming concepts can be hard. So you''ll need a guide
  or a roadmap to help you navigate through the process.

  Learning Golang is no exception. And as a beginner, you''ll need to work diligently
  to learn the fundamental building blocks o...'
---


Apprendre de nouveaux concepts de programmation peut être difficile. Vous aurez donc besoin d'un guide ou d'une feuille de route pour vous aider à naviguer dans ce processus.

<!-- more -->

L'apprentissage de Golang ne fait pas exception. En tant que débutant, vous devrez travailler avec diligence pour apprendre les blocs de construction fondamentaux du langage. Ces concepts introductifs clés sont importants car ils vous aident à poser les bases d'un développement plus complexe.

Dans cet article, nous explorerons les principales parties de Go que chaque débutant devrait apprendre pour acquérir une base solide dans le langage. Si vous venez de commencer, ce guide vous aidera à consolider vos connaissances et à commencer à construire des projets qui vous rendront plus confiant pour coder en Golang.

## Table des matières

-   [Variables et types de données][1]
    
-   [Structures de contrôle][2]
    
    -   [1\. Instructions If/Else][3]
        
    -   [2\. Instructions Switch][4]
        
    -   [3\. Boucles For][5]
        
-   [Fonctions][6]
    
-   [Pointeurs][7]
    
-   [Gestion des erreurs][8]
    
-   [Goroutines et concurrence][9]
    
-   [Structs et héritage][10]
    
-   [Bibliothèque standard de Go][11]
    
    -   [Accéder à et utiliser un package de la bibliothèque standard][12]
-   [Tests en Go][13]
    
-   [Conclusion !][14]
    

## Variables et types de données

Les variables en Go sont utilisées pour stocker et gérer des données au sein d'un programme. Elles agissent comme des conteneurs qui détiennent des valeurs de types spécifiques. Les variables vous permettent de récupérer et de manipuler les informations stockées.

Voici un exemple d'utilisation de variables en Go :

```
package main

import "fmt"

func main(){
 // Variables
    var age int = 30
    var name string = "John"
    salary := 50000.50 // Short variable declaration(only to be used inside a function
  fmt.Println(age)
  fmt.Println(name)
   fmt.Println(salary)
}
```

Pour en savoir plus sur les variables, vous pouvez consulter [mon tutoriel à leur sujet ici][15].

D'un autre côté, les types de données définissent le genre de données qu'une variable peut contenir. Comme Go est un langage statiquement typé, il vous oblige à spécifier le type de données de chaque variable.

Certains des principaux types de données en Go incluent :

-   **Boolean** : Représente une valeur vraie ou fausse. Il est utilisé pour les décisions logiques dans le programme.
    
-   **Number** : Comprend les types entiers (comme `int`, `int32`, `int64`) et les types à virgule flottante (comme `float32`, `float64`) pour stocker des nombres entiers et des valeurs décimales.
    
-   **String** : Représente une séquence de caractères (texte). Il est utilisé pour stocker des mots, des phrases ou toute donnée textuelle.
    
-   **Array** : Une collection d'éléments de taille fixe du même type. Les tableaux vous permettent de stocker plusieurs valeurs dans une seule variable.
    
-   **Slice** : Semblable aux tableaux, mais avec une taille dynamique. Les slices sont plus couramment utilisés en Go car ils offrent une plus grande flexibilité.
    
-   **Map** : Une collection de paires clé-valeur. Les maps sont utilisées lorsque vous souhaitez associer des valeurs à des clés spécifiques pour une recherche rapide.
    
-   **Struct** : Un moyen de regrouper des données liées ensemble. Les structs vous permettent de définir des types de données personnalisés avec plusieurs champs, chacun d'un type différent.
    
-   **Pointer** : Détient l'adresse mémoire d'une autre variable, permettant une manipulation de la mémoire plus efficace dans certains cas.
    

Voici un exemple montrant comment certains de ces types de données fonctionnent :

```
package main

import "fmt"

func main() {

    // Data Types
    var isEmployed bool = true // boolean
    var count int = 42 // integer
    var greeting string = "Hello, Go!" // string

    // Struct
    type Rectangle struct {
        width  float64
        height float64
    }
    rect := Rectangle{width: 10.5, height: 5.2}

    fmt.Println("Is Employed:", isEmployed)
    fmt.Println("Count:", count)
    fmt.Println("Greeting:", greeting)
    fmt.Println("Numbers:", numbers)
    fmt.Printf("Rectangle: width = %.2f, height = %.2f\n", rect.width, rect.height)

}
```

Dans cet exemple, nous démontrons l'utilisation de plusieurs types de données :

1.  `bool` : La variable `isEmployed` est déclarée comme un `bool` et se voit assigner la valeur `true`.
    
2.  `int` : La variable `count` est déclarée comme un `int` et se voit assigner la valeur `42`.
    
3.  `string` : La variable `greeting` est déclarée comme une `string` et se voit assigner la valeur `"Hello, Go!"`.
    
4.  `struct` : Nous définissons un nouveau type de données appelé `Rectangle` qui possède deux champs : `width` et `height`, tous deux de type `float64`. Nous créons ensuite une nouvelle instance de `Rectangle` et assignons des valeurs à ses champs.
    

Les variables et les types de données forment la base de la programmation en Go. Ces concepts sont des blocs de construction essentiels que vous utiliserez dans presque tous les programmes que vous écrirez. Ils vous permettent de stocker, manipuler et organiser les données efficacement.

Avec une solide maîtrise des variables et des types de données, vous serez également mieux équipé pour aborder des concepts Go plus avancés et écrire un code robuste et efficace au fur et à mesure de votre progression.

## Structures de contrôle

En Go, les structures de contrôle sont simplement des constructions qui contrôlent le flux d'exécution dans un programme. Elles vous permettent d'effectuer différentes actions en fonction de conditions ou d'exécuter de manière répétée un bloc de code.

Certaines des principales structures de contrôle en Go incluent :

### 1\. Instructions If/Else

L'[instruction if/else][16] en Go exécute un bloc de code basé sur une condition. Si la condition renvoie vrai, le code à l'intérieur du bloc `if` est exécuté. Si la condition renvoie faux, le bloc `else` (le cas échéant) est exécuté.

Par exemple :

```
package main

import "fmt"

func main() {
    x := 10
    if x > 5 {
        fmt.Println("x is greater than 5")
    } else {
        fmt.Println("x is 5 or less")
    }
}
```

Dans le code ci-dessus, si x est supérieur à 5, le premier bloc est exécuté. Sinon, le bloc `else` s'exécute.

### 2\. Instructions Switch

L'[instruction switch][17] est une branche multidirectionnelle qui vous permet d'exécuter différents blocs de code en fonction de la valeur d'une expression. Elle est plus facile à lire que de multiples instructions if/else.

Par exemple :

```
package main

import "fmt"

func main() {
    day := "Monday"
    switch day {
    case "Monday":
        fmt.Println("Start of the week")
    case "Friday":
        fmt.Println("Almost weekend")
    default:
        fmt.Println("It's another day")
    }
}
```

Dans le code ci-dessus, la sortie sera "Start of the week" car la variable `day` correspond au cas `Monday`.

### 3\. Boucles For

Go n'a qu'une seule construction de boucle, la [boucle for][18]. Elle peut être utilisée sous diverses formes : boucles traditionnelles, boucles basées sur une plage (pour itérer sur des slices, des maps, etc.) et boucles infinies.

Voici un exemple de boucle traditionnelle :

```
package main

import "fmt"

func main() {
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }
}
```

Dans le code ci-dessus, la boucle affiche les nombres de 0 à 4.

La boucle basée sur une plage (`range`) offre un moyen simplifié d'itérer sur les slices, les maps et autres. Elle facilite l'accès direct à chaque élément sans avoir besoin de gérer manuellement l'index ou les vérifications de longueur. La boucle fournit automatiquement l'index et la valeur lors de chaque itération, améliorant la lisibilité et réduisant les risques d'erreurs d'indexation.

Voici un exemple de boucle basée sur une plage :

```
package main

import "fmt"

func main() {
    nums := []int{1, 2, 3, 4}
    for i, num := range nums {
        fmt.Println(i, num)
    }
}
```

Dans le code ci-dessus, la boucle `for` est utilisée pour itérer sur la slice `nums`. Le mot-clé `range` renvoie à la fois l'index et la valeur de chaque élément de la slice. Cela facilite le traitement de tous les éléments d'une slice sans avoir besoin d'une variable de compteur.

## Fonctions

Une [fonction][19] en Go est un bloc de code qui effectue une tâche spécifique. Les fonctions vous aident à organiser le code en vous permettant de construire une logique de code réutilisable, plus facile à maintenir et à comprendre.

Voici un exemple de fonction qui additionne deux nombres :

```
package main

import "fmt"

func add(a int, b int) int {
    return a + b
}

func main() {
    result := add(2, 3)
    fmt.Println("Result:", result)
}
```

Ici, nous avons une fonction simple appelée `add` qui prend deux paramètres entiers (`a` et `b`) et renvoie leur somme, qui est également de type entier. La fonction est ensuite appelée à l'intérieur de la fonction `main` qui affiche le résultat.

Les fonctions sont le fondement des programmes Go, et comprendre leur structure et leurs capacités est essentiel.

## Pointeurs

En Go, un [pointeur][20] est une variable qui stocke l'adresse mémoire d'une autre variable. Un pointeur « pointe » vers la région de la mémoire où la valeur réelle est stockée plutôt que de conserver la valeur elle-même.

Les pointeurs sont utiles lorsque vous devez passer des références à de grandes structures ou lorsque vous souhaitez modifier la valeur d'une variable depuis l'intérieur d'une fonction. Ils sont également essentiels pour la gestion de la mémoire.

Voici un exemple simple qui illustre le fonctionnement des pointeurs en Go :

```
package main

import "fmt"

func main() {
    var num int = 10

    var ptr *int = &num

    fmt.Println("Value of num:", num)      
    fmt.Println("Pointer address:", ptr)   
    fmt.Println("Value at pointer:", *ptr)

    *ptr = 20
    fmt.Println("Updated value of num:", num) 
}
```

Dans l'exemple ci-dessus, nous déclarons d'abord une variable `num` et lui assignons la valeur 10. Nous créons ensuite un pointeur `ptr` qui stocke l'adresse mémoire de `num` (en utilisant `&num`) puis nous l'affichons. Pour accéder à la valeur stockée à l'adresse du pointeur, nous utilisons `*ptr`. Nous modifions ensuite la valeur de `num` via le pointeur en définissant `*ptr` à 20, ce qui change directement `num` en 20.

Cela démontre comment les pointeurs vous permettent d'accéder et de modifier des variables via leurs adresses mémoire, ce qui est utile pour une gestion plus efficace de la mémoire et le passage de paramètres de fonction en Go.

Pour mieux comprendre ce que sont les pointeurs, vous pouvez [consulter mon article à leur sujet ici][21].

## Gestion des erreurs

Afin d'écrire des applications robustes et fiables, vous devrez apprendre la [gestion des erreurs][22]. Comparé à d'autres langages de programmation, Go adopte une approche unique, vous encourageant à gérer les problèmes de manière explicite et immédiate plutôt que de compter sur des exceptions.

En Go, les erreurs sont traitées comme des valeurs, ce qui signifie qu'elles sont renvoyées par les fonctions comme n'importe quelle autre valeur et doivent être gérées par le développeur. Cette approche favorise la clarté et garantit également que les problèmes potentiels sont traités au point où ils surviennent.

Voici un exemple de code pour illustrer la gestion de base des erreurs en Go :

```
package main

import (
    "errors"
    "fmt"
)

func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("cannot divide by zero")
    }
    return a / b, nil
}

func main() {
    result, err := divide(10, 0)
    if err != nil {
        fmt.Println("Error:", err)
    } else {
        fmt.Println("Result:", result)
    }
}
```

Dans le code ci-dessus, nous avons une fonction `divide` qui prend deux nombres et renvoie à la fois un résultat et une erreur. Si le deuxième nombre est zéro, une erreur est renvoyée car la division par zéro n'est pas autorisée.

Nous avons également une fonction `main` où nous appelons `divide` et vérifions si une erreur s'est produite en examinant la valeur `err`. Si une erreur est présente, nous la gérons en affichant un message d'erreur. Sinon, nous affichons le résultat.

Cette approche de la gestion des erreurs en Go garantit que les erreurs sont capturées et traitées immédiatement, ce qui rend le programme plus fiable et plus facile à dépanner.

## Goroutines et concurrence

Les [Goroutines][23] et la concurrence sont des concepts qui permettent à votre code d'exécuter efficacement plusieurs tâches en parallèle.

Une goroutine est une fonction qui s'exécute de manière concurrente avec d'autres fonctions. Les goroutines sont incroyablement légères, avec une faible empreinte mémoire, vous permettant d'exécuter des milliers (voire des millions) de goroutines simultanément sans saturer les ressources du système.

La concurrence, quant à elle, fait référence à la capacité d'un programme à gérer de nombreuses tâches en même temps. Cela n'implique pas nécessairement que les tâches s'exécutent simultanément (ce qui est le parallélisme), mais plutôt qu'elles progressent indépendamment.

Regardons un exemple de code pour illustrer ces concepts :

```
package main

import (
    "fmt"
    "time"
)

func printNumbers() {
    for i := 1; i <= 5; i++ {
        fmt.Println(i)
        time.Sleep(1 * time.Second)
    }
}

func printLetters() {
    for i := 'A'; i <= 'E'; i++ {
        fmt.Printf("%c\n", i)
        time.Sleep(1 * time.Second)
    }
}

func main() {

    go printNumbers()  // This runs concurrently
    go printLetters()  // This runs concurrently

    // Wait for goroutines to finish
    time.Sleep(6 * time.Second)
    fmt.Println("All tasks completed.")
}
```

Dans le code ci-dessus, nous créons deux fonctions, `printNumbers` et `printLetters`. L'une affiche les chiffres de 1 à 5, et l'autre affiche les lettres de 'A' à 'E'. Nous lançons ces fonctions en tant que **goroutines** en ajoutant le mot-clé `go` avant de les appeler dans la fonction `main`.

Les **goroutines** sont des threads légers qui permettent aux fonctions de s'exécuter de manière concurrente. Cela signifie que `printNumbers()` et `printLetters()` peuvent s'exécuter en même temps sans s'attendre mutuellement. Le concept clé ici est la **concurrence**, où plusieurs tâches progressent indépendamment.

Dans ce cas, les deux goroutines dorment pendant une seconde entre chaque affichage, mais comme elles s'exécutent de manière concurrente, les chiffres et les lettres peuvent être affichés presque simultanément sans bloquer l'exécution de l'autre.

Pour s'assurer que le programme ne s'arrête pas avant que les goroutines n'aient terminé leur travail, nous ajoutons un `time.Sleep(6 * time.Second)` dans la fonction `main`. Cela laisse suffisamment de temps aux deux goroutines pour finir l'affichage avant que le programme ne se termine.

Cet exemple illustre le puissant modèle de concurrence de Go via les goroutines, permettant un multitâche efficace sans la complexité du threading traditionnel.

Pour approfondir les goroutines et la concurrence, [**Destiny Erhabor**][24] a fait un excellent travail en expliquant ce qu'elles sont dans [son article ici][25].

## Structs et héritage

En Go, une `struct` est un type de données composite qui organise des variables (champs) en un seul type. Ces champs peuvent inclure une variété de types de données, ce qui rend les structs adaptées à la description de structures de données complexes. Les structs en Go fonctionnent de manière similaire aux classes dans d'autres langages de programmation, mais sans les méthodes d'héritage classiques.

Commençons par un exemple de struct :

```
type Person struct {
    Name string
    Age  int
}
```

Dans cet exemple, `Person` est une struct avec deux champs : `Name` qui est une `string` et `Age` qui est un `int`. Vous pouvez créer une instance de cette struct comme ceci :

```
p := Person{Name: "Alice", Age: 30}
fmt.Println(p.Name)  // Output: Alice
```

Go ne possède pas d'**héritage** traditionnel comme certains langages orientés objet où une classe hérite des champs et des méthodes d'une autre. Au lieu de cela, Go utilise la **composition**, qui vous permet d'imbriquer une `struct` à l'intérieur d'une autre.

Voici un exemple de code de composition de struct :

```
type Employee struct {
    Person
    Position string
}

e := Employee{
    Person:   Person{Name: "Bob", Age: 25},
    Position: "Developer",
}

fmt.Println(e.Name)     // Output: Bob
fmt.Println(e.Position) // Output: Developer
```

Dans le code ci-dessus, la struct `Employee` imbrique la struct `Person`, et les champs de `Person` peuvent être accédés directement comme `e.Name`. Cela imite certains des comportements que vous attendriez de l'héritage dans d'autres langages, mais c'est fait par composition.

Bien que Go manque d'héritage, il réalise le polymorphisme via les **interfaces**. Une **interface** est un type qui spécifie un ensemble de signatures de méthodes. Un type est dit implémenter une interface s'il fournit les méthodes déclarées par cette interface.

Ce qui rend Go unique, c'est qu'il utilise l'**implémentation implicite**, ce qui signifie qu'un type n'a pas besoin de déclarer explicitement qu'il implémente une interface – il doit simplement correspondre aux signatures de méthodes.

Voyons un exemple :

```
type Speaker interface {
    Speak() string
}

type Person struct {
    Name string
}

func (p Person) Speak() string {
    return "Hi, my name is " + p.Name
}

func saySomething(s Speaker) {
    fmt.Println(s.Speak())
}

func main() {
    p := Person{Name: "Alice"}
    saySomething(p)  // Output: Hi, my name is Alice
}
```

Dans cet exemple, `Person` implémente l'interface `Speaker` en définissant une méthode `Speak`. La fonction `saySomething` prend n'importe quel type qui implémente l'interface `Speaker`, démontrant le **polymorphisme**. Les interfaces de Go offrent un moyen flexible de concevoir un code **propre et extensible** sans avoir besoin de s'appuyer sur l'héritage traditionnel.

## Bibliothèque standard de Go

Il est important de se familiariser avec la bibliothèque standard de Go. Elle contient une collection complète de bibliothèques packagées qui vous offrent un large éventail de fonctionnalités pour des tâches telles que la gestion de fichiers, la communication réseau, la manipulation de chaînes de caractères, les structures de données, la cryptographie, les tests, et plus encore. Cela vous permet d'effectuer des tâches de programmation courantes sans avoir besoin d'installer des packages externes.

### Accéder à et utiliser un package de la bibliothèque standard

Pour accéder à un package de la bibliothèque standard, il vous suffit de l'importer dans votre fichier Go à l'aide de l'instruction `import`. Ensuite, vous pouvez utiliser directement les fonctions du package.

Certains des packages que vous pouvez importer de la bibliothèque standard incluent :

-   `fmt` pour les E/S formatées
    
-   `net/http` pour construire des serveurs web
    
-   `io` pour les opérations d'E/S
    
-   `strings` pour la manipulation de chaînes
    
-   `time` pour les opérations de date et d'heure
    

Par exemple, regardons le package `fmt`, qui est utilisé pour les entrées et sorties formatées. Voici un exemple simple de la façon d'utiliser le package `fmt` pour afficher une sortie formatée :

```
package main

import "fmt"

func main() {
    name := "Alice"
    age := 30
    fmt.Printf("Hello, my name is %s and I am %d years old.\n", name, age)
}
```

Dans cet exemple :

-   La ligne `import "fmt"` nous permet d'accéder au package `fmt` de la bibliothèque standard.
    
-   Nous utilisons `fmt.Printf` pour formater et afficher une chaîne qui inclut un nom (`%s` pour les chaînes) et un âge (`%d` pour les entiers).
    

Chaque package de la bibliothèque standard est bien documenté, avec de nombreux exemples, c'est donc une bonne idée d'explorer la documentation officielle de Go pour mieux comprendre comment utiliser ces packages dans vos projets. Vous pouvez trouver la documentation de la bibliothèque standard de Go [ici][26].

## Tests en Go

Les tests sont des citoyens de première classe en Go. Cela signifie que Go traite les tests comme une partie centrale et intégrante du processus de développement.

Le framework de test de Go est construit autour du package `testing`, qui fournit les outils nécessaires pour écrire des tests. Vous écrivez vos tests dans des fichiers séparés, qui sont automatiquement détectés et exécutés par l'outil Go.

Pour écrire un test, vous devez ajouter le suffixe `_test.go`. Par exemple, si votre fichier de code principal est `math.go`, les tests pour ce fichier iraient dans `math_test.go`.

Voyons comment écrire un test simple. Disons que nous avons une fonction simple dans `math.go` :

```

package math

func Add(a, b int) int {
    return a + b
}
```

Pour tester la fonction `Add`, vous devez créer un fichier de test appelé `math_test.go` :

```

package math

import "testing"

func TestAdd(t *testing.T) {
    result := Add(2, 3)
    expected := 5
    if result != expected {
        t.Errorf("Add(2, 3) = %d; want %d", result, expected)
    }
}
```

Dans le test ci-dessus :

-   La fonction `TestAdd` est définie pour tester la fonction `Add`.
    
-   Le `t.Errorf` est utilisé pour signaler une erreur si le résultat ne correspond pas à la valeur attendue.
    

Pour exécuter le test, vous utilisez cette commande dans votre terminal :

```
go test
```

Vous pouvez également obtenir une sortie plus détaillée en ajoutant le drapeau `-v` comme ceci :

```
go test -v
```

Ce ne sont que les bases, car il existe d'autres types de tests, tels que les tests pilotés par les données (table-driven tests) et le benchmarking.

## Conclusion !

Dans cet article, nous avons examiné neuf concepts clés à apprendre en tant que débutant commençant avec Golang.

Et gardez à l'esprit que ce n'est pas tout ce que vous aurez besoin de savoir lors de votre apprentissage de Go – ce sont juste ce que je considère comme les bases les plus importantes. Elles devraient vous aider à mettre un pied dans le monde de Go.

Si vous pensez que j'ai oublié un concept clé, j'aimerais beaucoup que vous le partagiez avec moi afin que je puisse mettre à jour l'article. Merci !

[1]: #heading-variables-et-types-de-donnees
[2]: #heading-structures-de-controle
[3]: #heading-1-instructions-ifelse
[4]: #heading-2-instructions-switch
[5]: #heading-3-boucles-for
[6]: #heading-fonctions
[7]: #heading-pointeurs
[8]: #heading-gestion-des-erreurs
[9]: #heading-goroutines-et-concurrence
[10]: #heading-structs-et-heritage
[11]: #heading-bibliotheque-standard-de-go
[12]: #heading-acceder-a-et-utiliser-un-package-de-la-bibliotheque-standard
[13]: #heading-tests-en-go
[14]: #heading-conclusion
[15]: https://www.freecodecamp.org/news/variables-and-constants-in-go/
[16]: https://go.dev/tour/flowcontrol/7
[17]: https://go.dev/tour/flowcontrol/9
[18]: https://go.dev/tour/flowcontrol/1
[19]: https://go.dev/tour/basics/4
[20]: https://go.dev/tour/moretypes/1
[21]: https://dev.to/oyedeletemitope/understanding-pointers-in-go-1fa6
[22]: https://go.dev/blog/error-handling-and-go
[23]: https://go.dev/tour/concurrency/1
[24]: https://www.freecodecamp.org/news/author/CaesarSage/
[25]: https://www.freecodecamp.org/news/how-to-handle-concurrency-in-go/
[26]: https://pkg.go.dev/std