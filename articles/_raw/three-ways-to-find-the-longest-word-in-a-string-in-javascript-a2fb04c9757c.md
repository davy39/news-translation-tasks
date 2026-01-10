---
title: Three Ways to Find the Longest Word in a String in JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-03-30T13:06:33.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*k2RZZ3j1e-_r9Av7SgzFDw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'This article is based on Free Code Camp Basic Algorithm Scripting “Find
  the Longest Word in a String”.

  In this algorithm, we want to look at each individual word and count how many letters
  are in each. Then, compare the counts to determine which word...'
---

_This article is based on Free Code Camp Basic Algorithm Scripting “_[Find the Longest Word in a String](https://www.freecodecamp.com/challenges/find-the-longest-word-in-a-string)_”._

**In this algorithm**, we want to look at each individual word and count how many letters are in each. Then, compare the counts to determine which word has the most characters and return the length of the longest word.

In this article, I’m going to explain three approaches. First with a FOR loop, second using the sort() method, and third using the reduce() method.

#### Algorithm Challenge

> Return the length of the longest word in the provided sentence.  
>   
> Your response should be a number.

#### **_Provided test cases_**

* **_findLongestWord(“The quick brown fox jumped over the lazy dog”)_** should return a number
* **_findLongestWord(“The quick brown fox jumped over the lazy dog”)_** should return 6
* **_findLongestWord(“May the force be with you”)_** should return 5
* **_findLongestWord(“Google do a barrel roll”)_** should return 6
* **_findLongestWord(“What is the average airspeed velocity of an unladen swallow”)_** should return 8
* **_findLongestWord(“What if we try a super-long word such as otorhinolaryngology”)_** should return 19

```js
function findLongestWord(str) {
  return str.length;
}
findLongestWord("The quick brown fox jumped over the lazy dog");
```

### 1. Find the Longest Word With a FOR Loop

For this solution, we will use the String.prototype.split() method

* The **split()** method splits a String object into an array of strings by separating the string into sub strings.

We will need to add an empty space between the parenthesis of the **split()** method,

```
var strSplit = “The quick brown fox jumped over the lazy dog”.split(‘ ‘);
```

which will output an array of separated words:

```
var strSplit = [“The”, “quick”, “brown”, “fox”, “jumped”, “over”, “the”, “lazy”, “dog”];
```

If you don’t add the space in the parenthesis, you will have this output:

```
var strSplit = 
[“T”, “h”, “e”, “ “, “q”, “u”, “i”, “c”, “k”, “ “, “b”, “r”, “o”, “w”, “n”, “ “, “f”, “o”, “x”, “ “, “j”, “u”, “m”, “p”, “e”, “d”, “ “, “o”, “v”, “e”, “r”, “ “, “t”, “h”, “e”, “ “, “l”, “a”, “z”, “y”, “ “, “d”, “o”, “g”];
```

```js
function findLongestWord(str) {
  // Step 1. Split the string into an array of strings
  var strSplit = str.split(' ');
  // var strSplit = "The quick brown fox jumped over the lazy dog".split(' ');
  // var strSplit = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"];
	
  // Step 2. Initiate a variable that will hold the length of the longest word
  var longestWord = 0;

  // Step 3. Create the FOR loop
  for(var i = 0; i < strSplit.length; i++){
    if(strSplit[i].length > longestWord){ // If strSplit[i].length is greater than the word it is compared with...
	longestWord = strSplit[i].length; // ...then longestWord takes this new value
     }
  }
  /* Here strSplit.length = 9
     For each iteration: i = ?   i < strSplit.length?   i++  if(strSplit[i].length > longestWord)?   longestWord = strSplit[i].length
     1st iteration:        0             yes             1   if("The".length > 0)? => if(3 > 0)?     longestWord = 3
     2nd iteration:        1             yes             2   if("quick".length > 3)? => if(5 > 3)?   longestWord = 5   
     3rd iteration:        2             yes             3   if("brown".length > 5)? => if(5 > 5)?   longestWord = 5   
     4th iteration:        3             yes             4   if("fox".length > 5)? => if(3 > 5)?     longestWord = 5  
     5th iteration:        4             yes             5   if("jumped".length > 5)? => if(6 > 5)?  longestWord = 6 
     6th iteration:        5             yes             6   if("over".length > 6)? => if(4 > 6)?    longestWord = 6 
     7th iteration:        6             yes             7   if("the".length > 6)? => if(3 > 6)?     longestWord = 6
     8th iteration:        7             yes             8   if("lazy".length > 6)? => if(4 > 6)?    longestWord = 6 
     9th iteration:        8             yes             9   if("dog".length > 6)? => if(3 > 6)?     longestWord = 6 
     10th iteration:       9             no               
     End of the FOR Loop*/

  //Step 4. Return the longest word
  return longestWord; // 6
}

findLongestWord("The quick brown fox jumped over the lazy dog");
```

#### Without comments:

```js
function findLongestWord(str) {
  var strSplit = str.split(' ');
  var longestWord = 0;
  for(var i = 0; i < strSplit.length; i++){
    if(strSplit[i].length > longestWord){
	longestWord = strSplit[i].length;
     }
  }
  return longestWord;
}
findLongestWord("The quick brown fox jumped over the lazy dog");
```

### 2. Find the Longest Word With the sort() Method

For this solution, we will use the Array.prototype.sort() method to sort the array by some ordering criterion and then return the length of the first element of this array.

* The **sort()** method sorts the elements of an array in place and returns the array.

In our case, if we just sort the array

```
var sortArray = [“The”, “quick”, “brown”, “fox”, “jumped”, “over”, “the”, “lazy”, “dog”].sort();
```

we will have this output:

```
var sortArray = [“The”, “brown”, “dog”, “fox”, “jumped”, “lazy”, “over”, “quick”, “the”];
```

In Unicode, numbers come before upper case letters, which come before lower case letters.

We need to sort the elements by some ordering criterion,

```
[].sort(function(firstElement, secondElement) {     return secondElement.length — firstElement.length; })
```

where the length of the second element is compared to the length of the first element in the array.

```js
function findLongestWord(str) {
  // Step 1. Split the string into an array of strings
  var strSplit = str.split(' ');
  // var strSplit = "The quick brown fox jumped over the lazy dog".split(' ');
  // var strSplit = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"];
  
  // Step 2. Sort the elements in the array
  var longestWord = strSplit.sort(function(a, b) { 
    return b.length - a.length;
  });
  /* Sorting process
    a           b            b.length     a.length     var longestWord
  "The"      "quick"            5            3         ["quick", "The"]
  "quick"    "brown"            5            5         ["quick", "brown", "The"]  
  "brown"    "fox"              3            5         ["quick", "brown", "The", "fox"]
  "fox"      "jumped"           6            3         ["jumped", quick", "brown", "The", "fox"]
  "jumped"   "over"             4            6         ["jumped", quick", "brown", "over", "The", "fox"]
  "over"     "the"              3            4         ["jumped", quick", "brown", "over", "The", "fox", "the"]
  "the"      "lazy"             4            3         ["jumped", quick", "brown", "over", "lazy", "The", "fox", "the"]
  "lazy"     "dog"              3            4         ["jumped", quick", "brown", "over", "lazy", "The", "fox", "the", "dog"]
  */
  
  // Step 3. Return the length of the first element of the array
  return longestWord[0].length; // var longestWord = ["jumped", "quick", "brown", "over", "lazy", "The", "fox", "the", "dog"];
                                // longestWord[0]="jumped" => jumped".length => 6
}

findLongestWord("The quick brown fox jumped over the lazy dog");
```

#### Without comments:

```js
function findLongestWord(str) {
  var longestWord = str.split(' ').sort(function(a, b) { return b.length - a.length; });
  return longestWord[0].length;
}
findLongestWord("The quick brown fox jumped over the lazy dog");
```

### 3. Find the Longest Word With the reduce() Method

For this solution, we will use the Array.prototype.reduce().

* The **reduce()** method applies a function against an accumulator and each value of the array (from left-to-right) to reduce it to a single value.

reduce() executes a callback function once for each element present in the array.

You can provide an initial value as the second argument to reduce, here we will add an empty string “”.

```
[].reduce(function(previousValue, currentValue) {...}, “”);
```

```js
function findLongestWord(str) {
  // Step 1. Split the string into an array of strings
  var strSplit = str.split(' ');
  // var strSplit = "The quick brown fox jumped over the lazy dog".split(' ');
  // var strSplit = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"];

  // Step 2. Use the reduce method
  var longestWord = strSplit.reduce(function(longest, currentWord) {
    if(currentWord.length > longest.length)
       return currentWord;
    else
       return longest;
  }, "");
  
  /* Reduce process
  currentWord      longest       currentWord.length     longest.length    if(currentWord.length > longest.length)?   var longestWord
  "The"             ""                  3                     0                              yes                          "The"
  "quick"           "The"               5                     3                              yes                         "quick"
  "brown"           "quick"             5                     5                              no                          "quick"
  "fox"             "quick"             3                     5                              no                          "quick"
  "jumped"          "quick"             6                     5                              yes                         "jumped"
  "over"            "jumped"            4                     6                              no                          "jumped"
  "the"             "jumped"            3                     6                              no                          "jumped"
  "lazy"            "jumped"            4                     6                              no                          "jumped"
  "dog"             "jumped"            3                     6                              no                          "jumped"
  */
  
  // Step 3. Return the length of the longestWord
  return longestWord.length; // var longestWord = "jumped" 
                             // longestWord.length => "jumped".length => 6
}

findLongestWord("The quick brown fox jumped over the lazy dog");
```

#### Without comments:

```js
function findLongestWord(str) {
  var longestWord = str.split(' ').reduce(function(longest, currentWord) {
    return currentWord.length > longest.length ? currentWord : longest;
  }, "");
  return longestWord.length;
}
findLongestWord("The quick brown fox jumped over the lazy dog");
```

I hope you found this helpful. This is part of my “How to Solve FCC Algorithms” series of articles on the Free Code Camp Algorithm Challenges, where I propose several solutions and explain step-by-step what happens under the hood.

[**Three ways to repeat a string in JavaScript**  
_In this article, I’ll explain how to solve freeCodeCamp’s “Repeat a string repeat a string” challenge. This involves…_](https://www.freecodecamp.org/news/three-ways-to-repeat-a-string-in-javascript-2a9053b93a2d/)

[**Two ways to confirm the ending of a String in JavaScript**  
_In this article, I’ll explain how to solve freeCodeCamp’s “Confirm the Ending” challenge._](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)

[**Three Ways to Reverse a String in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Reverse a String”_](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Three Ways to Factorialize a Number in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Factorialize a Number”_](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)

[**Two Ways to Check for Palindromes in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Check for Palindromes”._](https://www.freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7/)

[**Three Ways to Title Case a Sentence in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Title Case a Sentence”._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

[**Three ways you can find the largest number in an array using JavaScript**  
_In this article, I’m going to explain how to solve Free Code Camp’s “Return Largest Numbers in Arrays” challenge. This…_](https://www.freecodecamp.org/news/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1/)

If you have your own solution or any suggestions, share them below in the comments.

Or you can follow me on [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** and [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), right after you click the green heart below ;-)

‪#‎StayCurious‬, ‪#‎KeepOnHacking‬ & ‪#‎MakeItHappen‬!

### Resources

* [split() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
* [sort() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
* [reduce() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)
* [String.length — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
* [for — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for)

