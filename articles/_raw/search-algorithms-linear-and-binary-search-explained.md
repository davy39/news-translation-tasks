---
title: Search Algorithms – Linear Search and Binary Search Code Implementation and
  Complexity Analysis
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-01-11T17:21:54.000Z'
originalURL: https://freecodecamp.org/news/search-algorithms-linear-and-binary-search-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/searching.png
tags:
- name: algorithms
  slug: algorithms
- name: '#big o notation'
  slug: big-o-notation
- name: binary search
  slug: binary-search
- name: Computer Science
  slug: computer-science
seo_title: null
seo_desc: 'Search algorithms are a fundamental computer science concept that you should
  understand as a developer. They work by using a step-by-step method to locate specific
  data among a collection of data.

  In this article, we''ll learn how search algorithms wo...'
---

**Search algorithms** are a fundamental computer science concept that you should understand as a developer. They work by using a step-by-step method to locate specific data among a collection of data.

In this article, we'll learn how search algorithms work by looking at their implementations in Java and Python.

## What is a Search Algorithm?

According to Wikipedia, a search algorithm is:

> *Any algorithm which solves the search problem, namely, to retrieve information stored within some data structure, or calculated in the search space of a problem domain, either with discrete or continuous values.*

Search algorithms are designed to check or retrieve an element from any data structure where that element is being stored. They search for a target (key) in the search space.

## Types of Search Algorithms

In this post, we are going to discuss two important types of search algorithms:

1. **Linear or Sequential Search**
    
2. **Binary Search**
    

Let's discuss these two in detail with examples, code implementations, and time complexity analysis.

## Linear or Sequential Search

This algorithm works by sequentially iterating through the whole array or list from one end until the target element is found. If the element is found, it returns its index, else -1.

Now let's look at an example and try to understand how it works:

```python
arr = [2, 12, 15, 11, 7, 19, 45]
```

Suppose the target element we want to search is `7`.

### Approach for Linear or Sequential Search

* Start with index 0 and compare each element with the target
    
* If the target is found to be equal to the element, return its index
    
* If the target is not found, return -1
    

### **Code Implementation**

Let's now look at how we'd implement this type of search algorithm in a couple different programming languages.

#### Linear or Sequential Search in Java

```java
package algorithms.searching;

public class LinearSearch {
    public static void main(String[] args) {
        int[] nums = {2, 12, 15, 11, 7, 19, 45};
        int target = 7;
        System.out.println(search(nums, target));

    }

    static int search(int[] nums, int target) {
        for (int index = 0; index < nums.length; index++) {
            if (nums[index] == target) {
                return index;
            }
        }
        return -1;
    }
}
```

#### Linear or Sequential Search in Python

```python
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

if __name__ == '__main__':
    nums = [2, 12, 15, 11, 7, 19, 45]
    target = 7
    print(search(nums, target))
```

### **Time Complexity Analysis**

**The Best Case** occurs when the target element is the first element of the array. The number of comparisons, in this case, is 1. So, the time complexity is `O(1)`.

**The Average Case:** On average, the target element will be somewhere in the middle of the array. The number of comparisons, in this case, will be N/2. So, the time complexity will be `O(N)` (the constant being ignored).

**The Worst Case** occurs when the target element is the last element in the array or not in the array. In this case, we have to traverse the entire array, and so the number of comparisons will be N. So, the time complexity will be `O(N)`.

## Binary Search

This type of searching algorithm is used to find the position of a specific value contained **in a sorted array**. The binary search algorithm works on the principle of divide and conquer and it is considered the best searching algorithm because it's faster to run.

Now let's take a sorted array as an example and try to understand how it works:

```python
arr = [2, 12, 15, 17, 27, 29, 45]
```

Suppose the target element to be searched is `17`.

### **Approach for Binary Search**

* Compare the target element with the middle element of the array.
    
* If the target element is greater than the middle element, then the search continues in the right half.
    
* Else if the target element is less than the middle value, the search continues in the left half.
    
* This process is repeated until the middle element is equal to the target element, or the target element is not in the array
    
* If the target element is found, its index is returned, else -1 is returned.
    

### Code Implementation

#### Binary Search in Java

```java
package algorithms.searching;

public class BinarySearch {
    public static void main(String[] args) {
        int[] nums = {2, 12, 15, 17, 27, 29, 45};
        int target = 17;
        System.out.println(search(nums, target));
    }

    static int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (nums[mid] > target)
                end = mid - 1;
            else if (nums[mid] < target)
                start = mid + 1;
            else
                return mid;
        }
        return -1;
    }
}
```

#### Binary Search in Python

```python
def search(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start + (end-start)//2


        if nums[mid] > target:
            end = mid-1
        elif nums[mid] < target:
            start = mid+1
        else:
            return mid

    return -1


if __name__ == '__main__':
    nums = [2, 12, 15, 17, 27, 29, 45]
    target = 17
    print(search(nums, target))
```

### **Time Complexity Analysis**

**The Best Case** occurs when the target element is the middle element of the array. The number of comparisons, in this case, is 1. So, the time complexity is `O(1)`.

**The Average Case:** On average, the target element will be somewhere in the array. So, the time complexity will be `O(logN)`.

**The Worst Case** occurs when the target element is not in the list or it is away from the middle element. So, the time complexity will be `O(logN)`.

### How to Calculate Time Complexity:

Let's say the iteration in Binary Search terminates after **k** iterations.

At each iteration, the array is divided by half. So let’s say the length of array at any iteration is **N**.

At **Iteration 1,**

```markdown
Length of array = N
```

At **Iteration 2**,

```markdown
Length of array = N/2
```

At **Iteration 3**,

```markdown
Length of array = (N/2)/2 = N/2^2
```

At **Iteration k**,

```markdown
Length of array = N/2^k
```

Also, we know that after k divisions, the **length of the array becomes 1**: Length of array = **N⁄<sub>2</sub><sup>k</sup> = 1**\=&gt; **N = 2<sup>k</sup>**

If we apply a log function on both sides: **log<sub>2</sub> (N) = log<sub>2</sub> (2<sup>k</sup>)**\=&gt; **log<sub>2</sub> (N) = k log<sub>2</sub> (2)**

As **(log<sub>a</sub> (a) = 1)**  
Therefore,=&gt; **k = log<sub>2</sub> (N)**

So now we can see why the time complexity of Binary Search is log<sub>2</sub> (N).

You can also visualize the above two algorithms using the simple tool built by [Dipesh Patil](https://www.linkedin.com/in/dipesh-patil/) - [Algorithms Visualizer](https://dipeshpatil.github.io/algorithms-visualiser/#/searching).

## Order-agnostic Binary Search

Suppose, we have to find a target element in a sorted array. We know that the array is sorted, but we don’t know if it’s sorted in ascending or descending order.

### **Approach for Order-agnostic Binary Search**

The implementation is similar to binary search except that we need to identify whether the array is sorted in ascending order or descending order. This then lets us make the decision about whether to continue the search in the left half of the array or the right half of the array.

* We first compare the target with the middle element
    
* If the array is sorted in ascending order and the target is less than the middle element **OR** the array is sorted in descending order and the target is greater than the middle element, then we continue the search in the lower half of the array by setting `end=mid-1`.
    
* Otherwise, we perform the search in the upper half of the array by setting `start=mid+1`
    

The only thing we need to do is to figure out whether the array is sorted in ascending order or descending order. We can easily find this by comparing the first and last elements of the array.

```markdown
if arr[0] < arr[arr.length-1]
    array is sorted in ascending order 
else
    array is sorted in descending order
```

### **Code Implementation**

#### Order-agnostic Binary Search in Java

```java
package algorithms.searching;

public class OrderAgnosticBinarySearch {
    public static void main(String[] args) {
        int[] nums1 = {-1, 2, 4, 6, 7, 8, 12, 15, 19, 32, 45, 67, 99};
        int[] nums2 = {99, 67, 45, 32, 19, 15, 12, 8, 7, 6, 4, 2, -1};
        int target = -1;
        System.out.println(search(nums1, target));
        System.out.println(search(nums2, target));
    }

    static int search(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;

        boolean isAscending = arr[start] < arr[end];

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (target == arr[mid])
                return mid;

            if (isAscending) {
                if (target < arr[mid]) {
                    end = mid - 1;
                } else {
                    start = mid + 1;
                }
            } else {
                if (target < arr[mid]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
        }
        return -1;
    }


}
```

#### Order-agnostic Binary Search in Python

```python
def search(nums, target):
    start = 0
    end = len(nums)-1

    is_ascending = nums[start] < nums[end]

    while start <= end:
        mid = start + (end-start)//2

        if target == nums[mid]:
            return mid

        if is_ascending:
            if target < nums[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if target < nums[mid]:
                start = mid+1
            else:
                end = mid-1

    return -1


if __name__ == '__main__':
    nums1 = [-1, 2, 4, 6, 7, 8, 12, 15, 19, 32, 45, 67, 99]
    nums2 = [99, 67, 45, 32, 19, 15, 12, 8, 7, 6, 4, 2, -1]
    target = -1
    print(search(nums1, target))
    print(search(nums2, target))
```

### **Time Complexity Analysis**

There will be no change in the time complexity, so it will be the same as Binary Search.

# **Conclusion**

In this article, we discussed two of the most important search algorithms along with their code implementations in Python and Java. We also looked at their time complexity analysis.

Thanks for reading!

[Subscribe to my newsletter](https://newsletter.ashutoshkrris.tk)
