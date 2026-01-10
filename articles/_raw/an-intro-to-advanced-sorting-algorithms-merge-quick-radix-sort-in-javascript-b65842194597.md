---
title: 'An intro to advanced sorting algorithms: merge, quick & radix sort in JS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-19T15:45:45.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-advanced-sorting-algorithms-merge-quick-radix-sort-in-javascript-b65842194597
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BtcGRVPLOjnY5zFrhGX4TQ.gif
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yung L. Leung

  In my previous article, “The Complexity of Simple Algorithms & Data Structures in
  JavaScript,” we discussed simple sorting algorithms (bubble, selection & insertion
  sorts). Here, I go through merge, quick & radix sort, each of which ...'
---

By Yung L. Leung

In my previous article, “[The Complexity of Simple Algorithms & Data Structures in JavaScript](https://medium.freecodecamp.org/the-complexity-of-simple-algorithms-and-data-structures-in-javascript-11e25b29de1e?source=friends_link&sk=994bc3da2b4cc5b78da06cf161dad6a7),” we discussed simple sorting algorithms (bubble, selection & insertion sorts). Here, I go through **merge**, **quick** & **radix sort,** each of which has a significant improvement on **average** **time complexity**, less than **O(n²)**.

Let’s go through each of these in more detail.

### Merge

A **merge sort** separates a list into its individual items. It then sorts them as they are being merged into a growing ordered list.

![Image](https://cdn-media-1.freecodecamp.org/images/l8DC03SRDhOSepFxlfGQLZdNFstJiRVv4ro-)
_[source](https://codepumpkin.com/wp-content/uploads/2017/10/MergeSort_Avg_case.gif" rel="noopener" target="_blank" title=")_

In practice, this would mean continuously slicing an array into single element arrays, before pushing each element into a larger array (the smaller value first). Every stage of pushing elements from 2 smaller arrays into 1 larger array involves determining which element from which array has the smaller value.

The complexity of merge sort is **O((n log n) + 1)**. Remember that Big O notation ([Complexity of Simple Algorithms & Data Structures in JS](https://medium.freecodecamp.org/the-complexity-of-simple-algorithms-and-data-structures-in-javascript-11e25b29de1e?source=friends_link&sk=994bc3da2b4cc5b78da06cf161dad6a7)) is a count of the **number of operations (**O**)** with respect to the **number of elements (**n**)**. So a 4 element list requires 3 splits. **Note**, the list is already ordered for the simplicity of the example.

![Image](https://cdn-media-1.freecodecamp.org/images/4NvlwpDKTdqjvzsLjPGXppr5d1wkuV-DpI5n)
_Splitting a 4 element list._

Merging the 4 arrays requires 6 comparisons.

![Image](https://cdn-media-1.freecodecamp.org/images/-3m3gNldPcs19pC42uSrtnZn6CPZiqSrXnre)
_Once split, as it is being merged, the 4 elements requires a total of 6 comparisons._

So, the mathematical calculation is as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/30Xikd3S8hvaeN5QCQ7FUebqfRHtXNdfMlOS)
_9 operations (**3 splits &amp; 6 comparisons**) are required to perform a merge sort on a 4 element array_

For simplicity, the complexity of merge sort is **O(n log n)**. The **+1** is insignificant relative to the value of **n log n** and log base 2 is assumed.

### Quick

A **quick sort** selects a value (at index 0), swaps all lesser values closer to it, then makes a final swap to place the selected value ahead of the lesser values (an index somewhere after 0). In this manner, all values behind the **pivot value** are lesser values. All values ahead of it are greater values. Hence, upon pivoting, the **selected value (**pivot**)** is placed into its correct position. The process repeats until all values are “pivoted” to their correct positions.

![Image](https://cdn-media-1.freecodecamp.org/images/kjyINxAg57U9i3L3LR82l3a78eczlbmTWxeJ)
_[source](https://thumbs.gfycat.com/RectangularHarmlessGalapagosmockingbird-size_restricted.gif" rel="noopener" target="_blank" title=")_

Similar in practice to **merge sort,** **quick sort** requires splitting a list into smaller lists. Rather than sorting on merge, a pivot is selected to order the list such that lesser values are to its left & greater values are to its right. Therefore, it is no surprise that, like **merge sort**, **quick sort** also has a complexity of **O(n log n)**.

So, for a 4 element array, a pivot is selected & its correct position is found (i.e., 2 at index 0 belongs at index 1). During this discovery, 3 comparisons are made with the pivot value (2) to the remaining elements (4, 1 & 3).

![Image](https://cdn-media-1.freecodecamp.org/images/SzBMbtjRvg4D4mob41oxqTAfY533YVJmTC8q)
_Quick Sort of Array [2, 4, 1, 3]_

The partially sorted array (1, 2, 4, 3) is then decomposed to find the pivot positions of value **1** and **4 (**by comparison to value 3**)**, before discovering the last pivot position (value **3**). This amounts to 4 comparisons and the discovery of 4 pivot positions or:

![Image](https://cdn-media-1.freecodecamp.org/images/44KtTSDkRKtWfoJxjCkRO-cQZ6AqZ9-5Fyb8)
_O(n log n)_

### Radix

A **radix sort** continuously orders a list of numbers by their base ten digit.

![Image](https://cdn-media-1.freecodecamp.org/images/Yol000Gd9BoRp6zYTLOlLaBwogDcQEUQ3DQ9)
_Digits 0 to 9_

In this case, the numbers (101, 54, 305, 6, 81) are first ordered by their 0’s place digit, then, 10’s place digit & finally, 100’s place digit. In practice, this means creating buckets (digits 0 to 9) for storing numbers with common digits (i.e., 10**1** & 8**1** shares a common digit at 0’s place). Then, combining all numbers in their bucket order (starting with 0’s place: 10**1**, 8**1**, 5**4**, 30**5**, **6**), before repeating the process over with the 10’s place digits. This continues until the highest placed digits are reached (i.e., **1**01 & **3**05 have 100’s place digits).

In general, the complexity of the **radix sort** is **O(kn)**.

* **n** is the number of elements
* **k** is the average number of digits per element

The quantity of numbers to sort (**n**) is the number of times it is required to make deposits into these digit buckets. So the list of **101, 54, 305, 6, 81** requires at least 5 deposits. The higher the digits (**k**) of the number collection, the more times it is required to repeat the sorting process from 0’s, 10’s, 100’s, 1000’s, etc. So the list **101, 54, 305, 6, 81** requires 5 deposits for **0’s**, **10’s** & **100’s** place. That’s a total of **3 x 5 = 15** deposits.

### Conclusion

Learning advanced algorithms does not diminish the importance of the more basic ones. It is through the studying of basic algorithms that you learn about what it means to search or sort, simply. And from this study, you can begin to understand the problems that come with these basic algorithms.

Nothing is created in a vacuum. It starts with an idea. Where it goes from there is limited by the human mind and what we can do with the physical world around us. It is “always day one,” should you choose to expand your horizons.

### **Reference:**

[https://www.udemy.com/js-algorithms-and-data-structures-masterclass/](https://www.udemy.com/js-algorithms-and-data-structures-masterclass/)

