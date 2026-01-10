---
title: JavaScript Array.filter() Tutorial – How to Iterate Through Elements in an
  Array
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-08-26T16:07:48.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-filter-tutorial-how-to-iterate-through-elements-in-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/filter-cover.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'The Array.filter() method is arguably the most important and widely used
  method for iterating over an array in JavaScript.

  The way the filter() method works is very simple. It entails filtering out one or
  more items (a subset) from a larger collectio...'
---

The `Array.filter()` method is arguably the most important and widely used method for iterating over an array in JavaScript.

The way the `filter()` method works is very simple. It entails filtering out one or more items (a subset) from a larger collection of items (a superset) based on some condition/preference.

We all do this everyday, whether we're reading, choosing friends or our spouse, choosing what movie to watch, and so on.

## The JavaScript `Array.filter()` Method

The `filter()` method takes in a callback function and calls that function for every item it iterates over inside the target array. The callback function can take in the following parameters:

* `currentItem`: This is the element in the array which is currently being iterated over.
    
* `index`: This is the index position of the `currentItem` inside the array.
    
* `array`: This represents the target array along with all its items.
    

The filter method creates a new array and returns all of the items which pass the condition specified in the callback.

## How to Use the `filter()` Method in JavaScript

In the following examples, I will demonstrate how you can use the `filter()` method to filter items from an array in JavaScript.

### `filter()` Example 1: How to filter items out of an array

In this example, we filter out every person who is a toddler (whose age falls between 0 and 4 ).

```js
let people = [
    {name: "aaron",age: 65},
    {name: "beth",age: 2},
    {name: "cara",age: 13},
    {name: "daniel",age: 3},
    {name: "ella",age: 25},
    {name: "fin",age: 1},
    {name: "george",age: 43},
]

let toddlers = people.filter(person => person.age <= 3)

console.log(toddlers)



/*
[{
  age: 2,
  name: "beth"
}, {
  age: 3,
  name: "daniel"
}, {
  age: 1,
  name: "fin"
}]
*/
```

### `filter()` Example 2: How to filter out items based on a particular property

In this example, we will only be filtering out the team members who are developers.

```js
let team = [
	{
  		name: "aaron",
    	position: "developer"
 	 },
  	{
  		name: "beth",
    	position: "ui designer"
  	},
  	{
  		name: "cara",
    	position: "developer"
  	},
 	{
  		name: "daniel",
    	position: "content manager"
 	 },
  	{
  		name: "ella",
    	position: "cto"
  	},
  	{
  		name: "fin",
    	position: "backend engineer"
  	},
  	{
  		name: "george",
    	position: "developer"
  },

]

let developers = team.filter(member => member.position == "developer")

console.log(developers)


/*
[{
  name: "aaron",
  position: "developer"
}, {
  name: "cara",
  position: "developer"
}, {
  name: "george",
  position: "developer"
}]
*/
```

In the above example, we filtered out the developers. But what if we want to filter out every member who is **not** a developer instead?

We could do this:

```js
let team = [
	{ 
        name: "aaron",
   		position: "developer"
  	},
  	{
  		name: "beth",
   		position: "ui designer"
 	 },
  	{
  		name: "cara",
    	position: "developer"
  	},
  	{
  		name: "daniel",
    	position: "content manager"
  	},
  	{
  		name: "ella",
    	position: "cto"
  	},
  	{
  		name: "fin",
    	position: "backend engineer"
  	},
  	{
  		name: "george",
    	position: "developer"
  	},

]

let nondevelopers = team.filter(member => member.position !== "developer")

console.log(nondevelopers)


/*
[
    {
  		name: "beth",
  		position: "ui designer"
	}, 
    {
  		name: "daniel",
  		position: "content manager"
	}, 
    {
  		name: "ella",
  		position: "cto"
	}, 
    {
  		name: "fin",
  		position: "backend engineer"
	}
]

*/
```

### `filter()` Example 3: How to access the index property

This is a competition. In this competition, there are three winners. The first will get the gold medal, the second will get silver, and the third, bronze.

By using `filter` and accessing the `index` property of every item on each iteration, we can filter out each of the three winners into different variables.

```js
let winners = ["Anna", "Beth", "Cara"]

let gold = winners.filter((winner, index) => index == 0)
let silver = winners.filter((winner, index) => index == 1)
let bronze = winners.filter((winner, index) => index == 2)

console.log(Gold winner: ${gold}, Silver Winner: ${silver}, Bronze Winner: ${bronze})

// "Gold winner: Anna, Silver Winner: Beth, Bronze Winner: Cara"
```

### `filter()` Example 4: How to use the array parameter

One of the most common uses of the third parameter (array) is to inspect the state of the array being iterated over. For example, we can check to see if there is another item left in the array. Depending on the outcome, we can specify that different things should happen.

In this example, we are going to define an array of four people. However, since there can only be three winners, the fourth person in the list will have to be discounted.

To be able to do this, we need to get information about the target array on every iteration.

```js
let competitors = ["Anna", "Beth", "Cara", "David"]

function displayWinners(name, index, array) {
    let isNextItem = index + 1 < array.length ? true : false
    if (isNextItem) {
    	console.log(`The No${index+1} winner is ${name}.`);
    } else {
    	console.log(`Sorry, ${name} is not one of the winners.`)
    }
}

competitors.filter((name, index, array) => displayWinners(name, index, array))

/*
"The No1 winner is Anna."
"The No2 winner is Beth."
"The No3 winner is Cara."
"Sorry, David is not one of the winners."
*/
```

![Image](https://www.freecodecamp.org/news/content/images/2021/08/sorry.png align="left")

*Oops, sorry David!*

### How to Use the Context Object

In addition to the callback function, the `filter()` method can also take in a context object.

```js
filter(callbackfn, contextobj)
```

This object can then be referred to from inside the callback function using the `this` keyword reference.

### `filter()` Example 5: How to access the context object with `this`

This is going to be similar to `example 1`. We are going to be filtering out every person who falls between the ages of 13 and 19 (teenagers).

However, we will not be hardcoding the values inside of the callback function. Instead, we will define these values 13 and 19 as properties inside the `range` object, which we will subsequently pass into `filter` as the context object (second parameter).

```js
let people = [
    {name: "aaron", age: 65},
    {name: "beth", age: 15},
    {name: "cara", age: 13},
    {name: "daniel", age: 3},
    {name: "ella", age: 25},
    {name: "fin", age: 16},
    {name: "george", age: 18},
]

let range = {
  lower: 13,
  upper: 16
}

   
let teenagers = people.filter(function(person) {
	return person.age >= this.lower && person.age <= this.upper;
}, range)

console.log(teenagers)

/*
[{
  age: 15,
  name: "beth"
}, {
  age: 13,
  name: "cara"
}, {
  age: 16,
  name: "fin"
}]
*/
```

We passed the `range` object as a second argument to `filter()`. At that point, it became our context object. Consequently, we were able to access our upper and lower ranges in our callback function with the `this.upper` and `this.lower` reference respectively.

## Wrapping Up

The `filter()` array method filters out item(s) which match the callback expression and returns them.

In addition to the callback function, the `filter` method can also take in a context object as the second argument. This will enable you access any of its properties from the callback function using `this`.

I hope you got something useful from this article.

**I**f you want to learn more about Web Development, feel free to visit my\*\*\*\* [Blog](https://ubahthebuilder.tech/my-top-10-youtube-channels-for-programmers)**.**

Thank you for reading and see you soon.

> **P/S**: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
