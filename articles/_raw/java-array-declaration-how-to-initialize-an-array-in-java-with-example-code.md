---
title: Java Array Declaration – How to Initialize an Array in Java with Example Code
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-09T14:34:15.000Z'
originalURL: https://freecodecamp.org/news/java-array-declaration-how-to-initialize-an-array-in-java-with-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/javaArrays.png
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: null
seo_desc: "Arrays are an important part of the fundamental data structures in Java.\
  \ And they are incredibly useful in solving a lot of programming problems. \nWhat\
  \ is an array?\nBy definition, an array is a collection of data of the same type.\
  \ \nAn array is usuall..."
---

Arrays are an important part of the fundamental data structures in Java. And they are incredibly useful in solving a lot of programming problems. 

## What is an array?

By definition, an array is a collection of data of the same type. 

An array is usually declared so you can have multiple values in the same memory – unlike variables where you can only have one value in the memory. 

So, arrays let you create one variable that holds different values together, instead of declaring a variable for each value. 

The position of a particular data point in the array is called its index, while the data itself is called an element.

In this tutorial, I will show you how to declare an array, initialize it, and loop through it with the for loop and enhanced for loop. Then you can start using it in your Java projects.

I will be using the intelliJIDEA IDE to write the code. You can use it if you want, or you can also use any IDE of your choice.

## How to Declare and Intialize an Array in Java

There are two ways you can declare and initialize an array in Java. The first is with the `new` keyword, where you have to initialize the values one by one. The second is by putting the values in curly braces.

### How to initialize an array with the `new` keyword

You can declare the array with the syntax below:

```java
dataType [ ] nameOfArray;
```

`dataType`: the type of data you want to put in the array. This could be a string, integer, double, and so on.
`[ ]`: signifies that the variable to declare will contain an array of values
`nameOfArrary`: The array identifier.

With the above information, you have only declared the array – you still need to initialize it.

The basic syntax for initializing an array in this way looks like this:

```java
dataType [] nameOfArray = new dataType [size]
```

The size is usually expressed with a numberic value. It signifies how many values you want to hold in the array. Its value is immutable, meaning you won’t be able to put more than the number specified as the size in the array. 

You can now go ahead and put values in the array like this: 

```java
package com.kolade;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
   // write your code here
String [] names = new String[3];
names[0] = "Quincy";
names[1] = "Abbey";
names[2] = "Kolade";
   }
}
```

In the code snippet above, I initialized an array of strings called names (the identifier). The size is 3, so it can only hold three values. 

There are 3 indexes in total: 

- The value, `Quincy` is at index `0`
- The value `Abbey` is at index `1`
- The value`Kolade` is at index `2`

Don’t be confused by the numbers 0, 1, 2. Arrays are zero-indexed, so counting starts from 0, not 1.

In the array above, if you add extra data – for example, `names[3] = “Chris”` – you would get an error because you have specified that the array should only contain 3 values. If you want to add more values, you have to increase the size of the array.

![error-1](https://www.freecodecamp.org/news/content/images/2021/09/error-1.png)

To print the array to the console, you can use the inbuilt `toString()` method:

```java
System.out.println(Arrays.toString(names));
```

![names-print](https://www.freecodecamp.org/news/content/images/2021/09/names-print.png)

### 2. How to initialize an array in one line

You can initialize an array in one line with the basic syntax below:

```java
dataType [ ] nameOfArray = {value1, value2, value3, value4}

```

With this method, you don’t need to specify the size of the array, so you can put any number of values you want in it.

Check out the example in the code snippet below:

```java
package com.kolade;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
   // write your code here
     String [] namesTwo = {"Quincy", "Abbey", "Kolade", "Chris", "Kayode"};
  }
}
```

Printing the array to the console shows the values like this:
![names-print-2](https://www.freecodecamp.org/news/content/images/2021/09/names-print-2.png)

## How to Loop Through an Array in Java

You can loop through an array in Java with the for loop and enhanced for loop. With the for loop, you have access to the index of the individual values, but with the enhanced for loop, you don’t.

### How to loop through an array with the `for` loop

In Java, you can use the for loop with the basic syntax below:

```java
for (dataType i = 0; i < nameOfArray.length; i++) {
    //   Code to execute
}
```

You can then loop through the `namesTwo` array like this:

```java
package com.kolade;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
   // write your code here

        String [] namesTwo = {"Quincy", "Abbey", "Kolade", "Chris", "Kayode"};

        for (int i = 0; i < namesTwo.length; i++) {
            System.out.println("Element at index " + i + " : " + namesTwo[i]);
        }
    }
}
``` 

![for-loop](https://www.freecodecamp.org/news/content/images/2021/09/for-loop.png)

### How to loop through an array with the enhanced `for` loop

The enhanced for loop is a cleaner version of the for loop. The downside is that with it, you don’t have access to the index of the individual values in the array.

The basic syntax of the enhanced for loop looks like this: 

```java
for (dataType variable : nameOfArray) {
    // Code to execute
}
```

```java
package com.kolade;

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
   // write your code here

        String [] namesTwo = {"Quincy", "Abbey", "Kolade", "Chris", "Kayode"};

        for (String names : namesTwo) {
            System.out.println(names);
        }
    }
}
```

![enhanced-for-loop](https://www.freecodecamp.org/news/content/images/2021/09/enhanced-for-loop.png)

## Conclusion

In this tutorial, you learned how to declare and initialize an array in two different ways – with the new keyword and using curly braces. 

You also learned how to loop through arrays with the for loop and enhanced for loop, so you don’t just initialize an array and do nothing with it.

Thank you for reading, and keep coding.


