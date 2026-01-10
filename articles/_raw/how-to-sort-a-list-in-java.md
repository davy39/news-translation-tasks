---
title: How to Sort a List in Java – Java List Sorting Example
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-01-24T19:22:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-sort-a-list-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/kelly-sikkema-ABkfxGoB-RE-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "Sometimes data needs to be arranged in a specific order so it's easier\
  \ to understand, search, and process. \nWe call this process sorting. Sorting refers\
  \ to arranging data in a specific order using certain criteria. You can sort different\
  \ types of dat..."
---

Sometimes data needs to be arranged in a specific order so it's easier to understand, search, and process. 

We call this process sorting. Sorting refers to arranging data in a specific order using certain criteria. You can sort different types of data, including numbers, strings, and objects. Java provides built-in methods for sorting, such as the Collections classes.  
  
Sorting data in Java could be useful in an e-commerce application where a list of products needs to be displayed to the user. The products can be sorted in various ways depending on the requirements the user sets such as price, rating, brand, and so on.

For example, if the user wants to see all the products sorted by price in ascending order, the application can use a sorting algorithm to arrange the products in that order. This way, when the user views the products, they will be able to see the cheapest products first and make a purchase decision accordingly.  
  
This article will look at various methods for sorting a list in Java.

## How to Use the `Collections.Sort()` Method in Java

One of the most common ways to sort data in Java is to use the `Collections.sort()` method. It sorts a list in ascending order by default. 

Here is an example of how to use the `Collections.sort()` method to sort a list of integers:

```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<Integer>();
        numbers.add(3);
        numbers.add(1);
        numbers.add(4);
        numbers.add(2);
        
        Collections.sort(numbers);
        
        System.out.println("Sorted List: " + numbers);
    }
}

```

The above code creates a list of integers, adds four numbers to it, sorts the list, and then prints the sorted list to the console. 

It uses classes from the Java standard library, including **`java.util.Collections`**, **`java.util.List`**, and **`java.util.ArrayList`** to perform the operations. 

The output of the above code is shown below:

```bash
//Output
Sorted List: [1, 2, 3, 4]
```

You can also sort a list of custom objects using the `Collections.sort()` method. To do this, you will need to create a comparator and pass it as an argument to the `Collections.sort()` method. 

A comparator is an object that implements the `java.util.Comparator` interface. It has a single method called `compare()` that compares two objects and returns an integer indicating their relative order.

Here is an example of how to use a comparator to sort a list of custom objects:

```java
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        people.add(new Person("Alice", 25));
        people.add(new Person("Bob", 30));
        people.add(new Person("Charlie", 20));
        
        Collections.sort(people, new PersonComparator());
        
        System.out.println("Sorted List: " + people);
    }
}

class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
    
    @Override
    public String toString() {
        return name + " (" + age + ")";
    }
}

class PersonComparator implements java.util.Comparator<Person> {
    @Override
    public int compare(Person a, Person b) {
        return a.getAge() - b.getAge();
    }
}

```

The code above creates a list of 'Person' objects, adds several Person objects to the list, sorts the list using a custom comparator (`PersonComparator`), and then prints out the sorted list. 

The `Person` class has two fields, `name` and `age`, and getter methods for these fields. The `PersonComparator` class implements the Comparator interface and overrides the compare method to sort `Person` objects by age.  
  
The output of this program will be the following:

```bash
//output
Sorted List: [Charlie (20), Alice (25), Bob (30)]
```

It's best to use the **`Collections.sort()`** method when you have a collection of objects that need to be sorted based on one or more fields. 

For example, if you have a collection of Employee objects and you want to sort them by their last name, you can use the `Collections.sort()` method and pass in a custom Comparator that compares the last names of the Employee objects.

## How to Use the List.Sort() Method in Java

This method sorts a list in ascending order. Here's how it works:

```java
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(5, 3, 2, 4, 1);
        numbers.sort(null);
        System.out.println(numbers); // prints [1, 2, 3, 4, 5]
    }
}

```

Inside the main method above, a list of integers called "numbers" is created using the `Arrays.asList` method. The code then sorts this list of numbers using the default sorting method since null is passed to the sort method.

Finally, the sorted list is printed to the console using the `System.out.println` method, which will output "[1, 2, 3, 4, 5]".

**`List.sort()`** is useful when you have a list of elements that need to be sorted. For example, if you have a list of strings and you want to sort them in alphabetical order, you can use the `List.sort()` method. 

`List.sort()` is an instance method of the List class and it sorts the elements in the order defined by their natural ordering or by a specified `Icomparer` implementation.

## How to Use the `stream.sorted()` Method in Java

In Java 8 and above, you can use the **Stream API** to sort a list. The Stream API provides a sorted method that you can use to sort the elements of a stream. 

Here is an example of how to sort a list of integers using a stream:

```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {

        List<Integer> numbers = Arrays.asList(5, 3, 2, 4, 1);
        List<Integer> sortedList = numbers.stream().sorted().collect(Collectors.toList());
        System.out.println(sortedList); // prints [1, 2, 3, 4, 5]

    }
}

```

In the example above, the number list is converted to a stream using the `stream()` method. The `sorted()` method is then called on the stream to sort the elements. The `collect(Collectors.toList())` method is used to collect the sorted elements back into a list. The result is a new list containing the sorted elements. The output will be "[1, 2, 3, 4, 5]".

**`stream.sorted()`** is best used when you have a stream of elements that need to be sorted. For example, if you have a stream of integers and you want to sort them in ascending order, you can use the `stream.Sorted()` method.

## Conclusion

In this tutorial, you learned that there are several ways to sort a list in Java – the **Collections.sort()** method, the **stream.sorted()** method, and the **List.sort()** method. The best method to use depends on the specific requirements of the task at hand as we discussed above.

I hope this article has given you the correct information on how to sort a list in Java.

Happy coding!

