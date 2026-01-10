---
title: A quick introduction to Tagged Template Literals
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-15T18:19:34.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-tagged-template-literals-2a07fd54bc1d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iuk6ay4N9W42ACJg7BCjiQ.png
tags:
- name: CSS
  slug: css
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Michael Ozoemena

  In this article, I’m going to be talking about what “tagged template literals” are
  and some places where I’ve seen them being used.

  What are “tagged template literals”?

  Tagged template literals were enabled by a new technology int...'
---

By Michael Ozoemena

In this article, I’m going to be talking about what “tagged template literals” are and some places where I’ve seen them being used.

#### What are “tagged template literals”?

Tagged template literals were enabled by a new technology introduced in ES6, called “template literals”. This is simply a syntax that makes string interpolation possible in JavaScript. Before `template literals` was born, JavaScript developers would need to do ugly string concatenation.

`Tagged template literals` offers you the opportunity to parse template literals in whatever way you want. It works by combining functions with `template literals`. There are two parts of a `tagged template literal`, the first one being the `tag function` and the second, the `template literal`.

```
const coolVariable = "Cool Value";
```

```
const anotherCoolVariable = "Another Cool Value";
```

```
randomTagFunctionName`${coolVariable} in a tagged template literal with ${anotherCoolVariable} just sitting there`
```

Now, the first parameter in the `tag function` is a variable containing an array of strings in the template literal:

```
function randomTagFunctionName(firstParameter) {
```

```
console.log(firstParameter);     // ["", " in a tagged template literal with ", " just sitting there"]
```

```
}
```

And all other subsequent parameters will contain the values passed to the template literal:

```
function randomTagFunctionName(firstParameter, secondParameter, thirdParameter) {
```

```
console.log(secondParameter);   // "Cool Value"
```

```
console.log(thirdParameter);   // "Another Cool Value"
```

```
}
```

Taking advantage of the ES6 Rest operator, we can redefine our function like this:

```
function randomTagFunctionName(firstParameter, ...otherParameters) {
```

```
console.log(otherParameters);   // ["Cool Value", "Another Cool Value"]
```

```
}
```

#### Tagged Template Literals in Styled-Components.

Now that you understand what tagged template literals are, let us discuss an application of it in the real world.

Styled-Components is a JavaScript library that lets you create and attach CSS styles to your React and React Native components. Here’s what that looks like:

```
const Button = styled.button`  color: red;`
```

In the example above, Button isn’t just a variable, it’s a component. That means you can mix it with other components and its output is an HTML button element.

This is a very exciting use case for tagged template literals because it lets you have scoped CSS in a way that still keeps your component file clean and makes you feel like you are writing CSS in a regular stylesheet. Without tagged template literals, we would have to represent that style as a JavaScript object like this:

```
const Button = styled.button({  color: 'red'})
```

Another use case is with the [graphql-tag](https://github.com/apollographql/graphql-tag) library used in **Apollo GraphQL**. I don’t think there is a possible way to not use the `graphql-tag` library when dealing with Apollo GraphQL (if there is, please let me know!).

#### In conclusion.

I think it’s great to learn new technologies and even better to look at ways in which others have used it to solve problems. If you have other real-world use cases for Tagged Template Literals, please let me know.

PS: “Real-World” also means your side-projects or `codesandbox` code samples.

