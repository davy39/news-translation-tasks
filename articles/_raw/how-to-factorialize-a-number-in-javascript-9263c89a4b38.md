---
title: Three Ways to Factorialize a Number in JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-03-16T11:51:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uKMWUxeIBoqzbgBNRHiyjQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'This article is based on Free Code Camp Basic Algorithm Scripting “Factorialize
  a Number”

  In mathematics, the factorial of a non-negative integer n can be a tricky algorithm.
  In this article, I’m going to explain three approaches, first with the recu...'
---

_This article is based on Free Code Camp Basic Algorithm Scripting “[Factorialize a Number](https://www.freecodecamp.com/challenges/factorialize-a-number)”_

**In mathematics**, the factorial of a non-negative integer _n_ can be a tricky algorithm. In this article, I’m going to explain three approaches, first with the recursive function, second using a while loop and third using a for loop.

We have already seen a recursion approach on a String in the previous article, [**How to Reverse a String in JavaScript in 3 Different Ways ?**](https://medium.com/@sonya.moisset/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb#.ekpftot4d) This time we will apply the same concept on a number.

#### Algorithm Challenge

> Return the factorial of the provided integer.  
>   
> If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.  
>   
> Factorials are often represented with the shorthand notation **n!**  
>   
> For example: **5! = 1 * 2 * 3 * 4 * 5 = 120**

```js

function factorialize(num) {
  return num;
}
factorialize(5);
```

#### _Provided test cases_

* **_factorialize(0)_** should return 1
* **_factorialize(5)_** should return 120
* **_factorialize(10)_** should return 3628800
* **_factorialize(20)_** should return 2432902008176640000

### What is factorializing a number all about?

When you factorialize a number, you are multiplying that number by each consecutive number minus one.

If your number is 5, you would have:

```
5! = 5 * 4 * 3 * 2 * 1
```

The pattern would be:

```
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2 * 1
4! = 4 * 3 * 2 * 1
5! = 5 * 4 * 3 * 2 * 1
```

### 1. Factorialize a Number With Recursion

```js
function factorialize(num) {
  // If the number is less than 0, reject it.
  if (num < 0) 
        return -1;
    
  // If the number is 0, its factorial is 1.
  else if (num == 0) 
      return 1;
    
  // Otherwise, call the recursive procedure again
    else {
        return (num * factorialize(num - 1));
        /* 
        First Part of the recursion method
        You need to remember that you won’t have just one call, you’ll have several nested calls
        
        Each call: num === "?"        	         num * factorialize(num - 1)
        1st call – factorialize(5) will return    5  * factorialize(5 - 1) // factorialize(4)
        2nd call – factorialize(4) will return    4  * factorialize(4 - 1) // factorialize(3)
        3rd call – factorialize(3) will return    3  * factorialize(3 - 1) // factorialize(2)
        4th call – factorialize(2) will return    2  * factorialize(2 - 1) // factorialize(1)
        5th call – factorialize(1) will return    1  * factorialize(1 - 1) // factorialize(0)
        
        Second part of the recursion method
        The method hits the if condition, it returns 1 which num will multiply itself with
        The function will exit with the total value
        
        5th call will return (5 * (5 - 1))     // num = 5 * 4
        4th call will return (20 * (4 - 1))    // num = 20 * 3
        3rd call will return (60 * (3 - 1))    // num = 60 * 2
        2nd call will return (120 * (2 - 1))   // num = 120 * 1
        1st call will return (120)             // num = 120
        
        If we sum up all the calls in one line, we have
        (5 * (5 - 1) * (4 - 1) * (3 - 1) * (2 - 1)) = 5 * 4 * 3 * 2 * 1 = 120
        */
    }
}
factorialize(5);
```

#### Without comments:

```js
function factorialize(num) {
  if (num < 0) 
        return -1;
  else if (num == 0) 
      return 1;
  else {
      return (num * factorialize(num - 1));
  }
}
factorialize(5);
```

### 2. Factorialize a Number with a WHILE loop

```js
function factorialize(num) {
  // Step 1. Create a variable result to store num
  var result = num;
   
  // If num = 0 OR num = 1, the factorial will return 1
  if (num === 0 || num === 1) 
    return 1; 
 
  // Step 2. Create the WHILE loop 
  while (num > 1) { 
    num--; // decrementation by 1 at each iteration
    result = result * num; // or result *= num; 
    /* 
                    num           num--      var result      result *= num         
    1st iteration:   5             4            5             20 = 5 * 4      
    2nd iteration:   4             3           20             60 = 20 * 3
    3rd iteration:   3             2           60            120 = 60 * 2
    4th iteration:   2             1          120            120 = 120 * 1
    5th iteration:   1             0          120
    End of the WHILE loop 
    */
  }
     
  // Step 3. Return the factorial of the provided integer
  return result; // 120
}
factorialize(5);
```

#### Without comments:

```js
function factorialize(num) {
  var result = num;
  if (num === 0 || num === 1) 
    return 1; 
  while (num > 1) { 
    num--;
    result *= num;
  }
  return result;
}
factorialize(5);
```

### 3. Factorialize a Number with a FOR loop

```js
function factorialize(num) {
  // If num = 0 OR num = 1, the factorial will return 1
  if (num === 0 || num === 1)
    return 1;
  
  // We start the FOR loop with i = 4
  // We decrement i after each iteration 
  for (var i = num - 1; i >= 1; i--) {
    // We store the value of num at each iteration
    num = num * i; // or num *= i;
    /* 
                    num      var i = num - 1       num *= i         i--       i >= 1?
    1st iteration:   5           4 = 5 - 1         20 = 5 * 4        3          yes   
    2nd iteration:  20           3 = 4 - 1         60 = 20 * 3       2          yes
    3rd iteration:  60           2 = 3 - 1        120 = 60 * 2       1          yes  
    4th iteration: 120           1 = 2 - 1        120 = 120 * 1      0          no             
    5th iteration: 120               0                120
    End of the FOR loop 
    */
  }
  return num; //120
}
factorialize(5);
```

#### Without comments:

```js
function factorialize(num) {
  if (num === 0 || num === 1)
    return 1;
  for (var i = num - 1; i >= 1; i--) {
    num *= i;
  }
  return num;
}
factorialize(5);
```

I hope you found this helpful. This is part of my “How to Solve FCC Algorithms” series of articles on the Free Code Camp Algorithm Challenges, where I propose several solutions and explain step-by-step what happens under the hood.

[**Three ways to repeat a string in JavaScript**  
_In this article, I’ll explain how to solve freeCodeCamp’s “Repeat a string repeat a string” challenge. This involves…_](https://www.freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d/)

[**Two ways to confirm the ending of a String in JavaScript**  
_In this article, I’ll explain how to solve freeCodeCamp’s “Confirm the Ending” challenge._](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)

[**Three Ways to Reverse a String in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Reverse a String”_](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Two Ways to Check for Palindromes in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Check for Palindromes”._](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)

[**Three Ways to Find the Longest Word in a String in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Find the Longest Word in a String”._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Three Ways to Title Case a Sentence in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Title Case a Sentence”._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

[**Three ways you can find the largest number in an array using JavaScript**  
_In this article, I’m going to explain how to solve Free Code Camp’s “Return Largest Numbers in Arrays” challenge. This…_](https://medium.freecodecamp.com/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1)

If you have your own solution or any suggestions, share them below in the comments.

Or you can follow me on [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** and [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), right after you click the green heart below ;-)

‪#‎StayCurious‬, ‪#‎KeepOnHacking‬ & ‪#‎MakeItHappen‬!

