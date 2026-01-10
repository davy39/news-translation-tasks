---
title: Int to String in Java – How to Convert an Integer into a String
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-01-05T15:57:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-integer-to-string-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/marcel-eberle-rendLSpkDtY-unsplash--1-.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "You can convert variables from one data type to another in Java using different\
  \ methods. \nIn this article, you'll learn how to convert integers to strings in\
  \ Java in the following ways:\n\nUsing the Integer.toString() method. \nUsing the\
  \ String.valueOf(..."
---

You can convert variables from one data type to another in Java using different methods. 

In this article, you'll learn how to convert integers to strings in Java in the following ways:

* Using the `Integer.toString()` method. 
* Using the `String.valueOf()` method. 
* Using the `String.format()` method.
* Using the `DecimalFormat` class.

## How to Convert an Integer to a String in Java Using `Integer.toString()`

The `Integer.toString()` method takes in the integer to be converted as a parameter. Here's what the syntax looks like:

```
Integer.toString(INTEGER_VARIABLE)
```

Here's an example:

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        String AGE_AS_STRING = Integer.toString(age);
        
        System.out.println("The child is " + AGE_AS_STRING + " years old");
        // The child is 2 years old
    }
}
```

In the example above, we created an integer – `age` – and assigned a value of 2 to it. 

To convert the `age` variable to a string, we passed it as a parameter to the `Integer.toString()` method: `Integer.toString(age)`. 

We stored this new string value in a string variable called `AGE_AS_STRING`. 

We then concatenated the new string variable with other strings: `"The child is " + AGE_AS_STRING + " years old"`. 

But, would an error be raised if we just concatenated the age variable to these other strings without any sort of conversion? 

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        System.out.println("The child is " + age + " years old");
        // The child is 2 years old
    }
}
```

The output above is the same as the example where we had to convert the integer to a string. 

So how do we know if the type conversion actually worked? 

We can check variable types using the Java `getClass()` object. That is: 

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        String AGE_AS_STRING = Integer.toString(age);
        
        
        System.out.println(((Object)age).getClass().getSimpleName());
        // Integer
        
        System.out.println(AGE_AS_STRING.getClass().getSimpleName());
        // String
    }
}
```

Now we can verify that when the `age` variable was created, it was an `Integer`, and after type conversion, it became a `String`. 

## How to Convert an Integer to a String in Java Using `String.valueOf()`

The `String.valueOf()` method also takes the variable to be converted to a string as its parameter. 

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        String AGE_AS_STRING = String.valueOf(age);
        
        System.out.println("The child is " + AGE_AS_STRING + " years old");
        // The child is 2 years old
    }
}
```

The code above is similar to that in the last section: 

* We created an integer called `age`. 
* We passed the `age` integer as a parameter to the `String.valueOf()` method: `String.valueOf(age)`. 

You can also check to see if the type conversion worked using the `getClass()` object: 

```java
System.out.println(((Object)age).getClass().getSimpleName());
// Integer
        
System.out.println(AGE_AS_STRING.getClass().getSimpleName());
// String
```

## How to Convert an Integer to a String in Java Using `String.format()`

The `String.format()` method takes in two parameters: a format specifier and the variable to be formatted. 

Here's an example: 

```java
class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        String AGE_AS_STRING = String.format("%d", age);
        
        System.out.println("The child is " + AGE_AS_STRING + " years old");
        // The child is 2 years old
        
    }
}

```

In the example above, we passed in two parameters to the `String.format()` method: `"%d"` and `age`.

`"%d"` is a format specifier which denotes that the variable to be formatted is an integer. 

`age`, which is the second parameter, will be converted to a string and stored in the `AGE_AS_STRING` variable. 

You can also check the variable types before and after conversion: 

```java
System.out.println(((Object)age).getClass().getSimpleName());
// Integer
        
System.out.println(AGE_AS_STRING.getClass().getSimpleName());
// String
```

## How to Convert an Integer to a String in Java Using `DecimalFormat`

The `DecimalFormat` class is used for formatting decimal numbers in Java. You can use it in different ways, but we'll be using it to convert an integer to a string. 

Here's an example:

```java
import java.text.DecimalFormat;

class IntToStr {
    public static void main(String[] args) {
        
        int age = 2;
        
        DecimalFormat DFormat = new DecimalFormat("#");
        
        
        String AGE_AS_STRING = DFormat.format(age);
        
        System.out.println("The child is " + AGE_AS_STRING + " years old");
        // The child is 2 years old
        
        
        System.out.println(((Object)age).getClass().getSimpleName());
        // Integer
        
        System.out.println(AGE_AS_STRING.getClass().getSimpleName());
        // String
        
    }
}
```

Let's break the code down:

* To be able to use the `DecimalFormat` class in the example above, we imported it: `import java.text.DecimalFormat;`. 
* We created the integer `age` variable.
* We then created a new object of the `DecimalFormat` class called `DFormat`. 
* Using the object's `format()` method, we converted `age` to a string: `DFormat.format(age);`. 

## Summary

In this article, we talked about converting integers to strings in Java. 

We saw examples that showed how to use three different methods – `Integer.toString()`, `String.valueOf()`, `String.format()` — and the `DecimalFormat` class to convert variables from integers to strings. 

Each example showed how to check the data type of a variable before and after conversion. 

Happy coding!

