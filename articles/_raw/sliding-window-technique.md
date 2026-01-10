---
title: How to Use the Sliding Window Technique – Algorithm Example and Solution
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2024-01-11T15:11:48.000Z'
originalURL: https://freecodecamp.org/news/sliding-window-technique
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Sliding-Window-Technique---Banner.png
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
seo_title: null
seo_desc: "Recently, I was practicing coding problems that focused on Data Structures\
  \ and Algorithms in preparation for a job change. \nDuring this process, I came\
  \ across the Sliding Window technique. I found this algorithm to be very interesting,\
  \ so I wanted to..."
---

Recently, I was practicing coding problems that focused on Data Structures and Algorithms in preparation for a job change. 

During this process, I came across the Sliding Window technique. I found this algorithm to be very interesting, so I wanted to share my learnings with the community. 

This tutorial will be useful for you if you're preparing for competitive programming interviews. So, let's get started. 

## What is the Sliding Window Technique?

The sliding window technique is an algorithmic approach used in computer science and signal processing. It involves selecting a fixed-size subset, or "window," from a larger dataset and moving this window through the dataset in a step-wise fashion. 

The window slides over the data, typically one element at a time, and performs some operation on the elements within the window at each step. 

Are you confused? Let me elaborate on this technique with an example. 

### Sliding Window example

Assume you're practicing for competitive programming and you encounter the following problem:

"Find the maximum sum of sub-array of size k with the time complexity of O(N).

Array = [1, 2, 6, 2, 4, 1], k = 3"

If you're not familiar with the concept of time complexity, here's a quick definition:

> In theoretical computer science, the time complexity is the computational complexity that describes the amount of computer time it takes to run an algorithm.

And [here's a course](https://www.freecodecamp.org/news/learn-big-o-notation/) if you'd like to learn more.

Back to our problem. Basically, we have to find the sub-array of size 3, whose sum is the maximum (largest number). Here's a pictorial view of how we can go about solving this:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-27.png)
_Find sum of sub-array of size k_

#### Manual solution

Let's solve it manually. From the above image, let's find the sum of each of the sub-arrays of size 3. 

* Sum of 1st sub-array = 1 + 2 + 6 = 9
* Sum of 2nd sub-array = 2 + 6 + 2 = 10
* Sum of 3rd sub-array = 6 + 2 + 4 = 12
* Sum of 4th sub-array = 2 + 4 + 1 = 7

The maximum (biggest) number among 9, 10, 12, and 7 is 12 – or the 3rd sub-array. That is our solution. 

#### Code solution

Alright, let's wear our programming shoes and try to solve this using code. 

Here's my solution to the problem:

<script src="https://gist.github.com/5minslearn/c4867d2750d89f81c8d72cc8bbacf700.js"></script>

Here's a quick walk through of the above code. 

I'm defining the input array and window size at the bottom, and calling the method `findMaxSumOfSequence` with these parameters. 

Initially I'm doing a validation if the input array size is more than the window size, else the calculation is not possible, so return null. 

I'm assuming the maximum sum to be negative infinity. 

I iterate over the array, and for each item in the array, I iterate for next `k` items, find their sum, and assign the current window sum to maximum sum variable if the current window sum is more than existing maximum sum. Finally, return the maximum sum. 

Let's try to run the code. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-26.png)
_Find maximum sum of a sub-array of size k_

Here we go. We got the right answer. 

But, the problem does not stop here. If you look at the problem carefully, we have to find the solution in O(N) time complexity. 

So, you might wonder what's the time complexity of the above solution. Well, the time complexity of the above solution is O(N*k). This means, we're iterating `k` times for each item in the array (nested for-loop). 

O(N) time complexity basically describes that you have to find the maximum value by iterating over the given array only once. 

#### Using the Sliding Window technique

How do we solve this with one iteration? Here's where sliding window technique comes into play. Let's take a look at the pictorial representation of our solution once again:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-27.png)
_Sliding window technique_

Here, you may notice that the window slides over the array. It's initially covering the indices 0, 1, and 2 in the 1st sub-array. For the next sub-array, it slides one-position to the right, eliminating 0th index to the left and adding the 3rd index to the right. So, now it covers the 1, 2, and 3 in the 2nd sub-array...and so on. 

The calculation goes this way for the sub-arrays:

* 1st sub-array = 1 + 2 + 6 = 9
* 2nd sub-array = 9 (sum of 1st sub-array) - 1 + 2 = 10

Let's take a look at this carefully. We find the sum of 1st sub-array to be 9. To calculate the sum of 2nd sub-array, we subtract the number that's going out (1 at 0th index) and add the number that's coming in (2 at 3rd index). 

* 3rd sub-array = 10 (sum of 2nd sub-array) - 2 + 4 = 12
* 4th sub-array = 12 (sum of 3rd sub-array) - 6 + 1 = 7

This is the sliding window technique. Following this technique, we'll able to find the sum of maximum sub-array in a single iteration. 

#### How to implement Sliding Window in code

Alright, let's put on our coding shoes again and try to implement this. 

<script src="https://gist.github.com/5minslearn/f5fb22bec4cba7e39403bc59b55c8d44.js"></script>

Let's try to understand the above code. I made some changes to the `findMaxSumOfSequence` method. I introduced `start` and `end` variables which describe the window block. 

In this implementation, we have 2 loops but they're not nested. This is because, in the first loop, we have to find the sum of the 1st window. The second loop will subtract and add items from the result of the first loop. 

From the above example, the first loop will iterate over the first k items (3) which are 1, 2, and 6. I calculate the sum and store them in the `maxSum` and `windowSum` variables. 

In the next loop, I'm iterating over each item in the array. For each item, I'm subtracting the previous number and adding the next number, and updating the result in the `windowSum` variable. I compare the `windowSum` and `maxSum` variables and update the `maxSum` variable if the `windowSum` is larger. Then I move the window to the next sub-array by incrementing the `start` and `end` variables. Finally, I return the maximum sum. 

Here's the output of the above code:

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-32.png)
_Find maximum sum of a sub-array of size k using sliding window technique_

With this implementation, we have satisfied the problem's requirement by iterating over the array only once and finding the maximum sum of a sub-array (with O(N) time complexity). 

## Applications of the Sliding Window Technique

The Sliding Window Technique is versatile and finds applications in various domains. 

**Array and String Manipulation**: In array or string processing, a sliding window can be used to efficiently perform operations such as finding subarrays or substrings that satisfy certain conditions.

**Data Compression**: Sliding window compression algorithms, like LZ77 and its variants, use a window to find repeated patterns in the input data and replace them with references to previous occurrences.

**Image Processing**: In image processing, a sliding window can be employed for tasks such as feature extraction, object detection, or image segmentation.

**Signal Processing**: Time-series data can be analyzed using a sliding window to capture local patterns, trends, or anomalies.

**Network Protocols**: Sliding window protocols are used in computer networks for reliable and efficient data transmission. The sender and receiver maintain a window of allowable sequence numbers to manage the flow of data. 

## Conclusion

Hope you now have a clear idea of how the Sliding Window Technique works after seeing these examples. I would recommend that you try to solve some other problems with this technique to get familiar with it. Trying to find the minimum sum of the sub-array of size k on your own using this technique would be a helpful exercise.

As I mentioned earlier, I'm actively looking to switch my job. If you have a good position available in your organization, please refer [me](https://arunachalam-b.github.io/). 

Hope you enjoyed reading this article. If you wish to learn more about techniques to crack competitive programming interviews, subscribe to my newsletter by visiting my [site](https://5minslearn.gogosoon.com/?ref=fcc_sliding_window_technique) which also has a consolidated list of all my blogs. 


