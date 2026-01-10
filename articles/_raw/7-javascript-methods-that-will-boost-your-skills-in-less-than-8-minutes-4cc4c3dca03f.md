---
title: These JavaScript methods will boost your skills in just a few minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-06T10:31:40.000Z'
originalURL: https://freecodecamp.org/news/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H-25KB7EbSHjv70HXrdl6w.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dler Ari

  Most of the applications we build today require some sort of data collection modification.
  Processing items in a collection is a common operation you will most likely encounter.
  Forget the conventional way of doing for-loop like (let i=0;...'
---

By Dler Ari

Most of the applications we build today require some sort of data collection modification. Processing items in a collection is a common operation you will most likely encounter. Forget the conventional way of doing `for-loop` like `(let i=0; i < value.length; i+`+ ).

> Quick heads-up, using `const` in `for-loop` will give you an error. Reason why is because it re-declares the value during each execution hence `i` is modified by `i++`. So whenever you think of either using `const` or `let`, ask yourself — Will this value be re-declared? If the answer is **yes**, go for `let` , and if **no**, go for `const`. [More info](https://stackoverflow.com/questions/41067790/why-does-const-work-in-some-for-loops-in-javascript).

Let’s say you want to show list of products and categorize, filter, search, modify or update a collection. Or maybe you want to perform quick calculations such as sum, multiplication, and so forth. What is the optimal way to achieve this?

Maybe you don’t like **arrow functions**, you don’t want to spend too much time learning something new, or they’re just not relevant for you. Don’t worry, you are not alone. I’ll show you how it is done in ES5 (functional deceleration) and ES6 (arrow functions).

**Be aware:** Arrow functions and function declarations / expressions are not equivalent and cannot be [replaced blindly](https://stackoverflow.com/questions/34361379/arrow-function-vs-function-declaration-expressions-are-they-equivalent-exch?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa). Keep in mind that the `this` keyword works differently between the two.

#### The methods we’ll be looking at:

1. Spread operator
2. for…of iterator
3. includes()
4. some()
5. every()
6. filter()
7. map()
8. reduce()

> If you want to become a better web developer, start your own business, teach others, or improve your development skills, I’ll be posting weekly tips and tricks on the latest web development languages.

### 1. Spread operator

The Spread Operator **expands** an array into its elements. It can also be used for object literals.

**Why should I use it?**

* It’s a simple and fast way to show the items of an array
* It works for arrays and object literals
* It’s a quick and intuitive way to pass arguments
* It only requires three dots…

**Example:**   
Let’s say you want to show a list of favorite foods without creating a loop function. Use a spread operator like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*NPgk0vqyWiXXkNDPMbxujA.png)

### 2. for…of iterator

The `for...of` statement loops/iterates through the collection, and provides you the ability to modify specific items. It replaces the conventional way of doing a `for-loop`.

**Why should I use it?**

* It’s a simple way to add or update an item
* To perform calculations (sum, multiplication etc)
* When using conditional statements (if, while, switch, and so on)
* Leads to clean and readable code

**Example:**   
Let’s say you have a toolbox, and you want to show all the tools inside it. The `for...of` iterator makes it easy.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kjQYvjeeHUuP8inZYqjJVg.png)
_for…of operator_

### 3. Includes() method

The `includes()` method is used to check if a specific string exists in a collection, and returns `true` or `false`. Keep in mind that it is case sensitive: if the item inside the collection is `SCHOOL`, and you search for `school`, it will return `false`.

**Why should I use it?**

* To build simple search-functionality
* It’s an intuitive approach to determine if a string exists
* It uses conditional statements to modify, filter, and so on
* Leads to readable code

**Example:**  
Let’s say for whatever reason that you are not aware of what cars you have in your garage, and you need a system to check if the car you want exists or not. `includes()`to the rescue!

![Image](https://cdn-media-1.freecodecamp.org/images/1*m1InU7VDxdfpxMXuV2A1MA.png)
_includes() method w/ arrow function_

### 4. Some() method

The `some()` method checks if some elements exists in an array, and returns `true` or `false`. This is somewhat similar to the concept of the `includes()` method, except the argument is a function and not a string.

**Why should I use it?**

* It makes sure **some** item passes the test
* It performs conditional statements using functions
* Make your code declarative
* Some is good enough

**Example:**   
Let’s say you are a club owner, and don’t care who enters the club. But some are not allowed in, because they have been drinking too much (my creativity at its best). Check out the differences between ES5 and ES6 below:

#### ES5:

![Image](https://cdn-media-1.freecodecamp.org/images/1*-5YnlNy48wi0FHnIG3bXDg.png)
_some() method_

#### ES6:

![Image](https://cdn-media-1.freecodecamp.org/images/1*pmaXrKpg5vI__WwztfATGg.png)
_some() method w/ arrow function_

### 5. Every() method

The `every()` method loops through the array, checks every item, and returns `true` or `false`. Same concept as `some()`. Except every item must satisfy the conditional statement, otherwise, it will return `false`.

**Why should I use it?**

* It makes sure **every** item passes the test
* You can perform conditional statements using functions
* Make your code declarative

**Example:**   
The last time you allowed `some()` underage students to enter the club, someone reported this and the police caught you. This time you won’t let that happen, and you’ll make sure that **everyone** passes the age limit with the `every()`operator.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/1*DNQqzRJ_K01ognj3_c8HqQ.png)
_every() method_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/1*avukLSBlIG1ycSzoHLMOYA.png)
_every() method w/ arrow function_

### 6. Filter() method

The `filter()` method creates a new array with all elements that pass the test.

**Why should I use it?**

* So you can avoid changing the main array
* It lets you filter out items you do not need
* Gives you more readable code

**Example:**   
Let’s say you want to return only prices that are above or equal to 30. Filter out all those other prices…

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/1*O9EhGZRxC1DWan0822fKvQ.png)
_filter() method_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/1*1C22z5zvw_Gw_SiJnLuTig.png)
_filter() method w/ arrow function_

### 7. Map() method

The `map()` method is similar to the `filter()` method in terms of returning a new array. However, the only difference is that it is used to modify items.

**Why should I use it?**

* It lets you avoid making changes to the main array
* You can modify the items you want
* Gives you more readable code

**Example:**   
Let’s say you have a list of products with prices. Your manager needs a list to show the new prices after they have been taxed by 25%. The `map()` method can help you out.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/1*iIOcN4rc6r-55YWrHQVNHw.png)
_map() method_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/1*s2ePAwDuw-qJOju7WAm9Uw.png)
_map() method w/ arrow function_

### 8. Reduce() method

The `reduce()` method can be used to transform an array into something else, which could be an integer, an object, a chain of promises ( sequential execution of promises) etc. For practical reasons, a simple use case would be to sum a list of integers. In short, it “reduces” the whole array into one value.

**Why should I use it?**

* Perform calculations
* Calculate a value
* Count duplicates
* Group objects by property
* Execute promises sequentially
* It’s a quick way to perform calculations

**Example:**   
Let’s say you want to find out your total expenses for a week. Use `reduce()` to get that value.

#### ES5

![Image](https://cdn-media-1.freecodecamp.org/images/1*OX1oPjVVoPXfIsAqHD3TTQ.png)
_reduce() method_

#### ES6

![Image](https://cdn-media-1.freecodecamp.org/images/1*DGa7HZwy40o71B4_ICP6kQ.png)
_reduce() method w/ arrow function_

You can find me on Developer News where I publish every week. Or you can follow me on [Twitter](http://twitter.com/dleroari), where I post relevant web development tips and tricks.

