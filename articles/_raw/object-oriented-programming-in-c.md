---
title: Object Oriented Programming in C++
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-29T18:03:00.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-in-c
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e69740569d1a4ca3cf0.jpg
tags:
- name: c programming
  slug: c-programming
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: "Object oriented programming, OOP for short, aims to implement real world\
  \ entities like inheritance, hiding and polymorphism in programming. \nThe main\
  \ aim of OOP is to bind together the data and the functions that operate on them\
  \ so that no other part..."
---

Object oriented programming, OOP for short, aims to implement real world entities like inheritance, hiding and polymorphism in programming. 

The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

Let's learn about different characteristics of an Object Oriented Programming language.

### **Object:**

Objects are basic run-time entities in an object oriented system. Objects are instances of a class which are user defined data types.

```cpp
class person
{
    char name[20];
    int id;
public:
    void getdetails(){}
};
 
int main()
{
   person p1; //p1 is an object 
}
```

Objects take up space in memory and have an associated address like a record in pascal or a structure or union in C.

When a program is executed the objects interact by sending messages to one another.

Each object contains data and code to manipulate the data. Objects can interact without having to know the details of each others' data or code. It's enough to know the type of message accepted and type of response returned by the objects.

### **Class:**

A class is a blueprint of data and functions or methods. Class does not take any space.

```cpp
class class_name
{
  private:
     //data members and member functions declarations
  public:
     //data members and member functions declarations
  protected:
     //data members and member functions declarations
};
```

Class is a user defined data type like structures and unions in C.

By default class variables are private, but in case of structure they are public. In the above example, person is a class.

### **Encapsulation and Data abstraction:**

Wrapping up (combining) data and functions into a single unit is known as encapsulation. The data is not accessible to the outside world and only those functions which are wrapping the class can access it. This insulation of the data from direct access by the program is called data hiding or information hiding.

Data abstraction refers to providing only needed information to the outside world and hiding implementation details. 

For example, consider a class Complex with public functions getReal() and getImag(). We may implement the class as an array of size 2 or as two variables. 

The advantage of abstraction is that we can change implementation at any point and the users of the Complex class won’t be affected as our method interface remains same. Had our implementation been public, we would not have been able to change it.

### **Inheritance:**

Inheritance is the process by which objects of one class acquire the properties of objects of another class. It supports the concept of hierarchical classification. 

Inheritance provides reusability. This means that we can add additional features to an existing class without modifying it.

### **Polymorphism:**

Polymorphism refers to the ability to take more than one form. An operation may exhibit different behaviors in different instances. The behavior depends on the types of data used in the operation.

C++ supports operator overloading and function overloading. Operator overloading is the process of making an operator exhibit different behaviors in different instances. Function overloading is using a single function name to perform different types of tasks. Polymorphism is extensively used in implementing inheritance.

### **Dynamic Binding:**

In dynamic binding, the code to be executed in response to a function call is decided at runtime. C++ has virtual functions to support this.

### **Message Passing:**

Objects communicate with one another by sending and receiving information to each other. A message for an object is a request that a procedure be executed and therefore it will invoke a function in the receiving object that generates the desired results. 

Message passing involves specifying the name of the object, the name of the function and the information to be sent.

## More information

[Object Oriented Programming Concepts: How to go from Zero to One with Objects](https://www.freecodecamp.org/news/object-oriented-concepts/)

[How to Explain Object Oriented Programming Concepts to a 6 Year Old](https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/)

