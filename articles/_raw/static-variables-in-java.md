---
title: Static Variables in Java – Why and How to Use Static Methods
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-03-07T15:57:36.000Z'
originalURL: https://freecodecamp.org/news/static-variables-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/markus-spiske-AaEQmoufHLk-unsplash--1-.jpg
tags:
- name: Java
  slug: java
seo_title: null
seo_desc: "Static variables and static methods are two important concepts in Java.\
  \ \nWhenever a variable is declared as static, this means there is only one copy\
  \ of it for the entire class, rather than each instance having its own copy. A static\
  \ method means it ..."
---

Static variables and static methods are two important concepts in Java. 

Whenever a variable is declared as static, this means there is only one copy of it for the entire class, rather than each instance having its own copy. A static method means it can be called without creating an instance of the class. 

Static variables and methods in Java provide several advantages, including memory efficiency, global access, object independence, performance, and code organization. 

In this article, you will learn how static variables work in Java, as well as why and how to use static methods.

## The Static Keyword in Java

The static keyword is one of the most essential features in the Java programming language. We use it to define class-level variables and methods. 

Here is an example of how to use the static keyword:

```java
public class StaticKeywordExample {
  private static int count = 0; // static variable  

  public static void printCount() { // static method
    System.out.println("Number of Example objects created so far: " + count);
  }
}

```

As you can see above, we declared the **count** variable as a static variable, while we declared the **printCount** method as a static method. 

When a variable is declared static in Java programming, it means that the variable belongs to the class itself rather than to any specific instance of the class. This means that there is only one copy of the variable in memory, regardless of how many instances of the class are created. 

Here's an example. Say we have a **Department** class that has a static variable called **`numberOfWorker`**. We declare and increment the static variable at the constructor level to show the value of the static variable whenever the class object is created.

```java
public class Department{
    public static int numberOfWorker= 0;
    public String name;
    
    public Department(String name) {
        this.name = name;
        numberOfWorker++; // increment the static variable every time a new 							//Person is created
    }
}

```

The results of the above code show that as we create new Department objects, the static variable `numberOfWorker` retains its value. 

When we print out the value of `numberOfWorker` in the console, we can see that it retains its value across all instances of the `Department` class. This is because there is only one copy of the variable in memory, and any changes to the variable will be reflected across all instances of the class.

```java
Department dpt1 = new Department("Admin");
System.out.println(Department.numberOfWorker); // output: 1

Department dpt2 = new Department ("Finance");
System.out.println(Department.numberOfWorker); // output: 2

Department dpt3 = new Department ("Software");
System.out.println(Department.numberOfWorker); // output: 3

```

We can also use the `static` keyword to define static methods. 

Static methods are methods that belong to the class rather than to any specific instance of the class. Static methods can be called directly on the class itself without needing to create an instance of the class first. See the code below:

```java
public class Calculation{
    public static int add(int a, int b) {
        return a + b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }
}

```

In the above code, the `Calculation` class has two static methods. The declared static methods can be called directly on the Calculation class without creating an instance of the class first. That is to say, you do not need to create an object of the Calculation class before you access the static `add` and `multiply` classes.

```java
int result = Calculation.add(5, 10);
System.out.println(result); // Output: 15

int result2 = Calculation.multiply(5, 10);
System.out.println(result2); // Output: 50

```

The `main()` method in Java is an example of a static method. The `main()` method is a special static method that is the entry point for Java applications. The `Math` class in Java also provides many static methods that perform mathematical operations.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

int result = Math.max(5, 10);
System.out.println(result); // Output: 10

```

The above code shows that the entry point for Java applications is a static method. It also shows that the `max()` method is a static method of the Math class and does not require an instance of the Math class to be created. 

As you can see, static methods can be useful in providing utility functions that do not necessitate the creation of a class object.

## Conclusion

The static keyword is a powerful tool in Java that can help solve many programming challenges. It aids in memory consumption management, improves code consistency, and helps speed up applications. 

To prevent unforeseen issues from cropping up in the code, it is crucial to use the static keyword wisely and be aware of its limitations. 

Code that relies heavily on static variables and methods can be harder to test because it introduces dependencies between different parts of the program. Static variables and methods can introduce hidden dependencies between different parts of the program, making it harder to reason about how changes in one part of the code might affect other parts. 

Code that relies heavily on static variables can also be less flexible and harder to extend over time. Static variables can also lead to concurrency issues if multiple threads access and modify the same variable at the same time. 

Lastly, if a static variable is not properly released or disposed of when it is no longer needed, it can lead to memory leaks and other performance issues over time. 

By using static variables and methods appropriately, you can create efficient and maintainable code that will be easier to work with over time.

Happy coding!

