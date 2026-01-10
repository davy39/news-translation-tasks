---
title: Functional Programming for Android Developers — Part 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-07T11:51:59.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-for-android-developers-part-4-b7e1d436a62b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P4uiwrwGsjs6pDls38RTZw.jpeg
tags:
- name: Android
  slug: android
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anup Cowkur

  In the last post, we learned about higher order functions and closures. In this
  one, we’ll talk about functional error handling.

  If you haven’t read part 3, please read it here.

  Functional error handling

  If you’ve been following this s...'
---

By Anup Cowkur

In the last post, we learned about _higher order functions_ and c_losures_. In this one, we’ll talk about _functional error handling._

If you haven’t read part 3, please read it [here](https://medium.freecodecamp.org/functional-programming-for-android-developers-part-3-f9e521e96788).

### Functional error handling

If you’ve been following this series so far, you might have noticed a recurring theme in FP: _Everything is a computation or a value._

We create functions which can optionally take some values. They then perform some useful computation and return other values.

In most OOP programming, we treat errors as _exceptions —_ things that are not part of the computation result. The big difference in FP is that we model errors just like any other value. _Errors are a natural part of computation, not extraneous agents of evil that showed up out of nowhere._

Here’s an example of some typical error handling in OOP:

```
try {  result = readFromDB()} catch (e: Exception) {  result = null}
```

The result of the function `readFromDb` is an error, but it’s not represented as a result of the computation. Instead, it’s a side effect handled somewhere else in the catch block.

This kind of code is very hard to parse and understand when there are multiple operations in a sequence which can produce errors (which is a very common case):

```
try {   data = readFromDB()   newData = doSomethingWithData(data)   isSuccess = putModifiedDataInDb(newData)} catch (e: Exception) {   // Which one of the operations caused this exception?   isSuccess = false}
```

If any one of these operations fail, it’s really hard to detect which one failed unless you put a try catch around each operation. Further, if future operations are dependent on the result of the previous operations, then you’d have to keep state of whether the previous operations have failed or not before executing future operations:

```
fun updateDbData(): Boolean {    try {       data = readFromDb()    } catch (e: Exception) {       data = null    }        if(data == null) {        return false    }        try {       newData = doSomethingWithData(data)    } catch (e: Exception) {        newData = null    }        if(newData == null) {        return false    }        try {       return putModifiedDataInDb(newData)    } catch (e: Exception) {        return false    }     }
```

Ewww.

#### So how do we improve this in a functional way?

Simple, _let’s model failures as part of the result of the operation itself instead of an out of band process._

Many functional languages also have exception handling, but it’s generally encouraged to ignore them. It’s much easier to reason about code where the failures and successes are a natural part of the computation itself.

Let’s see what that looks like. Let’s make a [Kotlin data class](https://kotlinlang.org/docs/reference/data-classes.html) that encapsulates the result of our operation. This class will keep state of the success/failure state as well as the result data:

```
data class Result(val data: Data = Data(), val success: Boolean = false)
```

`success` will tell us if the operation succeeded or failed. `data` is the data we need from the computation. We only access this if the `success` value is `true`(if the operation has succeeded).

Let’s use this to model our previous example:

```
fun updateDbData(): Boolean {       val result1 = readFromDb()       if(!result1.success) {        return false    }        val result2 = doSomethingWithData(result1.data)       if(!result2.success) {        return false    }        val result3 = putModifiedDataInDb(result2.data)       if(!result3.success) {        return false    }        return true}
```

Much better.

All we have done here is encapsulate computation errors as part of the natural computation.

Congratulations! We’ve just built a **_Maybe_** monad!

A Maybe monad represents the presence or absence of a value (hence the name _maybe_) which makes it perfect to represent computations that only have result data if they succeed.

But wait! Why do we need the `success` variable at all? If we use Kotlin’s nullable type to represent the `Data` object, we can ensure that data is only present if computation succeeds.

So our `Result` class is now:

```
data class Result(val data: Data?)
```

and our function becomes:

```
fun updateDbData(): Boolean {       val result1 = readFromDb()       if(result1.data == null) {        return false    }        val result2 = doSomethingWithData(result1.data)       if(result2.data == null) {        return false    }        val result3 = putModifiedDataInDb(result2.data)       if(result3.data == null) {        return false    }        return true}
```

You see? Kotlin’s optional types are just **_Maybe_** monads!

![Image](https://cdn-media-1.freecodecamp.org/images/EMAzcG7SugWj0cXAYPibjcmvZJ1eUYFc9Unc)

We can make this code even nicer if we get rid of the data class altogether and just use the optional type directly:

```
fun updateDbData(): Boolean {    readFromDb()?. let {        doSomethingWithData(it)?.let {            putModifiedDataInDb(it)?.let {                return true            }        }    }        return false}
```

We are using Kotlin’s `?.let` syntax which only executes a lambda if the variable it’s applied to is not null.

Neat huh?

### Yeah, but what’s a Monad?

Monads are computation builders. They encapsulate types, specific ways to combine those types, and operations on those types.

For example, in our function above, Kotlin’s optional type can be used to encapsulate an operation result. When combined with the `?.let` operator, it only allows the lambda to be executed if the result of the operation is non null. It allows us to _express computation results and combine them in specific ways according to a defined ruleset._

Monads come from category theory, and to truly understand the mathematical meaning of them, we will have to study that meaning. The good news however, is that we don’t need to get a masters in math to use ‘em. A basic understanding will do for our purposes, and as we get more into FP, we can keep on increasing your knowledge.

### The ‘Either’ Monad

The _Maybe_ monad let’s us model the presence or absence of a result. But what about a computation that can have two valid result paths? For example, we might want to return a default value for a computation instead of an absent value like null.

This is where the **_Either_** monad comes in. It can represent a `good` and `bad` value. Usually `left` is used to indicate a failure and `right` is used to indicate success.

Let’s see an example. Suppose we have a function `getUser`. If no user is present, it’ll give us an anonymous user. Otherwise it’ll give us the current logged in user.

We can model it as an _Either_ like this:

```
data class Either(val left: AnonUser?, val right: CurrentUser?)
```

and we can use it in calling code like this:

```
fun updateProfileData(): Boolean {    val either = getUser()        if(either.left) {        // can't update profile for anon user        return false    }    else {        updateProfile(either.right)        return true    }}
```

### More resources

You can find plenty of explanations on monads around the web like [this one](http://blog.jorgenschaefer.de/2013/01/monads-for-normal-programmers.html). If you wanna go deep and learn FP along with monads, I’d recommend the excellent free book [Learn You A Haskell For Great Good](http://learnyouahaskell.com/chapters).

The monad implementations I’ve describe here are incomplete and mostly for the purpose of understanding the concepts. You can find more robust implementations in projects like [kotlin-monads](https://github.com/h0tk3y/kotlin-monads).

### Summary

Functional programming encourages treating errors as part of the computation itself and not as aberrations to the regular flow of control. This makes control flow easier to understand, handle, and test. We achieve this easily by representing computation results using Kotlin’s optional types or our own custom monad implementations.

In the next and final part of this series, we’ll look at implementing a functional architecture on Android by tying together all the concepts we have learned so far.

_If you liked this, click the ? below. I notice each one and I’m grateful for every one of them._

_For more musings about programming, follow me so you’ll get notified when I write new posts._

