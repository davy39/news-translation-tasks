---
title: Java Data Types And Variables – Explained for Beginners
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-27T16:59:18.000Z'
originalURL: https://freecodecamp.org/news/java-data-types-and-variables
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/data-types-and-variables.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Java
  slug: java
seo_title: null
seo_desc: "By Jacob Isah \nAs a beginner learning Java, one of the fundamental topics\
  \ you'll need to understand is data types. \nEvery day in the life of every software\
  \ engineer is about how to manipulate data, how to get data from users, the format\
  \ of the data, ..."
---

By Jacob Isah 

As a beginner learning Java, one of the fundamental topics you'll need to understand is data types. 

Every day in the life of every software engineer is about how to manipulate data, how to get data from users, the format of the data, and how this data is stored and managed.

Java is a popular programming language known for its strong typing system, which means that every variable must have a declared type. Java provides a wide range of data types to accommodate various kinds of data and operations. 

In this article, I will walk you through Java's data types and explain how they work.

There are two types of data types in Java – primitive data types and reference data types. Let's dive in and learn more about each.

## Differences Between Primitive Data Types and Reference Data Types

In Java, there are important differences between reference data types and primitive data types.

Primitive data types store the actual value directly in memory, while reference data types store references or memory addresses that point to the location where the object is stored.

Primitive data types have default values if not explicitly initialized, while reference data types default to `null`.

Primitive data types have fixed sizes defined by the language, while reference data types have a fixed size, regardless of the object they reference.

Operations on primitive data types can be performed directly, while operations on reference data types can only be performed through the methods provided by the object.

Primitive data types have corresponding wrapper classes, while reference data types do not.

When passing a primitive data type as a method argument, a copy of the value is passed, while passing a reference data type passes the reference by value.

These differences shows how important storage, default values, size, operations, and pass-by-value semantics between reference data types and primitive data types work in Java.

### Primitive Data Types in Java

Java has eight primitive data types, which are the most basic building blocks for storing data. These types serve as the building blocks of data manipulation in Java. 

Primitive data types serve only one purpose — containing pure, simple values of a certain kind. They are reserved keywords in Java. Because they are keywords, they cannot be used as variable names. They include the following:

#### Byte

Imagine that you have a small box that can hold numbers. This box can hold numbers from -128 to 127. It's like a toy box that can only fit a certain range of toys, from -128 to 127. You can put any number from this range inside the box.

The `byte` data type is an 8-bit signed integer that can hold values from -128 to 127. It is commonly used when memory space is a concern. Let’s create a variable of type `byte`:

```java
byte myByte = 100;
System.out.println("byte: " + myByte);
```

```java
Output
byte: 100
```

#### Short

Now, imagine you have a bigger box. This box can hold the `short` data type that is a 16-bit signed integer that can hold values from -32,768 to 32,767. It is useful for storing larger integer values than the `byte` data type.

```java
short myShort = 30000;
System.out.println("short: " + myShort);
```

```java
Output:
short: 30000
```

#### Int

Now, let's think of a bigger storage container. The box is an `int` data type that is a 32-bit signed integer that can hold numbers from -2,147,483,648 to 2,147,483,647. It's like a big treasure box that can hold a wide range of numbers, both positive and negative. It is the most commonly used data type for representing whole numbers in Java.

```java
int myInt = 2000000000;
System.out.println("int: " + myInt);
```

```java
Output::
int: 2000000000
```

#### Long

Okay, now we have a huge storage room. This room can hold numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807. It's like having a massive warehouse that can store a gigantic range of numbers. It is used when a wider range of integer values is required.

```java
long myLong = 9,223,372,036,854,775,807;
System.out.println("long: " + myLong);
```

```java
Output::
long: 9,223,372,036,854,775,807
```

#### Float

Imagine you have a special box that can hold decimal numbers. This box can hold decimal numbers with moderate precision. It's like a container that can hold water with a reasonable amount of accuracy. 

The `float` data type is a single-precision 32-bit floating-point number. It is useful for representing decimal numbers with moderate precision.

```java
float myFloat = 9,223,372,036,854,775,807;
System.out.println("float: " + myFloat);
```

```java
Output::
float: 9,223,372,036,854,775,807
```

#### Double

The `double` data type is a double-precision 64-bit floating-point number. It provides higher precision than float and is commonly used for calculations involving decimal numbers.

```java
double myDouble = 129.7;
System.out.println("double: " + mydouble);
```

```java
Output::
double: 129.7
```

#### Boolean 

The `boolean` data type represents a `boolean` value, which can be either true or false. It is used for logical operations and control flow.

```java
boolean isJavaFun = true;
boolean isProgrammingFun = false;

System.out.println(isJavaFun);     
System.out.println(isProgrammingFun);


```

```java
Output::
true
false
```

#### Char

The `char` data type represents a single Unicode character and is 16 bits in size. It can store any character from the Unicode character set.

```java
char johnGrade = 'B';
System.out.println(johnGrade);
```

```java
Output::
B
```

### Reference Data Types in Java

In addition to primitive data types, reference data types are used to store references or memory addresses that point to objects stored in memory. 

These data types do not actually store the data itself but rather a reference to the memory location where the data is stored. Let's look at a few popular types of reference data now.

#### Strings

The `String` class represents a sequence of characters. It is widely used for manipulating and storing textual data.

```java
String name = "John Doe";
System.out.println("Name: " + name);
```

```java
Output::
Name: John Doe
```

#### Arrays

`Arrays` are used to store a collection of elements of the same type. They provide a convenient way to work with groups of related values.

```java
int[] numbers = {1, 2, 3, 4, 5};
System.out.println("Numbers: " + java.util.Arrays.toString(numbers));
```

```java
Output::
Numbers: 12345
```

#### Classes

The `class` data type represents a `class` in Java. It is used to create objects and define their behavior.

To understand how classes works in Java, we will create a class example and implement the class in the main class.

In the following example, we will create a `Car` class  that represents a car with color and speed attributes. We will have a constructor to initialize the color and the speed will be set to 0 by default. The class also will includes methods to accelerate the car, and brake the car.

Here's an example:

```java
public class ClassCarExample {
    // Instance variables or fields
    String color;
    int speed;

	//Method start that gets the car started
    public void start() {
        System.out.println("The car has started.");
    }
	
    //Method accelerate that increases the speed of the car by 10 km/h
      public void accelerate() {
        speed += 10;
        System.out.println("The car is accelerating. Current speed: " + 		speed + " km/h");
    }
	
    //Method brake that reduces the speed of the car by 5 each time the 		 method is called
    
    public void brake() {
        speed -= 5;
        System.out.println("The car is braking. Current speed: " + 			speed + " km/h");
    }
}
```

We will now create the main method where we will run our class and get our car moving, accelerating, and braking.

```java
public class Main {
    public static void main(String[] args) {
        // Create an instance of ClassCarExample
        ClassCarExample car = new ClassCarExample();

        // Start the car
        car.start();
        

        // Accelerate the car
        car.accelerate();
       

        // Brake the car
        car.brake();
        }
    }
}

```

```java
Output:
The car has started.
The car is accelerating. Current speed: 10 km/h
The car is braking. Current speed: 5 km/h
```

#### Interfaces

The `interface` keyword is used to declare an `interface` .Total abstraction (hiding) is offered, which means that all methods in an `interface` are declared with an empty body and that all fields are by default `public`, `static`, and `final`. 

All of the methods declared in an `interface` must be implemented by a `class` that implements the `interface`.   
  
To better understand how interface works, we will create an interface class called `MyInterfaceClass` that declares three methods: `methodExampleOne()`  `methodExampleTwo()`, and `methodExampleThree()`:

```java
// The interface class
interface MyInterfaceClass {
    void methodExampleOne();
    void methodExampleTwo();
    void methodExampleThree();
}
```

Now we need a class that implement the interface class. We will create a `MyClass` class that implements `MyInterfaceClass` interface and provides the implementation for all three methods created above.

```java
// Implement the interface in a class
class MyClass implements MyInterfaceClass {
    public void methodExampleOne() {
        System.out.println("Implementing methodExampleOne");
    }

    public void methodExampleTwo() {
        System.out.println("Implementing methodExampleTwo");
    }

    public void methodExampleThree() {
        System.out.println("Implementing methodExampleThree");
    }
}
```

To better drive this home, let's create a main method where we can create an object of our `myClass` and call our methods on the `myObj` object we will create and run our Java program.

```java
// Main class to test the implementation
public class Main {
    public static void main(String[] args) {
    	
        //create myObj from MyClass
        MyClass myObj = new MyClass();

        // Call the implemented methods on the object we created.
        myObj.methodExampleOne();
        myObj.methodExampleTwo();
        myObj.methodExampleThree();
    }
}
```

When we run the `Main` class, we will see the following output:

```java
Output:
Implementing methodExampleOne
Implementing methodExampleTwo
Implementing methodExampleThree
```

#### Enums

The `Enum` data type represents an enumeration (list) type. It is used to define a fixed set of named values, such as days of the week or colors.

```java
class EnumClassExample {  
	//defining the enum inside the class  
public enum Weekdays { 
    SUNDAY,MONDAY,TUESDAY,WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
  }  
	//main method  
public static void main(String[] args) {  

	//loop throught the enum  

	for (Weekdays w : Weekdays.values())  
    System.out.println(w);  
	}
}  

```

```java
Output::
SUNDAY
MONDAY
TUESDAY
WEDNESDAY
THURSDAY
FRIDAY
SATURDAY
```

## Wrapping Up

Understanding Java data types is crucial for effective programming in Java. Whether it's the primitive data types for basic value storage or the reference data types for complex objects and behaviors, each data type serves a specific purpose. 

By leveraging the appropriate data types, software engineers can write more efficient, reliable, and maintainable code in Java.

Your feedback is highly appreciated. You can follow me on [Twitter](https://twitter.com/IsahJakub) and [LinkedIn](https://www.linkedin.com/in/isahejacob/).  

