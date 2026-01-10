---
title: Mes exemples préférés de programmation fonctionnelle en Kotlin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-08T14:49:32.000Z'
originalURL: https://freecodecamp.org/news/my-favorite-examples-of-functional-programming-in-kotlin-e69217b39112
coverImage: https://cdn-media-1.freecodecamp.org/images/0*X2-yHGibmWx5pAWN.jpg
tags:
- name: coding
  slug: coding
- name: Kotlin
  slug: kotlin
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Mes exemples préférés de programmation fonctionnelle en Kotlin
seo_desc: 'By Marcin Moskala

  One of the great things about Kotlin is that it supports functional programming.
  Let’s see and discuss some simple but expressive functions written in Kotlin.


  Collection processing

  Kotlin has some of the best support for collection...'
---

Par Marcin Moskala

L'une des grandes qualités de Kotlin est qu'il supporte la programmation fonctionnelle. Examinons et discutons de quelques fonctions simples mais expressives écrites en Kotlin.

![Image](https://cdn-media-1.freecodecamp.org/images/bpsAIvlpGbHPATxHWfcxBL1XaS8o9YzE1o56)

### Traitement des collections

Kotlin offre l'un des meilleurs supports pour le traitement des collections. Il est expressif et supporte de nombreuses fonctions. Pour voir un exemple, supposons que nous créons un système pour une université. Nous devons trouver les meilleurs étudiants qui méritent une bourse. Nous avons le modèle `Student` suivant :

```kotlin
class Student(
    val name: String,
    val surname: String,
    val passing: Boolean,
    val averageGrade: Double
)
```

Maintenant, nous pouvons effectuer le traitement suivant pour obtenir une liste des 10 meilleurs étudiants qui répondent à tous les critères :

```kotlin
students.filter { it.passing && it.averageGrade > 4.0 } // 1
    .sortedBy { it.averageGrade } // 2
    .take(10) // 3
    .sortedWith(compareBy({ it.surname }, { it.name })) // 4
```

1. Nous obtenons uniquement les étudiants qui réussissent et dont la moyenne est supérieure à 4,0.
2. Nous trions par la moyenne.
3. Nous prenons les 10 premiers étudiants.
4. Nous trions les étudiants par ordre alphanumérique. Le comparateur compare d'abord les noms de famille, et si ils sont égaux, il compare les prénoms.

Que faire si, au lieu de l'ordre alphanumérique, nous devons conserver les étudiants dans le même ordre qu'avant ? Ce que nous pouvons faire, c'est préserver l'ordre en utilisant des index :

```kotlin
students.filter { it.passing && it.averageGrade > 4.0 }
    .withIndex() // 1
    .sortedBy { (i, s) -> s.averageGrade } // 2
    .take(10)
    .sortedBy { (i, s) -> i } // 3
    .map { (i, s) -> s } // 4
```

1. Nous ajoutons l'index actuel à chaque élément.
2. Nous devons [déstructurer](https://kotlinlang.org/docs/reference/multi-declarations.html) la valeur et l'index avant de les utiliser.
3. Nous trions par index.
4. Nous supprimons l'index et gardons uniquement les étudiants.

Cela montre à quel point le traitement des collections en Kotlin est simple et intuitif.

![Image](https://cdn-media-1.freecodecamp.org/images/rtCcHJSwA5EDuSEqe2MX6E7tHJS-vNtvTJS8)

### Ensemble des parties (Powerset)

Si vous avez étudié l'algèbre à l'université, vous vous souvenez peut-être de ce qu'est un ensemble des parties. Pour tout ensemble, son ensemble des parties est l'ensemble de tous ses sous-ensembles, y compris cet ensemble et l'ensemble vide. Par exemple, si nous avons l'ensemble suivant :

`{1,2,3}`

Son ensemble des parties est le suivant :

`{{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}`

Une telle fonction est très utile en algèbre. Comment pouvons-nous l'implémenter ?

Si vous voulez vous challenger, arrêtez-vous ici et essayez de le résoudre vous-même d'abord.

Commençons notre analyse par une observation simple. Si nous prenons n'importe quel élément de l'ensemble (comme 1), alors l'ensemble des parties inclura un nombre égal d'ensembles avec ces éléments `({1}, {1,2}, {1,3}, {1,2,3})`, et sans ces éléments `({}, {2}, {3}, {2,3})`.

Notez que le second est un `powerset({2,3})`, et le premier est un `powerset({2,3})` avec 1 ajouté à chaque ensemble. Nous pouvons donc calculer l'ensemble des parties en prenant le premier élément, en calculant l'ensemble des parties pour tous les autres, et en retournant la somme du résultat et du résultat avec le premier élément ajouté à chaque ensemble :

```kotlin
fun <T> powerset(set: Set<T>): Set<Set<T>> {
   val first = set.first()
   val powersetOfRest = powerset(set.drop(1))
   return powersetOfRest.map { it + first } + powersetOfRest
}
```

La déclaration ci-dessus ne fonctionnera pas correctement. Le problème est avec l'ensemble vide : `first` lèvera une erreur lorsque l'ensemble est vide. Ici, la définition vient avec une solution : powerset({}) = {{}}. Lorsque nous le corrigeons, nous aurons notre algorithme prêt :

```kotlin
fun <T> powerset(set: Set<T>): Set<Set<T>> =
    if (set.isEmpty()) setOf(emptySet())
    else {
       val powersetOfRest = powerset(set.drop(1))
       powersetOfRest + powersetOfRest.map { it + set.first() }
    }
```

![Image](https://cdn-media-1.freecodecamp.org/images/YNPYNMMoDmdl-fJTrnbuC-VQnPgROvW737hq)

Voyons comment cela fonctionne. Supposons que nous devons calculer le `powerset({1,2,3})`. L'algorithme le calculera de cette manière :

`powerset({1,2,3}) = powerset({2,3}) + powerset({2,3}).map { it + 1 }`

`powerset({2,3}) = powerset({3}) + powerset({3}).map { it + 2}`

`powerset({3}) = powerset({}) + powerset({}).map { it + 3}`

`powerset({}) = {{}}`

`powerset({3}) = {{}, {3}}`

`powerset({2,3}) = {{}, {3}} + {{2}, {2, 3}} = {{}, {2}, {3}, {2, 3}}`

`powerset({1,2,3}) = {{}, {2}, {3}, {2, 3}} + {{1}, {1, 2}, {1, 3}, {1, 2, 3}} = {{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}`

La fonction ci-dessus peut être améliorée. Nous pouvons utiliser la fonction `let` pour rendre la notation plus courte et plus compacte :

```kotlin
fun <T> powerset(set: Set<T>): Set<Set<T>> =
    if (set.isEmpty()) setOf(emptySet())
    else powerset(set.drop(1))
           .let { it+ it.map { it + set.first() }
```

Nous pouvons également définir cette fonction comme une fonction d'extension de `Collection` afin de pouvoir utiliser cette fonction comme si c'était la méthode de `Set` (`setOf(1,2,3).powerset()` au lieu de `powerset(setOf(1,2,3))`) :

```kotlin
fun <T> Collection<T>.powerset(): Set<Set<T>> =
    if (isEmpty()) setOf(emptySet())
    else drop(1)
           .powerset()
           .let { it+ it.map { it + first() }
```

Une grande amélioration consiste à rendre `powerset` récursif terminal. Dans l'implémentation ci-dessus, l'état de `powerset` grandit avec chaque itération (appel récurrent), car l'état de l'itération précédente doit être conservé en mémoire.

Au lieu de cela, nous pourrions utiliser une boucle impérative ou le modificateur `tailrec`. Nous utiliserons la deuxième option pour maintenir la lisibilité de la fonction. Le modificateur `tailrec` permet uniquement un seul appel récursif dans la dernière instruction. Voici comment nous pouvons modifier notre fonction pour l'utiliser efficacement :

```kotlin
fun <T> Collection<T>.powerset(): Set<Set<T>> = 
    powerset(this, setOf(emptySet()))

private tailrec fun <T> powerset(left: Collection<T>, acc: Set<Set<T>>): Set<Set<T>> =
    if (left.isEmpty()) acc
    else powerset(left.drop(1), acc + acc.map { it + left.first() })
```

L'implémentation ci-dessus fait partie de la bibliothèque [KotlinDiscreteMathToolkit](https://github.com/MarcinMoskala/KotlinDiscreteMathToolkit), qui définit de nombreuses autres fonctions utilisées en mathématiques discrètes.

### Quicksort

Il est temps pour mon exemple préféré. Nous verrons comment un problème difficile peut être simplifié et rendu hautement lisible en utilisant un style de programmation fonctionnelle et des outils.

Nous allons implémenter l'algorithme [Quicksort](https://en.wikipedia.org/wiki/Quicksort). L'algorithme est simple : nous choisissons un élément (pivot) et nous distribuons tous les autres éléments dans la liste avec des éléments plus grands et plus petits que le pivot. Ensuite, nous trions récursivement ces sous-tableaux. Enfin, nous ajoutons la liste triée des éléments plus petits, le pivot et la liste triée des éléments plus grands. Pour simplifier, nous prendrons le premier élément comme pivot. Voici l'implémentation complète :

```kotlin
fun <T : Comparable<T>> List<T>.quickSort(): List<T> = 
    if(size < 2) this
    else {
        val pivot = first()
        val (smaller, greater) = drop(1).partition { it <= pivot}
        smaller.quickSort() + pivot + greater.quickSort()
    }
// Usage
listOf(2,5,1).quickSort() // [1,2,5]
```

Cela semble génial, n'est-ce pas ? C'est la beauté de la programmation fonctionnelle.

![Image](https://cdn-media-1.freecodecamp.org/images/emNxRiIIWRrws3g6FbGv2PcUQDyjzd0Tp2Um)

La première préoccupation d'une telle fonction est son temps d'exécution. Elle n'est pas du tout optimisée pour la performance. Au lieu de cela, elle est courte et hautement lisible.

Si vous avez besoin d'une fonction hautement optimisée, vous pouvez utiliser celle de la bibliothèque standard Java. Elle est basée sur différents algorithmes selon certaines conditions, et elle a des implémentations réelles écrites de manière naïve. Elle devrait être beaucoup plus efficace. Mais dans quelle mesure exactement ? Comparons ces deux fonctions. Trions quelques tableaux différents avec des éléments aléatoires et comparons les temps d'exécution. Voici le code que j'ai utilisé à cette fin :

```kotlin
val r = Random()
listOf(100_000, 1_000_000, 10_000_000)
    .asSequence()
    .map { (1..it).map { r.nextInt(1000000000) } }
    .forEach { list: List<Int> ->
        println("Java stdlib sorting of ${list.size} elements took ${measureTimeMillis { list.sorted() }}")
        println("quickSort sorting of ${list.size} elements took ${measureTimeMillis { list.quickSort() }}")
    }
```

Sur ma machine, j'ai obtenu le résultat suivant :

Java stdlib sorting of 100000 elements took 83  
quickSort sorting of 100000 elements took 163  
Java stdlib sorting of 1000000 elements took 558  
quickSort sorting of 1000000 elements took 859  
Java stdlib sorting of 10000000 elements took 6182  
quickSort sorting of 10000000 elements took 12133`

Comme nous pouvons le voir, la fonction `quickSort` est généralement 2 fois plus lente. Même pour les grandes listes. Elle a la même évolutivité. Dans les cas normaux, la différence sera généralement entre 0,1 ms et 0,2 ms. Notez qu'elle est beaucoup plus simple et plus lisible. Cela explique pourquoi dans certains cas nous pouvons utiliser une fonction un peu moins optimisée, mais lisible et simple.

Si vous êtes intéressé par Kotlin, consultez [Kotlin Academy](https://blog.kotlin-academy.com/). C'est une excellente publication et communauté dédiée à Kotlin. 

Je publie également de grandes ressources sur mon [Twitter](https://twitter.com/marcinmoskala). Pour me mentionner là-bas, utilisez [@marcinmoskala](https://twitter.com/marcinmoskala). Si vous pouvez utiliser mon aide, n'oubliez pas que [je suis ouvert pour des consultations](https://medium.com/@marcinmoskala/ive-just-opened-up-for-online-consultations-640349aaba55).