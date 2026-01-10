---
title: Java Sort Array – How to Reverse an Array in Ascending or Descending Order
  with Arrays.sort()
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-14T21:14:36.000Z'
originalURL: https://freecodecamp.org/news/java-sort-array-how-to-reverse-an-array-in-ascending-or-descending-order-with-arrays-sort-2
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/andre-taissin-hOwcob_3dpc-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: null
seo_desc: "In Java, you use arrays to store a collection of variables (with the same\
  \ data type) in a single variable. \nIn many cases, the values stored in an array\
  \ appear in a random order. Using the Arrays class in Java, you have access to various\
  \ methods you ..."
---

In Java, you use arrays to store a collection of variables (with the same data type) in a single variable. 

In many cases, the values stored in an array appear in a random order. Using the `Arrays` class in Java, you have access to various methods you can use to manipulate arrays.

One of the methods we'll be using from the `Arrays` class is the `sort()` method which sorts an array in ascending order.

We'll also see how to sort an array in descending order using the `reverseOrder()` method from the `Collections` class in Java. 

## How to Sort an Array in Ascending Order in Java Using `Arrays.sort()`

In this section, we'll see an example on how we can use the `sort()` method to sort an array in ascending order. 

```java
import java.util.Arrays;

class ArraySort {
    public static void main(String[] args) {
        int[] arr = { 5, 2, 1, 8, 10 };
        Arrays.sort(arr);
        
        for (int values : arr) {
            System.out.print(values + ", ");
            // 1, 2, 5, 8, 10,
        }
    }
}
```

The first thing we did in the example above was to import the `Arrays` class: `import java.util.Arrays;`. This give us access to all the methods of the `Arrays` class. 

We then created an array with numbers in a random order: `int[] arr = { 5, 2, 1, 8, 10 };`.

In order to sort this array in ascending order, we passed in the array as parameter to the `sort()` method: `Arrays.sort(arr);`.

Note that the `Arrays` class was written first before accessing the `sort()` method using dot notation.

Lastly, we looped through and printed the array in the console. The result was a sorted array: `1, 2, 5, 8, 10`.

In the next section, we'll talk about sorting an array in descending order. 

## How to Sort an Array in Descending Order in Java Using `Collections.reverseOrder()`

To sort an array in descending order, we use the `reverseOrder()` which we can access from the `Collections` class.

We'll still make use of `Arrays.sort();`, but in this example, it'll take in two parameters – the array to be sorted and `Collections.reverseOrder()`. 

Here's an example:

```java
import java.util.Arrays;
import java.util.Collections;

class ArraySort {
    public static void main(String[] args) {
        Integer[] arr = { 5, 2, 1, 8, 10 };
        Arrays.sort(arr, Collections.reverseOrder());
        
        for (int values : arr) {
            System.out.print(values + ", ");
            // 10, 8, 5, 2, 1,
        }
    }
}
```

First things first, we imported the Arrays and Collections classes because we'll be making use the methods provided by the classes. 

We then created an array of numbers in random order: `Integer[] arr = { 5, 2, 1, 8, 10 };`.  You'll notice that we used `Integer[]` instead of `int[]` like we did in the last example – the latter would throw an error. 

To sort the array in descending order, we did this: `Arrays.sort(arr, Collections.reverseOrder());`. 

The first parameter is the array `arr` which will be sorted in ascending order. The second parameter – `Collections.reverseOrder()` – will then reverse the order of the sorted array so it is arranged in descending order.

When looped through and printed, the array would look like this: `10, 8, 5, 2, 1`.

## Summary

In this article, we talked about sorting arrays in Java. Arrays can be sorted in ascending or descending order. 

We can sort arrays in ascending order using the `sort()` method which can be accessed from the `Arrays` class. The `sort()` method takes in the array to be sorted as a parameter. 

To sort an array in descending order, we used the `reverseOrder()` method provided by the `Collections` class. This is passed in as a second parameter in the `sort()` method so that the sorted array can be rearranged in descending order. 

Happy coding!

