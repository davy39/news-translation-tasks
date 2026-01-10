---
title: Conditional Rendering in React using Ternaries and Logical AND
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-01T12:59:42.000Z'
originalURL: https://freecodecamp.org/news/conditional-rendering-in-react-using-ternaries-and-logical-and-7807f53b6935
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eASRJrCIVgsy5VbNMAzD9w.jpeg
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

  There are several ways that your React component can decide what to render. You
  can use the traditional if statement or the switch statement. In this article, we’ll
  explore a few alternatives. But be warned that some come with their o...'
---

By Donavon West

There are several ways that your React component can decide what to render. You can use the traditional `if` statement or the `switch` statement. In this article, we’ll explore a few alternatives. But be warned that some come with their own gotchas, if you’re not careful.

### Ternary vs if/else

Let’s say we have a component that is passed a `name` prop. If the string is non-empty, we display a greeting. Otherwise we tell the user they need to sign in.

Here’s a Stateless Function Component (SFC) that does just that.

```
const MyComponent = ({ name }) => {  if (name) {    return (      <div className="hello">        Hello {name}      </div>    );  }  return (    <div className="hello">      Please sign in    </div>  );};
```

Pretty straightforward. But we can do better. Here’s the same component written using a **conditional ternary operator**.

```
const MyComponent = ({ name }) => (  <div className="hello">    {name ? `Hello ${name}` : 'Please sign in'}  </div>);
```

Notice how concise this code is compared to the example above.

A few things to note. Because we are using the single statement form of the arrow function, the `return` statement is implied. Also, using a ternary allowed us to DRY up the duplicate `<div className="hell`o"> markup. ?

### Ternary vs Logical AND

As you can see, ternaries are wonderful for `if/else` conditions. But what about simple `if` conditions?

Let’s look at another example. If `isPro` (a boolean) is `true`, we are to display a trophy emoji. We are also to render the number of stars (if not zero). We could go about it like this.

```
const MyComponent = ({ name, isPro, stars}) => (  <div className="hello">    <div>      Hello {name}      {isPro ? '?' : null}    </div>    {stars ? (      <div>        Stars:{'⭐️'.repeat(stars)}      </div>    ) : null}  </div>); 
```

But notice the “else” conditions return `null`. This is becasue a ternary expects an else condition.

For simple `if` conditions, we could use something a little more fitting: the **logical AND operator**. Here’s the same code written using a logical AND.

```
const MyComponent = ({ name, isPro, stars}) => (  <div className="hello">    <div>      Hello {name}      {isPro && '?'}    </div>    {stars && (      <div>        Stars:{'⭐️'.repeat(stars)}      </div>    )}  </div>); 
```

Not too different, but notice how we eliminated the `: null` (i.e. else condition) at the end of each ternary. Everything should render just like it did before.

Hey! What gives with John? There is a `0` when nothing should be rendered. That’s the gotcha that I was referring to above. Here’s why.

[According to MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_Operators), a Logical AND (i.e. `&&`):

> `_expr1_ && _expr2_`

> Returns `expr1` if it can be converted to `false`; otherwise, returns `expr2`. Thus, when used with Boolean values, `&&` returns `true` if both operands are true; otherwise, returns `false`.

OK, before you start pulling your hair out, let me break it down for you.

In our case, `expr1` is the variable `stars`, which has a value of `0`. Because zero is falsey, `0` is returned and rendered. See, that wasn’t too bad.

I would write this simply.

> If `expr1` is falsey, returns `expr1`, else returns `expr2`.

So, when using a logical AND with non-boolean values, we must make the falsey value return something that React won’t render. Say, like a value of `false`.

There are a few ways that we can accomplish this. Let’s try this instead.

```
{!!stars && (  <div>    {'⭐️'.repeat(stars)}  </div>)}
```

Notice the double bang operator (i.e. `!!`) in front of `stars`. (Well, actually there is no “double bang operator”. We’re just using the bang operator twice.)

The first bang operator will coerce the value of `stars` into a boolean and then perform a NOT operation. If `stars` is `0`, then `!stars` will produce `true`.

Then we perform a second NOT operation, so if `stars` is 0, `!!stars` would produce `false`. Exactly what we want.

If you’re not a fan of `!!`, you can also force a boolean like this (which I find a little wordy).

```
{Boolean(stars) && (
```

Or simply give a comparator that results in a boolean value (which some might say is even more semantic).

```
{stars > 0 && (
```

#### A word on strings

Empty string values suffer the same issue as numbers. But because a rendered empty string is invisible, it’s not a problem that you will likely have to deal with, or will even notice. However, if you are a perfectionist and don’t want an empty string on your DOM, you should take similar precautions as we did for numbers above.

### Another solution

A possible solution, and one that scales to other variables in the future, would be to create a separate `shouldRenderStars` variable. Then you are dealing with boolean values in your logical AND.

```
const shouldRenderStars = stars > 0;
```

```
return (  <div>    {shouldRenderStars && (      <div>        {'⭐️'.repeat(stars)}      </div>    )}  </div>);
```

Then, if in the future, the business rule is that you also need to be logged in, own a dog, and drink light beer, you could change how `shouldRenderStars` is computed, and what is returned would remain unchanged. You could also place this logic elsewhere where it’s testable and keep the rendering explicit.

```
const shouldRenderStars =   stars > 0 && loggedIn && pet === 'dog' && beerPref === 'light`;
```

```
return (  <div>    {shouldRenderStars && (      <div>        {'⭐️'.repeat(stars)}      </div>    )}  </div>);
```

### Conclusion

I’m of the opinion that you should make best use of the language. And for JavaScript, this means using conditional ternary operators for `if/else` conditions and logical AND operators for simple `if` conditions.

While we could just retreat back to our safe comfy place where we use the ternary operator everywhere, you now possess the knowledge and power to go forth AND prosper.

_I also write for the American Express Engineering Blog. Check out my other works and the works of my talented co-workers at [AmericanExpress.io](http://americanexpress.io/). You can also [follow me on Twitter](https://twitter.com/donavon)._

