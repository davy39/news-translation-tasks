---
title: Object Oriented Programming Basics – OOP, Classes, and Objects in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-02T07:33:30.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-basics-oop-classes-and-objects-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Gradient-Modern-Digital-Marketing-Facebook-Cover--51-.png
tags:
- name: Java
  slug: java
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: 'By Avdhoot Fulsundar

  Java is a powerful programming language to develop software in. And if you''re trying
  to learn it, that''s great.

  The first thing you''ll need to know to develop software in Java is Object Oriented
  Programming, or OOP for short.

  Now...'
---

By Avdhoot Fulsundar

Java is a powerful programming language to develop software in. And if you're trying to learn it, that's great.

The first thing you'll need to know to develop software in Java is Object Oriented Programming, or OOP for short.

Now if you're asking yourself, "What is OOP?" don't worry. We'll cover the key concepts now.

## What is Objected Oriented Programming?

An object oriented language has two very important things: classes and objects. You use both when you're writing any type of program in Java.

OOP allows you to create a reusable blocks of code called objects. You can think of them as small machines.

Imagine you're building a car. You can't just throw all the parts together and hope they magically work. 

Instead, you break down the car into smaller parts like the engine, wheels, and chassis. Each of these parts has a specific job to do and can be worked on independently.

Similarly, OOP allows you to break up a large program into smaller pieces of code. This makes the code easier to understand and maintain.

Alright, so what are classes and objects? 😶

### What are Classes in Java?

Classes are simply blueprints for creating objects. Think of a class like an architect's blueprint for building a house.

An architect's blueprint defines the structure, layout, and shape of the house. Similarly, a class defines the structure and behavior of an object.

You can also think of a class as a recipe for creating objects. Just like a recipe tells you what ingredients to use, how to prepare them, and how long to cook them for, a class tells you what properties the object has, what it can do, and so on.

The beauty of classes is that they allow you to create objects that behave in a consistent and predictable way.

A class has its own attributes, objects, and methods.

In simple terms:

* **Attributes**: What the class looks like
* **Methods**: What the class does
* **Objects**: What the class is

Let's say you define a class called `Avengers`.

The first question is, what will it look like (that is, what are its attributes)?

The `Avengers` class will have a special suit, an amazing weapon, and an incredible origin story. 🦸‍♀️ These are the attributes of the `Avengers` class.

Let's take a closer look at attributes now.

## What are Attributes?

Imagine you have a puzzle. Each puzzle piece has its own unique shape, color, and design.

In OOP, attributes are like the different characteristics of a puzzle piece. They define the properties of an object, just like how the shape, color, and design of a puzzle piece define its role in completing the puzzle.

Similar to how the shape of each puzzle piece determines where it fits, attributes help define the identity and purpose of an object. For example, a cat object may have attributes like breed, age, and fur color, while a book object may have attributes like title, author, and genre.

These attributes help differentiate one object from another, and their unique attributes to create a complete program.

Let's return to our three questions. The next thing to ask is what will an Avenger do?

An Avenger will save the world, defeat the villains, do impossible tasks, pretend to be a normal human being, and lots of other things.

These are the methods of the `Avengers` class.

## What are Methods?

In OOP, methods define the actions that objects can perform.

Methods can take arguments, just like functions, and they can also return values. This allows objects to interact with other objects and perform complex tasks within a program.

For example, a car object may have methods like `start_engine()` and `stop_engine()` to manipulate its attributes like speed and fuel level, while a bank account object may have methods like `deposit()` and `withdraw()` to manipulate its balance.

The final question is who will be an Avenger?

Well, you could have Ironman, Captain America, Superman, and...

![Homelander from The Boys](https://www.freecodecamp.org/news/content/images/2023/04/image-150.png)
_Homelander from The Boys_

Sorry, not him. He's kinda evil. 😅

All the superheroes mentioned above (except Homelander) are objects of the class `Avengers`.

But what are objects, technically?

## What are Objects?

Imagine you are planning a once in a lifetime road trip with your friends, and you want to pack all the necessary items for the journey. 

You start by making a list of all the things you need, like snacks, drinks, clothes, and so on.

In object oriented programming (OOP), objects are like the items on your packing list. They have their own unique characteristics and behaviors.

Like a bag of chips has a specific flavor, size, and nutritional information, an object in OOP has its own set of attributes and methods.

Or similar to how you can use different items on your road trip for different purposes, objects can also be used in different ways within a program. For example, you can use a car object to drive from one place to another, or a music player object to listen to your favorite tunes.

So, think of objects in OOP as the building blocks that make up a program, each with their own distinct personality and purpose, just like the items on your packing list.

Alright, do you understand the basic concepts? Now let's write some code.

## How to Create a Class

First, we'll use the Avengers example and create an `Avengers` class:

```java
class Main {
    public static void main(String[] args) {

    }
}

class Avengers {

}

```

Now we'll create some attributes for our own Superhero:

```java
class Avengers {
    String name;
    int power;
    
}

```

And we'll create a method for our superhero so they can stop villains:

```java
class Avengers {
    String name;
    int power;

    void Punch() {
        System.out.println("I can do this all day.");
    }
}

```

Then let's create a Captain America object:

```java
class Main {
    public static void main(String[] args) {
        Avengers hero1 = new Avengers();
        hero1.name = "Captain America";
        System.out.println(hero1.name);
    }
}

```

Here's the syntax to create an object:

```java
ClassName ObjectName = new ClassName();
```

In the code above, I've created an object of the class `Avengers` called `hero1`.

As you can see, by using the dot operator (`.`) I have assigned a value to the `name` variable of the `hero1` object.

Let's call the method `punch` to see if our Captain America can really stop villains:

```java
class Main {
    public static void main(String[] args) {
        Avengers hero1 = new Avengers();
        hero1.name = "Captain America";
        System.out.println(hero1.name);

        // Calling the method on hero1
        hero1.Punch();
    }
}

```

Finally, when you run your code, you'll see this output:

```shell
$ java -classpath .:target/dependency/* Main
Captain America
I can do this all day.

```

Hurray! It looks like our own personal Captain America can actually save the world. 😁

## Wrapping Up

I hope you enjoyed learning about how to create your own Avenger with OOP in Java. Create your own superhero and give them some awesome powers. 😎

If you want to chit chat about web or software development, then you can connect with me on [LinkedIn](https://www.linkedin.com/m/in/avdhoot-fulsundar). 😉 I share awesome tips about content marketing, too.

