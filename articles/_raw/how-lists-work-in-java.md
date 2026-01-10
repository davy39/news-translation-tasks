---
title: Java List – Example Lists in Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-01-31T18:09:00.000Z'
originalURL: https://freecodecamp.org/news/how-lists-work-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/java-list-interface-cover.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "You can use the Java List interface to store objects/elements in an ordered\
  \ collection. It extends the Collection interface. \nThe  List interface provides\
  \ us with various methods for inserting, accessing, and deleting elements in a collection.\
  \  \nIn t..."
---

You can use the Java `List` interface to store objects/elements in an ordered collection. It extends the Collection interface. 

The  `List` interface provides us with various methods for inserting, accessing, and deleting elements in a collection.  

In this article, you'll learn how to extend and implement the `List` interface in Java, and how to interact with elements in a collection. 

## Implementation Classes of the Java List Interface

Here are the different implementation classes of the `List` interface in Java:

* AbstractList.
* AbstractSequentialList.
* ArrayList.
* AttributeList.
* CopyOnWriteArrayList.
* LinkedList.
* RoleList.
* RoleUnresolvedList.
* Stack.
* Vector.

The most commonly used implementation of the `List` interface are `ArrayList` and `LinkedList`. 

Since both classes above implement the `List` interface, they make use of the same methods to add, access, update, and remove elements in a collection. 

In this tutorial, we'll have a look at how we can add, access, update, and remove elements in a collection using the `ArrayList`.

## How to Implement a `List` in Java Using `ArrayList`

Unlike arrays in Java, which have a specified size, the `ArrayList` is more dynamic when it comes to storing elements. This means that you can add items as you please. 

Here's how you can create an `ArrayList`:

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
  }
}
```

In the code above, we first imported the `ArrayList` class: `import java.util.ArrayList;`.

We then created a new `ArrayList` object called `students`: `ArrayList<String> students = new ArrayList<String>();`.

Note that the data types of elements that would be stored in the `ArrayList` were specified in angle brackets: `<String>`.

### How to Add Elements to the `ArrayList`

You can use the `add()` method to add elements to the `ArrayList`.

Here's an example:

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    
    System.out.println(students);
    // [John, Jane, Doe]
    
  }
}
```

In the code above, we passed the element to be added to the `ArrayList` as a parameter: `students.add("Doe")`.

### How to Access Elements in the `ArrayList`

To access elements in the `ArrayList`, you make use of the `get()` method. Here's how:

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    System.out.println(students.get(1));
    // Jane
    
  }
}


```

As can be seen above, we passed in the index of the element to be accessed as a parameter to the `get()` method: `students.get(1)`.

### How to Update Elements in the `ArrayList`

To update the value of elements in the `ArrayList`, you make use of the `set()` method. 

It takes two parameters: the index of the element to be updated, and the new value. 

Here's an example:

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    students.set(2,"Jade");
    
    System.out.println(students);
    // [John, Jane, Jade]
    
  }
}
```

### How to Remove Elements in the `ArrayList`

To remove elements in the `ArrayList`, you make use of the `remove()` method. We also use the index to specify which element to remove. 

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    students.remove(2);
    
    System.out.println(students);
    // [John, Jane]
    
  }
}


```

You can use the `clear()` method to remove all the elements in the collection:

```java
import java.util.ArrayList;

public class Main {
    
  public static void main(String[] args) {
      
    ArrayList<String> students = new ArrayList<String>();
    
    students.add("John");
    students.add("Jane");
    students.add("Doe");
    
    students.clear();
    
    System.out.println(students);
    // []
    
  }
}


```

Although the `ArrayList` and `LinkedList` classes both have the same methods as seen in the examples in this article, the `LinkedList` class has some additional methods like:

* `addFirst()` adds an element at the beginning of the list.
* `addLast()` adds an element at the end of the list.
* `getFirst()` returns the first element of the list.
* `getLast()` returns the last element of the list.
* `removeFirst()` removes the first element of the list.
* `removeLast()` removes the last element of the list.

## Summary

In this article, we talked about the `List` interface in Java. You use it to store ordered collections of elements. 

We had a look at some of the implementation classes of the `List` interface. The most commonly used are the `ArrayList` and `LinkedList` classes.

Using code examples, we saw how to add, access, update, and remove elements in a collection with the `ArrayList`.

Although both `ArrayList` and `LinkedList` have similar methods, we highlighted some of the additional methods that you can use with the `LinkedList` class. 

Happy coding!


