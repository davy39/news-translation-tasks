---
title: How to Use Optional Chaining in JavaScript
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-02-07T17:13:35.000Z'
originalURL: https://freecodecamp.org/news/javascript-optional-chaining
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pexels-pixabay-220237.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Optional chaining is a safe and concise way to perform access checks for
  nested object properties.

  The optional chaining operator ?. takes the reference to its left and checks if
  it is undefined or null. If the reference is either of these nullish va...'
---

Optional chaining is a safe and concise way to perform access checks for nested object properties.

The optional chaining operator `?.` takes the reference to its left and checks if it is undefined or null. If the reference is either of these nullish values, the checks will stop and return undefined. Otherwise, the chain of access checks will continue down the happy path to the final value. 

```
// An empty person object with missing optional location information
const person = {}

// The following will equate to undefined instead of an error
const currentAddress = person.location?.address


```

Optional chaining was introduced in ES2020. According to [TC39](https://github.com/tc39/proposal-optional-chaining) it is currently at stage 4 of the proposal process and is prepared for inclusion in the final ECMAScript standard. This means that you can use it, but note that older browsers may still require polyfill usage.

Optional chaining is a useful feature that can help you write cleaner code. Now let's learn how we can use it.

## Optional Chaining Syntax

In this article, I will mostly be covering how to access object properties. But you can also use optional chaining as a check on functions. 

Here are all of the use cases for optional chaining:

```
obj?.prop       // optional static property access
obj?.[expr]     // optional dynamic property access
func?.(...args) // optional function or method call

```

Source: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining) 

### Example:

```
const value = obj?.propOne?.propTwo?.propThree?.lastProp;
```

In the code snippet above, we are checking if `obj` is null or undefined, then `propOne`, then `propTwo`, and so on. Optional chaining lives up to its name. In the chain of object property access we can check that each value is not undefined or null.

This check can be extremely useful when accessing deeply nested object values. It has been a highly anticipated feature and it keeps you from having to do numerous null checks. It also means you don't need to use temporary variables to store checked values, for example:

```
const neighborhood = city.nashville && city.nashvile.eastnashville;

```

Here we can check that `nashville` is a property within `city` before attempting to access the inner neighborhood property of `eastnashville`. We can convert the above to use optional chaining, like so:

```
const neighborhood = city?.nashville?.eastnashville;
```

Optional chaining simplifies this expression.

## Error Handling with Optional Chaining

Optional chaining is particularly useful when working with API data. If you're not sure whether an optional property exists, you can reach for optional chaining.

### A Word of Caution

Don't use optional chaining at every opportunity. This could result in silencing errors by having undefined potentially returned in many places.

It's also important to remember that the check will stop and "short-circuit" the moment it encounters a nullish value. Consider this for the subsequent properties in the chain and what will occur if they are not able to be reached. 

It's best to use this check when you know that something may not have a value, such as an optional property. If a required value has a nullish check on, it may be silenced with undefined returned instead of returning an error to alert of this issue.

## Optional Chaining + Nullish Coalescing 

Optional chaining pairs well with nullish coalescing `??` to provide fallback values. 

```
const data = obj?.prop ?? "fallback string";
```

```
const data = obj?.prop?.func() ?? fallbackFunc();
```

If the item to the left of `??` is nullish, the item to the right will be returned.

We know that if any `?.` check equates to a nullish value within the chain, it will return `undefined`. So we can use our nullish coalescing to respond to the undefined outcome and set an explicit fallback value.

```
const meal = menu.breakfast?.waffles ?? "No Waffles Found."
```

### Wrapping Up

Optional chaining is a handy recent feature of JavaScript that lets you check for nullish values while accessing property values. You can also use it with the `?.` operator. 

I hope this article has helped to introduce or clarify optional chaining. Happy coding! 

