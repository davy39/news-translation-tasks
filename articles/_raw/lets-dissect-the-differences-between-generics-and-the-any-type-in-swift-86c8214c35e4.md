---
title: Let’s dissect the differences between Generics and the Any type in Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T23:30:10.000Z'
originalURL: https://freecodecamp.org/news/lets-dissect-the-differences-between-generics-and-the-any-type-in-swift-86c8214c35e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HHsbUAAWhF6WcopEr39yuw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Boudhayan Biswas

  Swift is one of the topmost type-safe languages nowadays. ???

  Ohhh wait!! What does it mean if a language is type-safe? ?

  A type-safe language always ensures that an operation works with the right kind
  of data available at that po...'
---

By Boudhayan Biswas

Swift is one of the topmost type-safe languages nowadays. ???

#### **_Ohhh wait!! What does it mean if a language is type-safe? ?_**

A type-safe language always ensures that an operation works with the right kind of data available at that point.✓

If a language has the ability to declare different data types (e.g., Int, Float, String, Array, Dictionary) and it has also the ability to ensure that a variable that is declared with a particular data type will never hold a different kind of data, then it is called a type-safe language.

In type-safe languages, type checking is always done. It may happen in compile time or run time depending on the language.✅

#### **_Now, what are Generics in Swift??_**

Generics are type safe, and help us write flexible, reusable functions and types. Using Generics, we can write code that works for all data types. Since Swift is a type-safe language, without breaking this we are able to write generic codes that can avoid code duplication.

Let’s take a simple example: an Array is an ordered collection which can hold the same type of data. That’s why in the definition of an Array, we can see that it takes a generic type of **Element_._** Hence an Array becomes a **generic type of Collection**.

**_Ok. Cool. Then what is the Any type in Swift?_**???

Swift also supports the Any type. As the name indicates, it can represent an instance of any type like a struct, class, enum and function type.

#### **_So are the Objective C id and Swift’s Any the same?_**?

In Swift 3, the Objective C _id_ type maps to Swift’s Any type. This improves the compatibility of Swift and Objective C.

#### **_But how and why??_**

In Swift 2, the Objective C _id_ was mapped to Swift’s Any object. This worked well for most of the cases, but sometimes it resulted in unexpected behavior. One of the key concepts in Swift is Value Types, and this mapping was not doing the proper justice to this concept.

Swift is just a new language for iOS development, and Objective C has been around for years. So of course most of the projects were developed in Objective C only. Now in order to convert an Objective project to a Swift project, the requirement came that it should be possible to bridge any Swift type to any Objective C object.

But this was not a problem for Swift classes and Swift value types like Int, String, Float because they already have their Objective C counterparts. The problem arose for the Swift value types that did not have any Objective C counterparts.

So to fix this, the Objective C id type mapped onto the Swift Any type.✅✅✅

**Enough Definitions ?. Now let’s come to the main topic. By the above points, it looks like Generics and the Any type are the same. But are they really???**

**On a high level, Any may look similar to Generics. But let’s try to find some differences-???**

**We all know what a **Stack** is in Data Structures, right? A stack is a basic linear data structure where insertion and deletion of items takes place at one end only.**

**Now we will implement the Stack structure in Swift. First, we will implement using Generics then with the Any type.**

#### **Stack Implementation using Generics:**

**The above Stack implementation is using Generics. The struct takes a generic type of **Element** item and implements a stack using that item. Now let’s do some operation with Generic Stack:**

**It declares a Generic Stack which can hold an Integer type of element. We are pushing the integer element to the stack. Up to this point, everything works great.**

**But what if I want to push a float element onto that above the genericStack?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ir_5WJ9UvNMUqRlGihdgoA.png)

**❌❌ Oops! Compilation Error! ❌❌**

#### **Stack Implementation using the Any type:**

**In this Stack Implementation, the items array can hold Any type of element. We are not specifying about what will be the exact data type of the _items_ array element in the definition. Now let’s do the same basic operations on this stack:**

**No issues, right? Everything is working fine here also. Initially, we declared a stack and pushed two integer elements into it. When we call the _show()_ method, it prints the exact array _[3, 4]._**

**Now let’s push a float value into it.☄️**

![Image](https://cdn-media-1.freecodecamp.org/images/1*07nwXABEbmgViY7OXJC60Q.png)

**✅✅ No Error! Everything works fine! ✅✅**

#### **_So what is happening behind the scenes? Why we are not getting any error???_**?

**Generics basically tells the compiler that:**

> **I have declared a generic type and I am going to give you an exact type later. I want you to apply that type everywhere I specify.**

**The Any type basically tells the compiler:**

> **Don’t worry about this variable, no need to apply any type here let me do whatever I want to do.**

**Generics can be used to define flexible functions, but the types of arguments are still checked by the compiler. Any type can be used to dodge Swift’s type system.?**

**In the generic stack declaration**, we are telling the compiler that the stack should take the integer type only. Then when we are trying to insert a float type of element into it, that means we are breaking that promise. Hence it is throwing a compile time error. It always expects that the element should be an integer type.

**But for the Any Stack**, we are not getting any compile time or runtime error. Even if we call the _show()_ method, it prints the stack as _[3, 4, 5.0]_ which means the stack holds integer and float type of values. So in any stack, there is no type restriction, we can push any type of value into it (but there are possibilities of runtime exceptions).

### **Conclusion**

**So if we use Generics then we can write flexible functions, structures, classes, and protocols without compromising Swift’s type safety. But if we use the Any type, then we are kind of our own boss, we can do almost anything we want.**

**_??? Cheers!!! Thank you for reading!! ???_**

