---
title: How to Initialize a Java List – List of String Initialization in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-14T14:30:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-initialize-a-java-list
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Shittu-Olumide-How-to-Initialize-a-Java-List---List-of-String-Initialization-in-Java.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: 'By Shittu Olumide

  Java is a popular programming language widely used for developing robust and scalable
  applications. One of the essential data structures in Java is a list, which allows
  developers to store and manipulate a collection of elements.

  In...'
---

By Shittu Olumide

Java is a popular programming language widely used for developing robust and scalable applications. One of the essential data structures in Java is a list, which allows developers to store and manipulate a collection of elements.

Initializing a list in Java is a crucial step in the development process as it defines the initial state of the list and prepares it for further operations. There are various ways to initialize a list in Java, and the choice depends on the specific requirements of the project. 

In this article, we will explore the different methods to initialize a Java list and provide examples to illustrate their usage. Whether you are a beginner or an experienced Java developer, this guide will help you understand the best practices for initializing a Java list and improving the performance of your application.

In Java, there are different ways to initialize a list:

1. Using the `ArrayList` constructor.
2. Using the `add()` method.
3. Using the `Arrays.asList()` method.
4. Using the `Stream.of()` method.

Let's take a deep look into these methods.

## How to Initialize a List Using the `ArrayList` Constructor

In Java, the `ArrayList` class is a dynamic array implementation of the `List` interface, allowing elements to be added and removed from the list as needed. The `ArrayList` class provides several constructors for creating an instance of the class.

The syntax for creating an `ArrayList` object with no initial capacity is:

```java
ArrayList<Object> list = new ArrayList<Object>();

```

The constructor with no arguments creates an empty list with an initial capacity of 10 elements. If the list grows beyond that capacity, the `ArrayList` class automatically increases the capacity by creating a new array with a larger size and copying the elements from the old array to the new array.

Alternatively, we can create an `ArrayList` object with an initial capacity using the constructor with a single integer argument:

```java
ArrayList<Object> list = new ArrayList<Object>(capacity);

```

where `capacity` is the initial capacity of the list.

To initialize a `List` with values, we can use the constructor that takes a `Collection` as an argument. We can pass any collection object that implements the `Collection` interface to this constructor, such as another `ArrayList` or a `LinkedList`. The elements in the collection are added to the new `ArrayList` in the order they appear in the collection.

Here's an example of how to create an `ArrayList` and initialize it with values using the constructor that takes a `Collection`:

```java
import java.util.ArrayList;
import java.util.Arrays;

public class Example {
    public static void main(String[] args) {
        // create an array of integers
        Integer[] array = {1, 2, 3, 4, 5};

        // create a list from the array
        ArrayList<Integer> list = new ArrayList<Integer>(Arrays.asList(array));

        // print the list
        System.out.println(list); // [1, 2, 3, 4, 5]
    }
}

```

In this example, we create an array of integers and then pass it to the `Arrays.asList()` method to create a `List` object. We then pass this `List` object to the `ArrayList` constructor to create a new `ArrayList` with the same elements as the original array. Finally, we print the contents of the list using the `System.out.println()` method.

## How to Initialize a List Using the `add()` Method

The `add()` method is a commonly used method in Java that is used to add elements to a collection or list. This method is available for several types of collections in Java, including List, Set, and Map. The `add()` method takes a single argument, which is the element that needs to be added to the collection.

When it comes to adding elements to a Java List, the `add()` method is particularly useful. Lists in Java are ordered collections that can contain duplicates. The `add()` method can be used to add elements to the end of a list, which makes it a convenient way to initialize a list with some initial values.

Here is an example of how to use the `add()` method to initialize a Java list:

```java
import java.util.ArrayList;
import java.util.List;

public class ListExample {
    public static void main(String[] args) {
        // create a new ArrayList
        List<String> myList = new ArrayList<>();

        // add elements to the list using the add() method
        myList.add("apple");
        myList.add("banana");
        myList.add("cherry");

        // print the contents of the list
        System.out.println(myList);
    }
}

```

 In this example, we first create a new ArrayList called `myList`. We then use the `add()` method to add three strings ("apple", "banana", and "cherry") to the end of the list. Finally, we print the contents of the list using the `System.out.println()` method.

When we run this program, the output will be:

```
[apple, banana, cherry]

```

## How to Initialize a List Using the `Arrays.asList()` Method

The `Arrays.asList()` method is a built-in method in Java that converts an array into a List. This method takes an array as an argument and returns a List object. The List object returned by the `Arrays.asList()` method is a fixed-size list, which means that we cannot add or remove elements from it.

To use the `Arrays.asList()` method to initialize a Java List, we can follow these steps:

First, declare an array of elements that we want to initialize the list with. For example, let's say we want to initialize a list with three elements: "apple", "banana", and "orange". We can declare an array as follows:

```java
String[] fruits = {"apple", "banana", "orange"};

```

Then call the `Arrays.asList()` method and pass the array as an argument. This will return a List object containing the elements of the array.

```java
List<String> fruitList = Arrays.asList(fruits);

```

We can now use the `fruitList` object to access the elements of the list. For example, we can iterate over the list and print each element:

```java
for (String fruit : fruitList) {
    System.out.println(fruit);
}

```

Output:

```
apple
banana
orange

```

It is important to note that the `Arrays.asList()` method does not create a new List object, but rather returns a view of the original array as a List object. This means that if we modify the original array, the changes will be reflected in the List object as well. For example:

```java
fruits[0] = "pear";
System.out.println(fruitList.get(0)); // Output: pear

```

In the above example, we modified the first element of the `fruits` array to "pear". When we access the first element of the `fruitList` object, we get "pear" as well, because `fruitList` is just a view of the `fruits` array.

## How to Initialize a List Using the `Stream.of()` Method

The `Stream.of()` method is a convenient method provided by Java 8 and higher versions in the `java.util.stream` package. It is used to create a stream of elements of any type, including primitive types, arrays, and objects. This method takes one or more arguments and returns a stream consisting of those arguments.

Here is the syntax for the `Stream.of()` method:

```java
Stream<T> stream = Stream.of(t1, t2, t3, ..., tn);

```

where `T` is the type of the elements in the stream, and `t1` through `tn` are the elements to be included in the stream.

To initialize a Java list using the `Stream.of()` method, we can follow these steps:

First, import the `java.util.stream` package.

Then create a list of the desired type using the `ArrayList` constructor, for example:

```java
List<String> myList = new ArrayList<>();

```

Initialize the list using the `Stream.of()` method, passing in the desired elements as arguments, and then use the `collect()` method to collect the stream elements into the list, for example:

```java
myList = Stream.of("Apple", "Banana", "Cherry", "Date")
              .collect(Collectors.toList());
              
```

We can then print the list to verify its contents.

```java
System.out.println(myList);

```

Output:

```
[Apple, Banana, Cherry, Date]

```

## Conclusion 

In conclusion, initializing a Java List is a common task in Java programming, and there are several ways to do it. 

By following the steps outlined in this article, we can easily create and initialize a Java List with the desired elements using the `Stream.of()` method. This approach is concise and flexible, and it can be especially useful when we need to initialize a list with a small number of elements.

Let's connect on [Twitter](https://www.twitter.com/Shittu_Olumide_) and on [LinkedIn](https://www.linkedin.com/in/olumide-shittu). You can also subscribe to my [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A) channel.

Happy Coding!

