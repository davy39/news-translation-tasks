---
title: How to Convert an Int to a String in C++ – Integer Cast Tutorial
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-11-10T18:54:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-an-int-to-a-string-in-cpp
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/uday-awal-UjJWhMerJx0-unsplash.jpg
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: "Type casting or type conversion is the process of converting a variable\
  \ from one data type to another. \nType casting can be done implicitly or explicitly.\
  \ \nImplicit type casting gets done automatically via the compiler, while explicit\
  \ type casting is..."
---

Type casting or type conversion is the process of converting a variable from one data type to another. 

Type casting can be done implicitly or explicitly. 

Implicit type casting gets done automatically via the compiler, while explicit type casting is done by the developer.

In this article, you'll learn how to convert an integer to a string in C++ using the `stringstream` class and the `to_string()` method.

## How to Convert an Int to a String in C++ Using the `stringstream` Class

Using the `stringstream` class, we can convert an integer to a string. 

Here's an example to help you understand why you'd need to convert an integer to a string:

```c++
#include <iostream>
using namespace std;

int main() {

    int age = 20;

    cout << "The user is " + age + " years old";
    // error: invalid operands of types 'const char*' and 'const char [11]' to binary 'operator+'

    return 0; 

}

```

In the example above, we created an `int` variable with a value of 20. 

When we tried to concatenate that value in a string, we got an error saying "invalid operands of types...". 

The error was raised because we tried to perform an operation using two incompatible variable types. The solution would be to convert one variable and make it compatible with the other. 

The `stringstream` class has insertion (`<<`) and extraction (`>>`) operators. 

The insertion operator is used to pass a variable to the stream. In our case, to pass an integer to the stream. 

The extraction operator is used to give out the modified variable. 

In other words, a `stringstream` object would take in a data type, convert it to another data type, and assign the new data type to a variable.

Here's an example: 

```c++
#include <iostream>
#include <sstream>  
using namespace std;

int main() {

    int age = 20;
    
    // stringstream object
    stringstream stream;
    
    // insertion of integer variable to stream
    stream << age;
    
    // variable to hold the new variable from the stream
    string age_as_string;
    
    // extraction of string type of the integer variable
    stream >> age_as_string;
    
    cout << "The user is " + age_as_string + " years old";
    // The user is 20 years old

    return 0; 

}

```

In the code above, we created a `stringstream` object called `stream`. Note that you must include the stringstream class before you can use it: `include <sstream>`.

We then inserted the integer into the stream: `stream << age;`.

After that, we created a new variable called `age_as_string`. This variable will store the string variable that will be extracted from the stream. 

Lastly, we extracted the string type of the integer and stored it in the variable created above: `stream >> age_as_string;`. 

Now we can concatenate the strings and get the desired result: 

```c++
    cout << "The user is " + age_as_string + " years old";
    // The user is 20 years old
```

## How to Convert an Int to a String in C++ Using the `to_string()` Method

You can use the [to_string() method](https://www.freecodecamp.org/news/int-to-string-in-cpp-how-to-convert-an-integer-with-tostring/) to convert int, float, and double data types to strings. 

Here's an example: 

```c++
#include <iostream>
using namespace std;

int main() {

    int age = 20;
    
    string age_as_string = to_string(age);
    
    cout << "The user is " + age_as_string + " years old";
    // The user is 20 years old

    return 0; 

}

```

In the code above, we passed in the `age` variable to the `to_string()`: `string age_as_string = to_string(age);`.

This converted the `age` variable to a string. Just like the example in the last section, we can now use the variable as a string: 

```c++
cout << "The user is " + age_as_string + " years old";
// The user is 20 years old
```

## Summary

In this article, we talked about the different ways of converting an integer to a string in C++. 

The examples showed how to use the `stringstream` class and the `to_string()` method to convert an integer to a string. 

Happy coding!

