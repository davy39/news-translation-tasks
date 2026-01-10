---
title: Three Ways to Title Case a Sentence in JavaScript
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2016-04-07T14:08:35.000Z'
originalURL: https://freecodecamp.org/news/three-ways-to-title-case-a-sentence-in-javascript-676a9175eb27
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YPdTg5Gx1FX66jSc_uwwlQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'This article is based on Free Code Camp Basic Algorithm Scripting “Title
  Case a Sentence”.

  In this algorithm, we want to change a string of text so that it always has a capital
  letter at the start of every word.

  In this article, I’m going to explain ...'
---

_This article is based on Free Code Camp Basic Algorithm Scripting “_[Title Case a Sentence](https://www.freecodecamp.com/challenges/title-case-a-sentence)_”._

**In this algorithm**, we want to change a string of text so that it always has a capital letter at the start of every word.

In this article, I’m going to explain three approaches. First with a FOR loop, second using the map() method, and third using the replace() method.

#### Algorithm Challenge

> Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.  
>   
> For the purpose of this exercise, you should also capitalize connecting words like “the” and “of”.

#### Provided test cases

* **_titleCase(“I’m a little tea pot”)_** should return a string.
* **_titleCase(“I’m a little tea pot”)_** should return “I’m A Little Tea Pot”.
* **_titleCase(“sHoRt AnD sToUt”)_** should return “Short And Stout”.
* **_titleCase(“HERE IS MY HANDLE HERE IS MY SPOUT”)_** should return “Here Is My Handle Here Is My Spout”.

### 1. Title Case a Sentence With a FOR Loop

For this solution, we will use the String.prototype.toLowerCase() method, the String.prototype.split() method, the String.prototype.charAt() method, the String.prototype.slice() method and the Array.prototype.join() method.

* The **toLowerCase()** method returns the calling string value converted to lowercase
* The **split()** method splits a String object into an array of strings by separating the string into substrings.
* The **charAt()** method returns the specified character from a string.
* The **slice()** method extracts a section of a string and returns a new string.
* The **join()** method joins all elements of an array into a string.

We will need to add an empty space between the parenthesis of the **split()**method,

```
var strSplit = "I'm a little tea pot".split(' ');
```

which will output an array of separated words:

```
var strSplit = ["I'm", "a", "little", "tea", "pot"];
```

If you don’t add the space in the parenthesis, you will have this output:

```
var strSplit = ["I", "'", "m", " ", "a", " ", "l", "i", "t", "t", "l", "e", " ", "t", "e", "a", " ", "p", "o", "t"];
```

We will concatenate

```
str[i].charAt(0).toUpperCase()
```

— which will uppercase the index 0 character of the current string in the FOR loop —

and

```
str[i].slice(1)
```

— which will extract from index 1 to the end of the string.

We will set the whole string to lower case for normalization purposes.

#### With comments:

```js

function titleCase(str) {
  // Step 1. Lowercase the string
  str = str.toLowerCase();
  // str = "I'm a little tea pot".toLowerCase();
  // str = "i'm a little tea pot";
  
  // Step 2. Split the string into an array of strings
  str = str.split(' ');
  // str = "i'm a little tea pot".split(' ');
  // str = ["i'm", "a", "little", "tea", "pot"];
  
  // Step 3. Create the FOR loop
  for (var i = 0; i < str.length; i++) {
    str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1); 
  /* Here str.length = 5
    1st iteration: str[0] = str[0].charAt(0).toUpperCase() + str[0].slice(1);
                   str[0] = "i'm".charAt(0).toUpperCase()  + "i'm".slice(1);
                   str[0] = "I"                            + "'m";
                   str[0] = "I'm";
    2nd iteration: str[1] = str[1].charAt(0).toUpperCase() + str[1].slice(1);
                   str[1] = "a".charAt(0).toUpperCase()    + "a".slice(1);
                   str[1] = "A"                            + "";
                   str[1] = "A";
    3rd iteration: str[2] = str[2].charAt(0).toUpperCase()   + str[2].slice(1);
                   str[2] = "little".charAt(0).toUpperCase() + "little".slice(1);
                   str[2] = "L"                              + "ittle";
                   str[2] = "Little";
    4th iteration: str[3] = str[3].charAt(0).toUpperCase() + str[3].slice(1);
                   str[3] = "tea".charAt(0).toUpperCase()  + "tea".slice(1);
                   str[3] = "T"                            + "ea";
                   str[3] = "Tea";
    5th iteration: str[4] = str[4].charAt(0).toUpperCase() + str[4].slice(1);
                   str[4] = "pot".charAt(0).toUpperCase() + "pot".slice(1);
                   str[4] = "P"                           + "ot";
                   str[4] = "Pot";                                                         
    End of the FOR Loop*/
  }
  
  // Step 4. Return the output
  return str.join(' '); // ["I'm", "A", "Little", "Tea", "Pot"].join(' ') => "I'm A Little Tea Pot"
}

titleCase("I'm a little tea pot");
```

#### Without comments:

```js
function titleCase(str) {
  str = str.toLowerCase().split(' ');
  for (var i = 0; i < str.length; i++) {
    str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1); 
  }
  return str.join(' ');
}
titleCase("I'm a little tea pot");
```

### 2. Title Case a Sentence With the map() Method

For this solution, we will use the Array.prototype.map() method.

* The **map()** method creates a new array with the results of calling a provided function on every element in this array. Using map will call a provided callback function once for each element in an array, in order, and constructs a new array from the results.

We will lowercase and split the string as seen in the previous example before applying the map() method.

Instead of using a FOR loop, we will apply the map() method as the condition on the same concatenation from the previous example.

```
(word.charAt(0).toUpperCase() + word.slice(1));
```

#### With comments:

```js

function titleCase(str) {
  // Step 1. Lowercase the string
  str = str.toLowerCase() // str = "i'm a little tea pot";
  
  // Step 2. Split the string into an array of strings
           .split(' ') // str = ["i'm", "a", "little", "tea", "pot"];
         
  // Step 3. Map over the array
           .map(function(word) {
    return (word.charAt(0).toUpperCase() + word.slice(1));
    /* Map process
    1st word: "i'm"    => (word.charAt(0).toUpperCase() + word.slice(1));
                          "i'm".charAt(0).toUpperCase() + "i'm".slice(1);
                                "I"                     +     "'m";
                          return "I'm";
    2nd word: "a"      => (word.charAt(0).toUpperCase() + word.slice(1));
                          "a".charAt(0).toUpperCase()   + "".slice(1);
                                "A"                     +     "";
                          return "A";
    3rd word: "little" => (word.charAt(0).toUpperCase()    + word.slice(1));
                          "little".charAt(0).toUpperCase() + "little".slice(1);
                                "L"                        +     "ittle";
                          return "Little";
    4th word: "tea"    => (word.charAt(0).toUpperCase() + word.slice(1));
                          "tea".charAt(0).toUpperCase() + "tea".slice(1);
                                "T"                     +     "ea";
                          return "Tea";
    5th word: "pot"    => (word.charAt(0).toUpperCase() + word.slice(1));
                          "pot".charAt(0).toUpperCase() + "pot".slice(1);
                                "P"                     +     "ot";
                          return "Pot";                                                        
    End of the map() method */
});

 // Step 4. Return the output
 return str.join(' '); // ["I'm", "A", "Little", "Tea", "Pot"].join(' ') => "I'm A Little Tea Pot"
}

titleCase("I'm a little tea pot");
```

#### Without comments:

```js
function titleCase(str) {
  return str.toLowerCase().split(' ').map(function(word) {
    return (word.charAt(0).toUpperCase() + word.slice(1));
  }).join(' ');
}
titleCase("I'm a little tea pot");
```

### 3. Title Case a Sentence With the map() and the replace() Methods

For this solution, we will keep using the Array.prototype.map() method and add the String.prototype.replace() method.

* The **replace()** method returns a new string with some or all matches of a pattern replaced by a replacement.

In our case, the pattern for the replace() method will be a String to be replaced by a new replacement and will be treated as a verbatim string. We can also use a **regular expression** as the pattern to solve this algorithm.

We will lowercase and split the string as seen in the first example before applying the map() method.

#### With comments:

```js

function titleCase(str) {
  // Step 1. Lowercase the string
  str = str.toLowerCase() // str = "i'm a little tea pot";
  
  // Step 2. Split the string into an array of strings
           .split(' ') // str = ["i'm", "a", "little", "tea", "pot"];
         
  // Step 3. Map over the array
           .map(function(word) {
    return word.replace(word[0], word[0].toUpperCase());
    /* Map process
    1st word: "i'm" => word.replace(word[0], word[0].toUpperCase());
                       "i'm".replace("i", "I");
                       return word => "I'm"
    2nd word: "a" => word.replace(word[0], word[0].toUpperCase());
                     "a".replace("a", "A");
                      return word => "A"
    3rd word: "little" => word.replace(word[0], word[0].toUpperCase());
                          "little".replace("l", "L");
                          return word => "Little"
    4th word: "tea" => word.replace(word[0], word[0].toUpperCase());
                       "tea".replace("t", "T");
                       return word => "Tea"
    5th word: "pot" => word.replace(word[0], word[0].toUpperCase());
                       "pot".replace("p", "P");
                       return word => "Pot"                                                        
    End of the map() method */
});

 // Step 4. Return the output
 return str.join(' '); // ["I'm", "A", "Little", "Tea", "Pot"].join(' ') => "I'm A Little Tea Pot"
}

titleCase("I'm a little tea pot");
```

#### Without comments:

```js
function titleCase(str) {
  return str.toLowerCase().split(' ').map(function(word) {
    return word.replace(word[0], word[0].toUpperCase());
  }).join(' ');
}
titleCase("I'm a little tea pot");
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

[**Three Ways to Find the Longest Word in a String in JavaScript**  
_This article is based on Free Code Camp Basic Algorithm Scripting “Find the Longest Word in a String”._](https://www.freecodecamp.org/news/three-ways-to-find-the-longest-word-in-a-string-in-javascript-a2fb04c9757c/)

[**Three ways you can find the largest number in an array using JavaScript**  
_In this article, I’m going to explain how to solve Free Code Camp’s “Return Largest Numbers in Arrays” challenge. This…_](https://www.freecodecamp.org/news/three-ways-to-return-largest-numbers-in-arrays-in-javascript-5d977baa80a1/)

If you have your own solution or any suggestions, share them below in the comments.

Or you can follow me on [**Medium**](https://medium.com/@sonya.moisset)**, [Twitter](https://twitter.com/SonyaMoisset), [Github](https://github.com/SonyaMoisset)** and [**LinkedIn**](https://www.linkedin.com/in/sonyamoisset)**.**

‪#‎StayCurious‬, ‪#‎KeepOnHacking‬ & ‪#‎MakeItHappen‬!

### Resources

* [toLowerCase() method — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase)
* [toUpperCase() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase)
* [charAt() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt)
* [slice() method — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/String/slice)
* [split() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
* [join() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)
* [for — MDN](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for)
* [map() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
* [replace() method — MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)

