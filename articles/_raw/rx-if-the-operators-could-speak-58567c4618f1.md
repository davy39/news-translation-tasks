---
title: Rx — If the Operators could speak!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-13T20:51:00.000Z'
originalURL: https://freecodecamp.org/news/rx-if-the-operators-could-speak-58567c4618f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U9DEpj0xpch6t3VdCxAZVA.png
tags:
- name: Java
  slug: java
- name: mobile
  slug: mobile
- name: General Programming
  slug: programming
- name: Reactive Programming
  slug: reactive-programming
- name: rx
  slug: rx
seo_title: null
seo_desc: 'By Ahmed Rizwan

  If the operators could talk, how exactly would they tell us what they do?

  In order to take full advantage of Rx, you need a clear understanding of what Rx
  Operators are and what they do.

  This is what the Operators would be telling the...'
---

By Ahmed Rizwan

If the operators could talk, how exactly would they tell us what they do?

In order to take full advantage of Rx, you need a clear understanding of what Rx Operators are and what they do.

This is what the Operators would be telling the observables if they could talk when we use them.

For this article, I’ll assume that you already know what Rx is. If not, go [read this](https://medium.com/@ahmedrizwan/rxandroid-and-kotlin-part-1-f0382dc26ed8#.vundiz1fq). Or just simply google Rx and you’ll find a ton of helpful articles, tutorials, and videos.

### **Creational Operators**

#### [Create](http://reactivex.io/documentation/operators/create.html)

> I tell you what to emit, when to terminate, and what error to throw. ‘Cause I’m the boss.

#### [Defer](http://reactivex.io/documentation/operators/defer.html)

> You only get to “create” yourself once someone subscribes to you. And it’ll be a brand new version of yourself every single time.

#### [Empty](http://reactivex.io/documentation/operators/empty-never-throw.html)

> Hm. Emit nothing. And then die, please.

#### [Never](http://reactivex.io/documentation/operators/empty-never-throw.html)

> Emit nothing. And don’t… ever… terminate.

#### [Throw](http://reactivex.io/documentation/operators/empty-never-throw.html)

> Emit nothing, and then throw an error, OK?

#### [From](http://reactivex.io/documentation/operators/from.html)

> I’ll give you some objects, then you emit them right back at me.

#### [Interval](http://reactivex.io/documentation/operators/interval.html)

> How about this: you emit items. But not immediately. Send them back, one by one, after certain “intervals.”

#### [Just](http://reactivex.io/documentation/operators/just.html)

> I need just one thing back from you. Just one.

#### [Range](http://reactivex.io/documentation/operators/range.html)

> I give you a range of integers, then you emit back all the values in that range.

#### [Repeat](http://reactivex.io/documentation/operators/repeat.html)

> How about you emit that same object repeatedly.

#### [Start](http://reactivex.io/documentation/operators/start.html)

> Ok. I have a function. When it returns, you start emitting. But only when it returns. Got it?

#### [Timer](http://reactivex.io/documentation/operators/timer.html)

> So you got an item. Don’t emit it just yet. I’ll tell you the exact time when you should emit it. Don’t jump the gun.

### Transformational Operators

#### [Buffer](http://reactivex.io/documentation/operators/buffer.html)

> Ok, so here’s the deal. Whatever it is you normally emit, well don’t emit that. Instead ,collect the items into bundles over time. And send bundles instead. ‘Cause I want bundles!

#### [FlatMap](http://reactivex.io/documentation/operators/flatmap.html)

> So, like, if you have lists of items and there’s another observable that’s full of items, can you please “flatten” yourself and that observable so you can just send items?

#### [Map](http://reactivex.io/documentation/operators/map.html)

> Transform each item into another item.

#### [Scan](http://reactivex.io/documentation/operators/scan.html)

> Transform each item into another item, like you did with map. But also include the “previous” item when you get around to doing a transform.

### Filtering Operators

#### [Debounce](http://reactivex.io/documentation/operators/debounce.html)

> Only emit if a certain amount of time is passed.

#### [Distinct](http://reactivex.io/documentation/operators/distinct.html)

> Emit only distinct items. All right?

#### [ElementAt](http://reactivex.io/documentation/operators/elementat.html)

> I tell you the index. You emit the item at that index.

#### [Filter](http://reactivex.io/documentation/operators/filter.html)

> I give you a criteria. You give me items that pass the criteria.

#### [First](http://reactivex.io/documentation/operators/first.html)

> Just give me back the first item.

#### [IgnoreElements](http://reactivex.io/documentation/operators/ignoreelements.html)

> Do not, I repeat, do not emit a single item. And then die.

#### [Last](http://reactivex.io/documentation/operators/last.html)

> Just give me back the last item.

#### [Sample](http://reactivex.io/documentation/operators/sample.html)

> I give you an interval. You give me only the most recent items from that that interval.

#### [Skip](http://reactivex.io/documentation/operators/skip.html)

> OK, skip the first n items, would you?

#### [SkipLast](http://reactivex.io/documentation/operators/skiplast.html)

> Skip the last n item s. Yeah, those ones.

#### [Take](http://reactivex.io/documentation/operators/take.html)

> Emit only the first n items.

#### [TakeLast](http://reactivex.io/documentation/operators/takelast.html)

> Emit only the last n items.

### Combining Operators

#### [Merge](http://reactivex.io/documentation/operators/merge.html)

> Here are two observables. Let’s pretend they’re only one observable.

#### [StartWith](http://reactivex.io/documentation/operators/startwith.html)

> Here are two observables. But I get to tell you which one to start with.

#### [CombineLatest](http://reactivex.io/documentation/operators/combinelatest.html)

> Here are two observables. Between the two, make pairs of the latest items.

#### [Zip](http://reactivex.io/documentation/operators/zip.html)

> Here are two observables. But I tell you how to combine their items (through a function, of course).

### Handling Errors

#### [Catch](http://reactivex.io/documentation/operators/catch.html)

> After an error is thrown, continue on with the emits.

#### [Retry](http://reactivex.io/documentation/operators/retry.html)

> After an error is thrown, restart from the very beginning.

### Utility

#### [Delay](http://reactivex.io/documentation/operators/delay.html)

> Just add a delay before you start emitting, OK?

#### [ObserveOn](http://reactivex.io/documentation/operators/observeon.html)

> “Observational” code should run on this particular thread.

#### [SubscribeOn](http://reactivex.io/documentation/operators/subscribeon.html)

> “Subscription” code should run on this particular thread.

#### [Subscribe](http://reactivex.io/documentation/operators/subscribe.html)

> You can start emitting now. *music intensifies*

#### [TimeInterval](http://reactivex.io/documentation/operators/timeinterval.html)

> OK, so observables send back items, right? Instead, I want you to send the time intervals back. Like the time differences between each emission.

#### [TimeOut](http://reactivex.io/documentation/operators/timeout.html)

> Set a TimeOut on each emission. And if an item doesn’t get emitted within that time, just throw an error _?_

### Conditional and Boolean

#### [All](http://reactivex.io/documentation/operators/all.html)

> If all items fulfill a certain criteria, return true.

#### [Amb](http://reactivex.io/documentation/operators/amb.html)

> Here are at least two observables. Give me the one that starts emitting first.

#### [Contains](http://reactivex.io/documentation/operators/contains.html)

> If I ask for an item, can you tell me whether you already have it?

#### [DefaultIfEmpty](http://reactivex.io/documentation/operators/defaultorempty.html)

> When you have nothing to emit, here’s a default value that you can send back.

#### [SequenceEqual](http://reactivex.io/documentation/operators/sequenceequal.html)

> Here are two observables. Return true if their items (and their sequence) are the same.

#### [SkipUntil](http://reactivex.io/documentation/operators/skipuntil.html)

> Here are two observables. Skip the items of the first one until the second one starts emitting.

#### [SkipWhile](http://reactivex.io/documentation/operators/skipwhile.html)

> I give you a condition. You emit items until that condition becomes false.

#### [TakeUntil](http://reactivex.io/documentation/operators/takeuntil.html)

> Here are two observables. Only give me the items of the first one until the second one starts emitting.

### Mathematical Operators

#### [Average](http://reactivex.io/documentation/operators/average.html)

> Give me an average of your Integer items.

#### [Count](http://reactivex.io/documentation/operators/count.html)

> Give me a count of your items.

#### [Max](http://reactivex.io/documentation/operators/max.html)

> Emit only the maximum-valued item.

#### [Min](http://reactivex.io/documentation/operators/min.html)

> Emit only the minimum-valued item.

#### [Reduce](http://reactivex.io/documentation/operators/reduce.html)

> Do a scan, but only emit the final value.

#### [Sum](http://reactivex.io/documentation/operators/sum.html)

> Return the sum of all your items.

### Conversion Operators

#### [To](http://reactivex.io/documentation/operators/to.html)

> Convert an observable into a List, Map or Array, or whatever I tell you to.

That’s it for now. There are other operators as well, which you can find [here](http://reactivex.io/documentation/operators.html). You can also check out [RxMarbles](http://rxmarbles.com), which has cool diagrams for demonstrating each operator.

Anyway, thank you for reading. I hope the article helped you better understand what each of these commands does in a fun way.

Happy coding!

