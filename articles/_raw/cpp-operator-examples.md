---
title: C++ Operator Example – &, or, + Operators in C++
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-18T15:37:31.000Z'
originalURL: https://freecodecamp.org/news/cpp-operator-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/towfiqu-barbhuiya-5u6bz2tYhX8-unsplash--1-.jpg
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: "Most programming languages have built-in functionalities that let us carry\
  \ out certain operations like arithmetic, comparison, logical operations, and so\
  \ on. \nIn this article, we'll talk about three operators in C++ – the bitwise AND\
  \ (&) operator, th..."
---

Most programming languages have built-in functionalities that let us carry out certain operations like arithmetic, comparison, logical operations, and so on. 

In this article, we'll talk about three operators in C++ – the bitwise **AND** (`&`) operator, the logical **OR** (`||`) operator, and the arithmetic `+` operator. 

## How to Use the Bitwise AND (`&`) Operator in C++

The bitwise **AND** operator is denoted by the `&` symbol. 

Here's how the `&` operator works in C++:

* Evaluates the binary value of each operand.
* Adds the binary values together using a truth table AND format (we'll see a practical application in the examples in this section).
* Returns the base 10 value of the addition.

Let's see an example right away.

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x & y);
    // 8
}
```

In the code above, our operands are 10 and 12, stored in `x` and `y` respectively. We then used the `&` operator to evaluate both operands: `cout << (x & y);` and got a value of 8. 

That might seem confusing so let's break it down.

The binary value of 10 is 1010.

The binary value of 12 is 1100.

We'll then add both binary values, with each index corresponding with the other. That is, we add the value of the first index in 1010 which is 1 and the first index in 1100 which is also 1. The same applies to the other indexes.

Here's how:

As a reminder, this is how the **AND** truth table works: 1 and 1 => 1, 0 and 1 => 0, 1 and 0 => 1, 0 and 0 => 0. 

First index in 1010 => 1 & first index in 1100 => 1

1 and 1 => 1

Second index in 1010 => 0 & second index in 1100 => 1

o and 1 => 0

Third index in 1010 => 1 & third index in 1100 => 0

1 and 0 => 0

Fourth index in 1010 => 0 & fourth index in 1100 => 0

o and 0 => 0

Now we can get all our outputs: 1000. 

The base 10 value of 1000 is 8. This is why the `10 & 12` operation returned 8 in the code example.

You can also see the operation this way:

```txt
    10 = 1010
&
    12 = 1100
        _________
         1000
 
 1000 = 8 in base 10
```

## How to Use the Logical OR (`||`) Operator in C++

The logical **OR** operator is denoted by the `||` symbol. 

Here's how the `||` operator works:

* Evaluates two statements.
* If both statements are true, returns 1 (true).
* If both statements are false, returns 0 (false).
* If either of the statements is true, returns 1 (true).

Here is the first example:

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x > 5 || y < 15);
    // 1
}
```

The operation above returns 1 because both statements are true – the value of `x` is greater than 5 and the value `y` is less than 15. 

Let's have a look at another example.

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x > 20 || y < 10);
    // 0
}
```

We are getting 0 returned to us in the example because both statements are false – the value of `x` is not greater than 20 and the value of `y` is not less than 10.

Here's another example:

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x > 5 || y < 10);
    // 1
}
```

In the example above, we got 1 returned because one out of both statements is true – the value of `x` is greater than 5 and the value of `y` is less than 10. So, the `||` operator checks both statements, if any one of them is true, it returns 1. 

## How to Use the Arithmetic `+` Operator in C++

The `+` operator is used to add two or more variables/values together.

Here's an example:

```c++
#include <iostream>
using namespace std;
int main() {
    int x = 10;
    int y = 12;
    
    cout << (x + y);
    // 22
}
```

The example above is a simple mathematical operation that adds two number and returns the value of the addition. 

You can also perform this operation without storing them in a variable. That is:

```c++
#include <iostream>
using namespace std;
int main() {
    
    cout << (10 + 12);
    // 22
}
```

## Conclusion

In this article, we talked about three operator in C++. These operators are the bitwise **AND** (`&`) operator, the logical **OR** (`||`) operator, and the arithmetic `+` operator. 

We saw how the each operator works and some of the logic behind their operation. Each section had an example to help us understand the operators and how they evaluate their operands to give us a result.

Happy coding!


