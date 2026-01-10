---
title: How to Use Arrays.binarySearch() in Java
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-08-23T15:31:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-arrays-binarysearch-in-java
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/binarysearch-arrays-java.png
tags:
- name: arrays
  slug: arrays
- name: Java
  slug: java
seo_title: null
seo_desc: "In this article, I'm going to show you how to use the Arrays.binarySearch()\
  \ method in Java.\nWhat is Arrays.binarySearch() in Java?\n According to the official\
  \ docs on the Arrays.binarySearch() method:\n\n(It) Searches the specified array\
  \ of bytes for th..."
---

In this article, I'm going to show you how to use the `Arrays.binarySearch()` method in Java.

## What is `Arrays.binarySearch()` in Java?

 According to the [official docs](https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html#binarySearch(byte[],%20byte)) on the `Arrays.binarySearch()` method:

> (It) Searches the specified array of bytes for the specified value using the binary search algorithm.   
>   
> The array must be sorted (as by the [`sort(byte[])`](https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html#sort(byte[])) method) prior to making this call. If it is not sorted, the results are undefined.   
>   
> If the array contains multiple elements with the specified value, there is no guarantee which one will be found.

Simply put, the `Arrays.binarySearch()` method can look for a given element in a sorted array and return its index if found.

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		char vowels[] = {'a', 'e', 'i', 'o', 'u'};
		
		char key = 'i';
		
		int foundItemIndex = Arrays.binarySearch(vowels, key);
		
		System.out.println("The given vowel is at index: " + foundItemIndex);

	}
}

```

The `Arrays.binarySearch()` method takes the array you want to search as the first argument and the key you're looking for as the second argument. The output from this program will be:

```
The given vowel is at index: 2
```

Remember, the method returns the index of the found item and not the item itself. So you can store the index in an integer like the one used in this example.

By default, the method uses the first index of the array as the starting point for the search and the length of the array as the ending point of the search. So in this case, the starting index is `0` and the ending index is `6`.

Instead of using the default starting and ending indices, you can define them yourself. For example, if you want to perform the search from index `2` to index `4`, you can do so as follows:

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		char vowels[] = {'a', 'e', 'i', 'o', 'u'};
		
		char key = 'i';
		int startIndex = 2;
		int endIndex = 4;
		
		int foundItemIndex = Arrays.binarySearch(vowels, startIndex, endIndex, key);
		
		System.out.println("The given vowel is at index: " + foundItemIndex);

	}
}

```

In this case, the `Arrays.binarySearch()` method takes the array you want to search as the first argument, the starting index as the second argument, the ending index as the third argument, and the key as the fourth argument.

As long as you keep the ending index within the length of the array, the method should work fine. If you exceed that, however, you'll get the `Array index out of range` exception.

This is simple right? The method returns the index of the element if found. But what happens if it doesn't find the given element?

## What Happens When `Arrays.binarySearch()` Doesn't Find the Given Element?

Once again according to the [official docs](https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html#binarySearch(byte[],%20byte)) on the `Arrays.binarySearch()` method:

> (The method returns the) index of the search key, if it is contained in the array within the specified range; otherwise, `(-(_insertion point_) - 1)`.   
>   
> The _insertion point_ is defined as the point at which the key would be inserted into the array: the index of the first element in the range greater than the key, or `toIndex` (ending index) if all elements in the range are less than the specified key.   
>   
> Note that this guarantees that the return value will be >= 0 if and only if the key is found.

Not very clear right? Let me explain. The first line states that the method will return the index of the search key if found in the array.

But if not found, the output will be equal to the value of `(-(_insertion point_) - 1)`. Here, based on the search key, the `insertion point` can have different values.

Assume we have an array `[5, 6, 7, 8, 9, 10]` and a search key `0` which is clearly not in the array. In this case, the search key is smaller than all the elements of the array. But the first element that is larger than the search key is `5`. So in this case the `insertion point` will be:

```
(-(the index of the first element larger than the search key) - 1) = (0 - 1) = -1
```

You can implement this into a code snippet as follows:

```java
package arrays;

import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		int numbers[] = {5, 6, 7, 8, 9, 10};
		
		System.out.println(Arrays.binarySearch(numbers, 0)); // -1
	}
}

```

Again assume we have an array `[5, 6, 7, 8, 9, 10]` and a search key `12` which is clearly not in the array. In this case, the search key is larger than all the elements of the array. So in this case the `insertion point` will be:

```
(-(the ending index (-(6) - 1) = (-6 - 1) = -7
```

Remember, when you don't define an ending index manually, the method uses the length of the array as the ending index which in this case is `6`.

You can implement this into a code snippet as follows:

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {		
		int numbers[] = {5, 6, 7, 8, 9, 10};
		
		System.out.println(Arrays.binarySearch(numbers, 12)); // -7
	}
}

```

However, the results will change if you define the starting and ending indices manually as follows:

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		int numbers[] = {5, 6, 7, 8, 9, 10};
		
		int startIndex = 1;
		int endIndex = 3;
		
		System.out.println(Arrays.binarySearch(numbers, startIndex, endIndex, 5)); // -2
		System.out.println(Arrays.binarySearch(numbers, startIndex, endIndex, 10)); // -4

	}
}

```

Try calculating the values by yourself. You can also use the `Arrays.binarySearch()` method with characters like this:

```java
import java.util.Arrays;

public class Main {

	public static void main(String[] args) {
		char vowels[] = {'a', 'e', 'i', 'o', 'u'};
		
		char key = 'i';
		int startIndex = 2;
		int endIndex = 4;
		
		System.out.println(Arrays.binarySearch(vowels, startIndex, endIndex, key));

	}
}

```

The same principles apply in this case when the given search key is not found. But when comparing between a character in the array and a given search key, the [ASCII code](https://www.ascii-code.com/) of the corresponding character will be used. So `A (65)` will be smaller than `a (97)`. Keep this in mind when cross checking outputs from your program.

## Wrapping Up

That was pretty much it for this one. I hope you now understand how to use the `Arrays.binarySearch()` method. 

If you have any questions or just want to communicate with me, I'm on [Twitter](https://twitter.com/frhnhsin) and [LinkedIn](https://www.linkedin.com/in/farhanhasin/). Hit me up with direct messages.

