---
title: How to get started with Competitive Programming in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-10T16:22:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-competitive-programming-in-javascript-76ad2e760efe
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SPx_5yXieH6SA9dpkyosOw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Priyabrata Biswas

  If you’re not familiar with competitive programming, basically it is a mind sport
  with the aim of writing code to solve given problems. I was introduced to it in
  my freshman year by my seniors. As of this writing, I’m still not r...'
---

By Priyabrata Biswas

If you’re not familiar with [competitive programming](https://en.wikipedia.org/wiki/Competitive_programming), basically it is a mind sport with the aim of writing code to solve given problems. I was introduced to it in my freshman year by my seniors. As of this writing, I’m still not really great at it! Maybe it is due to the fact that I don’t like to code in C++, or maybe I am a lazy person who won’t take the time to actually learn it well enough. But, I like algorithms and data-structures as much as I like JavaScript!

So, the preposterous thought crossed my mind over and over again. ‘What if we start using JavaScript in the competitive arena?’ Turns out, this doesn’t seem like the uncharted territory that I thought it would be. Many platforms like [HackerRank](https://www.hackerrank.com/), [CodeChef](https://www.codechef.com/), and [Codeforces](https://codeforces.com/) support JavaScript.

I know C++ is a lot faster compared to JavaScript and can dynamically allocate memory. C and C++ are quite similar in terms of performance, but competitive programmers mostly use C++ because of its [Standard Template Library](https://www.geeksforgeeks.org/the-c-standard-template-library-stl/) (or STL). It provides common programming data structures like list, stack, array along with container classes, algorithms, and iterators out of the box.

But, JavaScript offers something C++ lacks:

> Freedom!

Being a scripting language, JavaScript is inherently slow. But still, it is the most popular language out there. According to 2018’s [Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey/2018/), 69.8% of respondents use JavaScript for their development purposes. But, at the same time, it doesn’t shine so well in the case of competitive programming. The reason is that it was simply not built for it!

Back in 1995, [Brendan Eich](https://en.wikipedia.org/wiki/Brendan_Eich) developed JavaScript only for adding interactivity to web pages like handling a mouse click.

Today, we can build servers, games, mobile applications, IoT applications and even machine learning in the browser is possible with JavaScript. So, why feel ashamed while using it in competitive programming?

> “Any application that can be written in JavaScript, will eventually be written in JavaScript.” — [Jeff Atwood](https://en.wikipedia.org/wiki/Jeff_Atwood)

Remember what I told you about STL and the toolkit it provides for competitive programming? I thought to myself why doesn’t [TC 39](https://www.ecma-international.org/memento/tc39.htm) come up with something similar for JavaScript!

![Image](https://cdn-media-1.freecodecamp.org/images/1*WscERe0SENQYJ-lh-NRHhw.jpeg)
_Eventually, I had an idea! ?_

Have you heard of ‘Node Package Manager’ also known as ‘**npm**’?

Well, it’s the world’s [largest software registry](https://www.npmjs.com/) with over 874,285 packages (as of this writing) and is the default package manager for Node.js.

> The idea is to develop an npm package much like C++’s STL

### Introducing Mathball

Mathball is an npm package for competitive programming in JavaScript implementing optimized algorithms for faster execution. Okay, now I’m exaggerating! The truth is, it only supports 16 utility functions implementing [brute-force approaches](https://discuss.codechef.com/questions/281/brute-force-approach) so far. I put together this tiny helper library for assisting people in competitive programming.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UbZwDVpX-diNhP4zdxLytg.png)
_how’s the logo! ?_

You can get the package quite easily if you have Node.js and npm installed on your machine by typing the following command in your terminal:

```
npm install mathball
```

You can access all the utilities via a `mathball` object, `M`, like so:

Again, just getting an individual function is as easy as this:

Oh, now you must be thinking —

> How am I supposed to use a third-party library inside a platform like HackerRank or CodeChef?

The answer is simple, just **bundle** it! ?

Let me explain what I mean! Let’s say you are trying to solve this particular problem on HackerRank —

[**Simple Array Sum | HackerRank**](https://www.hackerrank.com/challenges/simple-array-sum/problem)  
[_Calculate the sum of integers in an array._www.hackerrank.com](https://www.hackerrank.com/challenges/simple-array-sum/problem)

Don’t be overwhelmed by all those lines of code. If you’ve used HackerRank before then you already know that it’s just for handling I/O.

First, copy and paste the above contents in a file, `index.js`. Then, in the same directory, open up the terminal and type:

```
npm install mathball
```

Next, inside the `index.js` file, modify the following:

Lastly, in order to bundle everything into a single file, I’m using Webpack but you’re free to choose any CommonJS module bundler!

So, let’s create a `webpack.config.js` file in the same directory with the following code in it:

If you don’t already have Webpack installed, please install it like so:

```
npm install -g webpack webpack-cli
```

Finally, type the following:

```
webpack --config ./webpack.config.js --mode=development
```

Now, the above command will create a file named `bundle.js` in the same directory. So, copy and paste its content on HackerRank and hit ***Submit Code***. That’s it!

![Image](https://cdn-media-1.freecodecamp.org/images/1*XmAdDfmGO6yucBPyeSM1YQ.png)
_Bazinga! ?_

### Epilogue

It doesn’t make sense to go through all that nonsense just so you can compute the sum of an array…right? So I must confess that problems on competitive programming tend to be far more complicated than this.

> I believe competitive programming is more about figuring out ways to solve a problem than just solving them!

Once you figure out what algorithm or data structure your problem needs, coding becomes quite easy if you have a library like Mathball at your disposal. Also, you don’t have to go through all those steps for bundling every time you code something. It’s basically a one-time setup process. Just code along, and bundle your files with the last command.

**Fun fact** — you can use Mathball in your project too!

I will be constantly improving Mathball and I sincerely welcome your contribution. Together, we can make Mathball do so much more! Here’s the [link](https://github.com/pbiswas101/Mathball) for the repo.

The purpose of this article was to evangelize the importance of competitive programming in the JavaScript community. I think learning algorithms and data structures prepares us to care more about the efficiency and complexity of our codebase. It makes us look twice for any memory leaks, and helps us to become better developers, in general.

Here’s a list of resources that inspired me to embark on my journey of supporting JavaScript in competitive programming:

1. [Pranay Dubey — JavaScript for Competitive Programming](https://www.youtube.com/watch?v=2OUw6jRYSKA)
2. [JavaScript for Algorithmic Competitive Programming](https://hackernoon.com/javascript-for-algorithms-competitive-programming-45cf723cd16f)

Thank you for your time! ✌️

