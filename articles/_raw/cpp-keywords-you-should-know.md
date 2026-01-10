---
title: C++ Keywords You Should Know
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2021-03-22T16:39:23.000Z'
originalURL: https://freecodecamp.org/news/cpp-keywords-you-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/keyword.png
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: 'C++ has various keywords, and you should know what they are and how to
  use them. So in this article, I will be talking about some of the most important
  keywords you''ll find in the language.

  What are Keywords in C++?

  Keywords are certain reserved word...'
---

C++ has various keywords, and you should know what they are and how to use them. So in this article, I will be talking about some of the most important keywords you'll find in the language.

## What are Keywords in C++?

Keywords are certain reserved words which have a predefined meaning in C++. Since keywords have their own predefined meaning, they cannot be used as identifiers (for example, a function's name or a variable's name). 

The function definition below is an error because **friend** is a keyword in c++.

```c++
void friend(){
/*.......*/
}
```

Let's look at some of the common keywords in C++ and how they're used.

## C++ Keywords

### The `typedef` keyword in C++

Sometime it can be tedious to declare a variable of a certain type like this:

```c++
const unsigned char
```

Programmers have hard time declaring such variables, and they're too long to use frequently. Can't we make it shorter or create something different? Yes we can.

Using **`typedef`** we can create synonyms:

```c++
typedef const unsigned char CON_UCHAR;
```

So instead of using such long base types, like this:

```c++
const unsigned char x;
```

We can use this:

```c++
CON_UCHAR x;
```

**typedefs** are helpful for pointer declaration, too:

```c++
typedef char *const CON_PTRCHAR; //const pointer to char

typedef const char* PTR_CONCHAR; //pointer to const char
```

### The `bool` keyword in C++

**bool** is a type name which has two values – it is either **true** or **false.** 

Every non-zero value is **true**, while zero is **false.**

```c++
if(1){
std::cout<<"Hello World"<<'\n';
}
else{
std::cout<<"Sorry World<<'\n';
}
```

Since all non zero values are true, every time the program runs, it outputs **Hello World.**

Remember that the two bool values, **true** and **false**, are also keywords.

### The `using` keyword in C++

```c++
using namespace std;
```

You might have used the **using** keyword unknowingly. It can be used like this:

**`using-declaration`:**

```c++
namespace My_space{

class My_class{
/*Your code here*/
};
}

namespace Her_space{

using My_space:: My_class;

}
```

This is what a using declaration looks like. A using declaration brings every declaration with a given name to a scope.

**`using directive`:**

The most common example of a using directive is this:

```c++
using namespace std;
```

The above line of code makes every name from std namespace available.

### The `public`, `protected`, and `private` keywords in C++

The keywords **public**, **protected**, and **private** are used as access specifiers in a class.

```c++
class Home{
private:
int members;
protected:
double tot_expenditure;
public:
void display_detail();
};
```

The members after the **private** label are only accessible through member functions. If no label is provided, then it is private by default.

The members after the **public** label are accessible everywhere.

The members after the **protected** label are similar to **public** members for derived class and are similar to **private** members for non-derived class.

### The `enum` keyword in C++

An enumeration is a user defined type. We declare enumeration using the **enum** keyword.

```c++
enum days{SUN, MON, TUE, WED, THU, FRI, SAT};
```

Here, SUN, MON, TUE ... are called enumerators and their values are assigned increasing from 0.

By default, SUN==0, MON ==1 and so on.

However, we can initialize enumerators ourselves too.

```c++
enum{ a = 5, b = 6};
```

By default, enumerations are converted to integers for arithmetic operations. Since enums are _user defined types_, we can [overload operators for them](https://www.freecodecamp.org/news/how-to-overload-operators-in-cplusplus/), too.

### The `new` keyword in C++

The **new** keyword (also a operator) is used to create objects in free store (also referred to as heap).

```c++
int main(){

int *p = new int;

*p = 20;
//..

}


```

For the above line of code, the new operator allocates a memory for storing an object of integer type and returns a pointer pointing to that allocated address.

### The `delete` keyword in C++

Memory is an important resource for us. So we should use it wisely. Unwanted memory should not be occupied. So **delete** (also a operator) is used to deallocate memory that was previously allocated by the **new** operator.

```c++
int main(){

int *p = new int;
*p =20;

delete p;
//..

}
```

### The `this` keyword in C++

All the (non-static) member functions know for which object they were invoked and they can refer to it using the pointer **this**.

```c++
class A{
int b;
public:
//...
void display() const;
};
```

Consider a class which has a private member b and a member function display.

Our display function would be the following:

```c++
void A::display() const{
cout<<"b = "<<b<<'\n';
}
```

The same code above can be written using **this** like so:

```c++
void A::display() const{
cout<<"b = "<<this->b<<'\n';
}
```

Note that **this** is a pointer, so we should use the -> operator. Furthermore **this** here refers to the object which invoked the function.

### The `class` keyword in C++

C++ supports object oriented programming, so we have the concept of classes. The keyword **class** is used to declare / define a class.

```c++
class Fb_user{
//..your code here
};
```

**struct** is also a keyword. It's a class with all the members labelled public by default.

```c++
struct Fb_user{
//...Your code here
};
```

The above code is shorthand for this code:

```c++
class Fb_user{
public:
//..your code here
};
```

To learn more about classes you can refer to my in-depth article about classes [here](https://www.freecodecamp.org/news/how-classes-work-in-cplusplus/).

### The `operator` keyword in C++

The keyword **operator** is used while overloading operators. The syntax for overloading an operator is the following:

```c++
return_type operator operator's_symbol(parameters){
//...Your code here...
}
```

To learn more about overloading operators in c++ you can refer to my article [here](https://www.freecodecamp.org/news/how-to-overload-operators-in-cplusplus/).

### The `inline` keyword in C++

The keyword **inline** is used with functions which are expanded " in line " during every call.

A member function defined within the class definition is taken to be an inline function.

But we can use the keyword **inline** to inline a member function like this:

```c++
class Random(){
int a;
public:
int display const();
//...
};

inline int Random::display() const{
return a;
}
```

The 'inline' specification is just a request to the compiler to inline a function. The compiler may ignore that request.

### The `goto` keyword in C++

C++ also supports the **goto** keyword. **goto** is used as a jump statement to jump in and out of a block. The restriction is that we cannot jump into an exception handler. 

**goto** statements are useful for breaking out from a nested loop or any switch case statement.

```c++
int main(){

for(int i = 0 ; i < 5 ; i++){
  for(int j = 0 ; j < 5 ; j++{
    if(){//check for some condition
    goto here;
    }
  }
}

here:
cout<<"I am here"<<;

}
```

So basically we use goto to jump from one block to another.

It is a good idea to avoid using goto in general, though it can sometimes be useful.

## That's It!

These are some of the most common keywords in C++. I hope you had a good time reading about this (not the **this** pointer :) ) 

Happy Coding!

You can read my other blogs [here](https://abhilekhblogs.blogspot.com/).

