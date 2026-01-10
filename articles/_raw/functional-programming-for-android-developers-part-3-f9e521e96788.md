---
title: Functional Programming for Android Developers — Part 3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-06T05:21:43.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-for-android-developers-part-3-f9e521e96788
coverImage: https://cdn-media-1.freecodecamp.org/images/1*exgznl7z65gttRxLsMAV2A.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Anup Cowkur

  In the last post, we learned about immutability and concurrency. In this one, we’ll
  look at Higher Order Functions and Closures.

  If you haven’t read part 2, please read it here:

  Functional Programming for Android Developers — Part 2_In...'
---

By Anup Cowkur

In the last post, we learned about _immutability_ and _concurrency_. In this one, we’ll look at _Higher Order Functions_ and _Closures._

If you haven’t read part 2, please read it here:

[**Functional Programming for Android Developers — Part 2**](https://medium.freecodecamp.com/functional-programming-for-android-developers-part-2-5c0834669d1a)  
[_In the last post, we learned about Purity, Side effects and Ordering. In this part, let’s talk about immutability and…_medium.freecodecamp.com](https://medium.freecodecamp.com/functional-programming-for-android-developers-part-2-5c0834669d1a)

### Higher Order Functions

Higher Order Functions are functions that can take functions as parameters and returns functions as results. Cool, huh?

But why would anyone wanna do that?

Let’s take an example. Suppose I want to compress a bunch of files. I want to do this two ways — using ZIP or RAR format. To do this in traditional Java, we would use something like the [Strategy Pattern](https://en.wikipedia.org/wiki/Strategy_pattern).

Firstly, I’d make an interface that defines the strategy:

```
public interface CompressionStrategy {    void compress(List<File> files);}
```

Then I would implement the two strategies like so:

```
public class ZipCompressionStrategy implements CompressionStrategy {    @Override public void compress(List<File> files) {        // Do ZIP stuff    }}
```

```
public class RarCompressionStrategy implements CompressionStrategy {    @Override public void compress(List<File> files) {        // Do RAR stuff    }}
```

Then at runtime, I can use one of these strategies:

```
public CompressionStrategy decideStrategy(Strategy strategy) {    switch (strategy) {        case ZIP:            return new ZipCompressionStrategy();        case RAR:            return new RarCompressionStrategy();    }}
```

That’s a lot of code and ceremony.

All we are trying to do here is try to do two different bits of business logic depending on some variable. Since business logic can’t live on it’s own in Java, we have to dress it up in classes and interfaces.

Wouldn’t it be great if we could directly pass in the business logic? That is, if we could treat functions as variables, could we pass business logic around just as easily as variables and data?

This is **exactly** what higher order functions are for!

Let’s see the same example with Higher Order Functions. I’m going to use [Kotlin](https://kotlinlang.org/) here, since Java 8 lambdas still involve [some ceremony of creating functional interfaces](https://stackoverflow.com/a/13604748/1369222) which we’d like to avoid.

```
fun compress(files: List<File>, applyStrategy: (List<File>) -> CompressedFiles){    applyStrategy(files)}
```

The `compress` method takes two parameters — a list of files and a function called `applyStrategy` which a function of type `List<File> -> Compres`sedFiles.That is, it’s a function that takes a list of files and `returns Compre`ssedFiles.

Now we can call `compress` with any function that takes a list of files and returns compressed files:

```
compress(fileList, {files -&gt; // ZIP it})
```

```
compress(fileList, {files -&gt; // RAR it})
```

Better. Much better.

So Higher Order Functions allow us to pass logic around and treat code as data. Neat.

### Closures

Closures are functions that capture their environments. Let’s understand this with an example. Suppose I have a click listener on a view and we want to print some value inside it:

```
int x = 5;view.setOnClickListener(new View.OnClickListener() {    @Override public void onClick(View v) {        System.out.println(x);    }});
```

Java won’t let us do this since `x` isn’t final. `x` has to be final in Java since the click listener can be executed anytime and at the time it is executed, `x` might not be around anymore or it’s value might have changed. Java forces us to make this variable final to effectively make it immutable.

Once it’s immutable, Java will know that `x` is always going to be `5` whenever the click listener is executed. This system isn’t perfect since `x` can point to a list which can be mutated even though the reference to the list is the same.

Java doesn’t have a mechanism for a function to capture and respond to variables that are outside it’s scope. Java functions cannot capture or _close_ over their environment.

Let’s try doing the same thing in Kotlin. We don’t even need an anonymous inner class since we have first class functions in Kotlin:

```
var x = 5view.setOnClickListener { println(x) }
```

This is perfectly valid in Kotlin. Functions in Kotlin are _closures._ They can keep track of and respond to updates in their environment.

The first time the click listener is triggered, it will print `5`. If we then change the value of `x` and say `x = 9` and trigger the click listener again, it will print `9` this time.

#### So what can I do with these closures?

Closures have many nifty use cases. Anytime you want business logic to respond to some state in the environment, you can use closures.

Suppose you have a click listener on a button that shows a dialog with a bunch of messages to the user. If you don’t have closures, you’d have to initialize a new listener with the new list of messages every time the messages change.

With closures, you can store the list of messages somewhere and pass the reference to the list in the listener, like we did above, and the listener will always show the latest set of messages.

**Closures can also be used to completely replace objects.** This is often used in functional languages where you might need some OOP like behavior and the language doesn’t support them.

Let’s see an example:

```
class Dog {    private var weight: Int = 10    fun eat(food: Int) {        weight += food    }    fun workout(intensity: Int) {        weight -= intensity    }}
```

I have dog that gains weight when we feed it and loses weight when it exercises. Can we describe the same behavior with closures?

```
fun main(args: Array<String>) {   dog(Action.feed)(5)}
```

```
val dog = { action: Action ->    var weight: Int = 10
```

```
when (action) {        Action.feed -> { food: Int -> weight += food; println(weight) }        Action.workout -> { intensity: Int -> weight -= intensity; println(weight) }    }}
```

```
enum class Action {    feed, workout}
```

The `dog` function takes an `Action` and depending on the action, will either feed the dog or get it to workout. When we call `dog(Action.feed)(5)` in the `main` function, the result will be `15`. The `dog` function is taking a `feed` action and returning another function that will feed the dog. When we pass the value `5` to this returned function, it will increment the dog’s weight to `10 + 5 = 15` and print it out.

> So combining Closures and Higher Order Functions, we can get Objects without OOP.

![Image](https://cdn-media-1.freecodecamp.org/images/3kHTFLmBq02uXvhIh4MNZingIOakRfXUKnNK)

You probably don’t wanna do this in real code but it’s fun to know it can be done. Indeed, Closures are called the [_poor man’s objects_](http://wiki.c2.com/?ClosuresAndObjectsAreEquivalent)_._

### Summary

Higher Order Functions allow us to encapsulate business logic better than OOP in many cases and we can pass them around and treat them as data. Closures capture their surrounding environment and help us use Higher Order Functions effectively.

In the next part, we’ll learn about error handling in a functional way.

_If you liked this, click the ? below. I notice each one and I’m grateful for every one of them._

_For more musings about programming, follow me so you’ll get notified when I write new posts._

