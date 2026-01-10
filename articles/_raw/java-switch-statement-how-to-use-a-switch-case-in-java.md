---
title: Java Switch Statement – How to Use a Switch Case in Java
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-21T17:39:06.000Z'
originalURL: https://freecodecamp.org/news/java-switch-statement-how-to-use-a-switch-case-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/jaye-haych-bPOEB3sy4As-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "You use the switch statement in Java to execute a particular code block\
  \ when a certain condition is met. \nHere's what the syntax looks like:\nswitch(expression)\
  \ {\n  case 1:\n    // code block\n    break;\n  case 2:\n    // code block\n  \
  \  break;\n    case 3..."
---

You use the `switch` statement in Java to execute a particular code block when a certain condition is met. 

Here's what the syntax looks like:

```java
switch(expression) {
  case 1:
    // code block
    break;
  case 2:
    // code block
    break;
    case 3:
    // code block
    break;
  default:
    // code block
}
```

Above, the `expression` in the `switch` parenthesis is compared to each `case`. When the `expression` is the same as the `case`, the corresponding code block in the `case` gets executed. 

If all the cases do not match the `expression`, then the code block defined under the `default` keyword gets executed. 

We use the `break` keyword to terminate the code whenever a certain condition is met (when the `expression` matches with a `case`).

Let's see some code examples.

## How to Use a Switch Case in Java

Take a look at the following code:

```java
class CurrentMonth {
    public static void main(String[] args) {
        
        int month = 6;
        
        switch (month) {
          case 1:
            System.out.println("January");
            break;
          case 2:
            System.out.println("February");
            break;
          case 3:
            System.out.println("March");
            break;
          case 4:
            System.out.println("April");
            break;
          case 5:
            System.out.println("May");
            break;
          case 6:
            System.out.println("June");
            break;
          case 7:
            System.out.println("July");
            break;
          case 8:
            System.out.println("August");
            break;
          case 9:
            System.out.println("September");
            break;
          case 10:
            System.out.println("October");
            break;
          case 11:
            System.out.println("November");
            break;
          case 12:
            System.out.println("December");
            break;
            
            // June
        }
    }
}
```

In the code above, June is printed out. Don't worry about the bulky code. Here's a breakdown to help you understand:

We created an integer called `month` and assigned a value of 6 to it: `int month = 6;`. 

Next, we created a `switch` statement and passed in the `month` variable as a parameter: `switch (month){...}`. 

The value of `month`, which is acting as the expression for the `switch` statement, will be compared with every `case` value in the code. We have case 1 to 12. 

The value of `month` is 6 so it matches with `case` 6. This is why the code in `case` 6 was executed. Every other code block got ignored. 

Here's another example to simplify things:

```java
class Username {
    public static void main(String[] args) {
        
        String username = "John";
        
        switch (username) {
          case "Doe":
            System.out.println("Username is Doe");
            break;
          case "John":
            System.out.println("Username is John");
            break;
          case "Jane":
            System.out.println("Username is Jane");
            break;
            // Username is John
        }
    }
}
```

In the example above, we created a string called `username` which has a value of "John".

In the `switch` statement, `username` is passed in as the expression. We then created three cases – "Doe", "John", and "Jane". 

Out of the three classes, only one matches the value of `username` — "John". As a result, the code block in `case "John"` got executed.

## How to Use the Default Keyword in a Switch Statement

In the examples in the previous section, our code got executed because one `case` matched an `expression`. 

In this section, you'll see how to use the `default` keyword. You can use it as a fallback in situations where none of the cases match the `expression`. 

Here's an example:

```java
class Username {
    public static void main(String[] args) {
        
        String username = "Ihechikara";
        
        switch (username) {
          case "Doe":
            System.out.println("Username is Doe");
            break;
          case "John":
            System.out.println("Username is John");
            break;
          case "Jane":
            System.out.println("Username is Jane");
            break;
          default:
            System.out.println("Username not found!");
            // Username not found!
        }
    }
}
```

The `username` variable in the example above has a value of  "Ihechikara". 

The code block for the `default` keyword will be executed because none of the cases created match the value of `username`. 

## Summary

In this article, we saw how to use the `switch` statement in Java. 

We also talked about the `switch` statement's expression, cases, and default keyword in Java along with their use cases with code examples. 

Happy coding!

