---
title: 'How to Use Constructors in Java: A Beginner''s Guide'
subtitle: ''
author: Ateev Duggal
co_authors: []
series: null
date: '2025-07-08T18:15:32.094Z'
originalURL: https://freecodecamp.org/news/how-to-use-constructors-in-java-a-beginners-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1751998519087/7808c004-c8e5-4e63-b293-10fa479a179f.png
tags:
- name: Java
  slug: java
- name: Beginner Developers
  slug: beginners
- name: constructors
  slug: constructors
seo_title: null
seo_desc: Java is an object-oriented programming language that is centred around the
  concept of objects. Objects are like real-world entities that are created with the
  new keyword and occupy memory. But all this happens in the front-end code – so what
  about th...
---

Java is an object-oriented programming language that is centred around the concept of objects. Objects are like real-world entities that are created with the new keyword and occupy memory. But all this happens in the front-end code – so what about the back-end? How are objects created and initialised with values?

This is where constructors come into play. Constructors are special types of methods with no return type. They are basically used to initialise the object, to set up its internal state, or to assign default values to its attributes.

In this tutorial, we will go deep into the topic of constructors in Java. You’ll learn how they work and why they are essential in object creation and Java programming. By the end, I hope you’ll understand why they’re one of the core concepts of OOP.

Let’s start…

### Prerequisites

You don’t need to know anything too advanced to start learning about constructors in Java. Just a basic understanding of Java syntax, classes, objects, methods, parameters, arguments, and access modifiers is enough to get started.

## What we’ll cover:

* [What are Constructors in Java?](#heading-what-are-constructors-in-java)
    
    * [Constructor syntax:](#heading-constructor-syntax)
        
* [Types of Constructors](#heading-types-of-constructors)
    
    * [Default Constructor](#heading-default-constructor)
        
    * [No Argument constructor](#heading-no-argument-constructor)
        
    * [Parameterised Constructor](#heading-parameterised-constructor)
        
    * [Copy Constructor](#heading-copy-constructor)
        
* [What Happens Behind the Scenes When a Constructor Is Called in Java?](#heading-what-happens-behind-the-scenes-when-a-constructor-is-called-in-java)
    
* [How to Use the return Keyword in Constructors](#heading-how-to-use-the-return-keyword-in-constructors)
    
    * [Sample Code:](#heading-sample-code)
        
    * [Example:](#heading-example-4)
        
* [Conclusion](#heading-conclusion)
    
* [Frequently Asked Questions](#heading-frequently-asked-questions)
    

## **What are Constructors in Java?**

As mentioned above, constructors are special types of methods that:

1. do not have a return type (not even void), 
    
2. have the same name as the class
    
3. are called automatically when an object is created using the new keyword. 
    

A constructor’s main purpose is to initialise a newly created object, to set up its internal state, or to assign default values to its attributes.

Constructors can also be understood as a special block of code which is called when an object is created – either automatically or manually by hard-coding it – with the values we want to initialise the object with.

If we’re okay with the object using default values (like 0 for numbers or null for objects), Java will handle that for us automatically. But if we want to give the object specific values when it's created, we need to write a constructor that takes those values as parameters and uses them to set up the object.

### **Constructor syntax:**

```java
class ClassName {

    // Default constructor with access modifier
    [access_modifier] ClassName(parameters...) {
        // constructor body
    }

}
```

### Examples

**When the constructor is not defined explicitly**

```java
class Car {

    String brand;
    int year;

    // No constructor is defined, so Java provides a default one
}

public class Main {

    public static void main(String[] args) {

        Car car1 = new Car();  // Java calls the default constructor

        // Default values: brand = null, year = 0
        System.out.println("Brand: " + car1.brand);
        System.out.println("Year: " + car1.year);
    }
}
```

Output:

![output of the code in which there is no constructor](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcTW6FYYmq8kB1QL_vSBNqbaVBgo7hLXvqmA3l52HBh9Yvq4AN1aLIAKRqqiOz_tDcCFOTWBVoO1bgjWOD2yyt1nykuobAPQTWRayjqK0jDu2COmPxqI5AaapIyFzDbkrvreV-qyw?key=-LGNq3k7xufJJBHkVFXMZw align="center")

In the above code, we have a **Car** class with two variables:

1. brand of type `String`
    
2. year of type `int`
    

Since a class is just a blueprint, we need to create an object to actually use it. This is done in the `Main` class. When we create a Car object using `new` Car(), Java looks for a constructor. Because we didn’t define one, the compiler automatically provides a default constructor (one with no arguments).

This allows us to create the object and print its variables without any errors. The values printed will be the default ones — `null` **for the** `String`**, and** `0` **for the** `int`**.**

We'll dive deeper into how this works behind the scenes later, step by step, so it becomes easier to understand.

**When we have defined a constructor**

```java
public class Car {

    String brand;
    int year;

    // Constructor with parameters to initialize custom values
    public Car(String brandName, int modelYear) {
        brand = brandName;
        year = modelYear;
    }
}

public class Main {

    public static void main(String[] args) {

        Car car2 = new Car("Toyota", 2022);  // Custom values

        System.out.println("Brand: " + car2.brand);
        System.out.println("Year: " + car2.year);
    }
}
```

**Output**

![Output of the code which has a constructor.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751864448284/2cbb8360-1c6d-42b8-811f-b7603625288d.png align="center")

This is the same code as before, with one key difference: this time, we’ve explicitly defined a constructor. Because of this, the output we see isn’t the default values (`null` for `String`, `0` for `int`), but the custom values we provided.

How does that happen? Simple – we pass values as arguments when creating the object:

`Car car2 = new Car("Toyota", 2022);`

These values are received by the constructor as parameters and are then used to initialize the object’s variables. As a result, instead of default values, we get the brand and year we specified.

## **Types of Constructors**

There are mainly four types of constructors:

1. Default Constructors
    
2. No-Arguments Constructor
    
3. Parameterised Constructor
    
4. Copy Constructor
    

![Types of constructors](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfafO5dDmX5UA0ADQI5Q8DZSU2H_bVlHjmtKdDpMkmWB4Rhui1kR4w_BP_7-mPz6eb9KdGkVmYxYsZHa4HI044mz3O0CXtXJZBhpJr_wCqWgLO6U0BDUNzm_C9piUHfyXr84xEsoQ?key=-LGNq3k7xufJJBHkVFXMZw align="center")

### **Default Constructor**

A type of no-argument constructor that is added by the compiler during the compilation process so that the values of the object can be initialised. It’s only added by the compiler if you don’t add one explicitly.

#### **Syntax:**

```java
public class MyClass {

    public MyClass() {
        // Constructor body
    }

}
```

#### **Example**

```java
public class Bike {

    // No constructor defined here
    // Compiler will automatically add a default constructor

    public static void main(String[] args) {
        Bike myBike = new Bike();  // Calls the compiler-provided default constructor
        System.out.println("Bike object created!");
    }

}
```

The code becomes the following after the compiler adds a default constructor during the compilation process:

```java
public class Bike {

    // Compiler-added default constructor
    public Bike() {
        super();  // Calls Object class constructor
    }

    public static void main(String[] args) {
        Bike myBike = new Bike();  // Now calls this explicit default constructor
        System.out.println("Bike object created!");
    }

}
```

#### **Output**

Bike object created!

![Default Constructor](https://cdn.hashnode.com/res/hashnode/image/upload/v1751867033814/3296a90c-3576-4a57-a863-fe0d1acfafa2.png align="center")

### **No Argument constructor**

No-argument constructor is a type of constructor that you explicitly write in your code and that does not contain any parameters.

Now, you may be wondering…Isn't it the same as the default constructor? The answer is both yes and no.

There isn’t much difference between the default constructor and the no-argument constructor, as both do not take any parameters. But there is one key difference.

The default constructor, as we have already discussed, is a type of no-argument constructor that is automatically added by the compiler when it doesn’t find one in our code. In contrast, a no-argument constructor is a type of constructor that we write in our code. 

In short, if the compiler is the one that is adding a constructor during the compilation process, it's called a default constructor. But if we are the ones adding the constructor, it’s called a no-argument constructor. 

The main difference between a default constructor and a user-defined constructor is **how they are created and what they do**.

* A **default constructor** is automatically added by the compiler **if we don’t add one ourselves**. It doesn’t do much – it just calls the parent class (usually the `Object class`) and sets all variables to their default values. For example, `int` becomes `0`and objects become `null`.
    
* A **user-defined constructor** is one that **we write ourselves**. We can add custom logic inside it, set custom values to variables, and use access modifiers like `public`, `private`, or `protected`. This means we can decide how the object should be set up when it is created.
    

Note that even if we don’t write `super()` in our constructor, Java still adds it automatically unless we call another constructor with `this()` or call a different `super(...)` with parameters.

We will understand this deeply in the next section.

| **Aspect** | **Default Constructor** | **No-Argument Constructor** |
| --- | --- | --- |
| **Definition** | A constructor is automatically provided by the compiler when no other constructors exist. | A constructor explicitly written by the programmer that takes no arguments. |
| **Defined By** | Compiler | Programmer |
| **Custom Logic** | Not possible – does only basic, default initialization | Yes – can contain any initialization logic |
| **When Available** | Only if the class has no constructors defined at all | When explicitly written by the programmer |
| **Purpose** | To allow object creation with default initialization | To allow object creation with programmer-defined behavior |

#### **Syntax:**

```java
class ClassName {

    public ClassName() {
        // Body (optional)
    }

}
```

#### **Example**

Let's use the same Bike example we used to explain the default constructor.

```java
public class Bike {

    public Bike() {
        System.out.println("Bike object created!");
    }

    public static void main(String[] args) {
        Bike myBike = new Bike();
    }
}
```

#### **Output:**

Bike object created!

![No Argument Construment](https://cdn.hashnode.com/res/hashnode/image/upload/v1751868234945/565ec06d-7e4d-4415-b983-f517c721d0b9.png align="center")

In the above code, we have defined a constructor in our code while writing it. This means that it is an example of a no-argument constructor.

We know that both types of constructors are defined without any parameters, but what about the body? We haven’t said anything about it. Let’s see what happens if we write code with a no-argument constructor without a body:

```java
public class Bike {

    Bike() {
        // No body
    }

    public static void main(String[] args) {
        Bike myBike = new Bike(); // Calls the user-defined no-argument constructor
        System.out.println("Bike object created!");
    }
}
```

#### **Output:**

Bike object created!

The code still gets compiled because the compiler adds the `super()` keyword during the compilation process, which initialises the object using the object class.

### **Parameterised Constructor**

A constructor that accepts parameters is called a parameterised constructor and is only used when we have to initialise an object’s attributes with custom values. 

* Parameter refers to the variable listed in the constructor or method definition.
    
* Argument is the actual value passed when calling the constructor or method.
    

It gives us the flexibility of initiating our object with custom values given at the time of object creation.

#### **Syntax**

Below is the syntax for a parameterised constructor that takes one parameter:

```java
class ClassName {

    // Data members (instance variables)
    DataType variable1;

    // Parameterized constructor
    ClassName(DataType param1) {
        variable1 = param1;
    }

    // Main method to create objects
    public static void main(String[] args) {
        // Creating object using parameterized constructor
        ClassName obj = new ClassName(value1);
    }
}
```

#### **Example**

We will again use the Bike example for this.

```java
public class Bike {

    String modelName;  // instance variable

    // Parameterized constructor
    Bike(String model) {
        modelName = model;
    }

    public static void main(String[] args) {
        // Pass parameter while creating the Bike object
        Bike myBike = new Bike("Mountain Bike");
        System.out.println("Bike object created! Model: " + myBike.modelName);
    }
}
```

#### Output:

Bike object created! Model: Mountain Bike

![Parameterized Constructor](https://cdn.hashnode.com/res/hashnode/image/upload/v1751870395133/72bcbe0c-3a7c-4cc1-87d4-1ae9106b21d9.png align="center")

In this example, we’re working with a Bike class that has an instance variable of String data type called modelName, and a constructor to set the value of that variable.

The constructor takes a parameter called model and assigns it to modelName. So, when we create a new Bike object and pass in the string "Mountain Bike", the constructor stores that value in the modelName variable.

Because of this, when we print out the model name, we see "Mountain Bike" instead of null, which is the default value of the String data type, as now the value of the modelName has been updated.

### **Copy Constructor**

A copy constructor is used to create a new object as a copy of the existing object. Unlike C++, Java doesn’t have a default copy constructor. Instead, we have to create our own by creating a constructor that takes an object of the same class as a parameter and copies its fields.

#### **Syntax**

```java
class ClassName {

    // Fields
    DataType1 field1;
    DataType2 field2;
    // ... other fields

    // Normal constructor
    ClassName(DataType1 f1, DataType2 f2) {
        field1 = f1;
        field2 = f2;
        // ... initialize other fields
    }

    // Copy constructor 
    ClassName(ClassName other) {
        field1 = other.field1;
        field2 = other.field2;
        // ... copy other fields
    }
}
```

#### **Example**

```java
public class Bike {

    String modelName;  // instance variable

    // Parameterized constructor
    Bike(String model) {
        modelName = model;
    }

    // Copy constructor
    Bike(Bike otherBike) {
        modelName = otherBike.modelName;
    }

    public static void main(String[] args) {
        // Create a Bike object using the parameterized constructor
        Bike myBike = new Bike("Mountain Bike");
        System.out.println("Bike object created! Model: " + myBike.modelName);

        // Create a copy of the existing Bike object using the copy constructor
        Bike copiedBike = new Bike(myBike);
        System.out.println("Copied Bike object created! Model: " + copiedBike.modelName);
    }
}
```

#### **Output:**

Bike object created! Model: Mountain Bike

Copied Bike object created! Model: Mountain Bike

![Copy Constructor](https://cdn.hashnode.com/res/hashnode/image/upload/v1751874707838/772bdc8a-75d7-437d-a296-7f472fe5c764.png align="center")

In the above code, we have created a copy constructor to copy the values of the object (myBike) into a new object (copiedBike), which we have defined in the main class.

But the way the new object is called is a little different. Instead of passing arguments for the constructor, we have passed the original object.

#### **Why Copy Constructors?**

A copy constructor is used to make a copy of the object, but you can also make a copy using the clone() method or the object.clone() method. So why do we use a copy constructor?

The copy constructor makes a deep copy, while the clone method makes a shallow copy of the object. There are various things that you should know before using cloning techniques, like [CloneNotSupportedException](https://docs.oracle.com/javase/8/docs/api/java/lang/CloneNotSupportedException.html)**.**

On the other hand, copy constructors are clear and easy to understand, and work well with final fields. We can control how the copy happens (deep vs. shallow) and especially when we are dealing with mutable objects.

## **What Happens Behind the Scenes When a Constructor Is Called in Java?**

So, just to recap: when we create an object using the `new` keyword, a constructor is automatically called. If we haven't defined any constructors in our class, Java automatically defines a constructor for us. 

But while writing and running our code, we mostly focus on what’s visible in our editor, as in what we can see. Let’s dive a little deeper and explore what happens behind the scenes – at the compiler and JVM level – when an object is created and executed.

* **Step 1: Memory Allocation** – When we create an object using a new keyword, Java allocates memory for that object in the heap. This memory is where the object’s fields (also called attributes) will be placed.
    
* **Step 2: Reference Creation** – A reference to this object is stored on the stack, which lets our program interact with the object that lives in the heap.
    
* **Step 3: Constructor Creation** – Java then determines which constructor to call. If no constructor is explicitly defined in our class, the compiler automatically inserts a constructor with no parameters.
    
* **Step 4: Superclass Constructor Call** – Before executing the constructor’s body, Java first calls the constructor of the superclass using the `super()` keyword. This ensures that the fields inherited from the parent class are properly initialised. If you don’t explicitly write `super()`, the compiler adds it automatically in the first line of the code, but only if the superclass has a no-argument constructor, unless we're already calling another constructor via `this()`.
    

But don’t use both the `super()` and `this()` keywords in the same constructor (you can use them in separate constructors.

Let’s say that it doesn’t have a super class – then what? 

The answer is simple: Java has an in-built Object class that has a no-argument constructor by default.  This is why our classes run smoothly even if we don’t write super() ourselves, as Java calls it in the background. 

That means every class we create is a subclass of the object class:

#### Attribute Initialisation:

At this point, fields get initialised:

* First, with default values (for example, 0 for int, null for objects),
    
* Then, with any explicit initialisations we've written (for example, int x = 10), the default values will get replaced by them.
    

#### Constructor Execution:

And finally, the logic runs. This is where all or some of the attributes defined in the class for object creation are initialised by the parameters used during object creation, with the help of constructors. 

But not every field may get initialised. Fields that are not updated by the constructor will keep the values they already have (either the default value or the explicitly initialised values). 

In short, the constructor gives us the flexibility to customise our object at the time of creation, but it doesn't automatically set every field unless we explicitly write the logic for it.

Check the code below to understand better:

```java
class Example {

    int a;           // default 0
    int b = 10;      // explicitly initialized to 10
    String name;     // default null

    Example(int x) {
        a = x;       // only 'a' is set through constructor
        // 'b' is not changed, stays 10
        // 'name' is not changed, stays null
    }

    void display() {
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("name = " + name);
    }

    public static void main(String[] args) {
        Example obj = new Example(5);
        obj.display();
    }
}
```

**Output:**

![Output of the code explaining how constructor work.](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfRr6j8-QeGffPm7DYMImJL5s9X-apEGhLzXAv_cNw2CcwONejKxd4-_xKbmdKGSW1w09lt3Pib_psv7RLkd5LJ1uUxd9LSU2KOcDU9kYeqjYbZWS-qUN1PuLbNV8uF0M373kl7Cw?key=-LGNq3k7xufJJBHkVFXMZw align="center")

In the above example, we have three data members – a, b, and name. We have already done the declaration and initialisation of the variable b at the beginning and given a value to a at the time of object creation.

So we can see that:

1.  ‘**a**’, whose value has been updated by the constructor with the value given at the time of object creation, has the same value
    
2. **‘b’,** which already had a value and does not get updated by the constructor, prints the same value 
    
3. the string **‘name’** didn’t have a value, so null was printed instead, as it is the default value of the String data type.
    

## **How to Use the** `return` **Keyword in Constructors**

We know that constructors are defined without a return type, but we can use the return keyword in the constructor only to exit the constructor early, not to return a value. Check out the code below.

### **Sample Code:**

```java
public class Bike {

    String modelName;  // instance variable
    int speed;

    // Parameterized constructor
    Bike(String model, int sp) {
        modelName = model;
        return;
        speed = sp;
    }

    public static void main(String[] args) {
        // Pass parameter while creating the Bike object
        Bike myBike = new Bike("Mountain Bike", 20);
        System.out.println("Bike object created! Model: " + myBike.modelName);
        System.out.println("Speed of the Bike is " + myBike.speed);
    }
}
```

Let’s try to understand the above code and the use of the return keyword along with it. We will start with what would happen if the return keyword wasn’t here. The code would have executed without any errors and would have received an output.

![code without the return keyword](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdRpxqN-7mjbNNenChHDcIxtufG5P4LQOG1GXo4L7_kFz955k-YF2HJfy96ZoIbPtxy3flUKiw4Mq6C8qSdZEnw3bzg5rbAy3BR4Q4x7uO2EjZfN7zFGDRlCWbAth_s97TGvoHpCQ?key=-LGNq3k7xufJJBHkVFXMZw align="center")

Now, what will happen if we add the return keyword? As we have discussed above, the return keyword will tell the compiler not to go beyond this point in the constructor. 

So whatever we have written in the constructor after the return keyword will not be compiled, and if that had any value and was necessary for the proper execution of our code, the compiler will throw an error.

![code with the return keyword](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc63VgyWkEdvcPr8x9TkVb-ZJKuPO2Z-ips_sNT70zGwFYRRdzfYYWG1Bfwnjmdypz-Pt8YS6SwQGBKMNrNhz4J27psGuOxz9Fs0gLVpM0oHzn5N1J0w3wgL7HU7rUQlB200qoRoA?key=-LGNq3k7xufJJBHkVFXMZw align="center")

The error says it clearly ‘unreachable statement’, which means that the compiler was not allowed to go beyond the return keyword. 

Now that you understand the return keyword, let’s see when you can use it.

### **Example:**

```java
public class Bike {

    // Constructor with a condition to exit early
    Bike(boolean skip) {
        if (skip) {
            System.out.println("Constructor exited early");
            return; // Ends constructor execution here
        }

        System.out.println("Constructor continues...");
        // More initialization logic can go here
        System.out.println("Bike object initialized successfully");
    }

    public static void main(String[] args) {
        System.out.println("Creating first bike (skip = true):");
        Bike bike1 = new Bike(true);  // Constructor will exit early

        System.out.println("\nCreating second bike (skip = false):");
        Bike bike2 = new Bike(false); // Constructor will continue
    }
}
```

We’ve defined a Bike class that has a constructor with one boolean parameter called skip. Inside the constructor, there's an if statement that checks if skip is true. If it is, the constructor prints a message and uses the return keyword to exit early. This means the rest of the constructor won’t run.

But there is no else block. So what happens when skip is false? In that case, the if condition is not true, then the code inside the if statement is not executed (including the return keyword) and the constructor simply continues to the next lines of code. That’s where we do the actual bike initialisation and print a success message.

In short:

1. If skip is true, the constructor exits early.
    
2. If skip is false, the constructor continues and finishes the setup.
    

![output of the example explaining return keyword](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeK-1kbbG97wMT_d-zrZ28eCuVsWZEkH6Ve3kuYSyXM1e-pZDsJl8K1S4GVfp54XnxGLOGGH_y_B3lZvmy1GRSvOY5Xp_rqHZd7jdNHHxdVAdVuW5vM__6DU99SdS38b03jXjkj?key=-LGNq3k7xufJJBHkVFXMZw align="center")

This is a simple way to control how much of the constructor runs, based on a condition.

## **Conclusion**

In this blog, we have understood many different topics, what a constructor is, its different types, like default constructor, no argument constructor, parameterised constructor and copy constructor, not only with theory but with code examples as well.

Understanding them will not only enhance our understanding but also help us write modular and well-maintained code in Java. While this concept is also important in OOP, as it is centred around the concept of objects and constructors are the ones that are used to initialise them.

## **Frequently Asked Questions**

**Q1. Why do we use constructors?**

**A:** We use constructors because:

1. They are created automatically by the compiler and initialise the object with default values.
    
2. We can initialise all the attributes of the objects in one go.
    
3. They prevent incomplete or incorrect object initialisation by ensuring that important data is provided during object creation.
    
4. Code maintainability and modularity increase.
    
5. We can use objects as soon as they are created.
    

**Q2. What is the basic difference between Method Overloading and Constructor Overloading?**

**A:** 

<table><tbody><tr><td colspan="1" rowspan="1"><p><strong>Feature</strong></p></td><td colspan="1" rowspan="1"><p><strong>Method Overloading</strong></p></td><td colspan="1" rowspan="1" colwidth="256"><p><strong>Constructor Overloading</strong></p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Purpose</strong></p></td><td colspan="1" rowspan="1"><p>To perform different operations with the same method name</p></td><td colspan="1" rowspan="1" colwidth="256"><p>To create objects with different initialisations</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Return Type</strong></p></td><td colspan="1" rowspan="1"><p>Can have a return type</p></td><td colspan="1" rowspan="1" colwidth="256"><p>Has no return type</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Name</strong></p></td><td colspan="1" rowspan="1"><p>Can be any valid method name</p></td><td colspan="1" rowspan="1" colwidth="256"><p>Always has the same name as the class</p></td></tr><tr><td colspan="1" rowspan="1"><p><strong>Usage Context</strong></p></td><td colspan="1" rowspan="1"><p>Called on existing objects</p></td><td colspan="1" rowspan="1" colwidth="256"><p>Called when creating objects</p></td></tr></tbody></table>

You can check out some of my other beginner-friendly articles on my blog:

1. [Understanding abstraction in Java](https://tekolio.com/what-is-abstraction-in-java-and-how-to-achieve-it/)
    
2. [How to build a Movie App in React using TMDB API?](https://tekolio.com/how-to-build-a-movie-app-in-react-using-tmdb-api/)
    
3. [How to merge two sorted arrays](https://tekolio.com/how-to-merge-two-sorted-arrays/)
