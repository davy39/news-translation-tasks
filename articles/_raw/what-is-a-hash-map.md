---
title: What is a Hash Map? Time Complexity and Two Sum Example
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2024-01-25T17:02:13.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-hash-map
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/joan-gamell-ZS67i1HLllo-unsplash.jpg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: Hash tables
  slug: hash-tables
- name: Mapping
  slug: mapping
seo_title: null
seo_desc: 'A hash table or hash map, is a data structure that helps with mapping keys
  to values for highly efficient operations like the lookup, insertion and deletion
  operations.

  In this tutorial, you''ll learn the following:


  Constant and linear time complexit...'
---

A hash table or hash map, is a data structure that helps with mapping keys to values for highly efficient operations like the lookup, insertion and deletion operations.

In this tutorial, you'll learn the following:

* Constant and linear time complexity.
* Why use a hash map?
* Things to consider when writing hash functions.
* How to solve the Two Sum problem in PHP and JavaScript.

## What is Constant Time Complexity - O(1)?

O(1) indicates that the running time of an algorithm is constant, regardless of the input size. 

This implies that the algorithm's performance isn't dependent on the size of the input. An example is accessing an index of an array.

```php
<?php

function constantTimeAlgorithm($arr) 
{
    
    echo $arr[0] . PHP_EOL;
}
```

Here is a non-code example to illustrate the concept of constant time complexity:

Imagine sending a file through an airline to your friend, and the airline has a policy where they charge based on the weight of the package.

Now, whether your file weighs 2 grams or 20 kilograms, the airline's processing time remains constant. This means that the time it takes for the airline to handle your package doesn't depend on the weight of the file – it's always the same. 

In other words, the processing time is constant irrespective of the size of the file.

## What is Linear Time Complexity - O(n)?

O(n) indicates that the running time of an algorithm grows linearly with the size of the input. 

The performance of the algorithm is directly proportional to the input size. An example is traversing a `for` loop and printing elements.

```php
<?php

function linearTimeAlgorithm($arr) 
{
    foreach ($arr as $element) {
        echo $element . PHP_EOL;
    }
}

```

Here's a non-code example to illustrate the concept of linear time complexity:

Consider using an electronic transfer service to send a file to your friend. In this scenario, the time it takes to transfer the file increases linearly with the size of the file. 

For instance, if it takes 1 minutes to transfer a 100 MB file, it would take approximately 100 minutes to transfer a 10 GB file using the same service. 

This linear relationship between the size of the file and the time it takes to transfer it reflects linear time complexity. The time taken to transfer the file increases proportionally or linearly with the size of the input or file.

## Why use a Hash Map?

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-108.png)
_Illustration of how a hash map works_

A hash map is a concrete implementation of the abstract data type known as an associative array. 

In a hash map, keys are hashed to determine the index where the corresponding values will be stored, allowing for efficient retrieval and storage of key-value pairs. 

This implementation typically provides fast access times for operations like insertion, deletion, and lookup of values based on their associated keys. 

In languages like PHP or JavaScript, when you use an associative array, you are essentially using a hash map. Their associative arrays are implemented using hash tables behind the scenes. 

You can use strings, integers, or other data types as keys, and the language's internal hashing mechanism efficiently maps these keys to their corresponding values. Additionally, JavaScript provides the `Map` object for more advanced hash map functionalities.

### Time and Space Complexity for Hash Map

The time and space complexity for a hash map (or hash table) is not necessarily O(n) for all operations. The typical and desired time complexity for basic operations like insertion, lookup, and deletion in a well-designed hash map is O(1) on average. 

Here's a breakdown of time and space complexity for a hash map:

#### Time Complexity:

Average Case:

* Insertion (average): O(1)
* Lookup (average): O(1)
* Deletion (average): O(1)

Worst Case:

* Insertion (worst): O(n), where n is the size of the hash map. This occurs when there are many hash collisions, leading to linear probing or other collision resolution strategies that may involve traversing the entire hash map.
* Lookup and Deletion (worst): O(n), for the same reason as insertion.

#### Space Complexity:

* The space complexity is typically O(n). Where n is the number of key-value pairs stored in the hash map. Each key-value pair occupies constant space, and the space required grows linearly with the number of elements.

In algorithm analysis, the notation O(1) and O(n) represent the upper bounds on the time complexity of an algorithm, where n is the size of the input.

#### Operations 

1. **Insertion:** The key-value pair is hashed, and the resulting index is used to store the value in the corresponding slot. If a collision occurs, the collision resolution strategy is applied.
2. **Deletion:** The key is hashed to find the index, and the item at that index is removed. Collision resolution may be necessary.
3. **Lookup:** The key is hashed to find the index, and the value at that index is returned. Collision resolution may be applied if needed.

## Things to consider When Creating Hash Tables

When creating hash tables, there are several important considerations to ensure efficiency, including fast computation of hash codes and effective collision resolution strategies.

### Fast Computation

Hash codes should be computed quickly to ensure efficient insertion, lookup, and deletion operations. A good hash function contributes to the speed of hash code computation.

### Avoid collision

A collision happens when two or more keys produce the same hash code. In other words, multiple keys map to the same array index.

## How to Handle Collisions

Hash maps use collision resolution techniques to deal with collisions. Common strategies include:

#### Chaining

To manage several values with the same hash code, chaining involves storing a linked list or other data structure at each array index.  If a collision occurs, the new key-value pair is appended to the linked list at the relevant index.

#### Open addressing

When a collision happens in a hash table, a technique called open addressing is employed to resolve it by searching for the next open space. 

All it does is search the array for the next empty slot where the key-value combination can be placed. Methods including double hashing, quadratic probing, and linear probing are applied.

**Linear Probing:** In linear probing, the algorithm moves linearly to the next index in the array in order to find the next open slot when a collision occurs.

**Quadratic Probing:** In this method, an algorithm employs a quadratic function to find the next slot that becomes available.

**Double Hashing:** In double hashing, the algorithm calculates the step size between probes using a secondary hash function.

In order to reduce the possibility of collisions, a good hash function should generate distinct hash codes for various inputs. By making sure the hash codes are evenly distributed throughout the range of potential values, collisions can be prevented.

## How to Solve the Two Sum Problem

![Image](https://www.freecodecamp.org/news/content/images/2024/01/image-117.png)
_Two sum problem_

The Two Sum problem involves finding all pairs of elements in an array that sum up to a specific target value. Now let's look at the problem statement.

### Problem statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the `target`.

_Example 1:_

**Input:** nums = [3,2,4, 8], target = 12

**Output:** [2, 3]

_Example 2:_

**Input:** nums = [5,5], target = 10 

**Output:** [0,1]

### Solution

To solve the Two Sum problem, we can use a hash table. The idea is to traverse the `nums` array and, for each element, check if the complement (the difference between the target and the current element) is already in the hash table. If it is, we have found a pair of indices whose elements add up to the target.

Here are the steps to follow:

1. To hold the elements and their respective indices, create an empty hash table upon initialization.
2. Go over the array of `nums`.
3. Do the complement calculation (target - current element) for each element.
4. Verify if the complement has already been added to the hash table.  If yes, return the current index and the index stored in the hash table for the complement.
5. If the complement is not in the hash table, store the current element and its index in the hash table.
6. If no such pair is found during the traversal, it implies that there is no solution.

##### PHP Code Solution

```php
<?php

function twoSum($nums, $target) {
    $hashTable = [];

    foreach ($nums as $i => $num) {
        $complement = $target - $num;

        if (array_key_exists($complement, $hashTable)) {
        
            // Found the pair, return the indices
            return [$hashTable[$complement], $i];
        }

        // Store the current element in the hash table
        $hashTable[$num] = $i;
    }

    // No solution found
    return [];
}

// Example usage:
$nums = [2, 7, 11, 5, 15, 30];
$target = 12;
$result = twoSum($nums, $target);

echo "Indices of the two numbers: [" . implode(", ", $result) . "]";

```

##### JavaScript Code Solution using `map` Function

```javascript
function twoSum(nums, target) {
    const hashTable = new Map();

    for (const [index, num] of nums.entries()) {
        const complement = target - num;

        // Check if the complement is in the Map
        if (hashTable.has(complement)) {
        
            // Found the pair, return the indices
            return [hashTable.get(complement), index];
        }

        // Store the current number and its index in the Map
        hashTable.set(num, index);
    }

    // No solution found
    return [];
}

// Example usage:
const nums = [2, 7, 11, 5, 15, 30];
const target = 12;
const result = twoSum(nums, target);

console.log(`Indices of the two numbers that add up to ${target}: [${result.join(', ')}]`);

```

This approach has a time complexity of O(n) because we iterate through the array once. The space complexity is also O(n) due to the storage of elements in the hash map.

## Resources

1. [Hash table From Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
2. [Hash maps in Python](https://www.youtube.com/watch?v=RcZsTI5h0kg)

## Conclusion

In this article, you learned about hash maps, things to consider when writing hash functions and a real world problem that involves solving the Two Sum problem.

Keep learning, and Happy Coding!

You can find me on [LinkedIn](https://www.linkedin.com/in/suleolanrewaju/) and [Twitter](https://twitter.com/bigdevlarry).

