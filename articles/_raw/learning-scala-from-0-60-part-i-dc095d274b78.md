---
title: 'Learn Scala from 0–60: The Basics'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-16T19:20:45.000Z'
originalURL: https://freecodecamp.org/news/learning-scala-from-0-60-part-i-dc095d274b78
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q0JQttpYtxDBv_BPT_apQg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Durga Prasana

  Scala is a general purpose, high-level programming language that offers a balance
  between developing functional and object-oriented programs.

  What is functional programming all about? In simple terms, functions are the first-class
  ci...'
---

By Durga Prasana

Scala is a general purpose, high-level programming language that offers a balance between developing functional and object-oriented programs.

What is functional programming all about? In simple terms, functions are the first-class citizens in functional programming. In order to extend upon a core set of functionalities of a program, we tend to write additional classes extending upon certain guidelines / interfaces. In functional programming, functions help us achieve the same.

We’ll use [the Scala REPL](https://docs.scala-lang.org/overviews/repl/overview.html) for all explanations. It is a very handy and informative tool for learning Scala. It logs cute little messages on how our code is interpreted and executed.

Let’s start with the basics first.

#### **1. Variables**

We can define immutable variables using `val`:

```
scala> val name = "King"name: String = King
```

Mutable variables can be defined and modified using `var`:

```
scala> var name = "King"name: String = King
```

```
scala> name = "Arthur"name: String = Arthur
```

We use `def` to assign a label to an immutable value whose evaluation is deferred for a later time. It means the label’s value is lazily evaluated every time upon use.

```
scala> var name = "King"name: String = King
```

```
scala> def alias = namealias: String
```

```
scala> aliasres2: String = King
```

Did you observe something interesting?

While defining `alias`, no value was assigned to `alias: String` since it is lazily associated, when we invoke it. What would happen if we change the value of `name`?

```
scala> aliasres5: String = King
```

```
scala> name = "Arthur, King Arthur"name: String = Arthur, King Arthur
```

```
scala> aliasres6: String = Arthur, King Arthur
```

#### 2. Control flow

We use control flow statements to express our decision logic.

You can write an `if-else` statement as below:

```
if(name.contains("Arthur")) {  print("Entombed sword")} else {  print("You're not entitled to this sword")}
```

Or, you can use `while`:

```
var attempts = 0while (attempts < 3) {  drawSword()  attempts += 1}
```

#### 3. Collections

Scala explicitly distinguishes between immutable versus mutable collections — right from the package namespace itself ( `scala.collection.immutable` or `scala.collection.mutable`).

Unlike immutable collections, mutable collections can be updated or extended in place. This enables us to change, add, or remove elements as a side effect.

But performing addition, removal, or update operations on immutable collections returns a new collection instead.

Immutable collections are always automatically imported via the `scala._` (which also contains alias for `scala.collection.immutable.List`).

However, to use mutable collections, you need to explicitly import `scala.collection.mutable.List`.

In the spirit of functional programming, we’ll primarily base our examples on immutable aspects of the language, with minor detours into the mutable side.

#### **List**

We can create a list in various ways:

```
scala> val names = List("Arthur", "Uther", "Mordred", "Vortigern")
```

```
names: List[String] = List(Arthur, Uther, Mordred, Vortigern)
```

Another handy approach is to define a list using the cons `::` operator. This joins a head element with the remaining tail of a list.

```
scala> val name = "Arthur" :: "Uther" :: "Mordred" :: "Vortigern" :: Nil
```

```
name: List[String] = List(Arthur, Uther, Mordred, Vortigern)
```

Which is equivalent to:

```
scala> val name = "Arthur" :: ("Uther" :: ("Mordred" :: ("Vortigern" :: Nil)))
```

```
name: List[String] = List(Arthur, Uther, Mordred, Vortigern)
```

We can access list elements directly by their index. Remember Scala uses zero-based indexing:

```
scala> name(2)
```

```
res7: String = Mordred
```

Some common helper methods include:

`list.head`, which returns the first element:

```
scala> name.head
```

```
res8: String = Arthur
```

`list.tail`, which returns the tail of a list (which includes everything except the head):

```
scala> name.tail
```

```
res9: List[String] = List(Uther, Mordred, Vortigern)
```

#### **Set**

`Set` allows us to create a non-repeated group of entities. `List` doesn’t eliminate duplicates by default.

```
scala> val nameswithDuplicates = List("Arthur", "Uther", "Mordred", "Vortigern", "Arthur", "Uther")
```

```
nameswithDuplicates: List[String] = List(Arthur, Uther, Mordred, Vortigern, Arthur, Uther)
```

Here, ‘Arthur’ is repeated twice, and so is ‘Uther’.

Let’s create a Set with the same names. Notice how it excludes the duplicates.

```
scala> val uniqueNames = Set("Arthur", "Uther", "Mordred", "Vortigern", "Arthur", "Uther")
```

```
uniqueNames: scala.collection.immutable.Set[String] = Set(Arthur, Uther, Mordred, Vortigern)
```

We can check for the existence of specific element in Set using `contains()`:

```
scala> uniqueNames.contains("Vortigern")res0: Boolean = true
```

We can add elements to a Set using the + method (which takes `varargs` i.e. variable-length arguments)

```
scala> uniqueNames + ("Igraine", "Elsa", "Guenevere")res0: scala.collection.immutable.Set[String] = Set(Arthur, Elsa, Vortigern, Guenevere, Mordred, Igraine, Uther)
```

Similarly we can remove elements using the `-` method

```
scala> uniqueNames - "Elsa"
```

```
res1: scala.collection.immutable.Set[String] = Set(Arthur, Uther, Mordred, Vortigern)
```

#### **Map**

`Map` is an iterable collection which contains mappings from `key` elements to respective `value` elements, which can be created as:

```
scala> val kingSpouses = Map( | "King Uther" -> "Igraine", | "Vortigern" -> "Elsa", | "King Arthur" -> "Guenevere" | )
```

```
kingSpouses: scala.collection.immutable.Map[String,String] = Map(King Uther -> Igraine, Vortigern -> Elsa, King Arthur -> Guenevere)
```

Values for a specific key in map can be accessed as:

```
scala> kingSpouses("Vortigern")res0: String = Elsa
```

We can add an entry to Map using the `+` method:

```
scala> kingSpouses + ("Launcelot" -> "Elaine")res0: scala.collection.immutable.Map[String,String] = Map(King Uther -> Igraine, Vortigern -> Elsa, King Arthur -> Guenevere, Launcelot -> Elaine)
```

To modify an existing mapping, we simply re-add the updated key-value:

```
scala> kingSpouses + ("Launcelot" -> "Guenevere")res1: scala.collection.immutable.Map[String,String] = Map(King Uther -> Igraine, Vortigern -> Elsa, King Arthur -> Guenevere, Launcelot -> Guenevere)
```

Note that since the collection is immutable, each edit operation returns a new collection( `res0`, `res1`) with the changes applied. The original collection `kingSpouses` remains unchanged.

#### 4. Functional combinators

Now that we’ve learned how to group a set of entities together, let’s see how we can use functional combinators to generate meaningful transformations on such collections.

In John Hughes’ simple words:

> A combinator is a function which builds program fragments from program fragments.

An in-depth look at how combinators work is outside of this article’s scope. But, we’ll try to touch upon a high-level understanding of the concept anyhow.

Let’s take an example.

Suppose we want to find names of all queens using the `kingSpouses` collection map that we created.

We’d want to do something along the lines of examining each entry in the map. If the `key` has the name of a king, then we’re interested in the name of it’s spouse (i.e. queen).

We shall use the `filter` combinator on map, which has a signature like:

```
collection.filter( /* a filter condition method which returns true on matching map entries */)
```

Overall we shall perform the following steps to find queens:

* Find the (key, value) pairs with kings’ names as keys.
* Extract the values (names of queen) only for such tuples.

The `filter` is a function which, when given a (key, value), returns true / false.

1. Find the map entries pertaining to kings.

Let’s define our filtering predicate function. Since `key_value` is a tuple of (key, value), we extract the key using `._1` (and guess what `._2` returns?)

```
scala> def isKingly(key_value: (String, String)): Boolean = key_value._1.toLowerCase.contains("king")
```

```
isKingly: (key_value: (String, String))Boolean
```

Now we shall use the filter function defined above to `filter` kingly entries.

```
scala> val kingsAndQueens = kingSpouses.filter(isKingly)
```

```
kingsAndQueens: scala.collection.immutable.Map[String,String] = Map(King Uther -> Igraine, King Arthur -> Guenevere)
```

2. Extract the names of respective queens from the filtered tuples.

```
scala> kingsAndQueens.values
```

```
res10: Iterable[String] = MapLike.DefaultValuesIterable(Igraine, Guenevere)
```

Let’s print out the names of queens using the `foreach` combinator:

```
scala> kingsAndQueens.values.foreach(println)IgraineGuenevere
```

Some other useful combinators are `foreach`, `filter`, `zip`, `partition`, `find`.

We shall re-visit some of these after having learnt how to define functions and passing functions as arguments to other functions in higher-order functions.

Let’s recap on what we’ve learned:

* Different ways of defining variables
* Various control-flow statements
* Some basics about various collections
* Overview of using functional combinators on collections

I hope you found this article useful. It is first in a series of articles to follow on learning Scala.

In part two, we’ll learn about defining classes, traits, encapsulation and other object-oriented concepts.

Please feel free to let me know your feedback and suggestions on how I can improve the content. Until then, ❤ coding.

