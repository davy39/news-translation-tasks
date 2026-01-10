---
title: 'An Intro to Imba: the JavaScript-compatible language for lightning fast DOM
  updates'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T07:56:49.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-imba-the-alternative-to-javascript-e2aa1e3d1769
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Clq_Sxied7OsDJPgH-n1yw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: vue
  slug: vue
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  Imba is an open-source programming language we created specifically for building
  web apps. It compiles to JavaScript and works inside the existing JS ecosystem,
  meaning you can use it with Node, npm, and Webpack.

  The big benefit ...'
---

By Per Harald Borgen

Imba is an open-source programming language we created specifically for building web apps. It compiles to JavaScript and works inside the existing JS ecosystem, meaning you can use it with Node, npm, and Webpack.

The big benefit with Imba is that it results in much faster apps than if you were to use virtual DOM-based libraries like React and Vue. The increased speed is thanks to how Imba handles DOM updates, which my cofounder and Imba creator [Sindre Osen Aarsaether](https://www.freecodecamp.org/news/introduction-to-imba-the-alternative-to-javascript-e2aa1e3d1769/undefined) [explains here](https://medium.freecodecamp.org/the-virtual-dom-is-slow-meet-the-memoized-dom-bb19f546cc52).

I’ve been using Imba myself the past few years, and it’s indeed a pleasant language to work with, as the syntax is cleaner than JavaScript, which improves the readability of the code.

Throughout this article I’ll teach you how to start developing simple Imba apps on your own. We’ll start off with some syntax before we move onto creating user interfaces. Finally, I’ll help you get set up on your machine so that you can continue hacking on your own.

### Projects using Imba

But before we jump into code, I want to point out that this isn’t just an obscure language used in hobby projects. Imba powers mission-critical apps for large companies as well.

One example is the [fish auction market](https://rsf.is/) on Iceland. As fish is a big deal on Iceland, this market accounts for 1.6% of the country’s economy — roughly US $390 million.

> So Imba actually handles 1.6% Iceland’s GDP!

![Image](https://cdn-media-1.freecodecamp.org/images/1*hx-omKWeIS8rDU5vfKOC4A.png)

Secondly, the entire learning platform [Scrimba.com](https://scrimba.com/) is built with Imba, both the front-end and the back-end. It’s a complex app which is highly dependent upon Imba’s speedy DOM reconciliation.

![Image](https://cdn-media-1.freecodecamp.org/images/1*th9zBq40K-4HkByEKbILhg.png)

So the language you’ll learn today can both help you build large-scale production applications and smaller side-projects.

Let’s get started!

### The syntax

The Imba syntax has a lot of similarities with JavaScript, but it’s also influenced by Ruby and Python. It’s easy to pick up along the way, so let’s start with an example. Below you’ll see a simple JavaScript function which returns the largest of two numbers, or false if they’re equal:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vCJGm1ZHEkc5BYaAsbgNuw.png)
_findGreatest in JavaScript_

Now let’s translate this into Imba:

![Image](https://cdn-media-1.freecodecamp.org/images/1*FIY4FhDdPoFmHy5I0FxuQA.png)
_findGreatest in Imba_

Just by looking at the two examples, you can probably deduct some core differences between Imba and JavaScript:

1. **function → def.** First off, the `function` keyword has been renamed to `def`.
2. **No parentheses.** Also, the function parameters aren’t wrapped in parentheses. You’ll actually rarely need parentheses in Imba, but you can use it if you’d like to.
3. **Indentations.** Imba is indentation-based. This means we don’t need to use curly brackets, which saves space.
4. **No return.** In Imba, returns are implicit, meaning we don’t have to write `return`. Imba automatically returns the last expression of the function.

Neither of these is the most important aspect of Imba, but together they make the code less verbose than JavaScript. This benefit will become clearer as we progress through this article.

### Building user interfaces

Let’s move onto creating user interfaces. This is actually what Imba is built for. This means that DOM nodes are embedded into the language as so called _first class citizens._

> If you’re coming from React world, you can look at it as if Imba has its own version of JSX built into the language.

Consider the following code in React, which simply renders a button, and logs something to the console when it’s clicked:

![Image](https://cdn-media-1.freecodecamp.org/images/1*7-oYsP6nqhipaw-sgsYfTA.png)

If we rewrite this example to Imba we’ll get the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*NI4x41wXBq9OAFbhoKM6BA.png)

Take a moment to compare the two. There are three things I want you to notice:

1. **Tags are native.** The`class App extends React.Component` has been translated into the much simpler `tag App`. This is because `tag` is a native part of the Imba language. This is true for both DOM tags and custom tags.
2. **No closing tags.** As we’re indenting, we don’t need to close off our tags (e.g. `</butt`on>). This saves us a lot of typing and space.
3. **Simple class syntax.** Adding classes is simple in Imba. Instead of the cumbersome `className="container"` we simply add a `.container` to the tag itself.

You might also have noticed that the event handler is different. We do `:tap.logOut` as opposed to `onClick={this.logOut}`. This is just one of several ways to handle user inputs in Imba, which you can read more about [in the docs](http://imba.io/guides/essentials/event-handling#event-handling) if you’re interested.

### Handling data

Now, let’s have a look at how Imba handles data. In the example below, I’ve modified our app to include a `count` variable in the `App` component’s state. This variable will be increased or decreased depending on which button the user clicks.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CHovwPSo9VYJD5bES9KyTw.png)

Here’s how the rewrite looks in Imba:

![Image](https://cdn-media-1.freecodecamp.org/images/1*JtfkPX_D10cQMTdlYOmEVQ.png)

The most striking difference is the amount of code.

> The Imba example is around half the size, both in lines of code and number of characters.

While lines of code certainly is a shallow comparison, the readability of a codebase is important. Fewer lines, fewer characters and fewer symbols make the Imba example easier to read than React.

#### Implicit self

One thing you also might have noticed is that we accessed our instance variable directly through `count`, as opposed to React, where we use `this.state.count` in order fetch the value.

In Imba, we could have done `self.count`. However, the `self` is implicit, so we don’t need to write it. Imba checks if there’s either a `count` variable in the scope, or if`count` exists as an instance variable on `App` itself.

#### Mutability

Another big difference between the two examples above is how they treat state changes. In the Imba example, the state is mutable, as we simply change it — the `count` variable — directly.

This follows an opposing pattern than React, where `this.state` is to be treated as immutable, and the only way to change it is through `this.setState`.

You can use an immutable library along with Imba if you prefer that. It’s actually agnostic in that sense. At Scrimba we use mutability, as we don’t think the costs of going immutable is worth it.

### Setting up Imba locally

Now that you’ve learned the basics, it’s about time you start coding for yourself, so let’s get you set up on your local machine. Simply follow these four steps, and you’ll be good to go:

```
git clone https://github.com/somebee/hello-world-imba.git
```

```
cd hello-world-imba
```

```
npm install
```

```
npm run dev
```

Navigate to [http://localhost:8080/](http://localhost:8080/) and you’ll see your project. Open _src/client.imba_ to start modifying the app.

Alternatively, if you want to get started without setting it up locally you can use [this interactive Scrimba playground.](https://scrimba.com/c/cyW2esn?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=imba_intro_article)

### The speed of Imba

Before we round off, let’s also look at Imba’s speed. This reason it’s so incredibly fast is actually because it _isn’t_ following the virtual DOM implementation which React has made popular. It’s using something it calls the Memoized DOM instead, which is simpler and more direct way of doing it.

In the [benchmark](https://somebee.github.io/dom-reconciler-bench/index.html) below, we count how many DOM operations we’re able to do per second through performing a _live test_ alongside Vue and React. The three libraries do the exact same thing, which is to modify a todo-list thousands of times.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EXQcYGJWR06_EDyRc0MRSA.png)
_Benchmarking Imba against React and Vue. The result: 20–30 times faster DOM reconciliation._

> As you can see, Imba actually handles 20–30 times more operations than React and Vue.

So Imba is fast. Really fast.

#### Rounding up

There are many other things to learn about Imba, so I’d recommend you to visit the [doc’s.](http://imba.io/) For example, its concepts of getters/setters and implicit invocations are important to get a grasp of. The learning curve might be a bit steep in the beginning, but that’s just how it is. Everything worth doing in life requires a little bit of pain and effort ;)

In the next article, I’ll cover some of the more advanced features. [Follow me on Twitter](http://bit.ly/perborgen) to be notified when that time comes.

Good luck and happy coding!

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=imba_intro_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=imba_intro_article)_

