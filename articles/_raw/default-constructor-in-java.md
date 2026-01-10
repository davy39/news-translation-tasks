---
title: Default Constructor in Java – Class Constructor Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-13T16:53:28.000Z'
originalURL: https://freecodecamp.org/news/default-constructor-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/default-constructor.png
tags:
- name: Java
  slug: java
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: 'In this article, we will talk about constructors, how to create our own
  constructors, and what default constructors are in Java.

  What is a constructor?

  As a class-based object-oriented programming term, a constructor is a unique method
  used to initia...'
---

In this article, we will talk about constructors, how to create our own constructors, and what default constructors are in Java.

## What is a constructor?

As a class-based object-oriented programming term, a constructor is a unique method used to initialize a newly created object (class). There are a few rules you must follow when creating constructors. These rules include:

* The name of the constructor must be the same as the class name.
* The constructor must have no return type.

Before we proceed, let's see what a class looks like in Java:

```java
public class Student {
  String firstName;
  String lastName;
  int age;
}
```

The code above shows a class called Student with three attributes – `firstName`, `lastName`, and `age`. We will assume that the class is supposed to be a sample for registering students. Recall that the three attributes do not have any values so none of the information is hard coded.

Now we will use constructors to create a new instance of our `Student` object. That is:

```java
public class Student {
  String firstName;
  String lastName;
  int age;

  //Student constructor
  public Student(){
      firstName = "Ihechikara";
      lastName = "Abba";
      age = 100;
  }
  
  public static void main(String args[]) {
      Student myStudent = new Student();
      System.out.println(myStudent.age);
      // 100
  }
}
```

We have created a constructor which we used to initialize the attributes defined in the `Student` object. The code above is an example of a **no-argument** constructor. Let's see an example of a different kind now:

```java
public class Student {
  String firstName;
  String lastName;
  int age;
  
  //constructor
  public Student(String firstName, String lastName, int age){
      this.firstName = firstName;
      this.lastName = lastName;
      this.age = age;
  }
  
  public static void main(String args[]) {
    Student myStudent = new Student("Ihechikara", "Abba", 100);
    System.out.println(myStudent.age);
  }

}
```

Now we have created a **parameterized constructor**. A parameterized constructor is a constructor created with arguments/parameters. Let's break it down.

```java
public Student(String firstName, String lastName, int age){
      
  }
```

We created a new constructor that takes in three arguments – two strings and an integer. 

```java
this.firstName = firstName;
this.lastName = lastName;
this.age = age;
```

We then linked these arguments to the attributes we defined when we created our class.  Now we have initialized the Student object using a constructor.

```java
public static void main(String args[]) {
    Student myStudent = new Student("Ihechikara", "Abba", 100);
    System.out.println(myStudent.age);
  }
```

Lastly, we created a new instance of the Student object and passed in our arguments. We were able to pass in these arguments because we had already defined them in a constructor.

I created one constructor with three arguments, but you can also create separate constructors for initializing each attribute.

Now that you know what a constructor is in Java and how to use it, let's now look into default constructors. 

## What is a default constructor?

A default constructor is a constructor created by the compiler if we do not define any constructor(s) for a class. Here is an example:

```java
public class Student {
  String firstName;
  String lastName;
  int age;
  
  public static void main(String args[]) {
      Student myStudent = new Student();
      
      myStudent.firstName = "Ihechikara";
      myStudent.lastName = "Abba";
      myStudent.age = 100;
      
      System.out.println(myStudent.age);
      //100
      
      System.out.println(myStudent.firstName);
      //Ihechikara
  }
}
```

Can you spot the difference between this and the two previous examples? Notice that we did not define any constructor before creating  `myStudent` to initialize the attributes created in the class.

This will not throw an error our way. Rather, the compiler will create an empty constructor but you will not see this constructor anywhere in the code – this happens under the hood. 

This is what the code above will look like when the compiler starts doing its job:

```java
public class Student {
  String firstName;
  String lastName;
  int age;
  
  
  /* empty constructor created by compiler. This constructor will not be seen in your code */
  Student() {
  
  }
  
  public static void main(String args[]) {
      Student myStudent = new Student();
      
      myStudent.firstName = "Ihechikara";
      myStudent.lastName = "Abba";
      myStudent.age = 100;
      
      System.out.println(myStudent.age);
      //100
      
      System.out.println(myStudent.firstName);
      //Ihechikara
  }
}
```

A lot of people mix up the default constructor for the no-argument constructor, but they are not the same in Java. Any constructor created by the programmer is not considered a default constructor in Java.

## Conclusion

In this article, we learned what constructors are and how we can create and use them to initialize our objects. 

We also talked about default constructors and what makes them different from no-argument constructors. 

Happy Coding!

