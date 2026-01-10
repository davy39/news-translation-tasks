---
title: String to Int in C++ – How to Convert a String to an Integer Example
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-10-18T14:54:58.000Z'
originalURL: https://freecodecamp.org/news/string-to-int-in-c-how-to-convert-a-string-to-an-integer-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/nick-hillier-yD5rv8_WzxA-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: C++
  slug: c-2
seo_title: null
seo_desc: 'When you''re coding in C++, there will often be times when you''ll want
  to convert one data type to a different one.

  In this article you''ll learn how to convert a string to an integer in C++ by seeing
  two of the most popular ways to do so.

  Let''s get st...'
---

When you're coding in C++, there will often be times when you'll want to convert one data type to a different one.

In this article you'll learn how to convert a string to an integer in C++ by seeing two of the most popular ways to do so.

Let's get started!

## Data types in C++

The C++ programming language has a few built-in data types:

- `int`, for integer (whole) numbers (for example 10, 150)
- `double`, for floating point numbers (for example 5.0, 4.5)
- `char`, for single characters (for example 'D', '!')
- `string`, for a sequence of characters (for example "Hello")
- `bool`, for boolean values (true or false)


C++ is a **strongly typed** programming language, meaning that when you create a variable you have to explicitely declare what type of value will be stored in it. 

## How to declare and initialize `int`s  in C++

To *declare* an `int` variable in C++ you need to first write the data type of the variable – `int` in this case. This will let the compiler know what kind of values the variable can store and therefore what actions it can take. 

Next, you need give the variable a name. 

Lastly, don't forget the semicolon to end the statement!

```cpp
#include <iostream>

int main() {
    int age;
}
```

You can then give the variable you created a value, like so:

```cpp
#include <iostream>

int main() {
    int age;
    age = 28;
}
```

Instead of doing these actions as separate steps, you can combine them by *initializing* the variable and finally printing the result:

```cpp
// a header file that enables the use of functions for outputing information
//e.g. cout or inputing information e.g. cin
#include <iostream> 

// a namespace statement; you won't have to use the std:: prefix
using namespace std;


int main() { // start of main function of the program
    int age = 28; 
    // initialize a variable. 
    //Initializing  is providing the type,name and value of the varibale in one go.

    // output to the console: "My age is 28",using chaining, <<
    cout << "My age is: " << age << endl;
}// end the main function
```

## How to declare and initialize `string`s in C++

Strings are a collection of individual characters.

Declaring strings in C++ works very similarly to declaring and initializing `int`s, which you saw in the section above.

The C++ standard library provides a `string` class. In order to use the string data type, you'll have to include the `<string>` header library at the top of your file, after `#include <iostream>`. 

After including that header file, you can also add `using namespace std;` which you saw earlier. 

Among other things, after adding this line, you won't have to use `std::string` when creating a string variable – just `string` alone.


```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    //declare a string variable

    string greeting;
    greeting = "Hello";
    //the `=` is the assignment operator,assigning the value to the variable

}
```

Or you can initialize a string variable and print it to the console:

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    //initialize a string variable

    string greeting = "Hello";
   
   //output "Hello" to the console
   cout << greeting << endl;
}
```

## How to convert a string to an integer

As mentioned earlier, C++ is a *strongly typed* language. 

If you try to give a value that doesn't align with the data type, you'll get an error.

Also, converting a string to an integer is not as simple as using type casting, which you can use when converting `double`s to `int`s.

For example, you **cannot** do this:

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
   string str = "7";
   int num;

   num = (int) str;
}
```

The error after compiling will be:

```
hellp.cpp:9:10: error: no matching conversion for C-style cast from 'std::__1::string' (aka
      'basic_string<char, char_traits<char>, allocator<char> >') to 'int'
   num = (int) str;
         ^~~~~~~~~
/Library/Developer/CommandLineTools/usr/bin/../include/c++/v1/string:875:5: note: candidate function
    operator __self_view() const _NOEXCEPT { return __self_view(data(), size()); }
    ^
1 error generated.
```

There are a few ways to convert a string to an int, and you'll see two of them mentioned in the sections that follow.

### How to convert a string to an int using the `stoi()` function

One effective way to convert a string object into a numeral int is to use the `stoi()` function. 

This method is commonly used for newer versions of C++, with is being introduced with C++11.

It takes as input a string value and returns as output the integer version of it.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
   // a string variable named str
   string str = "7";
   //print to the console
   cout << "I am a string " << str << endl;

   //convert the string str variable to have an int value
   //place the new value in a new variable that holds int values, named num
   int num = stoi(str);
   
   //print to the console
   cout << "I am an int " << num << endl;
}
```

Output:

```
I am a string 7
I am an int 7
```


### How to convert a string to an int using the `stringstream` class

The `stringstream` class is mostly used in earlier versions of C++. It works  by performing inputs and outputs on strings.

To use it, you first have to include the `sstream` library at the top of your program by adding the line `#include <sstream>`.

You then add the `stringstream` and create an `stringstream` object, which will hold the value of the string you want to convert to an int and will be used during the process of converting it to an int.

You use the `<<` operator to *extract* the string from the string variable.

Lastly, you use the `>>` operator to *input* the newly converted int value to the int variable.

```cpp
#include <iostream>
#include <string>
#include <sstream> // this will allow you to use stringstream in your program

using namespace std;

int main() {
    //create a stringstream object, to input/output strings
   stringstream ss; 
   
   // a variable named str, that is of string data type
   string str = "7";
   
   // a variable named num, that is of int data type
   int num;
   
   
   //extract the string from the str variable (input the string in the stream)
   ss << str;
   
   // place the converted value to the int variable
   ss >> num;
   
   //print to the consloe
   cout << num << endl; // prints the intiger value 7
}
```

## Conclusion

And there you have it! You have seen two simple ways to convert a string to an integer in C++.

If you're looking to learn more about the C++ programming language, check out [this 4-hour course](https://www.youtube.com/watch?v=vLnPwxZdW4Y&t=3485s) on freeCodeCamp's YouTube channel.

Thanks for reading and happy learning 😊



