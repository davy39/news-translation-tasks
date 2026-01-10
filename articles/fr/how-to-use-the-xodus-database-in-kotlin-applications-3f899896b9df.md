---
title: Comment utiliser la base de données Xodus dans les applications Kotlin
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
seo_title: Comment utiliser la base de données Xodus dans les applications Kotlin
seo_desc: 'By Mariya Davydova

  I want to show you how to use one of my favorite database choices for Kotlin applications.
  Namely, Xodus. Why do I like using Xodus for Kotlin applications? Well, here are
  a couple of its selling points:


  Transactional

  Embedded

  Sch...'
---

Par Mariya Davydova

Je veux vous montrer comment utiliser l'une de mes bases de données préférées pour les applications [Kotlin](https://kotlinlang.org/). À savoir, [Xodus](https://github.com/JetBrains/xodus). Pourquoi j'aime utiliser Xodus pour les applications Kotlin ? Eh bien, voici quelques-uns de ses points forts :

* **Transactionnel**
* **Intégré**
* **Sans schéma**
* **Purement basé sur la JVM**
* Dispose d'un DSL Kotlin supplémentaire — [Xodus-DNQ](https://github.com/JetBrains/xodus-dnq).

Que signifie cela pour vous ?

* ACID intégré — toutes les opérations de la base de données sont atomiques, cohérentes, isolées et durables.
* Pas besoin de gérer une base de données externe — tout est à l'intérieur de votre application.
* Refactorings sans douleur — si vous devez ajouter quelques propriétés, vous n'aurez pas à reconstruire les tables.
* Base de données multiplateforme — Xodus peut fonctionner sur n'importe quelle plateforme capable d'exécuter une machine virtuelle Java.
* Avantages du langage Kotlin — tirez le meilleur parti de l'utilisation des types, des valeurs nulles et des délégués pour la déclaration des propriétés et la description des contraintes.

[Xodus](https://github.com/JetBrains/xodus) est un produit open-source de [JetBrains](https://www.jetbrains.com/). À l'origine, il a été développé pour un usage interne, mais il a ensuite été publié au public en juillet 2016. [YouTrack issue tracker](https://www.jetbrains.com/youtrack) et [Hub team tool](https://www.jetbrains.com/hub/) l'utilisent comme stockage de données. Si vous êtes curieux concernant les performances, vous pouvez consulter les [benchmarks](https://github.com/JetBrains/xodus/wiki/Benchmarks). En ce qui concerne un exemple concret, regardez l'[installation de JetBrains YouTrack](https://youtrack.jetbrains.com/issues) : qui, au moment de l'écriture, compte plus de 1,6 million de problèmes, et cela ne prend même pas en compte tous les commentaires et les entrées de suivi du temps stockés là-bas.

[Xodus-DNQ](https://github.com/JetBrains/xodus-dnq) est une bibliothèque Kotlin qui contient le langage de définition des données et les requêtes pour Xodus. Elle a également été développée d'abord comme une partie du produit puis publiée publiquement plus tard. YouTrack et Hub l'utilisent tous deux pour la définition de la couche persistante.

### Installation

Écrivons une petite application qui stocke des livres et leurs auteurs.

J'utiliserai Gradle comme outil de construction, car il aide à simplifier toute la gestion des dépendances et la compilation du projet. Si vous n'avez jamais travaillé avec Gradle, je recommande de consulter les guides officiels qu'ils ont sur [l'installation](https://gradle.org/install/) et [la création de nouvelles constructions](https://guides.gradle.org/creating-new-gradle-builds/).

Commençons donc par créer un nouveau répertoire pour notre exemple, puis exécutez `gradle init` là-bas. Cela initialisera la structure du projet et ajoutera certains répertoires et scripts de construction.

Maintenant, créez un fichier `bookstore.kt` dans le répertoire `src/main/kotlin`. Remplissez-le avec les classiques intemporels :

```kotlin
fun main() {
  println("Hello World")
}
```

Ensuite, mettez à jour le fichier `build.gradle` en utilisant un code similaire à celui-ci :

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

Il y a quelques choses qui se passent ici :

1. Nous ajoutons le plugin Kotlin et déclarons que la sortie de compilation est ciblée pour JVM 1.8.
2. Nous ajoutons des dépendances à la bibliothèque standard Kotlin et Xodus-DNQ.
3. Nous ajoutons également le plugin d'application et définissons la classe principale. Dans le cas d'une application Kotlin, nous n'avons pas de classe avec une méthode statique main, comme en Java. Au lieu de cela, nous devons définir une fonction autonome `main`. Cependant, sous le capot, Kotlin crée toujours une classe contenant cette fonction, et le nom de la classe est généré à partir du nom du fichier. Par exemple, `'bookstore.kt'` crée `'BookstoreKt'`.

Nous pouvons en fait supprimer en toute sécurité `settings.gradle`, car nous n'en avons pas besoin dans cet exemple.

Maintenant, exécutez `./gradlew run` ; vous devriez voir "Hello World" dans votre console :

```
> Task :run
Hello World
```

### Définition des données

![Image](https://cdn-media-1.freecodecamp.org/images/VQdCPUo-UlHYulNuJGemzF98MzBCfgfsq3k7)
_Photo par [Unsplash](https://unsplash.com/@alfonsmc10?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Alfons Morales</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Xodus fournit trois façons différentes de gérer les données, à savoir [Environments](https://github.com/JetBrains/xodus/wiki/Environments), [Entity Stores](https://github.com/JetBrains/xodus/wiki/Entity-Stores) et le [Virtual File System](https://github.com/JetBrains/xodus/wiki/Virtual-File-Systems). Cependant, Xodus-DNQ ne supporte que les Entity Stores, qui décrivent un modèle de données comme un ensemble d'entités typées avec des propriétés nommées (attributs) et des liens d'entités nommés (relations). C'est similaire aux lignes dans une table de base de données SQL.

Mon objectif étant de démontrer à quel point il est simple d'opérer Xodus via Kotlin DSL, je vais m'en tenir à l'API des types d'entités pour cette histoire.

Commençons par un `XdAuthor` :

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

À mon avis, cette déclaration semble assez naturelle : nous disons que nos auteurs ont toujours des noms et une année de naissance, peuvent avoir un pays de naissance et une année de décès (ce dernier est sans importance pour les auteurs actuellement vivants) ; également, il pourrait y avoir un nombre quelconque de livres de chaque auteur dans notre librairie.

Il y a plusieurs choses à mentionner dans cet extrait de code :

* L'objet `companion` déclare la propriété `entityType` pour chaque classe (qui est utilisée par le moteur de la base de données).
* Les champs de données sont déclarés à l'aide de délégués, qui encapsulent les types, les propriétés et les contraintes pour ces champs.
* Les liens sont des valeurs, pas des variables ; c'est-à-dire que vous ne les définissez pas avec `=`, mais vous y accédez comme à une collection. (Faites attention à `val books` versus `var name` ; j'ai passé pas mal de temps à essayer de comprendre pourquoi la compilation avec `var books` continuait à échouer.)

Le deuxième type est un `XdBook` :

```kotlin
class XdBook(entity: Entity) : XdEntity(entity) {
  companion object : XdNaturalEntityType<XdBook>()
var title by xdRequiredStringProp()
  var year by xdNullableIntProp()
  val genres by xdLink1_N(XdGenre)
  val authors : XdMutableQuery<XdAuthor> by xdLink1_N(XdAuthor::books)
}
```

La chose à laquelle il faut faire attention ici est la déclaration du champ `authors` :

* Remarquez que nous écrivons le type explicitement (`XdMutableQuery<XdAuthor>`). Pour le lien bidirectionnel, nous devons aider le compilateur à résoudre les types en laissant un indice à l'une des extrémités du lien.
* Remarquez également que `XdAuthor::books` référence `XdBook::authors` et vice versa. Nous devons ajouter ces références si nous voulons que le lien soit bidirectionnel ; donc si vous ajoutez un auteur au livre, le livre apparaîtra dans la liste des livres de cet auteur, et vice versa.

Le troisième type d'entité est une énumération `XdGenre`, qui est assez triviale :

```kotlin
class XdGenre(entity: Entity) : XdEnumEntity(entity) {
 companion object : XdEnumEntityType<XdGenre>() {
   val FANTASY by enumField {}
   val ROMANCE by enumField {}
 }
}
```

### Initialisation de la base de données

Maintenant que nous avons déclaré les types d'entités, nous devons initialiser la base de données :

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

Ce code montre la configuration la plus basique :

* Nous définissons le modèle de données. Ici, nous listons tous les types d'entités manuellement, mais il est possible de [scanner automatiquement le classpath](https://jetbrains.github.io/xodus-dnq/meta-model.html) également.
* Nous initialisons le stockage de la base de données dans le dossier `{user.home}/bookstore`.
* Nous lions les métadonnées avec le stockage.

### Remplissage des données

![Image](https://cdn-media-1.freecodecamp.org/images/X41x19KiXNapMX3lR5wDETktCtpl1prZQiHD)
_Photo par [Unsplash](https://unsplash.com/@anniespratt?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Annie Spratt</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Maintenant que nous avons initialisé la base de données, il est temps d'y mettre quelque chose. Avant de faire cela, ajoutons des méthodes `toString` à nos classes d'entités. Leur seul but est de nous permettre de sortir le contenu de la base de données dans un format lisible par l'homme.

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

Remarquez les instructions `books.asSequence().joinToString("\n")` et `genres.asSequence().joinToString(", ")` : ici, nous utilisons la méthode `asSequence()` pour convertir un `XdQuery` en une collection Kotlin.

Bien, ajoutons maintenant plusieurs livres de notre collection à l'intérieur de la fonction principale. Toutes les opérations de la base de données (création, lecture, mise à jour et suppression d'entités) sont effectuées à l'intérieur de transactions — des modifications atomiques de la base de données, qui garantissent de préserver la cohérence.

Dans le cas de notre librairie, il y a de nombreuses façons de la remplir :

1. Ajouter un auteur et un livre séparément :

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

2. Ajouter un auteur et mettre plusieurs livres dans leur liste :

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

3. Ajouter un auteur avec des livres :

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

Pour vérifier que tout est créé, tout ce que nous avons à faire est d'imprimer le contenu de notre base de données :

```kotlin
store.transactional(readonly = true) {     println(XdAuthor.all().asSequence().joinToString("\n***\n"))
 }
```

Maintenant, si vous exécutez `./gradlew run`, vous devriez voir la sortie suivante :

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

### Contraintes

Comme mentionné, les transactions garantissent la cohérence des données. L'une des opérations que Xodus effectue avant d'enregistrer les modifications est la vérification des contraintes. Dans le DNQ, certaines d'entre elles sont encodées dans le nom du délégué qui fournit une propriété d'un type donné. Par exemple, `xdRequiredIntProp` doit toujours être défini à une certaine valeur, tandis que `xdNullableIntProp` peut rester vide.

Malgré cela, Xodus-DNQ permet de définir des contraintes plus complexes qui sont décrites dans la [documentation officielle](https://jetbrains.github.io/xodus-dnq/properties.html#simple-property-constraints). J'ai ajouté plusieurs exemples au type d'entité `XdAuthor` :

```kotlin
  var name by xdRequiredStringProp { containsNone("?!") }
  var country by xdStringProp {
    length(min = 3, max = 56)
    regex(Regex("[A-Za-z.,]+"))
  }
  var yearOfBirth by xdRequiredIntProp { max(2019) }
  var yearOfDeath by xdNullableIntProp { max(2019) }
```

Vous vous demandez peut-être pourquoi j'ai limité la longueur de la propriété `countryOfBirth` à 56 caractères. Eh bien, le nom de pays officiel le plus long que j'ai [trouvé](https://www.worldatlas.com/articles/what-is-the-longest-country-name-in-the-world.html) est « The United Kingdom of Great Britain and Northern Ireland » — précisément 56 caractères !

### Requêtes

Nous avons déjà utilisé des requêtes de base de données ci-dessus. Vous vous souvenez ? Nous avons imprimé la liste des auteurs en utilisant `XdAuthor.all().asSequence()`. Comme vous pouvez le deviner, la méthode `all()` retourne toutes les entrées d'un type d'entité donné.

Cependant, nous préférerons souvent filtrer les données. Voici quelques exemples :

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

Encore une fois, il y a de nombreuses options pour construire des requêtes de données, donc je recommande vivement de consulter la [documentation](https://jetbrains.github.io/xodus-dnq/queries.html).

J'espère que cette histoire est aussi utile pour vous qu'elle l'a été pour moi lorsque je l'ai écrite :) Tout retour est grandement apprécié !

Vous pouvez trouver le [code source](https://github.com/mariyadavydova/bookstore-xodus-example) pour ce tutoriel ici.