---
title: What is a Java Hashmap?
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-12T20:53:24.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-java-hashmap
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/tyler-nix-7ukf-r-Oh-k-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "In Java, you use a HashMap to store items in key/value pairs. You can access\
  \ items stored in a HashMap using the item's key, which is unique for each item.\
  \ \nIn this article, we'll talk about the features of a HashMap, how to create a\
  \ HashMap, and the..."
---

In Java, you use a HashMap to store items in key/value pairs. You can access items stored in a `HashMap` using the item's key, which is unique for each item. 

In this article, we'll talk about the features of a `HashMap`, how to create a `HashMap`, and the different methods we can use to interact with the data stored in them. 

## What Are the Features of a HashMap in Java?

Before working with HashMaps, it is important to understand how they work.

Here are some of the features of a `HashMap`:

* Items are stored in key/value pairs. 
* Items do not maintain any order when added. The data is unordered. 
* In a case where there are duplicate keys, the last one will override the other(s). 
* Data types are specified using wrapper classes instead of primitive data types. 

## How to Create a HashMap in Java

In order to create and use a HashMap, you must first import the `java.util.HashMap` package. That is:

```java
import java.util.HashMap;
```

Here's what the syntax looks like for creating a new `HashMap`:

```txt
HashMap<KeyDataType, ValueDataType> HashMapName = new HashMap<>();
```

Let's explain some of the key terms in the syntax above. 

* `KeyDataType` denotes the data type of all the keys that'll be stored in the `HashMap`. 
* `ValueDataType` denotes the data type of all the values that'll be stored in the `HashMap`. 
* `HashMapName` denotes the name of the `HashMap`. 

Here's an example to simplify the terms:

```java
HashMap<Integer, String> StudentInfo = new HashMap<>();
```

In the code above, we created a `HashMap` called `StudentInfo`. The keys that will be stored in the `HashMap` will all be integers while the values will be strings. 

You'll notice that we're working with wrapper classes and not primitive types when specifying the data types for the keys and values. This is how HashMaps work. 

Before we dive into examples, here's a list of wrapper classes and their corresponding primitive data types in Java:

### Wrapper Classes and Primitive Types in Java

| Wrapper classes   |      Primitive data types      |
|----------|:-------------:|
| Integer |  int	 |
| Character |    char   |
| Float | float | 
| Byte |  byte	 |
| Short | short | 
| Long |  long	 |
| Double |    double   |
| Boolean | boolean | 

When working with HashMaps, we make use of wrapper classes. 

## HashMap Methods in Java

In this section, we'll talk about some of the useful methods that you can use when working with HashMaps. 

You'll learn how to add, access, remove, and update items in a `HashMap`. 

### How to Add Items to a `HashMap` in Java

To add items to a `HashMap`, we make use of the `put()` method. It takes in two parameters — the key and the value of the item being added. 

Here's how it works:

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        System.out.println(StudentInfo);
        // {1=Ihechikara, 2=Jane, 3=John}
    }
}
```

In the code above, the `HashMap` is called `StudentInfo`. We specified the keys as integers while the values were strings: `HashMap<Integer, String>`. 

To add items to the `HashMap`, we used the `put()` method: 

```java
StudentInfo.put(1, "Ihechikara");
StudentInfo.put(2, "Jane");
StudentInfo.put(3, "John");
```

We added three items, each of them having an integer as a key and a string as their values. 

### How to Access Items in a `HashMap` in Java

You can use the `get()` method to access items stored in a `HashMap`. It takes one parameter — the key of the item being accessed. 

Here's an example:

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        System.out.println(StudentInfo.get(2));
        // Jane
    }
}
```

In the example above, `StudentInfo.get(2)` returns the value with a key of `2`. "Jane" was printed out to the console.

### How to Change the Value of Items in a HashMap in Java

To change the value of items in a `HashMap`, we make use of the `replace()` method. It takes two parameters – the key of the item to be changed and the new value to be assigned to it.

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        // Update key 1
        StudentInfo.replace(1, "Doe");
        
        System.out.println(StudentInfo);
        // {1=Doe, 2=Jane, 3=John}
    }
}
```

When the `HashMap` above got items assigned to it, the item with a key of `1` had a value of "Ihechikara". 

We changed its value to "Doe" using the `replace()` method: `StudentInfo.replace(1, "Doe");`

### How to Delete Items in a `HashMap` in Java

You can use the `remove()` method to delete an item from a `HashMap`. It takes in one parameter — the key of the item to be removed. 

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        // Remove key 1
        StudentInfo.remove(1);
        
        System.out.println(StudentInfo);
        // {2=Jane, 3=John}
    }
}
```

Using the `remove()` method, we deleted the item with a key of `1`. 

If you want to remove all the items in a `HashMap` at once, you use the `clear()` method. That is: 

```java
import java.util.HashMap;
class HashMapExample {
    public static void main(String[] args) {
        HashMap<Integer, String> StudentInfo = new HashMap<>();

        StudentInfo.put(1, "Ihechikara");
        StudentInfo.put(2, "Jane");
        StudentInfo.put(3, "John");
        
        // Remove all items
        StudentInfo.clear();
        
        System.out.println(StudentInfo);
        // {}
    }
}
```

There are other useful methods like:

* `containsKey` which returns `true` if a specified key exists in a `HashMap`.
* `containsValue` which returns `true` if a specified value exists in a `HashMap`.
* `size()` which returns the number of items in a `HashMap`. 
* `isEmpty()` which returns `true` if a `HashMap` has no items in it, and so on.

## Summary

In this article, we talked about `HashMap` in Java. First, we talked about the features of a `HashMap`.

We then saw how to create a `HashMap` and some of the methods you can use to interact with the data stored in them, with code examples.

Happy coding!

