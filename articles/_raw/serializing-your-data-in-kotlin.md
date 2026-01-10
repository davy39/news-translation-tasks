---
title: How to Serialize Your Data in Kotlin and Jetpack Compose
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2023-02-01T21:19:13.000Z'
originalURL: https://freecodecamp.org/news/serializing-your-data-in-kotlin
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/fineas-anton-cnoMG2034k8-unsplash.jpg
tags:
- name: Jetpack Compose
  slug: jetpack-compose
- name: Kotlin
  slug: kotlin
seo_title: null
seo_desc: "Serialization is the process of transforming data that's in one format\
  \ into another format that can be stored. \nIf you have ever worked with a database\
  \ or fetching data from a server, this should all be familiar to you. If not, you\
  \ have come to the r..."
---

Serialization is the process of transforming data that's in one format into another format that can be stored. 

If you have ever worked with a database or fetching data from a server, this should all be familiar to you. If not, you have come to the right place. 

In this tutorial, we will go over:

* How to setup serialization in a Jetpack Compose project
* How to serialize a data class
* How to de-serialize a data class

You might be asking yourself, what’s so special about serialization in Jetpack Compose? In essence, there isn’t a lot of difference than with a regular Kotlin Android project. The only difference is in the setup.

## How to Set Everything Up

Each version of Jetpack Compose corresponds with a version of Kotiln that it is compatible with. Each version of the kotlin-serialization library is also compatible with a specific version of Kotlin. So you need to make sure that each of the three parts in this tripod are compatible with one another.

How can you that?

Your first resource you'll want to consult is the [Compose to Kotlin Compatibility Map](https://developer.android.com/jetpack/androidx/releases/compose-kotlin).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/1_5brVwILW54aNaFFimDF87Q.jpeg)

Here you can see which version of Jetpack Compose corresponds to which Kotlin version.

The second resource you will need is the [releases page](https://github.com/Kotlin/kotlinx.serialization/releases) for the kotlin-serialization library. There you will find which library version is compatible with which Kotlin version.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/1_y6Ba1fROOcSSXXm-Nll4Ew.jpeg)

Confused? 😕

Let’s illustrate this with an example:

* Your Jetpack Compose version is **1.1.0**.
* Looking over the compatibility map, you see it is compatible with Kotlin version **1.6.10**.
* Heading to the releases page of kotlin-serialization library, you see that the version of the kotlin-serialization library that you need to use is **1.3.2**.

Head into your project level build.gradle file, and inside the buildscript object, in the dependencies section, put in classpath for the kotlin-serialization library with the version you need.

```kotlin
dependencies {
        ...
        classpath "org.jetbrains.kotlin:kotlin-serialization:X.Y.Z"
 }
```

Then, head over to your application build.gradle file and do these two things:

1. Add the **id ‘org.jetbrains.kotlin.plugin.serialization’** inside of the plugins at the top of the file:

```kotlin
plugins {
   ...
   id 'org.jetbrains.kotlin.plugin.serialization'
}
```

2. At the bottom of the file, inside the dependencies section add **implementation ‘org.jetbrains.kotlinx:kotlinx-serialization-json:X.Y.Z’**:

```kotlin
dependencies {
   ...
   implementation 'org.jetbrains.kotlinx:kotlinx-serialization-json:X.Y.Z'
}
```

Sync your project and you should be good to go.

Note that we are using the **json** format of the library, but there are other formats that are supported as well:

* Protocol Buffers
* CBOR (Concise Binary Object Representation)
* Properties
* HOCON (Human Optimized Config Object Notation)

> ⚠️ If you encounter any errors, make sure the versions you put are correct

## How to Build Your Data Class

In order to have something we can serialize and later de-serialize, we need to work with data classes. 

Creating a data class is simple. If you are using Android Studio, just right click inside your project’s module and choose New Kotlin file. Enter your class name and then append the data keyword before it.

For the sake of this article, let's say we are working with an API that returns a list of users. Each user object has a range of attributes it can have (just to name a few):

* First name
* Last name
* Age
* Birthdate
* Id

To make our data class serializable, all you need to do is add the **@Serializable** annotation above the class declaration.

```kotlin
@Serializable
data class UserModel(
   val firstName: String,
   val lastName: String,
   val age: Int,
   val birthdate: Date,
   val id: Long
)
```

Pretty nifty, right?

Well, there’s more.

The variable that will hold the user’s first name is written as firstName. That means that in the response from our server, it needs to return in a field with the same name. 

Sometimes, in API responses, the keys are not written in camelCase, but rather in kebab_case. That would mean that the key for first name, might be first_name. In that case, we would have to write it out like this:

```kotlin
@Serializable
data class UserModel(
   val first_name: String,
   val lastName: String,
   val age: Int,
   val birthdate: Date,
   val id: Long
)
```

But that is not the [convention](https://kotlinlang.org/docs/coding-conventions.html) for property names in Kotlin.

So what can we do?

We can use the **@SerialName** annotation. This allows us to mark what the name of the field will be from the response and then write anything as the property for it.

```kotlin
@Serializable
data class UserModel(
   @SerialName("first_name")
   val firstName: String,
   val lastName: String,
   val age: Int,
   val birthdate: Date,
   val id: Long
)
```

## How to Serialize and De-Serialize

Now that our data class is set up, let’s enjoy the fruits of our labor. Whenever we need to serialize our data class, we will use the [Json.encodeToString](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/encode-to-string.html) method:

```kotlin
val dataAsString: String = Json.encodeToString(user)
```

When we run the above line of code, we will get our data class in string form.

De-serializing our data is as simple as serializing it. We will use the [Json.decodeFromString](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/decode-from-string.html) method:

```kotlin
val user: UserModel = Json.decodeFromString<UserModel>(dataAsString)
```

> ✋ Notice that we specified which type of data we want to de-serialize to with the type parameter (<UserModel>).

![Image](https://images.unsplash.com/photo-1600176842064-635fe81d2441?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDMwfHxyZW1vdGUlMjBjb250cm9sfGVufDB8fHx8MTY3NTAxODM0NQ&ixlib=rb-4.0.3&q=80&w=2000)
_Photo by [Unsplash](https://unsplash.com/@macroman?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Immo Wegmann</a> / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)_

Time for some extra credit.

Let’s say that in your data class you have a field that you don’t want to serialize. If we take our UserModel class, imagine that we want to have a user’s actual picture (bitmap).

```kotlin
@Serializable
data class UserModel(
   @SerialName("first-name")
   val firstName: String,
   val lastName: String,
   val age: Int,
   val birthdate: Date,
   val id: Long,
   var photo: Bitmap?
)
```

This is not something we will get from our API call, so how can we exclude it? Because if we don’t, our serialization will fail.

Here to our rescue is the [**@Transient** annotation](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-transient/).

```
@Serializable
data class UserModel(
   @SerialName("first-name")
   val firstName: String,
   val lastName: String,
   val age: Int,
   val birthdate: Date,
   val id: Long,
   @Transient
   var photo: Bitmap?
)
```

This will exclude the marked field from being serialized and de-serialized.

* If you want to see a real life example of using serialization inside a project, you can check out a project I made [here](https://medium.com/r?url=https%3A%2F%2Fgithub.com%2FTomerPacific%2Fmovies-presenter)
* And if you would like to read other articles I have written, you can go [here](https://medium.com/r?url=https%3A%2F%2Fgithub.com%2FTomerPacific%2FMediumArticles)
* For more information about the kotlin-serialization library, you can go [here](https://github.com/Kotlin/kotlinx.serialization/blob/master/docs/basic-serialization.md#json-encoding)

Thank you for reading! Happy serializing.

