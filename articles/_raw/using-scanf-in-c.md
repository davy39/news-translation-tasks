---
title: How to Use scanf( ) in C to Read and Store User Input
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-03-06T21:59:30.000Z'
originalURL: https://freecodecamp.org/news/using-scanf-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-element-digital-1370294.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: "The scanf() function is a commonly used input function in the C programming\
  \ language. It allows you to read input from the user or from a file and store that\
  \ input in variables of different data types. \nInput is an essential part of most\
  \ programs, an..."
---

The `scanf()` function is a commonly used input function in the C programming language. It allows you to read input from the user or from a file and store that input in variables of different data types. 

Input is an essential part of most programs, and the `scanf()` function provides an easy way to read input in a variety of formats. But it's important to use `scanf()` carefully and to always validate user input to prevent security vulnerabilities and unexpected program behavior. 

In this article, we'll take a closer look at the `scanf()` function and how to use it effectively in C programming.

### **What you will learn**

Here are some things that you will learn:

1. What `scanf()` is and what it's used for
2. How to use `scanf()` to read input from the user or from a file
3. The syntax of the `scanf()` function and how to use conversion specifiers to read input
4. How to store input in variables using pointers
5. The importance of input validation and error checking to prevent unexpected program behavior and security vulnerabilities

## Syntax of the `scanf()` function

The basic syntax of the `scanf()` function is as follows:

```c
int scanf(const char *format, ...);
```

The `scanf()` function returns the number of items successfully read, or `EOF` if an error occurs or the end of the input stream is reached. 

The function takes two arguments:

1. `format`: A string that specifies the format of the input to be read. This string can contain conversion specifiers that tell `scanf()` what type of input to expect and how to read it. See the next section for more details on conversion specifiers.
2. `...`: A variable-length argument list that contains the memory addresses of variables where the input values will be stored. These memory addresses must be passed as pointers.

## How to Use Conversion Specifiers to Read Input

The `scanf()` function takes a format string as its first argument, which specifies the format and data types of the input that will be read. 

The format string can include conversion specifiers, which begin with the percent sign (`%`) and are followed by one or more characters that specify the type of data to be read. 

The most common conversion specifiers are:

* `%d`: reads an integer value
* `%f`: reads a floating-point value
* `%c`: reads a single character
* `%s`: reads a string of characters
* `%lf`: reads a double-precision floating-point value

After the format string, the `scanf()` function takes a variable number of arguments, each of which is a pointer to the variable where the input value will be stored. The number and type of arguments must match the conversion specifiers in the format string.

For example, the following code reads an integer value and a floating-point value from the user, and stores them in the variables `num` and `fnum`, respectively:

```c
#include <stdio.h>

int main() {
    int num;
    float fnum;
    printf("Enter an integer and a floating-point number: ");
    scanf("%d %f", &num, &fnum);
    printf("You entered %d and %f\n", num, fnum);
    return 0;
}

```

Below is the expected output:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-from-2023-03-06-11-06-14.png)
_output_

In this example, the format string `"%d %f"` tells `scanf()` to read an integer value followed by a floating-point value, separated by a space. The `&` operator is used to pass the address of the `num` and `fnum` variables to `scanf()`, so that the input values can be stored in those variables.

## Conversion Specifiers vs Type Specifiers

In the C programming language, "conversion specifiers" and "type specifiers" are related concepts, but they have different meanings and purposes.

A "type specifier" is a keyword that specifies the data type of a variable or expression. For example, the `int`, `float`, and `char` keywords are type specifiers that indicate integer, floating-point, and character data types, respectively. We use type specifiers to declare variables and functions and to define the return type of a function.

On the other hand, a "conversion specifier" is a symbol we use in format strings to specify the format of input and output operations. Conversion specifiers start with the `%` character, followed by a single letter or sequence of characters that indicates the type of data to be read or written. For example, the `%d` conversion specifier reads integer values, while the `%f` specifier reads floating-point values.

In summary, type specifiers are used to specify the data type of variables and expressions, while conversion specifiers are used to specify the format of input and output operations. Both concepts are important in C programming and are used in different contexts.

## How to Store Input in Variables Using Pointers

To store input in a variable using `scanf()`, you need to pass the memory address of the variable as an argument to the function using the `&` (address of) operator. This is because `scanf()` expects pointers as arguments to store input values directly in memory locations.

Here's an example of using `scanf()` to read an integer value from the user and store it in a variable called `num`:

```c
int num;
printf("Enter an integer: ");
scanf("%d", &num);
```

In this example, the `%d` conversion specifier tells `scanf()` to expect an integer input value. The memory address of the `num` variable is passed to `scanf()` using the `&` operator, which returns a pointer to the memory location of `num`.

If you need to read multiple input values, you can pass multiple pointers as arguments to `scanf()` in the order that they appear in the format string. For example, to read two integer values and store them in variables `num1` and `num2`, you could do:

```c
int num1, num2;
printf("Enter two integers: ");
scanf("%d %d", &num1, &num2);
```

Note that it's important to make sure that the data types of the input values match the data types of the variables that you're storing them in. If the types don't match, the input value may be interpreted incorrectly, leading to unexpected program behavior. 

Additionally, it's a good practice to validate input values and handle input errors, as discussed in the next section.

## Input Validation and Error Checking

Input validation and error checking are important concepts in programming, especially when dealing with user input or input from external sources. In C, you can use various techniques to validate input and handle input errors.

One common technique is to use the return value of `scanf()` to check if the input operation was successful or if an error occurred. The `scanf()` function returns the number of input values that were successfully read and stored, or `EOF` if an error occurred or the end of the input stream was reached. 

By checking the return value, you can determine if the input operation was successful or if an error occurred.

For example, if you're using `scanf()` to read an integer value from the user and store it in a variable called `num`, you could use the following code to validate the input:

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int num;
    printf("Enter an integer: ");
    if (scanf("%d", &num) != 1) {
        printf("Error: Invalid input\n");
        exit(1);
    }
    return 0;
}

```

In this example, the `scanf()` function is used to read an integer value and store it in the `num` variable. The return value of `scanf()` is compared to `1` to check if one input value was successfully read and stored. If the return value is not `1`, an error message is printed to the console and the program exits with an error code.

Below is the expected output:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-from-2023-03-06-11-02-36.png)
_Output_

You can use similar techniques to validate input of other types, such as floating-point numbers or strings. For example, to validate the input of a floating-point value, you could use the `%f` conversion specifier and check if the return value of `scanf()` is equal to `1`.

In addition to checking the return value of `scanf()`, you can also use other techniques to validate input and handle errors, such as using `fgets()` to read input as a string and then parsing the string to extract the desired values, or using regular expressions to validate input patterns.

It's important to carefully validate input and handle errors to prevent unexpected program behavior or security vulnerabilities.

## `scanf()` and the Standard C Library

The `scanf()` function is included in the standard C library, which provides a collection of pre-defined functions that you can use in C programs. The `stdio.h` header file is also part of the standard C library and contains declarations for input and output functions like `scanf()`, `printf()`, and others.

To use the `scanf()` function in a C program, you need to include the `stdio.h` header file at the beginning of your program using the `#include` preprocessor directive. This allows you to access the functions and data types defined in the standard C library, including `scanf()`.

Here's an example of how to use `scanf()` in a C program:

```c
#include <stdio.h>

int main() {
    int num;
    printf("Enter an integer: ");
    scanf("%d", &num);
    printf("You entered: %d\n", num);
    return 0;
}
```

In this example, we first include the `stdio.h` header file using `#include`. We then define a variable `num` of type `int`. We use the `printf()` function to prompt the user to enter an integer, and the `scanf()` function reads the user's input and stores it in the `num` variable. Finally, we use another `printf()` statement to print the value of `num`.

Note that we use the `&` operator before the variable name in the `scanf()` function to pass the memory address of the variable to the function. This allows the `scanf()` function to store the user's input directly in the variable.

## Conclusion

The `scanf()` function in C is a powerful tool for reading input from the user or from a file and storing it in variables. By specifying conversion specifiers in the format string, you can read input values of different types, such as integers, floating-point numbers, and strings.

When using `scanf()`, it's important to be aware of potential input errors and to validate input values to prevent unexpected program behavior or security vulnerabilities. 

You can use the return value of `scanf()` to check if the input operation was successful. You can also use various techniques to validate input and handle errors, such as checking input ranges, using regular expressions, or converting input values to strings and parsing them.

Overall, `scanf()` is a versatile function that you can use in a variety of programming scenarios. By understanding how to use `scanf()` effectively and how to validate and handle input errors, you can build robust and reliable C programs that interact with users and external data sources in a safe and secure manner.

  

