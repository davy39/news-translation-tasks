---
title: Learn to spot red flags in your React/JavaScript code ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-06T20:11:15.000Z'
originalURL: https://freecodecamp.org/news/learn-to-spot-red-flags-in-your-react-javascript-code-d52d5fac85f4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tfKnZ6l_0P7r1Wim-n-0og.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Donavon West

  This opinionated article will explain some of the red flags to look for when reviewing
  a React/JavaScript project. Avoiding these patterns can make your code more performant,
  more reliable, and easier to maintain.

  ? Look out for the l...'
---

By Donavon West

This opinionated article will explain some of the red flags to look for when reviewing a React/JavaScript project. Avoiding these patterns can make your code more performant, more reliable, and easier to maintain.

### ? Look out for the l`et` keyword

Back in the ES5 days, `var` was the only means at our disposal to create variables. ES6 introduced the block-scoped `let` and `const` keywords.

In my experience, I see very few situations where you should use `let`. Sure, it has its place (like a counter, for example), but for most applications `const` is better suited. You’ll soon see why.

Take the following common use case. It renders the `amount` in red if negative, otherwise, it will be in black.

```
let color;
```

```
if (amount < 0) {  color = 'red';} else {  color = 'black';}
```

```
return (  <span style={{ color }}>    {formatCurrency(amount)}  </span>);
```

The code is using a `let` , but after initialization, the `color` variable is never re-assigned. **This is exactly the use case for a `const`!**

We can’t simply replace the `let` with a `const` because of how the code is structured. However, if we refactor to use a ternary, a `const` works out perfectly.

```
const color = amount < 0 ? 'red' : 'black';
```

Not only did we go from 6 lines of code to 1, but by using a `const` instead of a `let`, our tooling will throw an error if we inadvertently reassign `const` somewhere else in the code.

Here is the output from ESLint if I try to set `color` to `null` after it’s defined.

```
/Users/donavon/Projects/my-project/src/index.jsx
```

```
43:5  error 'color' is constant
```

So the next time you feel your muscle memory start to type `let`, catch yourself and use a `const` instead. Nine times out of ten, it will serve you just fine.

#### Benefits of using const

* Forces you to write cleaner code
* Compile-time checking of unintentional variable re-assignment

### ? Destructuring is your friend

According to [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment):

> The **destructuring assignment** syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.

It also makes the code significantly easier to read. Take this snippet for example.

```
render() {  return(    <div className={this.props.className}>      {        this.props.isLoading          ? 'Loading...'          : this.props.children      }    </div>  );}
```

There are multiple `this.props` operations going on. This is slower to execute (OK, marginally, but still, multiple object property lookups need to occur), and again, it adds visual clutter.

```
render() {  const { className, isLoading, children } = this.props;
```

```
  return(    <div className={className}>      {isLoading ? 'Loading...' : children}    </div>  );}
```

By adding the single line of code, above, the rest of the code is more readable.

#### Benefits of **destructuring**

* Potentially faster execution
* Cleaner
* Less prone to hidden errors caused by typos

### ? Spread over Object.assign

It used to be that making a shallow copy of an object or building an object out of other objects required `Object.assign`. But today, with the help of babel, we can use the new ES spread syntax.

Here’s some code using `Object.assign`.

```
const defaults = { foo: 'foo', bar: 'bar' };const obj1 = Object.assign({}, defaults, { bar: 'baz' });// {foo:'foo', bar:'baz'}
```

The code below outputs the same results, but using the object spread syntax.

```
const defaults = { foo: 'foo', bar: 'bar' };const obj1 = { ...defaults, bar: 'baz' };// {foo:'foo', bar:'baz'}
```

This “syntactic sugar” allows you to see the data you’re working on without all of the noise and clutter caused by the ES5 plumbing. You can read more about noise and clutter in my article “[**Noise is all around us**](https://medium.freecodecamp.org/noise-is-all-around-us-d0c0fcb8d48)”.

[Axel Rauschmayer](https://www.freecodecamp.org/news/learn-to-spot-red-flags-in-your-react-javascript-code-d52d5fac85f4/) has a great in-depth explanation of spread vs `Object.assign` in his article “[ES2018: Rest/Spread Properties](http://2ality.com/2016/10/rest-spread-properties.html)”. It’s well worth your time if you like to dig around in the plumbing.

#### Benefits of using spread

* Less clutter
* Potentially more efficient

### ? Using a ternary instead of using a logical AND

For simple `if` conditions, a ternary is not the right tool. I explain this in detail in my article about ternaries and logical AND in my article “[**Conditional Rendering in React using Ternaries and Logical AND**](https://medium.freecodecamp.org/conditional-rendering-in-react-using-ternaries-and-logical-and-7807f53b6935)”.

#### Benefits using logical AND

* Less clutter

### ? Expression body arrow function

Arrow functions are perfect for writing Stateless Functional Components (SFCs) in React and come in two forms. The statement body form like this.

```
const SomeFunction = () =&gt; {  return 'value';};
```

And the expression body form that has an implied `return` statement.

```
const SomeFunction = () =&gt; 'value';
```

Some people erroneously call this “single line”, but as you can see below, the expression can span multiple lines. Note that I’m using parentheses and not curly braces.

```
const SomeFunction = () =&gt; (  'value');
```

So if your function returns a single expression, and you don’t need any intermediate computational `const` statements, use the expression form on the arrow function. It’s a simple idea, and almost too obvious when it’s written out like this, but it’s an easy thing for some people to overlook.

Fortunately, ESLint again can come to your rescue.

```
/Users/donavon/Projects/my-project/src/index.jsx
```

```
  12:17  error Unexpected block statement surrounding arrow body;         move the returned value immediately after the `=>`
```

The only thing to remember is that in order to return an object in the expression form, you must enclose the object literal in parentheses, like so.

```
const SomeFunction = () =&gt; ({  foo: 'foo',  bar: 'bar',});
```

#### Benefits of expression body arrow functions

* Less clutter

### ? DRY up that duplicate code

You didn’t think I would write an article about red flags in your code without mentioning DRY, did you? Here we go…

Take a look at the following two SFCs.

```
const Foo = () => (  <;div>    <h2 className="sectionTitle">      Foo Title    </h2>    ...  </div>);
```

```
const Bar = () => (  <;div>    <h2 className="sectionTitle">      Bar Title    </h2>    ...  </div>);
```

Notice how the highlighted sections of code above in `Foo` and `Bar` are nearly identical. It’s apparent that they both display a title in a certain style. What if you had the same code in 4, 5, or more places? It’s highly likely that any changes done in the future would require that you make the change in multiple places.

You should refactor the duplicate code into its own function. This is called DRYing or [Don’t Repeat Yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

```
const Title = text => (  <h2 className="sectionTitle">    {text}  </h2>);
```

```
const Foo = () => (  <div>    <Title text="Foo Title" />    ...  </div>);
```

```
const Bar = () => (  <div>    <Title text="Bar Title" />    ...  </div>);
```

#### Benefits of DRY code

* Cleaner
* More maintainable

### ? Why are you using a constructor?

Many times, when writing a stateful React class component, you create a constructor to set the initial value of `state`. Here is a common example.

```
constructor(props) {  super(props);  this.state = { count: 0 };}
```

But did you know that you can do all of this using the new class properties proposal? The code above can be written simply as this.

```
state = { count: 0 };
```

You can read more about this in my article “[**The constructor is dead, long live the constructor**](https://hackernoon.com/the-constructor-is-dead-long-live-the-constructor-c10871bea599)”.

#### Benefits of not using a constructor

* Cleaner

### ? Conclusion

As I said in the opening, learning to avoid some of these patterns can make your code more performant, more reliable, and easier to maintain.

These are not hard and fast rules, but general guidelines meant to open your eyes to other ways of looking at code. Use with caution. Your mileage may vary.

Strict ESLint rules will go along way to helping you spot some of these for you, or… you can always tag me in your pull request. ?

I’d like to apologize if this article seemed like a flashback episode of your favorite sitcom (I hate those), but I wanted to expose those of you who have never read my other articles, with the chance to dive deeper.

I also write for the American Express Engineering Blog. Check out my other works and the works of my talented co-workers at [AmericanExpress.io](http://americanexpress.io/). You can also [follow me on Twitter](https://twitter.com/donavon).

