---
title: Int to String in C++ – How to Convert an Integer with to_string
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-02T21:01:13.000Z'
originalURL: https://freecodecamp.org/news/int-to-string-in-cpp-how-to-convert-an-integer-with-tostring
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/oskar-yildiz-cOkpTiJMGzA-unsplash.jpg
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: "When working with strings in your code, you might want to perform certain\
  \ operations like concatenating (or linking together) two strings. \nBut there are\
  \ cases when you'd rather work with numerical values as though they were strings\
  \ because concatena..."
---

When working with strings in your code, you might want to perform certain operations like concatenating (or linking together) two strings. 

But there are cases when you'd rather work with numerical values as though they were strings because concatenating a string and an integer will give you an error.

In this article, we'll see how to convert an integer to a string using the `to_string()` method in C++.

## How to Convert an Integer with `to_string()`

To use the `to_string()` method, we have to pass in the integer as a parameter. Here is what the syntax looks like to help you understand:

```txt
to_string(INTEGER)
```

Let's see an example.

```c++
#include <iostream>
using namespace std;

int main() {

    string first_name = "John";
    
    int age = 80;
    
    cout << first_name + " is " + age + " years old";
    
}
```

From the code above, you'll be expecting to see "John is 80 years old" in the console. But this actually returns an error because we are trying concatenate strings with an integer.

Let's fix this using the `to_string()` method.

```c++
#include <iostream>
using namespace std;

int main() {

    string first_name = "John";
    
    int age = 80;
    
    string AGE_TO_STRING = to_string(age);
    
    cout << first_name + " is " + AGE_TO_STRING + " years old";
    
}
```

We created a new variable called `AGE_TO_STRING` which stores the string value of the `age` variable with the help of the `to_string()` method. 

As you can see in the example, the integer `age` was passed in as a parameter to the `to_string()` method, converting it to a string.

Now when we run the code, we get "John is 80 years old" printed to the console.

The `to_string()` method also works when we want to convert the `float` and `double` data type values – used to store numbers with decimals – to strings.

Here are some examples to demonstrate that:

```c++
#include <iostream>
using namespace std;

int main() {

    string first_name = "John";
    
    float age = 10.5;
    
    string AGE_TO_STRING = to_string(age);
    
    cout << first_name + " is " + AGE_TO_STRING + " years old";
    // John is 10.500000 years old
    
}
```

The example above shows a `float` value being converted to a string. In the output (commented out in the code above), you can see the decimal value in the string. 

For the `double` data type:

```c++
#include <iostream>
using namespace std;

int main() {

    string first_name = "John";
    
    double age = 10.5;
    
    string AGE_TO_STRING = to_string(age);
    
    cout << first_name + " is " + AGE_TO_STRING + " years old";
    // John is 10.500000 years old
    
}
```

This is the same result as the last example. The only difference is that we're making use of a `double` value.

## Conclusion

In this article, we talked about converting an integer to a string in C++ using the `to_string()` method.

In our example, we tried to concatenate strings and an integer into one larger string but this gave us an error.

Using the `to_string()` method, we were able to convert variables with `int`, `float` and `double` data types and used them as though they were strings.

Happy coding!

