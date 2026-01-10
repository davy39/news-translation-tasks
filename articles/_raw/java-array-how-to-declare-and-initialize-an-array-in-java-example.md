---
title: Java Array – How to Declare and Initialize an Array in Java Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-04T16:42:44.000Z'
originalURL: https://freecodecamp.org/news/java-array-how-to-declare-and-initialize-an-array-in-java-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/andrew-moca-yAGNjU4rtss-unsplash-1.jpg
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: null
seo_desc: 'In this article, we will talk about arrays in Java. We will go over some
  examples to help you understand what an array is, how to declare them, and how to
  use them in your Java code.

  What is an array?

  In Java, you use an array to store multiple value...'
---

In this article, we will talk about arrays in Java. We will go over some examples to help you understand what an array is, how to declare them, and how to use them in your Java code.

## What is an array?

In Java, you use an array to store multiple values of the same data type in one variable. You can also see it as a collection of values of the same data type. This means that if you are going to store strings in your array, for example, then all the values of your array should be strings.

## How to declare an array in Java

We use square brackets `[]` to declare an array. That is: 

```java
String[] names;
```

We have declared a variable called `names` which will hold an array of strings.

If we were to declare a variable for integers (whole numbers) then we would do this:

```java
int[] myIntegers;
```

So to create an array, you specify the data type that will be stored in the array followed by square brackets and then the name of the array.

## How to initialize an array in Java

To initialize an array simply means to assign values to the array. Let's initialize the arrays we declared in the previous section:

```java
String[] names = {"John", "Jade", "Love", "Allen"};
```

```java
int[] myIntegers = {10, 11, 12};
```

We have initialized our arrays by passing in values with the same data type with each value separated by a comma.

If we wanted to access the elements/values in our array, we would refer to their index number in the array. The index of the first element is 0. Here is an example:

```java
String[] names = {"John", "Jade", "Love", "Allen"};

System.out.println(names[0]);
// John

System.out.println(names[1]);
// Jade

System.out.println(names[2]);
// Love

System.out.println(names[3]);
// Allen
```

Now that we now how to access each element, let's change the value of the third element. That looks like this:

```java
String[] names = {"John", "Jade", "Love", "Allen"};
names[2] = "Victor";

System.out.println(names[2]);
// Victor
```

We can also check the length of an array using the `length` property. Here is an example: 

```java
String[] names = {"John", "Jade", "Love", "Allen"};
System.out.println(names.length);
// 4
```

## How to loop through an array in Java

We can use the `for` loop to loop through the elements in an array. 

```java
String[] names = {"John", "Jade", "Love", "Allen"};
for (int i = 0; i < names.length; i++) {
  System.out.println(names[i]);
}

// John
// Jade
// Love
// Allen
```

The loop above will print the elements of our array. We have used the `length` property to specify the number of times the loop is supposed to run.

## Conclusion

In this article, we learned how to declare and initialize arrays in our Java code. We also saw how to access each element in the array and how to loop through these elements.

Happy Coding!

