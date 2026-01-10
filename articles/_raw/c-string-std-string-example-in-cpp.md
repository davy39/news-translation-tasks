---
title: C++ String – std::string Example in C++
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2022-01-31T23:37:41.000Z'
originalURL: https://freecodecamp.org/news/c-string-std-string-example-in-cpp
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/c---string.jpeg
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: 'Strings are essential components in any programming language, and C++ is
  no exception.

  Whether you want to store text, manipulate it, or accept keyboard inputs and outputs,
  understanding what strings are and how to effectively use them is extremely i...'
---

Strings are essential components in any programming language, and C++ is no exception.

Whether you want to store text, manipulate it, or accept keyboard inputs and outputs, understanding what strings are and how to effectively use them is extremely important.

This article will teach everything you need to know about handling and working with strings in C++.

## What is a String?

Strings, at their core, are essentially collections of characters. Some examples include "Hello World", "My name is Bob", and so on. They're enclosed in double quotes `"`.

In C++, we have two types of strings:

1. C-style strings
    
2. `std::string`s (from the C++ Standard string class)
    

You can very easily create your own string class with their own little functions, but it's not something we're going to get into in this article.

# C-style Strings

These are strings derived from the C programming language and they continue to be supported in C++. These "collections of characters" are stored in the form of arrays of type `char` that are *null-terminated* (the `\0` null character).

#### How to define a C-style string:

```c
char str[] = "c string";
```

Here, `str` is a `char` array of length `9` (the extra character comes from the `\0` null character that's added by the compiler).

Here are some other ways of defining C-style strings in C++:

```c
char str[9] = "c string";
char str[] = {'c', ' ', 's', 't', 'r', 'i', 'n', 'g', '\0'};
char str[9] = {'c', ' ', 's', 't', 'r', 'i', 'n', 'g', '\0'};
```

#### How to pass C-style strings to a function

```c++
#include <iostream>

int main() {
    char str[] = "This is a C-style string";
    display(str);
}

// C-style strings can be passed to functions as follows:
void display(char str[]) {
    std::cout << str << "\n";
}
```

### How to use C-style string functions in C++

The C Standard Library came with a couple of handy functions that you can use to manipulate strings. While they're not widely recommended to use (see below), you can still use them in C++ code by including the `<cstring>` header:

```json
#include <cstring> // required


1. strcpy(s1,s2) --> Copies string s2 into string s1.                 
2. strcat(s1,s2) --> Concatenates string s2 onto the end of string s1
3. strlen(s1)    --> Returns the length of string s1         
4. strcmp(s1,s2) --> Returns 0 if s1==s2; less than 0 if s1<s2; greater than 0 if s1>s2
5. strchr(s1,ch) --> Returns a pointer to the first occurrence of character ch in string s1
6. strstr(s1,s2) --> Returns a pointer to the first string s2 in string s1
```

# std::string

C-style strings are relatively *unsafe* – if the string/char array is not null-terminated, it can lead to a whole host of potential bugs.

For example, [buffer overflows](https://en.wikipedia.org/wiki/Buffer_overflow) among a [whole host of other drawbacks](https://stackoverflow.com/questions/312570/what-are-some-of-the-drawbacks-to-using-c-style-strings) are some reasons why the use of C-style strings are not recommended in the C++ developer community.

The `std::string` class that's provided by the C++ Standard Library is a much safer alternative. Here's how you use it:

#### How to define a `std::string`

```c++
#include <iostream> 
#include <string> // the C++ Standard String Class

int main() {
    std::string str = "C++ String";
    std::cout << str << "\n"; // prints `C++ String`"
}
```

The most obvious difference to note between C-style strings and `std::string`s is the *length* of the string. If you ever need the length of a C-style string, you'll need to compute it each time using the `strlen()` function like so:

```c++
#include <iostream>
#include <cstring> // required to use `strlen`

int main() {
    char str[] = "hello world";
    std::cout << strlen(str) << "\n";
}
```

If you don't store this in a variable and require it in multiple parts of your program, you can quickly observe how expensive this option is.

On the other hand, a `std::string` string already has an in-built length property. To access it, you use the `.length()` property as follows:

```c++
#include <iostream>
#include <string> // required to use `std::string`

int main() {
    std::string str = "freeCodeCamp";
    std::cout << str.length() << "\n";
}
```

Simple, neat, concise, but an important computational reduction.

But accessing the *length* property isn't the only benefit to using `std::string`s. Here are a few more examples:

```c++
#include <iostream>
#include <string>

int main() {
   std::string str = "freeCodeCamp";
   
   // Inserting a single character into `str`
   str.push_back('s');
   std::cout << str << "\n"; // `str` is now `freeCodeCamps`
   
   // Deleting the last character from `str`
   str.pop_back();
   std::cout << str << "\n"; // `str` is now `freeCodeCamp`
   
   // Resizing a string
   str.resize(13);
   std::cout << str << "\n"; 
   
   // Decreasing excess capacity of the string
   str.shrink_to_fit()
   std::cout << str << "\n";
}
```

#### How to pass an `std::string` to a function

```c++
#include <iostream>

int main() {
    std::string str = "This is a C-style string";
    display(str);
}

// Passing `std::string`s are as you would normally pass a regular object
void display(std::string str) {
    std::cout << str << "\n";
}
```

## When would you use a C-style string over `std::string`?

By now, you should be convinced of the numerous advantages that `std::string`s have over C-style strings (most notably automatic memory management). But there are times when you'd want to use C-style strings instead:

1. If you're from a C background, you might be comfortable working with C-style strings.
    
2. A `std::string`, despite its benefits, is enormously complex. Like the rest of the language, if you don't know what you're doing, it can get real complicated very quickly. Plus, it uses a ton of memory that may not be ideal for the purposes of your programs.
    
3. If you're careful to manage your program's memory during runtime (by freeing an object's memory when you're done using it), there is a performance benefit to using C-style strings considering how small and lightweight they are.
    

# Wrapping Up

I hope this article served as an introduction to strings in C++. There's *so much more* to learn about this wonderful abstraction, and I hope to write more articles delving into the more advanced concepts of strings and C++.

Happy learning!
