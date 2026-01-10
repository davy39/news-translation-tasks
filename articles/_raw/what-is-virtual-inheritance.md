---
title: What is Virtual Inheritance?
subtitle: ''
author: Abhilekh gautam
co_authors: []
series: null
date: '2023-02-23T21:09:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-virtual-inheritance
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-ruiyang-zhang-3717242.jpg
tags:
- name: C++
  slug: c-2
- name: inheritance
  slug: inheritance
seo_title: null
seo_desc: "C++ supports the concept of inheritance – that is, a class can inherit\
  \ properties from other classes. \nBut sometimes you might need to use what is commonly\
  \ referred as virtual inheritance. \nIn this article we will discuss when you might\
  \ need to use v..."
---

C++ supports the concept of inheritance – that is, a class can inherit properties from other classes. 

But sometimes you might need to use what is commonly referred as virtual inheritance. 

In this article we will discuss when you might need to use virtual inheritance and how to implement it in C++.

## What is Virtual Inheritance?

In C++, a class can inherit from multiple classes which is commonly referred as multiple inheritance. But this can cause problems sometimes, as you can have multiple instances of the base class.

To tackle this problem, C++ uses a technique which ensures only one instance of a base class is present. That technique is referred as virtual inheritance.

### Example of When Virtual Inheritance is Useful

Let's look at an example and then explain what's happening:

```c++
#include <iostream>

class A {
    public:
     int x = 5;
     //some other things
};
class B : public A { // inherit from the Class A.
    public:
      int i = 6;
};
class C : public A { // inherit from the Class A.
    public:
      int i = 7;
};
class D : public B, public C { // inherit from both class B and C
    // something can go here..
};

int main(){
    D obj;
    std::cout << obj.x << std::endl;
    return 0;
}
```

Let's see what's going on here:

First, we have a class `A` which is being inherited by two classes `B` and `C`.  Both of these classes are then inherited by another class `D`. 

Inside our `main` function, we create a new instance (object) of the class `D`. We then simply tried to print the value of `x` to the console. 

It might look legit to access the value of `x` here, because class `D` is inherited from both `B` and `C` which are ultimately inherited from the class `A`. 

But when you try to compile the above program, you get the following error:

```
<source>: In function 'int main()':
<source>:21:22: error: request for member 'x' is ambiguous
   21 |     std::cout << obj.x << std::endl;
      |                      ^
<source>:5:10: note: candidates are: 'int A::x'
    5 |      int x = 5;
      |          ^
<source>:5:10: note:                 'int A::x'
```

The error is pretty clear: **`error:`** `request for member '`**`x`**`' is ambiguous`. Let's now see how the request is ambiguous. 

If we draw the hierarchical class structure, it should become pretty clear:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/hierarchial-1.png)
_Hierarchical class structure_

We can see that we have multiple instances of the class `A`. So the request to the variable `x` becomes ambiguous because the compiler doesn't know which instance we are referring to – is it through `B` or through `C` ? That's the real problem. 

### One Way to Solve this Problem

One way to tackle the problem is to use the `scope-resolution operator (::)` with which we can directly specify which instance of `A` we want.

```c++
int main(){
    D obj;
    std::cout << obj.B::x << std::endl;
    std::cout << obj.C::x << std::endl;
}
```

Using the  `scope-resolution operator` we explicitly told the compiler which instance of `A` we referred to.

The main problem with this approach is that it doesn't solve our problem – because our main problem is having multiple instances of class `A`, and we still have that. So we need to look around for some other solutions.

And the other solution is to use virtual inheritance. Let's see how it works now.

### How to Use Virtual Inheritance

To inherit virtually we simply add a keyword `virtual` before our base class name in the derived class declaration like this:

```c++
class B : virtual public A{
    public:
      int i = 6;
};
class C : virtual public A{
    public:
      int i = 7;
};
```

The addition of the `virtual` keyword indicates that we want to inherit from `A` virtually. 

Inheriting virtually guarantees that there will be only one instance of the base class among the derived classes that virtually inherited it. After the changes, our hierarchical class structure becomes:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/diamond-1.png)
_The Hierarchical structure after virtual inheritance_

So now if we try to compile the following code, it will successfully compile.

```c++
#include <iostream>

class A {
    public:
     int x = 5;
};
class B : virtual public A{
    public:
      int i = 6;
};
class C : virtual public A{
    public:
      int i = 7;
};
class D : public B, public C{
    
};

int main(){
    D obj;
    std::cout << obj.x << std::endl;

}
```

So with the introduction of `virtual` inheritance we are able to remove the ambiguities we had earlier.

## Wrapping Up

In this article you learnt about the problem you might face while inheriting a class and a way to solve it using `virtual` inheritance.

Happy Coding!

