---
title: ES6 Tagged Template Literals
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-18T16:35:00.000Z'
originalURL: https://freecodecamp.org/news/es6-tagged-template-literals-48a70ef3ed4d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZG68vCYoeNM8ID1pC3-f-A.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sanket Meghani

  You may already be familiar with ES6 template literals, which allows string interpolation
  like this:

  const name = ''Steve'';const message = `Hello ${name}!`;

  console.log(message); // Output -> Hello Steve!

  ES6 also introduced a more a...'
---

By Sanket Meghani

You may already be familiar with ES6 template literals, which allows string interpolation like this:

```
const name = 'Steve';const message = `Hello ${name}!`;
```

```
console.log(message); // Output -> Hello Steve!
```

ES6 also introduced a more advanced and powerful concept of Tagged Template Literals. A tag is a function which has ability to interpret & process the template. This means we can run the template string through a function and have more control over how the template is converted to string representation.

Tags are just normal functions, but to be useful they have to be invoked differently. Following example shows how a tag is defined and invoked:

Tag needs to be invoked by passing a template literal without using brackets as shown in line 9 above.

The template literal is passed to tag function as multiple parameters. The first argument is a string array containing string literals from the template: First element in the array is string starting from index 0 to the first interpolated value, second element in the array is string after first interpolated value up-to next interpolation and so on until end of template is reached.

All the interpolated **expressions** are evaluated and passed to the tag as second argument on-wards in order of their occurrence. The tag can process the literals and evaluated expressions to form the return value.

### What makes it powerful?

The obvious question is: how is this more powerful than normal template literals?

All the interpolated **expressions** are evaluated and passed to the tag as second argument on-wards…

This allows us to use function expressions as interpolated values which can be called back. Let’s take an example to make it more clearer.

When the interpolation contains a function expression, it is evaluated as normal string in case of normal template literals.

For example `${() => myFunction`()}is evaluated as stri`ng () => myFunc`tion().

While the same expression is evaluated as function in case of tagged template literals and the tag can call that function. As shown in the example, while invoking the `myTag` the expression `{() => myFunction`()} is evaluated and passed as function `in f`unc parameter which our tag invoked usi`ng fun`c() on line 9.

### Conclusion

Tag’s ability to use function expressions as an interpolation — along with it’s ability to interpret a template using any logic it desires — makes it very powerful. It can be used to create a domain specific language and opens up many possibilities for the use (or abuse) of tagged template literals.

Tagged template literals enable the development of libraries like [styled-components](https://github.com/styled-components/styled-components). Please comment below if you can think of what all other use cases could be enabled by tagged template literals.

