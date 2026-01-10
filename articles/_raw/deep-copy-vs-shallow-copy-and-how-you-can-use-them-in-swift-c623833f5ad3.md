---
title: Deep copy vs. shallow copy — and how you can use them in Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T23:42:32.000Z'
originalURL: https://freecodecamp.org/news/deep-copy-vs-shallow-copy-and-how-you-can-use-them-in-swift-c623833f5ad3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7s9oXXuSiTw_HDCwc0Mrqw.jpeg
tags:
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Payal Gupta

  Copying an object has always been an essential part in the coding paradigm. Be it
  in Swift, Objective-C, JAVA or any other language, we’ll always need to copy an
  object for use in different contexts.

  In this article, we’ll discuss in d...'
---

By Payal Gupta

Copying an object has always been an essential part in the coding paradigm. Be it in Swift, Objective-C, JAVA or any other language, we’ll always need to copy an object for use in different contexts.

In this article, we’ll discuss in detail how to copy different data types in Swift and how they behave in different circumstances.

### Value and Reference types

All the data types in Swift broadly fall into two categories, namely **value types** and **reference types**.

* **Value type** — each instance keeps a unique copy of its data. Data types that fall into this category include — `all the basic data types, struct, enum, array, tuples`.
* **Reference type** — instances share a single copy of the data, and the type is usually defined as a `class`.

The most distinguishing feature of both the types lies in their copying behaviour.

### What is Deep and Shallow copy?

An instance, whether it’s a value type or a reference type, can be copied in one of the following ways:

#### **Deep copy —** Duplicates everything

* With a deep copy, any object pointed to by the source is copied and the copy is pointed to by the destination. So two completely separate objects will be created.
* **Collections** — A deep copy of a collection is two collections with all of the elements in the original collection duplicated.
* **Less prone to race conditions** and performs well in a multithreaded environment — changes in one object will have no effect on another object.
* **Value types** are copied deeply.

In the above code,

* **Line 1**: `arr1` — array (a value type) of Strings
* **Line 2**: `arr1` is assigned to `arr2`. This will create a deep copy of `arr1` and then assign that copy to `arr2`
* **Lines 7 to 11**: any changes done in `arr2` don’t reflect in `arr1` .

This is what deep copy is — completely separate instances. The same concept works with all the value types.

In some scenarios, that is when a value type contains nested reference types, deep copy reveals a different kind of behaviour. We’ll see that in upcoming sections.

#### **Shallow copy —** Duplicates as little as possible

* With a shallow copy, any object pointed to by the source is also pointed to by the destination. So only one object will be created in the memory.
* **Collections** — A shallow copy of a collection is a copy of the collection structure, not the elements. With a shallow copy, two collections now share the individual elements.
* **Faster** — only the reference is copied.
* Copying **reference types** creates a shallow copy.

In the above code,

* **Lines 1 to 8**: `Address` class type
* **Line 10**: `a1` — an instance of `Address` type
* **Line 11**: `a1` is assigned to `a2`. This will create a shallow copy of `a1` and then assign that copy to `a2` , that is only the reference is copied into `a2`.
* **Lines 16 to 19**: any changes done in `a2` will certainly reflect in `a1` .

![Image](https://cdn-media-1.freecodecamp.org/images/1*HCBKXip1e4ACmsDcDcGOrA.png)

In the above illustration, we can see that both `a1` and `a2` point to the same memory address.

### Copying Reference Types Deeply

As of now, we know that whenever we try to copy a reference type, only the reference to the object is copied. No new object is created. What if we want to create a completely separate object?

We can create a deep copy of the reference type using the `[copy()](https://developer.apple.com/documentation/objectivec/nsobject/1418807-copy)` method. According to the [documentation](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy),

copy() — Returns the object returned by `[copy(with:)](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy)`.

This is a convenience method for classes that adopt the `[NSCopying](https://developer.apple.com/documentation/foundation/nscopying)` protocol. An exception is raised if there is no implementation for `[copy(with:)](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy)`.

Let’s restructure the `Address class` we created in Code Snippet 2 to conform to the `NSCopying` protocol.

In the above code,

* **Lines 1 to 14**: `Address` class type conforms to `NSCopying` and implements `[copy(with:)](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy)` method
* **Line 16**: `a1` — an instance of `Address` type
* **Line 17**: `a1` is assigned to `a2` using `copy()` method. This will create a deep copy of `a1` and then assign that copy to `a2` , that is a completely new object will be created.
* **Lines 22 to 25**: any changes done in `a2` will not reflect in `a1` .

![Image](https://cdn-media-1.freecodecamp.org/images/1*KRe3gHvPBmPeclvEctU4qA.png)

As is evident from the above illustration, both `a1` and `a2` point to different memory locations.

Let’s look at another example. This time we’ll see how it works with **nested reference types — a reference type containing another reference type**.

In the above code,

* **Line 22:** a deep copy of `p1` is assigned to `p2` using the `copy()` method. This implies that any change in one of them must not have any effect on the other one.
* **Lines 27 to 28:** `p2’s` `name` and `city` values are changed. These must not reflect in `p1`.
* **Line 30:** `p1’s` `name` is as expected, but its `city`? It should be `“Mumbai”` shouldn’t it? But we can’t see that happening. `“Bangalore”` was only for `p2` right? Yup…exactly.?

_Deep copy…!_? T_hat was not expected from you. You said you’ll copy everything. And now you are behaving like this. Why oh why..?! What do I do now? ☠_️

Don’t panic. Let’s look at what memory addresses has to say in this.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6AbWa3I3gC4p-PsFCILOew.png)

From the above illustration, we can see that

* `p1` and `p2` point to different memory locations as expected.
* But their `address` variables are still pointing to the same location. This means that even after copying them deeply, only the references are copied — that is, a **shallow copy** of course.

**Please note:** every time we copy a reference type, a shallow copy is created by default until we explicitly specify that it should be copied deeply.

```
func copy(with zone: NSZone? = nil) -> Any{    let person = Person(self.name, self.address)    return person}
```

In the above method we implemented earlier for the `Person` class, we have created a new instance by copying the address with `self.address` . This will only copy the reference to the address object. This is the reason why both `p1` and `p2’s` `address` point to the same location.

So, copying the object using the `copy()` method won’t create a true deep copy of the object**_._**

**To duplicate a reference object completely:** the reference type along with all the nested reference types must be copied with the `copy()` method.

```
let person = Person(self.name, self.address.copy() as? Address)
```

Using the above code in the `func copy(with zone: NSZone? = nil) ->` Any method will get everything working. You can see that from the below illustration.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XdsZvbu6N5jYEDumL3PCUw.png)

### True Deep Copy — Reference and Value types

We’ve already seen how we can create a deep copy of the reference types. Of course we can do that with all the nested reference types.

But what about the nested reference type in a value type, that is an array of objects, or a reference type variable in a struct or maybe a tuple? Can we resolve that using `copy()` too? No we can’t, actually. The `copy()` method requires implementing `NSCopying` protocol which only works for `NSObject` subclasses. Value types don’t support inheritance, so we can’t use `copy()` with them.

In line 2, only the structure of `arr1` is deep copied, but the `Address` objects inside it are still shallow copied. You can see that from the below memory map.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P4qAq9o-mqCbhiHx0mfnYA.png)

The elements in both `arr1` and `arr2` both point to the same memory locations. This is because of the same reason — reference types are shallow copied by default.

**Serializing and then de-serializing** an object always creates a brand new object. It is valid for both value types as well as the reference types.

Here are some APIs that we can use to serialize and de-serialize data:

1. [**NSCoding**](https://developer.apple.com/documentation/foundation/nscoding) — A protocol that enables an object to be encoded and decoded for archiving and distribution. It will only work with `class` type objects as it requires inheriting from `NSObject` .
2. [**Codable**](https://developer.apple.com/documentation/foundation/archives_and_serialization/encoding_and_decoding_custom_types) — Make your data types encodable and decodable for compatibility with external representations such as JSON. It will work for both value types — `struct, array, tuple, basic data types`well as reference types — `class` .

Let’s restructure the `Address` class a bit further to conform to the `Codable` protocol and remove all the `NSCopying` code that we added earlier in Code Snippet 3.

In the above code, lines 11–13 will create a true deep copy of `arr1`. Below is the illustration that gives a clear picture of the memory locations.

![Image](https://cdn-media-1.freecodecamp.org/images/1*17lE3zZhorgMa6GFLNoOoA.png)

### Copy on Write

Copy on write is an optimization technique that helps boost performance when copying value types.

Let’s say we copy a single String or Int or maybe any other value type — we won’t face any crucial performance issues in that case. But what about when we copy an array of thousands of elements? Will it still not create any performance issues? What if we just copy it and don’t make any changes to that copy? Isn’t that extra memory we used just a waste in that case?

Here comes the concept of Copy in Write — when copying, each reference points to the same memory address. It’s only when one of the references modifies the underlying data that Swift actually copies the original instance and makes the modification.

That is, whether it’s deep copy or shallow copy, a new copy will not be created until we make a change in one of the objects.

In the above code,

* **Line 2**: a deep copy of `arr1` is assigned to `arr2`
* **Lines 4 and 5**: `arr1` and `arr2` still point to the same memory address
* **Line 7**: changes made in `arr2`
* **Lines 9 and 10**: `arr1` and `arr2` now pointing to different memory locations

Now you know more about deep and shallow copies and how they behave in different scenarios with different data types. You can try them with your own set of examples and see what results you get.

### Further reading

Don’t forget to read my other articles:

1. [Everything about Codable in Swift 4](https://hackernoon.com/everything-about-codable-in-swift-4-97d0e18a2999)
2. [Everything you’ve always wanted to know about notifications in iOS](https://medium.freecodecamp.org/ios-10-notifications-inshorts-all-in-one-ad727e03983a)
3. [Color it with GRADIENTS — iOS](https://hackernoon.com/color-it-with-gradients-ios-a4b374c3c79f)
4. [Coding for iOS 11: How to drag & drop into collections & tables](https://hackernoon.com/drag-it-drop-it-in-collection-table-ios-11-6bd28795b313)
5. [All you need to know about Today Extensions (Widget) in iOS 10](https://hackernoon.com/app-extensions-and-today-extensions-widget-in-ios-10-e2d9fd9957a8)
6. [UICollectionViewCell selection made easy..!!](https://hackernoon.com/uicollectionviewcell-selection-made-easy-41dae148379d)

Feel free to leave comments in case you have any questions.

