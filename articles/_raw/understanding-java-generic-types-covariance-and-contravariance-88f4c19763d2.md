---
title: 'An introduction to generic types in Java: covariance and contravariance'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-21T04:00:37.000Z'
originalURL: https://freecodecamp.org/news/understanding-java-generic-types-covariance-and-contravariance-88f4c19763d2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*h03xxe8xFKcFv262.jpg
tags:
- name: generics
  slug: generics
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Fabian Terh

  Types

  Java is a statically typed language, which means you must first declare a variable
  and its type before using it.

  For example: int myInteger = 42;

  Enter generic types.

  Generic types

  Definition: “A generic type is a generic class o...'
---

By Fabian Terh

### Types

Java is a statically typed language, which means you must first declare a variable and its type before using it.

For example: `int myInteger = 42;`

Enter generic types.

#### Generic types

[Definition](https://docs.oracle.com/javase/tutorial/java/generics/types.html): “A _generic type_ is a generic class or interface that is parameterized over types.”

Essentially, generic types allow you to write a general, generic class (or method) that works with different types, allowing for code re-use.

Rather than specifying `obj` to be of an `int` type, or a `String` type, or any other type, you define the `Box` class to accept a type parameter `<`;T>. Then, you ca`n` use T to represent that generic type in any part within your class.

Now, enter covariance and contravariance.

### Covariance and contravariance

#### Definition

Variance refers to how subtyping between more complex types relates to subtyping between their components ([source](https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science))).

An easy-to-remember (and extremely informal) definition of covariance and contravariance is:

* Covariance: accept subtypes
* Contravariance: accept supertypes

#### Arrays

In Java, **arrays are covariant**, which has 2 implications.

Firstly, an array of type `T[]` may contain elements of type `T` and its subtypes.

```
Number[] nums = new Number[5];nums[0] = new Integer(1); // Oknums[1] = new Double(2.0); // Ok
```

Secondly, an array of type `S[]` is a subtype of `T[]` if `S` is a subtype of `T`.

```
Integer[] intArr = new Integer[5];Number[] numArr = intArr; // Ok
```

However, it’s important to remember that: (1) `numArr` is a reference of reference type `Number[]` to the “actual object” `intArr` of “actual type” `Integer[]`.

Therefore, the following line will compile just fine, but will produce a runtime `ArrayStoreException` (because of heap pollution):

```
numArr[0] = 1.23; // Not ok
```

It produces a runtime exception, because Java knows at runtime that the “actual object” `intArr` is actually an array of `Integer`.

#### Generics

With generic types, Java has no way of knowing at runtime the type information of the type parameters, due to type erasure. Therefore, it cannot protect against heap pollution at runtime.

**As such, generics are invariant.**

```
ArrayList<Integer> intArrList = new ArrayList<>();ArrayList<Number> numArrList = intArrList; // Not okArrayList<Integer> anotherIntArrList = intArrList; // Ok
```

The type parameters must match exactly, to protect against heap pollution.

But enter wildcards.

#### Wildcards, covariance, and contravariance

With wildcards, it’s possible for generics to support covariance and contravariance.

Tweaking the previous example, we get this, which works!

```
ArrayList<Integer> intArrList = new ArrayList<>();ArrayList<? super Integer> numArrList = intArrList; // Ok
```

The question mark “?” refers to a wildcard which represents an unknown type. It can be lower-bounded, which restricts the unknown type to be a specific type or its supertype.

Therefore, in line 2, `? super Integer` translates to “any type that is an Integer type or its supertype”.

You could also upper-bound the wildcard, which restricts the unknown type to be a specific type or its subtype, by using `? extends Integer`.

#### Read-only and write-only

Covariance and contravariance produce some interesting outcomes. **Covariant types are read-only, while contravariant types are write-only.**

Remember that covariant types accept subtypes, so `ArrayList<? extends Numb`er> can contain any object that is either `of a` Number type or its subtype.

In this example, line 9 works, because we can be certain that whatever we get from the ArrayList can be upcasted to a `Number` type (because if it extends `Number`, by definition, it _is a_ `Number`).

But `nums.add()` doesn’t work, because we cannot be sure of the “actual type” of the object. All we know is that it must be a `Number` or its subtypes (e.g. Integer, Double, Long, etc.).

With contravariance, the converse is true.

Line 9 works, because we can be certain that whatever the “actual type” of the object is, it must be `Integer` or its supertype, and thus accept an `Integer` object.

But line 10 doesn’t work, because we cannot be sure that we will get an `Integer`. For instance, `nums` could be referencing an ArrayList of `Objects`.

#### Applications

Therefore, since covariant types are read-only and contravariant types are write-only (loosely speaking), we can derive the following rule of thumb: **“Producer extends, consumer super”**.

A producer-like object that produces objects of type `T` can be of type parameter `<? extends` T>, while a consumer-like object that consumes objects of type T can be of type para`meter <?` super T>.

