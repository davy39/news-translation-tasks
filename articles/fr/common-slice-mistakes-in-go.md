---
title: Erreurs courantes avec les Slices en Go et comment les éviter
subtitle: ''
author: Temitope Oyedele
co_authors: []
series: null
date: '2025-09-30T16:52:28.684Z'
originalURL: https://freecodecamp.org/news/common-slice-mistakes-in-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759251032781/125e9bfc-2e78-4f71-b423-2d045bf82a9f.png
tags:
- name: Go Language
  slug: go
seo_title: Erreurs courantes avec les Slices en Go et comment les éviter
seo_desc: Slices are one of the most fundamental and powerful data structures in Go.
  They provide a dynamic array-like interface that's both flexible and efficient.
  However, they can be very tricky when implementing. And if not implemented correctly,
  they can ...
---

Les slices sont l'une des structures de données les plus fondamentales et les plus puissantes de Go. Elles fournissent une interface de type tableau dynamique qui est à la fois flexible et efficace. Cependant, elles peuvent être très délicates lors de l'implémentation. Et si elles ne sont pas implémentées correctement, elles peuvent provoquer des bugs subtils qui seraient très difficiles à traquer.

Vous penserez probablement qu'il s'agit d'un problème avec votre algorithme ou votre logique, passant des heures à déboguer des flux de travail complexes. En revanche, le véritable problème provient d'une simple incompréhension du comportement des slices sous le capot. La partie la plus frustrante ? Votre code pourrait fonctionner parfaitement en développement avec de petits ensembles de données, pour échouer mystérieusement en production avec des données plus volumineuses ou sous un accès concurrent.

Dans cet article, nous explorerons sept erreurs courantes que les développeurs commettent lorsqu'ils travaillent avec des slices en Go et fournirons des solutions pratiques pour les prévenir.

## Table des matières

* [Passer des slices par valeur et s'attendre à des changements structurels](#heading-passer-des-slices-par-valeur-et-s-attendre-a-des-changements-structurels)
    
* [Partage d'en-tête de slice et mutations involontaires](#heading-partage-d-en-tete-de-slice-et-mutations-involontaires)
    
* [Fuites de mémoire avec des références à de grandes slices](#heading-fuites-de-memoire-avec-des-references-a-de-grandes-slices)
    
* [Utilisation incorrecte des variables de boucle avec des slices de pointeurs](#heading-utilisation-incorrecte-des-variables-de-boucle-avec-des-slices-de-pointeurs)
    
* [Modifier une slice pendant une itération range](#heading-modifier-une-slice-pendant-une-iteration-range)
    
* [Confusion entre Slice Nil et Slice Vide](#heading-confusion-entre-slice-nil-et-slice-vide)
    
* [Limites de slice et erreurs de panique](#heading-limites-de-slice-et-erreurs-de-panique)
    
* [Conclusion](#heading-conclusion)
    

## Passer des slices par valeur et s'attendre à des changements structurels

Une incompréhension courante consiste à s'attendre à ce que les modifications de la structure d'une slice (changements de longueur/capacité) dans une fonction affectent la slice originale à l'extérieur de la fonction.

Bien que les éléments d'une slice puissent être modifiés via les paramètres de fonction (car les slices contiennent un pointeur vers les données sous-jacentes), l'en-tête de la slice lui-même (contenant la longueur et la capacité) est passé par valeur.

Voici un exemple de cette idée fausse :

```go
func appendToSlice(s []int) {
    s = append(s, 4) // Ceci crée un nouvel en-tête de slice
    fmt.Println("À l'intérieur de la fonction :", s) // [1, 2, 3, 4]
}

func main() {
    slice := []int{1, 2, 3}
    appendToSlice(slice)
    fmt.Println("Après l'appel de la fonction :", slice) // Toujours [1, 2, 3]
}
```

Dans ce code, l'opération append à l'intérieur de la fonction crée un nouvel en-tête de slice, mais ce changement n'affecte pas la slice originale dans la fonction appelante.

### Comment le prévenir

Pour modifier la structure d'une slice depuis l'intérieur d'une fonction, retournez la slice modifiée ou utilisez un pointeur vers la slice :

```go
// Méthode 1 : Retourner la slice modifiée
func appendToSlice(s []int) []int {
    return append(s, 4)
}

// Méthode 2 : Utiliser un pointeur vers la slice
func appendToSlicePtr(s *[]int) {
    *s = append(*s, 4)
}

func main() {
    // Utilisation de la méthode 1
    slice1 := []int{1, 2, 3}
    slice1 = appendToSlice(slice1)
    fmt.Println("Méthode 1 :", slice1) // [1, 2, 3, 4]
    
    // Utilisation de la méthode 2
    slice2 := []int{1, 2, 3}
    appendToSlicePtr(&slice2)
    fmt.Println("Méthode 2 :", slice2) // [1, 2, 3, 4]
}
```

Les deux approches garantissent que les modifications de la structure de la slice sont visibles pour l'appelant.

## Partage d'en-tête de slice et mutations involontaires

Une autre erreur courante est de ne pas réaliser que les slices créées à partir du même tableau sous-jacent partagent les données. Ne pas le savoir peut provoquer des mutations inattendues lorsque vous modifiez une slice.

Les slices en Go sont des types référence qui contiennent un pointeur vers le tableau sous-jacent, ainsi que des informations sur la longueur et la capacité. Lorsque vous créez une slice à partir d'une autre slice, elles pointent toutes deux vers les mêmes données sous-jacentes.

Voici un exemple de la façon dont cela peut conduire à un comportement surprenant :

```go
func main() {
    original := []int{1, 2, 3, 4, 5}
    subset := original[1:4] // Crée [2, 3, 4]
    
    fmt.Println("Original :", original) // [1, 2, 3, 4, 5]
    fmt.Println("Subset :", subset)     // [2, 3, 4]
    
    subset[0] = 99 // Modifier le premier élément de subset
    
    fmt.Println("Original après modification :", original) // [1, 99, 3, 4, 5]
    fmt.Println("Subset après modification :", subset)     // [99, 3, 4]
}
```

Dans ce code, la modification de la slice `subset` modifie également la slice `original` car elles partagent le même tableau sous-jacent.

### **Comment le prévenir**

Pour éviter les mutations involontaires, utilisez la fonction `copy()` pour créer des slices indépendantes :

```go
func main() {
    original := []int{1, 2, 3, 4, 5}
    
    // Créer une copie indépendante
    subset := make([]int, 3)
    copy(subset, original[1:4])
    
    fmt.Println("Original :", original) // [1, 2, 3, 4, 5]
    fmt.Println("Subset :", subset)     // [2, 3, 4]
    
    subset[0] = 99
    
    fmt.Println("Original après modification :", original) // [1, 2, 3, 4, 5] - inchangé
    fmt.Println("Subset après modification :", subset)     // [99, 3, 4]
}
```

La fonction `copy()` garantit que les données sont dupliquées plutôt que partagées, évitant ainsi les effets secondaires indésirables.

## **Fuites de mémoire avec des références à de grandes slices**

Conserver des références à de petites slices dérivées de grandes slices est considéré comme une erreur mineure mais sérieuse. En effet, cela empêche le garbage collector de libérer le grand tableau sous-jacent, ce qui entraîne des fuites de mémoire.

Lorsque vous créez une slice à partir d'une slice plus grande, la nouvelle slice référence toujours l'intégralité du tableau d'origine, même si elle n'en utilise qu'une petite partie.

Voici un exemple de la façon dont cette fuite de mémoire peut se produire :

```go
func processLargeData() []byte {
    largeData := make([]byte, 1<<30) // Allouer 1 Go
    // ... remplir largeData avec des informations importantes ...
    
    // Extraire juste les 100 premiers octets
    return largeData[:100] // Fuite de mémoire : l'intégralité du Go reste en mémoire
}

func main() {
    result := processLargeData()
    // Même si result ne fait que 100 octets, 1 Go reste alloué
    fmt.Printf("Longueur du résultat : %d\n", len(result))
}
```

Dans ce code, même si nous n'avons besoin que des 100 premiers octets, l'intégralité du tableau de 1 Go reste en mémoire car notre slice retournée le référence toujours.

### **Comment le prévenir**

Pour éviter les fuites de mémoire, copiez les données nécessaires dans une nouvelle slice lorsque vous travaillez avec de grands ensembles de données :

```go
func processLargeData() []byte {
    largeData := make([]byte, 1<<30) // Allouer 1 Go
    // ... remplir largeData avec des informations importantes ...
    
    // Créer une copie indépendante des données nécessaires
    result := make([]byte, 100)
    copy(result, largeData[:100])
    
    return result // largeData peut maintenant être collecté par le garbage collector
}

func main() {
    result := processLargeData()
    // Seuls 100 octets restent en mémoire
    fmt.Printf("Longueur du résultat : %d\n", len(result))
}
```

En copiant les données dans une nouvelle slice, vous permettez au garbage collector de libérer le grand tableau lorsqu'il n'est plus nécessaire.

## **Utilisation incorrecte des variables de boucle avec des slices de pointeurs**

Il existe des scénarios ou des instances où vous créez ce qui ressemble à une boucle parfaitement raisonnable pour collecter des pointeurs, mais d'une manière ou d'une autre, tous vos pointeurs finissent par pointer vers la même valeur. C'est parce que Go réutilise la même variable de boucle à travers toutes les itérations, donc prendre son adresse aboutit toujours au même emplacement mémoire.

Voici un exemple de la façon dont cette erreur se manifeste :

```go
func main() {
    var ptrs []*int
    
    for i := 0; i < 3; i++ {
        ptrs = append(ptrs, &i) // Erreur : tous les pointeurs référencent la même variable
    }
    
    // Afficher les valeurs
    for j, ptr := range ptrs {
        fmt.Printf("ptrs[%d] = %d\n", j, *ptr)
    }
    // Sortie : Tous les pointeurs affichent la même valeur (3)
}
```

Dans ce code, tous les pointeurs de la slice pointent vers la même variable de boucle `i`, qui a la valeur finale de `3` une fois la boucle terminée.

### **Comment le prévenir**

Pour résoudre ce problème, créez une nouvelle variable à chaque itération ou utilisez l'indexation de slice :

```go
func main() {
    // Méthode 1 : Créer une nouvelle variable à chaque itération
    var ptrs1 []*int
    for i := 0; i < 3; i++ {
        j := i // Créer une nouvelle variable
        ptrs1 = append(ptrs1, &j)
    }
    
    // Méthode 2 : Utiliser une slice et l'indexer
    values := []int{0, 1, 2}
    var ptrs2 []*int
    for i := range values {
        ptrs2 = append(ptrs2, &values[i])
    }
    
    // Méthode 3 : Utiliser make et l'assignation directe
    values2 := make([]int, 3)
    var ptrs3 []*int
    for i := 0; i < 3; i++ {
        values2[i] = i
        ptrs3 = append(ptrs3, &values2[i])
    }
    
    // Toutes les méthodes fonctionnent maintenant correctement
    fmt.Println("Méthode 1 :", *ptrs1[0], *ptrs1[1], *ptrs1[2]) // 0 1 2
    fmt.Println("Méthode 2 :", *ptrs2[0], *ptrs2[1], *ptrs2[2]) // 0 1 2
    fmt.Println("Méthode 3 :", *ptrs3[0], *ptrs3[1], *ptrs3[2]) // 0 1 2
}
```

Ces approches garantissent que chaque pointeur référence un emplacement mémoire unique avec la valeur correcte.

## **Modifier une slice pendant une itération range**

Modifier une slice tout en l'parcourant avec une boucle `range` peut entraîner des problèmes tels que des éléments ignorés, des boucles infinies ou le traitement de mauvaises données, selon le type de modification.

Lorsque vous utilisez `range` sur une slice, Go évalue la longueur de la slice au début de la boucle. Cependant, si vous modifiez la slice pendant l'itération, la longueur réelle de la slice peut changer alors que la boucle continue sur la base de la longueur d'origine.

Voici un exemple de la façon dont cela peut causer des problèmes :

```go
func removeEvenNumbers() {
    numbers := []int{1, 2, 3, 4, 5, 6, 7, 8}
    fmt.Println("Original :", numbers)
    
    // Dangereux : modification de la slice pendant l'itération range
    for i, num := range numbers {
        if num%2 == 0 {
            // Supprimer le nombre pair par découpage (slicing)
            numbers = append(numbers[:i], numbers[i+1:]...)
        }
    }
    
    fmt.Println("Après suppression :", numbers) // Résultat inattendu !
}

func main() {
    removeEvenNumbers()
    // La sortie pourrait être : [1 3 5 7 8] - remarquez que le 8 n'a pas été supprimé !
}
```

Dans ce code, la suppression d'éléments pendant l'itération provoque un décalage des indices, ce qui conduit à l'omission de certains éléments. Le nombre `8` reste car lorsque `6` est supprimé, `8` se déplace vers une position qui a déjà été traitée par la boucle.

### **Comment le prévenir**

Pour modifier en toute sécurité des slices pendant l'itération, itérez dans l'ordre inverse, utilisez une slice de résultat séparée ou collectez d'abord les indices :

```go
// Méthode 1 : Itérer en sens inverse pour éviter les problèmes de décalage d'index
func removeEvenNumbersReverse() {
    numbers := []int{1, 2, 3, 4, 5, 6, 7, 8}
    fmt.Println("Original :", numbers)
    
    for i := len(numbers) - 1; i >= 0; i-- {
        if numbers[i]%2 == 0 {
            numbers = append(numbers[:i], numbers[i+1:]...)
        }
    }
    
    fmt.Println("Après suppression :", numbers) // [1, 3, 5, 7]
}

// Méthode 2 : Construire une nouvelle slice avec les éléments souhaités
func filterOddNumbers() []int {
    numbers := []int{1, 2, 3, 4, 5, 6, 7, 8}
    var result []int
    
    for _, num := range numbers {
        if num%2 != 0 { // Garder les nombres impairs
            result = append(result, num)
        }
    }
    
    return result // [1, 3, 5, 7]
}

// Méthode 3 : Collecter d'abord les indices, puis modifier
func removeEvenNumbersByIndex() {
    numbers := []int{1, 2, 3, 4, 5, 6, 7, 8}
    var toRemove []int
    
    // Première passe : collecter les indices des nombres pairs
    for i, num := range numbers {
        if num%2 == 0 {
            toRemove = append(toRemove, i)
        }
    }
    
    // Seconde passe : supprimer dans l'ordre inverse
    for i := len(toRemove) - 1; i >= 0; i-- {
        idx := toRemove[i]
        numbers = append(numbers[:idx], numbers[idx+1:]...)
    }
    
    fmt.Println("Résultat :", numbers) // [1, 3, 5, 7]
}
```

Ces approches garantissent que vos modifications n'interfèrent pas avec le processus d'itération, vous donnant des résultats prévisibles et corrects.

## **Confusion entre Slice Nil et Slice Vide**

Une autre source de confusion est de ne pas comprendre la différence entre les slices `nil` et les slices vides, ce qui peut entraîner un comportement incohérent dans vos applications.

Une slice `nil` n'a pas de tableau sous-jacent, tandis qu'une slice vide a un tableau sous-jacent mais ne contient aucun élément.

Voici un exemple qui démontre les différences :

```go
func main() {
    var nilSlice []int
    emptySlice := []int{}
    emptySlice2 := make([]int, 0)
    
    fmt.Printf("nilSlice == nil : %t\n", nilSlice == nil)       // true
    fmt.Printf("emptySlice == nil : %t\n", emptySlice == nil)   // false
    fmt.Printf("emptySlice2 == nil : %t\n", emptySlice2 == nil) // false
    
    // Le marshaling JSON se comporte différemment
    nilJSON, _ := json.Marshal(nilSlice)
    emptyJSON, _ := json.Marshal(emptySlice)
    
    fmt.Printf("JSON de slice Nil : %s\n", nilJSON)   // null
    fmt.Printf("JSON de slice vide : %s\n", emptyJSON) // []
}
```

Cette différence peut causer des problèmes lors de l'utilisation d'API JSON ou lorsque des fonctions attendent des états de slice spécifiques.

### **Comment le prévenir**

Soyez explicite sur vos intentions et gérez les deux cas de manière cohérente. Une bonne pratique consisterait à vérifier la longueur au lieu de `nil` lorsque cela est important :

```go
func processSlice(s []int) {
    if len(s) == 0 { // Fonctionne pour les slices nil et vides
        fmt.Println("La slice est vide")
        return
    }
    fmt.Printf("Traitement de %d éléments\n", len(s))
}

// Initialiser les slices nil si nécessaire
func ensureSliceInitialized(s []int) []int {
    if s == nil {
        return make([]int, 0) // ou []int{} si vous préférez une slice vide non-nil
    }
    return s
}

func main() {
    var nilSlice []int
    emptySlice := []int{}
    
    processSlice(nilSlice)  // Fonctionne de manière cohérente
    processSlice(emptySlice) // Fonctionne de manière cohérente
    
    nilSlice = ensureSliceInitialized(nilSlice)
    fmt.Printf("Après initialisation : %t\n", nilSlice == nil) // false
}
```

Cette approche garantit un comportement cohérent, que vous travailliez avec des slices `nil` ou vides.

## **Limites de slice et erreurs de panique**

La dernière erreur courante est de ne pas valider les limites de la slice avant d'accéder aux éléments. Lorsque vous ne validez pas les limites d'une slice, vous la rendez sujette à des paniques à l'exécution qui peuvent faire planter votre application.

Go ne fournit pas de vérification automatique des limites pour les opérations sur les slices, il est donc de votre responsabilité de vous assurer que les indices se situent dans des plages valides.

Voici un exemple d'opérations de slice dangereuses :

```go
func dangerousSliceOperations(s []int, index int, start int, end int) {
    // Dangereux : peut paniquer si l'index est hors limites
    value := s[index]
    fmt.Printf("Valeur à l'index %d : %d\n", index, value)
    
    // Également dangereux : peut paniquer si les limites sont invalides
    subset := s[start:end]
    fmt.Printf("Sous-ensemble [%d:%d] : %v\n", start, end, subset)
}

func main() {
    slice := []int{1, 2, 3, 4, 5}
    
    // Ceux-ci provoqueront des paniques
    // dangerousSliceOperations(slice, 10, 2, 8) // index hors limites
    // dangerousSliceOperations(slice, 0, -1, 3) // index négatif
}
```

Ces opérations provoqueront des paniques à l'exécution lorsque les limites sont invalides, ce qui pourrait faire planter votre application.

### **Comment le prévenir**

Pour éviter cela, vous devez toujours valider les limites avant d'accéder aux éléments d'une slice :

```go
// Accès sécurisé aux éléments avec gestion des erreurs
func safeGetElement(s []int, index int) (int, error) {
    if index < 0 || index >= len(s) {
        return 0, fmt.Errorf("index %d hors limites pour une slice de longueur %d", index, len(s))
    }
    return s[index], nil
}

// Opérations de slice sécurisées avec gestion des erreurs
func safeGetSubslice(s []int, start, end int) ([]int, error) {
    if start < 0 || end > len(s) || start > end {
        return nil, fmt.Errorf("limites de slice invalides [%d:%d] pour une slice de longueur %d", start, end, len(s))
    }
    return s[start:end], nil
}

// Aide à la vérification des limites qui restreint les valeurs
func clampedSlice(s []int, start, end int) []int {
    if start < 0 {
        start = 0
    }
    if end > len(s) {
        end = len(s)
    }
    if start > end {
        start = end
    }
    return s[start:end]
}

func main() {
    slice := []int{1, 2, 3, 4, 5}
    
    // Accès sécurisé avec gestion des erreurs
    if value, err := safeGetElement(slice, 2); err == nil {
        fmt.Printf("Élément à l'index 2 : %d\n", value)
    }
    
    if subset, err := safeGetSubslice(slice, 1, 4); err == nil {
        fmt.Printf("Sous-ensemble [1:4] : %v\n", subset)
    }
    
    // Accès avec limites restreintes (ne panique jamais)
    clamped := clampedSlice(slice, -1, 10)
    fmt.Printf("Slice restreinte : %v\n", clamped) // [1, 2, 3, 4, 5]
}
```

Ces approches offrent des alternatives sûres qui soit gèrent les erreurs avec élégance, soit garantissent que les opérations ne dépassent jamais les limites valides.

## **Conclusion**

Dans cet article, nous avons examiné sept problèmes fréquents qui peuvent survenir lors de l'utilisation des slices en Go. Ces problèmes découlent souvent du comportement subtil de l'implémentation des slices de Go, en particulier autour du partage de mémoire, de la distinction entre les en-têtes de slice et les tableaux sous-jacent, et de la sémantique de référence des slices.

En comprenant ces pièges et en mettant en œuvre les stratégies de prévention dont nous avons discuté, vous pouvez écrire des applications Go plus robustes et efficaces. N'oubliez pas de toujours prendre en compte la capacité par rapport à la longueur de la slice, d'être attentif aux données sous-jacentes partagées, de valider les limites avant d'accéder aux éléments et de comprendre les implications du passage de slices aux fonctions.

Maîtriser ces concepts vous aidera à exploiter toute la puissance des slices de Go tout en évitant les pièges courants qui peuvent mener à des bugs et des problèmes de performance dans vos applications.

N'oubliez pas de partager.