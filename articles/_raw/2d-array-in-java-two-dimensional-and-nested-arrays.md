---
title: 2D Array in Java – Two-Dimensional and Nested Arrays
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-08-10T20:49:04.000Z'
originalURL: https://freecodecamp.org/news/2d-array-in-java-two-dimensional-and-nested-arrays
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/pawel-czerwinski-dYjFmiQb_aE-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: null
seo_desc: "A multidimensional array is simply an array of arrays. You can look it\
  \ as a single container that stores multiple containers. \nIn this article, we'll\
  \ talk two dimensional arrays in Java. You'll see the syntax for creating one, and\
  \ how to add and acce..."
---

A multidimensional array is simply an [array](https://www.freecodecamp.org/news/java-array-how-to-declare-and-initialize-an-array-in-java-example/) of arrays. You can look it as a single container that stores multiple containers. 

In this article, we'll talk two dimensional arrays in Java. You'll see the syntax for creating one, and how to add and access items in a two dimensional array. 

## How to Declare a Two Dimensional Array in Java

To create a two dimensional array in Java, you have to specify the data type of items to be stored in the array, followed by two square brackets and the name of the array. 

Here's what the syntax looks like:

```txt
data_type[][] array_name;
```

Let's look at a code example. 

```java
int[][] oddNumbers = { {1, 3, 5, 7}, {9, 11, 13, 15} };
```

Don't worry if you're yet to understand what's going on above. In the next section, you'll learn more about how two dimensional arrays work and how to access items stored in them. 

## How to Access Items in a Two Dimensional Array in Java

We can access items in a two dimensional using two square brackets. 

The first denotes the array from which we want to access the items while the second denotes the index of the item we want to access. 

Let's simplify the explanation above with an example:

```java
int[][] oddNumbers = { {1, 3, 5, 7}, {9, 11, 13, 15} };

System.out.println(oddNumbers[0][0]);
// 1
```

In the example above, we have two arrays in the `oddNumbers` array – `{1, 3, 5, 7}` and `{9, 11, 13, 15}`. 

The first array — `{1, 3, 5, 7}` — is denoted using 0. 

The second array — `{9, 11, 13, 15}` — is denoted using 1. 

First array is 0, second is 1, third is 2, and so on. 

So to access an item from the first array, we assigned 0 to the first square bracket. Since we were trying to access the first item in the array, we used its index which is zero: `oddNumbers[0][0]`. 

Let's break it down even further. 

Here's the code to access items: `oddNumbers[?][?]`

I've put question marks in both square brackets – we'll fill them in as we progress. 

So let's say we want to access an item in the second array which is denoted using 1, our code will look like this: `oddNumbers[1][?]`.

Now that we're in the second array (`{9, 11, 13, 15}`) let's try to access an item in it. Just like regular arrays, each items has an index starting from zero. 

So to access `13` which is the third item, we pass its index number to the second square bracket: `oddNumbers[1][2]`. 

In the next section, we'll start with a fresh example. 

## How to Access Items in a Two Dimensional Array in Java Example

```java
int[][] oddNumbers = { {1, 3, 5, 7}, {9, 11, 13, 15}, {17, 19, 21, 23} };
```

The objective here is to access 21 in the third array. Our access code still has question marks: `oddNumbers[?][?]`. 

We'll start by giving the first question mark a value which points to the particular array to access. 

Array 0 => `{1, 3, 5, 7}`  
Array 1 => `{9, 11, 13, 15}`  
Array 2 => `{17, 19, 21, 23}`

The number we're looking for is in the third array with an array index of 2. So we've found the value for the first square bracket: `oddNumbers[2][?]`

The second square bracket's value will point to the actual item to be accessed. To do that, we have to specify the index number of the item. Here are the indexes in that array:

17 => Index 0  
19 => Index 1  
21 => Index 2  
23 => Index 3

21 has an index of 2 so we can go on and add that to the second square bracket: `oddNumbers[2][2]`. When you print that to the console, you'll get 21 printed out. 

Here's what the code looks like:

```java
int[][] oddNumbers = { {1, 3, 5, 7}, {9, 11, 13, 15}, {17, 19, 21, 23} };

System.out.println(oddNumbers[2][2]);
// 21
```

You can loop through all the items in a two dimensional array by using a nested loop. Here's an example:

```java
int[][] oddNumbers = { {1, 3, 5, 7}, {9, 11, 13, 15}, {17, 19, 21, 23} };

for(int i = 0; i < oddNumbers.length; i++){
    for(int j = 0; j < oddNumbers[i].length; j++){
        System.out.println(oddNumbers[i][j]);
    }   
}

// 1
// 3
// 5
// 7
// 9
// 11
// 13
// 15
// 17
// 19
// 21
// 23
```

The code above prints out all the items in the `oddNumbers` array. 

## Summary

In this article, we talked about two dimensional arrays in Java.

We saw the syntax for creating two dimensional arrays. We also saw examples that showed how to access items stored in them. 

Lastly, we saw how to loop through and print the items in a two dimensional array.

Happy coding!

