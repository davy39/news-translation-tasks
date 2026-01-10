---
title: The C++ Programming Language
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-12T00:28:00.000Z'
originalURL: https://freecodecamp.org/news/the-c-plus-plus-programming-language
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ec1740569d1a4ca3ee9.jpg
tags:
- name: C++
  slug: c-2
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'C++ is a general purpose programming language which was first developed
  in the 1980s. The language was designed by Bjarne Stroustrup under with the name
  “C with classes”.

  C++ is a version of C that includes Object-Oriented elements, including classes...'
---

C++ is a general purpose programming language which was first developed in the 1980s. The language was designed by Bjarne Stroustrup under with the name “C with classes”.

C++ is a version of C that includes Object-Oriented elements, including classes and functions.

It is considered one of the most widely used programming languages, as you can see in the following image:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/image-209.png)

![Img](http://static1.businessinsider.com/image/59deb30392406c21008b6148-1200/for-bonus-points-heres-the-chart-showing-these-languages-relative-popularity.jpg)
_Source: GitHub_

## Hello World in C++

```cpp
#include <iostream>
using namespace std;
int main()
{
    cout << "Hello World" << endl;
    return 0;
}
```

And the output of this program will be:

```text
Hello World!
```

Now, let’s break down the code.

### Lines 1 and 2

```cpp
#include <iostream>
using namespace std;
```

The first line tells the computer to use the `iostream` header file for this specific program. A header file is a separate file with prewritten C++ code.   
  
There are many other header files which are required for a specific program to run properly. Some of them are `math`, `vector`, and `string`. Header files are generally represented by a `.h` extension (you don’t need to add `.h` when including C++ standard library files)

`iostream` stands for "input-output stream". The `iostream` file contains code for allowing the computer to take input and generate an output, using the C++ language.

The second line, `using namespace std;`, tells the computer to use the standard namespace which includes features of standard C++.  
  
You could write this program without this line, but you’d have to use `std::cout` instead of `cout` and `std::endl` instead of `endl` on line 4. But the second line makes the code more readable and our lives as programmers easier.

### Lines 3 and 4

```cpp
int main()
{
```

C++ starts the execution of a program from the global `main()` function, which is declared with `int main()`. During execution, the computer starts running the code from every line from the opening curly brace, `{`, to the closing curly brace, `}`.  
  
Note: Every function starts with `{` and ends with `}`.

Line 4 indicates the start of the `main()` function with the opening curly brace.

### Lines 5, 6, and 7

```cpp
    cout << "Hello World" << endl;
    return 0;
}
```

`cout` stands for "character output", and is an object to display output on the screen.

`cout` is followed by `<<`, which is an insertion operator. Insertion operators send data to the stream operators that come before them.

Next is the phrase `Hello World` surrounded by double quotes (`"`). Anything between double quotes is a string. This is a simple string with standard characters, but certain special characters have a different syntax for print statements.

So the insertion operator, `<<`, passes the string `"Hello World"` to the `cout` object.

But if you look at the end of the line, there's another insertion operator and `endl`.

`endl` is a reserved word in the C++ language, and stand for "end line". In C++, you can use the `endl` object to end the current line, flush the stream, and go to the next line in the output.

Finally, the line ends with a semicolon, `;`.

So looking at line 5, both the string `"Hello World"` and the `endl` are passed to `cout` with insertion operators, and the line ends with a semicolon.

On line 6, `return 0;` safely terminates the current function, `main()`. And since there's no function after `main()`, the entire program is terminated.

Finally on line 7, the `main()` function ends with a closing curly brace, `}`. If you don't end a function with a closing curly brace, you'll run into an execution error.

## Review

Again, your code should look something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/07/cpp-hello-world-review.jpg)

Congratulations! You've written your first C++ program, and have taken your first steps to learning C++.

To actually compile and run your C++ program, check out these tutorials:

* [C++ Compiler Explained: What is the Compiler and How Do You Use it?](https://www.freecodecamp.org/news/c-compiler-explained-what-is-the-compiler-and-how-do-you-use-it/)
* [How to compile your C++ code in Visual Studio Code](https://www.freecodecamp.org/news/how-to-compile-your-c-code-in-visual-studio-code/)

