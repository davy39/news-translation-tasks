---
title: How to solve the Sherlock and Anagrams coding challenge in JavaScript
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2019-04-23T15:28:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-the-sherlock-and-anagrams-coding-challenge-in-javascript-a80baa908637
coverImage: https://cdn-media-1.freecodecamp.org/images/1*A_R6N6YK1HylRbzIi_0KPw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding challenge
  slug: coding-challenge
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'This post is going to get you through my solution to a coding challenge
  called “Sherlock and Anagrams.” You may take a look at it in HackerRank.

  I spent a lot of time trying to solve it, with JavaScript. When I tried to google
  it, I could not find a ...'
---

This post is going to get you through my solution to a coding challenge called “Sherlock and Anagrams.” You may take a look at it in [HackerRank](https://www.hackerrank.com/challenges/sherlock-and-anagrams).

I spent a lot of time trying to solve it, with JavaScript. When I tried to google it, I could not find a decent JS solution. I found just one, and it was not working correctly. Also, any explanations were completely out of the question. That’s why I decided to write an article about it and try to put some nice and easy to digest explanations along the way. Keep reading now!

⚠️CAUTION: *I will roll out my solution below with short explanations about each of the steps. If you want to give a try yourself, please stop here and go to HackerRank’s site.*

### Problem

Two strings are [anagrams](http://en.wikipedia.org/wiki/Anagram) of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example *s = mom*, the list of all anagrammatic pairs is \[*m, m*\], \[*mo, om*\] at positions \[\[0\], \[2\]\], \[\[0, 1\], \[1, 2\]\] respectively.

**Constraints**  
Length of the input string: 2 ≤ |s| ≤ 100  
String *s* contains only lowercase letters from the range ascii\[a-z\].

### Analysis

First thing first — we need to get a better understanding of the whole problem. What is an anagram? What is an anagrammatic pair? Can I see one? Also, what exactly does it mean *substrings*?

**In other words, we need to have a clear picture of what are we trying to solve, before solving it.**

From the description of the problem, we can deduct all we need. Keep walking! ?

*I think this is a good moment to mention that the challenge in question is under the “Dictionaries and Hashmaps” section in the HackerRank website. You’ll probably think that you should use this kind of data structure when solving it.* ?

#### Anagrams

Since we are going to look for anagrams, let’s start with them. As it is described above, an anagram of one word is another word that has the same length and is created with the same characters from the former word.

![Image](https://cdn-media-1.freecodecamp.org/images/yqexlCorVcBamgbm1UuU1q2ixW74Zgd50bOs align="left")

*Animation for the anagram “Listen = Silent”*

So we will have to look for words and compare them with other words, in order to see if they are anagrammatic pairs. Once found, we will just count them.

#### Anagrammatic pairs

Since we’ve seen what an anagram is, it should be relatively easy to conclude that an anagrammatic pair is just two strings that are anagrams. Such as “mo” and “om”, or “listen” and “silent”. We will have to count how many pairs like this can be found in a given string. In order to do that, we need to split this original string to substrings.

#### Substrings

Substrings, as the name infers, are parts of a string. These parts could be just a letter or a pair of letters, such as what have we seen in the example above — “*m*” or “*mo.*” In our solution, we will split the original string to such substrings and then we will go over them and do the comparison, which will tell us whether we have anagrammatic pairs among them.

### Solution

Now that we’ve done our analysis, it’s showtime! ?

Let’s summarize:

1. We need to find all substrings of the given string — create a method for that.
    
2. We need to be able to check if two strings are anagrams — create a method for that.
    
3. We need to count all anagrammatic pairs in the given string — create a method for that.
    
4. Combine everything from above and spit the result — create a method for that.
    

#### Get all substrings

This will be our helper method for finding all substrings of a given string:

```js
function getAllSubstrings(str) {
  let i, j, result = [];

  for (i = 0; i < str.length; i++) {
    for (j = i + 1; j < str.length + 1; j++) {
      result.push(str.slice(i, j))
    }
  }
  return result
}
```

As you can see, it has O(n²) time complexity. For our case, it does the job, because we have limited length of the input string (up to 100 characters).

#### Check for anagrams

This will be our helper method for checking if two strings are anagrammatic pairs:

```js
function isAnagram(str1, str2) {
  const hist = {}

  for (let i = 0; i < str1.length; i++) {
    const char = str1[i]
    if (hist[char]) {
      hist[char]++
    } else {
      hist[char] = 1
    }
  }

  for (let j = 0; j < str2.length; j++) {
    const char = str2[j]
    if (hist[char]) {
      hist[char]--
    } else {
      return false
    }
  }

  return true
}
```

Remember that we assumed we’d most probably have to use data structures such as hashmaps or dictionaries (given the section where this challenge is found on HackerRank).

We use a simple JavaScript object to play the role of a hashmap. We do two iterations — one per string. When we iterate over the first one, we add its characters as keys to the hashmap and count their appearances, which are going to be stored as their values. Then we do another iteration over the second string. Check if its characters are stored in our hashmap. If yes — decrement their value. If there are missing characters, which means the two strings are not an anagrammatic pair, we simply return false. If both loops complete, we return true, signifying that the strings being analyzed are an anagrammatic pair.

#### Do the counting

This is the method, where we will use the helper for checking if a pair is anagrammatic and count it. We do that with the help of JavaScript arrays and the methods they provide. We iterate over an array containing all the substrings of the original string. Then we get the correct element and remove it from the array. And then we do another loop through that array and return 1 if we find that there is an anagram of the current element. If nothing is found, we return 0.

```js
function countAnagrams(currentIndex, arr) {
  const currentElement = arr[currentIndex]
  const arrRest = arr.slice(currentIndex + 1)
  let counter = 0

  for (let i = 0; i < arrRest.length; i++) {
    if (currentElement.length === arrRest[i].length && isAnagram(currentElement, arrRest[i])) {
      counter++
    }
  }

 return counter
}
```

#### And in the end

The only thing left to be done now is to combine all of the above and spit the desired result. Here is how the final method looks like:

```js
function sherlockAndAnagrams(s) {
  const duplicatesCount = s.split('').filter((v, i) => s.indexOf(v) !== i).length

  if (!duplicatesCount) return 0
  let anagramsCount = 0

  const arr = getAllSubstrings(s)

  for (let i = 0; i < arr.length; i++) {
    anagramsCount += countAnagrams(i, arr)
  }

  return anagramsCount
}
```

*Maybe you have noticed, here I am checking first for duplicates in order to know if I should continue further. As if there are no duplicated letters, then it’s not possible to have an anagram.*

And finally, we get all substrings into an array, iterate over it, count the anagrammatic pairs that are found and return this number.

You can find the full code [here](https://github.com/mihailgaberov/misc/blob/master/coding-challenges/sherlock-and-anagrams.js).

### Conclusion

These kind of exercises are very good for making you think algorithmically. Also they change your way of working in your day to day job. My recommendation would be to do the same I am trying to do — train your brain now and then with one of those. And if you can — share. I know sometimes you don’t have time for such challenges, but when you do — go for it.

My personal feeling after finishing this was total satisfaction, which is completely understandable, considering the time it took me to do it. But in the end, dear reader, I am even happier I can share this experience with you?!

Thanks for reading. Read more of my articles at [mihail-gaberov.eu](https://mihail-gaberov.eu/sherlock-and-anagrams/).
