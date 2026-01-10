---
title: C Print String – How to Print a String in C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2024-04-17T13:50:03.705Z'
originalURL: https://freecodecamp.org/news/how-to-print-a-string-in-c
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/Hcfwew744z4/upload/73cd11d4c62fcaa9d6fa85514d7cb732.jpeg
tags:
- name: c programming
  slug: c-programming
- name: C
  slug: c
- name: string
  slug: string
seo_title: null
seo_desc: 'Printing strings is a fundamental operation in programming. It helps you
  output information, inspect and debug your code, and display prompts to users.

  In this article, you will learn some of the different techniques to print strings
  in C.

  What is a ...'
---

Printing strings is a fundamental operation in programming. It helps you output information, inspect and debug your code, and display prompts to users.

In this article, you will learn some of the different techniques to print strings in C.

## What is a String in C?

A string is a sequence of characters, like letters, numbers, or symbols, that are grouped together. It is used to represent text in programs.

Strings are not a built-in data type in C. Instead, they are represented as arrays of characters, terminated with a special character called the null terminator, `\0`.

Here is an example of how to create a string in C:

```c
char greeting[] = "Hello world!";
```

In the code above, I declared a character array named `greeting`, and initialized it with the string `Hello world!` enclosed within double quotes, `" "`.

The C compiler automatically includes the null terminator, `\0`, at the end of `Hello world!`.

## How to Print a String in C Using the `printf()` Function

The `printf()` function is one of the most commonly used ways of printing strings in C.

It stands for "print formatted", and belongs to the standard input/output library, `stdio.h`. So, in order to use it, you need to first include the `stdio.h` header file at the beginning of your program.

Let’s take the following example:

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello world!";
  
  printf("%s\n", greeting);
}

// Output:
// Hello world!
```

In the example above, I first included the `stdio.h` header file at the beginning of my program, which contains the declaration of the `printf()` function.

Next, I declared a character array named `greeting` and initialized it with the text `Hello world!` wrapped in double quotes.

Lastly, I used the `printf()` function to print the text `Hello world!`.

When printing a string using the `printf()` function, you need to use a format specifier.

A format specifier acts as a placeholder that tells the `printf()` function how to format and print specific types of data. They begin with a percent sign `%`, followed by a character that specifies the type of data to be formatted. The format specifier for strings is `%s`.

So, in the line `printf("%s\n", greeting);`, the `%s` format specifier tells `printf()` to print the string stored in the `greeting` variable followed by a newline character, `\n`.

Note that the `%s` format specifier doesn’t include the null terminator, `\0,` when printing strings. It prints the characters in the string until it encounters it.

## How to Print a String in C Using the `puts()` Function

Another function used for printing strings is `puts()`.

Let’s take the following example:

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello world!";
  
  puts(greeting);
}

// Output
// Hello world!
```

In the example above, I first included the `stdio.h` header file which contains the `puts()` declaration.

Then, I declared a character array and initialized it with the text `Hello world!`. The string automatically ends with the null terminator, `\0`.

Lastly, I used the `puts()` function to print the string to the console and passed the string variable `greeting` as an argument.

The `puts()` function automatically adds a newline character, `\n`, at the end of the string.

Note that the `puts()` function is used to print null-terminated strings. A null-terminated string is a sequence of characters stored in memory followed by a character called the null terminator `\0`.

So far, all the examples have used only null-terminated strings, such as `char greeting[] = "Hello world!";`. In memory, it would be represented as `['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '!', '\0']`.

Creating non-null-terminated strings intentionally is not common in C.

Here is an example of a non-null-terminated string: `char greeting[] = {'H', 'e', 'l', 'l', 'o'};`This array of characters does not include the null terminator, `\0`, so it is a non-null-terminated string.

If you try to print a non-null-terminated string using `puts()`, you will end up getting undefined behavior, such as garbage characters at the end of the string:

```c
#include <stdio.h>

int main(void) {
  char greeting[] = {'H', 'e', 'l', 'l', 'o'};

  puts(greeting);
}

// Ouput when I run the code the first time:
// Helloq

// Ouput when I run the code a second time:
// Hellop

// Ouput when I run the code a thrid time:
// Hellow
```

## The `printf()` Function VS the `puts()` Function – What's the Difference?

You may be wondering what the difference is between `printf()` and `puts()`.

The `puts()` function prints the text as it is, without any formatting. It also automatically adds a newline character at the end of the string.

The `printf()` function doesn’t automatically add a new line - you have to do it explicitly.

However, it allows for formatted output, and gives you more control and flexibility over where and how you insert different data types into the format string:

```c
#include <stdio.h>

int main(void) {
    char name[] = "John";
    int age = 30;

    // Printing strings using puts()
    puts("Using puts():");
    puts("My name is John and I'm 30 years old.");

    // Printing strings usingprintf()
    printf("\nUsing printf():\n");
    printf("My name is %s and I'm %d years old. \n", name, age);
}
```

In the example above, the `puts()` function prints a simple string without any formatting. It also automatically adds a newline character, `\n`, at the end of the string.

On the other hand, the `printf()` function formats the string and embeds two variable values. It uses format specifiers, such as `%s` for strings and `%d` for integers, to specify the type of data the variables hold, and where the variables should be inserted into the string. It also adds a newline character at the end.

## Conclusion

In this article, you learned about the two most commonly used functions in C for printing strings.

The `printf()` function is commonly used for printing formatted text to the console. It allows you to format your output and print strings, numbers and characters.

The `puts()` function is more simple compared to `printf()`. It is great for basic text output and automatically adds a newline character, `\n`, to the printed string.

Thank you for reading, and happy coding!
