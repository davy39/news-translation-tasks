---
title: Java Enum – Enumeration in Java Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-03-25T21:33:55.000Z'
originalURL: https://freecodecamp.org/news/java-enum-enumeration-in-java-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/enum.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "An enumeration (enum for short) in Java is a special data type which contains\
  \ a set of predefined constants. \nYou'll usually use an enum when dealing with\
  \ values that aren't required to change, like days of the week, seasons of the year,\
  \ colors, and ..."
---

An enumeration (enum for short) in Java is a special data type which contains a set of predefined constants. 

You'll usually use an `enum` when dealing with values that aren't required to change, like days of the week, seasons of the year, colors, and so on.

In this article, we'll see how to create an `enum` and how to assign its value other variables. We'll also see how to use an `enum` in `switch` statements or loop through its values. 

## How to Create an Enum in Java

To create an `enum`, we use the `enum` keyword, similar to how you'd create a class using the `class` keyword.  

Here's an example:

```java
enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}
```

In the code above, we created an `enum` called `Colors`. You may notice that the values of this `enum` are all written in uppercase – this is just a general convention. You will not get an error if the values are lowercase.

Each value in an `enum` is separated by a comma.

Next, we're going to create a new variable and assign one of the values of our `enum` to it. 

```java
enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}

public class Main { 
  public static void main(String[] args) { 
  
    Colors red = Colors.RED; 
    
    System.out.println(red); 
    // RED
  } 
}

```

This is similar to initializing any other variable. In the code above, we initialized a `Colors` variable and assigned one of the values of an `enum` to it using the dot syntax: `Colors red = Colors.RED;`. 

Note that we can create our `enum` inside the `Main` class and the code will still work. That is: 

```java
public class Main { 
  enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}
  public static void main(String[] args) { 
  
    Colors red = Colors.RED; 
    
    System.out.println(red); 
  } 
}

```

If we want to get the index number of any of the values, we would have to use the `ordinal()` method. Here is an example: 

```java
enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}

public class Main { 
  public static void main(String[] args) { 
  
    Colors red = Colors.RED; 
    
    System.out.println(red.ordinal()); 
    // 0
  } 
}

```

`red.ordinal()` from the code above returns 0. 

## How to Use an Enum in a Switch Statement

In this section, we'll se how we can use an `enum` in a `switch` statement.

Here is an example:

```java
  public class Main { 
      enum Colors {
      RED,
      BLUE,
      YELLOW,
      GREEN
  }
  public static void main(String[] args) { 
    
    Colors myColor = Colors.YELLOW;

    switch(myColor) {
      case RED:
        System.out.println("The color is red");
        break;
      case BLUE:
         System.out.println("The color is blue");
        break;
      case YELLOW:
        System.out.println("The color is yellow");
        break;
      case GREEN:
        System.out.println("The color is green");
        break;
    }
  } 
}

```

This is a very basic example of how we can use an `enum` in a `switch` statement. We would get "The color is yellow" printed to the console because that is the only `case` that matches the `switch` statement's condition.

## How to Loop Through the Values of an Enum

`enum` in Java has a `values()` method that returns an array of the values of an `enum`. We're going to use a for-each loop to iterate through and print the values of our `enum`. 

Here's how we can do that:

```java
enum Colors {
  RED,
  BLUE,
  YELLOW,
  GREEN
}

public class Main { 
  public static void main(String[] args) { 
      
      for (Colors allColors : Colors.values()) {
      System.out.println(allColors);
      
      /* 
      RED
      BLUE
      YELLOW
      GREEN
      */
    }
    
  } 
}

```

## Conclusion

In this article, we got to know what an `enum` is in Java, how to create it, and how to assign its values to other variables.

We also saw how to use use the `enum` type with a `switch` statement and how we can loop through the values of an `enum`. 

Happy coding!

