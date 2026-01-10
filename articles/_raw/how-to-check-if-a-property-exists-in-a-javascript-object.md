---
title: How to Check if a Property Exists in a JavaScript Object
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-04-25T17:53:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-a-property-exists-in-a-javascript-object
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/kevin-canlas-cFFEeHNZEqw-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "When you are working with objects in JavaScript, you might need to check\
  \ if a specific property exists or not. \nIn this article, I will show you three\
  \ ways to check if a property exists in a JavaScript object. \nHow to Use the hasOwnProperty()\
  \ Method ..."
---

When you are working with objects in JavaScript, you might need to check if a specific property exists or not. 

In this article, I will show you three ways to check if a property exists in a JavaScript object. 

## How to Use the `hasOwnProperty()` Method in JavaScript

The `hasOwnProperty()` method will check if an object contains a direct property and will return true or false if it exists or not. 

Here is the basic syntax:

```js
obj.hasOwnProperty(prop)
```

In this first example, we have an object called `developer` with three properties:

```js
const developer = {
  name: "Jessica Wilkins",
  country: "United States",
  isEmployed: true
};
```

If we wanted to check if the `isEmployed` property exists in the `developer` object, then we can use the `hasOwnProperty()` method, like this:

```js
developer.hasOwnProperty("isEmployed")
```

This would return true because the property called `isEmployed` is a direct property of the `developer` object. 

But what if we tried checking for a property called `isPrototypeOf`?

```js
developer.hasOwnProperty("isPrototypeOf")
```

This would return false because there is no direct property called `isPrototypeOf` on the `developer` object. But what do I mean by direct property? 

Whenever you create an object in JavaScript, there is a built-in property called a prototype and the value is another object. That object will have its own prototype, and this is know as a prototype chain. 

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-23-at-6.47.02-PM.png)

Our `developer` object has access to these other properties, like `toString`, and this is what is known as an inherited property. 

The `hasOwnProperty()` method will only return true for direct properties and not inherited properties from the prototype chain. 

## How to Use the `in` Operator

Unlike the `hasOwnProperty()` method, the `in` operator will return true for both direct and inherited properties that exist in the object. 

Here is the basic syntax:

```js
property in object
```

We can modify our earlier example to check if the `country` property exists in the `developer` object using the `in` operator.

```js
"country" in developer
```

This would return true because the `country` property is a direct property in the `developer` object. 

We can also check if the `toString` property exists on the `developer` object or in the prototype chain. 

```js
"toString" in developer
```

This would return true because the `toString` property does exist in the prototype chain because it was inherited from the prototype object. 

## How to Check if a Property Exists in an Object using `undefined`

If I tried to access a property name in an object that does not exist, then I would get undefined.  

For example, if I tried `developer.age` then the return value would be undefined because the `developer` object does not have that property name. 

We can check if a property exists in the object by checking if `property !== undefined`.

In this example, it would return true because the `name` property does exist in the `developer` object. 

```js
developer.name !== undefined
```

## Conclusion

If you need to check if a property exists in a JavaScript object, then there are three common ways to do that. 

The `hasOwnProperty()` method will check if an object contains a direct property and will return true or false if it exists or not. The `hasOwnProperty()` method will only return true for direct properties and not inherited properties from the prototype chain. 

Unlike the `hasOwnProperty()` method, the `in` operator will return true for both direct and inherited properties that exist in the object or its prototype chain. 

Lastly, we can see if a property exists in the object by checking if `property !== undefined`.

I hope you enjoyed this article and best of luck on your developer journey. 

