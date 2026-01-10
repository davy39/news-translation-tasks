---
title: Double VS Float in C++ – The Difference Between Floats and Doubles
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-19T22:29:11.000Z'
originalURL: https://freecodecamp.org/news/double-vs-float-in-cpp-the-difference-between-floats-and-doubles
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/nick-hillier-yD5rv8_WzxA-unsplash-1.jpg
tags:
- name: C++
  slug: c-2
seo_title: null
seo_desc: 'In C++, there are various data types like string, int, char, bool, float,
  and double. Each of these data types have specific values that can be stored in
  them.

  When working with integers, we usually store them in an int data type. But this
  is only us...'
---

In C++, there are various data types like `string`, `int`, `char`, `bool`, `float`, and `double`. Each of these data types have specific values that can be stored in them.

When working with integers, we usually store them in an `int` data type. But this is only useful for whole numbers. 

When we want to store numbers with decimals, we can either use the `float` or `double`. Though these two data types are used for a similar purpose, they have some differences.

In this article, we'll talk about the differences between floats and doubles in C++ along with some examples.

## Difference Between Floats and Doubles

This section will be divided into sub-sections with each section focusing on one difference between floats and doubles.

### Difference in Byte Size

The byte size for `float` is 4 while the byte size for `double` is 8. 

This implies that `double` can store values that are twice the amount that `float` can hold.

We can see this by using the `sizeof()` operator. Here is an example:

```c++
#include <iostream>
using namespace std;
int main() {
    
    cout << "float: " << sizeof(float) << endl; // float: 4
    cout << "double: " << sizeof(double) << endl;// double: 8

}
```

### Difference in Precision (Accuracy)

When working with numbers that have a lot of decimal digits, we usually hope that the resulting value will be accurate. But the accuracy of our result is dependent on the number of decimal digits we are dealing with. 

Don't worry, we're still talking about C++, not mathematics. 

`float` and `double` both have varying capacities when it comes to the number of decimal digits they can hold. `float` can hold up to 7 decimal digits accurately while `double` can hold up to 15. 

Let's see some examples to demonstrate this. 

```c++
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    double MY_DOUBLE_VALUE = 5.12345678987;

    float MY_FLOAT_VALUE = 5.12345678987;
    
    cout << setprecision(7);
    cout << MY_DOUBLE_VALUE << endl; // 5.123457
    cout << MY_FLOAT_VALUE << endl; // 5.123457
}
```

In the example above, we created `float` and `double` variables – both having the same value: `5.12345678987`. 

The `setprecision()` function is used to tell the compiler the number of decimal places we want printed out. In our case, the value is 7. 

We can observe from the results in the code above, that both variables printed accurate values up to the 7th decimal place: `5.123457`.

Let's increase the parameter in the `setprecision()` function to 12 and see what happens.

```c++
#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    double MY_DOUBLE_VALUE = 5.12345678987;

    float MY_FLOAT_VALUE = 5.12345678987;
    
    cout << setprecision(12);
    cout << MY_DOUBLE_VALUE << endl; // 5.12345678987
    cout << MY_FLOAT_VALUE << endl; // 5.12345695496
}
```

From the results above, the `MY_DOUBLE_VALUE` variable printed out accurate values. But the `MY_FLOAT_VALUE` variable, from its 7th decimal place, printed out values entirely different from the original value it was given. 

This shows us the precision of both data types. Just like `float`, if we try to return a value that exceeds the accuracy range for the `double` data type, we will get an inaccurate value returned. 

### Difference in Usage

`float` is mostly used in graphic libraries for high processing power due to its small range. 

`double` is mostly used for calculations in programming to eliminate errors when decimal values are being rounded off. Although `float` can still be used, it should only be in cases when we're dealing with small decimal values. To be on the safe side, you should always use `double`. 

## Conclusion

In this article, we talked about the differences between floats and doubles in C++. 

We talked about three differences: byte size, precision, and usage.

We also learned that doubles have twice the byte size of floats. Also, doubles are more accurate when dealing with large decimal values.

Lastly, we talked about use cases which helped us understand when to use each data type. 

Happy coding!

