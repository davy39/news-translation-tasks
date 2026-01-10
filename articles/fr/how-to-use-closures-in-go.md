---
title: Comment utiliser les closures en Go
subtitle: ''
author: Gabor Koos
co_authors: []
series: null
date: '2025-10-27T20:35:29.503Z'
originalURL: https://freecodecamp.org/news/how-to-use-closures-in-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761597115311/04035f6b-6bd0-4889-8433-3f0d652f2586.png
tags:
- name: Go Language
  slug: go
- name: closure
  slug: closure
- name: golang
  slug: golang
seo_title: Comment utiliser les closures en Go
seo_desc: 'If you''ve written code in JavaScript, Python, or Rust, you''ve probably
  heard the word closure before. The concept has subtle differences in each language,
  but the core idea is the same: a closure is a function that captures variables from
  its surroun...'
---

Si vous avez déjà écrit du code en JavaScript, Python ou Rust, vous avez probablement déjà entendu le mot *closure*. Le concept présente de subtiles différences dans chaque langage, mais l'idée centrale reste la même : une closure est une fonction qui capture des variables de sa portée environnante. Cela permet à la fonction de « se souvenir » de l'environnement dans lequel elle a été créée, même lorsqu'elle est exécutée en dehors de cet environnement, ce qui a des implications puissantes sur la façon dont nous écrivons et structurons notre code.

Dans cet article, nous explorerons le fonctionnement des closures en Go, un langage statiquement typé connu pour sa simplicité et son efficacité. Nous verrons comment créer des closures, comment elles capturent les variables et quelques cas d'utilisation pratiques.

## Ce que nous allons aborder

* [Prérequis](#heading-prerequis)
    
* [Ce que sont réellement les closures en Go](#heading-ce-que-sont-reellement-les-closures-en-go)
    
    * [Comment Go rend cela possible](#heading-comment-go-rend-cela-possible)
        
    * [Plusieurs closures indépendantes](#heading-plusieurs-closures-independantes)
        
* [Le piège classique de la boucle](#heading-le-piege-classique-de-la-boucle)
    
* [Comment créer des closures en Go](#heading-comment-creer-des-closures-en-go)
    
    * [Retourner des closures depuis des fonctions](#heading-retourner-des-closures-depuis-des-fonctions)
        
    * [Fonctions internes nommées](#heading-fonctions-internes-nommees)
        
    * [Closures en ligne dans les boucles ou les goroutines](#heading-closures-en-ligne-dans-les-boucles-ou-les-goroutines)
        
    * [Closures avec paramètres](#heading-closures-avec-parametres)
        
    * [Capturer plusieurs variables](#heading-capturer-plusieurs-variables)
        
    * [Closures dans les structs](#heading-closures-dans-les-structs)
        
    * [Note sur les récepteurs de méthodes](#heading-note-sur-les-recepteurs-de-methodes)
        
    * [Points clés à retenir](#heading-points-cles-a-retenir)
        
* [Closures et concurrence](#heading-closures-et-concurrence)
    
    * [État indépendant à travers les goroutines](#heading-etat-independant-a-travers-les-goroutines)
        
    * [Capturer des variables partagées en toute sécurité](#heading-capturer-des-variables-partagees-en-toute-securite)
        
* [Modèles pratiques avec les closures](#heading-modeles-pratiques-avec-les-closures)
    
    * [Mémoïsation / Mise en cache](#heading-memoisation-mise-en-cache)
        
    * [Gestionnaires d'événements / Callbacks](#heading-gestionnaires-devenements-callbacks)
        
    * [Pipelines encapsulés / Producteurs](#heading-pipelines-encapsules-producteurs)
        
    * [Exécution différée avec état capturé](#heading-execution-differee-avec-etat-capture)
        
    * [Comment implémenter des interfaces de manière dynamique](#heading-comment-implementer-des-interfaces-de-maniere-dynamique)
        
    * [Points clés à retenir](#heading-points-cles-a-retenir-1)
        
* [Comment les closures affectent la mémoire et les performances](#heading-comment-les-closures-affectent-la-memoire-et-les-performances)
    
    * [Les variables peuvent vivre plus longtemps que prévu](#heading-les-variables-peuvent-vivre-plus-longtemps-que-prevu)
        
    * [De nombreuses closures peuvent ajouter une surcharge](#heading-de-nombreuses-closures-peuvent-ajouter-une-surcharge)
        
* [Comment tester et déboguer les closures](#heading-comment-tester-et-deboguer-les-closures)
    
    * [Isoler la closure](#heading-isoler-la-closure)
        
    * [Vérifier les variables capturées](#heading-verifier-les-variables-capturees)
        
    * [Utiliser les journaux ou les impressions de débogage](#heading-utiliser-les-journaux-ou-les-impressions-de-debogage)
        
    * [Tester la concurrence avec soin](#heading-tester-la-concurrence-avec-soin)
        
    * [Points clés à retenir](#heading-points-cles-a-retenir-2)
        
* [Bonnes pratiques et points à retenir pour l'utilisation des closures en Go](#heading-bonnes-pratiques-et-points-a-retenir-pour-lutilisation-des-closures-en-go)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre cet article, vous devez avoir une compréhension de base de la programmation en Go, y compris les fonctions et la portée des variables. Si vous débutez avec Go, n'hésitez pas à consulter le [tour officiel de Go](https://tour.golang.org/) pour vous mettre à niveau.

## Ce que sont réellement les closures en Go

Au plus simple, une closure en Go est une fonction qui **référence des variables définies en dehors d'elle-même**. Cela peut paraître abstrait, alors commençons par un exemple que vous pouvez exécuter immédiatement :

```go
package main

import "fmt"

func counter() func() int {
    n := 0
    return func() int {
        n++
        return n
    }
}

func main() {
    next := counter()
    fmt.Println(next()) // 1
    fmt.Println(next()) // 2
    fmt.Println(next()) // 3
}
```

Lorsque vous appelez `counter()`, elle retourne une autre fonction, mais cette fonction **conserve l'accès à la variable** `n` qui résidait à l'intérieur de counter.

Même si `counter()` a déjà fini de s'exécuter, `n` n'a pas disparu. Chaque fois que vous appelez `next()`, elle met à jour le même `n` qui a été créé lors de l'appel original de `counter()`.

C'est la propriété définissante d'une closure :

> Une closure « se ferme sur » (closes over) son environnement, maintenant en vie les variables dont elle a besoin aussi longtemps que la closure elle-même existe.

### Comment Go rend cela possible

Normalement, les variables locales en Go vivent sur la **pile** (stack), qui est vidée lorsqu'une fonction se termine.

Mais si une fonction imbriquée doit continuer à utiliser l'une de ces variables, le compilateur de Go effectue ce qu'on appelle une *analyse d'échappement* (escape analysis) : il voit que la variable survivra à l'appel de la fonction, il déplace donc cette variable vers le **tas** (heap), où elle peut rester en vie tant que quelque chose la référence - dans ce cas, la closure.

Vous pouvez d'ailleurs demander au compilateur de vous montrer ce processus :

```bash
go build -gcflags="-m" main.go
```

Vous pourriez voir une sortie comme :

```bash
./main.go:6:6: moved to heap: n
```

Cela vous indique que la variable `n` a « échappé » à la pile pour que la closure puisse l'utiliser en toute sécurité plus tard.

### Plusieurs closures indépendantes

Chaque appel à une fonction qui retourne une closure crée un nouvel environnement indépendant :

```go
a := counter()
b := counter()
fmt.Println(a()) // 1
fmt.Println(a()) // 2
fmt.Println(b()) // 1
```

Ici, `a` et `b` sont deux closures distinctes, chacune ayant son propre `n`. Appeler `a()` incrémente son propre `n`, tandis qu'appeler `b()` commence à partir de son propre `n` séparé.

## Le piège classique de la boucle

L'une des surprises les plus courantes pour les développeurs Go survient lorsque des closures sont utilisées à l'intérieur d'une boucle. Même les programmeurs expérimentés tombent souvent dans ce piège.

Considérez cet exemple :

```go
package main

import "fmt"

func main() {
    funcs := make([]func(), 0)
    for i := 0; i < 3; i++ {
        funcs = append(funcs, func() {
            fmt.Println(i)
        })
    }
    for _, f := range funcs {
        f()
    }
}
```

On pourrait s'attendre à ce que cela affiche `0`, `1` et `2`, mais cela affiche en réalité :

```bash
3
3
3
```

**Pourquoi cela arrive-t-il ?**

À l'intérieur de la boucle, chaque fonction littérale **capture la variable** `i` elle-même, et non sa valeur à cet instant précis.

La boucle réutilise la même variable `i` pour toutes les itérations. Au moment où la boucle se termine, `i` est égal à 3, et **toutes les closures voient ce même** `i` lorsqu'elles s'exécutent plus tard.

**Comment corriger cela**

Il existe deux corrections idiomatiques courantes :

1. Masquer la variable de boucle (shadowing) :
    

```go
for i := 0; i < 3; i++ {
    i := i // une nouvelle variable masque la variable de boucle
    funcs = append(funcs, func() {
        fmt.Println(i)
    })
}
```

2. Passer la variable comme paramètre à une fonction interne :
    

```go
for i := 0; i < 3; i++ {
    funcs = append(funcs, func(x int) func() {
        return func() { fmt.Println(x) }
    }(i))
}
```

Les deux approches créent une nouvelle variable pour chaque itération, de sorte que chaque closure capture sa propre valeur indépendante.

## Comment créer des closures en Go

Il existe plusieurs façons de créer des closures en Go. Explorons quelques modèles courants.

### Retourner des closures depuis des fonctions

Le modèle le plus courant consiste à faire en sorte qu'une fonction retourne une closure qui conserve son propre état :

```go
func makeCounter() func() int {
    n := 0
    return func() int {
        n++
        return n
    }
}

c1 := makeCounter()
fmt.Println(c1()) // 1
fmt.Println(c1()) // 2
```

Chaque appel à `makeCounter` crée une nouvelle closure avec son propre `n`, comme nous l'avons vu précédemment.

### Fonctions internes nommées

Vous pouvez également donner un nom à une fonction littérale pour la lisibilité ou le débogage :

```go
func makeCounter() func() int {
    n := 0
    next := func incr() int {
        n++
        return n
    }
    return next
}
```

Cela fonctionne de la même manière mais donne un nom à la fonction interne (`incr`), ce qui peut être utile dans les traces de pile (stack traces). À part cela, elle se comporte exactement comme une fonction anonyme.

### Closures en ligne dans les boucles ou les goroutines

Les closures sont souvent définies en ligne, en particulier pour les boucles ou les goroutines :

```go
for i := 0; i < 3; i++ {
    go func(x int) {
        fmt.Println(x)
    }(i)
}
```

Ici, nous passons `i` comme paramètre à la closure, garantissant que chaque goroutine reçoit sa propre copie de la valeur, évitant ainsi le piège de la variable de boucle.

### Closures avec paramètres

Les closures peuvent accepter leurs propres arguments :

```go
func adder(base int) func(int) int {
    return func(x int) int {
        return base + x
    }
}

add5 := adder(5)
fmt.Println(add5(10)) // 15
```

Ici, `adder` retourne une closure qui ajoute une valeur `base` fixe à n'importe quel argument qu'elle reçoit.

### Capturer plusieurs variables

Les closures peuvent capturer plusieurs variables externes :

```go
func multiplier(factor int) func(int) int {
    offset := 2
    return func(x int) int {
        return x*factor + offset
    }
}

m := multiplier(3)
fmt.Println(m(4)) // 14
```

Dans cet exemple, la closure capture à la fois `factor` et `offset` de sa portée environnante - `factor` est un paramètre, tandis qu'`offset` est une variable locale.

### Closures dans les structs

Les closures peuvent également être stockées dans des structs, comme n'importe quelle autre valeur de fonction. C'est un modèle utile lorsque vous voulez des objets ayant un comportement dynamique ou avec état.

```go
type Counter struct {
    Next func() int
}

func NewCounter() Counter {
    n := 0
    return Counter{
        Next: func() int {
            n++
            return n
        },
    }
}

func main() {
    c := NewCounter()
    fmt.Println(c.Next()) // 1
    fmt.Println(c.Next()) // 2
}
```

Ici, le champ `Next` contient une closure qui capture la variable `n`. Chaque instance de `Counter` possède son propre état indépendant, sans avoir besoin d'un type séparé ou d'un mutex.

Ce modèle montre comment les closures peuvent agir comme des objets légers : regroupant comportement et état.

### Note sur les récepteurs de méthodes

En Go, les closures ne capturent pas implicitement le récepteur de la méthode comme dans certains langages. Si vous voulez qu'une closure utilise le récepteur à l'intérieur d'une méthode, vous l'assignez généralement à une variable locale :

```go
type Counter struct {
    n int
}

func (c *Counter) MakeIncrementer() func() int {
    r := c // capture explicitement le récepteur
    return func() int {
        r.n++
        return r.n
    }
}
```

Cela garantit que la closure référence le récepteur prévu plutôt que d'introduire un comportement inattendu.

Contrairement à JavaScript ou Python, les closures Go capturent des variables lexicales, et non le `this` ou `self` implicite.

### Points clés à retenir

* Les closures peuvent être retournées par des fonctions, nommées, en ligne ou même stockées dans des structs.
    
* Elles capturent les variables externes, et non des copies de leurs valeurs.
    
* Utilisées de cette manière, les closures peuvent remplacer de petits types ou interfaces pour une encapsulation légère.
    

## Closures et concurrence

Les closures sont puissantes en Go, mais lorsque vous les combinez avec la concurrence, leurs variables capturées peuvent agir de manière inattendue si vous n'êtes pas prudent.

### État indépendant à travers les goroutines

Chaque closure maintient ses propres variables capturées en vie, même lorsqu'elle est utilisée dans des goroutines concurrentes :

```go
func makeWorker(start int) func() int {
    counter := start
    return func() int {
        counter++
        return counter
    }
}

func main() {
    worker1 := makeWorker(0)
    worker2 := makeWorker(100)

    go func() { fmt.Println(worker1()) }() // affiche 1
    go func() { fmt.Println(worker2()) }() // affiche 101
}
```

Ici, `worker1` et `worker2` ont des variables `counter` indépendantes, elles n'interfèrent donc pas l'une avec l'autre. Chaque closure maintient un état indépendant, même dans des goroutines séparées.

### Capturer des variables partagées en toute sécurité

Lorsque plusieurs closures partagent une variable, vous devez coordonner l'accès. Par exemple :

```go
counter := 0
ch := make(chan int)

for i := 0; i < 3; i++ {
    go func() {
        // incrémente une variable partagée
        ch <- 1
    }()
}

// agrégation sécurisée
for i := 0; i < 3; i++ {
    counter += <-ch
}
fmt.Println(counter) // 3
```

La closure capture la variable externe `ch` (un canal), ce qui est sûr car les canaux sérialisent l'accès. L'utilisation d'un canal tamponné ici ne changerait pas le comportement de la closure : elle capture toujours son propre `n` et envoie les valeurs au canal de manière indépendante.

Les closures elles-mêmes **ne synchronisent pas l'état partagé, vous avez toujours besoin de canaux ou de mutex**.

## Modèles pratiques avec les closures

Les closures en Go ne sont pas seulement une curiosité du langage, elles sont un outil puissant pour écrire du code avec état, réutilisable et flexible. Voici quelques modèles pratiques qui vont au-delà des bases.

### Mémoïsation / Mise en cache

Les closures peuvent capturer une map interne ou un cache pour stocker les résultats de calculs coûteux :

```go
func memoize(f func(int) int) func(int) int {
    cache := map[int]int{}
    return func(x int) int {
        if val, ok := cache[x]; ok {
            return val
        }
        result := f(x)
        cache[x] = result
        return result
    }
}

func main() {
    fib := memoize(func(n int) int {
        if n <= 1 {
            return n
        }
        return fib(n-1) + fib(n-2)
    })
    fmt.Println(fib(10)) // 55
}
```

Ici, la fonction `memoize` retourne une closure qui met en cache les résultats de la fonction Fibonacci, évitant ainsi les calculs redondants.

### Gestionnaires d'événements / Callbacks

Les closures sont parfaites pour définir des gestionnaires d'événements ou des callbacks qui doivent maintenir un état :

```go
type Button struct {
    onClick func()
}

func (b *Button) Click() {
    if b.onClick != nil {
        b.onClick()
    }
}

func main() {
    count := 0
    button := Button{
        onClick: func() {
            count++
            fmt.Println("Bouton cliqué", count, "fois")
        },
    }

    button.Click() // Bouton cliqué 1 fois
    button.Click() // Bouton cliqué 2 fois
}
```

Dans cet exemple, la closure capture la variable `count`, permettant au bouton de suivre le nombre de fois qu'il a été cliqué.

### Pipelines encapsulés / Producteurs

Les closures peuvent envelopper une logique avec état pour les canaux et les pipelines :

```go
func producer(start int) func(chan int) {
    n := start
    return func(ch chan int) {
        for i := 0; i < 3; i++ {
            ch <- n
            n++
        }
    }
}

func main() {
    ch := make(chan int, 3)
    go producer(5)(ch)
    for i := 0; i < 3; i++ {
        fmt.Println(<-ch) // 5, 6, 7
    }
}
```

Ici, la fonction `producer` retourne une closure qui envoie une séquence de nombres à un canal, en maintenant son propre état avec `n`.

### Exécution différée avec état capturé

L'utilisation d'une closure avec `defer` vous permet de capturer des variables au moment où l'instruction defer est exécutée, ce qui est particulièrement utile dans les boucles ou le nettoyage de ressources :

```go
func main() {
    for i := 0; i < 3; i++ {
        defer func(x int) {
            fmt.Println(x)
        }(i) // capture le i actuel
    }
}
```

Sortie :

```bash
2
1
0
```

Ici, chaque closure différée capture la valeur de `i` au moment de l'instruction `defer`, de sorte qu'elles s'affichent dans l'ordre inverse lorsque la fonction se termine.

### Comment implémenter des interfaces de manière dynamique

Les closures peuvent également être utilisées pour implémenter des interfaces sans définir un type struct complet. Par exemple, une simple fonction peut satisfaire une interface à méthode unique :

```go
type Greeter interface {
    Greet() string
}

func MakeGreeter(name string) Greeter {
    return struct{ Greeter }{
        Greeter: func() string { return "Bonjour, " + name },
    }
}

func main() {
    g := MakeGreeter("Alice")
    fmt.Println(g.Greet()) // Bonjour, Alice
}
```

Ici, la closure capture `name`, permettant à l'objet retourné d'implémenter la méthode `Greet` de manière dynamique.

### Points clés à retenir

* Les closures permettent la mémoïsation et la mise en cache sans structs supplémentaires.
    
* Le stockage de closures dans des structs offre un comportement personnalisable pour les objets.
    
* Les closures peuvent encapsuler des pipelines concurrents avec état, gardant la logique localisée et sûre.
    
* Les closures avec `defer` capturent les variables au moment du report, ce qui est utile pour le nettoyage ou la journalisation.
    
* Elles permettent des implémentations d'interface dynamiques sans code répétitif (boilerplate).
    

## Comment les closures affectent la mémoire et les performances

Les closures sont puissantes, mais la capture de variables de portées externes a des implications sur la mémoire et les performances.

### Les variables peuvent vivre plus longtemps que prévu

Parce que les closures conservent des références aux variables capturées (et les déplacent vers le tas si nécessaire, comme nous l'avons vu plus haut), ces variables vivent aussi longtemps que la closure elle-même, ce qui peut augmenter l'utilisation de la mémoire :

```go
func main() {
    bigData := make([]byte, 10_000_000) // 10 Mo
    f := func() int { return len(bigData) }
    _ = f
}
```

Dans cet exemple, `bigData` reste en mémoire tant que la closure `f` existe, même si `bigData` n'est plus nécessaire ailleurs.

### De nombreuses closures peuvent ajouter une surcharge

Chaque closure transporte un petit environnement pour ses variables capturées. Créer des milliers de closures est généralement acceptable, mais dans un code haute performance ou sensible à la mémoire, cela peut ajouter une surcharge mesurable.

* Les variables capturées peuvent être allouées sur le tas.
    
* Chaque closure possède une petite struct cachée pour son environnement.
    

Les alternatives incluent les **structs** ou les **fonctions simples** lorsque vous avez besoin d'une efficacité maximale.

## Comment tester et déboguer les closures

Les closures peuvent parfois se comporter de manière inattendue lors de la capture de variables ou du travail avec la concurrence. Voici quelques conseils pour les tester et les déboguer efficacement.

### Isoler la closure

Testez la closure indépendamment de sa fonction externe pour vérifier son comportement :

```go
func TestCounter(t *testing.T) {
    counter := makeCounter()
    if counter() != 1 {
        t.Error("attendu 1")
    }
    if counter() != 2 {
        t.Error("attendu 2")
    }
}
```

Cela garantit que la closure maintient l'état correctement.

### Vérifier les variables capturées

Rappelez-vous : les closures capturent les variables par référence, pas par valeur. Soyez attentif aux variables de boucle ou à l'état partagé :

```go
for i := 0; i < 3; i++ {
    i := i // masquer la variable de boucle
    t.Run(fmt.Sprintf("i=%d", i), func(t *testing.T) {
        if i != i { // vérification simplifiée
            t.Fail()
        }
    })
}
```

Cela permet d'éviter le piège de la boucle dans les tests.

### Utiliser les journaux ou les impressions de débogage

L'affichage de l'état interne de la closure est souvent le moyen le plus rapide de déboguer un comportement subtil :

```go
adder := func(base int) func(int) int {
    return func(x int) int {
        fmt.Printf("base=%d, x=%d\n", base, x)
        return base + x
    }
}
result := adder(5)(10) // log : base=5, x=10
```

### Tester la concurrence avec soin

Lorsque des closures sont utilisées dans des goroutines, des conditions de concurrence (race conditions) peuvent apparaître. Utilisez le détecteur de compétition de Go :

```bash
go test -race ./...
```

Cela signale tout accès à une variable partagée qui n'est pas correctement synchronisé.

### Points clés à retenir

* Testez les closures indépendamment pour vous assurer que l'état capturé se comporte comme prévu.
    
* Soyez prudent avec les variables de boucle et l'état partagé.
    
* Utilisez la journalisation et le détecteur de compétition pour déboguer les problèmes de concurrence.
    

## Bonnes pratiques et points à retenir pour l'utilisation des closures en Go

Les closures sont une fonctionnalité polyvalente de Go, mais comme tout outil, elles fonctionnent mieux lorsqu'elles sont utilisées avec discernement. Voici quelques directives pratiques :

* **Encapsulez l'état proprement** : Utilisez des closures pour maintenir un état privé sans introduire de structs ou de types supplémentaires. Les compteurs, les caches de mémoïsation et les petites fabriques sont des modèles courants.
    
* **Soyez prudent dans les boucles** : Capturez toujours correctement les variables de boucle pour éviter le piège classique. Masquer la variable ou la passer comme paramètre à la closure sont des solutions idiomatiques.
    
* **Gérez la concurrence explicitement** : Les closures peuvent maintenir en toute sécurité un état indépendant dans les goroutines, mais elles ne synchronisent pas automatiquement l'état partagé. Lorsque plusieurs closures partagent des variables, coordonnez l'accès avec des canaux ou des mutex.
    
* **Attention à l'usage de la mémoire** : Les variables capturées peuvent s'échapper vers le tas, de sorte que les closures à longue durée de vie peuvent retenir plus de mémoire que prévu. Évitez de capturer de gros objets sauf si nécessaire.
    
* **Tirez parti des closures dans les structs** : Le stockage de closures dans des champs de struct permet aux objets d'avoir un comportement dynamique ou personnalisable sans code répétitif supplémentaire, rendant votre code plus flexible.
    

## Conclusion

Les closures en Go permettent aux fonctions de transporter un état, d'encapsuler un comportement et d'interagir en toute sécurité avec les modèles de concurrence, tout en gardant votre code propre et expressif. En comprenant comment les closures capturent les variables, comment elles se comportent dans les boucles et les goroutines, et leurs implications sur la mémoire, vous pouvez les utiliser en toute confiance pour écrire un code Go plus idiomatique et maintenable.