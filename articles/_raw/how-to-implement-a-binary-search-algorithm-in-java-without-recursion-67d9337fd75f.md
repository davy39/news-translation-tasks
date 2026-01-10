---
title: How to implement a Binary Search Algorithm in Java without recursion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-21T22:30:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-a-binary-search-algorithm-in-java-without-recursion-67d9337fd75f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pFQO8pwHj6QwYaQewgKM0Q.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By javinpaul

  An Iterative implementation of the popular binary search algorithm to find an element
  in a sorted array.


  Hello everyone! I have published a lot of algorithms and data structure articles
  on my blog, but this one is the first one here. In...'
---

By javinpaul

#### An Iterative implementation of the popular binary search algorithm to find an element in a sorted array.

![Image](https://cdn-media-1.freecodecamp.org/images/Tfy1QANC2jqqQyLtL2XjiPLc80XxVlCEOP5V)

Hello everyone! I have published a lot of algorithms and data structure articles on my blog, but this one is the first one here. In this article, we’ll examine popular [fundamental algorithms for interviews](http://www.java67.com/2018/06/data-structure-and-algorithm-interview-questions-programmers.html).

Yes, you guessed it right: you need to implement a **binary search** in Java, and you need to write both iterative and recursive binary search algorithms.

In computer science, a binary search, or half-interval search, is a **divide and conquer algorithm** that locates the position of an item in a [sorted array](http://www.java67.com/2014/12/how-to-find-missing-number-in-sorted.html). Binary searching works by comparing an input value to the middle element of the array.

The comparison determines whether the element equals the input, is less than the input, or is greater than the input.

When the element being compared equals the input, the search stops and typically returns the position of the element.

If the element is not equal to the input, then a comparison is made to determine whether the input is less than or greater than the element.

Depending on the result, the [algorithm](https://javarevisited.blogspot.com/2018/11/top-5-data-structures-and-algorithm-online-courses.html#axzz5YFaOvjsh) then starts over again, but only searching the top or a bottom subset of the array’s elements.

If the input is not located within the [array](https://javarevisited.blogspot.com/2015/06/3-ways-to-find-duplicate-elements-in-array-java.html), the algorithm will usually output a unique value indicating this like -1 or just throw a [RuntimeException](http://www.java67.com/2012/12/difference-between-runtimeexception-and-checked-exception.html) in Java like NoValueFoundException.

Binary search algorithms typically halve the number of items to check with each successive iteration, thus locating the given item (or determining its absence) in logarithmic time.

Btw, if you are not familiar with fundamental search and sort algorithms, then you can also join a course like [**Data Structures and Algorithms: Deep Dive Using Java**](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fdata-structures-and-algorithms-deep-dive-using-java%2F) to learn fundamental algorithms.

![Image](https://cdn-media-1.freecodecamp.org/images/Zt9Z-B2aXoNxNBMlPUPF5lsJlenEMLYCpqlz)

If Java is not your choice of language, you can find more recommendations for JavaScript and Python in this [list of algorithms courses](https://javarevisited.blogspot.com/2018/11/top-5-data-structures-and-algorithm-online-courses.html#axzz5YFaOvjsh).

Btw, if you prefer books, I suggest you read a comprehensive algorithm book like [**Introduction to Algorithms**](http://www.amazon.com/dp/0072970545/?tag=javamysqlanta-20) by Thomas H. Cormen.

![Image](https://cdn-media-1.freecodecamp.org/images/EXhvYsB0TaNmtUXJgxwRhdAZjhruvJKSMHjD)

Here is some sample code which shows the logic of **iterative binary search in Java**:

![Image](https://cdn-media-1.freecodecamp.org/images/EXXBjdY30v3FxQ1Ug5nPzJPt0sPxlw9ZOBFt)

### Binary Search Implementation in Java

Here is a sample program to implement binary search in Java. The algorithm is implemented recursively. Also, an interesting fact to know about binary search implementation in Java is that Joshua Bloch, author of the famous [Effective Java](https://www.amazon.com/Effective-Java-3rd-Joshua-Bloch/dp/0134685997/?tag=javamysqlanta-20) book, wrote the binary search in “java.util.Arrays”.

```
import java.util.Arrays;import java.util.Scanner;
```

```
/** * Java program to implement Binary Search. We have implemented Iterative* version of Binary Search Algorithm in Java** @author Javin Paul*/
```

```
public class IterativeBinarySearch {
```

```
  public static void main(String args[]) {    int[] list = new int[]{23, 43, 31, 12};    int number = 12;    Arrays.sort(list);    System.out.printf("Binary Search %d in integer array %s %n", number, Arrays.toString(list));
```

```
    binarySearch(list, 12);    System.out.printf("Binary Search %d in integer array %s %n", 43, Arrays.toString(list));
```

```
    binarySearch(list, 43);    list = new int[]{123, 243, 331, 1298};    number = 331;    Arrays.sort(list);    System.out.printf("Binary Search %d in integer array %s %n", number,    Arrays.toString(list));
```

```
    binarySearch(list, 331);    System.out.printf("Binary Search %d in integer array %s %n",   331, Arrays.toString(list));    binarySearch(list, 1333);
```

```
   // Using Core Java API and Collection framework   // Precondition to the Arrays.binarySearch   Arrays.sort(list);
```

```
   // Search an element   int index = Arrays.binarySearch(list, 3);
```

```
}
```

```
/** * Perform a binary Search in Sorted Array in Java * @param input * @param number * @return location of element in array */
```

```
public static void binarySearch(int[] input, int number) {int first = 0;int last = input.length - 1;int middle = (first + last) / 2;
```

```
while (first <= last) {  if (input[middle] < number) {  first = middle + 1;} else if (input[middle] == number) {
```

```
System.out.printf(number + " found at location %d %n", middle);break;} else {  last = middle - 1;}
```

```
middle = (first + last) / 2;
```

```
}
```

```
if (first > last) {  System.out.println(number + " is not present in the list.\n");}
```

```
}
```

```
}
```

```
OutputBinary Search 12 in integer array [12, 23, 31, 43]12 found at location 0Binary Search 43 in integer array [12, 23, 31, 43]43 found at location 3Binary Search 331 in integer array [123, 243, 331, 1298]331 found at location 2Binary Search 331 in integer array [123, 243, 331, 1298]1333 is not present in the list.
```

That’s all about **how to implement binary search using recursion in Java**. Along with Linear search, these are two of the essential search algorithms you learn in your computer science class.

The binary search tree data structure takes advantage of this algorithm and arranges data in a hierarchical structure so that you can search any node in O(logN) time.

Though, you must remember that in order to use binary search, you need a sorted list or array, so you also need to consider the cost of sorting when you consider using binary search algorithm in the real world.  
   
 **Further Learning**  
 [Data Structures and Algorithms: Deep Dive Using Java](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fdata-structures-and-algorithms-deep-dive-using-java%2F)  
 [Algorithms and Data Structures — Part 1 and 2](https://pluralsight.pxf.io/c/1193463/424552/7490?u=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fads-part1)   
 [Data Structures in Java 9 by Heinz Kabutz](https://learning.javaspecialists.eu/courses/data-structures?affcode=92815_johrd7r8)  
[10 Algorithms books for Interviews](http://www.java67.com/2015/09/top-10-algorithm-books-every-programmer-read-learn.html)  
[10 Data Structure and Algorithm Courses for Interviews](https://hackernoon.com/10-data-structure-algorithms-and-programming-courses-to-crack-any-coding-interview-e1c50b30b927)  
[5 Free Courses to Learn Data Structure and Algorithms](https://javarevisited.blogspot.com/2018/01/top-5-free-data-structure-and-algorithm-courses-java--c-programmers.html)

Other **Data Structure and Algorithms tutorials** you may like

* How to implement Quicksort algorithm in place in Java? ([tutorial](http://javarevisited.blogspot.sg/2014/08/quicksort-sorting-algorithm-in-java-in-place-example.html))
* How to implement Binary Search Tree in Java? ([solution](http://javarevisited.blogspot.sg/2015/10/how-to-implement-binary-search-tree-in-java-example.html))
* How to implement Quicksort algorithm without recursion? ([tutorial](http://javarevisited.blogspot.sg/2016/09/iterative-quicksort-example-in-java-without-recursion.html))
* How to implement Insertion sort algorithm in Java? ([tutorial](http://javarevisited.blogspot.sg/2014/12/insertion-sort-algorithm-in-java-to-array-example.html))
* How to implement Bubble sort algorithm in Java? ([tutorial](http://www.java67.com/2012/12/bubble-sort-in-java-program-to-sort-integer-array-example.html))
* What is the difference between Comparison and Non-Comparison based sorting algorithm? ([answer](http://javarevisited.blogspot.sg/2017/02/difference-between-comparison-quicksort-and-non-comparison-counting-sort-algorithms.html))
* How to implement Bucket Sort in Java? ([tutorial](http://javarevisited.blogspot.sg/2017/01/bucket-sort-in-java-with-example.html))
* How to implement a Binary Search Algorithm without recursion in Java? ([tutorial](http://www.java67.com/2016/05/java-program-to-perform-binary-search-without-recursion.html))
* 50+ Data Structure and Algorithms Courses for Programmers ([questions](https://hackernoon.com/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0))

Thanks for reading this article. If you like this article then please share with your friends and colleagues. If you have any suggestion or feedback then please drop a comment.

#### P.S. — If you are serious about improving your Algorithms skills, I think the [Data Structures and Algorithms: Deep Dive Using Java](https://click.linksynergy.com/fs-bin/click?id=JVFxdTr9V80&subid=0&offerid=323058.1&type=10&tmpid=14538&RD_PARM1=https%3A%2F%2Fwww.udemy.com%2Fdata-structures-and-algorithms-deep-dive-using-java%2F) is the best one to start with.

