---
title: How to use the Xodus database in Kotlin applications
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T16:12:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-xodus-database-in-kotlin-applications-3f899896b9df
coverImage: https://cdn-media-1.freecodecamp.org/images/0*1jikfdFxD_A5SK6z
tags:
- name: database
  slug: database
- name: Kotlin
  slug: kotlin
- name: NoSQL
  slug: nosql
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mariya Davydova

  I want to show you how to use one of my favorite database choices for Kotlin applications.
  Namely, Xodus. Why do I like using Xodus for Kotlin applications? Well, here are
  a couple of its selling points:


  Transactional

  Embedded

  Sch...'
---

By Mariya Davydova

I want to show you how to use one of my favorite database choices for [Kotlin](https://kotlinlang.org/) applications. Namely, [Xodus](https://github.com/JetBrains/xodus). Why do I like using Xodus for Kotlin applications? Well, here are a couple of its selling points:

* **Transactional**
* **Embedded**
* **Schema-less**
* **Pure JVM-based**
* Has an additional **Kotlin DSL** — [Xodus-DNQ](https://github.com/JetBrains/xodus-dnq).

What does this mean to you?

* ACID on-board — all database operations are atomic, consistent, isolated, and durable.
* No need to manage an external database — everything is inside your application.
* Painless refactorings — if you need to add a couple of properties you won’t have to then rebuild the tables.
* Cross-platform database — Xodus can run on any platform that can run a Java virtual machine.
* Kotlin language benefits — take the best from using types, nullable values and delegates for properties declaration and constraints description.

[Xodus](https://github.com/JetBrains/xodus) is an open-source product from [JetBrains](https://www.jetbrains.com/). Originally it was developed for internal use, but it was subsequently released to the public back in July 2016. [YouTrack issue tracker](https://www.jetbrains.com/youtrack) and [Hub team tool](https://www.jetbrains.com/hub/) use it as their data storage. If you are curious about the performance, you can check out the [benchmarks](https://github.com/JetBrains/xodus/wiki/Benchmarks). As for the real-life example, take a look at the [JetBrains YouTrack installation](https://youtrack.jetbrains.com/issues): which at the time of writing has over 1,6 million issues, and that is not even taking into account all the comments and time tracking entries all stored there.

[Xodus-DNQ](https://github.com/JetBrains/xodus-dnq) is a Kotlin library that contains the data definition language and queries for Xodus. It was also developed first as a part of the product and then later released publicly. YouTrack and Hub both use it for persistent layer definition.

### Setup

Let’s write a small application which stores books and their authors.

I will use Gradle as a build tool, as it helps simplify all the dependencies management and project compilation stuff. If you have never worked with Gradle, I recommend taking a look at the official guides they have on [installation](https://gradle.org/install/) and [creating new builds](https://guides.gradle.org/creating-new-gradle-builds/).

So first, we need to start by creating a new directory for our example, and then run `gradle init` there. This will initialize the project structure and add some directories and build scripts.

Now, create a `bookstore.kt` file in `src/main/kotlin` directory. Fill it with the never-going-out-of-fashion classics:

```kotlin
fun main() {
  println("Hello World")
}
```

Then, update the `build.gradle` file using code similar to this:

```kotlin
plugins {
  id 'application'
  id 'org.jetbrains.kotlin.jvm' version '1.3.21'
}
group 'mariyadavydova'
version '1.0-SNAPSHOT'
sourceCompatibility = 1.8
targetCompatibility = 1.8
tasks.withType(org.jetbrains.kotlin.gradle.tasks.KotlinCompile).all {
  kotlinOptions {
    jvmTarget = "1.8"
  }
}
repositories {
  mavenCentral()
}
dependencies {
  implementation 'org.jetbrains.kotlin:kotlin-stdlib-jdk8:1.3.21'
  implementation 'org.jetbrains.xodus:dnq:1.2.420'
}
mainClassName = 'BookstoreKt'
```

There are a few things that are happening here:

1. We add the Kotlin plugin and claim that the compilation output is targeted for JVM 1.8.
2. We add dependencies to the Kotlin standard library and Xodus-DNQ.
3. We also add the application plugin and define the main class. In the case of the Kotlin application, we do not have a class with a static method main, like in Java. Instead, we have to define a standalone function `main`. However, under the hood, Kotlin still makes a class containing this function, and the name of the class is generated from the name of the file. For example, `‘bookstore.kt’` makes `‘BookstoreKt’`.

We can actually safely remove `settings.gradle`, as we don’t need it in this example.

Now, execute `./gradlew run`; you should see “Hello World” in your console:

```
> Task :run
Hello World
```

### Data definition

![Image](https://cdn-media-1.freecodecamp.org/images/VQdCPUo-UlHYulNuJGemzF98MzBCfgfsq3k7)
_Photo by [Unsplash](https://unsplash.com/@alfonsmc10?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Alfons Morales</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Xodus provides three different ways to deal with data, namely [Environments](https://github.com/JetBrains/xodus/wiki/Environments), [Entity Stores](https://github.com/JetBrains/xodus/wiki/Entity-Stores) and the [Virtual File System](https://github.com/JetBrains/xodus/wiki/Virtual-File-Systems). However, Xodus-DNQ supports only the Entity Stores, which describe a data model as a set of typed entities with named properties (attributes) and named entity links (relations). It is similar to rows in the SQL database table.

As my goal is to demonstrate how simple it is to operate Xodus via Kotlin DSL, I’ll stick to the entity types API for this story.

Let’s start with an `XdAuthor`:

```
class XdAuthor(entity: Entity) : XdEntity(entity) {
  companion object : XdNaturalEntityType<XdAuthor>()
var name by xdRequiredStringProp()
  var countryOfBirth by xdStringProp()
  var yearOfBirth by xdRequiredIntProp()
  var yearOfDeath by xdNullableIntProp()
  val books by xdLink0_N(XdBook::authors)
}
```

From my point of view, this declaration looks pretty natural: we say that our authors always have names and year of birth, may have country of birth and year of death (the latter is irrelevant for the currently living authors); also, there could be any number of books from each author in our bookstore.

There are several things worth mentioning in this code snippet:

* The `companion` object declares the `entityType` property for each class (which is used by the database engine).
* The data fields are declared with the help of the delegates, which encapsulate the types, properties, and constraints for these fields.
* Links are values, not variables; that is, you don’t set them with `=`, but access them as a collection. (Pay attention to `val books` versus `var name`; I spent quite a bit of time trying to figure out why the compilation with `var books` kept failing.)

The second type is an `XdBook`:

```kotlin
class XdBook(entity: Entity) : XdEntity(entity) {
  companion object : XdNaturalEntityType<XdBook>()
var title by xdRequiredStringProp()
  var year by xdNullableIntProp()
  val genres by xdLink1_N(XdGenre)
  val authors : XdMutableQuery<XdAuthor> by xdLink1_N(XdAuthor::books)
}
```

The thing to pay attention to here is the declaration of the `authors`’ field:

* Notice that we write down the type explicitly (`XdMutableQuery<XdAuth`or>). For the bidirectional link, we have to help the compiler to resolve the types by leaving a hint on one of the link ends.
* Also, notice that `XdAuthor::books` references `XdBook::authors` and vice versa. We have to add these references if we want the link to be bidirectional; so if you add an author to the book, the book will appear in the list of the books of this author, and vice versa.

The third entity type is an `XdGenre` enumeration, which is pretty trivial:

```kotlin
class XdGenre(entity: Entity) : XdEnumEntity(entity) {
 companion object : XdEnumEntityType<XdGenre>() {
   val FANTASY by enumField {}
   val ROMANCE by enumField {}
 }
}
```

### Database initialization

Now, when we have declared the entity types, we have to initialize the database:

```
fun initXodus(): TransientEntityStore {
  XdModel.registerNodes(
      XdAuthor,
      XdBook,
      XdGenre
  )
  val databaseHome = File(System.getProperty("user.home"), "bookstore")
  val store = StaticStoreContainer.init(
      dbFolder = databaseHome,
      environmentName = "db"
  )
  initMetaData(XdModel.hierarchy, store)
  return store
}
fun main() {
  val store = initXodus()
}
```

This code shows the most basic setup:

* We define the data model. Here we list all entity types manually, but it is possible to [auto scan the classpath](https://jetbrains.github.io/xodus-dnq/meta-model.html) as well.
* We initialize the database store in `{user.home}/bookstore` folder.
* We link the metadata with the store.

### Filling the data in

![Image](https://cdn-media-1.freecodecamp.org/images/X41x19KiXNapMX3lR5wDETktCtpl1prZQiHD)
_Photo by [Unsplash](https://unsplash.com/@anniespratt?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Annie Spratt</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Now that we have initialized the database, it’s time to put something inside. Before doing this, let’s add `toString` methods to our entity classes. Their only purpose is to allow us to output the database content in a human-readable format.

```kotlin
class XdAuthor(entity: Entity) : XdEntity(entity) {
  ...
  override fun toString(): String {
    val bibliography = books.asSequence().joinToString("\n")
    return "$name ($yearOfBirth-${yearOfDeath ?: "???"}):\n$bibliography"
  }
}
class XdBook(entity: Entity) : XdEntity(entity) {
  ...
  override fun toString(): String {
    val genres = genres.asSequence().joinToString(", ")
    return "$title (${year ?: "Unknown"}) - $genres"
  }
}
class XdGenre(entity: Entity) : XdEnumEntity(entity) {
  ...
  override fun toString(): String {
    return this.name.toLowerCase().capitalize()
  }
}
```

Notice `books.asSequence().joinToString("\n")` and `genres.asSequence().joinToString(", ")` instructions: here we use `asSequence()` method to convert an `XdQuery` to a Kotlin collection.

Right, let’s now add several books from our collection inside the main function. All database operations (creating, reading, updating and removing entities) we do inside transactions — atomic database modifications, which guarantees to preserve the consistency.

In the case of our bookstore, there are plenty of ways to fill it with stuff:

1. Add an author and a book separately:

```kotlin
 val bronte = store.transactional {
   XdAuthor.new {
     name = "Charlotte Brontë"
     countryOfBirth = "England"
     yearOfBirth = 1816
     yearOfDeath = 1855
   } 
 }
 store.transactional {
   XdBook.new {
     title = "Jane Eyre"
     year = 1847
     genres.add(XdGenre.ROMANCE)
     authors.add(bronte)
   }
 }
```

2. Add an author and put several books in their list:

```kotlin
 val tolkien = store.transactional {
   XdAuthor.new {
     name = "J. R. R. Tolkien"
     countryOfBirth = "England"
     yearOfBirth = 1892
     yearOfDeath = 1973
   }
 }
 store.transactional {
   tolkien.books.add(XdBook.new {
     title = "The Hobbit"
     year = 1937
     genres.add(XdGenre.FANTASY)
   })
   tolkien.books.add(XdBook.new {
     title = "The Lord of the Rings"
     year = 1955
     genres.add(XdGenre.FANTASY)
   })
 }
```

3. Add an author with books:

```kotlin
 store.transactional {
   XdAuthor.new {
     name = "George R. R. Martin"
     countryOfBirth = "USA"
     yearOfBirth = 1948
     books.add(XdBook.new {
       title = "A Game of Thrones"
       year = 1996
       genres.add(XdGenre.FANTASY)
     })
   }
 }
```

To check that everything is created, all we need to do is to print the content of our database:

```kotlin
store.transactional(readonly = true) {     println(XdAuthor.all().asSequence().joinToString("\n***\n"))
 }
```

Now, if you execute `./gradlew run`, you should see the following output:

```
Charlotte Brontë (1816-1855):
Jane Eyre (1847) - Romance
***
J. R. R. Tolkien (1892-1973):
The Hobbit (1937) - Fantasy
The Lord of the Rings (1955) - Fantasy
***
George R. R. Martin (1948-???):
A Game of Thrones (1996) - Fantasy
```

### Constraints

As mentioned, the transactions guarantee data consistency. One of the operations which Xodus does before saving the changes is checking the constraints. In the DNQ, some of them are encoded in the name of the delegate which provides a property of a given type. For example, `xdRequiredIntProp` has to always be set to some value, whereas `xdNullableIntProp` can remain empty.

Despite this, Xodus-DNQ allows defining more complex constraints which are described in the [official documentation](https://jetbrains.github.io/xodus-dnq/properties.html#simple-property-constraints). I have added several examples to the `XdAuthor` entity type:

```kotlin
  var name by xdRequiredStringProp { containsNone("?!") }
  var country by xdStringProp {
    length(min = 3, max = 56)
    regex(Regex("[A-Za-z.,]+"))
  }
  var yearOfBirth by xdRequiredIntProp { max(2019) }
  var yearOfDeath by xdNullableIntProp { max(2019) }
```

You may be wondering why I have limited the `countryOfBirth` property length to 56 characters. Well, the longest official country name which I [found](https://www.worldatlas.com/articles/what-is-the-longest-country-name-in-the-world.html) is “The United Kingdom of Great Britain and Northern Ireland” — precisely 56 characters!

### Queries

We have already used database queries above. Do you remember? We printed the list of authors using `XdAuthor.all().asSequence()`. As you may guess, the `all()` method returns all the entries of a given entity type.

More often than not though, we will prefer filtering data. Here are some examples:

```kotlin
store.transactional(readonly = true) {
  val fantasyBooks = XdBook.filter { 
    it.genres contains XdGenre.FANTASY }
  val booksOf20thCentury = XdBook.filter { 
    (it.year ge 1900) and (it.year lt 1999) }
  val authorsFromEngland = XdAuthor.filter { 
    it.countryOfBirth eq "England" }
  
  val booksSortedByYear = XdBook.all().sortedBy(XdBook::year)
  val allGenres = XdBook.all().flatMapDistinct(XdBook::genres)
}
```

Again, there are plenty of options for building data queries, so I strongly recommend taking a look at the [documentation](https://jetbrains.github.io/xodus-dnq/queries.html).

I hope this story is as useful for you as it was for me when I wrote it :) Any feedback is highly appreciated!

You can find the [source code](https://github.com/mariyadavydova/bookstore-xodus-example) for this tutorial here.

