---
title: Why we will always need new programming languages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-25T15:40:40.000Z'
originalURL: https://freecodecamp.org/news/why-we-will-always-need-new-programming-languages-3415869ea37e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ngXgBNNdx6iiWP8q.png
tags:
- name: coding
  slug: coding
- name: Kotlin
  slug: kotlin
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Marcin Moskala

  Structure and Interpretation of Computer Programs by Harold Abelson and Gerald Jay
  Sussman is one of the best books about programming ever written. It was ahead of
  its time for many years.

  The advantages of functional programming th...'
---

By Marcin Moskala

[Structure and Interpretation of Computer Programs](http://web.mit.edu/alexmv/6.037/sicp.pdf) by Harold Abelson and Gerald Jay Sussman is one of the best books about programming ever written. It was ahead of its time for many years.

The advantages of functional programming that were highlighted there are still a constant source of inspiration for speakers, teachers, and other writers. It showed the power and flaws of object-oriented programming when it was still young. The powers quickly become advertised thanks to object-oriented programming fanatics. On the other hand, it took years for the community to see the flaws.

The last chapter was wholly devoted to another concept that is still not much discussed in the popular dialogue: the need for new programming languages. Even though the book sympathized with [Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language)), it clearly claimed that it is not the final programming language. No language will ever be.

We will always need new programming languages to improve our expressiveness. This is not a trivial statement, and to understand what is behind it, we need to go two levels down.

### What is a programming language?

See the following function:

```
fun square(a: Int) = a * a
```

```
// Usageprint(square(10) + square(20))
```

What does it mean that `square` is defined?

From a technical point of view, it is just a simplification and the body can replace all calls:

```
// Kotlinprint(10 * 10 + 20 * 20)
```

From the programmer’s point of view, `square` is much more. The fact that we can define such a function is not only a simpler way to make an operation but also it allows us to express a concept of squaring. This function is some abstraction.

If it were more complex, it would allow us to hide all this complexity behind a simple function call. This is what programming is: Different programming language features allow us to express things in different ways.

### Evolution of programming languages

The programming industry evolves, and so programming languages do too. Think of the for-loop. Initially, there was only a when-loop.

Soon programmers noticed a common pattern:

```
// Cint i = 0;while(i < n) {    i++;    // ...} 
```

The `while` expression was used again and again to iterate over something — mostly numbers, addresses, or iterators.

So we introduced for-loops:

```
// C++for (int i = 0; i < n; i++) {    // ...}
```

Soon the industry observed that the for-loop is mainly used to iterate over elements from a list.

This is why languages introduced a new variant of for-loop which is designed to iterate over `list`:

```
// Kotlinfor(e in list) {    // ...}
```

### So we need new features

#### But languages evolve, why not stick with them?

It is true that languages evolve. In some cases, it is really impressive how old languages like C++, Java, or JavaScript can have good support for functional programming elements they were not designed for. But the problem is that new features do not replace old ones — instead they are added on.

In terms of programming language features, more is not necessarily better. It is confusing when we can express the same concept in many different ways.

Think of [Scala](https://www.scala-lang.org/). The biggest objection with Scala is that too many different features make it extremely hard to understand what is going on in the code of a developer with a little too much creativity.

The [Go](https://golang.org/) programming language built its popularity on simplicity. It is not about how many features some languages have, but about having the perfect set of features.

In my opinion, this is why everyone loves [Kotlin](https://kotlinlang.org/) so much. It is the most well-designed programming language I know.

There are strong reasons for that:

* It was in beta for 6 years and it was evolving iteratively throughout that whole time
* It is designed by [JetBrains](https://www.jetbrains.com/) who have been mastering their understanding of programming languages and how people use them for years

During the beta period, there were some important features fully implemented, and yet they were removed before 1.0. Among them are tuples. Kotlin fully supported them! Yet the Kotlin team removed support for tuples before Kotlin 1.0 because their analysis and experiments showed that tuples do more harm than good, and people should use data classes instead. This shows that JetBrains understands the importance of good design.

Another language that is well designed is [Swift](https://swift.org/). It was developed much faster, and the developers who were designing it made a lot of mistakes. Yet Apple just changed the design with nearly every major version release. They don’t really care about legacy.

Developers are grumbling, but from the design point of view, it is great. Although they cannot continue doing that for long. The more things that are in Swift, the bigger the cost of design change. Also, I don’t think they are able to change major functionalities.

![Image](https://cdn-media-1.freecodecamp.org/images/gyPeeyU3As2Bd4PHAt50byzZlibC2ResHNDd)
_Source: [https://getbadges.io/blog/12-gamification-platforms-that-help-learn-coding](https://getbadges.io/blog/12-gamification-platforms-that-help-learn-coding" rel="noopener" target="_blank" title=")_

### So if we have well-designed new languages, are they the final languages?

Not at all. Industries evolve. Our thinking evolves. And so programming languages need to evolve as well.

One thing is that ideas for new features and ways of thinking will be born, and so perfectly designed languages won’t be perfect anymore.

The second thing is that we learn more about programming. Classes and methods are open by default in Java. Kotlin made them both final by default because developers were highly overusing inheritance when they shouldn’t have been.

Java class members were package-private by default. This modifier was almost never used. Kotlin doesn’t allow it at all, but instead class members are public by default because this is the most common modifier for them. We change our habits and we learn, so also languages should change with us.

The third thing is that paradigms change. I see stagnation in terms of programming paradigms, but we still have some to introduce into everyday practice.

Where did logical programming go? Notice that you can use this paradigm and just provide a set of constraints for a website and expect the website to be built automatically based on them. It is possible to implement that. Also, new paradigms will sooner or later be born. It can’t be that we’ve explored everything.

Finally, new technologies are born and the old way of thinking that is represented by the previous languages might not be adequate.

Think of [blockchain](https://en.wikipedia.org/wiki/Blockchain). When I talk to people who consider switching, they want to use their favourite languages like Java or JavaScript. Although when I talk to blockchain developers, they claim that blockchain needs to be developed in languages that are designed for it.

For example, a contract is a concept that doesn’t have an equivalent in programming. It can be simulated by class, but this is harmful to the way people think about it. It is damaging when we try to express new things using old words. It is like naming a car “steel horse” and trying to make mechanics from vets.

### Closing

Think of mathematics. Equilibrium can be expressed in a descriptive way:

**Two plus three equals five**

Although it is something totally different than expressing it using the mathematical notation:

**2 + 3 = 5**

It is not the only an optimization for readability and space. These two notations mean the same thing, but they represent totally different concepts. This is something that is not important from a computer’s point of view — which can easily translate the descriptive form into mathematical — but it is the most important thing to us as humans.

If it weren’t important, we would operate on Assembler instead of Java, JavaScript, Python or Kotlin. But it is important. This is why we need better and better expression, and we need new programming languages.

![Image](https://cdn-media-1.freecodecamp.org/images/Vr01qrslh5N7yR1gf6L3OfIRGPg6r2ttP102)

### About the author

[Marcin Moskała](http://marcinmoskala.com/) ([@marcinmoskala](https://twitter.com/marcinmoskala)) is a trainer and consultant, currently concentrating on giving Kotlin in Android and advanced Kotlin workshops (for more details, [apply here](https://marcinmoskala.typeform.com/to/iwKnN9)). He is also a [speaker](https://www.youtube.com/results?search_query=Marcin+Moska%C5%82a), author of [articles](https://medium.com/@marcinmoskala) and [a book](https://www.packtpub.com/application-development/android-development-kotlin) about Android development in Kotlin.

![Image](https://cdn-media-1.freecodecamp.org/images/70Dz9UeSMUlQTowTe8t8N-QuMO2BZSD80C5b)

