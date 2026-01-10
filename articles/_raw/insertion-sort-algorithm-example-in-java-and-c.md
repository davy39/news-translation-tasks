---
title: Insertion Sort – Algorithm Example in Java and C++
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-02-28T23:44:34.000Z'
originalURL: https://freecodecamp.org/news/insertion-sort-algorithm-example-in-java-and-c
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/insertion-sort-algorithm.png
tags:
- name: algorithms
  slug: algorithms
- name: C++
  slug: c-2
- name: Java
  slug: java
seo_title: null
seo_desc: "Insertion sort is a sorting algorithm that creates a sorted array of items\
  \ from an unsorted array, one item at a time. \nIn this article, we will see how\
  \ the algorithm works and how to apply it in our code.\nHow to Use Insertion Sort\n\
  Consider an array ..."
---

**Insertion sort** is a sorting algorithm that creates a sorted array of items from an unsorted array, one item at a time. 

In this article, we will see how the algorithm works and how to apply it in our code.

## How to Use Insertion Sort

Consider an array of numbers: 7, 3, 10, 4, 1, 11. These numbers are not sorted/organized in any order (ascending or descending). With the insertion sort algorithm, we can sort them from the smallest to the biggest number. 

The original array will be divided into two – the sorted array and the unsorted array. We will then pick numbers from the unsorted array and place them in the right spot. 

When a number is picked from the unsorted array, we begin sorting from the rear part of the sorted array. If the number picked is less than the last number in the sorted array, the last number will be moved to the right and the selected number will takes its position. The iteration continues until the selected number gets to a position where the next number to be compared with is not greater than it. 

This might seem like a lot of information, but you will understand better with an example:

This is our array of numbers: 7, 3, 10, 4, 1, 11

We will split this array into two – the sorted array and the unsorted array. Like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/insertion-sort-sides.png)

By default, we are putting the first number in the sorted section because we will start our comparison with it.

So, how do we sort this array? 

The first number in the unsorted array is 3, so it becomes the selected number. When we move 3 to the sorted array, the number there is 7. Since 7 is greater than 3, it will be moved to the right and then 3 will take its position.

The array will now look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/insertion-sort-1.png)

For 10, we start our comparison with the sorted array from the rear and the first number from the rear is 7. Since 7 is less than 10, there is no need for a position shift so 10 would stay directly after 7. 

Now have a look at the current position of the numbers on each side:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/insertion-sort-2.png)

You might be a bit confused as to how these numbers change their position when they move over the sorted area. Let's demonstrate that with the next example.

The next number to be sorted is 4.

Here is what our sorted array looks like at the moment: 3, 7, 10.

Now the current number to be sorted is 4. So starting from rear again, we compare 4 and 10. 10 is greater than 4 so it moves one space to the right and creates an empty space for four. Something like this: 3, 7, ?, 10.

The question mark is the space created. But we cannot insert 4 just yet; we have to compare it with the next number which is 7. Another space will be created because 7 is greater than 4 and our array will look like this: 3, ?, 7, 10.

The next number is 3. We have gotten to the point where the number being compared is less than the current number we picked from the unsorted array. Since 3 is less than 4, 4 will be inserted into the last space created. Our sorted array will now look like this: 3, 4, 7, 10. 

For 1, if you have understood the last example then it should be easy to work it out. You should try sorting and inserting the last two numbers on your own. 

As a reminder, if the current number from the unsorted array is less than any number it is being compared with in the sorted array, the one in the sorted array will move to the right and create an empty space on its previous position to insert the current number. 

This will continue until the current number gets to a position where it is greater than the number it is being compared with. At this point, you insert the current number into the last created space. 

When you are done, the array will look like this: 1, 3, 4, 7, 10, 11.

Let's see some code examples!

## Insertion Sort Example in Java

If we want to do this with code, here's what that would look like:

```java
public class InsertionSort {
	
	void sortArray(int arr[])
	{
		int n = arr.length;
		for (int i = 1; i < n; i++) {
			int current = arr[i];
			int j = i - 1;
            
			while (j >= 0 && arr[j] > current) {
				arr[j + 1] = arr[j];
				j = j - 1;
			}
			arr[j + 1] = current;
		}
	}

	static void printArray(int arr[])
	{
		int n = arr.length;
		for (int i = 0; i < n; i++)
			System.out.print(arr[i] + " ");

		System.out.println();
	}

	public static void main(String args[])
	{
		int arr[] = { 7, 3, 10, 4, 1, 11 };

		InsertionSort arrayOfNumbers = new InsertionSort();
		arrayOfNumbers.sortArray(arr);

		printArray(arr);
        
        // prints 1 3 4 7 10 11
	}
} 

```

Let's break the code down.

```java
void sortArray(int arr[])
	{
		int n = arr.length;
		for (int i = 1; i < n; i++) {
			int current = arr[i];
			int j = i - 1;
            
			while (j >= 0 && arr[j] > current) {
				arr[j + 1] = arr[j];
				j = j - 1;
			}
			arr[j + 1] = current;
		}
	}
```

Above, we created a function for sorting an array. It takes in an array data type as an argument. We then stored the array length in a variable called `n`. 

In our loop, you might notice that the `i` variable is 1. You might be used to seeing that as 0 in loops. It is 1 here because we are starting our sorting from the second value in the array.

The `current` variable is the current value being sorted. The `j` is used to shift the position of the `current` variable towards the left by decreasing its value. 

The while loop that follows helps us check when to stop decreasing the `current` variable's position through the conditions provided. 

When these conditions are met, the current value is inserted into the right spot. This is the same as the example we saw in the last section.

```java
static void printArray(int arr[])
	{
		int n = arr.length;
		for (int i = 0; i < n; i++)
			System.out.print(arr[i] + " ");

		System.out.println();
	}
```

The code above is just a function for printing the values of our array.

```
public static void main(String args[])
	{
		int arr[] = { 7, 3, 10, 4, 1, 11 };

		InsertionSort arrayOfNumbers = new InsertionSort();
		arrayOfNumbers.sortArray(arr);

		printArray(arr);
        
        // prints 1 3 4 7 10 11
	}
```

Now we have used it to sort our array, and then we printed the value using the function we had already created.

## Insertion Sort Example in C++

```c++
#include <bits/stdc++.h>
using namespace std;

void insertionSort(int arr[], int n)
{
	int i, current, j;
	for (i = 1; i < n; i++)
	{
		current = arr[i];
		j = i - 1;

		while (j >= 0 && arr[j] > current)
		{
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = current;
	}
}

void printArray(int arr[], int n)
{
	int i;
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
	cout << endl;
}

int main()
{
	int arrayOfNumbers[] = { 7, 3, 10, 4, 1, 11 };
	int n = sizeof(arrayOfNumbers) / sizeof(arrayOfNumbers[0]);

	insertionSort(arrayOfNumbers, n);
	printArray(arrayOfNumbers, n); // 1 3 4 7 10 11 

	return 0;
}


```

This code is identical to the one we used in the last section. The only difference is that we have written it in this section with C++. So you can have a look at the explanation given in the last section to understand better.

## Conclusion

In this article, we learned how the insertion sort algorithm works with some examples and how to apply it in our Java and C++ code.

Happy coding!

