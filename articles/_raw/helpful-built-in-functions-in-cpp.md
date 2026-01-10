---
title: Helpful Built-in Functions in C++ that All Devs Should Know
subtitle: ''
author: AYUSH MISHRA
co_authors: []
series: null
date: '2025-07-22T17:24:12.694Z'
originalURL: https://freecodecamp.org/news/helpful-built-in-functions-in-cpp
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1753105870543/7bdb3c7e-873b-46a2-bdbd-0d881aacedfc.png
tags:
- name: C++
  slug: cpp
- name: Functional Programming
  slug: functional-programming
seo_title: null
seo_desc: 'Built-in functions in C++ are those functions that are part of the C++
  standard libraries. These functions are designed to provide common and essential
  functionality that is often required in programming.

  In this article, we will look at some of the ...'
---

Built-in functions in C++ are those functions that are part of the C++ standard libraries. These functions are designed to provide common and essential functionality that is often required in programming.

In this article, we will look at some of the most commonly used built-in functions in C++ so you can start using them in your code.

### What we’ll cover:

1. [The `sqrt()` Function](#heading-the-sqrt-function)
    
2. [The `pow()` Function](#heading-the-pow-function)
    
3. [The `sort()` Function](#heading-the-sort-function)
    
4. [The `find()` Function](#heading-the-find-function)
    
5. [The `binarysearch()` Function](#heading-the-binarysearch-function)
    
6. [The `max()` Function](#heading-the-max-function)
    
7. [The `min()` Function](#heading-the-min-function)
    
8. [The `swap()` Function](#heading-the-swap-function)
    
9. [The `toupper()` Function](#heading-the-toupper-function)
    
10. [The `tolower()` Function](#heading-the-tolower-function)
    

## The `sqrt()` Function

You use the `sqrt()` function to determine the square root of the value of type double. It is defined inside the `<cmath>` header file.

### **Syntax:**

```plaintext
sqrt (n)
```

**Parameter:** This function takes only one parameter of type double which is a number we want to find the square root of.

**Return Type:** The square root of the value of type double.

### Example Code

Let’s look at an example so you can see how this function works:

```cpp
// C++ program to see the use of sqrt() function
#include <cmath>     
#include <iostream>  

using namespace std;  
int main()
{
    double x = 100;

    double answer;

    // Use the sqrt() function to calculate the square root of the number
    answer = sqrt(x);

    // Print the result 
    cout << answer << endl;

    return 0;
}
```

Output:

10

## **The** `pow()` **Function**

You use the `pow()` function to find the value of the given number raised to some power. This function is also defined inside the `<cmath>` header file.

### **Syntax:**

```plaintext
double pow(double x, double y);
```

**Parameters:**

* **x:** The base number.
    
* **y:** The exponential power.
    

**Return Type:** value of **x** raised to the power **y**.

### Example Code:

Let’s look at an example to see how this works:

```cpp
// C++ program to see the use of the pow() function
#include <cmath>
#include <iostream>
using namespace std;

int main()
{
 // Declare an integer variable 'base' 
    int base = 5;

// Declare an integer variable 'exponent' 
    int exponent = 3;

// pow(5, 3) means 5^3 which is 5*5*5 = 125
// Use the pow() function to calculate base raised to the power of exponent
    int answer = pow(base, exponent);

// output the result
    cout << answer << endl;
}
```

Output:

125

## The `sort()` Function

The `sort()` function is part of STL's `<algorithm>` header. It is a function template that you can use to sort the random access containers, such as vectors, arrays, and so on.

### Syntax:

```plaintext
sort (arr , arr + n, comparator)
```

**Parameters:**

* **arr:** The pointer or iterator to the first element of the array.
    
* **arr + n:** The pointer to the imaginary element next to the last element of the array.
    
* **comparator:** The unary predicate function that is used to sort the value in some specific order. The default value of this sorts the array in ascending order.
    

**Return Value:** This function does not return any value.

### Example Code:

Let’s look at an example:

```cpp
#include <iostream>     
#include <algorithm>    // Header file that includes the sort() function

using namespace std;    

int main()
{
    // Declare and initialize an integer array with unsorted elements
    int arr[] = { 13, 15, 12, 14, 11, 16, 18, 17 };

    // Calculate the number of elements in the array
    int n = sizeof(arr) / sizeof(arr[0]);

    // Use the built-in sort() function from the algorithm library
    sort(arr, arr + n);

    // Print the sorted array using a loop
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";  
    
    return 0;
}
```

Output:

11 12 13 14 15 16 17 18

## The `find()` Function

The `find()` function is also part of the STL `<algorithm>` library. You use this function to find a value in the given range. You can use it with both sorted and unsorted datasets as it implements a linear search algorithm.

### **Syntax:**

```plaintext
find(startIterator, endIterator, key)
```

**Parameters:**

* **startIterator:** Iterates to the beginning of the range.
    
* **endIterator:** Iterates to the end of the range.
    
* **key:** The value to be searched.
    

**Return Value:** If the element is found, then the iterator is set to the element. Otherwise, it iterates to the end.

### Example Code:

Let’s look at an example to better understand how it works:

```cpp
// C++ program to see the the use of the find() function

#include <algorithm>   // Required for the find() function
#include <iostream>    
#include <vector>      

using namespace std;   

int main()
{
    // Initialize a vector 
    vector<int> dataset{ 12, 28, 16, 7, 33, 43 };

    // Use the find() function to search for the value 7
    auto index = find(dataset.begin(), dataset.end(), 7);

    // Check if the element was found
    if (index != dataset.end()) {
        // If found, print the position (index) by subtracting the starting iterator
        cout << "The element is found at the "
             << index - dataset.begin() << "nd index";
    }
    else {
        // If not found
        cout << "Element not found";
   }
    return 0;
}
```

Output:

The element is found at the 3rd index

## The `binary_search()` Function

The `binary_search()` function is also used to find an element in the range – but this function implements binary search instead of linear search as compared to the `find()` function. It’s also faster than the `find()` function, but you can only use it on sorted datasets with random access. It’s defined inside the `<algorithm>` header file.

### **Syntax:**

```plaintext
binary_search (starting_pointer , ending_pointer , target);
```

**Parameters:**

* **starting\_pointer:** Pointer to the start of the range.
    
* **ending\_pointer:** Pointer to the element after the end of the range.
    
* **target:** Value to be searched in the dataset.
    

**Return Value:**

* Returns true if the target is found.
    
* Else return false.
    

### Example Code:

Let’s check out an example to see how it works:

```cpp
// C++ program for the binary_search() function

#include <algorithm>   
#include <iostream>    
#include <vector>      

using namespace std;   

int main()
{
    // Initialize a sorted vector of integers
    vector<int> arr = { 56, 57, 58, 59, 60, 61, 62 };

    // binary_search() works only on sorted containers
    if (binary_search(arr.begin(), arr.end(), 62)) {
        // If found, print that the element is present
        cout << 62 << " is present in the vector.";
    }
    else {
        // If not found, print that the element is not present
        cout << 16 << " is not present in the vector";
    }

    cout << endl;
}
```

Output:

62 is present in the vector.

## The `max()` Function

You can use the `std::max()` function to compare two numbers and find the bigger one between them. It’s also defined inside the `<algorithm>` header file.

### Syntax:

```plaintext
max (a , b)
```

**Parameters:**

* **a:** First number
    
* **b:** Second number
    

**Return Value:**

* This function returns the larger number between the two numbers **a** and **b.**
    
* If the two numbers are equal, it returns the first number.
    

### Example Code:

Here’s an example:

```cpp
// max() function

#include <algorithm>  
#include <iostream>   
using namespace std;

int main()
{
    // Declare two integer variables
    int a = 8 ;
    int b = 10 ;

    // Use the max() function to find the larger number between a and b
    int maximum = max(a, b);

    // Display the result with a meaningful message
    cout << "The maximum of " << a << " and " << b << " is: " << maximum << endl;

    return 0;
}
```

Output:

The maximum of 8 and 10 is: 10

## The `min()` Function

You can use the `std::min()` function to compare two numbers and find the smaller of the two. It’s also defined inside the `<algorithm>` header file.

### Syntax:

```plaintext
min (a , b)
```

**Parameters:**

* **a:** First number
    
* **b:** Second number
    

**Return Value:**

* This function returns the smaller number between the two numbers **a** and **b.**
    
* If the two numbers are equal, it returns the first number.
    

### Example Code:

Here’s an example:

```cpp
// use of the min() function

#include <algorithm>  // For the built-in min() function
#include <iostream>   
using namespace std;

int main()
{
    // Declare two integer variables to store user input
    int a = 4 ;
    int b = 8 ;

    // Use the min() function to find the smaller 
    int smallest = min(a, b);

    // Display the result 
    cout << "The smaller number between " << a << " and " << b << " is: " << smallest << endl;

    return 0;
}
```

Output:

The smaller number between 4 and 8 is: 4

## The `swap()` Function

The `std::swap()` function lets you swap two values. It’s defined inside `<algorithm>` header file.

### **Syntax:**

```plaintext
swap(a , b);
```

**Parameters:**

* **a:** First number
    
* **b:** Second number
    

**Return Value:** This function does not return any value.

### Example:

Here’s how it works:

```cpp
//  use of the swap() function

#include <algorithm>  // For the built-in swap() function
#include <iostream>   
using namespace std;

int main()
{
    int firstNumber = 8 ;
    int secondNumber = 9 ;

    
    // Use the built-in swap() function to exchange values
    swap(firstNumber, secondNumber);

    // Display values after swapping
    cout << "After the swap:" << endl;
    cout << firstNumber << " " << secondNumber << endl;

    return 0;
}
```

Output:

After the swap:

9 8

## The `tolower()` Function

You can use the `tolower()` function to convert a given alphabet character to lowercase. It’s defined inside the `<cctype>` header.

### Syntax:

```plaintext
tolower (c);
```

**Parameter(s):**

* **c:** The character to be converted.
    

**Return Value:**

* Lowercase of the character c.
    
* Returns c if c is not a letter.
    

### Example Code:

Here’s how it works:

```cpp
// C++ program

// use of tolower() function

#include <cctype>     
#include <iostream>   
using namespace std;

int main()
{
    // Declare and initialize a string with uppercase characters
    string str = "FRECODECAMP";

    for (auto& a : str) {
        a = tolower(a);
    }

    // Print the modified string 
    cout << str;

    return 0;
}
```

Output:

freecodecamp

## The `toupper()` Function

You can use the `toupper()` function to convert the given alphabet character to uppercase. It’s defined inside the `<cctype>` header.

### Syntax:

```plaintext
toupper (c);
```

**Parameters:**

* **c:** The character to be converted.
    

**Return Value**

* Uppercase of the character c.
    
* Returns c if c is not a letter.
    

### Example Code:

Here’s how it works:

```cpp
// use of toupper() function

#include <cctype>     
#include <iostream>   
using namespace std;

int main()
{
    // Declare and initialize a string 
    string str = "freecodecamp";

    for (auto& a : str) {
        a = toupper(a);
    }

    // Output the converted uppercase string
    cout << str;

    return 0;
}
```

Output:

FREECODECAMP

## Conclusion

Inbuilt functions are helpful tools in competitive programming and in common programming tasks. These help in improving code readability and enhance the efficiency of code. In the above article, we discussed some very useful common inbuilt functions. Some common inbuilt functions are `max()`, `min()`, `sort()`, and `sqrt()`, etc. By using these inbuilt libraries, we can reduce boilerplate code and speed up the process of software development. These help in writing more concise, reliable, and maintainable C++ programs.

And if you'd like to support me and my work directly so I can keep creating these tutorials, [you can do so here](https://paypal.me/ayushM010). Thank you!
