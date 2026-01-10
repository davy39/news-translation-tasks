---
title: A stress-free way to test frustrating static method calls in Kotlin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-06T18:48:29.000Z'
originalURL: https://freecodecamp.org/news/a-stress-free-way-to-test-frustrating-static-method-calls-in-kotlin-81db43e7ed82
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fylN7XB0FWB7vVVF8yfoqQ.png
tags:
- name: development
  slug: development
- name: Kotlin
  slug: kotlin
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: null
seo_desc: 'By Oleksii Fedorov

  Let me make a wild guess… You have encountered some code in Kotlin that is using
  some third-party library. The API that the library provides is one or a few static
  methods. And you want to test some code using these static methods....'
---

By Oleksii Fedorov

Let me make a wild guess… You have encountered some code in Kotlin that is using some third-party library. The API that the library provides is one or a few static methods. And you want to test some code using these static methods. It is painful.

You are not sure how to approach that problem.

Perhaps you ask yourself, “When will third-party library authors stop using static methods?”

Anyway, who am I to tell you how to test static method calls in Kotlin?

I’m a fanatic of testing and test-driven development evangelist for the last five years — they call me [TDD Fellow](http://tddfellow.com/) for a reason. I have been working with Kotlin in production for about two years at the time of writing this.

Onward!

That is how I feel when I see such awful APIs:

![Image](https://cdn-media-1.freecodecamp.org/images/VqR1mKMGNy9Q80UjC7KRGAB3I4WVgDA428t6)
_(source: pexels.com)_

Let me show you what I mean with a rough example that I have been dealing with recently. The library was a `newrelic` client. To use it I had to call a static method on some class. If simplified, it looks something like this:

```kotlin
NewRelicClient.addAttributesToCurrentRequest(“orderId”, order.id)
```

I needed to change what exactly we are sending, and I had to add more attributes. Since I wanted to have confidence that my change is not breaking anything and does exactly the thing I want, I needed to write a test. There was no test for this code yet.

If you are still reading, I’m assuming you are in the same situation. Or you have been in the past.

I agree that is a painful situation.

How am I supposed to mock these calls in the test?

I know, it is frustrating that most of the mocking libraries are unable to mock static method calls. And even the ones that work in Java don’t always work in Kotlin.

There are libraries that could do that, such as `powermock,` for instance. But you know what? Perhaps, you are already using `mockito` or some other library. Adding another mocking tool to the project will make things more confusing and frustrating.

I know how annoying it is to have multiple tools for the same job in the same codebase. That causes a hell lot of confusion for everyone.

Well, that problem was already solved about two decades ago!

Interested? Come for a ride.

### Refactoring towards the Humble Object

Let’s take a look at the code that we are working with here:

```kotlin
class FulfilOrderService {

    fun fulfil(order: Order) {
    
        // .. do various things ..
        
        NewRelicClient.addAttributesToCurrentRequest(
                "orderId", order.id)
        NewRelicClient.addAttributesToCurrentRequest(
                "orderAmount", order.amount.toString())
                
    }
    
}
```

It is doing various things with the order to fulfill it, and then it is assigning a few attributes to the current request for `newrelic`.

The first thing that we will do together here is extract the method `addAttributesToRequest`. We also want to parametrize it with `key` and `value` arguments. You can do so manually, or, if you are lucky enough to use IntelliJ IDEA, you can do such refactoring automatically.

Here is how:

1. Select `”orderId”` and extract a local variable. Name it `key`.
2. Select `order.id` and extract a local variable. Name it `value`.
3. Select `NewRelicClient.addAttributesToCurrentRequest(key, value)` and extract a method. Name it `addAttributesToRequest`.
4. IntelliJ will highlight that second call to `NewRelicClient` as a duplicate and tell you that you can replace it with the call to the new private method. IntelliJ will ask you if you want to do that. Do it.
5. Inline variables `key` and `value`.
6. Finally, make the method `protected` instead of `private`. I’ll show you in a bit why the method has to be protected.
7. You’ll notice that IntelliJ highlights `protected` with a warning. That is because all classes in Kotlin are `final` by default. As final classes are not extendable, `protected` is useless. One of the solutions IntelliJ offers is to make the class `open`. Do it. The method `addAttributesToRequest` should become open too.

Here is what you should get in the end:

```kotlin
open class FulfilOrderService {

    fun fulfil(order: Order) {
    
        // .. do various things ..
        
        addAttributesToRequest("orderId", order.id)
        addAttributesToRequest("orderAmount",
                               order.amount.toString())
                               
    }
    
    protected open fun addAttributesToRequest(key: String,
                                              value: String) {
                                              
        NewRelicClient.addAttributesToCurrentRequest(key, value)
        
    }
    
}
```

Notice, how all these refactorings were completely automatic and therefore safe to execute. We do not need tests to do these. Having that method as protected will give us the opportunity to write a test:

```kotlin
private val attributesAdded = mutableListOf<Pair<String, String>>()

private val subject = FulfilOrderService()

@Test
fun `adds order id to the current request within newrelic`() {

    val order = Order(id = "some-id", amount = 142)
    
    subject.fulfil(order)
    
    val expectedAttributes = listOf(
            Pair("orderId", "some-id"),
            Pair("orderAmount", "142"))
    assertEquals(expectedAttributes, attributesAdded)
    
}
```

Speaking of tests and refactoring…

Do you want to learn how to write an acceptance test in Kotlin? Maybe, how to use the power of IntelliJ IDEA to your advantage?

Perhaps, you want to learn how to build applications in Kotlin well? — be it command-line, web or android apps?

There is this ultimate tutorial e-book that I have ACCIDENTALLY written about getting started with Kotlin. 350 pages of hands-on tutorial that you can follow along.

You will feel as if I’m sitting together with you and we are enjoying our time, all the while building a full-fledged command-line application.

Interested?

Download the [ultimate tutorial here](https://iwillteachyoukotlin.com/). By the way, it is free and will always be!

Going back to our test.

That all looks correct, but it doesn’t work because nobody is adding any elements to the list `attributesAdded`. Since we have that small protected method, we can “hack into it”:

```kotlin
private val subject: FulfilOrderService = object :
                                          FulfilOrderService() {
                                          
    override fun addAttributesToRequest(key: String,
                                        value: String) {
                                        
        attributesAdded.add(Pair(key, value))
        
    }
    
}
```

If you run the test, it passes. You can change values in the test or production code to see the failure and make sure that it indeed is testing what you think it does.

Let’s see the whole test code:

```kotlin
import org.junit.Assert.*
import org.junit.Test

@Suppress("FunctionName")
class FulfilOrderServiceTest {

    private val attributesAdded = 
            mutableListOf<Pair<String, String>>()
            
    private val subject: FulfilOrderService = object :
                                      FulfilOrderService() {
                                      
        override fun addAttributesToRequest(key: String,
                                            value: String) {
                                            
            attributesAdded.add(Pair(key, value))
            
        }
        
    }
    
    @Test
    fun `adds order id to the current request within newrelic`() {
    
        val order = Order(id = "some-id", amount = 142)
        
        subject.fulfil(order)
        
        val expectedAttributes = listOf(
                Pair("orderId", "some-id"),
                Pair("orderAmount", "142"))
        assertEquals(expectedAttributes, attributesAdded)
        
    }
    
}
```

So, what just happened here?

See, I’ve made a slightly different version of `FulfilOrderService` class — a testable one. The only weakness of this testing method is that if somebody screws up with `addAttributesToRequest` function, no test will break.

On the other hand, that function will never have to contain more than one line of simple code and will probably not change that often. That will happen only in the case when authors of the third-party library that we are using are going to introduce a breaking change to that single method.

That is unlikely. Will happen probably every few years.

And you know what?

Even if you do test it somehow more “black-box’ey” than what I’m offering here, when such breaking change comes around the block, you’ll still have to re-visit all the usages and fix them. Probably, you will need to throw away or rewrite all the related tests too.

Oh, and in case of such breaking change, I would still recommend testing manually at least once to see if you understood the new API correctly and it interacts with the third-party system in a way you think it should.

Given all this information, I guess it should be alright to leave that one line untested.

But if such change comes around the block, do you have to hunt for all the places where we are calling to `NewRelicClient`?

Short answer — yes.

Long answer: in current design — yes. But did you think we are done here?

Nope.

The design is terrible as it is right now. Let’s fix that via extraction of the Humble Object. Once we do that, there will be only one place in a whole code base that will require change — that humble object.

Unfortunately, IntelliJ doesn’t support `Move method` or `Extract method object` refactorings for Kotlin quite yet, so we will have to perform this one manually.

But you know what? — It is OK because we already have related tests backing us up!

To do the `Extract method object` refactoring, we will need to replace the implementation inside of the method with object creation, and immediate call to the method of that object with the same arguments as the refactored method has:

```kotlin
protected open fun addAttributesToRequest(key: String,
                                          value: String) {
                                          
//   NewRelicClient.addAttributesToCurrentRequest(key, value)
    NewRelicHumbleObject().addAttributesToRequest(key, value)
    
}
```

Then we will need to create this class and create the method on it. Finally, we will put the contents of the refactored method, the one we have commented out, to the freshly created method; don’t forget to remove the comment as we don’t need it anymore:

```kotlin
class NewRelicHumbleObject {
    
    fun addAttributesToRequest(key: String, value: String) {
        
        NewRelicClient.addAttributesToCurrentRequest(key, value)
        
    }
    
}
```

We are done with this step of refactoring, and we should run our tests now. They all should pass if we didn’t make any mistakes — and they do!

The next step in this refactoring is to move creation of the humble object into the field. Here we can perform an automated refactoring to extract the field from the expression `NewRelicHumbleObject()`. That is what you should get after the refactoring:

```kotlin
private val newRelicHumbleObject = NewRelicHumbleObject()

protected open fun addAttributesToRequest(key: String,
                                          value: String) {
                                          
    newRelicHumbleObject.addAttributesToRequest(key, value)
    
}
```

Now, because we have that value in the field, we can move it to the constructor. There is an automated refactoring for that too! It is called `Move to constructor`. You should get the following result:

```kotlin
open class FulfilOrderService(
        private val newRelicHumbleObject: NewRelicHumbleObject =
                                          NewRelicHumbleObject()) {
                                          
    fun fulfil(order: Order) {
    
        // .. do various things ..
        
        addAttributesToRequest("orderId", order.id)
        addAttributesToRequest("orderAmount",
                               order.amount.toString())
                               
    }
    
    protected open fun addAttributesToRequest(key: String,
                                              value: String) {
                                              
        newRelicHumbleObject.addAttributesToRequest(key, value)
        
    }
    
}
```

That will make it super simple to inject the dependency from the test. And notice, it is an ordinary object with one non-static method.

Do you know what that means?

Yes! You can use your favorite mocking tool to mock that. Let’s do just that now. I’ll use `mockito` for this example.

First, we will need to create the mock in our test:

```kotlin
private val newRelicHumbleObject =
        Mockito.mock(NewRelicHumbleObject::class.java)
```

To be able to mock our humble object, we will have to make its class `open` and the method `addAttributesToRequest` open too:

```kotlin
open class NewRelicHumbleObject {

    open fun addAttributesToRequest(key: String, value: String) {
        // ...
        
    }
    
}
```

Then we will need to provide that mock as an argument to `FulfilOrderService`’s constructor:

```kotlin
private val subject = FulfilOrderService(newRelicHumbleObject)
```

Finally, we want to replace our assertion with `mockito`’s verification:

```kotlin
Mockito.verify(newRelicHumbleObject)
        .addAttributesToRequest("orderId", "some-id")
Mockito.verify(newRelicHumbleObject)
        .addAttributesToRequest("orderAmount", "142")
Mockito.verifyNoMoreInteractions(newRelicHumbleObject)
```

Here we are verifying that our humble object’s method `addAttributesToRequest` has been called with appropriate arguments twice and with nothing else. And we don’t need `attributesAdded` field anymore, so let’s get rid of that.

Here is what you should get now:

```kotlin
class FulfilOrderServiceTest {

    private val newRelicHumbleObject =
            Mockito.mock(NewRelicHumbleObject::class.java)
            
    private val subject = FulfilOrderService(newRelicHumbleObject)
    
    @Test
    fun `adds order id to the current request within newrelic`() {
    
        val order = Order(id = "some-id", amount = 142)
        
        subject.fulfil(order)
        
        Mockito.verify(newRelicHumbleObject)
                .addAttributesToRequest("orderId", "some-id")
        Mockito.verify(newRelicHumbleObject)
                .addAttributesToRequest("orderAmount", "142")
        Mockito.verifyNoMoreInteractions(newRelicHumbleObject)
        
    }
    
}
```

Now that we are not overriding that protected method anymore, we can inline it. By the way, the class doesn’t have to be `open` anymore. Our `FulfilOrderService` class is now ready to accept the changes that we wanted to make, as it is testable now (at least in regard to `newrelic` request attributes):

```kotlin
class FulfilOrderService(
        private val newRelicHumbleObject: NewRelicHumbleObject = 
                                          NewRelicHumbleObject()) {
                                          
    fun fulfil(order: Order) {
    
        // .. do various things ..
        
        newRelicHumbleObject.addAttributesToRequest(
                "orderId", order.id)
        newRelicHumbleObject.addAttributesToRequest(
                "orderAmount", order.amount.toString())
                
    }
    
}
```

Let’s run all the tests again, just for good measure! — they all pass.

Great, I think we are done here.

### Share what you think about Humble Object!

Thank you for reading!

It would make me happy if you shared what you think of such refactoring in the comments. Do you know a simpler way to refactor that? — share!

Also, if you like what you see, consider giving me a clap on Medium and sharing the article on social media.

If you are interested in learning Kotlin and you like my writing style, [grab my ultimate tutorial on getting started with Kotlin](https://iwillteachyoukotlin.com/).

### My related articles

[**How Kotlin’s “@Deprecated” Relieves Pain of Colossal Refactoring?**](https://hackernoon.com/how-kotlins-deprecated-relieves-pain-of-colossal-refactoring-8577545aaed)  
[_I’m going to tell you a real story how we saved ourselves tons of time. The power of Kotlin’s @Deprecated refactoring…_](https://hackernoon.com/how-kotlins-deprecated-relieves-pain-of-colossal-refactoring-8577545aaed)  
[hackernoon.com](https://hackernoon.com/how-kotlins-deprecated-relieves-pain-of-colossal-refactoring-8577545aaed)

[**How Kotlin Calamity Devours Your Java Apps Like Lightning?**](https://hackernoon.com/how-kotlin-calamity-devours-your-java-apps-like-cancer-f3ce9500a028)  
[_I hear what you are saying. There is that buzz around Android actively adopting Kotlin as a primary programming…_](https://hackernoon.com/how-kotlin-calamity-devours-your-java-apps-like-cancer-f3ce9500a028)  
[hackernoon.com](https://hackernoon.com/how-kotlin-calamity-devours-your-java-apps-like-cancer-f3ce9500a028)

[**Parallel Change Refactoring**](https://medium.com/@oleksii_f/parallel-change-refactoring-b83a2993ef26)  
[_Parallel Change is the refactoring technique that allows implementing backward-incompatible changes to an API in a safe…_](https://medium.com/@oleksii_f/parallel-change-refactoring-b83a2993ef26)  
[medium.com](https://medium.com/@oleksii_f/parallel-change-refactoring-b83a2993ef26)

