---
title: You can finally declare Inferred Type local variables in Java with var — here’s
  why that’s awesome
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/you-can-finally-declare-local-variables-in-java-with-var-heres-why-that-s-awesome-4418cb7e2da3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*sJnvQ7q-_Vd6XVUa
tags:
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By javinpaul

  Hello everyone! In this article, I’ll discuss new features of Java 10. Specifically,
  I am going to talk about probably the most popular and most useful: the introduction
  of the var keyword in Java. Well, it’s not really a keyword — but I...'
---

By javinpaul

Hello everyone! In this article, I’ll discuss new features of **Java 10.** Specifically, I am going to talk about probably the most popular and most useful: the **introduction of the var keyword in Java.** Well, it’s not really a keyword — but I’ll tell you about it later.

### At long last…

Finally, Java has gotten the **var** keyword to declare **local variables.** This allows you to declare a variable without its type. For example, instead of doing this:

`String str = “Java”`

you can now just say this:

`var str = “Java”.`

This may not sound like much to gain when you’re declaring a String or an int variable, but think about complex types with generics, for example. This will surely save a lot of typing, and will also improve the readability of the code.

#### A little background

Java developers have long been complaining about boilerplate code and the ceremonies involved while writing code. Many things which take just 5 minutes in languages like [Python](http://javarevisited.blogspot.sg/2018/03/top-5-courses-to-learn-python-in-2018.html), [Groovy](http://javarevisited.blogspot.sg/2017/08/top-5-books-to-learn-groovy-for-java.html), or [JavaScript](http://javarevisited.blogspot.sg/2017/02/top-5-javascript-books-to-learn-best-of-lot-must-read.html) can take more than 30 minutes in Java due to its verbosity.

If you have coded in Scala, Kotlin, Go, C# or any other [JVM language](https://javarevisited.blogspot.com/2018/02/top-3-jvm-languages-java-programmer-learn.html), then you know that they all have some kind of local variable type inference already built into the language.

For example, JavaScript has **let** and **var**, [Scala](http://javarevisited.blogspot.sg/2018/01/10-reasons-to-learn-scala-programming.html#axzz550Ppgfxg) and [Kotlin](http://www.java67.com/2017/12/10-programming-languages-to-learn-in.html) have **var** and **val**, C++ has the **auto**, C# has **var,** and Go supports this by declaration with the **:=** operator.

Until [Java 10](http://javarevisited.blogspot.sg/2018/03/java-10-released-10-new-features-java.html), Java was the only language which didn’t have local variable type inference or support for the var keyword.

Though type inference was improved a lot in Java 8 with the introduction of the lambda expression, method references, and Streams, local variables still needed to be declared with proper type. But that’s now gone! [Java 10](http://javarevisited.blogspot.sg/2018/03/java-10-released-10-new-features-java.html#axzz5ALJyiIAt) has a feature, [**JEP 286: Local-Variable Type Inference**](http://openjdk.java.net/jeps/286)**,** which will allow declaring local variables without type information and by just using the var keyword.

Let’s take a closer look.

### Java 10 var keyword examples

Here are some examples of Java 10's var keyword:

```
var str = "Java 10"; // infers String 
```

```
var list = new ArrayList<String>(); // infers ArrayList<String>
```

```
var stream = list.stream(); // infers Stream<String>
```

As I said, at this point you may not fully appreciate what var is doing for you. But look at the next example:

```
var list = List.of(1, 2.0, "3")
```

Here, the list will be inferred into **List<? extends Serializable & Comparable&l**t;..>> which is an intersection type, but you won’t have to type the full type information. var makes the code much easier to write and read in this case.

In next section, we’ll see some more examples that’ll help you learn how to write concise code using var in Java 10.

### Writing concise code using the var keyword in Java

The use of the var reserve word also makes your code concise by reducing duplication — for example, the name of the Class which comes on both the right and left-hand side of assignments as shown in the following example:

```
ByteArrayOutputStream bos = new ByteArrayOutputStream();
```

Here [ByteArrayOutputStream](https://docs.oracle.com/javase/10/docs/api/java/io/ByteArrayOutputStream.html) repeats twice, and we can eliminate that by using the var feature of Java 10 as shown below:

```
var bos = new ByteArrayOutputStream();
```

We can do similar things while using [try-with-resource](https://javarevisited.blogspot.com/2011/09/arm-automatic-resource-management-in.html) statements in Java, for example this

```
try (Stream<Book> data = dbconn.executeQuery(sql)) {    return data.map(...) .filter(...) .findAny(); }
```

can be written as follows:

```
try (var books = dbconn.executeQuery(query)) {   return books.map(...) .filter(...) .findAny(); }
```

These are just a few examples. There are a lot of places where you can use var to make your code more concise and readable, many of which you can see on Sander’s Pluarlsight course [**What’s New in Java 10**](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwhats-new-java-10-local-variable-type-inference).

It’s a paid course but you can check out this [10-day free trial](http://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Flearn).

![Image](https://cdn-media-1.freecodecamp.org/images/unYRUbTTXMNdA-id-rw25UbXpaksermD2GOc)

For those programmers who have used [Groovy](http://javarevisited.blogspot.sg/2016/09/10-basic-differences-between-java-and-groovy-programming.html#axzz5ArdIFI7y) or [Scala](http://javarevisited.blogspot.sg/2017/12/top-5-courses-to-learn-big-data-and.html#axzz5ArdIFI7y), the introduction of var makes it seem like Java is going the Scala way…but only time will tell.

For now, we can just be happy that **var makes it easier to declare a complex local variable in Java 10.**

And do note: the local variable type inference of the Java 10 var keyword can only be used to declare [local variables](http://javarevisited.blogspot.sg/2012/02/difference-between-instance-class-and.html#axzz5ArdIFI7y) (for example, any variable inside the method body or code block).

### Can you use var to declare member variables in Java?

You **cannot** use var to declare member variables inside the class, method formal parameters or return type of methods.

For example, this example of var is OK:

```
public void aMethod(){ var name = "Java 10"; } 
```

But, following example is NOT OK:

```
class aClass{   var list; // compile time error }
```

So, even though this [new Java 10 feature](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwhats-new-java-10-local-variable-type-inference) is eye-catching and looks good, it still has a long way to go. Still, you can start using it to further simplify your code. Less boilerplate code always means better and more readable code.

### Important points about this new var keyword

Now that you know that you can declare local variables without declaring the type in Java 10, it’s time to learn a few important things about this feature before you start using it in your production code:

1. This feature is built under **JEP 286: Local-Variable Type Inference** and was authored by none other than [Brian Goetz](https://www.freecodecamp.org/news/you-can-finally-declare-local-variables-in-java-with-var-heres-why-that-s-awesome-4418cb7e2da3/undefined). He’s the author of [Java Concurrency in Practice](http://www.amazon.com/dp/0321349601/?tag=javamysqlanta-20), one of the most popular books for Java developers.

2. The var keyword allows local variable type inference, which means the type for the [local variable](https://javarevisited.blogspot.com/2012/02/difference-between-instance-class-and.html) will be inferred by the compiler. Now you don’t need to declare it.

3. The local variable type inference or Java 10 var keyword can only be used to declare **local variables**, for example inside methods, on initializers code block, indexes in the [enhanced for loop](http://javarevisited.blogspot.sg/2017/01/difference-between-for-loop-and-enhanced-forlop-in-java.html#axzz4pp42TeHu), [lambda expressions](http://www.java67.com/2017/06/10-points-about-lambda-expressions-in-java-8.html), and local variables declared in a traditional for loop.

You cannot use it for declaring formal variables and return types of methods, for declaring member variables or fields, on constructor formal variables, and any other kind of variable declaration.

4. Despite the introduction of var, Java is still a statically typed language and there should be enough information to infer the type of the local variable. If not, the compiler will throw an error.

5. The var keyword is similar to the auto keyword of C++, var of C#, [JavaScript](http://javarevisited.blogspot.sg/2018/01/top-10-udemy-courses-for-java-and-web-developers.html), [Scala](http://javarevisited.blogspot.sg/2017/03/top-30-scala-and-functional-programming.html), [Kotlin](http://javarevisited.blogspot.sg/2018/02/5-courses-to-learn-kotlin-programming-java-android.html), def of [Groovy](http://javarevisited.blogspot.sg/2018/02/top-3-jvm-languages-java-programmer-learn.html#axzz56WXxxAC0) and [Python](http://www.java67.com/2018/02/5-free-python-online-courses-for-beginners.html) (to some extent), and the : = operator of the Go programming language.

6. One important thing to know is that, even though var looks like a keyword, it’s not really a keyword. Instead, it is a reserved type name. This means that code that uses var as a variable, method, or package name will not be affected.

7. Another thing to note is that code that uses var as a class or interface name will be affected by this Java 10 change. But as JEP says, these names are rare in practice, since they violate usual naming conventions.

8. The [immutable](http://javarevisited.blogspot.sg/2018/02/java-9-example-factory-methods-for-collections-immutable-list-set-map.html) equivalent of local variables or final variables val and let is not yet supported in Java 10.

### Wrapping up

That’s all about the **var in Java 10!** It’s an interesting Java 10 feature, which allows you to declare local variables without declaring their type. This will also help Java developers pick up other languages quickly, like [Python](https://javarevisited.blogspot.com/2018/05/10-reasons-to-learn-python-programming.html), [Scala](https://javarevisited.blogspot.com/2018/01/10-reasons-to-learn-scala-programming.html#axzz550Ppgfxg), or [Kotlin](https://hackernoon.com/should-android-developers-learn-kotlin-or-java-ee391902736f), because they heavily use var to declare mutable variables and val to declare immutable local variables.

Even though **JEP 286: Local-Variable Type Inference** only supports **var** and not **val**, it is still useful and feels more like coding Scala in Java.

#### **Further Learning**

[What’s New in Java 10 by Sander Mak](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwhats-new-java-10-local-variable-type-inference)  
 [Style Guidelines for Local Variable Type Inference in Java](http://openjdk.java.net/projects/amber/LVTIstyle.html)  
 [JEP 286: Local-Variable Type Inference](http://openjdk.java.net/jeps/286)  
 [10 Things Java Developer Should learn in 2018](http://javarevisited.blogspot.sg/2017/12/10-things-java-programmers-should-learn.html#axzz53ENLS1RB)  
 [The Complete Java MasterClass to learn Java Better](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fjava-the-complete-java-developer-course%2F)

Thanks for reading this article. If you like this **new Java 10 feature,** then please share with your friends and colleagues.

If you have any questions or feedback, please drop a note and stay tuned for more Java 10 tutorials and articles here.

_Originally published at [javarevisited.blogspot.com](https://javarevisited.blogspot.com/2018/03/finally-java-10-has-var-to-declare-local-variables.html) on March 27, 2018._

