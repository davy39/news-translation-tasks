---
title: How to form the smallest possible number from a given number in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-29T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/forming-the-smallest-possible-number-from-the-given-number-in-javascript-bda790655c8e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XoEDgZmZ-IWBZivc4DJakg.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: data structures
  slug: data-structures
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Prashant Yadav

  In this tutorial, we will implement an algorithm to form the smallest possible number
  with ES6.


  Source: Pixabay

  Input: 55010 7652634

  Output: 10055 2345667

  Note: The transformed number should not start with 0 if it has at least one ...'
---

By Prashant Yadav

In this tutorial, we will implement an algorithm to form the smallest possible number with [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/).

![Image](https://cdn-media-1.freecodecamp.org/images/w8OnyWg2LPtjbRckRL41TKnrqr6ObvUOZbEW)
_Source: Pixabay_

```
Input: 55010 7652634
```

```
Output: 10055 2345667
```

**Note**: The transformed number should not start with 0 if it has at least one non-zero character.

We are going to use two different approaches to solve this problem. Everything will be written in [ES6](https://learnersbucket.com/tutorials/es6/es6-intro).

* In the first approach, we will assume that the provided number is in string format and solve it using sorting which will take O(nlogn).
* In the Second approach, we will solve with numeric value with O(d) time, where d is the number of digits.

### Using sorting O(nlogn).

#### Implementation

* We will convert the number to the character array and then sort that array.
* After sorting we will check if the first character in the array is 0.
* If it is not 0 then we will join the array and return it.
* If it is 0 then we will find the first non-zero number and swap it with 0 and return it.

```
function smallestPossibleNumber(num){
```

```
//Create a character array and sort it in ascending orderlet sorted = num.split('').sort();
```

```
//Check if first character is not 0 then join and return it if(sorted[0] != '0'){    return sorted.join('');}
```

```
//find the index of the first non - zero character let index = 0; for(let i = 0; i < sorted.length; i++){  if(sorted[i] > "0"){    index = i;    break;  } }
```

```
//Swap the indexes  let temp = sorted[0];  sorted[0] = sorted[index];  sorted[index] = temp;
```

```
//return the string after joining the characters of array return sorted.join(''); }
```

Running the Program

```
Input:console.log(smallestPossibleNumber('55010'));console.log(smallestPossibleNumber('7652634'));console.log(smallestPossibleNumber('000001'));console.log(smallestPossibleNumber('000000'));
```

```
Output:100552345667100000000000
```

```
/*How it works  let sorted = num.split('').sort();   = ['5','5','0','1','0'].sort() = ['0','0','1','5','5']  if(sorted[0] != '0'){   // '0' != '0' condition fails     return sorted.join('');  }    //Find the index of the first non - zero character  let index = 0;  for(let i = 0; i < sorted.length; i++){     if(sorted[i] > '0'){  // '1' > '0'       index = i;      // index = 2;       break;          // break;     }  }    //swap the index  var temp = sorted[0];        sorted[0] = sorted[index];  sorted[index] = temp;    //return the string  return sorted.join('');*/
```

#### How it works

We first created the array of characters like `['5', '5', '0', '1', 0]` . Then we sort this to`['0', '0', '1', '5', '5']` After this, we find the first non-zero element and swap it with first zero elements like `['1', '0', '0', '5', '5']` . Now we have our smallest number ready we just need to concatenate them together and return it.

Learn more about the [split()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split), [sort()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort), [join()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join).

Time Complexity: O(nlogn).  
Space Complexity: O(n).

#### Time and Space complexity explanation

We are creating a character array which will take O(n) time. Then sorting the array will take O(nlogn).

After that, we are finding the index of smallest non zero number which can take O(n) in the worst case and joining the array to create the string will take O(n). As these all operations are running one after other. So time complexity is O(n + nlogn + n + n) = O(nlogn).

We are creating an array of characters from the string, so space complexity is O(n).

### Using numeric value O(logn).

There is a drawback in this approach: if the number only contains zeros then it will return a single zero.

#### Implementation

* We will create an array of numbers from 0 to 9.
* Then we will keep track of the digits present in the number by increasing their count in the array.
* After that, we will find the smallest non-zero digit and decrease its count by 1.
* In the end, we will recreate the number by arranging them in ascending order and return the result.
* This solution is based on the counting sort.

```
function smallestPossibleNumber(num) {    // initialize frequency of each digit to Zero   let freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];          // count frequency of each digit in the number   while (num > 0){      let d = parseInt(num % 10); // extract last digit     freq[d]++; // increment counting     num = parseInt(num / 10); //remove last digit   }
```

```
// Set the LEFTMOST digit to minimum expect 0   let result = 0;    for (let i = 1 ; i <= 9 ; i++) {       if (freq[i] != 0) {          result = i;          freq[i]--;          break;      }    }           // arrange all remaining digits   // in ascending order   for (let i = 0 ; i <= 9 ; i++) {      while (freq[i]-- != 0){          result = result * 10 + i;       }   }        return result; }
```

Running the program

```
Input:console.log(smallestPossibleNumber('55010'));console.log(smallestPossibleNumber('7652634'));console.log(smallestPossibleNumber('000001'));console.log(smallestPossibleNumber('000000'));
```

```
Output:10055234566710
```

```
/* How it works   // initialize frequency of each digit to Zero   let freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];      // count frequency of each digit in the number   while (num > 0){      let d = parseInt(num % 10); // extract last digit     freq[d]++; // increment counting             num = parseInt(num / 10); //remove last digit   }    //After incrementing count   //freq = [2, 1, 0, 0, 0, 2, 0, 0, 0, 0]      // Set the LEFTMOST digit to minimum expect 0   let result = 0;    for (let i = 1 ; i <= 9 ; i++) {       if (freq[i] != 0) {          result = i;          freq[i]--;          break;      }    }    // result = 1     // arrange all remaining digits   // in ascending order   for (let i = 0 ; i <= 9 ; i++) {      while (freq[i]-- != 0){          result = result * 10 + i;       }   }
```

```
   //10   //100   //1005   //10055   //10055      return result*/
```

Time Complexity: O(nlogn).  
Space Complexity: O(1).

#### Time and Space complexity explanation

We are removing each digit from the number and incrementing its respective count in an array that will take O(logn). Then we find the smallest non-zero number from the array in O(10).

After that we are rearranging the digits to create the smallest number in O(10 * logn). Time complexity is O(logn + 10+ 10logn) = O(logn) or O(d), where d is the no of digits

We are using constant space (an array of 10 numbers), so space complexity is O(1).

If you liked this article, please give it some ?and share it! If you have any questions related to this feel free to ask me.

_For more like this and algorithmic solutions in Javascript, follow me on_ [**Twitter**](https://twitter.com/LearnersBucket)_._ I write about [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), React, Nodejs, [Data structures](https://learnersbucket.com/tutorials/topics/data-structures/), and [Algorithms](https://learnersbucket.com/examples/topics/algorithms/) on [_learnersbucket.com_](https://learnersbucket.com/)_._

