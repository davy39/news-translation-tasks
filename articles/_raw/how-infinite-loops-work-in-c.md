---
title: How Infinite Loops Work in C++
subtitle: ''
author: AYUSH MISHRA
co_authors: []
series: null
date: '2025-08-01T22:44:18.097Z'
originalURL: https://freecodecamp.org/news/how-infinite-loops-work-in-c
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754065314765/5c8e45f0-6a43-4f1f-b254-2603b7d37e0c.png
tags:
- name: C++
  slug: cpp
- name: Loops
  slug: loops
- name: while loop
  slug: while-loop
- name: Do while loop
  slug: do-while-loop
- name: for loop
  slug: for-loop
seo_title: null
seo_desc: 'In C++, a loop is a part of code that is executed repetitively until the
  given condition is satisfied. An infinite loop is a loop that runs indefinitely,
  without any condition to exit the loop.

  In this article, we will learn about infinite loops in C...'
---

In C++, a loop is a part of code that is executed repetitively until the given condition is satisfied. An infinite loop is a loop that runs indefinitely, without any condition to exit the loop.

In this article, we will learn about infinite loops in C++, their types and causes, and their applications.

### Here’s what we’ll cover:

1. [What is an Infinite Loop in C++?](#heading-what-is-infinte-loop-in-c)
    
2. [Types of Infinite Loops in C++](#heading-types-of-infinte-loops-in-c)
    
3. [Common Causes of Accidental Infinite Loops in C++](#heading-common-cause-of-accidental-infinte-loops-in-c)
    
4. [Applications of Infinite Loops in C++](#heading-application-of-infinte-loops-in-c)
    
5. [Using Infinite Loops To Take User Input in C++](#heading-using-infinite-loops-to-take-user-input-in-c)
    
6. [Conclusion](#heading-conclusion)
    

## What is an Infinite Loop in C++?

An infinite loop is any loop in which the loop condition is always true, leading to the given block of code being executed an infinite number of times. They can also be called endless or non-terminating loops, which will run until the end of the program’s life.

Infinite loops are generally accidental and occur due to some mistake by the programmer. But they are pretty useful, too, in different kinds of applications, such as creating a program that does not terminate until a specific command is given.

## Types of Infinite Loops in C++

There are several ways to create an infinite loop in C++, using different loop constructs such as while, for, and do-while loops. Here, we will explore each method and provide examples.

* Infinite While Loops
    
* Infinite For Loops
    
* Infinite do-while Loops
    

### 1\. Infinite Loop using While Loop

This is the most popular type of while loop due to its simplicity. You just pass the value that will result in true as the condition of the while loop.

**Syntax:**

```plaintext
while(1)
    or
while(true)
```

**Example Code:**

```cpp
// Example of Infinite loop in C++ using for loop
#include <iostream>
using namespace std;

int main() {
    // Infinite loop using while
    while (true) {
        cout << "This is an infinite loop." << endl;
    }
    return 0;
}
```

Output:

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

………………….

### Infinite Loop using For Loop

In a for loop, if we remove the initialization, comparison, and update conditions, then it will result in an infinite loop.

**Syntax:**

```plaintext
for(;;)
```

**Example Code:**

```cpp
//Example of Infinite loop in C++ using for loop

#include <iostream>
using namespace std;

int main() {
    // Infinite loop using for loop
    for (;;) {
        cout << "This is an infinite loop." << endl;
    }
    return 0;
}
```

Output:

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

……………………….

### Infinite Loop using do-while Loop

Just like the other two loops discussed above, we can also create an infinite loop using a do-while loop. Although this loop is not preferred much due to its longer syntax.

**Syntax:**

```plaintext
do{
}while(1)
```

**Example Code:**

```cpp
// Infinite loop in C++ using do-while loop

#include <iostream>
using namespace std;

int main() {
   // infinite do-while loop
    do {
        cout << "This is an infinite loop." << endl;
    } while (true);
    
    return 0;
}
```

Output:

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

……………………….

## Common Causes of Accidental Infinite Loops in C++

Infinite loops can be both intentional and accidental. Accidental infinite loops are those which were not intended by the programmer but are caused due to some error in the program.

Following are some of the errors that may cause infinite loops in your programs unintentionally:

### 1\. Missing Update Statements

Infinite loops are caused when you forget to add an update condition inside the loop, which will terminate the loop in the future. The following program illustrates such a scenario:

**Example Code:**

```cpp
// Infinite loop caused due to missing update statement

#include <iostream>
using namespace std;

int main() {
    int i = 3;
    while (i < 5) {
        cout << i <<endl;
        // Missing update: i++;
    }
    return 0;
}
```

Output:

3

3

3

3

3

3

3

……………………

To fix the above code, we can add an update condition inside the loop like this:

```cpp
// fixed code

#include<iostream>
using namespace std ;

int main() {
int i = 3;
while (i < 5) {
    cout << i << endl;
    i++; // add the condition
}

return 0 ; 

}
```

Output:

3

4

### Incorrect Loop Conditions

The conditions mentioned inside the loop body are crucial to terminate a loop. An incorrect loop condition can result in an infinite loop. The following program illustrates such a scenario:

**Example Code:**

```cpp
// Infinite loop caused due to incorrect loop conditions

#include <iostream>
using namespace std;

int main() {
    int i = 2;
    while (i >= 0) {  
        cout << "Hello AnshuAyush " << endl;
        
    }
    return 0;
}
```

Output:

Hello AnshuAyush

Hello AnshuAyush

Hello AnshuAyush

Hello AnshuAyush

Hello AnshuAyush

……………………..

To fix the above code, we can update `i` inside the loop to eventually make the condition false:

```cpp
// fixed code 

#include<iostream>
using namespace std ;

int main() {
int i = 2;
while (i >= 0) {  
    cout << "Hello AnshuAyush" << endl;
    i--; // loop will stop
}

return 0 ; 

}
```

Ouptut:

Hello AnshuAyush

Hello AnshuAyush

Hello AnshuAyush

### Logical Errors in the Loop

In many scenarios, infinite loops are caused by small logical errors in the code. The following program illustrates such a scenario:

**Example Code:**

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 3; i >2; i += 2) {  
        cout <<"This is an infinite loop" << endl;
    }
    return 0;
}
```

Output:

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

This is an infinite loop.

……………………….

To fix the above code, we can either use a decreasing condition or use an incrementing loop condition.

Decreasing condition:

```cpp
for (int i = 3; i > 0; i--) {
    cout <<"This is NOT an infinite loop" << endl;
}
```

Increasing condition:

```cpp
for (int i = 3; i < 10; i += 2) {
    cout <<"Loop will end when i reaches 10" << endl;
}
```

## Applications of Infinite Loops in C++

Infinite loops do not only occur by accident, as I mentioned above. You can also create them on purpose for different use cases. The following are some of the common applications where you might use infinite loops intentionally:

* **Event loops:** Many Graphical User Interfaces (GUIs) use infinite loops to keep the program running and responsive to user actions.
    
* **Server applications:** Web servers use infinite loops to continuously listen to client connections or requests.
    
* **Embedded systems:** Embedded systems, such as microcontrollers, frequently use infinite loops as their main program loops to continuously respond to external events.
    
* **User inputs:** Infinite loops are also used to wait for valid user inputs. The loop keeps running until a valid input is provided by the user. We’ll look at an example of this one.
    

### Using Infinite Loops to Take User Input in C++

Infinite loops are commonly used in scenarios where a program needs to continuously take user input until a specific condition is met, such as exiting the program or getting a valid user input. The following program demonstrates how we can take user input from the user until a specific condition is met:

**Example Code:**

```cpp
// C++ Program to take user input from users using infinite loops

#include <iostream>
#include <string>
using namespace std;

int main() {
    string input;
    
    while (true) {
        cout << "Enter a command (type 'exit' to quit): ";
        getline(cin, input);

        if (input == "exit") {
        // Exit the loop if the user types 'exit'
            break; 
        }

        cout << "You entered: " << input << endl;
        // Process the input
    }
    cout << "Program exited." << endl;
    return 0;
}
```

Output:

Enter a command (type 'exit' to quit): Anshu

You entered: Anshu

Enter a command (type 'exit' to quit): Ayush

You entered: Ayush

Enter a command (type 'exit' to quit): exit

Program exited.

## Conclusion

Infinite loops aren’t always dangerous. They can be very useful when used with proper control, like break statements or condition checks. But if you use them carelessly, they can crash your program.

So just make sure you check your loop conditions and test your code using print statements between the programs to discover any unexpected behavior. In sum, infinite loops can be very powerful when handled carefully but can be very risky if left unchecked.

And if you'd like to support me and my work directly so I can keep creating these tutorials, [you can do so here](https://paypal.me/ayushM010). Thank you!
