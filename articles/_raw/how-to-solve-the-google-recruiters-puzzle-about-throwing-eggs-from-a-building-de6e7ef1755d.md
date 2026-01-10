---
title: How to solve the Google recruiters’ puzzle about throwing eggs from a building
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T08:28:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-the-google-recruiters-puzzle-about-throwing-eggs-from-a-building-de6e7ef1755d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Uq3d3wn7B8yOPGIK.jpg
tags:
- name: Google
  slug: google
- name: interview
  slug: interview
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Marcin Moskala

  There are a lot of great puzzles for programming job interviews. My favorite one
  is also known as one of the favorites among Google recruiters:


  You work in a 100 floor building and you get 2 identical eggs. You need to figure
  out t...'
---

By Marcin Moskala

There are a lot of great puzzles for programming job interviews. My favorite one is also known as one of the favorites among Google recruiters:

> You work in a 100 floor building and you get 2 identical eggs. You need to figure out the highest floor an egg can be dropped without breaking. Find an algorithm that is minimizing number of throws in the worst-case scenario.

We can make a few assumptions:

* If an egg doesn’t break when dropped from some floor, then it will not break when dropped from any lower floors.
* An egg that survives a fall can be used again.
* A broken egg must be discarded.
* The effect of a fall is the same for all eggs.
* If an egg breaks when dropped, then it would break if dropped from a higher floor.

Most people writes some algorithms to solve this puzzle (and we will do it too), but there is actually an easy solution.

#### Simplest answer

The simplest way to obtain the minimal floor is to throw an egg from the first floor, then from the second and so on. This way when the egg is finally broken then we will know that this is the floor. This is a reliable algorithm, but in the worst-case scenario it would take 100 throws.

The important thing to notice is that it is the only reliable algorithm when you have only one egg. So you need to start using this algorithm when you break the first egg.

#### Intuitive answer

This way, our first egg should be used to split the 100 floors range into smaller ranges as efficiently as possible. Thus, an intuitive and popular answer is to throw the first egg from 1/n-th of the floors to check. For instance 1/3. Then the algorithm will look like the following:

* Throw the egg from 33rd floor. If it breaks, then we check the first 32 floors using the second egg.
* Otherwise, we throw the egg from 33 + (67 * 1/3) = 55th floor. If it breaks, then we check floors 34 to 55 using the second egg.
* …

Worst case scenario for 1/3 is max(33, 24, …) = 33. This way we might find a perfect n that optimizes the number of throws using some dynamic programming. This is a valuable solution that presents programming thinking, but it is not an optimal solution.

#### Perfect solution

To understand the perfect solution, we need to understand the equilibrium that is used to calculate the number of throws in the worst case scenario:

![Image](https://cdn-media-1.freecodecamp.org/images/OolWyrKqqniWgpZFcEXGMM8mey-gDM94m5Ln)

Where F(n) is the next floor from which we throw the first egg

If we introduce following variable:

![Image](https://cdn-media-1.freecodecamp.org/images/aksQXa8OxxKjmyWm4sH1JAygveWHijT0fMBB)

then equilibrium is following:

![Image](https://cdn-media-1.freecodecamp.org/images/WFWn-DWbpK3pgWfCAKq1Jgf6CWTjZdLyPwyZ)

The optimal solution is when all [arguments](https://blog.kotlin-academy.com/programmer-dictionary-parameter-vs-argument-type-parameter-vs-type-argument-b965d2cc6929) of this max function are equal. How do we achieve it? Looking from the end, the last D(n) is going to be 1, because we will finally get to the point where there is only the single floor for the first egg. Therefore D(n-1) should be equal to 2 because it has one less throw of the first egg.

We see then that the first egg should be thrown finally from the 99th floor, previously from 99–2=97, previously from 97–3=94, 90, 85, 79, 72, 64, 55, 45, 34, 22 and the 9th floor. **This is an optimal solution!** This way, we need 14 throws in the worst case scenario (the smallest difference is 13, but we had to make one extra throw on the 9th floor).

Simple equation to find the answer is following:

![Image](https://cdn-media-1.freecodecamp.org/images/7McAQgwk2rOkUR9Qc7g3-4Yz5HYBWFNi3JMG)

Where `f` is number of floors. This can be simplified to:

![Image](https://cdn-media-1.freecodecamp.org/images/XzJrN3BfcOlZgyoUgnjLSyznLhWyQ1MG9mu-)

That is equal to:

![Image](https://cdn-media-1.freecodecamp.org/images/EY22gKaNq7dvfRNd7Qo4wAdkQ36gubIzatvq)

#### Check

OK, so we have a solution and we can calculate it without any help. It is time to check if it is correct. We will write a simple Kotlin program for that. First, let’s express how to count the number of throws for some decision. When there are 2 or fewer floors, then we need as many throws as there are floors left. Otherwise we should use the already presented equilibrium:

```
fun maxThrows(floorsLeft: Int, nextFloor: Int): Int =  if (floorsLeft <= 2) floorsLeft  else maxOf(nextFloor, bestMaxThrows(floorsLeft - nextFloor) + 1)
```

We’ve used here the `bestMaxThrows` function. It is a hypothetical function that returns a number of throws supposing that the next decisions are perfect. This is how we can define it:

```
fun bestMaxThrows(floorsLeft: Int): Int =  maxThrows(floorsLeft, bestNextStep(floorsLeft))
```

Again, we’ve just delegated the responsibility of next floor optimization to `_bestNextStep_` function. This function gives us the best next step. We can define it simply — when 2 or fewer floors are left, then we will throw an egg from the first floor. Otherwise we need to check all options and find the optimal one. Here is the implementation:

```
val bestNextStep(floorsLeft: Int): Int =   if (floorsLeft <= 2) 1  else (1..floorsLeft)        .toList()        .minBy { maxThrows(floorsLeft, it) }!!
```

Note that this function uses the `_maxThrows_` function, so we deal with recurrence. It is not a problem, because when `bestNextStep` calls `maxThrows`, it always calls it with a smaller value then `floorsLeft` (because `nextFloor` is always bigger than 0). Before we use it we will add buffering to speed up the calculations:

```
val bestNextStep: (Int) -> Int = memorise { floorsLeft ->  if (floorsLeft <= 2) 1  else (1..floorsLeft)        .toList()        .minBy { maxThrows(floorsLeft, it) }!!}fun maxThrows(floorsLeft: Int, nextFloor: Int): Int =  if (floorsLeft <= 2) floorsLeft  else maxOf(nextFloor, bestMaxThrows(floorsLeft - nextFloor) + 1)val bestMaxThrows: (Int) -> Int = memorise { floorsLeft ->  maxThrows(floorsLeft, bestNextStep(floorsLeft))}fun <V, T> memorise(f: (V) -&gt; T): (V) -> T {    val map = mutableMapOf<V, T&gt;()    return { map.getOrPut(it) { f(it) } }}
```

First, we can check if it returns the same result as the one we have calculated:

```
fun main(args: Array<String>) {    print(bestMaxThrows(100)) // Prints: 14}
```

The answer is good :) Let’s check out our next steps:

```
fun main(args: Array<String>) {    var floor = 0    while (floor < 100) {        val floorsLeft = 100 - floor        val nextStep = bestNextStep(floorsLeft)        floor += nextStep        print("$floor, ")    }}
```

Result:

9, 22, 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99, 100,

Just how we calculated! Nice :D

### Bigger picture

Now we have a nice algorithm that we can use for a lot of similar problems. For example, we can change it a little to calculate the number of throws for the most probabilistic scenario. We can also check how this minimal number of throws will differ depending on the height of the building. Here is a graph answering that:

![Image](https://cdn-media-1.freecodecamp.org/images/avPL-Nw2Cqndgf57fnyD80X3PA9rjYlmoG-8)

### Conclusion

You are now better prepared for your Google interview, but it is more important that you are now better prepared for general algorithmic thinking. This algorithm presented a nice, functional approach. A similar approach can be used for lot’s of different problems in our daily jobs.

I hope that you liked it. **Clap** to say thank you and to help others find this article. More interesting materials on [my Twitter](https://twitter.com/marcinmoskala). Reference me using [@marcinmoskala](https://twitter.com/marcinmoskala). If you are interested in Kotlin, check out [Kotlin Academy](https://blog.kotlin-academy.com/) and [Kotlin Academy portal](http://portal.kotlin-academy.com/) for Kotlin puzzlers and advanced materials.

