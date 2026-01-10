---
title: Learn the C# Programming Language – Full Book for Beginners
subtitle: ''
author: Gavin Lon
co_authors: []
series: null
date: '2024-02-06T22:35:57.000Z'
originalURL: https://freecodecamp.org/news/learn-csharp-book
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/The-C--Handbook---Version-4-Cover.png
tags:
- name: beginner
  slug: beginner
- name: book
  slug: book
- name: C#
  slug: csharp
seo_title: null
seo_desc: 'C# version 1 was released in January 2002. It is a modern, general purpose
  programming language designed and developed from the ground up by the renowned Danish
  software engineer, Anders Heijleberg and his team at Microsoft.

  I’ve heard Anders Heijlsb...'
---

C# version 1 was released in January 2002. It is a modern, general purpose programming language designed and developed from the ground up by the renowned Danish software engineer, Anders Heijleberg and his team at Microsoft.

I’ve heard Anders Heijlsberg say in an interview that with C# the goal was to provide the power and expressiveness of C++ and the RAD (Rapid Application Development) capabilities of Visual Basic.

C# is similar to Java in the sense that it runs within its own environment. Java runs within an environment known as the JRE (Java Runtime Environment) whereas C# runs in an environment known as .NET. Both the JRE and .NET run on top of the relevant operating system.

The first version of .NET is known as the .NET Framework which needs to be deployed to the target computer in its entirely and can only run on Windows platforms. But now, .NET has evolved into an environment that can run on multiple platforms like Windows, Mac OS, Linux, IOS, Android and more.

The .NET environment became fragmented in 2016 with the release of .NET Core, which enabled .NET to be cross platform and agile in the sense that only your application’s base class library dependencies need to be deployed to the target computer with your application.

Then in 2020, .NET became unified with the release of NET 5, which meant that the confusion created by having two strands of .NET, namely .NET Framework and .NET Core, was alleviated.

The latest stable release of C# is a highly evolved, sophisticated programming language that allows you to create almost any kind of application that can run on multiple platforms. You can create a single code base that can run on multiple platforms, for example Linux, Mac OS, Android, IOS, in the Cloud, of course Windows operating systems and more.

You are able to write and build your C# applications using free tools like Visual Studio 2022 Community edition or the cross platform, light weight tool, Visual Studio Code. Visual Studio Code can run on Windows, Mac OS, and Linux platforms.

C# is a highly versatile programming language. You can build many types of applications, such as web-based applications using ASP .NET, cross platform mobile and desktop applications using the .Net MAUI framework, Internet of things applications, AI applications using ML.NET, cloud native applications, games and more.

C# has a huge support base, backed by Microsoft, and is constantly evolving. A new version of .NET is shipped every November, which always contains many improvements and enhancements. This means that .NET is forever evolving, improving, and keeping up with the latest trends in technology.

C# is a well designed, modern, general purpose programming language that will be a great addition to your developer toolkit. So let's dive in.

## Table of Contents

* [Introduction to .NET](#heading-introduction-to-net)
* [Free Tools Available for Creating C# Applications](#heading-free-tools-available-for-creating-c-applications)
  * [Create a Basic Console App using Visual Studio Community Edition](#heading-create-a-basic-console-app-using-visual-studio-community-edition)
    * [The Main Method \(Application Entry Point\)](#heading-the-main-method-application-entry-point)
  * [Creating a Basic Console App using Visual Studio Code](#heading-how-to-create-a-basic-console-app-using-visual-studio-code)
* [C# Data Types](#heading-c-data-types)
  * [Value Types and Reference Types](#heading-value-types-and-reference-types)
  * [C# Built-in Value Types](#heading-c-built-in-value-types)
  * [C# Built-in Reference Types](#heading-c-built-in-reference-types)
* [C# Strings](#heading-c-strings)
  * [Immutability of C# Strings](#heading-immutability-of-c-strings)
  * [Quoted String Literals, Verbatim String Literals and Raw String Literals](#heading-quoted-string-literals-verbatim-string-literals-and-raw-string-literals)
    * [Quoted String Literals](#heading-quoted-string-literals)
    * [Verbatum String Literals](#heading-verbatum-string-literals)
    * [Raw String Literals](#heading-raw-string-literals)
* [Useful C# Built-in String Methods](#heading-useful-c-built-in-string-methods)
  * [The IndexOf Built-in Method](#heading-the-indexof-built-in-method)
  * [The Replace Built-in Method](#heading-the-replace-built-in-method)
  * [The Substring Built-in Method](#heading-the-substring-built-in-method)
* [C# Data Type Conversion](#heading-c-data-type-conversion)
  * [Implicit vs Explicit Data Type Conversion](#heading-implicit-vs-explicit-data-type-conversion)
* [C# Operators](#heading-c-operators)
  * [Types of C# Operators](#heading-types-of-c-operators)
* [Constants and Read-only Variables](#heading-constants-and-read-only-variables)
  * [Introduction to Constants](#heading-introduction-to-constants)
  * [Introduction to Read-only Variables](#heading-introduction-to-read-only-variables)
  * [Code Example Using a Const](#heading-code-example-using-a-const)
  * [Code Example Using a Read-only Variable](#heading-code-example-using-a-read-only-variable)
  * [Code Example of the Incorrect Use of a Read-only Variable](#heading-code-example-of-the-incorrect-use-of-a-read-only-variable)
* [C# if / else if / else Statements](#heading-c-if-else-if-else-statements)
  * [Basic if/else Conditional Logic](#heading-basic-ifelse-conditional-logic)
  * [Implementing if/else if/else Conditional Logic](#heading-implementing-ifelse-ifelse-conditional-logic)
  * [Nested if Statements](#heading-nested-if-statements)
  * [More Complex Conditional Expressions](#heading-more-complex-conditional-expressions)
    * [The && Operator](#heading-the-ampamp-operator)
    * [The || Operator](#heading-the-operator)
* [C# Loops](#heading-c-loops)
  * [The for Loop](#heading-the-for-loop)
  * [The while Loop](#heading-the-while-loop)
  * [The do-while Loop](#heading-the-do-while-loop)
  * [The foreach Loop](#heading-the-foreach-loop)
* [C# Arrays](#heading-c-arrays)
  * [One-dimensional Arrays](#heading-one-dimensional-arrays)
  * [Multi-dimensional Arrays](#heading-multi-dimensional-arrays)
    * [Two-dimensional Arrays](#heading-two-dimensional-arrays)
    * [Three-dimensional Arrays](#heading-three-dimensional-arrays)
  * [Jagged Arrays](#heading-jagged-arrays)
* [C# Methods](#heading-c-methods)
  * [Introduction to Methods](#heading-introduction-to-methods-in-c)
  * [The Main Method](#heading-the-main-method)
  * [The Structure of Methods](#heading-the-structure-of-methods)
* [C# Classes](#heading-c-classes)
  * [The 'class' Keyword](#heading-the-class-keyword)
  * [Public Access Modifier](#heading-the-public-access-modifier)
  * [Private Member Variable](#heading-the-private-member-variable)
  * [The Constructor](#heading-the-constructor)
* [C# Structs](#heading-c-structs)
  * [Key Differences Between a Class and a Struct](#heading-key-differences-between-a-class-and-a-struct)
  * [Use a Struct in Code](#heading-use-a-struct-in-code)
* [Enums and Switch Statements](#heading-enums-and-switch-statements)
  * [Introduction to Enums](#heading-introduction-to-enums)
  * [Use an Enum in Code](#heading-use-an-enum-in-code)
  * [Using a switch Statement in Code with an enum](#heading-using-a-switch-statement-in-code-with-an-enum)
  * [Associating One Code Block with More than One Case](#heading-associating-one-code-block-with-more-than-one-case)
  * [Using Strings in switch Statements](#heading-using-strings-in-switch-statements)
* [Inheritance in C#](#heading-inheritance-in-c)
* [Abstraction in C#](#heading-abstraction-in-c)
* [C# Exceptions](#heading-c-exception-handling)
* [C# Delegates](#heading-c-delegates)
* [C# Events](#heading-c-events)
* [C# Generics](#heading-c-generics)
* [LINQ](#heading-linq)
* [C# Attributes](#heading-c-attributes)
* [Reflection](#heading-reflection-in-c)
* [Video on Asynchronous Programming in C#](#heading-video-on-asynchronous-programming-in-c)
* [Conclusion](#heading-conclusion)

## Introduction to .NET

As we briefly discussed in the introductory section, .NET provides an environment in which your C# applications run.

An essential feature of .NET is what can be described as a virtual machine known as the CoreCLR or Core Common Language Runtime.

The Core Common Language Runtime provides services like Just-in-time compilation, memory management, garbage collection, security and exception handling. Also provided with .NET is a variety of base class libraries, that provide generic functionality that can be leveraged by your C# code.

The first version of .NET was the .NET Framework which was released in 2002. .NET Framework could only run on certain windows platforms and had to be installed in its entirety on the target computer.

.NET Core was released in 2016 and provided a modular, cross platform version of .NET that is optimized for the cloud. A significant feature of .NET Core was that only the dependencies used by your application needed to be shipped to the target computer, unlike .NET Framework that had to exist in its entirety on the target computer.

The rapid evolution of these two versions of .NET, .NET Framework and .NET Core, resulted in growing fragmentations of .NET.

In order to deal with the continuing fragmentation of .NET, Microsoft created the .NET Standard, where all platforms running .NET had to support .NET Standard. This was the first step in unifying .NET but it was a temporary solution.

Then in November 2020, .NET 5 was released. This version of .NET retained the great features of both .NET Framework and .NET core, but this release was significant in that .NET 5 meant that .NET was now unified under one umbrella (as it were). There is now no more .NET Framework and .NET core – rather just one version of .NET moving forward.

With the release of .NET 6 the following year, in November 2021, came many significant improvements and new features. Perhaps what is most significant about .NET 6, is that it cemented the unification of .NET.

At this point in time, .NET is a cross platform, modular, agile, fast, robust and secure environment in which your C# applications can run. This means C# and .NET have now evolved to a point where you can “write once and run anywhere”.

Here's a video overview about how .NET works in more detail:

%[https://youtu.be/P6lJA3E3Uog]

And for a full video series on the evolution of .NET, you can check this out:

%[https://www.youtube.com/watch?v=OkeM7XVwEdA&list=PL4LFuHwItvKZAL8rpQiGRbWmgBj6TI7fM]

## Free Tools Available for Creating C# Applications

Microsoft provides two sophisticated free tools that you can use for creating C# applications: Visual Studio Community Edition, which is an IDE (Integrated Development Environment) that can run on Windows platforms, and Visual Studio Code (a light weight code editor) that can run on Windows, Mac OS, and Linux platforms.

You can download and install Visual Studio Community Edition 2022 and the latest version of Visual Studio Code from here: [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/).

### Create a Basic Console App using Visual Studio Community Edition

The easiest way to create your first C# application is by using the simplest project template made available to you through Visual Studio.

The simplest project template is named “Console App”. To get started building your first C# application using Visual Studio, just follow the instructions below:

* Launch Visual Studio
* From the “Get Started” section on the dialog presented to you, select “Create a new project”.
* Find the project template named, “Console App”.
* Select the “Console App” project template option and press the “Next” button.
* Provide a name for your project and the location on your hard disk drive where you’d like to store the files for your project. Press the “Next” button.
* At the time of the creation of this book, the latest stable release of .NET is .NET version 8. If you have this latest version installed on your target computer, it will be selected in the relevant dropdown list for the field marked “Framework”.
* Press the ‘Create’ button to generate the files for your C# project.

You can check out the YouTube video below for a demonstration of creating a basic "Console App" project using Visual Studio 2022.

In this YouTube video, the first demonstration of creating a basic project shows how to create a "Console App" project that includes top-level statements (that is, the `Main` method definition is not present by default).

The second demonstration shows the creation of a basic "Console App" project that doesn't include top-level statements. You'll see how the `Main` method is shown in the default code, whereas in the first demonstration only the body of the `Main` method is shown, and the actual `Main` method definition is not present.

Note that the `Main` method is always the entry point of C# applications. Where top-level-statements are included, the `Main` method is still there but is not visible by default in your code. The inclusion of top-level-statements results in a reduced amount of boilerplate code needed in order for a developer to get started.

%[https://youtu.be/10QrZCLfuCQ]

#### The Main Method (Application Entry Point)

If you look at the "Program.cs" file, you’ll see the following code:

```csharp

    Console.WriteLine(“Hello World”); 

```

You can run this code by pressing the play button on your toolbar. The code for this application is very basic and simply outputs the line, "Hello World" to the console screen.

If you look at the code in the "Program.cs" file, it may seem that there is no real entry point to the application. This is specificially when you have elected to use top-level-statements. If you have written code in previous versions of .NET, the absence of a `Main` method will be conspicuous.

So in .NET 5, for example, the same code currently in your application would look different because the program class and within it the `Main` method would be included.

Check out the code depicted in figure 1 for an example of this:

Figure 1.

```csharp
namespace CSharpSampleCode
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}

```

In .NET 6, a marked effort was made to simplify the amount of boilerplate code needed in your applications. Note that with C# 10, you can simply write the body of the `Main` method in the "Program.cs" file. You don't need to include a class definition (and within the relevant class, a `Main` method definition) as is depicted in figure 1.

So the relevant statements do not need to reside within a `Main` method. The statements can exist as what’s known as top-level-statements.

A `Main` method does still exist behind the scenes and is still the entry point for all C# applications. But after the release of .NET 6, the `Main` method does not need to be present within your code because the compiler synthesises a `Program` class with a `Main` method and places all your top-level-statements within the `Main` method.

But this is now done behind the scenes. The term top-level-statements means that you're able to write statements that are not wrapped in a `Main` method within a class. Behind the scenes the `Main` method and relevant class are created by the compiler. So you're able to write a lot less code, and the entry point of the application – that used to be explicitly written using the `Main` method – is now synthesised by the C# compiler.

Figure 2 depicts how you can avoid writing multiple lines of code for the `Main` method (the entry point for a C# application).

Figure 2.

```csharp
Console.WriteLine("Hello, World!"); //The ‘Main' method is not visible within the code

```

%[https://youtu.be/2pquQMSYk6c]

### How to Create a Basic Console App using Visual Studio Code

I'll now walk you through the process of creating a console application using Visual Studio Code.

First, you'll need to launch VS Code. For the best experience coding an application in C#, you should install the C# Dev Kit extension using the Extensions view.

You can bring up the Extensions view by clicking the Activity Bar on the side of Visual Studio Code. You can then search for C# Dev Kit and install this extension.

Next, create a local folder where you’d like to store the files for your C# project anywhere on your computer.

Using the File > Open Folder menu option, open the folder you created in the previous step, from within VS Code.

Then launch the terminal window using the View > Terminal menu option. You can also launch the terminal window by pressing ctrl + `

You’ll need to ensure that you have installed an appropriate version of the .NET SDK. The latest stable release is .NET version 8. You can download the recommended install file from this location, [https://dotnet.microsoft.com/download](https://dotnet.microsoft.com/download).

In order to verify that you have installed the .NET SDK, you can type `dotnet —-version` within the terminal window and then press the enter key.

To create a project based on the "Console App" project template, you can type this command at your command prompt: `dotnet new console`. Then press the enter key.

To run the project, type `dotnet run` at the command prompt and press the enter key.

After you have appropriately updated the code in your 'Program.cs' file, remember to save your changes before running the updated code.

As an exercise, change the the code so that the output is 'Hello C#', then save your code, and then run your code by typing in, `dotnet run` in the terminal window. Once you press the enter key, 'Hello C#' should be outputted to your console screen.

For a detailed video guide on how to use Visual Studio Code to create C# applications, you can watch the following YouTube video:

%[https://youtu.be/rab_1cFQUF4]

## C# Data Types

It's important to note that C# is a statically typed programming language, whereas JavaScript and Python, for example, are both dynamically typed.

This means that in C#, when variables are declared at compile time, the variables must be defined as a specific C# type.

An exception to this rule is made through the use of the `dynamic` type. The `dynamic` data type allows you to circumvent the .Net type system. If a variable is declared as the `dynamic` data type, this is similar to how variables are typed in a dynamically typed language like JavaScript.

In most cases, you should strongly type variables so that you can reap the benefits inherent in a statically typed language. The advantage of strongly typing variables is that potential data type-related errors can be flagged at compiled time and then dealt with appropriately at compile time.

If you create code that is not valid in relation to the type used to define a variable, this can be flagged by the C# compiler at compile time.

If you look at the code example in figure 3, the C# code is invalid because variable `a` is defined as an integer and in the `DoSomething` method, the `a` variable is assigned a string value.

The C# compiler flags the exception at compile time, and the exception is represented within the Visual Studio IDE, where a red squiggly line is drawn under the offending code.

Figure 3.

```csharp
internal class SomeClass
{
    int a = 1;

    public void DoSomething()
    {
        a = "Gavin Lon"; // Compile time error stating: "Cannot implicitly convert type 'string' to 'int'"
    }
}

```

So the code fails to compile and the cause of the compile time exception is made clear to you through a red squiggly line which appears under the offending code.

This safeguards type-related exceptions from being deployed to a production environment where code that is not appropriately checked at compile time could be prone to runtime errors.

Statically typed languages ensure better code robustness at runtime than dynamically typed languages. C# also performs better than dynamically typed languages like JavaScript or Python because the use of statically typed variables means that the type of the variable is known at compile time. This means that variable types do not need to be determined at runtime, which is what happens with dynamically typed languages.

With dynamically typed languages, the type of a variable is determined at runtime based on the value assigned to the relevant variable. With statically typed languages like C#, the type is known, as it were, at compile time – so the added step of determining the variable's type at runtime is not necessary. This results a performance advantage over dynamically typed code.

### Value Types and Reference Types

C# data types can be put into two main classifications: value types and reference types. These main data type classifications denote how data for C# data types are stored in memory.

A value type is stored in a memory location called the stack, where the value assigned to a variable is stored in the relevant memory space on the stack.

A reference type is stored in a memory location known as the heap, where an address of where the actual data is stored resides on the stack and points to the location where the actual data is stored on the heap.

A key difference between data stored on the stack and data stored on the heap is that all data stored on the stack has a fixed size, where data stored on the heap does not have a fixed size. the fixed size for discrete data stored on the stack means more efficiency in the storage and retrieval of such data when compared to the management of data stored on the heap.

A very basic example that highlights the significance of value types and references types is the following:

Let’s say an integer named `a` is assigned a value of `1`, and an integer named `b` is assigned the value stored in `a`. Then let’s say that the value of `3` is assigned to variable `a`. Does this assignment affect the value stored in variable `b`?

The answer is no. This is because the integer data type is a value type. The `a` variable’s data and the `b` variable’s data are stored in completely different memory locations on the stack. So a change to the data stored in variable `a` will not affect the data stored in variable `b`, even though the value stored in `a` was assigned to the `b` variable.

Figure 4.

```csharp
int a = 1;
int b = a;
a = 3;

```

The object data type in C# is the root type for all data types in C#. An object data type is a reference type, and so all types that inherit directly from the object data type are reference types.

In the example below (in figure 5), variable `a`, which is defined as the `Employee` user defined type, is assigned a new `Employee` object, where the `Name` property is set to the string value of `"Gavin Lon"`. Variable `b`, which is defined as the `Employee` user defined type, is assigned the value of `a`.

When the `Name` property of object variable `a` is changed to `David Hasslehoff`, the `Name` property of object variable `b` is automatically changed to `"David Hasslehof"`.

This is because when `b` is assigned the value stored in `a`, the data stored in `a` is not copied to the storage location that stores the data in `b`. A memory address is copied to `b`, which contains the memory location of where the data is stored for variable `a`. The actual data is stored on the heap and only the memory location of where the data is stored on the heap, is stored on the stack.

This means that variable `a` and variable `b` reference the same data (stored on the heap) at this point. So when the `Name` property of object variable `a` is changed to `"David Hasslehof"`, this change also affects variable `b`. So the `Name` property in variable `b` will also reflect `"David Hasselhof"`.

Figure 5.

```csharp
Employee a = new Employee { Id = 1, Name = "Gavin Lon" };
Employee b = a;
a.Name = "David Hasslehof";
Console.WriteLine(b.Name); // This code prints out the value of David Hasslehof

```

### C# Built-in Value Types

You can see below, in figure 6, the built-in value type data types in C#. Each item contains a link to an appropriate Microsoft Learn page so that you can read more about the relevant data type.

Figure 6.

<table style="box-sizing: inherit ; outline-color: inherit ; border-collapse: collapse ; border-spacing: 0px ; margin-top: 1rem ; color: rgb(22 , 22 , 22) ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 16px ; font-style: normal ; font-weight: 400 ; letter-spacing: normal ; text-transform: none ; white-space: normal ; word-spacing: 0px ; text-decoration: none"><thead style="box-sizing: inherit ; outline-color: inherit"><tr style="box-sizing: inherit ; outline-color: inherit"><th style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left">C# type keyword</th><th style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left">.NET type</th></tr></thead><tbody style="box-sizing: inherit ; outline-color: inherit"><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">bool</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.boolean" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Boolean</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">byte</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.byte" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Byte</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">sbyte</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.sbyte" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.SByte</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/char" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">char</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.char" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Char</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">decimal</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.decimal" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Decimal</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">double</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.double" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Double</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">float</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.single" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Single</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">int</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.int32" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Int32</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">uint</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.uint32" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.UInt32</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">nint</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.intptr" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.IntPtr</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">nuint</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.uintptr" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.UIntPtr</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">long</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.int64" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Int64</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">ulong</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.uint64" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.UInt64</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">short</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.int16" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Int16</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">ushort</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.uint16" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.UInt16</a></td></tr></tbody></table>

### C# Built-in Reference Types

And you can also see all of the built-in reference type data types in C# in figure 7.

Figure 7.

<table style="box-sizing: inherit ; outline-color: inherit ; border-collapse: collapse ; border-spacing: 0px ; margin-top: 1rem ; color: rgb(22 , 22 , 22) ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 16px ; font-style: normal ; font-weight: 400 ; letter-spacing: normal ; text-transform: none ; white-space: normal ; word-spacing: 0px ; text-decoration: none"><thead style="box-sizing: inherit ; outline-color: inherit"><tr style="box-sizing: inherit ; outline-color: inherit"><th style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left">C# type keyword</th><th style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left">.NET type</th></tr></thead><tbody style="box-sizing: inherit ; outline-color: inherit"><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/reference-types#the-object-type" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">object</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.object" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Object</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/reference-types#the-string-type" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">string</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.string" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.String</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/reference-types#the-dynamic-type" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">dynamic</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.object" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Object</a></td></tr></tbody></table>

And now you can check out two YouTube videos where C# data types and C# variables are discussed. Code examples are also provided.

%[https://youtu.be/sW-fsSJaFA0]

%[https://youtu.be/rM9HostBLJ4]

## C# Strings

In C#, you can define a string using the `System.String` class or using its alias, `string`. In the example depicted in figure 8, the two lines of code are equivalent:

Figure 8.

```csharp
string fullName = "Gavin Lon";
System.String fullName = "Gavin Lon";

```

A string is simply a reference to an object in memory that stores text. Internally, a string is an array of char objects.

To create a new string object, the `new` keyword is not generally used. The `new` keyword is only used to create a new string when an array of char objects is passed as an argument to the constructor of the relevant string object.

You can see an example of this below in figure 9.

Figure 9.

```csharp
char[] nameCharacters = { 'G', 'a', 'v', 'i', 'n', ' ', 'L', 'o', 'n' };
string fullName = new string(nameCharacters);

```

### Immutability of C# Strings

Strings are reference types, which means a numeric reference to a memory address is stored on the stack and points to the actual string data which is stored on the heap.

The difference between the string reference type and other reference types (like, for example, an object instantiated from a class) is that the data for a particular string (stored on the heap) cannot be directly changed in memory. This means that every time, for example, a concatenation operation occurs in code, the memory address stored on the stack is simply amended to point to a new memory location on the heap that stores the new string that has been created as a result of the relevant concatenation operation.

### Quoted String Literals, Verbatim String Literals and Raw String Literals

#### Quoted String Literals

Quoted string literals are string values defined on one line in code that start with a single double quote character and end with a single double quote character. Quoted string literals are best suited for stings that exist on one line and don’t contain escape sequences.

If you were to include a backslash (`\`) character in a quoted string literal (like when expressing a directory path, for example), you would need to escape the backslash character with a backslash character directly preceding the backslash character you wish to output as part of the string.

Here's an example of this depicted in figure 11.

Figure 11.

```csharp
string path = "C:\\development\\CSharpProjects";
Console.Write(path);
// Output: C:\development\CSharpProjects

```

The `\` character has a special meaning in C#, so it must be escaped with the appropriate escape character – which is the `\` character. To make it clear that the `\` character is an escape character used in C# string literals, see the below example (in figure 12) where the `\` character is used to escape the double quote (`"`) characters included in a string literal.

Figure 12.

```csharp
string path = "\"C:\\development\\CSharpProjects\"";
Console.WriteLine(path);
//Output: "C:\development\CSharpProjects"

```

#### Verbatum String Literals

Verbatim string literals are recommended where quotations and backslash characters need to be included in the output for string literals. If you precede a string literal with the `@` symbol, the relevant code can output the relevant string verbatim.

Note how the code in figure 13 outputs the same result as the code depicted in figure 12.

Figure 13.

```csharp
string path = @"""C:\development\CSharpProjects""";
Console.WriteLine(path);
// Output: "C:\development\CSharpProjects"

```

The output is the same when the same string lateral is represented in code as a quoted string literal and as a verbatim string literal.

But using a verbatim string literal is much easier to read and is cleaner in its representation. So where the backslash and double quote symbols need to be outputted within the string literal, it's better to use a verbatim string literal.

It's also better to use a verbatim string literal for code that outputs multiline text. In figure 14 is a code example where a verbatim string literal is used in code to output multiline text.

Figure 14.

```csharp
string narrative =
    @"Humpty Dumpty sat on the wall
Humpty Dumpty had a great fall
all the kings horses and all the kings men
couldn’t put Humpty together again";

```

So the above code example dipicted in figure 14 would output the narrative as it is written in the literal string – that is, the text is outputted on multiple lines as the text appears within the literal string in code.

#### Raw String Literals

C# 11 introduced raw string literals. These make it even easier to write code to output multiline text.

Raw string literals remove the need to ever use escape sequences within literal strings.

To indicate in code that you are using a raw string literal, you wrap the relevant text in three double quote symbols. So the first 3 characters should be three double quote symbols followed by the literal string, and the last 3 characters must be three double quote symbols.

Note that in this example, the three quotes that wrap the string literal appear on their own line. This is important because in this example the first part of the string literal appears within double quotes.

Note the output of the code below in figure 15.

Figure 15.

```csharp
string text = """
"To be or not to be" is a quote from Shakespeare's Hamlet.
""";
Console.WriteLine(text);
// Output: "To be or not to be" is a quote from Shakespeare’s Hamlet.

```

Note the output of the code example depicted in figure 16.

Figure 16.

```csharp
string path = """C:\development\CSharpProjects""";
Console.WriteLine(path);
// Output: C:\development\CSharpProjects

```

You could output the multiline text shown in the code example in figure 17, where the output is displayed to the screen in much the same way as the text is represented over multiple lines in the relevant raw literal string in code.

Note that when using a raw string literal to output multiple lines of text, the three double quote characters that must be used to wrap the relevant multiline text must each be on their own line, as is depicted in the example in figure 17.

Figure 17.

```csharp
string narrative = """
Humpty Dumpty sat on the wall
Humpty Dumpty had a great fall
all the kings horses and all the kings men
couldn’t put Humpty together again
""";

```

## Useful C# Built-in String Methods

The C# language has many useful built-in string methods that can, for example, be leveraged for common string-related functionality.

### The IndexOf Built-in Method

One common example is finding a string literal within text stored within a string variable using the `IndexOf` method. See the code example of this depicted in figure 18.

Figure 18.

```csharp
var narrative = "Gavin Lon loves to create free courses on the freeCodeCamp YouTube channel.";

// find freeCodeCamp in the narrative
var indx = narrative.IndexOf("freeCodeCamp");

// the value of indx will be 46
if (indx == -1)
{
    Console.WriteLine("\"freeCodeCamp\" could not be found in the narrative");
}
else
{
    Console.WriteLine($"\"freeCodeCamp\" was found at position {indx} in the narrative");
}
indx = narrative.IndexOf("Gavin Lon");

// the value of indx will be 0
if (indx == -1)
{
    Console.WriteLine("\"Gavin Lon\" could not be found in the narrative");
}
else
{
    Console.WriteLine($"\"Gavin Lon\" was found at position {indx}");
}
// Output:
// "freeCodeCamp" was found at position 46 in the narrative
// "Gavin Lon" was found at position 0

```

### The Replace Built-in Method

Another example of common string related functionality used in C# is finding a specific literal string value within text stored in a variable and replacing the relevant literal string with another literal string value. You can do this in C# using the builtin `Replace` method.

Check out the code example showing this in figure 19.

Figure 19.

```csharp
var narrative = "Gavin Lon loves to create free courses on the freeCodeCamp YouTube channel.";
var newNarrative = narrative.Replace("Gavin Lon", "Farhan Hassan Chowdury");
Console.WriteLine(newNarrative);
// Output: Farhan Hassan Chowdury loves to create free courses on the freeCodeCamp YouTube channel.

```

### The Substring Built-in Method

Another common example is assigning a portion of text stored within a variable to another variable using the builtin `Substring` method. Here's a code example depicting this in figure 20.

Figure 20.

```csharp
var narrative = "Gavin Lon loves to create free courses on the freeCodeCamp YouTube channel.";
var charityName = narrative.Substring(46, 12);
Console.WriteLine(charityName);
// Output: freeCodeCamp

```

You can also watch the YouTube video below for more information and code examples that talk about using and manipulating strings in C#.

%[https://youtu.be/tzJjrrOe69c]

## C# Data Type Conversion

As we discussed above, in C#, variables are statically typed at compile time. This means that once a variable has been defined as a specific type, you can’t define the variable again and you can’t assign a value of an incompatible data type to a variable.

Have a look at the example depicted in figure 21 that highlights static typing in C#.

Figure 21.

```csharp
string narrative = "The cat sat on the mat.";
narrative = 1 + 1; // Compile time error: "Cannot implicitly convert type 'int' to 'string'"

```

Here's an example of what happens if you attempt to define a variable twice in code:

Figure 22.

```csharp
int a = 1;
string a = "one";
// The compiler would immediately flag an error and underline the ‘a’ variable, where an attempt to
// define variable, a, as string is made.
// A compile time error occurs: "A local variable or function named 'a' is already defined in this scope"

```

### Implicit vs Explicit Data Type Conversion

Variables defined as numeric datatypes can be implicitly converted to certain other numeric datatypes – but in other cases an explicit conversion is required.

Implicit data type conversion means that the compiler will automatically convert a variable defined as one data type to another data type, and you don't need to appropriately implement explicit data type conversion code in order for the appropriate data type conversion to occur.

The following code example in figure 23 demonstrates trying to implicitly convert a variable defined as a short integer to the byte data type. Note the commented lines that explain what happens in your code editor.

Figure 23.

```csharp
short b = 255;
byte a = b;
// The compiler would immediately flag an exception and a red squiggly line would appear under
// variable b in the second line of code.
// If you hover your mouse pointer over the red squiggly line the following error message is
// presented: “Cannot implicitly convert type ‘short’ to ‘byte’. An explicit conversion exists (are you missing a cast?)”

```

After reading the commented lines in figure 23, you can see that an explicit conversion is required to satisfy the C# compiler.

The code in figure 24 shows how you can use an explicit type conversion in this case to prevent the relevant data type compile time exception from being flagged.

Figure 24.

```csharp
short b = 255;
byte a = Convert.ToByte(b);
Console.Write(b);
// When this code runs, 255, is printed to the console screen

```

It's important to note that an explicit type conversion can result in a runtime error occurring. If you assigned `b` with a value of `256` instead of `255` (as in the code depicted in figure 24), a run time error would occur when the code is run.

So this explicit type conversion is dangerous because, in this case, the erroneous code would not be flagged at compile time – which would have forced you to fix the error at compile time (before the code is released into production). So this code would result in a runtime error occuring.

The error is caused because the byte data type supports storing whole number values in memory from `0` to `255`. A value of `256` is clearly outside of this range, so a runtime error will occur with the following error message, `System.OverFlowException: Value was either too large or too small for an unsigned byte.`. So a value of `256` must be stored in a variable defined with a data type that supports a range that is greater than the range supported by the byte data type.

The next data type in C# that supports a greater range than the byte data type for whole number values is the short integer data type (or short data type). The value range that a short data type supports is from `-32,768` to `32,767`.

The variable defined as the short data type would be clearly be appropriate for storing a whole number value of `256`.

The next data type that supports a greater value range for whole numbers (than the short data type) is the int data type. The int data type supports a value range from `-2,147,483,648` to `2,147,483,647`.

The data type that supports the greatest value range for whole numbers is the long data type, which supports values from `-9,223,372,036,854,775,808` to `9,223,372,036,854,775,807`.

As we have just discussed, the C# language has data types like the byte data type, the short data type, the int data type and the long datatype for defining variables for the purpose of storing whole number values.

In C#, there are built-in data types appropriate for the storage of values that contain fractal values. Three data types that you can use for the definition of variables for the storage of values with fractal parts are the float, double, and decimal data type.

A great example of a type of value where you’d want to use one of these data types to define a variable (for storing a value that contains a fractal part) is the decimal data type used for storing monetary values. You could use the float or the double data type for storing monetary values, but the decimal data type is more appropriate for this scenario. This is because the decimal data type (although supports less magnitude than the float or double data types) supports greater precision.

In a banking application, for example, where monetary value precision is of the utmost importance, accounting for fractions of value is essential. So the decimal data type (that supports the highest precision for values in C#) should be leveraged for storing monetary values.

Keep in mind that data can be lost when converting a value stored in a variable defined as one particular data type to another data type.

For example, if you have a monetary value stored in a variable defined as a decimal data type that contains a fractal part, converting this value to, for e.g. an int data type would result in the loss of the fractal part of the value.

Here's an example of this depicted in figure 25.

Figure 25

```csharp
var monetaryValue = 10.34m; // note if the ‘m’ suffix is not provided the data type is

// assumed to be the double data type.
// The ‘m’ suffix explicitly defines the variable as
// decimal
var value = Decimal.ToInt32(monetaryValue); //converts decimal to int
Console.WriteLine(value); // this outputs 10 – the value of 0.34 is lost

```

So you can see that a value of `0.34` would be lost as a result of running the data type conversion code depicted in figure 25.

You can check out the YouTube video below for more information on implicit and explicit data type conversions in C#.

%[https://youtu.be/NF4lyA1yx8Y]

## C# Operators

C# operators are made up of one or more symbols that signify to the C# compiler that a particular operation should be performed between relevant operands.

In figure 26, we have a few simple examples of built-in C# operators used to perform mathematical operations.

Figure 26.

```csharp
var a = 1;
var b = 2;
var r = a + b; // the ‘+’ symbol signifies to the compiler to perform an appropriate Addition operation
Console.WriteLine(r); // prints 3 to the screen
r = a * 2; //the ‘*’ symbol signifies to the compiler to perform an appropriate multiplication operation
Console.WriteLine(r); //prints 2 to the screen
r = b - a; //the ‘-’ symbol signifies to the compiler to perform an appropriate subtraction operation
Console.WriteLine(r); // prints 1 to the screen
r = b / 2; //the ‘/’ symbol signifies to the compiler to perform an appropriate multiplication operation
Console.WriteLine(r); // prints 1 to the screen

```

Typically you are able to overload the default behaviour for built-in operators for numeric data types in C#. So you can change the behaviour of specific operators between two operands defined as specific built-in C# data types.

In the above example, the `+` operator performs an addition mathematical operation between the relevant operands. You could write code to overload the `+` operator and change the default addition functionality between two integers.

For example, instead of performing an addition operation between `1` and `2` where a value of `3` is the result of the relevant operation, your operator overload code could return `12`. So in this case the `1` and `2` are simply put together as if a concatenation of two string values was being performed. An integer value of `12` would be the result of the relevant operation.

Of course, overloading the operator in this way may not be very practical. This example merely illustrates how you could change the behaviour of the `+` operator between two integer values by overloading the `+` operator in C#.

### Types of C# Operators

The table below is copied from the Microsoft Learn platform at this URL, [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators)

<table>
<thead>
<tr>
<th>Operators</th>
<th>Category or name</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="member-access-operators#member-access-expression-" data-linktype="relative-path">x.y</a>, <a href="member-access-operators#invocation-expression-" data-linktype="relative-path">f(x)</a>, <a href="member-access-operators#indexer-operator-" data-linktype="relative-path">a[i]</a>, <a href="member-access-operators#null-conditional-operators--and-" data-linktype="relative-path"><code>x?.y</code></a>, <a href="member-access-operators#null-conditional-operators--and-" data-linktype="relative-path"><code>x?[y]</code></a>, <a href="arithmetic-operators#increment-operator-" data-linktype="relative-path">x++</a>, <a href="arithmetic-operators#decrement-operator---" data-linktype="relative-path">x--</a>, <a href="null-forgiving" data-linktype="relative-path">x!</a>, <a href="new-operator" data-linktype="relative-path">new</a>, <a href="type-testing-and-cast#typeof-operator" data-linktype="relative-path">typeof</a>, <a href="../statements/checked-and-unchecked" data-linktype="relative-path">checked</a>, <a href="../statements/checked-and-unchecked" data-linktype="relative-path">unchecked</a>, <a href="default" data-linktype="relative-path">default</a>, <a href="nameof" data-linktype="relative-path">nameof</a>, <a href="delegate-operator" data-linktype="relative-path">delegate</a>, <a href="sizeof" data-linktype="relative-path">sizeof</a>, <a href="stackalloc" data-linktype="relative-path">stackalloc</a>, <a href="pointer-related-operators#pointer-member-access-operator--" data-linktype="relative-path">x-&gt;y</a></td>
<td>Primary</td>
</tr>
<tr>
<td><a href="arithmetic-operators#unary-plus-and-minus-operators" data-linktype="relative-path">+x</a>, <a href="arithmetic-operators#unary-plus-and-minus-operators" data-linktype="relative-path">-x</a>, <a href="boolean-logical-operators#logical-negation-operator-" data-linktype="relative-path">!x</a>, <a href="bitwise-and-shift-operators#bitwise-complement-operator-" data-linktype="relative-path">~x</a>, <a href="arithmetic-operators#increment-operator-" data-linktype="relative-path">++x</a>, <a href="arithmetic-operators#decrement-operator---" data-linktype="relative-path">--x</a>, <a href="member-access-operators#index-from-end-operator-" data-linktype="relative-path">^x</a>, <a href="type-testing-and-cast#cast-expression" data-linktype="relative-path">(T)x</a>, <a href="await" data-linktype="relative-path">await</a>, <a href="pointer-related-operators#address-of-operator-" data-linktype="relative-path">&amp;x</a>, <a href="pointer-related-operators#pointer-indirection-operator-" data-linktype="relative-path">*x</a>, <a href="true-false-operators" data-linktype="relative-path">true and false</a></td>
<td>Unary</td>
</tr>
<tr>
<td><a href="member-access-operators#range-operator-" data-linktype="relative-path">x..y</a></td>
<td>Range</td>
</tr>
<tr>
<td><a href="switch-expression" data-linktype="relative-path">switch</a>, <a href="with-expression" data-linktype="relative-path">with</a></td>
<td><code>switch</code> and <code>with</code> expressions</td>
</tr>
<tr>
<td><a href="arithmetic-operators#multiplication-operator-" data-linktype="relative-path">x * y</a>, <a href="arithmetic-operators#division-operator-" data-linktype="relative-path">x / y</a>, <a href="arithmetic-operators#remainder-operator-" data-linktype="relative-path">x % y</a></td>
<td>Multiplicative</td>
</tr>
<tr>
<td><a href="arithmetic-operators#addition-operator-" data-linktype="relative-path">x + y</a>, <a href="arithmetic-operators#subtraction-operator--" data-linktype="relative-path">x – y</a></td>
<td>Additive</td>
</tr>
<tr>
<td><a href="bitwise-and-shift-operators#left-shift-operator-" data-linktype="relative-path">x &lt;&lt;  y</a>, <a href="bitwise-and-shift-operators#right-shift-operator-" data-linktype="relative-path">x &gt;&gt; y</a>, <a href="bitwise-and-shift-operators#unsigned-right-shift-operator-" data-linktype="relative-path">x &gt;&gt;&gt; y</a></td>
<td>Shift</td>
</tr>
<tr>
<td><a href="comparison-operators#less-than-operator-" data-linktype="relative-path">x &lt; y</a>, <a href="comparison-operators#greater-than-operator-" data-linktype="relative-path">x &gt; y</a>, <a href="comparison-operators#less-than-or-equal-operator-" data-linktype="relative-path">x &lt;= y</a>, <a href="comparison-operators#greater-than-or-equal-operator-" data-linktype="relative-path">x &gt;= y</a>, <a href="type-testing-and-cast#is-operator" data-linktype="relative-path">is</a>, <a href="type-testing-and-cast#as-operator" data-linktype="relative-path">as</a></td>
<td>Relational and type-testing</td>
</tr>
<tr>
<td><a href="equality-operators#equality-operator-" data-linktype="relative-path">x == y</a>, <a href="equality-operators#inequality-operator-" data-linktype="relative-path">x != y</a></td>
<td>Equality</td>
</tr>
<tr>
<td><code>x &amp; y</code></td>
<td><a href="boolean-logical-operators#logical-and-operator-" data-linktype="relative-path">Boolean logical AND</a> or <a href="bitwise-and-shift-operators#logical-and-operator-" data-linktype="relative-path">bitwise logical AND</a></td>
</tr>
<tr>
<td><code>x ^ y</code></td>
<td><a href="boolean-logical-operators#logical-exclusive-or-operator-" data-linktype="relative-path">Boolean logical XOR</a> or <a href="bitwise-and-shift-operators#logical-exclusive-or-operator-" data-linktype="relative-path">bitwise logical XOR</a></td>
</tr>
<tr>
<td><code>x | y</code></td>
<td><a href="boolean-logical-operators#logical-or-operator-" data-linktype="relative-path">Boolean logical OR</a> or <a href="bitwise-and-shift-operators#logical-or-operator-" data-linktype="relative-path">bitwise logical OR</a></td>
</tr>
<tr>
<td><a href="boolean-logical-operators#conditional-logical-and-operator-" data-linktype="relative-path">x &amp;&amp; y</a></td>
<td>Conditional AND</td>
</tr>
<tr>
<td><a href="boolean-logical-operators#conditional-logical-or-operator-" data-linktype="relative-path">x || y</a></td>
<td>Conditional OR</td>
</tr>
<tr>
<td><a href="null-coalescing-operator" data-linktype="relative-path">x ?? y</a></td>
<td>Null-coalescing operator</td>
</tr>
<tr>
<td><a href="conditional-operator" data-linktype="relative-path">c ? t : f</a></td>
<td>Conditional operator</td>
</tr>
<tr>
<td><a href="assignment-operator" data-linktype="relative-path">x = y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x += y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x -= y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x *= y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x /= y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x %= y</a>, <a href="boolean-logical-operators#compound-assignment" data-linktype="relative-path">x &amp;= y</a>, <a href="boolean-logical-operators#compound-assignment" data-linktype="relative-path">x |= y</a>, <a href="boolean-logical-operators#compound-assignment" data-linktype="relative-path">x ^= y</a>, <a href="bitwise-and-shift-operators#compound-assignment" data-linktype="relative-path">x &lt;&lt;= y</a>, <a href="bitwise-and-shift-operators#compound-assignment" data-linktype="relative-path">x &gt;&gt;= y</a>, <a href="bitwise-and-shift-operators#compound-assignment" data-linktype="relative-path">x &gt;&gt;&gt;= y</a>, <a href="null-coalescing-operator" data-linktype="relative-path">x ??= y</a>, <a href="lambda-operator" data-linktype="relative-path">=&gt;</a></td>
<td>Assignment and lambda declaration</td>
</tr>
</tbody>
</table>


For more information on C# Operators, you can watch the YouTube Video below:

%[https://youtu.be/qGgwm95FK5M]

For instructions on how you can overload operators in C#, check out the following YouTube video:

%[https://youtu.be/tq3_8GQxM14]

## Constants and Read-only Variables

### Introduction to Constants

A constant is like a variable in the sense that you can store a value in it by declaring it and assigning it a value. You can then reference that value with a human readable name that denotes the const value in code.

A constant is different from a variable in the sense that it must be assigned a value on the same line in which it is declared. Also, once you have assigned a value to a constant, you cannot assign a new value to that constant at any other point in the code.

You should use constants in your code where they make your code more readable and maintainable. When you appropriately use a const, you don’t have to repeat a value that you assigned to the const in your code. When you need to reference that value in code, you can instead include the human readable name you gave the const in your code that denotes the relevant constant value.

If a const value needs to change, you only need to change the code in one place (that is where the const has been declared). This change will automatically propagate to where the constant is referenced in other lines of code (that are appropriately scoped).

### Introduction to Read-only Variables

A read-only variable is like a variable in that you can store a value in it by declaring it and assigning it a value. You can then reference that value with a human readable name that denotes the read-only variable.

A read-only variable is different from a variable in that its value can only be changed once in code after it has been declared. Its value can be changed in the constructor of a class, but cannot be changed in other parts of your code.

So if you have assigned a read-only variable with a value in the line where it's declared, you can assign that read-only variable with a different value in the constructor of a class – but you can't then assign that read-only variable a new value in any other code.

So a read-only variable is often referred to as a runtime constant. A constant is declared and assigned its value on the same line of code at compile time, and the value for that const cannot be subsequently changed at compile time (and so also can’t be changed at runtime).

A read-only variable is assigned the value that cannot be subsequently changed at runtime. So with a read-only variable, where it is assigned a value within the constructor of a class, is set once when an object instance is created from that class at runtime. That read-only variable cannot be changed after this assignment is made.

### Code Example Using a Const

Here's an example of how to use a const depicted in figure 27.

Figure 27.

```csharp
const int SpeedOfLight = 299792458;
Console.WriteLine($"The speed of light is {SpeedOfLight}");
// The output for this code is:
// The speed of light is 299792458

```

### Code Example Using a Read-only Variable

And here's an example in figure 28 of how to use a read-only variable:

Figure 28.

```csharp
Employee employee = new Employee("Admin");
employee.PrintEmployeeRole();

```

Notice how the read-only string variable named `"RoleName"` has been assigned a value twice. It's assigned an empty string when it's first declared at the top of the class. The read-only variable is assigned its final value within the constructor of the `Employee` class.

Note that you can only change the value of a read-only variable once, and you can only do this within the constructor of a class. Once a read-only variable’s value is assigned within the constructor of a class, you can't change its value in any other part of the code.

In the example below in figure 29, a method named `SetRoleName` contains code to change the value of the `RoleName` read-only variable. This is not possible in C#, because the read-only variable can only be assigned its final value within the contructor of a class. You cannot for e.g. assign the read-only variable a value within a method.

This code will result in a compile time error being flagged by the C# compiler. The error message will state the following in your code editor: `A readonly field cannot be assigned to (except in a constructor or init-only setter of the type in which the field is defined or a variable initialiser)`.

### Code Example of the Incorrect Use of a Read-only Variable

Figure 29.

```csharp
Employee employee = new Employee("Admin");
employee.PrintEmployeeRole();

```

For more information on const and read-only variables, you can watch the YouTube video below:

%[https://youtu.be/yvOdN5PBY2g]

## C# if / else if / else Statements

### Basic if/else Conditional Logic

If statements allow you to include conditional logic in your code. Let's look at a basic example to see how they work.

Let's say you are working on a shopping cart application and a particular piece of code adds a product to the user's shopping cart. In your code, you only want that item added to the user’s shopping cart if the product is in stock.

When a user tries to add a product that is out of stock, you want a message displayed informing the user that the item they want to add is not in stock. You could also add to this message that they should try to add this item to their shopping cart in a week (i.e. when the item may be in stock).

In C#, to automate this conditional logic, you can implement an `if / else` statement. The code in figure 30 shows how this might look:

```csharp
Product product = new();
product.Name = "Ladder";
product.ItemCount = 10;
if (product.ItemCount == 0)
{
    DisplayMessage($"{product.Name} is currently not in stock. Please try again in a week.");
}
else
{
    AddToShopingCart(product);
    DisplayMessage($"A {product.Name} has been successfully added to your shopping cart.");
}
void DisplayMessage(string message)
{
    Console.WriteLine(message);
}
void AddToShopingCart(Product product)
{
    Console.WriteLine("Code runs to add product");
}

class Product
{
    public string Name { get; set; } = "";
    public int ItemCount { get; set; }
}

```

The `if` statement contains a boolean expression. A boolean expression returns either `true` or `false`. If the product is in stock, this boolean expression, `product.ItemCount == 0`, will return `false`. If the product is not in stock, then the boolean expression will return `true`.

The `if` statement expression evaluates whether the relevant product is currently in stock. If the relevant product is no longer in stock, the `ItemCount` property will return `0`. In the case, where the number of products in stock is equal to `0`, code runs and tells the user that the product is not in stock and that they should try to add the product to their cart in a week.

If, however, the count of stock for the product is not equal to `0` (meaning the product is in stock), code will run that adds the product to the user's shopping cart. A message will also appear on the user's screen stating that the product has been successfully added to the user's shopping cart.

You can simply include an `if` statement on its own – and not include an `else` block within the relevant conditional logic. For example, let's say you wanted to output a message to people using a banking application. When their account is overdrawn (that is, they've taken out too much money), the code might look like the basic example in figure 31:

Figure 31.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 2000m;
var balance = currentAccountValue - withdrawalAmount;
if (balance < 0)
{
    DisplayMessage("Your account is overdrawn."); // this message will be displayed to the user
}

```

### Implementing if/else if/else Conditional Logic

Let’s say that in addition to the above code logic, we want to add a requirement so that a specific message is displayed to the person if they can successfully make a withdrawal without their account being overdrawn.

In this requirement, we also want to include a message that gets displayed if their withdrawal results in the balance being less than `100` dollars.

To account for these additional requirements, we can update the relevant conditional logic with an `else if` block and an `else` block. The code in figure 32 shows how this code might look.

Figure 32.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 876m;
var balance = currentAccountValue - withdrawalAmount;
if (balance < 0)
{
    DisplayMessage("Your account is overdrawn.");
}
else if (balance < 100)
{
    DisplayMessage("You have less than 100 dollars left in your account.");
}
else
{
    DisplayMessage($"You have successfully withdrawn {withdrawalAmount} dollars");
}

```

So how does the `if/else if/ else` code work? The first boolean expression is evaluated which accounts for if the balance is less than `0`. If this expression returns `true`, the message, `"Your account is overdrawn."`, is displayed to the user.

If that expression returns `false`, the code in the `else if` block is evaluated, and then the expression is evaluated to check if the balance is less than `100`. If this expression returns `true` (that is, if the value of `balance` is less than `100`) the message , `"You have less than 100 dollars left in your account."`>, is displayed to the user.

If however, the expression returns `false`, this means that the code within the `else` block is executed. So the message, `"You have successfully withdrawn {withdrawalAmount} dollars"` is displayed to the screen.

Each expression is evaluated from top to bottom and each section of the `if/else if/else` code is mutually exclusive. This means that only one of the statements within each of the sections of the `if/else if/else` logic can be run when the relevant conditional logic is executed.

When this conditional logic is run, only one of the messages will be displayed to the user as a result of them making a withdrawal from their account.

### Nested if Statements

You can also include nested if statements within your conditional logic. An example of this is depicted in figure 33.

Figure 33.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 6500m;
var balance = currentAccountValue - withdrawalAmount;
if (balance < 0)
{
    if (balance < -5000)
    {
        DisplayMessage(
            "You have reached your allowable overdraft limit. You will be charged a penalty amount!"
        );
    }
    else
    {
        DisplayMessage("Your account is overdrawn.");
    }
}
else if (balance < 100)
{
    DisplayMessage("You have less than 100 dollars left in your account.");
}
else
{
    DisplayMessage($"You have successfully withdrawn {withdrawalAmount} dollars");
}

```

In the above example, the top `if` statement first checks to see if the account has been overdrawn. If the account has been overdrawn (that is, the value of `balance` is less than `0`), a nested `if/else` statement runs. A nested `if` statement is an `if` statement that resides within another `if` statement.

The nested `if` statement only runs if the expression in the `if`statement in which the nested `if` statement resides returns `true`.

The nested `if` statement depicted in figure 33 further evaluates if the balance is less than `-5000`. If this expression returns `true`, then the user sees a message informing them that the amount just drawn from their account has resulted in the account being overdrawn (i.e. in excess of their allowable overdraft amount). It also lets the user know that the user will be charged an additional penalty amount.

The code in the `else` part of the nested `if` statement runs if the user’s balance is between `-5000` and `0`. This means their account is overdrawn but will not, in this case, result in a penalty amount being charged (because it's within their allowable overdraft limit).

### More Complex Conditional Expressions

#### The && Operator

An `if` statement can include more complex boolean logic as well. For example, you can use the `&&` operator or the `||` operator to evaluate multiple boolean expressions on one line. Figure 34 below depicts a code example of using the `&&` operator in an `if` statement to evaluate more than one boolean expression on one line.

The `&&` operator can be translated as "And also". If the first expression on the left side of the `&&` operator is evaluated as `false`, this means that the entire boolean expression evaluated by the `if` statement is deemed `false`. The boolean expression on the right side of the expression is not evaluated.

In this case, `false` is returned by the `if` statement, meaning that the code within the `if` statements will not be run.

But if, in this example, the condition on the left hand side of the `&&` operator is `true`, this means that the expression on the right side of the `&&` operator must be evaluated. So in this case, if the value of `balance` is less than `-5000`, the boolean expression returns `false`. This means that the entire boolean expression `(balance < -4000 && balance >= -5000)` is `false`. This also means that the message displayed by the code within the `if` statement will not run.

But if the code on the right side of the `&&` operator is `true` (so in this case the balance is greater than or equal to `-5000`), the entire boolean expression in the `if` statement is `true`. This means the message in the `if` statement will be outputted to the screen. So `Your transaction is successful but you are close to your overdraft limit` will be outputted to the screen.

Figure 34.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 5500m;
var balance = currentAccountValue - withdrawalAmount;

```

#### The || Operator

You can also use the `||` operator (as shown in figure 35) when appropriate for boolean expressions that consist of more than one boolean expression.

The `||` operator can be translated as "or-else". When the boolean expression on the left side of the `||` operator returns `true`, the boolean expression on the right side of the `||` operator does not need to be evaluated. This is because only one of the expressions needs to return true for the entire boolean expression to return `true`.

If the boolean expression on the left of the `||` operator returns `false`, then the expression on the right will be evaluated.

If the expression on the right returns `false`, then the entire expression returns `false`. If, however, the expression on the right of the `||` operator returns `true`, the entire boolean expression returns `true`.

Figure 35.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 960m;
var balance = currentAccountValue - withdrawalAmount;
if (withdrawalAmount < 50 || balance < -5000)
{
    RollBackTransaction();
    DisplayMessage(
        "Your transaction failed either because you tried to withdraw less than 50 dollars or your total withdrawal would have resulted in your account having a balance of less than -5000 dollars which exceeds your overdraft limit."
    );
}
else
{
    DisplayMessage("Thank you! Your transaction was successful!");
    CommitTransaction();
}

```

The code in figure 35 evaluates the boolean expression in the `if` statement as, if the withdrawl amount is less than 50 dollars then rollback the transaction and display the appropriate message. If, however, the withdrawl amount is greater than 50 dollars the expression on the right hand side of the `||` operator needs to be evaluated because this means that the expression on the left hand side of the `||` operator has returned `false`.

So if the expression on the right hand side of the `||` operator returns `true` meaning that the customer's `balance` is less than `-5000`, the code to rollback the transaction and display the appropriate message must be run.

So the key take away when using the `||` operator in an `if` condition is that if one of the expressions on either side of the `||` operator returns true, this means that the entire condition returns `true`. In order for the entire condition to return `false`, both expressions on either side of the `||` operator must return `false`.

So if both expressions on either side of the `||` operator returns `false`, this means that the customer has made a valid withdrawl, and the customer's transaction proceeds successfully. A message to this effect is displayed to the customer as a result.

Here's a comprehensive explanation of using `if` statements for conditional logic in C# in the YouTube video below:

%[https://youtu.be/2mChNV9GmpM]

## C# Loops

### The for Loop

Through the use of loops in code, programmers are able to drastically reduce the lines of code required to perform specific tasks. A very simple example of this is displaying a count from `1` to `10` where each value is printed on a new line in the console window. Without using a loop the code could look like the code depicted in figure 36.

Figure 36.

```csharp
Console.WriteLine("1");
Console.WriteLine("2");
Console.WriteLine("3");
Console.WriteLine("4");
Console.WriteLine("5");
Console.WriteLine("6");
Console.WriteLine("7");
Console.WriteLine("8");
Console.WriteLine("9");
Console.WriteLine("10");

```

Using a `for` loop in C# you could reduce 10 lines of code to 3 lines of code as is depicted in figure 37. You could update the code so that the `for` loop loops 100 times instead of 10 times. To do this you would change the relevant `for` loop expression from, `count<=10`, to `count <=100`. So in the code example depicted in figure 38 you would have reduced 100 lines of code to 3 lines of code by using the `for` loop to achieve exactly the same output.

Figure 37.

```csharp
for (int count = 1; count <= 10; count++)
{
    Console.WriteLine(count);
}

```

Figure 38.

```csharp
for (int count = 1; count <= 100; count++)
{
    Console.WriteLine(count);
}

```

You could implement the same functionality using a `while` loop that loops 10 times as is depicted in figure 39.

### The while Loop

Figure 39.

```csharp
var count = 1;

```

### The do-while Loop

You could implement the same functionality using a `do-while` loop in C# as is depicted in figure 40.

Figure 40.

```csharp
var count = 1;
do
{
    Console.WriteLine(count);
    count++;
} while (count <= 10);

```

The difference between a `while` loop and a `do-while` loop is that a `do-while` loop will always execute the code within it at least once. With a `while` loop the boolean conditional expression is at the top of the loop so when this expression returns `false` (i.e. before code within the `while` loop has a chance to run), no code within the `while` loop will run. With the `do-while` loop, code within the `do-while` loop is always executed at least once. In the example depicted in Figure 41, the statements within the `while` block will never run.

Figure 41.

The value of `count` is equal to `11` and the boolean conditional expression, `(count <= 10)`, returns `false` so the two lines of code within the `while` loop will not execute. Let's look at a similar example but where a `do-while` loop is used. This example is depicted in figure 42.

Figure 42.

```csharp
var count = 11;
do
{
    Console.WriteLine(count);
    count++;
} while (count <= 10);

```

The lines of code within the `do-while` loop will execute one time. So the result of this is the value of `11` will be printed to the console screen. After the value of `11` is printed to the console screen, the boolean expression, `(count <= 10)`, is run. The value of `count` is `11` which means the boolean expression at the bottom of the `do-while` loop returns `false`, so the loop will be exited.

### The foreach Loop

In C# you can leverage a `foreach` loop instead of a `for` loop. One of the advantages of using a `foreach` loop rather than a `for` loop is that if the number of traversals that need to occur in order to traverse all of the relevant items in the loop change, the code created for the execution of the loop does not need to change. Consider this example depicted in figure 43 where a `foreach` loop is used to print each value contained within an array to the console screen.

Figure 43.

```csharp
int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
foreach (var val in arr)
{
    Console.Write($"{val} ");
}
// Output:  1 2 3 4 5 6 7 8 9 10

```

Consider what happens when the number of items and values in the array are changed. Please see a code example depiciting this in figure 44.

Figure 44.

```csharp
int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12 };
foreach (var val in arr)
{
    Console.Write($"{val} ");
}
// Output:  1 2 3 4 5 6 7 8 9 10 11 13 12

```

A `for` loop used to execute the same code would look like the code example depicted in figure 45.

Figure 45.

```csharp
int[] arr = { 10, 8, 5, 1, 2, 6, 7, 4, 8, 9, 3, 11, 13, 12 };
for (var x = 0; x <= arr.Length - 1; x++)
{
    Console.Write($"{arr[x]} ");
}
// Output: 10 8 5 1 2 6 7 4 8 9 3 11 13 12

```

With the `for` loop, the length of the array must be included in the code for executing the loop. The index of the array must be included in the code where each item is printed to the screen. You can accomplish the same task using a `for` loop and a `foreach` loop in these scenarios but the `foreach` loop is cleaner and easier to read. So with the `foreach` loop you don’t have to worry about the index of the elements in the array or the length of the array.

For more details on loops in C# and more code examples, please watch the YouTube video below this paragraph.

%[https://youtu.be/oO0GXIIE56U]

## C# Arrays

An array is a data structure. You can store multiple values of the same type within an array. You can also store multiple types within an array by defining the array elements as the object data type.

All types in C# inherit from the object data type, so you can store multiple types of data within an array where the elements are defined as objects.

Consider the below example depicted in figure 46 where an integer array is defined that can store 10 integer values.

Figure 46.

```csharp
int[] arrValues = new int[10];

```

In this example, the array can only store integer values. If you try to store any other type in this array, an appropriate compile time error will be flagged.

In the next example in figure 47, you can only store string values.

Figure 47.

```csharp
string[] arrayStringValues = new string[10];

```

But in the example depicted in figure 48 below, you can store both string and integer values as well as other types of data in the array. This is because, as discussed, all data types in C# inherit from the object data type. So in the array in the example below, you can store string values, integer values, decimal values, boolean values, char values, user defined typed values, and so on.

Figure 48.

```csharp
object[] arrayObjectValues = new object[10];

```

Storing multiple data types in this way this is known as 'boxing', because, for example, if an integer is stored as an element within an array defined as object, the integer data is first ‘boxed’ within the object type. This means that in order to retrieve the data as its appropriate data type from the array, the value must first be ‘unboxed’. This simply means that the relevant array element is explicitly type cast from an object to its appropriate data type.

It is important to note that when defining an array as an object, you are in effect circumventing the type system of the C# language and losing the benefits of a strongly typed language (like faster performance, as well as increased robustness of runtime code).

The 'unboxing' code that needs to run when retrieving values from the array can potentially cause runtime errors to occur, as well as causes a casting runtime overhead. And this slows down the performance of the code.

So strongly typing the array is recommended to increase runtime performance and runtime robustness. This lets you leverage the benefits of the strong type system supported by the C# language.

### One-dimensional Arrays

In C# you have three types of arrays, one dimensional arrays, multi-dimensional arrays, and jagged arrays.

A one dimensional array allows for the storage of data that is one dimensional in nature. An example of this would be an array of grades for a particular student for a particular year.

So for example, let's say that a student received the following grades in 2023: 60, 50, 72, 85, 91. These grades could be stored in a one dimensional integer array like is depicted in figure 49.

Figure 49.

```csharp
int[] grades = new int[5]{60, 50, 72, 85, 91};

```

### Multi-dimensional Arrays

#### Two-dimensional Arrays

An example of using a multi-dimensional array could be an array where more than one student’s grades are stored in the array. This code example is depicted in below figure 50.

So lets say that grades for Sarah, John, and Bob are stored within the two dimensional array. Within the main set of curley brackets, all of the values are included in the two dimensional array. Also within the main set of curly brackets are three sets of curly brackets, one set for each student. And within each of the three sets of curly brackets are 5 grades pertaining to the three students.

So lets say the first set of grades belongs to Sarah, the second set of grades belongs to John, and the third set of grades belongs to Bob.

Figure 50.

```csharp
int[,] studentGrades = new int[3, 5]
{
    { 60, 50, 72, 85, 91 },
    { 50, 45, 67, 80, 93 },
    { 48, 58, 90, 57, 87 }
};

```

So the first subscript in the array is 3, which in this example represents the number of students. The second subscript in the array represents the number of grades. So you could use a C# nested `for` loop to loop through the items in this array and print their values to the screen in a two dimensional matrix display.

In figure 51 you'll see an example of looping through a two dimensional array and displaying the results to the console screen in a two dimensional matrix.

Figure 51.

```csharp
int[,] studentGrades = new int[3, 5]
{
    { 60, 50, 72, 85, 91 },
    { 50, 45, 67, 80, 93 },
    { 48, 58, 90, 57, 87 }
};

```

#### Three-dimensional Arrays

You could add another dimension to this array – for example, you could split the grades up for each student so the grades relate to a particular time of year.

For simplicity, let's divide the year in half. So for the first half of 2023, Sarah received the following grades: 54, 42, 70, 80, 93. For the second half of the year, Sarah received the these grades: 65, 46, 68, 90, 95.

So in this example (depicted in figure 52), the relevant three dimensional array includes the results for Sarah and two other students (John and bob) where their results include their grades for the first half of 2023 as well as their grades for the second half of 2023.

Figure 52.

```csharp
int[,,] studentGrades = new int[3, 2, 5]
{
    {
        { 60, 50, 72, 85, 91 },
        { 65, 46, 68, 90, 95 }
    },
    {
        { 45, 40, 64, 70, 90 },
        { 55, 50, 73, 90, 95 }
    },
    {
        { 46, 60, 88, 55, 89 },
        { 50, 56, 92, 59, 85 }
    }
};
for (int i = 0; i < studentGrades.GetLength(0); i++)
{
    for (int j = 0; j < studentGrades.GetLength(1); j++)
    {
        for (int k = 0; k < studentGrades.GetLength(2); k++)
        {
            Console.Write($"{studentGrades[i, j, k]}\t");
        }
        Console.WriteLine();
    }
    Console.WriteLine();
    Console.WriteLine();
}

```

So in figure 52 above, you can see the first student’s data is printed to the console screen where the first line presents the student’s grades for the first half of the year.

This is followed by a line feed and the first student’s grades for the second half of the year are printed on the subsequent line. Two line feeds follow the data printed for the first student. This is followed by the second student’s grades, and so on.

The first dimension of the array is in this case denoted by the three students. The second dimension of the array is in this case denoted by the the parts of the year (in this case the year is divided into 2 parts (or two halves)). The third dimension of the array is denoted by the actual grades for each student (in this case, five grades).

So depicted in Figure 52 is an example of a three dimensional array declared and initialised. The code that follows outputs the values stored in the three dimensional array to the console screen. So the example in figure 52 is a great example of C# code that implements nested for loops to print out the data stored in a 3 dimensional array to the console screen.

So with this example, you are in effect printing out three dimensional data onto a 2 dimensional screen using C#.

### Jagged Arrays

Basically a Jagged array is an array of arrays. It allows you to store uneven data (if you like).

So what do I mean by uneven data? If you go back to the 2-dimensional array example depicted in figure 51, you have 5 grades represented for each of the three students.

Let’s say that student number two (John in the example) studies only the first three subjects, so you only have grades for those three subjects for John. But you have five grades pertaining to the first three subjects as well as grades pertaining to the last two subjects for the other two students (Sarah and Bob) completed. You still want to store John’s three grades along with the five grades for Sarah and Bob in the array.

Well, good news - you can store all of the data (without the need to include redundant ‘placeholder’ data for John’s missing two grades) by using a jagged array.

In the example depicted in figure 53, C# code is implemented for storing the relevant grades in a jagged array. The code that follows outputs the grades to the console screen.

Figure 53.

```csharp
int[][] studentGrades = new int[3][];
studentGrades[0] = new int[5] { 60, 50, 72, 85, 91 }; // Sarah’s grades
studentGrades[1] = new int[3] { 50, 45, 67 }; // John’s grades
studentGrades[2] = new int[5] { 48, 58, 90, 57, 87 }; // Bob’s grades
for (int i = 0; i < studentGrades.Length; i++)
{
    for (int j = 0; j < studentGrades[i].Length; j++)
    {
        Console.Write($"{studentGrades[i][j]}\t");
    }
    Console.WriteLine();
}

```

You can see by the outputted results, that when compared to the output in the two dimensional array example depicted in figure 51, the shape of the data is jagged (uneven). This is why this data structure is referred to as a jagged array.

You can watch the YouTube video below for more information on arrays in C#, as well as more code examples of how arrays are used in C# code.

%[https://youtu.be/K4wjL7kRJyE]

## C# Methods

### Introduction to Methods in C#

A method is simply a block of code that contains a series of statements. When a program is run and a method is called, the statements within that method are executed.

In C#, every statement is executed in the context of a method. So methods are fundamental to how C# code is structured and executed.

### The Main Method

The `Main` method is the entry point of all C# applications. So this is the method that is first executed whenever a program coded in C# is run.

The CLR (Common Language Runtime) calls the `Main` method when a program (coded in C#) is first started. In C# you can create both named methods and anonymous methods. In this part of the C# book, we'll discuss named methods.

### The Structure of Methods

Methods are used to encapsulate a series of statements that get executed when the method is called in code. In some cases, a method is just a series of statements where (at runtime) the statements are executed in sequence and no value is returned from the relevant method to the calling code.

These methods (that don’t return a value) contain the `void` keyword in the relevant method declaration to signify that the method does not return a value.

Methods can also be created that contain a list of statements that are executed sequentially. At the end of the list of statements, a value of a specified data type is returned to the calling code.

For methods that return values, the data type denoting the value that must be returned from the method is appropriately included within the method's declaration. At the end of the sequence of statements encapsulated by the method, the `return` keyword is included, followed by the value that will be returned to the calling code, on the same line as where the `return` keyword is included.

You can see a simple example of a method that is used for returning the result of a mathematical operation in figure 54.

Figure 54.

```csharp
int result = AddTwoNumbers(2, 3);
Console.WriteLine(result);
int result2 = AddTwoNumbers(300, 400);
Console.WriteLine(result2);

```

In the example above, this simple method has a method declaration that contains a `private` access modifier. This means that the `AddTwoNumbers` method is only accessible from methods contained within the same class in which the `AddTwoNumbers` method resides.

The `AddTwoNumbers` method returns a value that is of type integer. This is denoted by the `int` alias used in the method declaration.

The method declaration contains two parameters, both of the integer data type. The first line of code within the method executes the addition mathematical operation between two arguments that are appropriately passed to the method’s parameters at runtime. The second line of code within the method uses the `return` C# keyword followed by the result of the previous statement, to return the result of the relvant mathematical operation to the calling code.

The `return` keyword denotes returning a value to the calling code, which in this case will be the result of the mathematical operation executed in the first line of code within the `AddTwoNumbers` method.

In the example below (depicted in figure 55), two statements are contained within the method. A fundamental difference between the `AddTwoNumbers` method (depicted in figure 54) and the method below (depicted in Figure 55) is that the `LogFormulaResultToFile` method (depicted in figure 55) does not return a value. This is denoted by the `void` keyword which is included within the `LogFormulaResultToFile` method declaration.

Figure 55.

```csharp
LogFormulaResultToFile(3, 4, "This is the result: ");

// Output:
// This is the result:  7

void LogFormulaResultToFile(int operand1, int operand2, string message)
{
    int result = operand1 + operand2;
    LogToFile($"{message} {result}");
}

void LogToFile(string message)
{
    Console.WriteLine(message); // for simplicity print message to screen rather than write to file
}

```

The fundamental structure for every method in C# is defined by its method signature. And we’ve discussed that within methods are a series of statements.

The method signature defines what type of value is returned by the method, the name of the method, and the level of access (or scope) associated with the method (for example, `private` or `public`). The method signature also includes zero, one, or a list of parameters denoting arguments that can be passed to the method when the method is called at runtime. The method signature can also contain the following keywords, `abstract`,`sealed`, or `virtual`. These keywords are beyond the scope of this handbook.

Methods are declared in a `class`, `struct` or `interface`. Methods in an `interface` do not contain any implementation (that is, any statements) and only the method signature is defined in an `interface`.

Note that methods defined within an `interface` do not include access modifiers. When a `class` implements an `interface`, the methods contained within the `interface` must be appropriately implemented by the `class` that implements the `interface`.

On the other hand, when methods are contained within a `class` or a `struct`, both the method signatures and code implementations for the methods are included.

The example below (depicted in figure 56) demonstrates the implementation of a `public` method that can be used to return the factorial of a number.

Figure 56.

```csharp
MathFunctions mathFunctions = new MathFunctions();
var result = mathFunctions.GetFactorial(6);
Console.WriteLine(result);

// Output:
// 720
public class MathFunctions
{
    public int GetFactorial(int num)
    {
        int fact = 1;
        for (int i = 1; i <= num; i++)
        {
            fact = fact * i;
        }
        return fact;
    }
}

```

In the `public` method named, `GetFactorial`, a local variable is declared and initialised to a value of `1` at the top of the method.

A local variable is a variable that has local scope, meaning that in this case the `fact` variable is not accessible outside of the `GetFactorial` method. It is only accessible within the `GetFactorial` method. This means that the `fact` variable’s value cannot be changed from outside the method but can only be changed from within the method.

You can see that within the `for` loop, a statement is run that alters the value of the `fact` variable with each iteration of the loop. Once the the loop is terminated, a final result is reached and that result is returned (using the C# `return` keyword) to the calling code.

If for example the `GetFactorial` method resides within a class named, `MathFunctions`, the calling code could look like the example below depicted in figure 57.

Figure 57.

```csharp

MathFunctions mathFunctions = new MathFunctions();
var result = mathFunctions.GetFactorial(6);
Console.WriteLine(result);

```

Below, you'll see an example of a `private` method that uses C# string manipulation to appropriately concatenate and reformat the string arguments representing the first name and last name of an employee (depicted in figure 58).

So if the employee’s first name is "John" and the employee's last name is "Denver", the relevant method will return the string value, "Denver, J". The method concatenates the last name with a comma followed by the a further concatenation of the first initial of the employee’s first name.

This concatenation operation is presented by the `return` keyword on the same line, which means the result of the concatenation operation is returned to the calling code.

Figure 58.

```csharp
private string FormatName(string firstName, string lastName)
{
    return lastName + ", " + firstName.Substring(0, 1).ToUpper();
}
```

In figure 59 below, we have a code sample where a class named `Employee` is included. This class contains a read-only property named, `DisplayName`. This property exposes the formatted `name` to the calling code through the use of the `public` access modifier.

The `firstName` and `lastName` string arguments are passed to the constructor of the `Employee` class when it is instantiated by the calling code. The calling code can then write the relevant employee’s formatted name to the console screen. So the `private` method, `FormatName`, is not accessible to the calling code. The formatting of the employee's name is handled within the `Employee` class.

This is a design decision driven by the requirements.

Figure 59.

```csharp
public class Employee
{
    private string firstName = "";
    private string lastName = "";

    public Employee(string firstName, string lastName)
    {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public string DisplayName
    {
        get { return FormatName(this.firstName, this.lastName); }
    }

    private string FormatName(string firstName, string lastName)
    {
        return lastName + ", " + firstName.Substring(0, 1).ToUpper();
    }
}

```

The calling code could look like the code example depicted in figure 60:

Figure 60.

```csharp
Employee employee = new Employee("John", "Denver");
Console.WriteLine(employee.DisplayName);
// Output:
// Denver, J

```

The code example depicted in figure 59 demonstrates the use of the code design concept of encapsulation. The complexity of the `FormatName` functionality is encapsulated within a `private` method in the `Employee` class so the calling code is not concerned with the implementation detail of the formatting functionality of the employee’s name. The calling code only needs to reference the `DisplayName` property on an object derived from the `Employee` user defined type (or class). The formatting functionality is handled within the `Employee` class.

The `private` access modifier enforces the encapsulation of the formatting functionality. The `FormatName` method is not accessible from the calling code, but is only accessible from within the `Employee` class.

This particular design decision is enforced through the use of the `private` access modifier appropriately contained within the `FormatName` method declaration.

## C# Classes

C# supports object-oriented programming. All data types including user defined types in C# inherit from the `object` data type, so you could say that everything in C# is an object. So an `int` is an object, a `decimal` is an object, a `string` is an object, a `bool` is an object etc…

The main difference between an `int`, `decimal` and `bool` when compared to a `string` data type is that the `int`, `decimal` and `bool` data types inherit from the ValueType abstract class, the ValueType class in turn inserts from the `object` type. This means that the `int`, `decimal` and `bool` data types are value types. Strings, on the other hand are reference types. The `string` data type does not inherit from the ValueType abstract class but inherits directly from `System.Object` class.

Note that `int`, `bool` and `decimal` data types are implemented as structs in C#. Structs are value types and are similar to classes in many ways.

The main difference between a struct and a class in C# is that structs are value types and classes are reference types. The `string` data type inherits directly form the `System.Object` type which means the `string` datatype is a reference type.

In C# you are able to create your own custom classes. When you create a class in C#, behind the scenes your user defined type inherits from the `System.Object` type. So your user defined class is a reference type.

Note that you can also create user defined structs using the `struct` keyword, whereas when you create user defined classes, you use the `class` keyword.

The underlying difference between a class and a struct is the way they are stored in memory. Value types store their data directly in a memory location known as the stack, while reference types store a numeric reference (memory address) on the stack, to an object containing the actual data (where the data is actually stored) known as the heap.

The stack stores data in a more structured way than how data is stored on the heap. Make sure you understand this difference, because it affects how the objects derived from classes or structs are copied and passed around in code, and the efficiency with which data is stored and retreived in memory.

Structs are generally faster than classes, so if you are working with large amounts of data, structs may be a more efficient option because they don’t require the overhead of heap memory. Structs may be the best option when needing to represent a simple data structure that contains  data types like integer, boolean, or decimal datatypes.

Structs also have the benefit of being handled more efficiently in memory, which means when dealing with large amounts of instantiated objects from a particular data structure, a struct may be a better option to represent that data, rather than a class.

Structs and classes are both similar in that they both support concepts like for example constructors, fields, properties and methods.

In figure 61 the `Player` class is used as a template for an object that represents a game object for a particular game.

Figure 61

```csharp
public class Player
{
    private string name = "";

    public Player(string name)
    {
        this.name = name;
    }

    public void Move(double x, double y)
    {
        Console.WriteLine($"Moving {name} to coordinates where 'x' = {x}, and 'y' = {y}");
    }
}

```

In the above example (depicted in figure 61), you can see some of the fundamental concepts in C# being expressed, through for example the use of the `class` keyword, the `private` and public access modifiers, a constructor that contains one parameter, a method that contains two parameters and a private member variable defined as a string.

### The class keyword

The class keyword in C# is used for defining a user defined reference type or class.

### The Public Access Modifier

Preceding the `class` keyword is the `public` access modifier. The use of the `public` access modifier in this way means that this class can be accessed and instantiated from anywhere within the assembly in which the class resides as well as from outside of the assembly in which the class resides.

### The Private Member Variable

The `private` member variable named, `name`, is not directly accessible to code that exists outside of the `Player` class. The `name` member variable can only be accessed and used from within a property, constructor or method that resides within the `Player` class.

### The Constructor

The `Player` class (depicted in the code example in figure 61) has one constructor. Classes are instantiated into objects at runtime. The Player constructor contains one string parameter named `name`. When calling code instantiates an object derived from the `Player` class, the name of the `Player` can be passed as an argument to the Player objects constructor.

Within the constructor of the ‘Player’ class the private member variable named, `name` is assigned the value passed in by calling code to the parameterised constructor of the ‘Player’ class. When the calling code subsequently calls the `Move` method, the `name` member variable is accessed and utilised by code within the `Move` method. The constructor is called when the object is derived from the `Player` class.

The constructor enables the calling code to assign a value for the name of the player pertaining to the relevant object at the point at which the relevant object is instantiated.

### The Move Method

Once the calling code has instantiated an object from the `Player` class, the calling code is able to execute the code within the Move method by appropriately calling the `Move` method on the relevant object.

The `Move` method is accessible to code from outside of the class in which it resides because it has a `public` access modifier. If the method had, for example, a private access modifier, this method would only be accessible from within the class in which it resides.

When the `Move` method is executed by calling code, two arguments of type `double`, must be passed into the move method because the `Move` method contains two parameters of type `double`.

Below (in figure 62) is an example of calling code instantiating an object from the `Player` class and subsequently calling the Move method on the relevant instantiated player object.

Figure 62.

```csharp
Player player = new Player("Bob");
player.Move(10.54, 18.43);

```

For more information on C# Classes please view the video below:

%[https://youtu.be/6rlUl5T2Sck]

And below you can find a full video series on C# classes:

[C# Classes Video Series](https://www.youtube.com/watch?v=6rlUl5T2Sck&list=PL4LFuHwItvKY76WTDhfGAwrpLZaSxF9fS)

## C# Structs

The `struct` keyword is used to define a data structure in C# that is a value type. Structs are similar to classes in many respects – for example, you can use both structs and classes to represent data structures that can contain data members and related behavioural functionality expressed within methods.

### Key differences between a Class and a Struct.

* The main difference is that a class is a reference type and a struct is a value type. Structs implicitly inherit from the `System.ValueType` abstract class (which in turn inherits from the `System.Object` class), while reference types inherit directly from the `System.Object` type.
* A struct is a better choice than a class when representing data structures that store small amounts of data. Another good reason to use a struct is if you need to store small amounts of data in the relevant data structure and where a vast number of objects derived from the relevant struct are being dealt with in code.
* You can instantiate an object from a struct using the `new` keyword just like you would when instantiating an object from a class. But the `new` keyword is not required when declaring and initialising a struct before you can use it in code.
* In C# certain value type primitives are represented as structs, for example the `int` alias represents the `System.Int32` struct, the `bool` alias represents the `System.Bool` struct, and the `float` alias represents `System.Single` struct.

### Use a Struct in Code

Below (depicted in figure 63) is an example of code that uses a struct to store the specifications for a pattern. The pattern is denoted by a circle that is drawn within a square.

The `Radius` field stores the value that denotes the radius of the circle, which also determines the size of the square. The `InnerSymbol` field denotes the `char` value printed to the screen that is used for depicting the inner circle. The `OuterSymbol` field denotes the `char` value printed to the screen that is used for depicting the outer square in the overall pattern.

Figure 63.

```csharp
Console.WriteLine("Please enter the radius of the circle");
double radius = Convert.ToDouble(Console.ReadLine());

CircleInSquare circleInSquare;
circleInSquare.Radius = radius;
circleInSquare.InnerSymbol = '0';
circleInSquare.OuterSymbol = '1';
circleInSquare.Draw();

//Output

// 11111111111111111111111111111111111111111
// 11111111111111000000000000011111111111111
// 11111111110000000000000000000001111111111
// 11111111000000000000000000000000011111111
// 11111100000000000000000000000000000111111
// 11110000000000000000000000000000000001111
// 11100000000000000000000000000000000000111
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11100000000000000000000000000000000000111
// 11110000000000000000000000000000000001111
// 11111100000000000000000000000000000111111
// 11111111000000000000000000000000011111111
// 11111111110000000000000000000001111111111
// 11111111111111000000000000011111111111111
// 11111111111111111111111111111111111111111
public struct CircleInSquare
{
    public double Radius;
    public char InnerSymbol;
    public char OuterSymbol;

    public CircleInSquare(double radius, char innerSymbol, char outerSymbol)
    {
        Radius = radius;
        InnerSymbol = innerSymbol;
        OuterSymbol = outerSymbol;
    }

    public void WriteMemberValuesToScreen()
    {
        Console.WriteLine(
            $"Radius = {Radius}, InnerSymbol = '{InnerSymbol}', OuterSymbol = '{OuterSymbol}'"
        );
    }

    public void Draw()
    {
        double radiusInner = Radius - 0.5;
        double radiusOuter = Radius + 0.5;

        Console.WriteLine();

        for (double y = Radius; y >= -Radius; --y)
        {
            for (double x = -Radius; x < radiusOuter; x += 0.5)
            {
                double value = x * x + y * y;

                if (value >= radiusInner * radiusInner)
                {
                    Console.Write(OuterSymbol);
                    System.Threading.Thread.Sleep(50);
                }
                else
                {
                    Console.Write(InnerSymbol);
                }
            }
            Console.WriteLine();
        }
    }
}

```

Note that as demonstrated in the example above (in figure 63), the `new` keyword does not need to be used when instantiating an object from a struct in C#.

A struct is a data structure in C# that is ideal for storing a small amount of values, for example that are needed for objects derived from the `CircleInSquare` struct.

As discussed above, structs are value types in C# which means they are handled more efficiently in memory, where the relevant data is stored in memory on the stack. If you needed to store a sufficiently large number of instances of objects derived from the `CircleInSquare` struct in a collection, this is where a performance advantage could be noticeably gained over a scenario where object instances derived from a class version of the `CircleInSquare` template are stored within a collection.

So for example in a game where perhaps vector information needs to be stored in a large collection to represent the position of a `player` object, you could use a struct to represent the data rather than a class. This would help the data be managed more efficiently in memory, which brings a performance advantage as well in terms of code execution.

%[https://youtu.be/NVKGxzuBe8c]

## Enums and Switch Statements

### Introduction to Enums

In C#, an enum, short for enumeration, is a value type that you can use to define a set of named integral constants. Enums are used to create human readable names for a set of related and unique values, making the code more readable.

### Use an Enum in Code

To declare an enum, you use the `enum` C# keyword. In figure 64 is a code example demonstrating the use of an enum. You can see that months of the year are represented by an enum named `MonthOfYear`. Each of the twelve members of the `MonthOfYear` enum represents a unique month of the year. Each month’s associated integer value is ordered in ascending order by the chronological order in which they occur for a calendar year.

So `Jan` is given the value of `1`, `Feb` is given the value of `2`,  `Mar` is given the value of `3` and so on, until the last month `Dec`, which is given a value of `12` (the twelfth and final month of the calendar year).

A simple method named `OutputMonthMainFocus` is passed an enum value in order to output an appropriate narrative to the user that displays the user focus for the passed-in month argument.

Figure 64.

```csharp
OutputMonthMainFocus("Focus for Jan:", MonthOfYear.Jan);
OutputMonthMainFocus("Focus for Mar:", MonthOfYear.Mar);
OutputMonthMainFocus("Focus for Dec:", MonthOfYear.Dec);

// Output:
// Focus.for Jan: Health and fitness
// Focus.for Mar: Increase knowledge of calculus
// Focus for Dec: Spend more time with friends and family
void OutputMonthMainFocus(string prependedText, MonthOfYear month)
{
    switch (month)
    {
        case MonthOfYear.Jan:
            Console.WriteLine($"{prependedText} Health and fitness");
            break;
        case MonthOfYear.Feb:
            Console.WriteLine($"{prependedText} Learn Spanish");
            break;
        case MonthOfYear.Mar:
            Console.WriteLine($"{prependedText} Increase knowledge of calculus");
            break;
        case MonthOfYear.Apr:
            Console.WriteLine($"{prependedText} Getting up earlier");
            break;
        case MonthOfYear.May:
            Console.WriteLine($"{prependedText} Better work organisation");
            break;
        case MonthOfYear.Jun:
            Console.WriteLine($"{prependedText} Volunteer work");
            break;
        case MonthOfYear.Jul:
            Console.WriteLine($"{prependedText} Eating more vegetables");
            break;
        case MonthOfYear.Aug:
            Console.WriteLine($"{prependedText} Travel to London");
            break;
        case MonthOfYear.Sep:
            Console.WriteLine($"{prependedText} Learning to cook better");
            break;
        case MonthOfYear.Oct:
            Console.WriteLine($"{prependedText} Learn to. surf");
            break;
        case MonthOfYear.Nov:
            Console.WriteLine($"{prependedText} Be more productive");
            break;
        case MonthOfYear.Dec:
            Console.WriteLine($"{prependedText} Spend more time with friends and family");
            break;
        default:
            throw new ArgumentException("Invalid Month");
    }
}

```

### Using a switch Statement in Code with an enum

You can see that the above `switch` statement depicted in figure 64 is similar to an `if/else` statement.

At the top of the `switch` statement is code that contains the `switch` keyword. Within the brackets following the `switch` keyword is the value that the `switch` operation compares to a series of values that are denoted by each `case` statement that's encapsulated within the `switch` code block.

Each `case` section is comparing the value within the brackets following the `switch` keyword to a value following each `case` keyword. When a match between the value within the brackets following the `switch` keyword and a value following one of the `case` keywords is found, the statement list within the matched case section is executed.

For example, where the first line in the calling code (that is code that calls the `OutputMonthMainFocus` method) is called, the statement in the first case section is executed. This is because `Month.Jan` is passed in as an argument to the `OutputMonthMainFocus` method and `Month.Jan` is a match against the value following the `case` keyword in the first `case` section.

Note that a `break` keyword or a `return` keyword (if appropriate) must be included as the bottom statement of each case section’s statement list.

Each case section is mutually exclusive. This means that in the code example depicted in figure 64 where a `break` keyword is included as the bottom statement in each `case` section, when a match occurs, only the statements within that matching `case` section are run. Once the statements within that `case` statement are run, the code breaks out of the `switch` code block. If there is any code below the `switch` code block, then that code will subsequently be run. No other code within that `switch` statement will be run after a match occurs.

If no matches are found within any of the `case` statements, the code within the `default` section is run.

You can see in the example in figure 64 that the code throws an `ArgumentException` if no values within the relevant `case` statements match the value passed into the `switch` statement.

### Associating One Code Block with More than One Case

You could alter the `switch` statement as depicted in figure 65, so that more than one case statement is associated with a block of code (or lines of code). So if, for example, `Month.Jan` was passed into the `switch` statement, the code statements within the `Month.Mar` case section would run.

The same lines of code within the `Month.Mar` case section would also run where `Month.Feb` or `Month.Mar` are passed in as arguments to the `switch` statement. This happens because there are no lines of coded included within the `Month.Jan` case section and there are no lines of code included within the `Month.Feb` section. So if the `Month.Jan` or `Month.Feb` sections aren't matched, the code falls through to the `Month.Mar` case section and the lines of code within the `Month.Mar` case section are run.

Of course the lines of code within the `Month.Mar` section will also run if the `Month.Mar` case section is matched. So the logic for this is the same as the `if` statement depicted in figure 64b.

Figure 64b.

```csharp
MonthOfYear month = MonthOfYear.Feb;
string prependedText = "Focus for Feb";
if (month == MonthOfYear.Jan || month == MonthOfYear.Feb || month == MonthOfYear.Mar)
{
    Console.WriteLine($"{prependedText} Health and fitness");
    Console.WriteLine($"{prependedText} Learn Spanish");
    Console.WriteLine($"{prependedText} Increase knowledge of calculus");
}

```

Figure 65.

```csharp
OutputMonthMainFocus("Focus for Jan:", MonthOfYear.Jan);
OutputMonthMainFocus("Focus for Mar:", MonthOfYear.Feb);
OutputMonthMainFocus("Focus for Dec:", MonthOfYear.Mar);

// Output:
// Focus for Jan: Health and fitness
// Focus for Jan: Learn Spanish
// Focus for Jan: Increase knowledge of calculus
// Focus for Mar: Health and fitness
// Focus for Mar: Learn Spanish
// Focus for Mar: Increase knowledge of calculus
// Focus for Dec: Health and fitness
// Focus for Dec: Learn Spanish
// Focus for Dec: Increase knowledge of calculus
void OutputMonthMainFocus(string prependedText, MonthOfYear month)
{
    switch (month)
    {
        case MonthOfYear.Jan:
        case MonthOfYear.Feb:
        case MonthOfYear.Mar:
            Console.WriteLine($"{prependedText} Health and fitness");
            Console.WriteLine($"{prependedText} Learn Spanish");
            Console.WriteLine($"{prependedText} Increase knowledge of calculus");
            break;
        case MonthOfYear.Apr:
            Console.WriteLine($"{prependedText} Getting up earlier");
            break;
        case MonthOfYear.May:
            Console.WriteLine($"{prependedText} Better work organisation");
            break;
        case MonthOfYear.Jun:
            Console.WriteLine($"{prependedText} Volunteer work");
            break;
        case MonthOfYear.Jul:
            Console.WriteLine($"{prependedText} Eating more vegetables");
            break;
        case MonthOfYear.Aug:
            Console.WriteLine($"{prependedText} Travel to London");
            break;
        case MonthOfYear.Sep:
            Console.WriteLine($"{prependedText} Learning to cook better");
            break;
        case MonthOfYear.Oct:
            Console.WriteLine($"{prependedText} Learn to. surf");
            break;
        case MonthOfYear.Nov:
            Console.WriteLine($"{prependedText} Be more productive");
            break;
        case MonthOfYear.Dec:
            Console.WriteLine($"{prependedText} Spend more time with friends and family");
            break;
        default:
            throw new ArgumentException("Invalid Month");
    }
}

```

### Using Strings in switch Statements

The example depicted in figure 64, specifically deals with the value list within an enum type. You can also, of course, use a `switch` statement to evaluate the values for any C# data type.

For example, in figure 66, values of the string data type are evaluated instead of the numeric values contained within an enum. figure 66.

```csharp
OutputMonthMainFocus("Focus for Jan:", "JAN");
OutputMonthMainFocus("Focus for Mar:", "MAR");
OutputMonthMainFocus("Focus for Dec:", "DEC");
// Output:
// Focus for Jan: Health and fitness
// Focus for Mar: Increase knowledge of calculus
// Focus for Dec: Spend more time with friends and family

```

Note that you can use `if/else if/else` conditional logic where appropiate in order to replace a `switch` statement, however it is better to use a `switch` statement when there are a large number of logical conditions to evaluate. This is because a `switch` statement is more readible in this scenario.

You can watch the YouTube videos below to learn more about switch statements and enums.

%[https://youtu.be/XTDEYQUymt8]

%[https://youtu.be/1248C0V_yHs]

## Inheritance in C#

C# is an object-oriented programming language. The principles of object-oriented programming are encapsulation, inheritance, polymorphism, and abstraction.

Inheritance is where one class is based on another class. It is important to note that multiple inheritance is not permitted in C#. A class in C# can inherit from multiple interfaces but not multiple classes at one time. We'll discuss interfaces in the next section of this handbook along with the principle of abstraction.

So if, for example, the `ManagingDirector` class is based on the `Manger` class, which in turn is based on the `Employee` class, in C# you cannot implement the code like in the example below (in figure 67) in order to express this inheritance hierarchy.

Figure 67.

```csharp
public class ManagingDirector : Manager, Employee
{
    // code goes here
}

```

In C++, this type of multiple inheritance is permitted. But in C#, only single inheritance is permitted.

In C# you are, however, still able to express that the `ManagingDirector` class inherits from the `Manager` class that in turn inherits from the `Employee` class – but you have to do this in a specific way.

The example below (in figure 68) depicts how this specific inheritance hierarchy can be expressed in C#.

Figure 68.

```csharp
public class Manager:Employee
{
	// code goes here
} 
public ManagingDirector:Manager
{	
	// code goes here
}

```

So C# only supports single inheritance for classes, but you can achieve multiple inheritance by implementing code in a certain way in C#. The example above (in figure 68) shows you how to do this.

## Abstraction in C#

Abstraction is another principle of object-oriented programming. It is a concept that is often confused with another one of the principles of object-oriented programming, namely, encapsulation.

Abstraction can be defined as the inclusion of essential design related code but no implementation detail. The implementation detail is denoted by the lines of code within a method, and the abstraction of that method is the method’s method signature.

In the simplified example below (in figure 69), you can see a method named `LogData` that is responsible for either printing data to the console screen or printing data to a predefined local file.

Figure 69

```csharp
public void LogData(string data)
{
	LogToScreen(data);
}

```

The abstraction of this method would be the method signature that could be represented inside an interface like in the example below depicted in figure 70:

Figure 70.

```csharp
public interface ILogging
{
    void LogData(string data);
}

```

The `LogData` method could reside inside a class named `Logging` that implements the `ILogging` interface. When a class implements an interface in C# this means that the class must contain and implement all the methods that are defined within the relevant `interface`.

See below (in figure 71) an example of the `Logging` class implementing the `ILogging` interface.

Figure 71

```csharp
public class Logging : ILogging
{
    public void LogData(string data)
    {
        LogToScreen(data);
    }
}

```

The `ILogging` interface can be described as an abstraction of the `Logging` class. In C#, the calling code does not need to know (as it were) about the the code implementation of the `LogData` method. The calling code only needs to know about the type definition. The type definition is the abstraction of the `Logging` class.

In the example below (in figure 72) you can see an example of calling code instantiating an object from the `Logging` user defined type. Notice how the type definition can be implemented using the `ILogging` interface. This means the calling code will know about the `LogData` method at compile time, but will not know anything about its implementation.

Figure 72.

```csharp
ILogging logging = new Logging();
logging.LogData("Data to be logged.");

```

Now you could create many logging classes with different implementations of the `LogData` method.

For example, currently the `Logging` class contains an implementation of the `LogData` method that logs data to the console screen. Let’s say a requirement emerges where you want to log the data to the a predefined file. To do this you could simply create a new class that implements the `ILogging` interface, where the code within the new class contains code that logs the relevant data to a predefined file.

The example below (in figure 73) depicts the new class. For the sake of simplicity let’s name this class `Logging2`.

Figure 73.

```csharp
public class Logging2 : ILogging
{
    public void LogData(string data)
    {
        LogToFile(data);
    }
}
// Calling code
ILogging logging = new Logging2();
logging.LogData("Data to be logged.");

```

The calling code that implements the `LogData` method in the `Logging` class would look very similar to when the `LogData` method is called on an object instantiated from the `Logging2` class.

In fact you could abstract the instantiation of the relevant `logging` object into its own factory class like you see below in figure 74. So through the use of an interface we are able to further abstract our code, by abstracting the instantiation process of the logging classes.

Figure 74.

```csharp
public static class LoggingFactory
{
    public static ILogging GetLoggingObject(bool toScreen)
    {
        if (toScreen)
        {
            return new Logging();
        }
        else
        {
            return new Logging2();
        }
    }
}

```

The calling code could now be implemented as is depicted below in figure 75.

Figure 75.

```csharp
ILogging logging = LoggingFactory.GetLoggingObject(true);
logging.LogData("Log data to screen");

```

And the calling code could be implemented as is depicted in figure 76 for logging data to a predefined file.

Figure 76.

```csharp
ILogging logging = LoggingFactory.GetLoggingObject(false);
logging.LogData("Log data to file");

```

We have abstracted away the implementation for both the `LogData` method as well as the instantiation of the `logging` object. This is a very basic example of how the principle of abstraction can be implemented using C# in order to create a separation of concerns.

You can of course create many layers of abstraction using similar techniques and various design patterns. Some key driving forces behind how you abstract your code should be better code reuse, better code readability, easier maintenance of code, design extensibility, and to facilitate better unit testing.

In this book, I haven't delved deep into object-oriented principles. For a more detailed explanation of object-oriented programming using C#, you can check out the videos in the playlist link below. In the videos in this playlist the object-orientied principles of encapsulation, inheritance, polymorphism and abstraction are explained and many practicle code eamples are included.

%[https://www.youtube.com/watch?v=HcjOcwMS43w&list=PL4LFuHwItvKYD0e60jNOtT6mFKqFMH1u_]

For a full video series on object-oriented programming in C#, please visit here:

[Full Video Series on Object-oriented Programming using C#](https://www.youtube.com/watch?v=HcjOcwMS43w&list=PL4LFuHwItvKYD0e60jNOtT6mFKqFMH1u_)

## C# Exception Handling

One of your core design criterion when designing an application should be ensuring that your application is as robust as possible.

In order to do this, you'll need to devise and implement a well-designed exception handling strategy. C# makes this fairly easy through the use of `try/catch/finally` blocks.

Exception handling is used to prevent an application from crashing. As a good rule, you should try as much as possible to prevent exceptions from being thrown through code, and only use built-in C# `try/catch` blocks to handle exceptions under truly exceptional circumstances.

A`try/catch'` block allows you to wrap certain code that you know, under certain exceptional circumstances, can result in your application crashing. By understanding the relevant exceptional circumstances that may cause your application to crash, you can implement the appropriate exception handling functionality.

You can catch specific exceptions through the `catch` section of the `try/catch` block. Then you can handle the exception appropriately either by handing the exception within the relevant catch block or by throwing the exception up the stack to be handled appropriately at a further point further up the execution stack.

In this very basic calculator application code example (depicted in figure 77), a method named `Calculate` is implemented to carry out the calculations.

Figure 77.

```csharp
try
{
    int result1 = Calculate(200000, 500000, '*'); // OverFlowException occures
    int result2 = Calculate(5, 2, '^'); // InvalidOperation exception will occur within the Calculate method
    int result3 = Calculate(4, 0, '/'); // Attempted to divide by zero
    Console.WriteLine(result1);
}
catch (ArgumentException)
{
    WriteToScreen("The operation symbol input is not recognised by this application");
}
catch (Exception ex)
{
    WriteToScreen(ex.Message);
}
int Calculate(int operand1, int operand2, char operatorSymbol)
{
    int result = 0;
    try
    {
        switch (operatorSymbol)
        {
            case '+':
                result = operand1 + operand2;
                break;
            case '-':
                result = operand1 - operand2;
                break;
            case '*':
                checked
                {
                    result = operand1 * operand2;
                }
                break;
            case '/':
                result = operand1 / operand2;
                break;
            default:
                throw new InvalidOperationException();
        }
    }
    catch (OverflowException)
    {
        WriteToScreen(
            "The result of the calculation exceeded that max value for the int data type"
        );
    }
    catch (InvalidOperationException ex)
    {
        throw new ArgumentException(
            $"{nameof(operatorSymbol)} is invalid",
            nameof(operatorSymbol),
            ex
        );
    }
    return result;
}

```

With the first call to the `Calculate` method in the above example, the calculation will yield a result that is too large to be supported by the integer data type. This means that an `OverFlowException` will be initially flagged by the C# compiler.

Within the `OverFlowException` catch filter in the code example depicted in figure 77, code is implemented that handles the exception locally within the `Calculate` method. This means the exception is not thrown up the stack to be handled within the calling method. The exception handling code in the `OverFlowException` catch block is simply logging a message to a file through a custom `LogException` method.

With the second call to the `Calculate` method, an invalid operator (that is `^`) is passed to the `Calculate` method. In the default part of the relevant `switch` statement, the code is throwing an `InvalidOperation` exception which is an exception type that is built into the C# language. Within the `try/catch` block is a `catch` filter for specifically catching this `InvalidOperation` exception.

Within the `catch` block, the code is throwing a new `ArgumentException` exception which is subsequently being handled within the calling method (which in this case is the `Main` method, the entry point of this application). In the relevant code example top-level-statements are enabled which means the `Main` is not present in the code but as discussed earlier, the `Main` method is added behind the scenes and encapsulates the calling code which is expressed in this example as top-level-statements.

The `Main` method contains an `ArgumentException` catch section. In this `catch` section, the exception is being handled by outputting an informative message to the user.

Arguably this type of exception would be best handled in code rather than using `try/catch` code for this purpose. You could, for example, validate the operator before the `Calculate` method is called. If the operator is entered by the user incorrectly, output an informative message to them. The user can then alter their input appropriately.

So in order to use validation rather than `try/catch` code in this scenario, the calling code could be changed to what you see in the example below in figure 78:

Figure 78.

```csharp
int result = 0;
Console.WriteLine("Please enter a whole number value for the first operand");
int operand1 = int.Parse(Console.ReadLine());
Console.WriteLine("Please enter a whole number value for the second operand");
int operand2 = int.Parse(Console.ReadLine());
Console.WriteLine("Please enter a valid operator symbol ('+','-','*','/')");
char operatorSymbol = char.Parse(Console.ReadLine());

if (
    operatorSymbol != '+'
    || operatorSymbol != '-'
    || operatorSymbol != '*'
    || operatorSymbol != '/'
)
{
    WriteToScreen(
        "Incorrect operator input. The operator symbol must be one of the following ('+'’','-','*','/') "
    );
}
else
{
    result = Calculate(operand1, operand2, operatorSymbol);
    WriteToScreen(result.ToString());
}

int Calculate(int operand1, int operand2, char operatorSymbol)
{
    int result = 0;
    try
    {
        switch (operatorSymbol)
        {
            case '+':
                result = operand1 + operand2;
                break;
            case '-':
                result = operand1 - operand2;
                break;
            case '*':
                checked
                {
                    result = operand1 * operand2;
                }
                break;
            case '/':
                result = operand1 / operand2;
                break;
            default:
                throw new InvalidOperationException();
        }
    }
    catch (OverflowException)
    {
        WriteToScreen(
            "The result of the calculation exceeded that max value for the int data type"
        );
    }
    catch (InvalidOperationException ex)
    {
        throw new ArgumentException(
            $"{nameof(operatorSymbol)} is invalid",
            nameof(operatorSymbol),
            ex
        );
    }
}
return result;

```

In this case, it's unnecessary to use exception handling, and instead you can use conditional code to validate the operator symbol before the `Calculate` method is even called.

It is important to note that all `Exception` types – including the ones that have been used in these code examples – are derived from the `Exception` type.

The `Exception` type is built into C#. All `Exception` types in C# are derived from the base `Exception` type. An exception inheritance hierarchy has been deliberately designed and implemented in C#. The exceptions I've used in the examples in this section of the book are `OverflowException`, `InvalidOperationException` and `ArgumentException`. These exception types are derived from the base `Exception` type.

The exception type hierarchy in C# means that when there are multiple exception filters within a `try/catch` block, the more derived exception types must be included first within the relevant list of catch filters.

For example, in the examples depicted in this section, the `ArgumentException` appears before the `Exception` catch filter. If the `Exception` catch filter appeared before the `ArgumentException` filter, this would mean that the code within the `ArgumentException` catch filter would never be called. So it's important that the `Exception` catch filter appear after the `ArgumentException` catch filter.

Note that in many cases you'll want to include a `finally` section in your `try/catch` code. This `finally` section is always called when the relevant `try/catch` code is executed. So the code included in the `finally` section is run when code within the `try` section causes an exception to occur (resulting in code within the relevant catch filter being executed) or even if no exceptions occur due to code included within the relevant `try` section. This makes the `finally`  section ideal for including clean up code, that is used for cleaning up resources (for example database connection objects) that are no longer needed.

For more detail on exception handling in C#, you can check out the videos in the playlist below.

%[https://www.youtube.com/watch?v=mpdg6SAaoZ4&list=PL4LFuHwItvKaHOvj1B5DhTnH0MJ1JFJzr]

For a full video series on exception handling in C#, go here:

[Full Video Series on Exception Handling in C#](https://www.youtube.com/watch?v=mpdg6SAaoZ4&list=PL4LFuHwItvKaHOvj1B5DhTnH0MJ1JFJzr)

For a full video series on file handling in C#, go here:

[Full Video Series on File Handling in C#](https://www.youtube.com/watch?v=DHgU_tAC85U&list=PL4LFuHwItvKaqc6w0awyyNGfkzU4ke5fu)

## C# Delegates

Delegates can be described as type safe function pointers. With a delegate, you can define a method definition that includes a parameter list as well as a return type (if no return type is included in the delegate definition, the `void` keyword must be included in place of a data type).

Methods that conform (appropriately in terms of their method signatures) to that defined delegate type can be referenced by the compatible delegate type. A variable can be assigned the relevant delegate and you can then use the variable to invoke any appropriate method that is referenced by the delegate.

In the code example depicted in figure 79 below, a delegate is defined and named `LogDel`. With the declaration of the `LogDel` delegate, a method definition for a method is declared. The method definition in this case represents any method that accepts a string argument and does not return a value (which is denoted by the `void` keyword).

The C# `void` keyword is used in the delegate definition to signify that any method referenced by this delegate must not return a value. Of course you can declare a delegate for a method that does return a value (in which case the delegate definition would include the appropriate data type instead of the `void` keyword).

In this case, however, a delegate is defined to provide an abstraction for a method that accepts a string argument and does not return a value.

In the code example depicted in figure 79, you can see how a delegate is used to create flexibility where calling code can reuse the `LogDel` delegate to log text to the console screen or log the text to a text file. Using this delegate definition the calling code can even implement what is known as a multi-cast delegate.

In this case, an instantiation of the `LogDel` delegate type is used to combine the functionality of a method that logs text to the screen as well as a method that logs text to a file. In the code, the `+` operator is used in between two delegates and the result is assigned to a delegate named `multiLogDel`.

When the `multiLogDel` delegate is invoked, the text is logged both to the console screen as well as to the text file. So delegates can be used to call multiple methods (that are appropriately defined where the method definitions match the delegate definition) through one invocation of the delegate instantiation.

Also, through the delegate, you can invoke functionality for just one of the methods – in this example either `LogTextToScreen` or `LogTextToFile`.

So delegates provide a type safe, flexible abstraction over methods that you can use to call one or multiple methods that conform to a specified method definition.

Figure 79.

```csharp
Log log = new Log();
LogDel LogTextToScreenDel,
    LogTextToFileDel;
LogTextToScreenDel = new LogDel(log.LogTextToScreen);
LogTextToFileDel = new LogDel(log.LogTextToFile);
LogDel multiLogDel = LogTextToScreenDel + LogTextToFileDel;
Console.WriteLine("Please enter your name");
var name = Console.ReadLine();
LogText(multiLogDel, name);
Console.ReadKey();
void LogText(LogDel logDel, string text)
{
    logDel(text);
}
delegate void LogDel(string text);

class Log
{
    public void LogTextToScreen(string text)
    {
        Console.WriteLine($"{DateTime.Now}: {text}");
    }

    public void LogTextToFile(string text)
    {
        using (
            StreamWriter sw = new StreamWriter(
                Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Log.txt"),
                true
            )
        )
        {
            sw.WriteLine($"{DateTime.Now}: {text}");
        }
    }
}

```

For more detail on delegates, you can watch the videos in the playlist below.

%[https://www.youtube.com/watch?v=5YTqMe2GC5U&list=PL4LFuHwItvKZwUnVL2KKvfYxNMVo-TQAB]

For a full video series on delegates in C#, go here:

[Full Video Series on C# Delegates](https://www.youtube.com/watch?v=5YTqMe2GC5U&list=PL4LFuHwItvKZwUnVL2KKvfYxNMVo-TQAB)

## C# Events

Events can be used in C# to notify other classes or objects when, for example, a condition is met within the class or object in which that event resides. When the condition is met within the class or object that contains the event, the event can be raised. This means that those classes or objects that have elected to receive notifications when the relevant event is raised will receive those notifications.

The classes or objects elect to receive these notifications by subscribing in code to the event that resides in the class or object that contains the event. The class or object that contains the event is known as the publisher, and the classes or objects that have subscribed to recieve notifications when the relevant event is raised are known as the subscribers.

In the example depicted in figure 80 below, the publisher is the class named `GuessNumberGame`. You can see that an event named `GameEvent` has been published within this class. In this simple example, the subscription to the `GameEvent` class is made within the entry point or `Main` method of the application (shown in this example in the top-level-statements of the application).

Here, this is for the sake of simplicity – but in a real-world application you may have many subscriber classes subscribing to the event within the publisher class.

So within the calling code, a subscription to the `GameEvent` event is made through the use of the `+=` operator. This operator is used when a subscription to an event is made in C# code.

On the right hand side of the `+=` operator is the name of a method that is designated to handle the event when the event is raised. So this event handling method resides within the subscriber code.

We used a built-in C# generic delegate to define the `GameEvent` event. This in effect defines the the method definition for the method or methods that are designated to handle the event.

The `EventHandler` delegate provides a definition for a method that contains two parameters. One is defined as `object`, and the other is defined as a generic type argument that is passed in as an argument to the `EventHandler` delegate at compile time within the publisher class where the event is declared.

So you can see in the calling code, a method named `EventHandlerMethod` is defined that contains an argument of type `object`. There's also an object defined as the data type argument passed into the type parameter for the built-in generic `EventHandler` delegate, when the `GameEvent` is declared inside the publisher class.

So when the relevant condition is met within the `OnCorrectNumberGuessed` method, the `GameEvent` event is raised. This, in effect, results in the `EventHandlerMethod` being executed within the calling code, or within the subscriber's code, if you like.

The code in figure 80 is a simple game. The user gets three chances to guess a random number between 1 and 4 (including 4), generated within the `GuessNumberGame` class.

If the user guesses the correct number, the `GameEvent` event is raised and the code within the `EventHandlerMethod` is run. This results in outputted text being displayed to the user, informing them that they have guessed the correct number and have therefore won the game.

So when the user guesses the correct number, the following text is outputted to the console screen: `You guessed it!! Well done! :)`.

As we discussed before, the `+=` operator is used for subscribers to subscribe to an event within the publisher class or object. This lets them receive notifications when the event is raised through code within the publisher class or object.

After the `while` loop code, there's a line of code where the subscriber unsubscribes from the event. This is important, as it prevents possible memory leaks from occurring.

To unsubscribe from the event, you can use the `-=` C# operator:

Figure 80.

```csharp
Console.WriteLine("Guess the number of which the computer is thinking. Is it 1,2,3 or 4?");
Console.WriteLine();
int counter = 0;
bool gameIsWon = false;
GuessNumberGame guessNumberGame = new GuessNumberGame();
guessNumberGame.GameEvent += EventHandlerMethod;
do
{
    counter++;
    Console.WriteLine("Please input your number choice");
    int userGuessedNumber = Int32.Parse(Console.ReadLine());
    guessNumberGame.CompareUsersNumber(userGuessedNumber);
} while (gameIsWon == false && counter < 3);
guessNumberGame.GameEvent -= EventHandlerMethod;
void EventHandlerMethod(object sender, GuessNumberDataEventArgs args)
{
    Console.WriteLine(args.GuessNumberGameOutputMessage);
    gameIsWon = true;
}

class GuessNumberGame
{
    Random rnd = new Random();
    private readonly int generatedRandomNumber = 0;

    public GuessNumberGame()
    {
        this.generatedRandomNumber = rnd.Next(1, 5);
        Console.WriteLine("Computer Gen =" + generatedRandomNumber);
    }

    public void CompareUsersNumber(int guessedNumber)
    {
        if (guessedNumber == this.generatedRandomNumber)
        {
            OnCorrectNumberGuessed(
                new GuessNumberDataEventArgs
                {
                    GuessNumberGameOutputMessage = "You guessed it!! Well done! :)"
                }
            );
        }
    }

    public void OnCorrectNumberGuessed(GuessNumberDataEventArgs e)
    {
        EventHandler & lt;
        GuessNumberDataEventArgs & gt;
        handler = GameEvent;
        if (handler != null)
        {
            handler(this, e);
        }
    }
}

public event EventHandler<GuessNumberDataEventArgs> GameEvent;

}

```

For more details on using C# Events and more code examples, you can check out the YouTube video below.

%[https://www.youtube.com/watch?v=QJJKMW3ErEw&list=PL4LFuHwItvKa3dr0NL732rnnOhcc3aEgG]

For a full video series on events in C#, you can go here:

[Full Video Series on C# Events](https://www.youtube.com/watch?v=QJJKMW3ErEw&list=PL4LFuHwItvKa3dr0NL732rnnOhcc3aEgG)

## C# Generics

Generics allow C# developers to reuse specific code (like that which exists within a method, class, or collection) in the context of multiple different C# data types.

You determine this data type context at compile time where, for example, you can pass a data type argument to a data type parameter that is contained within the definition of the method, class, or collection type.

A simple code example of this is the C# generic `List` type, which is a built-in collection you can use. You can strongly type a generic list at compile time with C# built-in data types like `int`, `string`, `char`, `bool`, `decimal`, `float`, `double` and so on, as well as user defined types, like those that are implemented using a class or a struct.

In the example depicted in figure 82, the generic list type is being used to store the grades of a university student. All of the grades are integers. When you look at the definition for the `List` generic type that is built into C#, you see the word `List` followed by angle brackets, with a `T` included within the angle brackets. So the generic built-in C# `List` type is defined as is depicted in figure 81.

The `T` is a placeholder representing the generic data type parameter, which you can use to pass a data type argument to the 'List' type at compile time in order to strongly type the list.

Generics means that type parameters are included in .NET. This makes it possible for you to design classes and methods that defer the specification of one or more types until the class or method is declared and instantiated by calling code.

Figure 81.

```csharp
List<T>

```

Figure 82.

```csharp
List<int> grades = new List<int>();
grades.Add(60);
grades.Add(73);
grades.Add(85);
grades.Add(92);
foreach (int grade in grades)
{
    Console.Write($"{grade}, ");
}

// Output: 60, 73, 85, 92,
// You could also use the generic list to store the subject names pertaining to the grades of the relevant
// student.
List<string> subjects = new List<string>();
subjects.Add("Observational Astronomy");
subjects.Add("Particle Physics");
subjects.Add("Quantum mechanics");
subjects.Add("Advanced Math");

```

You can also use the same generic list data type to store objects derived from a specific user defined type, implemented, for example, as a class in code.

So in the example in figure 83, the list data type is used to store a collection of 'student' objects:

Figure 83.

```csharp
List<Student> students = new List<Student>();
students.Add(
    new Student
    {
        Id = 1,
        Name = "Dale Jones",
        Grade = 60
    }
);
students.Add(
    new Student
    {
        Id = 2,
        Name = "Gale Davis",
        Grade = 89
    }
);
students.Add(
    new Student
    {
        Id = 3,
        Name = "Debbie Hill",
        Grade = 56
    }
);
students.Add(
    new Student
    {
        Id = 4,
        Name = "Dave Brown",
        Grade = 76
    }
);
foreach (Student student in students)
{
    Console.WriteLine($"{student.Id} {student.Name} {student.Grade} ");
}
// Output:
// 1 Dale Jones 60
// 2 Gale Davis 89
// 3 Debbie Hill 56
// 4 Dave Brown 76

```

Through generics, you are able to reuse the functionality in the built-in `list` data type to store multiple types of data. Any generic list used in your C# code must be strongly typed with one particular data type.

You can strongly type the generic list by passing in the relevant type as an argument when defining and instantiating an object of the `List` type.

Prior to the generic `List` type being introduced (in .NET Framework 2.0), you could use an `ArrayList` to store a collection of heterogeneous data types. You could store multiple different data types within one `ArrayList`.

The problem with the `ArrayList` is that any calling code retrieving an item from an `ArrayList` must first convert that value to its appropriate data type before the value can be of any use.

Every item stored in an `ArrayList` is ‘boxed' within the `object` type. This is possible because all C# data types inherit from the `object` data type, so every data type in C# can be implicitly boxed into an object.

Boxing is simply the process of converting a value type to the `object` type in C#. When the common language runtime (CLR) boxes a value type, it wraps the value inside a `System.Object` instance and stores it on the managed heap. So in order to use an item retrieved from an `ArrayList`, the object must first be converted or 'unboxed' into its original type.

This highlights one of the main advantages of using generics in C#. Through using the generic `List` to store strongly typed items in a collection, you can avoid 'boxing' and 'unboxing'. This means that with generics, the performance overhead caused through 'boxing' and 'unboxing' is also avoided.

The other main advantage is that you can avoid type-related errors that can occur as a result of explicit type conversions needing to be performed on an item retrieved from an `ArrayList` at runtime.

So by strongly typing a `List` at compile time, the compiler is able to check that all data type-related code is correct before it is deployed into production. In this way, data type-related errors are preempted at compile time.

Depicted in figure 84, is an example of using an `ArrayList`  to store heterogeneous data types.

Figure 84.

```csharp
using System.Collections;
using System.ComponentModel;

ArrayList studentDetails = new ArrayList();
int grade = 90;
string name = "Bob Jones";
studentDetails.Add(90); // int value boxed as object
studentDetails.Add("Bob Jones");
studentDetails.Add(
    new Student
    {
        Id = 1,
        Name = "Bob Jones",
        Grade = 90
    }
);
grade = Convert.ToInt32(studentDetails[0]); // runtime performance slowed by unboxing int student = int32.Parse(studentDetails[2]); // This would result in a runtime exception being thrown due to an invalid type conversion operation being performed at runtime

```

So you can see that using a generic `List` to store strongly typed values in a collection (rather than an `ArrayList` where 'boxing' and 'unboxing' code needs to be performed) results in a performance improvement. It also ensures better robustness at runtime.

The example depicted in figure 85 is a more complicated example of using generics in C#. In this example, the factory pattern is employed where you can reuse the `GetInstance` method to instantiate objects of different types using the same instantiation functionality enveloped in the `GetInstance` method.

You can see that `K` and `T` are used as placeholders to represent the types that can be passed as arguments to the class at compile time (that is, in order to strongly type the class). The `where` keyword denotes constraints (which are defined rules) on the type arguments passed to this class.

So these constraints mean that the type passed as an argument to the parameter represented by the `T` placeholder must be a class. The `new` keyword followed by open and closed brackets denotes that a new object must be created from the relevant class which is of type `K`.

Figure 85.

```csharp
// Instantiation of objects from the generic types passed as objects to the FactoryPattern class.
IStudent student = FactoryPattern<IStudent, Student>.GetInstance();
student.Name = "Bob Jones";
student.Grade = 78;
student.Subject = "Math";
Console.WriteLine($"{student.Name} {student.Grade} {student.Subject}");
IStudent student2 = FactoryPattern<IStudent, Student>.GetInstance();
student2.Name = "Debbie Long";
student2.Grade = 84;
student2.Subject = "Science";
Console.WriteLine($"{student2.Name} {student2.Grade} {student2.Subject}");
IProfessor professor = FactoryPattern<IProfessor, Proffessor>.GetInstance();
professor.Name = "Ron Willis";
professor.MainSubject = "Math";
Console.WriteLine($"{professor.Name} {professor.MainSubject}");

// Output:
// Bob Jones 78 Math
// Debbie Long 84 Science
// Ron Willis Math
static class FactoryPattern<K, T>
    where T : class, K, new()
{
    public static K GetInstance()
    {
        K objK;
        objK = new T();
        return objK;
    }
}

```

So in the example depicted in figure 85, generics is used to create clean, reusable code for the implementation of the factory pattern.

A single code block is used to create instances of objects derived from multiple user defined types. Through generics the amount of code is minimised, and if you have a good knowledge of generics, this code is easy to maintain and reuse. Generics gives you greater design flexibility, and ensures better runtime performance and robustness.

For more information on C# Generics and more code examples, you can watch the YouTube video below.

%[https://www.youtube.com/watch?v=UUF8QCf3rpI&list=PL4LFuHwItvKaeSVOur67Lu-0I7sfjf5N3]

For a full video series on generics in C#, you can go here:

[Full Video Series on C# Generics](https://www.youtube.com/watch?v=UUF8QCf3rpI&list=PL4LFuHwItvKaeSVOur67Lu-0I7sfjf5N3)

## LINQ

LINQ stands for Language-Integrated Query and was first introduced to .NET languages with .NET Framework version 3.5 in 2007. It provides .NET developers with a high level query abstraction where, for example, C# code can be used to natively query collections of C# objects. It's similar to the well known relational database management system declarative query language, T-SQL – but the entities being queried with LINQ code are collections of objects rather than rows within database tables.

The code example depicted in figure 86 shows how T-SQL might be used to query a database table named, `Employees`, in order to bring back all the field values in each row stored in the `Employees` database table.

Figure 86.

```sql
SELECT * FROM Employees

```

In figure 87, a code example is depicted where LINQ in C# code is leveraged to query a collection of `Employee` objects.

Figure 87

```csharp
List<Employee> employees = new List<Employee>();
employees.Add(
    new Employee
    {
        Id = 1,
        FirstName = "Gavin",
        LastName = "Lon",
        Salary = 10000
    }
);
employees.Add(
    new Employee
    {
        Id = 2,
        FirstName = "Sandy",
        LastName = "James",
        Salary = 90000
    }
);
employees.Add(
    new Employee
    {
        Id = 3,
        FirstName = "Greg",
        LastName = "Jones",
        Salary = 73000
    }
);
var employeeResults = from e in employees select e;
foreach (Employee emp in employees)
{
    Console.WriteLine(emp.FirstName);
}

```

If for example the `Employees` database table contained four fields, namely `Id`, `FirstName`, `LastName` and `Salary`, and you wanted to only bring back the `FirstName` and `LastName` fields through your T-SQL query, your query would look like the example in figure 88.

Figure 88.

```sql
SELECT FirstName, LastName FROM Employees

```

In order to bring back the `FirstName` and `LastName` fields from a collection of objects where each object has an `Id` property, a `FirstName` property, a `LastName` property, and a `Salary` property your LINQ query could be implemented as is shown in the code example in figure 89.

Figure 89.

```csharp
var employeeResults =
    from e in employees
    select new Employee { FirstName = e.FirstName, LastName = e.LastName };

```

There are two types of syntax you can leverage to implement LINQ in C#. The type of syntax you've seen so far in this section is known as query syntax. Another way to implement LINQ code is by using method syntax.

To illustrate the use of query syntax vs method syntax, let's look at a slightly more complex example. In the example depicted in figure 90, a T-SQL query is used to bring back the `FirstName` and `LastName` fields, for rows pertaining to employees that have a salary higher than `50000`.

Figure 90.

```sql
SELECT FirstName, LastName FROM Employees e WHERE e.Salary > 50000

```

Using Query syntax in LINQ to perform the equivalent query against a collection of `Employee` objects, the code would look like what is depicted in figure 91.

Figure 91.

```csharp
var employeeResults =
    from e in employees
    where e.Salary > 50000
    select new Employee
    {
        FirstName = e.FirstName,
        LastName = e.LastName,
        Salary = e.Salary
    };

```

Using method syntax in LINQ, the equivalent query could be implemented with the code depicted in figure 92.

Figure 92.

```csharp
var employeeResults = employees
    .Select(e => new Employee
    {
        FirstName = e.FirstName,
        LastName = e.LastName,
        Salary = e.Salary
    })
    .Where(e => e.Salary > 50000);

```

These LINQ related code examples hopefully give you a sense of how method syntax looks compared to query syntax.

Note that you can't create all LINQ queries using query syntax, so depending on your requirements you may have to use method syntax for performing certain queries using LINQ.

Behind the scenes, the C# compiler converts query syntax to method syntax. Query syntax was introduced in the LINQ technology specifically to improve the readability of your queries.

LINQ is made up of many extension methods that reside within the `System.LINQ` namespace. In the example in figure 92, the `Select` and `Where` LINQ extension methods have been appropriately chained together to create the desired query.

For more detils on LINQ and for more code examples, you can watch the  YouTube video below.

%[https://www.youtube.com/watch?v=UfZOmSCCbDY&list=PL4LFuHwItvKbzDl6MBp3XY0MrnALSfyub]

For a full video series on LINQ, you can go here:

[Full Video Series on Using LINQ in C#](https://www.youtube.com/watch?v=UfZOmSCCbDY&list=PL4LFuHwItvKbzDl6MBp3XY0MrnALSfyub)

## C# Attributes

You can associate metadata with program entities (for example assemblies, types, methods, and properties) through the use of attributes in C#.

Attributes are powerful when combined with reflection (a concept we'll discuss in the next section). Through the use of reflection, the attributes can be queried at runtime and then custom functionality can be executed based on the metadata provided through the use of the relevant attributes.

Attributes in C# are created as objects at runtime. Their properties and methods can be used just like any other object in C#.

There are two broad categories for attributes: predefined attributes and custom attributes. Predefined attributes are built into the base class libraries provided in .NET, and custom attributes allow you to define your own attributes that address your unique application requirements.

An example of a predefined general attribute is the `obsolete` attribute. You can check out figure 93 for a code example depicting how you can use the `obsolete` attribute and how it can be useful when you're attempting to consume an obsolete method (or a method marked as obsolete with the `obsolete` attribute).

In the code example, you can see that the `obsolete` attribute decorates a method named `LogToScreen`. A new updated method named `LogToFile` has been created within the same class to replace the old `LogToScreen` method. So the creator of the `Logging` class would prefer the `LogToFile` method be consumed by developers (when applying logging functionality in calling code) rather than the `LogToScreen` method.

When the consumer of the class tries to use the older obsolete method (in this example, the `LogToScreen` method), a predefined warning message can be displayed to the developer from inside their code editor. This warning message is created to warn developers who wish to consume the logging functionality that the `LogToFile` method should be used for logging and not the obsolete `LogToScreen` method.

So to ensure that an appropriate message is displayed, you can pass an appropriate custom message as an argument to the `obsolete` attribute that appropriately decorates the `LogToScreen` method (which has now been deemed as obsolete). The warning message can for example warn developers that the old method (`LogToScreen`) is now obsolete and direct them to use the new preferred method (`LogToFile`) in its place.

Figure 93.

```csharp
Logging logAction = new Logging();
logAction.LogToScreen("Start of Code"); // This message, "The LogToScreen method is now obsolete. Please use the LogToFile method instead" is flagged by the C# compilerSomeFunction();
logAction.LogToScreen("End of Code"); // This message, "The LogToScreen method is now obsolete. Please use the LogToFile method instead" is flagged by the C# compiler

```

In the example depicted in figure 94, a custom attribute is created through the implementation of a C# class that inherits from the built-in C# class `System.Attribute`. A general predefined attribute named, `AttributeUsage` is used to decorate the class in order to enforce the usage rules associated with the `Required` custom attribute.

The arguments being passed (in this example) to the `AttributeUsage` attribute establish the rules where the `Required` attribute can only be associated with field, parameter, and property program elements, and cannot be applied to the same element multiple times.

The `Required` attribute can only be applied to a particular program element once, and can be applied to fields, parameters, and properties.

In the example depicted in **figure 94**, a very basic use of a custom attribute is implemented where an custom attribute named `RequiredAttribute` is used to decorate certain properties of a model. Note that when a custom attribute is actually applied, the 'Attribute' part of the custom attribute's name can be omitted. So in **figure 94** you can see that the relevant program elements are decorated with the attribute named,`Required` and not `RequiredAttribute`.

The `EmployeeModel` model class is used to represent an `Employee` record. The class named, `EmployeeModel`, provides a template for an employee record. The `Required` attribute gives you the ability to reuse this custom attribute across properties where `Required` validation is necessary (that is, where a user must input a value that is subsequently assigned to the property decorated with the `Required` attribute).

In the calling code, reflection is employed to inspect the property program elements of the `EmployeeModel` user defined type at runtime to see if there are any attributes applied to its properties.

In this basic example, the code queries the `Id` property of the `EmployeeModel` class, and the `Required` attribute is found to be associated with the `Id` property. The code then knows to appropriately validate the user's input for the `Id` property of the `EmployeeModel` class.

Note that the `Required` attribute is also applied to the `FirstName` property. So you can see how an attribute can be applied multiple times in order to address cross cutting concerns.

Figure 94.

```csharp
using System.Reflection;

Console.WriteLine("Please enter an Id for the employee:");
string id = Console.ReadLine();
Type employeeType = typeof(EmployeeModel);
PropertyInfo prop = employeeType.GetProperty("Id");
Attribute[] attributes = prop.GetCustomAttributes().ToArray();
foreach (Attribute attr in attributes)
{
    if (attr is RequiredAttribute)
    {
        if (string.IsNullOrEmpty(id))
        {
            Console.WriteLine(
                "The employee’s Id is required. You did not enter the employee’s Id. "
            );
        }
    }
}

class EmployeeModel
{
    [Required]
    public int Id { get; set; }

    [Required]
    public string FirstName { get; set; }
    public string LastName { get; set; }
}

[AttributeUsage(
    AttributeTargets.Field | AttributeTargets.Parameter | AttributeTargets.Property,
    AllowMultiple = false
)]
class RequiredAttribute : Attribute
{
    public string ErrorMessage { get; set; }

    public RequiredAttribute()
    {
        ErrorMessage = "You cannot leave field, {0}, empty";
    }

    public RequiredAttribute(string errorMessage)
    {
        ErrorMessage = errorMessage;
    }
}

```

You can check out the following video that contains more details and code examples pertaining to C# Attributes.

%[https://youtu.be/JOM6zDb9Wa8]

## Reflection in C#

Reflection is a concept in C#, where the programmer is able to create C# code that can dynamically read the metadata of .NET assemblies at runtime. This gives you a powerful tool where you can create code to dynamically analyse a .NET assembly based on the assembly's metadata at runtime. Your code can for e.g. read the assemblies relevant metadata using Reflection, and output the descriptive metadata about the analysed assembly.

Reflection can even be used to dynamically bind an object to a specific type that resides within the assembly at runtime and execute code that resides within the type’s methods. This is known as late binding.

Most of the time, you won't use reflection to call the code within a .NET assembly and will rather use early binding. Early binding means the C# compiler knows (as it were) about the assemblies' relevant program elements for e.g. an assemblies' classes and public methods at compile time.

Using early binding is the safest way to consume a type’s functionality, because any potential exceptions related to calling code within the early bound object are flagged at compile time. This prevents potentially erroneous code from being released into production, where it can result in runtime errors occurring.

When early binding is used, due to the self-describing nature of .NET assemblies where metadata is stored within the .NET assembly, the C# compiler is able to know (as it were) all the relevant details about the assembly at compile time.

So this metadata stored within .NET assemblies means early binding is possible, where the C# compiler has all the necessary type knowledge, if you like, at compile time.

Using reflection, you are able to use the technique of late binding which occurs at runtime. Late binding can be used to dynamically bind to an object (derived from a type that resides within the relevant assembly) at runtime and consume functionality that resides within the relevant .NET assembly.

This is a powerful tool, but is not a safe way to execute the functionality within a .NET assembly, because late binding means that the calling code learns about the target assembly at runtime by reading its metadata before executing the code within the assembly. The technique of late binding is therefore more prone to runtime errors, as potential errors cannot be dealt with at compile time – that is, before the code within the assembly is executed at runtime.

In the example depicted in figure 96, code within an assembly is dynamically invoked using reflection and late binding.

Figure 95.

```csharp
using System;
using System.Collections.Generic;
using System.Text;

namespace UtilityFunctions
{
    public class BasicMathFunctions
    {
        public double DivideOperation(double number1, double number2)
        {
            return number1 / number2;
        }

        public double MultiplyOperation(double number1, double number2)
        {
            return number1 * number2;
        }
    }
}

```

A code example is depicted in figure 96, where the code resides within a different assembly to the assembly that contains the `BasicMathFunctions` type depicted in figure 95.

In the calling code (depicted in figure 96), reflection is used to late bind to the `BasicMathFunctions` type and call the `MultiplyOperation` method. So the code depicted in figure 95 resides within an assembly denoted by a file named "UtilityFunctions.dll".

The "UtilityFunction.dll" assembly resides within the same directory as the assembly that contains the calling code (depicted in figure 96). Reflection is used to dynamically load the "UtilityFunctions" assembly, late bind to the `BasicMathFunctions` type, and call its `MultiplyOperation` method.

Figure 96.

```csharp
using System.Reflection;

const string TargetAssemblyFileName = "UtilityFunctions.dll";
const string TargetNamespace = "UtilityFunctions";
Assembly assembly = Assembly.LoadFile(
    Path.Combine(AppDomain.CurrentDomain.BaseDirectory, TargetAssemblyFileName)
);
Type classType = assembly.GetType("UtilityFunctions.BasicMathFunctions");
object classInstance = Activator.CreateInstance(classType);
MethodInfo method = classType.GetMethod("MultiplyOperation");
object[] paramValues = new object[2];
paramValues[0] = 2;
paramValues[1] = 3;
object result = method.Invoke(classInstance, paramValues);
Console.WriteLine($"{paramValues[0]} * {paramValues[1]}  = {result}");
// Output:
// 2 * 3  = 6

```

For more details and code examples pertaining to reflection, you can watch the YouTube video below.

%[https://youtu.be/tGMa9qjncjs]

## Video on Asynchronous Programming in C#

I haven't covered Asynchronous programming in this C# book. But if you'd like to learn about Asynchronous programming in C#, you can watch the YouTube video below.

%[https://www.youtube.com/watch?v=MyblIAk8cNI&list=PL4LFuHwItvKb5A9W1myICdC-GJU4_6cKE]

For a full video series on asynchronous programming in C#, check this out:

[Full Video Series on Asynchronous Programming in C#](https://www.youtube.com/watch?v=MyblIAk8cNI&list=PL4LFuHwItvKb5A9W1myICdC-GJU4_6cKE)

If you'd like to learn about how to create sophisticated web applications using C#, I've provided some resources below.

The first link takes you do a YouTube video playlist that provides step by step instructions on how to build a Shopping Cart SPA (Single Page Application) using the Blazor framework. The second link takes you to a YouTube video playlist that provides step by step instructions on how to build a real-word web application using the ASP .NET Core MVC framework.

* [Full Blazor Shopping Cart SPA (Single Page Application) Course](https://www.youtube.com/watch?v=3_AsedRrqww&list=PL4LFuHwItvKbdK-ogNsOx2X58hHGeQm8c)
* [Full ASP .Net CORE MVC Course](https://www.youtube.com/watch?v=D7R_ToqDKHg&list=PL4LFuHwItvKZ6Mz5W5wzD9uo3w6tNChhX)

## Conclusion

The goal of this book is to help you gain an understanding of the powerful features available in the C# programming language. The code examples were designed to provide you with a practical knowledge of these features.

You can apply these code examples yourself using free tools like Visual Studio 2022 Community edition or Visual Studio Code in order to gain hands-on experience working with the concepts discussed in this book.

I have worked with C# for over two decades and have been impressed with the evolution of the language itself as well as the environment in which C# code runs, namely .NET. When you master C#, a whole world of creativity, intellectually challenging concepts, and a multitude of career opportunities will open up to you.

In today’s world, you have the benefit of development tools as well as instructions on how to use those development tools freely available to you. There is also a lot of free content available online on how to use the C# programming language in order to create real-world applications.

Using C#, you can create a large variety of different types of applications. You can create cross platform desktop applications, cross platform mobile applications, a variety of types of web applications like SPAs that leverage the Blazor framework. You can create sophisticated 2D and 3D games. You can create IoT applications. You can create globally distributed cloud native applications that leverage the Micro-service architecture.

You are almost unlimited in terms of the types of applications you can create for a multitude of types of platforms and devices. With C# you can easily integrate AI into your applications as well.

It is a very exciting time to be a C# and .NET developer. I wish you the very best with learning and leveraging this powerful programming language on your journey as a developer!

For a full course for C# beginners and a full Advanced C# course, check out these resources:

* [Full C# for Beginners Course](https://www.youtube.com/watch?v=2pquQMSYk6c&list=PL4LFuHwItvKbneXxSutjeyz6i1w32K6di)
* [Full Advanced C#  Course](https://www.youtube.com/watch?v=3cfVmcAkR2w&list=PL4LFuHwItvKaOi-bN1E2WUVyZbuRhVokL)

