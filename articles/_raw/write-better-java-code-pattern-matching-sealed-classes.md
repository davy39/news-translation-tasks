---
title: How to Write Better Java Code using Pattern Matching and Sealed Classes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-11T15:48:42.000Z'
originalURL: https://freecodecamp.org/news/write-better-java-code-pattern-matching-sealed-classes
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/Pattern-Matching.png
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "By Sameer Shukla\nThis article explores how you can improve your Java code\
  \ quality using Pattern Matching and Sealed Classes. \nJava Pattern Matching allows\
  \ you to write more concise and readable code when working with complex data structures.\
  \ It simpl..."
---

By Sameer Shukla

This article explores how you can improve your Java code quality using Pattern Matching and Sealed Classes. 

Java Pattern Matching allows you to write more concise and readable code when working with complex data structures. It simplifies extracting data from data structures and performing operations on them. 

Let's dive in and learn more about pattern matching and sealed classes.

## What is Pattern Matching in Java?

Pattern Matching matches a value against a pattern that includes variables and conditions. If the value matches the pattern, the corresponding parts of the value are bound to the variables in the pattern. This allows for more readable and intuitive code. 

There are two types of pattern matching: traditional and modern. Let's see the differences between the two in the following sections.

### Traditional Pattern Matching

In traditional pattern matching, the `switch` statement is extended to support pattern matching by adding the `case` keyword with a pattern argument. The `switch` statement can match against a primitive type, wrappers, enums, and strings.

For example:

```java
private static void printGreetingBasedOnInput(String input){
        switch (input){
            case "hello":
                System.out.println("Hi There");
                break;
            case "goodbye":
                System.out.println("See you Later!");
                break;
            case "thank you":
                System.out.println("You are welcome");
                break;
            default:
                System.out.println("I don't understand");
                break;
        }
    }
```

The Java method `printGreetingBasedOnInput` takes an `input` string and prints a corresponding greeting message based on its value using a switch-case statement. It covers cases for "hello," "goodbye," and "thank you," providing appropriate responses, and defaults to "I don't understand" for any other inputs.

### Modern Pattern Matching

In modern pattern matching, the `switch` statement can match against a variety of patterns like any type of objects, enums, or primitives. The `case` keyword is used to specify the pattern to match against.

```java
private static void printGreetingBasedOnInput(String input){
        switch (input){
            case "hello" -> System.out.println("Hi There");
            case "goodbye" -> System.out.println("See you Later!");
            case "thank you" -> System.out.println("You are welcome");
            default -> System.out.println("I don't understand");
        }
    }
```

This code snippet uses a more concise syntax. It simplifies the code by directly specifying the action to perform for each case label. 

Before Java 16, we needed to check the object's type and then explicitly cast it to a variable. The enhanced `instanceof` operator introduced in Java 16 can both verify the type and perform an implicit cast to a variable, like in the example below: 

```java
private static void printType(Object input){
        switch (input) {
            case Integer i -> System.out.println("Integer");
            case String s -> System.out.println("String!");
            default -> System.out.println("I don't understand");
        }
    }
```

The enhancement of `instanceof` becomes particularly valuable when working with pattern guards. Pattern guards are a way to make case statements in Java pattern matching more specific by including boolean expressions. 

This allows for more fine-grained control over how patterns are matched and can make code more readable and expressive.

```java
private static void printType(Object input){                                                 
    switch (input) {                                                                         
        case Integer i && i > 10 -> System.out.println("Integer is greater than 10");        
        case String s && !s.isEmpty()-> System.out.println("String!");                       
        default -> System.out.println("Invalid Input");                                      
    }                                                                                        
}                                                                                            
```

Based on the examples shown above, you can hopefully see that Java pattern matching offers various benefits:

* It improves code readability by allowing for efficient matching of values against patterns and extracting data.
* It reduces code duplication by handling different cases with a single piece of code.
* It enhances type safety by enabling the matching of values against specific types.
* Pattern guards can be used within cases to further enhance code readability and maintainability.

## What Are Sealed Classes in Java?

Sealed classes allow developers to restrict the set of classes that can extend or implement a given class or interface. 

Sealed classes provide a way to create a hierarchy of classes or interfaces that can be extended or implemented by only a specified set of classes.

For example:

```java
public sealed class Result permits Success, Failure {
    protected String response;

    public String message(){
        return response;
    }
}

public final class Success extends Result {

    @Override
    public String message() {
        return "Success!";
    }
}

public final class Failure extends Result {

    @Override
    public String message() {
        return "Failure!";
    }
}

```

In this example, we've defined a sealed class called `Result` which can be extended by either `Success` or `Failure` classes. 

Any other class that attempts to extend `Result` will result in a compilation error.

This provides a way to restrict the set of classes that can be used to extend `Result`, making the code more maintainable and extensible.

### A few important points to keep in mind:

* If a subclass wants to be a permitted subclass of a sealed class in Java, it must be defined in the same package as the sealed class. If the subclass is not defined in the same package, a compilation error will occur.
* If a subclass is to be permitted to extend a sealed class in Java, it must have one of three modifiers: final, sealed, or non-sealed.
* A sealed subclass must define the same or more restrictive set of permitted subclasses as its sealed superclass. Sealed subclasses must be either final or sealed. Non-sealed subclasses are not allowed as permitted subclasses of a sealed superclass and all permitted subclasses must belong to the same package as the sealed superclass.

## How to Combine Java Pattern Matching and Sealed Classes

You can use sealed classes and their permitted subclasses in switch statements with pattern matching. 

This can make the code more concise and easier to read. Here's an example:

```java
private static String checkResult(Result result){                                     
    return switch (result) {                                                          
        case Success s -> s.message();                                                
        case Failure f -> f.message();                                                
        default -> throw new IllegalArgumentException("Unexpected Input: " + result); 
    };                                                                                
}                                                                                     
```

In the case of sealed classes, the compiler requires a default branch in pattern matching to ensure that all possible cases are covered. 

Since sealed classes have a fixed set of permitted subclasses, it is possible to cover all cases with a finite number of case statements.

If a default branch is not included, it's possible to add a new subclass to the hierarchy in the future, which would not be covered by the existing case statements. This would result in a runtime error, which could be difficult to debug.

By requiring a default branch, the compiler ensures that the code is complete and covers all possible cases, even if new subclasses are added to the sealed class hierarchy in the future. 

This helps to prevent runtime errors and makes the code more robust and maintainable. 

If we modify the `Result` class to include a new subclass called `Pending` and we have not included that in our pattern matching, it will be covered by the default branch.

## What is a Sealed Interface in Java?

When working with a Sealed Interface in Java, the compiler will not require a default branch in pattern matching if all cases are covered.

In case a branch is missing, the compiler will require a default branch to ensure that all possible cases are handled. 

We are always required to include the default branch when working with Sealed Classes. Here's a code example:

```java
public sealed interface OtherResult permits Pending, Timeout {
    void message();
}

public final class Pending implements OtherResult{
    @Override
    public void message() {
        System.out.println("Pending!");
    }
}

public final class Timeout implements OtherResult{
    @Override
    public void message() {
        System.out.println("Timeout!");
    }
}

private static void checkResult(OtherResult result){
        switch (result) {
            case Pending p -> p.message();
            case Timeout t -> t.message();
        };
    }

```

## Conclusion

Here are some key takeaways of using Pattern Matching and Sealed Classes in Java code:

* **Improved readability**: Pattern Matching and Sealed Classes can make code more expressive and easier to read, since they allow for more concise and intuitive syntax.
* **Greater control over class hierarchies**: Sealed Classes provide a way to control class hierarchies and ensure that only permitted subclasses can be used. This can improve code safety and maintainability.
* **Implicit type safety**: Pattern Matching and Sealed Classes provide implicit type safety, which can reduce the risk of runtime errors and make code easier to maintain.
* **Reduced code duplication**: Pattern Matching and Sealed Classes can reduce code duplication by allowing different cases to be handled in a single piece of code.
* **Better code organization:** Sealed Classes can help to organize code and reduce the complexity of class hierarchies by grouping related classes together.
* **Improved maintainability:** Pattern Matching and Sealed Classes can improve the maintainability of code by making it easier to understand and update, which can save time and effort in the long run.

Thank you so much for reading.

