---
title: How to count the number of 0s and 1s in a string without using a counter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-23T22:17:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-count-no-of-0-and-1-in-a-string-without-using-counter
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca0ae740569d1a4ca4a21.jpg
tags:
- name: interview questions
  slug: interview-questions
- name: Job Hunting
  slug: job-hunting
seo_title: null
seo_desc: 'By Ujjwal Gupta

  This question is often asked in interviews to test the candidate''s approach to
  thinking about code.

  Problem Statement

  You have a string which contains only 0''s and 1''s. You need to write a program
  which will return the number of 0''s a...'
---

By Ujjwal Gupta

This question is often asked in interviews to test the candidate's approach to thinking about code.

### Problem Statement

You have a string which contains only 0's and 1's. You need to write a program which will return the number of 0's and 1's, and you are not allowed to use a counter variable by any means. 

Seems tricky right? 

Worry not - it's very simple. I am going to teach you how to do it both ways:

* With a counter (the classic approach)
* Without using a counter (as required in the interview question)

## Let's Code 

### With a Counter

```javascript
function count(str) {
  var countForZero = 0;
  var countForOne = 0;
    
  for (var i = 0, length = str.length; i < length; i++) {
    if (str[i] === '0') {
      countForZero++;
    }
    else {
      countForOne++;
    }
  }
    
  return {
    'zero': countForZero,
    'One': countForOne
  };
}

```

**The logic of the above code is:**

* Keep two variables for counting zeros and ones. 
* Loop through the characters of the string, and when a zero is found, increment countForZero. When a one is found, increment countForOne.
* In the last part, we are returning the count in an object.

You can try the above code using this link: [https://repl.it/repls/PurpleIdolizedInstructions](https://repl.it/repls/PurpleIdolizedInstructions)

Now, let's see the solution without a counter.

### Without a Counter

```
function count(str) {
  var sum = 0;
  
  for (var i = 0, length = str.length; i < length; i++) {
    sum += Number(str[i]);
  }
  
  return {
    'zero': str.length - sum,
    'One': sum
  };
}
```

As you can see in the above code, I am not using any counter, but rather a variable called sum. So what's the concept here?

**The concept is:**

> The sum of a character of a string which contains zero and one will always be equal to the number of 1's.

For example: 0011001 : 0+0+1+1+0+0+1 = 3 = number of 1's

> And the number of zeroes = length of string - number of 1's

**The logic of the above code is:** 

* Keep a sum variable initialized with value zero.
* Loop through the characters of string and take the sum of all the characters.
* The sum of all the characters of the string will be the number of 1's, and the number of zeroes will be the (length of string - number of 1's). 
* In the last part, we are returning the count in an object.

You can try the above code using this link: [https://repl.it/repls/ComfortableOrdinaryConversions](https://repl.it/repls/ComfortableOrdinaryConversions)

I hope you are able to understand how to answer this question both with and without a counter now. 

If you have any questions, feel free to ask in the comment section. Or if you have any other tricks, let me know as well.

