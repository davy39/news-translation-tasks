---
title: Why Static in Java? What does this keyword mean? [Solved]
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-24T21:38:54.000Z'
originalURL: https://freecodecamp.org/news/why-static-in-java-what-does-this-keyword-mean
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/radowan-nakif-rehan-cYyqhdbJ9TI-unsplash.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "You can use the static keyword in different parts of a Java program like\
  \ variables, methods, and static blocks. \nThe main purpose of using the static\
  \ keyword in Java is to save memory. When we create a variable in a class that will\
  \ be accessed by oth..."
---

You can use the `static` keyword in different parts of a Java program like variables, methods, and static blocks. 

The main purpose of using the `static` keyword in Java is to save memory. When we create a variable in a class that will be accessed by other classes, we must first create an instance of the class and then assign a new value to each variable instance – even if the value of the new variables are supposed to be the same across all new classes/objects. 

But when we create a static variables, its value remains constant across all other classes, and we do not have to create an instance to use the variable. This way, we are creating the variable once, so memory is only allocated once. 

You'll understand this better with the examples in the sections that follow.

In order to understand what the `static` keyword is and what it actually does, we'll see some examples that show its use in declaring static variables, methods, and blocks in Java. 

## How to Create a Static Variable in Java

To understand the use of the `static` keyword in creating variables, let's look at the usual way of creating variables shared across every instance of a class.

```java
class Student {
    String studentName; 
    String course; 
    String school;
        
    public static void main(String[] args) {
        Student Student1 = new Student();
        Student Student2 = new Student();
        
        Student1.studentName = "Ihechikara";
        Student1.course = "Data Visualization";
        Student1.school = "freeCodeCamp";
        
        Student2.studentName = "John";
        Student2.course = "Data Analysis with Python";
        Student2.school = "freeCodeCamp";
        
        System.out.println(Student1.studentName + " " + Student1.course + " " + Student1.school + "\n");
        // Ihechikara Data Visualization freeCodeCamp
        System.out.println(Student2.studentName + " " + Student2.course + " " + Student2.school);
        // John Data Analysis with Python freeCodeCamp
    }
}
```

I'll explain what happened in the code above step by step. 

We created a class called `Student` with three variables – `studentName`, `course`, and `school`. 

We then created two instances of the `Student` class:

```java
Student Student1 = new Student();
Student Student2 = new Student();
```

The first instance – `Student1` – which has access to the variables created in its class had these values: 

```java
Student1.studentName = "Ihechikara";
Student1.course = "Data Visualization";
Student1.school = "freeCodeCamp";
```

The second instance had these values: 

```java
Student2.studentName = "John";
Student2.course = "Data Analysis with Python";
Student2.school = "freeCodeCamp";
```

If you look closely, you'll realize that both students have the same school name – "freeCodeCamp". What if we had to create 100 students for the same school? That means we'd be initializing a variable with the same value 100 times – allocating new memory every time. 

While this may not appear to be a problem, in a much larger codebase, it could become a flaw and unnecessarily slow your program down.

To fix this problem, we'll use the `static` keyword to create the `school` variable. After that, all instances of the class can make use of that variable.

Here's how:

```java
class Student {
    String studentName; 
    String course; 
    static String school;
        
    public static void main(String[] args) {
        Student Student1 = new Student();
        Student Student2 = new Student();
        
        
        Student1.studentName = "Ihechikara";
        Student1.course = "Data Visualization";
        Student1.school = "freeCodeCamp";
        
        
        Student2.studentName = "John";
        Student2.course = "Data Analysis with Python";
        
        System.out.println(Student1.studentName + " " + Student1.course + " " + Student1.school + "\n");
        // Ihechikara Data Visualization freeCodeCamp
        System.out.println(Student2.studentName + " " + Student2.course + " " + Student2.school);
        // John Data Analysis with Python freeCodeCamp
    }
}
```

In the code above, we created a static variable called `school`. You'll notice that the `static` keyword preceded the data type and the name of the variable: `static String school = "freeCodeCamp";`. 

Now when we create a new instance of our class, we do not have to initialize the `school` variable for every instance. In our code, we only assigned a value to the variable in the first instance and it was inherited by the second instance as well.

Note that changing the value of the static variable anywhere in the code overrides the value in other parts of the code where it was declared previously. 

So you should only use the `static` keyword for variables that are supposed to remain constant in the program. 

You can also assign a value to the variable when it is created so you don't have to declare it again when you create a class instance: `static String school = "freeCodeCamp";`.

You'll have this if you use the method above:

```java
class Student {
    String studentName; 
    String course; 
    static String school = "freeCodeCamp";
        
    public static void main(String[] args) {
        Student Student1 = new Student();
        Student Student2 = new Student();
        
        
        Student1.studentName = "Ihechikara";
        Student1.course = "Data Visualization";
        
        Student2.studentName = "John";
        Student2.course = "Data Analysis with Python";
        
        System.out.println(Student1.studentName + " " + Student1.course + " " + Student1.school + "\n");
        // Ihechikara Data Visualization freeCodeCamp
        System.out.println(Student2.studentName + " " + Student2.course + " " + Student2.school);
        // John Data Analysis with Python freeCodeCamp
    }
}
```

In the last section, you'll see how to initialize static variables using static blocks.

## How to Create a Static Method in Java

Before we look at an example, here are some things you should know about static methods in Java: 

* Static methods can **only** access and modify static variables. 
* Static methods can be called/used without creating a class instance.

Here's an example to help you understand:

```java
class EvenNumber {
    
    static int evenNumber;
    
    static void incrementBy2(){
        evenNumber = evenNumber + 2;
        System.out.println(evenNumber);
    }
        
    public static void main(String[] args) {
        incrementBy2(); // 2
        incrementBy2(); // 4
        incrementBy2(); // 6
        incrementBy2(); // 8
    }
}
```

In the code above, we created an integer (`evenNumber`) in a class called `EvenNumber`. 

Our static method is named `incrementBy2()`. This method increases the value of the `evenNumber` integer and prints its value. 

Without creating a class instance, we were able to call the `incrementBy2()` method in the program's `main` method. Each time we called the method, the value of `evenNumber` was incremented by 2 and printed out.

You can also attach the name of the class to the method using dot notation while calling the method: `EvenNumber.incrementBy2();`. Every static method belongs to the class and not instances of the class.

## How to Create a Static Block in Java

Static blocks in Java are similar to constructors. We can use them to initialize static variables, and they are executed by the compiler before the `main` method. 

```java
class Block {
    
    static int year;
    
    static {
        year = 2022;
        System.out.println("This code block got executed first");
    }
        
    public static void main(String[] args) {
        
        System.out.println("Hello World");
        System.out.println(year);
    }
}

```

In the code above, we created a static integer variable `year`. We then initialized it in a static block:

```java
static {
        year = 2022;
        System.out.println("This code block got executed first");
    }
```

You can create a static block, as you can see above, using the `static` keyword followed by curly brackets. In the static block in our code, we initialized the `year` variable with a value of 2022. We also printed out some text – "This code block got executed first". 

In the `main` method, we printed "Hello World" and the static `year` variable. 

In the console, the code will be executed in this order: 

```txt
This code block got executed first
Hello World
2022
```

This demonstrates how the code in the static block is executed first before the `main` method. 

## Summary

In this article, we talked about the `static` keyword in Java. It is a keyword which mainly helps us optimize memory in our Java programs. 

We saw how to create static variables and methods with examples. 

Lastly, we talked about static blocks which you can use to initialize static variables. Static blocks get executed before the main method.

Happy coding!

