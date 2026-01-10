---
title: Le Guide Go – Apprendre Golang pour Débutants
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2022-10-18T18:35:37.000Z'
originalURL: https://freecodecamp.org/news/go-beginners-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/golang.png
tags:
- name: beginner
  slug: beginner
- name: beginners guide
  slug: beginners-guide
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Le Guide Go – Apprendre Golang pour Débutants
seo_desc: 'Golang is an awesome, simple, modern, and fast programming language.

  It’s compiled, open source, and strongly typed.

  Golang – also called Go – was created by Google engineers with these main goals:


  make their projects compile (and run) faster

  be sim...'
---

Golang est un langage de programmation génial, simple, moderne et rapide.

Il est compilé, open source et fortement typé.

Golang – également appelé Go – a été créé par des ingénieurs de Google avec ces principaux objectifs :

* rendre leurs projets plus rapides à compiler (et à exécuter)
* être simple afin que les gens puissent l'apprendre en peu de temps
* être suffisamment bas niveau mais aussi éviter certains pièges d'être trop bas niveau
* être portable (les programmes Go compilés sont des binaires qui ne nécessitent pas d'autres fichiers pour s'exécuter et sont multiplateformes, donc ils peuvent être distribués facilement)
* être ennuyeux, stable, prévisible, offrir moins d'opportunités de faire des erreurs
* faciliter l'exploitation des systèmes multiprocesseurs

Go était destiné à être un remplacement pour les bases de code C et C++. Il vise à simplifier certaines choses comme la concurrence et la gestion de la mémoire, avec un ramasse-miettes.

De plus, il a été conçu pour fonctionner avec les bases de code C et C++, grâce à ses fonctionnalités d'interopérabilité C.

Vous pouvez utiliser Go pour de nombreuses tâches différentes, et il peut résoudre à la fois des problèmes simples et très complexes.

Vous pouvez utiliser Go pour créer des utilitaires de ligne de commande et des serveurs réseau, et il est largement utilisé dans de nombreux scénarios différents.

Par exemple, Docker et Kubernetes sont écrits en Go.

Mon générateur de site statique préféré (Hugo) est écrit en Go.

Caddy, un serveur web assez populaire, est écrit en Go.

Il existe de nombreux outils différents et largement utilisés qui utilisent ce langage de programmation sous le capot.

Ce guide vous présentera le langage de programmation Go afin que vous puissiez commencer à coder en Go.

[Vous pouvez obtenir une version PDF et ePub de ce Guide du Débutant en Go ici](https://thevalleyofcode.com/download/go/).

## Table des Matières

1. [Comment commencer avec Go](#heading-comment-commencer-avec-go)
2. [Comment installer Go](#heading-comment-installer-go)
3. [Comment configurer votre éditeur](#heading-comment-configurer-votre-editeur)
4. [Comment écrire Hello, World! en Go](#heading-comment-ecrire-hello-world-en-go)
5. [Comment compiler et exécuter un programme Go](#heading-comment-compiler-et-executer-un-programme-go)
6. [L'espace de travail Go](#heading-lespace-de-travail-go)
7. [Plonger dans le langage Go](#heading-plonger-dans-le-langage-go)
8. [Variables en Go](#heading-variables-en-go)
9. [Types de base en Go](#heading-types-de-base-en-go)
10. [Chaînes de caractères en Go](#heading-chaines-de-caracteres-en-go)
11. [Tableaux en Go](#heading-tableaux-en-go)
12. [Tranches en Go](#heading-tranches-en-go)
13. [Cartes en Go](#heading-cartes-en-go)
14. [Boucles en Go](#heading-boucles-en-go)
15. [Conditionnelles en Go](#heading-conditionnelles-en-go)
16. [Opérateurs en Go](#heading-operateurs-en-go)
17. [Structures en Go](#heading-structures-en-go)
18. [Fonctions en Go](#heading-fonctions-en-go)
19. [Pointeurs en Go](#heading-pointeurs-en-go)
20. [Méthodes en Go](#heading-methodes-en-go)
21. [Interfaces en Go](#heading-interfaces-en-go)
22. [Où aller à partir d'ici](#heading-ou-aller-a-partir-dici)

## Comment commencer avec Go

Voici quelques choses que vous devez savoir avant de plonger dans les spécificités du langage.

Tout d'abord, [https://go.dev](https://go.dev/) est la page d'accueil du langage. Ce sera votre ressource de référence pour :

* Télécharger les binaires Go (la commande `go` et d'autres outils associés) depuis [https://go.dev/doc/install](https://go.dev/doc/install)
* Référencer la documentation officielle de Go [https://go.dev/doc/](https://go.dev/doc/)
* Voir tous les packages Go [https://pkg.go.dev/](https://pkg.go.dev/)
* Accéder au Go Playground [https://go.dev/play/](https://go.dev/play/)

…et plus encore.

## Comment installer Go

Allez sur [https://go.dev/doc/install](https://go.dev/doc/install) et téléchargez le package pour votre système d'exploitation.

Exécutez l'installateur, et à la fin du processus, vous aurez la commande `go` disponible dans votre terminal :

![Screen Shot 2022-07-28 at 10.19.21.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_10.19.21.png)
_Bienvenue dans l'installateur Go_

![Screen Shot 2022-07-28 at 10.20.54.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_10.20.54.png)
_Modale d'installation réussie_

Ouvrez le terminal et exécutez `go version` et vous devriez voir quelque chose comme ceci :

![Screen Shot 2022-07-28 at 10.21.32.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_10.21.32.png)
_Affichage de la version de Go que vous avez_

REMARQUE : vous devrez peut-être ouvrir un nouveau terminal avant de pouvoir exécuter le programme, car l'installateur a ajouté le dossier des binaires Go au chemin.

L'emplacement exact des fichiers d'installation de Go dépendra de votre système d'exploitation.

Sur macOS, il se trouve sous `/usr/local/go`, avec les binaires dans `/usr/local/go/bin`.

Sur Windows, il se trouvera sous `C:\Program Files\go`.

Les installateurs Windows et Mac définiront automatiquement le chemin des binaires Go.

Sur un Mac, vous pourriez également vouloir installer Go via Homebrew en utilisant `brew install golang`. Cela facilitera les mises à jour ultérieures.

Sur Linux, vous devrez ajouter le dossier des binaires Go à votre chemin de terminal avant de pouvoir exécuter la commande `go` après avoir décompressé le package Linux dans `/usr/local/go` avec cette commande :

```bash
echo 'export PATH=$PATH:/usr/local/go/bin' >> $HOME/.profile
source $HOME/.profile
```

## Comment configurer votre éditeur

Je recommande d'utiliser [**Visual Studio Code**](https://code.visualstudio.com/) (aka VS Code) comme éditeur.

Lisez [Go dans Visual Studio Code](https://code.visualstudio.com/docs/languages/go) pour une configuration rapide "up and running". Au minimum, installez [l'extension Go](https://marketplace.visualstudio.com/items?itemName=golang.go).

![Screen Shot 2022-07-28 at 10.54.06.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_10.54.06.png)
_Extension Go pour VSCode_

Cette extension facilitera votre vie, car elle fournit IntelliSense (coloration syntaxique, autocomplétion, informations au survol, mise en évidence des erreurs…) et d'autres fonctionnalités comme le formatage automatique, des options de menu pour installer des packages, des tests, et plus encore.

## Comment écrire Hello, World! en Go

Maintenant, nous sommes prêts à créer notre premier programme Go !

C'est une tradition des programmeurs de faire en sorte que le premier programme imprime la chaîne "Hello, World!" dans le terminal lorsqu'il est exécuté. Nous allons donc faire cela en premier, puis nous expliquerons comment nous l'avons fait.

Peut-être avez-vous un dossier dans votre répertoire personnel où vous gardez tous vos projets et tests de codage.

Dans ce dossier, créez un nouveau dossier, par exemple appelez-le `hello`.

Dans ce dossier, créez un fichier `hello.go` (vous pouvez le nommer comme vous le souhaitez).

Ajoutez ce contenu :

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")
}
```

![Screen Shot 2022-07-28 at 12.17.14.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_12.17.14.png)
_Code Go "Hello, World!"_

C'est votre premier programme Go !

Analysons cela ligne par ligne.

```go
package main
```

Nous organisons les programmes Go en packages.

Chaque fichier `.go` déclare d'abord à quel package il appartient.

Un package peut être composé de plusieurs fichiers, ou d'un seul fichier.

Un programme peut contenir plusieurs packages.

Le package `main` est le point d'entrée du programme et identifie un programme exécutable.

```go
import "fmt"
```

Nous utilisons le mot-clé `import` pour importer un package.

`fmt` est un package intégré fourni par Go qui fournit des fonctions utilitaires d'entrée/sortie.

Nous avons une [grande bibliothèque standard](https://pkg.go.dev/std) prête à l'emploi que nous pouvons utiliser pour tout, de la connectivité réseau aux mathématiques, à la cryptographie, au traitement d'images, à l'accès au système de fichiers, et plus encore.

Vous pouvez lire toutes les fonctionnalités que ce package `fmt` fournit [dans la documentation officielle](https://pkg.go.dev/fmt).

```go
func main() {
	
}
```

Ici, nous déclarons la fonction `main()`.

Qu'est-ce qu'une fonction ? Nous en verrons plus sur elles plus tard, mais en attendant, disons qu'une fonction est un bloc de code auquel on assigne un nom et qui contient certaines instructions.

La fonction `main` est spéciale car c'est là que le programme commence.

Dans ce cas simple, nous n'avons qu'une seule fonction – le programme commence avec celle-ci et se termine ensuite.

```go
fmt.Println("Hello, World!")
```

C'est le contenu de la fonction que nous avons définie.

Nous appelons la fonction `Println()` définie dans le package `fmt` que nous avons précédemment importé, en passant une chaîne comme paramètre.

Cette fonction, selon les [docs](https://pkg.go.dev/fmt#Printf) "_formate selon un spécificateur de format et écrit dans la sortie standard_".

Jetez un coup d'œil aux docs car elles sont excellentes. Elles ont même des exemples que vous pouvez exécuter :

![Screen Shot 2022-07-28 at 14.18.46.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_14.18.46.png)
_Exemple de fonction de base Go_

Nous utilisons la syntaxe « point » `fmt.Println()` pour spécifier que la fonction est fournie par ce package.

Après que le code ait exécuté la fonction `main`, il n'a plus rien à faire et l'exécution se termine.

## Comment compiler et exécuter un programme Go

Maintenant, ouvrez le terminal dans le dossier `hello` et exécutez le programme en utilisant :

```bash
go run hello.go
```

![Screen Shot 2022-07-28 at 12.18.23.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_12.18.23.png)
_Sortie Hello world en Go_

Notre programme s'est exécuté avec succès et a imprimé « Hello, World! » dans le terminal.

L'outil `go run` compile d'abord puis exécute le programme spécifié.

Vous pouvez créer un **binaire** en utilisant `go build` :

```bash
go build hello.go
```

Cela créera un fichier `hello` qui est un binaire que vous pouvez exécuter :

![Screen Shot 2022-07-28 at 12.19.50.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_12.19.50.png)
_Binaire exécutable en Go_

Dans l'introduction, j'ai mentionné que Go est portable.

Maintenant, vous pouvez distribuer ce binaire et tout le monde peut exécuter le programme tel quel, car le binaire est déjà conditionné pour l'exécution.

Le programme s'exécutera sur la même architecture sur laquelle nous l'avons construit.

Nous pouvons créer un binaire différent pour une architecture différente en utilisant les variables d'environnement `GOOS` et `GOARCH`, comme ceci :

```go
GOOS=windows GOARCH=amd64 go build hello.go
```

Cela créera un exécutable `hello.exe` pour les machines Windows 64 bits :

![Screen Shot 2022-07-28 at 15.36.55.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_15.36.55.png)
_Exécutable Hello.exe_

La configuration pour macOS 64 bits (Intel ou Apple Silicon) est `GOOS=darwin GOARCH=amd64` et Linux est `GOOS=linux GOARCH=amd64`.

C'est l'une des meilleures fonctionnalités de Go.

## L'espace de travail Go

Une chose spéciale à propos de Go est ce que nous appelons l'**espace de travail**.

L'espace de travail est la « base de départ » pour Go.

Par défaut, Go choisit le chemin `$HOME/go`, donc vous verrez un dossier `go` dans votre répertoire personnel.

Il est d'abord créé lorsque vous installez un package (comme nous le verrons plus tard) mais aussi pour stocker certains outils.

Par exemple, au moment où j'ai chargé le fichier `hello.go` dans VS Code, il m'a invité à installer la commande `[gopls](https://pkg.go.dev/golang.org/x/tools/gopls)`, le débogueur Delve (`dlv`), et le [`staticcheck` linter](https://staticcheck.io/).

Ils ont été automatiquement installés sous `$HOME/go` :

![Screen Shot 2022-07-28 at 12.27.27.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_12.27.27.png)
_`$HOME/go`_

Lorsque vous installez des packages en utilisant `go install`, ils seront stockés ici.

C'est ce que nous appelons **GOPATH**.

Vous pouvez changer la variable d'environnement `GOPATH` pour modifier l'endroit où Go doit installer les packages.

Cela est utile lorsque vous travaillez sur différents projets en même temps et que vous souhaitez isoler les bibliothèques que vous utilisez.

## Plonger dans le langage Go

Maintenant que nous avons les premières notions en place, et que nous avons exécuté notre premier programme Hello, World!, nous pouvons plonger dans le langage.

Le langage n'a pas d'espaces blancs sémantiquement significatifs. C'est comme C, C++, Rust, Java, JavaScript, mais contrairement à Python, où les espaces blancs sont significatifs et sont utilisés pour créer des blocs au lieu d'accolades.

Les points-virgules sont optionnels, comme en JavaScript (contrairement à C, C++, Rust ou Java).

Go prend très au sérieux l'indentation et l'ordre visuel.

Lorsque nous installons Go, nous obtenons également accès à l'outil de ligne de commande `gofmt` que nous pouvons utiliser pour formater les programmes Go. VS Code utilise cela sous le capot pour formater les fichiers sources Go.

C'est très intéressant et innovant car le formatage et les problèmes comme les tabulations vs les espaces ou « devrais-je mettre les accolades sur la même ligne que la définition de la boucle ou sur la ligne suivante » sont une énorme perte de temps.

Les créateurs du langage ont défini les règles, et tout le monde utilise ces règles.

C'est génial pour les projets avec de grandes équipes.

Je vous recommande d'activer dans les paramètres de VS Code « **Format on Save** » et « **Format on Paste** » :

![Screen Shot 2022-07-28 at 14.39.42.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_14.39.42.png)
_Paramètres VS Code pour Go - Format on Paste et Format on Save_

Vous pouvez écrire des commentaires en Go en utilisant la syntaxe habituelle C / C++ / JavaScript / Java :

```go
// ceci est un commentaire de ligne

/*
commentaire
multi
ligne
*/
```

## Variables en Go

L'une des premières choses que vous faites dans un langage de programmation est de définir une variable.

En Go, nous définissons des variables en utilisant `var` :

```go
var age = 20
```

Vous pouvez définir des variables au niveau du package :

```go
package main

import "fmt"

var age = 20

func main() {
	fmt.Println("Hello, World!")
}
```

ou à l'intérieur d'une fonction :

```go
package main

import "fmt"

func main() {
	var age = 20

	fmt.Println("Hello, World!")
}
```

Définie au niveau du package, une variable est visible dans tous les fichiers qui composent le package. Un package peut être composé de plusieurs fichiers, il vous suffit de créer un autre fichier et d'utiliser le même nom de package en haut.

Définie au niveau de la fonction, une variable n'est visible que dans cette fonction. Elle est initialisée lorsque la fonction est appelée, et détruite lorsque la fonction termine l'exécution.

Dans l'exemple, nous avons utilisé :

```go
var age = 20
```

nous attribuons la valeur `20` à `age`.

Cela fait que Go détermine que le **type** de la variable `age` est `int`.

Nous verrons plus de détails sur les types plus tard, mais vous devez savoir qu'il en existe de nombreux différents, commençant par `int`, `string`, et `bool`.

Nous pouvons également déclarer une variable sans valeur existante, mais dans ce cas, nous devons définir le type comme ceci :

```go
var age int
var name string
var done bool
```

Lorsque vous connaissez la valeur, vous utilisez généralement la déclaration de variable courte avec l'opérateur `:=` :

```go
age := 10
name := "Roger"
```

Pour le nom de la variable, vous pouvez utiliser des lettres, des chiffres et le caractère de soulignement `_` tant que le nom commence par un caractère ou `_`.

Les noms sont **sensibles à la casse**.

Si le nom est long, il est courant d'utiliser le camelCase. Donc pour indiquer le nom de la voiture, nous utilisons `carName`.

Vous pouvez attribuer une nouvelle valeur à une variable avec l'opérateur d'affectation `=`

```go
var age int
age = 10
age = 11
```

Si vous avez une variable qui ne change jamais pendant le programme, vous pouvez la déclarer comme une constante en utilisant `const` :

```go
const age = 10
```

Vous pouvez déclarer plusieurs variables sur une seule ligne :

```go
var age, name
```

et les initialiser aussi :

```go
var age, name = 10, "Roger"

//ou

age, name := 10, "Roger"
```

Les variables déclarées qui ne sont pas utilisées dans le programme génèrent une erreur et le programme ne compile pas.

Vous verrez un avertissement dans VS Code :

![Screen Shot 2022-07-28 at 15.45.31.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_15.45.31.png)
_Avertissement pour les variables déclarées non utilisées_

et l'erreur du compilateur :

![Screen Shot 2022-07-28 at 15.45.44.png](https://www.freecodecamp.org/news/content/images/2022/10/Screen_Shot_2022-07-28_at_15.45.44.png)
_Erreur dans le compilateur pour les variables déclarées non utilisées_

Si vous déclarez une variable sans l'initialiser à une valeur, elle se voit attribuer automatiquement une valeur qui dépend du type – par exemple, un entier est `0` et une chaîne est une chaîne vide.

## Types de base en Go

Go est un langage typé.

Nous avons vu comment vous pouvez déclarer une variable, en spécifiant son type :

```go
var age int
```

Ou vous pouvez laisser Go déduire le type de la valeur initiale attribuée :

```go
var age = 10
```

Les types de base en Go sont :

* Entiers (`int`, `int8`, `int16`, `int32`, `rune`, `int64`, `uint`, `uintptr`, `uint8`, `uint16`, `uint64`)
* Flottants (`float32`, `float64`), utiles pour représenter les décimaux
* Types complexes (`complex64`, `complex128`), utiles en mathématiques
* Octet (`byte`), représente un seul caractère ASCII
* Chaînes de caractères (`string`), un ensemble d'`octet`s
* Booléens (`bool`), soit vrai soit faux

Nous avons beaucoup de types différents pour représenter les entiers. Vous utiliserez `int` la plupart du temps, et vous pourriez choisir un type plus spécialisé pour l'optimisation (ce n'est pas quelque chose dont vous devez vous soucier lorsque vous apprenez).

Un type `int` sera par défaut de 64 bits lorsqu'il est utilisé sur un système 64 bits, 32 bits sur un système 32 bits, et ainsi de suite.

`uint` est un `int` qui est non signé, et vous pouvez l'utiliser pour doubler la quantité de valeurs que vous pouvez stocker si vous savez que le nombre ne sera pas négatif.

Tous les types de base ci-dessus sont des **types de valeur**, ce qui signifie qu'ils sont **passés par valeur** aux fonctions lorsqu'ils sont passés en paramètres, ou lorsqu'ils sont retournés par des fonctions.

## Chaînes de caractères en Go

Une chaîne de caractères en Go est une séquence de valeurs `byte`.

Comme nous l'avons vu ci-dessus, vous pouvez définir une chaîne de caractères en utilisant cette syntaxe :

```go
var name = "test"
```

Il est important de noter que contrairement à d'autres langages, les chaînes de caractères sont définies uniquement en utilisant des guillemets doubles, et non des guillemets simples.

Pour obtenir la longueur d'une chaîne de caractères, utilisez la fonction intégrée `len()` :

```go
len(name) //4
```

Vous pouvez accéder à des caractères individuels en utilisant des crochets, en passant l'index du caractère que vous souhaitez obtenir :

```go
name[0] //"t" (les index commencent à 0)
name[1] //"e"
```

Vous pouvez obtenir une portion de la chaîne de caractères en utilisant cette syntaxe :

```go
name[0:2] //"te"
name[:2]  //"te"
name[2:]  //"st"
```

En utilisant cela, vous pouvez créer une copie de la chaîne de caractères en utilisant :

```go
var newstring = name[:]
```

Vous pouvez attribuer une chaîne de caractères à une nouvelle variable comme ceci :

```go
var first = "test"
var second = first
```

Les chaînes de caractères sont **immuables**, donc vous ne pouvez pas mettre à jour la valeur d'une chaîne de caractères.

Même si vous attribuez une nouvelle valeur à `first` en utilisant un opérateur d'affectation, la valeur `second` sera toujours `"test"` :

```go
var first = "test"
var second = first

first = "another test"

first  //"another test"
second //"test"
```

Les chaînes de caractères sont des types de référence, ce qui signifie que si vous passez une chaîne de caractères à une fonction, la **référence** à la chaîne de caractères sera copiée, et non sa valeur. Mais puisque les chaînes de caractères sont immuables, dans ce cas, ce n'est pas une grande différence en pratique avec le passage d'un `int`, par exemple.

Vous pouvez concaténer deux chaînes de caractères en utilisant l'opérateur `+` :

```go
var first = "first"
var second = "second"

var word = first + " " + second  //"first second"
```

Go fournit plusieurs utilitaires de chaînes de caractères dans le package `strings`.

Nous avons déjà vu comment importer un package dans l'exemple "Hello, World!" .

Voici comment vous pouvez importer `strings` :

```go
package main

import (
    "strings"
)
```

Et ensuite vous pouvez l'utiliser.

Par exemple, nous pouvons utiliser la fonction `HasPrefix()` pour voir si une chaîne de caractères commence par une sous-chaîne spécifique :

```go
package main

import (
    "strings"
)

func main() {
    strings.HasPrefix("test", "te") // true
}
```

Vous pouvez trouver la liste complète des méthodes ici : [https://pkg.go.dev/strings](https://pkg.go.dev/strings).

Voici une liste de méthodes que vous pourriez utiliser fréquemment :

* `strings.ToUpper()` retourne une nouvelle chaîne de caractères, en majuscules
* `strings.ToLower()` retourne une nouvelle chaîne de caractères, en minuscules
* `strings.HasSuffix()` vérifie si une chaîne de caractères se termine par une sous-chaîne
* `strings.HasPrefix()` vérifie si une chaîne de caractères commence par une sous-chaîne
* `strings.Contains()` vérifie si une chaîne de caractères contient une sous-chaîne
* `strings.Count()` compte combien de fois une sous-chaîne apparaît dans une chaîne de caractères
* `strings.Join()` utilisé pour joindre plusieurs chaînes de caractères et en créer une nouvelle
* `strings.Split()` utilisé pour créer un tableau de chaînes de caractères à partir d'une chaîne de caractères, en divisant l'originale sur un caractère spécifique, comme une virgule ou un espace
* `strings.ReplaceAll()` utilisé pour remplacer une portion dans une chaîne de caractères et la remplacer par une nouvelle

## Tableaux en Go

Les tableaux sont une séquence d'éléments d'un seul type.

Nous définissons un tableau de cette manière :

```go
var myArray [3]string //un tableau de 3 chaînes de caractères
```

et vous pouvez initialiser le tableau avec des valeurs en utilisant :

```go
var myArray = [3]string{"First", "Second", "Third"}
```

Dans ce cas, vous pouvez également laisser Go faire un peu de travail et compter les éléments pour vous :

```go
var myArray = [...]string{"First", "Second", "Third"}
```

Un tableau ne peut contenir que des valeurs du même type.

Le tableau ne peut pas être redimensionné – vous devez explicitement définir la longueur d'un tableau en Go. Cela fait partie du _type_ d'un tableau. De plus, vous ne pouvez pas utiliser une variable pour définir la longueur du tableau.

En raison de cette limitation, les tableaux sont rarement utilisés directement en Go. Au lieu de cela, nous utilisons des **tranches** (plus sur elles plus tard). Les tranches utilisent des tableaux sous le capot, donc il est toujours nécessaire de savoir comment ils fonctionnent.

Vous pouvez accéder à un élément dans le tableau avec la notation des crochets que nous avons déjà utilisée dans les chaînes de caractères pour accéder à un seul caractère :

```go
myArray[0] //les index commencent à 0
myArray[1]
```

Vous pouvez définir une nouvelle valeur pour une position spécifique dans le tableau :

```go
myArray[2] = "Another"
```

Et vous pouvez obtenir la longueur d'un tableau en utilisant la fonction `len()` :

```go
len(myArray)
```

Les tableaux sont des **types de valeur**. Cela signifie que copier un tableau :

```go
anotherArray := myArray
```

ou passer un tableau à une fonction, ou le retourner depuis une fonction, crée une copie du tableau original.

Cela est différent des autres langages de programmation.

Faisons un exemple simple où nous attribuons une nouvelle valeur à un élément de tableau après l'avoir copié. Voyez, la copie ne change pas :

```go
var myArray = [3]string{"First", "Second", "Third"}
myArrayCopy := myArray
myArray[2] = "Another"

myArray[2]     //"Another"
myArrayCopy[2] //"Third"
```

Rappelez-vous que vous ne pouvez ajouter qu'un seul type d'éléments dans un tableau, donc définir `myArray[2] = 2` par exemple générera une erreur.

Les éléments de bas niveau sont stockés de manière continue en mémoire.

## Tranches en Go

Une tranche est une structure de données similaire à un tableau, mais elle peut changer de taille.

Sous le capot, les tranches utilisent un tableau et elles sont une abstraction construite par-dessus elles qui les rend plus flexibles et utiles (pensez aux tableaux comme étant de plus bas niveau).

Vous utiliserez des tranches de manière très similaire à la façon dont vous utilisez des tableaux dans des langages de plus haut niveau.

Vous définissez une tranche de manière similaire à un tableau, en omettant la longueur :

```go
var mySlice []string //une tranche de chaînes de caractères
```

Vous pouvez initialiser la tranche avec des valeurs :

```go
var mySlice = []string{"First", "Second", "Third"}

//ou

mySlice := []string{"First", "Second", "Third"}
```

Vous pouvez créer une tranche vide d'une longueur spécifique en utilisant la fonction `make()` :

```go
mySlice := make([]string, 3) //une tranche de 3 chaînes de caractères vides
```

Vous pouvez créer une nouvelle tranche à partir d'une tranche existante, en ajoutant un ou plusieurs éléments à celle-ci :

```go
mySlice := []string{"First", "Second", "Third"}

newSlice := append(mySlice, "Fourth", "Fifth")
```

Notez que nous devons attribuer le résultat de `append()` à une nouvelle tranche, sinon nous obtiendrons une erreur de compilation. La tranche originale n'est pas modifiée – nous obtiendrons une toute nouvelle.

Vous pouvez également utiliser la fonction `copy()` pour dupliquer une tranche afin qu'elle ne partage pas la même mémoire que l'autre et soit indépendante :

```go
mySlice := []string{"First", "Second", "Third"}

newSlice := make([]string, 3)

copy(newSlice, mySlice)
```

Si la tranche que vous copiez n'a pas assez d'espace (est plus courte que l'originale), seuls les premiers éléments (jusqu'à ce qu'il y ait de l'espace) seront copiés.

Vous pouvez initialiser une tranche à partir d'un tableau :

```go
myArray := [3]string{"First", "Second", "Third"}

mySlice = myArray[:]
```

Plusieurs tranches peuvent utiliser le même tableau comme tableau sous-jacent :

```go
myArray := [3]string{"First", "Second", "Third"}

mySlice := myArray[:]
mySlice2 := myArray[:]

mySlice[0] = "test"

fmt.Println(mySlice2[0]) //"test"
```

Ces 2 tranches partagent maintenant la même mémoire. Modifier une tranche modifie le tableau sous-jacent et provoque la modification de l'autre tranche générée à partir du tableau, également.

Comme pour les tableaux, chaque élément dans une tranche est stocké en mémoire dans des emplacements mémoire consécutifs.

Si vous savez que vous devez effectuer des opérations sur la tranche, vous pouvez demander qu'elle ait plus de capacité que nécessaire initialement. De cette façon, lorsque vous avez besoin de plus d'espace, l'espace sera immédiatement disponible (au lieu de trouver et de déplacer la tranche vers un nouvel emplacement mémoire avec plus d'espace pour grandir et disposer via le ramasse-miettes de l'ancien emplacement).

Nous pouvons spécifier la **capacité** en ajoutant un troisième paramètre à `make()` :

```go
newSlice := make([]string, 0, 10)
//une tranche vide avec une capacité de 10
```

Comme pour les chaînes de caractères, vous pouvez obtenir une portion d'une tranche en utilisant cette syntaxe :

```go
mySlice := []string{"First", "Second", "Third"}

newSlice := mySlice[:2] //obtenir les 2 premiers éléments
newSlice2 := mySlice[2:] //ignorer les 2 premiers éléments
newSlice3 := mySlice[1:3] //nouvelle tranche avec les éléments en position 1-2
```

## Cartes en Go

Une carte est un type de données très utile en Go.

Dans d'autres langages, elle est également appelée _dictionnaire_ ou _table de hachage_ ou _tableau associatif_.

Voici comment vous créez une carte :

```go
agesMap := make(map[string]int)
```

Vous n'avez pas besoin de définir combien d'éléments la carte contiendra.

Vous pouvez ajouter un nouvel élément à la carte de cette manière :

```go
agesMap["flavio"] = 39
```

Vous pouvez également initialiser la carte avec des valeurs directement en utilisant cette syntaxe :

```go
agesMap := map[string]int{"flavio": 39}
```

Vous pouvez obtenir la valeur associée à une clé en utilisant :

```go
age := agesMap["flavio"]
```

Vous pouvez supprimer un élément de la carte en utilisant la fonction `delete()` de cette manière :

```go
delete(agesMap, "flavio")
```

## Boucles en Go

L'une des meilleures fonctionnalités de Go est de vous donner moins de choix.

Nous avons une seule instruction de boucle : `for`.

Vous pouvez l'utiliser comme ceci :

```go
for i := 0; i < 10; i++ {
	fmt.Println(i)
}
```

Nous initialisons d'abord une variable de boucle, puis nous définissons la _condition_ que nous vérifions à chaque itération pour décider si la boucle doit se terminer. Enfin, nous avons l'_instruction post_, exécutée à la fin de chaque itération, qui dans ce cas incrémente `i`.

`i++` incrémente la variable `i`.

L'opérateur `<` est utilisé pour comparer `i` au nombre `10` et retourne `true` ou `false`, déterminant si le corps de la boucle doit être exécuté ou non.

Nous n'avons pas besoin de parenthèses autour de ce bloc, contrairement à d'autres langages comme C ou JavaScript.

D'autres langages offrent différents types de structures de boucle, mais Go n'a que celle-ci. Nous pouvons simuler une boucle `while`, si vous êtes familier avec un langage qui l'a, comme ceci :

```go
i := 0

for i < 10 {
	fmt.Println(i)
  i++
}
```

Nous pouvons également omettre complètement la condition et utiliser `break` pour terminer la boucle lorsque nous le souhaitons :

```go
i := 0

for {
	fmt.Println(i)

	if i < 10 {
		break
	}

  i++
}
```

J'ai utilisé une instruction `if` à l'intérieur du corps de la boucle, mais nous n'avons pas encore vu les _conditionnelles_ ! Nous le ferons ensuite.

Une chose que je veux introduire maintenant est `range`.

Nous pouvons utiliser `for` pour itérer à travers un tableau en utilisant cette syntaxe :

```go
numbers := []int{1, 2, 3}

for i, num := range numbers {
	fmt.Printf("%d: %d\n", i, num)
}

//0: 1
//1: 2
//2: 3
```

Note : J'ai utilisé `fmt.Printf()` qui nous permet d'imprimer n'importe quelle valeur dans le terminal en utilisant les _verbes_ `%d` qui signifient _entier décimal_ et `\n` signifie ajouter un terminateur de ligne.

Il est courant d'utiliser cette syntaxe lorsque vous n'avez pas besoin d'utiliser l'index :

```go
for _, num := range numbers {
  //...
}
```

Nous utilisons le caractère spécial `_` qui signifie « ignorer ceci » pour éviter que le compilateur Go ne génère une erreur disant « vous n'utilisez pas la variable `i` ! ».

## Conditionnelles en Go

Nous utilisons l'instruction `if` pour exécuter différentes instructions en fonction d'une condition :

```go
if age < 18 {
	//mineur
}
```

La partie `else` est optionnelle :

```go
if age < 18 {
	//mineur
} else {
  //adulte
}
```

et peut être combinée avec d'autres `if` :

```go
if age < 12 {
	//enfant
} else if age < 18  {
  //ado
} else {
	//adulte
}
```

Si vous définissez une variable à l'intérieur du `if`, celle-ci n'est visible qu'à l'intérieur du `if` (même chose pour `else` et partout où vous ouvrez un nouveau bloc avec `{}`).

Si vous allez avoir de nombreuses instructions if différentes pour vérifier une seule condition, il est probablement préférable d'utiliser `switch` :

```go
switch age {
case 0: fmt.Println("Zéro an")
case 1: fmt.Println("Un an")
case 2: fmt.Println("Deux ans")
case 3: fmt.Println("Trois ans")
case 4: fmt.Println("Quatre ans")
default: fmt.Println(i + " ans")
}
```

Comparé à C, JavaScript et autres langages, vous n'avez pas besoin d'avoir un `break` après chaque `case`.

## Opérateurs en Go

Nous avons utilisé certains opérateurs jusqu'à présent dans nos exemples de code, comme `=`, `:=` et `<`.

Parlons un peu plus d'eux.

Nous avons les opérateurs d'affectation `=` et `:=` que nous utilisons pour déclarer et initialiser des variables :

```go
var a = 1

b := 1
```

Nous avons les opérateurs de comparaison `==` et `!=` qui prennent 2 arguments et retournent un booléen :

```go
var num = 1
num == 1 //true
num != 1 //false
```

et `<`, `<=`, `>`, `>=` :

```go
var num = 1
num > 1 //false
num >= 1 //true
num < 1 //false
num <= 1 //true
```

Nous avons les opérateurs arithmétiques binaires (nécessitent deux arguments), comme `+`, `-`, `*`, `/`, `%`.

```go
1 + 1 //2
1 - 1 //0
1 * 2 //2
2 / 2 //1
2 % 2 //0
```

`+` peut également joindre des chaînes de caractères :

```go
"a" + "b" //"ab"
```

Nous avons les opérateurs unaires `++` et `--` pour incrémenter ou décrémenter un nombre :

```go
var num = 1
num++ // num == 2
num-- // num == 1
```

Notez que contrairement à C ou JavaScript, nous ne pouvons pas les préfixer à un nombre comme `++num`. De plus, l'opération ne retourne aucune valeur.

Nous avons les opérateurs booléens qui nous aident à prendre des décisions basées sur les valeurs `true` et `false` : `&&`, `||` et `!` :

```go
true && true  //true
true && false //false
true || false //true
false || false //false
!true  //false
!false //true
```

Ce sont les principaux.

## Structs en Go

Un **struct** est un _type_ qui contient une ou plusieurs variables. C'est comme une collection de variables. Nous les appelons _champs_. Et ils peuvent avoir différents types.

Voici un exemple de définition de struct :

```go
type Person struct {
	Name string
	Age int
}
```

Notez que j'ai utilisé des noms en majuscules pour les champs, sinon ceux-ci seront _privés_ au package. Et lorsque vous passez le struct à une fonction fournie par un autre package, comme celles que nous utilisons pour travailler avec JSON ou une base de données, ces champs ne peuvent pas être accessibles.

Une fois que nous avons défini un struct, nous pouvons initialiser une variable avec ce type :

```go
flavio := Person{"Flavio", 39}
```

et nous pouvons accéder aux champs individuels en utilisant la syntaxe de point :

```go
flavio.Age //39
flavio.Name //"Flavio"
```

Vous pouvez également initialiser une nouvelle variable à partir d'un struct de cette manière :

```go
flavio := Person{Age: 39, Name: "Flavio"}
```

Cela vous permet d'initialiser un seul champ, aussi :

```go
flavio := Person{Age: 39}
```

ou même l'initialiser sans aucune valeur :

```go
flavio := Person{}

//ou

var flavio Person
```

et définir les valeurs plus tard :

```go
flavio.Name = "Flavio"
flavio.Age = 39
```

Les structs sont utiles car vous pouvez regrouper des données non liées et les transmettre à/de fonctions, les stocker dans une tranche, et plus encore.

Une fois défini, un struct est un type comme `int` ou `string` et cela signifie que vous pouvez l'utiliser à l'intérieur d'autres structs, aussi :

```go
type FullName struct {
	FirstName string
	LastName string
}

type Person struct {
	Name FullName
	Age int
}
```

## Fonctions en Go

Une fonction est un bloc de code auquel on assigne un nom et qui contient certaines instructions.

Dans l'exemple "Hello, World!" nous avons créé une fonction `main`, qui est le point d'entrée du programme.

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")
}
```

C'est une fonction spéciale.

Habituellement, nous définissons des fonctions avec un nom personnalisé :

```go
func doSomething() {

}
```

et ensuite vous pouvez les appeler, comme ceci :

```go
doSomething()
```

Une fonction peut accepter des paramètres, et nous devons définir le type des paramètres comme ceci :

```go
func doSomething(a int, b int) {

}

doSomething(1, 2)
```

`a` et `b` sont les noms que nous associons aux paramètres en interne à la fonction.

Une fonction peut retourner une valeur, comme ceci :

```go
func sumTwoNumbers(a int, b int) int {
	return a + b
}

result := sumTwoNumbers(1, 2)
```

Notez que nous avons spécifié le _type_ de la valeur de retour.

Une fonction en Go peut retourner plus d'une valeur :

```go
func performOperations(a int, b int) (int, int) {
	return a + b, a - b
}

sum, diff := performOperations(1, 2)
```

C'est intéressant car de nombreux langages ne permettent qu'une seule valeur de retour.

Toute variable définie à l'intérieur de la fonction est locale à la fonction.

Une fonction peut également accepter un nombre illimité de paramètres, et dans ce cas, nous l'appelons une _fonction variadique_ :

```go
func sumNumbers(numbers ...int) int {
	sum := 0
	for _, number := range numbers {
		sum += number
	}
	return sum
}

total := sumNumbers(1, 2, 3, 4)
```

## Pointeurs en Go

Go supporte les pointeurs.

Supposons que vous avez une variable :

```go
age := 20
```

En utilisant `&age`, vous obtenez le pointeur vers la variable, son adresse mémoire.

Lorsque vous avez le pointeur vers la variable, vous pouvez obtenir la valeur à laquelle il pointe en utilisant l'opérateur `*` :

```go
age := 20
ageptr = &age
agevalue = *ageptr
```

Cela est utile lorsque vous souhaitez appeler une fonction et passer la variable comme paramètre. Go, par défaut, copie la valeur de la variable à l'intérieur de la fonction, donc cela ne changera pas la valeur de `age` :

```go
func increment(a int) {
	a = a + 1
}

func main() {
	age := 20
	increment(age)

	//age est toujours 20
}
```

Vous pouvez utiliser des pointeurs pour cela :

```go
func increment(a *int) {
	*a = *a + 1
}

func main() {
	age := 20
	increment(&age)

	//age est maintenant 21
}
```

## Méthodes en Go

Vous pouvez assigner une fonction à une structure, et dans ce cas, nous l'appelons une _méthode_.

Exemple :

```go
type Person struct {
	Name string
	Age int
}

func (p Person) Speak() {
	fmt.Println("Hello from " + p.Name)
}

func main() {
	flavio := Person{Age: 39, Name: "Flavio"}
	flavio.Speak()
}
```

Vous pouvez déclarer des méthodes pour être des récepteurs de pointeur ou des récepteurs de valeur.

L'exemple ci-dessus montre un récepteur de valeur. Il reçoit une copie de l'instance de la structure.

Ceci serait un récepteur de pointeur qui reçoit le pointeur vers l'instance de la structure :

```go
func (p *Person) Speak() {
	fmt.Println("Hello from " + p.Name)
}
```

## Interfaces en Go

Une interface est un _type_ qui définit une ou plusieurs _signatures de méthode_.

Les méthodes ne sont pas implémentées, juste leur signature : le nom, les types de paramètres et le type de valeur de retour.

Quelque chose comme ceci :

```go
type Speaker interface {
	Speak()
}
```

Maintenant, vous pourriez avoir une fonction accepter n'importe quel type qui implémente toutes les méthodes définies par l'interface :

```go
func SaySomething(s Speaker) {
	s.Speak()
}
```

Et nous pouvons lui passer n'importe quelle structure qui implémente ces méthodes :

```go
type Speaker interface {
	Speak()
}

type Person struct {
	Name string
	Age int
}

func (p Person) Speak() {
	fmt.Println("Hello from " + p.Name)
}

func SaySomething(s Speaker) {
	s.Speak()
}

func main() {
	flavio := Person{Age: 39, Name: "Flavio"}
	SaySomething(flavio)
}
```

## Où aller à partir d'ici

Ce guide est une introduction au langage de programmation Go.

Outre ces bases, il y a beaucoup de choses à apprendre maintenant.

Le ramasse-miettes, la gestion des erreurs, la concurrence et la mise en réseau, les API du système de fichiers, et bien plus encore.

Le ciel est la limite.

Ma suggestion est de choisir un programme que vous souhaitez construire et de simplement commencer, en apprenant les choses dont vous avez besoin en cours de route.

Ce sera amusant et gratifiant.

Note : [vous pouvez obtenir une version PDF et ePub de ce Guide du Débutant en Go ici](https://thevalleyofcode.com/download/go/).