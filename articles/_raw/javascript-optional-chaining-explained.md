---
title: JavaScript Optional Chaining `?.` Explained - How it Works and When to Use
  it
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-08-25T15:39:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-optional-chaining-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c990e740569d1a4ca1d97.jpg
tags:
- name: Babel
  slug: babel
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "What is optional chaining?\nOptional chaining, represented by ?. in JavaScript,\
  \ is a new feature introduced in ES2020. \nOptional chaining changes the way properties\
  \ are accessed from deeply nested objects. It fixes the problem of having to do\
  \ multiple..."
---



## What is optional chaining?

Optional chaining, represented by `?.` in JavaScript, is a new feature introduced in ES2020. 

Optional chaining changes the way properties are accessed from deeply nested objects. It fixes the problem of having to do multiple null checks when accessing a long chain of object properties in JavaScript.

Current Status: `ECMAScript proposal at stage 4 of the process.` : https://github.com/tc39/proposal-optional-chaining
                
## Use cases

1. Accessing potentially `null` or `undefined` properties of an object. 
2. Getting results from a variable that may not be available yet.
3. Getting default values.
4. Accessing long chains of properties.

Imagine you are expecting an API to return an object of this sort:

```javascript
obj = {
  prop1: {
    prop2: {
      someProp: "value"
    }
  }
};
```

But you may not know if each of these fields are available ahead of time. Some of them may not have been sent back by the API, or they may have come back with null values. 

Here is an example:

```javascript
//expected
obj = {
  id: 9216,
  children: [
    { id: 123, children: null },
    { id: 124, children: [{ id: 1233, children: null }] }
  ]
};

//actual
obj = {
  id: 9216,
  children: null
};
```

This happens very often with functions that call APIs. You may have seen code in React that tries to safeguard against these issues like this:

```jsx
render = () => {
  const obj = {
    prop1: {
      prop2: {
        someProp: "value",
      },
    },
  };

  return (
    <div>
      {obj && obj.prop1 && obj.prop1.prop2 && obj.prop1.prop2.someProp && (
        <div>{obj.prop1.prop2.someProp}</div>
      )}
    </div>
  );
};

```

In order to better prepare for this issue, often times in the past we have used `Lodash`, specifically the `_.get` method:

```javascript
_.get(obj, prop1.prop2.someProp);

```

This outputs `undefined` if either of those properties are `undefined`. **Optional chaining is exactly that**! Now instead of using an external library, this functionality is built-in.


## How does optional chaining work?

`?.` can be used to chain properties that may be `null` or `undefined`.

```
const propNeeded = obj?.prop1?.prop2?.someProp;

```

If either of those chained properties is `null` or `undefined`, JavaScript will return `undefined`. 

What if we want to return something meaningful? Try this: 

```javascript
let familyTree = {
    us: {
        children: {}
    }
}


// with _.get
const grandChildren = _.get(familyTree, 'us.children.theirChildren', 'got no kids' );

//with optional chaining and null coalescing 
const nullCoalescing = familyTree?.us?.children?.theirChildren ?? 'got no kids'
console.log(nullCoalescing) //got no kids

```

It also works for objects that may be `null` or `undefined`:

```
let user;
console.log(user?.id) // undefined

```


## How to get this newest feature

1. Try it in your browser's console: This is a recent addition and old browsers may need polyfills. You can try it in Chrome or Firefox in the browser's console. If it doesn't work, try turning on JavaScript experimental features by visiting `chrome://flags/` and enabling "Experimental JavaScript".
  
2. Try it in your Node app by using Babel:
```
{
  "plugins": ["@babel/plugin-proposal-optional-chaining"]
}
```

## Resources

1. https://dmitripavlutin.com/javascript-optional-chaining/
2. Babel's doc: https://babeljs.io/docs/en/babel-plugin-proposal-optional-chaining

## TL;DR
Use optional chaining `?.` for objects or long chain properties that may be `null` or `undefined`. The syntax is as follows:

```javascript
let user = {};
console.log(user?.id?.name) 
```
****

Interested in more tutorials and JSBytes from me? [Sign up for my newsletter.](https://tinyletter.com/shrutikapoor) or [follow me on Twitter](https://twitter.com/shrutikapoor08)


