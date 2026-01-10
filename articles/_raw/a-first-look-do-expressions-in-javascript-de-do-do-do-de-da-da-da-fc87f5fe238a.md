---
title: 'A first look: do expressions in JavaScript (De Do Do Do, De Da Da Da)'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-03T15:52:11.000Z'
originalURL: https://freecodecamp.org/news/a-first-look-do-expressions-in-javascript-de-do-do-do-de-da-da-da-fc87f5fe238a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1EjPzePghALoUfc2lUcQOQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Donavon West

  This article is not about about the The Police’s 1980 hit song from album Zenyatta
  Mondatta (although that would be awesome!) No, it’s about the T39 proposal called
  do expressions. If approved by TC39, “do expressions” will be part of...'
---

By Donavon West

This article is **not** about about the The Police’s 1980 hit song from album [_Zenyatta Mondatta_](https://en.wikipedia.org/wiki/Zenyatta_Mondatta) (although that would be awesome!) No_,_ it’s about the T39 proposal called [do expressions](https://github.com/tc39/proposal-do-expressions). If approved by TC39, “do expressions” will be part of JavaScript and could help usher your code out of ternary hell.

Do expressions allow you to embed a statement inside of an expression. The resulting value is returned from the expression.

It’s currently in what is called “stage 1” of the TC39 process, which means that do expressions have a long way to go before they see the light of day.

[Axel Rauschmayer](https://www.freecodecamp.org/news/a-first-look-do-expressions-in-javascript-de-do-do-do-de-da-da-da-fc87f5fe238a/undefined) explains the [TC39 process](http://exploringjs.com/es2016-es2017/ch_tc39-process.html) in his book titled [Exploring ES2016 and ES2017](https://leanpub.com/exploring-es2016-es2017/) (free online, or purchase the eBook).

### What is a do expression?

Here is a simple example of a simple do expression.

```
const status = do {  if (isLoading) {    'Loading';  } else if (isError) {    'Error'  } else {    'Running'  };};
```

It takes whatever is “returned” as the value of the statement and assigns it to `status`. Not very useful over a basic `if` statement, IMO.

Where it really shines is when used within JSX in a React application.

### Use in JSX

Do expressions are especially useful within JSX. Let’s take a look at how you might use them for a common React pattern in the context of JSX: determining what to render based on `loading` and `error` props.

```
const View = ({ loading, error, ...otherProps }) => (  <;div>    {do {      if (loading) {        <Loading />      } else if (error) {        <Error error={error} />      } else {        <MyLoadedComponent {...otherProps} />      };    }}  </div>);
```

Wow! Now that’s incredibly powerful.

The same thing could be performed with a logical AND statement, but you end up negating all of the other values. This can get pretty messy, and is rather hard to follow. It’s also not as efficient from an execution perspective, as this is roughly equivalent to performing three `if` statements.

```
const View = ({ loading, error, ...otherProps }) => (  <;div>    {loading && !error &&      <Loading />    }    {!loading && error &&      <Error error={error} />    }    {!loading && !error &&      <MyLoadedComponent {...otherProps} />    }  </div>);
```

### What is ternary hell?

For a little background, a [ternary](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator) is a JavaScript operator that accepts three operands: a condition, followed by two expressions. It is often used to replace an `if` statement.

Here is an example of a ternary operator in action.

```
const text = isLoading ? 'Loading' : 'Loaded';
```

The variable `text` is set to “Loading” or “Loaded” depending on the `isLoading` binary flag. This is roughly equivalent to the following `if` statement.

```
let text;
```

```
if (isLoading) {  text = 'Loading';} else {  text = 'Loaded';}
```

However, notice that we need to use a `let` statement vs. a `const`. You can see that a ternary is a great way to reduce clutter from your code, plus it allows you to avoid using an unnecessary `let` statement in lieu of a `const`.

I see let statements as a red-flag when I’m doing code reviews. Same thing with `if` statements.

But what if we have a non-binary value? You might combine ternaries and end up with something like this.

```
const text =   stopSignColor === 'red'     ? 'Stop' :  stopSignColor === 'yellow'     ? 'Caution' :  stopSignColor === 'green'     ? 'Go' :  'Error';
```

This is what I’m referring to when I say ternary hell.

It’s a kind of `if/else if/else if/else` statement written using a ternary. Many people find this form hard to follow. In fact, you can even prevent this behavior with an [ESLint `no-nested-ternary`](https://eslint.org/docs/rules/no-nested-ternary) setting.

Here’s the same code written using a `switch` statement embedded within a do expression.

```
const text = do {  switch (stopSignColor) {  case 'red': 'Stop'  case 'yellow': 'Caution'  case 'green': 'Go'  case default: 'Error'  }};
```

### The future is now

Even though do expressions are not officially part of the language (yet?), you can still use them **now** in your project. This is because most of us don’t really code in JavaScript — we code in Babel. And luckily, there’s a [Babel transform](https://babeljs.io/docs/plugins/transform-do-expressions/) that will bring us tomorrow’s language syntax today.

But be careful when choosing this option. There’s no guarantee that the proposal will pass as-is. The specification may dramatically change, leaving your code in need of some re-factoring. In fact, it’s entirely plausible that the specification could be dropped all-together.

### Conclusion

Do expressions have their place, but are hardly a silver bullet. With the help of a Babel transform, they can be used today. One of the greatest benefits of do expressions is when used from within JSX.

And that’s “all I want to say to you”.

I also write for the American Express Engineering Blog. Check out my other works and the works of my talented co-workers at [AmericanExpress.io](http://americanexpress.io/). You can also [follow me on Twitter](https://twitter.com/donavon).

