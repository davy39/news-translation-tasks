---
title: JavaScript Array.some() Tutorial – How to Iterate Through Elements in an Array
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-09-07T22:14:16.000Z'
originalURL: https://freecodecamp.org/news/javascript-array-some-tutorial-how-to-iterate-through-elements-in-an-array
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/array-some.png
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'When you''re working with an array in JavaScript, sometimes you might just
  want to check if at least one element inside that array passes a test. And you might
  not care about any other subsequent matches.

  In such a case, you should use the some() Java...'
---

When you're working with an array in JavaScript, sometimes you might just want to check if **at least one** element inside that array passes a test. And you might not care about any other subsequent matches.

In such a case, you should use the `some()` JavaScript method. So let's see how it works.

## How to Use the Array.some() JavaScript Method

The `some()` method is an `Array.propotype` (built-in) method which takes in a callback function and will test that function on each iteration against the current item.

If any elements in the array pass the test specified in the callback, the method stops iterating and returns `true`. If no elements pass the test, the method returns `false`.

The method takes in three parameters:

* `currentItem`: This is the element inside of the array which is currently being iterated over
    
* `index`: This is the index position of the `currentItem` inside of the array
    
* `array`: This represents the array collection to which the `some()` method is bound
    

A simple way to understand the main idea behind `Array.some()` method is to consider one of our biggest propensities as humans: **generalization**. People tend to make generalizations based on just one single experience or perception.

For example, if a certain person from a certain place behaves a certain way, a lot of people will assume that everyone from that place also behaves the same way. Even though such an assumption was based on just one single experience.

The `some()` method essentially **makes up its mind** the moment it finds a match, and returns `true`.

## How to Use Array.some() in Your JavaScript

In the following examples, we will be taking a practical look at how we can use the `some()` method inside our JavaScript.

### How to test for at least one match with `some()`

In this example, we will check if there is at least one male inside of the `people` array

```js
let people = [{
    name: "Anna",
    sex: "Female"
  },

  {
    name: "Ben",
    sex: "Male"
  },

  {
    name: "Cara",
    sex: "Female"
  },
  
  {
    name: "Danny",
    sex: "Female"
  }
  
]


function isThereMale(person) {
	return person.sex === "Male"
}

console.log(people.some(person => isThereMale(person)) // true
```

Since a male actually exists, the `some()` method returns true.

Even if we were to define two males inside the array, the method will still return `true`. The method doesn't care if there is a second male or not, all it cares about is the first one.

```js
let people = [{
    name: "Anna",
    sex: "Female"
  },

  {
    name: "Ben",
    sex: "Male"
  },

  {
    name: "Cara",
    sex: "Female"
  },
  
  {
    name: "Danny",
    sex: "Female"
  },
  
  {
    name: "Ethan",
    sex: "Male"
  }
  
]


function isThereMale(person) {
	return person.sex === "Male"
}

console.log(people.some(person => isThereMale(person)) // true
```

If all items within an array fail the callback test, the `some()` method will return `false`.

In this example, since there is no male inside of our people array, `false` will be returned instead:

```js
let people = [{
    name: "Anna",
    sex: "Female"
  },

  {
    name: "Bella",
    sex: "Female"
  },

  {
    name: "Cara",
    sex: "Female"
  },
  
  {
    name: "Danny",
    sex: "Female"
  },
  
  {
    name: "Ella",
    sex: "Female"
  }
  
]


function isThereMale(person) {
		return person.sex === "Male"
}

console.log(people.some(person => isThereMale(person))) // false
```

### How to use the index parameter with `some()`

The callback function defined inside `some()` can access the index property of every item being iterated over. The index is just a numerical value that uniquely identifies the position of each and every element inside an array. That way, you can refer to any element in the array by its index.

Here, we use the index value to construct a message which we log onto the console:

```js
let people = [{
    name: "Anna",
    sex: "Female"
  },

  {
    name: "Ben",
    sex: "Male"
  },

  {
    name: "Cara",
    sex: "Female"
  },
  
  {
    name: "Danny",
    sex: "Female"
  },
  
  {
    name: "Ethan",
    sex: "Male"
  }
  
]


function isThereMale(person, index) {
		if (person.sex === "Male") console.log(`No ${index+1}, which is ${person.name}, is a Male`)
		return person.sex === "Male"
}

console.log(people.some((person, index) => isThereMale(person, index)))

/* 
"No 2, which is Ben, is a Male"

true
*/
```

## How to Use the Context Object with `some()`

In addition to the callback function, `some()` can also take in a context object.

```js
some(callbackFn, contextObj)
```

We can then refer to the object from inside the **callback** function on each iteration, using `this` as a reference. This allows us to access any properties or methods defined inside the context object.

### Example of using the context object with `some()`

In this example, we are looking to check if at least one person in the people array is a **tricenarian**. That is, the person's age falls between 30 and 39.

We can define the rule inside the `conditions` object and then access it from inside the callback function using the `this.property` notation. We then perform a check to determine if at least one person matches the criteria.

```js
let people = [{
    name: "Anna",
    age: 20
  },

  {
    name: "Ben",
    age: 35
  },

  {
    name: "Cara",
    age: 8
  },
  
  {
    name: "Danny",
    age: 17
  },
  
  {
    name: "Ethan",
    age: 28
  }
  
]

let conditions = {
	lowerAge: 30,
  upperAge: 39
}



console.log(people.some(person => function(person) {
	return person.age >= this.lowerAge && person.age <= this.upperAge
}, conditions)) // true
```

Since one person (Ben) falls in that range, `some()` will return `true`.

## **Wrapping Up**

The `some()` method is an `Array.prototype` method which takes in a callback function and calls that function for every item within the bound array.

When an item passes the callback test, the method will return `true` and stop the loop. Otherwise, it returns `false`.

In addition to the callback function, the `some()` method can also take in a context object as the second argument. This will enable you to access any of its properties from the callback function using `this`.

I hope you got something useful from this article.

**I**f you want to learn more about Web Development, feel free to visit my\*\*\*\* [blog\*\*.\*\*](https://ubahthebuilder.tech/the-ultimate-tutorial-on-javascript-dom-js-dom-with-examples)

Thank you for reading and see you soon.

> **P/S**: If you are learning JavaScript, I created an eBook which teaches 50 topics in JavaScript with hand-drawn digital notes. [Check it out here](https://ubahthebuilder.gumroad.com/l/js-50).
