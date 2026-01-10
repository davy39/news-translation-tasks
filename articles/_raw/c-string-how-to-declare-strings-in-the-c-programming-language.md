---
title: C String – How to Declare Strings in the C Programming Language
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-10-06T17:51:39.000Z'
originalURL: https://freecodecamp.org/news/c-string-how-to-declare-strings-in-the-c-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/carlos-alberto-gomez-iniguez-fzZEURcKr4Q-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: "Computers store and process all kinds of data.\nStrings are just one of\
  \ the many forms in which information is presented and gets processed by computers.\
  \ \nStrings in the C programming language work differently than in other modern\
  \ programming language..."
---

Computers store and process all kinds of data.

Strings are just one of the many forms in which information is presented and gets processed by computers. 

Strings in the C programming language work differently than in other modern programming languages.

In this article, you'll learn how to declare strings in C. 

Before doing so, you'll go through a basic overview of what data types, variables, and arrays are in C. This way, you'll understand how these are all connected to one another when it comes to working with strings in C. 

Knowing the basics of those concepts will then help you better understand how to declare and work with strings in C.

Let's get started!

## Data types in C

C has a few built-in data types.

They are `int`, `short`, `long`, `float`, `double`, `long double` and `char`.

As you see, there is no built-in string or str (short for string) data type.

### The `char` data type in C

From those types you just saw, the only way to use and present characters in C is by using the `char` data type. 

Using `char`, you are able to to represent a *single* character – out of the 256 that your computer recognises. It is most commonly used to represent the characters from the ASCII chart.

The single characters are surrounded by *single quotation marks*. 

The examples below are all `char`s – even a number surrounded by single quoation marks and a single space is a `char` in C:

```c
'D', '!', '5', 'l', ' ' 
```

Every single letter, symbol, number and space surrounded by single quotation marks is a single piece of character data in C.

What if you want to present more than one single character? 

The following is **not** a valid `char` – despite being surrounded by single quotation marks. This is because it doesn't include only a single character inside the single quotation marks:

`'freeCodeCamp is awesome'`

When many single characters are strung together in a group, like the sentence you see above, a *string* is created. In that case, when you are using strings, instead of single quotation marks you should only use *double* quotation marks.

`"freeCodeCamp is awesome"`

## How to declare variables in C

So far you've seen how text is presented in C.

What happens, though, if you want to store text somewhere? After all, computers are really good at saving information to memory for later retrieval and use.

The way you store data in C, and in most programming languages, is in variables.

Essentially, you can think of variables as boxes that hold a value which can change throughout the life of a program. Variables allocate space in the computer's memory and let C know that you want some space reserved.

C is a **statically typed** language, meaning that when you create a variable you have to specify what data type that variable will be.

There are many different variable types in C, since there are many different kinds of data.  

Every variable has an associated data type. 

When you create a variable, you first mention the type of the variable (wether it will hold integer, float, char or any other data values), its name, and then optionally, assign it a value:

```c
#include <stdio.h>
int main(void){

char letter = 'D';

//creates a variable named letter 
//it holds only values of type char
// the single character 'D' is assigned to letter
}
```

Be careful not to mix data types when working with variables in C, as that will cause errors.

For intance, if you try to change the example from above to use double quotation marks (remember that chars *only* use single quotation marks), you'll get an error when you compile the code:

```c
#include <stdio.h>
int main(void){

char letter = "D";

//output:

test.c:4:6: warning: incompatible pointer to integer conversion initializing 'char' with an expression of type
      'char [2]' [-Wint-conversion]
char letter = "D";
     ^        ~~~
1 warning generated.


}
```

As mentioned earlier on, C doesn't have a built-in string data type. That also means that C doesn't have string variables!


### How to create arrays in C

An array is essentially a variable that stores multiple values. It's a collection of many items of the same type.

As with regular variables, there are many different types of arrays because arrays can hold only items of the same data type. There are arrays that hold only `int`s, only `float`s, and so on.

This is how you define an array of `ints`s for example:

```c
int numbers[3];
```

First you specify the data type of the items the array will hold. Then you give it a name and immediately after the name you also include a pair of square brackets with an integer. The integer number speficies the *length* of the array.

In the example above, the array can hold `3` values.

After defining the array, you can assign values individually, with square bracket notation, using indexing. Indexing in C (and most programming languages) starts at `0`.

```c
//Define the array; it can hold 3 values
int numbers[3];

//assign the 1st item of the numbers array the value of 1
int numbers[0] = 1;

//assign the 2nd item of the numbers array the value of 2
int numbers[1] = 2;

//assing the 3rd item of the numbers array the value of 3
int numbers[2] = 3;
```

You reference and fetch an item from an array by using the name of the array and the item's index in square brackets, like so:

```c
numbers[2]; // returns the value 3
```

## What are character arrays in C?

So, how does everything mentioned so far fit together, and what does it have to do with initializing strings in C and saving them to memory?

Well, strings in C are actually a type of array – specifically, they are a `character  array`. Strings are a collection of `char` values.

### How strings work in C

In C, all strings end in a `0`. That `0` lets C know where a string ends.

That string-terminating zero is called a **string terminator**. You may also see the term **null zero** used for this, which has the same meaning.

Don't confuse this final zero with the numeric integer `0` or even the character `'0'` - they are not the same thing. 

The string terminator is added automatically at the end of each string in C. But it is not visible to us – it's just always there.

The string terminator is represented like this: `'\0'`. What sets it apart from the character `'0'` is the backslash it has.

When working with strings in C, it's helpful to picture them always ending in *null zero* and having that extra byte at the end.

![Screenshot-2021-10-04-at-8.46.08-PM](https://www.freecodecamp.org/news/content/images/2021/10/Screenshot-2021-10-04-at-8.46.08-PM.png)

Each character takes up one byte in memory. 

The string `"hello"`, in the picture above, takes up `6 bytes`.

"Hello" has five letters, each one taking up 1 byte of space, and then the null zero takes up one byte also.

### The length of strings in C

The length of a string in C is just the number of characters in a word, **without** including the string terminator (despite it always being used to terminate strings). 

The string terminator is not accounted for when you want to find the length of a string.

For example, the string `freeCodeCamp` has a length of `12` characters.

But when counting the length of a string, you must always count any blank spaces too.

For example, the string `I code` has a length of `6` characters. `I` is 1 character, `code` has 4 characters, and then there is 1 blank space.

So the length of a string is not the same number as the number of bytes that it has and the amount of memory space it takes up.

### How to create character arrays and initialize strings in C

The first step is to use the `char` data type. This lets C know that you want to create an array that will hold characters. 

Then you give the array a name, and immediatelly after that you include a pair of opening and closing square brackets.

Inside the square brackets you'll include an integer. This integer will be *the largest number of characters you want your string to be*  **including** the string terminator.

```c
char city[7];
```

You can initialise a string one character at a time like so:

```c
#include <stdio.h>

int main(void) {
    char city[7];

    city[0] = 'A';
    city[1] = 't';
    city[2] = 'h';
    city[3] = 'e';
    city[4] = 'n';
    city[5] = 's';
    city[6] = '\0'; //don't forget this!

    printf("I live in %s",city);

}
```

But this is quite time-consuming. Instead, when you first define the character array, you have the option to assign it a value directly using a string literal in double quotes:

```c
#include <stdio.h>
int main(void){

char city[7] = "Athens";

//defines a character array named city
//it can hold a string up to 7 characters INCLUDING the string terminator
//the value "Athens" is assigned when the character array is being defined

//this is how you print the character array value
printf("I live in %s",city);

}
```

If you want, istead of including the number in the square brackets, you can only assign the character array a value. 

It works exactly the same as the example above. It will count the number of characters in the value you provide and automatically add the null zero character at the end:

```c
char city[] = "Athens";

//"Athens" has a length of 6 characters
//"Athens" takes up 7 bytes in memory,with the null zero included

/*
char city[7]  = "Athens";

is equal to 

char city[] = "Athens";

*/
```

Remember, you always need to reserve enough space for the longest string you want to include *plus* the string terminator.

If you want more room, need more memory, and plan on changing the value later on, include a larger number in the square brackets:

```c
char city[15] = "Athens";

/* 
The city character array will now be able to hold 15 characters 
(including the null zero)

In this case, the remaining 8 (15 - 7) places will be empty

You'll be able to reassign a value up to 15 characters (including null zero as always)
*/
```

### How to change the contents of a character array

So, you know how to initialize strings in C. What if you want to change that string though?

You cannot simply use the assignment operator (`=`) and assign it a new value. You can only do that when you first define the character array.

As seen earlier on, the way to access an item from an array is by referencing the array's name and the item's index number.

So to change a string, you can change each character individually, one by one:

```c
#include <stdio.h>

int main(void) {
    char city[7] = "Athens";

    printf("I live in %s",city);

    //changing each character individually means you have to use single quotation marks
    
    //the new value has to take up 7 bytes of memory

   //indexing starts at 0, the first character has an index of 0

    city[0] = 'L';
    city[1] = 'o';
    city[2] = 'n';
    city[3] = 'd';
    city[4] = 'o';
    city[5] = 'n';
    city[6] = '\0'; //DON'T FORGET THIS!

    printf("\nBut now I live in %s",city);

}
//output:
//I live in Athens
//But now I live in London
```

That method is quite cumbersome, time-consuming, and error-prone, though. It definitely is not the preferred way.

You can instead use the `strcpy()` function, which stands for `string copy`.

To use this function, you have to include the `#include <string.h>` line after the `#include <stdio.h>` line at the top of your file. 

The `<string.h>` file offers the `strcpy()` function.

When using `strcpy()`, you first include the name of the character array and then the new value you want to assign. The `strcpy()` function automatically add the string terminator on the new string that is created:

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char city[15] = "Athens";
    strcpy(city,"Barcelona");

    printf("I am going on holiday to %s",city);
    
    //output:
    //I am going on holiday to Barcelona
}
```

## Conclusion

And there you have it. Now you know how to declare strings in C.

To summarize:

- C does not have a built-in string function.
- To work with strings, you have to use character arrays.
- When creating character arrays, leave enough space for the longest string you'll want to store plus account for the string terminator that is included at the end of each string in C.
- To place or change strings in character arrays you either:
    - Define the array and then assign each individual character element one at a time.
    - OR define the array and initialize a value at the same time.
- When changing the value of the string, you can use the `strcpy()` function after you've included the `<string.h>` header file.

If you want to learn more about C, I've written a [guide](https://www.freecodecamp.org/news/what-is-the-c-programming-language-beginner-tutorial/) for beginners taking their first steps in the language.

It is based on the first couple of weeks of [CS50's Introduction to Computer Science course](https://www.freecodecamp.org/news/introduction-to-computer-science/) and I explain some fundamental concepts and go over how the language works at a high level.

You can also watch the [C Programming Tutorial for Beginners](https://www.youtube.com/watch?v=KJgsSFOSQv0&t=14s) on freeCodeCamp's YouTube channel.

Thanks for reading and happy learning :)






