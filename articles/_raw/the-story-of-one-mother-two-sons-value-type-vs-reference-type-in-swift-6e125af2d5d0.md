---
title: 'The story of one mother & two sons: value type vs reference type in Swift'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-21T16:47:32.000Z'
originalURL: https://freecodecamp.org/news/the-story-of-one-mother-two-sons-value-type-vs-reference-type-in-swift-6e125af2d5d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ri49w8TcHeXrnmO5dD4_aQ.jpeg
tags:
- name: iOS
  slug: ios
- name: mobile
  slug: mobile
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Boudhayan Biswas

  Swift is a mother?and it has two sons ?-


  Value Type ??‍♀️

  Reference Type ?‍♂️


  But what are their characteristics??‍♂️

  Do they behave the same or opposite to each other? ?‍♂️

  Swift is a multi-paradigm programming language develop...'
---

By Boudhayan Biswas

Swift is a mother?and it has two sons ?-

* Value Type ??‍♀️
* Reference Type ?‍♂️

But what are their characteristics??‍♂️

Do they behave the same or opposite to each other? ?‍♂️

Swift is a multi-paradigm programming language developed by Apple for iOS, macOS, watchOS, tvOS, Linux, and z/OS.?

Just like other object-oriented programming languages, Swift has classes as building blocks which can define methods, properties, initializers, and can conform to protocols, support inheritance & polymorphism.?

But, wait wait wait…???

Swift has structs also and it can define methods, properties, initializers and can conform to protocols with only one exception of inheritance.?

What? Now I am confused!!! ???

Now let’s spice up your confusion: structs are not only the value types in Swift. Tuples and enums are also value types. Classes are also not the only one used as a reference type. Functions and closures are also reference types. But as a token of relief, we at least know the primary focus & specialization of usage of these types.?

So up to this point, we are left with only one big confusion with the usage of structs and classes.?

So, let’s go and clear the confusions going around.?‍♂️

### Storage Locations

There are three types of storage available:

* Register ?
* Stack ☄️
* Heap ?

The objects that have a shorter lifespan are stored inside registers or the stack and those that have a longer lifespan are stored inside the heap.?

A value type stores its contents in memory allocated in the stack, so we can say value types are allocated in the stack in Swift. ?

But there is a common misconception about value types, have you heard it??‍♂️

The misconception is that most people think value types are always stored in the Stack.

❌❌ Wait a minute — this is not the case always. ❌❌

Value types can be stored inside the stack when they are either temporary or local variables. But what if a value type is contained inside a reference type?

In this situation, it can be stored inside the heap memory. ?

Wow…that’s cool!!!?

So the value types can be stored inside the register, stack or heap depending on their lifespan, whether they are short lived or long lived. If it is a local variable it can live inside the stack and if it is a part of class then it can live inside heap memory also.✅

On the other hand, reference type stores its contents in memory allocated in the heap memory and the variable holds only a reference to that memory location where actual data has been stored. ??

How does it work for reference type??

So for reference type, it is quite a common situation when there can be several variables holding the reference to the same memory location.⚔️

When a value type instance is assigned to a variable or passed to a function, the instance is copied and assigned to that variable. But with the reference type, only the reference gets copied and the new variable holds the same reference to the same memory location. ?

### Differences in terms of Mutability

There can be two states for a variable:

* ?‍♀ ️Mutable ?‍♀
* ?️‍♂️ Immutable ?️‍♂️

If a value type instance is assigned to an immutable variable, then the instance also becomes immutable. As a result, we can not make any changes to that instance.?‍♂️

If a value type instance is assigned to a mutable variable, then only it makes the instance mutable. ?‍♂️

But things are totally different for reference types. The variable and the instance it is assigned to are totally different. If we declare an immutable variable holding a reference to a class, this means that the reference it is holding will never change. We can not the change the reference and it will always point to the same reference. ?

### Structural Types

Values of structural types are compared for equality in terms of their attributes or elements. We can say a value type is equal to another if and only if all of the corresponding attributes are equal. ???

Umm…too many strong words…what do you mean???

Let’s say, we have a **_Person_** value type which has attributes like **_firstName_** and **_lastName._**

```
struct Person {
   var firstName: String
   var lastName: String
}

var person1 = Person(firstName: "foo", lastName: "bar")

var person2 = Person(firstName: "foo", lastName: "bar")
```

Here both **_person1_** & **_person2_** instances are holding the same value for **_firstName_ (“foo”)** and **_lastName (“bar”)_**_._ So as per our understanding, we can say that the two instances are equal to each other since their attributes (**_firstName_** & **_lastName_**) are holding the same values.

But it’s not only limited to this: in the future, any two person instances holding the same values for **_firstName_** & **_lastName_** will be equal to each other.

So as per our understanding till this point, we can say that:

> _**Value Types do not have identity, so there can be no reference to them. Value types are faceless.?**_

What? How can you say that????

```
var myAge: Int = 21
var friendAge: Int = 21
```

Both **_myAge_** & **_friendAge_** are integer type variable with value 21.

**_Can we distinguish one from the other? ?_**

No, because they are holding the same value.?

An integer variable with value 21 cannot be different from another integer variable which is also having the value 21. As simple as that.???

Not having an identity gives value types another advantage: if you think practically, then you can imagine if you do not have an identity then anyone with same characteristics can replace or substitute you. ???

The same we can think for us as humans also. If I don’t have an identity then anyone with same characteristics can replace me???. It’s good for us that we have an identity otherwise it would be a great risk to our existence.?

But for value types, they don’t have an identity and it is an advantage to them. ?

### What are the benefits of using Value Types?

#### ? No Race Conditions and Deadlocks: ?

For values types in a multi-threaded environment, it is impossible for one thread to mutate the state of the instance while it is being used by another thread. So we can say that there will be no race conditions or deadlocks.

#### ⚔️ **No Retain Cycles: ⚔️**

When there are two reference type instances that are holding strong references to each other and preventing each other from being deallocated from memory, it is called a retain cycle. Since value types don’t work as a reference, so we can say there will be no retain cycles for value types.

#### ?‍?‍?‍? Automatic Reference Counting: ?‍?‍?‍?

For reference type, Swift uses automatic reference counting to keep track of all the live or active objects and deallocates the instance only when there are no more strong references to it. If we think a little bit, then we can say that it is kind of a heavy operation because Swift runtime needs to keep track of the objects always. But since value types are allocated in the stack, it does not need ARC. So it is cheaper and faster??.

But wait...How does it manage memory for Array, Dictionary and String??

Since we can not know what will be the actual size of an array, a dictionary, and a string at compile time, there is no scope for them to be allocated at compile time. Though they are value types internally, they can not be allocated in stack. They need to be allocated in heap memory, and to manage this, Swift comes up with **_copy on write_**.?

But what is this??

When we say one instance is a copy of another instance, this really means they are the same, that they contain the same values. But in Swift, for these above types (Array, Dictionary, String, etc), an actual copy has been made on heap only when an instance is mutated. This is called a performance optimization technique for value types.???

### Conclusion

There is no hard rule which defines when to use value type and when to use reference type. Value types have some unique advantages over reference types and vice versa. They both are unique in their own way. It really depends on your requirements and what you are trying to achieve. You should know the semantics of your code because you only know your code best, so it’s up to you to choose. You have the full freedom.

So rather than fighting over value type vs reference type, use them intelligently.

**_??? Cheers!!! Thank you for reading!!_** _???_

**_✅✅✅You can find me on_** [**_Twitter_**](https://twitter.com/_boudhayan_)**_.✅✅✅_**

