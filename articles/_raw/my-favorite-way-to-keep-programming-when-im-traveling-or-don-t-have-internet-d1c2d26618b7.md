---
title: My favorite way to keep programming when I’m traveling or don’t have internet
subtitle: ''
author: Andrico Karoulla
co_authors: []
series: null
date: '2018-11-14T17:32:46.000Z'
originalURL: https://freecodecamp.org/news/my-favorite-way-to-keep-programming-when-im-traveling-or-don-t-have-internet-d1c2d26618b7
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5djL-YOSdGd_rK_x
tags:
- name: JavaScript
  slug: javascript
- name: personal development
  slug: personal-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'This is a short guide on sharpening your skills and keeping productive
  when in transit. And it doesn’t involve burying your face in a book.

  Books can only get you so far

  Now don’t get me wrong, I love a good programming book. Jon Duckett’s series on
  ...'
---

This is a short guide on sharpening your skills and keeping productive when in transit. And it doesn’t involve burying your face in a book.

### Books can only get you so far

Now don’t get me wrong, I love a good programming book. Jon Duckett’s series on HTML, CSS, and JavaScript were the guiding beacons during my formative years as a Web Developer. Robert C Martin’s seminal tome Clean Code has its pages bent. It is misshapen through years of being wrung dry for each drop of information. Even Simon Holmes’ Getting MEAN, while now dated, had its time by my side in the local café. It was my companion as I created my first full-stack application.

With a little preparation, most of these books could’ve been used with no, or much more frighteningly, slow internet. Download the packages in advance. Get your local environments working. If the book’s comprehensive enough, you’ll likely make solid progress without needing Google, GitHub or StackOverflow.

On the flip-side, we as programmers thrive best when tasked with a challenge. Having an author walk us through solutions is nice, but it’s not enough. The best way for us to improve our problem-solving skills is to solve problems.

If you’re a professional programmer then you’re likely to be solving your fair share of problems on a day-to-day basis. If you’re a hobbyist then you might find pleasure from creating your own [JSF**k](http://www.jsfuck.com/) applications. Or even killing time by solving algorithm challenges online. It’s why sites like CodeWars or HackerRank are so popular.

The underlying problem with most of these, particularly the latter, is continuing when the internet breaks. Or without connection to begin with. Both are common scenarios as developers are becoming more nomadic. How do you kill time during your 12-hour flight from London to Shanghai, while still reaping the rewards gained from solving problems?

I have had the displeasure of being on such a long flight. There’s about enough space on said flight to prop your laptop on the foldout tray. Everything beyond that becomes a game of Tetris, trying to make your comfort and possessions fit in the limited space given to you on your budget flight. So you’ve got your laptop, headphones, jumper, snacks, and water all within arms reach? It’s starting to feel cramped, right? Try pulling out your 600 page 2-kilo programming book. Yeah, not gonna happen.

### The silver bullet

So how did I overcome this impediment? Well, I reimplemented the Lodash library.

Why did I choose a such an arbitrary task? There are many key reasons. Some I rationalized before taking on the challenge and others I discovered along the way. Here are some of the most notable:

* Each function feels like a miniature code challenge
* The documentation is on a single HTML page, easy to download and view offline
* It encourages looking inside the source code when stuck
* It allows you to build your own suite of utility functions
* It’s a library with no dependencies, which keeps things simple
* You will get more familiar with your programming language of choice

Let’s dive a bit more into each of these points.

#### **Each function feels like a code challenge**

As I mentioned earlier on, Codewars and HackerRack are two very popular programming challenge sites. For those unfamiliar, you’re given a programming task to complete within the built-in text-editor. When completed, you run your finished code against the curated suite of tests. The aim of the challenge is to get all tests passing.

It’s not difficult emulating this yourself. If anything, it’s a great way of improving your approach to TDD (test driven development). My general approach to reimplementing a function would be to stub out the method:

```js
const concat = (arr, ...otherParams) => {
  // if array is invalid throw error

  // handle no input for second parameter

  // add each item to a new array
    // flatten 1 level if item is array

  // return new array
};
```

const concat = (arr, ...otherParams) => {  // if array is invalid throw error  // handle no input for second parameter  // add each item to a new array    // flatten 1 level if item is array  // return new array};

The next step is to create my test suite with some assertions I’d expect my function to satisfy:

```js
const concat = require('../concat');

describe('concat', () => {
  it('should return the expect results with valid inputs', () => {
    expect(concat([1, 2], [1], [2], 4939, 'DDD')).toEqual([1, 2, 1, 2, 4939, 'DDD']);
    expect(concat([], null, 123)).toEqual([null, 123]);
  });

  it('should throw errors with invalid inputs', () => {
    expect(() => concat(23, 23).toThrow(TypeError));
    expect(() => concat([1, 2, 3], -1).toThrow(TypeError));
  });

  it('should correctly handle strange inputs', () => {
    expect(concat([111], null, 'rum ham')).toEqual([111, null, 'rum ham']);
  });
});
```

Then I’d implement the code so the tests run successfully:

```js
const { isValidArray } = require('../helpers');

const concat = (arr, ...otherParams) => {
  if (!isValidArray(arr)) throw new Error('Argument is not a valid array');

  if (otherParams.length === 0) return [];

  const concatenatedArray = otherParams.reduce((acc, item) => {
    if (isValidArray(item)) return [...acc, ...item];

    return [...acc, item];
  }, [...arr]);

  return concatenatedArray
};
```

Knocking out one of these functions will leave you with a sense pride and accomplishment.

#### **Simple HTML documentation**

Most libraries have a GitHub page with an API reference. These are usually a single page of Markdown that’s available for download. Take a snippet from the Recompose library:

### `branch()`

```js
branch(
  test: (props: Object) => boolean,
  left: HigherOrderComponent,
  right: ?HigherOrderComponent
): HigherOrderComponent
```

Accepts a test function and two higher-order components. The test function is passed the props from the owner. If it returns true, the `left` higher-order component is applied to `BaseComponent`; otherwise, the `right` higher-order component is applied. If the `right` is not supplied, it will by default render the wrapped component.

There’s plenty of information here to get you on your way. If you’re learning React and want to get your head around HOCs (higher order components), then implementing this library might be a gratifying challenge to take on.

#### **Reviewing the source code**

Up until recently, I wouldn’t take much time to see how the packages I use most frequently work under the hood. Being without Google or StackOverflow made me desperate and so I started to look inside. I don’t know what I expected to see, but it wasn’t a minified, garbled mess.

Opening Pandora’s box didn’t send a swarm of scorn, hate and famine to taunt me and my family. Instead I was welcomed with cleanly written and well-documented code.

You can even take a peek to see how the people at Lodash write their solutions differently to yours:

```js

function concat() {
  var length = arguments.length;
  if (!length) {
    return [];
  }
  var args = Array(length - 1),
      array = arguments[0],
      index = length;

  while (index--) {
    args[index - 1] = arguments[index];
  }
  return arrayPush(isArray(array) ? copyArray(array) : [array], baseFlatten(args, 1));
}
```

You’ll learn new ways of achieving the same goals. Maybe their solutions are more efficient, maybe yours are. It’s still a great way to open your eyes to new paradigms and patterns.

#### **Developing your own utility functions**

Lodash gets a bad rep as a library that has a large footprint. Projects may need a small number of the utilities. We will still import the whole library as a dependency.

You could download the couple of functions that you use. Why not use the methods you spent 8 hours writing whilst flying over the Pacific Ocean? It might not be quite as robust. But you’ll always be reminded of your journey to Angular Fest Hawaii ’19 whenever you whip out your implementation of `_.memoize`.

#### **Keep things simple**

Traveling’s draining and flying’s stressful. When feeling fatigued, any level of bureaucracy that sits in the way of any programming becomes a barrier. The idea is to choose a task that gets you coding with as little friction as possible.

I didn’t want to faff around with a bunch of random dependencies and messy vendor code when packed between two snorers on my overnight flight to Canada. It was a happy accident discovering that Lodash doesn’t rely on any external modules. The Lodash package itself is laid out simply. Each method has its own file, which may import a couple of base or utility methods.

#### **Becoming familiar with your tools of choice**

If you’re reading this article, chances are you’re familiar with JavaScript. Like most other modern programming languages, JavaScript receives semi-regular updates. These updates give you access to some new features. Implementing a library might take you to corners of your chosen language that you’ve never been before. It happened to me.

In fact, I recently came across some of JavaScript’s newer [built-in objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects#Keyed_collections). I’d never used them in code before, so I made a conscious effort to integrate some of them into the utility methods I made:

```js
const difference = (arr, ...otherArgs) => {
  if (!isValidArray(arr)) throw new TypeError('First argument must be an array');

  const combinedArguments = otherArgs.reduce((acc, item) => [...acc, ...item], [])
  if (!isValidArray(combinedArguments)) throw new TypeError('2nd to nth arguments must be arrays');

  const differenceSet = new Set([...arr]);
  combinedArguments.forEach(item => {
    if (differenceSet.has(item)) differenceSet.delete(item);
  });

  return [...differenceSet]
}
```

Using `Set()` makes a lot of sense here. What separates it from a normal array is that only unique values can be stored. This means you can’t have any duplicate values inside of your set. This works well when trying to create a function that removes duplicate values.

Whether you’re a guitarist, a painter, or a molecular physicist, you’re not going to get far without familiarizing yourself with your guitar, or your paints, or your … molecules?

The same goes with being a programmer. Master your tools and actively seek gaps in your knowledge. Make a conscious effort to implement features that you haven’t come across before. Or use ones that you find intimidating. It’s one of the strongest ways to learn.

### **Conclusion**

This isn’t the only way to stay productive when without internet, but it’s worked well for me. In fact, it’s something I recommend people do in the early stages of their programming careers.

I’d love to know if you’ve done something similar, or if you have your own ways of staying sharp without the internet. Let me know below!

Do you know any other packages that would lend themselves well to being rewritten?

#### Thanks for reading!

Knowledge sharing is one of the cornerstones of what makes the development community so great. Please don’t hesitate to comment your solutions.

If you’re interested in hosting me at a conference, meetup, or as a speaking guest for any engagement, then you can DM me on [twitter](https://twitter.com/andricokaroulla?lang=en)!

I hope this article taught you something new. I post regularly, so if you want to keep up to date with my latest releases then you can follow me. And remember, the longer you hold the clap button, the more claps you can give. ???

#### You can also check out my other articles below:

[_Add a touch of Suspense to your web app with React.lazy()_](https://codeburst.io/add-a-touch-of-suspense-to-your-web-app-with-react-lazy-374e66ee05af)

[_How to use Apollo’s brand new Query components to manage local state_](https://medium.com/@andricokaroulla/updated-for-apollo-v2-1-managing-local-state-with-apollo-d1882f2fbb7)

[_No need to wait for the holidays, start Decorating now_](https://codeburst.io/no-need-to-wait-for-the-holidays-start-decorating-now-67b9dabd60d7)

[_Managing local state with Apollo and Higher Order Components_](https://itnext.io/managing-local-state-with-apollo-client-3be522258645)

[_The React Conference drinking game_](https://medium.com/@andricokaroulla/the-react-conference-drinking-game-7a996bfbef3)

[_Develop and Deploy your own React monorepo app in under 2 hours, using Lerna, Travis and Now_](https://codeburst.io/develop-and-deploy-your-own-react-monorepo-app-in-under-2-hours-using-lerna-travis-and-now-2b140d647238)

