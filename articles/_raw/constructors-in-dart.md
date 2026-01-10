---
title: Constructors in Dart – Use Cases and Examples
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2021-03-29T19:53:46.000Z'
originalURL: https://freecodecamp.org/news/constructors-in-dart
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60591ab5687d62084bf6a7c6.jpg
tags:
- name: Dart
  slug: dart
seo_title: null
seo_desc: "Most of us are familiar with the concept of constructors. They allow us\
  \ to create different instances of our classes. We can specify which parameters\
  \ the class should depend on when it is being instantiated and hide inner initialization\
  \ logic. \nWe ca..."
---

Most of us are familiar with the concept of constructors. They allow us to create different instances of our classes. We can specify which parameters the class should depend on when it is being instantiated and hide inner initialization logic. 

We can have many constructors for different use cases, or we can rely on the default one. 

In dart, constructors play a similar role, but have several variations that do not exist in most programming languages. This article will go over the different use cases and examples of constructors.

In all of the examples for this article, we will be using the following class:

```dart
class Car {
   String make;
   String model;
   String yearMade;
   bool hasABS;
}
```

## How to Get Started with Constructors in Dart

If you do not specify any constructor in Dart, it will create a default constructor for you. 

This does not mean that you will see a default constructor generated in your class. Instead, when creating a new instance of your class, this constructor will be called. It will have no arguments and will call the constructor of the super class, with no arguments as well.

To declare a constructor in your class, you can do the following:

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(String make, String model, int year, bool hasABS) {
    	this.make = make;
      	this.model = model;
      	this.yearMade = year;
      	this.hasABS = hasABS;
   	}
}
```

As you can imagine, there must be a better way to initialize our class fields – and in Dart, there is:

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(this.make, this.model, this.yearMade, this.hasABS);
}
```

The way we use above is just syntactic sugar that Dart has to simplify the assignment.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-321.png)
_Photo by [Unsplash](https://unsplash.com/@lin_alessio?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Alessio Lin</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

## More Complex Constructor Features

In other languages, it is possible to overload your constructor. This means that you can have different constructors with the same name, but with a varying signature (or different set of arguments). 

### Named constructors in Dart

In Dart, this is not possible, but there is a way around it. It is called **named constructors**. Giving your constructors different names allows your class to have many constructors and also to better represent their use cases outside of the class.

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(this.make, this.model, this.yearMade, this.hasABS);
   
   	Car.withoutABS(this.make, this.model, this.yearMade): hasABS = false;
}
```

The constructor **withoutABS** initializes the instance variable hasABS to false, before the constructor body executes. This is known as an **initializer list** and you can initialize several variables, separated by a comma. 

The most common use case for initializer lists is to initialize final fields declared by your class.

> ✋ Anything that is placed on the right hand side of the colon (:) has no access to **this**.

### Factory constructors in Dart

A factory constructor is a constructor that can be used when you don't necessarily want a constructor to create a new instance of your class. 

This might be useful if you hold instances of your class in memory and don't want to create a new one each time (or if the operation of creating an instance is costly). 

Another use case is if you have certain logic in your constructor to initialize a final field that cannot be done in the initializer list.

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	factory Car.ford(String model, String yearMade, bool hasABS) {
    	return FordCar(model, yearMade, hasABS);
    }
}

class FordCar extends Car {
	FordCar(String model, String yearMade, bool hasABS): super("Ford", model, yearMade, hasABS);
 
}
```

## Advanced Constructors in Dart

### Constant constructors and redirecting constructors in Dart

Dart also allows you to create constant constructors. What does this mean exactly? If your class represents an object that will never change after its creation, you can benefit from the use of a constant constructor. You have to make sure that all your class fields are final.

```dart
class FordFocus {
   static const FordFocus fordFocus = FordFocus("Ford", "Focus", "2013", true);
   
   final String make;
   final String model;
   final String yearMade;
   final bool hasABS;
   
   const FordFocus(this.make, this.model, this.yearMade, this.hasABS);
   
}
```

When you want one constructor to call another constructor under the hood, it's referred to as **redirecting constructors**.

```dart
class Car {
	String make;
   	String model;
   	String yearMade;
   	bool hasABS;
   
   	Car(this.make, this.model, this.yearMade, this.hasABS);
   
   	Car.withoutABS(this.make, this.model, this.yearMade): this(make, model, yearMade, false);
}
```

## Wrapping up

Each of the constructors we discussed has a different purpose and use case. It is up to you to determine and understand when to use each one. Hopefully, this article gave you the necessary knowledge to do so.

