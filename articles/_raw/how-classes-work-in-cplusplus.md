---
title: How Classes Work in C++
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2021-03-09T01:48:00.000Z'
originalURL: https://freecodecamp.org/news/how-classes-work-in-cplusplus
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60424789a7946308b7682566.jpg
tags:
- name: C++
  slug: c-2
- name: class
  slug: class
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: null
seo_desc: "C++ supports Object Oriented Programming, and classes and objects are the\
  \ heart of this programming paradigm. \nYou might be wondering – what is a class\
  \ and why do we need them? In this article I'll go over some basics to help you\
  \ understand how class..."
---

C++ supports Object Oriented Programming, and classes and objects are the heart of this programming paradigm. 

You might be wondering – what is a class and why do we need them? In this article I'll go over some basics to help you understand how classes work in C++.

## How Classes Work in C++

C++ has various built in types (like `bool`, `int`, `floats`, and so on). Each of these types has various features (for example, the size of their memory occupancy). Operators have different meanings for each different type.

For example: The '+' operator  adds ints, floats, and doubles:

```c++
int x = 5;
int y = 6;

int z= x+y;//z==11
```

However if we use the '+' operator with strings, it concatenates those strings.

```c++
string s1 = "abhilekh";
string s2 = "gautam";

string s3=s1+s2;//s3 will be abhilekhgautam
```

Here, x, y, and z represent an integer, while s1, s2, and s3 represent strings. So x, y, and z are objects of type `int`. Meanwhile s1, s2, and s3 are objects of type `string`.

**Note: don't confuse this with the word 'Object'**. An object is anything that occupies memory.

But what if we want to have a type that represents objects in our daily life? How could you represent a house, a car, books, animals, and so on? This is why we need Classes.

**A class is a user defined type**. This means that you can define your own types. You can make your own types like ints, floats, and chars. You can define operators for your types and set various properties for your own types.

Classes are really a powerful feature. Let's see how they work:

```c++
class Book{
string author_name,title;
int no_of_pages,edition_no;
//...
};
```

Here we have created a class named Book. The keyword class is enough for us to understand that.

A book must have an author, a title, and pages – these are the members of our class. Here, `book` represents an entity which has those features. 

But creating our own type won't be useful until we have an object of that type. So how do we do that?

```c++
int x;//x is an object of type x.

Book y;//y is an object of type Book
```

The only difference here is that x is an object of a built-in type (that is, `int`) and y is an object of the type Book (Book is a user-defined type, defined by you).

So now let's discuss the basics of defining a class, how to create objects of that class, and ways we can use those objects.

## What Are Member Functions in C++?

Functions declared in a class are member functions. They can only be invoked by the object of the class in which the function is defined.

Let's now update our `Book` class a little bit:

```c++
class Book{
//..
public:
void update_edition(int edition);
//..
};
```

Thats it – `update_edition` is a member function of our class book. We can define our function in two ways: inside the class, and outside the class.

Let's see how each of them works:

```c++
/*Inside class declaration*/
class Book{
//..
public:
void update_edition(int edition){
//Define your function 
edition_no = edition;
}
};
```

```c++
/* Outside Class declaration*/
void Book::update_edition(int edition){
//Define your function here
//..
}
```

So what about calling the function?

```c++
Book y;//y is an object of type Book

y.update_edition(5);
```

Remember that only the objects of type Book can invoke the function. **A call from objects of any other type will result in a syntactical error.**

A (non-static) member function always knows the object for which it was invoked and can refer to it like this:

```c++
void Book::update_edition(int edition){
this->edition_no = edition;
}
```

## Types of Member Functions in C++

There are a number of types of member functions in C++. Let's look at each one in more detail here.

### Constant Member Functions

```c++
class Book{
//..
public:
//..
int display_edition() const{
return edition_no;
}
//..
};
```

The `const` keyword indicates that this function does not change the state of the function.

Changing the state of the function from constant member function will result in an error.

```c++
int Book::book_edition() const{
edition_no = edition_no + 1;//error:cannot change value in constant function
}
```

### Static Member Functions

If you have a member function that needs access to the members of the class but does not need to be invoked by each and every object of that class, you should declare it as static.

Such functions will be part of the class but will not be part of the object.

```c++
class Book{
//..
public:
static void my_static_func();
};
```

A static member can be referred to without using an object.

```
void Book::my_static_func(){
//define here.
}
```

The **static** keyword should not be repeated in the function declaration. Static member functions do not have access to the **`this`** pointer.

### Friend Functions

Friend functions are not within the scope of a class and don't have any access to **`this`**.

```c++
class Book{
//..
public:
//..
void check();
void display();
//..
};

class E_book{
//..
public:
//..
friend void Book::check();
};
```

Here, the member function `check` of class `Book` is a friend of class `E_book`.

If we want all the member functions of a class to be the friend of another class, we can use the following syntax:

```c++
class E_book{
//...
public:
//..
friend class Book;
};
```

Now all the functions of class `Book` are now friends to class `E-book`.

### Access Specifiers

If you have a background in C, you might remember creating your own type using the **struct** keyword.

```c,c++
struct Book{
char author_name[20];
char title[20];
int no_of_page,edition_no;
};

Book b1;//b1 is an object of type Book
```

Structure is a user defined type. In fact, **structure is a type of class that has all its members public by default.** Confused?

Do you remember the **`public:`** label we used in one of our previous code snippets above? That is what we call an access specifier.

So what's the difference between private and public access specifiers?

Members after a `private` label are said to be private members. This means that they can only accessed by the member function of that class. If no label is provided, it is private by default.

On the other hand, members after `public` label are accessible everywhere.

These specifiers are used for the purpose of **data hiding**, **data abstraction,** and **data encapsulation**.

### Constructors

A constructor is a member function which is used to initialize an object. A constructor is run whenever an object of that class type is created. 

The name of the constructor function is the same as the name of the class and it does not have any return type, either.

```c++
class Book{
//..
public:
//Constructor

Book(){  //no return type and name same as the class name

//define constructor here

}
};
```

There can be multiple constructor of a class because there can be multiple functions with the same name reffered as function overloading.

### Destructors

The destructor releases the memory occupied by the object. It simply destroys the object. The `~` (tilde) symbol denotes a destructor.

```c++
class Book{
//..
public:
//constructor
//..
//destructor
~Book(){
//destroy object here
}
};
```

## That's it!

By using these various class concepts in c++, you can easily create new types (your own types) which you can conveniently use as built in types.

You can read my other articles [here](https://abhilekhblogs.blogspot.com/).

