---
title: Action and Func Delegates in C# – Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-06T19:46:15.000Z'
originalURL: https://freecodecamp.org/news/action-and-func-delegates-in-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Untitled--Copy---1-.png
tags:
- name: C
  slug: c
seo_title: null
seo_desc: "By Umoh Tobby\nIn C#, types called delegates represent references to methods\
  \ with specific signatures. \nDevelopers use delegates to implement callback methods,\
  \ handle events, and perform tasks where executing a method at a later time is necessary.\
  \ \nC#..."
---

By Umoh Tobby

In C#, types called delegates represent references to methods with specific signatures. 

Developers use delegates to implement callback methods, handle events, and perform tasks where executing a method at a later time is necessary. 

C# offers various delegates, and two commonly used ones are Action and Func, both defined in the System namespace.

In this tutorial, you'll learn about the Action and Func delegates in C#.

To download the source code for this article, visit this **[GitHub Repository](https://github.com/TobbyJay/ActionAndFuncDelegate)**.

Let’s begin by discussing the Action delegate and exploring its usage

## What is the Action Delegate in C#?

The Action delegate is a predefined delegate type that encapsulates a method with zero or more input parameters that doesn't return a value. In other words, an Action delegate represents a void-returning method.

Consider this example, demonstrating the usage of an Action delegate in a simple console calculator application:

```c#
Action<int, int> ActionCalculator = (a, b) =>
{
    Console.WriteLine($"Addition result: {a + b}");
    Console.WriteLine($"Subtraction result: {a - b}");
    Console.WriteLine($"Multiplication result: {a * b}");
    Console.WriteLine($"Division result: {a / b}");
};

ActionCalculator(4, 2);
```

In this example, we defined an Action delegate named ActionCalculator. It takes two integer parameters and performs four basic arithmetic operations using those parameters. Then, we invoke the delegate with the values 4 and 2.

The application produced the following output upon running:

```c#
Addition result: 6
Subtraction result: 2
Multiplication result: 8
Division result: 2
```

As you can see, utilizing an Action delegate simplifies the process of passing a method as a parameter to another method.

## What is the Func Delegate in C#?

The Func delegate is another predefined delegate type that represents a method with zero or more input parameters that returns a value. Unlike the Action delegate, the return type of a Func delegate can be any type.

Let’s consider an example of using a Func delegate in a simple console calculator application.

In this example, we define a Calculator class:

```c#
public class Calculator
{
    public int Add(int a, int b) => a + b;
    public int Subtract(int a, int b) => a - b;
    public int Multiply(int a, int b) => a * b;
    public int Divide(int a, int b) => a / b;
}
```

The Calculator class contains methods to perform four basic arithmetic operations.

Next, we create four Func delegates, with each delegate pointing to one of the calculator’s methods:

```c#
var FuncCalculator = new Calculator();

Func<int, int, int> add = FuncCalculator.Add;
Func<int, int, int> subtract = FuncCalculator.Subtract;
Func<int, int, int> multiply = FuncCalculator.Multiply;
Func<int, int, int> divide = FuncCalculator.Divide;

Console.WriteLine($"Addition result: {add(4, 2)}");
Console.WriteLine($"Subtraction result: {subtract(4, 2)}");
Console.WriteLine($"Multiplication result: {multiply(4, 2)}");
Console.WriteLine($"Division result: {divide(4, 2)}");
```

Finally, we invoke each of the delegates with the values 4 and 2 and print the results to the console.

The calculator application displayed the following output upon running:

```c#
Addition result: 6
Subtraction result: 2
Multiplication result: 8
Division result: 2
```

Func delegates offer a straightforward approach to defining and utilising methods by passing them as parameters and returning them as results.

## **Conclusion**

In conclusion, Action and Func delegates provide a way to encapsulate a method call within a delegate object. 

Developers use Action delegates when a method does not return a value, and Func delegates when a method returns a value.

