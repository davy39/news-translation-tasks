---
title: Closures, Curried Functions, and Cool Abstractions in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-26T14:56:12.000Z'
originalURL: https://freecodecamp.org/news/playing-around-with-closures-currying-and-cool-abstractions
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/curry.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By TK

  In this article, we will talk about closures and curried functions and we''ll play
  around with these concepts to build cool abstractions. I want to show the idea behind
  each concept, but also make it very practical with examples and refactored c...'
---

By TK

In this article, we will talk about closures and curried functions and we'll play around with these concepts to build cool abstractions. I want to show the idea behind each concept, but also make it very practical with examples and refactored code to make it more fun.

## Closures

Closures are a common topic in JavaScript, and it's the one we'll start with. According to MDN:

> A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment).

Basically, every time a function is created, a closure is also created and it gives access to the state (variables, constants, functions, and so on). The surrounding state is known as the `lexical environment`.

Let's show a simple example:

```javascript
function makeFunction() {
  const name = 'TK';
  function displayName() {
    console.log(name);
  }
  return displayName;
};

```

What do we have here?

* Our main function is called `makeFunction`
* A constant named `name` is assigned with the string, `'TK'`
* The definition of the `displayName` function (which just logs the `name` constant)
* And finally, `makeFunction` returns the `displayName` function

This is just a definition of a function. When we call the `makeFunction`, it will create everything within it: a constant and another function, in this case.

As we know, when the `displayName` function is created, the closure is also created and it makes the function aware of its environment, in this case, the `name` constant. This is why we can `console.log` the `name` constant without breaking anything. The function knows about the lexical environment.

```javascript
const myFunction = makeFunction();
myFunction(); // TK

```

Great! It works as expected. The return value of `makeFunction` is a function that we store in the `myFunction` constant. When we call `myFunction`, it displays `TK`.

We can also make it work as an arrow function:

```javascript
const makeFunction = () => {
  const name = 'TK';
  return () => console.log(name);
};

```

But what if we want to pass the name and display it? Simple! Use a parameter:

```javascript
const makeFunction = (name = 'TK') => {
  return () => console.log(name);
};

// Or as a one-liner
const makeFunction = (name = 'TK') => () => console.log(name);

```

Now we can play with the name:

```javascript
const myFunction = makeFunction();
myFunction(); // TK

const myFunction = makeFunction('Dan');
myFunction(); // Dan

```

`myFunction` is aware of the argument that's passed in, and whether it's a default or dynamic value.

The closure makes sure the created function is not only aware of the constants/variables, but also other functions within the function.

So this also works:

```javascript
const makeFunction = (name = 'TK') => {
  const display = () => console.log(name);
  return () => display();
};

const myFunction = makeFunction();
myFunction(); // TK

```

The returned function knows about the `display` function and is able to call it.

One powerful technique is to use closures to build "private" functions and variables.

Months ago I was learning data structures (again!) and wanted to implement each one. But I was always using the object oriented approach. As a functional programming enthusiast, I wanted to build all the data structures following FP principles (pure functions, immutability, referential transparency, etc.).

The first data structure I was learning was the Stack. It is pretty simple. The main API is:

* `push`: add an item to the first place of the stack
* `pop`: remove the first item from the stack
* `peek`: get the first item from the stack
* `isEmpty`: verify if the stack is empty
* `size`: get the number of items the stack has

We could clearly create a simple function to each "method" and pass the stack data to it. It could then use/transform the data and return it.

But we can also create a stack with private data and only expose the API methods. Let's do this!

```javascript
const buildStack = () => {
  let items = [];

  const push = (item) => items = [item, ...items];
  const pop = () => items = items.slice(1);
  const peek = () => items[0];
  const isEmpty = () => !items.length;
  const size = () => items.length;

  return {
    push,
    pop,
    peek,
    isEmpty,
    size,
  };
};

```

Because we created the `items` stack inside our `buildStack` function, it is "private". It can be accessed only within the function. In this case, only `push`, `pop`, and so one could touch the data. This is exactly what we're looking for.

And how do we use it? Like this:

```javascript
const stack = buildStack();

stack.isEmpty(); // true

stack.push(1); // [1]
stack.push(2); // [2, 1]
stack.push(3); // [3, 2, 1]
stack.push(4); // [4, 3, 2, 1]
stack.push(5); // [5, 4, 3, 2, 1]

stack.peek(); // 5
stack.size(); // 5
stack.isEmpty(); // false

stack.pop(); // [4, 3, 2, 1]
stack.pop(); // [3, 2, 1]
stack.pop(); // [2, 1]
stack.pop(); // [1]

stack.isEmpty(); // false
stack.peek(); // 1
stack.pop(); // []
stack.isEmpty(); // true
stack.size(); // 0

```

So, when the stack is created, all the functions are aware of the `items` data. But outside the function, we can't access this data. It's private. We just modify the data by using the stack's builtin API.

## **Curry**

> "Currying is the process of taking a function with multiple arguments and turning it into a sequence of functions each with only a single argument."   
> - [Frontend Interview](https://frontendinterview.co/question/what-is-currying-function?tech=javascript)

So imagine you have a function with multiple arguments: `f(a, b, c)`. Using currying, we achieve a function `f(a)` that returns a function `g(b)` that returns a function `h(c)`.

Basically: `f(a, b, c)` —> `f(a) => g(b) => h(c)`

Let's build a simple example that adds two numbers. But first, without currying:

```javascript
const add = (x, y) => x + y;
add(1, 2); // 3

```

Great! Super simple! Here we have a function with two arguments. To transform it into a curried function we need a function that receives `x` and returns a function that receives `y` and returns the sum of both values.

```javascript
const add = (x) => {
  function addY(y) {
    return x + y;
  }

  return addY;
};

```

We can refactor `addY` into a anonymous arrow function:

```javascript
const add = (x) => {
  return (y) => {
    return x + y;
  }
};

```

Or simplify it by building one liner arrow functions:

```javascript
const add = (x) => (y) => x + y;

```

These three different curried functions have the same behavior: build a sequence of functions with only one argument.

How can we use it?

```javascript
add(10)(20); // 30

```

At first, it can look a bit strange, but there's a logic behind it. `add(10)` returns a function. And we call this function with the `20` value.

This is the same as:

```javascript
const addTen = add(10);
addTen(20); // 30

```

And this is interesting. We can generate specialized functions by calling the first function. Imagine we want an `increment` function. We can generate it from our `add` function by passing `1` as the value.

```javascript
const increment = add(1);
increment(9); // 10

```

When I was implementing [Lazy Cypress](https://github.com/leandrotk/lazy-cypress), an npm library to record user behavior on a form page and generate Cypress testing code, I wanted to build a function to generate this string `input[data-testid="123"]`. So I had the element (`input`), the attribute (`data-testid`), and the value (`123`). Interpolating this string in JavaScript would look like this: `${element}[${attribute}="${value}"]`.

My first implementation was to receive these three values as parameters and return the interpolated string above:

```javascript
const buildSelector = (element, attribute, value) =>
  `${element}[${attribute}="${value}"]`;

buildSelector('input', 'data-testid', 123); // input[data-testid="123"]

```

And it was great. I achieved what I was looking for. 

But at the same time, I wanted to build a more idiomatic function. Something where I could write "G_et element X with attribute Y and value Z_". So if we break this phrase into three steps:

* "_get an element X_": `get(x)`
* "_with attribute Y_": `withAttribute(y)`
* "_and value Z_": `andValue(z)`

We can transform `buildSelector(x, y, z)` into `get(x)` ⇒ `withAttribute(y)` ⇒ `andValue(z)` by using the currying concept.

```javascript
const get = (element) => {
  return {
    withAttribute: (attribute) => {
      return {
        andValue: (value) => `${element}[${attribute}="${value}"]`,
      }
    }
  };
};

```

Here we use a different idea: returning an object with function as key-value. Then we can achieve this syntax: `get(x).withAttribute(y).andValue(z)`.

And for each returned object, we have the next function and argument.

Refactoring time! Remove the `return` statements:

```javascript
const get = (element) => ({
  withAttribute: (attribute) => ({
    andValue: (value) => `${element}[${attribute}="${value}"]`,
  }),
});

```

I think it looks prettier. And here's how we use it:

```javascript
const selector = get('input')
  .withAttribute('data-testid')
  .andValue(123);

selector; // input[data-testid="123"]

```

The `andValue` function knows about the `element` and `attribute` values because it is aware of the lexical environment like with closures that we talked about before.

We can also implement functions using "partial currying" by separating the first argument from the rest for example.

After doing web development for a long time, I am really familiar with the [event listener Web API](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener). Here's how to use it:

```javascript
const log = () => console.log('clicked');
button.addEventListener('click', log);

```

I wanted to create an abstraction to build specialized event listeners and use them by passing the element and a callback handler.

```javascript
const buildEventListener = (event) => (element, handler) => element.addEventListener(event, handler);

```

This way I can create different specialized event listeners and use them as functions.

```javascript
const onClick = buildEventListener('click');
onClick(button, log);

const onHover = buildEventListener('hover');
onHover(link, log);

```

With all these concepts, I could create an SQL query using JavaScript syntax. I wanted to query JSON data like this:

```javascript
const json = {
  "users": [
    {
      "id": 1,
      "name": "TK",
      "age": 25,
      "email": "tk@mail.com"
    },
    {
      "id": 2,
      "name": "Kaio",
      "age": 11,
      "email": "kaio@mail.com"
    },
    {
      "id": 3,
      "name": "Daniel",
      "age": 28,
      "email": "dani@mail.com"
    }
  ]
}

```

So I built a simple engine to handle this implementation:

```javascript
const startEngine = (json) => (attributes) => ({ from: from(json, attributes) });

const buildAttributes = (node) => (acc, attribute) => ({ ...acc, [attribute]: node[attribute] });

const executeQuery = (attributes, attribute, value) => (resultList, node) =>
  node[attribute] === value
    ? [...resultList, attributes.reduce(buildAttributes(node), {})]
    : resultList;

const where = (json, attributes) => (attribute, value) =>
  json
    .reduce(executeQuery(attributes, attribute, value), []);

const from = (json, attributes) => (node) => ({ where: where(json[node], attributes) });

```

With this implementation, we can start the engine with the JSON data:

```javascript
const select = startEngine(json);

```

And use it like a SQL query:

```javascript
select(['id', 'name'])
  .from('users')
  .where('id', 1);

result; // [{ id: 1, name: 'TK' }]

```

That's it for today. I could go on and on showing you a lot of different examples of abstractions, but I'll let you play with these concepts.

You can other articles like this [on my blog](https://leandrotk.github.io/tk/2020/03/closure-currying-and-cool-abstractions/index.html).

My [Twitter](https://twitter.com/leandrotk_) and [Github](https://github.com/leandrotk).

## Resources

* [Blog post source code](https://github.com/tk-notes/blog/tree/master/closures-currying-and-cool-abstractions)
* [Closures | MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
* [Currying | Fun Fun Function](https://www.youtube.com/watch?v=iZLP4qOwY8I)
* [Learn React by building an App](https://alterclass.io/?ref=5ec57f513c1321001703dcd2)

