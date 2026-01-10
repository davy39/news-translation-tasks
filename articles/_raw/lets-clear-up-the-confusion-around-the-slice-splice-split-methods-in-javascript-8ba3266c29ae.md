---
title: Let’s clear up the confusion around the slice( ), splice( ), & split( ) methods
  in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-09T17:57:55.000Z'
originalURL: https://freecodecamp.org/news/lets-clear-up-the-confusion-around-the-slice-splice-split-methods-in-javascript-8ba3266c29ae
coverImage: https://cdn-media-1.freecodecamp.org/images/0*QaNtLL7jbyw3062_
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Cem Eygi

  JavaScript built-in methods help us a lot while programming, once we understand
  them correctly. I would like to explain three of them in this article: the slice(),
  splice() and split() methods. Perhaps because their naming is so similar t...'
---

By Cem Eygi

JavaScript built-in methods help us a lot while programming, once we understand them correctly. I would like to explain three of them in this article: the **`slice()`**, **`splice()`** and **`split()`** methods. Perhaps because their naming is so similar they are often confused, even among experienced developers.

**I advise students and junior developers to read this article carefully because these three methods can also be asked in JOB INTERVIEWS.**

You can find a summary of each method in the end. If you prefer, you can also watch the video version below:

%[https://youtu.be/alFcHCWwS0I]

So let’s start…

### JavaScript Arrays

Firstly, you need to understand how **JavaScript arrays** work. Like in other programming languages, we use arrays to store multiple data in JS. But the difference is that **JS** **arrays can contain different type of data at once.**

Sometimes we need to do operations on those arrays. Then we use some JS methods like **slice () & splice ()**. You can see below how to declare an array in JavaScript:

`let arrayDefinition = [];   // Array declaration in JS`

Now let’s declare another array with different data types. I will use it below in examples:

`let array = [1, 2, 3, "hello world", 4.12, true];`

This usage is **valid** in JavaScript. An array with different data types: string, numbers, and a boolean.

### Slice ( )

The **slice( )** method **copies** a given part of an array and returns that copied part as a new array. **It doesn’t change the original array.**

`array.slice(from, until);`

* **From:** Slice the array starting **from** an element index
* **Until:** Slice the array **until** another element index

For example, I want to slice the first three elements from the array above. Since the first element of an array is always indexed at 0, I start slicing **“from”**0.

`array.slice(0, until);`

Now here is the tricky part. When I want to slice the first three elements, I must give the **until** parameter as 3. **The** **slice( ) method doesn’t include the last given element.**

```
array[0] --> 1              // included
array[1] --> 2              // included
array[2] --> 3              // included
array[3] --> "hello world"  // not included
```

This can create some confusion. That’s why I call the second parameter **“until”.**

`let newArray = array.slice(0, 3);   // Return value is also an array`

Finally, I assign the sliced Array to the **newArray** variable. Now let’s see the result:

![Image](https://cdn-media-1.freecodecamp.org/images/1*UECVH_JWknae04kVqTr1gg.png)
_Slice <strong class="markup--strong markup--figure-strong" style="font-weight: 700;">array** and assign the members to <strong class="markup--strong markup--figure-strong" style="font-weight: 700;">newArray**_

![Image](https://cdn-media-1.freecodecamp.org/images/1*YImz2x-CAY-8wqoyT8c6eA.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">newArray** variable is an array now, and the original one remains the same_

> _Important Note: the **Slice( )**_ method can also be used for **strings.**

### Splice ( )

The name of this function is very similar to **slice( )**. This naming similarity often confuses developers. The **splice( )** method **changes** an array, by adding or removing elements from it. Let’s see how to add and remove elements with **splice(** **)**:

#### Removing Elements

For removing elements, we need to give the **index** parameter, and the **number of elements** to be removed:

`array.splice(index, number of elements);`

**Index** is the **starting point** for removing elements. Elements which have a **smaller** index number from the given index won’t be removed:

`array.splice(2);  // Every element starting from index 2, will be removed`

If we don’t define the second parameter, every element starting from the given index will be removed from the array:

![Image](https://cdn-media-1.freecodecamp.org/images/1*OGTbYRkU4C_5iMF5Sw9lBA.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">only index 0 and 1 are still there**_

As a second example, I give the second parameter as 1, so elements starting from index 2 will be removed one by one each time we call the **splice ( )**method:

`array.splice(2, 1);`

![Image](https://cdn-media-1.freecodecamp.org/images/1*uCZHAfeq46dG182y6oHrpg.png)
_Array at beginning_

**After 1st call:**

![Image](https://cdn-media-1.freecodecamp.org/images/1*gMh3g8RLvpAjMGxgfanB8w.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">3** is removed so <strong class="markup--strong markup--figure-strong" style="font-weight: 700;">“hello world”** has now index 2_

**After 2nd call:**

![Image](https://cdn-media-1.freecodecamp.org/images/1*6YWBPU0UsPeoJTcwn8-gWg.png)
_This time, <strong class="markup--strong markup--figure-strong" style="font-weight: 700;">“hello world”** is removed as <strong class="markup--strong markup--figure-strong" style="font-weight: 700;">index: 2**_

This can continue until there is no index 2 anymore.

#### Adding Elements

For adding elements, we need to give them as the 3rd, 4th, 5th parameter (depends on how many to add) to the **splice ( )** method:

array.splice(index, number of elements, element, element);

As an example, I’m adding **a** and **b** in the very beginning of the array and I remove nothing:

`array.splice(0, 0, 'a', 'b');`

![Image](https://cdn-media-1.freecodecamp.org/images/1*E7TMFWTYGJDkuhG3VrTCKw.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">a** and<strong class="markup--strong markup--figure-strong" style="font-weight: 700;"> b** added to the beginning of array, no elements removed_

### Split ( )

**Slice( )** and **splice( )** methods are for arrays. The **split( )** method is used for **strings**. It divides a string into substrings and returns them as an array. It takes 2 parameters, and both are **optional.**

`string.split(separator, limit);`

* **Separator:** Defines how to split a string… by a comma, character etc.
* **Limit:** Limits the number of splits with a given number

The **split( )** method doesn’t work directly for **arrays**. However, we can first convert the elements of our array to a string, then we can use the **split( )** method.

Let’s see how it works.

Firstly, we convert our array to a string with **toString( )** method:

`let myString = array.toString();`

![Image](https://cdn-media-1.freecodecamp.org/images/1*JW9u0vQSmZM6wQ540w3eTg.png)

Now let’s split **myString** by **commas,** limit them to **three** substrings, and return them as an array:

`let newArray = myString.split(",", 3);`

![Image](https://cdn-media-1.freecodecamp.org/images/1*v53Ct4WVDXNsCjzDAtpc_g.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">Only the first 3 elements are returned**_

As we can see, **myString** is split by commas. Since we limit split to 3, only the first 3 elements are returned.

> _**NOTE:**_ If we have a usage like this: `_array.split("");_` then each character of the string will be divided as substrings:

![Image](https://cdn-media-1.freecodecamp.org/images/1*s7RYTgCHVGzZKXDJZYyjaQ.png)
_<strong class="markup--strong markup--figure-strong" style="font-weight: 700;">Each character split one by one**_

### Summary:

#### Slice ( )

* Copies elements from an array
* Returns them as a new array
* Doesn’t change the original array
* Starts slicing from … until given index: **array.slice (from, until)**
* Slice doesn’t include **“until”** index parameter
* Can be used both for arrays and strings

#### Splice ( )

* Used for adding/removing elements from array
* Returns an array of removed elements
* Changes the array
* For adding elements: **array.splice (index, number of elements, element)**
* For removing elements: **array.splice (index, number of elements)**
* Can only be used for arrays

#### Split ( )

* Divides a string into substrings
* Returns them in an array
* Takes 2 parameters, both are optional: **string.split(separator, limit)**
* Doesn’t change the original string
* Can only be used for strings

There are many other built-in methods for JavaScript arrays and strings, which make easier to work with JavaScript programming. Next, you can check out my new article about [JavaScript Substring Methods](https://www.freecodecamp.org/news/javascript-substring-examples-slice-substr-and-substring-methods-in-js/).

**If you want to learn more about web development, feel free to** [**follow me on Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)**!**

Thank you for reading!

