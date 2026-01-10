---
title: Psst! Here’s why ReasonReact is the best way to write React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-20T17:10:34.000Z'
originalURL: https://freecodecamp.org/news/psst-heres-why-reasonreact-is-the-best-way-to-write-react-5088d434d035
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jU57ThAZc50pyAG1INey3g.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: reasonml
  slug: reasonml
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By David Kopal

  Are you using React to build user interfaces? Well, I am too. And now, you’ll learn
  why you should write your React applications using ReasonML.

  React is a pretty cool way to write user interfaces. But, could we make it even
  cooler? Be...'
---

By David Kopal

Are you using [React](https://reactjs.org/) to build user interfaces? Well, I am too. And now, you’ll learn why you should write your React applications [using ReasonML](https://medium.freecodecamp.org/learn-reasonml-by-building-tic-tac-toe-in-react-334203dd513c).

React is a pretty cool way to write user interfaces. But, could we make it even cooler? Better?

To make it better, we need to identify its problems first. So, what is the main problem of React as a JavaScript library?

### **React wasn’t initially developed for JavaScript**

If you take a closer look at React, you’ll see that some of its main principles are foreign to JavaScript. Let’s talk about immutability, functional programming principles, and type system in particular.

Immutability is one of the core principles of React. You don’t want to mutate your props or your state because if you do, you might experience unpredictable consequences. In JavaScript, we don’t have immutability out of the box. We are keeping our data structures immutable by a convention, or we use libraries such as [immutableJS](https://facebook.github.io/immutable-js/) to achieve it.

React is based on the principles of functional programming since its applications are compositions of functions. Although JavaScript has some of these features, such as first-class functions, it’s not a functional programming language. When we want to write some nice declarative code, we need to use external libraries like [Lodash/fp](https://github.com/lodash/lodash/wiki/FP-Guide) or [Ramda](https://ramdajs.com/).

So, what’s up with the type system? In React, we had [PropTypes](https://reactjs.org/docs/typechecking-with-proptypes.html). We’ve used them to mimic the types in JavaScript since it isn’t a statically typed language itself. To take advantage of advanced static typing, we again need to use external dependencies, such as [Flow](https://flow.org/) and [TypeScript](https://www.typescriptlang.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/MBTOborji3cqg5Fulhsv9cA3tiEoSi8fu3l4)
_React, and JavaScript comparison_

As you can see, **JavaScript isn’t compatible with React’s core principles.**

Is there another programming language that would be more compatible with React than JavaScript?

Fortunately, we have [ReasonML](https://reasonml.github.io/).

In Reason, we get immutability out of the box. Since it’s based on [OCaml](https://ocaml.org/), the functional programming language, we have such features built into the language itself as well. Reason also provides us with a strong type system on its own.

![Image](https://cdn-media-1.freecodecamp.org/images/QHbj6LVoIlCNOKjfeZdBDkRBClnsL1qnz5kr)
_React, JavaScript, and Reason comparison_

Reason is compatible with React’s core principles.

### Reason

It isn’t a new language. It’s an alternative JavaScript-like syntax and toolchain for OCaml, a functional programming language that’s been around for more than 20 years. Reason was created by Facebook developers who already used OCaml in their projects ([Flow,](https://github.com/facebook/flow) [Infer](https://github.com/facebook/infer)).

![Image](https://cdn-media-1.freecodecamp.org/images/iZOPlVop1OKOO36dranfKTTg9P0b0PGtCR6x)

Reason, with its C-like syntax, makes OCaml approachable for people coming from mainstream languages such as JavaScript or Java. It provides you with better documentation (compared to OCaml) and a [growing community](https://reasonml.github.io/docs/en/community) around it. Plus, it makes it easier to integrate with your existing JavaScript codebase.

![Image](https://cdn-media-1.freecodecamp.org/images/FeHSk51tA2kwbv2sVbu-QinVHCzYipvQUMWp)

OCaml serves as a backing language for Reason. Reason has the same semantics as OCaml — only the syntax is different. This means that you can write OCaml using Reason’s JavaScript-like syntax. As a result, you can take advantage of OCaml’s awesome features, such as its strong type system and pattern matching.

Let’s take a look at an example of Reason’s syntax.

```js
let fizzbuzz = (i) =>
  switch (i mod 3, i mod 5) {
  | (0, 0) => "FizzBuzz"
  | (0, _) => "Fizz"
  | (_, 0) => "Buzz"
  | _ => string_of_int(i)
  };
for (i in 1 to 100) {
  Js.log(fizzbuzz(i))
};
```

Although we’re using pattern matching in this example, it’s still pretty similar to JavaScript, right?

However, the only usable language for browsers is still JavaScript, meaning we need to compile to it.

#### BuckleScript

![Image](https://cdn-media-1.freecodecamp.org/images/X36FEoHL7z2YWiiLNhNWbOy0Wx5O7FTEerBX)

One of Reason’s powerful features is [BuckleScript compiler](https://bucklescript.github.io/), which takes your Reason code, and compiles it to readable and performant JavaScript with great dead code elimination. You’ll appreciate the readability if you’re working on a team where not everyone is familiar with Reason, since they’ll still be able to read the compiled JavaScript code.

The similarity with JavaScript is so close that some of Reason’s code doesn’t need to be changed by the compiler at all. So, you can enjoy the benefits of the statically typed language with no change to the code whatsoever.

```
let add = (a, b) => a + b;add(6, 9);
```

This is valid code in both Reason and JavaScript.

BuckleScript is shipped with four libraries: the standard library called [Belt](https://bucklescript.github.io/bucklescript/api/Belt.html) ([OCaml standard library is insufficient](https://discuss.ocaml.org/t/what-is-the-preferable-solution-for-the-role-of-standard-library/1092)), and bindings to JavaScript, Node.js and, DOM APIs.

Since BuckleScript is based on OCaml compiler, you’ll get [a blazingly fast compilation](https://bucklescript.github.io/docs/en/build-performance) that is much faster than Babel and several times faster than TypeScript.

Let’s compile our FizzBuzz algorithm written in Reason to JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/IQVd0AQHgI7i26a21uf9kALk6xi2CzpGcoiM)
_Reason’s code compilation to JavaScript through BuckleScript_

As you can see, the resulting JavaScript code is pretty readable. It seems like it was written by a JavaScript developer.

Not only does Reason compile to JavaScript, but to native and bytecode as well. So, you can write a single application using Reason syntax and be able to run it in the browser on MacOS, Android, and iOS phones. There’s a game called [Gravitron](https://github.com/jaredly/gravitron) by Jared Forsyth which is written in Reason and it can be run on all the platforms I’ve just mentioned.

#### JavaScript interop

BuckleScript also provides us with JavaScript [interoperability](https://en.wikipedia.org/wiki/Interoperability). Not only can you paste your working JavaScript code in your Reason codebase, but your Reason code can also interact with that JavaScript one. This means you can easily integrate Reason code into your existing JavaScript codebase. Moreover, you can use all the JavaScript packages from the NPM ecosystem in your Reason code. For example, you can combine Flow, TypeScript, and Reason together in a single project.

However, it’s not that simple. To use JavaScript libraries or code in Reason, you need to port it to Reason first via Reason bindings. In other words, you need types for your untyped JavaScript code to be able to take an advantage of Reason’ s strong type system.

Whenever you need to use a JavaScript library in your Reason code, check if the library was already ported to Reason by browsing the Reason Package Index ([Redex](https://redex.github.io/)) database. It’s a website that aggregates different libraries and tools written in Reason and JavaScript libraries with Reason bindings. If you found your library there, you can just install it as a dependency and use it in your Reason application.

However, if you didn’t find your library, you’ll need to write Reason bindings yourself. If you’re just starting with Reason, keep in mind that writing bindings aren’t a thing you want to start with, since it’s one of the more challenging things in Reason’s ecosystem.

Fortunately, I’m just writing a post about writing Reason bindings, so stay tuned!

When you need some functionality from a JavaScript library, you don’t need to write the Reason bindings for a library as a whole. You can do that only for the functions or components you need to use.

### ReasonReact

This article is about writing React in Reason, which you can do thanks to the [ReasonReact library](https://reasonml.github.io/reason-react/).

Maybe you’re now thinking “I still don’t know why I should use React in Reason.”

We’ve already mentioned the main reason to do so — Reason is more compatible with React than JavaScript. Why is it more compatible? Because React was developed for Reason, or more precisely, for OCaml.

#### Road to ReasonReact

![Image](https://cdn-media-1.freecodecamp.org/images/biX58BUYBBeSlVU4t3h4n-wBYAqi8oFUXReH)

React’s first prototype was developed by Facebook and was written in Standard Meta Language ([StandardML](https://en.wikipedia.org/wiki/Standard_ML)), a cousin of OCaml. Then, it was moved to OCaml. React was also transcribed to JavaScript.

This was because the whole web was using JavaScript, and it wasn’t probably smart to say, “Now we’ll build UI in OCaml.” And it worked — React in JavaScript has been widely adopted.

So, we became used to React as a JavaScript library. React together with other libraries and languages — [Elm](https://elm-lang.org/), [Redux](https://redux.js.org/), [Recompose](https://github.com/acdlite/recompose), [Ramda](https://ramdajs.com/), and [PureScript](http://www.purescript.org/) — made functional programming in JavaScript popular. And with the rise of [Flow](https://flow.org/) and [TypeScript](https://www.typescriptlang.org/), static typing became popular as well. As a result, the functional programming paradigm with static types became mainstream in the world of the front-end.

In 2016, [Bloomberg](https://www.bloomberg.com/company/announcements/open-source-at-bloomberg-introducing-bucklescript/) developed and open-sourced BuckleScript, the compiler that transforms OCaml to JavaScript. This enabled them to write safe code on the front-end using OCaml’s strong type system. They took the optimized and blazingly fast OCaml compiler and swapped its back-end generating native code for a JavaScript generating one.

The popularity of **functional programming** together with the release of the BuckleScript generated the ideal climate for Facebook to get back to the original idea of React, which was initially written in an [ML language](https://en.wikipedia.org/wiki/ML_(programming_language)).

![Image](https://cdn-media-1.freecodecamp.org/images/XrSsanYlN4ilFGc7k97yqreJTWjNx0IQrOHl)
_ReasonReact_

They took OCaml semantics and JavaScript syntax, and created Reason. They also created the Reason wrapper around React — ReasonReact library — with additional functionalities such as the encapsulation of the Redux principles in stateful components. By doing so, they returned [React to its original roots](https://news.ycombinator.com/item?id=15209704).

#### The power of React in Reason

When React came into JavaScript, we adjusted JavaScript to React’s needs by introducing various libraries and tools. This also meant more dependencies for our projects. Not to mention that these libraries are still under development and breaking changes are introduced regularly. So you need to maintain these dependencies with care in your projects.

This added another layer of complexity to JavaScript development.

Your typical React application will have at least these dependencies:

![Image](https://cdn-media-1.freecodecamp.org/images/AAN8F1esKaCoYudXoz90QfiWd40IrF8B4IRc)

* static typing — Flow/TypeScript
* immutability — immutableJS
* routing — ReactRouter
* formatting — Prettier
* linting — ESLint
* helper function — Ramda/Lodash

Let’s now swap JavaScript React for ReasonReact.

Do we still need all these dependencies?

![Image](https://cdn-media-1.freecodecamp.org/images/tMqUDBPlT3UvrGwf9UqaBTXanS6QgUqEmOSi)

* static typing — **built-in**
* immutability — **built-in**
* routing — **built-in**
* formatting — **built-in**
* linting — **built-in**
* helper functions — **built-in**

You can learn more about [these built-in features in my other post.](https://www.codinglawyer.io/posts/why-building-stuff-in-reason)

In the ReasonReact application, you don’t need these and many other dependencies since many crucial features that make your development easier are already included in the language itself. So, maintaining your packages will become easier and you don’t have an increase in complexity over time.

This is thanks to the OCaml, which is more than 20 years old. It’s a matured language with all of its core principles in place and stable.

### Wrap-up

At the beginning, the creators of Reason had two options. To take JavaScript and somehow make it better. By doing that they’d also need to deal with its historical burdens.

However, they went a different path. They took OCaml as a matured language with great performance and modified it so it resembles JavaScript.

React is also based on the principles of OCaml. That’s why you’ll get a much better developer experience when you’re using it with Reason. React in Reason represents a safer way of building React components, since the strong type system has got your back and you don’t need to deal with most of the JavaScript (legacy) issues.

### What’s next?

![Image](https://cdn-media-1.freecodecamp.org/images/yD9SkLowMRhycLIc0Zz4X0VjYig9qDQb7EjK)

If you’re coming from the world of JavaScript, it’ll be easier for you to get started with Reason, due to its syntax similarity with JavaScript. If you’ve been programming in React, it’ll be even easier for you since you can use all your React knowledge as ReasonReact has the same mental model as React and very similar workflow. This means you don’t need to start from scratch. You’ll learn Reason as you develop.

The best way to start using Reason in your projects is to do it incrementally. I’ve already mentioned that you can take Reason code and use it in JavaScript, and the other way around. You can do the same thing with ReasonReact. You take your ReasonReact component and use it in your React JavaScript application, and vice versa.

This incremental approach has been chosen by Facebook developers who are using Reason extensively in the development of [the Facebook Messenger app](https://reasonml.github.io/blog/2017/09/08/messenger-50-reason.html).

If you want to build an application using React in Reason and learn the basics of Reason in a practical way, check my other article where [we’ll build a Tic Tac Toe game together.](https://medium.freecodecamp.org/learn-reasonml-by-building-tic-tac-toe-in-react-334203dd513c)

If you have any questions, criticism, observations, or tips for improvement, feel free to write a comment below or reach me via [Twitter](https://twitter.com/coding_lawyer) or [my blog](https://www.codinglawyer.io/).

