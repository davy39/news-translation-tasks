---
title: Two Ways to Check for Palindromes in JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-03-22T11:23:37.000Z'
originalURL: https://freecodecamp.org/news/two-ways-to-check-for-palindromes-in-javascript-64fea8191fd7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gaAkSMf6J7cMTJCgQVX2Kg.jpeg
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
seo_desc: 'This article is based on Free Code Camp Basic Algorithm Scripting “Check
  for Palindromes”.

  A palindrome is a word, phrase, number, or other sequence of characters which reads
  the same backward or forward. The word “palindrome” was first coined by the...'
---

_This article is based on Free Code Camp Basic Algorithm Scripting “[Check for Palindromes](https://www.freecodecamp.com/challenges/check-for-palindromes)”._

**A palindrome** is a word, phrase, number, or other sequence of characters which reads the same backward or forward. The word “palindrome” was first coined by the English playwright [Ben Jonson](https://en.wikipedia.org/wiki/Ben_Jonson) in the 17th century, from the Greek roots _palin_ (“again”) and _dromos_ (“way, direction”). — _src. Wikipedia_

In this article, I’m going to explain two approaches, first with built-in functions and second using a for loop.

#### Algorithm Challenge

> Return true if the given string is a palindrome. Otherwise, return false.  
>   
> A palindrome is a word or sentence that’s spelled the same way both forward and backward, ignoring punctuation, case, and spacing.  
>   
> **Note.** You’ll need to remove **all non-alphanumeric characters** (punctuation, spaces and symbols) and turn everything lower case in order to check for palindromes.  
>   
> We’ll pass strings with varying formats, such as “racecar”, “RaceCar”, and “race CAR” among others.

```js
function palindrome(str) {
  return true;
}
palindrome("eye");
```

#### _Provided test cases_

* **_palindrome(“race car”)_** should return true
* **_palindrome(“not a palindrome”)_** should return false
* **_palindrome(“A man, a plan, a canal. Panama”)_** should return true
* **_palindrome(“never odd or even”)_** should return true
* **_palindrome(“nope”)_** should return false
* **_palindrome(“almostomla”)_** should return false
* **_palindrome(“My age is 0, 0 si ega ym.”)_** should return true
* **_palindrome(“1 eye for of 1 eye.”)_** should return false
* **_palindrome(“0_0 (: /-\ :) 0–0”)_** should return true

### Which **Regular Expression** will we need to pass the last test case?

Regular expressions are patterns used to match character combinations in strings.

When the search for a match requires something more than a direct match, the pattern includes special characters.

```
To pass the last test case, we can use two Regular Expressions:

/[^A-Za-z0–9]/g  or

/[\W_]/g
```

**\W** removes **all non-alphanumeric characters**:

* **\W** matches any non-word character
* **\W** is equivalent to [^A-Za-z0–9_]
* **\W** matches anything that is not enclosed in the brackets

What does that mean?

```
[^A-Z] matches anything that is not enclosed between A and Z

[^a-z] matches anything that is not enclosed between a and z

[^0-9] matches anything that is not enclosed between 0 and 9

[^_] matches anything that does not enclose _
```

But in our test case, we need palindrome(“**0_0 (: /-\ :) 0–0**”) to return **true**, which means “**_(: /-\ :)–**” has to be matched.

We will need to add “**_**” to pass this specific test case.

```
We now have “\W_”
```

We will also need to add the **g** flag for global search.

```
We finally have “/[\W_]/g”
```

> **_/[\W_]/g_** _was used for pure demonstrative purpose to show how RegExp works. **/[^A-Za-z0–9]/g** is the easiest RegExp to choose**.**_

### 1. Check for Palindromes With Built-In Functions

For this solution, we will use several methods:

* The **toLowerCase()** method to return the calling string value converted to lowercase.
* The **replace()** method to return a new string with some or all matches of a pattern replaced by a replacement. We will use one of the RegExp we just created earlier.
* The **split()** method splits a String object into an array of strings by separating the string into sub strings.
* The **reverse()** method reverses an array in place. The first array element becomes the last and the last becomes the first.
* The **join()** method joins all elements of an array into a string.

```js
function palindrome(str) {
  // Step 1. Lowercase the string and use the RegExp to remove unwanted characters from it
  var re = /[\W_]/g; // or var re = /[^A-Za-z0-9]/g;
  
  var lowRegStr = str.toLowerCase().replace(re, '');
  // str.toLowerCase() = "A man, a plan, a canal. Panama".toLowerCase() = "a man, a plan, a canal. panama"
  // str.replace(/[\W_]/g, '') = "a man, a plan, a canal. panama".replace(/[\W_]/g, '') = "amanaplanacanalpanama"
  // var lowRegStr = "amanaplanacanalpanama";
     
  // Step 2. Use the same chaining methods with built-in functions from the previous article 'Three Ways to Reverse a String in JavaScript'
  var reverseStr = lowRegStr.split('').reverse().join(''); 
  // lowRegStr.split('') = "amanaplanacanalpanama".split('') = ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"]
  // ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"].reverse() = ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"]
  // ["a", "m", "a", "n", "a", "p", "l", "a", "n", "a", "c", "a", "n", "a", "l", "p", "a", "n", "a", "m", "a"].join('') = "amanaplanacanalpanama"
  // So, "amanaplanacanalpanama".split('').reverse().join('') = "amanaplanacanalpanama";
  // And, var reverseStr = "amanaplanacanalpanama";
   
  // Step 3. Check if reverseStr is strictly equals to lowRegStr and return a Boolean
  return reverseStr === lowRegStr; // "amanaplanacanalpanama" === "amanaplanacanalpanama"? => true
}
 
palindrome("A man, a plan, a canal. Panama");
```

#### Without comments:

```js
function palindrome(str) {
  var re = /[\W_]/g;
  var lowRegStr = str.toLowerCase().replace(re, '');
  var reverseStr = lowRegStr.split('').reverse().join(''); 
  return reverseStr === lowRegStr;
}
palindrome("A man, a plan, a canal. Panama");
```

### 2. Check for Palindromes With a FOR loop

Half-indexing (len/2) has benefits when processing large strings. We check the end from each part and divide the number of iterations inside the FOR loop by two.

```js
function palindrome(str) {
 // Step 1. The first part is the same as earlier
 var re = /[^A-Za-z0-9]/g; // or var re = /[\W_]/g;
 str = str.toLowerCase().replace(re, '');

 // Step 2. Create the FOR loop
 var len = str.length; // var len = "A man, a plan, a canal. Panama".length = 30
 
 for (var i = 0; i < len/2; i++) {
   if (str[i] !== str[len - 1 - i]) { // As long as the characters from each part match, the FOR loop will go on
       return false; // When the characters don't match anymore, false is returned and we exit the FOR loop
   }
   /* Here len/2 = 15
      For each iteration: i = ?    i < len/2    i++    if(str[i] !== str[len - 1 - i])?
      1st iteration:        0        yes         1     if(str[0] !== str[15 - 1 - 0])? => if("a"  !==  "a")? // false
      2nd iteration:        1        yes         2     if(str[1] !== str[15 - 1 - 1])? => if("m"  !==  "m")? // false      
      3rd iteration:        2        yes         3     if(str[2] !== str[15 - 1 - 2])? => if("a"  !==  "a")? // false  
      4th iteration:        3        yes         4     if(str[3] !== str[15 - 1 - 3])? => if("n"  !==  "n")? // false  
      5th iteration:        4        yes         5     if(str[4] !== str[15 - 1 - 4])? => if("a"  !==  "a")? // false
      6th iteration:        5        yes         6     if(str[5] !== str[15 - 1 - 5])? => if("p"  !==  "p")? // false
      7th iteration:        6        yes         7     if(str[6] !== str[15 - 1 - 6])? => if("l"  !==  "l")? // false
      8th iteration:        7        yes         8     if(str[7] !== str[15 - 1 - 7])? => if("a"  !==  "a")? // false
      9th iteration:        8        yes         9     if(str[8] !== str[15 - 1 - 8])? => if("n"  !==  "n")? // false
     10th iteration:        9        yes        10     if(str[9] !== str[15 - 1 - 9])? => if("a"  !==  "a")? // false
     11th iteration:       10        yes        11    if(str[10] !== str[15 - 1 - 10])? => if("c" !==  "c")? // false
     12th iteration:       11        yes        12    if(str[11] !== str[15 - 1 - 11])? => if("a" !==  "a")? // false
     13th iteration:       12        yes        13    if(str[12] !== str[15 - 1 - 12])? => if("n" !==  "n")? // false
     14th iteration:       13        yes        14    if(str[13] !== str[15 - 1 - 13])? => if("a" !==  "a")? // false
     15th iteration:       14        yes        15    if(str[14] !== str[15 - 1 - 14])? => if("l" !==  "l")? // false
     16th iteration:       15        no               
    End of the FOR Loop*/
 }
 return true; // Both parts are strictly equal, it returns true => The string is a palindrome
}

palindrome("A man, a plan, a canal. Panama");
```

#### Without comments:

```js
function palindrome(str) {
 var re = /[^A-Za-z0-9]/g;
 str = str.toLowerCase().replace(re, '');
 var len = str.length;
 for (var i = 0; i < len/2; i++) {
   if (str[i] !== str[len - 1 - i]) {
       return false;
   }
 }
 return true;
}
palindrome("A man, a plan, a canal. Panama");
```

I hope you found this helpful. This is part of my “How to Solve FCC Algorithms” series of articles on the Free Code Camp Algorithm Challenges, where I propose several solutions and explain step-by-step what happens under the hood.

[**Two ways to confirm the ending of a String in JavaScript**  
_In this article, I’ll explain how to solve freeCodeCamp’s “Confirm the Ending” challenge._](https://www.freecodecamp.org/news/two-ways-to-confirm-the-ending-of-a-string-in-javascript-62b4677034ac/)

[**Three Ways to Reverse a String in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Reverse a String”_](https://www.freecodecamp.org/news/how-to-reverse-a-string-in-javascript-in-3-different-ways-75e4763c68cb/)

[**Three Ways to Factorialize a Number in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Factorialize a Number”_](https://www.freecodecamp.org/news/how-to-factorialize-a-number-in-javascript-9263c89a4b38/)

[**Three Ways to Find the Longest Word in a String in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Find the Longest Word in a String”._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Three Ways to Title Case a Sentence in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Title Case a Sentence”._](https://www.freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27/)

[**Three ways you can find the largest number in an array using JavaScript**  
_In this article, I’m going to explain how to solve Free Code Camp’s “Return Largest Numbers in Arrays” challenge. This…_](https://www.freecodecamp.org/news/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1/)

If you have your own solution or any suggestions, share them below in the comments.

Or you can follow me on [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** and [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset), right after you click the green heart below ;-)

‪#‎StayCurious‬, ‪#‎KeepOnHacking‬ & ‪#‎MakeItHappen‬!

### Resources

* [Regular Expressions — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Guide/Regular_Expressions)
* [toLowerCase() method — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
* [replace() — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
* [split() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
* [reverse() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)
* [join() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
* [String.length — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length)
* [for — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for)

