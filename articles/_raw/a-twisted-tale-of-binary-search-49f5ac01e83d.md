---
title: A twisted tale of Binary Search
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-04T00:33:07.000Z'
originalURL: https://freecodecamp.org/news/a-twisted-tale-of-binary-search-49f5ac01e83d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DClFFS2kX-MPvGuHYvOyTw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Divya Godayal

  Awesome. That’s how I feel right now. Writing my first solo tech article.

  I must say I have a lot to share with you guys, and have a lot more to learn as
  well. So without any further ado, lets get to it. And yes, hold on tight — ‘cau...'
---

By Divya Godayal

Awesome. That’s how I feel right now. Writing my first solo tech article.

I must say I have a lot to share with you guys, and have a lot more to learn as well. So without any further ado, lets get to it. And yes, hold on tight — ‘cause there is a twist in the tale. ?

### Binary Search

All of us have heard of the classic [2 Eggs and 100 Stories](https://www.geeksforgeeks.org/puzzle-set-35-2-eggs-and-100-floors/) problem. I have something similar for you.

You have a 100 story building with a rule:

`**People with pets can only occupy top floors**`

Your friend wishes to buy an apartment in this building. She is too scared of pets to live near them, but you love them. She asked if you can help her find out where exactly the pet friendly floors start. She wants to explore all of the different options available, and so you need to find out which floors starting from the ground up are the ones that don’t allow pets.

The building management folks are on a holiday. On every floor, there is a sign board next to the elevator telling you if the floor is pet friendly or not. But you are too lazy to stop at every floor to check the pet sign board since the lift is so slow.

What do you do?

![Image](https://cdn-media-1.freecodecamp.org/images/1*mVvYhywAIoa11tCRfsHPQA.png)
_The two possible sign boards. #GoRed is what your friend roots for._

The lift takes almost a minute at every floor to stop and then start again. Yes that’s how bad it is. But between the floors, navigation is pretty smooth. You have to get this done quickly.

How do you go about it ?

### Iterative approach

One naïve approach to this would be to start at the very bottom of the building (the ground floor) and keep stopping the lift at every single floor to check the sign that floor has posted. You stop when you find the pet friendly sign.

**Best case** is that the ground floor has the pet sign. Meaning the entire building has pets. No way your friend would buy an apartment here.

**Average case** is that you go to the 50th floor, stopping at every floor in between, and finally find a pet sign board. So your friend can buy one from 1–49.

**Worst case** scenario would be you reaching the 100th floor, stopping at every floor on the way up, only to find out that there are no pet sign boards in the entire building. So your friend can buy any apartment from 1–100, but who cares, it took you almost two hours to find that out. ? ?.

Algorithmically, given an array of 100 boolean values, the index of the array represents building floors and a 0 represents a floor where no pets are allowed while a 1 represents a floor where pets would be allowed. From the rule of the building, the array would be of the form

```
000... 1111...
```

that is, all 0s followed by all 1s, because only the top floors can be the ones where pets are allowed.

Given this array, we need to find the first index where there is a `1` . A linear search algorithm for this problem would be as simple as iterating over the array and looking for a `1` and returning when we find one.

As expected, the complexity of this algorithm would be `O(n)` where n = 100 for our specific building example. You need to come up with something faster than this. Stopping at every floor is not feasible, as it would take you a lot of time to cover the entire building in the worst case.

### Binary Search Approach

Let’s say you start from ground floor and got to the 50th floor with no stops. At the 50th floor, you stopped and got out of the lift and checked for the sign. The board sign said `“No Pets”`. This would mean that, until the 50th floor, there are definitely no pets.

So now knowing that you reduce your search space to the other half, which is floors 51–100. This means that with a single stop, you were able to cover half of the building knowing for sure that the first half doesn’t have any pets. That’s amazing!

Moving on, you again divide your remaining set of floors into half and take the lift and go directly to the 75th floor. And you see a `“Pets”` sign board there. This means the floor where it started showing up must be between 50–75. You can keep following a similar approach of diving the remaining floors into half and checking until you find the first floor with the `“Pets”` sign board.

You see, every time you make a decision, you divide your search space into two halves and go ahead with one half of the search space. That’s how we narrow down our search. Since we always divide the search space in two and choose one over the other, that is why this type of search strategy is called a `Binary` search strategy.

Isn’t that way faster?

Let’s look into the algorithm for this.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5xqxb4gs88vQGaK8CCp47w.png)
_Binary Search Algorithm_

If you’ve been following along closely and have a grasp of the algorithm, you would have realized a hard and fast condition for the binary search algorithm to work. The condition is that the array needs to be sorted beforehand. In our example, the building floors were sorted from 1–100 and we could easily divide the search space in two.

Let’s look at an example array which is sorted and try and search for an element in it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sCdkKU8RqA6_R3uiy4nL2w.png)

In the above example, the element to be searched is 8. The given array is a sorted array in increasing order. Once we find the middle element (which is 5), we see that the element to be searched is greater than the current index element. Since the array is sorted in increasing order, 8 would lie on the right of the array and can never be on the left side.

So we ignore the elements to the left of 5 and continue our search with the remaining elements, eventually finding out 8.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S2lDovD5HeUsdSHm3NM4Sw.png)

On the other hand, what if the array is not sorted? Even though we know the current element is 5 and we know we need to search for 8, we are not sure which direction is the right way to go. If we end up thinking the array is sorted and apply binary search and go to the right part, we will never find 8.

**So binary search essentially wants your array to be sorted.**

That was the standard binary search algorithm that we just looked at. But, as the title of the article suggests, there is a twist in the tale!

I am an avid competitive programmer, and there was an interesting variant of the binary search algorithm in the [CodeChef May Long Challenge](https://www.codechef.com/MAY18B/problems/FAKEBS).

Essentially, the Chef wrote the classic binary search, assuming the input array would be sorted. All the other children in the class copied the code from him, as Chef is the best programmer in the class. His assumption could’ve cost the entire class their assignment marks, as the input array was not sorted beforehand.

The only thing the Chef can do is to preprocess the array by swapping some pair of numbers here and there so that the binary search procedure still returns the right index.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MOupjMd8PLQIkCoXHPIkHw.png)

**Note:** The preprocessor above should ideally return the modified array for the binary search to work correctly. However, as the problem statement asks, we are just trying to determine the number of swaps needed for binary search to work correctly on the unsorted array given an input. The algorithm would also return a -1 if such a modification is not possible for the given array and element.

The idea here is very simple.

We need to understand two basic steps. I call them the **TI-ME** steps. Perhaps that’ll help you remember what we are doing here.

a. **T**arget **I**ndex: The index of the element to be searched for. We need to know this, since this index would help us drive the modifications. Because every time we modify any element, we need to sail towards this index and not away from it.

b. **M**iddle **E**lement: If you look clearly in a binary search, it’s the middle element of the current search space which drives the next move. If this middle element takes us in the wrong direction, we need to replace with the appropriate element.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xgnYQLeH-9l2MVU_OqTNLQ.png)
_We are searching for 8 in the above unsorted array. We already saw in the examples above a normal binary search would fail for an unsorted array._

![Image](https://cdn-media-1.freecodecamp.org/images/1*sJNU_8PdNlbIuy7RStVHdA.png)
_Mid elements give direction to binary search. Middle element 5 would take binary search to go right. This way we would never find `8. If we swap 5 with an element greater than 8 we would force the search to go to left.`_

So, the whole idea here is that we swap all the middle elements which are wrongly placed.

The binary search algorithm (the value of the middle element with respect to the element to be searched, that is, X) can either take us towards the left half of the array or the right half. So, there are two possibilities for a wrongly placed middle element:

1. The element to be searched was on the right of the middle element, but since `Element[Mid] > Element[Target Ind`ex] , the binary search would have had to ignore the right half and move towards the left half. OR
2. The element to be searched was on the left of the middle element, but since `Element[Mid] < Element[Target Ind`ex] , the binary search would have had to ignore the left half and move towards the right half.

Therefore, if a middle element is wrongly placed such that a number `X` was needed in its place where `X < Element[Target Ind`ex] , then we maintain a counter for that and call `it count_low_nee`ded .

Similarly, if a middle element is wrongly placed such that a number `X` was needed in its place where `X > Element[Target Ind`ex] , then we maintain a counter for that and call `it count_high_nee`ded .

Also, if we simply run the binary search algorithm over the given array while searching for numbers, there would be some numbers that would be correctly placed. These would be the middle elements that drove the binary search in correct directions corresponding to the given element `X` (the element to be searched). These numbers cannot be a part of the swapping, because they are rightly positioned with respect to `X` .

Let’s look at the pseudo code for this algorithm first and then go through an example.

```
function can_preprocess(arr, X){     low = 0     high= 0
```

```
while X is not found {          mid = (low + high) / 2          if arr[mid] == X {             break                     }
```

```
correctly_placed_low = 0          correctly_placed_high = 0          count_low_needed = 0          count_high_needed = 0
```

```
if `mid` suggests we should go right for X {               if X is actually on the right {                   correctly_placed_low ++               }               else {                   count_low_needed ++               }          } else {               if X is actually on the left {                  correctly_placed_high ++               }                else {                  count_high_needed ++               }          }
```

```
modify low and high according to           where `X` actually is with respect to `mid`
```

```
}
```

```
// Total smaller numbers available for swapping     TSM = sorted_index[X] - correctly_placed_low
```

```
// Total Larger numbers available for swapping     TLM = (N - sorted_index[X]) - correctly_placed_high
```

```
if count_low_needed > TSM or count_high_needed > TLM {          return -1     }
```

```
return max(count_low_needed, count_high_needed)
```

**NOTE:** The problem statement fixes the input array for us and repeatedly passes values to be searched in the input array. So, we can iterate once over the original array to know the actual location of the element to be searched (create a dictionary, essentially).

Also, we need `sorted_index[X]` to tell us how many values are lesser than or greater than the element `X` in our array. We can sort the array and create another dictionary storing location of each element in the sorted array.

Let’s go through the steps of the proposed algorithm while dry running an example.

1. Given an unsorted array, you need to search for `X = 4` .  
Hence our target index is 7.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3vnVPsJgCPjLLmWENiB8rQ.png)

2. Mid element index < Target Index, so we need to maneuver our search to the right half. B`ut Element[Mid] > Element[Target` Index], `hence count_low_need`ed = 1

![Image](https://cdn-media-1.freecodecamp.org/images/1*goOz9sCtElJn8_GVf86n-Q.png)

3. Mid element index < Target Index, so we still need to maneuver our search to the right half. Once agai`n, Element[Mid] > Element[Target` Index], `hence count_low_need`ed = 2

![Image](https://cdn-media-1.freecodecamp.org/images/1*RuHR_k66dh-G0KzI-6DRuQ.png)

4. The total number of swaps needed for binary search to return the correct index here would be two swaps with elements lower than 4. We have smaller numbers `1, 3 or 2` for swapping available, so we can successfully do the swapping for this array so that binary search correctly finds out `4` .

Below is the Python code for the given problem. Every step is explained in the comments.

The time complexity of this Twisted Binary Search algorithm is still `O(nlogn)` .

I hope you were able to grasp the inner workings of the binary search algorithm and had fun while going through this interesting problem as well. If you found this post useful, spread the love and share as much as possible. ?

