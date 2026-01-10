---
title: Angular RxJS In-Depth
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-22T21:34:20.000Z'
originalURL: https://freecodecamp.org/news/angular-rxjs-in-depth
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/s_98CC91BB1D7ABCD50AC04362B7F541F3549A631A6219D02FE7AED5645CF1CAA7_1549549534749_use-reactive-programming-you-must.jpg
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Ahmed Bouchefra

  In this tutorial, we''ll learn to use the RxJS 6 library with Angular 6 or Angular
  7. We''ll learn about:


  How to import the Observable class and the other operators.

  How to subscribe and unsubscribe from Observables.

  How to import a...'
---

By Ahmed Bouchefra

In this tutorial, we'll learn to use the RxJS 6 library with Angular 6 or Angular 7. We'll learn about:

* How to import the Observable class and the other operators.
* How to subscribe and unsubscribe from Observables.
* How to import and call operators and chain them with the `pipe()` function.
* We'll also see how to use the async pipe to subscribe to Observables from Angular templates.
* Finally we'll see how to use some popular pipeable operators such as `tap()`, `map()` and `filter()` and their new import paths in RxJS 6.

**Note**: This tutorial works with both Angular 6 and Angular 7.

Throughout this tutorial, we’ll start looking at what reactive programming, asynchronous operations and data streams are and how they are related to the RxJS library. We’ll then see the concept of an RxJS `Observable` with examples, the various types of Observables such as:

* `Subject`,
* `BehaviorSubject` and `ReplaySubject`,
* unicast and multicast Observables,
* cold and hot Observables  etc.

Next, we’ll see what RxJS operators are and examples of some popular operators such as `tap()`, `map()`, `filter()`, `share()`, etc. And finally we’ll see how Angular uses the RxJS Observable to do asynchronous programming.

## What is Reactive Programming

![What is Reactive Programming](https://d2mxuefqeaa7sj.cloudfront.net/s_98CC91BB1D7ABCD50AC04362B7F541F3549A631A6219D02FE7AED5645CF1CAA7_1549549534749_use-reactive-programming-you-must.jpg)

Let’s see the definition of Reactive programming from different sources.

This is how  Andre Staltz, the creator of [cycle.js](https://cycle.js.org/) (A functional and reactive JavaScript framework for predictable code) defines it:

Reactive Programming is programming with asynchronous data streams

This means when you are writing code that deals with asynchronous operations and streams of data, you are doing reactive programming.

Now, this is the definition from [Wikipedia](https://en.wikipedia.org/wiki/Reactive_programming) which is more in-depth:

In computing, reactive programming is a declarative programming paradigm concerned with data streams and the propagation of change.

This means reactive programming is a declarative (vs. a procedural) style of programming  that works on streams of data.

For a detailed guide on reactive programming and data streams, check out: [The introduction to Reactive Programming you've been missing](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754).

**What is Stream**

A stream is an essential concept in reactive programming so it's worth seeing the definition before we proceed further.

![What is a stream](https://d2mxuefqeaa7sj.cloudfront.net/s_98CC91BB1D7ABCD50AC04362B7F541F3549A631A6219D02FE7AED5645CF1CAA7_1549549589200_687474703a2f2f692e696d6775722e636f6d2f4149696d5138432e6a7067.jpeg)

In all definitions we’ve seen the word **stream.**

So what is a stream?

Simply put:

A stream refers to values of data overtime.

We'll see later that Observables and streams are very related concepts.

## What is RxJS

Now, that we’ve seen the conceps of reactive programming and data streams, let’s see what RxJS is.

![What is RxJS](https://d2mxuefqeaa7sj.cloudfront.net/s_98CC91BB1D7ABCD50AC04362B7F541F3549A631A6219D02FE7AED5645CF1CAA7_1549549625485_what-if-reactive-programming-is-just-a-myth-and-facebook-and-netflix-dont-exist.jpg)

[RxJS](https://github.com/ReactiveX/rxjs) is a popular library among web developers. It provides functional and reactive programming patterns for working with events and streams of data and has been integrated in many web development libraries and frameworks such as Angular.

RxJS makes it easy for JavaScript developers to write asynchronous code using composable Observables instead of callbacks and Promises.

RxJS stands for Reactive Extensions for JavaScript and it actually has implementations in other programming languages such as Java, Python, Ruby, and PHP etc. It's also available for platforms such as Android. Check out the [complete list of supported languages and platforms](http://reactivex.io/languages.html).

RxJS v6 is currently the stable version of RxJS and it has many breaking changes with RxJS v5. You can check out more information about the changes and how to migrate from the old version from this official [migration guide](https://github.com/ReactiveX/rxjs/blob/master/docs_app/content/guide/v6/migration.md).

RxJS 6 has many advantages over the previous RxJS 5 version(s), such as:

* The bundle size of the library is smaller,
* The performance of the latest version is better,
* RxJS 6 Observable follows the [Observable Spec Proposal](https://github.com/zenparsing/es-observable),
* The latest version provides better debugability,
* A better modular architecture,
* It's backward compatible.

## How to Install and Use RxJS

RxJS is a JavaScript library which means you can install it in the same way you install other libraries:

**Using RxJS with ES6 via npm**

In your project, you can run the following command to install RxJS:

```
$ npm install rxjs

```

You can then import the symbols you want to use from the `rxjs` package or a sub-package such as `rxjs/operators`:

```
import { Observable, Subscriber } from 'rxjs';
import { tap, map, filter } from 'rxjs/operators';

```

We imported the `Observable` and `Subscriber` symbols from `rxjs` and the `tap`, `map` and `filter` operators from `rxjs/operators`.

We'll see later what these symbols are and how to use them in your Angular application.

**Using RxJS from a CDN**

You can also use RxJS from a [CDN](https://unpkg.com/rxjs/bundles/rxjs.umd.min.js) using a `<script>` in your HTML document:

```
<script src="https://unpkg.com/rxjs/bundles/rxjs.umd.min.js"></script>

```

**Note**: Please note that in Angular 6 & 7, RxJS 6 is already included in your project so you don't need to install it manually.

## What is an Observable, Observer and Subsription in RxJS 6

RxJS uses the concept of Observables to handle and work with asynchronous and event-based code.

The asynchronous word comes from Asynchrony. In computer programming, here is the definition of Asynchrony from [Wikipedia](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)):

Asynchrony, in computer programming, refers to the occurrence of events independent of the main program flow and ways to deal with such events. These may be "outside" events such as the arrival of signals, or actions instigated by a program that take place concurrently with program execution, without the program blocking to wait for results.

After reading this definition, you may have concluded how much asynchrony is important for computers and programming!

Let's make this simple!

**Asynchronous** code is the inverse of **synchronous** code which is the original way of thinking about your code when you are first introduced to programming.

Your code is synchronous when it's running in sequences i.e instruction by instruction in the order they appear in the source code.

For example, let's consider this simple JavaScript code:

```
const foo = "foo" //1
const bar = "bar" //2
const foobar = foo  +  bar //3
console.log(foobar) //4

```

The browser will run this synchronous code line by line from line 1 to 4 starting by assigning the `foo` and `bar` variables, concatenating them and displaying the `foobar` variable in the console.

JavaScript supports also the **asynchronous** approach of writing code which makes sense, since you need to respond to the user events in the browser but you don't actually know when the user interacts with your application (and in which order) when you are writing code.

This was originally achieved using callbacks which you need to define in your code and specify when they will be called.

For example, the following asynchronous code will display **You clicked the button!** when the user clicks the button identified by the `mybutton` identifier:

```
document.getElementById('mybutton').addEventListener('click', () => {
  console.log("You clicked the button!")
})

```

The second argument of the `addEventListener()` method is the callback.

You can also use callbacks to handle asynchronous operations which don't involve the DOM. For example, the following code can be used to send an HTTP POST request to a web server:

```
const xhr = new XMLHttpRequest()
xhr.onreadystatechange = () => {
  if (xhr.readyState === 4) {
    xhr.status === 200 ? console.log(xhr.responseText) : console.error('error')
  }
}
xhr.open('POST', 'your.server.com')
xhr.send()

```

This is how you perform the famous Ajax calls in JavaScript.

Actually, [Ajax](https://en.wikipedia.org/wiki/Ajax_(programming)) itself stands for **A**synchronous **J**avaScript **a**nd **X**ML.

**Note**: Sending HTTP requests (which is a common operation in web apps) is an asynchronous operation by nature since the request will take time to reach the server which will then send a response back to your client application. In this mean time, the application needs to respond to other actions and perform other tasks and only process the server response when it's received.

If you have ever extensively worked with callbacks, you'll notice one problem with them. They are difficult to track!

When you write complex applications you usually end up writing nested callbacks (callbacks inside callbacks) with multiple nesting levels. This is what's known as the [callback hell](https://stackoverflow.com/questions/25098066/what-is-callback-hell-and-how-and-why-rx-solves-it).

Modern JavaScript introduced other approaches or abstractions to deal with asynchronous operations (without using too much callbacks) such as Promises and Async/Await.

Promises have been introduced in [ES6](https://www.ecma-international.org/ecma-262/6.0/) (JS 2015).

Async/await has been introduced in ES8 (JS 2017) and it's actually a syntactic sugar on top of Promises which helps developers write asynchronous code with Promises in a way that looks synchronous.

But Promises are actually similar to callbacks and have the same nesting problem at some degree.

Since developers are always looking for better solutions we now have Observables which use the [observer](https://en.wikipedia.org/wiki/Observer_pattern) software pattern.

The observer pattern is a software design pattern in which an object, called the subject, maintains a list of its dependents, called observers, and notifies them automatically of any state changes, usually by calling one of their methods. [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern).

Observables are implemented in the [ReactiveX](http://reactivex.io/) project which has implementations in various languages. RxJS is the JavaScript implementation.

**Note**: Observables are implemented in many other libraries such as [zen-observable](https://github.com/zenparsing/zen-observable) and [xstream](https://github.com/staltz/xstream) but RxJS Observables are the most popular in JavaScript.

Observables are not yet a builtin feature of JavaScript but there is a [proposal](https://tc39.github.io/proposal-observable/) to add them in EcmaScript.

Now, what's an RxJS Observable?

An Observable is an entity that emits (or publishes) multiple data values (stream of data) over time and asynchronously.

This is the definition of an Observable from the [RxJS docs](https://rxjs.dev/guide/overview)

Observable represents the idea of an invokable collection of future values or events.

**Observers and Subscriptions**

There are also related concepts that you'll work with when using Observables which are **Observers** and **Subscriptions**.

Observers are also called listeners (or consumers) as they can listen or subscribe to get the observed data.

From the RxJS docs:

Observer is a collection of callbacks that knows how to listen to values delivered by the Observable.

[Subscriptions](http://reactivex.io/rxjs/class/es6/Subscription.js~Subscription.html) are objects that are returned when you subscribe to an Observable. They contain many methods such as the `unsubscribe()` method that you can call to unsubscribe from receving published values from the Observable.

From the official docs:

Subscription represents the execution of an Observable, is primarily useful for cancelling the execution.

## What is a Subject in RxJS

A [Subject](https://rxjs-dev.firebaseapp.com/guide/subject) is a special type of Observable that observers can also subscribe to it to receive published values but with one difference:  **The values are multicasted to many Observers**.

**Note**: By default an RxJS Observable is unicast.

Unicast simply means that each subscribed observer has an independent execution of the Observable while multicast means that the Observable execution is shared by multiple Observers.

**Note**: Subjects are similar to Angular EventEmitters.

So when using Subjects instead of plain Observables, all subscribed Observers will get the same values of emitted data.

**Note**: Subjects are also Observers i.e they can also subscribe to other Observables and listen to published data.

**Hot and Cold Observables**

Unlike regular Observables, Subjects are called **hot**.  A hot Observable starts emitting events even before any observer subscribes to it which means observers may lose previous emitted values if they don’t subscribe at that right time while **cold** Observables ****start emitting values when at least one observer is subscribed.

**Note**: You can use the `asObservable()` method to convert a subject to only an Observable.

## RxJS’ `BehaviorSubject` and `ReplaySubject`

RxJS provides two other types of Subjects: `BehaviorSubject` and `ReplaySubject`.

With a normal Subject, Observers that are subscribed at a point later will not receive data values emitted before their subscriptions. In many situations, this is not the desired behavior we want to implement. This can be solved using  `BehaviorSubject` and `ReplaySubject`.

`ReplaySubject` works by using a buffer that keeps the emitted values and re-emit them when new Observers are subscribed.

`BehaviorSubject` works like `ReplaySubject` but only re-emits the last emitted value.

## How to Create an RxJS Observable

You can create an RxJS Observable using the `Observable.create()` method which takes a function with an `observer` argument. You can then subscribe to the returned Observable instance.

There many other methods to create Observables besides the static `create()` method:

* The `lift()` instance method which creates a new Observable from the instance (the source) it's called on,
* The `of([])` operator which creates an Observable of a single value. We'll see an example next,
* The `interval(interval)` operator which creates an Observable that emits an infinite sequence of numbers. Each number is emitted at a constant interval of time in seconds,
* The [timer()](http://reactivex.io/documentation/operators/timer.html) operator which returns an Observable that after a specified amount of time, emits numbers in sequence every specified duration,
* The `from()` method that creates an Observable from a Promise or an array of values,
* The `fromEvent()` method that creates an Observable from a DOM event,
* The `ajax()` method which creates an Observable that sends an Ajax request.

We'll see these creation methods by example later.

### How to Subscribe to an RxJS Observable

After creating an `Observable`, you can subscribe to it using the `subscribe()` method on the instance which returns an instance of `Subscription`.

### A Simple Example of the RxJS Observable

Let's now see a simple example of creating and working with an Observable.

First let's create an Observable:

```
let ob$ = Observable.create((observer) => {
    observer.next("A new value!");
});

```

We create an `ob$` Observable and we define the logic that our Observable is supposed to do in the body of the passed in method.

In this example, the Observable will simply emit the **A new value!** value to the subscribed Observer.

**Note**: The dollar sign is just a convention for naming variables that hold instance of Observables.

We call the `next()` method of the observer object to inform it of the available values.

**Note**: All observer objects must have a collection of methods such as `next()`, `complete()` and `error()`. This allows Observables to communicate with them.

The `next()` method is used by the Observable to pass values (publish values) to the subscribed Observer.

Next, let's create an observer object:

```
let observer = {
    next: data => console.log( 'Data received: ', data),
    complete: data => console.log('Completed'),
};

```

An observer is a plain JavaScript object that contains methods such as `next()`, `complete()` and `error()`. This means it knows how to get notified by the Observable.

**Note**: You can also add other custom attributes and methods to the Observer objects besides `next()`, `complete()` and `error()`.

Finally, let's subscribe to our `ob$` Observable and return a `Subscription`:

```
let subscription = ob$.subscribe(observer);

```

Once you susbscribe to the `ob$` Observable, you'll get the following output in the console:

```
Data received: A new value! 

```

## RxJS Operators

RxJS provides the implemenation of Observable concept but also a variety of operators that allows you to compose Observables.

Operators offer a declarative way to perform complex asynchronous operations with Observables.

An operator works on a source Observable by observing its emitted values and applying the intended transformation on them then return a new Observable with the modified values.

There many RxJS operators such as:

* `tap()`,
* `map()`,
* `filter()`,
* `concat()`,
* `share()`,
* `retry()`,
* `catchError()`,
* `switchMap()`,
* and `flatMap()` etc.

## Pipes: Combining Multiple Operators

RxJS provides two versions of the `pipe()` function: A standalone function and a method on the `Observable` interface.

You can use the `pipe()` function/method to combine multiple Operators. For example:

```
import { filter, map } from 'rxjs/operators';
const squareOf2 = of(1, 2, 3, 4, 5,6)
  .pipe(
    filter(num => num % 2 === 0),
    map(num => num * num)
  );
squareOf2.subscribe( (num) => console.log(num));

```

The `of()` method will create and return an Observable from the `1, 2, 3, 4, 5,6` numbers and the `pipe()` method will apply the `filter()` and `map()` operators on each emitted value.

## How Observables are Used in Angular

Angular uses the RxJS Observable as a built-in type for many of its APIs such as:

* The `HttpClient` methods return Observables and actual requests are only sent when you subscribe to the returned Observable.
* The Router uses Observables in multiple places such as:
* the `[events](https://angular.io/api/router/Router#events)` of the Router instance is an Observable to listen to events on the router.
* Also `ActivatedRoute` (which contains information about the route associated with the currently loaded component on the router outlet) has many Observable properties such as `params` and `paramMap` for the route parameters.

Let's assume, you have an Angular component and the Router service injected as `router`. This example from [StackOverflow](https://stackoverflow.com/questions/33520043/how-to-detect-a-route-change-in-angular) shows you how you can subscribe to the router events for detecting a route change:

```
import { Component } from '@angular/core'; 
import { Router, Event, NavigationStart, NavigationEnd, NavigationError } from '@angular/router';
@Component({
    selector: 'app-root',
    template: `<router-outlet></router-outlet>`
})
export class AppComponent {
    constructor(private router: Router) {
        this.router.events.subscribe((event: Event) => {
            if (event instanceof NavigationStart) {
                console.log("Navigation start");
            }
            if (event instanceof NavigationEnd) {
                console.log("Navigation end");
            }
            if (event instanceof NavigationError) {

                console.log(event.error);
            }
        });
   }
}     

```

* The Reactive Forms Module uses reactive programming and Observables for listening to user input.
* The `@output()` decorator in a component takes an `EventEmitter` instance. `EventEmitter` is a subclass of the RxJS Observable.

## How to Use RxJS 6 Observable in Your Angular Code

Angular uses Observables (implemented with the RxJS library) for all asynchronous events. If you are using Angular CLI 6|7, RxJS 6 will be installed by default on your project.

Otherwise you can install it via npm using:

```
$ npm install rxjs --save 

```

To be able to use the Observable symbol in your code, you first need to import it:

```
import { Observable } from 'rxjs';

```

This is the new import path in RxJS 6 which is different from RxJS 5.

## Working with the HttpClient Module and Observables

The new Angular `HttpClient` works with Observables by default. Methods such as `get()`, `post()`, `put()` and `delete()` return an instance of the Observable interface.

HTTP requests are only sent when we subscribe to the Observable.

This is an example of making an HTTP request:

```
getItems(): Observable<Item[]> {
   return this.httpClient.get<Item[]>(this.itemUrl);
}

```

We assume that you have injected the `HttpClient` service as _httpClient_.

## Using `Observable` with `AsyncPipe`

Angular `AsyncPipe` subscribes to Observable and returns the emitted data. For example. Let's suppose we have this method:

```
getItems(): Observable {
  this.items$ = this.httpClient.get(this.itemUrl);
}

```

The `items$` variable is of type Observable<Item[]>`.

After calling the `getItems()` method on the component we can use the `async` pipe in the component template to subscribe to the returned Observable:

## Subscribing to Observables

Observables are used for better support of event handling, asynchronous programming, and handling multiple values. When you define an Observable to publish some values for a consumer, the values are not emitted until you actually subscribe to the Observable.

The Consumer that subscribes to the Observable keeps receiving values until the Observable is completed or the consumer unsubscribes from the observable.

Let's start by defining an observable that provides a stream of updates

## Using the `map()` Operator

The `map()` operator is similar to the `Array.map()` method. It lets you map observable responses to other values. For example:

```
import { Observable} from 'rxjs';
import { map } from 'rxjs/operators';
getItems(): Observable> {
  return this.aService.getItems().pipe(map(response => response.data));
}

```

The `getItems()` method returns an Observable. We're using the `map()` operator to return the `data` property of the response object.

The operator enables us to map the response of the Observable stream to the `data` value.

We import the pipeable operator `map()` from the `rxjs/operators` package and we use the `pipe()` method (which takes a variable number of pipeable operators) to wrap the operator.

## Using the `filter()` Operator

The `filter()` operator is similar to the `Array.filter()` method. It lets you filter the observable stream and returns another observable. For example:

```
import { Observable} from 'rxjs';
import { filter } from 'rxjs/operators';

filter(): Observable<Array<any>> {
  
  return this.aService.getItems()
    .pipe(
      filter(response => response.code === 200));
}

```

We use the  `filter()` operator to only emit a notification to observers of the observable stream when the status code of the HTTP response is 200.

## Conclusion



In this tutorial, you have been introduced to reactive programming, data streams and RxJS 6.

You have learned that reactive programming is about coding with asynchronous data streams and that RxJS is the most popular implementation that implements Observables and the observer pattern.

You have learned what an Observable is — An object that emits or publishes values over time and asynchronously.

You have learned about the related concepts to Observables such as Observers and Subscriptions — Observers are objects that listen and consume values published by an Observable and Subscriptions are the objects returned from the `subscribe()` method (They are usually used to unsubscribe the Observer from the Observable).

You have also learned about special types of Observables such as Subjects, behavior Subjects (`BehaviorSubject`) and replay Subjects (`ReplaySubject`) and also the difference between unicast and multicast Observables. As a reminder a multicast Observable shares its execution between all its Observers.

You learned about cold and hot Observables — hot refers to when the Obseravble starts publishing values when it’s created even before getting any subscriptions.

You learned about RxJS operators which are methods that are used to compose Observables and work on their data streams.

Finally, you learned that Angular 6 & 7 uses RxJS v6 for working with asynchronous operations and APIs (instead of callbacks or Promises) in many of its commonly used modules such as `HttpClient`, `Router` and `ReactiveForms`.

This [article](https://www.techiediaries.com/angular-rxjs-tutorial/) was originally posted in [techiediaries](https://www.techiediaries.com/).


