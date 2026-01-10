---
title: ⚡ How to never repeat the same RxJs mistakes again⚡
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T13:14:28.000Z'
originalURL: https://freecodecamp.org/news/blitz-tips-rxjs-pipe-is-not-a-subscribe-125c89437a2c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8WNtSRqKD9vfik5zLqDRzw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Tomas Trajan

  Remember: .pipe() is not .subscribe()!


  _Look! A lightning tip! (Original ? by M[ax Bender)](https://unsplash.com/photos/iF5odYWB_nQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="blank" tit...'
---

By Tomas Trajan

#### Remember: .pipe() is not .subscribe()!

![Image](https://cdn-media-1.freecodecamp.org/images/fNpm-kNhaYwgz2TVveT9Zs1BYKjC9I5G6wR0)
_Look! A lightning tip! (Original ? by M[ax Bender)](https://unsplash.com/photos/iF5odYWB_nQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> This article is directed at the beginners trying to increase their RxJs knowledge but can also be a quick refresh or a reference to show to beginners for more experienced developers!

Today we are going to keep it short and straight to the point!

Currently I am working in a rather large organization quite a few teams and projects (more than 40 SPAs) that are in the process of migration to Angular and therefore also RxJs.

This represents a great opportunity to get in touch with the confusing parts of RxJs which can be easy to forget once one masters the APIs and focuses on the implementation of the features instead.

### The “.subscribe()” function

RxJs observable represent a “recipe” of what we want to happen. It’s declarative which means that all the operations and transformations are specified in their entirety from the get go.

An example of an observable stream could look something like this…

![Image](https://cdn-media-1.freecodecamp.org/images/RilFbbGg9L-sldm9tExd5KJeYZDpaI-tkDB6)
_Example of the RxJs observable stream declaration_

This RxJs observable stream will do literally nothing by itself. To execute it we have to subscribe to it somewhere in our codebase!

![Image](https://cdn-media-1.freecodecamp.org/images/slCuDufj5NNymYAfjvD5ZjCk1ImU5j56Ydww)
_This subscription will log our greetings every odd minute_

In the example above, we provided a handler only for the values emitted by the observable. The subscribe function itself accepts up to three different argument to the handle **next** value, **error** or **complete** event.

Besides that we could also pass in an object with the properties listed above. Such an object is an implementation of the `Observer` interface. The advantage of observer is that we don’t have to provide implementation or at least a `null` placeholder for the handlers we are not interested in.

Consider the following example…

![Image](https://cdn-media-1.freecodecamp.org/images/o0QFSmaoJWlc3EB1EwioXq8y4feIBLr1JcS6)

In the code above, we are passing an object literal which contains only complete handler, the normal values will be ignored and errors will bubble up the stack.

![Image](https://cdn-media-1.freecodecamp.org/images/tdaiNzIWmElXpTcw-dBTX5XNtSEspNyyAu2S)

And in this example, we are passing the handler of the next error and complete it as direct arguments of the subscribe function. All unimplemented handlers have to be passed as a null or undefined until we get to the argument we’re interested in.

As we can see, the inline argument style of implementation of a `.subscribe()` function call is positional.

> In my experience, the inline arguments style is the one which is most common in various projects and organizations.

Unfortunately, many times we may encounter implementation like the following…

![Image](https://cdn-media-1.freecodecamp.org/images/HzGX7f-wmb1vGY1r8A2aaKkUYhf5H74LbC9N)
_Example of redundant handlers often encountered in the “wild”_

The example above contains redundant handlers for both `next` and `error` handlers which **do exactly nothing** and could have been replaced by `null`.

> Even better would be to pass the observer object with the `complete` handler implementation, omitting other handlers altogether!

### The “.pipe()” and the operators

As beginners are used to providing three arguments to subscribe, they often try to implement a similar pattern when using similar operators in the pipe chain.

RxJs operators, which are often confused with the `.subscribe()` handlers, are `catchError` and `finalize`. They both serve a similar purpose too — the only difference being that they are used in the context of the pipe instead of the subscription.

In case we would like to react to the complete event of every subscription of the RxJs observable stream, we could implement `finalize` operator as a part of the observable stream itself.

> That way we don’t have to depend on the developers to implement complete handlers in the every single .subscribe() call. Remember, the observable stream can be subscribed to more than once!

![Image](https://cdn-media-1.freecodecamp.org/images/KyNcUrKEuK-5ho4qMmrJH9rRsgUIYBFDx8kr)
_Use the finalize operator to react to the complete event of the stream independently from the subscription. (Similar to tap)_

This brings us to the final and arguably most problematic pattern we may encounter when exploring various code bases: redundant operators added when trying to follow .subscribe() pattern in the .pipe() context.

![Image](https://cdn-media-1.freecodecamp.org/images/VoSsjJj6f-9Tmlkpqn53d5LikSlKgaQVPMzg)

Also, we might encounter its even more verbose cousin…

![Image](https://cdn-media-1.freecodecamp.org/images/XZb1uYVdeTzKVx1YSpK5NY88CB6YrY0BMh85)
_Stuff might get verbose…_

Notice we have progressed from the original single line to the full nine lines of code which we have to read and understand when we want to fix a bug or add a new feature.

> Stuff might get even more complex when combined with more complex generic Typescript types, which can make the whole code block even more mysterious (and hence waste more of our time).

### Recapitulation

1. The `.subscribe()` method accepts both the observer object and inline handlers.
2. The observer object represents the most versatile and concise way to subscribe to an observable stream.
3. In case we want to go with the inline subscribe arguments (`next`, `error`, `complete`) we can provide `null` in place of a handler we don’t need.
4. We should make sure that we don’t try to repeat the `.subscribe()` pattern when dealing with `.pipe()` and operators.
5. Always strive to keep the code as simple as possible and remove unnecessary redundancies!

#### That’s it! ✨

> I hope you enjoyed this article and will now have better understanding of how to subscribe to RxJs observables with clean, concise implementation!

Please support this guide with your ??? using the clap button and help it spread to a wider audience ? Also, don’t hesitate to ping me if you have any questions using the article responses or Twitter DMs @tom[astrajan.](https://twitter.com/tomastrajan)

> [And never forget, the future is bright](https://twitter.com/tomastrajan)

![Image](https://cdn-media-1.freecodecamp.org/images/HDE38gYVRZf0lweAmygW6hc5yW3sHdp3agm9)
_[avier Coiffic)](https://twitter.com/tomastrajan" rel="noopener" target="_blank" title="">Obviously the bright future! (? by X</a><a href="https://unsplash.com/photos/WV4B_aVj0aQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> Starting an Angular project? Check out [Angular NgRx Material Starter](https://github.com/tomastrajan/angular-ngrx-material-starter)!

![Image](https://cdn-media-1.freecodecamp.org/images/mWKbDXFT-UMK-sCaFd9yMEVZstrY1roIHN7v)
_Angular NgRx Material Starter with built in best practices, theming and much more!_

If you made it this far, feel free to check out some of my other articles about Angular and frontend software development in general…

[**?‍?️ The 7 Pro Tips To Get Productive With Angular CLI & Schematics ?**](https://hackernoon.com/%EF%B8%8F-the-7-pro-tips-to-get-productive-with-angular-cli-schematics-b59783704c54)  
[**An**g_ular Schematics is a workflow tool for the modern web — official introduction articlehac_kernoon.com](https://hackernoon.com/%EF%B8%8F-the-7-pro-tips-to-get-productive-with-angular-cli-schematics-b59783704c54)  [**The Best Way To Unsubscribe RxJS Observable In The Angular Applications!**](https://blog.angularindepth.com/the-best-way-to-unsubscribe-rxjs-observable-in-the-angular-applications-d8f9aa42f6a0)  
[_There are many different ways how to handle RxJS subscriptions in Angular applications and we’re going to explore their…_blog.angularindepth.com](https://blog.angularindepth.com/the-best-way-to-unsubscribe-rxjs-observable-in-the-angular-applications-d8f9aa42f6a0)[**Total Guide To Angular 6+ Dependency Injection — providedIn vs providers:[ ] ?**](https://medium.com/@tomastrajan/total-guide-to-angular-6-dependency-injection-providedin-vs-providers-85b7a347b59f)  
[L_et’s learn when and how to use new better Angular 6+ dependency injection mechanism with new providedIn syntax to make…m_edium.com](https://medium.com/@tomastrajan/total-guide-to-angular-6-dependency-injection-providedin-vs-providers-85b7a347b59f) [**The Ultimate Answer To The Very Common Angular Question: subscribe() vs | async Pipe**](https://blog.angularindepth.com/angular-question-rxjs-subscribe-vs-async-pipe-in-component-templates-c956c8c0c794)  
[_Most of the popular Angular state management libraries like NgRx expose application state in a form of a stream of…_blog.angularindepth.com](https://blog.angularindepth.com/angular-question-rxjs-subscribe-vs-async-pipe-in-component-templates-c956c8c0c794)

