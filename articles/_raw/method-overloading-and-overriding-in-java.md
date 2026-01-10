---
title: Method Overloading vs Method Overriding in Java – What's the Difference?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-17T17:26:47.000Z'
originalURL: https://freecodecamp.org/news/method-overloading-and-overriding-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Method-Overloading-and-Overriding-in-Java-copy.jpeg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "By Mikael Lassa\nIn Java, method overloading and method overriding both\
  \ refer to creating different methods that share the same name. \nWhile the two\
  \ concepts share some similarities, they are distinct notions with markedly different\
  \ use cases. Having ..."
---

By Mikael Lassa

In Java, method overloading and method overriding both refer to creating different methods that share the same name. 

While the two concepts share some similarities, they are distinct notions with markedly different use cases. Having a firm grasp of them is important in building strong foundational Java skills. 

In this post, we'll explore the key rules of method overloading and overriding, as well as the differences between them. 

## What is Method Overloading in Java?

Overloading a method, in simple terms, means creating a different method with the same name in the same class, but with a different parameter list. 

There can be many cases where you might need to handle different types of input for the same operation, and method overloading is one way to handle such cases. 

For example, let's say you want to create a method that performs an addition of two numbers. This calculation is designed to return a number as its output. If your method handles parameters of type `int`, attempting to call it by passing values of type `double` as arguments results in a compilation error. 

For this reason, you might want to overload the method by creating a new version of that method that is able to handle a different type of input (in this case of type `double`): 

```java
public class Calculator {

    public int sum(int a, int b) {
        return a + b;
    }

    public double sum(double a, double b) {
        return a + b;
   }
}
```

In the example above, the `sum()` method is overloaded, because it is defined more than once within the same class, but with a different parameter list. 

A method can also be overloaded by changing the number of parameters. On this basis, the following methods are also legal examples of how the `sum()` method can be overloaded, assuming they are placed within the same class: 

```java
public int sum(int a, int b, int c) {
        return a + b + c;
    }
    
protected void sum() {
        System.out.print("Nothing to sum");
    }
```

Note that, as in some of the examples above, you can also change the return type or the access modifier, but this is not mandatory. 

### Key Rules of Method Overloading

Remember these rules when overloading a method:

* The overloaded and overloading methods must be in the same class (Note: this includes any methods inherited, even implicitly, from a superclass).
* The method parameters must change: either the number or the type of parameters must be different in the two methods.
* The return type can be freely modified.
* The access modifier (`public`, `private`, and so on) can be freely modified.
* Thrown exceptions, if any, can be freely modified.

## What is Method Overriding in Java?

Method overriding refers to redefining a method in a subclass that already exists in the superclass. 

When you call an overridden method using an object of the subclass type, Java uses the method's implementation in the subclass rather than the one in the superclass. For this reason, an understanding of the concept of inheritance in Java is important in order to get a good grasp of method overriding. 

Any subclass can generally override any method from a superclass, unless a method is marked with the `final` or `static` keywords. The overriding method must not change the name and parameter list of the overridden method. 

While not compulsory, it is good practice to use the `@Override` annotation when overriding a method: this annotation will check that the method is being overridden correctly, and will warn you if that's not the case. 

In the following example, you'll see a class `Car` that extends the class `Vehicle`. The `Car` class overrides the `move()` method from the superclass, and this is made explicit by the use of the `@Override` annotation. The two methods are implemented differently in the method body.

```java
class Vehicle {
    public void move() {
        System.out.println("The vehicle is moving");
    }
}

class Car extends Vehicle {
    @Override
    public void move() {
        System.out.println("The car is moving");
    }
}
```

The choice of which version of `move()` will be called is based on the object type the method is being called on. Note that the version of the overridden method that is called is determined at runtime and is based on the object type, not the object reference.

This is illustrated in the following example, particularly in the third call to `move()`: while the method is called on an object reference on type `Vehicle`, the actual object is of type `Car`. The type of the object here is determined at runtime, and the version of the method that is called is therefore the one from the `Car` subclass. 

```java
public static void main(String[] args) {
        
        Vehicle vehicle = new Vehicle();
        vehicle.move();     // Prints: The vehicle is moving

        Car car = new Car();
        car.move();     // Prints: The car is moving

        Vehicle secondVehicle = new Car();
        secondVehicle.move();     // Prints: The car is moving
}
```

### Key Rules of Method Overriding

Remember these rules when overriding a method:

* The parameter list must not change: the overriding method must take the same number and type of parameters as the overridden method – otherwise, you would just be overloading the method.
* The return type must not change (Note: if the method returns an object, a subclass of that object is allowed as the return type).
* The access modifier must be either the same or a less restrictive one (for example, if the overridden method is `protected`, you can declare the overriding method as `public`, but not `private`).
* Thrown checked exceptions, if any, can be removed or reduced by the overriding method. This means that the overriding method can throw the same checked exception as the overridden method, or a subclass of that checked exception, but not a broader exception. This restriction does not apply to unchecked exceptions.

## Conclusion

In this article we explored the main rules of method overloading and method overriding in Java. You saw that the main point of overloading a method is to change its parameter list in order to implement a different behaviour based on the arguments that are passed to it. 

Overriding, on the other hand, refers to re-defining the same method, with the same parameter list, in a subclass in order to tailor its behaviour to the needs of the subclass. 

These concepts are interlinked with some of the core object-oriented programming ideas, such as inheritance and polymorphism, so they're fundamental in order to master Java. They can cause some confusion, especially for beginners, but having a firm understanding of the rules and the uses of these concepts should help developers write more efficient and readable code. 

If you would like to read any of my other articles, you are welcome to check out my [blog](https://medium.com/@mikael.lassa). 






