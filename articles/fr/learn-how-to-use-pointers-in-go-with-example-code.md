---
title: Apprenez à utiliser les pointeurs en Go – Avec des exemples de code
subtitle: ''
author: Gabor Koos
co_authors: []
series: null
date: '2025-10-06T15:04:41.333Z'
originalURL: https://freecodecamp.org/news/learn-how-to-use-pointers-in-go-with-example-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759763060124/8b3f21fa-052e-4c18-a1b4-9fe4fd456830.png
tags:
- name: Go Language
  slug: go
- name: pointers
  slug: pointers
seo_title: Apprenez à utiliser les pointeurs en Go – Avec des exemples de code
seo_desc: 'Pointers are a fundamental but often dreaded concept in every programming
  language that supports them. Luckily for us, Go makes working with pointers straightforward
  and safe.

  In this article, we will demystify pointers in Go. You''ll learn:


  What poi...'
---

Les pointeurs sont un concept fondamental mais souvent redouté dans chaque langage de programmation qui les supporte. Heureusement pour nous, Go rend le travail avec les pointeurs simple et sûr.

Dans cet article, nous allons démystifier les pointeurs en Go. Vous apprendrez :

* Ce que sont les pointeurs et comment les utiliser
    
* Comment déclarer des pointeurs et les déréférencer
    
* Les pièges courants, comme les pointeurs nil et les types de référence
    
* Les récepteurs de pointeur dans les structs (une raison clé pour laquelle les pointeurs sont si utiles en Go)
    
* Un aperçu bonus des pointeurs faibles (Go 1.24+) pour la gestion avancée de la mémoire
    

À la fin, vous aurez une solide compréhension des pointeurs et serez confiant pour les utiliser dans vos propres programmes Go.

## Ce que nous allons couvrir :

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce qu'un pointeur ?](#heading-qu-est-ce-qu-un-pointeur)
    
    * [Comprendre la mémoire](#heading-comprendre-la-memoire)
        
    * [Pile vs Tas (Stack vs Heap)](#heading-pile-vs-tas)
        
    * [Le pointeur](#heading-le-pointeur)
        
* [Déclarer et utiliser des pointeurs](#heading-declarer-et-utiliser-des-pointeurs)
    
    * [Pointeurs vers des types de base](#heading-pointeurs-vers-des-types-de-base)
        
    * [Obtenir une adresse avec &](#heading-obtenir-une-adresse-avec-amp)
        
    * [Pointeurs vers des structs](#heading-pointeurs-vers-des-structs)
        
    * [Pointeurs vers d'autres types utilisateur](#heading-pointeurs-vers-d-autres-types-utilisateur)
        
* [Pourquoi utiliser des pointeurs ?](#heading-pourquoi-utiliser-des-pointeurs)
    
    * [Éviter les copies](#heading-eviter-les-copies)
        
    * [Partager et modifier l'état](#heading-partager-et-modifier-l-etat)
        
    * [Récepteurs de méthodes](#heading-recepteurs-de-methodes)
        
    * [Interfaçage avec des API de bas niveau](#heading-interfacage-avec-des-api-de-bas-niveau)
        
* [Pièges courants et malentendus](#heading-pieges-courants-et-malentendus)
    
    * [Pointeurs Nil](#heading-pointeurs-nil)
        
    * [Types de référence](#heading-types-de-reference)
        
* [Récepteurs de pointeur](#heading-recepteurs-de-pointeur)
    
    * [Récepteurs de valeur vs Récepteurs de pointeur](#heading-recepteurs-de-valeur-vs-recepteurs-de-pointeur)
        
    * [Go idiomatique](#heading-go-idiomatique)
        
* [Exercices pour le lecteur](#heading-exercices-pour-le-lecteur)
    
* [Bonus : Pointeurs faibles (Go 1.24+)](#heading-bonus-pointeurs-faibles-go-124)
    
    * [Que sont les pointeurs faibles ?](#heading-que-sont-les-pointeurs-faibles)
        
    * [Quand utiliser des pointeurs faibles ?](#heading-quand-utiliser-des-pointeurs-faibles)
        
* [Résumé et bonnes pratiques](#heading-resume-et-bonnes-pratiques)
    
* [Solutions des exercices](#heading-solutions-des-exercices)

## Prérequis

Cet article suppose que vous avez une compréhension de base de Go, incluant :

* Les variables et les types de base (`int`, `string`, etc.)
    
* Les fonctions et les appels de fonctions
    
* Les structs et les méthodes
    

Une familiarité avec les concepts de mémoire (comme la copie vs le référencement de valeurs) peut être utile, mais n'est pas requise. J'expliquerai tous les exemples de manière accessible aux débutants.

## Qu'est-ce qu'un pointeur ?

### Comprendre la mémoire

La mémoire d'un ordinateur est une large séquence d'octets, chacun ayant une adresse unique. Chaque variable d'un programme occupe un ou plusieurs octets contigus en mémoire, selon son type :

* Un `int32` occupe typiquement 4 octets.
    
* Un `int64` occupe typiquement 8 octets.
    
* Un `bool` occupe généralement 1 octet.
    

Les structs, les tableaux et les slices occupent la somme des tailles de leurs champs, plus un éventuel rembourrage (padding) pour l'alignement (pour un accès rapide). Chaque variable possède une adresse mémoire unique, qui est l'endroit où ses données sont stockées.

Par exemple, considérons :

```go
var a int32 = 100
var b bool = true
```

Cela ressemblera à quelque chose comme ceci en mémoire :

![Disposition de la mémoire](https://i.ibb.co/B2jZ3Smc/memory.png align="left")

`a` occupe 4 octets et contient la valeur `100`. `b` occupe 1 octet et contient `true`. L'adresse d'une variable est simplement l'emplacement en mémoire où ses données commencent (0x0202 pour `a`, et 0x0207 pour `b` dans cet exemple).

### Pile vs Tas (Stack vs Heap)

En Go, les variables peuvent être allouées sur la **pile** (stack) ou sur le **tas** (heap). La pile est une région de mémoire qui stocke les variables locales et les informations d'appel de fonction. Elle est rapide à allouer et à désallouer, car elle fonctionne selon le principe du dernier entré, premier sorti (LIFO).

Le tas est un pool de mémoire plus important utilisé pour l'allocation dynamique. Les variables allouées sur le tas peuvent survivre à la fonction qui les a créées, ce qui les rend adaptées aux données qui doivent être partagées ou modifiées entre différentes parties d'un programme.

Le runtime Go gère automatiquement l'allocation de mémoire et le Garbage Collector, vous n'avez donc pas besoin de vous soucier de libérer manuellement la mémoire comme dans certains autres langages.

La pile et le tas ne sont que des détails d'implémentation. En tant que programmeur Go, vous n'avez généralement pas besoin de vous soucier de l'endroit où une variable est allouée. Le compilateur et le runtime Go s'en occupent pour vous. Vous n'avez certainement pas à vous en soucier dans cet article – sachez simplement qu'ils existent et que les pointeurs peuvent pointer vers des valeurs dans l'un ou l'autre emplacement.

### Le pointeur

Un pointeur est simplement une variable qui **stocke l'adresse mémoire d'une autre variable**. D'après le diagramme ci-dessus, vous pouvez voir qu'une adresse est essentiellement une valeur entière (qui se trouve représenter un emplacement en mémoire). Sur un système 64 bits, les adresses font généralement 8 octets (64 bits) de long, donc une variable pointeur occupera également 8 octets.

En Go, vous déclarez un pointeur en utilisant l'opérateur `*`. Les pointeurs ont également un **type**, qui est le type de la variable vers laquelle ils pointent. Par exemple :

```go
var p *int32 // un pointeur vers un int32
```

You pouvez obtenir l'adresse d'une variable en utilisant l'opérateur `&` :

```go
var a int32 = 100
var p *int32 = &a // p contient maintenant l'adresse de a
```

En mémoire :

![Exemple de pointeur](https://i.ibb.co/4ZGzs3Rz/pointer.png align="left")

`a` contient la valeur `100` à l'adresse `0x0202`. `p` contient l'adresse de `a` (`0x0202`), et `p` lui-même est stocké à sa propre adresse (`0x0207`).

La raison pour laquelle les pointeurs portent des informations de type est que vous pouvez les **déréférencer** : suivre l'adresse pour accéder à la valeur sous-jacente. Cela se fait également en utilisant l'opérateur `*` :

```go
var a int32 = 100
var p *int32 = &a // p contient maintenant l'adresse de a

fmt.Println(*p) // affiche la valeur à l'adresse pointée par p, qui est la valeur de a : 100
```

Ce double usage de `*` est une source courante de confusion, clarifions donc :

1. Dans une *déclaration de type* (comme `var p *int32`), `*` indique que `p` est un pointeur vers un `int32`.
    
2. Dans une *expression* (comme `*p`), `*` déréférence le pointeur, vous donnant accès à la valeur vers laquelle il pointe.
    

Ensuite, voyons comment déclarer et utiliser des pointeurs en pratique, afin que vous puissiez voir comment `&` et `*` fonctionnent ensemble.

## Déclarer et utiliser des pointeurs

Maintenant que nous savons ce que sont les pointeurs conceptuellement, voyons à quoi ils ressemblent dans du code Go réel.

### Pointeurs vers des types de base

Comme nous l'avons vu précédemment, vous pouvez déclarer une variable pointeur avec l'opérateur `*` dans le type :

```go
var p *int      // p est un pointeur vers un int, mais actuellement nil
fmt.Println(p)  // <nil>
```

Comme chaque variable en Go, si vous ne l'initialisez pas, elle prend par défaut la valeur zéro pour son type. Pour les pointeurs, la valeur zéro est `nil`, ce qui signifie qu'il ne pointe vers aucune adresse mémoire valide.

You pouvez également utiliser la fonction intégrée `new` pour allouer une valeur et obtenir son pointeur :

```go
p := new(int)  // p est un pointeur vers un int avec une valeur zéro (0 pour int)
fmt.Println(*p) // affiche 0, la valeur zéro pour int
```

### Obtenir une adresse avec `&`

L'opérateur `&` récupère l'adresse d'une variable existante :

```go
x := 42
p := &x // p contient maintenant l'adresse de x

fmt.Println(*p) // 42
*p = 99         // change la valeur à l'adresse pointée par p (qui est x)
fmt.Println(x)  // 99
fmt.Println(p)  // affiche l'adresse mémoire de x, ex: 0xc0000140b8
fmt.Println(&x) // affiche la même adresse que p
```

### Pointeurs vers des structs

Les pointeurs peuvent pointer vers n'importe quel type. Ils sont particulièrement courants avec les **structs** :

```go
type User struct {
    Name string
    Age  int
}

func main() {
    u := User{"Alice", 30}
    p := &u                 // pointeur vers User
    fmt.Println((*p).Age)   // 30
    fmt.Println(p.Name)     // Alice - raccourci pour (*p).Name
}
```

You pouvez accéder aux champs avec soit `(*p).Name` ou simplement `p.Name`. Go **déréférence automatiquement les pointeurs de struct** par commodité.

Nous explorerons davantage les pointeurs de struct dans la section "Récepteurs de pointeur".

### Pointeurs vers d'autres types utilisateur

Vous pouvez créer des pointeurs vers n'importe quel type nommé :

```go
type Point struct {
    X, Y int
}
p := &Point{X: 1, Y: 2} // pointeur vers Point
fmt.Println(p.X, p.Y)   // 1 2 - raccourci pour (*p).X et (*p).Y
```

La syntaxe fonctionne exactement de la même manière pour les types définis par l'utilisateur que pour les types intégrés.

## Pourquoi utiliser des pointeurs ?

À première vue, les pointeurs peuvent ressembler à de la gymnastique mentale. Pourquoi ne pas simplement utiliser les valeurs directement ? Voici quelques raisons clés d'utiliser des pointeurs en Go :

### Éviter les copies

Lorsque vous assignez une valeur en Go, elle est copiée :

```go
type User struct {
    Name string
    Age  int
}

u1 := User{"Alice", 30}
u2 := u1  // copie
u2.Age = 40

fmt.Println(u1.Age) // 30
fmt.Println(u2.Age) // 40
```

Lorsque le struct est petit avec seulement quelques champs (comme cet exemple), la copie est peu coûteuse. Mais s'il est volumineux (des centaines de champs ou des données imbriquées), la copie peut être inefficace. Passer un pointeur évite de faire une copie complète :

```go
func Birthday(u *User) {
    u.Age++
}

u := User{"Bob", 29}
Birthday(&u)
fmt.Println(u.Age) // 30
```

### Partager et modifier l'état

Parfois, vous voulez que plusieurs parties de votre programme travaillent avec le même objet. Avec les valeurs, chaque affectation crée une copie :

```go
type Counter struct {
    value int32
}

c1 := Counter{value: 0} // c1 est un Counter
c2 := c1  // c2 est une copie - un autre Counter

c2.value++
fmt.Println(c1.value) // 0
fmt.Println(c2.value) // 1
```

L'utilisation de pointeurs garantit que les deux variables se réfèrent aux mêmes données sous-jacentes :

```go
pc1 := &Counter{value: 0} // pc1 est un pointeur vers un Counter
pc2 := pc1   // copie du pointeur - les deux pointent vers le même Counter

pc2.value++
fmt.Println(pc1.value) // 1
fmt.Println(pc2.value) // 1
```

Ce diagramme illustre les deux dispositions de mémoire :

![Valeur vs Pointeur](https://i.ibb.co/tPXSr9FN/counter.png align="left")

`c1` et `c2` sont stockés séparément à `0x0202` et `0x0207`, chacun avec son propre champ `value` de 4 octets. Dans le second exemple, `pc1` et `pc2` sont stockés respectivement à `0x0202` et `0x020a`, et tous deux contiennent la même adresse (`0x1002`) pointant vers une instance unique de `Counter` dans le tas, ayant son propre champ `value` de 4 octets.

### Récepteurs de méthodes

Les méthodes Go peuvent avoir des **récepteurs de valeur** ou des **récepteurs de pointeur**. Les récepteurs de pointeur sont nécessaires lorsque :

* La méthode doit modifier le struct
    
* Le struct est volumineux et la copie serait coûteuse
    
* Vous voulez de la cohérence (il est courant de faire de tous les récepteurs des pointeurs si certains doivent l'être)
    

Nous couvrirons cela en détail dans la section "Récepteurs de pointeur".

### Interfaçage avec des API de bas niveau

Certaines bibliothèques et appels système exigent que vous passiez des adresses mémoire, pas des copies. Les pointeurs rendent cela possible, tout en restant sûrs en Go.

## Pièges courants et malentendus

### Pointeurs Nil

Si vous déclarez un pointeur sans l'initialiser, il sera `nil`. Déréférencer un pointeur nil provoquera immédiatement un panic à l'exécution :

```go
var p *int
fmt.Println(*p) // panic: runtime error: invalid memory address or nil pointer dereference
```

C'est la façon de Go de vous dire que vous avez essayé de suivre une adresse qui n'existe pas. Pour utiliser les pointeurs en toute sécurité, vous devez toujours leur donner une cible valide avant de les déréférencer :

```go
x := 42
p := &x          // p pointe vers x
fmt.Println(*p)  // 42

q := new(int)    // alloue de la mémoire pour un int, l'initialise à 0
fmt.Println(*q)  // 0
```

`&` et `new` garantissent tous deux que le pointeur pointe vers une mémoire valide.

### Types de référence

En Go, tout est passé par valeur. Mais cette valeur dépend de la **représentation interne** du type. Par exemple, une slice est stockée en mémoire comme ceci :

```go
struct {
    ptr *ElementType // pointeur vers le tableau sous-jacent
    len int          // longueur de la slice
    cap int          // capacité de la slice
}
```

Lorsque vous passez une slice à une fonction, vous passez une copie de cette structure. Le champ `ptr` pointe toujours vers le même tableau sous-jacent, donc les modifications apportées aux éléments de la slice à l'intérieur de la fonction affecteront la slice originale.

En raison de ce comportement, les slices sont souvent appelées **types de référence** : vous n'avez pas besoin d'utiliser des pointeurs avec elles pour partager ou modifier des données. Les autres types de référence en Go incluent les maps et les channels. Les strings sont également considérées comme des types de référence, mais elles sont immuables, vous ne pouvez donc pas modifier leur contenu.

Notez que les pointeurs eux-mêmes ne sont pas des types de référence : ce sont simplement des variables qui contiennent des adresses mémoire.

(Pour compliquer un peu plus les choses, si vous passez une slice à une fonction puis que vous la re-slicez ou que vous y ajoutez des éléments avec append, vous modifiez la copie de la structure de la slice. La slice originale à l'extérieur de la fonction ne verra pas ces changements !)

## Récepteurs de pointeur

Lors de la définition de méthodes sur des structs en Go, vous pouvez choisir entre des récepteurs de valeur et des récepteurs de pointeur. Comprendre la différence est essentiel pour écrire du code Go correct et efficace.

### Récepteurs de valeur vs Récepteurs de pointeur

**Récepteur de valeur** : la méthode reçoit une copie du struct. Toute modification à l'intérieur de la méthode n'affecte pas le struct original.

**Récepteur de pointeur** : la méthode reçoit une copie du pointeur, qui pointe toujours vers le struct original. Les modifications à l'intérieur de la méthode affectent le struct original.

Exemple :

```go
type Counter struct {
    value int
}
```

Si vous essayez d'incrémenter le compteur en utilisant un récepteur de valeur, cela ne fonctionnera pas comme prévu :

```go
func (c Counter) Inc() {
    c.value++ // INCORRECT : modifie la copie, pas l'original
}

c := Counter{value: 5}
c.Inc()
fmt.Println(c.value) // toujours 5
```

Avec un récepteur de pointeur, cela fonctionne correctement :

```go
func (c *Counter) Inc() {
    // notez la syntaxe raccourcie pour (*c).value
    c.value++ // CORRECT : modifie l'original via le pointeur
}

c := Counter{value: 5}
c.Inc()
fmt.Println(c.value) // maintenant 6
```

Même si la méthode reçoit une copie du pointeur, la copie et le pointeur d'origine pointent vers le même struct en mémoire (dans le tas), de sorte que les changements à l'intérieur de la méthode affectent l'original.

### Go idiomatique

* Les petits structs peuvent utiliser des récepteurs de valeur si la mutation n'est pas nécessaire.
    
* Les grands structs ou tout struct qui doit être modifié doivent utiliser des récepteurs de pointeur.
    
* Si certaines méthodes ont besoin de récepteurs de pointeur, il est courant que toutes les méthodes utilisent des récepteurs de pointeur par souci de cohérence.
    

Les récepteurs de pointeur sont sans doute l'utilisation la plus courante et la plus pratique des pointeurs en Go. Ils permettent aux méthodes de modifier l'état en toute sécurité sans copies inutiles.

## Exercices pour le lecteur

Pour consolider votre compréhension des pointeurs, essayez les exercices suivants :

1. Écrivez une fonction qui échange deux entiers en utilisant des pointeurs.
    
2. Créez un struct représentant un `Rectangle` avec une largeur (width) et une hauteur (height). Écrivez des méthodes pour calculer l'aire et pour redimensionner le rectangle par un facteur, en utilisant des récepteurs de pointeur.
    

## Bonus : Pointeurs faibles (Go 1.24+)

Go 1.24 a introduit les références faibles, qui vous permettent de détenir une référence vers une valeur sans empêcher son ramassage par le Garbage Collector. Ceci est utile lorsque vous voulez un cache ou une structure de données auxiliaire sans prolonger la durée de vie des objets.

### Que sont les pointeurs faibles ?

Un pointeur faible est un pointeur qui ne compte pas pour maintenir l'objet référencé en vie. Si les seules références à un objet sont faibles, le Garbage Collector peut toujours le libérer.

Les pointeurs faibles sont fournis par le package `runtime/weak` :

```go
import "runtime/weak"

type Cache struct {
    data weak.Map[string, *User]
}

func main() {
    c := Cache{data: weak.MakeMap[string, *User]()}
    u := &User{"Alice", 30}
    
    c.data.Set("alice", u) // référence faible stockée
}

// ...plus tard
if user, ok := c.data.Get("alice"); ok {
    fmt.Println(user.Name) // Alice
} else {
    fmt.Println("L'utilisateur a été collecté par le Garbage Collector")
}
```

Si `u` n'est plus référencé ailleurs, le Garbage Collector peut le récupérer, même s'il existe dans la `weak.Map`.

Essentiellement, un pointeur faible peut se transformer en un pointeur nil si l'objet vers lequel il pointe a été collecté. Vous devriez toujours vérifier s'il est nil avant de le déréférencer.

### Quand utiliser des pointeurs faibles

* Caches : Gardez les objets s'ils sont encore utilisés, mais n'empêchez pas le GC s'ils ne le sont plus.
    
* Éviter les fuites de mémoire : Surtout dans les services à longue durée de vie où les objets temporaires pourraient autrement s'accumuler.
    
* Indexation auxiliaire : Comme mapper des IDs à des objets sans contrôler leur durée de vie.
    

Les pointeurs faibles sont une fonctionnalité avancée et doivent être utilisés avec discernement. La plupart des programmes Go n'en auront jamais besoin, mais dans certains scénarios, ils peuvent être très utiles.

## Résumé et bonnes pratiques

* Les pointeurs stockent les adresses des variables et vous permettent de partager et de modifier les données efficacement.
    
* Utilisez `&` pour obtenir une adresse, `*` pour déréférencer et déclarer.
    
* Les récepteurs de pointeur permettent aux méthodes de modifier les structs sans copies inutiles.
    
* Soyez prudent avec les pointeurs nil pour éviter les panics.
    
* Les types de référence (slices, maps, channels) partagent déjà les données sous-jacentes.
    
* Les pointeurs faibles (Go 1.24+) offrent une gestion de mémoire avancée pour les caches ou les structures auxiliaires.

Bien qu'ils ne soient pas aussi puissants que dans des langages comme C/C++, les pointeurs Go sont sûrs et faciles à utiliser. Expérimentez avec eux dans de petits programmes, et vous verrez rapidement comment ils peuvent vous aider à écrire du code Go plus efficace et facile à lire.

## Solutions des exercices

1. Échanger deux entiers en utilisant des pointeurs :
    

```go
func swap(a, b *int) {
    *a, *b = *b, *a
}

x, y := 1, 2
swap(&x, &y)
fmt.Println(x, y) // 2 1
```

Ici, `swap` prend deux pointeurs vers des entiers et échange leurs valeurs en les déréférençant. Sans pointeurs, vous n'échangeriez que des copies des entiers, laissant les originaux inchangés.

2. Struct Rectangle avec méthodes :
    

```go
type Rectangle struct {
    Width, Height float64
}

func (r *Rectangle) Area() float64 {
    return r.Width * r.Height
}

func (r *Rectangle) Scale(factor float64) {
    r.Width *= factor
    r.Height *= factor
}

rect := Rectangle{Width: 3, Height: 4}
fmt.Println(rect.Area()) // 12
rect.Scale(2)
fmt.Println(rect.Area()) // 48
```

Parce que `Scale` modifie le rectangle, il utilise un récepteur de pointeur. La méthode `Area` pourrait utiliser soit un récepteur de valeur, soit un récepteur de pointeur puisqu'elle ne modifie pas le struct, mais l'utilisation d'un récepteur de pointeur est cohérente et évite de copier le struct.