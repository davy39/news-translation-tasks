---
title: Abstract Classes in Java Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/abstract-classes-in-java-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d14740569d1a4ca35ca.jpg
tags:
- name: class
  slug: class
- name: Java
  slug: java
- name: object oriented
  slug: object-oriented
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Abstract classes are classes declared with abstract. They can be subclassed
  or extended, but cannot be instantiated. You can think of them as a class version
  of interfaces, or as an interface with actual code attached to the methods.

  For example, say...'
---

Abstract classes are classes declared with `abstract`. They can be subclassed or extended, but cannot be instantiated. You can think of them as a **class version** of interfaces, or as an interface with actual code attached to the methods.

For example, say you have a class `Vehicle` which defines the basic functionality (methods) and components (object variables) that vehicles have in common. 

You cannot create an object of `Vehicle` because a vehicle is itself an abstract, general concept. Vehicles have wheels and motors, but the number of wheels and the size of motors can differ greatly.

You can, however, extend the functionality of the vehicle class to create a `Car` or a `Motorcycle`:

```java
abstract class Vehicle
{
  //variable that is used to declare the no. of wheels in a vehicle
  private int wheels;
  
  //Variable to define the type of motor used
  private Motor motor;
  
  //an abstract method that only declares, but does not define the start 
  //functionality because each vehicle uses a different starting mechanism
  abstract void start();
}

public class Car extends Vehicle
{
  ...
}

public class Motorcycle extends Vehicle
{
  ...
}
```

Remember, you cannot instantiate a `Vehicle` anywhere in your program – instead, you can use the `Car` and `Motorcycle` classes you declared earlier and create instances of those:

```java
Vehicle newVehicle = new Vehicle();    // Invalid
Vehicle car = new Car();  // valid
Vehicle mBike = new Motorcycle();  // valid

Car carObj = new Car();  // valid
Motorcycle mBikeObj = new Motorcycle();  // valid
```

## More information:

* [Learn Functional Programming in Java - Full Course](https://www.freecodecamp.org/news/functional-programming-in-java-course/)
* [Getters and Setters in Java Explained](https://www.freecodecamp.org/news/java-getters-and-setters/)
* [Inheritance in Java Explained](https://www.freecodecamp.org/news/inheritance-in-java-explained/)

