---
title: Methods in Java – Explained with Code Examples
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2024-02-29T20:05:17.000Z'
originalURL: https://freecodecamp.org/news/java-methods
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-divinetechygirl-1181298.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "Methods are essential for organizing Java projects, encouraging code reuse,\
  \ and improving overall code structure. \nIn this article, we will look at what\
  \ Java methods are and how they work, including their syntax, types, and examples.\n\
  Here's what we'l..."
---

Methods are essential for organizing Java projects, encouraging code reuse, and improving overall code structure. 

In this article, we will look at what Java methods are and how they work, including their syntax, types, and examples.

### Here's what we'll cover:

1. [What are Java Methods?](#heading-what-are-java-methods)
2. [Types of Access Specifiers in Java](#heading-types-of-access-specifiers-in-java)  
– [Public (`public`)](#heading-public-public)  
– [Private (`private`)](#heading-private-private)  
– [Protected (`protected`)](#heading-protected-protected)  
– [Default (`Package-Private`)](#heading-default-package-private)
3. [Types of Methods](#heading-types-of-methods)  
– [Pre-defined vs. User-defined](#heading-1-predefined-vs-user-defined)  
– [Based on functionality](#heading-2-based-on-functionality)
4. [Conclusion](#heading-conclusion)

## What are Java Methods?

In Java, a method is a set of statements that perform a certain action and are declared within a class. 

Here's the fundamental syntax for a Java method:

```java
acessSpecifier returnType methodName(parameterType1 parameterName1, parameterType2 parameterName2, ...) {
    // Method body - statements to perform a specific task
    // Return statement (if applicable)
}

```

Let's break down the components:

* **`accessSpecifier`**: defines the visibility or accessibility of classes, methods, and fields within a program.
* **`returnType`**: the data type of the value that the method returns. If the method does not return any value, the `void` keyword is used.
* **`methodName`**: the name of the method, following Java naming conventions.
* **`parameter`**: input value that the method accepts. These are optional, and a method can have zero or more parameters. Each parameter is declared with its data type and a name.
* **method body**: the set of statements enclosed in curly braces `{}` that define the task the method performs.
* **return statement**: if the method has a return type other than `void`, it must include a `return` statement followed by the value to be returned.

Here's an example of a simple Java method:

```java
public class SimpleMethodExample {

    // Method that takes two integers and returns their sum
    public static int addNumbers(int a, int b) {
        int sum = a + b;
        return sum;
    }

    public static void main(String[] args) {
        // Calling the method and storing the result
        int result = addNumbers(5, 7);

        // Printing the result
        System.out.println("The sum is: " + result);
    }
}

```

In this example, the `addNumbers` method takes two integers as parameters (`a` and `b`), calculates their sum, and returns the result. The `main` method then calls this method and prints the result.

Compile the Java code using the terminal, using the `javac` command:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-02-28-09-27-12.png)
_Output_

Methods facilitate code reusability by encapsulating functionality in a single block. You can call that block from different parts of your program, avoiding code duplication and promoting maintainability.

## Types of Access Specifiers in Java

Access specifiers control the visibility and accessibility of class members (fields, methods, and nested classes). 

There are typically four main types of access specifiers: public, private, protected, and default. They dictate where and how these members can be accessed, promoting encapsulation and modularity.

### Public (`public`)

This grants access to the member from **anywhere** in your program, regardless of package or class. It's suitable for widely used components like utility functions or constants.

**Syntax:**

```java
public class MyClass {
    public int publicField;
    public void publicMethod() {
        // method implementation
    }
}

```

**Example:**

```java
// File: MyClass.java

// A class with public access specifier
public class MyClass {
    
    // Public field
    public int publicField = 10;

    // Public method
    public void publicMethod() {
        System.out.println("This is a public method.");
    }

    // Main method to run the program
    public static void main(String[] args) {
        // Creating an object of MyClass
        MyClass myObject = new MyClass();

        // Accessing the public field
        System.out.println("Public Field: " + myObject.publicField);

        // Calling the public method
        myObject.publicMethod();
    }
}

```

In this example:

* The `MyClass` class is declared with the `public` modifier, making it accessible from any other class.
* The `publicField` is a public field that can be accessed from outside the class.
* The `publicMethod()` is a public method that can be called from outside the class.
* The `main` method is the entry point of the program, where an object of `MyClass` is created, and the public field and method are accessed.

```output
Public Field: 10
This is a public method.
```

### Private (`private`)

This confines access to the member **within the class** where it's declared. It protects sensitive data and enforces encapsulation.

**Syntax:**

```java
public class MyClass {
    private int privateField;
    private void privateMethod() {
        // method implementation
    }
}

```

**Example:**

```
// File: MyClass.java

// A class with private access specifier
public class MyClass {
    
    // Private field
    private int privateField = 10;

    // Private method
    private void privateMethod() {
        System.out.println("This is a private method.");
    }

    // Public method to access private members
    public void accessPrivateMembers() {
        // Accessing the private field
        System.out.println("Private Field: " + privateField);

        // Calling the private method
        privateMethod();
    }

    // Main method to run the program
    public static void main(String[] args) {
        // Creating an object of MyClass
        MyClass myObject = new MyClass();

        // Accessing private members through a public method
        myObject.accessPrivateMembers();
    }
}

```

In this example:

* The `MyClass` class has a `privateField` and a `privateMethod`, both marked with the `private` modifier.
* The `accessPrivateMembers()` method is a public method that can be called from outside the class. It provides access to the private field and calls the private method.

```output
Private Field: 10
This is a private method.

```

### Protected (`protected`)

The `protected` access specifier is used to make members (fields and methods) accessible within the same package or by subclasses, regardless of the package. They are not accessible from unrelated classes. It facilitates inheritance while controlling access to specific members in subclasses.

**Syntax:**

```java
public class MyClass {
    protected int protectedField;
    protected void protectedMethod() {
        // method implementation
    }
}

```

**Example:**

```java
// File: Animal.java

// A class with protected access specifier
public class Animal {
    
    // Protected field
    protected String species = "Unknown"; // Initialize with a default value

    // Protected method
    protected void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

```

```java
// File: Dog.java

// A subclass of Animal
public class Dog extends Animal {

    // Public method to access protected members
    public void displayInfo() {
        // Accessing the protected field from the superclass
        System.out.println("Species: " + species);

        // Calling the protected method from the superclass
        makeSound();
    }
}

```

```java
// File: Main.java

// Main class to run the program
public class Main {
    public static void main(String[] args) {
        // Creating an object of Dog
        Dog myDog = new Dog();

        // Accessing protected members through a public method
        myDog.displayInfo();
    }
}

```

In this example:

* The `Animal` class has a `protected` field (`species`) and a `protected` method (`makeSound`).
* The `Dog` class is a subclass of `Animal`, and it can access the `protected` members from the superclass.
* The `displayInfo()` method in the `Dog` class accesses the protected field and calls the protected method.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-from-2024-02-28-10-05-27.png)
_Output_

With the `protected` access specifier, members are accessible within the same package and by subclasses, promoting a certain level of visibility and inheritance while still maintaining encapsulation.

### Default (`Package-Private`)

If no access specifier is used, the default access level is `package-private`. Members with default access are accessible within the same package, but not outside it. It's often used for utility classes or helper methods within a specific module.

**Syntax:**

```java
class MyClass {
    int defaultField;
    void defaultMethod() {
        // method implementation
    }
}

```

**Example:**

```java
// File: Animal.java

// A class with default (package-private) access specifier
class Animal {
    String species = "Unknown";

    void makeSound() {
        System.out.println("Some generic animal sound");
    }
}

```

```java
// File: Main.java

// Main class to run the program
public class Main {
    public static void main(String[] args) {
        // Creating an object of Dog
        Dog myDog = new Dog();

        // Accessing default (package-private) members through a public method
        myDog.displayInfo();
    }
}

```

```java
// File: Dog.java

// Another class in the same package
public class Dog {
    Animal myAnimal = new Animal();

    void displayInfo() {
        // Accessing the default (package-private) field and method
        System.out.println("Species: " + myAnimal.species);
        myAnimal.makeSound();
    }
}

```

In this example:

* The `Animal` class does not have any access modifier specified, making it default (package-private). It has a package-private field `species` and a package-private method `makeSound`.
* The `Dog` class is in the same package as `Animal`, so it can access the default (package-private) members of the `Animal` class.
* The `Main` class runs the program by creating an object of `Dog` and calling its `displayInfo` method.

When you run this program, it should output the species and the sound of the animal. 

### How to Choose the Right Access Specifier

* **Public:** Use for widely used components, interfaces, and base classes.
* **Private:** Use for internal implementation details and sensitive data protection.
* **Default:** Use for helper methods or components specific to a package.
* **Protected:** Use for shared functionality among subclasses, while restricting access from outside the inheritance hierarchy.

## **Types of Methods**

In Java, methods can be categorized in two main ways:

### 1. Predefined vs. User-defined:

**Predefined methods:** These methods are already defined in the Java Class Library and can be used directly without any declaration. 

Examples include `System.out.println()` for printing to the console and `Math.max()` for finding the maximum of two numbers.

**User-defined methods:** These are methods that you write yourself to perform specific tasks within your program. They are defined within classes and are typically used to encapsulate functionality and improve code reusability.

```java
public class RectangleAreaCalculator {

    // User-defined method to calculate the area of a rectangle
    public static double calculateRectangleArea(double length, double width) {
        double area = length * width;
        return area;
    }

    public static void main(String[] args) {
        // Example of using the method
        double length = 5.0;
        double width = 3.0;
        
        // Calling the method
        double result = calculateRectangleArea(length, width);

        // Displaying the result
        System.out.println("The area of the rectangle with length " + length + " and width " + width + " is: " + result);
    }
}

```

In this example:

* `add` is a user-defined method because it's created by the user (programmer).
* The method takes two parameters (`num1` and `num2`) and returns their sum.
* The `main` method calls the `add` method with specific values, demonstrating the customized functionality provided by the user.

### 2. Based on functionality:

Within user-defined methods, there are several other classifications based on their characteristics:

### Instance Methods: 

Associated with an instance of a class. They can access instance variables and are called on an object of the class.

Here are some key characteristics of instance methods:

**Access to Instance Variables:**

* Instance methods have access to instance variables (also known as fields or properties) of the class.
* They can manipulate the state of the object they belong to.

**Use of `this` Keyword:**

* Inside an instance method, the `this` keyword refers to the current instance of the class. It's often used to differentiate between instance variables and parameters with the same name.

**Non-static Context:**

* Instance methods are called in the context of an object. They can't be called without creating an instance of the class.

**Declaration and Invocation:**

* Instance methods are declared without the `static` keyword.
* They are invoked on an instance of the class using the dot (`.`) notation.

Here's a simple example in Java to illustrate instance methods:

**Example:**

```
public class Dog {
    // Instance variables
    String name;
    int age;

    // Constructor to initialize the instance variables
    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Instance method to bark
    public void bark() {
        System.out.println(name + " says Woof!");
    }

    // Instance method to age the dog
    public void ageOneYear() {
        age++;
        System.out.println(name + " is now " + age + " years old.");
    }

    public static void main(String[] args) {
        // Creating instances of the Dog class
        Dog myDog = new Dog("Buddy", 3);
        Dog anotherDog = new Dog("Max", 2);

        // Calling instance methods on objects
        myDog.bark();
        myDog.ageOneYear();

        anotherDog.bark();
        anotherDog.ageOneYear();
    }
}

```

In this example:

* `bark` and `ageOneYear` are instance methods of the `Dog` class.
* They are invoked on instances of the `Dog` class (`myDog` and `anotherDog`).
* These methods can access and manipulate the instance variables (`name` and `age`) of the respective objects.

Instance methods are powerful because they allow you to encapsulate behavior related to an object's state and provide a way to interact with and modify that state.

### Static Methods: 

A static method belongs to the class rather than an instance of the class. This means you can call a static method without creating an instance (object) of the class. It's declared using the `static` keyword.

Static methods are commonly used for utility functions that don't depend on the state of an object. For example, methods for mathematical calculations, string manipulations, and so on.

**Example:**

```java
public class MathOperations {
    // Static method
    public static int add(int a, int b) {
        return a + b;
    }

    // Static method
    public static int multiply(int a, int b) {
        return a * b;
    }
}

```

### Abstract Methods:

These methods are declared but not implemented in a class. They are meant to be overridden by subclasses, providing a blueprint for specific functionality that must be implemented in each subclass.

Abstract methods are useful when you want to define a template in a base class or interface, leaving the specific implementation to the subclasses. Abstract methods define a contract that the subclasses must follow.

**Example:**

```
public abstract class Shape {
    // Abstract method
    abstract double calculateArea();
}

```

  
**Other method types:** Additionally, there are less common types like constructors used for object initialization, accessor methods (getters) for retrieving object data, and mutator methods (setters) for modifying object data.

## Conclusion

Methods are essential for organizing Java projects, encouraging code reuse, and improving overall code structure. 

In this article, we will look at Java methods, including their syntax, types, and recommended practices.

Happy Coding!

