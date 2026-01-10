---
title: How to Find the Size of an Array in C with the sizeof Operator
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-12-05T14:53:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-the-size-of-an-array-in-c-with-the-sizeof-operator
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-eduardo-dutra-2115217-1.jpg
tags:
- name: arrays
  slug: arrays
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: 'When coding in the C programming language, there may be times when you
  need to know the size of an array.

  For example, when you want to loop through all the elements stored in the array
  to determine whether a specific value is present.

  In this articl...'
---

When coding in the C programming language, there may be times when you need to know the size of an array.

For example, when you want to loop through all the elements stored in the array to determine whether a specific value is present.

In this article, you will learn how to find the size of an array using the `sizeof()` operator.

Let's dive in!

## What is An Array in the C Programming Language?

Arrays let you store multiple values under the same variable name.

An array in the C programming language is a collection of items of the same data type. This means you can create an array of only integer values or an array of `char`s and so on.

To create an array in C, you first need to specify the data type of the values the array will store.

Then, you give the array a name followed by a pair of square brackets, `[]`.

Inside the square brackets, you can specify the size of the array.

So, here is how you would create an array of type `int` called `faveNumbers` that will hold `5` integers:

```c
int faveNumbers[5];
```

To insert values inside the array during its declaration, use the assignment operator, `=`, and a pair of curly braces, `{}`.

Inside the curly braces, enter the items and separate each one with a comma:

```c
int faveNumbers[5] = {7, 33, 13, 9, 29};
```

The code above creates an array with the name `faveNumbers` that holds `5` integers, `7, 33, 13, 9, 29`.

You could also write the code above as follows:

```c
int faveNumbers[] = {7, 33, 13, 9, 29};
```

In the example above, I didn't specify the size of the array. 

However, the compiler can tell that the size is `5` since I initialized it with `5` elements.

Something to note here is that you cannot change the size and type of the array once you declare it since they have a fixed length.

## How to Find the Size of An Array in the C Programming Language

C does not provide a built-in way to get the size of an array. 

With that said, it does have the built-in `sizeof` operator, which you can use to determine the size.

The general syntax for using the `sizeof` operator is the following:

```
datatype size = sizeof(array_name) / sizeof(array_name[index]);
```

Let's break it down:

- `size` is the variable name that stores the size of the array, and `datatype` specifies the type of data value stored in `size`.
- `sizeof(array_name)` calculates the size of the array in bytes.
- `sizeof(array_name[index])` calculates the size of one element in the array.

Now, let's see this operation in action and break it down into individual steps to see how it works.

Firstly, the `sizeof` operator returns the total amount of memory allocated to the array in bytes. 

```c
#include <stdio.h>
int main() {
    // my array
    int faveNumbers[] = {7, 33, 13, 9, 29};

    // using sizeof to get the size of the array in bytes
    size_t size = sizeof(faveNumbers);
    
    printf("The size is %d bytes \n", size);
}

// output

// The size is 20 bytes 
```

However, the code above doesn't calculate the size of the array directly. 

You will need some extra programming logic, which will look something like this:

```
array_length = (total size of the array) / (size of the first element in the array) 
```

To find the length of the array, you need to divide the total amount of memory by the size of one element - this method works because the array stores items of the same type. 

So, you can divide the total number of bytes by the size of the first element in the array.

To access the first element in an array, specify the name and, in square brackets, include `0`. 

In programming and Computer Science in general, indexing always starts at `0`, so the first element in an array will always have an index of `0`. 


```c
#include <stdio.h>
int main() {
    int faveNumbers[] = {7, 33, 13, 9, 29};

    size_t size = sizeof(faveNumbers) / sizeof(faveNumbers[0]);
  
    printf("The length of the array is %d \n", size);
}

// output

// The length of the array is 5 
```

Something to note here is the size of data types will vary from platform to platform.

## Conclusion

Hopefully, this article helped you understand how to find the size of an array in the C programming language using the built-in `sizeof` operator.

Thank you for reading, and happy coding!


