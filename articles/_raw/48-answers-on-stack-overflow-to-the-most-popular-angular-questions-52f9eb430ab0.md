---
title: 48 answers on StackOverflow to the most popular Angular questions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-11T12:13:18.000Z'
originalURL: https://freecodecamp.org/news/48-answers-on-stack-overflow-to-the-most-popular-angular-questions-52f9eb430ab0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TtrtAMfn2PATB_nD8YpeAA.png
tags:
- name: Angular
  slug: angular
- name: General Programming
  slug: programming
- name: Stack Overflow
  slug: stackoverflow
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Shlomi Levi

  I gathered the most common questions and answers from Stackoverflow. These questions
  were chosen by the highest score received. Whether you are an expert or a beginner,
  you can learn from others’ experiences.

  Table of Contents


  Angular...'
---

By Shlomi Levi

I gathered the most common questions and answers from Stackoverflow. These questions were chosen by the highest score received. Whether you are an expert or a beginner, you can learn from others’ experiences.

### Table of Contents

* [Angular — Promise vs Observable](#b4d0)
* [Difference between Constructor and ngOnInit](#d37e)
* [Can’t bind to ‘ngModel’ since it isn’t a known property of ‘input’](#008f)
* [Angular HTML binding](#7e4b)
* [Angular/RxJs When should I unsubscribe from `Subscription`](#22fe)
* [How can I select an element in a component template?](#5251)
* [What is the equivalent of ngShow and ngHide in Angular?](#b510)
* [How to bundle an Angular app for production](#76f3)
* [BehaviorSubject vs Observable?](#9842)
* [@Directive v/s @Component in Angular](#883d)
* [Angular HTTP GET with TypeScript error http.get(…).map is not a function in [null]](#4653)
* [How to use jQuery with Angular?](#9c12)
* [Angular EXCEPTION: No provider for Http](#2739)
* [Can’t bind to ‘formGroup’ since it isn’t a known property of ‘form’](#b612)
* [Angular DI Error — EXCEPTION: Can’t resolve all parameters](#ce7e)
* [Angular — Set headers for every request](#1761)
* [How to use *ngIf else in Angular?](#cace)
* [Angular no provider for NameService](#92c6)
* [Binding select element to object in Angular](#bc7c)
* [What is difference between declarations, providers and import in NgModule](#e423)
* [In Angular, how do you determine the active route?](#d774)
* [Angular CLI SASS options](#17bd)
* [Triggering change detection manually in Angular](#83b6)
* [Angular and Typescript: Can’t find names](#eb6d)
* [Angular — What is the meanings of module.id in component?](#c874)
* [How can I get new selection in “select” in Angular 2?](#831b)
* [Angular exception: Can’t bind to ‘ngForIn’ since it isn’t a known native property](#aad5)
* [*ngIf and *ngFor on same element causing error](#1556)
* [What is the Angular equivalent to an AngularJS $watch?](#a331)
* [Importing lodash into angular2 + typescript application](#7a78)
* [How to detect a route change in Angular?](#5b1c)
* [Global Events in Angular](#869e)
* [What are differences between SystemJS and Webpack?](#e7f2)
* [Angular: Can’t find Promise, Map, Set and Iterator](#176d)
* [Angular RC4 — Angular ^2.0.0 with Typescript 2.0.0](#2459)
* [How to detect when an @Input() value changes in Angular?](#6188)
* [How to pass url arguments (query string) to a HTTP request on Angular](#d2d3)
* [How do you deploy Angular apps?](#57cd)
* [ngFor with index as value in attribute](#fb28)
* [Define global constants in Angular 2](#c709)
* [Angular — Use pipes in services and components](#7910)
* [Angular2 Exception: Can’t bind to ‘routerLink’ since it isn’t a known native property](#1cef)
* [Angular 2 dynamic tabs with user-click chosen components](#4d6c)
* [Delegation: EventEmitter or Observable in Angular](#4f96)
* [How to add bootstrap to an angular-cli project](#bcef)
* [access key and value of object using *ngFor](#d3fa)
* [Angular exception: Can’t bind to ‘ngFor’ since it isn’t a known native property](#3f0e)
* [How to add font-awesome to Angular 2 + CLI project](#7f27)
* [Difference between HTTP and HTTPClient in angular 4?](#54eb)

**Enjoy!**

### Angular — Promise vs Observable

> 551+ points _? 1_50,497+ viewed   
> _**[Rohit](https://stackoverflow.com/users/6364715/rohit) asked,**_

Can someone please explain the difference between `Promise` and `Observable` in Angular?

An example on each would be helpful in understanding both the cases. In what scenario can we use each case?

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_answered, (686+ points)_**

**Promise**

A `Promise` handles a **single event** when an async operation completes or fails.

Note: There are `Promise` libraries out there that support cancellation, but ES6 `Promise` doesn't so far.

**Observable**

An `Observable` is like a `**Stream**` (in many languages) and allows to pass zero or more events where the callback is called for each event.

Often `Observable` is preferred over `Promise` because it provides the features of `Promise` and more. With `Observable` it doesn't matter if you want to handle 0, 1, or multiple events. You can utilize the same API in each case.

`Observable` also has the advantage over `Promise` to be **cancelable**. If the result of an HTTP request to a server or some other expensive async operation isn't needed anymore, the `Subscription` of an `Observable` allows to cancel the subscription, while a `Promise` will eventually call the success or failed callback even when you don't need the notification or the result it provides anymore.

Observable provides **operators** like `map`, `forEach`, `reduce`, ... similar to an array

There are also powerful operators like `retry()`, or `replay()`, ... that are often quite handy.

[**Source**](https://stackoverflow.com/questions/37364973)  
**[Top](#599b)**

### Difference between Constructor and ngOnInit

> 444+ points _? 1_90,166+ viewed   
> _**[Haseena P A](https://stackoverflow.com/users/4029338/haseena-p-a) asked,**_

Angular provides lifecycle hook `ngOnInit` by default.

Why should `ngOnInit` be used, if we already have a `constructor`?

> [**_Pardeep Jain_**](https://stackoverflow.com/users/5043867) **_answered, (512+ points)_**

The `Constructor` is a default method of the class that is executed when the class is instantiated and ensures proper initialization of fields in the class and its subclasses. Angular or better Dependency Injector (DI) analyzes the constructor parameters and when it creates a new instance by calling `new MyClass()` it tries to find providers that match the types of the constructor parameters, resolves them and passes them to the constructor like

```js
new MyClass(someArg);
```

`ngOnInit` is a lifecycle hook called by Angular2 to indicate that Angular is done creating the component.

We have to import `OnInit` in order to use like this (actually implementing `OnInit` is not mandatory but considered good practice):

```js
import {Component, OnInit} from '@angular/core';
```

then to use the method of `OnInit` we have to implement in the class like this.

```js
export class App implements OnInit{
  constructor(){
     //called first time before the ngOnInit()
  }
  
  ngOnInit(){
     //called after the constructor and called  after the first ngOnChanges() 
  }
}
```

`Implement this interface to execute custom initialization logic after your directive's data-bound properties have been initialized. ngOnInit is called right after the directive's data-bound properties have been checked for the first time, and before any of its children have been checked. It is invoked only once when the directive is instantiated.`

Mostly we use `ngOnInit` for all the initialization/declaration and avoid stuff to work in the constructor. The constructor should only be used to initialize class members but shouldn't do actual "work".

So you should use `constructor()` to setup Dependency Injection and not much else. ngOnInit() is better place to "start" - it's where/when components' bindings are resolved.

For more information refer here:

* [https://angular.io/api/core/OnInit](https://angular.io/api/core/OnInit)
* [Angular 2 Component Constructor Vs OnInit](https://stackoverflow.com/a/35846307/5043867)

[**Source**](https://stackoverflow.com/questions/35763730)  
**[Top](#599b)**

### Can’t bind to ‘ngModel’ since it isn’t a known property of ‘input’

> 442+ points _? 2_46,901+ viewed   
> _**[abreneliere](https://stackoverflow.com/users/3433751/anthony-breneli%C3%A8re) asked,**_

I’ve got the following error when launching my Angular app, even if the component is not displayed.

I have to comment out the so that my app works.

```bash
zone.js:461 Unhandled Promise rejection: Template parse errors:
Can't bind to 'ngModel' since it isn't a known property of 'input'. ("
    <div>
        <label>Created:</label>
        <input  type="text" [ERROR ->][(ngModel)]="test" placeholder="foo" />
    </div>
</div>"): InterventionDetails@4:28 ; Zone: <root> ; Task: Promise.then ; Value:
```

I’m looking at the Hero plucker but I don’t see any difference.

Here is the component file:

```js
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Intervention } from '../../model/intervention';

@Component({
    selector: 'intervention-details',
    templateUrl: 'app/intervention/details/intervention.details.html',
    styleUrls: ['app/intervention/details/intervention.details.css']
})

export class InterventionDetails
{
    @Input() intervention: Intervention;
    public test : string = "toto";
}
```

> [**_abreneliere_**](https://stackoverflow.com/users/3433751) **_answered, (674+ points)_**

Yes that’s it, in the app.module.ts, I just added :

```js
import { FormsModule } from '@angular/forms';

[...]

@NgModule({
  imports: [
    [...]
    FormsModule
  ],
  [...]
})
```

[**Source**](https://stackoverflow.com/questions/38892771)  
**[Top](#599b)**

### Angular HTML binding

> 385+ points _? 2_27,115+ viewed   
> _**[Aviad P.](https://stackoverflow.com/users/3433751/anthony-breneli%C3%A8re) asked,**_

I am writing an Angular application, and I have an HTML response I want to display. How do I do that? If I simply use the binding syntax `{{myVal}}` it encodes all HTML characters (of course).

I need somehow to bind the inner html of a div to the variable value.

> [**_prolink007_**](https://stackoverflow.com/users/427763) **_answered, (691+ points)_**

The correct syntax is now the following:

```html
<div [innerHTML]="theHtmlString"></div>
```

Working in `5.2.6`

[Documentation Reference](https://angular.io/docs/ts/latest/guide/template-syntax.html#!#property-binding-or-interpolation-)

[**Source**](https://stackoverflow.com/questions/31548311)  
**[Top](#599b)**

### Angular/RxJs When should I unsubscribe from `Subscription`

> 320+ points _? 6_9,606+ viewed   
> _**[Sergey Tihon](https://stackoverflow.com/users/1429493/sergey-tihon) asked,**_

When should I store the `Subscription` instances and invoke `unsubscribe()` during the NgOnDestroy lifecycle and when can I simply ignore them?

Saving all subscriptions introduces a lot of mess into component code.

[HTTP Client Guide](https://angular.io/docs/ts/latest/guide/server-communication.html) ignore subscriptions like this:

```js
getHeroes() {
  this.heroService.getHeroes()
                   .subscribe(
                     heroes => this.heroes = heroes,
                     error =>  this.errorMessage = <any>error);
}
```

In the same time [Route & Navigation Guide](https://angular.io/docs/ts/latest/guide/router.html) says that:

`Eventually, we'll navigate somewhere else. The router will remove this component from the DOM and destroy it. We need to clean up after ourselves before that happens. Specifically, we must unsubscribe before Angular destroys the component. Failure to do so could create a memory leak.`

`We unsubscribe from our Observable in the ngOnDestroy method.`

```js
private sub: any;

ngOnInit() {
  this.sub = this.route.params.subscribe(params => {
     let id = +params['id']; // (+) converts string 'id' to a number
     this.service.getHero(id).then(hero => this.hero = hero);
   });
}

ngOnDestroy() {
  this.sub.unsubscribe();
}
```

> [**_seangwright_**](https://stackoverflow.com/users/939634) **_answered, (508+ points)_**

#### — — Edit 3 — The ‘Official’ Solution (2017/04/09)

I spoke with Ward Bell about this question at NGConf (I even showed him this answer which he said was correct) but he told me the docs team for Angular had a solution to this question that is unpublished (though they are working on getting it approved). He also told me I could update my SO answer with the forthcoming official recommendation.

The solution we should all use going forward is to add a `private ngUnsubscribe: Subject = new Subject();` field to all components that have `.subscribe()` calls to `Observable`s within their class code.

We then call `this.ngUnsubscribe.next(); this.ngUnsubscribe.complete();` in our `ngOnDestroy()` methods.

The secret sauce (as noted already by [@metamaker](https://stackoverflow.com/a/42695571/939634)) is to call `.takeUntil(this.ngUnsubscribe)` before each of our `.subscribe()` calls which will guarantee all subscriptions will be cleaned up when the component is destroyed.

Example:

```js
import { Component, OnDestroy, OnInit } from '@angular/core';
import 'rxjs/add/operator/takeUntil';
// import { takeUntil } from 'rxjs/operators'; // for rxjs ^5.5.0 lettable operators
import { Subject } from 'rxjs/Subject';

import { MyThingService } from '../my-thing.service';

@Component({
    selector: 'my-thing',
    templateUrl: './my-thing.component.html'
})
export class MyThingComponent implements OnDestroy, OnInit {
    private ngUnsubscribe: Subject = new Subject();
    
    constructor(
        private myThingService: MyThingService,
    ) { }
    
    ngOnInit() {
        this.myThingService.getThings()
            .takeUntil(this.ngUnsubscribe)
            .subscribe(things => console.log(things));
            
        /* if using lettable operators in rxjs ^5.5.0
        this.myThingService.getThings()
            .pipe(takeUntil(this.ngUnsubscribe))
            .subscribe(things => console.log(things));
        */
        
        this.myThingService.getOtherThings()
            .takeUntil(this.ngUnsubscribe)
            .subscribe(things => console.log(things));
            
    }
    
    ngOnDestroy() {
        this.ngUnsubscribe.next();
        this.ngUnsubscribe.complete();
    }
}
```

#### — — Edit 2 (2016/12/28)

**Source 5**

The Angular tutorial, the Routing chapter now states the following: “The Router manages the observables it provides and localizes the subscriptions. The subscriptions are cleaned up when the component is destroyed, protecting against memory leaks, so we don’t need to unsubscribe from the route params Observable.” — [Mark Rajcok](https://stackoverflow.com/questions/38008334/angular2-rxjs-when-should-i-unsubscribe-from-subscription/41177163?noredirect=1#comment69909721_41177163)

Here’s a [discussion](https://github.com/angular/angular.io/issues/3003#issuecomment-268429065) on the Github issues for the Angular docs regarding Router Observables where Ward Bell mentions that clarification for all of this is in the works.

#### — — Edit 1

**Source 4**

In this [video from NgEurope](https://youtu.be/WWR9nxVx1ec?t=20m32s) Rob Wormald also says you do not need to unsubscribe from Router Observables. He also mentions the `http` service and `ActivatedRoute.params` in this [video from November 2016](https://youtu.be/VLGCCpOWFFw?t=33m37s).

#### — — Original Answer

**TLDR:**

For this question there are (2) kinds of `Observables` - **finite** value and **infinite** value.

`http` `Observables` produce **finite** (1) values and something like a DOM `event listener` `Observables` produce **infinite** values.

If you manually call `subscribe` (not using async pipe), then `unsubscribe` from **infinite** `Observables`.

Don’t worry about **finite** ones, `RxJs` will take care of them.

**Source 1**

I tracked down an answer from Rob Wormald in Angular’s Gitter [here](https://gitter.im/angular/angular?at=5681e8fa3c68940269251fa5).

He states (i reorganized for clarity and emphasis is mine)

`if it's **a single-value-sequence** (like an http request) the **manual cleanup is unnecessary** (assuming you subscribe in the controller manually)`

`i should say "if it's a **sequence that completes**" (of which single value sequences, a la http, are one)`

`**if it's an infinite sequence**, **you should unsubscribe** which the async pipe does for you`

Also he mentions in this [youtube video](https://youtu.be/UHI0AzD_WfY?t=26m42s) on Observables that `they clean up after themselves`... in the context of Observables that `complete` (like Promises, which always complete because they are always producing 1 value and ending - we never worried about unsubscribing from Promises to make sure they clean up `xhr` event listeners, right?).

**Source 2**

Also in the [Rangle guide to Angular 2](https://angular-2-training-book.rangle.io/handout/observables/disposing_subscriptions_and_releasing_resources.html) it reads

`In most cases we will not need to explicitly call the unsubscribe method unless we want to cancel early or our Observable has a longer lifespan than our subscription. The default behavior of Observable operators is to dispose of the subscription as soon as .complete() or .error() messages are published. Keep in mind that RxJS was designed to be used in a "fire and forget" fashion most of the time.`

When does the phrase `our Observable has a longer lifespan than our subscription` apply?

It applies when a subscription is created inside a component which is destroyed before (or not ‘long’ before) the `Observable` completes.

I read this as meaning if we subscribe to an `http` request or an observable that emits 10 values and our component is destroyed before that `http` request returns or the 10 values have been emitted, we are still ok!

When the request does return or the 10th value is finally emitted the `Observable` will complete and all resources will be cleaned up.

**Source 3**

If we look at [this example](https://angular-2-training-book.rangle.io/handout/routing/routeparams.html) from the same Rangle guide we can see that the `Subscription` to `route.params` does require an `unsubscribe()` because we don't know when those `params` will stop changing (emitting new values).

The component could be destroyed by navigating away in which case the route params will likely still be changing (they could technically change until the app ends) and the resources allocated in subscription would still be allocated because there hasn’t been a `completion`.

[**Source**](https://stackoverflow.com/questions/38008334)  
**[Top](#599b)**

### How can I select an element in a component template?

> 263+ points _? 2_65,966+ viewed   
> _**[Aman Gupta](https://stackoverflow.com/users/2748475/aman-gupta) asked,**_

Does anybody know how to get hold of an element defined in a component template? Polymer makes it really easy with the `$` and `$$`.

I was just wondering how to go about it in Angular.

Take the example from the tutorial:

```js
import {Component} from '@angular/core'

@Component({
    selector:'display'
    template:`
     <input #myname(input)="updateName(myname.value)"/>
     <p>My name : {{myName}}</p>
    `
    
})
export class DisplayComponent {
    myName: string = "Aman";
    updateName(input: String) {
        this.myName = input;
    }
}
```

How do I catch hold of a reference of the `p` or `input` element from within the class definition?

> [**_Brocco_**](https://stackoverflow.com/users/1413538) **_answered, (149+ points)_**

You can get a handle to the DOM element via `ElementRef` by injecting it into your component's constructor:

```js
constructor(myElement: ElementRef) { ... }
```

Docs: [https://angular.io/docs/ts/latest/api/core/index/ElementRef-class.html](https://angular.io/docs/ts/latest/api/core/index/ElementRef-class.html)

[**Source**](https://stackoverflow.com/questions/32693061)  
**[Top](#599b)**

### What is the equivalent of ngShow and ngHide in Angular?

> 261+ points _? 2_06,651+ viewed   
> **[Mihai Răducanu](https://stackoverflow.com/users/2870735/mihai-r%C4%83ducanu)** _**asked,**_

I have a number of elements that I want to be visible under certain conditions.

In AngularJS I would write

```html
<div ng-show="myVar">stuff</div>
```

How can I do this in Angular?

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_answered, (445+ points)_**

Just bind to the `hidden` property

```html
[hidden]="!myVar"
```

See also

* [https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden)

**issues**

`hidden` has some issues though because it can conflict with CSS for the `display` property.

See how `some` in [**Plunker example**](https://plnkr.co/edit/SO3c3UUT3LBvhNAeriCz?p=preview) doesn't get hidden because it has a style

```css
:host {display: block;}
```

set. (This might behave differently in other browsers — I tested with Chrome 50)

**workaround**

You can fix it by adding

```css
[hidden] { display: none !important;}
```

To a global style in `index.html`.

**another pitfall**

```html
hidden="false"
hidden="{{false}}"
hidden="{{isHidden}}" // isHidden = false;
```

are the same as

```html
hidden="true"
```

and will not show the element.

`hidden="false"` will assign the string `"false"` which is considered truthy.  
Only the value `false` or removing the attribute will actually make the element visible.

Using `{{}}` also converts the expression to a string and won't work as expected.

Only binding with `[]` will work as expected because this `false` is assigned as `false` instead of `"false"`.

`***ngIf**` **vs `[hidden]`**

`*ngIf` effectively removes its content from the DOM while `[hidden]` modifies the `display` property and only instructs the browser to not show the content but the DOM still contains it.

[**Source**](https://stackoverflow.com/questions/35578083)  
**[Top](#599b)**

### How to bundle an Angular app for production

> 258+ points _? 1_11,603+ viewed   
> _**[Pat M](https://stackoverflow.com/users/4155124/pat-m) asked,**_

I would like to track and update in this thread the latest best (and hopefully the simplest) method to bundle Angular (version 2, 4, …) for production on a live web server.

Please include the Angular version within answers so we can track better when it moves to later releases.

> [**_Nicolas Henneaux_**](https://stackoverflow.com/users/1630604) **_answered, (267+ points)_**

#### `2.x, 4.x, 5.x` (TypeScript) with Angular CLI

#### OneTime Setup

* `npm install -g @angular/cli`
* `ng new projectFolder` creates a new application

#### Bundling Step

* `ng build --prod` (run in command line when directory is `projectFolder`)
* _flag `prod` bundle for production (see the [Angular documentation](https://github.com/angular/angular-cli/wiki/build#--dev-vs---prod-builds) for the list of option included with the production flag)._
* Compress using [Brotli compression](https://en.wikipedia.org/wiki/Brotli) the resources using the following command`for i in dist/*; do brotli $i; done`

_bundles are generated by default to **projectFolder/dist/**_

#### Output

_Sizes with Angular `5.2.8` with CLI `1.7.2`_

* `dist/main.[hash].bundle.js` Your application bundled [ size: 151 KB for new Angular CLI application empty, **36 KB** compressed].
* `dist/polyfill.[hash].bundle.js` the polyfill dependencies (@angular, RxJS...) bundled [ size: 58 KB for new Angular CLI application empty, **17 KB** compressed].
* `dist/index.html` entry point of your application.
* `dist/inline.[hash].bundle.js` webpack loader
* `dist/style.[hash].bundle.css` the style definitions
* `dist/assets` resources copied from the Angular CLI assets configuration

#### Deployment

You can get a preview of your application using the `ng serve --prod` command that starts a local HTTP server such that the application with production files is accessible using [http://localhost:4200](http://localhost:4200).

For a production usage, you have to deploy all the files from the `dist` folder in the HTTP server of your choice.

[**Source**](https://stackoverflow.com/questions/37631098)  
**[Top](#599b)**

### BehaviorSubject vs Observable?

> 250+ points _? 1_22,248+ viewed   
> _**[Kevin Mark](https://stackoverflow.com/users/6620551/kevin-mark) asked,**_

I’m looking into Angular RxJs patterns and I don’t understand the difference between a BehaviorSubject and an Observable.

From my understanding, a BehaviorSubject is a value that can change over time (can be subscribed to and subscribers can receive updated results). This seems to be the exact same purpose of an Observable.

When would you use an Observable vs a BehaviorSubject? Are there benefits to using a BehaviorSubject over an Observable or vice versa?

> [**_Shantanu Bhadoria_**](https://stackoverflow.com/users/3070452) **_answered, (425+ points)_**

BehaviorSubject is a type of subject, a subject is a special type of observable so you can subscribe to messages like any other observable. The unique features of BehaviorSubject are:

* It needs an initial value as it must always return a value on subscription even if it hasn’t received a `next()`
* Upon subscription it returns the last value of the subject. A regular observable only triggers when it receives an `onnext`
* at any point you can retrieve the last value of the subject in a non-observable code using the `getValue()` method.

Unique features of a subject compared to an observable are:

* It is an observer in addition to being an observable so you can also send values to a subject in addition to subscribing to it.

In addition you can get an observable from behavior subject using the `asobservable()` method on BehaviorSubject.

Observable is a Generic, and BehaviorSubject is technically a sub-type of Observable because BehaviorSubject is an observable with specific qualities.

Example with BehaviorSubject:

```js
// Behavior Subject

// a is an initial value. if there is a subscription 
// after this, it would get "a" value immediately
let bSubject = new BehaviorSubject("a"); 

bSubject.next("b");

bSubject.subscribe((value) => {
  console.log("Subscription got", value); // Subscription got b, 
                                          // ^ This would not happen 
                                          // for a generic observable 
                                          // or generic subject by default
});

bSubject.next("c"); // Subscription got c
bSubject.next("d"); // Subscription got d
```

Example 2 with regular subject:

```js
// Regular Subject

let subject = new Subject(); 

subject.next("b");

subject.subscribe((value) => {
  console.log("Subscription got", value); // Subscription wont get 
                                          // anything at this point
});

subject.next("c"); // Subscription got c
subject.next("d"); // Subscription got d
```

An observable can be created from both Subject and BehaviorSubject using `subject.asobservable()`. Only difference being you can't send values to an observable using `next()` method.

In Angular services, I would use BehaviorSubject for a data service as a angular service often initializes before component and behavior subject ensures that the component consuming the service receives the last updated data even if there are no new updates since the component’s subscription to this data.

[**Source**](https://stackoverflow.com/questions/39494058)  
**[Top](#599b)**

### @Directive v/s @Component in Angular

> 239+ points _? 6_1,582+ viewed   
> _[**Prasanjit Dey**](https://stackoverflow.com/users/4917853/prasanjit-dey) **asked,**_

What is the difference between `@Component` and `@Directive` in Angular? Both of them seem to do the same task and have the same attributes.

What are the use cases and when to prefer one over another?

> [**_jaker_**](https://stackoverflow.com/users/1771017) **_answered, (327+ points)_**

**A @Component requires a view whereas a @Directive does not.**

### Directives

I liken a @Directive to an Angular 1.0 directive with the option `restrict: 'A'` (Directives aren't limited to attribute usage.) Directives add behaviour to an existing DOM element or an existing component instance. One example use case for a directive would be to log a click on an element.

```js
import {Directive} from '@angular/core';

@Directive({
    selector: "[logOnClick]",
    hostListeners: {
        'click': 'onClick()',
    },
})

class LogOnClick {
    constructor() {}
    onClick() { console.log('Element clicked!'); }
}
```

Which would be used like so:

```js
<button logOnClick>I log when clicked!<;/button>
```

### Components

A component, rather than adding/modifying behaviour, actually creates its own view (hierarchy of DOM elements) with attached behaviour. An example use case for this might be a contact card component:

```js
import {Component, View} from '@angular/core';

@Component({
  selector: 'contact-card',
  template: `
    <div>
      <h1>{{name}}</h1>
      <p>{{city}}</p>
    </div>
  `
})
class ContactCard {
  @Input() name: string
  @Input() city: string
  constructor() {}
}
```

Which would be used like so:

```js
<contact-card [name]="'foo'" [city]="'bar'"></contact-card>
```

`ContactCard` is a reusable UI component that we could use anywhere in our application, even within other components. These basically make up the UI building blocks of our applications.

### In summary

Write a component when you want to create a reusable set of DOM elements of UI with custom behaviour. Write a directive when you want to write reusable behaviour to supplement existing DOM elements.

Sources:

* [@Directive documentation](https://angular.io/api/core/Directive)
* [@Component documentation](https://angular.io/api/core/Component)
* [Helpful blog post](http://blog.codeleak.pl/2015/06/angular2hello-world.html)

[**Source**](https://stackoverflow.com/questions/32680244)  
**[Top](#599b)**

### Angular HTTP GET with TypeScript error http.get(…).map is not a function in [null]

> 233+ points _? 1_41,917+ viewed   
> _[**Claudiu**](https://stackoverflow.com/users/4834129/claudiu) **asked,**_

I have a problem with HTTP in Angular.

I just want to `GET` a `JSON` list and show it in the view.

#### Service class

```js
import {Injectable} from "angular2/core";
import {Hall} from "./hall";
import {Http} from "angular2/http";
@Injectable()
export class HallService {
    public http:Http;
    public static PATH:string = 'app/backend/' 
    
    constructor(http:Http) {
        this.http=http;
    }
    
    getHalls() {
           return this.http.get(HallService.PATH + 'hall.json').map((res:Response) => res.json());
    }
}
```

And in the `HallListComponent` I call the `getHalls` method from the service:

```js
export class HallListComponent implements OnInit {
    public halls:Hall[];
    public _selectedId:number;
    
    constructor(private _router:Router,
                private _routeParams:RouteParams,
                private _service:HallService) {
        this._selectedId = +_routeParams.get('id');
    }
    
    ngOnInit() {
        this._service.getHalls().subscribe((halls:Hall[])=>{ 
            this.halls=halls;
        });
    }
}
```

However, I got an exception:

`TypeError: this.http.get(...).map is not a function in [null]`

#### hall-center.component

```js
import {Component} from "angular2/core";
import {RouterOutlet} from "angular2/router";
import {HallService} from "./hall.service";
import {RouteConfig} from "angular2/router";
import {HallListComponent} from "./hall-list.component";
import {HallDetailComponent} from "./hall-detail.component";
@Component({
    template:`
        <h2>my app</h2>
        <router-outlet></router-outlet>
    `,
    directives: [RouterOutlet],
    providers: [HallService]
})

@RouteConfig([
    {path: '/',         name: 'HallCenter', component:HallListComponent, useAsDefault:true},
    {path: '/hall-list', name: 'HallList', component:HallListComponent}
])

export class HallCenterComponent{}
```

#### app.component

```js
import {Component} from 'angular2/core';
import {ROUTER_DIRECTIVES} from "angular2/router";
import {RouteConfig} from "angular2/router";
import {HallCenterComponent} from "./hall/hall-center.component";
@Component({
    selector: 'my-app',
    template: `
        <h1>Examenopdracht Factory</h1>
        <a [routerLink]="['HallCenter']">Hall overview</a>
        <router-outlet></router-outlet>
    `,
    directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
    {path: '/hall-center/...', name:'HallCenter',component:HallCenterComponent,useAsDefault:true}
])
export class AppComponent { }
```

#### tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES5",
    "module": "system",
    "moduleResolution": "node",
    "sourceMap": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "removeComments": false,
    "noImplicitAny": false
  },
  "exclude": [
    "node_modules"
  ]
}
```

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_answered, (416+ points)_**

I think that you need to import this:

```js
import 'rxjs/add/operator/map'
```

Or more generally this if you want to have more methods for observables. **WARNING: This will import all 50+ operators and add them to your application, thus affecting your bundle size and load times.**

```js
import 'rxjs/Rx';
```

See [this issue](https://github.com/angular/angular/issues/5632#issuecomment-167026172) for more details.

[**Source**](https://stackoverflow.com/questions/34515173)  
**[Top](#599b)**

### How to use jQuery with Angular?

> 233+ points _? 2_46,869+ viewed   
> _**[Waog](https://stackoverflow.com/users/2398523/waog) asked,**_

Can anyone tell me, how to use **jQuery** with **Angular**?

```js
class MyComponent {
    constructor() {
        // how to query the DOM element from here?
    }
}
```

I’m aware there are workarounds like manipulating the _class_ or _id_ of the DOM element upfront, but I’m hoping for a cleaner way of doing it.

> [**_werenskjold_**](https://stackoverflow.com/users/2881743) **_answered, (258+ points)_**

Using jQuery from Angular2 is a breeze compared to ng1. If you are using TypeScript you could first reference jQuery typescript definition.

```bash
tsd install jquery --save
or
typings install dt~jquery --global --save
```

TypescriptDefinitions are not required since you could just use `any` as the type for `$` or `jQuery`

In your angular component you should reference a DOM element from the template using `@ViewChild()` After the view has been initialized you can use the `nativeElement` property of this object and pass to jQuery.

Declaring `$` (or `jQuery`) as JQueryStatic will give you a typed reference to jQuery.

```ts
import {bootstrap}    from '@angular/platform-browser-dynamic';
import {Component, ViewChild, ElementRef, AfterViewInit} from '@angular/core';
declare var $:JQueryStatic;

@Component({
    selector: 'ng-chosen',
    template: `<select #selectElem>
        <option *ngFor="#item of items" [value]="item" [selected]="item === selectedValue">{{item}} option</option>
        </select>
        <h4> {{selectedValue}}</h4>`
})
export class NgChosenComponent implements AfterViewInit {
    @ViewChild('selectElem') el:ElementRef;
    items = ['First', 'Second', 'Third'];
    selectedValue = 'Second';
    
    ngAfterViewInit() {
        $(this.el.nativeElement)
            .chosen()
            .on('change', (e, args) => {
                this.selectedValue = args.selected;
            });
    }
}

bootstrap(NgChosenComponent);
```

This example is available on plunker: [http://plnkr.co/edit/Nq9LnK?p=preview](http://plnkr.co/edit/Nq9LnK?p=preview)

tslint will complain about `chosen` not being a property on $, to fix this you can add a definition to the JQuery interface in your custom *.d.ts file

```js
interface JQuery {
    chosen(options?:any):JQuery;
}
```

[**Source**](https://stackoverflow.com/questions/30623825)  
**[Top](#599b)**

### Angular EXCEPTION: No provider for Http

> 230+ points _? 1_42,976+ viewed   
> _**[daniel](https://stackoverflow.com/users/516389/daniel) asked,**_

I am getting the `EXCEPTION: No provider for Http!` in my Angular app. What am I doing wrong?

```ts
import {Http, Headers} from 'angular2/http';
import {Injectable} from 'angular2/core'

@Component({
    selector: 'greetings-ac-app2',
    providers: [],
    templateUrl: 'app/greetings-ac2.html',
    directives: [NgFor, NgModel, NgIf, FORM_DIRECTIVES],
    pipes: []
})
export class GreetingsAcApp2 {
    private str:any;
    
    constructor(http: Http) {
    
        this.str = {str:'test'};
        http.post('http://localhost:18937/account/registeruiduser/',
            JSON.stringify(this.str),
            {
                headers: new Headers({
                    'Content-Type': 'application/json'
                })
            });
```

> [**_Philip Miglinci_**](https://stackoverflow.com/users/2083492) **_answered, (381+ points)_**

Import the HttpModule

```ts
import { HttpModule } from '@angular/http';

@NgModule({
    imports: [ BrowserModule, HttpModule ],
    providers: [],
    declarations: [ AppComponent ],
    bootstrap: [ AppComponent ]
})
export default class AppModule { }

platformBrowserDynamic().bootstrapModule(AppModule);
```

Ideally you split up this code in two separate files. For further information read:

* [https://angular.io/docs/ts/latest/cookbook/rc4-to-rc5.html](https://angular.io/docs/ts/latest/cookbook/rc4-to-rc5.html)
* [https://angular.io/docs/ts/latest/guide/ngmodule.html](https://angular.io/docs/ts/latest/guide/ngmodule.html)

[**Source**](https://stackoverflow.com/questions/33721276)  
**[Top](#599b)**

### Can’t bind to ‘formGroup’ since it isn’t a known property of ‘form’

> 227+ points _? 1_27,130+ viewed   
> _**[johnnyfittizio](https://stackoverflow.com/users/2433664/francescomussi) asked,**_

**THE SITUATION:**

Please help! I am trying to make what should be a very simple form in my Angular2 app but no matter what it never works.

**ANGULAR VERSION:**

Angular 2.0.0 Rc5

**THE ERROR:**

```
Can't bind to 'formGroup' since it isn't a known property of 'form'
```

![Image](https://cdn-media-1.freecodecamp.org/images/SP8f73A8L3lPs6fS9frNubiN5UEniPY2yj3p)

**THE CODE:**

The view:

```html
<form [formGroup]="newTaskForm" (submit)="createNewTask()">
    <div class="form-group">
        <label for="name">Name</label>
        <input type="text" name="name" required>
    </div>
     <button type="submit" class="btn btn-default">Submit</button>
</form>
```

The controller:

```ts
import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder }  from '@angular/forms';
import {FormsModule,ReactiveFormsModule} from '@angular/forms';
import { Task } from './task';

@Component({
    selector: 'task-add',
    templateUrl: 'app/task-add.component.html'
    
})

export class TaskAddComponent {

    newTaskForm: FormGroup;
    
    constructor(fb: FormBuilder) 
    {
        this.newTaskForm = fb.group({
            name: ["", Validators.required]
        });
    }
    
    createNewTask()
    {
        console.log(this.newTaskForm.value)
    }
    
}
```

The ngModule:

```ts
import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';

import { routing }        from './app.routing';
import { AppComponent }  from './app.component';
import { TaskService } from './task.service'

@NgModule({
    imports: [ 
        BrowserModule,
        routing,
        FormsModule
    ],
    declarations: [ AppComponent ],
    providers: [
        TaskService
    ],
    bootstrap: [ AppComponent ]
})

export class AppModule { }
```

**THE QUESTION:**

Why am I getting that error?

Am I missing something?

> [**_Stefan Svrkota_**](https://stackoverflow.com/users/6677986) **_answered, (465+ points)_**

**RC5 FIX**

You need to `import { REACTIVE_FORM_DIRECTIVES } from '@angular/forms'` in your controller and add it to `directives` in `@Component`. That will fix the problem.

After you fix that, you will probably get another error because you didn’t add `formControlName="name"` to your input in form.

**RC6/RC7/Final release FIX**

To fix this error, you just need to import `ReactiveFormsModule` from `@angular/forms` in your module. Here's the example of a basic module with `ReactiveFormsModule` import:

```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppComponent }  from './app.component';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        ReactiveFormsModule
    ],
    declarations: [
        AppComponent
    ],
    bootstrap: [AppComponent]
})

export class AppModule { }
```

To explain further, `formGroup` is a selector for directive named `FormGroupDirective` that is a part of `ReactiveFormsModule`, hence the need to import it. It is used to bind an existing `FormGroup` to a DOM element. You can read more about it on [Angular's official docs page](https://angular.io/docs/ts/latest/api/forms/index/FormGroupDirective-directive.html).

[**Source**](https://stackoverflow.com/questions/39152071)  
**[Top](#599b)**

### Angular DI Error — EXCEPTION: Can’t resolve all parameters

> 221+ points _? 1_42,497+ viewed   
> _**[Keith Otto](https://stackoverflow.com/users/4321757/keith-otto) asked,**_

I’ve built a basic app in Angular, but I have encountered a strange issue where I cannot inject a service into one of my components. It injects fine into any of the three other components I have created however.

For starters, this is the service:

```ts
import { Injectable } from '@angular/core';

@Injectable()
export class MobileService {
  screenWidth: number;
  screenHeight: number;
  
  constructor() {
    this.screenWidth = window.outerWidth;
    this.screenHeight = window.outerHeight;
    
    window.addEventListener("resize", this.onWindowResize.bind(this) )
  }
  
  onWindowResize(ev: Event) {
    var win = (ev.currentTarget as Window);
    this.screenWidth = win.outerWidth;
    this.screenHeight = win.outerHeight;
  }
  
}
```

And the component that it refuses to work with:

```ts
import { Component, } from '@angular/core';
import { NgClass } from '@angular/common';
import { ROUTER_DIRECTIVES } from '@angular/router';

import {MobileService} from '../';

@Component({
  moduleId: module.id,
  selector: 'pm-header',
  templateUrl: 'header.component.html',
  styleUrls: ['header.component.css'],
  directives: [ROUTER_DIRECTIVES, NgClass],
})
export class HeaderComponent {
  mobileNav: boolean = false;
  
  constructor(public ms: MobileService) {
    console.log(ms);
  }
  
}
```

The error I get in the browser console is this:

`EXCEPTION: Can't resolve all parameters for HeaderComponent: (?).`

I have the service in the bootstrap function so it has a provider. And I seem to be able to inject it into the constructor of any of my other components without issue.

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_answered, (272+ points)_**

Import it from the file where it is declared directly instead of the barrel.

I don’t know what exactly causes the issue but I saw it mentioned several times (probably some kind of circular dependency).

It should also be fixable by changing the order of the exports in the barrel (don’t know details, but was mentioned as well)

[**Source**](https://stackoverflow.com/questions/37997824)  
**[Top](#599b)**

### Angular — Set headers for every request

> 209+ points _? 2_05,557+ viewed   
> _**[Avijit Gupta](https://stackoverflow.com/users/4135178/avijit-gupta) asked,**_

I need to set some Authorization headers after the user has logged in, for every subsequent request.

To set headers for a particular request,

```ts
import {Headers} from 'angular2/http';
var headers = new Headers();
headers.append(headerName, value);

// HTTP POST using these headers
this.http.post(url, data, {
  headers: headers
})
// do something with the response
```

[Reference](https://auth0.com/blog/2015/10/15/angular-2-series-part-3-using-http/)

But it would be not be feasible to manually set request headers for every request in this way.

How do I set the headers set once the user has logged in, and also remove those headers on logout?

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_answered, (283+ points)_**

To answer, you question you could provide a service that wraps the original `Http` object from Angular. Something like described below.

```ts
import {Injectable} from '@angular/core';
import {Http, Headers} from '@angular/http';

@Injectable()
export class HttpClient {

  constructor(private http: Http) {}
  
  createAuthorizationHeader(headers: Headers) {
    headers.append('Authorization', 'Basic ' +
      btoa('username:password')); 
  }
  
  get(url) {
    let headers = new Headers();
    this.createAuthorizationHeader(headers);
    return this.http.get(url, {
      headers: headers
    });
  }
  
  post(url, data) {
    let headers = new Headers();
    this.createAuthorizationHeader(headers);
    return this.http.post(url, data, {
      headers: headers
    });
  }
}
```

And instead of injecting the `Http` object you could inject this one (`HttpClient`).

```ts
import { HttpClient } from './http-client';

export class MyComponent {
  // Notice we inject "our" HttpClient here, naming it Http so it's easier
  constructor(http: HttpClient) {
    this.http = httpClient;
  }
  
  handleSomething() {
    this.http.post(url, data).subscribe(result => {
        // console.log( result );
    });
  }
}
```

I also think that something could be done using multi providers for the `Http` class by providing your own class extending the `Http` one... See this link: [http://blog.thoughtram.io/angular2/2015/11/23/multi-providers-in-angular-2.html](http://blog.thoughtram.io/angular2/2015/11/23/multi-providers-in-angular-2.html).

[**Source**](https://stackoverflow.com/questions/34464108)  
**[Top](#599b)**

### How to use *ngIf else in Angular?

> 205+ points _? 2_03,768+ viewed   
> _[**kawli norman**](https://stackoverflow.com/users/5486494/kawli-norman) **asked,**_

I’m using Angular and I want to use `*ngIf else` (available since version 4) in this example:

```
<div *ngIf="isValid">
  content here ...
</div>

<div *ngIf="!isValid">
 other content here...
</div>
```

How can I acheive the same behavior with `ngIf else` ?

> [**_Bougarfaoui El houcine_**](https://stackoverflow.com/users/7273246) **_answered, (384+ points)_**

**Angular 4 and 5**:

using `else` :

```html
<div *ngIf="isValid;else other_content">
    content here ...
</div>

<ng-template #other_content>other content here...</ng-template>
```

you can also use `then else` :

```html
<div *ngIf="isValid;then content else other_content">here is ignored</div>

<ng-template #content>content here...</ng-template>
<ng-template #other_content>other content here...</ng-template>
```

or `then` alone :

```html
<div *ngIf="isValid;then content"></div>

<ng-template #content>content here...</ng-template>
```

**Demo :**

[**Plunker**](https://plnkr.co/edit/XD5vLvmwTApcaHJ66Is1)

**Details:**

`<ng-template>` : is Angular’s own implementation of the `<template>` tag which is [according to MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template) :

`The HTML <template> element is a mechanism for holding client-side content that is not to be rendered when a page is loaded but may subsequently be instantiated during runtime using JavaS`cript.

[**Source**](https://stackoverflow.com/questions/43006550)  
**[Top](#599b)**

### Angular no provider for NameService

> 196+ points _? 1_86,526+ viewed   
> _**[M.Svrcek](https://stackoverflow.com/users/2667885/m-svrcek) asked,**_

I’ve got problem with loading class into Angular component. I’m trying to solve for long time, even tried to add it to single file. What I have is:

**Application.ts**

```ts
/// <reference path="../typings/angular2/angular2.d.ts" />

import {Component,View,bootstrap,NgFor} from "angular2/angular2";
import {NameService} from "./services/NameService";

@Component({
    selector:'my-app',
    injectables: [NameService]
})
@View({
    template:'<h1>Hi {{name}}</h1>' +
    '<p>Friends</p>' +
    '<ul>' +
    '   <li *ng-for="#name of names">{{name}}</li>' +
    '</ul>',
    directives:[NgFor]
})

class MyAppComponent
{
    name:string;
    names:Array<string>;
    
    constructor(nameService:NameService)
    {
        this.name = 'Michal';
        this.names = nameService.getNames();
    }
}
bootstrap(MyAppComponent);
```

**services/NameService.ts**

```ts
export class NameService {
    names: Array<string>;
    constructor() {
        this.names = ["Alice", "Aarav", "Martín", "Shannon", "Ariana", "Kai"];
    }
    getNames()
    {
        return this.names;
    }
}
```

All the time I’m getting error message saying “No provider for NameService” …

Can someone help me spot that small issue with my code?

> [**_Klas Mellbourn_**](https://stackoverflow.com/users/46194) **_answered, (309+ points)_**

You have to use `providers` instead of `injectables`

```ts
@Component({
    selector: 'my-app',
    providers: [NameService]
})
```

[Complete code sample here](https://github.com/Mellbourn/angular2-step-by-step-guide).

[**Source**](https://stackoverflow.com/questions/30580083)  
**[Top](#599b)**

### Binding select element to object in Angular

> 194+ points _? 1_97,048+ viewed   
> _[**RHarris**](https://stackoverflow.com/users/372296/rharris) **asked,**_

I’m new to Angular and trying to get up to speed with the new way of doing things.

I’d like to bind a select element to a list of objects — which is easy enough:

```ts
@Component({
   selector: 'myApp',
   template: `<h1>My Application</h1>
              <select [(ngModel)]="selectedValue">
                 <option *ngFor="#c of countries" value="c.id">{{c.name}}</option>
              </select>`
})
export class AppComponent{
    countries = [
       {id: 1, name: "United States"},
       {id: 2, name: "Australia"}
       {id: 3, name: "Canada"}
       {id: 4, name: "Brazil"}
       {id: 5, name: "England"}
     ];
    selectedValue = null;
}
```

In this case, it appears that selectedValue would be a number — the id of the selected item.

However, I’d actually like to bind to the country object itself so that selectedValue is the object rather than just the id. I tried changing the value of the option like so:

```ts
<option *ngFor="#c of countries" value="c">{{c.name}}<;/option>
```

but this does not seem to work. It seems to place an object in my selectedValue — but not the object that I’m expecting. You can [see this in my Plunker example](http://plnkr.co/edit/HGRGv33EFwxDsSnELofk?p=preview).

I also tried binding to the change event so that I could set the object myself based on the selected id; however, it appears that the change event fires before the bound ngModel is updated — meaning I don’t have access to the newly selected value at that point.

Is there a clean way to bind a select element to an object with Angular 2?

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_answered, (361+ points)_**

```ts
<h1>My Application</h1>
<select [(ngModel)]="selectedValue">
  <option *ngFor="let c of countries" [ngValue]="c">{{c.name}}</option>
</select>
```

[**Plunker example**](https://plnkr.co/edit/njGlIV?p=preview)

NOTE: you can use `[ngValue]="c"` instead of `[ngValue]="c.id"` where c is the complete country object.

`[value]="..."` only supports string values  
`[ngValue]="..."` supports any type

**update**

If the `value` is an object, the preselected instance needs to be identical with one of the values.

See also the recently added custom comparison [https://github.com/angular/angular/issues/13268](https://github.com/angular/angular/issues/13268) **available since 4.0.0-beta.7**

```ts
<select [compareWith]="compareFn" ...
```

Take care of if you want to access `this` within `compareFn`.

```ts
compareFn = this._compareFn.bind(this);

// or 
// compareFn = (a, b) => this._compareFn(a, b);

_comareFn((a, b) {
   if(this.x ...) {
     ...
}
```

[**Source**](https://stackoverflow.com/questions/35945001)  
**[Top](#599b)**

### What is difference between declarations, providers and import in NgModule

> 188+ points _? 5_5,432+ viewed   
> _[**Ramesh Papaganti**](https://stackoverflow.com/users/2822252/ramesh-papaganti) **asked,**_

I am trying to understand Angular (sometimes called Angular2+), then I came across @Module

1. Imports
2. Declarations
3. Providers

Following [Angularjs-2 quick start](https://angular.io/guide/quickstart)

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_answered, (277+ points)_**

**Angular Concepts**

* `imports` makes the exported declarations of other modules available in the current module
* `declarations` are to make directives (including components and pipes) from the current module available to other directives in the current module. Selectors of directives, components or pipes are only matched against the HTML if they are declared or imported.
* `providers` are to make services and values known to DI. They are added to the root scope and they are injected to other services or directives that have them as dependency.

A special case for `providers` are lazy loaded modules that get their own child injector. `providers` of a lazy loaded module are only provided to this lazy loaded module by default (not the whole application as it is with other modules).

For more details about modules see also [https://angular.io/docs/ts/latest/guide/ngmodule.html](https://angular.io/docs/ts/latest/guide/ngmodule.html)

* `exports` makes the components, directives, and pipes available in modules that add this module to `imports`. `exports` can also be used to re-export modules such as CommonModule and FormsModule, which is often done in shared modules.
* `entryComponents` registers components for offline compilation so that they can be used with `ViewContainerRef.createComponent()`. Components used in router configurations are added implicitly.

**TypeScript (ES2015) imports**

`import ... from 'foo/bar'` (which [may resolve to an `index.ts`](https://stackoverflow.com/a/38158884/1175496)) are for TypeScript imports. You need these whenever you use an identifier in a typescript file that is declared in another typescript file.

Angular’s `@NgModule()` `imports` and TypeScript `import` are _entirely different concepts_.

See also [jDriven — TypeScript and ES6 import syntax](https://blog.jdriven.com/2017/06/typescript-and-es6-import-syntax/)

`Most of them are actually plain ECMAScript 2015 (ES6) module syntax that TypeScript uses as well.`

[**Source**](https://stackoverflow.com/questions/39062930)  
**[Top](#599b)**

### In Angular, how do you determine the active route?

> 187+ points _? 1_00,870+ viewed   
> _[**Michael Oryl**](https://stackoverflow.com/users/1480995/michael-oryl) **asked,**_

**NOTE:** _There are many different answers here, and most have been valid at one time or another. The fact is that what works has changed a number of times as the Angular team has changed its Router. The Router 3.0 version that will eventually be **the** router in Angular breaks many of these solutions, but offers a very simple solution of its own. As of RC.3, the preferred solution is to use `[routerLinkActive]` as shown in [this answer](https://stackoverflow.com/a/37947435/1480995)._

In an Angular application (current in the 2.0.0-beta.0 release as I write this), how do you determine what the currently active route is?

I’m working on an app that uses Bootstrap 4 and I need a way to mark navigation links/buttons as active when their associated component is being shown in a `<router-outp`ut> tag.

I realize that I could maintain the state myself when one of the buttons is clicked upon, but that wouldn’t cover the case of having multiple paths into the same route (say a main navigation menu as well as a local menu in the main component).

Any suggestions or links would be appreciated. Thanks.

> [**_jessepinho_**](https://stackoverflow.com/users/974981) **_answered, (229+ points)_**

With the new [Angular router](https://github.com/angular/vladivostok), you can add a `[routerLinkActive]="['your-class-name']"` attribute to all your links:

```
<a [routerLink]="['/home']" [routerLinkActive]="['is-active']">Home</a>
```

Or the simplified non-array format if only one class is needed:

```
<a [routerLink]="['/home']" [routerLinkActive]="'is-active'">Home</a>
```

See the [poorly documented `routerLinkActive` directive](https://github.com/angular/angular/blob/ae75e3640a2d9eb1e897a0771d92b976c5a42c75/modules/%40angular/router/src/directives/router_link_active.ts) for more info. (I mostly figured this out via trial-and-error.)

UPDATE: Better documentation for the `routerLinkActive` directive can now be found [here](https://angular.io/docs/ts/latest/api/router/index/RouterLinkActive-directive.html). (Thanks to @Victor Hugo Arango A. in the comments below.)

[**Source**](https://stackoverflow.com/questions/34323480)  
**[Top](#599b)**

### Angular CLI SASS options

> 187+ points _? 1_06,289+ viewed   
> _[**JDillon522**](https://stackoverflow.com/users/2109585/jdillon522) **asked,**_

I’m new to Angular and I’m coming from the Ember community. Trying to use the new Angular-CLI based off of Ember-CLI.

I need to know the best way to handle SASS in a new Angular project. I tried using the `[ember-cli-sass](https://github.com/aexmachina/ember-cli-sass)` repo to see if it would play along since a number of core components of the Angular-CLI are run off of Ember-CLI modules.

It didnt work but than again not sure if I just misconfigured something.

Also, what is the best way to organize styles in a new Angular project? It would be nice to have the sass file in the same folder as the component.

> [**_Mertcan Diken_**](https://stackoverflow.com/users/6265549) **_answered, (323+ points)_**

When you are creating your project with angular cli try this:

```bash
ng new My_New_Project --style=sass
```

This generating all your components with predifined sass files.

If you want scss syntax create your project with :

```bash
ng new My_New_Project --style=scss
```

If you are changing your existing style in your project

```bash
ng set defaults.styleExt scss
```

Cli handles the rest of it.

[**Source**](https://stackoverflow.com/questions/36220256)  
**[Top](#599b)**

### Triggering change detection manually in Angular

> 186+ points _? 1_02,556+ viewed   
> _[**jz87**](https://stackoverflow.com/users/515279/jz87) **asked,**_

I’m writing an Angular component that has a property `Mode(): string`. I would like to be able to set this property programmatically not in response to any event. The problem is that in the absence of a browser event, a template binding `{{Mode}}` doesn't update. Is there a way to trigger this change detection manually?

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_answered, (345+ points)_**

Try one of these:

* `[ApplicationRef.tick()](https://angular.io/docs/ts/latest/api/core/index/ApplicationRef-class.html#!#tick-anchor)` - similar to AngularJS's `$rootScope.$digest()` -- i.e., check the full component tree
* `[NgZone.run(callback)](https://angular.io/docs/ts/latest/api/core/index/NgZone-class.html#!#run-anchor)` - similar to `$rootScope.$apply(callback)` -- i.e., evaluate the callback function inside the Angular zone. I think, but I'm not sure, that this ends up checking the full component tree after executing the callback function.
* `[ChangeDetectorRef.detectChanges()](https://angular.io/docs/ts/latest/api/core/index/ChangeDetectorRef-class.html#!#detectChanges-anchor)` - similar to `$scope.$digest()` -- i.e., check only this component and its children

You can inject `ApplicationRef`, `NgZone`, or `ChangeDetectorRef` into your component.

[**Source**](https://stackoverflow.com/questions/34827334)  
**[Top](#599b)**

### Angular and Typescript: Can’t find names

> 184+ points _? 1_81,472+ viewed   
> _[**user233232**](https://stackoverflow.com/users/4997649/user233232) **asked,**_

I am using Angular (version 2) with TypeScript (version 1.6) and when I compile the code I get these errors:

```bash
Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/change_detection/parser/locals.d.ts(4,42): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(1,25): Error TS2304: Cannot find name 'MapConstructor'.
    node_modules/angular2/src/core/facade/collection.d.ts(2,25): Error TS2304: Cannot find name 'SetConstructor'.
    node_modules/angular2/src/core/facade/collection.d.ts(4,27): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(4,39): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(7,9): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(8,30): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(11,43): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(12,27): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(14,23): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(15,25): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(94,41): Error TS2304: Cannot find name 'Set'.
    node_modules/angular2/src/core/facade/collection.d.ts(95,22): Error TS2304: Cannot find name 'Set'.
    node_modules/angular2/src/core/facade/collection.d.ts(96,25): Error TS2304: Cannot find name 'Set'.
    node_modules/angular2/src/core/facade/lang.d.ts(1,22): Error TS2304: Cannot find name 'BrowserNodeGlobal'.
    node_modules/angular2/src/core/facade/lang.d.ts(33,59): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/promise.d.ts(1,10): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(3,14): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(8,32): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(9,38): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(10,35): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(10,93): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(11,34): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(12,32): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(12,149): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(13,43): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(72,32): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(74,17): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(78,184): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(83,182): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(107,37): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/proto_view_factory.d.ts(27,146): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(52,144): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(76,79): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(77,73): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(94,31): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(97,18): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(100,24): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(103,142): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(104,160): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/render/api.d.ts(281,74): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/zone/ng_zone.d.ts(1,37): Error TS2304: Cannot find name 'Zone'.
```

This is the code:

```ts
import 'reflect-metadata';
import {bootstrap, Component, CORE_DIRECTIVES, FORM_DIRECTIVES} from 'angular2/core';
@Component({
  selector: 'my-app',
  template: '<input type="text" [(ng-model)]="title" /><h1>{{title}}</h1>',
  directives: [ CORE_DIRECTIVES ]
})
class AppComponent {
  title :string;
  
  constructor() {
    this.title = 'hello angular 2';
  }
}
bootstrap(AppComponent);
```

> [**_basarat_**](https://stackoverflow.com/users/390330) **_answered, (50+ points)_**

A known issue: [https://github.com/angular/angular/issues/4902](https://github.com/angular/angular/issues/4902)

Core reason: the `.d.ts` file implicitly included by TypeScript varies with the compile target, so one needs to have more ambient declarations when targeting `es5` even if things are actually present in the runtimes (e.g. chrome). More on `[lib.d.ts](https://basarat.gitbooks.io/typescript/content/docs/types/lib.d.ts.html)`

[**Source**](https://stackoverflow.com/questions/33332394)  
**[Top](#599b)**

### Angular — What is the meanings of module.id in component?

> 181+ points _? 5_4,337+ viewed   
> _[**Nishchit Dhanani**](https://stackoverflow.com/users/2837412/nishchit-dhanani) **asked,**_

In an Angular app, I have seen that `@Component` has property `moduleId`. What does it mean?

And when `module.id` is not defined anywhere, the app still works. How can it still work?

```ts
@Component({
  moduleId: module.id,
  selector: 'ng-app',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.css'],
  directives: [AppComponent]
});
```

> [**_Nishchit Dhanani_**](https://stackoverflow.com/users/2837412) **_answered, (145+ points)_**

The beta release of Angular (since vesion 2-alpha.51) supports relative assets for components, like **templateUrl** and **styleUrls** in the `@Component` decorator.

`module.id` works when using CommonJS. You don't need to worry about how it works.

`**Remember**: setting moduleId: module.id in the @Component decorator is the key here. If you don't have that then Angular 2 will be looking for your files at the root level.`

Source from [Justin Schwartzenberger’s post](http://schwarty.com/2015/12/22/angular2-relative-paths-for-templateurl-and-styleurls/), thanks to [@Pradeep Jain](https://stackoverflow.com/users/5043867/pardeep-jain)

**Update on 16 Sep 2016:**

`If you are using **webpack** for bundling then you don't need module.id in decorator. Webpack plugins auto handle (add it) module.id in final bundle`

[**Source**](https://stackoverflow.com/questions/37178192)  
**[Top](#599b)**

### How can I get new selection in “select” in Angular 2?

> 175+ points _? 2_03,064+ viewed   
> _[**Hongbo Miao**](https://stackoverflow.com/users/2000548/hongbo-miao) **asked,**_

I am using Angular 2 (TypeScript).

I want to do something for new selection, but what I got in onChange() is always last selection. How can I get new selection?

```ts
<select [(ngModel)]="selectedDevice" (change)="onChange($event)">
    <option *ngFor="#i of devices">{{i}}</option>
</select>

onChange($event) {
    console.log(this.selectedDevice);
    // I want to do something here for new selectedDevice, but what I
    // got here is always last selection, not the one I just select.
}
```

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_answered, (370+ points)_**

If you don’t need two-way data-binding:

```ts
<select (change)="onChange($event.target.value)">
    <option *ngFor="let i of devices">{{i}}</option>
</select>

onChange(deviceValue) {
    console.log(deviceValue);
}
```

For two-way data-binding, separate the event and property bindings:

```ts
<select [ngModel]="selectedDevice" (ngModelChange)="onChange($event)" name="sel2">
    <option [value]="i" *ngFor="let i of devices">{{i}}</option>
</select>

export class AppComponent {
  devices = 'one two three'.split(' ');
  selectedDevice = 'two';
  onChange(newValue) {
    console.log(newValue);
    this.selectedDevice = newValue;
    // ... do other stuff here ...
}
```

If `devices` is array of objects, bind to `ngValue` instead of `value`:

```ts
<select [ngModel]="selectedDeviceObj" (ngModelChange)="onChangeObj($event)" name="sel3">
  <option [ngValue]="i" *ngFor="let i of deviceObjects">{{i.name}}</option>
</select>
{{selectedDeviceObj | json}}

export class AppComponent {
  deviceObjects = [{name: 1}, {name: 2}, {name: 3}];
  selectedDeviceObj = this.deviceObjects[1];
  onChangeObj(newObj) {
    console.log(newObj);
    this.selectedDeviceObj = newObj;
    // ... do other stuff here ...
  }
}
```

[Plunker](http://plnkr.co/edit/VbJUBkqAlS8UPVgh4bqV?p=preview) — does not use `<form>`  
[Plunker](http://plnkr.co/edit/pv5j4b1NFyTGFkxHUSga?p=preview) - uses `<form>` and uses the new forms API

[**Source**](https://stackoverflow.com/questions/33700266)  
**[Top](#599b)**

### Angular exception: Can’t bind to ‘ngForIn’ since it isn’t a known native property

> 172+ points _? 4_8,252+ viewed   
> _[**Mark Rajcok**](https://stackoverflow.com/users/215945/mark-rajcok) **asked,**_

What am I doing wrong?

```ts
import {bootstrap, Component} from 'angular2/angular2'

@Component({
  selector: 'conf-talks',
  template: `<div *ngFor="let talk in talks">
     {{talk.title}} by {{talk.speaker}}
     <p>{{talk.description}}
   </div>`
})
class ConfTalks {
  talks = [ {title: 't1', speaker: 'Brian', description: 'talk 1'},
            {title: 't2', speaker: 'Julie', description: 'talk 2'}];
}
@Component({
  selector: 'my-app',
  directives: [ConfTalks],
  template: '<conf-talks></conf-talks>'
})
class App {}
bootstrap(App, [])
```

The error is

```bash
EXCEPTION: Template parse errors:
Can't bind to 'ngForIn' since it isn't a known native property
("<div [ERROR ->]*ngFor="let talk in talks">
```

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_answered, (403+ points)_**

Since this is at least the third time I’ve wasted more than 5 min on this problem I figured I’d post the Q & A. I hope it helps someone else down the road… probably me!

I typed `in` instead of `of` in the ngFor expression.

**Befor 2-beta.17**, it should be:

```
<div *ngFor="#talk of talks">
```

_As of beta.17, use the `let` syntax instead of `#`. See the UPDATE further down for more info._

Note that the ngFor syntax “desugars” into the following:

```ts
<template ngFor #talk [ngForOf]="talks">
  <div>...</div>
</template>
```

If we use `in` instead, it turns into

```ts
<template ngFor #talk [ngForIn]="talks">
  <div>...</div>
</template>
```

Since `ngForIn` isn't an attribute directive with an input property of the same name (like `ngIf`), Angular then tries to see if it is a (known native) property of the `template` element, and it isn't, hence the error.

**UPDATE** — as of 2-beta.17, use the `let` syntax instead of `#`. This updates to the following:

```
<div *ngFor="let talk of talks">
```

Note that the ngFor syntax “desugars” into the following:

```ts
<template ngFor let-talk [ngForOf]="talks">
  <div>...</div>
</template>
```

If we use `in` instead, it turns into

```ts
<template ngFor let-talk [ngForIn]="talks">
  <div>...</div>
</template>
```

[**Source**](https://stackoverflow.com/questions/34561168)  
**[Top](#599b)**

### *ngIf and *ngFor on same element causing error

> 171+ points _? 8_5,728+ viewed   
> _**[garethdn](https://stackoverflow.com/users/1128290/garethdn) asked,**_

I’m having a problem with trying to use Angular’s `*ngFor` and `*ngIf` on the same element.

When trying to loop through the collection in the `*ngFor`, the collection is seen as `null` and consequently fails when trying to access its properties in the template.

```ts
@Component({
  selector: 'shell',
  template: `
    <h3>Shell</h3><button (click)="toggle()">Toggle!</button>
    
    <div *ngIf="show" *ngFor="let thing of stuff">
      {{log(thing)}}
      <span>{{thing.name}}</span>
    </div>
  `
})

export class ShellComponent implements OnInit {

  public stuff:any[] = [];
  public show:boolean = false;
  
  constructor() {}
  
  ngOnInit() {
    this.stuff = [
      { name: 'abc', id: 1 },
      { name: 'huo', id: 2 },
      { name: 'bar', id: 3 },
      { name: 'foo', id: 4 },
      { name: 'thing', id: 5 },
      { name: 'other', id: 6 },
    ]
  }
  
  toggle() {
    this.show = !this.show;
  }
  
  log(thing) {
    console.log(thing);
  }
  
}
```

I know the easy solution is to move the `*ngIf` up a level but for scenarios like looping over list items in a `ul`, I'd end up with either an empty `li` if the collection is empty, or my `li`s wrapped in redundant container elements.

Example at this [plnkr](http://plnkr.co/edit/C5tZ8mD3iWczVvWkWycH?p=preview).

Note the console error:

`EXCEPTION: TypeError: Cannot read property 'name' of null in [{{thing.name}} in ShellComponent@5:12]`

Am I doing something wrong or is this a bug?

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_answered, (284+ points)_**

Angular2 doesn’t support more than one structural directive on the same element.  
As a workaround use the `**<ng-container>**` element that allows you to use separate elements for each structural directive, but **it is not stamped to the DOM**.

```ts
<ng-container *ngIf="show">
  <div *ngFor="let thing of stuff">
    {{log(thing)}}
    <span>{{thing.name}}</span>
  </div>
</ng-container>
```

`<ng-template>` (`<template>` before Angular4) allows to do the same but with a different syntax which is confusing and no longer recommended

```ts
<ng-template [ngIf]="show">
  <div *ngFor="let thing of stuff">
    {{log(thing)}}
    <span>{{thing.name}}</span>
  </div>
</ng-template>
```

[**Source**](https://stackoverflow.com/questions/34657821)  
**[Top](#599b)**

### What is the Angular equivalent to an AngularJS $watch?

> 169+ points _? 9_5,029+ viewed   
> _[**Erwin**](https://stackoverflow.com/users/1716567/erwin) **asked,**_

In AngularJS you were able to specify watchers to observe changes in scope variables using the `$watch` function of the `$scope`. What is the equivalent of watching for variable changes (in, for example, component variables) in Angular?

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_answered, (226+ points)_**

In Angular 2, change detection is automatic… `$scope.$watch()` and `$scope.$digest()` R.I.P.

Unfortunately, the Change Detection section of the dev guide is not written yet (there is a placeholder near the bottom of the [Architecture Overview](https://angular.io/docs/ts/latest/guide/architecture.html) page, in section “The Other Stuff”).

Here’s my understanding of how change detection works:

* Zone.js “monkey patches the world” — it intercepts all of the asynchronous APIs in the browser (when Angular runs). This is why we can use `setTimeout()` inside our components rather than something like `$timeout`... because `setTimeout()` is monkey patched.
* Angular builds and maintains a tree of “change detectors”. There is one such change detector (class) per component/directive. (You can get access to this object by injecting `[ChangeDetectorRef](https://angular.io/docs/ts/latest/api/core/index/ChangeDetectorRef-class.html)`.) These change detectors are created when Angular creates components. They keep track of the state of all of your bindings, for dirty checking. These are, in a sense, similar to the automatic `$watches()` that Angular 1 would set up for `{{}}` template bindings.  
Unlike Angular 1, the change detection graph is a directed tree and cannot have cycles (this makes Angular 2 much more performant, as we'll see below).
* When an event fires (inside the Angular zone), the code we wrote (the event handler callback) runs. It can update whatever data it wants to — the shared application model/state and/or the component’s view state.
* After that, because of the hooks Zone.js added, it then runs Angular’s change detection algorithm. By default (i.e., if you are not using the `onPush` change detection strategy on any of your components), every component in the tree is examined once (TTL=1)... from the top, in depth-first order. (Well, if you're in dev mode, change detection runs twice (TTL=2). See [ApplicationRef.tick()](https://angular.io/docs/ts/latest/api/core/index/ApplicationRef-class.html#!#tick-anchor) for more about this.) It performs dirty checking on all of your bindings, using those change detector objects.
* Lifecycle hooks are called as part of change detection.   
If the component data you want to watch is a primitive input property (String, boolean, number), you can implement `ngOnChanges()` to be notified of changes.   
If the input property is a reference type (object, array, etc.), but the reference didn't change (e.g., you added an item to an existing array), you'll need to implement `ngDoCheck()` (see [this SO answer](https://stackoverflow.com/a/34298708/215945) for more on this).   
You should only change the component's properties and/or properties of descendant components (because of the single tree walk implementation -- i.e., unidirectional data flow). Here's [a plunker](http://plnkr.co/edit/XWBSvE0NoQlRuOsXuOm0?p=preview) that violates that. Stateful pipes can also [trip you up](https://stackoverflow.com/questions/34456430/ngfor-doesnt-update-data-with-pipe-in-angular2/34497504#34497504) here.
* For any binding changes that are found, the Components are updated, and then the DOM is updated. Change detection is now finished.
* The browser notices the DOM changes and updates the screen.

Other references to learn more:

* [Angular’s $digest is reborn in the newer version of Angular](https://blog.angularindepth.com/angulars-digest-is-reborn-in-the-newer-version-of-angular-718a961ebd3e) — explains how the ideas from AngularJS are mapped to Angular
* [Everything you need to know about change detection in Angular](https://blog.angularindepth.com/everything-you-need-to-know-about-change-detection-in-angular-8006c51d206f) — explains in great detail how change detection works under the hood
* [Change Detection Explained](http://blog.thoughtram.io/angular/2016/02/22/angular-2-change-detection-explained.html) — Thoughtram blog Feb 22, 2016 — probably the best reference out there
* Savkin’s [Change Detection Reinvented](https://www.youtube.com/watch?v=jvKGQSFQf10) video — definitely watch this one
* [How does Angular 2 Change Detection Really Work?](http://blog.jhades.org/how-does-angular-2-change-detection-really-work/)- jhade’s blog Feb 24, 2016
* [Brian’s video](https://www.youtube.com/watch?v=3IqtmUscE_U) and [Miško’s video](https://www.youtube.com/watch?v=V9Bbp6Hh2YE) about Zone.js. Brian’s is about Zone.js. Miško’s is about how Angular 2 uses Zone.js to implement change detection. He also talks about change detection in general, and a little bit about `onPush`.
* Victor Savkins blog posts: [Change Detection in Angular 2](http://victorsavkin.com/post/110170125256/change-detection-in-angular-2), [Two phases of Angular 2 applications](http://victorsavkin.com/post/114168430846/two-phases-of-angular-2-applications), [Angular, Immutability and Encapsulation](http://victorsavkin.com/post/110170125256/change-detection-in-angular-2). He covers a lot of ground quickly, but he can be terse at times, and you’re left scratching your head, wondering about the missing pieces.
* [Ultra Fast Change Detection](https://docs.google.com/document/d/1QKTbyVNPyRW-otJJVauON4TFMHpl0zNBPkJcTcfPJWg/edit) (Google doc) — very technical, very terse, but it describes/sketches the ChangeDetection classes that get built as part of the tree

[**Source**](https://stackoverflow.com/questions/34569094)  
**[Top](#599b)**

### Importing lodash into angular2 + typescript application

> 167+ points _? 1_04,431+ viewed   
> _[**Davy**](https://stackoverflow.com/users/1854793/davy) **asked,**_

I am having a hard time trying to get the lodash modules imported. I’ve setup my project using npm+gulp, and keep hitting the same wall. I’ve tried the regular lodash, but also lodash-es.

The lodash npm package: (has an index.js file in the package root folder)

```ts
import * as _ from 'lodash';
```

Results in:

```
error TS2307: Cannot find module 'lodash'.
```

The lodash-es npm package: (has a defaut export in lodash.js i the package root folder)

```
import * as _ from 'lodash-es/lodash';
```

Results in:

```
error TS2307: Cannot find module 'lodash-es'.
```

Both the gulp task and webstorm report the same issue.

Funny fact, this returns no error:

```ts
import 'lodash-es/lodash';
```

… but of course there is no “_” …

My tsconfig.json file:

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "system",
    "moduleResolution": "node",
    "sourceMap": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "removeComments": false,
    "noImplicitAny": false
  },
  "exclude": [
    "node_modules"
  ]
}
```

My gulpfile.js:

```json
var gulp = require('gulp'),
    ts = require('gulp-typescript'),
    uglify = require('gulp-uglify'),
    sourcemaps = require('gulp-sourcemaps'),
    tsPath = 'app/**/*.ts';
    
gulp.task('ts', function () {
    var tscConfig = require('./tsconfig.json');
    
    gulp.src([tsPath])
        .pipe(sourcemaps.init())
        .pipe(ts(tscConfig.compilerOptions))
        .pipe(sourcemaps.write('./../js'));
});

gulp.task('watch', function() {
    gulp.watch([tsPath], ['ts']);
});

gulp.task('default', ['ts', 'watch']);
```

If i understand correctly, moduleResolution:’node’ in my tsconfig should point the import statements to the node_modules folder, where lodash and lodash-es are installed. I’ve also tried lots of different ways to import: absolute paths, relative paths, but nothing seems to work. Any ideas?

If necessary i can provide a small zip file to illustrate the problem.

> [**_Taytay_**](https://stackoverflow.com/users/544130) **_answered, (293+ points)_**

Here is how to do this as of Typescript 2.0: (tsd and typings are being deprecated in favor of the following):

```bash
$ npm install --save lodash

# This is the new bit here: 
$ npm install --save @types/lodash
```

Then, in your .ts file:

Either:

```ts
import * as _ from "lodash";
```

Or (as suggested by @Naitik):

```ts
import _ from "lodash";
```

I’m not positive what the difference is. We use and prefer the first syntax. However, some report that the first syntax doesn’t work for them, and someone else has commented that the latter syntax is incompatible with lazy loaded webpack modules. YMMV.

Edit on Feb 27th, 2017:

According to @Koert below, `import * as _ from "lodash";` is the only working syntax as of Typescript 2.2.1, lodash 4.17.4, and @types/lodash 4.14.53. He says that the other suggested import syntax gives the error "has no default export".

[**Source**](https://stackoverflow.com/questions/34660265)  
**[Top](#599b)**

### How to detect a route change in Angular?

> 160+ points _? 1_08,593+ viewed   
> _[**AngularM**](https://stackoverflow.com/users/1590389/angularm) **asked,**_

I am looking to detect a route change in my `AppComponent`.

Thereafter I will check the global user token to see if he is logged in. Then I can redirect the user if he is not logged in.

> [**_Ludohen_**](https://stackoverflow.com/users/1048274) **_answered, (223+ points)_**

In Angular 2 you can `subscribe` (Rx event) to a Router instance. So you can do things like

```ts
class MyClass {
  constructor(private router: Router) {
    router.subscribe((val) => /*whatever*/)
  }
}
```

**Edit** (since rc.1)

```ts
class MyClass {
  constructor(private router: Router) {
    router.changes.subscribe((val) => /*whatever*/)
  }
}
```

**Edit 2** (since 2.0.0)

see also : [Router.events doc](https://angular.io/api/router/RouterEvent)

```ts
class MyClass {
  constructor(private router: Router) {
    router.events.subscribe((val) => {
        // see also 
        console.log(val instanceof NavigationEnd) 
    });
  }
}
```

[**Source**](https://stackoverflow.com/questions/33520043)  
**[Top](#599b)**

### Global Events in Angular

> 157+ points _? 8_3,980+ viewed   
> _[**skovmand**](https://stackoverflow.com/users/3368477/skovmand) **asked,**_

Is there no equivalent to `$scope.emit()` or `$scope.broadcast()` in Angular?

I know the `EventEmitter` functionality, but as far as I understand that will just emit an event to the parent HTML element.

What if I need to communicate between fx. siblings or between a component in the root of the DOM and an element nested several levels deep?

> [**_pixelbits_**](https://stackoverflow.com/users/3661630) **_answered, (304+ points)_**

There is no equivalent to `$scope.emit()` or `$scope.broadcast()` from AngularJS. EventEmitter inside of a component comes close, but as you mentioned, it will only emit an event to the immediate parent component.

In Angular, there are other alternatives which I’ll try to explain below.

@Input() bindings allows the application model to be connected in a directed object graph (root to leaves). The default behavior of a component’s change detector strategy is to propagate all changes to an application model for all bindings from any connected component.

Aside: There are two types of models: View Models and Application Models. An application model is connected through @Input() bindings. A view model is a just a component property (not decorated with @Input()) which is bound in the component’s template.

To answer your questions:

What if I need to communicate between sibling components?

1. **Shared Application Model**: Siblings can communicate through a shared application model (just like angular 1). For example, when one sibling makes a change to a model, the other sibling that has bindings to the same model is automatically updated.
2. **Component Events**: Child components can emit an event to the parent component using @Output() bindings. The parent component can handle the event, and manipulate the application model or it’s own view model. Changes to the Application Model are automatically propagated to all components that directly or indirectly bind to the same model.
3. **Service Events**: Components can subscribe to service events. For example, two sibling components can subscribe to the same service event and respond by modifying their respective models. More on this below.

How can I communicate between a Root component and a component nested several levels deep?

1. **Shared Application Model**: The application model can be passed from the Root component down to deeply nested sub-components through @Input() bindings. Changes to a model from any component will automatically propagate to all components that share the same model.
2. **Service Events**: You can also move the EventEmitter to a shared service, which allows any component to inject the service and subscribe to the event. That way, a Root component can call a service method (typically mutating the model), which in turn emits an event. Several layers down, a grand-child component which has also injected the service and subscribed to the same event, can handle it. Any event handler that changes a shared Application Model, will automatically propagate to all components that depend on it. This is probably the closest equivalent to `$scope.broadcast()` from Angular 1. The next section describes this idea in more detail.

**Example of an Observable Service that uses Service Events to Propagate Changes**

Here is an example of an observable service that uses service events to propagate changes. When a TodoItem is added, the service emits an event notifying its component subscribers.

```ts
export class TodoItem {
    constructor(public name: string, public done: boolean) {
    }
}
export class TodoService {
    public itemAdded$: EventEmitter<TodoItem>;
    private todoList: TodoItem[] = [];
    
    constructor() {
        this.itemAdded$ = new EventEmitter();
    }
    
    public list(): TodoItem[] {
        return this.todoList;
    }
    
    public add(item: TodoItem): void {
        this.todoList.push(item);
        this.itemAdded$.emit(item);
    }
}
```

Here is how a root component would subscribe to the event:

```ts
export class RootComponent {
    private addedItem: TodoItem;
    constructor(todoService: TodoService) {
        todoService.itemAdded$.subscribe(item => this.onItemAdded(item));
    }
    
    private onItemAdded(item: TodoItem): void {
        // do something with added item
        this.addedItem = item;
    }
}
```

A child component nested several levels deep would subscribe to the event in the same way:

```ts
export class GrandChildComponent {
    private addedItem: TodoItem;
    constructor(todoService: TodoService) {
        todoService.itemAdded$.subscribe(item => this.onItemAdded(item));
    }
    
    private onItemAdded(item: TodoItem): void {
        // do something with added item
        this.addedItem = item;
    }
}
```

Here is the component that calls the service to trigger the event (it can reside anywhere in the component tree):

```ts
@Component({
    selector: 'todo-list',
    template: `
         <ul>
            <li *ngFor="#item of model"> {{ item.name }}
            </li>
         </ul>
        <br />
        Add Item <input type="text" #txt /> <button (click)="add(txt.value); txt.value='';">Add</button>
    `
})
export class TriggeringComponent{
    private model: TodoItem[];
    
    constructor(private todoService: TodoService) {
        this.model = todoService.list();
    }
    
    add(value: string) {
        this.todoService.add(new TodoItem(value, false));
    }
}
```

Reference: [Change Detection in Angular](http://victorsavkin.com/post/110170125256/change-detection-in-angular-2)

[**Source**](https://stackoverflow.com/questions/34700438)  
**[Top](#599b)**

### What are differences between SystemJS and Webpack?

> 155+ points _? 6_0,183+ viewed   
> _[**smartmouse**](https://stackoverflow.com/users/2516399/smartmouse) **asked,**_

I’m creating my first Angular application and I would figure out what is the role of the module loaders. Why we need them? I tried to search and search on Google and I can’t understand why we need to install one of them to run our application?

Couldn’t it be enough to just use `import` to load stuff from node modules?

I have followed [this tutorial](https://angular.io/docs/ts/latest/quickstart.html#!#systemjs) (that uses SystemJS) and it makes me to use `systemjs.config.js` file:

```js
/**
 * System configuration for Angular samples
 * Adjust as necessary for your application needs.
 */
(function(global) {
  // map tells the System loader where to look for things
  var map = {
    'app':                        'transpiled', // 'dist',
    '@angular':                   'node_modules/@angular',
    'angular2-in-memory-web-api': 'node_modules/angular2-in-memory-web-api',
    'rxjs':                       'node_modules/rxjs'
  };
  // packages tells the System loader how to load when no filename and/or no extension
  var packages = {
    'app':                        { main: 'main.js',  defaultExtension: 'js' },
    'rxjs':                       { defaultExtension: 'js' },
    'angular2-in-memory-web-api': { main: 'index.js', defaultExtension: 'js' },
  };
  var ngPackageNames = [
    'common',
    'compiler',
    'core',
    'forms',
    'http',
    'platform-browser',
    'platform-browser-dynamic',
    'router',
    'router-deprecated',
    'upgrade',
  ];
  // Individual files (~300 requests):
  function packIndex(pkgName) {
    packages['@angular/'+pkgName] = { main: 'index.js', defaultExtension: 'js' };
  }
  // Bundled (~40 requests):
  function packUmd(pkgName) {
    packages['@angular/'+pkgName] = { main: '/bundles/' + pkgName + '.umd.js', defaultExtension: 'js' };
  }
  // Most environments should use UMD; some (Karma) need the individual index files
  var setPackageConfig = System.packageWithIndex ? packIndex : packUmd;
  // Add package entries for angular packages
  ngPackageNames.forEach(setPackageConfig);
  var config = {
    map: map,
    packages: packages
  };
  System.config(config);
})(this);
```

Why we need this configuration file?  
Why we need SystemJS (or WebPack or others)?  
Finally, in your opinion what is the better?

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_answered, (97+ points)_**

If you go to the SystemJS Github page, you will see the description of the tool:

`Universal dynamic module loader - loads ES6 modules, AMD, CommonJS and global scripts in the browser and NodeJS.`

Because you use modules in TypeScript or ES6, you need a module loader. In the case of SystemJS, the `systemjs.config.js` allows us to configure the way in which module names are matched with their corresponding files.

This configuration file (and SystemJS) is necessary if you explicitly use it to import the main module of your application:

```html
<script>
  System.import('app').catch(function(err){ console.error(err); });
</script>
```

When using TypeScript, and configuring the compiler to the `commonjs` module, the compiler creates code that is no longer based on SystemJS. In this example, the typescript compiler config file would appear like this:

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs", // <------
    "moduleResolution": "node",
    "sourceMap": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "removeComments": false,
    "noImplicitAny": false
  }
}
```

Webpack is a flexible module bundler. This means that it goes further and doesn’t only handle modules but also provides a way to package your application (concat files, uglify files, …). It also provides a dev server with load reload for development

SystemJS and Webpack are different but with SystemJS, you still have work to do (with [Gulp](http://gulpjs.com/) or [SystemJS builder](https://github.com/systemjs/builder) for example) to package your Angular2 application for production.

[**Source**](https://stackoverflow.com/questions/38263406)  
**[Top](#599b)**

### Angular: Can’t find Promise, Map, Set and Iterator

> 154+ points _? 9_0,201+ viewed   
> _[**Stav Alfi**](https://stackoverflow.com/users/806963/stav-alfi) **asked,**_

After installing Angular, the Typescript compiler keep getting some errors about not finding `Promise`, `Map`, `Set` and `Iterator`.

Until now I ignored them but now I need `Promise` so my code can work.

```ts
import {Component} from 'angular2/core';
@Component({
    selector: 'greeting-cmp',
    template: `<div>{{ asyncGreeting | async}}</div>`
})
export class GreetingCmp {
    asyncGreeting: Promise<string> = new Promise(resolve => {
// after 1 second, the promise will resolve
        window.setTimeout(() => resolve('hello'), 1000);
    });
}

Additional information:
npm -v is 2.14.12
node -v is v4.3.1
typescript v is 1.6
```

**The errors:**

```bash
................ERROS OF MY CODE.................
    C:\Users\armyTik\Desktop\angular2\greeting_cmp.ts
    Error:(7, 20) TS2304: Cannot find name 'Promise'.
    Error:(7, 42) TS2304: Cannot find name 'Promise'.
    .........................................
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\platform\browser.d.ts
    Error:(77, 90) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\application_ref.d.ts
    Error:(83, 60) TS2304: Cannot find name 'Promise'.
    Error:(83, 146) TS2304: Cannot find name 'Promise'.
    Error:(96, 51) TS2304: Cannot find name 'Promise'.
    Error:(96, 147) TS2304: Cannot find name 'Promise'.
    Error:(133, 90) TS2304: Cannot find name 'Promise'.
    Error:(171, 81) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\change_detection\parser\locals.d.ts
    Error:(3, 14) TS2304: Cannot find name 'Map'.
    Error:(4, 42) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\debug\debug_node.d.ts
    Error:(14, 13) TS2304: Cannot find name 'Map'.
    Error:(24, 17) TS2304: Cannot find name 'Map'.
    Error:(25, 17) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\di\provider.d.ts
    Error:(436, 103) TS2304: Cannot find name 'Map'.
    Error:(436, 135) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\linker\compiler.d.ts
    Error:(12, 50) TS2304: Cannot find name 'Promise'.
    Error:(16, 41) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\linker\dynamic_component_loader.d.ts
    Error:(108, 136) TS2304: Cannot find name 'Promise'.
    Error:(156, 150) TS2304: Cannot find name 'Promise'.
    Error:(197, 128) TS2304: Cannot find name 'Promise'.
    Error:(203, 127) TS2304: Cannot find name 'Promise'.
    Error:(204, 141) TS2304: Cannot find name 'Promise'.
    Error:(205, 119) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\render\api.d.ts
    Error:(13, 13) TS2304: Cannot find name 'Map'.
    Error:(14, 84) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\facade\async.d.ts
    Error:(27, 33) TS2304: Cannot find name 'Promise'.
    Error:(28, 45) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\facade\collection.d.ts
    Error:(1, 25) TS2304: Cannot find name 'MapConstructor'.
    Error:(2, 25) TS2304: Cannot find name 'SetConstructor'.
    Error:(4, 27) TS2304: Cannot find name 'Map'.
    Error:(4, 39) TS2304: Cannot find name 'Map'.
    Error:(7, 9) TS2304: Cannot find name 'Map'.
    Error:(8, 30) TS2304: Cannot find name 'Map'.
    Error:(11, 43) TS2304: Cannot find name 'Map'.
    Error:(12, 27) TS2304: Cannot find name 'Map'.
    Error:(14, 23) TS2304: Cannot find name 'Map'.
    Error:(15, 25) TS2304: Cannot find name 'Map'.
    Error:(95, 41) TS2304: Cannot find name 'Set'.
    Error:(96, 22) TS2304: Cannot find name 'Set'.
    Error:(97, 25) TS2304: Cannot find name 'Set'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\facade\lang.d.ts
    Error:(13, 17) TS2304: Cannot find name 'Map'.
    Error:(14, 17) TS2304: Cannot find name 'Set'.
    Error:(78, 59) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\facade\promise.d.ts
    Error:(2, 14) TS2304: Cannot find name 'Promise'.
    Error:(7, 32) TS2304: Cannot find name 'Promise'.
    Error:(8, 38) TS2304: Cannot find name 'Promise'.
    Error:(9, 35) TS2304: Cannot find name 'Promise'.
    Error:(9, 93) TS2304: Cannot find name 'Promise'.
    Error:(10, 34) TS2304: Cannot find name 'Promise'.
    Error:(11, 32) TS2304: Cannot find name 'Promise'.
    Error:(11, 149) TS2304: Cannot find name 'Promise'.
    Error:(12, 43) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\http\headers.d.ts
    Error:(43, 59) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\http\url_search_params.d.ts
    Error:(11, 16) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\platform\browser\browser_adapter.d.ts
    Error:(75, 33) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\platform\dom\dom_adapter.d.ts
    Error:(85, 42) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\CoreOperators.d.ts
    Error:(35, 67) TS2304: Cannot find name 'Promise'.
    Error:(50, 66) TS2304: Cannot find name 'Promise'.
    Error:(89, 67) TS2304: Cannot find name 'Promise'.
    Error:(94, 38) TS2304: Cannot find name 'Promise'.
    Error:(94, 50) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\Observable.d.ts
    Error:(46, 62) TS2304: Cannot find name 'Promise'.
    Error:(47, 42) TS2304: Cannot find name 'Iterator'.
    Error:(103, 74) TS2304: Cannot find name 'Promise'.
    Error:(103, 84) TS2304: Cannot find name 'Promise'.
    Error:(143, 66) TS2304: Cannot find name 'Promise'.
    Error:(158, 65) TS2304: Cannot find name 'Promise'.
    Error:(201, 66) TS2304: Cannot find name 'Promise'.
    Error:(206, 38) TS2304: Cannot find name 'Promise'.
    Error:(206, 50) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\observable\ForkJoinObservable.d.ts
    Error:(6, 50) TS2304: Cannot find name 'Promise'.
    Error:(7, 58) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\observable\FromObservable.d.ts
    Error:(7, 38) TS2304: Cannot find name 'Promise'.
    Error:(7, 51) TS2304: Cannot find name 'Iterator'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\observable\PromiseObservable.d.ts
    Error:(9, 31) TS2304: Cannot find name 'Promise'.
    Error:(10, 26) TS2304: Cannot find name 'Promise'.
```

> [**_Kris Hollenbeck_**](https://stackoverflow.com/users/1949099) **_answered, (162+ points)_**

#### Angular RC4 — Angular ^2.0.0 with Typescript 2.0.0

_Updated 9/19/2016_

To get this to work with typescript 2.0.0, I did the following.

`npm install --save-dev @types/core-js`

**tsconfig.json**

```json
"compilerOptions": {
    "declaration": false,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "mapRoot": "./",
    "module": "es6",
    "moduleResolution": "node",
    "noEmitOnError": true,
    "noImplicitAny": false,
    "outDir": "../dist/out-tsc",
    "sourceMap": true,
    "target": "es5",
    "typeRoots": [
      "../node_modules/@types"
    ],
    "types": [
      "core-js"
    ]
  }
```

**More about @types with typescript 2.0.0.**

1. [https://blogs.msdn.microsoft.com/typescript/2016/06/15/the-future-of-declaration-files/](https://blogs.msdn.microsoft.com/typescript/2016/06/15/the-future-of-declaration-files/)
2. [https://www.npmjs.com/~types](https://www.npmjs.com/~types)

Install Example:

```
npm install --save-dev @types/core-js
```

**Duplicate Identifier errors**

This is most likely because duplicate ecmascript 6 typings are already being imported from somewhere else most likely an old es6-shim.

Double check `typings.d.ts` make sure there are no references to `es6`. Remove any reference to `es6` from your typings directory if you have one.

**For Example:**

This will conflict with `types:['core-js']` in typings.json.

```json
{
  "globalDependencies": {
    "core-js": "registry:dt/core-js#0.0.0+20160602141332" 
    // es6-shim will also conflict
  }
}
```

Including `core-js` in the types array in `tsconfig.json` should be the only place it is imported from.

**Angular CLI 1.0.0-beta.30**

If you are using the Angular-CLI, remove the lib array in `typings.json`. This seems to conflict with declaring core-js in types.

```json
"compilerOptions" : {
  ...
  // removed "lib": ["es6", dom"],
  ...
},
"types" : ["core-js"]
```

**Webstorm/Intellij Users using the Angular CLI**

Make sure the built in typescript compiler is disabled. This will conflict with the CLI. To compile your typescript with the CLI you can setup a `ng serve` configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/YG2jiM4rYeIBDbXVSaDe3VOIdHlSAH1Z7hmN)

**Tsconfig compilerOptions lib vs types**

If you prefer not to install core js type definitions there are some es6 libraries that come included with typescript. Those are used via the `lib: []` property in tsconfig.

See here for example: [https://www.typescriptlang.org/docs/handbook/compiler-options.html](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

`Note: If --lib is not specified a default library is injected. The default library injected is: ? For --target ES5: DOM,ES5,ScriptHost ? For --target ES6: DOM,ES6,DOM.Iterable,ScriptHost`

**tl;dr**

Short answer either `"lib": [ "es6", "dom" ]` or `"types": ["core-js"]` can be used to resolve `can't find Promise,Map, Set and Iterator`. Using both however will cause duplicate identifier errors.

[**Source**](https://stackoverflow.com/questions/35660498)  
**[Top](#599b)**

### How to detect when an @Input() value changes in Angular?

> 154+ points _? 8_9,893+ viewed   
> _[**Jon Catmull**](https://stackoverflow.com/users/3604283/jon-catmull) **asked,**_

I have a parent component (**CategoryComponent**), a child component (**videoListComponent**) and an ApiService.

I have most of this working fine i.e. each component can access the json api and get its relevant data via observables.

Currently video list component just gets all videos, I would like to filter this to just videos in a particular category, I achieved this by passing the categoryId to the child via `@Input()`.

CategoryComponent.html

```ts
<video-list *ngIf="category" [categoryId]="category.id"></video-list>
```

This works and when the parent CategoryComponent category changes then the categoryId value gets passed through via `@Input()` but I then need to detect this in VideoListComponent and re-request the videos array via APIService (with the new categoryId).

In AngularJS I would have done a `$watch` on the variable. What is the best way to handle this?

> [**_Alan C. S._**](https://stackoverflow.com/users/2107767) **_answered, (181+ points)_**

**Actually, there are two ways of detecting and acting up on when an input changes in the child component in angular2+ :**

1. You can use the **ngOnChanges() lifecycle method** as also mentioned in older answers:   
`@Input() categoryId: string; ngOnChanges(changes: SimpleChanges) { this.doSomething(changes.categoryId.currentValue); // You can also use categoryId.previousValue and // categoryId.firstChange for comparing old and new values }`
2. Documentation Links: [ngOnChanges,](https://angular.io/api/core/OnChanges) [SimpleChanges,](https://angular.io/api/core/SimpleChanges) [SimpleChange](https://angular.io/api/core/SimpleChange)  
Demo Example: Look at [this plunker](https://plnkr.co/edit/LUr2bMQRhhAeuLN3R5B6?p=preview)
3. Alternately, you can also use an **input property setter** as follows:  
`private _categoryId: string; @Input() set categoryId(value: string) { this._categoryId = value; this.doSomething(this._categoryId); } get categoryId(): string { return this._categoryId; }`
4. Documentation Link: Look [here](https://angular.io/guide/component-interaction#intercept-input-property-changes-with-a-setter).
5. Demo Example: Look at [this plunker](https://plnkr.co/edit/EsolgwJVuvOUx6rKk8d4?p=preview).

**WHICH APPROACH SHOULD YOU USE?**

If your component has several inputs, then, if you use ngOnChanges(), you will get all changes for all the inputs at once within ngOnChanges(). Using this approach, you can also compare current and previous values of the input that has changed and take actions accordingly.

However, if you want to do something when only a particular single input changes (and you don’t care about the other inputs), then it might be simpler to use an input property setter. However, this approach does not provide a built in way to compare previous and current values of the changed input (which you can do easily with the ngOnChanges lifecycle method).

**EDIT 2017–07–25: ANGULAR CHANGE DETECTION MAY STILL NOT FIRE UNDER SOME CIRCUMSTANCES**

Normally, change detection for both setter and ngOnChanges will fire whenever the parent component changes the data it passes to the child, **provided that the data is a JS primitive datatype(string, number, boolean)**. However, in the following scenarios, it will not fire and you have to take extra actions in order to make it work.

1. If you are using a nested object or array (instead of a JS primitive data type) to pass data from Parent to Child, change detection (using either setter or ngchanges) might not fire, as also mentioned in the answer by user: muetzerich. For solutions look [here](https://stackoverflow.com/questions/34796901/angular2-change-detection-ngonchanges-not-firing-for-nested-object).
2. If you are mutating data outside of the angular context (i.e., externally), then angular will not know of the changes. You may have to use ChangeDetectorRef or NgZone in your component for making angular aware of external changes and thereby triggering change detection. Refer to [this](https://stackoverflow.com/questions/42971865/angular2-zone-run-vs-changedetectorref-detectchanges).

[**Source**](https://stackoverflow.com/questions/38571812)  
**[Top](#599b)**

### How to pass URL arguments (query string) to a HTTP request on Angular

> 154+ points _? 1_57,619+ viewed   
> _[**Miguel Lattuada**](https://stackoverflow.com/users/3276721/miguel-lattuada) **asked,**_

Hi guys I’m creating a HTTP request on Angular, but I do not know how to add URL arguments (query string) to it.

```ts
this.http.get(StaticSettings.BASE_URL).subscribe(
  (response) => this.onGetForecastResult(response.json()),
  (error) => this.onGetForecastError(error.json()),
  () => this.onGetForecastComplete()
);
```

Now my StaticSettings.BASE_URL is something like a url with no query string like: [http://atsomeplace.com/](http://atsomeplace.com/) but I want it to be [http://atsomeplace.com/?var1=val1&var2=val2](http://atsomeplace.com/?var1=val1&var2=val2)

Where var1, and var2 fit on my Http request object? I want to add them like an object.

```json
{
  query: {
    var1: val1,
    var2: val2
  }
}
```

and then just the Http module do the job to parse it into URL query string.

> [**_toskv_**](https://stackoverflow.com/users/5152732) **_answered, (216+ points)_**

The [**HttpClient**](https://angular.io/api/common/http/HttpClient) methods allow you to set the **params** in it’s options.

You can configure it by importing the [**HttpClientModule**](https://angular.io/api/common/http) from the @angular/common/http package.

```ts
import {HttpClientModule} from '@angular/common/http';

@NgModule({
  imports: [ BrowserModule, HttpClientModule ],
  declarations: [ App ],
  bootstrap: [ App ]
})
export class AppModule {}
```

After that you can inject the **HttpClient** and use it to do the request.

```ts
import {HttpClient} from '@angular/common/http'
```

```ts
import {HttpClient} from '@angular/common/http'

@Component({
  selector: 'my-app',
  template: `
    <div>
      <h2>Hello {{name}}</h2>
    </div>
  `,
})
export class App {
  name:string;
  constructor(private httpClient: HttpClient) {
    this.httpClient.get('/url', {
      params: {
        appid: 'id1234',
        cnt: '5'
      },
      observe: 'response'
    })
    .toPromise()
    .then(response => {
      console.log(response);
    })
    .catch(console.log);
  }
}
```

You can find a working example [here](https://plnkr.co/edit/G4mczOLOHfVYKpuaWee3?p=preview).

For angular versions prior to version 4 you can do the same using the **Http** service.

The **Http.get** method takes an object that implements [RequestOptionsArgs](https://angular.io/docs/ts/latest/api/http/index/RequestOptionsArgs-interface.html) as a second parameter.

The **search** field of that object can be used to set a string or a [URLSearchParams](https://angular.io/docs/ts/latest/api/http/index/URLSearchParams-class.html) object.

An example:

```ts
// Parameters obj-
 let params: URLSearchParams = new URLSearchParams();
 params.set('appid', StaticSettings.API_KEY);
 params.set('cnt', days.toString());
 
 //Http request-
 return this.http.get(StaticSettings.BASE_URL, {
   search: params
 }).subscribe(
   (response) => this.onGetForecastResult(response.json()), 
   (error) => this.onGetForecastError(error.json()), 
   () => this.onGetForecastComplete()
 );
```

The documentation for the **Http** class has more details. It can be found [here](https://angular.io/docs/ts/latest/api/http/index/Http-class.html) and an working example [here](https://plnkr.co/edit/pKdztZBHr0wr1YLmmI8P?p=preview).

[**Source**](https://stackoverflow.com/questions/34475523)  
**[Top](#599b)**

### How do you deploy Angular apps?

> 153+ points _? 8_9,991+ viewed   
> _[**Joseph Assem Sobhy**](https://stackoverflow.com/users/1362355/joseph-girgis) **asked,**_

How do you deploy Angular apps once they reach the production phase?

All the guides I’ve seen so far (even on [angular.io](https://angular.io/)) are counting on a lite-server for serving and browserSync to reflect changes — but when you finish with development, how can you publish the app?

Do I import all the compiled `.js` files on the `index.html` page or do I minify them using gulp? Will they work? Do I need SystemJS at all in the production version?

> [**_Amid_**](https://stackoverflow.com/users/1035889) **_answered, (74+ points)_**

You are actually here touching two questions in one. First one is how to host your application. And as @toskv mentioned its really too broad question to be answered and depends on numerous different things. Second one is more specific — how do you prepare the deployment version of the application. You have several options here:

1. Deploy as it is. Just that — no minification, concatenation, name mangling etc. Transpile all your ts project, copy all your resulting js/css/… sources + dependencies to the hosting server and your are good to go.
2. Deploy using special bundling tools. Like webpack or systemjs builder. They come with all possibilities that are lacking in #1. You can pack all your app code into just couple of js/css/… files that you reference in your html. Systemjs buider even allows you to get rid of need to include systemjs as part of your deployment package.

Yes you will most likely need to deploy systemjs and bunch of other external libraries as part of your package. And yes you will be able to bundle them into just couple of js files you reference from your html page. You do not have to reference all your compiled js files from the page though — systemjs as a module loader will take care of that.

I know it sounds muddy — to help get you started with the #2 here are two really good sample applications:

SystemJS builder: [angular2 seed](https://github.com/mgechev/angular2-seed)

WebPack: [angular2 webpack starter](https://github.com/AngularClass/angular2-webpack-starter)

Look how they do it — and hopefully this will help you to find your way of bundling apps you make.

[**Source**](https://stackoverflow.com/questions/35539622)  
**[Top](#599b)**

### ngFor with index as value in attribute

> 149+ points _? 1_95,294+ viewed   
> _[**Vivendi**](https://stackoverflow.com/users/1175327/vivendi) **asked,**_

I have a simple `ngFor` loop which also keeps track of the current `index`. I want to store that `index` value in an attribute so I can print it. But I can't figure out how this works.

I basically have this:

```ts
<ul *ngFor="#item of items; #i = index" data-index="#i">
    <li>{{item}}</li>
</ul>
```

I want to store the value of `#i` in the attribute `data-index`. I tried several methods but none of them worked.

I have a demo here: [http://plnkr.co/edit/EXpOKAEIFlI9QwuRcZqp?p=preview](http://plnkr.co/edit/EXpOKAEIFlI9QwuRcZqp?p=preview)

How can I store the `index` value in the `data-index` attribute?

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_answered, (284+ points)_**

I would use this syntax to set the index value into an attribute of the HTML element:

```ts
<ul>
    <li *ngFor="#item of items; #i = index" [attr.data-index]="i">
        {{item}}
    </li>
</ul>
```

Here is the updated plunkr: [http://plnkr.co/edit/LiCeyKGUapS5JKkRWnUJ?p=preview](http://plnkr.co/edit/LiCeyKGUapS5JKkRWnUJ?p=preview).

**Update for recent angular 2 releases** You have to use `let` to declare the value rather than `#`.

```ts
<ul>
    <li *ngFor="let item of items; let i = index" [attr.data-index]="i">
        {{item}}
    </li>
</ul>
```

[**Source**](https://stackoverflow.com/questions/35405618)  
**[Top](#599b)**

### Define global constants in Angular 2

> 149+ points _? 1_28,101+ viewed   
> _[**AndreFeijo**](https://stackoverflow.com/users/2946773/andrefeijo) **asked,**_

In Angular 1.x you can define constants like this:

```ts
angular.module('mainApp.config', [])
.constant('API_ENDPOINT', 'http://127.0.0.1:6666/api/')
```

What would be the equivalent in Angular2 (with Typescript)? I just don’t want to repeat the API base url over and over again in all my services.

> [**_AndreFeijo_**](https://stackoverflow.com/users/2946773) **_answered, (159+ points)_**

**Below changes works for me on Angular 2 final version:**

```ts
export class AppSettings {
   public static API_ENDPOINT='http://127.0.0.1:6666/api/';
}
```

**And then in the service:**

```ts
import {Http} from 'angular2/http';
import {Message} from '../models/message';
import {Injectable} from 'angular2/core';
import {Observable} from 'rxjs/Observable';
import {AppSettings} from '../appSettings';
import 'rxjs/add/operator/map';

@Injectable()
export class MessageService {

    constructor(private http: Http) { }
    
    getMessages(): Observable<Message[]> {
        return this.http.get(AppSettings.API_ENDPOINT+'/messages')
            .map(response => response.json())
            .map((messages: Object[]) => {
                return messages.map(message => this.parseData(message));
            });
    }
    
    private parseData(data): Message {
        return new Message(data);
    }
}
```

[**Source**](https://stackoverflow.com/questions/34986922)  
**[Top](#599b)**

### Angular — Use pipes in services and components

> 148+ points _? 7_5,716+ viewed   
> _[**POSIX-compliant**](https://stackoverflow.com/users/4602586/posix-compliant) **asked,**_

In AngularJS, I am able to use filters (pipes) inside of services and controllers using syntax similar to this:

```ts
$filter('date')(myDate, 'yyyy-MM-dd');
```

Is it possible to use pipes in services/components like this in Angular?

> [**_cexbrayat_**](https://stackoverflow.com/users/971121) **_answered, (271+ points)_**

As usual in Angular, you can rely on dependency injection:

```ts
import { DatePipe } from '@angular/common';
class MyService {

  constructor(private datePipe: DatePipe) {}
  
  transformDate(date) {
    this.datePipe.transform(myDate, 'yyyy-MM-dd');
  }
}
```

Add `DatePipe` to your providers list in your module; if you forget to do this you'll get an error `no provider for DatePipe`:

```
providers: [DatePipe,...]
```

Be warned though that the `DatePipe` was relying on the Intl API until version 5, which is not supported by all browsers (check the [compatibility table](http://kangax.github.io/compat-table/esintl/)).

If you’re using older Angular versions, you should add the `Intl` polyfill to your project to avoid any problem. See this [related question](https://stackoverflow.com/questions/35017800/ionic-2-using-angular-2-pipe-breaks-on-ios-cant-find-variable-intl/35018352#35018352) for a more detailed answer.

[**Source**](https://stackoverflow.com/questions/35144821)  
**[Top](#599b)**

### Angular2 Exception: Can’t bind to ‘routerLink’ since it isn’t a known native property

> 144+ points _? 8_3,326+ viewed   
> _[**Lester Burnham**](https://stackoverflow.com/users/1798547/lester-burnham) **asked,**_

Obviously the beta for Angular2 is newer than new, so there’s not much information out there, but I am trying to do what I think is some fairly basic routing.

Hacking about with the quick-start code and other snippets from the [https://angular.io](https://angular.io) website has resulted in the following file structure:

```
angular-testapp/
    app/
        app.component.ts
        boot.ts
        routing-test.component.ts
    index.html
```

With the files being populated as follows:

**index.html**

```html
<html>

  <head>
    <base href="/">
    <title>Angular 2 QuickStart</title>
    <link href="../css/bootstrap.css" rel="stylesheet">
    
    <!-- 1. Load libraries -->
    <script src="node_modules/angular2/bundles/angular2-polyfills.js"></script>
    <script src="node_modules/systemjs/dist/system.src.js"></script>
    <script src="node_modules/rxjs/bundles/Rx.js"></script>
    <script src="node_modules/angular2/bundles/angular2.dev.js"></script>
    <script src="node_modules/angular2/bundles/router.dev.js"></script>
    
    <!-- 2. Configure SystemJS -->
    <script>
      System.config({
        packages: {        
          app: {
            format: 'register',
            defaultExtension: 'js'
          }
        }
      });
      System.import('app/boot')
            .then(null, console.error.bind(console));
    </script>
    
  </head>
  
  <!-- 3. Display the application -->
  <body>
    <my-app>Loading...</my-app>
  </body>
  
</html>
```

**boot.ts**

```ts
import {bootstrap}    from 'angular2/platform/browser'
import {ROUTER_PROVIDERS} from 'angular2/router';

import {AppComponent} from './app.component'

bootstrap(AppComponent, [
    ROUTER_PROVIDERS
]);
```

**app.component.ts**

```ts
import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS, LocationStrategy, HashLocationStrategy} from 'angular2/router';

import {RoutingTestComponent} from './routing-test.component';

@Component({
    selector: 'my-app',
    template: `
        <h1>Component Router</h1>
        <a [routerLink]="['RoutingTest']">Routing Test</a>
        <router-outlet></router-outlet>
        `
})

@RouteConfig([
    {path:'/routing-test', name: 'RoutingTest', component: RoutingTestComponent, useAsDefault: true},
])

export class AppComponent { }
```

**routing-test.component.ts**

```ts
import {Component} from 'angular2/core';
import {Router} from 'angular2/router';

@Component({
    template: `
        <h2>Routing Test</h2>
        <p>Interesting stuff goes here!</p>
        `
})
export class RoutingTestComponent { }
```

Attempting to run this code produces the error:

```bash
EXCEPTION: Template parse errors:
Can't bind to 'routerLink' since it isn't a known native property ("
        <h1>Component Router</h1>
        <a [ERROR ->][routerLink]="['RoutingTest']">Routing Test</a>
        <router-outlet></router-outlet>
        "): AppComponent@2:11
```

I found a vaguely related issue here; [router-link directives broken after upgrading to angular2.0.0-beta.0](https://stackoverflow.com/questions/34304115/router-link-directives-broken-after-upgrading-to-angular2-0-0-beta-0). However, the “working example” in one of the answers is based on pre-beta code — which may well still work, but I would like to know why the code I have created is not working.

Any pointers would be gratefully received!

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_answered, (220+ points)_**

**>=R**C.5

import the `RouterModule` See also [https://angular.io/docs/ts/latest/guide/router.html](https://angular.io/docs/ts/latest/guide/router.html)

```ts
@NgModule({ 
  imports: [RouterModule],
  ...
})
```

**>=R**C.2

**app.routes.ts**

```ts
import { provideRouter, RouterConfig } from '@angular/router';

export const routes: RouterConfig = [
  ...
];

export const APP_ROUTER_PROVIDERS = [provideRouter(routes)];
```

**main.ts**

```
import { bootstrap } from '@angular/platform-browser-dynamic';
import { APP_ROUTER_PROVIDERS } from './app.routes';

bootstrap(AppComponent, [APP_ROUTER_PROVIDERS]);
```

**<=RC.1**

Your code is missing

```ts
@Component({
    ...
    directives: [ROUTER_DIRECTIVES],
    ...)}
```

You can’t use directives like `routerLink` or `router-outlet` without making them known to your component.

While directive names were changed to be case-sensitive in Angular2, elements still use `-` in the name like `<router-outl`et> to be compatible with the web-components spec which requ`i`re a - in the name of custom elements.

**register globally**

To make `ROUTER_DIRECTIVES` globally available, add this provider to `bootstrap(...)`:

```
provide(PLATFORM_DIRECTIVES, {useValue: [ROUTER_DIRECTIVES], multi: true})
```

then it’s no longer necessary to add `ROUTER_DIRECTIVES` to each component.

[**Source**](https://stackoverflow.com/questions/34317044)  
**[Top](#599b)**

### Angular 2 dynamic tabs with user-click chosen components

> 143+ points _? 8_0,735+ viewed   
> _[**Cuel**](https://stackoverflow.com/users/2951897/cuel) **asked,**_

I’m trying to setup a tab system that allows for components to register themselves (with a title). The first tab is like an inbox, there’s plenty of actions/link items to choose from for the users, and each of these clicks should be able to instantiate a new component, on click. The actions / links comes in from JSON.

The instantiated component will then register itself as a new tab.

I’m not sure if this is the ‘best’ approach? Sofar the only guides I’ve seen are for static tabs, which doesn’t help.

So far I’ve only got the tabs service which is bootstrapped in main to persist throughout the app, looks ~something like this.

```ts
export interface ITab { title: string; }

@Injectable()
export class TabsService {
    private tabs = new Set<ITab>();
    
    addTab(title: string): ITab {
        let tab: ITab = { title };
        this.tabs.add(tab);
        return tab;
    }
    
    removeTab(tab: ITab) {
        this.tabs.delete(tab);
    }
}
```

Questions:

1) How can I have a dynamic list in the inbox that creates new (different) tabs? I am sort of guessing the DynamicComponentBuilder would be used?

2) How can the components created from the inbox (on click) register themselves as tabs and also be shown? I’m guessing ng-content but I can’t find much info on how to use it

Edit: Try to clarify

Think of the inbox as a mail inbox, items are fetched as JSON and displays several items. Once one of the items is clicked, a new tab is created with that items action ‘type’. The type is then a component

Edit2: Image

[http://i.imgur.com/yzfMOXJ.png](http://i.imgur.com/yzfMOXJ.png)

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_answered, (190+ points)_**

**update**

[**Angular 5 StackBlitz example**](https://stackblitz.com/edit/angular-ygz3jg)

**update**

`ngComponentOutlet` was added to 4.0.0-beta.3

**update**

There is a `NgComponentOutlet` work in progress that does something similar [https://github.com/angular/angular/pull/11235](https://github.com/angular/angular/pull/11235)

**RC.7**

[**Plunker example RC.7**](http://plnkr.co/edit/UGzoPTCHlXKWrn4p8gd1?p=preview)

```ts
// Helper component to add dynamic components
@Component({
  selector: 'dcl-wrapper',
  template: `<div #target></div>`
})
export class DclWrapper {
  @ViewChild('target', {read: ViewContainerRef}) target: ViewContainerRef;
  @Input() type: Type<Component>;
  cmpRef: ComponentRef<Component>;
  private isViewInitialized:boolean = false;
  
  constructor(private componentFactoryResolver: ComponentFactoryResolver, private compiler: Compiler) {}
  
  updateComponent() {
    if(!this.isViewInitialized) {
      return;
    }
    if(this.cmpRef) {
      // when the `type` input changes we destroy a previously 
      // created component before creating the new one
      this.cmpRef.destroy();
    }
    
    let factory = this.componentFactoryResolver.resolveComponentFactory(this.type);
    this.cmpRef = this.target.createComponent(factory)
    // to access the created instance use
    // this.compRef.instance.someProperty = 'someValue';
    // this.compRef.instance.someOutput.subscribe(val => doSomething());
  }
  
  ngOnChanges() {
    this.updateComponent();
  }
  
  ngAfterViewInit() {
    this.isViewInitialized = true;
    this.updateComponent();  
  }
  
  ngOnDestroy() {
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }    
  }
}
```

Usage example

```ts
// Use dcl-wrapper component
@Component({
  selector: 'my-tabs',
  template: `
  <h2>Tabs</h2>
  <div *ngFor="let tab of tabs">
    <dcl-wrapper [type]="tab"></dcl-wrapper>
  </div>
`
})
export class Tabs {
  @Input() tabs;
}

@Component({
  selector: 'my-app',
  template: `
  <h2>Hello {{name}}</h2>
  <my-tabs [tabs]="types"></my-tabs>
`
})
export class App {
  // The list of components to create tabs from
  types = [C3, C1, C2, C3, C3, C1, C1];
}

@NgModule({
  imports: [ BrowserModule ],
  declarations: [ App, DclWrapper, Tabs, C1, C2, C3],
  entryComponents: [C1, C2, C3],
  bootstrap: [ App ]
})
export class AppModule {}
```

See also [angular.io DYNAMIC COMPONENT LOADER](https://angular.io/docs/ts/latest/cookbook/dynamic-component-loader.html)

**older versions** **xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx**

This changed again in Angular2 RC.5

I will update the example below but it’s the last day before vacation.

This [Plunker example](http://plnkr.co/edit/3dzkMVXe4AGSRhk11TXG?p=preview) demonstrates how to dynamically create components in RC.5

**Update — use [ViewContainerRef](https://angular.io/docs/ts/latest/api/core/index/ViewContainerRef-class.html).createComponent()**

Because `DynamicComponentLoader` is deprecated, the approach needs to be update again.

```ts
@Component({
  selector: 'dcl-wrapper',
  template: `<div #target></div>`
})
export class DclWrapper {
  @ViewChild('target', {read: ViewContainerRef}) target;
  @Input() type;
  cmpRef:ComponentRef;
  private isViewInitialized:boolean = false;
  
  constructor(private resolver: ComponentResolver) {}
  
  updateComponent() {
    if(!this.isViewInitialized) {
      return;
    }
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }
   this.resolver.resolveComponent(this.type).then((factory:ComponentFactory<any>) => {
      this.cmpRef = this.target.createComponent(factory)
      // to access the created instance use
      // this.compRef.instance.someProperty = 'someValue';
      // this.compRef.instance.someOutput.subscribe(val => doSomething());
    });
  }
  
  ngOnChanges() {
    this.updateComponent();
  }
  
  ngAfterViewInit() {
    this.isViewInitialized = true;
    this.updateComponent();  
  }
  ngOnDestroy() {
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }    
  }
}
```

[**Plunker example RC.4**](http://plnkr.co/edit/GJTLrnQdRDBvZenX59PZ?p=preview)  
[**Plunker example beta.17**](https://plnkr.co/edit/PpgMvS?p=preview)

**Update — use loadNextToLocation**

```ts
export class DclWrapper {
  @ViewChild('target', {read: ViewContainerRef}) target;
  @Input() type;
  cmpRef:ComponentRef;
  private isViewInitialized:boolean = false;
  
  constructor(private dcl:DynamicComponentLoader) {}
  
  updateComponent() {
    // should be executed every time `type` changes but not before `ngAfterViewInit()` was called 
    // to have `target` initialized
    if(!this.isViewInitialized) {
      return;
    }
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }
    this.dcl.loadNextToLocation(this.type, this.target).then((cmpRef) => {
      this.cmpRef = cmpRef;
    });
  }
  
  ngOnChanges() {
    this.updateComponent();
  }
  
  ngAfterViewInit() {
    this.isViewInitialized = true;
    this.updateComponent();  
  }
  
  ngOnDestroy() {
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }    
  }
}
```

[**Plunker example beta.17**](https://plnkr.co/edit/kc2Bgg?p=preview)

**original**

Not entirely sure from your question what your requirements are but I think this should do what you want.

The `Tabs` component gets an array of types passed and it creates "tabs" for each item in the array.

```ts
@Component({
  selector: 'dcl-wrapper',
  template: `<div #target></div>`
})
export class DclWrapper {
  constructor(private elRef:ElementRef, private dcl:DynamicComponentLoader) {}
  @Input() type;
  
  ngOnChanges() {
    if(this.cmpRef) {
      this.cmpRef.dispose();
    }
    this.dcl.loadIntoLocation(this.type, this.elRef, 'target').then((cmpRef) => {
      this.cmpRef = cmpRef;
    });
  }
}

@Component({
  selector: 'c1',
  template: `<h2>c1</h2>`
  
})
export class C1 {
}

@Component({
  selector: 'c2',
  template: `<h2>c2</h2>`
})
export class C2 {
}
@Component({
  selector: 'c3',
  template: `<h2>c3</h2>`
  
})
export class C3 {
}

@Component({
  selector: 'my-tabs',
  directives: [DclWrapper],
  template: `
  <h2>Tabs</h2>
  <div *ngFor="let tab of tabs">
    <dcl-wrapper [type]="tab"></dcl-wrapper>
  </div>
`
})
export class Tabs {
  @Input() tabs;
}

@Component({
  selector: 'my-app',
  directives: [Tabs]
  template: `
  <h2>Hello {{name}}</h2>
  <my-tabs [tabs]="types"></my-tabs>
`
})
export class App {
  types = [C3, C1, C2, C3, C3, C1, C1];
}
```

[**Plunker example beta.15**](https://plnkr.co/edit/kc2Bgg?p=preview) (not based on your Plunker)

There is also a way to pass data along that can be passed to the dynamically created component like (`someData` would need to be passed like `type`)

```ts
this.dcl.loadIntoLocation(this.type, this.elRef, 'target').then((cmpRef) => {
  cmpRef.instance.someProperty = someData;
  this.cmpRef = cmpRef;
});
```

There is also some support to use dependency injection with shared services.

For more details see [https://angular.io/docs/ts/latest/cookbook/dynamic-component-loader.html](https://angular.io/docs/ts/latest/cookbook/dynamic-component-loader.html)

[**Source**](https://stackoverflow.com/questions/36325212)  
**[Top](#599b)**

### Delegation: EventEmitter or Observable in Angular

> 141+ points _? 7_8,505+ viewed   
> _[**the_critic**](https://stackoverflow.com/users/1066899/the-critic) **asked,**_

I am trying to implement something like a delegation pattern in Angular. When the user clicks on a `nav-item`, I would like to call a function which then emits an event which should in turn be handled by some other component listening for the event.

Here is the scenario: I have a `Navigation` component:

```ts
import {Component, Output, EventEmitter} from 'angular2/core';

@Component({
    // other properties left out for brevity
    events : ['navchange'], 
    template:`
      <div class="nav-item" (click)="selectedNavItem(1)"></div>
    `
})

export class Navigation {

    @Output() navchange: EventEmitter<number> = new EventEmitter();
    
    selectedNavItem(item: number) {
        console.log('selected nav item ' + item);
        this.navchange.emit(item)
    }
    
}
```

Here is the observing component:

```ts
export class ObservingComponent {

  // How do I observe the event ? 
  // <----------Observe/Register Event ?-------->
  
  public selectedNavItem(item: number) {
    console.log('item index changed!');
  }
  
}
```

The key question is, how do I make the observing component observe the event in question ?

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_answered, (306+ points)_**

**Update 2016–06–27:** instead of using Observables, use either

* a BehaviorSubject, as recommended by @Abdulrahman in a comment, or
* a ReplaySubject, as recommended by @Jason Goemaat in a comment

A [Subject](http://reactivex.io/rxjs/manual/overview.html#subject) is both an Observable (so we can `subscribe()` to it) and an Observer (so we can call `next()` on it to emit a new value). We exploit this feature. A Subject allows values to be multicast to many Observers. We don't exploit this feature (we only have one Observer).

[BehaviorSubject](http://reactivex.io/rxjs/manual/overview.html#behaviorsubject) is a variant of Subject. It has the notion of “the current value”. We exploit this: whenever we create an ObservingComponent, it gets the current navigation item value from the BehaviorSubject automatically.

The code below and the [plunker](http://plnkr.co/edit/XqwwUM44NQEpxQVFFxNW?p=preview) use BehaviorSubject.

[ReplaySubject](http://reactivex.io/rxjs/manual/overview.html#replaysubject) is another variant of Subject. If you want to wait until a value is actually produced, use `ReplaySubject(1)`. Whereas a BehaviorSubject requires an initial value (which will be provided immediately), ReplaySubject does not. ReplaySubject will always provide the most recent value, but since it does not have a required initial value, the service can do some async operation before returning it's first value. It will still fire immediately on subsequent calls with the most recent value. If you just want one value, use `first()` on the subscription. You do not have to unsubscribe if you use `first()`.

```ts
import {Injectable}      from '@angular/core'
import {BehaviorSubject} from 'rxjs/BehaviorSubject';

@Injectable()
export class NavService {
  // Observable navItem source
  private _navItemSource = new BehaviorSubject<number>(0);
  // Observable navItem stream
  navItem$ = this._navItemSource.asObservable();
  // service command
  changeNav(number) {
    this._navItemSource.next(number);
  }
}

import {Component}    from '@angular/core';
import {NavService}   from './nav.service';
import {Subscription} from 'rxjs/Subscription';

@Component({
  selector: 'obs-comp',
  template: `obs component, item: {{item}}`
})
export class ObservingComponent {
  item: number;
  subscription:Subscription;
  constructor(private _navService:NavService) {}
  ngOnInit() {
    this.subscription = this._navService.navItem$
       .subscribe(item => this.item = item)
  }
  ngOnDestroy() {
    // prevent memory leak when component is destroyed
    this.subscription.unsubscribe();
  }
}

@Component({
  selector: 'my-nav',
  template:`
    <div class="nav-item" (click)="selectedNavItem(1)">nav 1 (click me)</div>
    <div class="nav-item" (click)="selectedNavItem(2)">nav 2 (click me)</div>`
})
export class Navigation {
  item = 1;
  constructor(private _navService:NavService) {}
  selectedNavItem(item: number) {
    console.log('selected nav item ' + item);
    this._navService.changeNav(item);
  }
}
```

[Plunker](http://plnkr.co/edit/XqwwUM44NQEpxQVFFxNW?p=preview)

**Original answer that uses an Observable:** (it requires more code and logic than using a BehaviorSubject, so I don’t recommend it, but it may be instructive)

So, here’s an implementation that uses an Observable [instead of an EventEmitter](https://stackoverflow.com/a/34402436/215945). Unlike my EventEmitter implementation, this implementation also stores the currently selected `navItem` in the service, so that when an observing component is created, it can retrieve the current value via API call `navItem()`, and then be notified of changes via the `navChange$` Observable.

```ts
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/share';
import {Observer} from 'rxjs/Observer';

export class NavService {
  private _navItem = 0;
  navChange$: Observable<number>;
  private _observer: Observer;
  constructor() {
    this.navChange$ = new Observable(observer =>
      this._observer = observer).share();
    // share() allows multiple subscribers
  }
  changeNav(number) {
    this._navItem = number;
    this._observer.next(number);
  }
  navItem() {
    return this._navItem;
  }
}

@Component({
  selector: 'obs-comp',
  template: `obs component, item: {{item}}`
})
export class ObservingComponent {
  item: number;
  subscription: any;
  constructor(private _navService:NavService) {}
  ngOnInit() {
    this.item = this._navService.navItem();
    this.subscription = this._navService.navChange$.subscribe(
      item => this.selectedNavItem(item));
  }
  selectedNavItem(item: number) {
    this.item = item;
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}

@Component({
  selector: 'my-nav',
  template:`
    <div class="nav-item" (click)="selectedNavItem(1)">nav 1 (click me)</div>
    <div class="nav-item" (click)="selectedNavItem(2)">nav 2 (click me)</div>
  `,
})
export class Navigation {
  item:number;
  constructor(private _navService:NavService) {}
  selectedNavItem(item: number) {
    console.log('selected nav item ' + item);
    this._navService.changeNav(item);
  }
}
```

[Plunker](http://plnkr.co/edit/vL76b0UjrAav3Ao7kF4W?p=preview)

See also the [Component Interaction Cookbook example](https://angular.io/docs/ts/latest/cookbook/component-communication.html#!#bidirectional-service), which uses a `Subject` in addition to observables. Although the example is "parent and children communication," the same technique is applicable for unrelated components.

[**Source**](https://stackoverflow.com/questions/34376854)  
**[Top](#599b)**

### How to add bootstrap to an angular-cli project

> 140+ points _? 1_66,741+ viewed   
> _[**Jerome**](https://stackoverflow.com/users/811865/jerome) **asked,**_

We want to use bootstrap 4 (4.0.0-alpha.2) in our app generated with angular-cli 1.0.0-beta.5 (w/ node v6.1.0).

After getting bootstrap and its dependencies with npm, our first approach consisted in adding them in `angular-cli-build.js`:

```js
'bootstrap/dist/**/*.min.+(js|css)',  
  'jquery/dist/jquery.min.+(js|map)',  
  'tether/dist/**/*.min.+(js|css)',
```

and import them in our `index.html`

```html
<script src="vendor/jquery/dist/jquery.min.js"></script>
  <script src="vendor/tether/dist/js/tether.min.js"></script>
  <link rel="stylesheet" type="text/css" href="vendor/bootstrap/dist/css/bootstrap.min.css">
  <script src="vendor/bootstrap/dist/js/bootstrap.min.js"></script>
```

This worked fine with `ng serve` but as soon as we produced a build with `-prod` flag all these dependencies disappeared from `dist/vendor` (surprise !).

**How we are intended to handle such scenario (i.e. loading bootstrap scripts) in a project generated with angular-cli ?**

We had the following thoughts but we don’t really know which way to go…

* use a CDN ? but we would rather serve these files to guarantee that they will be available
* copy dependencies to `dist/vendor` after our `ng build -prod` ? But that seems like something angular-cli should provide since it 'takes care' of the build part ?
* adding jquery, bootstrap and tether in src/system-config.ts and somehow pull them into our bundle in main.ts ? But that seemed wrong considering that we are not going to explicitly use them in our application’s code (unlike moment.js or something like lodash, for example)

> [**_pd farhad_**](https://stackoverflow.com/users/1417742) **_answered, (202+ points)_**

**IMPORTANT UPDATE: ng2-bootstrap is now replaced by [ngx-bootstrap](https://github.com/valor-software/ngx-bootstrap) **

ngx-bootstrap supports both angular 3 and 4.

**Update :** `**1.0.0-beta.11-webpack**` **or above versions**

First of all check your angular-cli version with the following command in the terminal: `ng -v`

If your angular-cli version is greater than `1.0.0-beta.11-webpack` then you should follow these steps:

1. install **ngx-bootstrap** and **bootstrap:**  
`npm install ngx-bootstrap bootstrap --save`

This line installs bootstrap 3 nowadays, but can install bootstrap 4 in future. Keep in mind ngx-bootstrap supports both versions.

1. open **src/app/app.module.ts** and add  
`import { AlertModule } from 'ngx-bootstrap'; ... @NgModule({ ... imports: [AlertModule.forRoot(), ... ], ... })`
2. open **angular-cli.json** and insert a new entry into the styles array  
`"styles": [ "styles.css", "../node_modules/bootstrap/dist/css/bootstrap.min.css" ],`
3. open **src/app/app.component.html** and add  
`<alert type="success">hello&l`t;/alert>

**1.0.0-beta.10 or below versions:**

And, if your angular-cli version is 1.0.0-beta.10 or below versions then you can use below steps.

First go to the project directory and type

```
npm install ngx-bootstrap --save
```

then open your **angular-cli-build.js** and add this line

```js
vendorNpmFiles: [
   ..................
   'ngx-bootstrap/**/*.js',
    ....................
  ]
```

now open your **src/system-config.ts**, write

```ts
const map:any = {
     ..................
   'ngx-bootstrap': 'vendor/ngx-bootstrap',
    ....................
}
```

and

```ts
const packages: any = {
  'ngx-bootstrap': {
    format: 'cjs',
    defaultExtension: 'js',
    main: 'ngx-bootstrap.js'
  }
};
```

[**Source**](https://stackoverflow.com/questions/37649164)  
**[Top](#599b)**

### access key and value of object using *ngFor

> 136+ points _? 1_39,816+ viewed   
> _[**Pardeep Jain**](https://stackoverflow.com/users/5043867/pardeep-jain) **asked,**_

Bit confused about how to get `Key and Value` of object in angular2 while usng *ngFor for iteration over object. i know in angular 1.x there is syntax like

```ts
ng-repeat="(key, value) in demo"
```

but in angular2 i don’t know i tired the same but did’t get successful. i have tried the below code but did’t run please tell me where i am doing wrong.

```ts
<ul>
  <li *ngFor='#key of demo'>{{key}}</li>
</ul>

demo = {
    'key1': [{'key11':'value11'}, {'key12':'value12'}],
    'key2': [{'key21':'value21'}, {'key22':'value22'}],
  }
```

here is plnkr where i have tried the same : [http://plnkr.co/edit/mIj619FncOpfdwrR0KeG?p=preview](http://plnkr.co/edit/mIj619FncOpfdwrR0KeG?p=preview)

I want to get `key1` and `key2` dynamically using *ngFor. How to get it? i searched a lot found idea of using pipe but how to use i dont know. is there any inbuild pipe for doing same in angular2 ?

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_answered, (134+ points)_**

You could create a custom pipe to return the list of key for each element. Something like that:

```ts
import { PipeTransform, Pipe } from '@angular/core';

@Pipe({name: 'keys'})
export class KeysPipe implements PipeTransform {
  transform(value, args:string[]) : any {
    let keys = [];
    for (let key in value) {
      keys.push(key);
    }
    return keys;
  }
}
```

and use it like that:

```ts
<tr *ngFor="let c of content">           
  <td *ngFor="let key of c | keys">{{key}}: {{c[key]}}</td>
</tr>
```

**Edit**

You could also return an entry containing both key and value:

```ts
@Pipe({name: 'keys'})
export class KeysPipe implements PipeTransform {
  transform(value, args:string[]) : any {
    let keys = [];
    for (let key in value) {
      keys.push({key: key, value: value[key]});
    }
    return keys;
  }
}
```

and use it like that:

```ts
<span *ngFor="let entry of content | keys">           
  Key: {{entry.key}}, value: {{entry.value}}
</span>
```

[**Source**](https://stackoverflow.com/questions/35534959)  
**[Top](#599b)**

### Angular exception: Can’t bind to ‘ngFor’ since it isn’t a known native property

> 134+ points _? 6_3,054+ viewed   
> _[**Mark Rajcok**](https://stackoverflow.com/users/215945/mark-rajcok) **asked,**_

What am I doing wrong?

```ts
import {bootstrap, Component} from 'angular2/angular2'

@Component({
  selector: 'conf-talks',
  template: `<div *ngFor="talk of talks">
     {{talk.title}} by {{talk.speaker}}
     <p>{{talk.description}}
   </div>`
})
class ConfTalks {
  talks = [ {title: 't1', speaker: 'Brian', description: 'talk 1'},
            {title: 't2', speaker: 'Julie', description: 'talk 2'}];
}
@Component({
  selector: 'my-app',
  directives: [ConfTalks],
  template: '<conf-talks></conf-talks>'
})
class App {}
bootstrap(App, [])
```

The error is

```bash
EXCEPTION: Template parse errors:
Can't bind to 'ngFor' since it isn't a known native property
("<div [ERROR ->]*ngFor="talk of talks">
```

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_answered, (325+ points)_**

I missed `let` in front of `talk`:

```ts
<div *ngFor="let talk of talks">
```

Note that [as of beta.17](https://github.com/angular/angular/blob/master/CHANGELOG.md#200-beta17-2016-04-28) usage of `#...` to declare local variables inside of structural directives like NgFor is deprecated. Use `let` instead.   
`<div *ngFor="#talk of talk`s"> now be`comes <div *ngFor="let talk o`f talks">

Original answer:

I missed `#` in front of `talk`:

```ts
<div *ngFor="#talk of talks">
```

It is so easy to forget that `#`. I wish the Angular exception error message would instead say:  
`you forgot that # again`.

[**Source**](https://stackoverflow.com/questions/34012291)  
**[Top](#599b)**

### How to add font-awesome to Angular 2 + CLI project

> 132+ points _? 7_1,934+ viewed   
> _[**Nik**](https://stackoverflow.com/users/1394625/nik) **asked,**_

I’m using Angular 2+ and Angular CLI.

How do I add font-awesome to my project?

> [**_AIon_**](https://stackoverflow.com/users/5904566) **_answered, (285+ points)_**

After Angular 2.0 final release, **the structure of the Angular2 CLI project has been changed** — you don’t need any vendor files, no system.js — only webpack. So you do:

1. `npm install font-awesome --save`
2. In the angular-cli.json file locate the `styles[]` array and add font-awesome references directory here, like below:   
`“apps”: [ { “root”: “src”, “outDir”: “dist”, …. “styles”: [ “styles.css”, “../node_modules/bootstrap/dist/css/bootstrap.css”, “../node_modules/font-awesome/css/font-awesome.css” // -here webpack will automatically build a link css element out of this!? ], … } ] ]`
3. Place some font-awesome icons in any html file you want:   
`<i class=”fa fa-american-sign-language-interpreting fa-5x” aria-hidden=”true”> </i>`
4. Run `ng build` and `ng serve` again - because the watchers are only for the src folder and angular-cli.json is not observed for changes.
5. Enjoy your awesome icons!

[**Source**](https://stackoverflow.com/questions/38796541)  
**[Top](#599b)**

### Difference between HTTP and HTTPClient in angular 4?

> 130+ points _? 4_7,082+ viewed   
> _[**Aioub Amini**](https://stackoverflow.com/users/3551590/aiyoub-amini) **asked,**_

I want to know which one to use to build a mock web service to test the Angular program?

> [**_AngularInDepth.com_**](https://stackoverflow.com/users/2545680) **_answered, (208+ points)_**

Use the `HttpClient` class from `HttpClientModule` if you're using Angular 4.3.x and above:

```ts
import { HttpClientModule } from '@angular/common/http';

@NgModule({
 imports: [
   BrowserModule,
   HttpClientModule
 ],
 ...
 
 class MyService() {
    constructor(http: HttpClient) {...}
```

It’s an upgraded version of `http` from `@angular/http` module with the following improvements:

* Interceptors allow middleware logic to be inserted into the pipeline
* Immutable request/response objects
* Progress events for both request upload and response download

You can read about how it works in [Insider’s guide into interceptors and HttpClient mechanics in Angular](https://blog.angularindepth.com/insiders-guide-into-interceptors-and-httpclient-mechanics-in-angular-103fbdb397bf).

* Typed, synchronous response body access, including support for JSON body types
* JSON is an assumed default and no longer needs to be explicitly parsed
* Post-request verification & flush based testing framework

Going forward the old http client will be deprecated. Here are the links to the [commit message](https://github.com/angular/angular/commit/37797e2) and [the official docs](https://angular.io/guide/http).

Also pay attention that old http was injected using `Http` class token instead of the new `HttpClient`:

```ts
import { HttpModule } from '@angular/http';

@NgModule({
 imports: [
   BrowserModule,
   HttpModule
 ],
 ...
 
 class MyService() {
    constructor(http: Http) {...}
```

Also, new `HttpClient` seem to require `tslib` in runtime, so you have to install it `npm i tslib` and update `system.config.js` if you're using `SystemJS`:

```ts
map: {
     ...
    'tslib': 'npm:tslib/tslib.js',
```

And you need to add another mapping if you use SystemJS:

```
'@angular/common/http': 'npm:@angular/common/bundles/common-http.umd.js',
```

[**Source**](https://stackoverflow.com/questions/45129790)  
**[Top](#599b)**

**That’s all for today. if you found this article helpful please help me to share it.** ? ? ?

**Follow me on [Medium](http://medium.com/wizardnet972) or [Twitter](https://twitter.com/wizardnet972) to read more about angular, webpack, typescript, nodejs and javascript! ? ? ?**

