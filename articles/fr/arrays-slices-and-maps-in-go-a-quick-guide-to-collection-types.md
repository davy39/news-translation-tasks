---
title: 'Tableaux, Slices et Maps en Go : un guide rapide des types de collections'
subtitle: ''
author: Gabor Koos
co_authors: []
series: null
date: '2025-09-05T16:40:48.856Z'
originalURL: https://freecodecamp.org/news/arrays-slices-and-maps-in-go-a-quick-guide-to-collection-types
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757090426408/327ded41-5020-4f83-afa2-334f15569998.png
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
- name: data structures
  slug: data-structures
seo_title: 'Tableaux, Slices et Maps en Go : un guide rapide des types de collections'
seo_desc: 'Golang has a reputation for simplicity, and one reason is its small set
  of core data structures. Unlike some languages that offer lists, vectors, dictionaries,
  hashmaps, tuples, sets, and more, Go keeps things minimal.

  The three fundamental building ...'
---

Golang a la réputation d'être simple, et l'une des raisons est son petit ensemble de structures de données de base. Contrairement à certains langages qui proposent des listes, des vecteurs, des dictionnaires, des hashmaps, des tuples, des ensembles, et plus encore, Go reste minimaliste.

Les trois blocs de construction fondamentaux que vous utiliserez quotidiennement sont :

* **Tableaux (Arrays)** : séquences d'éléments de taille fixe.
    
* **Slices** : vues flexibles et dynamiques de tableaux.
    
* **Maps** : magasins de clés-valeurs implémentés sous forme de tables de hachage.
    

Avec ces trois éléments, vous pouvez représenter presque n'importe quelle collection de données dont vous avez besoin.

Dans ce tutoriel, vous apprendrez à utiliser les tableaux, les slices et les maps de manière efficace. Vous jetterez également un œil sous le capot pour voir comment Go les représente en mémoire. Cela vous aidera à comprendre leurs caractéristiques de performance et à éviter les pièges courants.

À la fin, vous serez capable de :

* Choisir le bon type de données pour votre problème.
    
* Écrire du code Go idiomatique pour les collections.
    
* Comprendre comment ces types se comportent en interne.
    
* Construire un petit projet combinant tableaux, slices et maps.
    

Plongeons dans le vif du sujet !

### Ce que nous allons couvrir :

1. [Prérequis](#heading-pre-requis)
    
2. [Les Tableaux en Go](#heading-les-tableaux-en-go)
    
    * [Initialisation avec des valeurs](#heading-initialisation-avec-des-valeurs)
        
    * [Taille des tableaux](#heading-taille-des-tableaux)
        
    * [Représentation interne des tableaux](#heading-representation-interne-des-tableaux)
        
    * [Tableaux multidimensionnels](#heading-tableaux-multidimensionnels)
        
    * [Limitations](#heading-limitations)
        
    * [Quand les tableaux sont utiles](#heading-quand-les-tableaux-sont-utiles)
        
3. [Les Slices en Go](#heading-les-slices-en-go)
    
    * [Quand utiliser les slices ?](#heading-quand-utiliser-les-slices)
        
    * [Comment déclarer une slice](#heading-comment-declarer-une-slice)
        
    * [Allocation (avec make)](#heading-allocation-avec-make)
        
    * [Ajouter des éléments](#heading-ajouter-des-elements)
        
    * [Comment découper des slices](#heading-comment-decouper-des-slices)
        
    * [Représentation interne des slices](#heading-representation-interne-des-slices)
        
    * [Comment copier des slices](#heading-comment-copier-des-slices)
        
    * [Slices multidimensionnelles](#heading-slices-multidimensionnelles)
        
    * [Slices vs Tableaux](#heading-slices-vs-tableaux)
        
4. [Les Maps en Go](#heading-les-maps-en-go)
    
    * [Comment déclarer une map](#heading-comment-declarer-une-map)
        
    * [Comment accéder aux valeurs](#heading-comment-acceder-aux-valeurs)
        
    * [Comment itérer sur une map](#heading-comment-iterer-sur-une-map)
        
    * [Représentation interne des maps](#heading-representation-interne-des-maps)
        
    * [Tableaux vs Slices vs Maps](#heading-tableaux-vs-slices-vs-maps)
        
5. [Mini Projet : Totaux du panier d'achat](#heading-mini-projet-totaux-du-panier)
    
6. [Défi pratique](#heading-defi-pratique)
    
7. [Conclusion](#heading-conclusion)
    
    * [Solution du défi pratique](#heading-solution-du-defi-pratique)
        

## Prérequis

Ce tutoriel est conçu pour les lecteurs qui ont déjà une certaine expérience de base avec Go. Vous n'avez pas besoin d'être un expert, mais vous devriez être à l'aise avec :

* L'écriture et l'exécution de programmes Go simples (`go run`, `go build`).
    
* La déclaration et l'utilisation de variables, de fonctions et de types de base (par exemple, `int`, `string`, `bool`).
    
* La compréhension des structures de contrôle comme `if`, `for`, et `range`.
    
* L'utilisation de la chaîne d'outils Go et de `go mod init` pour configurer un projet.
    

Si vous avez terminé le [Tour of Go](https://go.dev/tour) ou écrit quelques petits programmes en Go, vous serez prêt à suivre – nous couvrirons les aspects internes à un niveau accessible aux débutants.

## Les Tableaux en Go

Un tableau est une séquence numérotée d'éléments du même type avec une longueur fixe. Voici un exemple en Go :

```go
package main

import "fmt"

func main() {
    var nums [3]int // tableau de 3 entiers
    fmt.Println(nums) // [0 0 0]
}
```

Ce code déclare un tableau avec de l'espace pour exactement trois valeurs `int`. Les tableaux Go sont indexés à partir de zéro, ce qui signifie que le premier élément est à l'index 0. Les éléments, comme chaque variable Go, sont initialisés à la valeur zéro de leur type (0 pour les entiers, "" pour les chaînes de caractères, etc.).

Une fois le tableau créé, vous pouvez accéder à ses éléments en utilisant leur index comme ceci :

```go
package main

import "fmt"

func main() {
    var nums [3]int // tableau de 3 entiers
    nums[1] = 2
    fmt.Println(nums[1]) // 2
    fmt.Println(nums) // [0 2 0]
}
```

### Initialisation avec des valeurs

Jusqu'à présent, nous avons vu que les tableaux sont créés avec leurs éléments définis sur la valeur zéro du type d'élément. Mais souvent, vous voudrez donner à un tableau des valeurs de départ spécifiques dès que vous le déclarez. Ce processus est appelé **initialisation** : vous fournissez les valeurs dans une liste, et Go remplit le tableau dans l'ordre.

```go
package main

import "fmt"

func main() {
    nums := [3]int{1, 2, 3} // tableau de 3 entiers
    fmt.Println(nums) // [1 2 3]
}
```

Si vous omettez la taille lors de l'initialisation d'un tableau, Go l'inférera à partir du nombre d'éléments que vous fournissez :

```go
package main

import "fmt"

func main() {
    nums := [...]int{1, 2, 3} // tableau de 3 entiers
    fmt.Println(nums) // [1 2 3]
}
```

Si vous spécifiez la taille explicitement, le compilateur appliquera cette taille :

```go
package main

import "fmt"

func main() {
    nums := [3]int{1, 2} // tableau de 3 entiers
    fmt.Println(nums) // [1 2 0]
}
```

### Taille des tableaux

En Go, la taille d'un tableau fait partie de son type. `[3]int` et `[4]int` sont considérés comme des types complètement différents, même s'ils contiennent tous deux des entiers (vous ne pouvez pas affecter un `[4]int` à un `[3]int`, ni même les comparer directement, car leurs longueurs ne correspondent pas) :

```go
package main

import "fmt"

func main() {
    var a [3]int
    var b [4]int
    fmt.Println(a == b) // erreur de compilation
}
```

Lorsque vous utilisez `[...]` dans un littéral de tableau, Go compte combien d'éléments vous avez fournis et cela sera la longueur. La longueur d'un tableau est fixe et ne peut pas être modifiée par la suite.

Vous pouvez récupérer la longueur d'un tableau en utilisant la fonction intégrée `len` :

```go
package main

import "fmt"

func main() {
    nums := [3]int{1, 2, 3}
    fmt.Println(len(nums)) // 3
}
```

### Représentation interne des tableaux

En Go, les tableaux sont représentés comme des blocs contigus de mémoire. Cela signifie que les éléments d'un tableau sont stockés les uns après les autres en mémoire, ce qui facilite le calcul de l'adresse de n'importe quel élément en fonction de son index.

Par exemple, considérons le tableau suivant :

```go
package main

import "fmt"

func main() {
    nums := [3]int32{1, 2, 3} // tableau de 3 entiers 32 bits
    fmt.Println(&nums[0]) // adresse du premier élément
    fmt.Println(&nums[1]) // adresse du deuxième élément
    fmt.Println(&nums[2]) // adresse du troisième élément
}
```

Cela vous donnera quelque chose comme ceci :

```plaintext
0xc00000a0f0
0xc00000a0f4
0xc00000a0f8
```

32 bits font 4 octets, donc les adresses des éléments diffèrent également de 4 octets.

Dans l'exemple ci-dessus, nous avons utilisé `&nums[0]` pour obtenir l'adresse du premier élément. Vous pourriez vous demander ce qui se passe si vous prenez l'adresse du tableau lui-même, en utilisant `&nums` :

```go
fmt.Println(&nums)
```

À première vue, vous pourriez vous attendre à ce que cela donne le même résultat que `&nums[0]`, comme en C où les tableaux se « décomposent » souvent en pointeurs. Mais Go est différent :

* `&nums` est un pointeur vers le **tableau entier** (type `*[3]int32`).
    
* `&nums[0]` est un pointeur vers le **premier élément** (type `*int32`).
    

Lorsque vous imprimez `&nums`, le package `fmt` le reconnaît comme un pointeur vers un tableau et affiche le contenu du tableau (`&[1 2 3]`) plutôt qu'une adresse mémoire brute.

En Go, les tableaux et les pointeurs vers des tableaux sont des types distincts, et `&nums` est de type `*[3]int32`, pas `*int32`. Si vous voulez l'adresse du premier élément, vous utilisez `&nums[0]`.

Si vous essayez d'accéder à un index hors limites, votre programme paniquera au moment de l'exécution avec une erreur :

```go
package main

import "fmt"

func main() {
    nums := [3]int32{1, 2, 3}
		i := 4
    fmt.Println(&nums[i])
}
```

```plaintext
panic: runtime error: index out of range [4] with length 3

goroutine 1 [running]:
main.main()
        C:/projects/Articles/Go Context/main.go:8 +0x3d
exit status 2
```

Ce comportement est appelé **bounds checking** (vérification des bornes) : avant que Go ne lise ou n'écrive un élément de tableau, il s'assure que l'index se trouve dans la plage valide (`0` jusqu'à `len(array)-1`). Si ce n'est pas le cas, le programme panique immédiatement au lieu de vous laisser accéder à une mémoire qui n'appartient pas au tableau.

La vérification des bornes est importante car elle :

* Prévient la corruption de mémoire : dans des langages comme C, un accès hors limites peut écraser de la mémoire non liée et causer des bogues difficiles à trouver ou des problèmes de sécurité.
    
* Rend les programmes plus sûrs par défaut : Go arrêtera l'exécution immédiatement plutôt que de laisser un accès mémoire invalide se poursuivre silencieusement.
    
* Aide au débogage : le message de panique indique clairement l'index invalide et la longueur du tableau, afin que vous puissiez rapidement remonter jusqu'au bogue.
    
* Elle échange un petit coût d'exécution contre une sécurité et une fiabilité bien plus grandes.
    

Comme toute autre structure de données en Go, les tableaux sont passés par valeur, ce qui signifie que lorsque vous passez un tableau à une fonction, une copie est faite. Cela peut entraîner des problèmes de performance, donc pour les grands tableaux, il est souvent préférable de passer un pointeur vers le tableau à la place.

### Tableaux multidimensionnels

Les tableaux multidimensionnels vous permettent de modéliser des données qui s'insèrent naturellement dans des lignes et des colonnes (ou des dimensions supérieures). Voici quelques utilisations courantes :

* Matrices et grilles
    
* Images et données de pixels en 2D ou 3D
    
* Tables de recherche statiques
    

Go prend en charge les tableaux multidimensionnels, qui sont essentiellement des tableaux de tableaux. Voici un exemple :

```go
package main

import "fmt"

func main() {
    var matrix [2][3]int // matrice 2x3
    matrix[0][0] = 1
    matrix[0][1] = 2
    matrix[0][2] = 3
    matrix[1][0] = 4
    matrix[1][1] = 5
    matrix[1][2] = 6
    fmt.Println(matrix)
}
```

Dans cet exemple, nous créons une matrice 2x3 (2 lignes et 3 colonnes) et initialisons ses éléments. Vous pouvez accéder aux éléments en utilisant deux indices : le premier pour la ligne et le second pour la colonne. Cela peut être étendu à plus de dimensions également, mais la taille de chaque dimension doit être connue au moment de la compilation.

### Limitations

La plus grande limitation des tableaux en Golang est que leur taille doit être connue au moment de la compilation. Une fois déclaré, la taille ne peut pas être modifiée. En raison de cette rigidité, les tableaux sont rarement utilisés directement.

### Quand les tableaux sont utiles

Malgré leur rigidité, les tableaux ont quelques cas d'utilisation de niche mais importants en Go :

* Données de taille fixe comme les adresses IP
    
* Structures de données de bas niveau
    
* Interopérabilité avec C ou appels système
    

## Les Slices en Go

Parce que les tableaux sont de taille fixe, Go a introduit les **slices** : des séquences flexibles et dynamiques construites au-dessus des tableaux. Considérez les slices comme des vues sur des tableaux. Une slice conserve trois éléments :

1. **Pointeur** : Une référence au tableau sous-jacent.
    
2. **Longueur (Length)** : Le nombre d'éléments dans la slice.
    
3. **Capacité (Capacity)** : Le nombre maximum d'éléments que la slice peut contenir (qui est toujours supérieur ou égal à la longueur).
    

Contrairement aux tableaux, la longueur et la capacité d'une slice peuvent changer dynamiquement à mesure que vous ajoutez ou supprimez des éléments.

### Quand utiliser les slices ?

En pratique, les slices sont le moyen par défaut de travailler avec des collections en Go. Vous les utiliserez quand :

* Vous ne connaissez pas la taille de la collection à l'avance.
    
* Vous avez besoin de faire croître ou de réduire la collection au fil du temps.
    
* Vous voulez passer des sous-sections d'un tableau sans copier les données.
    
* Vous voulez du code Go idiomatique (la plupart des API Go acceptent et renvoient des slices, pas des tableaux).
    

Les tableaux sont principalement utiles lorsque vous avez besoin d'une taille fixe connue à la compilation (comme un UUID de 16 octets). Pour presque tout le reste, les slices sont le choix de prédilection.

### Comment déclarer une slice

```go
var s []int           // slice d'entiers
fmt.Println(s)        // []
fmt.Println(len(s))   // longueur : 0
fmt.Println(cap(s))   // capacité : 0
```

Avec `var s []int`, vous **déclarez une slice**. Cela signifie que vous avez introduit une variable `s` de type « slice de int » (`[]int`), mais vous ne lui avez pas encore donné de tableau de support. À ce stade, `s` est `nil` – il ne pointe vers aucun stockage réel. C'est pourquoi sa longueur et sa capacité sont toutes deux nulles, jusqu'à ce que vous lui allouiez de l'espace ou que vous y ajoutiez des éléments.

Notez que vous pouvez également déclarer une slice en utilisant `var s[]int{}` qui initialise la slice avec zéro élément, mais vous ne pouvez pas créer un tableau vide en utilisant cette syntaxe : `var s[...]int{}`. Cette dernière est invalide en Go : vous ne pouvez pas utiliser `[...]` avec `var` et un initialisateur vide !

### Allocation (avec `make`)

```go
s := make([]int, 3) // longueur 3, capacité 3
fmt.Println(s)      // [0 0 0]
```

Ici, Go crée un tableau sous-jacent de taille 3 et fait pointer `s` vers celui-ci. Maintenant, `s` a une longueur de 3 et une capacité de 3.

Vous pouvez également spécifier une capacité plus grande :

```go
s := make([]int, 3, 5) // longueur 3, capacité 5
fmt.Println(s)         // [0 0 0]
fmt.Println(len(s))    // longueur : 3
fmt.Println(cap(s))    // capacité : 5
```

La fonction intégrée `make` est la manière de Go d'allouer et d'initialiser certains types composites : les slices, les maps et les channels. Contrairement à `new`, qui vous donne un pointeur vers une valeur mise à zéro, `make` configure les structures de données internes dont ces types ont besoin pour fonctionner.

Pour les slices, `make` fait trois choses sous le capot :

1. Alloue un tableau de la taille donnée (soit la longueur que vous spécifiez, soit la capacité si vous fournissez les deux).
    
2. Crée un en-tête de slice (pointeur, longueur, capacité) qui pointe vers ce tableau.
    
3. Renvoie l'en-tête de la slice, prêt à l'emploi.
    

### Ajouter des éléments

L'une des principales raisons pour lesquelles les slices sont si utiles par rapport aux tableaux est qu'elles peuvent croître dynamiquement. En pratique, vous commencerez souvent avec une slice d'une certaine longueur, puis vous devrez ajouter plus d'éléments plus tard. Encore une fois, c'est quelque chose que les tableaux ne permettent pas.

Go fournit la fonction intégrée `append` pour cela. `append` prend une slice existante et un ou plusieurs nouveaux éléments, et renvoie une nouvelle slice avec ces éléments ajoutés :

```go
s := make([]int, 3, 5)  // crée [0 0 0]
s = append(s, 1)
s = append(s, 2, 3)
fmt.Println(s)          // [0 0 0 1 2 3]
fmt.Println(len(s))     // longueur : 6
fmt.Println(cap(s))     // capacité : 10 - peut différer selon la version de Go, mais généralement elle double en cas de dépassement
```

S'il y a assez de capacité, `append` écrit simplement dans le tableau existant. Sinon, Go alloue automatiquement un nouveau tableau plus grand, copie les anciens éléments et ajoute la nouvelle valeur. C'est pourquoi une slice peut croître même si les tableaux eux-mêmes sont de taille fixe. D'un côté, cela offre de la flexibilité, mais cela peut également entraîner une surcharge de performance due au besoin d'allocation mémoire et de copie.

Pour atténuer cela, il est de bonne pratique de pré-allouer des slices avec une capacité appropriée lorsque vous connaissez la taille à l'avance.

### Comment découper des slices

En Golang, vous pouvez créer une nouvelle slice en découpant une slice existante. Vous pouvez le faire en utilisant l'opérateur `[:]`. La syntaxe est `slice[bas:haut]`, où `bas` est l'index de départ (inclus) et `haut` est l'index de fin (exclus). Si `bas` est omis, il vaut 0 par défaut. Si `haut` est omis, il vaut par défaut la longueur de la slice :

```go
s := []int{1, 2, 3, 4, 5}
s1 := s[1:4] // [2 3 4]
s2 := s[:3]  // [1 2 3]
s3 := s[2:]  // [3 4 5]
fmt.Println(s1, s2, s3)
```

Si deux slices partagent le même tableau sous-jacent, les modifications apportées aux éléments d'une slice seront reflétées dans l'autre. C'est parce que les deux slices pointent vers les mêmes données en mémoire. Par exemple :

```go
s := []int{1, 2, 3, 4, 5}
s1 := s[1:4] // [2 3 4]
s2 := s[2:]  // [3 4 5]
s1[0] = 10
fmt.Println(s)   // [1 10 3 4 5]
fmt.Println(s2)  // [10 3 4 5]
```

### Représentation interne des slices

En interne, une slice est représentée par une structure qui contient un pointeur vers le tableau sous-jacent, la longueur de la slice et sa capacité :

```go
type slice struct {
    ptr *ElementType  // pointeur vers le tableau sous-jacent
    len int
    cap int
}
```

Cela permet aux slices d'être légères et efficaces, car elles ne nécessitent pas de copier tout le tableau lors de leur passage d'une fonction à l'autre, seulement le pointeur vers le tableau (ainsi que la longueur et la capacité). C'est souvent une source de confusion : passer une slice à une fonction *donne l'impression* de passer par référence, car les valeurs ne sont pas copiées – mais la structure de la slice elle-même est toujours passée par valeur :

```go
package main

import "fmt"

func modify(s1 [3]int, s2 []int) {
    s1[0] = 99
    s2[0] = 99
}

func main() {
    nums_array := [...]int{1, 2, 3} // tableau de 3 entiers
    nums_slice := []int{1, 2, 3}    // slice de 3 entiers
    modify(nums_array, nums_slice)
    fmt.Println(nums_array)         // Sortie : [1 2 3] - seulement la copie a été modifiée
    fmt.Println(nums_slice)         // Sortie : [99 2 3] - la valeur dans la slice originale a été modifiée
}
```

### Comment copier des slices

Copier une slice crée une nouvelle slice avec les mêmes éléments. Vous pouvez le faire en utilisant la fonction intégrée `copy` :

```go
s1 := []int{1, 2, 3}
s2 := make([]int, len(s1))
copy(s2, s1)      // copie les éléments de s1 vers s2
fmt.Println(s2)   // [1 2 3]
```

Pièges courants lors de la copie de slices :

* **Capacité** : Lors de la copie d'une slice, la capacité de la slice de destination n'est pas automatiquement ajustée. Si la slice de destination a une capacité inférieure à la slice source, elle ne copiera que jusqu'à la capacité de la destination.
    
* **Slices Nil** : Si la slice source est nil, la fonction `copy` ne paniquera pas, mais la slice de destination restera inchangée.
    
* **Slices qui se chevauchent** : Si les slices source et destination se chevauchent, le comportement est indéfini. Pour éviter cela, assurez-vous de copier vers une slice distincte.
    

### Slices multidimensionnelles

Tout comme les tableaux multidimensionnels, vous pouvez créer des slices multidimensionnelles, qui sont essentiellement des slices de slices :

```go
matrix := [][]int{
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
}
fmt.Println(matrix)
```

Ou :

```go
rows := 3
cols := 4
matrix := make([][]int, rows)
for i := range matrix {
    matrix[i] = make([]int, cols)
}
```

Les slices multidimensionnelles sont utiles lorsque vous avez besoin de grilles de données flexibles et dynamiques. Les cas d'utilisation courants incluent :

* La représentation de plateaux de jeu (par exemple, Morpion, Démineur). Cela pourrait aussi être fait avec un tableau.
    
* Les matrices mathématiques dont la taille n'est pas fixe.
    
* Les tableaux irréguliers (jagged arrays), où chaque ligne peut avoir une longueur différente.
    

Parce que les slices peuvent s'agrandir et rétrécir, elles sont généralement préférées aux tableaux multidimensionnels, sauf si vous avez besoin d'une taille fixe connue à la compilation.

### Slices vs Tableaux

Récapitulons les principales différences entre les slices et les tableaux en Go :

1. **Taille** : Les tableaux ont une taille fixe, tandis que les slices peuvent croître et rétrécir dynamiquement.
    
2. **Mémoire** : Les tableaux sont des types de valeur et sont copiés lors du passage aux fonctions, tandis que les slices sont des types de référence et seul l'en-tête de la slice est copié.
    
3. **Flexibilité** : Les slices offrent plus de flexibilité et sont généralement préférées aux tableaux pour la plupart des cas d'utilisation.
    

## Les Maps en Go

Une **map** est le type de données associatif intégré de Go (table de hachage). Elle stocke des paires clé-valeur avec des recherches rapides en temps moyen.

Contrairement aux tableaux et aux slices, qui ne sont indexés que par des entiers, les maps vous permettent d'utiliser des clés plus significatives telles que des noms, des identifiants ou d'autres valeurs comparables. Cela les rend idéales lorsque vous devez rechercher, grouper ou compter des données rapidement, par exemple, stocker les âges des utilisateurs par nom d'utilisateur, compter les fréquences de mots dans un texte ou mapper des ID de produits à leurs prix.

### Comment déclarer une map

```go
m := make(map[string]int)  // une map avec des clés string et des valeurs int
m["alice"] = 23
m["bob"] = 30
fmt.Println(m)             // map[alice:23 bob:30]
```

Ici, nous créons une map avec des clés de type string et des valeurs de type int. Nous pouvons ajouter des paires clé-valeur à la map en utilisant la syntaxe `m[clé] = valeur`. La fonction `make` est utilisée pour initialiser la map.

Les clés peuvent être de n'importe quel type comparable (par exemple, des chaînes, des entiers, des structs). Mais elles ne peuvent pas être des slices, des maps ou des fonctions.

Une clé dans une map doit être unique. Si vous affectez une valeur à une clé existante, elle écrasera la valeur précédente.

### Comment accéder aux valeurs

Une fois que vous avez une map, vous pouvez récupérer une valeur en utilisant sa clé avec la syntaxe `map[clé]` :

```go
age := m["alice"]
fmt.Println(age) // 23
```

Si la clé n'existe pas, vous obtenez la valeur zéro :

```go
age := m["charlie"]
fmt.Println(age) // 0
```

Voici ce qui se passe sous le capot :

1. Go calcule le hachage de la clé (`"alice"`) pour trouver dans quel bucket de la table de hachage chercher. Un **bucket** est un petit conteneur à l'intérieur de la table de hachage qui contient une ou plusieurs paires clé-valeur.
    
2. Il recherche la clé dans le bucket.
    
3. Si la clé existe, Go renvoie la valeur associée (`23` dans ce cas).
    
4. Si la clé n'existe pas, Go renvoie la valeur zéro du type de valeur de la map (`0` pour `int`, `""` pour `string`, `nil` pour un pointeur ou une slice, etc.).
    

Pour distinguer entre une **clé qui n'existe pas** et une clé dont la valeur se trouve être la valeur zéro, Go fournit une seconde valeur de retour lorsque vous accédez à une map. Normalement, `m[clé]` renvoie simplement la valeur. Mais si vous écrivez :

```go
value, ok := m[key]
```

* `value` est la valeur de la map pour cette clé (ou la valeur zéro si la clé est absente).
    
* `ok` est un booléen qui est `true` si la clé existe dans la map, et `false` sinon.
    

C'est indispensable car certains types ont une valeur zéro qui est valide dans votre application. Par exemple, considérons une map de noms d'utilisateurs vers des âges :

```go
m := map[string]int{
    "alice": 23,
    "bob":   0,
}
```

Si vous essayez d'accéder à `"bob"` ou `"charlie"` sans la seconde valeur de retour :

```go
fmt.Println(m["bob"])     // 0
fmt.Println(m["charlie"]) // 0
```

Les deux affichent `0`, vous ne pouvez donc pas dire si `"charlie"` est manquant ou si `"bob"` a réellement l'âge `0`. L'utilisation de la seconde valeur de retour résout ce problème :

```go
age, ok := m["charlie"]
if !ok {
    fmt.Println("Clé non trouvée")
}
```

Ici, `ok` est `false` pour `"charlie"` mais serait `true` pour `"bob"`. C'est un modèle courant en Go pour gérer en toute sécurité les recherches dans les maps.

### Comment itérer sur une map

Itérer sur une map signifie parcourir toutes les paires clé-valeur de la map, une par une. Vous le faites avec une boucle `for` et le mot-clé `range` :

```go
for key, value := range m {
    fmt.Printf("%s: %d\n", key, value)
}
```

Ce qui se passe ici :

* `range m` produit chaque clé de la map, une par une.
    
* La boucle affecte la clé actuelle à `key` et la valeur correspondante à `value`.
    
* À l'intérieur de la boucle, vous pouvez utiliser `key` et `value` pour traiter, imprimer ou modifier les données.
    

**Note importante :** L'ordre d'itération des maps en Go est aléatoire : chaque boucle peut produire les clés dans un ordre différent. Cela vous empêche de vous fier à l'ordre d'insertion. Si vous avez besoin d'un ordre déterministe, vous pouvez collecter les clés dans une slice, les trier et itérer sur les clés triées.

### Représentation interne des maps

Les maps Go sont implémentées sous forme de tables de hachage avec des buckets :

* Les clés sont hachées pour décider dans quel bucket elles vont.
    
* Chaque bucket contient plusieurs paires clé-valeur.
    
* Lorsqu'un bucket est trop plein, Go le divise en deux (similaire au redimensionnement dynamique).
    
* C'est pourquoi les opérations sur les maps sont généralement en O(1), mais pas garanties en temps constant.
    

Gardez à l'esprit que les maps ne sont pas sûres pour les écritures concurrentes. Si plusieurs goroutines écrivent dans une map en même temps, vous obtiendrez une panique à l'exécution. Utilisez `sync.Mutex` ou `sync.RWMutex` pour protéger l'accès aux maps dans les scénarios concurrents.

Si vous êtes intéressé par le fonctionnement interne des différentes implémentations de tables de hachage, consultez mon [article sur l'analyse approfondie des Hash Maps](https://blog.gaborkoos.com/posts/2025-08-03-Hash-Map-Deep-Dive/).

### Tableaux vs. Slices vs. Maps

Voici une comparaison rapide des fonctionnalités des types de collections en Go :

| Fonctionnalité | Tableaux | Slices | Maps |
| --- | --- | --- | --- |
| Taille | Fixe | Dynamique | Dynamique |
| Type | Type de valeur | Type de référence | Type de référence |
| Valeur zéro | Tableau de valeurs zéro | Slice Nil | Map Nil |
| Longueur | Connue à la compilation | Connue à l'exécution | N/A |
| Indexation | Par entier | Par entier | Par clé |
| Rép. interne | Bloc mémoire contigu | En-tête (ptr, len, cap) + tableau | Table de hachage avec buckets |
| Cas d'utilisation | Données bas niveau, taille fixe | La plupart des listes, séquences | Recherches, dictionnaires |

## Mini Projet : Totaux du panier d'achat

Combinons les slices et les maps dans un programme pratique : étant donné une liste d'articles et leurs prix, calculons le coût total de tous les articles.

La liste des articles est représentée sous forme de slice de chaînes de caractères, et les prix sont stockés dans une map. La clé est le nom de l'article, et la valeur est le prix :

```go
package main

import "fmt"

func main() {
	items := []string{"pomme", "banane", "orange"}
	prices := map[string]float64{
		"pomme":  0.99,
		"banane": 0.59,
		"orange": 0.79,
	}

	var total float64
	for _, item := range items {
		total += prices[item]
	}
	fmt.Printf("Coût total : $%.2f\n", total)
}
```

```plaintext
Coût total : $2.37
```

Ce court exemple montre la synergie entre les slices (pour contenir les noms des articles) et les maps (pour rechercher les prix).

## Défi pratique

Écrivez une fonction qui prend une slice d'entiers et renvoie une nouvelle slice avec les doublons supprimés. (Solution ci-dessous.)

## Conclusion

Go reste simple : avec les tableaux, les slices et les maps, vous pouvez modéliser presque tous les problèmes de données quotidiens.

* **Tableaux** : taille fixe, mémoire contiguë, rarement utilisés directement.
    
* **Slices** : flexibles, construites sur des tableaux, votre outil de prédilection pour les collections ordonnées.
    
* **Maps** : tables de hachage pour les recherches clé-valeur.
    

Vous avez maintenant les outils pour manipuler les collections en Go en toute confiance. La prochaine étape ? Essayez d'écrire un petit projet où vous lisez des données d'un fichier, les stockez dans des slices et les traitez dans des maps pour des recherches rapides. C'est ainsi que les développeurs Go gèrent les données du monde réel.

### Solution du défi pratique

Pour supprimer les doublons d'une slice, nous pouvons suivre les valeurs que nous avons déjà vues dans une map et construire une nouvelle slice contenant uniquement la première occurrence de chaque élément :

```go
package main

import "fmt"

func removeDuplicates(intSlice []int) []int {
	seen := make(map[int]bool) // pour suivre les entiers déjà vus
	result := []int{}
	for _, v := range intSlice {
		if !seen[v] { // si nous n'avons pas encore vu cet entier, on le marque et on l'ajoute au résultat
			seen[v] = true
			result = append(result, v)
		}
	}
	return result
}

func main() {
	s := []int{1, 2, 2, 3, 4, 4, 5}
	s = removeDuplicates(s)
	fmt.Println(s) // [1 2 3 4 5]
}
```

Comment ça marche :

* `seen` garde la trace des nombres qui ont déjà été ajoutés.
    
* `result` collecte les nombres uniques au fur et à mesure que nous itérons.
    
* Pour chaque élément de la slice d'entrée, s'il n'a pas été vu, nous le marquons et l'ajoutons à `result`.
    
* Enfin, `result` ne contient que des valeurs uniques.