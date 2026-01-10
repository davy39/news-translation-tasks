---
title: Enhanced For Loops in Java – How to Use ForEach Loops on Arrays
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-02-17T00:55:10.000Z'
originalURL: https://freecodecamp.org/news/enhanced-for-loops-in-java-how-to-use-foreach-loops-on-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/java-enhanced-loop.png
tags:
- name: Java
  slug: java
- name: Loops
  slug: loops
seo_title: null
seo_desc: "You can use enhanced loops in Java to achieve the same results as a for\
  \ loop. An enhanced loop is also known as a for-each loop in Java. \nEnhanced loops\
  \ simplify the way you create for loops. They are mostly used to iterate through\
  \ an array or collec..."
---

You can use enhanced loops in Java to achieve the same results as a [`for` loop](https://www.freecodecamp.org/news/java-for-loop-example/). An enhanced loop is also known as a `for-each` loop in Java. 

Enhanced loops simplify the way you create `for` loops. They are mostly used to iterate through an array or collection of variables.

In this tutorial, you'll learn the syntax and how to use the `for-each` loop (enhanced loop) in Java. 

## Java For-Each Loop Syntax

Here's what the syntax of a `for-each` loop in Java looks like:

```java
for(dataType variable : array) {
    // code to be executed
}
```

In the syntax above:

* **dataType** denotes the data type of the **array**.
* **variable** denotes a variable assigned to each element in the array during the iteration (you'll understand this through the examples that follow).
* **array** denotes the array to be looped through.

## Java For-Each Loop Example

Let's take a look at some examples to help you understand how a `for-each` loop works. 

### Java For-Each Loop Example #1

```java
class ForEachExample {
    public static void main(String[] args) {
        
        int[] even_numbers = { 2, 4, 6, 8 };
        
        for(int number : even_numbers){
           System.out.println(number);
           // 2
           // 4
           // 6
           // 8
        }
        
    }
}
```

In the code above, we created an array called `even_numbers`. 

To loop through and print all the numbers in the array, we made use of a `for-each` loop: `for(int number : even_numbers){...}`. 

In the parenthesis for the loop, we created an integer variable called `number` which would be used to loop through the `even_numbers` array. 

So, for:

#### Iteration #1

`number` = first element in the array (2). This gets printed out.

#### Iteration #2

`number` = second element in the array (4). This current value gets printed out. 

#### Iteration #3

`number` = third element in the array (6). This current value gets printed out. 

#### Iteration #4

`number` = fourth element in the array (8). This current value gets printed out. 

The value of `number` keeps changing to the current index during the iteration process until it gets to the end of the array. After each index is printed out, it moves to the next index. 

You can also see it this way: "For every `number` in the `even_numbers` array, print `number`)".

### Java For-Each Loop Example #2

```java
class ForEachExample {
    public static void main(String[] args) {
        
        int[] even_numbers = { 2, 4, 6, 8 };
        
        for(int number : even_numbers){
            number = number*2;
            System.out.println(number);
        }
        
    }
}
```

In the code above, we're multiplying the value of each element by two using the `number` variable: `number = number*2;`.

The process here is the same with the last example. When `number` becomes an element in the array, it doubles the element's value and prints it to the console.

## Summary

You can use `for-each` loops in Java to iterate through elements of an array or collection. 

They simplify how you create `for` loops. For instance, the syntax of a `for` loop requires that you create a variable, a condition that specifies when the loop should terminate, and an increment/decrement value. 

With `for-each` loops, all you need is a variable and the array to be looped through. 

But this doesn't mean that you should always go for `for-each` loops. 

`for` loops give you more control over what happens during the iteration process – controlling and tracking what happens at every index or some indexes. 

On the other hand, `for-each` loops can be used when you have no use for tracking each index. The code just runs through for every element in the array. 

You can learn more about `for` loops in Java by [reading this article](https://www.freecodecamp.org/news/java-for-loop-example/).

Happy coding!

