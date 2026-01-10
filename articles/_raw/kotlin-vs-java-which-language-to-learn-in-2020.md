---
title: Kotlin VS Java – Which Programming Language Should You Learn?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-27T19:10:12.000Z'
originalURL: https://freecodecamp.org/news/kotlin-vs-java-which-language-to-learn-in-2020
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9987740569d1a4ca2041.jpg
tags:
- name: Java
  slug: java
- name: Kotlin
  slug: kotlin
- name: programming languages
  slug: programming-languages
seo_title: null
seo_desc: 'By Pramono Winata

  It has been several years since Kotlin came out, and it has been doing well. Since
  it was created specifically to replace Java, Kotlin has naturally been compared
  with Java in many respects.

  To help you decide which of the two langu...'
---

By Pramono Winata

It has been several years since Kotlin came out, and it has been doing well. Since it was created specifically to replace Java, Kotlin has naturally been compared with Java in many respects.

To help you decide which of the two languages you should pick up, I will compare some of the main features of each language so you can choose the one you want to learn.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/asa-1-1.jpg align="left")

These are the 8 points I'll discuss in this article:

* Syntax
    
* Lambda Expressions
    
* Null Handling
    
* Model Classes
    
* Global Variables
    
* Concurrency
    
* Extension Functions
    
* Community
    

## Syntax comparison

To start it all let's do some basic syntax comparison. Many of you who are reading this might already have some knowledge about Java and/or Kotlin, but I will give out a basic example below so we can compare them directly:

### Java

```java
public class HelloClass { 

	public void FullName(String firstName, String lastName) {
    	String fullName = firstName + " " + lastName;
		System.out.println("My name is : " + fullName); 
	} 
    
    	public void Age() { 
		int age = 21;
		System.out.println("My age is : " + age); 
	} 

	public static void main(String args[]) { 
		HelloClass hello = new HelloClass(); 
		hello.FullName("John","Doe");
        hello.Age();
	} 
}
```

### Kotlin

```kotlin
class NameClass {
    fun FullName(firstName: String, lastName:String) {
        var fullName = "$firstName $lastName"
        println("My Name is : $fullName")
    }
}

fun Age() {
	var age : Int
    age = 21
    println("My age is: $age")
}

fun main(args: Array<String>) {
    NameClass().FullName("John","Doe")
    Age()
}
```

The feel of the code isn't that different aside from some small syntax changes in the methods and classes.

But the real difference here is that Kotlin supports type inference where the variable type does not need to be declared. Also we don't need semicolons ( `;` ) anymore.

We can also note that Kotlin does not strictly enforce OOP like Java where everything must be contained inside a class. Take a look at `fun Age` and `fun main` in the example where it is not contained inside any class.

Kotlin also typically has fewer lines of codes, whereas Java adheres more to a traditional approach of making everything verbose.

One advantage of Kotlin over Java is Kotlin's flexibility – it can choose to do everything in the traditional OOP approach or it can go a different way.

## Lambda Expressions

If we are talking about Java and Kotlin, of course we have to talk about the famous lambda expression. Kotlin has native Lambda support (and always has), while lambda was first introduced in Java 8.

Let's see how they both look.

### Java

```java
//syntaxes
parameter -> expression
(parameter1, parameter2) -> { code }

//sample usage
ArrayList<Integer> numbers = new ArrayList<Integer>();
numbers.add(5);
numbers.add(9);
numbers.forEach( (n) -> { System.out.println(n); } );
```

### Kotlin

```kotlin
//syntax
{ parameter1, parameter2 -> code }

//sample usage
max(strings, { a, b -> a.length < b.length })
```

In Java, the parentheses are more lenient: if only one parameter exists, there is no need for parenthesis. But in Kotlin brackets are always required. Overall, however, there are not many differences aside from syntax.

In my opinion, lambda functions won't be used much aside from using them as callback methods. Even though lambda functions have so many more uses, **readability** issues make it less desirable. They'll make your code shorter, but figuring out the code later will be much more difficult.

It's just a matter of preference, but I think it's helpful that Kotlin enforces the mandatory brackets to help with readability.

## Null Handling

In an object oriented language, null type values have always been an issue. This issue comes in the form of a Null Pointer Exception (NPE) when you're trying to use the contents of a null value.

As NPEs have always been an issue, both Java and Kotlin have their own way of handling null objects, as I will show below.

### Java

```java
Object object = objServ.getObject();

//traditional approach of null checking
if(object!=null){
    System.out.println(object.getValue());
}

//Optional was introduced in Java 8 to further help with null values

//Optional nullable will allow null object
Optional<Object> objectOptional = Optional.ofNullable(objServ.getObject());

//Optional.of - throws NullPointerException if passed parameter is null
Optional<Object> objectNotNull = Optional.of(anotherObj);

if(objectOptional.isPresent()){
    Object object = objectOptional.get();
    System.out.println(object.getValue());
}

System.out.println(objectNotNull.getValue());
```

### Kotlin

```kotlin
//Kotlin uses null safety mechanism
var a: String = "abc" // Regular initialization means non-null by default
a = null // compilation error

//allowing null only if it is set Nullable
var b: String? = "abc" // can be set null
b = null // ok
print(b)
```

For as long as I can remember, Java has been using traditional null checking which is prone to human error. Then Java 8 came out with optional classes which allow for more robust null checking, especially from the API/Server side.

Kotlin, on the other hand, provides null safety variables where the variable must be nullable if the value can be null.

I haven't really used optional class yet, but the mechanism and purpose seems pretty similar to Kotlin's null safety. Both help you identify which variable can be null and help you make sure the correct check is implemented.

Sometimes in code there might be just too many variables lying around and too many to check. But adding checking everywhere makes our code base ugly, and nobody likes that, right?

In my opinion, though, using Java's optional feels a bit messy because of the amount of code that needs to be added for the checks. Meanwhile in Kotlin, you can just add a small amount of code to do null checking for you.

## Model Class

Some people might also refer to this as the Entity class. Below you can see how both classes are used as model classes in each language.

### Java

```java
public class Student {

     private String name;
     private Integer age;
     
     // Default constructor
  	 public Student() { }

     public void setName(String name) {
         this.name = name;
     }

     public String getName() {
         return name;
     }
     
     public void setAge(Integer age) {
         this.age = age;
     }

     public Integer getAge() {
         return age;
     }
}
```

### Kotlin

```kotlin
//Kotlin data class
data class Student(var name: String = "", var age: Int = 0)

//Usage
var student: Student = Student("John Doe", 21)
```

In Java, properties are declared as private, following the practice of encapsulation. When accessing these properties, Java uses Getters and Setters, along with the isEqual or toString methods when needed.

On the Kotlin side, [data classes](https://kotlinlang.org/docs/reference/data-classes.html) are introduced for the special purpose of model classes. Data classes allow properties to be directly accessed. They also provide several in-built utility methods such as equals(), toString() and copy().

For me, data classes are one of the best things Kotlin offers. They aim to reduce the amount of the boilerplate code you need for regular model classes, and they do a really good job of that.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-164.png align="left")

*Random Pic because you are halfway there! Photo by \[Unsplash\](https://unsplash.com/@dinoreichmuth?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit"&gt;Dino Reichmuth / &lt;a href="https://unsplash.com/?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit)*

## Global Variables

Sometimes your code might need a variable needs to be accessed everywhere in your code base. This is what global variables are used for. Kotlin and Java each have their own ways of handling this.

### Java

```java
public class SomeClass {
	public static int globalNumber = 10;
}

//can be called without initializing the class
SomeClass.globalNumber;
```

### Kotlin

```kotlin
class SomeClass {
    companion object {
        val globalNumber = 10
    }
}

//called exactly the same like usual
SomeClass.globalNumber
```

Some of you might already be familiar with the [static](https://www.javatpoint.com/static-keyword-in-java) keyword here since it's also used in some other language like C++. It's initialized at the start of a program's execution, and is used by Java to provide global variables since it is not contained as an Object. This means it can be accessed anywhere without initializing the class as an object.

Kotlin is using quite a different approach here: it removes the static keyword and replaces it with a [companion object](https://kotlinlang.org/docs/tutorials/kotlin-for-py/objects-and-companion-objects.html) which is pretty similar to a singleton. It let's you implement fancy features such as extensions and interfacing.

The lack of the static keyword in Kotlin was actually quite surprising for me. You could argue that using the static keyword might not be a good practice because of its nature and because it's difficult to test. And sure, the Kotlin companion object can easily replace it.

Even then, using static for global variable should be simple enough. If we are careful with it and don't make it a habit of making every single thing global, we should be good.

The companion object might also give us some flexibility with interfacing and such, but how often will we ever be interfacing singleton classes?

I think static keywords help us keep things short and clean for global variables.

## Concurrency

Nowadays, concurrency is a hot topic. Sometimes the ability of a programming language to run several jobs concurrently might help you decide if that will be your language of choice.

Let's take a look at how both languages approach this.

### Java

```java

// Java code for thread creation by extending 
// the Thread class 
class MultithreadingDemo extends Thread 
{ 
    public void run() 
    { 
        try
        { 
            // Displaying the thread that is running 
            System.out.println ("Thread " + 
                  Thread.currentThread().getId() + 
                  " is running"); 
  
        } 
        catch (Exception e) 
        { 
            // Throwing an exception 
            System.out.println ("Exception is caught"); 
        } 
    } 
} 
  
// Main Class 
public class Multithread 
{ 
    public static void main(String[] args) 
    { 
        int n = 8; // Number of threads 
        for (int i=0; i<n; i++) 
        { 
            MultithreadingDemo object = new MultithreadingDemo(); 
            object.start(); 
        } 
    } 
}
```

### Kotlin

```kotlin
for (i in 1..1000)
    GlobalScope.launch {
        println(i)
    }
```

Java mostly uses [threads](https://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html) to support concurrency. In Java, making a thread requires you to make a class that extends to the in-built Java thread class. The rest of its usage should be pretty straightforward.

While threads are also available in Kotlin, you should instead use its [coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html). Coroutines are basically light-weight threads that excel in short non-blocking tasks.

Concurrency has always been a hard concept to grasp (and also, to test). Threading has been used for a long time and some people might already been comfortable with that.

Coroutines have become more popular lately with languages like Kotlin and Go (Go similarly has goroutines). The concept differs slightly from traditional threads – [coroutines are sequential while threads can work in parallel](https://stackoverflow.com/a/1934718/6065825).

Trying out coroutines, though, should be pretty easy since Kotlin does a very good job explaining them in their [docs](https://kotlinlang.org/docs/reference/coroutines-overview.html). And one bonus for Kotlin over Java is the amount of boilerplate code that can be removed in Kotlin.

## Extension Functions

You might be wondering why I'm bringing these up since Java itself doesn't even have this feature.

But I can't help but mention it, because extension functions are a very useful feature that was introduced in Kotlin.

```kotlin
fun Int.plusOne(): Int {
	return this + 1
}

fun main(args: Array<String>) {
    var number = 1
    var result = number.plusOne()
    println("Result is: $result")
}
```

They allow a class to have new functionality without extending it into the class or using any of the fancy Design Patterns. It even lets you to add functionality to Kotlin variable classes.

You can practically say goodbye to those lib method that need you to pass everything inside your parameters.

## Community

Last but not least, let's talk about something non-technical. First, let's take a look at this survey showing top commonly used programming languages in 2020.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-from-2020-07-24-23-05-40.png align="left")

*taken from* [*stack overflow survey*](https://insights.stackoverflow.com/survey/2020#development-environments-and-tools)

We can see that Java is one of the most commonly used languages. And while Kotlin is still rising a lot in popularity, the Java community still remains several times larger than Kotlin and it will probably not change anytime soon.

So what does that matter then? Actually it does matter, a lot. With the amount of people in the Java community, it's much easier to find references and get help when you need it, both on the Internet and in the real world.

Many companies are also still using Java as their base and it might not change anytime soon even with Kotlin's interoperability with Java. And usually, doing a migration just doesn't serve any business purpose unless the company has really really important reasons for it.

## Wrapping up

For those just scrolling for the summary, here's what we discussed:

* Syntax: the patterns don't differ that much aside from slight syntax differences, but Kotlin is more flexible in several aspects.
    
* Lambda Expressions: the syntax is almost the same, but Kotlin uses curly brackets to help readability.
    
* Null Handling: Java uses a class to help with null handling while Kotlin uses in-built null safety variables.
    
* Model Classes: Java uses classes with private variables and setter / getter while Kotlin supports it with data classes.
    
* Global Variables: Java uses the static keyword while Kotlin uses something akin to sub-classes.
    
* Concurrency: Java uses multi-threading whereas Kotlin uses coroutines (which are generally lighter).
    
* Extension Functions: a new feature introduced by Kotlin to easily give functionality into classes without extending it.
    
* Community: Java still reigns supreme in the community aspect which makes it easier to learn and get help.
    

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-165.png align="left")

*Photo by \[Unsplash\](https://unsplash.com/@glenncarstenspeters?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit"&gt;Glenn Carstens-Peters / &lt;a href="https://unsplash.com/?utm\_source=ghost&utm\_medium=referral&utm\_campaign=api-credit)*

There are many more features we could compare between Java and Kotlin. But what I've discussed here are, in my opinion, some of the most important.

I think Kotlin is well worth picking up at the moment. From the development side it helps you remove long boilerplate code and keep everything clean and short. If you are already a Java programmer, learning Kotlin shouldn't be too hard and it's okay to take your time at it.

Thanks for reading! I hope that this article will help you decide which programming language you should pick, Java or Kotlin. And for anything that I'm missing, feel free to leave feedback for me as it will be very much appreciated.
