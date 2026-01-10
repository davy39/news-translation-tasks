---
title: C vs C++ – What's The Difference?
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-04T20:16:23.000Z'
originalURL: https://freecodecamp.org/news/c-vs-cpp-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/vanesa-giaconi-n1nwTr_-lH4-unsplash.jpg
tags:
- name: C++
  slug: c-2
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: 'The C and C++ programming languages power a large part of the world''s
  products, applications, and websites.

  Each helped lay the foundation for the creation of many popular programming languages,
  such as Java. They also support many languages that you...'
---

The C and C++ programming languages power a large part of the world's products, applications, and websites.

Each helped lay the foundation for the creation of many popular programming languages, such as Java. They also support many languages that you might use regularly for your programming projects, such as Python.

In this artcile you'll find a general and beginner friendly overview of the two languages along with their main similarities and differences.

## The origins of C and C++

### A history of the C programming language

Ken Thompson and Dennis Ritchie had been working for quite a few years on the MULTICS (Multiplexed Information and Computing Service) project at AT&T Bell Laboratories. 

After the project came to a halt, in 1969 Ken Thompson started working on his *Space Travel* game on a little used PDP-7 machine.

While doing so, he ended up writing a nearly complete operating system, Unix, from scratch in assembly language.

While working on MULTICS, both Thompson and Ritchie had been writing system software and programming utilities using higher-level languages. And they'd seen how much easier the whole process was, compared to the cryptic and hard to decipher assembly language.

Ritchie joined Thompson to help port Unix onto a newer machine – the PDP-11.

During that period they experimented with various higher level languages that could help get the job done.

They used BCPL (Basic Combined Programming Language), which was used heavily during the MULTICS era. After trying it out, Thompson ended up writing a new language – the B programming language. 

The B language was similar to BCPL but was a more simple and stripped down version.

But B wasn't powerful enough and didn't take full advantage of the new features and power of the PDP-11.


![Image](https://www.freecodecamp.org/news/content/images/2021/11/Ken_Thompson_-sitting-_and_Dennis_Ritchie_at_PDP-11_-2876612463-.jpg)
_Thompson (sitting) and Ritchie working together at a PDP-11. [Image and text credit from Wikipedia](https://en.wikipedia.org/wiki/Ken_Thompson#/media/File:Ken_Thompson_(sitting)_and_Dennis_Ritchie_at_PDP-11_(2876612463).jpg)_

Dennis Ritchie started to improve the B language and ended up creating the C programming language.

C is a portable language, meaning programs written in it can be transfered and used on a variety of machine architectures. It's very fast and easy to compile and has direct mapping to machine code, giving the programmer access to low level functionalities. 

They ended up re-writing the Unix operating system in C in 1972.

Since C was portable and was the language Unix was implemented on, developers started adopting it and using it widely. This lead to the success of the Unix operating system, and in turn the C language became popular.

Dennis Ritchie and Brian Kernighan co-authored the book 'C programming language' in 1977, which created a standard for how the language is supposed to be used. This book popularized the language even more.

C is hugely significant in the history of computing and its creation lead to the creation of many other programming languages. For that, it is often referred to as the '*mother*' of all programming languages.

### History of C++

In 1979, the researcher Bjarne Stroustrup was hired at AT&T Bell Laboratories.

During the 1970s the complexity and computational power of computers increased and limitations in the C programming language started to crop up.

In the early 1980s, Bjarne Stroustrup created a new language which was influenced by two things:

 - The Object Oriented Programming capabilities of another language, Simula, which offered a different approach to programming compared to C. Code could be abstracted and better-organized and anything could be represented using classes.
 -  The systems programming language, C, which offered the ability to get really close to the machine hardware and do demanding low level computational tasks.

Those two ideas combined allowed for higher level abstraction without losing the low level efficiency of C. So, the language '*C with classes*' was created. 

In 1984 'C with classes' was renamed to C++.

So, C++ is a superset of C, meaning that it was an *extension*  of C and is based on it. C++ just provides additional capabilities to the C language. 

## Similarities between C and C++

Below are some of the similarities between C and C++.

### Syntax and code structure

The overall syntax of the two languages is very similar. The operators and keywords used in C are also used in C++ to achieve the same things. But C++ has more keywords than C, and it has an extended grammar.

Inline comments, `//`, and block comments, `*/ */`, look the same.

In addition, every statement ends with a semicolon,`;`.

Conditionals, looping, initializing and declaring variables – they all look similar between the two languages.

Both C and C++ have a `main()` method, which kickstarts every program, and both inlcude header files at the top of the respective files, with `#include`.

### Compiled programming languages

Both C and C++ are compiled programming languages.

A compiler is a computer software program.

It takes the source code that a programmer wrote in a higher level programming language and *translates* it into another language that the computer can understand.

This form is first assembly code which gets translated again to machine code – the native language of all computers.

Machine language is a set of instructions which are understood directly by a computer's CPU (Central Processing Unit).

Once the source code has been traslated to machine code, a binary executable file, `a.out`, gets created.

## Differences between C and C++

Now let's look at a few of the differences between the two languages.

### Input and Output methods

C and C++ use different ways to output information to the console and receive information from the user.

In C, `scanf()` is used for user input, whereas `printf()` is used for outputting data.

In C++, `std::cin >>` is used for getting user input and `std::cout <<` is used to output data.

### The programming paradigm

The most important difference between the two languages is the different approach to programming that each uses.

C is a **procedural oriented language** and its emphasis is on functions.

Programs are divided into a set of functions and they consist of step-by-step instructions, or commands, to be executed in sequential order.

This style of programming specifies *how* to do something, giving structured steps for how computational tasks will be carried out, following a top-down approach.

This style of programming can get quite messy and error-prone when programs grow in size. It leads to a lot of copying and pasting througout the file and updating many functions when there is a change.

Besides being a procedural language, C++ is also an **Object Oriented Programming language**, which is based on the concept of diving a program into objects.

Everything is organized and divided into smaller groups of related parts or *objects*, which are an instance of a *class*, following a bottom-up approach.

Object Oriented Programming is based on four principles: *encapsulation, abstraction, inheritance and polymorhism*.

This style of programming creates more readable and usable code that is easier to maintain, while also providing better data security.

### The STL

C++ offers the STL – Standard Template Library – and C doesn't.

It provides template classes for commonly used data structures and components for implementing added, built-in functionality.

One such component is containers such as [Vectors](https://www.freecodecamp.org/news/c-vector-std-pattern-vector-in-cpp-with-example-code/), that store collections of objects.

### Namespaces

Namespaces are a feature available in C++ and not C.

They are containers used to organize code into logical groups of identifiers and similar objects under a name, within a scope.

They prevent name colisions when multiple libraries are present, and prevent conflict with names of other namespaces within a program.

One example of a namespace is `std::`.

One way to use a namespace and introduce it into a scope is by using the `using` keyword, for example `using namespace std;`.

### Exception handing

C doesn't offer a way to handle exceptions in programs which help prevent errors.

C++, on the other hand, supports exception handling by introducing `try` and `catch` blocks.

### File extension

The file extension for a file that contains C code is `.c`, whereas the file extension for C++ files is `.cpp`.

## Where are C and C++ used?

C is commonly used for very demanding, low-level computational tasks where speed, efficiency, and close access to the machine are a must.

C assumes that programmers know what they are doing and gives them freedom.

It is therefore the language of choice for operating systems, embedded devices, systems programming, kernels and drivers, compiler development, and the growing industry of IoT (Internet of Things) applications.

C++ again allows the programmer close access to and manipulation of the machine, while providing efficiency and high-performance for large-scale systems. At the same time, it is higher-level with enough abstraction away from the machine.

C++ is a popular language of choice for creating game engines and computer graphics and applications, VR applications, web browsers such as Google Chrome, Mozilla Firefox, and Safari, and web browser extensions. The Google Search Engine is also built in C++.

## How to learn C and C++

Below is a list of some resources to help you get started on your C and C++ learning journey.

To learn C:
- [The C Beginner's Handbook: Learn C Programming Language basics in just a few hours](https://www.freecodecamp.org/news/the-c-beginners-handbook/)
- [What is The C Programming Language? A Tutorial for Beginners](https://www.freecodecamp.org/news/what-is-the-c-programming-language-beginner-tutorial/)
- [C Programming Tutorial for Beginners](https://www.youtube.com/watch?v=KJgsSFOSQv0)


To learn C++:

- [The C++ Programming Language](https://www.freecodecamp.org/news/the-c-plus-plus-programming-language/)
- [C++ Tutorial for Beginners](https://www.youtube.com/watch?v=vLnPwxZdW4Y)
- [Learn Object Oriented Programming (OOP) in C++](https://www.freecodecamp.org/news/learn-object-oriented-programming-oop-in-c-full-video-course/)
- [Learn Modern C++ by Building an Audio Plugin](https://www.freecodecamp.org/news/learn-modern-cpp-by-building-an-audio-plugin/)

## Conclusion

Thanks for making it to the end, and I hope you have found this article helpful.

You learned about the origins of C and C++ and their historical background. You then saw a few of their similarities and differences, how each language is used, and some resources for you to get started learning the languages.

Happy coding!


