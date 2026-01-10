---
title: The C Programming Handbook for Beginners
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-08-29T20:38:16.000Z'
originalURL: https://freecodecamp.org/news/the-c-programming-handbook-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726039032547/73b9df27-a4f7-4ee2-81c0-d1e3db521cdb.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: c programming
  slug: c-programming
- name: handbook
  slug: handbook
seo_title: null
seo_desc: 'C is one of the oldest, most widely known, and most influential programming
  languages.

  It is used in many industries because it is a highly flexible and powerful language.

  Learning C is a worthwhile endeavor – no matter your starting point or aspirat...'
---

C is one of the oldest, most widely known, and most influential programming languages.

It is used in many industries because it is a highly flexible and powerful language.

Learning C is a worthwhile endeavor – no matter your starting point or aspirations – because it builds a solid foundation in the skills you will need for the rest of your programming career.

It helps you understand how a computer works underneath the hood, such as how it stores and retrieves information and what the internal architecture looks like.

With that said, C can be a difficult language to learn, especially for beginners, as it can be cryptic.

This handbook aims to teach you C programming fundamentals and is written with the beginner programmer in mind.

There are no prerequisites, and no previous knowledge of any programming concepts is assumed.

If you have never programmed before and are a complete beginner, you have come to the right place.

Here is what you are going to learn in this handbook:

* [Chapter 1: Introduction to C Programming](#chapter-1)
    
* [Chapter 2: Variables and Data Types in C](#chapter-2)
    
* [Chapter 3: Operators in C](#chapter-3)
    
* [Chapter 4: Conditional Statements in C](#chapter-4)
    
* [Chapter 5: Loops in C](#chapter-5)
    
* [Chapter 6: Arrays in C](#chapter-6)
    
* [Chapter 7: Strings in C](#chapter-7)
    
* [Further learning: Advanced C Topics](#further-learning)
    

Without further ado, let’s get started with learning C!

## Chapter 1: Introduction to C Programming

In this introductory chapter, you will learn the main characteristics and use cases of the C programming language.

You will also learn the basics of C syntax and familiarize yourself with the general structure of all C programs.

By the end of the chapter, you will have set up a development environment for C programming so you can follow along with the coding examples in this book on your local machine.

You will have successfully written, compiled, and executed your first simple C program that prints the text "Hello, world!" to the screen.

You will have also learned some core C language features, such as comments for documenting and explaining your code and escape sequences for representing nonprintable characters in text.

### What Is Programming?

Computers are not that smart.

Even though they can process data tirelessly and can perform operations at a very high speed, they cannot think for themselves. They need someone to tell them what to do next.

Humans tell computers what to do and exactly how to do it by giving them detailed and step-by-step instructions to follow.

A collection of detailed instructions is known as a program.

Programming is the process of writing the collection of instructions that a computer can understand and execute to perform a specific task and solve a particular problem.

A programming language is used to write the instructions.

And the humans who write the instructions and supply them to the computer are known as programmers.

#### Low-level VS High-Level VS Middle-level Programming Languages – What's The Difference?

There are three types of programming languages: low-level languages, high-level languages, and middle-level languages.

Low-level languages include machine language (also known as binary) and assembly language.

Both languages provide little to no abstraction from the computer's hardware. The language instructions are closely related to or correspond directly to specific machine instructions.

This 'closeness to the machine' allows for speed, efficiency, less consumption of memory, and fine-grained control over the computer's hardware.

Machine language is the lowest level of programming languages.

The instructions consist of series of `0`s and `1`s that correspond directly to a particular computer’s instructions and locations memory.

Instructions are also directly executed by the computer’s processor.

Even though machine language was the language of choice for writing programs in the early days of computing, it is not a human-readable language and is time-consuming to write.

Assembly language allows the programmer to work closely with the machine on a slightly higher level.

It uses mnemonics and symbols that correspond directly to a particular machine’s instruction set instead of using sequences of `0`s and `1`s.

Next, high-level languages, like Python and JavaScript, are far removed from the instruction set of a particular machine architecture.

Their syntax resembles the English language, making them easier to work with and understand.

Programs written in high-level languages are also portable and machine-independent. That is, a program can run on any system that supports that language.

With that said, they tend to be slower, consume more memory, and make it harder to work with low-level hardware and systems because of how abstract they are.

Lastly, middle-level languages, like C and C++, act as a bridge between low-level and high-level programming languages.

They allow for closeness and a level of control over computer hardware. At the same time, they also offer a level of abstraction with instructions that are more human-readable and understandable for programmers to write.

### What Is the C Programming Language?

C is a general-purpose and procedural programming language.

A procedural language is a type of programming language that follows a step-by-step approach to solving a problem.

It uses a series of instructions, otherwise known as procedures or functions, that are executed in a specific order to perform tasks and accomplish goals. These intructions tell the computer step by step what to do and in what order.

So, C programs are divided into smaller, more specific functions that accomplish a certain task and get executed sequentially, one after another, following a top-down approach.

This promotes code readability and maintainability.

#### A Brief History of the C Programming Language

C was developed in the early 1970s by Dennis Ritchie at AT&T Bell Laboratories.

The development of C was closely tied to the development of the Unix operating system at Bell Labs.

Historically, operating systems were typically written in Assembly language and without portability in mind.

During the development of Unix, there was a need for a more efficient and portable programming language for writing operating systems.

Dennis Ritchie went on to create a language called B, which was an evolution from an earlier language called BCPL (Basic Combined Programming Language).

It aimed to bridge the gap between the low-level capabilities of Assembly and the high-level languages used at the time, such as Fortran.

B was not powerful enough to support Unix development, so Dennis Ritchie developed a new language that took inspiration from B and BCPL and had some additional features. He named this language C.

C’s simple design, speed, efficiency, performance, and close relationship with a computer’s hardware made it an attractive choice for systems programming. This led to the Unix operating system being rewritten in C.

#### C Language Characteristics and Use Cases

Despite C being a relatively old language (compared to other, more modern, programming languages in use today), it has stood the test of time and still remains popular.

According to the [TIOBE index](https://www.tiobe.com/tiobe-index/), which measures the popularity of programming languages each month, C is the second most popular programming language as of August 2023.

This is because C is considered the "mother of programming languages" and is one of the most foundational languages of computer science.

Most modern and popular languages used today either use C under the hood or are inspired by it.

For example, Python’s default implementation and interpreter, CPython, is written in C. And languages such as C++ and C# are extensions of C and provide additional functionality.

Even though C was originally designed with systems programming in mind, it is widely used in many other areas of computing.

C programs are portable and easy to implement, meaning they can be executed across different platforms with minimal changes.

C also allows for efficient and direct memory manipulation and management, making it an ideal language for performance-critical applications.

And C provides higher-level abstractions along with low-level capabilities, which allows programmers to have fine-grained control over hardware resources when they need to.

These characteristics make C an ideal language for creating operating systems, embedded systems, system utilities, Internet of things (IoT) devices, database systems, and various other applications.

C is used pretty much everywhere today.

### How to Set Up a Development Environment for C Programming on Your Local Machine

To start writing C programs on your local machine, you will need the following:

* A C Compiler
    
* An Integrated Development Environment (IDE)
    

C is a compiled programming language, like Go, Java, Swift, and Rust.

Compiled languages are different from interpeted languages, such as PHP, Ruby, Python, and JavaScript.

The difference between compiled and interpeted languages is that a compiled language is directly translated to machine code all at once.

This process is done by a special program called a compiler.

The compiler reads the entire source code, checks it for errors, and then translates the entire program into machine code. This is a language the computer can understand and it's directly associated with the particular instructions of the computer.

This process creates a standalone binary executable file containing sequences of `0`s and `1`s which is a more computer-friendly form of the initial source code. This file contains instructions that the computer can understand and run directly.

An interpeted language, on the other hand, doesn’t get translated into machine code all at once and doesn’t produce a binary executable file.

Instead, an interpreter reads and executes the source code one instruction at a time, line by line. The interpreter reads each line, translates it into machine code, and then immediately runs it.

If you are using a Unix or a Unix-like system such as macOS or Linux, you probably have the popular [GNU Compiler Collection (GCC)](https://gcc.gnu.org/) already installed on your machine.

If you are running either of those operating systems, open the terminal application and type the following command:

```plaintext
gcc --version
```

If you're using macOS and have not installed the command line developer tools, a dialog box will pop-up asking you to install them – so if you see that, go ahead and do so.

If you have already installed the command line tools, you will see an output with the version of the compiler, which will look similar to the following:

```plaintext
Apple clang version 14.0.0 (clang-1400.0.29.202)
```

If you are using Windows, you can check out [Code::Blocks](https://www.codeblocks.org/) or look into installing [Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install). Feel free to pick whatever programming environment works best for you.

An IDE is where you write, edit, save, run, and debug your C programs. You can think of it like a word processor but for writing code.

[Visual Studio Code](https://code.visualstudio.com/) is a great editor for writing code, and offers many IDE-like features.

It is free, open-source, supports many programming languages, and is available for all operating systems.

Once you have downloaded Visual Studio Code, install the [C/C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools).

It’s also a good idea to enable auto-saving by selecting: "File" -&gt; "Auto Save".

If you want to learn more, you can look through the [Visual Studio Code documentation for C/C++](https://code.visualstudio.com/docs/languages/cpp).

With your local machine all set up, you are ready to write your first C program!

### How to Write Your First C Program

To get started, open Visual Studio Code and create a new folder for your C program by navigating to "File" -&gt; "Open" -&gt; "New Folder".

Give this folder a name, for example, `c-practice`, and then select "Create" -&gt; “Open".

You should now have the `c-practice` folder open in Visual Studio Code.

Inside the folder you just created, create a new C file.

Hold down the `Command` key and press `N` on macOS or hold down the `Control` and press `N` for Windows/Linux to create an `Untitled-1` file.

Hold down the `Command` key and press `S` on macOS or hold down the `Control` key and press `S` for Windows/Linux, and save the file as a `main.c` file.

Finally, click "Save".

Make sure that you save the file you created with a `.c` extension, or it won’t be a valid C file.

You should now have the `main.c` file you just created open in Visual Studio Code.

Next, add the following code:

```c
#include <stdio.h>

int main(void) {

  // output 'Hello, world!' to the console

  printf("Hello, world!\n");
}
```

Let’s go over each line and explain what is happening in the program.

#### What Are Header Files in C?

Let’s start with the first line, `#include <stdio.h>`.

The `#include` part of `#include <stdio.h>` is a preprocessor command that tells the C compiler to include a file.

Specifically, it tells the compiler to include the `stdio.h` header file.

Header files are external libraries.

This means that some developers have written some functionality and features that are not included at the core of the C language.

By adding header files to your code, you get additional functionality that you can use in your programs without having to write the code from scratch.

The `stdio.h` header file stands for standard input-output.

It contains function definitions for input and output operations, such as functions for gathering user data and printing data to the console.

Specifically, it provides functions such as `printf()` and `scanf()`.

So, this line is necessary for the function we have later on in our program, `printf()`, to work.

If you don't include the `stdio.h` file at the top of your code, the compiler will not understand what the `printf()` function is.

#### What is the `main()` function in C?

Next, `int main(void) {}` is the main function and starting point of every C program.

It is the first thing that is called when the program is executed.

Every C program must include a `main()` function.

The `int` keyword in `int main(void) {}` indicates the return value of the `main()` function.

In this case, the function will return an integer number.

And the `void` keyword inside the `main()` function indicates that the function receives no arguments.

Anything inside the curly braces, `{}`, is considered the body of the function – here is where you include the code you want to write. Any code written here will always run first.

This line acts as a boilerplate and starting point for all C programs. It lets the computer know where to begin reading the code when it executes your programs.

#### What Are Comments in C?

In C programming, comments are lines of text that get ignored by the compiler.

Writing comments is a way to provide additional information and describe the logic, purpose, and functionality of your code.

Comments provide a way to document your code and make it more readable and understandable for anyone who will read and work with it.

Having comments in your source code is also helpful for your future self. So when you come back to the code in a few months and don't remember how the code works, these comments can help.

Comments are also helpful for debugging and troubleshooting. You can temporarily comment out lines of code to isolate problems.

This will allow you to ignore a section of code and concentrate on the piece of code you are testing and working on without having to delete anything.

There are two types of comments in C:

* Single-line comments
    
* Multi-line comments
    

Single-line comments start with two forward slashes, `//`, and continue until the end of the line.

Here is the syntax for creating a single-line comment in C:

```c
// I am a single-line comment
```

Any text written after the forward slashes and on the same line gets ignored by the compiler.

Multi-line comments start with a forward slash, `/`, followed by an asterisk, `*`, and end with an asterisk, followed by a forward slash.

As the name suggests, they span multiple lines.

They offer a way to write slightly longer explanations or notes within your code and explain in more detail how it works.

Here is the syntax for creating a multi-line comment in C:

```c
/*
This is
a multi-line
comment
*/
```

### What is the `printf()` function in C?

Inside the function's body, the line `printf("Hello, World!\n");` prints the text `Hello, World!` to the console (this text is also known as a string).

Whenever you want to display something, use the `printf()` function.

Surround the text you want to display in double quotation marks, `""`, and make sure it is inside the parentheses of the `printf()` function.

The semicolon, `;`, terminates the statement. All statements need to end with a semicolon in C, as it identifies the end of the statement.

You can think of a semicolon similar to how a full stop/period ends a sentence.

### What Are Escape Sequences in C?

Did you notice the `\n` at the end of `printf("Hello, World!\n");`?

It's called an escape sequence, which means that it is a character that creates a newline and tells the cursor to move to the next line when it sees it.

In programming, an escape sequence is a combination of characters that represents a special character within a string.

They provide a way to include special characters that are difficult to represent directly in a string.

They consist of a backslash, `\`, also known as the escape character, followed by one or more additional characters.

The escape sequence for a newline character is `\n`.

Another escape sequence is `\t`. The `\t` represrents a tab character, and will insert a space within a string.

### How to Compile and Run Your first C Program

In the previous section, you wrote your first C program:

```c
#include <stdio.h>

int main(void) {

  // output 'Hello, world!' to the console

  printf("Hello, world!\n");
}
```

Any code you write in the C programming language is called source code.

Your computer doesn’t understand any of the C statements you have written, so this source code needs to be translated into a different format that the computer can understand. Here is where the compiler you installed earlier comes in handy.

The compiler will read the program and translate it into a format closer to the computer’s native language and make your program suitable for execution.

You will be able to see the output of your program, which should be `Hello, world!`.

The compilation of a C program consists of four steps: preprocessing, compilation, assembling, and linking.

The first step is preprocessing.

The preprocessor scans through the source code to find preprocessor directives, which are any lines that start with a `#` symbol, such as `#include` .

Once the preprocessor finds these lines, it substitutes them with something else.

For example, when the preprocessor finds the line `#include <stdio.h>`, the `#include` tells the preprocessor to include all the code from the `stdio.h` header file.

So, it replaces the `#include <stdio.h>` line with the actual contents of the `stdio.h` file.

The output of this phase is a modified version of the source code.

After preprocessing, the next step is the compilation phase, where the modified source code gets translated into the corresponding assembly code.

If there are any errors, compilation will fail, and you will need to fix the errors to continue.

The next step is the assembly phase, where the assembler converts the generated assembly code statements into machine code instructions.

The output of this phase is an object file, which contains the machine code instructions.

The last step is the linking phase.

Linking is the process of combining the object file generated from the assembly phase with any necessary libraries to create the final executable binary file.

Now, let’s go over the commands you need to enter to compile your `main.c` file.

In Visual Studio Code, open the built-in terminal by selecting "Terminal" -&gt; "New Terminal".

Inside the terminal, enter the following command:

```plaintext
gcc main.c
```

The `gcc` part of the command refers to the C compiler, and `main.c` is the file that contains the C code that you want to compile.

Next, enter the following command:

```plaintext
ls
```

The `ls` command lists the contents of the current directory.

```plaintext
a.out  main.c
```

The output of this command shows an `a.out` file – this is the executable file containing the source code statements in their corresponding binary instructions.

The `a.out` is the default name of the executable file created during the compilation process.

To run this file, enter the following command:

```plaintext
./a.out
```

This command tells the computer to look in the current directory, `./`, for a file named `a.out`.

The above command generates the following output:

```plaintext
Hello, world!
```

You also have the option to name the executable file instead of leaving it with the default `a.out` name.

Say you wanted to name the executable file `helloWorld`.

If you wanted to do this, you would need to enter the following command:

```plaintext
gcc -o helloWorld main.c
```

This command with the `-o` option (which stands for output) tells the `gcc` compiler to create an executable file named `helloWorld`.

To run the new executable file that you just created, enter the following command:

```plaintext
./helloWorld
```

This is the output of the above command:

```plaintext
Hello, world!
```

Note that whenever you make a change to your source code file, you have to repeat the process of compiling and running your program from the beginning to see the changes you made.

## Chapter 2: Variables and Data Types

In this chapter, you will learn the basics of variables and data types – the fundamental storage units that allow you to preserve and manipulate data in your programs.

By the end of this chapter, you will know how to declare and initialize variables.

You will also have learned about various data types available in C, such as integers, floating-point numbers, and characters, which dictate how information is processed and stored within a program's memory.

Finally, you'll have learned how to receive user input in your programs, and how to use constants to store values that you don't want to be changed.

### What Is a Variable in C?

Variables store different kind of data in the computer's memory, and take up a certain amount of space.

By storing information in a variable, you can retrieve and manipule it, perform various calculations, or even use it to make decisions in your program.

The stored data is given a name, and that is how you are able to access it when you need it.

### How to Declare Variables in C

Before you can use a variable, you need to declare it – this step lets the compiler know that it should allocate some memory for it.

C is a strongly typed language, so to declare a variable in C, you first need to specify the type of data the variable will hold, such as an integer to store a whole number, a floating-point number for numbers with decimal places, or a char for a single character.

That way, during compilation time, the compiler knows if the variable is able to perform the actions it was set out to do.

Once you have specified the data type, you give the variable a name.

The general syntax for declaring variables looks something like this:

```plaintext
data_type variable_name;
```

Let's take the following example:

```c
#include <stdio.h>

int main(void) {

    int age;
}
```

In the example above, I declared a variable named `age` that will hold integer values.

#### What Are the Naming Conventions for Variables in C?

When it comes to variable names, they must begin either with a letter or an underscore.

For example, `age` and `_age` are valid variable names.

Also, they can contain any uppercase or lowercase letters, numbers, or an underscore character. There can be no other special symbols besides an underscore.

Lastly, variable names are case-sensitive. For example, `age` is different from `Age`.

### How to Initialize Variables in C

Once you've declared a variable, it is a good practice to intialize it, which involves assigning an initial value to the variable.

The general syntax for initialzing a variable looks like this:

```plaintext
data_type variable_name = value;
```

The assignment operator, `=`, is used to assign the `value` to the `variable_name`.

Let's take the previous example and assign `age` a value:

```c
#include <stdio.h>

int main(void) {

    int age;

    age = 29;
}
```

I initialized the variable `age` by assigning it an integer value of `29`.

With that said, you can combine the initialization and declaration steps instead of performing them separately:

```c
#include <stdio.h>

int main(void) {

    // declaration + initialization
    int age = 29;
}
```

### How to Update Variable Values in C

The values of variables can change.

For example, you can change the value of `age` without having to specify its type again.

Here is how you would change its value from `29` to `30`:

```c
#include <stdio.h>

int main(void) {

    // the variable age with its original value
    int age = 29;

    // changing the value of age
    // the new value will be 30
    age = 30;
}
```

Note that the data type of the new value being assigned must match the declared data type of the variable.

If it doesn't, the program will not run as expected. The compiler will raise an error during compilation time.

```c
#include <stdio.h>

int main(void) {

    int age = 29;
    
    /*
    trying to assign a floating-point value
    to a variable with type int
    will cause an error in your program
    */
    age = 29.5;
}
```

### What Are the Basic Data Types in C?

Data types specify the type of form that information can have in C programs. And they determine what kind of operations can be performed on that information.

There are various built-in data types in C such as `char`, `int`, and `float`.

Each of the data types requires different allocation of memory.

Before exploring each one in more detail, let’s first go over the difference between signed and unsigned data types in C.

Signed data types can represent both positive and negative values.

On the other hand, unsigned data types can represent only non-negative values (zero and positive values).

Wondering when to use signed and when to use unsigned data types?

Use signed data types when you need to represent both positive and negative values, such as when working with numbers that can have positive and negative variations.

And use unsigned data types when you want to ensure that a variable can only hold non-negative values, such as when dealing with quantities.

Now, let's look at C data types in more detail.

#### What Is the `char` Data Type in C?

The most basic data type in C is `char`.

It stands for "character" and it is one of the simplest and most fundamental data types in the C programming language.

You use it to store a single individual character such as an uppercase and lowercase letter of the ASCII (American Standard Code for Information Interchange) chart.

Some examples of `char`s are `'a'` and `'Z'`.

It can also store symbols such as `'!'`, and digits such as `'7'`.

Here is an example of how to create a variable that will hold a `char` value:

```c
#include <stdio.h>

int main(void) {

    char initial = 'D';

 }
```

Notice how I used single quotation marks around the single character.

This is because you can't use double quotes when working with `char`s.

Double quotes are used for strings.

Regarding memory allocation, a signed `char` lets you store numbers ranging from `[-128 to 127`\], and uses at least 1 byte (or 8 bits) of memory.

An unsigned char stores numbers ranging from `[0 to 255]`.

#### What Is the `int` Data Type in C?

An `int` is a an integer, which is also known as a whole number.

It can hold a positive or negative value or `0`, but it can't hold numbers that contain decimal points (like `3.5`).

Some examples of integers are `0`, `-3`,and `9`.

Here is how you create a variable that will hold an `int` value:

```c
#include <stdio.h>

int main(void) {

    int age = 29;
 }
```

When you declare an `int`, the computer allocates at least 2 bytes (or 16 bits) of memory.

With that said, on most modern systems, an `int` typically allocates 4 bytes (or 32 bits) of memory.

The range of available numbers for a signed `int` is `[-32,768 to 32,767]` when it takes up 2 bytes and `[-2,147,483,648 to 2,147,483,647]` when it takes up 4 bytes of memory.

The range of numbers for an unsigned `int` doesn't include any of the negative numbers in the range mentioned for signed `int`s.

So, the range of numbers for unsigned `ints` that take up 2 bytes of memory is `[0 to 65,535]` and the range is `[0 to 4,294,967,295]` for those that take up 4 bytes.

To represent smaller numbers, you can use another data type – the `short int`. It typically takes up 2 bytes (or 16 bits) of memory.

A signed `short int` allows for numbers in a range from `[-32,768 to 32,767]`.

An unsigned `short int` allows for numbers in a range from `[0 to 65,535]`.

Use a `short` when you want to work with smaller integers, or when memory optimisation is critically important.

If you need to work with larger integers, you can also use other data types like `long int` or `long long int`, which provide a larger range and higher precision.

A `long int` typically takes up at least 4 bytes of memory (or 32 bits).

The values for a signed `long int` range from `[-2,147,483,648 to 2,147,483,647]`.

And the values for an unsigned `long int` range from `[0 to 4,294,967,295]`.

The `long long int` data type is able to use even larger numbers than a `long int`. It usually takes up 8 bytes (or 64 bits) of memory.

A signed `long long int` allows for a range from `[-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807]`

And an unsigned `long long int` has a range of numbers from `[0 to 18,446,744,073,709,551,615]`.

#### What Is The `float` Data Type in C?

The `float` data type is used to hold numbers with a decimal value (which are also known as real numbers).

It holds 4 bytes (or 32 bits) of memory and it is a single-precision floating-point type.

Here is how you create a variable that will hold a `float` value:

```c
#include <stdio.h>

int main(void) {

   float temperature = 68.5;
 }
```

A `double` is a floating point value and is the most commonly used floating-point data type in C.

It holds 8 bytes (or 64 bits) of memory, and it is a double-precision floating-point type.

Here is how you create a variable that will hold a `double` value:

```c
#include <stdio.h>

int main(void) {

	double number = 3.14159;
 }
```

When choosing which floating-point data type to use, consider the trade-off between memory usage and precision.

A `float` has less precision that a `double` but consumes less memory.

Use a `float` when memory usage is a concern (such as when working with a system with limited resources) or when you need to perform calculations where high precision is not critical.

If you require higher precision and accuracy for your calculations and memory usage is not critical, you can use a `double`.

### What Are Format Codes in C?

Format codes are used in input and output functions, such as `scanf()` and `printf()`, respectively.

They act as placeholders and substitutes for variables.

Specifically, they specify the expected format of input and output.

They tell the program how to format or interpret the data being passed to or read from the `scanf()` and `printf()` functions.

The syntax for format codes is the `%` character and the format specifier for the data type of the variable.

Let's take the following example:

```c
#include<stdio.h>

int main(void)
{
	int age = 29;

	printf("My age is %i\n", age);  // My age is 29
}
```

In the example above, `age` is the variable in the program. It is of type `int`.

The format code – or placeholder – for integer values is `%i`. This indicates that an integer should be printed.

In the program's output, `%i` is replaced with the value of `age`, which is `29`.

Here is a table with the format specifiers for each data type:

| FORMAT SPECIFIER | DATA TYPE |
| --- | --- |
| %c | char |
| %c | unsigned char |
| %i, &d | int |
| %u | unsigned int |
| %hi, %hd | short int |
| %hu | unsigned short int |
| %li or %ld | long int |
| %lu | unsigned long int |
| %lli or %lld | long long int |
| %llu | unsigned long long int |
| %f | float |
| %lf | double |
| %Lf | long double |

### How to Recieve User Input Using the `scanf()` Function

Earlier you saw how to print something to the console using the `printf()` function.

But what happens when you want to receive user input? This is where the `scanf()` function comes in.

The `scanf()` function reads user input, which is typically entered via a keyboard.

The user enters a value, presses the Enter key, and the value is saved in a variable.

The general syntax for using `scanf()` looks something similar to the following:

```c
scanf("format_string", &variable);
```

Let's break it down:

* `format_string` is the string that lets the computer know what to expect. It specifies the expected format of the input. For example, is it a word, a number, or something else?
    
* `&variable` is the pointer to the variable where you want to store the value gathered from the user input.
    

Let's take a look at an example of `scanf()` in action:

```c
#include <stdio.h>

int main(void) {
  
  int number;

  printf("Please enter your age: ");
  
  scanf("%i", &number);

  printf("Your age is %i\n", number);
}
```

In the example above, I first have to include the `stdio.h` header file, which provides input and output functions in C.

Then, in the `main()` function, I declare a variable named `number` that will hold integer values. This variable will store the user input.

Then, I prompt the user to enter a number using the `printf()` function.

Next, I use `scanf()` to read and save the value that the user enters.

The format specifier `%i` lets the computer known that it should expect an integer input.

Note also the `&` symbol before the variable name. Forgetting to add it will cause an error.

Lastly, after receiving the input, I display the received value to the console using another `printf()` function.

### What are Constants in C?

As you saw earlier on, variable values can be changed throughout the life of a program.

With that said, there may be times when you don’t want a value to be changed. This is where constants come in handy.

In C, a constant is a variable with a value that cannot be changed after declaration and during the program's execution.

You can create a constant in a similar way to how you create variables.

The differences between constants and variables is that with constants you have to use the `const` keyword before mentioning the data type.

And when working with constants, you should always specify a value.

The general syntax for declaring constants in C looks like this:

```plaintext
const data_type constant_name = value;
```

Here, `data_type` represents the data type of the constant, `constant_name` is the name you choose for the constant, and `value` is the value of the constant.

It is also best practice to use all upper case letters when declaring a constant’s name.

Let’s see an example of how to create a constant in C:

```c
#include <stdio.h>

int main(void) {

    const int LUCKY_NUM = 7;

    printf("My lucky number is: %i\n", LUCKY_NUM);
}
```

In this example, `LUCKY_NUM` is defined as a constant with a value of `7`.

The constant's name, `LUCKY_NUM`, is in uppercase letters, as this is a best practice and convention that improves the readability of your code and distinguishes constants from variables.

Once defined, it cannot be modified in the program.

If you try to change its value, the C compiler will generate an error indicating that you are attempting to modify a constant.

```c
#include <stdio.h>

int main(void) {

    const int LUCKY_NUM = 7;

    printf("My lucky number is: %i\n", LUCKY_NUM);

    LUCKY_NUM = 13; // this will cause an error

}
```

## Chapter 3: Operators

Operators are essential building blocks in all programming languages.

They let you perform various operations on variables and values using symbols.

And they let you compare variables and values against each other for decision-making computatons.

In this chapter, you will learn about the most common operators in C programming.

You will first learn about arithmetic operators, which allow you to perform basic mathematical calculations.

You will then learn about relational (also known as comparisson operators), which help you compare values.

And you will learn about logical operators, which allow you to make decisions based on conditions.

After understanding these fundamental operators, you'll learn about some additional operators, such as assignment operators, and increment and decrement operators.

By the end of this chapter, you will have a solid grasp of how to use different operators to manipulate data.

### What Are the Arithmetic Operators in C?

Arithmetic operators are used to perform basic arithmetic operations on numeric data types.

Operations include addition, subtraction, multiplication, division, and calculating the remainder after division.

These are the main arithmetic operators in C:

| Operator | Operation |
| --- | --- |
| + | Addition |
| \- | Subtraction |
| \* | Multiplication |
| / | Division |
| % | Remainder after division (modulo) |

Let's see examples of each one in action.

#### How to Use the Addition (`+`) Operator

The addition operator adds two operands together and returns their sum.

```c
#include <stdio.h>

int main(void) {

    int a = 5;

    int b = 3;

    int sum = a + b;

    printf("Sum: %i\n", sum); // Output: Sum: 8
}
```

#### How to Use the Subtraction (`-`) Operator

The subtraction operator subtracts the second operand from the first operand and returns their difference.

```c
#include <stdio.h>

int main(void) {

    int a = 10; 

    int b = 5;

    int difference = a - b;

    printf("Difference: %i\n", difference); // Output: Difference: 5
}
```

#### How to Use the Multiplication (`*`) Operator

The multiplication operator multiplies two operands and returns their product.

```c
#include <stdio.h>

int main(void) {

    int a = 4;
    
    int b = 3;

    int product = a * b;

    printf("Product: %i\n", product); // Output: Product: 12
}
```

#### How to Use the Division (`/`) Operator

The division operator divides the first operand by the second operand and returns their quotient.

```c
#include <stdio.h>

int main(void) {

    int a = 10;
    
    int b = 2;

    int quotient = a / b;

    printf("Quotient: %i\n", quotient); // Output: Quotient: 5
}
```

#### How to Use the Modulo (`%`) Operator

The modulo operator returns the remainder of the first operand when divided by the second operand.

```c
#include <stdio.h>

int main(void) {

    int a = 10;
    
    int b = 3;

    int remainder = a % b;

    printf("Remainder: %i\n", remainder); // Output: Remainder: 1
}
```

The modulo operator is commonly used to determine whether an integer is even or odd.

If the remainder of the operation is `1`, then the integer is odd. If there is no remainder, then the integer is even.

### What Are The Relational Operators in C?

Relational operators are used to compare values and return a result.

The result is a Boolean value. A Boolean value is either `true` (represented by `1`) or `false` (represented by `0`).

These operators are commonly used in decision-making statements such as `if` statements, and `while` loops.

These are the relational operators in C:

| Operator | Name of Operator |
| --- | --- |
| \== | Equal to |
| != | Not equal to |
| \&gt; | Greater than |
| &lt; | Less than |
| \&gt;= | Greater than or equal to |
| &lt;= | Less than or equal to |

Let’s see an example of each one in action.

#### How to Use the Equal to (`==`) Operator

The equal to operator checks if two values are equal.

It essentially asks the question, "Are these two values equal?"

Note that you use the comparisson operator (two equal signs – `==`) and not the assignment operator (`=`) which is used for assigning a value to a variable.

```c
#include <stdio.h>

int main(void) {

    int a = 5;

    int b = 5;
    
    int result = (a == b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

The result is `1` (true), because `a` and `b` are equal.

#### How to Use the Not equal to (`!=`) Operator

The not equal to operator checks if two values are NOT equal.

```c
#include <stdio.h>

int main(void) {

    int a = 5; 

    int b = 3;

    int result = (a != b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

The result is `1` (true), because `a` and `b` are not equal.

#### How to Use the Greater than (`>`) Operator

This operator compares two values to check if one is greater than the other.

```c
#include <stdio.h>

int main(void) {

    int a = 10;

    int  b = 5;

    int result = (a > b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

The result is `1` (true), because `a` is greater than `b`.

#### How to Use the Less than (`<`) Operator

This operator compares two values to check if one is less than the other.

```c
#include <stdio.h>

int main(void) {

    int a = 10;

    int b = 5;

    int result = (a < b);

    printf("Result: %i\n", result); // Output: Result: 0
}
```

The result is `0` (false), because `a` is not less than `b`.

#### How to Use the Greater than or Equal to (`>=`) Operator

This operator compares two values to check if one is greater than or equal to the other.

```c
#include <stdio.h>

int main(void) {

    int a = 5;
    
    int  b = 5;

    int result = (a >= b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

The result is `1` (true), because `a` is equal to `b`.

#### How to Use the Less than or equal to (`<=`) Operator

This operator compares two values to check if one is less than or equal the other.

```c
#include <stdio.h>

int main(void) {

    int a = 1;

    int b = 5;

    int result = (a <= b);

    printf("Result: %i\n", result); // Output: Result: 1
}
```

The result is `1` (true), because `a` is less than `b`.

### Logical Operators

Logical operators operate on Boolean values and return a Boolean value.

Here are the logical operators used in C:

| Operator | Name of Operator |
| --- | --- |
| `&&` | Logical AND |
| \` |  |
| `!` | Logical NOT |

Let's go into more detail on each one in the following sections.

#### How to Use the AND (`&&`) Operator

The logical AND (`&&`) operator checks whether all operands are `true`.

The result is `true` only when all operands are `true`.

Here is the truth table for the AND (`&&`) operator when you are working with two operands:

| FIRST OPERAND | SECOND OPERAND | RESULT |
| --- | --- | --- |
| true | true | true |
| true | false | false |
| false | true | false |
| false | false | false |

Let's take the following example:

The result of `(10 == 10) && (20 == 20)` is `true` because both operands are `true`.

Let's look at another example:

The result of `(10 == 20) && (20 == 20)` is `false` because one of the operands is `false`.

When the first operand is `false`, the second operand is not evaluated (since there's no point - it's already determined that the first operand is false, so the result can only be `false`).

#### How to Use the OR (`||`) Operator

The logical OR (`||`) operator checks if at least one of the operands is `true`.

The result is `true` only when at least one of the operands is `true`.

Here is the truth table for the OR (`||`) operator when you are working with two operands:

| FIRST OPERAND | SECOND OPERAND | RESULT |
| --- | --- | --- |
| true | true | true |
| true | false | true |
| false | true | true |
| false | false | false |

Let's look at an example:

The result of `(10 == 20) || (20 == 20)` is `true` because one of the operands is `true`.

Let's look at another example:

The result of `(20 == 20) || (10 == 20)` is `true` because one of the operands is `true`

If the first operand is `true`, then the second operator is not evaluated.

### How to Use the NOT (`!`) Operator

The logical NOT (`!`) operator negates the operand.

If the operand is `true`, it returns `false`.

And if it is `false`, it returns `true`.

You may want to use the NOT operator when when you want to flip the value of a condition and return the opposite of what the condition evaluates to.

Here is the truth table for the NOT(`!`) operator:

| OPERAND | RESULT |
| --- | --- |
| true | false |
| false | true |

Let's look at an example:

The result of `!(10 == 10)` is `false`.

The condition `10 == 10` is `true`, but the `!` operator negates it so the result is `false`.

And let's look at another example:

The result of `!(10 == 20)` is `true`.

The condition `10 == 20` is false, but the `!` operator negates it.

### What Is the Assignement Operator in C?

The assignment operator is used to assign a value to a variable.

```c
#include <stdio.h>

int main(void) {

    // declare an integer variable named num
    int num;
		
    // assign the value 10 to num
    num = 10;

    printf("num: %i\n", num); // Output: num: 10

}
```

In the example above, the value `10` is assigned to the variable `num` using the assignment operator.

The assignment operator works by evaluating the expression on the right-hand side and then storing its result in the variable on the left-hand side.

The type of data assigned should match the data type of the variable.

#### How to Use Compound Assignment Operators

Compound assignment operators are shorthand notations.

They allow you to modify a variable by performing an operation on it and then storing the result of the operation back into the same variable in a single step.

This can make your code more concise and easier to read.

Some common compound assignment operators in C include:

* `+=`: Addition and assignment
    
* `=`: Subtraction and assignment
    
* `=`: Multiplication and assignment
    
* `/=`: Division and assignment
    
* `%=`: Modulo and assignment
    

Let’s see an example of how the `+=` operator works:

```c
#include <stdio.h>

int main(void) {

  int num = 10;

  num += 5; 
 
  printf("Num: %i\n", num); // Num: 15
}
```

In the example above, I created a variable named `num` and assigned it an initial value of `10`.

I then wanted to increment the variable by `5`. To do this, I used the `+=` compound operator.

The line `num += 5` increments the value of `num` by 5, and the result (15) is stored back into `num` in one step.

Note that the `num += 5;` line works exactly the same as doing `num = num + 5`, which would mean `num = 10 + 5`, but with fewer lines of code.

### What Are the Increment and Decrement Operators in C?

The increment `++` and decrement `--` operators increment and decrement a variable by one, respectively.

Let’s look at an example of how to use the `++` operator:

```c
#include <stdio.h>

int main(void) {
  
  int num = 10;
  num++;

  printf("Num: %i\n", num); // Num: 11

}
```

The initial value of the variable `num` is `10`.

By using the `++` increment operator, the value of `num` is set to `11`.

This is like perfoming `num = num + 1` but with less code.

The shorthand for decrementing a variable by one is `--`.

If you wanted to decrement `num` by one, you would do the following:

```c
#include <stdio.h>

int main(void) {
  
  int num = 10;
  num--;

  printf("Num: %i\n", num); // Num: 9

}
```

The initial value of the variable `num` is `10`.

By using the `--` increment operator, the value of `num` is now set to `9`.  
This is like perfoming `num = num - 1`.

## Chapter 4: Conditional Statements

The examples you have seen so far all execute line by line, from top to bottom.

They are not flexible and dynamic and do not adapt according to user behavior or specific situations.

In this chapter, you will learn how to make decisions and control the flow of a program.

You get to set the rules on what happens next in your programs by setting conditions using conditional statements.

Conditional statements take a specific action based on the result of a comparisson that takes place.

The program will decide what the next steps should be based on whether the conditions are met or not.

Certain parts of the program may not run depending on the results or depending on certain user input. The user can go down different paths depending on the various forks in the road that come up during a program's life.

First, you will learn about the `if` statement – the foundational building block of decision-making in C.

You will also learn about the `else if` and `else` statements that are added to the `if` statement to provide additional flexibility to the program.

You will then learn about the ternary operator which allows you to condense decision-making logic into a single line of code and improve the readability of your program.

### How to Create an `if` statement in C

The most basic conditional statement in C is the `if` statement.

It makes a decision based on a condition.

If the given condition evaluates to `true` only then is the code inside the `if` block executed.

If the given condition evaluates to `false`, the code inside the `if` block is ignored and skipped.

The general syntax for an `if` statement in C is the following:

```c
if (condition) {
  // run this code if condition is true
}
```

Let's look at an example:

```c
#include <stdio.h>

int main(void) {

    // variable age
   int age;

   // prompt user to enter their age
   printf("Please enter your age: ");

   // store user's answer in the variable
   scanf("%i", &age);

    // check if age is less than 18
    // if it is, then and only then, print a message to the console

   if (age < 18) {
       printf("You need to be over 18 years old to continue\\n");
   }
}
```

In the above code, I created a variable named `age` that holds an integer value.

I then prompted the user to enter their age and stored the answer in the variable `age`.

Then, I created a condition that checks whether the value contained in the variable `age` is less than 18.

If so, I want a message printed to the console letting the user know that to proceed, the user should be at least 18 years of age.

When asked for my age and I enter `16`, I'd get the following output:

```plaintext
#output

Please enter your age: 16
You need to be over 18 years old to continue
```

The condition (`age < 18`) evaluates to `true` so the code in the `if` block executes.

Then, I re-compile and re-run the program.

This time, when asked for my age, say I enter `28`, but I don't get any output:

```plaintext
#output

Please enter your age: 28
```

This is because the condition evaluates to `false` and therefore the body of the `if` block is skipped.

I have also not specified what should happen in the case that the user's age is greater than 18.

To specify what happens in case the user's age is greater than 18, I can use an `if else` statement.

### How to Create an `if else` statement in C

You can add an `else` clause to an `if` statement to provide code that will execute only when the `if` statement evaluates to `false`.

The `if else` statement essentially means that "`if` this condition is true do the following thing, `else` do this thing instead".

If the condition inside the parentheses evaluates to `true`, the code inside the `if` block will execute.

But if that condition evaluates to `false`, the code inside the `else` block will execute.

The `else` keyword is the solution for when the `if` condition is false and the code inside the `if` block doesn't run. It provides an alternative.

The general syntax looks like this:

```c
if (condition) {
  // run this code if condition is true
} else {
  // if the condition above is false, run this code
}
```

Now, let's revisit the example from the previous section, and specify what should happen if the user's age is greater than 18:

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Please enter your age: ");

   scanf("%i", &age);

 
    // if the condition in the parentheses is true the code inside the curly braces will execute
    // otherwise it is skipped
    // and the code in the else block will execute
    
   if (age < 18) {
       printf("You need to be over 18 years old to continue\n");
   } else {
      printf("You are over 18 so you can continue \n");
  }
  
   }
```

If the condition is `true` the code in the `if` block runs:

```plaintext
#output

Please enter your age: 14
You need to be over 18 years old to continue
```

If the condition is `false` the code in the `if` block is skipped and the code in the `else` block runs instead:

```plaintext
#output

Please enter your age: 45
You are over 18 so you can continue
```

### How to Create an `else if` statement in C

But what happens when you want to have more than one condition to choose from?

If you wish to chose between more than one option you can introduce an `else if` statement.

An `else if` statement essentially means that "If this condition is true, do the following. If it isn't, do this instead. However, if none of the above are true and all else fails, finally do this."

The general syntax looks something like the following:

```plaintext
if (condition) {
   // if condition is true run this code
} else if(another_condition) {
   // if the above condition was false and this condition is true,
   // run the code in this block
} else {
   // if the two above conditions are false run this code
}
```

Let's see how an `else if` statement works.

Say you have the following example:

```c
#include <stdio.h>

int main(void) {
   int age;

   printf("Please enter your age: ");

   scanf("%i", &age);

   if (age < 18) {
       printf("You need to be over 18 years old to continue\n");
   }  else if (age < 21) {
       printf("You need to be over 21\n");
   } else {
      printf("You are over 18 and older than 21 so you can continue \n");
  }
  
   }
```

If the first `if` statement is true, the rest of the block will not run:

```plaintext
#output

Please enter your age: 17
You need to be over 18 years old to continue
```

If the first `if` statement is false, then the program moves on to the next condition.

If that is true the code inside the `else if` block executes and the rest of the block doesn't run:

```plaintext
#output

Please enter your age: 20
You are need to be over 21
```

If both of the previous conditions are all false, then the last resort is the `else` block which is the one to execute:

```plaintext
#output

Please enter your age: 22
You are over 18 and older than 21 so you can continue
```

### How to Use the Ternary Operator in C

The ternary operator (also known as the conditional operator) allows you to write an `if else` statement with fewer lines of code.

It can provide a way of writing more readable and concise code and comes in handy when writing simple conditional expressions.

You would want to use it when you are making making simple decisions and want to keep your code concise and on one line.

However, it's best to stick to a regular `if-else` statement when you are dealing with more complex decisions as the ternary operator could make your code hard to read.

The general syntax for the ternary operator looks something similar to the following:

```plaintext
condition ? expression_if_true : expression_if_false;
```

Let's break it down:

* `condition` is the condition you want to evaluate. This condition will evaluate to either `true` of `false`
    
* `?` separates the condition from the two possible expressions
    
* `expression_if_true` is executed if the `condition` evaluates to `true`
    
* `:` separates the `expression_if_true` from the `expression_if_false`
    
* `expression_if_false` is executed if the `condition` evaluates to `false`.
    

Let's take a look at an example:

```c
#include <stdio.h>

int main(void) {
  
    int x = 10;
    
    int y = (x > 5) ? 100 : 200;
    
    printf("x: %i\n", x); // x: 10
    
    printf("y: %i\n", y);  // y: 100
   }
```

In the example above, the condition is `(x > 5)`.

If `x` is greater than 5, the condition evaluates to `true`. And when the condition is `true`, the value assigned to `y` will be `100`.

If the condition evaluates to `false`, the value assigned to `y` will be `200`.

So, since `x` is greater than 5 (`x = 10`), `y` is assigned the value `100`.

## Chapter 5: Loops

In this chapter you will learn about loops, which are essential for automating repetitive tasks without having to write the same code multiple times.

Loops allow you to execute a specific block of code instructions repeatedly over and over again until a certain condition is met.

You will learn about the different types of loops, such as the `for` , `while` and `do-while` loops, and understand their syntax and when you should use each one.

You will also learn about the `break` statement, which allows you to control the execution flow within loops in specific ways.

### How to Create a `for` Loop in C

A `for` loop allows you to execute a block of code repeatedly based on a specified condition.

It's useful when you know how many times you want to repeat a certain action.

The general syntax for a `for` loop looks like this:

```plaintext
for (initialization; condition; increment/decrement) {
    // Code to be executed in each iteration
}
```

Let's break it down:

* `initialization` is the step where you initialize a loop control variable. It's typically used to set the starting point for your loop.
    
* `condition` is the condition that is evaluated before each iteration. If the condition is `true`, the loop continues. If it's `false`, the loop terminates. The loop will run as long as the condition remains true.
    
* `increment/decrement` is the part responsible for changing the loop control variable after each iteration. It can be an increment (`++`), a decrement (`--`), or any other modification.
    
* `Code to be executed in each iteration` is the block of code inside the `for` loop's body that gets executed in each iteration if the condition is `true`.
    

Let's see an example of how a `for` loop works.

Say you want to print the numbers from 1 to 5 to the console:

```c
#include <stdio.h>

int main() {

    for (int i = 1; i <= 5; i++) {
        printf("Iteration %i\n", i);
    }
    
}
```

Output:

```plaintext
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

In the example above, I first initialize the loop control variable `i` with a value of `1`.

The condition `i <= 5` is true, so the loop's body is executed and `"Iteration 1"` is printed.

After each iteration, the value of `i` is incremented by `1`. So, `i` is incremented to `2`.

The condition is still `true`, so `"Iteration 2"` is printed.

The loop will continue as long as `i` is less than or equal to `5`.

When `i` becomes `6`, the condition evaluates to `false` and the loop terminates.

### How to Create a `while` Loop in C

As you saw in the previous section, a `for` loop is used when you know the exact number of iterations you want the loop to perform.

The `while` loop is useful when you want to repeat an action based on a condition but don't know the exact number of iterations beforehand.

Here is the general syntax of a `while` loop:

```plaintext
while (condition) {
    // Code to be executed in each iteration
}
```

With a `while` loop, the condition is evaluated before each iteration. If the condition is `true`, the loop continues. If it's false, the loop terminates.

The `while` loop will continue as long as the condition evaluates to `true`.

Something to note with `while` loops is that the code in the loop's body is not guaranteed to run even at least one time if a condition is not met.

Let's see an example of how a `while` loop works:

```c
#include <stdio.h>

int main() {

    int count = 1;
    
    while (count <= 5) {
    
        printf("Iteration %i\n", count);
        
        count++;
    }
    
}
```

Output:

```plaintext
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

In the example above, I first initialize a variable `count` with a value of `1`.

Before it runs any code, the `while` loop checks a condition.

The condition `count <= 5` is `true` because count is initially `1`. So, the loop's body is executed and `"Iteration 1"` is printed.

Then, `count` is incremented to `2`.

The condition is still `true`, so `"Iteration 2"` is printed.

The loop will continue as long as count is less than or equal to 5.

This process continues until count becomes `6`, at which point the condition becomes `false`, and the loop terminates.

Something to be aware of when working with `while` loops is accidentally creating an infinite loop:

```c
#include <stdio.h> 

int main(void)
{

	while(true)
	{
		printf("Hello world");
	}
}
```

In this case the condition always evaluates to `true`.

After printing the line of code inside the curly braces, it continuously checks wether it should run the code again.

As the answer is always yes (since the condition it needs to check is always true each and every time), it runs the code again and again and again.

The way to stop the program and escape from the endless loop is running `Ctrl C` in the terminal.

### How to Create a `do-while` Loop in C

As mentioned in the previous section, the code in the `while` loop's body is not guaranteed to run even at least one time if the condition is not met.

A `do-while` loop executes a block of code repeatedly for as long as a condition remains `true`.

However, in contrast to a `while` loop, it is guaranteed to run at least once, regardless of whether the condition is `true` or `false` from the beginning.

So, the `do-while` loop is useful when you want to ensure that the loop's body is executed at least once before the condition is checked.

The general syntax for a `do-while` loop looks like this:

```plaintext
do {
    // Code to be executed in each iteration
} while (condition);
```

Let's take a look at an example that demonstrates how a `do-while` loop works:

```c
#include <stdio.h>

int main() {

    int count = 1;
    
    do {
        printf("Iteration %i\n", count);
        
        count++;
        
    } while (count <= 5);

}
```

Output:

```plaintext
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

In the example above I initialize a variable `count` with a value of `1`.

A `do-while` loop first does something and then checks a condition.

So, the block of code inside the loop is executed at least one time.

The string `"Iteration 1"` is printed and then `count` is incremented to `2`.

The condition `count <= 5` is then checked and it evaluates to `true`, so the loop continues.

The loop will continue as long as `count` is less than or equal to 5.

After the iteration where `count` is `6`, the condition becomes `false`, and the loop terminates.

### How to Use the `break` Statement in C

The `break` statement is used to immediately exit a loop and terminate its execution.

It's a control flow statement that allows you to interrupt the normal loop execution and move on to the code after the loop.

The `break` statement is especially useful when you want to exit a loop under specific conditions, even if the loop's termination condition hasn't been met.

You might use it when you encounter a certain value, or when a specific condition is met.

Here's how to use a `break` statement in a loop:

```c
#include <stdio.h>

int main() {
    int target = 5;
    
    for (int i = 1; i <= 10; i++) {
        printf("Current value: %i\n", i);
        
        if (i == target) {
            printf("Target value reached. Exiting loop.\n");
            break; // Exit the loop
        }
    }
    
}
```

Output:

```plaintext
Current value: 1
Current value: 2
Current value: 3
Current value: 4
Current value: 5
Target value reached. Exiting loop.
```

In the example above, a `for` loop is set to iterate from `1` to `10`.

Inside the loop, the current value of `i` is printed on each iteration.

There is also an `if` statement that checks if the current value of `i` matches the target value, which is set to `5`.

If `i` matches the target value, the `if` statement is triggered and a message is printed.

As a result, the `break` statement exits the current loop immediately and prematurely.

The program will continue executing the code that is after the loop.

## Chapter 6: Arrays

Arrays offer a versatile and organized way to store multiple pieces of related data that are arranged in an ordered sequence.

They allow you to store multiple values of the same data type under a single identifier and perform repetitive tasks on each element.

In this chapter, you will learn how to declare and initialize arrays. You will also learn how to access individual elements within an array using index notation and modify them.

In addition, you will learn how to use loops to iterate through array elements and perform operations on each element.

### How to Declare and Initialize an Array in C

To declare an array in C, you first specify the data type of the elements the array will store.

This means you can create arrays of type `int`, `float`, `char`, and so on.

You then specify the array's name, followed by the array's size in square brackets.

The size of the array is the number of elements that it can hold. This number must be a positive integer.

Keep in mind that arrays have a fixed size, and once declared, you cannot change it later on.

Here is the general syntax for declaring an array:

```c
data_type array_name[array_size];
```

Here is how to declare an array of integers:

```c
#include <stdio.h>

int main() {

   int grades[5];
}
```

In the example above, I created an array named `grades` that can store `5` `int` numbers.

After declaring an array, you can initialize it with initial values.

To do this, use the assignment operator, `=`, followed by curly braces, `{}`.

The curly braces will enclose the values, and each value needs to be separated by a comma.

Here is how to initialize the `grades` array:

```c
#include <stdio.h>

int main() {

   int grades[5] = {50, 75, 100, 67, 90};
}
```

Keep in mind that the number of values should match the array size, otherwise you will encounter errors.

Something to note here is that you can also partially initialize the array:

```c
#include <stdio.h>

int main() {

   int grades[5] = {50, 75, 100};
}
```

In this case, the remaining two elements will be set to `0`.

Another way to initialize arrays is to omit the array's length inside the square brackets and only assign the initial values, like so:

```c
#include <stdio.h>

int main() {

   int grades[] = {50, 75, 100, 67, 90};
}
```

In this example, the array's size is `5` because I assigned it `5` values.

#### How to Find the Length of an Array in C Using the `sizeof()` Operator

The `sizeof` operator comes in handy when you need to calculate the size of an array.

Let's see an example of the `sizeof` operator in action:

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};

    // calculate the size of the array
    int array_size = sizeof(grades);

    printf("Size of array: %i bytes\n", array_size);
}
```

Output:

```plaintext
Size of array: 20 bytes
```

In the example above, `sizeof(grades)` calculates the total size of the array in bytes.

In this case, the array has five integers.

As mentioned in a previous chapter, on most modern systems an `int` typically occupies 4 bytes of memory. Therefore, the total size is `5 x 4 = 20` bytes of memory for the entire array.

Here is how you can check how much memory each `int` occupies using the `sizeof` operator:

```c
#include <stdio.h>

int main() {
    
    int grades[] = {50, 75, 100, 67, 90};
    
    // calculate the size of a single array element
    int element_size = sizeof(grades[0]);
    
    printf("Size of a single element: %i bytes\n", element_size);

}
```

Output:

```plaintext
Size of a single element: 4 bytes
```

The `sizeof(grades[0])` calculates the size of a single element in bytes.

By dividing the total size of the array by the size of a single element, you can calculate the number of elements in the array, which is equal to the array's length:

```c
#include <stdio.h>

int main() {
    
    int grades[] = {50, 75, 100, 67, 90};
    
     int array_size = sizeof(grades);
     
     int element_size = sizeof(grades[0]);
    
     // calculate the length of the array
     int length = array_size / element_size;

    printf("Length of the array: %i elements\n", length);

}
```

Output:

```plaintext
Length of the array: 5 elements
```

### How to Access Array Elements in C

You can access each element in an array by specifying its index or its position in the array.

Note that in C, indexing starts at `0` instead of `1`.

So, the index of the first element is `0`, the index of the second element is `1`, and so on.

The last element in an array has an index of `array_size - 1`.

To access individual elements in the array, you specify the array's name followed by the element's index number inside square brackets (`[]`).

```plaintext
array_name[index];
```

Let's take a look at the following example:

```c
#include <stdio.h>

int main() {

   int grades[] = {50, 75, 100, 67, 90};

   // Access each array element using index notation
    
   printf("Element at index 0: %i\n", grades[0]);  
    
   printf("Element at index 1: %i\n", grades[1]);  

   printf("Element at index 2: %i\n", grades[2]); 

   printf("Element at index 3: %i\n", grades[3]); 
    
   printf("Element at index 4: %i\n", grades[4]); 
}
```

Output:

```plaintext
Element at index 0: 50
Element at index 1: 75
Element at index 2: 100
Element at index 3: 67
Element at index 4: 90
```

In the example above, to access each item from the integer array `grades`, I have to specify the array's name along with the item's position in the array inside square brackets.

Remember that the index starts from `0`, so `grades[0]` gives you the first element, `grades[1]` gives you the second element, and so on.

Note that if you try to access an element with an index number that is higher than `array_size - 1`, the compiler will return a random number:

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};

    
    printf("Element at index 5: %d\n", grades[5]);  

}
```

Output:

```plaintext
Element at index 5: 220312136
```

### How to Modify Array Elements in C

Once you know how to access array elements, you can then modify them.

The general syntax for modifying an array element looks like this:

```plaintext
array_name[index] = new_value;
```

You can change the value of an element by assigning a new value to it using its index.

Let's take the `grades` array from earlier on:

```c
#include <stdio.h>

int main() {

   int grades[] = {50, 75, 100, 67, 90};
}
```

Here is how you would change the value `75` to `85`:

```c
#include <stdio.h>

int main() {

   int grades[] = {50, 75, 100, 67, 90};
   
   grades[1] = 85; // changing the value at index 1 to 85
   
   printf("Element at index 1: %i\n", grades[1]); 
}
```

Output:

```plaintext
Element at index 1: 85
```

When modifying arrays, keep in mind that the new value must match the declared data type of the array.

### How to Loop Through an Array in C

By looping through an array, you can access and perform operations on each element sequentially.

The `for` loop is commonly used to iterate through arrays.

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};
    
    for (int i = 0; i < 5; i++) {
        printf("Element at index %i: %i\n", i, grades[i]);
    }
}
```

Output:

```plaintext
Element at index 0: 50
Element at index 1: 75
Element at index 2: 100
Element at index 3: 67
Element at index 4: 90
```

When using a `for` loop to loop through an array, you have to specify the index as the loop variable, and then use the index to access each array element.

The `%i` placeholders are replaced with the current index `i` and the value at that index in the grades array, respectively.

You can also use a `while` loop to iterate through an array:

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};
    
    int i = 0;
    
    while (i < 5) {
    
        printf("Element at index %i: %i\n", i, grades[i]);
        i++;
    }
}
```

Output:

```plaintext
Element at index 0: 50
Element at index 1: 75
Element at index 2: 100
Element at index 3: 67
Element at index 4: 90
```

When using a `while` loop to loop through an array, you will need an index variable, `int i = 0`, to keep track of the current position in the array.

The loop checks the condition `(i < 5)` and prints the index of the grade as well as the actual grade value.

After each grade is shown, the variable `i` is increased by one, and the loop continues until it has shown all the grades in the list.

A `do-while` works in a similar way to the `while` loop, but it is useful when you want to ensure that the loop body is executed at least once before checking the condition:

```c
#include <stdio.h>

int main() {

     int grades[] = {50, 75, 100, 67, 90};

    int i = 0;
    
    do {
        printf("Element at index %i: %i\n", i, grades[i]);
        
        i++;
    } while (i < 5);
}
```

You can also use the `sizeof` operator to loop through an array.

This method is particularly useful to ensure your loop doesn't exceed the array's length:

```c
#include <stdio.h>

int main() {

    int grades[] = {50, 75, 100, 67, 90};
    
    int length = sizeof(grades) / sizeof(grades[0]);

    for (int i = 0; i < length; i++) {
        printf("Element at index %i: %i\n", i, grades[i]);
    }

}
```

The line `int length = sizeof(grades) / sizeof(grades[0]);` calculates the length of the `grades` array.

The length is calculated by dividing the total size (in bytes) of the array by the size of a single element `grades[0]`. The result is stored in the `length` variable.

The loop then iterates through the array using this `length` value.

For each iteration, it prints the index `i` and the value of the grade at that index `grades[i]`.

## Chapter 7: Strings

In the previous chapter, you learned the basics of arrays in C.

Now, it's time to learn about strings – a special kind of array.

Strings are everywhere in programming. They are used to represent names, messages, passwords, and more.

In this chapter, you will learn about strings in C and how they are stored as arrays of characters.

You'll also learn the fundamentals of string manipulation.

Specifically, you will learn how to find a string's length and how to copy, concatenate, and compare strings in C.

### What Are Strings in C?

A string is a sequence of characters, like letters, numbers, or symbols, that are used to represent text.

In C, strings are actually arrays of characters. And each character in the string has a specific position within the array.

Another unique characteristic of strings in C is that at the end of every one, there is a hidden `\0` character called the 'null terminator'.

This terminator lets the computer know where the string ends.

So, the string '`Hello`' in C is stored as '`Hello\0`' in memory.

### How to Create Strings in C

One way to create a string in C is to initialize an array of characters.

The array will contain the characters that make up the string.

Here is how you would initialize an array to create the string 'Hello':

```c
#include <stdio.h>

int main() {
  char word[6] = {'H', 'e', 'l', 'l', 'o', '\0'};

}
```

Note how I specified that the array should store `6` characters despite `Hello` being only `5` characters long. This is due to the null operator.

Make sure to include the null terminator, `\0`, as the last character to signify the end of the string.

Let's look at how you would create the string 'Hello world':

```c
#include <stdio.h>

int main() {
  char phrase[12] = {'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '\0'};
}
```

In this example, there is a space between the word 'Hello' and the word 'world'.

So, the array must include a blank space character.

To print the string, you use the `printf()` function, the `%s` format code and the name of the array:

```c
#include <stdio.h>

int main() {
  char phrase[] = {'H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '\0'};

  printf("%s\n", phrase);

}
```

Another way to create a string in C is to use a string literal.

In this case, you create an array of characters and then assign the string by enclosing it in double quotes:

```c
#include <stdio.h>

int main() {
  char word[] = "Hello";

}
```

With string literals, the null terminator (`\0`) is implied.

Creating strings with string literals is easier, as you don't need to add the null terminator at the end. This method is also much more readable and requires less code.

However, you may want to use character arrays when you want to modify the string's content. String literals are read-only, meaning the content is fixed.

### How to Manipulate Strings in C

C provides functions that allow you to perform operations on strings, such as copying, concatenating, and comparing, to name a few.

To use these functions, you first need to include the `string.h` header file by adding the line `#include <string.h>` at the top of your file.

#### How to Find the Length of a String in C

To calculate the length of a string, use the `strlen()` function:

```c
#include <stdio.h>
#include <string.h>

int main() {
  char phrase[] = "Hello";

  int length = strlen(phrase);

  printf("String length: %i\n", length);

}
```

Output:

```plaintext
String length: 5
```

The `strlen()` function will return the number of characters that make up the string.

Note that the result does not include the null terminator, `\0`.

#### How to Copy a String in C

To copy one string into another one, you can use the `strcpy()` function.

You may want to copy a string in C when you need to make changes to it without modifying it. It comes in handy when you need to keep the original string's content intact.

The general syntax for the `strcpy()` function looks like this:

```plaintext
strcpy(destination_string, original_string);
```

The `strcpy()` function copies `original_string` into `destination_string`, including the null terminator (`'\0'`).

One thing to note here is that you need to make sure the destination array has enough space for the original string:

```c
#include <stdio.h>
#include <string.h>

int main() {
  
    char original[] = "Hello";
  
    char destination[20]; // Make sure this array is big enough

    strcpy(destination, original);

    printf("Copied string: %s\n", destination);
}
```

Output:

```plaintext
Copied string: Hello
```

The `strcpy()` function copies the original string into an empty array and returns the copied string, which also includes the null terminator character (`'\0'`).

#### How to Concatenate Strings in C

You can concatenate (add) two strings together by using the `strcat()` function.

The general syntax for the `strcat()` function looks something like the following:

```plaintext
strcat(destination_string, original_string);
```

The `strcat()` function takes the `original` string and adds it to the end of `destination` string.

Make sure that the `destination_string` has enough memory for the `original_string`.

Something to note here is that `strcat()` does not create a new string.

Instead, it modifies the original `destination_string`, by including the `original_string` at the end.

Let's see an example of how `strcat()` works:

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    
  char greeting[50] = "Hello, ";
  
  char name[] = "Dionysia";

  strcat(greeting, name);

  printf("Message: %s\n", greeting);
  
}
```

Output:

```plaintext
Message: Hello, Dionysia
```

#### How to Compare Strings in C

To compare two strings for equality, you can use the `strcmp()` function.

The general syntax for the `strcmp()` function looks like this:

```plaintext
strcmp(string1, string2);
```

The `strcmp()` function compares `string1` with `string2` and returns an integer.

If the return value of `strcmp()` is `0`, then it means the two strings are the same:

```c
#include <stdio.h>
#include <string.h>

int main() {

  char word1[] = "apples";
  char word2[] = "apples";

  int result = strcmp(word1, word2);

  printf("Result: %i\n", result); // Result: 0

}
```

If the return value of `strcmp()` is less than `0`, then it means the first word comes before the second:

```c
#include <stdio.h>
#include <string.h>

int main() {

  char word1[] = "apples";
  char word2[] = "bananas";

  int result = strcmp(word1, word2);

  printf("Result: %i\n", result); // Result: -1

}
```

And if the return value of `strcmp()` is greater than `0`, then it means the first word comes after the second one:

```c
#include <stdio.h>
#include <string.h>

int main() {

  char word1[] = "bananas";
  char word2[] = "apples";

  int result = strcmp(word1, word2);

  printf("Result: %i\n", result); // Result: 1

}
```

## Further learning: Advanced C Topics

While this handbook has covered a wide range of topics, there is still so much to learn, as programming is so vast.

Once you have built a solid foundation with the basics of C programming, you may want to explore more advanced concepts.

You may want to move on to learning about functions, for example. They allow you to write instructions for a specific task and reuse that code throughout your program.

You may also want to learn about pointers. Pointers in C are like arrows that show you where a specific piece of information is stored in the computer's memory.

Then, you may want to move on to learning about structures. They're like custom data containers that allow you to group different types of information under one name.

Lastly, you may want to learn how to work with files. Working with files in C allows you to read from and write to files. This is useful for tasks like saving user data, reading configuration settings, or sharing data between different programs.

These suggestions are not a definitive guide – just a few ideas for you to continue your C programming learning journey.

If you are interested in learning more, you can check out the following freeCodeCamp resources:

* [C Programming Tutorial for Beginners](https://www.youtube.com/watch?v=KJgsSFOSQv0&t=12372s)
    
* [Learn C Programming Using the Classic Book by Kernighan and Ritchie](https://www.freecodecamp.org/news/learn-c-programming-classic-book-dr-chuck/)
    
* [Unlock the Mysteries of Pointers in C](https://www.freecodecamp.org/news/finally-understand-pointers-in-c/)
    

## Conclusion

This marks the end of this introduction to the C programming language.

Thank you so much for sticking with it and making it until the end.

You learned how to work with variables, various data types, and operators.

You also learned how to write conditional statements and loops. And you learned the basics of working with arrays and strings.

Hopefully, you have gained a good understanding of some of the fundamentals of C programming, got some inspiration on what to learn next, and are excited to continue your programming journey.

Happy coding!
