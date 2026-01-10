---
title: Binary Search in C++ – Algorithm Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-03-17T16:52:22.000Z'
originalURL: https://freecodecamp.org/news/binary-search-in-c-algorithm-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/binary-search-algorithm-1.png
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: C++
  slug: c-2
seo_title: null
seo_desc: "The binary search algorithm is a divide and conquer algorithm that you\
  \ can use to search for and find elements in a sorted array. \nThe algorithm is\
  \ fast in searching for elements because it removes half of the array every time\
  \ the search iteration ha..."
---

The binary search algorithm is a divide and conquer algorithm that you can use to search for and find elements in a sorted array. 

The algorithm is fast in searching for elements because it removes half of the array every time the search iteration happens. 

So instead of searching through the whole array, the algorithm removes half of the array where the element to be searched for can't be found. It does this continuously until the element is found. 

In a case where the element to be searched for doesn't exist, it returns a value of -1. If the element exists, then it returns the index of the element. 

If the explanations above seem complex, then you should check out this [visual guide on how the binary search algorithm works](https://www.freecodecamp.org/news/binary-search-in-java-algorithm-example/#:~:text=How%20Does%20the%20Binary%20Search%20Algorithm%20Work%3F). 

In this article, you'll see an implementation of the binary search algorithm in C++.

Let's get started!

## Binary Search Algorithm Example in C++

In this section, we'll break down and explain the implementation of binary search in C++.

Here's the code:

```c++
#include <iostream>
using namespace std;

int binarySearch(int array[], int low, int high, int number_to_search_for) {

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (number_to_search_for == array[mid]){
            return mid;
        }

        if (number_to_search_for > array[mid]){
            low = mid + 1;
        }
      
        if (number_to_search_for < array[mid]){
            high = mid - 1;
        }

    }

  return -1;
}

int main(void) {
  int arrayOfNums[] = {2,4,7,9,10,13,20};
  
  int n = sizeof(arrayOfNums) / sizeof(arrayOfNums[0]);
  
  int result = binarySearch(arrayOfNums, 0, n - 1, 13);
  
  if (result == -1){
      printf("Element doesn't exist in the array");
  }
  else{
      printf("The index of the element is %d", result);
  }
  
  // The index of the element is 5
}
```

To start with, we created a method called `binarySearch` which had four parameters:

* `array[]` represents the array to be searched through.
* `low` represents the first element of the array. 
* `high` represents the last element of the array. 
* `number_to_search_for` represents the number to be searched for in `array[]`. 

Next, we created a `while` loop that will run continuously until the search operation returns a value – either the index of the element or -1. 

In the `while` loop:

`mid` is used to represent the center/midpoint of the array: `int mid = low + (high - low) / 2;`.

The first `if` statement is executed if `mid` has the same value as the element to be searched for: 

```c++
if (number_to_search_for == array[mid]){
	return mid;
}
```

The second `if` statement moves the position of `low` to the index after the midpoint of the array:

```c++
if (number_to_search_for > array[mid]){
	low = mid + 1;
}
```

This removes all the elements on the left side of the array because the element to be searched for is greater than they are, so there is no need to search through that part of the array.

The third `if` statement does the opposite of the second statement – it moves the position of high to the index before the midpoint of the array: 

```c++
if (number_to_search_for < array[mid]){
	high = mid - 1;
}
```

Here's a summary of the code in the `if` statements: 

1. If the number to be searched for is equal to `mid`, the `mid` index will be returned.
2. If the number to be searched for is greater than `mid`, search through the elements on the right side of `mid`.
3. If the number to be searched for is less than `mid`, search through the elements on the left side of `mid`.

If the number to be searched for doesn't exist, -1 will be returned. You can see this after the `while` loop in the code. 

Lastly, we tested the `binarySearch` method:

```c++
int main(void) {
  int arrayOfNums[] = {2,4,7,9,10,13,20};
  
  int n = sizeof(arrayOfNums) / sizeof(arrayOfNums[0]);
  
  int result = binarySearch(arrayOfNums, 0, n - 1, 13);
  
  if (result == -1){
      printf("Element doesn't exist in the array");
  }
  else{
      printf("The index of the element is %d", result);
  }
  
  // The index of the element is 5
}
```

In the code above, we passed in the values of the parameters created in the `binarySearch` method: `binarySearch(arrayOfNums, 0, n -1, 13)`. 

* `arrayOfNums` represents the array to be searched for: {2,4,7,9,10,13,20}. 
* `0` represents the first index of the array. 
* `n - 1` represents the last index of the array. Have a look at the code to see how `n` was created. 
* `13` is the number to be searched for in `arrayOfNums`.

When you run the code, "The index of the element is 5" will be printed in the console. This is because the index of the number to be searched for (13) is 5. 

You can play around with the code by changing the value of the number to be searched for.

## Summary

In this article, we talked about the implementation of the binary search algorithm in C++. 

We saw a code example that had a `binarySearch` method which took in parameters, searched through an array of numbers, and returned the appropriate value after the search operation. 

We also saw a detailed explanation of each part of the code. 

Happy coding!

