---
title: Quick Sort – Algorithm Time Complexity with C++ and Java Code Example
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-11-03T00:43:11.000Z'
originalURL: https://freecodecamp.org/news/quick-sort-algorithm-time-complexity-with-cpp-and-java-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/kelly-sikkema-377gw1wN0Ic-unsplash.jpg
tags:
- name: algorithms
  slug: algorithms
- name: C++
  slug: c-2
- name: Java
  slug: java
seo_title: null
seo_desc: "In this article, you'll learn about one of the most commonly used programming\
  \ algorithms – the quick sort algorithm. \nYou'll get to know how the algorithm\
  \ works with the help of visual guides. You'll also see some code examples that\
  \ will help you imp..."
---

In this article, you'll learn about one of the most commonly used programming algorithms – the quick sort algorithm. 

You'll get to know how the algorithm works with the help of visual guides. You'll also see some code examples that will help you implement the algorithm in C++ and Java. 

Last but not the least, we'll talk about the [time complexity](https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/) for the quick sort algorithm in worst, average, and best case complexity scenarios.

Let's get started!

## How Does the Quick Sort Algorithm Work?

The quick sort algorithm is based on the divide and conquer rule. In a given array of unordered elements (numbers), a pivot is chosen. The pivot is important because other elements will be sorted in respect to its value.

At the end of the sorting operation, all the numbers lower than the pivot will be moved to the left side of the pivot while all numbers higher will be on the right. This is also known as partitioning.

At this stage, the numbers on the right and left of the pivot may/will most likely be unordered.

Next, the unordered numbers before and after the pivot are put into separate arrays – one array for the numbers on the left and another for those on the right.

A pivot will then be chosen in each array and the process from the start is repeated until each number is sorted out separately. Combining all the numbers, you'll have a sorted array in ascending order.

Here's a summary of the above explanations:

**Step #1:** An array of unordered numbers is given.

**Step #2:** One number is chosen as the pivot. 

**Step #3:** Numbers lower than the pivot move to the left side of the pivot.

**Step #4:** Numbers higher than the pivot move to the right side of the pivot.

**Step #5:** The array is broken down into two arrays – the first array will contain elements on the left side of the pivot while the second array will contain elements on the right. 

**Step #6:** Step #2 to #5 is repeated for each array until every element has been sorted in ascending order.

The steps above may seem confusing. You'll understand it better in the next section with the help of visual guides. 

## How Does Quick Sort Work?

In the last section, I gave a brief summary of what happens when you use the quick sort algorithm to sort an array of numbers. But that didn't explain how the sorting operation works under the hood.

In this section, using visual guides, you'll understand how numbers are moved to either the left or right side of the pivot, and how sub arrays are created (also known as partitioning). This will also help you understand the code easily when we get to that part. 

Here's the array we'll be working with: `9,4,8,3,7,1,6,2,5`.

The array above has a set of unordered numbers. So how does quick sort work? 

As I explained in the previous section, we have to select one element to act as the pivot. 

So let's take 5 as the pivot. We'll also need two variables: `X` and `Y`. They will be used to compare and interchange the positions of numbers in respect to the pivot.

Here's what that looks like:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort.png)
_quick-sort parameters_

In the image above, we have three arrows: red, blue, and yellow which denote `X`, `Y`, and the pivot, respectively. 

The operation is pretty simple: 

* If the value of `y` is greater than the pivot, increment `Y`. 
* If the value of `y` is less than or equal to the pivot, increment `X`, and swap the `x` with `y`. 

Let's demonstrate that using the array in the image above: `9,4,8,3,7,1,6,2,5`. 

### Iteration #1

Pivot = 5.  
Y = 9.

Is Y less than or equal to the pivot? No.

Increment Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort1.png)

### Iteration #2

Pivot = 5.  
Y = 4.

Is Y less than or equal to the pivot? Yes.

##### Step #1 - Increment X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort2.png)

##### Step #2 - Swap the value of X and Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort2i.png)

##### Step #3 - Increment Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort2ii.png)

Iterations #1 and #2 are basically all that happens during the sorting operation. 

In order to help you understand better, I'll go over all the iterations until we have numbers smaller than the pivot on the left and those higher on the right. 

### Iteration #3

Pivot = 5.  
Y = 8.

Is Y less than or equal to the pivot? No.

Increment Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort3.png)

### Iteration #4

Pivot = 5.  
Y = 3.

Is Y less than or equal to the pivot? Yes.

##### Step #1 - Increment X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort4.png)

##### Step #2 - Swap the value of X and Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort4i.png)

##### Step #3 - Increment Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort4ii.png)

### Iteration #5

Pivot = 5.  
Y = 7.

Is Y less than or equal to the pivot? No.

Increment Y. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort5.png)

### Iteration #6

Pivot = 5.  
Y = 1.

Is Y less than or equal to the pivot? Yes.

##### Step #1 - Increment X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort6.png)

##### Step #2 - Swap the value of X and Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort6i.png)

##### Step #3 - Increment Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort6ii.png)

### Iteration #7

Pivot = 5.  
Y = 6.

Is Y less than or equal to the pivot? No.

Increment Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort7.png)

### Iteration #8

Pivot = 5.  
Y = 6.

Is Y less than or equal to the pivot? Yes.

##### Step #1 - Increment X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort8.png)

##### Step #2 - Swap the value of X and Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort8i.png)

##### Step #3 - Increment Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort8ii.png)

### Iteration #9

At this point, `Y` is now pointing to the pivot. You can either increment `X` and swap if with `Y`, or you can use the format in the previous iterations. I'll go with the latter. 

Pivot = 5.  
Y = 5.

Is Y less than or equal to the pivot? Yes.

##### Step #1 - Swap the value of X and Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/quick-sort9i.png)

Our array now looks like this: `4,3,1,2,5,8,6,9,7`

If you look at the current state of the array, you'd realize that:

* The pivot is now at the center. 
* All the numbers on the left side of the pivot are lower than the pivot. 
* All the numbers on the right side of the pivot are higher than the pivot.

But we're not yet done. The numbers are still unordered. To sort them, we'll break the array down into two sub arrays (excluding the pivot element).

The first array will have all the numbers on the left side of the pivot: `4,3,1,2`.

The second array will have all the numbers on the right side of the pivot: `8,6,9,7`.

Let's sort the first array. As usual, you need a pivot.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array-1.png)

### Iteration #1

Pivot = 2.  
Y = 4.

Is Y less than or equal to the pivot? No.

Increment Y. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array.png)

### Iteration #2

Pivot = 2.  
Y = 3.

Is Y less than or equal to the pivot? No.

Increment Y. 

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array2.png)

### Iteration #3

Pivot = 2.  
Y = 1.

Is Y less than or equal to the pivot? Yes.

##### Step #1 - Increment X

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array3.png)

##### Step #2 - Swap the value of X and Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array3i.png)

##### Step #3 - Increment Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array4.png)

### Iteration #3

Pivot = 2.  
Y = 2.

Is Y less than or equal to the pivot? Yes.

##### Step #1 - Swap the value of X and Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sub-array6.png)

Again, we break down the array into sub arrays excluding the pivot (2). Note that we're still dealing with the numbers on the left side of the initial array.

The first array will have this: `1`.

The second array will have these: `4,3`.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/partition.png)

The first array has only one element so it is already sorted. Let's sort the second array:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/array.png)

### Iteration #1

Pivot = 3.  
Y = 4.

Is Y less than or equal to the pivot? No.

Increment Y.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/array2.png)

### Iteration #2

Pivot = 3.  
Y = 3.

Is Y less than or equal to the pivot? Yes.

##### Step #1 - Swap the value of X and Y

![Image](https://www.freecodecamp.org/news/content/images/2022/11/array3.png)

We'll now have the numbers in this order:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/sorted.png)

All the numbers on the left side of the first pivot have been sorted in ascending order: `1,2,3,4,5,8,6,9,7`.

The process is the same for sorting the numbers on the right side. It's time to attempt doing it yourself! Just follow the steps in previous examples. 

## Quick Sort Algorithm Java Code Example

Here is a code example in Java for the quick sort algorithm. I've included comments to make the code easier to understand.

If you have followed along in the previous sections then this should be self-explanatory.

```java
// Quick sort in Java

import java.util.Arrays;

class Quicksort {
    
    // method for swapping elements x and y
    static void swap(int[] arr, int x, int y) {
        int temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
    }

  // partition method
  static int partition(int array[], int low, int high) {
    
    //pivot
    int pivot = array[high];
    
    int x = (low - 1);
    
    

    // loop for comparing all elements with pivot element
    for (int y = low; y < high; y++) {
      if (array[y] <= pivot) {
        x++;
        
        swap(array, x, y);
      }

    }

    int temp = array[x + 1];
    array[x + 1] = array[high];
    array[high] = temp;

    return (x + 1);
  }

  static void quickSort(int array[], int low, int high) {
    if (low < high) {

      int array_partition = partition(array, low, high);
      
      // quick sort elements on the left recursively
      quickSort(array, low, array_partition - 1);

      // quick sort elements on the right recursively
      quickSort(array, array_partition + 1, high);
    }
  }
}

class Main {
  public static void main(String args[]) {

    int[] my_array = { 9,4,8,3,7,1,6,2,5 };

    int size = my_array.length;

    Quicksort.quickSort(my_array, 0, size - 1);

    System.out.println("Sorted Array: ");
    System.out.println(Arrays.toString(my_array));
    // Sorted Array: [1, 2, 3, 4, 5, 6, 7, 8, 9]
  }
}
```

## Quick Sort Algorithm C++ Code Example

Here's an example of the quick sort algorithm in C++:

```c++
#include <bits/stdc++.h>
using namespace std;

// function for swapping elements x and y
void swap(int* x, int* y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

int partition(int arr[], int low, int high)
{
    // pivot
	int pivot = arr[high]; 
	int x = (low- 1); 

    // loop for comparing all elements with pivot element
	for (int y = low; y <= high - 1; y++) {
		
		if (arr[y] < pivot) {
			x++; 
			swap(&arr[x], &arr[y]);
		}
	}
	swap(&arr[x + 1], &arr[high]);
	return (x + 1);
}

void quickSort(int arr[], int low, int high)
{
	if (low < high) {
		
		int array_partition = partition(arr, low, high);
        
        // quick sort elements on the left recursively
		quickSort(arr, low, array_partition - 1);
		
		// quick sort elements on the right recursively
		quickSort(arr, array_partition + 1, high);
	}
}

// print array function 
void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}

int main()
{
	int arr[] = { 9,4,8,3,7,1,6,2,5 };
	
	int size = sizeof(arr) / sizeof(arr[0]);
	
	quickSort(arr, 0, size - 1);
	cout << "Sorted array: ";
	printArray(arr, size);
    // Sorted array: 1 2 3 4 5 6 7 8 9 
	
	return 0;
}

```

## Time Complexity for Quick Sort Algorithm

Worst case => O(n<sup>2</sup>)

Average case => O(n*log(n))

Best case => O(n*log(n))

## Summary

In this article, we talked about the quick sort algorithm. 

We gave a brief explanation of how the algorithm works. After that, we saw an example that explained how it works under the hood using visual guides to sort an unordered array.

We also saw how to implement the quick sort algorithm in Java and C++.

Lastly, we listed the quick sort time complexity for worst, average, and best case.

Happy coding! 

