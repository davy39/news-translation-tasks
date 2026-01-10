---
title: JavaScript String Format – How to use String Interpolation in JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-08T19:27:43.000Z'
originalURL: https://freecodecamp.org/news/javascript-string-format-how-to-use-string-interpolation-in-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98d0740569d1a4ca1c2f.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "By Catalin Pit\nThe addition of template literals in ECMAScript 6 (ES6)\
  \ allows us to interpolate strings in JavaScript. \nIn simpler words, we can use\
  \ placeholders to inject variables into a string. You can see an example of string\
  \ interpolation using ..."
---

By Catalin Pit

The addition of template literals in ECMAScript 6 (ES6) allows us to interpolate strings in JavaScript. 

In simpler words, we can use placeholders to inject variables into a string. You can see an example of string interpolation using template literals in the snippet below:

```js
const age = 4.5;
const earthAge = `Earth is estimated to be ${age} billion years old.`;

console.log(earthAge);

```

First of all, you'll see that we are using backticks for template literals. Besides that, we also have the format of `${placeholder}`, which allows us to insert a dynamic value into the string. Anything inside `${}` is evaluated as JavaScript. 

For instance, we could write `Earth is estimated to be ${age + 10} billion years old.`, and it would work as if we did `const age = 4.5 + 10;`.

### How did we do it before? 

Before template literals, we would have done it like this:

```js
const earthAge = "Earth is estimated to be " + age + " billion years old.";

```

As you can see, we already have lots of quotes for a simple string. Imagine we have to insert a handful of variables. It can quickly transform into a complex string that is not very readable. Thus, template literals make strings cleaner and more readable.

However, this is just one case. Let's see more uses cases for template literals.

## Multi-line strings

Another handy use of template strings is multi-line strings. Before template literals, we used `\n` for new lines, as in `console.log('line 1\n' + 'line 2')`. 

For two lines, this might be fine. But imagine we want five lines. Again, the string becomes unnecessarily complex.

```js
const earthAge = `Earth is estimated to be ${age} billion years old.

Scientists have scoured the Earth searching for the oldest rocks to radiometrically date.

In northwestern Canada, they discovered rocks about 4.03 billion years old.
`;

```

The above snippet demonstrates once again how straightforward and clean it becomes to write multi-line strings with template literals. 

As an exercise, try to convert the above string to use concatenation, and new line `\n`.

## Expressions

With template literals, we can also use expressions in the strings. What does that mean? 

For instance, we could use mathematical expressions such as multiplying two numbers. The snippet below illustrates just that:

```js
const firstNumber = 10;
const secondNumber = 39;
const result = `The result of multiplying ${firstNumber} by ${secondNumber} is ${firstNumber * secondNumber}.`;

console.log(result);

```

Without template literals, we would have to do something like this:

```js
const result = "The result of multiplying " + firstNumber + " by " + secondNumber + " is " + firstNumber * secondNumber + ".";

```

Writing a string like the above can quickly get complex and confusing. As we keep seeing, template literals make it easier and more elegant to embed expressions in the string.

## Ternary operator

With the string interpolation, we can even use a ternary operator inside a string. This allows us to check the value of a variable, and display different things depending on that value. 

Let's look at the example below:

```js
const drinks = 4.99;
const food = 6.65;
const total = drinks + food;

const result = `The total bill is ${total}. ${total > 10 ? `Your card payment will be declined` : `Your card payment will be accepted`}.`

console.log(result);

```

In the above example, we check if the total amount is more than ten dollars, for instance. 

If the amount is more than ten, we let the user know that the card payment will be declined. Otherwise, the card payment is accepted. As you can see, string interpolation allows us to do cool things with strings.

# Conclusion

The addition of template literals in ES6 allows us to write better, shorter, and clearer strings. It also gives us the ability to inject variables and expressions into any string. Essentially, whatever you write inside the curly brackets (`${}`) is treated as JavaScript.

Thus, we can use template literals to:

* write multi-line strings
* embed expressions
* write strings with the ternary operator

Thanks for reading! If you want to keep in touch, let's connect on Twitter [@catalinmpit](https://twitter.com/intent/follow?screen_name=catalinmpit). I also publish articles regularly on my blog [catalins.tech](https://catalins.tech) if you want to read more content from me.

