---
title: What are the SOLID Principles in Java? Explained With Code Examples
subtitle: ''
author: Anjan Baradwaj
co_authors: []
series: null
date: '2024-06-24T15:45:17.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-solid-principles
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/kozjat-mlsSgJ6LiP4-unsplash.jpg
tags:
- name: Java
  slug: java
- name: solid
  slug: solid
seo_title: null
seo_desc: 'In this article, you''ll learn about the SOLID principles. You''ll gain
  an understanding of each principle along with Java code examples.

  SOLID principles are a set of five design principles used in object-oriented programming.
  Adhering to these princi...'
---

In this article, you'll learn about the SOLID principles. You'll gain an understanding of each principle along with Java code examples.

SOLID principles are a set of five design principles used in object-oriented programming. Adhering to these principles will help you develop robust software. They will make your code more efficient, readable, and maintainable.

SOLID is an acronym that stands for:
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

## Single Responsibility Principle
The single responsibilty principle states that every class must have a single, focused responsibility, a single reason to change.

```java
public class Employee{
  public String getDesignation(int employeeID){ // }
  public void updateSalary(int employeeID){ // }
  public void sendMail(){ // }
}
```

In the above example, the `Employee` class has a few employee class-specific behaviors like `getDesignation` & `updateSalary`. 

Additionally, it also has another method named `sendMail` which deviates from the responsibility of the `Employee` class. 

This behavior is not specific to this class, and having it violates the single responsibility principle. To overcome this, you can move the `sendMail` method to a separate class.

Here's how:

```java
public class Employee{
  public String getDesignation(int employeeID){ // }
  public void updateSalary(int employeeID){ // }
}

public class NotificationService {
    public void sendMail() { // }
}
```

## Open/Closed Principle

According to the open/closed priniciple, components must be open for extension, but, closed for modification. To understand this principle, let us take an example of a class that calculates the area of a shape.

```java
public class AreaCalculator(){
  public double area(Shape shape){
    double areaOfShape;
    if(shape instanceof Square){
        // calculate the area of Square
    } else if(shape instanceof Circle){
        // calculate the area of Circle
    }
    return areaOfShape;
  }
```

The problem with the above example is that if there is a new instance of type `Shape` for which you need to calculate the area in the future, you have to modify the above class by adding another conditional `else-if` block. You will end up doing this for every new object of the `Shape` type.

To overcome this, you can create an interface and have each `Shape` implement this interface. Then, each class can provide its own implementation for calculating the area. This will make your program easily extensible in the future. 

```java
interface IAreaCalculator(){
  double area();
}

class Square implements IAreaCalculator{
  @Override
  public double area(){
    System.out.println("Calculating area for Square");
    return 0.0;
   }
}

class Circle implements IAreaCalculator{
  @Override
  public double area(){
    System.out.println("Calculating area for Circle");
    return 0.0;
   }
}
```

## Liskov Substitution Principle

The Liskov substitution principle states that you must be able to replace a superclass object with a subclass object without affecting the correctness of the program.

```java
abstract class Bird{
   abstract void fly();
}

class Eagle extends Bird {
   @Override
   public void fly() { // some implementation }
}

class Ostrich extends Bird {
   @Override
   public void fly() { // dummy implementation }
}
```

In the above example, the `Eagle` class and the `Ostrich` class both extend the `Bird` class and override the `fly()` method. However, the `Ostrich` class is forced to provide a dummy implementation because it cannot fly, and therefore it does not behave the same way if we replace the `Bird` class object with it. 

This violates the Liskov substitution principle. To address this, we can create a separate class for birds that can fly and have the `Eagle` extend it, while other birds can extend a different class, which will not include any `fly` behavior.

```java
abstract class FlyingBird{
   abstract void fly();
}

abstract class NonFlyingBird{
   abstract void doSomething();
}

class Eagle extends FlyingBird {
   @Override
   public void fly() { // some implementation }
}

class Ostrich extends NonFlyingBird {
   @Override
   public void doSomething() { // some implementation }
}
```

## Interface Segregation Principle

According to the interface segregation principle, you should build small, focused interfaces that do not force the client to implement behavior they do not need.

A straightforward example would be to have an interface that calculates both the area and volume of a shape.

```java
interface IShapeAreaCalculator(){
  double calculateArea();
  double calculateVolume();
}

class Square implements IShapeAreaCalculator{
  double calculateArea(){ // calculate the area }
  double calculateVolume(){ // dummy implementation }
}
```

The issue with this is that if a `Square` shape implements this, then it is forced to implement the `calculateVolume()` method, which it does not need. 

On the other hand, a `Cube` can implement both. To overcome this, we can segregate the interface and have two separate interfaces: one for calculating the area and another for calculating the volume. This will allow individual shapes to decide what to implement.

```java
interface IAreaCalculator {
    double calculateArea();
}

interface IVolumeCalculator {
    double calculateVolume();
}

class Square implements IAreaCalculator {
    @Override
    public double calculateArea() { // calculate the area }
}

class Cube implements IAreaCalculator, IVolumeCalculator {
    @Override
    public double calculateArea() { // calculate the area }

    @Override
    public double calculateVolume() {// calculate the volume }
}
```

## Dependency Inversion Principle 

In the dependency inversion principle, high-level modules should not depend on low-level modules. In other words, you must follow abstraction and ensure loose coupling

```java
public interface Notification {
    void notify();
}

public class EmailNotification implements Notification {
    public void notify() {
        System.out.println("Sending notification via email");
    }
}

public class Employee {
    private EmailNotification emailNotification; 
    public Employee(EmailNotification emailNotification) {
        this.emailNotification = emailNotification;
    }
    public void notifyUser() {
        emailNotification.notify();
    }
}
```

In the given example, the `Employee` class depends directly on the `EmailNotification` class, which is a low-level module. This violates the  dependency inversion principle.

```java
public interface Notification{
  public void notify();
}

public class Employee{
  private Notification notification;
  public Employee(Notification notification){
      this.notification = notification;
  }
  public void notifyUser(){
    notification.notify();
  }
 }
 
 public class EmailNotification implements Notification{
    public void notify(){
        //implement notification via email 
    }
 }
 
 public static void main(String [] args){
    Notification notification = new EmailNotification();
    Employee employee = new Employee(notification);
    employee.notifyUser();
 }
```

In the above example, we have ensured loose coupling. `Employee` is not dependent on any concrete implementation, rather, it depends only on the abstraction (notification interface). 

If we need to change the notification mode, we can create a new implementation and pass it to the `Employee`.

## Conclusion

In conclusion, we've covered the essence of SOLID principles through straightforward examples in this article. 

These principles form the building blocks for developing applications that are highly extensible and reusable.

Let's connect on [LinkedIn](https://www.linkedin.com/in/abaradwaj/)


