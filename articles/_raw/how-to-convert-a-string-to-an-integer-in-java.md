---
title: String to Int in Java – How to Convert a String to an Integer
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-11-03T22:02:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-an-integer-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/marcel-eberle-rendLSpkDtY-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "When working with a programming language, you may want to convert strings\
  \ to integers. An example would be performing a mathematical operation using the\
  \ value of a string variable. \nIn this article, you'll learn how to convert a string\
  \ to an integer ..."
---

When working with a programming language, you may want to convert strings to integers. An example would be performing a mathematical operation using the value of a string variable. 

In this article, you'll learn how to convert a string to an integer in Java using two methods of the `Integer` class — `parseInt()` and `valueOf()`.

## How to Convert a String to an Integer in Java Using `Integer.parseInt`

The `parseInt()` method takes the string to be converted to an integer as a parameter. That is:

```txt
Integer.parseInt(string_varaible)
```

Before looking at an example of its usage, let's see what happens when you add a string value and an integer without any sort of conversion:

```java
class StrToInt {
    public static void main(String[] args) {
        String age = "10";
        
        System.out.println(age + 20);
        // 1020
    }
}
```

In the code above, we created an `age` variable with a string value of "10". 

When added to an integer value of 20, we got 1020 instead of 30. 

Here's a quick fix using the `parseInt()` method:

```java
class StrToInt {
    public static void main(String[] args) {
        String age = "10";
        
        int age_to_int = Integer.parseInt(age);
        
        System.out.println(age_to_int + 20);
        // 30
    }
}
```

In order to convert the `age` variable to an integer, we passed it as a parameter to the `parseInt()` method — `Integer.parseInt(age)` — and stored it in a variable called `age_to_int`. 

When added to another integer, we got a proper addition: `age_to_int + 20`. 

## How to Convert a String to an Integer in Java Using `Integer.valueOf`

The `valueOf()` methods works just like the `parseInt()` method. It takes the string to be converted to an integer as its parameter. 

Here's an example:

```java
class StrToInt {
    public static void main(String[] args) {
        String age = "10";
        
        int age_to_int = Integer.valueOf(age);
        
        System.out.println(age_to_int + 20);
        // 30
    }
}
```

The explanation for the code above is the same as the last section:

* We passed the string as a parameter to `valueOf()`: `Integer.valueOf(age)`. It was stored in a variable called `age_to_int`.
* We then added 20 to the variable created: `age_to_int + 20`. The resulting value was 30 instead of 1020.

## Summary

In this article, we talked about converting strings to integers in Java. 

We saw how to convert a string to an integer in Java using two methods of the `Integer` class — `parseInt()` and `valueOf()`.

Happy coding!

