---
title: 'Object-Oriented Programming Principles  in Java:  OOP Concepts for Beginners'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-01T12:46:39.000Z'
originalURL: https://freecodecamp.org/news/java-object-oriented-programming-system-principles-oops-concepts-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Love-Home.png
tags:
- name: Java
  slug: java
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: 'By Thanoshan MV


  Object-oriented programming offers a sustainable way to write spaghetti code. It
  lets you accrete programs as a series of patches.― Paul Graham


  Fundamentals of object-oriented programming

  Object-oriented programming is a programming...'
---

By Thanoshan MV

> _Object-oriented programming offers a sustainable way to write spaghetti code. It lets you accrete programs as a series of patches._  
> _― Paul Graham_

## Fundamentals of object-oriented programming

Object-oriented programming is a programming paradigm where everything is represented as an object.

Objects pass messages to each other. Each object decides what to do with a received message. OOP focuses on each object’s states and behaviors.

### What Are Objects?

**An object is an entity that has states and behaviors.**

For example, dog, cat, and vehicle. To illustrate, a dog has states like age, color, name, and behaviors like eating, sleeping, and running.

State tells us how the object looks or what properties it has.

Behavior tells us what the object does.

We can actually represent a real world dog in a program as a software object by defining its states and behaviors.

Software objects are the actual representation of real world objects. Memory is allocated in RAM whenever creating a logical object.

An object is also referred to an instance of a class. Instantiating a class means the same thing as creating an object.

The important thing to remember when creating an object is: the reference type should be the **same type** or a **super type** of the object type. We’ll see what a reference type is later in this article.

### What Are Classes?

**A class is a template or blueprint from which objects are created.**

Imagine a class as a cookie-cutter and objects as cookies.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/cookie-cutter.jpg)
_Figure 1: Illustrates class and object relationship through cookie-cutter and cookies. [Source](https://www.piqsels.com/en/public-domain-photo-sswme" rel="noopener)._

Classes define states as instance variables and behaviors as instance methods.

Instance variables are also known as member variables.

Classes don't consume any space.

To give you an idea about classes and objects, let's create a Cat class that represents states and behaviors of real world Cat.

```java
public class Cat {
    /*
    Instance variables: states of Cat
     */
    String name;
    int age;
    String color;
    String breed;

    /*
    Instance methods: behaviors of Cat
     */
    void sleep(){
        System.out.println("Sleeping");
    }
    void play(){
        System.out.println("Playing");
    }
    void feed(){
        System.out.println("Eating");
    }

}
```

Now we have successfully defined a template for Cat. Let’s say we have two cats named Thor and Rambo.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Russian-Blue_01.jpg)
_Figure 2: Thor is sleeping. [Source](https://www.petfinder.com/cat-breeds/collections/cutest-cat-breeds/" rel="noopener)_

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Maine-Coon_02.jpg)
_Figure 3: Rambo is playing. [Source](https://www.petfinder.com/cat-breeds/collections/cutest-cat-breeds/" rel="noopener)_

How can we define them in our program?

First, we need to create two objects of the Cat class.

```java
public class Main {
    public static void main(String[] args) {
       Cat thor = new Cat();
       Cat rambo = new Cat();
    }
}
```

Next, we’ll define their states and behaviors.

```java
public class Main {

    public static void main(String[] args) {
       /*
       Creating objects
        */
       Cat thor = new Cat();
       Cat rambo = new Cat();

       /*
       Defining Thor cat
        */
       thor.name = "Thor";
       thor.age = 3;
       thor.breed = "Russian Blue";
       thor.color = "Brown";

       thor.sleep();

       /*
       Defining Rambo cat
        */
       rambo.name = "Rambo";
       rambo.age = 4;
       rambo.breed = "Maine Coon";
       rambo.color = "Brown";

       rambo.play();
    }

}
```

Like the above code examples, we can define our class, instantiate it (create objects) and specify the states and behaviors for those objects. 

Now, we have covered the basics of object-oriented programming. Let's move on to the principles of object-oriented programming. 

## Principles of object-oriented programming

These are the four main principles of the object-oriented programming paradigm. Understanding them is essential to becoming a successful programmer.

1. Encapsulation
2. Inheritance
3. Abstraction
4. Polymorphism

Now let's look at each in more detail.

## Encapsulation

**Encapsulation is a process of wrapping code and data together into a single unit.**

It's just like a capsule that contains a mix of several medicines, and is a technique that helps keep instance variables protected.

This can be achieved by using `private` access modifiers that can’t be accessed by anything outside the class. In order to access private states safely, we have to provide public getter and setter methods. (In Java, these methods should follow JavaBeans naming standards.)

Let’s say there is a record shop that sells music albums of different artists and a stock keeper who manages them.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/classDiagramWithoutEncapsulation.png)
_Figure 4: Class diagram without encapsulation_

If you look at figure 4, the `StockKeeper` class can access the `Album` class’s states directly as `Album` class’s states are set to `public`.

What if the stock keeper creates an album and sets states to negative values? This can be done intentionally or unintentionally by a stock keeper.

To illustrate, let’s see a sample Java program that explains the above diagram and statement.

Album class:

```java
public class Album {
    public String name;
    public String artist;
    public double price;
    public int numberOfCopies;
    public void sellCopies(){
        if(numberOfCopies > 0){
            numberOfCopies--;
            System.out.println("One album has sold!");
        }
        else{
            System.out.println("No more albums available!");
        }
    }
    public void orderCopies(int num){
        numberOfCopies += num;
    }
}
```

StockKeeper class:

```java
public class StockKeeper {
    public String name;
    public StockKeeper(String name){
        this.name = name;
    }
    public void manageAlbum(Album album, String name, String artist, double price, int numberOfCopies){
      /*
       Defining states and behaviors for album
       */
        album.name = name;
        album.artist = artist;
        album.price = price;
        album.numberOfCopies = numberOfCopies;

       /*
       Printing album details
        */
        System.out.println("Album managed by :"+ this.name);
        System.out.println("Album details::::::::::");
        System.out.println("Album name : " + album.name);
        System.out.println("Album artist : " + album.artist);
        System.out.println("Album price : " + album.price);
        System.out.println("Album number of copies : " + album.numberOfCopies);
    }
}
```

Main class:

```java
public class Main {
    public static void main(String[] args) {
       StockKeeper johnDoe = new StockKeeper("John Doe");
       /*
       Stock keeper creates album and assigns negative values for price and number of copies available
        */
       johnDoe.manageAlbum(new Album(), "Slippery When Wet", "Bon Jovi", -1000.00, -50);
    }
}
```

Output:

```java
Album managed by :John Doe
Album details::::::::::
Album name : Slippery When Wet
Album artist : Bon Jovi
Album price : -1000.0
Album number of copies : -50
```

The album’s price and number of copies can’t be negative values. How can we avoid this situation? This is where we use encapsulation.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/classDiagramWithEncapsulation-1.png)
_Figure 5: Class diagram with encapsulation_

In this scenario, we can block the stock keeper from assigning negative values. If they attempt to assign negative values for the album’s price and number of copies, we’ll assign them as 0.0 and 0.

Album class:

```java
public class Album {
    private String name;
    private String artist;
    private double price;
    private int numberOfCopies;
    public void sellCopies(){
        if(numberOfCopies > 0){
            numberOfCopies--;
            System.out.println("One album has sold!");
        }
        else{
            System.out.println("No more albums available!");
        }
    }
    public void orderCopies(int num){
        numberOfCopies += num;
    }
   public String getName() {
      return name;
   }
   public void setName(String name) {
      this.name = name;
   }
   public String getArtist() {
      return artist;
   }
   public void setArtist(String artist) {
      this.artist = artist;
   }
   public double getPrice() {
      return price;
   }
   public void setPrice(double price) {
      if(price > 0) {
         this.price = price;          
      }
      else {
         this.price = 0.0;
      }
   }
   public int getNumberOfCopies() {
      return numberOfCopies;
   }
   public void setNumberOfCopies(int numberOfCopies) {
      if(numberOfCopies > 0) {
         this.numberOfCopies = numberOfCopies;        
      }
      else {
         this.numberOfCopies = 0;
      }
   }
}
```

StockKeeper class:

```java
public class StockKeeper {
    private String name;
    StockKeeper(String name){
        setName(name);
    }
    public void manageAlbum(Album album, String name, String artist, double price, int numberOfCopies){
         /*
          Defining states and behaviors for album
          */
        album.setName(name);
        album.setArtist(artist);
        album.setPrice(price);
        album.setNumberOfCopies(numberOfCopies);
          /*
          Printing album details
           */
        System.out.println("Album managed by :"+ getName());
        System.out.println("Album details::::::::::");
        System.out.println("Album name : " + album.getName());
        System.out.println("Album artist : " + album.getArtist());
        System.out.println("Album price : " + album.getPrice());
        System.out.println("Album number of copies : " + album.getNumberOfCopies());
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}
```

Main class:

```java
public class Main {
    public static void main(String[] args) {
       StockKeeper johnDoe = new StockKeeper("John Doe");
       /*
       Stock keeper creates album and assigns negative values for price and number of copies available
        */
       johnDoe.manageAlbum(new Album(), "Slippery When Wet", "Bon Jovi", -1000.00, -50);
    }
}
```

Output:

```java
Album managed by :John Doe
Album details::::::::::
Album name : Slippery When Wet
Album artist : Bon Jovi
Album price : 0.0
Album number of copies : 0
```

With encapsulation, we’ve blocked our stock keeper from assigning negative values, meaning we have control over the data.

### Advantages of encapsulation in Java

1. We can make a class **read-only** or **write-only**: for a read-only class, we should provide only a getter method. For a write-only class, we should provide only a setter method.
2. Control over the data: we can control the data by providing logic to setter methods, just like we restricted the stock keeper from assigning negative values in the above example.
3. Data hiding: other classes can’t access private members of a class directly.

## Inheritance 

Let’s say that the record shop we discussed above also sells Blu-ray movies.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/classDiagramForMovie.png)
_Figure 6: Movie, StockKeeper class diagram_

As you can see in the above diagram, there are many common states and behaviors (common code) between `Album` and `Movie`.

When implementing this class diagram into code, are you going to write (or copy & paste) the entire code for `Movie`? If you do, you are repeating yourself. How can you avoid code duplication?

This is where we use inheritance.

**Inheritance is a mechanism in which one object acquires all the states and behaviors of a parent object.**

Inheritance uses a parent-child relationship (IS-A relationship).

### So what exactly is inherited?

**Visibility/access modifiers** impact what gets inherited from one class to another.

In Java, as a **rule of thumb** we make instance variables `private` and instance methods `public` .

In this case, we can safely say that the following are inherited:

1. public instance methods.
2. private instance variables (private instance variables can be accessed only through public getter and setter methods).

### Types of Inheritance in Java

There are five types of inheritance in Java. They are single, multilevel, hierarchical, multiple, and hybrid.

Class allows single, multilevel and hierarchical inheritances. Interface allows multiple and hybrid inheritances.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/InheritanceTypes.jpg)
_Figure 7: Java inheritance types_

A class can extend only one class however it can implement any number of interfaces. An interface can extend more than one interfaces. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/inheritanceKeywords.jpg)
_Figure 8: Explains inheritance keywords._

### Relationships

**I. IS-A relationship**

An IS-A relationship refers to inheritance or implementation.

#### a. Generalization

Generalization uses an IS-A relationship from a specialization class to generalization class.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/generalization.jpg)
_Figure 9: Generalization diagram_

#### II. HAS-A relationship

An instance of one class HAS-A reference to an instance of another class.

#### a. Aggregation

In this relationship, the existence of class A and B are not dependent on each other.

For this aggregation part, we going to see an example of the `Student` class and the `ContactInfo` class. 

```java
class ContactInfo {
    private String homeAddress;
    private String emailAddress;
    private int telephoneNumber; //12025550156
}
public class Student {
    private String name;
    private int age;
    private int grade;
    private ContactInfo contactInfo;//Student HAS-A ContactInfo
    public void study() {
        System.out.println("Study");
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/aggregation-1.png)
_Figure 10: Class diagram shows the generalization relationship_

`Student` HAS-A `ContactInfo`. `ContactInfo` can be used in other places – for example, a company's `Employee` class can also use this `ContactInfo` class. So `Student` can exist without `ContactInfo` and `ContactInfo` can exist without `Student` . This type of relationship is known as aggregation.

#### b. Composition

In this relationship, class B can not exist without class A – but class A **can** exist without class B.

To give you an idea about composition, let's see an example of the `Student` class and the `StudentId` class.

```java
class StudentId {
    private String idNumber;//A-123456789
    private String bloodGroup;
    private String accountNumber;
}
public class Student {
    private String name;
    private int age;
    private int grade;
    private StudentId studentId;//Student HAS-A StudentId
    public void study() {
        System.out.println("Study");
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/composition--1-.png)
_Figure 11: Class diagram shows the composition relationship_

`Student` HAS-A `StudentId`. `Student` can exist without `StudentId` but `StudentId` can not exist without `Student`. This type of relationship is known as composition.

Now, let’s back to our previous record shop example that we discussed above. 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/classDiagramWithInheritance.png)
_Figure 12: Class diagram with inheritance_

We can implement this diagram in Java to avoid code duplication.

#### Advantages of inheritance

1. Code reuse: the child class inherits all instance members of the parent class.
2. You have more flexibility to change code: changing code in place is enough.
3. You can use polymorphism: method overriding requires IS-A relationship.

## Abstraction

**Abstraction is a process of hiding the implementation details and showing only functionality to the user.**

A common example of abstraction is that pressing the accelerator will increase the speed of a car. But the driver doesn’t know how pressing the accelerator increases the speed – they don't have to know that.

Technically abstract means something incomplete or to be completed later.

In Java, we can achieve abstraction in two ways: abstract class (0 to 100%) and interface (100%).

The keyword `abstract` can be applied to classes and methods. `abstract` and `final` or `static` can never be together.

#### I. Abstract class

An abstract class is one that contains the keyword `abstract`.

Abstract classes can’t be instantiated (can’t create objects of abstract classes). They can have constructors, static methods, and final methods.

#### II. Abstract methods

An abstract method is one that contains the keyword `abstract`.

An abstract method doesn’t have implementation (no method body and ends up with a semi colon). It shouldn’t be marked as `private`.

#### III. Abstract class and Abstract methods

* If at least one abstract method exists inside a class then the whole class should be abstract.
* We can have an abstract class with no abstract methods.
* We can have any number of abstract as well as non-abstract methods inside an abstract class at the same time.
* The first concrete sub class of an abstract class must provide implementation to all abstract methods.
* If this doesn't happen, then the sub class also should be marked as abstract.

In a real world scenario, the implementation will be provided by someone who is unknown to end users. Users don’t know the implementation class and the actual implementation.

Let’s consider an example of abstract concept usage.

```java
abstract class Shape {
    public abstract void draw();
}
class Circle extends Shape{
    public void draw() {
        System.out.println("Circle!");
    }
}
public class Test {
    public static void main(String[] args) {
        Shape circle = new Circle();
        circle.draw();
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/abstraction.png)
_Figure 13: Class diagram that shows the relationship between an abstract class and a concrete class_

#### When do we want to mark a class as abstract?

1. To force sub classes to implement abstract methods.
2. To stop having actual objects of that class.
3. To keep having a class reference.
4. To retain common class code.

### Interface

**An interface is a blueprint of a class.**

An interface is 100% abstract. No constructors are allowed here. It represents an IS-A relationship.

**NOTE:** Interfaces only define required methods. We can not retain common code. 

An interface can have only abstract methods, not concrete methods. By default, interface methods are `public` and `abstract`. So inside the interface, we don’t need to specify `public` and `abstract`.

So when a class implements an interface’s method without specifying the access level of that method, the compiler will throw an error stating `“Cannot reduce the visibility of the inherited method from interface”`. So that implemented method’s access level must be set to `public`.

By default, interface variables are `public`, `static` and `final`.

For instance:

```java
interface Runnable {
    int a = 10; //similar to: public static final int a = 10;
    void run(); //similar to: public abstract void run();
}
public class InterfaceChecker implements Runnable{
    public static void main(String[] args) {
        Runnable.a = 5;//The final field Runnable.a cannot be assigned.
    }
}
```

Let’s see an example that explains the interface concept:

```java
interface Drawable {
    void draw();
}
class Circle implements Drawable{
    public void draw() {
        System.out.println("Circle!");
    }
}
public class InterfaceChecker {
    public static void main(String[] args) {
        Drawable circle = new Circle();
        circle.draw();
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/interface.png)
_Figure 14: Class diagram that shows the relationship between an interface and a concrete class_

#### Default and Static methods in Interfaces

Usually we implement interface methods in a separate class. Let’s say we are required to add a new method in an interface. Then we must implement that method in that separate class, too.

To overcome this issue Java 8 introduced default and static methods that implement methods inside an interface, unlike abstract methods.

* **Default method**

```java
public interface DefaultInterface {
    void sleep();
    default void run() {
        System.out.println("I'm running!");
    }
}
public class InterfaceCheckers implements DefaultInterface{
    public void sleep() {
        System.out.println("Sleeping...");
    }
    public static void main(String[] args) {
        InterfaceCheckers checker = new InterfaceCheckers();
        checker.run();
        checker.sleep();
    }
}
/*
Output:
I'm running!
Sleeping...
 */
```

* **Static method**

Similar to static methods of classes, we can call them by their interface’s name.

```java
public interface DefaultInterface {
    void sleep();
    static void run() {
        System.out.println("I'm running!");
    }
}
public class InterfaceCheckers implements DefaultInterface{
    public void sleep() {
        System.out.println("Sleeping...");
    }
    public static void main(String[] args) {
        InterfaceCheckers checker = new InterfaceCheckers();
        DefaultInterface.run();
        checker.sleep();
    }
}
/*
Output:
I'm running!
Sleeping...
 */
```

* **Marker interface**

It’s an empty interface. For instance, Serializable, Cloneable, and Remote interfaces.

```java
public interface Serializable 
{
  //No fields or methods
}
```

### Advantages of interfaces

* They help us use multiple inheritance in Java.
* They provide abstraction.
* They provide loose coupling: objects are independent from one another.

### When do we want to change a class to an interface?

1. To force sub classes to implement abstract methods.
2. To stop having actual objects of that class.
3. To keep having a class reference.

**NOTE:** Remember, we can’t retain common code inside the interface.

If you want to define potentially required methods and common code, use an **abstract class**.

If you just want to define a required method, use an **interface**.

## Polymorphism

**Polymorphism is the ability of an object to take on many forms.**

Polymorphism in OOP occurs when a super class references a sub class object.

All Java objects are considered to be polymorphic as they share more than one IS-A relationship (at least all objects will pass the IS-A test for their own type and for the class Object).

We can access an object through a reference variable. A reference variable can be of only one type. Once declared, the type of a reference variable cannot be changed.

A reference variable can be declared as a class or interface type.

A single object can be referred to by reference variables of many different types as long as they are the **same type** or a **super type** of the object.

### Method overloading

**If a class has multiple methods that have same name but different parameters, this is known as method overloading.**

Method overloading rules:

1. **Must have a different parameter list.**
2. May have different return types.
3. May have different access modifiers.
4. May throw different exceptions.

```java
class JavaProgrammer{
    public void code() {
        System.out.println("Coding in C++");
    }
    public void code(String language) {
        System.out.println("Coding in "+language);
    }
}
public class MethodOverloader {
    public static void main(String[] args) {
        JavaProgrammer gosling = new JavaProgrammer();
        gosling.code();
        gosling.code("Java");
    }
}
/*
Output:
Coding in C++
Coding in Java
 */
```

**NOTE:** Static methods can also be overloaded.

```java
class Addition {
    public static int add(int a,int b) {
        return a+b;
    }
    public static int add(int a,int b,int c) {
        return a+b+c;
    }
}
public class PolyTest {
    public static void main(String[] args) {
        System.out.println(Addition.add(5, 5));
        System.out.println(Addition.add(2, 4, 6));
    }
}
```

**NOTE:** We can overload the main() method but the Java Virtual Machine (JVM) calls the main() method that receives String arrays as arguments.

```java
public class PolyTest {
    public static void main() {
        System.out.println("main()");
    }
    public static void main(String args) {
        System.out.println("String args");
    }
    public static void main(String[] args) {
        System.out.println("String[] args");
    }
}
//Output: String[] args
```

### Rules to follow for polymorphism

#### Compile time rules

1. Compiler only knows reference type.
2. It can only look in reference type for methods.
3. Outputs a method signature.

#### Run time rules

1. At runtime, JVM follows exact **runtime type (object type)** to find method.
2. Must match compile time method signature to method in actual object’s class.

### Method overriding

**If a subclass has the same method as declared in the super class, this is known as method overriding.**

Method overriding rules:

1. Must have the same parameter list.
2. Must have the same return type: although a covariant return allows us to change the return type of the overridden method.
3. Must not have a more restrictive access modifier: may have a less restrictive access modifier.
4. Must not throw new or broader checked exceptions: may throw narrower checked exceptions and may throw any unchecked exception.
5. Only inherited methods may be overridden (must have IS-A relationship).

Example for method overriding:

```java
public class Programmer {
    public void code() {
        System.out.println("Coding in C++");
    }
}
public class JavaProgrammer extends Programmer{
    public void code() {
        System.out.println("Coding in Java");
    }
}
public class MethodOverridder {
    public static void main(String[] args) {
        Programmer ben = new JavaProgrammer();
        ben.code();
    }
}
/*
Output:
Coding in Java
 */
```

**NOTE:** Static methods can’t be overridden because methods are overridden at run time. Static methods are associated with classes while instance methods are associated with objects. So in Java, the `main()` method also can’t be overridden. 

**NOTE:** Constructors can be overloaded but not overridden.

### Object types and reference types

```java
class Person{
    void eat() {
        System.out.println("Person is eating");
    }
}
class Student extends Person{
    void study() {
        System.out.println("Student is studying");
    }
}
public class InheritanceChecker {
    public static void main(String[] args) {
        Person alex = new Person();//New Person "is a" Person
        alex.eat();
        Student jane = new Student();//New Student "is a" Student
        jane.eat();
        jane.study();
        Person mary = new Student();//New Student "is a" Person
        mary.eat();
        //Student chris = new Person(); //New Person isn't a Student.
    }
}
```

In `Person mary = new Student();` , this object creation is perfectly fine.

`mary` is a `Person` type reference variable and `new Student()` will create a new `Student` object.

`mary` can’t access `study()` in compile time because the compiler only knows the reference type. Since there is no `study()` in the reference type class, it can’t access it. But in runtime `mary` is going to be the `Student` type (Runtime type/ object type). 

Please review this [post](https://coderanch.com/t/394210/java/compile-time-runtime-type) for more information on runtime types.

In this case, we can convince the compiler by saying “at runtime, `mary` will be `Student` type, so please allow me to call it”. How can we convince the compiler like this? This is where we use casting.

We can make `mary` a `Student` type in compile time and can call `study()` by casting it.

```java
((Student)mary).study();
```

We’ll learn about casting next.

### Object type casting

Java type casting is classified into two types:

1. Widening casting (implicit): automatic type conversion.
2. Narrowing casting (explicit): need explicit conversion.

In primitives, `long` is a larger type than `int` . Like in objects, the parent class is a larger type than the child class.

The reference variable only refers to an object. Casting a reference variable doesn’t change the object on the heap but it labels the same object in another way by means of instance members accessibility.

**I. Widening casting**

```java
Superclass superRef = new Subclass();
```

**II. Narrowing casting**

```java
Subclass ref = (Subclass) superRef;
```

We have to be careful when narrowing. When narrowing, we convince the compiler to compile without any error. If we convince it wrongly, we will get a run time error (usually `ClassCastException`).

In order to perform narrowing correctly, we use the `instanceof` operator. It checks for an IS-A relationship.

```java
class A {
    public void display(){
        System.out.println("Class A");
    }
}

class B extends A{
    public void display(){
        System.out.println("Class B");
    }
}

public class Test {
    public static void main(String[] args) {
        A objA = new B();
        if(objA instanceof B){
            ((B)objA).display();
        }
    }
}
/**
 * Output: Class B
 */

```

As I already stated before, we must remember one important thing when creating an object using the `new` keyword: the reference type should be the **same type** or a **super type** of the object type.

## Conclusion

Thank you everyone for reading. I hope this article helped you.

I strongly encourage you to read more related articles on OOP.

Checkout my original article series on Medium: [Object-oriented programming principles in Java](https://medium.com/@mvthanoshan9/object-oriented-programming-principles-in-java-820919dced1a)  

Please feel free to let me know if you have any questions. 

> Dream is not that which you see while sleeping it is something that does not let you sleep.  
> ― **A P J Abdul Kalam, Wings of Fire: An Autobiography**

Thank you.

**Happy Coding!**

