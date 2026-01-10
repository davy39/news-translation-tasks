---
title: How to Use Functions in C - Explained With Examples
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-04-06T14:20:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-functions-in-c
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/guillaume-bolduc-uBe2mknURG4-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
- name: functions
  slug: functions
seo_title: null
seo_desc: "Functions are an essential component of the C programming language. They\
  \ help you divide bigger problems into smaller, more manageable chunks of code,\
  \ making it simpler to create and run programs. \nWe'll look at functions in C,\
  \ their syntax, and how ..."
---

Functions are an essential component of the C programming language. They help you divide bigger problems into smaller, more manageable chunks of code, making it simpler to create and run programs. 

We'll look at functions in C, their syntax, and how to use them successfully in this article.

## What is a Function in C?

A function is a block of code that executes a particular task in programing. It is a standalone piece of code that can be called from anywhere in the program. 

A function can take in parameters, run computations, and output a value. A function in C can be created using this syntax:

```c
return_type function_name(parameter list) {
   // function body
}

```

The `return_type` specifies the type of value that the function will return. If the function does not return anything, the `return_type` will be `void`. 

The `function_name` is the name of the function, and the `parameter list` specifies the parameters that the function will take in.

## How to Declare a Function in C

Declaring a function in C informs the compiler about the presence of a function without giving implementation details. This enables the function to be called by other sections of the software before it is specified or implemented.

A function declaration usually contains the `function name`, `return type`, and the parameter types. The following is the syntax for defining a function in C:

```c
return_type function_name(parameter_list);

```

Here, `return_type` is the data type of the value that the function returns. `function_name` is the name of the function, and `parameter_list` is the list of parameters that the function takes as input.

For example, suppose we have a function called `add` that takes two integers as input and returns their sum. We can declare the function as follows:

```c
int add(int num1, int num2);

```

This tells the compiler that there is a function called `add` that takes two integers as input and returns an integer as output.

It's worth noting that function declarations do not include the function body, which includes the actual code that runs when the function is invoked. 

The body of the function is defined independently of the function statement, usually in a separate block of code called the function definition.

Here's an example:

```c
#include <stdio.h>

/* function statement */
int add(int a, int b);

/* function definition */
int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(2, 3);
    printf("The result is %d\n", result);
    return 0;
}

```

In this example, the `add` function is declared with a function statement at the top of the file, which specifies its name, return type (`int`), and parameters (`a` and `b`, both `int`s).

The actual code for the `add` function is defined in the function definition. Here, the function simply adds its two parameters and returns the result.

The `main` function calls the `add` function with arguments `2` and `3`, and stores the result in the `result` variable. Finally, it prints the result using the `printf` function.

### How to Use a Function in Multiple Source Files

If you want to use a function in numerous source files, you must include a function declaration (also known as a function prototype) in the header file and the definition in one source file.

when you build, you first compile the source files to object files, and then you link the object files into the final executable.

Let's create a header file called `myfunctions.h`:

```c
#ifndef MYFUNCTIONS_H
#define MYFUNCTIONS_H

int add(int a, int b);// Function prototype, its declaration

#endif /* MYFUNCTIONS_H */

```

In this header file, we declare a function `add` using a function statement.

Next, let's create a source file called `myfunctions.c`, which defines the `add` function:

```c
#include "myfunctions.h"

int add(int a, int b) {
    return a + b;
}

```

In this file, we include the `myfunctions.h` header file using quotes, and we define the `add` function.

Finally, let's create a source file called `main.c`, which uses the `add` function:

```c
#include <stdio.h>
#include "myfunctions.h"

int main() {
    int a = 10, b = 5;
    int sum = add(a, b);

    printf("Sum of %d and %d is %d\n", a, b, sum);

    return 0;
}

```

In this file, we include both the `stdio.h` header file and our `myfunctions.h` header file using angle brackets and quotes, respectively. We then call the `add` function, passing in values `a` and `b` and storing the result in `sum`. Finally, we print the result using `printf`.

 The way you create it is heavily influenced by your environment. If you are using an IDE (such as Visual Studio), you must position all files in the proper locations in the project.

If you are creating from the command line e.g Linux. To compile this program, you would need to compile both `myfunctions.c` and `main.c` and link them together as shown below:

```
gcc -c myfunctions.c
gcc -c main.c
gcc -o program main.o myfunctions.o

```

The `-c` option instructs the compiler to create an object file with the same name as the source file but with a `.o` suffix. The final instruction joins the two object files to create the final executable, which is named `program` (the -o option specifies the name of the output file).

## What Happens if You Call a Function Before Its Declaration in C?

In this instance, the computer believes the usual return type is an integer. If the function gives a different data type, it throws an error. 

If the return type is also an integer, it will function properly. But some cautions may be generated:

```c
#include<stdio.h>
main() {
   printf("The returned value: %d", function);
}
char function() {
   return 'V';
}

```

In this code, the function `function()` is  called before it is declared. This returns an error:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-from-2023-04-05-14-03-36.png)
_warnings and errors_

## How to Define a Function in C

Assuming you want to create a code that accepts two integers and returns their sum, you can define a function that does that this way:

```c
int sum(int num1, int num2) {
   int result = num1 + num2;
   return result;
}

```

In this example, the function `sum` takes in two integer parameters – `num1` and `num2`. The function calculates their sum and returns the result. The return type of the function is `int`.

## Where Should a Function Be Defined?

In C, a function can be defined anywhere in the program, as long as it is defined before it is used. But it is a good practice to define functions at the beginning of the file or in a separate file to make the code more readable and organized.

Here's an example code showing how to define a function in C:

```c
#include <stdio.h>

// function declaration (also known as function prototype)
int add(int a, int b);

int main() {
   int x = 10, y = 20, sum;
   sum = add(x, y);
   printf("The sum of %d and %d is %d\n", x, y, sum);
   return 0;
}

// function definition
int add(int a, int b) {
   int result;
   result = a + b;
   return result;
}

```

In this example, the function `add()` is defined after its declaration (or prototype) within the same file.

Another approach is to define the function in a separate header file, which is then included in the main file using the `#include` directive. For example:

```c
// header file: math.h
#ifndef MATH_H
#define MATH_H

int add(int a, int b);

#endif

```

```c
// main file: main.c
#include <stdio.h>
#include "math.h"  // include the header file

int main() {
   int x = 10, y = 20, sum;
   sum = add(x, y);
   printf("The sum of %d and %d is %d\n", x, y, sum);
   return 0;
}
```

```c
// implementation file: math.c
int add(int a, int b) {
   int result;
   result = a + b;
   return result;
}
```

In this approach, the function declaration (or prototype) is included in the header file `math.h`, which is then included in the main file `main.c` using the `#include` directive. The function implementation is defined in a separate file `math.c`.

This approach allows for better code organization and modularity, as the function implementation can be separated from the main program code.

### How to Call a Function in C

We can call a function from anywhere in the program once we've defined it. We use the function name followed by the argument list in parentheses to call a function. For example, we can use the following code to call the `sum` function that we defined earlier:

```c
int a = 5;
int b = 10;
int c = sum(a, b);

```

In this code, we are calling the `sum` function with `a` and `b` as its parameters. The function returns the sum of `a` and `b`, which is then stored in the variable `c`.

## How to Pass Parameters to a Function

There are two methods of passing parameters (also called arguments) to a function in C: by value and by reference. 

When we pass a parameter by value, the method receives a copy of the parameter's value. Changes to the parameter within the code have no effect on the initial variable outside the function. 

When we pass a parameter by reference, the method receives a link to the parameter's memory location. Any modifications to the parameter within the code will have an impact on the initial variable outside the function.

Consider the following examples of passing parameters by value and by reference. Assuming we want to create a function that accepts an integer and multiplies it by two, the function can be defined as follows:

```c
void doubleValue(int num) {
   num = num * 2;
}

```

In this example, the function `doubleValue` takes in an integer parameter `num` by value. It doubles the value of `num` and assigns it back to `num`. However, this change will not affect the original value of `num` outside the function.

Here's another example that shows how you can pass a single parameter by value:

```c
#include <stdio.h>

void square(int num) {
    // Function to calculate the square of a number.
    int result = num * num;
    printf("%d\n", result);
}

int main() {
    square(5);  // Output: 25
    return 0;
}

```

In this example, we define a function called `square` that takes an integer parameter `num` by value. Inside the function, we calculate the square of `num` and print the result. We then call the function with the argument `5`.

Now, let's look at an example of passing a parameter by reference:

```c
#include <stdio.h>

void square(int* num) {
    // Function to calculate the square of a number.
    *num = (*num) * (*num);
}

int main() {
    int x = 5;
    square(&x);
    printf("%d\n", x);  // Output: 25
    return 0;
}

```

In this example, we define a function `square` that takes an integer pointer parameter `num` by reference. Inside the function, we reference the pointer and calculate the square of the value pointed to by `num`. 

We then call the function with the address of the integer variable `x`. After calling the function, the value of `x` is modified to be the square of its original value, which we then print in the `main` function.

## Conclusion

In conclusion, functions are an essential component of C programming. You can use them to divide large problems into smaller, more manageable pieces of code.

You can declare and define functions in C, and pass parameters either by value or by reference. It's a good practice to declare all functions before using them, and to define them at the beginning of the file or in a separate file for better code organization and modularity. 

By using functions effectively, you can write cleaner, more readable code that is easier to debug and maintain.

