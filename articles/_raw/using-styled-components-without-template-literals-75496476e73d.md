---
title: How you can use styled-components without template literals
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-01T17:12:58.000Z'
originalURL: https://freecodecamp.org/news/using-styled-components-without-template-literals-75496476e73d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*p1TndLk3UsGPBsM7qHPZIw.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jake Wiesler

  If you’ve used styled-components in the past, you’ve probably seen the default (according
  to the documentation) way of declaring a component using the styled API:

  import styled from ''styled-components''

  const Button = styled.button`  b...'
---

By Jake Wiesler

If you’ve used `styled-components` in the past, you’ve probably seen the default (according to the documentation) way of declaring a component using the `styled` API:

```
import styled from 'styled-components'
```

```
const Button = styled.button`  background: palevioletred;   color: #fff;`
```

Nothing shocking here. The documentation uses this pattern, and if you view any material on `styled-components` , you’ve probably seen the exact same thing.

Well, in the past few weeks I’ve seen a different pattern in a few libraries utilizing `styled-components`, but I haven’t seen much information about it. Here it is:

```
const Button = styled('button')([],  'background: palevioletred',  'color: #fff')
```

This is interesting, and I’d like to explore it.

### How does it work?

If you read [Max Stoiber’s](https://medium.com/@mxstbr) post [The magic behind styled-components](https://mxstbr.blog/2016/11/styled-components-magic-explained/), he goes into some detail about the inner workings of his popular CSS library. The `styled` API of `styled-components` relies on tagged template literals, and this is probably the way you will see most people using it.

But, it’s not the only way to declare components using the `styled` API. This is the key idea behind this post, yet it may seem unclear right now. So, to answer the question, _how does it work?_, we first need to dive a bit further into tagged template literals.

#### Tagged template literals

Let’s make an important distinction regarding template literals vs tagged template literals. _What is the difference?_

**Template literals** are, according to Mozilla:

> “string literals allowing embedded expressions.”

These strings can be multi-line:

```
const multiLiner = `  Look Ma,  2 lines!`
```

And they can also contain embedded expressions, which is another way of saying they support _interpolations_:

```
const food = 'burger'
```

```
const str = 'Mmmm! That is a tasty ${food}!
```

![Image](https://cdn-media-1.freecodecamp.org/images/O4ksRAAXJa5q98ps0eX3yfffNUlPzyDX6TEF)
_pulp fiction ya dig_

`${ This here }` is an interpolation. Think of them as placeholders for JavaScript expressions.

**Tagged template literals**, on the other hand, are simply template literals that are used to call a function instead of the normal comma-separated values inside of parentheses:

```
// regular function call
```

```
myFunc(1, 2, 3)
```

```
// tag function call
```

```
myFunc`1, 2, 3`
```

The second version of `myFunc` above is known as a **tag function**.

The way the two call sites of `myFunc` pass on their parameters is what sets them apart. You already know how a regular function call passes on its parameters, but I don’t expect you to know how tag functions do so.

Max [sums this up](https://mxstbr.blog/2016/11/styled-components-magic-explained/) extremely well in his post, and it’s _the_ thing you must understand about tagged template literals, so I will summarize how it works by using the same function he created:

```
const logArgs = (...args) => console.log(...args)
```

The function above uses the _spread…rest_ operators. The arguments to the function are being collected into a single array named `args` using the `…args` syntax. This is referred to as **rest**. You can think of it as “collecting the rest” of the arguments into an array named `args`. It’s useful when you don’t know how many arguments the function might have.

Its sibling, **spread**, occurs when we log the arguments to the console using `console.log(...args)`. We’re literally “spreading out” the contents of the `args` array.

These two operators help us visualize exactly what’s being passed to `logArgs`. Let’s examine the result of this function when called in the two ways described earlier:

```
logArgs(1, 2, 3)
```

```
// -> 1
```

```
// -> 2
```

```
// -> 3
```

```
logArgs`1, 2, 3`
```

```
// -> ["1, 2, 3"]
```

Calling the function as normal does what we expect. It spreads the `args` array out into individual values, and logs each to the console.

Calling `logArgs` using a tagged template literal, on the other hand, logs an array. This is our first lesson:

_Tagged template literals pass an array of string values as the first argument to the tag function._

Things get even more interesting when we include interpolations:

```
const food = 'burger'
```

```
logArgs`Mmmm! That is a tasty ${food}!`
```

```
// -> ["Mmmm!  That is a tasty ", "!"]
```

```
// -> "burger"
```

`logArgs` still outputs an array of string values as its first argument, but if the tagged template literal has an interpolation, then the expression inside the interpolation is passed as the next argument.

What happens when there are multiple interpolations?

```
const food = 'burger'
```

```
const adj = 'tasty'
```

```
logArgs`Mmmm! That is a ${adj} ${food}!`
```

```
// -> ["Mmmm!  That is a ", " ", "!"]
```

```
// -> "tasty"
```

```
// -> "burger"
```

We could have as many interpolations as we want, and each one will be passed accordingly. This is the second lesson:

_If interpolations exist inside tagged template literals, their containing expressions are passed as additional arguments to the tag function._

Let’s see how tagged template literals handle interpolated functions:

```
logArgs`Mmmm! That is a tasty ${() => 'burger'}`
```

```
// -> ["Mmmm!  That is a tasty", "!"]
```

```
// -> () => "burger"
```

The function itself is being included as an argument. This is the essence of `styled-components`. By capturing such a function, the library can execute it and do what it needs to do, mainly merge the resulting value back in to the string values inside the array.

### Tying our new-found knowledge together

Now that we know how tagged template literals work, let’s gain a deeper understanding of the `styled` API:

```
const Button = styled.button`  background: ${props => props.primary ? 'red' : 'white'};  color: black;`
```

`styled.button` is a tag function. If we were to log the arguments of this function, we’d see this:

```
logArgs`  background: ${props => props.primary ? 'red' : 'white'};  color: black;`
```

```
// -> ["background: ", "; color: black;"]
```

```
// -> props => props.primary ? "red" : "white"
```

Are you seeing the power here? It’s no wonder why `styled-components` has become so popular as a CSS-in-JS solution. Not only do tagged template literals allow us to write multi-line CSS naturally, but it allows the library to manipulate styles through these interpolated functions, giving our components a dynamic feel.

### So how does the other pattern work?

Ah, yes. That’s why you’re here, isn’t it. Earlier, I showed another way of using the `styled` API that I’ve been seeing lately:

```
const Button = styled('button')([],  'background: palevioletred',  'color: #fff')
```

First, understand that `styled.button` and `styled('button')` are treated the same way. They’re interchangeable.

Second, there’s no tagged template literal action here. But, since we know that `styled` supports them, _we know how it expects its arguments_. This is the major key ?.

Remember the two rules:

1. **Tagged template literals pass an array of string values as the first argument to the tag function.**
2. **If interpolations exist inside tagged template literals, their containing expressions are passed as additional arguments to the tag function.**

So the tag function expects an array of string values as its first argument, and interpolated expressions follow suit.

In the pattern above, which I will give the name _“The Empty Array Pattern”_, the arguments are:

```
// -> []
```

```
// -> 'background: palevioletred'
```

```
// -> 'color: #fff'
```

The first argument is an array, and satisfies rule number one. Yes, there’s no string values inside the array, but that’s totally fine. The additional arguments are strings which, by definition are expressions that produce a value, and as such they satisfy rule number two.

_We’ve mimicked the behavior of tagged template literals without actually using them._

### Wrapping Up

At the end of the day, both patterns produce the same value. What I’m finding difficult to discover is why you would want to use one over the other. I guess I could see a situation where, using tagged template literals, you had multiple interpolations, and for code readability you could choose the _Empty Array Pattern_ instead:

```
// as tagged template literal
```

```
const Button = styled.button`  background: ${ props => props.background };  color: ${ props => props.color };`
```

```
// as Empty Array Pattern
```

```
const Button = styed.button([], props => ({  background: props.background,  color: props.color}))
```

I’d love to hear insights from others who have experience with these patterns, and what the pros and cons are of each!

This was a cross-post from [my own blog](https://www.jakewiesler.com/blog/using-styled-components-without-template-literals/). ?

Say hi on [Twitter](https://twitter.com/jakewies) ?

