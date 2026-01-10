---
title: Still using Java to develop your Android Apps? Try Kotlin instead.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-11T17:12:27.000Z'
originalURL: https://freecodecamp.org/news/still-using-java-for-android-development-you-should
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/photo-1509803874385-db7c23652552.jpeg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Java
  slug: java
- name: Kotlin
  slug: kotlin
seo_title: null
seo_desc: 'By Pramono Winata

  Kotlin has been a huge breakthrough for the last 2 years, it has been a trending
  topic everywhere and its popularity is still rising. And it is also official that
  Google has pushed Kotlin to become the official language for Android ...'
---

By Pramono Winata

Kotlin has been a huge breakthrough for the last 2 years, it has been a trending topic everywhere and its popularity is still rising. And it is also official that Google has pushed Kotlin to become the official language for Android App Development.

But even then, a lot of people still prefer Java over Kotlin for Android development, why is that? One of the main reason for that is people are still not comfortable in changing their main language of choice from Java to Kotlin, people are afraid of changing into new things.

## Start Using Kotlin now, the easy way

In actuality, it is very easy to switch into Kotlin from Java, being a very flexible language, you can easily code Kotlin but idiomatically, it's Java!

![Image](https://www.freecodecamp.org/news/content/images/2019/07/meme.jpeg)
_It looks kotlin, but actually it's Java. But I assure you, it's all gonna be okay!!_

So now, here are several things to be noted on when switching to Kotlin from Java:

**1. Java Interoperability**  
Kotlin is fully interoperable with Java and also, the other way around. What does that mean, it means that your Kotlin can call your Java code, it makes things very easy for app migration, you already code halfway with Java? Doesn't matter, code Kotlin anyway.

**2. No more primitive data types**  
Remember when choosing either using **int** or **Int** in java takes you half a day? There is no more primitive data types now in Kotlin, everything has been wrapped in Object instead.

**3. Slightly changed syntax (But don't worry it's easy to catch up)**  
Several syntax like variable, function and class declaration has been slightly changed, but if you come from OOP background such as Java, it will not be such an issue. And also, void keyword and semi-colon (';') have been removed, thanks Kotlin for that semicolon removal!!  
I will present you with the basic examples with Android class: 

```kotlin
//Inheritance and implementation is using ':' now
class BasicActivity : AppCompatActivity() {
    //variables declaration is now variable name first then type
    var a :Int = 10 //var is for mutable
    val b :Int = 15 //val is for immutable

    /*lateinit keyword must be added for initialisation of non-
    primitive type without initial value in Kotlin*/
    lateinit var someTextView:TextView

    //Also, no more new keyword here
    var gameList:List<Integer> = ArrayList()

    //overriding is using keyword instead of 
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_basic)
    }
}

```

4. **Type inference**  
Kotlin will make life easier by providing type inference for variables:

```kotlin
var a = 5 //will automatically infer this as integer
var b = "John" // will automatically infer this as String

```

5. **[Null safety](https://kotlinlang.org/docs/reference/null-safety.html) checks**  
Kotlin has provided null safety checking in order to avoid null pointer exception. Every variable that might return null value will be marked (and must be marked) with `?`  sign. 

```kotlin
var a:String? = null
var b:String = null //not allowed 
```

It also provides null safety call in order to avoid Null-Pointer Exception (Java Billon Dollar Mistakes)

```
//not allowed, a might be null
a.function() 

// this will not throw null pointer, instead will continue the flow
a?.function()

//force function call, can cause NPE, use this only if 100% sure that this value will not be null
a!!.function()
```

6. **No more static keyword**  
Static keyword has now been replaced with [Object](https://kotlinlang.org/docs/reference/object-declarations.html) keyword, both for classes and methods, more specifically [Companion Object](https://kotlinlang.org/docs/tutorials/kotlin-for-py/objects-and-companion-objects.html) for methods.  
  
7. **Switch case modified**  
Switch case has now been modified into a new keyword, called [when](https://kotlinlang.org/docs/reference/control-flow.html). Which looks cleaner and more flexible:

```kotlin
when (x) {
    1 -> println("One")
    2 -> print("Two")
	else -> print("Others")
}
```

8. **No more [checked exception](https://www.geeksforgeeks.org/checked-vs-unchecked-exceptions-in-java/)**  
Remember when you were making some operations or casting in Java, and that red warning comes out and told you to add exception checking there? It has been removed now in Kotlin. Now, your IDE will not force you to do any exception anymore!!

That's all for the part which you need to start developing in Kotlin, but idiomatically Java.  
It's not hard to get into Kotlin now, right? Now Kotlin doesn't seem that different from Java.

---

## Features Provided By Kotlin

![Image](https://www.freecodecamp.org/news/content/images/2019/07/download.png)

Now, after taking a look at how Kotlin and Java differ, we also need to take a look at the features provided by Kotlin and how to slowly start doing Kotlin, the Kotlin way:

**1. Flexibility**   
One of the main reasons for my love in Kotlin is the flexibility of the language. Are you OOP purist? Are you itching to try [Functional Programming](https://en.wikipedia.org/wiki/Functional_programming) which currently is the hot topic around? And for the love of _coding_ god, you can do both in Kotlin! Despite not fully providing all the features FP provides, it is good enough to support it. 

**2. [Lambda Support](https://kotlinlang.org/docs/reference/lambdas.html)**  
Yes, I know that now Java 8 supports lambda, but Kotlin came first at this and it does a very good job in that. Sure, transitioning into using Lambda Function will be difficult at first, but as stated, Kotlin is really flexible on that. So hey, it's your call!  
Some of the Android library has also enabled Lambda support, for instance `View.OnClickListener` (If you came from Android Background, I'm certain that this method is already very familiar to you) :

```kotlin
val randomButton : Button

//using lambda function as argument
randomButton.setOnClickListener{v -> doRandomStuff(v) }
```

**3. [Data Class](https://kotlinlang.org/docs/reference/data-classes.html)**  
Kotlin has provided a substitute for Model/Entity class, called [Data](https://kotlinlang.org/docs/reference/data-classes.html) class. It removes the need for redundant setter getter and also has in-built equal method and toString function without you having to make one for it. It's also very easy to utilize: 

```kotlin
data class Person(
    val id:String,
    val name:String = "John Doe" //Default Value
)

//Initialisation block
var person = Person("id","Not John")
```

4. **[Extension Functions](https://kotlinlang.org/docs/reference/extensions.html)**  
Kotlin allows the usage of extension functions, which makes code more readable. Also, it will enable you to give functionality to a class without modifying the class itself:

```kotlin
fun Int.superOperation(anotherInt:Int):Int {
    val superNumber = this * anotherInt + anotherInt
    return superNumber
}

//you can now call the functions
val someNumber = 5
val superNumber = someNumber.superOperation(10) //65
```

5. **[Named and Default Arguments](https://kotlinlang.org/docs/reference/functions.html)**  
Like C#, Kotlin also supports named and default parameters for its methods. It completely removes the need to pass values in each arguments. You can select which value you want to modify, and voila! No more hassles in passing the same particular value for 10 of your function calls!

```kotlin
//variable declaration
fun someOperations(var x: Int, var y:Int, var z:Int = 1){
	return x+y+z
}

someOperations(1,2) //return 4
someOpeartions(y = 1, x = 1) //return 3
```

6. [**Referential Equality**](https://kotlinlang.org/docs/reference/equality.html)  
Kotlin also comes with referential equality ('==='), it will check if two variables are currently referring to the same Object.

```kotlin
var a = 10
var b = 10
a == b //true
a === b //true also, primitive type object equation will only check its value

data class Person (val name: String)

val p1 = Person("John")
val p2 = Person("John")

p1 == p2 //true
p1 === p2 //false
```

7. [**Smart casting**](https://kotlinlang.org/docs/reference/typecasts.html)  
Instead of using instance of, Kotlin now provides easier and more readable syntax to use for casting or type checking:

```kotlin
//type checking
//kotlin smart cast mechanism will also automatically change the object into corresponding type if it passes the type checking
if (shape is Circle) {
    println(“it’s a Circle”)
    shape.radius //automatically be casted as Circle
} else if (shapeObject is Square) {
    println(“it’s a Square”)
} else if (shapeObject is Rectangle) {
    print(“it’s a Rectangle”)
}
```

Kotlin also has `as` keyword to enable explicit casting:

```kotlin
//It's considered unsafe since it behaves simillarly like static casting
var anotherShape = shape as Circle

//This can be used instead for safe casting
var safeShape = shape as? Circle
```

8. **[Coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html)**  
Asynchronous call has always been a hassle in Java. Making Thread takes so much of the code space and makes the code unreadable. Coroutines has been made to replace traditional thread operation, granting a clean and robust code:

```kotlin
import kotlinx.coroutines.*

fun main() {
    // launch a new coroutine in background and continue
    GlobalScope.launch { 
        // non-blocking delay for 1 second (default time unit is ms)
        delay(1000L) 
        
        // print after delay
        println("World!") 
    }
    // main thread continues while coroutine is delayed
    println("Hello,") 
    
    // block main thread for 2 seconds to keep JVM alive
    Thread.sleep(2000L) 
}
```

Coroutines also supports more complex operations such as Job Joining, Channel,                     Shared Context and Parents. Details and more usages can be read [here](https://kotlinlang.org/docs/reference/coroutines/coroutines-guide.html).

## Wrapping it up

To sum it up, it's very easy to **start using Kotlin, you can code Kotlin very similar to how you code Java.**  And also, **Kotlin has provided several features that can give you edges over using Java.**

Sure, Java is still going strong at the moment. But it's never wrong to start learning something new. We, as programmers, need to embrace lifetime learning and never stop learning. The best thing about Kotlin is how easy it is to migrate from Java.

Thanks for reading. I hope you do enjoy and hopefully it would be of a good use! Good luck in exploring Kotlin, and see you next time.  



