---
title: Comment apprendre Golang – Un guide pour débutants sur les bases
subtitle: ''
author: Adeola Ajiboso
co_authors: []
series: null
date: '2024-02-08T17:12:33.000Z'
originalURL: https://freecodecamp.org/news/golang-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/1.jpg
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Comment apprendre Golang – Un guide pour débutants sur les bases
seo_desc: "The Go programming language, also known as Golang, was developed at Google\
  \ in 2007 by Robert Griesemer, Rob Pike, and Ken Thompson. It was open-sourced in\
  \ 2009. \nGo is expressive, concise, clean, and efficient. The language is statically\
  \ typed with s..."
---

Le langage de programmation Go, également connu sous le nom de Golang, a été développé chez Google en 2007 par Robert Griesemer, Rob Pike et Ken Thompson. Il a été open-sourcé en 2009. 

Go est expressif, concis, propre et efficace. Le langage est statiquement typé avec une syntaxe similaire à celle du langage de programmation C. 

Go a été conçu pour fonctionner sur plusieurs cœurs et a été construit pour supporter la concurrency. Vous pouvez utiliser Go pour écrire des applications qui doivent être performantes et peuvent fonctionner à une échelle moderne, comme des systèmes distribués avec des centaines de milliers de serveurs sur une plateforme cloud.  
  
Dans cet article, vous apprendrez à écrire une application CLI (Command Line Interface) basique en Go. Tout d'abord, nous passerons brièvement en revue certaines caractéristiques principales de Go. Ensuite, nous parlerons de la structure de base d'un fichier Go. Enfin, vous apprendrez à configurer Go localement pour écrire du code. 

## Table des matières

* [Caractéristiques de Go](#heading-caracteristiques-de-go)
* [Comment installer Go localement sur Windows](#heading-comment-installer-go-localement-sur-windows) 
* [Comment commencer à écrire du code en Go](#comment-commencer-a-ecrire-du-code-en-go)
* [Qu'est-ce que les packages en Go ?](#heading-quest-ce-que-les-packages-en-go)
* [Qu'est-ce que les modules en Go ?](#heading-quest-ce-que-les-modules-en-go)
* [Qu'est-ce que la commande Go ?](#heading-quest-ce-que-la-commande-go)
* [Qu'est-ce que les variables en Go ?](#heading-quest-ce-que-les-variables-en-go)
* [Conventions de nommage en Go](#heading-conventions-de-nommage-en-go)
* [Différences entre le mot-clé `var` et les mots-clés `const`](#differences-entre-le-mot-cle-var-et-les-mots-cles-const)
* [Types de données en Go](#heading-types-de-donnees-en-go)
* [Opérateurs en Go](#heading-operateurs-en-go)
* [Conclusion](#heading-conclusion)

## Caractéristiques de Go

### Go est utilisé comme langage côté serveur et backend

Go est couramment utilisé pour construire des applications côté serveur et des services backend. Cela inclut une large gamme d'applications telles que les microservices, les applications web, les serveurs API et les services de base de données.

Go est conçu avec la concurrency à l'esprit, ce qui le rend bien adapté pour construire des applications côté serveur scalables et efficaces. Sa simplicité, ses performances et son support intégré pour la concurrency en font un choix favorable pour le développement backend.

### Go utilise une syntaxe simple

Go a une syntaxe directe et minimaliste. Il est intentionnellement conçu pour être facile à apprendre, à lire et à écrire du code. Go encourage un style de codage propre et concis.

Une syntaxe simple réduit la charge sur les développeurs, rendant plus facile pour eux de comprendre et de maintenir le code.

### Go a un temps de build, de démarrage et d'exécution rapides

Le processus de compilation de Go est rapide, permettant aux développeurs de voir les résultats de leurs changements de code rapidement.

De plus, les programmes Go démarrent généralement rapidement et ont des performances d'exécution efficaces.

### Go est efficace en ressources

Les programmes Go nécessitent généralement moins de ressources système comme le CPU et la RAM pour fonctionner par rapport à certains autres langages. Cela est en partie dû à la nature compilée statiquement de Go et à son runtime efficace.

Des exigences de ressources plus faibles rendent Go bien adapté pour construire des applications qui doivent être légères et efficaces, en particulier dans des environnements où les ressources sont limitées. Cela contribue à une meilleure scalabilité et à une rentabilité dans les déploiements de serveurs.

### Go est un langage compilé

Go est un langage compilé, ce qui signifie que le code source est traduit en code machine ou en une forme intermédiaire avant l'exécution. Cela contraste avec les langages interprétés où le code est exécuté directement par un interpréteur.

La compilation offre des avantages tels qu'une exécution plus rapide, car le code est pré-traité en une forme que la machine peut exécuter directement. Elle garantit également que les erreurs potentielles sont détectées pendant la phase de compilation, réduisant les erreurs d'exécution et améliorant la fiabilité globale du programme.

## Comment installer Go localement sur Windows 

### Installer Go sur votre système

Avant d'installer Go, ouvrez votre invite de commande, tapez « go » et appuyez sur Entrée. Cela permet de confirmer si vous avez Go installé sur votre PC ou non.

Lorsque vous entrez « go » et appuyez sur Entrée, vous devriez obtenir un message indiquant « 'go' n'est pas reconnu en tant que commande interne ou externe, programme exécutable ou fichier de commandes ».

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-4.png)
_Interface de l'invite de commande_

Cela signifie que vous devez l'installer.

Pour installer Go sur votre ordinateur Windows, vous devez d'abord [télécharger Golang](https://go.dev/doc/install) depuis le site officiel. Il supporte tous les principaux systèmes d'exploitation. Installez celui qui correspond à votre système d'exploitation.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image.png)
_Interface du site officiel de Golang_

Ensuite, double-cliquez sur l'installateur téléchargé pour installer Go. Suivez les invites en conséquence et Go sera installé.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-5.png)
_Interface de l'installateur de Go_

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-6.png)
_Interface de l'installateur de Golang_

Après avoir installé Go, retournez à la ligne de commande et tapez "go" à nouveau. Cette fois, vous devriez voir de nombreuses commandes en Go.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-8.png)
_Invite de commande pour montrer l'achèvement de l'installation de Go_

Maintenant, vous devrez configurer votre espace de travail Go en configurant les variables d'environnement. Allez sur votre bureau et créez un dossier appelé "go-projects" (vous pouvez l'appeler comme vous le souhaitez). C'est le dossier où vos projets Go seront sauvegardés. 

Tout d'abord, recherchez "env" dans la barre de recherche Windows et cliquez sur "Modifier les variables d'environnement système".

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-9.png)
_Rechercher Modifier les variables d'environnement système_

  
Cliquez sur le bouton Variables d'environnement, comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-10.png)
_Cliquez sur le bouton Variables d'environnement_

  
Vous devrez changer la valeur de la variable `GOPATH` pour le dossier que vous avez créé précédemment.

Assurez-vous que "GOPATH" est sélectionné, puis cliquez sur "Modifier...".

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-11.png)
_Sélectionnez GOPATH_

  
Cliquez sur "Parcourir le répertoire"

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-14.png)
_Cliquez sur "Parcourir le répertoire"_



Sélectionnez le dossier que vous avez créé précédemment ("go-projects", ou peu importe comment vous avez nommé le vôtre) et cliquez sur "OK".

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-16.png)
_Sélectionnez le dossier que vous avez créé précédemment_

  
Cliquez "OK" à nouveau.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-17.png)
_Cliquez OK_

Cliquez "OK" à nouveau.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-18.png)

Cliquez "OK" une dernière fois.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-20.png)

Voilà ! Vous avez terminé la configuration de la variable GOPATH. 

### Configurer un IDE

Installez un IDE (Integrated Development Environment) de votre choix si vous n'en avez pas déjà installé un. 

Un IDE est un éditeur pour écrire du code, comme Visual Studio Code, Sublime, etc.  
[Voici le lien pour télécharger Visual Studio Code](https://code.visualstudio.com/download).

### Installer l'extension Go dans VS Code

Ensuite, vous voudrez installer l'extension Go sur Visual Studio Code. Elle fournit des fonctionnalités comme la complétion de code, la navigation dans le code, la coloration syntaxique et les suggestions de snippets.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Go-extension.jpg)
_Extension Go_

## Comment commencer à écrire du code en Go

Ouvrez le dossier "go-projects" (ou peu importe comment vous l'avez nommé) avec VS Code (ou votre éditeur de code de choix). Créez un dossier appelé "hello-world" (c'est optionnel) et créez un fichier nommé `main.go`. Vous pouvez nommer le fichier comme vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/How-To-Write-Code-in-Go.jpg)
_Exemple de code Go_

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-29.png)
_Résultat_

Vous vous demandez peut-être ce que fait l'extrait de code ci-dessus 🤔. Je vais expliquer en détail ci-dessous.

Allons-y 🚀🚀

* **Déclaration de package (`package main`) :** Chaque programme Go commence par une déclaration de package, indiquant à quel package le fichier appartient. Le package `main` est un package spécial, car c'est le point d'entrée pour les programmes exécutables.
* **Instruction d'import (`import "fmt"`) :** En Go, vous importez des packages pour utiliser leurs fonctions et leurs fonctionnalités. Ici, nous importons le package `fmt`, qui signifie "format" et est utilisé pour les opérations d'entrée et de sortie.
* **Fonction principale (`func main()`) :** Chaque programme exécutable Go doit avoir une fonction `main`. Lorsque vous exécutez votre programme, c'est la première fonction qui est exécutée.
* **Instruction d'impression (`fmt.Println("Hello World")`) :** Cette ligne utilise la fonction `Println` du package `fmt` pour imprimer le texte "Hello World" sur la console. La fonction `Println` est utilisée pour l'impression avec un caractère de nouvelle ligne à la fin, de sorte que la sortie suivante apparaît sur une nouvelle ligne.

### Qu'est-ce que les packages en Go ?

Les packages sont la manière de Go d'organiser le code. Un package est une collection de fichiers sources. Il doit être étroitement focalisé et effectuer une seule chose comme le passage d'arguments, la gestion des requêtes HTTP, etc.  
  
Les programmes commencent à s'exécuter dans `package main`. Ce programme utilise les packages avec les chemins d'importation `"fmt"`.

En Go, le **chemin d'importation** est un identifiant unique pour un package. Il spécifie l'emplacement d'un package dans le système de modules Go. Le chemin d'importation est utilisé dans l'instruction `import` pour importer des packages externes ou des dépendances dans votre code Go.

Voici une ventilation du chemin d'importation :

**Packages de la bibliothèque standard :** Pour les packages qui font partie de la bibliothèque standard de Go, vous pouvez utiliser directement leur nom dans l'instruction d'importation. 

Par exemple :

```go
import "fmt"

```

**Packages locaux :** Si vous travaillez sur un projet avec plusieurs fichiers ou packages, vous pouvez utiliser des chemins d'importation relatifs pour importer des packages locaux. 

Par exemple, si vous avez un package nommé "mypackage" dans le même répertoire que votre fichier principal, vous pouvez l'importer comme ceci :

```go
import "./mypackage"

```

**Packages distants (à partir de dépôts de contrôle de version) :** Go supporte l'importation de packages directement à partir de dépôts de contrôle de version comme GitHub. Le chemin d'importation inclut l'URL du dépôt. 

Par exemple :

```go
import "github.com/example/mypackage"

```

**Packages distants (à partir de serveurs personnalisés) :** Vous pouvez également importer des packages à partir de serveurs personnalisés en spécifiant l'URL complète. 

Par exemple :

```go
import "myserver.com/mypackage"

```

**Packages vendus :** Si vous avez un package vendu (une copie d'un package conservée dans le dépôt de votre projet), vous pouvez l'importer en utilisant un chemin relatif à la racine de votre projet. 

Par exemple :

```go
import "myproject/vendor/mypackage"

```

**Packages à partir du cache de modules Go :** Avec l'introduction des modules Go, lors de l'utilisation de modules, Go met automatiquement en cache les dépendances dans un cache de modules. Les chemins d'importation peuvent faire référence aux packages dans le cache. 

Par exemple :

```go
import "example.com/mypackage"

```

`package main` est toujours écrit en haut de votre code comme montré ci-dessous 

Voici un exemple ci-dessous :

```go
package main

import "fmt"

func main(){
	fmt.Println("Hello World")
 }
```

### **Qu'est-ce que les modules en Go ?**

Un module est une collection de packages. Il contient des informations sur votre projet comme les dépendances, la version de Go et les informations sur les packages. Tous les projets Go ont un fichier go.mod.

Voici la commande pour initialiser le fichier `go.mod` à partir du terminal :

```go
go mod init <module path>
```

`module path` est également le **chemin d'importation**.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-25.png)
_Comment initialiser `go.mod` à partir du terminal_

L'image ci-dessus montre comment les modules sont créés directement à partir du terminal. Et voici le fichier `go.mod` généré :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-26.png)
_Capture d'écran du contenu de `go.mod`_

### Qu'est-ce que la commande `Go` ?

La "commande Go" fait référence à l'outil en ligne de commande `go` dans le langage de programmation Go. C'est un outil polyvalent que vous pouvez utiliser pour effectuer diverses tâches liées au développement Go telles que la compilation, les tests, l'installation de packages, la gestion des dépendances, et plus encore.

#### Que fait la commande `go` ?

La commande `go` automatise de nombreux aspects du flux de travail de développement Go. Elle gère des tâches comme la compilation, les tests, la gestion des dépendances, et plus encore, rendant plus facile pour les développeurs de construire, tester et maintenir des projets Go. Elle facilite également l'adoption des modules Go, un système de gestion des dépendances introduit pour améliorer le versionnage et le suivi des dépendances dans les projets Go.

Vous utilisez la commande `go` dans divers scénarios pendant le cycle de vie du développement d'un projet Go :

* **Exécuter du code :** `go run` compile et exécute un programme Go.
* **Construire des exécutables :** `go build` compile le code source Go en un binaire exécutable.
* **Tester du code :** `go test` exécute les tests dans le package actuel et `go test ./...` exécute les tests dans tous les sous-répertoires.
* **Gestion des packages (avec les modules) :** `go mod init` initialise un nouveau module (projet Go) et crée un fichier `go.mod`. `go get` télécharge et installe des packages et des dépendances. `go mod tidy` supprime toutes les dépendances qui ne sont plus nécessaires. Et `go list -m all` liste toutes les dépendances pour le module actuel.
* **Documentation :** `go doc` montre la documentation pour un package ou un symbole.
* **Analyse des dépendances :** `go list` liste les informations sur les packages disponibles. `go list -m -versions <module>` liste toutes les versions connues d'un module.
* **Formatage du code :** `go fmt` formate le code source Go.
* **Environnement :** `go env` imprime les informations sur l'environnement Go.

### Qu'est-ce que les variables en Go ?

Les variables fournissent un moyen de stocker et d'accéder aux données dans votre programme.

Pour créer une variable, vous pouvez utiliser la création simple, la création composée, la création par bloc, ou la méthode de création et d'affectation. Passons en revue des exemples de chacune d'entre elles maintenant.

#### Création simple

La création simple est utilisée lorsque vous devez créer et initialiser une seule variable.

Exemple d'utilisation de la méthode de création simple :

```go
package main

import "fmt"

func main() {
    var singleVariable int
    singleVariable = 10
    fmt.Println(singleVariable)
}

```

Dans cet exemple, `singleVariable` est déclarée et plus tard affectée de la valeur `10`.

#### Création composée

Nous pouvons également créer plusieurs variables en même temps. Cette façon de créer des variables simplifie l'affectation de plusieurs types de données différents à plusieurs variables.

```go
package main

import "fmt"

func main() {
    var a, b, c  = 1, 2, "Coders"
    fmt.Println(a, b, c)
}

```

#### Création par bloc

La création par bloc est utilisée lorsque vous voulez limiter la portée des variables à un bloc spécifique. Vous déclarez et initialisez plusieurs variables dans un bloc de code `{}`.

```go
package main

import "fmt"

func main() {
    {
        var blockVariable int
        blockVariable = 5
        fmt.Println(blockVariable)
    }

    // blockVariable n'est pas accessible ici
}

```

Dans cet exemple, `blockVar1` n'est accessible que dans le bloc où il est déclaré.

#### Créer et affecter

Vous déclarez et initialisez une variable en une seule ligne en utilisant le raccourci `:=`, comme ceci :

```go
package main

import "fmt"

func main() {
    createAndAssignVar := 42
    fmt.Println(createAndAssignVar)
}
```

Dans cet exemple, `createAndAssignVar` est déclarée et initialisée en une seule ligne en utilisant le raccourci `:=`.

### Conventions de nommage en Go

Le nommage des variables en Go utilise le camel case. Par exemple :

```go
const myVariable = 20
```

Chaque fois que vous créez un nom de variable, il est bon de lui donner un nom descriptif, par exemple `conferenceName := "Linux"` au lieu de `conference := "Linux"`.

### Différence entre le mot-clé `var` et le mot-clé `const` en Go

Il existe deux façons de déclarer des variables en Go : `var` et `const`. Pour ceux d'entre vous qui connaissent JavaScript, cela peut sembler familier.

* `var` est utilisé pour déclarer des variables, et leurs valeurs peuvent être changées après la déclaration.
* `const` est utilisé pour déclarer des constantes, et leurs valeurs ne peuvent pas être changées après la déclaration.

Voici un exemple d'utilisation de `var` et `const` pour déclarer des variables :

```go
package main

import "fmt"

func main() {
    // Utilisation de var
    var variable1 int = 5
    variable1 = 10  // Valide, la valeur de variable1 peut être changée

    // Utilisation de const
    const constant1 int = 5
    // constant1 = 10  // Invalide, les constantes ne peuvent pas être réaffectées
    
    fmt.Println(variable1, constant1)
}

```

Dans l'exemple ci-dessus, `variable1` peut être réaffectée à une nouvelle valeur, tandis que `constant1` ne peut pas être réaffectée en raison de sa nature `const`.

### Types de données en Go

Il existe différents types de données en Golang, qui incluent `number`, `string`, `boolean`, `array`, `pointer`, `struct`, `map`, et `interface`.

Voyons des exemples de chacun d'entre eux afin que vous puissiez apprendre comment ils fonctionnent.

* `Number` (int, float64) est utilisé pour représenter des valeurs numériques (nombres entiers ou décimaux). Voici un exemple :

```go
package main

import "fmt"

func main() {
    // Entiers
    var integerVar int = 42
    fmt.Println(integerVar)

    // Nombres à virgule flottante
    var floatVar float64 = 3.14
    fmt.Println(floatVar)
}

```

Dans cet exemple, `integerVar` est une variable entière, et `floatVar` est une variable à virgule flottante.

* `String` est utilisé pour représenter des séquences de caractères (texte). Voici un exemple :

```go
package main

import "fmt"

func main() {
    var stringVar string = "Hello, Golang!"
    fmt.Println(stringVar)
}

```

Dans cet exemple, `stringVar` est une variable de chaîne contenant le texte "Hello, Golang!".

* `Boolean` est utilisé pour représenter des valeurs logiques (`true` ou `false`). Voici un exemple :

```go
package main
import "fmt"
func main() {
	var boolVar bool = true
	fmt.Println(boolVar)
}
```

Dans cet exemple, `boolVar` est une variable booléenne définie sur `true`.

* `Array` est utilisé pour stocker des séquences de taille fixe d'éléments du même type. Voici un exemple

```go
package main

import "fmt"

func main() {
    var intArray [3]int = [3]int{1, 2, 3}
    fmt.Println(intArray)
}

```

Dans cet exemple, `intArray` est un tableau d'entiers avec une taille fixe de 3. 

* `Pointer` est utilisé pour stocker l'adresse mémoire d'une variable. Voici un exemple :

```go
package main

import "fmt"

func main() {
    var originalVar int = 42
    var pointerVar *int = &originalVar
    fmt.Println(*pointerVar) // Dereferencing the pointer
}

```

Dans cet exemple, `pointerVar` est un pointeur vers l'adresse mémoire de `originalVar`. 

* `Structure (Struct)` est utilisé pour regrouper des variables de différents types sous un seul nom. Voici un exemple :

```go
package main

import "fmt"

type Person struct {
    Name string
    Age  int
}

func main() {
    var personVar Person = Person{Name: "Alice", Age: 30}
    fmt.Println(personVar)
}

```

Dans cet exemple, `personVar` est une structure représentant une personne avec un nom et un âge 

* `Map` est utilisé pour représenter des paires clé-valeur. Voici un exemple :

```go
package main

import "fmt"

func main() {
    var myMap map[string]int = map[string]int{"one": 1, "two": 2, "three": 3}
    fmt.Println(myMap)
}

```

Dans cet exemple, `myMap` est une map avec des clés de type chaîne et des valeurs de type entier. 

* `Interface` est utilisé pour définir un ensemble de signatures de méthodes sans spécifier l'implémentation. Voici un exemple :

```go
package main

import "fmt"

type Shape interface {
    Area() float64
}

type Circle struct {
    Radius float64
}

func (c Circle) Area() float64 {
    return 3.14 * c.Radius * c.Radius
}

func main() {
    var myShape Shape = Circle{Radius: 5.0}
    fmt.Println(myShape.Area())
}

```

Dans cet exemple, `Shape` est une interface, et `Circle` est un type implémentant la méthode `Area` de l'interface `Shape`.

### Opérateurs en Go 

Il existe 3 principaux types d'opérateurs en Go : les opérateurs arithmétiques, les opérateurs logiques et les opérateurs relationnels

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Operators--1-.png)

Maintenant, passons en revue chaque catégorie d'opérateurs et voyons comment ils fonctionnent, avec des exemples.

#### Opérateurs arithmétiques

Les opérateurs arithmétiques sont utilisés lorsque vous devez effectuer des opérations mathématiques de base dans votre code. Ils incluent les éléments suivants :

* **Addition (+)** est utilisée pour additionner des valeurs numériques. Voici un exemple :

```go
package main

import "fmt"

func main (){    
	a := 5    
	b := 3    
	result := a + b  
    // result is 8
fmt.Println(result)
}

```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-39.png)
_Comment utiliser l'opérateur d'addition en Go_

* **Soustraction (-)** est utilisée pour trouver la différence entre deux valeurs numériques. Voici un exemple :

```go
package main

import "fmt"

func main (){
	a := 8
	b := 3
	result := a - b
	// result is 5
fmt.Println(result)

```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-40.png)
_Comment utiliser l'opérateur de soustraction_

* **Multiplication (*)** est utilisée pour calculer le produit de deux valeurs numériques. Voici un exemple :

```go
package main

import "fmt"

func main (){ 
	a := 4
	b := 6
	result := a * b
// result is 24
fmt.Println(result)

```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-41.png)
_Comment utiliser l'opérateur de multiplication_

* **Division (/)** est utilisée pour calculer le quotient de deux valeurs numériques. Voici un exemple :

```go
package main

import "fmt"

func main(){
	a := 10
	b := 2
	result := a / b
// result is 5
fmt.Println(result)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-42.png)
_Comment utiliser l'opérateur de division_

* **Modulo (%)** retourne le reste de la division du premier opérande par le second opérande. Voici un exemple :

```go
package main

import "fmt"

func main (){
    a := 15
    b := 7
    result := a % b
fmt.Println(result)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-43.png)
_Comment utiliser l'opérateur modulo_

#### Opérateurs relationnels

Les opérateurs relationnels sont utilisés pour comparer des valeurs et prendre des décisions basées sur les résultats de la comparaison. Ils incluent les éléments suivants :

* **Supérieur à (>)** est utilisé pour les comparaisons où le premier opérande est supérieur au second opérande. Voici un exemple

```go
package main

import "fmt"

func main (){
	x := 8
	y := 5
	isGreater := x > y
// isGreater is true
fmt.Println(isGreater)
}

```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-44.png)
_Comment utiliser le signe supérieur à_

* **Inférieur à (<)** est utilisé pour les comparaisons où le premier opérande est inférieur au second opérande. Voici un exemple :

```go
package main

import "fmt"

func main (){
	p := 12
	q := 18
	isLess := p < q
	// isLess is true
fmt.Println(isLess)

]

```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-45.png)
_**Comment utiliser le signe inférieur à**_

* **Supérieur ou égal (>=)** vérifie si le premier opérande est supérieur ou égal au second opérande. Voici un exemple :

```go
package main

import "fmt"

func main (){
	m := 5
	n := 5
	isGreaterOrEqual := m >= n
	// isGreaterOrEqual is true
fmt.Println(isGreaterOrEqual)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-46.png)
_**Comment utiliser le signe supérieur ou égal**_

* **Inférieur ou égal à (<=)** vérifie si le premier opérande est inférieur ou égal au second opérande.

```go
package main

import "fmt"

func main (){
	r := 10
	s := 15
	isLessOrEqual := r <= s
	// isLessOrEqual is true
fmt.Println(isLessOrEqual)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-47.png)
_Comment utiliser le signe inférieur ou égal_

* **Équivalence (==)** vérifie si le premier opérande est égal au second opérande. Vous utilisez cela pour les comparaisons d'égalité. Voici un exemple :

```go
package main

import "fmt"

func main (){
	age := 25
	checkAge := age == 25
	// checkAge is true
fmt.Println(checkAge)
}

```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-48.png)
_Comment utiliser le signe d'équivalence_

* **Non égal (!=)** vérifie si les deux opérandes ne sont pas égaux. Voici un exemple :

```go
package main

import "fmt"

func main (){
	score1 := 80
	passingScore := score1 != 75
	// passingScore is true
fmt.Println(passingScore)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-49.png)
_**Comment utiliser le signe non égal**_

#### Opérateurs logiques

Vous utilisez les opérateurs logiques lorsque vous devez implémenter une logique booléenne et prendre des décisions basées sur plusieurs conditions.

* **ET logique (&&) :** Cet opérateur retourne vrai uniquement si les deux opérandes sont vrais, sinon, il retourne faux. Voici un exemple :

```go
package main

import "fmt"

func main (){
	x := true
	y := false
	result := x && y
	// result is false
fmt.Println(result)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-50.png)
_Exemple de ET logique_

* **OU logique (||) :** Cet opérateur retourne vrai si au moins l'un des opérandes est vrai, sinon, il retourne faux. Voici un exemple :

```go
package main

import "fmt"

func main (){
	a := true
	b := false
	result := a || b
// result is true
fmt.Println(result)
}

```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-51.png)
_Exemple de OU logique_

* **NON logique (!) :** Cet opérateur est un opérateur unaire, ce qui signifie qu'il opère sur un seul opérande. Il nie la valeur de l'opérande, transformant vrai en faux et faux en vrai. Voici un exemple :

```go
package main

import "fmt"

func main (){
	isSunny := true
	isRainy := !isSunny
	// isRainy is false
fmt.Println(isRainy)
}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Logical-not.jpg)
_Exemple de NON logique_

## Conclusion

Dans cet article, vous avez appris le langage de programmation Go et pourquoi il est utile de le connaître. Vous avez également appris les caractéristiques de Go et comment installer Go localement sur Windows.

Ensuite, vous avez appris à commencer à écrire du code en Go, et vous avez vu des exemples de nombreuses fonctionnalités de Go en action. Nous avons également parlé de ce que sont les packages, de comment fonctionnent les modules, et plus encore.

Go vaut vraiment la peine d'être appris. Maintenant, allez étudier un peu plus Go.

Bonne programmation !