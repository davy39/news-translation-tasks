---
title: Java List Methods Tutorial – Util List API Example
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-15T16:15:27.000Z'
originalURL: https://freecodecamp.org/news/java-list-tutorial-util-list-api-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/collection0.jpg
tags:
- name: api
  slug: api
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: null
seo_desc: "By Yiğit Kemal Erinç\nLists are commonly used data structures in every\
  \ programming language. \nIn this tutorial we are going to investigate Java's List\
  \ API. We'll start off with basic operations, and then we will get into more advanced\
  \ stuff (like a co..."
---

By Yiğit Kemal Erinç

Lists are commonly used data structures in every programming language. 

In this tutorial we are going to investigate Java's List API. We'll start off with basic operations, and then we will get into more advanced stuff (like a comparison of different list types, such as ArrayList and LinkedList). 

I will also give you some guidelines to help you choose the list implementation that is best for your situation.

Although basic Java knowledge is enough for following the tutorial, the last section requires basic data structures (Array, LinkedList) and [Big-O](https://en.wikipedia.org/wiki/Big_O_notation) knowledge. If you are not familiar with those, feel free to skip that section.

## Definition of Lists

Lists are ordered collections of objects. They are similar to sequences in math in that sense. They're unlike sets, however, which do not have a certain order. 

A couple of things to keep in mind: lists are allowed to have duplicates and null elements. They are reference or object types, and like all objects in Java, they're stored in the heap.

A list in Java is an interface and there are many list types that implement this interface. 

![Image](https://www.freecodecamp.org/news/content/images/2020/09/ListHierarchy.png)
_Collection Hierarchy_

I will use ArrayList in the first few examples, because it is the most commonly used type of list. 

ArrayList is basically a resizable array. Almost always, you want to use ArrayList over regular arrays since they provide many useful methods. 

An array's only advantage used to be their fixed size (by not allocating more space than you need). But lists also support fixed sizes now.

## How to Create a List in Java

Enough chatting, let's start by creating our list. 

```java
import java.util.ArrayList;
import java.util.List;

public class CreateArrayList {
    public static void main(String[] args) {
        ArrayList<Integer> list0 = new ArrayList<>();

        // Makes use of polymorphism
        List list = new ArrayList<Integer>();

        // Local variable with "var" keyword, Java 10
        var list2 = new ArrayList<Integer>();
    }
}
```

In the angle brackets (<>) we specify the type of objects we are going to store. 

Keep in mind that the **type in brackets must be an object type and not a primitive type**. Therefore we have to use object wrappers, Integer class instead of int, Double instead of double, and so on.

There are many ways to create an ArrayList, but I presented three common ways in the snippet above. 

The first way is by creating the object from the concrete ArrayList class by specifying ArrayList on the left hand side of the assignment.

The second code snippet makes use of polymorphism by using list on the left hand side. This makes the assignment loosely coupled with the ArrayList class and allows us to assign other types of lists and switch to a different List implementation easily.

The third way is the Java 10 way of creating local variables by making use of the var keyword. The compiler interprets the type of variable by checking the right hand side.

We can see that all assignments result in the same type:

```java
System.out.println(list0.getClass());
System.out.println(list.getClass());
System.out.println(list2.getClass());
```

Output:

```java
class java.util.ArrayList
class java.util.ArrayList
class java.util.ArrayList

```

We can also specify the initial capacity of the list. 

```java
List list = new ArrayList<>(20);
```

This is useful because whenever the list gets full and you try to add another element, the current list gets copied to a new list with double the capacity of the previous list. This all happens behind the scenes. 

This operation makes our complexity _O(n)_, though, so we want to avoid it. The default capacity is 10, so if you know that you will store more elements, you should specify the initial capacity.

## How to Add and Update List Elements in Java

To add elements to the list we can use the _add_ method. We can also specify the index of the new element, but be cautious when doing that since it can result in an _IndexOutOfBoundsException_.

```java
import java.util.ArrayList;

public class AddElement {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("hello");
        list.add(1, "world");
        System.out.println(list);
    }
}
```

Output:

```
[hello, world]
```

We can use the _set_ method to update an element.

```java
list.set(1, "from the otherside");
System.out.println(list);
```

Output:

```
[hello, world]
[hello, from the otherside]
```

## How to Retrieve and Delete List Elements in Java

To retrieve an element from the list, you can use the _get_ method and provide the index of the element you want to get.

```java
import java.util.ArrayList;
import java.util.List;

public class GetElement {
    public static void main(String[] args) {
        List list = new ArrayList<String>();
        list.add("hello");
        list.add("freeCodeCamp");

        System.out.println(list.get(1));
    }
}
```

Output:

```java
freeCodeCamp

```

The complexity of this operation on ArrayList is _O(1)_ since it uses a regular random access array in the background.

To remove an element from the ArrayList, the _remove_ method is used. 

```java
list.remove(0);
```

This removes the element at index 0, which is "hello" in this example.

We can also call the remove method with an element to find and remove it. Keep in mind that it only removes the first occurrence of the element if it is present.

```java
public static void main(String[] args) {
        List list = new ArrayList();
        list.add("hello");
        list.add("freeCodeCamp");
        list.add("freeCodeCamp");

        list.remove("freeCodeCamp");
        System.out.println(list);
    }
```

Output:

```java
[hello, freeCodeCamp]
```

To remove all occurrences, we can use the _removeAll_ method in the same way.

These methods are inside the List interface, so every List implementations has them (whether it is ArrayList, LinkedList or Vector).

## How to Get the Length of a List in Java

To get the length of a list, or the number of elements, we can use the _size()_ method. 

```java
import java.util.ArrayList;
import java.util.List;

public class GetSize {
    public static void main(String[] args) {
        List list = new ArrayList();
        list.add("Welcome");
        list.add("to my post");
        System.out.println(list.size());
    }
}

```

Output:

```
2
```

## Two-Dimensional Lists in Java

It is possible to create two-dimensional lists, similar to 2D arrays. 

```java
ArrayList<ArrayList<Integer>> listOfLists = new ArrayList<>();
```

We use this syntax to create a list of lists, and each inner list stores integers. But we have not initialized the inner lists yet. We need to create and put them on this list ourselves:

```java
int numberOfLists = 3;
for (int i = 0; i < numberOfLists; i++) {
    listOfLists.add(new ArrayList<>());
}
```

I am initializing my inner lists, and I am adding 3 lists in this case. I can also add lists later if I need to.

Now we can add elements to our inner lists. To add an element, we need to get the reference to the inner list first. 

For example, let's say we want to add an element to the first list. We need to get the first list, then add to it.

```java
listOfLists.get(0).add(1);
```

Here is an example for you. Try to guess the output of the below code segment:

```java
public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> listOfLists = new ArrayList<>();
        System.out.println(listOfLists);
        int numberOfLists = 3;
        for (int i = 0; i < numberOfLists; i++) {
            listOfLists.add(new ArrayList<>());
        }

        System.out.println(listOfLists);

        listOfLists.get(0).add(1);
        listOfLists.get(1).add(2);
        listOfLists.get(2).add(0,3);

        System.out.println(listOfLists);
}
```

Output:

```
[]
[[], [], []]
[[1], [2], [3]]
```

Notice that it is possible to print the lists directly (unlike with regular arrays) because they override the _toString()_ method.

## Useful Methods in Java

There are some other useful methods and shortcuts that are used frequently. In this section I want to familiarize you with some of them so you will have an easier time working with lists.

### How to Create a List with Elements in Java

It is possible to create and populate the list with some elements in a single line. There are two ways to do this. 

The following is the old school way:

```java
public static void main(String[] args) {
        List<String> list = Arrays.asList(
                                "freeCodeCamp",
                                "let's",
                                "create");
 }
```

You need to be cautious about one thing when using this method: Arrays.asList returns an immutable list. So if you try to add or remove elements after creating the object, you will get an _UnsupportedOperationException._ 

You might be tempted to use _final_ keyword to make the list immutable but it won't work as expected. 

It just makes sure that the reference to the object does not change – it does not care about what is happening inside the object. So it permits inserting and removing.

```java
final List<String> list2 = new ArrayList<>();
list2.add("erinc.io is the best blog ever!");
System.out.println(list2);
```

Output:

```
[erinc.io is the best blog ever!]

```

Now let's look at the modern way of doing it:

```java
ArrayList<String> friends =  new ArrayList<>(List.of("Gulbike", "Sinem", "Mete"));

```

The _List.of_ method was shipped with Java 9. This method also returns an immutable list but we can pass it to the  ArrayList constructor to create a mutable list with those elements. We can add and remove elements to this list without any problems.

### How to Create a List with N Copies of Some Element in Java

Java provides a method called _NCopies_ that is especially useful for benchmarking. You can fill an array with any number of elements in a single line.

```java
public class NCopies {
    public static void main(String[] args) {
        List<String> list = Collections.nCopies(10, "HELLO");
        System.out.println(list);
    }
}
```

Output:

```java
[HELLO, HELLO, HELLO, HELLO, HELLO, HELLO, HELLO, HELLO, HELLO, HELLO]

```

### How to Clone a List in Java

As previously mentioned, Lists are reference types, so the rules of [passing by reference](https://www.cs.fsu.edu/~myers/c++/notes/references.html) apply to them. 

```java
public static void main(String[] args) {
        List list1 = new ArrayList<String>();
        list1.add("Hello");
        List list2 = list1;
        list2.add(" World");

        System.out.println(list1);
        System.out.println(list2);
}
```

Output:

```java
[Hello,  World]
[Hello,  World]
```

The list1 variable holds a reference to the list. When we assign it to list2 it also points to the same object. If we do not want the original list to change, we can clone the list.

```java
ArrayList list3 = (ArrayList) list1.clone();
list3.add(" Of Java");

System.out.println(list1);
System.out.println(list3);
```

Output:

```java
[Hello,  World]
[Hello,  World,  Of Java]
```

Since we cloned list1, list3 holds a reference to its clone in this case. Therefore list1 remains unchanged.

### How to Copy a List to an Array in Java

Sometimes you need to convert your list to an array to pass it into a method that accepts an array. You can use the following code to achieve that:

```java
List<Integer> list = new ArrayList<>(List.of(1, 2));
Integer[] toArray = list.toArray(new Integer[0]);
```

You need to pass an array and the _toArray_ method returns that array after filling it with the elements of the list.

### How to Sort a List in Java

To sort a list we can use _Collections.sort._ It sorts in ascending order by default but you can also pass a comparator to sort with custom logic.

```java
List<Integer> toBeSorted = new ArrayList<>(List.of(3,2,4,1,-2));
Collections.sort(toBeSorted);
System.out.println(toBeSorted);
```

Output:

```
[-2, 1, 2, 3, 4]
```

## How do I choose which list type to use?

Before finishing this article, I want to give you a brief performance comparison of different list implementations so you can choose which one is better for your use case. 

We will compare ArrayList, LinkedList and Vector. All of them have their ups and downs so make sure you consider the specific context before you decide.

### Java ArrayList vs LinkedList

Here is a comparison of runtimes in terms of algorithmic complexity.

```markdown
|                       | ArrayList                  | LinkedList |
|-----------------------|----------------------------|------------|
| GET(index)            | O(1)                       | O(n)       |
| GET from Start or End | O(1)                       | O(1)       |
| ADD                   | O(1), if list is full O(n) | O(1)       |
| ADD(index)            | O(n)                       | O(1)       |
| Remove(index)         | O(n)                       | O(1)       |
| Search and Remove     | O(n)                       | O(n)       |
```

Generally, the _get_ operation is much faster on ArrayList but _add_ and _remove_ are faster on LinkedList. 

ArrayList uses an array behind the scenes, and whenever an element is removed, array elements need to be shifted (which is an _O(n)_ operation).

Choosing data structures is a complex task and there is no recipe that applies to every situation. Still, I will try to provide some guidelines to help you make that decision easier:

* If you plan to do more get and add operations other than remove, use ArrayList since the get operation is too costly on LinkedList. Keep in mind that insertion is _O(1)_ only if you call it without specifying the index and add to the end of the list.
* If you are going to remove elements and/or insert in the middle (not at the end) frequently, you can consider switching to a LinkedList because these operations are costly on ArrayList.
* Keep in mind that if you access the elements sequentially (with an iterator), you will not experience a performance loss with LinkedList while getting elements.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-72.png)
_Benchmark source: [programcreek](https://www.programcreek.com/2013/03/arraylist-vs-linkedlist-vs-vector/)_

### Java ArrayList vs Vector

Vector is very similar to ArrayList. If you are coming from a C++ background, you might be tempted to use a Vector, but its use case is a bit different than C++. 

Vector's methods have the **[synchronized](https://docs.oracle.com/javase/tutorial/essential/concurrency/syncmeth.html)** keyword, so Vector guarantees thread safety whereas ArrayList does not. 

You might prefer Vector over ArrayList in multithreaded programming or you can use ArrayList and handle the synchronization yourself. 

In a single-threaded program, it is better to stick with ArrayList because thread-safety comes with a performance cost.

## Conclusion

In this post, I have tried to provide an overview of Java's List API. We have learned to use basic methods, and we've also looked at some more advanced tricks to make our lives easier. 

We also made a comparison of ArrayList, LinkedList and Vector which is a commonly asked topic in interviews. 

Thank you for taking the time to read the whole article and I hope it was helpful.

You can access the whole code from this [repository](https://github.com/yigiterinc/list-api-tutorial).

If you are interested in reading more articles like this, you can subscribe to my [blog's](https://erinc.io/) mailing list to get notified when I publish a new article.

