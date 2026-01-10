---
title: 'How to avoid null check pollution in JavaScript: use Optionals'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-08T11:28:38.000Z'
originalURL: https://freecodecamp.org/news/avoiding-null-check-pollution-in-javascript-4ed8e2702ce3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uJIvAC_iHveiJ5BEse6YMA.jpeg
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Konstantin Blokhin

  I’ve been using JavaScript for the past few years and have been enjoying it in general.
  But it lacks some cool features from other languages. For instance, there is no
  built-in safe navigation and no means to avoid null checks. ...'
---

By Konstantin Blokhin

I’ve been using JavaScript for the past few years and have been enjoying it in general. But it lacks some cool features from other languages. For instance, there is no built-in safe navigation and no means to avoid null checks. The code gets polluted with boilerplate conditional branches. It’s error-prone and less readable.

What’s wrong with null checks, you might ask?

First of all, the inventor of the null reference, [Tony Hoare](http://en.wikipedia.org/wiki/Tony_Hoare), [called](https://www.infoq.com/presentations/Null-References-The-Billion-Dollar-Mistake-Tony-Hoare) it a **billion-dollar mistake:**

> But I couldn’t resist the temptation to put in a null reference, simply because it was so easy to implement. This has led to innumerable errors, vulnerabilities, and system crashes, which have probably caused a billion dollars of pain and damage in the last forty years**.**

JavaScript is no different. How many times have you encountered `TypeError: Cannot read property 'bar' of null` error? To avoid these, developers always have to **keep this null possibility in mind.** And they would rather concentrate on the real thing like application-specific logic.

Next, you actually have to introduce new conditional branches into your code. And generally you don’t wanna have lots of them, since `**if**` **statements tend to decrease overall readability of the code.** Take the [arrow anti-pattern](http://wiki.c2.com/?ArrowAntiPattern) as an extreme example. Moreover, these statements are almost meaningless in terms of your domain or business logic.

I like one of the ways of solving that problem, explained [here](http://michaelfeathers.silvrback.com/converting-queries-to-commands) by Michael Feathers — the “commands instead of queries” approach. And he also develops this idea and [talks](https://www.youtube.com/watch?v=AnZ0uTOerUI) about the benefits of unconditional code in general.

Basically, instead of querying a piece of data and checking if it’s there for further processing, we just express our intention and let module internals decide whether or not the action should be taken.

Let’s say we want to fetch a user and their friends’ favourite books for recommendation. The code could be like:

So, I’d rather have some module to encapsulate the checking logic. Therefore, we just tell it what to do with an active user:

The code is more focused on the business logic now. And we can reuse it to perform other actions with an active user without the burden of null checks.

But the given solution is a bit too specific. Besides, we still have a null check in our controller or some other place where we use the function.

A more general approach is required. What we need is a special data type, a container for nullable values — such as the [Optional](https://docs.oracle.com/javase/9/docs/api/java/util/Optional.html) class in Java, for example. Point is, any actions, given to the container, will be executed only on a non-empty containing value.

There are some JS libraries (like [Optional.js](https://github.com/JasonStorey/Optional.js)), implementing almost the same interface as Java Optional. But they don’t take into account the asynchronous nature of JS and don’t work with Promises.

And most of the time when the absence of a value is possible, we actually have to deal with promises and async functions. For instance, take external resource requests like database queries and API calls.

That’s when [AsyncOptional](https://github.com/treble-snake/async-optional) comes to the rescue. So, **it’s a container for an optional value of asynchronous nature**. _Optional_ means that the value may be present or absent. Both `null` and `undefined` are considered absent.

As soon as we want to tell the program what to do with a non-empty value, the factory method is called “with”:

```
const withUser = AsyncOptional.with(user);
```

Then we could do some processing, as it’s shown in the example below. Once we’re done and want to fix the result somewhere, one of terminal methods should be used.

For instance, when we don’t need to react on an empty value:

We can also specify what to do in case of the absence of the value in this natural-language-like way:

Between factory and terminal method calls, there can be any processing logic, described in the [readme](https://github.com/treble-snake/async-optional#transform-it). It’s guaranteed that no action will be taken upon an empty value.

Some of the actions you can use to process the value:

So let’s take a final look at our example:

So, how is it better compared with the initial one?

I believe the answer is — it’s way **more clean and readable,** and readability is the essence of good code.

First, we got rid of null-checking conditional branches, so we can focus on the important thing — which is the business logic of the system.

Next, we eliminated the possibility of having null pointer exceptions here. This means we don’t have to keep the nullability of the value in mind, which is one less way to introduce bugs.

Another case the library can come in handy is in a “default value” situation. Let’s say we have some kind of form for a user to fill, and among other fields there is fruit selection. The user can choose an orange, apple or nothing.

So the output is:

```
conditionalChooseFruit(‘Joe’);// => You chose nothing, Joe.
```

```
conditionalChooseFruit(‘Joe’, {notFruit: ‘x’});// => You chose nothing, Joe.
```

```
conditionalChooseFruit(‘Joe’, {fruit: 1});// => You chose apple, Joe.
```

```
conditionalChooseFruit(‘Joe’, {fruit: 11});// => You chose a wrong gardener to mess with, Joe.
```

For me, this method looks a bit messy even with the help of async/await and reversed conditions. The business logic gets blurred by conditional branches.

And with AsyncOptional it can be rewritten in a more straightforward way:

Isn’t that more readable?

So, the [AsyncOptional](https://github.com/treble-snake/async-optional) library could help you to:

* write code you may find more readable, maintainable, clean and nice-looking;
* avoid null-related `TypeErrors` better, thus increasing the stability of your system;
* work with Promises and asynchronous functions in the same clean manner (and it works with synchronous ones too).

_If you’ve liked the examples, please feel free to explore the [Readme](https://github.com/treble-snake/async-optional#about) file in the [GitHub](https://github.com/treble-snake/async-optional) repo or even check out the complete [API Docs](https://github.com/treble-snake/async-optional/blob/master/docs/APIDOC.md). I even dare to suggest you could install the [package via npm](https://www.npmjs.com/package/async-optional). :) I would also appreciate any feedback._

[**async-optional**](https://www.npmjs.com/package/async-optional)  
[_Optional implementation with async support_www.npmjs.com](https://www.npmjs.com/package/async-optional)

