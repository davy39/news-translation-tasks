---
title: My favorite examples of functional programming in Kotlin
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
seo_title: null
seo_desc: 'By Marcin Moskala

  One of the great things about Kotlin is that it supports functional programming.
  Let’s see and discuss some simple but expressive functions written in Kotlin.


  Collection processing

  Kotlin has some of the best support for collection...'
---

By Marcin Moskala

One of the great things about Kotlin is that it supports functional programming. Let’s see and discuss some simple but expressive functions written in Kotlin.

![Image](https://cdn-media-1.freecodecamp.org/images/bpsAIvlpGbHPATxHWfcxBL1XaS8o9YzE1o56)

### Collection processing

Kotlin has some of the best support for collection processing. It is expressive and supports a lot of functions. To see an example, let’s say that we make a system for a University. We need to find the best students that deserve a scholarship. We have following `Student` model:

```kotlin
class Student(
    val name: String,
    val surname: String,
    val passing: Boolean,
    val averageGrade: Double
)
```

Now we can make the following processing to get a list of the best 10 students that match all criteria:

```kotlin
students.filter { it.passing && it.averageGrade > 4.0 } // 1
    .sortedBy { it.averageGrade } // 2
    .take(10) // 3
    .sortedWith(compareBy({ it.surname }, { it.name })) // 4
```

1. We get only students who are passing and with a grade point average of greater than 4.0.
2. We sort by the average grade.
3. We take first 10 students.
4. We sort students alphanumerically. The comparator compares surnames first, and if equal then it compares names.

What if, instead of alphanumerical order, we need to keep students in the same order as they were before? What we can do is preserve the order using indexes:

```kotlin
students.filter { it.passing && it.averageGrade > 4.0 }
    .withIndex() // 1
    .sortedBy { (i, s) -> s.averageGrade } // 2
    .take(10)
    .sortedBy { (i, s) -> i } // 3
    .map { (i, s) -> s } // 4
```

1. We add current index to every element.
2. We need to [destructure](https://kotlinlang.org/docs/reference/multi-declarations.html) value and index before use.
3. We sort by index.
4. We remove index and keep only students.

This shows how simple and intuitive collection processing in Kotlin is.

![Image](https://cdn-media-1.freecodecamp.org/images/rtCcHJSwA5EDuSEqe2MX6E7tHJS-vNtvTJS8)

### Powerset

If you had algebra at your University, then you might remember what a powerset is. For any set, its powerset is the set of all its subsets including this set and the empty set. For instance, if we have the following set:

`{1,2,3}`

Its powerset is the following:

`{{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}`

Such a function is very useful in algebra. How can we implement it?

If you want to challenge yourself, then stop right now and try to solve it yourself first.

Let’s start our analysis from simple observation. If we take any element of the set (like 1), then the powerset will include an equal number of sets with these elements `({1}, {1,2}, {1,3}, {1,2,3})`, and without these `({}, {2}, {3}, {2,3})`.

Note that the second is a `powerset({2,3})`, and the first is a `powerset({2,3})` with 1 added to every set. So we can calculate the powerset by taking the first element, calculating the powerset for all others, and returning the sum of the result and the result with the first element added to every set:

```kotlin
fun <T> powerset(set: Set<T>): Set<Set<T>> {
   val first = set.first()
   val powersetOfRest = powerset(set.drop(1))
   return powersetOfRest.map { it + first } + powersetOfRest
}
```

The above declaration will not work correctly. The problem is with the empty set: `first` will throw an error when the set is empty. Here, the definition comes with a solution: powerset({}) = {{}}. When we fix it, we will have our algorithm ready:

```kotlin
fun <T> powerset(set: Set<T>): Set<Set<T>> =
    if (set.isEmpty()) setOf(emptySet())
    else {
       val powersetOfRest = powerset(set.drop(1))
       powersetOfRest + powersetOfRest.map { it + set.first() }
    }
```

![Image](https://cdn-media-1.freecodecamp.org/images/YNPYNMMoDmdl-fJTrnbuC-VQnPgROvW737hq)

Let’s see how it works. Let’s say we need to calculate the `powerset({1,2,3})`. The algorithm will count it this way:

`powerset({1,2,3}) = powerset({2,3}) + powerset({2,3}).map { it + 1 }`

`powerset({2,3}) = powerset({3}) + powerset({3}).map { it + 2}`

`powerset({3}) = powerset({}) + powerset({}).map { it + 3}`

`powerset({}) = {{}}`

`powerset({3}) = {{}, {3}}`

`powerset({2,3}) = {{}, {3}} + {{2}, {2, 3}} = {{}, {2}, {3}, {2, 3}}`

`powerset({1,2,3}) = {{}, {2}, {3}, {2, 3}} + {{1}, {1, 2}, {1, 3}, {1, 2, 3}} = {{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}`

The above function can be improved. We can use the `let` function to make the notation shorter and more compact:

```kotlin
fun <T> powerset(set: Set<T>): Set<Set<T>> =
    if (set.isEmpty()) setOf(emptySet())
    else powerset(set.drop(1))
           .let { it+ it.map { it + set.first() }
```

We can also define this function as an extension function to `Collection` so we can use this function as if it is the method of `Set` (`setOf(1,2,3).powerset()` instead of `powerset(setOf(1,2,3))`):

```kotlin
fun <T> Collection<T>.powerset(): Set<Set<T>> =
    if (isEmpty()) setOf(emptySet())
    else drop(1)
           .powerset()
           .let { it+ it.map { it + first() }
```

One big improvement is to make the `powerset` tail recursive. In the above implementation, the state of `powerset` is growing with every iteration (recurrent call), because the state of the previous iteration needs to be kept in the memory.

Instead, we could use an imperative loop or the `tailrec` modifier. We will use the second option to maintain the readability of the function. The `tailrec` modifier allows only a single recursive call in the last statement. This is how we can change our function to use it effectively:

```kotlin
fun <T> Collection<T>.powerset(): Set<Set<T>> = 
    powerset(this, setOf(emptySet()))

private tailrec fun <T> powerset(left: Collection<T>, acc: Set<Set<T>>): Set<Set<T>> =
    if (left.isEmpty()) acc
    else powerset(left.drop(1), acc + acc.map { it + left.first() })
```

The above implementation is part of the [KotlinDiscreteMathToolkit](https://github.com/MarcinMoskala/KotlinDiscreteMathToolkit) library, which defines a lot of other functions used in discrete math.

### Quicksort

Time for my favorite example. We’ll see how a difficult problem can be simplified and made highly readable using a functional programming style and tools.

We will implement the [Quicksort](https://en.wikipedia.org/wiki/Quicksort) algorithm. The algorithm is simple: we choose some element (pivot) and we distribute all other elements to the list with bigger and smaller elements than the pivot. Then we recursively sort these sub-arrays. Finally, we add the sorted list of smaller elements, the pivot, and the sorted list of bigger elements. For simplification, we will take the first element as a pivot. Here is the full implementation:

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

Looks great, doesn’t it? This is the beauty of functional programming.

![Image](https://cdn-media-1.freecodecamp.org/images/emNxRiIIWRrws3g6FbGv2PcUQDyjzd0Tp2Um)

The first concern of such a function is its execution time. It is not optimized for performance at all. Instead, it is short and highly readable.

If you need a highly optimized function, then you can use one from the Java standard library. It is based on different algorithms depending on some conditions, and it has actual implementations written naively. It should be much more efficient. But how much exactly? Let’s compare these two functions. Let’s sort a few different arrays with random elements and compare execution times. Here is the code I’ve used for this purpose:

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

On my machine I got the following result:

Java stdlib sorting of 100000 elements took 83  
quickSort sorting of 100000 elements took 163  
Java stdlib sorting of 1000000 elements took 558  
quickSort sorting of 1000000 elements took 859  
Java stdlib sorting of 10000000 elements took 6182  
quickSort sorting of 10000000 elements took 12133`

As we can see, the `quickSort` function is generally 2 times slower. Even for huge lists. It has the same scalability. In normal cases, the difference will generally be between 0.1ms vs 0.2ms. Note that it is much simpler and more readable. This explains why in some cases we can use a function that’s a bit less optimized, but readable and simple.

If you are interested in Kotlin, check out [Kotlin Academy](https://blog.kotlin-academy.com/). It is great publication and community dedicated for Kotlin. 

I am also publishing great resources on my [Twitter](https://twitter.com/marcinmoskala). To mention me there use [@marcinmoskala](https://twitter.com/marcinmoskala). If you can use my help, remember that [I am open for consultations](https://medium.com/@marcinmoskala/ive-just-opened-up-for-online-consultations-640349aaba55).

