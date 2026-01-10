---
title: How to Solve freeCodeCamp's Record Collection Challenge
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-03-21T18:14:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-the-record-collection-challenge
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/fili-santillan-qp51FQhBnS0-unsplash.jpg
tags:
- name: challenge
  slug: challenge
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'freeCodeCamp''s JavaScript certification is filled with hundreds of interactive
  challenges. But one of the hardest ones to tackle for most beginners is the Record
  Collection.

  In this article, I will walk you through Record Collection and help you unde...'
---

[freeCodeCamp's JavaScript certification](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) is filled with hundreds of interactive challenges. But one of the hardest ones to tackle for most beginners is the [Record Collection](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection).

In this article, I will walk you through [Record Collection](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection) and help you understand how all of the pieces of the challenge work. 

## How to understand the function parameters

Parameters are special types of variables that are passed into the function and act as placeholders for the real values. When the function is called, then we will use the real values which are known as arguments. 

 This is an example of [Record Collection](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection)'s function parameters.

```js
function updateRecords(records, id, prop, value)
```

The `records` parameter represents an object literal. Here is the object literal from the challenge:

```js
const recordCollection = {
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
  2468: {
    albumTitle: '1999',
    artist: 'Prince',
    tracks: ['1999', 'Little Red Corvette']
  },
  1245: {
    artist: 'Robert Palmer',
    tracks: []
  },
  5439: {
    albumTitle: 'ABBA Gold'
  }
};
```

The `id` parameter represents the objects nested inside our `recordCollection` object. This is an example for one of the ids. 

```js
  2548: {
    albumTitle: 'Slippery When Wet',
    artist: 'Bon Jovi',
    tracks: ['Let It Rock', 'You Give Love a Bad Name']
  },
```

The `prop` parameter represents the property name, or key, inside the objects. `albumTitle`, `artist`, and `tracks` are all examples of properties inside the `id` objects. 

The `value` parameter represents the value in the object's property. In the example below, `albumTitle` would be the property name, or key, while `ABBA Gold` would be the value.

```js
albumTitle: 'ABBA Gold'
```

`records`, `id`, `prop` and `value` are the four parameters that we are going to use inside of the function. 

## How to tackle the rules for the challenge

The key to passing this challenge is to break down all four of these rules and tackle them one at a time. Here are the four rules we have to include in our function:

* If `prop` isn't `tracks` and `value` isn't an empty string, update or set that album's `prop` to `value`.
* If `prop` is `tracks` but the album doesn't have a `tracks` property, create an empty array and add `value` to it.
* If `prop` is `tracks` and `value` isn't an empty string, add `value` to the end of the album's existing `tracks` array.
* If `value` is an empty string, delete the given `prop` property from the album.

### How to tackle the first rule

Here is the first rule:

* If `prop` isn't `tracks` and `value` isn't an empty string, update or set that album's `prop` to `value`.

The first part of that rule can be seen as an `if` statement. In our function, we can start to write out the basic structure for an `if` statement. 

```js
function updateRecords(records, id, prop, value) {
  if (condition is true) {
    // do some code
  }
  return records;
}
```

Now we need to figure out what to write for our condition here:

```js
if (condition is true)
```

The first part of the rule says if `prop` isn't `tracks`. We can rephrase that as if `prop` does not equal `tracks`. 

Remember that the inequality operator `!==` can be used to check if two operands are not equal to each other.

But we can't use `tracks` like this in our code because we will get an error message.

```js
if(prop !== tracks)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screen-Shot-2022-03-20-at-12.51.17-AM.png)

To get rid of that error message, `tracks` needs to be a string.

```js
if(prop !== 'tracks')
```

But we are not finished with our condition because we still have to tackle this part:

* and `value` isn't an empty string

We can use the inequality operator `!==` again to say `value !== ""`. Then we can replace the word `and` by using the AND `&&` operator.

This is what the first condition looks like so far:

```js
  if (prop !== 'tracks' && value !== "") {
    // do some code here
  }
```

Now that we have figured out our condition, we need to figure out what goes inside of it.  Here is the second part of that rule:

* update or set that album's `prop` to `value`

We first need to reference the entire object literal which is `records`. Then we need to access the `id` which represents the albums. 

Finally, we need to access that `prop`. We will be using bracket notation to accomplish this.

```js
records[id][prop]
```

The final step is to assign value to the album's `prop`. We are going to use the assignment operator `=` to do that.

```js
records[id][prop] = value
```

This is what the entire first condition looks like:

```js
function updateRecords(records, id, prop, value) {
  if (prop !== 'tracks' && value !== "") {
    records[id][prop] = value
  }
  return records;
}
```

### How to tackle the second rule

Here is the second rule:

* If `prop` is `tracks` but the album doesn't have a `tracks` property, create an empty array and add `value` to it.

Let's take a look at this first part here.

* If `prop` is `tracks`

We can replace the word "is" with the equality operator, because we're checking if `prop` is equal to `tracks`. 

```js
else if (prop === 'tracks')
```

Here is the second part of the condition. 

* but the album doesn't have a `tracks` property

We need to check if the album has a `tracks` property and we can do that by using the `hasOwnProperty()` method. 

This is the basic syntax:

```js
object.hasOwnProperty(prop)
```

The object in this case would be `records[id]` because that represents the album and the property would be `"tracks"`. 

```js
records[id].hasOwnProperty('tracks')
```

But we need to check if the album does not have the `tracks` property. Since the `hasOwnProperty()` method returns a boolean (true or false) then we can write this:

```js
records[id].hasOwnProperty('tracks') === false
```

We can also rewrite that statement using the `NOT` operator `!` like this:

```js
!records[id].hasOwnProperty('tracks')
```

By using the `NOT` operator `!` here, we are basically saying if something is not true.

This is what our `if` statement looks like so far:

```js
else if (prop === 'tracks' && records[id].hasOwnProperty('tracks') === false) {
    //do some code here
  }
```

Here is the second part of the rule:

* create an empty array and add `value` to it

We know that to create an array we can use brackets `[]`. Then we can add `value` inside of it like this:

```js
[value]
```

The final part is to assign that array to the album's property like this:

```js
 records[id][prop] = [value]
```

Here is what the entire second condition looks like:

```js
function updateRecords(records, id, prop, value) {
  if (prop !== 'tracks' && value !== "") {
    records[id][prop] = value
  } else if (prop === 'tracks' && records[id].hasOwnProperty('tracks') === false) {
    records[id][prop] = [value]
  }
  return records;
}
```

### How to tackle the third rule

Here is the third rule:

* If `prop` is `tracks` and `value` isn't an empty string, add `value` to the end of the album's existing `tracks` array.

Let's take a look at the condition here:

* If `prop` is `tracks` and `value` isn't an empty string

We know from out previous code that `prop` is `tracks` can be rewritten as `prop === "tracks"`.  

We can also rewrite `value` isn't an empty string as `value !== ""`.

This is what our third condition looks like so far.

```js
else if (prop === 'tracks' && value !== "") {
    // do some code 
  }
```

Here is the second part of the rule:

* add `value` to the end of the album's existing `tracks` array.

We can use the `push` array method which adds elements to the end of an array.

```js
records[id][prop].push(value)
```

This is what our entire third condition looks like:

```js
function updateRecords(records, id, prop, value) {
  if (prop !== 'tracks' && value !== "") {
    records[id][prop] = value
  } else if (prop === 'tracks' && records[id].hasOwnProperty('tracks') === false) {
    records[id][prop] = [value]
  } else if (prop === 'tracks' && value !== "") {
    records[id][prop].push(value)
  }
  return records;
}
```

### How to tackle the fourth rule

Here is the fourth and final rule.

* If `value` is an empty string, delete the given `prop` property from the album.

Let's take a look at the first part here:

* If `value` is an empty string,

We know from our earlier code that we can translate `value` is an empty string to `value === ""`.

Here is what the `if` statement looks like so far:

```js
else if (value === ""){
    // do some code
  }
```

Here is the second part of the rule:

* delete the given `prop` property from the album.

If we need to delete a property from an object, then we can use JavaScript's `delete` operator. 

Here is how to delete the prop from the album:

```js
else if (value === "") {
    delete records[id][prop]
  }
```

This is what the entire function looks like:

```js
function updateRecords(records, id, prop, value) {
  if (prop !== 'tracks' && value !== "") {
    records[id][prop] = value
  } else if (prop === 'tracks' && records[id].hasOwnProperty('tracks') === false) {
    records[id][prop] = [value]
  } else if (prop === 'tracks' && value !== "") {
    records[id][prop].push(value)
  } else if (value === "") {
    delete records[id][prop]
  }
  return records;
}
```

## Conclusion

I hope this walk through of [Record Collection](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/basic-javascript/record-collection) helped you understand how to solve the challenge. We covered a lot of different methods and learned how to break down a problem into smaller pieces.

Best of luck on the rest of your JavaScript journey. 

