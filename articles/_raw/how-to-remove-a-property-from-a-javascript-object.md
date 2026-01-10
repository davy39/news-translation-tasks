---
title: How to Remove a Property from a JavaScript Object
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-21T17:48:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-property-from-a-javascript-object
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/remove-property-from-js-object.jpeg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Saransh Kataria\nThere are two ways to remove a property from a JavaScript\
  \ object. There's the mutable way of doing it using the delete operator, and the\
  \ immutable way of doing it using object restructuring. \nLet's go through each\
  \ of these methods ..."
---

By Saransh Kataria

There are two ways to remove a property from a JavaScript object. There's the mutable way of doing it using the delete operator, and the immutable way of doing it using object restructuring. 

Let's go through each of these methods in this tutorial.

## Remove a Property from a JS Object with the Delete Operator

`delete` is a JavaScript instruction that allows us to remove a property from a JavaScript object. There are a couple of ways to use it:

* `delete object.property;`
* `delete object[‘property’];`

The operator deletes the corresponding property from the object.

```javascript
let blog = {name: 'Wisdom Geek', author: 'Saransh Kataria'};
const propToBeDeleted = 'author';
delete blog[propToBeDeleted];
console.log(blog); // {name: 'Wisdom Geek'}
```

The delete operation modifies the original object. This means that it is a mutable operation.

## Remove a Property from a JS Object with Object Destructuring

Using the object restructuring and rest syntax, we can destructure the object with the property to be removed and create a new copy of it. 

After the destructuring, a new copy of the object gets created and assigned to a new variable without the property that we chose to remove.

```javascript
const { property, ...remainingObject } = object;
```

For example:

```javascript
let blog = {name: 'Wisdom Geek', author: 'Saransh Kataria'};
const { author, ...blogRest } = blog;
console.log(blogRest) // {name: 'Wisdom Geek'};
console.log(blog); // {name: 'Wisdom Geek', author: 'Saransh Kataria'}
```

If we want to do this dynamically, we can do this:

```javascript
const name = 'propertToBeRemoved';
const { [name]: removedProperty, ...remainingObject } = object;

```

It is also possible to remove multiple properties using the same syntax.

## Wrapping Up

And those are the two ways to remove a property from a JavaScript object. If you have any questions, feel free to reach out to me!

_Read more of my posts at: [https://www.wisdomgeek.com](https://www.wisdomgeek.com/)_  

