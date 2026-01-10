---
title: Integer Array in C – How to Declare Int Arrays with C Programming
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-13T17:22:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-declare-integer-arrays-with-c-programming
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/nick-hillier-yD5rv8_WzxA-unsplash.jpg
tags:
- name: c programming
  slug: c-programming
seo_title: null
seo_desc: "In this article, you will learn how to work with arrays in C.\nI will first\
  \ explain how to declare and initialize arrays. \nThen, I will also go over how\
  \ to access and change items in an array in C with the help of code examples along\
  \ the way.\nLet's ge..."
---

In this article, you will learn how to work with arrays in C.

I will first explain how to declare and initialize arrays. 

Then, I will also go over how to access and change items in an array in C with the help of code examples along the way.

Let's get into it!


## What Is An Array in C Programming?
An array is a data structure that stores multiple values in a single variable and in a sequential order that is easily accessible.

Arrays in C are a collection of values that store items of the same data type – an integer array holds only elements of the type `int`, a float array holds only elements of the type `float`, and so on.


## How to Declare an Integer Array in C Programming
The general syntax for declaring an array in C looks as you can see it in the code snippet below:

```
data_type array_name[array_size];
```

Let's take the following example:

```c
int my_numbers[5];
```

Let's break it down:

- I first defined the data type of the array, `int`.
- I then specified the name, `my_numbers`, followed by a pair of opening and closing square brackets,`[]`.
- Inside the square brackets, I defined the size (`5`), meaning the array can hold `5` integer values.
- Finally, I ended the statement with a semicolon (`;`).

Once you have set the array type and size during declaration, the array can't hold items of another type.

The array is also fixed in size, meaning you cannot add or remove items.


## How to Initialize an Integer Array in C Programming
There are a couple of ways you can initialize an integer array in C.

The first way is to initialize the array during declaration and insert the values inside a pair of opening and closing curly braces, `{}`. 

The general syntax to do that looks like this:
```
data_type array_name[array_size] = {value1, value2, value3, ...};
```

Let's take the array I declared in the previous section that can hold five integers and initialize it with some values:
```c
int my_numbers[5] = {10, 20, 30, 40, 50};
```

In the example above, I placed five comma-separated values inside curly braces, and assigned those values to `my_numbers` through the assignment operator (`=`).

Something to note here is that when you specify the size of the array, you can assign less number of elements, like so:
```c
int my_numbers[5] = {10, 20, 30};
```

Although the size of the array is `5`,  I only placed three values inside it. 

The array can hold two more items, and those remaining two positions have a default value of `0`.

Another way to initialize an array is to not specify the size, like so:
```c
int my_numbers[] = {10, 20, 30, 40, 50};
```

Even though I did not set the size of the array, the compiler knows its size because it knows the number of items stored inside it.


## How to Access Items in an Integer Array in C Programming
To access an element in an array, you have to specify the index of the element in square brackets after the array name.

The syntax to access an element looks like this:
```
array_name[element_index]
```

In C and programming in general, an array index always starts at `0`, becuase in computer science, counting starts from `0`.

So, the first item in an array has an index of `0`, the second item has an index of `1`, the third item has an index of `2`, and so on.

Taking the same array from the previous section, here is how you would access the first element, that is, `10`:
```c
#include <stdio.h>
int main() {
  int my_numbers[] = {10, 20, 30, 40, 50};
  printf("%d\n",my_numbers[0]);
  return 0;
}
```

Keep in mind that the last element in an array has an index of `array_size -1` – it is always one less than the size of the array. So, in an array that holds five elements, the index of the last element is `4`.

If in an array of five items, you try to access the last element by using an index of `5`, the program will run, but the element is not available, and you will get undefined behavior:
```c
#include <stdio.h>
int main() {
  int my_numbers[] = {10, 20, 30, 40, 50};
  printf("%d\n",my_numbers[5]);
  return 0;
}

// output
// -463152408
```


## How to Change Items in an Integer Array in C Programming
To change the value of a specific element, specify its index number and, with the assignment operator, `=`, assign a new value:
```c
#include <stdio.h>
int main() {
  int my_numbers[] = {10, 20, 30, 40, 50};
  my_numbers[0] = 11;
  return 0;
}
```

In the example above, I changed the first item in the array from `10` to `11`.


## Conclusion
And there you have it! You now know the basics of working with arrays in C.

To learn more about C, give this [C beginner's handbook](https://www.freecodecamp.org/news/the-c-beginners-handbook/) a read to become familiar with the basics of the language.

Thanks for reading, and happy coding!














