---
title: What is Abstraction in Programming? Explained for Beginners
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2022-12-21T18:08:21.000Z'
originalURL: https://freecodecamp.org/news/what-is-abstraction-in-programming-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/smartphone-g7993a9917_1280-1.jpg
tags:
- name: abstraction
  slug: abstraction
- name: Kotlin
  slug: kotlin
seo_title: null
seo_desc: 'This article will not be a dry and boring explanation of abstract classes,
  interfaces, protocols, or similar software entities.

  I will explain what they are in simple terms, but my main goal is to change how
  you think about abstractions in general. A...'
---

This article will not be a dry and boring explanation of abstract classes, interfaces, protocols, or similar software entities.

I will explain what they are in simple terms, but my main goal is to change how you think about abstractions in general. All of this is in service of helping you develop the art of programming.

These are the topics I will cover:

* [What is an abstraction?](#heading-what-is-an-abstraction)
    
* [How to use abstractions in your programs](#heading-how-to-use-abstractions-in-your-programs)  
    – [How to use interfaces and protocols](#heading-how-to-use-interfaces-and-protocols)  
    – [How to use function types and lambda expressions](#heading-how-to-use-function-types-and-lambda-expressions)
    
* [Is abstraction the most important idea in programming?](#heading-is-abstraction-the-most-important-idea-in-programming)
    
* [How much abstraction do I need?](#heading-how-much-abstraction-do-i-need)
    

The code samples will be in Kotlin, but I have written the article assuming you only have basic programming knowledge in any industry standard language.

I also use a variety of approaches to cover both object-oriented and functional styles of code.

## What Is An Abstraction?

To begin with, we will discuss what this term means in the most general sense. Here is a simplified definition I have come up with for an abstraction:

> “A **less detailed representation** of an object or concept in nature.”

I know my definition sounds very vague, but we will discuss some clear examples shortly. First, we must understand what **detail** is.

### What Is Detail?

Detail refers to the quantity, or density perhaps, of information. Here are two examples of data models which are more and less detailed:

```pgsql
User {
  name,
  id
}
```

```pgsql
User {
  name: String,
  id: Integer,
  phone: Integer,
  email: String
}
```

There is no need to overthink this point! More details is another way of saying more information or more complexity.

The only other key point is to understand what a **representation** is.

### How to Represent Something

Suppose you are going to travel somewhere which has a particularly deadly kind of venomous snake. In order to gain information about this snake, you have a few different options:

* Read a verbal description of the snake and its behaviour
    
* Look at a drawing or picture of the snake
    
* Listen to audio of what it sounds like when behaving aggressively
    

All of the above points are examples of different kinds of representations, or abstractions, of the venomous snake.

In each case, some pieces of information, which accurately represent properties of the real snake, are conveyed. However, neither a verbal description, nor an image, nor a recording can bite you!

Here we see the main utility of abstractions: **Conveying important information** (also known as details or properties) of an object or concept, **while leaving out the unnecessary information**.

## How to Use Abstractions In Your Programs

Before we discuss some specifics, it is worth mentioning that everything in a computer program is technically an abstraction.

In fact, **programming languages, as well as all forms of mathematics, are systems of abstractions**.

However, programmers tend to think of abstractions as a narrow band of software entities usually referred to as:

* Interfaces or Protocols
    
* Abstract Classes
    
* Function Types/References/Signatures
    
* Super/Parent-Classes
    

Unfortunately, the names and mechanics of the above software entities can vary substantially in different programming languages.

For this reason, I will take two examples which may be more or less appropriate to your preferred languages:

1. An interface or protocol (which will also cover abstract classes)
    
2. A function type or method reference
    

In any case, don't worry so much about the names or any minor differences in how these things work across languages. Instead, I invite you to focus on the general ideas.

## How to Use Interfaces and Protocols

I will use the term interface from here on, but this term is synonymous with protocol. I will also use the term function synonymously with method.

Interfaces allow you to define behaviour of functions, classes, or objects, without defining their implementation.

Don't worry, I am not like some teachers who throw out some jargon and pretend like I am teaching you something.

Let's look at exactly what I mean by behaviour and implementation.

**Behaviour** literally means a function declaration:

```kotlin
interface UserDataSource {
//this line below has a function declaration but no function "body"
  fun getUserById(id: String): User?
}

data class User(
  val id: String,
  val someData: Any
)
```

You can see the footnotes below regarding my usage of the term “function declaration.”

To translate this into English, this function declaration says the we are defining a function which:

* Is named “getUserById”
    
* Accepts a String type called “id” as an argument when called
    
* Returns a “User” or a null value if no user exists (this is because we have a “?” after the “User” type)
    

**Implementation** refers to the function body:

```kotlin
//Note that ":" is short for extends/implements in Kotlin for the class
//declaration
class UserDatabase(): UserDataSource {
//the curly braces, and everything between them, is the implementation
  override fun getUserById(id: String): User? {
    var user: User? = null
    //… not important for this example
    return user
  }
}
```

Another name for the function inside of the interface is an *abstract function*. Hopefully, our discussion on abstract meaning “*less detail*” is starting to make more sense here!

**Some notes for accuracy:**

1. Some languages have features to define properties, variables, and even implementations (that is, function declarations + function bodies) within interfaces. This does not change the primary purpose of interfaces, though.
    
2. The term function declaration will be defined differently depending on the language. Instead of worrying about verbal definitions, please consider my code examples to follow what I mean.
    

### What About Abstract Classes?

Apart from in Python (and perhaps other languages I am not aware of), abstract classes are very similar to interfaces except for one key difference: a **class may only inherit from a single abstract class.**

In my opinion, before languages started to include ways for interfaces to define their own implementations, the use of abstract classes versus interfaces was clear:

* If you only want to share behaviour across a set of software entities, use an interface
    
* If you want to share implementation **and** behaviour, use an abstract class instead
    

Unfortunately, this distinction is very blurry since many languages now have features to add implementation to interfaces (like Java’s Default Methods).

The only general recommendation I can make which does not account for the specific details of any particular programming language is this: Use the simplest construct to get the job done.

## How to Use Function Types and Lambda Expressions

There are different ways to achieve abstraction without defining interfaces or classes. But the amount of structure these language features require is still subject to language specifics.

Kotlin provides enough of these features that you will hopefully be able to make some connections with your preferred languages.

### How to Use Function Types Instead Of An Interface

We will start with a practical example and then explain the finer details part by part.

Suppose we want to set up an abstract function (recall that this means a function with no implementation) to handle a click event.

Using something like an interface, we could do the following:

```kotlin
//assume this is an platform/OS component that tells you when
//a user clicks something on screen
class PlatformComponent(
  var clickListener: ClickListener? = null
) {
  fun userClickedScreen() {
    //Note: the "?" means handleClick() is only
    //called when clickListener is NOT NULL
    clickListener?.handleClick()
  }
}
//This interfaces hides (abstracts) the concrete class/type
//which handles the click
interface ClickListener {
  fun handleClick()
}
//This concrete class/type handles the click
//by extending the interface
class ScreenController() : ClickListener {
  override fun handleClick() {
    println("Click handled.")
  }
}

fun main() {
  PlatformComponent(
    ScreenController()
  ).userClickedScreen()
}
```

An alternative approach is to use a function type instead of an interface:

```kotlin
fun main() {
  val controller = ScreenController()
  val component = PlatformComponent(
    //The double colon tells the compiler that we are referring to
    //the function handleClick defined in ScreenController
    controller::handleClick
  )
  component.userClickedScreen()
}

//assume this is an platform/OS component that tells
//you when a user clicks something on screen
class PlatformComponent(
  var clickListener: () -> Unit
) {
  fun userClickedScreen() {
    //This is equivalent to calling ScreenController.handleClick(),
    //but PlatformComponent does not know that. Abstraction!
    clickListener()
  }
}
//This concrete class/type handles the click
class ScreenController() {
  fun handleClick() {
    println("Click handled.")
  }
}
```

In this example, we can see how there is even less structure required to achieve the same result. But keep in mind that having less structure does not immediately imply better code. Really, **it depends**.

In any case, with a practical example in mind, we can break down how this code actually works in more detail.

### How to Use Function References

If you are unfamiliar with how function types, method references (or whatever else they are called) work, this section explains them in Kotlin. Feel free to jump to the next section if you are already familiar.

Similar to most modern programming languages, we can create a reference variable to a particular function in Kotlin:

```kotlin
var clickListener: () -> Unit
```

In Kotlin, function types have the following syntax:

```kotlin
(optional list of parameter types) -> return type
```

For example:

* `(Int, Int) -> Int` means that the associated function must take in two Int parameters, and return a single Int
    
* `() -> Unit` means that a function has no parameters and executes without returning a meaningful value
    

Unit is roughly equivalent to Java’s void return type or Python’s None type – at least in principle.

When it comes time to call (invoke) a function reference, we have two options:

* `clickListener()` for short
    
* `clickListener.invoke()` is the full syntax, which is necessary when making null-safe calls like `clickListener?.invoke()`, for example
    

### How to Use Lambda Expressions

In the previous example, it is worth noting that ScreenController does not care what the actual function it is invoking happens to be named.

We can take this level of abstraction even further, by not even defining a ScreenController:

```kotlin
fun main() {
  //note that the outer parenthesis are optional in Kotlin,
  //but may make this easier to understand
  val component = PlatformComponent(
    { println("Click handled.") }
  )
  component.userClickedScreen()
}
//assume this is an platform/OS component that tells
//you when a user clicks something on screen
class PlatformComponent(
  var clickListener: () -> Unit
) {
  fun userClickedScreen() {
    clickListener()
  }
}
```

Unlike the previous examples, this one is **not intended to resemble a practical scenario** – just to demonstrate a lambda expression.

The actual lambda expression is this:

`{ println(“Click handled.”) }`

As you can see, it does not get much more abstract than a lambda expression.

On the surface, it's almost like defining only the implementation but not the behaviour. But at least in Kotlin, the lambda expression must conform to the type we are assigning it to.

In this case, `{ println(“Click handled.”) }` has no parameters and does not return a meaningful value. So it conforms to `() -> Unit`.

### Which Approach Should I Use?

You may wonder which approach you should be using – assuming your language allows for multiple approaches.

The most accurate answer I can give you is that there is no general rule.

Plenty of teachers these days will say “*x* is worse than y” or simply “*x* is bad,” because it works great for clickbait and search engine optimization.

But a language, platform, code construct, architecture, and just about anything else can only be judged good, bad, better, or worse relative to your requirements.

In fact, different requirements are the reason we have languages as different as Python and Java which are both extremely popular.

So instead, try different approaches and be skeptical of anyone who makes absolute statements without discussing requirements.

## Is Abstraction the Most Important Idea in Programming?

The point of this article was never to say: *“Using interfaces and abstract classes everywhere will make you a better programmer.”*

In fairness, as many developers do, I went through a phase around 2016–2018 where I did actually think that statement was pretty accurate.

Instead, the point of this article is to explain two things:

* Abstraction in programming, in my opinion, **should** **not specifically mean abstract classes, or any particular code construct**
    
* Abstraction in programming is a **process** by which we design our software entities according to **how much detail** they internally (privately) contain and externally (publicly) provide
    

In a sense, every decision we make about the structure of our code, regardless of the language, comes down to this process of abstraction.

With that being said, how do we know when making some aspect of our program more abstract is beneficial, useless, or detrimental?

## How Much Abstraction Do I Need?

I can only think of one kind of situation where you should strongly consider using something like an interface or function type.

Recall that these software entities provide variability of implementation but consistent behaviour. Further, that implementation typically refers to the body of a function.

Two things follow from that observation:

* If no variability of implementation is required, there is not likely to be a benefit of using a more abstract software entity.
    
* If variability of implementation is required, using a more abstract software entity is likely beneficial.
    

We will now discuss two situations I have encountered where variability is a requirement.

### How to Make Your Code Easier to Test

Suppose that we have some kind of software entity, which must request some user data from a database or network adapter:

```kotlin
class PresentationLogic(
 val datasource: Datasource
) {
    fun start() {
        val someData = datasource.getData()
        presentData(someData)
    }
    
    //...
}

class Datasource() {
    fun getData(): Data {
        var someData = getLocalOrRemoteData()
        //... error handling and so on
        
        return someData
    }
}
```

Also suppose that we want to test `PresentationLogic` without needing a real datasource to supply the data.

There are a few different ways to solve this problem (see the note below), but a simple solution is to make the datasource more abstract:

```kotlin
class PresentationLogic(
 val datasource: DatasourceInterface
) {
    fun start() {
        val someData = datasource.getData()
        presentData(someData)
    }
    
    //...
}

interface DatasourceInterface {
    fun getData(): Data
}
```

From there, we can create a fake implementation of the datasource in a test environment:

```kotlin
class FakeDatasource(): DatasourceInterface {
        override fun getData(): Data {
            return Data()
        }
}

@Test
fun testLogic() {
    val logic = PresentationLogic(
       //here we provide the fake version
       FakeDatasource()
    )
}
```

Using abstraction, PresentationLogic does not know or care whether it is talking to a fake or real datasource. By extension, it does not need to change to work with either of them. Variability of implementation!

Note that there are other way to achieve this variability apart from using an interface. You could use a mocking library, or configure a build tool to swap out implementations.

There is no clear answer to which approach is better outside of discussing specific requirements.

Also, note that this approach would not actually work unless the details of how the datasource is created are kept separate from `PresentationLogic`.

This is commonly referred to as Dependency Injection, which I will discuss in a separate article.

### How to Work With Different Versions and Vendors of a Service

Suppose that for some reason, you must work with different versions or vendors of the same service depending on different requirements.

An example could be supporting both AWS and Firebase to store the same data. Another example could be supporting a legacy version of a service along with a newer version of that same service.

In any case, it is another situation where variability of implementation is expected.

The code examples we will discuss have the following requirements:

* A client program must use three services, all from different vendors, to perform the same behaviour
    
* The decision to choose a particular service is determined at runtime based on the environment (platform, OS, hardware, and so on) of the client program
    

For those wondering, “client” in this context is a generic word for some program or software entity which uses other programs or software entities.

For example, YouTube’s website and mobile apps are “client apps” of YouTube’s backend servers.

Without applying any abstraction, our client program will need to know about every possible service and be told which service to choose:

```kotlin
fun clientProgram(
    request: Request, 
    awsService: AwsService,
    firebaseService: FirebaseService,
    parseService: ParseService
): Result {
    val use: USE_SERVICE = determineBestService()
    
    val result = when (use) {
        USE_SERVICE.AWS -> awsService.executeRequest(request)
        USE_SERVICE.FIREBASE -> firebaseService.executeRequest(request)
        USE_SERVICE.PARSE -> parseService.executeRequest(request)
    }
    
    //assume additional work is done before returning the result
    return result
}

enum class USE_SERVICE {
    AWS,
    FIREBASE,
    PARSE
}
```

Notice that clientProgram has a parameter which refers to specific vendors of the service:

* Amazon Web Services (AWS)
    
* Firebase
    
* The now defunct Parse service from Facebook
    

It follows that any changes to our services will require `clientProgram` to be refactored (rewritten) appropriately.

The reason I chose Parse as one of the example services is specifically because it was shut down, despite being widely used. There are various reasons why a particular service may no longer fit requirements, but not working any more is a good one.

An alternative approach would be to hide all the details about the service being used from clientProgram. You could use an interface, but for variety’s sake I have used a function type instead:

```kotlin
fun main() {
    //Creating the services
    val awsService = AwsService()
    val firebaseService = FirebaseService()
    
    //determining which service to use must 
    //not be included in clientProgram
    val use: USE_SERVICE = determineBestService()

    //Assign serviceToUse to the appropriate function
    val serviceToUse: (Request) -> Result = when (use) {
        USE_SERVICE.AWS -> awsService::executeRequest
        USE_SERVICE.FIREBASE -> firebaseService::executeRequest
    }
    
    val request = getRequest()
    
    clientProgram(
       request,
       serviceToUse
    )
}


fun clientProgram(
    request: Request, 
    service: (Request) -> Result
): Result {
    
    val result = service.invoke(request)
    
    //assume additional work is done before returning the result
    
    return result
}

enum class USE_SERVICE {
    AWS,
    FIREBASE
}

class AwsService() {
    fun executeRequest(request: Request): Result = Result()
}
class FirebaseService() {
    fun executeRequest(request: Request): Result = Result()
}
```

The end result of this abstraction is that we can change services without needing to change `clientProgram` – assuming our behaviour does not change.

I want to point out that I am not advocating that you hide every service behind some kind of abstraction. If no variability is required or expected, there may not be any benefit to extra abstraction.

# Closing Thoughts

I hope it is clear when reading this article that my intention is not to push dogmatic opinions about how abstract your code should be.

As a junior and intermediate developer, it took me a few years to realize that it really does depend on project requirements.

I also hope that this article gave you some new ideas and perspectives about what abstraction is and how it can be applied in your code. Good luck and happy coding!

### **Before you go...**

If you liked this article and want more information on these principles and code constructs, check out my free, full length [programming fundamentals course](https://youtu.be/FL2SMZxNQlc). It includes professionally written English, Burmese, and Arabic subtitles.
