---
title: How to Initialize an ArrayList in Java – Declaration with Values
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-21T06:34:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-initialize-an-arraylist-in-java-with-values
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/java-arraylist-1.png
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: null
seo_desc: "You can use an ArrayList in Java to store and manipulate a collection of\
  \ similar variables. \nAn ArrayList is just like an array but offers more flexibility.\
  \ An ArrayList is more dynamic with the size of the collection, and gives you more\
  \ control over..."
---

You can use an `ArrayList` in Java to store and manipulate a collection of similar variables. 

An `ArrayList` is just like an [array](https://www.freecodecamp.org/news/java-array-how-to-declare-and-initialize-an-array-in-java-example/) but offers more flexibility. An `ArrayList` is more dynamic with the size of the collection, and gives you more control over the elements in a collection. 

In this article, you'll learn how to declare and initialize an `ArrayList` in Java. You'll see the different in-built methods that can be used to add, access, modify, and remove elements in an `ArrayList`. 

Let's get started!

## How To Declare an ArrayList With Values in Java

The terms "declaration" and "initialization" are commonly associated with data structures.

Declaration has to do with creating a data structure, while initialization involves assigning values to the data structure. 

Here's how you can declare an `ArrayList` in Java:

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
    }
}
```

To make use of an `ArrayList`, you must first import it from the **ArrayList** class: `import java.util.ArrayList;`. 

After that, you can create a new `ArrayList` object. In the code above, we created a new  `ArrayList` object called `people`. 

Note that the data type of the `ArrayList` is specified with angle brackets: `ArrayList<String>`.

At this point, we've created an `ArrayList` but it has no elements. You'll see how to add elements to it in another section. 

Alternatively, you can create an `ArrayList` with values/elements at the point of declaration by using the `add` method in an initializer block:

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>() {{
            add("John");
            add("Jane");
            add("Doe");
        }}; 
        
        System.out.println(people);
        // [John, Jane, Doe]
    }
}
```

## How To Add Elements to a Java `ArrayList`

You can use the `add()` method to add elements to an `ArrayList`. 

Here's an example:

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
        people.add("John");
        people.add("Jane");
        people.add("Doe");
        
        System.out.println(people);
        // [John, Jane, Doe]
        
    }
}
```

In the code above, we declared an `ArrayList` called `people` without any elements. 

Using dot notation and the `add()` method, we added elements to the `people` collection: `people.add("John")`. 

## How To Access Elements in a Java `ArrayList`

You can access elements in a Java `ArrayList` by using the element's index. 

The index of the element will be passed in as a parameter to the `get()` method. That is:

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
        people.add("John");
        people.add("Jane");
        people.add("Doe");
        
        System.out.println(people.get(0));
        // John
        
    }
}
```

In the code above, `people.get(0)` gets the first element — "John". 

Note that the first element has an index of `0`, the second has an index of `1`, and so on.

## How To Modify Elements in a Java `ArrayList`

You can change or modify the value of an element by using the `set()` method. 

The `set()` method takes in two parameters — the index of the element to be changed and the new value to be assigned to that index. 

Here's an example:

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
        people.add("John");
        people.add("Jane");
        people.add("Doe");
        
        people.set(1, "Jade");
        
        System.out.println(people);
        // [John, Jade, Doe]
        
    }
}
```

In the example above, we changed the second element from "Jane" to "Jade" using its index: `people.set(1, "Jade")`. 

## How To Remove Elements in a Java `ArrayList`

You can remove an element by using the `remove()` method. The method takes in the index of the element to be removed as a parameter. That is:

```java
import java.util.ArrayList;

public class ArrayListTut {
    public static void main(String[] args) {

        ArrayList<String> people = new ArrayList<>(); 
        
        people.add("John");
        people.add("Jane");
        people.add("Doe");
        
        people.remove(2);
        
        System.out.println(people);
        // [John, Jane]
        
    }
}
```

Using the `remove()` method, we removed the third element in the collection using the element's index: `people.remove(2);`. 

## Summary

In this article, we talked about the Java `ArrayList` data structure. It can be used to store a collection of variables. 

An `ArrayList` give you more control over the elements in a collection and has a dynamic size that isn't fixed on declaration like Java arrays. 

We saw how to declare and initialize an `ArrayList` with values. We also saw different methods for adding, accessing, changing, and removing elements in an `ArrayList`. 

Happy coding! I also write about Java on [my blog](https://ihechikara.com/). 


