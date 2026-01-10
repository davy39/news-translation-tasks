---
title: SOLID Definition – the SOLID Principles of Object-Oriented Design Explained
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-26T21:16:00.000Z'
originalURL: https://freecodecamp.org/news/solid-principles-single-responsibility-principle-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/solid.jpg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: solid
  slug: solid
seo_title: null
seo_desc: "The SOLID design principles help us create maintainable, reusable, and\
  \ flexible software designs. Each letter in the acronym SOLID stands for a specific\
  \ principle. \nHere is what each letter in the acronym stands for:\n\nS: Single\
  \ responsibility princip..."
---

The **SOLID** design principles help us create maintainable, reusable, and flexible software designs. Each letter in the acronym **SOLID** stands for a specific principle. 

Here is what each letter in the acronym stands for:

* **S**: Single responsibility principle.
* **O**: Open–closed principle.
* **L**: Liskov substitution principle.
* **I**: Interface segregation principle.
* **D**: Dependency inversion principle.

In this article, we'll start by defining each principle and then we'll see some examples to help you understand how and why you should use these principles in your code. 

The examples we will use in this article are going to be very basic. We will be using Java for our examples.

We'll conclude this article by talking about the basics of object oriented design.

## The Single Responsibility Principle (SRP)

The idea behind the SRP is that every class, module, or function in a program should have one responsibility/purpose in a program. As a commonly used definition, "every class should have only one reason to change". 

Consider the example below:

```java
public class Student {

     public void registerStudent() {
         // some logic
     }

     public void calculate_Student_Results() {
         // some logic
     }

     public void sendEmail() {
         // some logic
     }

}
```

The class above violates the single responsibility principle. Why?

This `Student` class has three responsibilities – registering students, calculating their results, and sending out emails to students.

The code above will work perfectly but will lead to some challenges. We cannot make this code reusable for other classes or objects. The class has a whole lot of logic interconnected that we would have a hard time fixing errors. And as the codebase grows, so does the logic, making it even harder to understand what is going on. 

Imagine a new developer joining a team with this sort of logic with a codebase of about two thousand lines of code all congested into one class. 

Now let's fix this!

```java
public class StudentRegister {
    public void registerStudent() {
        // some logic
    }
}

```

```java
public class StudentResult {
    public void calculate_Student_Result() {
        // some logic
    }
}
```

```java
public class StudentEmails {
    public void sendEmail() {
        // some logic
    }
}

```

Now we've separated each functionality in our program. We can call the classes anywhere we want to use them in our code. 

The examples we used use just showed each class having one method – this is mainly for simplicity. You can have as many methods as you want but they should be linked to the responsibility of the class.

Now that we have separated the logic, our code is easier to understand as each core functionality has its own class. We can test for errors more efficiently.

The code is now reusable. Before, we could only use these functionalities inside one class but now they can be used in any class. 

The code is also easily maintainable and scalable because instead of reading interconnected lines of code, we have separated concerns so we can focus on the features we want to work on.

## Open–Closed Principle (OCP)

The open-closed principle states that software entities should be open for extension, but closed for modification. 

This implies that such entities – classes, functions, and so on – should be created in a way that their core functionalities can be extended to other entities without altering the initial entity's source code. 

In the example below, we're going to write the code for calculating the body mass index (BMI) of a person:

```java
public class Human  {
    
     public int height;
     public int weight;
     
}
```

We've created the `Human` class which provides the `height` and `width` properties of the class. Now, let's calculate the first person's BMI.

```java
public class CalculateBMI {

     public int CALCULATE_JOHN_BMI(Human John) {   
         
         return John.height/John.weight;
         
     }
}
```

We've calculate the BMI of a person named `John`. We'll go on and calculate the BMI for a person named `Jane`. 

```
public class CalculateBMI {

     public int CALCULATE_JOHN_BMI(Human John) {   
         
         return John.height/John.weight;
         
     }
     
     public int CALCULATE_JANE_BMI(Human Jane) {   
         
         return Jane.height/Jane.weight;
         
     }
}
```

The problem with this is that we keep modifying the code every time we need to calculate the BMI of another person. 

This also violates the SRP because the class now has more than one reason to change.

Although the code above may work perfectly, it's not efficient. We modify the code constantly which may lead to bugs. And the code only has provision for humans. What if we have to calculate for an animal or an object?

Let's fix the problem using the open-closed principle.

```java
public interface Entity {

     public int CalculateBMI();

}

// John entity
public class John implements Entity {

     int height;
     int weight;

     public double CalculateBMI() {

           return John.height/John.weight;
     }
}

// Jane entity
public class Jane implements Entity {

     int height;
     int weight;

     public double CalculateBMI() {

           return Jane.height/Jane.weight;
     }
}

// Dog entity
public class Dog implements Entity {

     int height;
     int weight;

     public double CalculateBMI() {

           return Dog.height/Dog.weight;
     }
}
```

In the code above, we have created an interface called `Entity` with a `CalculateBMI()` method. 

Each entity – `John`, `Jane` and `Dog` – extends the functionality of the `Entity` interface. 

Now we no longer have to modify existing code when we create a new entity - we just extend the functionality we need and apply it to the new entity. 

Next, we'll talk about the Liskov Substitution Principle. 

## Liskov Substitution Principle (LSP)

According to Barbara Liskov and Jeannette Wing, the Liskov substitution principle states that:

> _Let _Φ(x)_ be a property provable about objects _x_ of type _T_. Then _Φ(y)_ should be true for objects _y_ of type _S_ where _S_ is a subtype of _T_. (Source:_ [Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle#:~:text=Subtype%20Requirement%3A%20Let,a%20subtype%20of%20T)_)_

Don't worry if you find that confusing, it will all make sense soon. Let's simplify this principle below:

The Liskov substitution principle simply implies that when an instance of a class is passed/extended to another class, the inheriting class should have a use case for all the properties and behavior of the inherited class.

Let's say we have a class called `Amphibian` for animals that can live on both land and water. This class has two methods to show the features of an amphibian – `swim()` and `walk()`. 

```java
public class Amphibian {

    public void swim();
    public void walk();

}


```

The `Amphibian` class can extend to a `Frog` class because frogs are amphibians, so they can inherit the properties of the `Amphibian` class without altering the logic and purpose of the class.

```java
public class Frog extends Amphibian {
    public void swim() {
        System.out.println("The frog is swimming");
    }
    
    public void walk() {
        System.out.println("The frog is walking on land");
    }
}
```

But we cannot extend the `Amphibian` class to a `Dolphin` class because dolphins only live in water which implies that the `walk()` method would be irrelevant to the `Dolphin` class.

So, when you extend a class, if some of the properties of the initial class are not useful for the new class, the Liskov substitution principle has been violated.

The solution to this is simple: create interfaces that match the needs of the inheriting class.

In summary, if a class inherits another, it should do so in a manner that all the properties of the inherited class would remain relevant to its functionality.

## Interface Segregation Principle (ISP)

The interface segregation principle states that the interface of a program should be split in a way that the user/client would only have access to the necessary methods related to their needs. 

To understand this better, we'll first look at an example that violates the ISP:

```java
public interface Teacher {

    void English();

    void Biology();

    void Chemistry();
    
    void Mathematics();

}
```

We've created an interface called `Teacher` which has various subjects as its methods. Let's extend this interface to our first teacher. 

```java
public class Jane implements Teacher {

    @Override
    public void English() {
        System.out.println("Jane is teaching the students English language.");
    }

    @Override
    public void Biology() {
    }

    @Override
    public void Chemistry() {
    }

    @Override
    public void Mathematics() {
    }
}
```

From the code above, you can tell that `Jane` is an English teacher who has no business with the other subjects. But these other methods are extended by default with the `Teacher` interface. 

Do not confuse the Liskov substitution principle and the interface segregation principle. They may seem similar but they are not entirely the same.

Liskov substitution principle gives us the idea that when a new class has the need to inherit an existing class, it should do so because this new class has a need for the methods the existing class has.

On the other hand, the interface segregation principle makes us understand that it is unnecessary and unreasonable to create an interface with a lot of methods as some of these methods may be irrelevant to the needs of a particular user when extended.

Now let's fix the code in the last example.

```java
public interface Teacher {

    void Teach();

}
```

The `Teacher` interface now has only one method. Let's go on and extend this interface to support the different subjects. 

```java
// English teacher interface

public interface EnglishTeacher extends Teacher {

    void English();

}
```

```java
// Biology teacher interface

public interface BiologyTeacher extends Teacher {

    void Bilogy();

}
```

```java
// Chemistry teacher interface

public interface ChemistryTeacher extends Teacher {

    void Chemistry();

}
```

```java
// Mathematics teacher interface

public interface MathematicsTeacher extends Teacher {

    void Mathematics();

}
```

We have created different interfaces for every subject. Now `Jane` can teach English without carrying the other methods with them. Here is an example:

```java
public class Jane implements EnglishTeacher {
    
    @Override
    public void Teach() {
        System.out.println("Jane has started teaching.");
    }

    @Override
    public void English() {
        System.out.println("Jane is teaching the students English language.");
    }

}
```

## Dependency Inversion Principle (DIP)

The dependency inversion principle states:

> High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces). _(Source:_ [Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle#:~:text=Subtype%20Requirement%3A%20Let,a%20subtype%20of%20T)_)._

And,

> Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions. _(Source:_ [Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle#:~:text=Subtype%20Requirement%3A%20Let,a%20subtype%20of%20T)_)._

Let's use a real-life example before writing some code. 

Imagine taking a one minute walk to the bank every time you had to withdraw money over the counter. It then takes an extra thirty seconds for you get your money. This is quite efficient because very little time is wasted. We'll assume you're the high-level module and the bank is the low-level module. 

But what happens when the bank is closed for a holiday or an emergency? You have absolutely no access to your funds. If you move further away from the bank, it becomes a bigger problem because you'd spend more time getting there.

To solve this problem, an interface is introduced – an automated teller machine (ATM) or a mobile banking app. Even though you have a relationship with the bank, you are no longer required to interact with them physically to be served.

This example is similar to the dependency inversion principle. We should make our classes rely on properties in our interfaces instead of relying on each other. 

The implications of violating this principle would result in a rigid system where testing blocks of code independently would be very difficult, reusability of code would be near impossible, and the addition or removal of code would lead to further complexity of the system and introduce bugs.

Here is a code example that violates this principle:

```java
public class Bank {

    public void GIVE_CUSTOMER_MONEY_OTC() {
        // some logic
    }
}
```

```java
public class Customer {
    private Bank myBank = new Bank();
    
    public void withdraw() {
        myBank.GIVE_CUSTOMER_MONEY_OTC();
    }
}
```

From the code examples above, we can see that the `Customer` class imports and relies on a method in the `Bank` class. This reliance on a low-level class is against the DIP. 

Like in our real-life example, we'll solve this problem by introducing an interface that both classes can interact with. 

Here's the ATM interface that our `Bank` and `Customer` class will interact with:

```java
public interface ATM {
    void ATM_OPERATION();
}
```

Here's the `Bank` class which uses a method in the `ATM` interface to add money to the ATM:

```java
public class Bank implements ATM {
    @Override
    ATM_OPERATION(){
        // code to add money to ATM and increase the ATM balance
    }
}
```

Lastly, the `Customer` class which uses the same interface to withdraw money:

```java
public class Customer implements ATM {
    
    @Override
    ATM_OPERATION(){
        // code to withdraw money from ATM and decrease the ATM balance
    }
}
```

## What Is Object Oriented Design?

Object oriented design is a design methodology for building object-based systems and applications. This enables us to build systems with a collection of objects where each object has its own properties and methods.

Take the computer system as an example. Its hardware is made up of different parts that comprise the whole system.

Here are some of the general terms associated with object oriented design:

* **Objects**: Each separate unit that makes up the system is an object. Objects can have properties and methods.
* **Classes**: Classes act as a general description for objects. So an object is an instance of a class. 
* **Encapsulation**: this aids in bundling all the relevant data of an object in one unit. This also helps in restricting access to specific data and methods which should only be found in one object.
* **Inheritance**: Inheritance makes it easier for us to extend the functionality of a class to other classes.  This way, we do not repeat the process of creating these functionalities over and over again.
* **Abstraction**: This means showing only important attributes and hiding the irrelevant ones.
* **Polymorphism**: This is the existence of an interface in various forms. The ability to extend an object/interface but with different or addition attributes.

## Conclusion

There are so many ways to solve a problem. But there are also many ways to create problems from a solution.

The more rigid and coupled the classes and methods in our code are, the more difficult it would be to maintain and reuse our code.

Neglecting or violating these principles could pose a serious threat to not just the codebase and the developer, but to the organization that owns the product as well.

A rigid and tightly coupled codebase makes it difficult to add or remove features in a product, test and reuse blocks of code, and introduces possible breaking changes with every code modification made.

The SOLID principles act as a guide to help us create a flexible and dynamic product and we went over each principle in this article to help us understand how the objects we create should interact which each other.

I hope you find this article helpful as you continue your journey through object oriented design.

Happy coding!

