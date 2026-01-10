---
title: A bluffer’s guide to JavaScript proficiency
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T16:47:13.000Z'
originalURL: https://freecodecamp.org/news/bluffers-guide-to-javascript-proficiency-18195dbe2618
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7ieiD5CDf0l6rYS5LvODGQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Greg Byrne

  So you’re trying to learn JavaScript but are inundated with all the different syntax
  and ways to program that have evolved over time?

  Why is that code littered with backticks? What in the world are these mysterious
  arrows, they look lik...'
---

By Greg Byrne

So you’re trying to learn JavaScript but are inundated with all the different syntax and ways to program that have evolved over time?

Why is that code littered with backticks? What in the world are these mysterious arrows, they look like someones introduced emoji’s? 3 dots, what the what?

Our industry consists of a mass of psychologically frayed individuals ever stressing about imposter syndrome and self doubt. “_Will I be found out that I don’t know what I’m doing?”, “I haven’t a clue how this code works, it just seems to run with magic.” “I got nowhere yesterday and everyone is looking at me now in the daily scrum”. “I’m such a failure and everyone is doing better than I am”_. Familiar?

In an environment where knowledge is power, we are ever the hamster on a learning treadmill just trying to outpace everyone else so we don’t look stupid in front of our peers. This lack of (my) knowledge became clear recently when I joined a front-end project comprised primarily of JavaScript code. I thought I knew JavaScript. I was completely wrong.

You say, _“Don’t you have to use the function keyword to declare functions?”_ (because it said so in that blog/video you’ve read/watched the other day); “_Idiot — how do you not know about Arrow functions. Pshhaw!”_ gloats a colleague.

> Note: not my experience thankfully, but please reconsider your environment if it’s that hostile…

So I give you this, a bluffer’s guide, to get you through your day. A highlight reel of JavaScript syntax introduced in ES2015+ that all the kids are using these days, as well as some not-so-well-known JS features. It will help disguise those awkward moments when you nod understanding and politely change subject.

Before you cry _“Oh Greg you fool, you created an article that is TLDR, where am I going to find the 15+ minutes to read your article”._ Firstly, I recognise that pain of not having enough time in life, so I empathise. Secondly, the article is broken into sections regarding a particular syntax, so if you’re not interested in Arrow functions, then skip it. Not sure about Template literals, then hang around for 2–3 mins, friend, and let me tell you all about it. **You do not have to consume the article in its entirety in one go!**

I make no attempt to hide that this article is for those learning JavaScript and **have the basic knowledge of how JavaScript works!** For this article to be of use to you, you must know how to write JavaScript (e.g. just the basics of functions, objects, etc.). If not, go check out my other JavaScript posts and/or supplement that with a video tutorial on JavaScript fundamentals if need be.

**Also, this article explains mostly using syntax introduced in ES2015 and beyond which may not be supported in every browser**. Using Babel, most syntax can be compiled for compatibility. For others like _Set_ or _includes()_, you can polyfill, but that is beyond the scope of this article. Always **check with browser compatibility tables**, your projects browser support requirements, and your tech lead(s) about introducing something new

### var is for chumps; let and const are the future

`let` and `const` are new variable declarations introduced in ES2015. The difference between these and `var` are primarily variable scope.

`var` is function scoped, which means its available in the function it’s declared and in nested functions. This means you get some crazy behaviour like:

And I haven’t even talked (and won’t) about the confusion with _hoisting._

`let` and `const` are how variables should be declared. They are block scoped so your head doesn’t have to swivel owl-like on your neck in frustration over undesirable and mysterious variable values that persist beyond the ending brace. `const` has the added benefit of immutability so this guy should be your default unless mutability is specifically required.

One thing to be aware with `const` is that it only is immutable in its assignment. This is fine for primitive types like String or Number. Objects behave slightly differently; the object reference is immutable, but their _properties_ are still mutable.

Which should you use? Well, definitely not `var`. There are differing opinions on whether to use `let` or `const`. Ultimately it comes down to personal opinion or the project conventions. I subscribe to using `const` (contrary to my code examples) because of its immutability (object properties aside).

If you see `var` in code now, be the first to proclaim how you can improve the code quality by replacing with `let` and `const` and stop using it right now. Period.

### Object initialisation short-hand notation — saving you some sweet precious time

I am about to share with you information that will save you some seconds in precious time. Valuable time; Leaving you free to do things you love (or loath). An extra load of washing, another “_Oh by the way_” next time your chatty over the proverbial office watercooler, extra time to sit back and relax before your day’s scrum, etc.

Objects can be initialised with a form of shorthand notation that allows you to implicitly set both key-value pair on objects without having to state them explicitly, but by passing just the parameter variable.

> Note: MENSA haven’t emailed me; if they did, with that subject line, I’d be quite worried as I couldn’t be certain it would be positively good news…

You must use this notation sensibly however, and not be the unfortunate engineer who tried to use keywords or duplicates in your function. The former will cause errors while the latter (and perhaps worse) will simply override your values with the latest argument value.

### Template literals — the cool cat of concatenation

[Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) (AKA _template strings_) allow you to reference variables within strings, without all the fuss of explicit concatenation, using the _backtick._ Users of Slack and Medium will be instantly familiar with the ` symbol to denote code markup.

Take this standard example of concatenation:

Ugh, effort. You can make the code more effective using template literals:

We can even use it to replace the horrible newline escape character `\n` with no extra code sauce required.

We can also execute calculations and expression (fancily known as _Expression interpolation_) within a template literal without breaking our “string”:

And we can do some funky template literal _nesting_:

[Template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) are the proverbial bee’s knees of JavaScript concatenation. In work projects, I’ve found it configured by default on linting rules so that explicit concatenation is auto-transformed to template literals. Don’t wait until a special holiday, impress your friends right now with your newfound concatenation syntax.

### Default Params — being fully equipped

Like a lot of this new code syntax, I saw default params before I even knew they existed. Of course, reading the code I was perplexed and a little apoplectic over why a certain value that was being assigned a value wasn’t that value at runtime. It was 5 damnit — it says so right in the function param, how could it be a 10 at runtime! Damn code gremlins. Of course that momentary hissy fit was simply ignorance on my part.

Default params allow you to use, you guessed it folks, a parameter…_by DEFAULT!_ As much I am lampooning it, it is actually a simple (like a slap to the forehead to cajole the brain to wake-up simple) but effective means of controlling the unpredictability of the `undefined` entering your function contract.

For example, most software developers across the spectrum of languages have at some stage seen `if(something != null)` _(looking at you Java)_ around code blocks simply because there is always that 1% chance our enemy will pass an object or value that is not something we expect, and we must take it as an absolute certainty they will.

Imagine if your bank account had a function that one day got passed an `undefined`. I imagine that surgery would be required to re-attach the jaw after it dropped from your face if you saw your account balance as **NaN**.

So how to defend? Correct — default params.

Simple yet effective.

Now this is a contrived example and many will point out the myriad ways to stop the economic collapse of the world accounting systems from NaN in different ways. Hold off my friend — it was just to show this example.

Default params guard against the `undefined` so you are correct when you think “_what if a non-expected type of value is entered — Default params won’t guard against that_”. Indeed so true and depending on your code, you may need additional checks to ensure the type of value of correct.

### Destructuring — Value assignment wizardry

When I first saw objects being destructured (not knowing what the flip I was looking at), I was mightily confused. Curly braces I associated with object notation, but in the variable name declaration with a bunch of other names all pointing to the one object reference? Dark wizardry indeed.

The reality is that it’s quite simple but it’s use will make you look so wizard, even Harry will be jealous. The concept is this: you declare immediate variables with values that match the same-named properties on an object.

No more _someObject.someProperty;_ just simple variables to for our further programming needs.

What happens if the variable isn’t available or we simply don’t want all the variables? Well we can create variables only for the values we want, and if we declare a variable that isn’t on the object, we simply get the same value as if we normally declared a variable without defining: `undefined`

But the magic doesn’t stop there. We can _ensure_ that our variables have defaulted values in case they aren’t assigned.

And if we want, we can even rename the variables as we want them. Sorcery indeed.

And as long as it’s an object that your destructuring, it doesn’t matter whether it’s destructured directly, or given as a return object on a function.

That also includes destructuring at the _parameter_ level. Why would you do that, you ask? It removes the need to have _parameter order_ when invoking a function. I do not lie.

Just like objects, we can do all this with Arrays. The trick is to use the Array braces notation rather than object braces. Assignment is given by index order of the array, so the first variable is assigned the first index item, and so on.

The above examples of destructuring are a good summary of what you can do, but if you really want to become the Gandalf of JavaScript destructuring, then check out the [MDN destructuring assignment documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

### For..of loop — iterating iterants iteratively

The `for..of` loop in JavaScript allows more effective looping of iterables. Often people think of iterables as Arrays (and they’re right of course), but iterables can also be the characters in a String, the key-value pairs in a Map, elements of a Set, etc. (pssshhh — see more Iterable types [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)).

You may be thinking, _aren’t there other for loops in JavaScript_, and you’d be right — there are; the traditional `for`, the `for..in`, the `while` and the `do..while`, the `forEach` and `map`. So what’s special with `for..of`?

The best way I describe to myself the difference between `for..of` and `for..in` is that, while both iterate over lists, `for..in` returns keys on the object, where `for..of` returns values of the object being iterated.

The difference is more apparent in Strings.

So why bother with the other `for` loops well-armed with the artillery of `for..of`? Well, the `for..of` doesn’t allow mutation (i.e. _change_) of the array like `for` would. It also it doesn’t work well on the properties of objects like `for..in`.

I found the different ways of looping in JavaScript fine, including `for..of` but most of my uses were satisfied by using `map`, `filter`, and `reduce` which are iterant royalty and that I describe further down.

Likely, `for..of` will be the _least_ useful for you on this list but will still impress others with your knowledge at least.

### Array includes — No indexing for me

In a work project, I saw `indexOf` being used to check a value within an array. It also had the check for `-1` to be sure that there was logic to handle if it wasn’t found — `if(array.indexOf(b) < 0) {`..}. In one of my rare flashes of inspiration, I had the thought that since I had seen all this new syntax I’m describing in this article, that surely some clever-clogs had made this easier and more readable! Surely. And I was right.

`[Array.prototype.includes()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)` allows you to, more readably and more logically, check if certain arrays have certain values. It returns a simple boolean rather than some sentinel number value and overall, should be the defacto for array interrogation.

One caveat — that work project I was on needed to support IE11 as a browser. And guess what? For the browser-that-will-not-die, it’s not supported. There is a polyfill available for those that have to work under such dramatic conditions.

### Set — Diversity in the workplace

For when you don’t want your array to have duplicate values, a Set is your friend. If you know Java and know all about the _Set_ _interface_ and implementations, this isn’t really new, so here’s a pass and skip on through.

A set is an object that takes an array and is able to strip it of duplicate values.

The Set has a bunch of functions such as `add`, `delete`, `forEach`, etc. that allow you to traverse and manipulate the set in question.

### Spread — spreading the love of values

The Spread operator, while I personally think its name is confusing for its use, is actually one of the most helpful new syntax additions.

The Spread operator syntax is three fullstops (…) before the object reference.

The Spread operator essentially _expands_ an iterable object containing values and places them into a space where multiple values are expected (by value and not by reference). Still confused? That’s fine — let’s break this down further.

Let’s combine some arrays into larger arrays.

Our use of the spread passes these objects _by value_ and not by reference. It means that we can mutate the original array without worry that a composed array is changed.

So sure, seems obvious now, you can essentially compose arrays like Lego blocks of other arrays. That’s fine, but what else?

Well Spreads can be used in function argument lists.

It follows the typical rues of JavaScript function arguments whereby additional values are not used and lacking arguments are `undefined`.

So arrays, check. Function arguments, check. Spread sounds great, doesn’t it? Well it has one last lovely surprise it really wants to show you — by spreading object literals!

In this way, we can _compose_ our objects with smaller objects. Non-unique key properties are overwritten by the latest value while unique properties are added.

One caveat; the spread of object literals is more cutting edge (at time of writing) than the other syntax features here (being introduced in ES2018).

For more information on _Spread_ and the general browser support for that spreading, see the [MDN article on Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) (especially the browser compatibility table).

### Rest operator — Accepting of all the rest of you

If you understand the Spread syntax, this should seem like a natural extension of its functionality. If you happen to come from a Java background, I’ll simply say _varargs_ so that you can move quickly on.

The Rest operator is syntax that allows _a reference_ to as many arguments as are passed into a function. It allows functions to accept as many arguments as you want to throw at them (as long as the Rest operator is the only and last function argument). I think of its name as a reference to _all the rest_ of the arguments a function should use.

That’s it. Simples.

Wait, what about `arguments`? Why not use that? Well, `arguments` is a funny thing, because it doesn’t return an array, but rather an array-like object. Because of this, we can’t treat it like an array.

In most cases, you don’t want your functions accepting of as many arguments as some hooligan engineers will want to chuck at it. It can lead to unpredictability; let’s be honest, the job is hard enough without adding _more_ complexity to it. There will be use cases where of course you need to be open to everything (e.g. a _sum_ function) and when these happen, the Rest operator is what you need.

### Arrow functions — straight to the functional point

More and more code I see nowadays use Arrow functions rather than the traditional `function` syntax. Personally, my background came from Java which is typically known for it’s verbosity, so I fall into that style quite naturally. Knowing arrow functions will go a long way to bluffing JavaScript proficiency among your peers, winning you friends, and influencing people.

Arrow functions streamline the traditional function syntax to be less verbose and shorter to implement. Of course there is _minor_ differences between it and function expressions (such as no `this`, `super`, or `arguments`), but generally that’s an acceptable trade-off.

In one-liners like above, not only did we get rid of the `function` keyword, we were also able to be rid of the curly braces and the `return` keyword. This is known as the ‘_concise body_’. You can of course still use curly braces for multi-line logic which is known as ‘_block body_’.

Arrow functions are effectively suited to be used in callbacks.

> Yes, yes, I know, the code above could have been streamlined, like the scales of an elegant fish, to be a one-liner; but if I did that, I couldn’t show a multi-line Arrow function!

Arrow functions have become more prevalent in JavaScript frameworks such as React, where seeing stateless components defined using arrow functions is quite ordinary.

This is really only a snippet of what Arrow functions can do, but as a bluffer’s guide, it’s enough to see you through the day without attracting the scrutiny of the your autocratic colleagues.

So get out there and start firing arrows everywhere; Point arrows at all your friend’s functions; it will enamor everyone of your JavaScript proficiency all the more. Become as accurate as an archer, and for masterclass lessons — see the [MDN documentation on Arrow functions.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

### Computed property names — does not compute?

Computed property names are the names of properties that are derived from the values of other variables. Unfortunately, you cannot assign variables directly as a key to an object.

One tool available is to use the _square bracket_ notation. This can be used to access properties on an object, just like it’s foe, the _dot_ operator. For example, `person['name']` is the same as `person.name`.

We can also use the same syntax to _set_ properties on objects using their value as the key.

What’s even better is that since ES2015, this has gotten a helluva lot easier! No more messing with creating the object, then assigning the value afterward, and other stuff, ugh so messy. Just straight up key-value setting. What a relief.

### Map, filter, reduce — Not cartography

I came late to the game learning `map`, `filter`, and `reduce`, and worse still these aren’t _new_ or _modern_ syntax.

I used typical looping syntax (e.g. `for`) coming from a Java background. That means when I had to look through elements within the array, I often created a new empty array, interrogated the valued array, and transfer the elements I wanted.

Such wasted effort. Thankfully there are nicer ways to complete these ordeals.

I like to think of using `map` for when my needs are:

* I need to _transform_ the contents of an array
* I return a new array

So what do I mean by _transform_? Well that’s a good question, it could be to manipulate the array contents in any means. For example if I want to double the numbers in a number array, or (more practically) create a bunch of HTML elements with values from a String array.

Generally, `map` is suitable for most looping needs I’ve found and it also retains the immutability of the original array by returning a new array, which is great. It has become my default way of looping in most use cases.

`filter` is, as the name suggests, filters an array and returns a new _copy_ of that array (filtered of course). Very similar in most respects to `map`, the only difference is the callback must return a boolean value (to indicate whether the value should be retained or not). Magical!

Finally, `reduce` is the act of _reducing_ your array to a single value, (how deductive of you). Anecdotally, I haven’t seen much use of this outside numbers other than concatenation of Strings, etc. But hey, if it’s the right tool for the right job, then who am I to argue.

`reduce` is a little different from `map` and `reduce` in so far that it takes an _accumulator_ or _previous_ value (representing the total so far) and the _current value_.

That’s cool — I can take a bunch of numbers and reduce to a single value based on a rule. From there I could get averages, counts, deviations, and apply a whole agglomeration of mathematical magic trickery.

But what about objects? Well you can…sort of. Reduce can take an initial object, append properties and attach values. As said before, I haven’t personally seen many use cases other than counting the number of times an object is in an array, and then assigning the count values to a return object. So with that bombshell….

What’s great about `map`, `filter`, and `reduce`, is that they are [functions of the Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), and as they all return arrays, it means they can be chained together, one after the other. Powerful stuff indeed.

### Classes — how to stay classy

For those who’ve read my other article [OOP Digest in JavaScript](https://medium.com/@byrne.greg/oop-digest-in-javascript-c57b52929fda), or those who have experienced the joys of React (yes I said it), classes aren’t unfamiliar. However what was the surprise to me, hopping into React before understanding modern JS, was the the `class` syntax was a product of _vanilla JavaScript_ and not a library or framework.

Classes is nearly another article to write and to be fair, this already is quite a cumbersome article, so to be concise I will highlight the simplified understanding and set you packing with the map to find more informational treasure.

So before you worry about how complicated Classes are, there is a simple comfort to know: JavaScript’s object-orientated prototypal model hasn’t changed. Sky is up and ground is down for those of us who are still somewhat upright. MDN defines classes as [**_syntactical sugar_** _over JavaScript’s existing prototype-based inheritance_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) and a lovely way to say — it’s just another way to create objects (hint: ‘object-orientated’).

Traditionally, we used `function` to create objects in JavaScript, and we still can of course. But classes **safely** replace the idea of using a `function Dog() {}` to create objects by removing the confusion around functions who are, well, functions, and those used in constructor mode.

It does this by forcing the use of the `new` keyword. Previously, when a function that was actually a constructor function (i.e. needed `new`) was called the old fashioned way, the properties were actually set on the _callee_ object, which of course caused pandemonium to ensue.

There are a bunch more features of classes to consider:

* Constructors

Constructors can be used for object initialisation and come with their OWN reserved keyword.

* Object functions

Previously, if we wanted an object “type” to contain a function accessible to all of that type, we would set it on that object’s prototype. Laborious. Now we can easily just add it to the class.

* Getters/Setters

Classes can use `get` and `set` keywords as accessors/mutators to access variables on a class. As a rule, classes cannot contain instance variables declared at class level (_like Java_), but can contain standard object properties defined and retrieved using functions. Note: our `_` convention to denote something private isn’t actually private in JavaScript and is accessible.

* Inheritance

Inheritance is quite similar to anyone with a background in OOP languages like Java. It, at its most simplistic, allows you to pass down functions from a parent type to a child type. This was apparently quite tedious to do prior to ES2015.

To pack you on the way for more information — I would thoroughly recommend an article in [JavaScript ES6 Class Syntax by Cory Rylan](https://coryrylan.com/blog/javascript-es6-class-syntax) which I found most enlightening to the world of JavaScript classes. It’s quick and full of nice(r) code examples comparing old and new JavaScript syntax.

### Summary

So armed (secretly of course) with this bluffer’s guide, you should be the envy of your friends, feared by your enemies, and be well on your way to leveling-up with all your newfound JavaScript experience points.

This article was long yes, I make no apology for my bardic articulation. However, you might offer a different and more violent counter-argument; so if I was to offer a minimal set of take-aways — focus on **let/const, Arrow functions, Spread** and **Destructuring.**

Lastly, I hope you think of me when you’re rich and famous from the teaching of this article. Take comfort in knowing that I will be angrily shaking my fist.

> If you’ve read this article, simply skipped it after a paragraph or two, or more simply you don’t really give a flying fudge; please feed my public validation addiction anyway by giving me a clap, and then go checkout my other articles.

> If you didn’t like this article and would like to register your resentment, you can do so by giving a hateful clap.

> The **opinions expressed** in this publication are those of the author. They do not purport to reflect the **opinions** or views of any organisation or business that the author may be connected to.

