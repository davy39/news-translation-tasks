---
title: How to Print Array Elements in a Given Order with or without a Function
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-02-16T21:58:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-print-array-elements-in-given-order-with-and-without-function
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/func.png
tags:
- name: arrays
  slug: arrays
- name: C++
  slug: c-2
- name: Problem Solving
  slug: problem-solving
seo_title: null
seo_desc: 'If you are learning to solve problems using a programming language, you''ve
  likely faced the problem of printing array elements in a given order or in reverse
  order.

  You might have also needed to do this by either using a user-defined function or
  not ...'
---

If you are learning to solve problems using a programming language, you've likely faced the problem of printing array elements in a given order or in reverse order.

You might have also needed to do this by either using a user-defined function or not using any function at all.

If this problem seems kind of complicated to you, then don't worry! I have come to help you. So, let's dive into the question real quick and see how it works.

🎥 If you are the kind of person that loves to follow along with a video too, I have also created a video for you:

%[https://youtu.be/pACJ2_bGaZ0]

## Understand The Question – Then Start Solving

For solving any kind of problem, the first thing you have to do is to understand the question first. Not only that, you also need to pay close attention to all the instructions including the required criteria for solving that problem.

If your question asks you to use recursion, that's the technique you'll employ. If your question asks you not to use any built-in special functions, you'll avoid those.

For this article, I will be using only one question but with two different criteria. I will go through the process to help you understand what you would need to do from the beginning for solving the problem.

### Here's the question with its criteria:

Create an integer array. Take the array elements as input from the user and print all the array elements in the given order and later in reverse order. You can't use any user-defined function.

Alright, now that we have our question, make sure you've read it fully. If reading it through one time does not make it clear in your mind, then read it two or three – or even more – times.

Then also look into the given criteria carefully. The question tells you that you can not use any user defined function. That means you can not add any kind of manually user-defined function in your code like `myFunction()`, and so on.

For this article, I will be using the **C++** programming language. But if you can understand the core concept then you can use any other programming language to solve this problem. After solving the problem, make sure to add your solution [to this GitHub repository](https://github.com/FahimFBA/problem-solving-made-easy). 

Also, if you like to solve problems using programming languages, then make sure to check [my ongoing YouTube playlist where I solve problems using the programming language](https://www.youtube.com/playlist?list=PL7ZCWbO2Dbl5p3wf0IOHeIZ6PHxTI3ADD).

### How to Solve the Problem

In C/C++, if you declare an array without initializing the value, then you need to specify the array size as well. 

When you declare the array with the array size, it automatically takes the necessary space in the memory for the entire array. So, if you take a larger array than you actually need, you will waste memory, as it takes the full space in memory for the full array whether you use all the indexes or not. 

So first, we want the user to input the array size (how many numbers they want us to process). Then we will create the array with the given array size. In that way, we can save unnecessary memory wastage. 

Well, as today's computers are more powerful, you would likely not notice any differences in memory wastage, as it would be pretty negligible. But trust me, you do need to understand how to save memory as that is one of the biggest concerns in today's world. Also, you never know when this knowledge will help you later, right?

```cpp
    cout << "Enter the array size: ";
    int arraySize;
    cin >> arraySize;
    int arr[arraySize];
```

Well then, after declaring our array, we will take the array elements from the user. We can simply use a `for()` loop for that. 

```cpp
    cout << "Enter the array elements " << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cin >> arr[i];
    }
```

In this way, we can take each value from the user and store it in our array in a sequential way. Keep in mind that the array always starts from the `0` index (the first element is at index `0`, the second is at index `1`, and so on).

Now it is time to print all the array elements (the value that each index of the array has) in the given order. That means we have to print the entire array in the same order we received from the user.

```cpp
    // printing the array in the correct order
    cout << "Printing the array in the original order" << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cout << arr[i] << " ";
    }
```

For printing the array in reverse order, we can simply print the array in a backwards direction. In this way, the last indexed value from the array will get printed first. Then the second to last indexed value (from the right side of the array) would get printed in the second position, and so on.

```cpp
    // printing the array in the reverse order
    cout << "\nPrinting the array in the reversed order" << endl;
    for (int i = arraySize - 1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }
```

That's it! Through this, you can solve the problem easily. Notice that we did not use any kind of user-defined function in our entire code. Thus, we also made sure that we successfully met all of the criteria.

The entire code now looks like this:

```cpp
#include <bits/stdc++.h>
using namespace std;

int main()
{
    cout << "Enter the array size: ";
    int arraySize;
    cin >> arraySize;
    int arr[arraySize];
    cout << "Enter the array elements " << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cin >> arr[i];
    }
    // printing the array in the correct order
    cout << "Printing the array in the original order" << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cout << arr[i] << " ";
    }
    // printing the array in the reverse order
    cout << "\nPrinting the array in the reversed order" << endl;
    for (int i = arraySize - 1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }    
}
```

### Here's another example question and criteria:

Create an integer array. Take the array elements as input from the user and print all the array elements in the given order and later in the reverse order. You have to use a user-defined function for printing the array in reverse order.

Now, this time the criteria has been changed. The only difference is that we need to use a user defined function right now.

If you can understand the previous technique and the code, then most probably you have already guessed how to solve this problem. We have to shift the part of the code that prints the array in the reverse order to a new user-defined function. Simply doing that will solve our problem. 

For example, I am going to name the new user-defined function `printReversely(int arr[], int arraySize)`. You can name it however you want by following the naming conventions of C++ (or whatever programming language you're using).

I am simply giving you the entire code for now:

```cpp
#include <bits/stdc++.h>
using namespace std;
void printReversely(int arr[], int arraySize);
int main()
{
    cout << "Enter the array size: ";
    int arraySize;
    cin >> arraySize;
    int arr[arraySize];
    cout << "Enter the array elements " << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cin >> arr[i];
    }
    // printing the array in the correct order
    cout << "Printing the array in the original order" << endl;
    for (int i = 0; i < arraySize; i++)
    {
        cout << arr[i] << " ";
    }
    // printing the array in the reverse order
    cout << "\nPrinting the array in the reversed order" << endl;
    printReversely(arr, arraySize);
}

void printReversely(int arr[], int arraySize)
{
    for (int i = arraySize - 1; i >= 0; i--)
    {
        cout << arr[i] << " ";
    }
}
```

In C/C++, the code execution always starts from the upper left corner.

As I wrote my `printReversely(int arr[], int arraySize)` function after the main function, I added the declaration part of it before the **main()** function. This will help the compiler determine whether it has access to the function or not. If you do not do that, then you'll get an error.

But if you write the entire `printReversely(int arr[], int arraySize)` function before the **main()** function then you do not necessarily need to add the declaration again before that. 

## Conclusion

Thanks for reading the entire article. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!

