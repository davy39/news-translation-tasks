---
title: Learn the basics of Swift in less than ten minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-25T16:21:21.000Z'
originalURL: https://freecodecamp.org/news/learn-swift-basics-in-5-minutes-30a530e23231
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S4__g3knEbuuE6qHyWIbNQ.png
tags:
- name: coding
  slug: coding
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: "By Saul Costa\nSwift is a relatively new programming language designed\
  \ by Apple Inc which was initially made available to Apple developers in 2014. \n\
  It was primarily intended as a replacement for the aging Objective-C language that\
  \ was the foundation ..."
---

By Saul Costa

Swift is a relatively new programming language designed by Apple Inc which was initially made available to Apple developers in 2014. 

It was primarily intended as a replacement for the aging Objective-C language that was the foundation of OS X and iOS software development at the time. It was made open source in December 2015. 

While it remains primarily used by developers targeting the Apple macOS and iOS platforms, Swift is also fully supported on Linux, and there are unofficial ports under development for Windows as well.

Unlike many object-oriented languages, which are based on older procedural languages — for example, C++ and Objective-C are based on C — Swift was designed from the ground up as a new, modern, object-oriented language that makes programming faster and easier, and helps developers produce expressive code that’s less prone to errors than many languages.

While not based on an older language, Swift, in the words of its chief architect, Chris Lattner, “_was inspired by drawing ideas from Ruby, Python, C#, CLU, and far too many others to list_”.

In this quick crash course, we will cover the fundamentals of using the Swift programming language. You’ll learn:

* Basic Swift syntax
* Swift program structure
* Variables and constants
* Type inference
* Variable and constant naming conventions
* Printing and string interpolation

Let’s get started!

> This crash course is adapted from Next Tech’s full Beginning Swift course, which includes an in-browser sandboxed environment with Swift pre-installed. It also has numerous activities for you to complete. You can check it out for free [here](https://c.next.tech/2FkiuWI)!

### Swift Syntax

In this first section, we’ll look at the basic language syntax for Swift.

Like many modern programming languages, Swift draws its most basic syntax from the programming language C. If you have previous programming experience in other C-inspired languages, many aspects of Swift will seem familiar, for example:

* Programs are made up of statements, executed sequentially.
* More than one statement is allowed per editor line when separated by a semicolon (`;`).
* Units of work in Swift are modularized using functions and organized into types.
* Functions accept one or more parameters, and return values.
* Single and multiline comments follow the same syntax as in C++ and Java.
* Swift data type names and usage are similar to that in Java, C#, and C++.
* Swift has the concept of named variables, which are mutable, and named constants, which are immutable.
* Swift has both struct and class semantics, as do C++ and C#.

However, Swift has some improvements and differences from C-inspired languages that you may have to become accustomed to, such as:

* Semicolons are _not required_ at the end of statements — except when used to separate multiple statements typed on the same line in a source file.
* Swift has no `main()` method to serve as the program’s starting point when the operating system loads the application. Swift programs begin at the first line of code of the program’s source file — as is the case in most **interpreted** languages.
* Functions in Swift place the function return type at the right-hand side of the function declaration, rather than the left.
* Function parameter declaration syntax is inspired by Objective-C, which is quite different and often at first confusing for Java, C#, and C++ developers.
* The difference between a struct and a class in Swift is similar to what we have in C# (value type versus reference type), but not the same as in C++ (both are the same, except struct members are public by default).

### Swift Program Structure — `Hello, World`!

To illustrate the basic structure of a Swift program, let’s create a simple Swift program to display the string `Hello, World.` to the console:

```
[Out:]Hello, World
```

> If you are using Next Tech’s sandbox, you can follow along with the code snippets in this crash course by simply typing in the editor. Otherwise, you can follow along with your own IDE — just make sure that Swift is installed!

Congratulations! In two lines of code, you’ve just written your first fully-functional Swift program.

Now, let’s move on to learning about and using the Swift language — and break down each part of your `Hello World` program!

### Swift Variables

Virtually all programming languages include the ability for programmers to store values in memory using an associated name chosen by the programmer. **Variables** allow programs to operate on data values that change during the run of the program.

A Swift variable declaration uses the following basic syntax:  
`var <variable name> : <type&g`t; = <value>

Given this syntax, a legal declaration for a variable called `pi` would be:

This declaration means: “_create a variable named `pi` , which stores a `Double`data type, and assign it an initial value of `3.14159`_”.

### Swift Constants

You may want to store a named value in your program that will not change during the life of the program. How can we ensure that, once defined, this named value can never be accidentally changed by our code? By declaring a **constant**!

In our earlier `Hello, World` program, we declared `message` using `let` instead of `var` — therefore, `message` is a constant.

Since `message` was declared as a constant, if we added the following line of code to the end of our program, we would receive a compile-time error, since changing a `let` constant is illegal:

```
[Out:]error: cannot assign to value: ‘message’ is a ‘let’ constant
```

Generally, any time you create a named value that will never be changed during the run of your program, you should use the `let` keyword to create a constant. The Swift compiler enforces this recommendation by creating a compile-time warning whenever a `var` is created that is not subsequently changed.

Other than the restriction on mutating the value of a constant once declared, Swift variables and constants are used in virtually identical ways.

### Type Inference

In our Hello World example, we created the constant `message` without specifying its data type. We took advantage of a Swift compiler feature called **type inference**.

When you assign the value of a variable or constant as you create it, the Swift compiler will analyze the right-hand side of the assignment, **infer** the data type, and assign that data type to the variable or constant you’re creating. For example, in the following declaration, the compiler will create the variable name as a String data type:

As a **type-safe** language, once a data type is inferred by the compiler, it remains fixed for the life of the variable or constant. Attempting to assign a non-string value to the name variable declared above would result in a compile-time error:

```
[Out:]error: “cannot assign value of type ‘Double’ to type ‘String’
```

While Swift is a type-safe language, where variable types are explicit and do not change, it is possible to create Swift code that behaves like a dynamic type language using the Swift `Any` data type. For example, the following code is legal in Swift:

While this is legal, it’s not a good Swift programming practice. The `Any` type is mainly provided to allow bridging between Objective-C and Swift code. To keep your code as safe and error-free as possible, you should use explicit types wherever possible.

### Variable Naming Conventions

Swift variables and constants have the same naming rules as most C-inspired programming languages:

* Must not start with a digit
* After the first character, digits are allowed
* Can begin with and include an underscore character
* Symbol names are case sensitive
* Reserved language keywords may be used as variable names if enclosed in backticks. For example:

When creating variable and constant names in Swift, the generally accepted naming convention is to use a **camelCase** naming convention, beginning with a lowercase letter. Following generally accepted [naming conventions](https://swift.org/documentation/api-design-guidelines/#follow-case-conventions) makes code easier for others to read and understand.

For example, the following would be a conventional variable declaration:

However, the following would not be conventional, and would be considered incorrect by many other Swift developers:

Unlike many other programming languages, Swift is not restricted to the Western alphabet for its variable name characters. You may use any Unicode character as part of your variable declarations. The following variable declarations are legal in Swift:

Note that just because you _can_ use any Unicode character within a variable name, and can use reserved words as variables when enclosed in backticks, it doesn’t mean you _should_. Always consider other developers who may need to read and maintain your code in the future. The priority for variable names is that they should make code easier to read, understand, and maintain.

### Printing and String Interpolation

In Swift, you can print a variable or a constant to your console using the `print()` function. Let’s create a variable and a constant and print them out.

Execute this snippet in your Code Editor to create a constant named `name`, and a variable named `address`:

```
[Out:]John Does lives at 201 Main Street
```

Both `name` and `address` store string text. By wrapping the variable or constant name in a pair of parentheses, prefixed by a backslash (`\`), we are able to print their stored values in a `print` statement — this is called **string interpolation**.

I hope you enjoyed this quick crash course on the basics of Swift! We learned about basic syntax and program structure, how to declare and use Swift variables and constants, type inference, printing, and string interpolation.

_If you are interested in learning more about Swift, we have a full [Beginning Swift](https://c.next.tech/2FkiuWI) course at Next Tech that you can start for free! In this course we cover:_

* _Other basic programming concepts such as: optionals, tuples, enums, conditionals and loops, methods, structs, and classes._
* _Creating scripts and command line applications in Swift_
* _Using Swift outside of iOS and macOS development lifecycles_

_Happy learning!_

