---
title: Why ClojureScript works so well with NPM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T15:03:32.000Z'
originalURL: https://freecodecamp.org/news/why-clojurescript-works-so-well-with-npm-128221d302ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7BrQfhUCEy_NObCNy3nv0A.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jacek Schae

  Every language that complies/transpiles to JavaScript wants to connect to npm to
  use this huge ecosystem. The master of this is, of course, ECMAScript. The second
  one — in my humble opinion — is ClojureScript, due to shadow-cljs.


  Disc...'
---

By Jacek Schae

Every language that complies/transpiles to JavaScript wants to connect to npm to use this huge ecosystem. The master of this is, of course, ECMAScript. The second one — in my humble opinion — is ClojureScript, due to [shadow-cljs](https://github.com/thheller/shadow-cljs).

> Disclaimer: I know there is a lot of work going on in different communities that tap into npm. By all means I’m not trying to diminish any of that by stating that CLJS (ClojureScript) is the best . I just want to give you a glance at how this works in ClojureScript.

### Installing npm packages

In ClojureScript, we install npm packages as we would in JavaScript. We use the standard package.json and [shadow-cljs](https://github.com/thheller/shadow-cljs) build tool and you’ll figure out the rest.

![Image](https://cdn-media-1.freecodecamp.org/images/UBPt1Q5nW8lvc4QSIE5Xmflmx17dCaDnvHAf)
_Install firebase_

After the installation, we have to require the package. The `require` statement is almost identical to `import` from JS. In CLJS we swap the order — first we say from where, and then what.

![Image](https://cdn-media-1.freecodecamp.org/images/tMBZsomfbJl47awHgNXrbAyj2bE4kVodwpsQ)

Every ClojureScript file starts with a ns — namespace declaration. Following that we have require instead of import . And then we define a function with defn. This function will tap into our required firebase packages, and instead of using . to navigate to our method initializeApp, we use / . We make sure that when we invoke the JS method _initializeApp_ we convert CLJS map (datastructure) to a JS Object with `#js`.

Let’s try some other npm packages to get a better feeling for the interop between npm and ClojureScript.

### React

How about using React? ClojureScript has a couple of wrappers for React— the most popular one is [Reagent](https://github.com/reagent-project/reagent). Here is a simple counter example with React hooks and Reagent.

![Image](https://cdn-media-1.freecodecamp.org/images/tIxelAYrSbrtoDJu5QDZiNTeMODKeHfYnMLe)
_JaveScript React and ClojureScript Reagent_

In both examples, we first import/require React and Reagent. Then we define state in React using hooks (and in Reagent using atoms).

What follows is a JSX (JavaScript) and hiccup (ClojureScript) component.

This is cool, but how do we use React UI Libraries from Reagent?

### React UI Libraries

One of the most popular UI libraries is [material-ui](https://material-ui.com/). After the installation we require this library and then import our Button component as well as React. In Clojure Script we only require the Button. We don’t need to require Reagent since it’s in our ClojureScript deps. To interop with React we would use `:&`gt; form and pass all of the properties that we want in `a` {} .

![Image](https://cdn-media-1.freecodecamp.org/images/qhK96GMfydism4K6VugPXBt5PTAP02UHwpzw)

### Redux

How about Redux, you might ask? Well, there is a library that is build on top of Reagent, called [re-frame](https://github.com/Day8/re-frame/tree/master/docs). First designed in Dec 2014, it even pre-dates the official [Elm Architecture](https://guide.elm-lang.org/architecture/).

![Image](https://cdn-media-1.freecodecamp.org/images/qOUTrm4E9RM1wEnC64sQagJ4lm4QkBricVn3)

By now you should have a pretty good picture as to why CLJS loves the npm ecosystem and how easy it is to interop from CLJS to JS. Maybe this is interesting to you, and you are wondering why? Why should you even try ClojureScript?

### Why?

#### Immutable

All ClojureScritp data structures are immutable and persistent. You don’t need to learn a new API if you want to leverage something like [ImmutableJS](https://immutable-js.github.io/immutable-js/).

#### Functional

ClojureScript embraces Functional Programming ideas at its core. You don’t need [Lodash](https://lodash.com/) or [Ramda](https://ramdajs.com/).

#### Simple

With [shadow-cljs](https://github.com/thheller/shadow-cljs) you don’t need to spend time configuring your builds. You require what you need and the build tool will do the job.

#### Concise

You liability is the LoC you write . ClojureScript is one of the concise programming languages out there. Check out the last section of [this comparison](https://medium.freecodecamp.org/a-real-world-comparison-of-front-end-frameworks-with-benchmarks-2018-update-e5760fb4a962).

#### **Powerful**

ClojureScript uses [Google Closure Tools](https://developers.google.com/closure/) for code minification and tree shaking. The same tools that Google is using to build Gmail, Google Calendar, Google Docs, and Google Maps.

#### JavaScript

It compiles/transpiles to JavaScript. Just as ES (EcmaScript) ReasonML, PureScript, and Elm.

#### Friendly

The ClojureScript community is the most friendly and welcoming group of people that I have ever meet online. We mainly hang out on [Slack](http://clojurians.net/) and [ClojureVerse](https://clojureverse.org/).

#### **Full-Stack**

ClojureScript’s older brother, Clojure, embraces all of these ideas with Java. If you want to write your server on one of the most performant and stable platforms there is — the Java Virtuel Machine — you can do that using the same language.

> If you like this article you should follow me on [Twitter](https://twitter.com/JacekSchae). I only write/tweet about programming and technology — mainly about ClojureScript and Clojure.

