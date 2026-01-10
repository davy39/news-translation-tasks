---
title: Extern – C and C++ Extern Keyword Function Tutorial
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-04-21T00:08:58.000Z'
originalURL: https://freecodecamp.org/news/extern-keyword-function-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Extern---C-and-C---Extern-Keyword-Function-Tutorial.png
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: "The extern keyword in C and C++ extends the visibility of variables and\
  \ functions across multiple source files. \nIn the case of functions, the extern\
  \ keyword is used implicitly. But with variables, you have to use the keyword explicitly.\n\
  I believe a ..."
---

The `extern` keyword in C and C++ extends the visibility of variables and functions across multiple source files. 

In the case of functions, the `extern` keyword is used implicitly. But with variables, you have to use the keyword explicitly.

I believe a simple code example can explain things better in some cases than a wall of text. So I'll quickly setup a simple C++ program for demonstration. 

If you have GCC installed on your system you may follow along. Otherwise, I'll include outputs from each code snippet with them for you to read through.

## `extern` with Functions

In the example, I have two C++ files named `main.cpp` and `math.cpp` and a header file named `math.h`. Code for the `math.h` file is as follows:

```header
int sum(int a, int b);
```

As you can see, the header file contains the declaration for a simple function called `sum` that takes two integers as parameters. The code for the `math.cpp` file is as follows:

```cpp
int sum(int a, int b) {
    return a + b;
}
```

This file contains the definition for the previously declared `sum` function and it returns the sum of the given parameters as an integer.

Finally, the code for the `main.cpp` file is as follows:

```cpp
#include <iostream>
#include "math.h"

int main () {
    std::cout << sum(10, 8) << std::endl;
}
```

This file includes the `math.h` header file containing the declaration for the `sum` function. Then inside the `main` function, the `std::cout << sum(10, 8) << std::endl;` statement calls the `sum` functions by passing `10` and `8` as the two parameters and prints out whatever the returned value is.

Now if you try to compile this program you'll see it compiles without any problem and upon executing the resultant binary file, you'll see following output in the console:

```
18
```

This works (even though the definition of the `sum` function is in a separate file than `main.cpp`) because all the functions in C/C++ are declared as `extern`. This means they can be invoked from any source file in the whole program. 

You can declare the function as `extern int sum(int a, int b)` instead but this will only cause redundancy.

## `extern` with Variables

Although the `extern` keyword is applied implicitly to all the functions in a C/C++ program, the variables behave a bit differently. 

Before I dive into the usage of `extern` with variables, I would like to clarify the difference between declaring a variable and defining it.

Declaring a variable simply declares the existence of the variable to the program. It tells the compiler that a variable of a certain type exists somewhere in the code. You declare a float variable as follows:

```cpp
float pi;
```

At this point, the variable doesn't have any memory allocated to it. The compiler only knows that a `float` variable named `pi` exists somewhere in the code.

Defining the variable, on the other hand, means declaring the existence of the variable, as well as allocating the necessary memory for it. You define a variable as follows:

```cpp
float pi = 3.1416;
```

You can declare a variable as many times as you want, but you can define a variable only once. This is because you can not allocate memory to the same variable multiple times.

Now, I'll modify the `math.h` header file created in the previous section to contain the declaration for the `pi` variable as follows:

```header
extern float pi;
int sum(int a, int b);
```

As you can see, the variable has been declared as an `extern` in the header file, which means this should be accessible anywhere in the program. Next, I'll update the `main.cpp` file as follows:

```cpp
#include <iostream>
#include "math.h"

int main () {
    std::cout << pi << std::endl;
    std::cout << sum(10, 8) << std::endl;
}
```

I've added a new `std::cout` statement to print out the value of the `pi` variable. If you try to compile this program at this point, the compilation process will fail.

```
Starting build...
C:\mingw64\bin\g++.exe -fdiagnostics-color=always -g C:\Users\shovi\repos\cpp-playground\extern\*.cpp -o C:\Users\shovi\repos\cpp-playground\extern\extern.exe
c:/mingw64/bin/../lib/gcc/x86_64-w64-mingw32/11.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:\Users\shovi\AppData\Local\Temp\ccFIWkmh.o:main.cpp:(.rdata$.refptr.pi[.refptr.pi]+0x0): undefined reference to `pi'
collect2.exe: error: ld returned 1 exit status

Build finished with error(s).
```

This happens because, declaring the variable has let the compiler know that this variable exists somewhere in the program – but in reality it doesn't. It has no memory allocation at all.

To get out of this problem, I'll define the `pi` variable inside the `math.cpp` file as follows:

```cpp
float pi = 3.1416;

int sum(int a, int b) {
    return a + b;
}
```

The compilation process finishes without any issues, and if I execute the resultant binary, I'll see the following output in my console:

```
3.1416
18
```

Since the `pi` variable has been declared as an `extern` and has been defined within the `math.cpp` file, the `main.cpp` file is able to access the value of `pi` without any problem at all. 

You can define the variable anywhere in the program but I chose the `math.cpp` file for definition to prove the point that this `extern` variable indeed is available to all the other source files as well.

## Conclusion

Even though it's not used that often, the `extern` keyword in C/C++ is undoubtedly one of the most important concept to understand. I hope you've understood how the keyword works at a basic level from this short article.

As you continue to use the keyword in your programs, you'll definitely come across problems and situations that are outside the scope of this article. Feel free to reach out to me in [Twitter](https://twitter.com/frhnhsin) and [LinkedIn](https://www.linkedin.com/in/farhanhasin/) if you think I can be of help. Otherwise, [Stack Overflow](https://stackoverflow.com/) is always there to help.

Also, if you're native Bengali speaker, checkout freeCodeCamp's [Bengali Publication](https://www.freecodecamp.org/bengali/news/) and [YouTube Channel](https://www.youtube.com/channel/UCYl5XjGuTM1gbXUuxH1e0jA). Till the next one, stay safe and keep learning.

