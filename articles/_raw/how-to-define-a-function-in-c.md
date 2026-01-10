---
title: Def in C – How to Define a Function in C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2024-04-12T17:54:27.333Z'
originalURL: https://freecodecamp.org/news/how-to-define-a-function-in-c
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/npxXWgQ33ZQ/upload/070d054c2dafa7e4a5f90cf0d0af30eb.jpeg
tags:
- name: C
  slug: c
- name: c programming
  slug: c-programming
- name: functions
  slug: functions
seo_title: null
seo_desc: 'Functions play a fundamental role in programming in C. They allow you to
  write code that is organized and easier to maintain.

  In this article, you''ll learn the basics of defining functions in C.

  What is a Function in C?

  In programming, a function is ...'
---

Functions play a fundamental role in programming in C. They allow you to write code that is organized and easier to maintain.

In this article, you'll learn the basics of defining functions in C.

## **What is a Function in C?**

In programming, a function is a block of code that performs a specific task.

Functions take inputs, process them, perform operations, and produce an output.

Functions are important because they organize your code and promote code reusability.

Instead of writing the same code again and again and repeating yourself, you write code once and then can use it whenever you want to perform that specific task.

In C, there are generally two types of functions:

* **Standard library functions**. Standard library functions are provided by the C standard library and defined in header files. Examples of standard library functions include `printf()` for printing formatted output to the console and `scanf()` for reading formatted input from the user. Both are defined in the `stdio.h` header file.
    
* **User-defined functions**. User-defined functions are defined by you, the programmer. These functions are tailored to your program’s needs and requirements. For example, a user-defined function may calculate the sum of two numbers or check if a number is even or odd.
    

In this article, you will learn how to create user-defined functions.

## Syntax of Functions in C

Here is the general syntax of a function in C:

```c
return_type function_name(parameter) {
  // function body with the code to be executed
  return value;
}
```

Let’s break it down:

* The `return_type` lets the C compiler know the type of data of the value the function will return after its execution. It can be any valid C data type such as `int`, `float`, `char`, or `void` if the function doesn’t return a value.
    
* The `function_name` is the name you give the function. It should be meaningful and accurately describe what the function does. You will later use this to call the function.
    
* The `parameter` is optional. A parameter is a variable a function accepts as input inside parentheses. A function can receive zero or more parameters. If the function accepts multiple parameters, they are separated by commas. Each parameter consists of the data type followed by a name.
    
* Inside the curly braces, `{}`, is the function’s body. Here is the actual code, the instructions that perform a specific task.
    
* Inside the function body, there can be an optional return value. You use the `return` keyword followed by the value you want to return. If the function has a `voidreturn_type`, you don't need to specify a return value.
    

## How to Call a Function in C

Here is the syntax for calling a function in C:

```c
function_name(arguments);
```

Let's break it down:

* `function_name` is the name of the function you want to call. It should be the same name you used to define your function.
    
* `arguments` are the values you pass to the function. If the function accepts any parameters, you pass the arguments in parentheses when you call the function. Each argument is separated by a comma.
    

If the function returns a value, you can store it in a variable for later use:

```c
data_type result = function_name(arguments);
```

## How to Define and Call a Function in C Example

Let's look at a simple function that adds two numbers:

```c
#include <stdio.h>
int add(int num1, int num2) {
    return num1 + num2;
}

int main(void) {
    int num1, num2, result;

    printf("Enter first number: ");
    scanf("%d", &num1);

    printf("Enter second number: ");
    scanf("%d", &num2);

    result = add(num1, num2);

    printf("The sum of %d and %d is %d\n", num1, num2, result);

    return 0;
}

// Output: 

// Enter first number: 2
// Enter second number: 3
// The sum of 2 and 3 is 5
```

Let’s break down the code step by step.

### Include the Header File

I first included the library `stdio.h` with the line `#include <stdio.h>`.

This line includes the standard input-output library (`<stdio.h>`), which gives you access to the `printf()` and `scanf()` functions. Now, you can receive user input and print text to the console.

### Define the `add` Function

Next, I defined the following function:

```c
int add(int num1, int num2) {
    return num1 + num2;
}
```

This function has an `int` return type, which indicates that it will return an integer value after execution.

The function is named `add`, and inside parentheses, it accepts the integer parameters `num1` and `num2`.

Within the curly braces, the function body contains the function code. In this case, the function code consists of only the return statement `return num1 + num2;`. This code calculates the sum of `num1` and `num2` using the `+` operator, and returns the result.

The `add()` function is defined before being used in the `main()` function later on. In C, functions must be defined before they are used. By placing the `add()` function definition above the `main()` function, the compiler knows about it when it encounters the function call in `main()`.

### Define the `main()` Function

Next, I defined the `main()` function, which is the starting point of every C program:

```c
int main(void) {
    int num1, num2, result;

    printf("Enter first number: ");
    scanf("%d", &num1);

    printf("Enter second number: ");
    scanf("%d", &num2);

    result = add(num1, num2);

    printf("The sum of %d and %d is %d\n", num1, num2, result);

    return 0;
}
```

Inside the `main()` function, I first declared the integer variables `num1`, `num2`, and `result`.

Note that `num1` and `num2` variables are different from the `num1` and `num2` parameters that the `add()` function receives. These two variables will store the numbers that the user will enter.

Then, I prompted the user to enter the first number using the `printf()` function, and used the `scanf()` function to read the input and store it in the variable `num1`. The `%d` format specifier is used to indicate that `scanf()` should expect an integer input.

I followed the exact same procedure for receiving and storing the second number.

Next, I called the `add()` function with the `num1` and `num2` as arguments. The `add()` function will add the two numbers together. The result of the calculation is then stored in the `result` variable.

Following that, I used the `printf()` function to print the `num1`, `num2` and `result` variables to the console. The format specifier `%d` is used to print integer values.

Lastly, the line `return 0;` is a statement that indicates that the program executed successfully. When a C program terminates, it returns an exit status to the operating system, with `0` typically indicating the program executed without any errors.

### Execute the Program

When the program is executed, the `main()` function is called first.

You first see the prompt `Enter first number:`. In my case, I entered `2` as the first number.

Once you enter a number, you will see the second prompt: `Enter second number:`. I entered the number `3` as the second number.

Then, the `add()` function is called, which adds the numbers `2` and `3`.

Lastly, the line `The sum of 2 and 3 is 5` is printed to the console.

## Conclusion

In this article, you learned the very basics of defining functions in C.

Specifically, you learned about the two different types of functions in C, and the general syntax for defining your own functions.

Lastly, you saw an example of a simple function that added two numbers and returned the result.

Thanks for reading, and happy coding!
