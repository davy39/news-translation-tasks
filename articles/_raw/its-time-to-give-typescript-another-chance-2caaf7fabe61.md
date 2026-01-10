---
title: It’s time to give TypeScript another chance
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-17T07:14:38.000Z'
originalURL: https://freecodecamp.org/news/its-time-to-give-typescript-another-chance-2caaf7fabe61
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i0qclSPNcjj8cWOPr3wLxg.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Jason Dreyzehner

  Since 2012, TypeScript has been a popular choice for programmers coming to JavaScript
  from more structured languages (like C++ or Java). But it’s also been largely dismissed
  by those native to the JavaScript world.

  You may have he...'
---

By Jason Dreyzehner

Since 2012, TypeScript has been a popular choice for programmers coming to JavaScript from more structured languages (like C++ or Java). But it’s also been largely dismissed by those native to the JavaScript world.

You may have heard that the Angular team recently [switched to TypeScript for Angular 2](https://vsavkin.com/writing-angular-2-in-typescript-1fa77c78d8e8). So have the teams behind [RxJS](https://github.com/ReactiveX/rxjs), [Ionic](https://blog.ionic.io/announcing-ionic-2-0-0-final/), [Cycle.js](https://cycle.js.org/), [Blueprint](https://github.com/palantir/blueprint), [Dojo](https://dojotoolkit.org/community/roadmap/vision.html), [NativeScript](https://github.com/NativeScript/NativeScript), [Plottable](https://github.com/palantir/plottable), and others.

If you’ve been in JavaScript/Node.js land for a while, it’s easy to assume that the shot-callers for these projects have lost their minds. Or maybe that they were paid off by Microsoft. ?

![Image](https://cdn-media-1.freecodecamp.org/images/VD0zelL6oRdE5C5mBEc8CV4sOTNNz3PdiNRa)

And if you haven’t been watching closely, you may have missed TypeScript’s amazing progress over the past year (and even the past few months).

**If you’re still thinking “TypeScript is kinda like CoffeeScript, right?”—this article is for you.**

There are dozens of great resources and articles on the benefits of using TypeScript. I hope that after reading this, you’ll take another look.

### JavaScript — with Types?

For those new to this discussion, it’s important to understand the aversion that much of the JavaScript world has to types. Besides its portability, much of JavaScript’s popularity could be attributed to its simplicity.

> “To be attractive to hackers, a language must be good for writing the kinds of programs they want to write. And that means, perhaps surprisingly, that it has to be good for writing throwaway programs.” — Paul Graham, [Being Popular](http://paulgraham.com/popular.html)

The kind of programmers who make JavaScript their tool of choice often do so for its flexibility. There’s no standard library, very little structure, and without types, JavaScript users don’t need to spend much time thinking about details when hacking on a new idea.

This is probably easiest to contrast to a language like C++, where programs tend to require a lot more structure and overhead. A lot of JavaScript programmers (particularly the above hacker-types) find the tedium of traditional classes, boilerplate, types, and typecasting slow them down.

> _“Give me your tired, your poor, your huddled masses yearning to breathe free — of over-protective programming languages.” — JavaScript_ ?️ _(basically)_

With this perspective, it’s easy to see why a lot of JavaScript users are so averse to the idea of JavaScript with types.

**Here are some insights that might help to ease those fears.**

### TypeScript is JavaScript with better linting

Probably one of the most common concerns with the idea of using TypeScript is that it isn’t _pure_ JavaScript. Because TypeScript is its own language, it’s assumed your code will be transpiled into a messy glob which you’ll someday be forced to debug.

![Image](https://cdn-media-1.freecodecamp.org/images/4KJABu71ToVztq9ECbZnIs6Jesry5geC5fq-)
_Too many people have this impression of Typescript._

Besides TypeScript being extremely well-tested and widely in use, it’s worth noting that depending on your configuration, very little “transpiling” is actually happening (if any). TypeScript is just Javascript with optional typings.

![Image](https://cdn-media-1.freecodecamp.org/images/Op0RURU0iG-XSOpaHcUcbNOhjdDzeAUTPC5f)
_Type a little extra now, get instant feedback when “add” is used incorrectly. You also get up-to-date documentation free (without JSDoc tags to maintain), and fantastic editor and tooling support._

**TypeScript is like a highly-advanced linter, able to check documentation and warn when code is not being used as intended.**

It provides immediate feedback and a better development experience for all future users of your code. This is also a good test for new projects—if your project is worth linting to enforce code style conventions, your project is probably long-lasting enough to benefit from TypeScript.

The TypeScript team has [committed to tracking JavaScript](https://github.com/Microsoft/TypeScript/wiki/TypeScript-Design-Goals) for the foreseeable future. So if/when additional features stabilize in JavaScript, TypeScript will match them and adapt.

### TypeScript eliminates runtime overhead

Another common misconception is that TypeScript’s type checking somehow persists into the runtime environment, adding complexity and overhead.

In fact, TypeScript is a good way to avoid runtime type checking overhead.

**TypeScript is a development-time/compile-time tool** — it takes in standard JavaScript with optional type-hints and outputs JavaScript with those hints removed. (If enabled, it can also transpile ES6 and ES7 JavaScript features back to current standards.)

TypeScript’s type-hints give us all the benefits of types, and then they disappear.

The only clues left at runtime of an object’s _type_ are the same clues provided by standard JavaScript features. (For example, when you create a new object from a prototype, you might check its type with `instanceof`.)

Ironically, because JavaScript doesn’t provide a standard means of development-time type checking, many of the most developed JavaScript libraries **reimplement their own runtime type checking systems**.

![Image](https://cdn-media-1.freecodecamp.org/images/DaV5pfLgbs5XVe8C2mUevmbcf8u8zZHYwJ3Q)
_Runtime type checking in the [Snippet→](https://github.com/request/request" rel="noopener" target="_blank" title="">Request</a> library. This provides a much better debugging experience for users who use the method incorrectly. But it requires more code at runtime and more cases to unit test. <a href="https://github.com/request/request/blob/092e1e657326626da0b8ac4cfe8752751689313b/index.js#L43-L55" rel="noopener" target="_blank" title=")_

These libraries don’t intend to do this at the outset, but part of providing a good development experience is ensuring developers see clear and actionable errors when they’ve made a mistake.

In pursuit of this goal, many libraries extensively check the types of parameters passed to methods at runtime, throwing errors meant only for the eyes of the developer implementing the method.

**This is most certainly the worst of both worlds_._** These cascades of runtime type checks add significant code bloat, make code less readable, and increase the difficulty of maintaining 100% unit test coverage.

Across large codebases, these runtime tests really add up. After a bit of refactoring, many largest codebases end up with **whole type systems**.

![Image](https://cdn-media-1.freecodecamp.org/images/tSTFwJOfo1V4VmlZ8bMJPtQEElxV0fsRmcue)
_[Snippet→](https://github.com/bcoin-org/bcoin/" rel="noopener" target="_blank" title="">Bcoin</a> provides a good development experience by failing fast (at runtime) and emitting helpful errors. But this comes at the cost of maintaining and testing an extensive, runtime type checking system. It would be more helpful and efficient to do this with Typescript. <a href="https://github.com/bcoin-org/bcoin/blob/4e7df6ef875e5936bea5139d922871498b4d9586/lib/primitives/tx.js#L84-L123" rel="noopener" target="_blank" title=")_

Without using Typescript, not only do you lose out on development-time type checking—you often shift it into runtime. (_I hope you have full test coverage._)

When you use TypeScript, you provide your users with an even better development experience, reduce runtime type checking to only cases where it’s needed (sanitizing end-user input, for example), and make your code easier to fully unit test.

### TypeScript has come a long way

Maybe for the reasons mentioned above, when I first heard of TypeScript, I ran the opposite direction as fast as I could. Besides being antithetical to the “best thing about JavaScript” (less structure), it was _made by Microsoft_.

But it’s not 2012 anymore. TypeScript is not a [leaky abstraction](https://en.wikipedia.org/wiki/Leaky_abstraction) of JavaScript, and the TypeScript project has some of the best hackers and engineers in this space. (And I’m impressed with how well Microsoft is managing it.)

**Since TypeScript tracks ECMAScript, using TypeScript doesn’t lock your project to a new language.** A lot of people still don’t realize this, so it’s not uncommon to hear sentiments like:

> “It’s hard to maintain a TypeScript project.”

Which, to me, sounds like:

> “It’s hard to maintain a project with linting.”

If your project somehow stops benefitting from TypeScript, you can run your project through the compiler (one last time) to remove all types from your codebase.

Then you’re back to untyped JavaScript.

### TL;DR

TypeScript has improved a lot recently. If you heard about TypeScript years ago, but haven’t really followed it since then, it’s worth another look.

### When to use TypeScript

#### [**Angular: Why TypeScript?**](https://vsavkin.com/writing-angular-2-in-typescript-1fa77c78d8e8)

A short technical discussion of exactly why the Angular team chose TypeScript to build Angular 2.

#### [**All JS Libraries Should be Authored in TypeScript**](http://staltz.com/all-js-libraries-should-be-authored-in-typescript.html)

A summary of why Typescript is a good idea for JS libraries, from the creator of Cycle.js and contributor to RxJS.

#### [**TypeScript Deep Dive — Why TypeScript**](https://basarat.gitbooks.io/typescript/content/docs/why-typescript.html)

A good summary of the benefits of using TypeScript. ([TypeScript Deep Dive](https://basarat.gitbooks.io/typescript/) is a great general reference.)

### Learn about TypeScript

#### [**The TypeScript tutorial**](https://www.typescriptlang.org/docs/tutorial.html)

A short tutorial maintained by the TypeScript team.

#### [**TypeScript Design Goals**](https://github.com/Microsoft/TypeScript/wiki/TypeScript-Design-Goals)

A short wiki outlining the TypeScript team’s general design principles.

![Image](https://cdn-media-1.freecodecamp.org/images/v6Z91ppLcyGMvaboJMYIqUKa-n-kaubsaqxM)

### [**typescript-starter**](https://github.com/bitjson/typescript-starter)

A boilerplate project for building JavaScript libraries. Includes proper unit testing, documentation generation, and both CommonJS and ES6 Module exports (for Node.js and the browser).

I wrote this with the hope of changing minds. If you have any ideas for how I could improve this article, please [let me know](https://twitter.com/bitjson).

Please ♡ and [share this post](https://twitter.com/bitjson/status/832497164467183616) if you found it interesting. Thanks for reading!

