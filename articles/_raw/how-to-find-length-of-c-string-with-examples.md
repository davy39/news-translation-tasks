---
title: Length of C String – How to Find the Size of a String in C
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2024-04-16T15:00:09.504Z'
originalURL: https://freecodecamp.org/news/how-to-find-length-of-c-string-with-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/JfhNqZtV56s/upload/0d58732b5a311298756b16ad3540b820.jpeg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: 'When working with strings in C, you need to know how to find their length.

  Finding the length of a string in C is essential for many reasons.

  You may need to perform string manipulation, and many string manipulation functions
  require the length of th...'
---

When working with strings in C, you need to know how to find their length.

Finding the length of a string in C is essential for many reasons.

You may need to perform string manipulation, and many string manipulation functions require the length of the string as an argument. You may also need to validate user input, compare two strings, or manage and allocate memory dynamically.

In this this article, you will learn different ways to find the length of a string in C.

## What are Strings in C?

Unlike other programming languages, C doesn’t have a built-in string data type.

Instead, strings in C are arrays of characters that have a character called the null terminator `\0` at the end.

There are many ways to create a string in C. Here is an example of one way:

```c
char greeting[] = "Hello";
```

In the code above, I created a character array named `greeting` using the `char` data type followed by square brackets, `[]`.

I then assigned the the string `Hello` which is surrounded by double quotes to `greeting`.

In this example, the size of the array is not specified explicitly – the size is determined by the size of the string assigned to it. Also, the null terminator, `\0,` is automatically added to the end of the string.

### What is the `string.h` header file in C?

The `string.h` header file provides functions for manipulating and working with strings.

It contains functions that complete tasks such as copying and concatenating. It also provides functions for finding the length of a string, such as `strlen()` which you will learn how to use in the following section.

To use functions from `string.h`, you need to include it at the beginning of your file like this:

```c
#include <stdio.h>
#include <string.h>

int main(void) {
  // Your code goes here
}
```

## How to Find the Length of a String in C Using the `strlen()` Function

The `strlen()` function is defined in the `string.h` header file, and is used to find the length of a string.

Let’s take the following example:

```c
#include <stdio.h>
#include <string.h>

int main(void) {
  char greeting[] = "Hello";

  int length = strlen(greeting);

  printf("The length is: %d\n", length);
}

// Output: 
// The length is: 5
```

In the example above, I first included the `stdio.h` header file to be able to use input/output functions such as `printf()`. I also included the `string.h` header file so I could use the `strlen()` function.

Inside the `main()` function, I created a `greeting` array and stored the string `Hello`.

Then, I called the `strlen()` function and passed `greeting` as the argument – this is the string I want to find the length of.

Lastly, I used the value returned in `length` and printed it using the `printf()` function.

Note that the `strlen()` function returns the number of characters in the string excluding the null terminator (`\0`).

## How to Find the Length of a String in C Using the `sizeof()` Operator

Another way to find the length of a string in C is using the `sizeof()` operator.

The `sizeof()` operator returns the total size in bytes of a string.

Let's take the following example:

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello";

  int size = sizeof(greeting);

  printf("The size is %d bytes \n", size);
}

// Output:
// The size is 6 bytes
```

In the following example, `sizeof(greeting)` returns the entire size of the `greeting` array in bytes – including the null operator, `\0`.

This is not always very helpful.

To exclude this character, you need to subtract one from the total `size`:

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello";

  int length = sizeof(greeting) - 1;

  printf("The length is %d\n", length);
}

// Output:
// The length is 5
```

Although the `sizeof()` operator doesn’t require you to include the `string.h` header file like `strlen()` does, it returns the total size of the array and not the length of the string.

The total size of the array includes the null terminator, `\0`, whereas the length of the string is the number of characters before the null terminator.

## How to Find the Length of a String in C Using a `while` Loop

Another way to find the length of a string is C is using a `while` loop.

The way this works is you keep iterating over the characters in a string until you reach the end of it and encounter the null terminator `\0`.

Let's look at the following example:

```c
#include <stdio.h>

int main(void) {
  char greeting[] = "Hello";
  int length = 0;

while (greeting[length] != '\0') {
    length++;
}
    printf("The length is %d", length );
}

// Output:
// The length is 5
```

Let’s break down how the loop works.

I initialized a counter variable, `length`, to `0`. This variable will store the length of the string.

The condition of the `while` loop, `greeting[length] != '\0'`, checks if the character at index `length` of the string is not equal to the null terminator `\0`.

If it is not, the `length` variable is incremented and the loop continues and moves on to the next character in `greeting`.

The `while` loop iterates over `greeting` until it encounters `\0` and then the iteration stops.

## Conclusion

In this article, you learned how to find the length of a string in C.

You learned how to use the `strlen()` function, which returns the number of characters in the string excluding the null terminator.

You also learned how to use the `sizeof()` operator which does not always return the desired result as it includes the null terminator in the length.

Lastly, you learned how to use a `while` loop to find the length of a string. A loop counts the characters in the string until it reaches the null terminator.

Thank you for reading, and happy coding!
