---
title: How to get the best performance out of your Angular apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-04T21:43:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-best-performance-out-of-your-angular-apps-d5132a6c3335
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ryh4WCX9tu1IdgFd
tags:
- name: Angular
  slug: angular
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: UI
  slug: ui
seo_title: null
seo_desc: 'By Mark Grichanik

  Angular is a great framework and can be used for developing large scale applications,
  but can be tricky to fine tune and achieve good load time and run-time performance.
  In this post, I’ll detail some best practices I have learned a...'
---

By Mark Grichanik

Angular is a great framework and can be used for developing large scale applications, but can be tricky to fine tune and achieve good load time and run-time performance. In this post, I’ll detail some best practices I have learned along the way, so you will not make the same mistakes I made.

### Change detection

Change detection is Angular’s mechanism to see if there are any values that have been changed and require the view to be updated. By default, Angular runs change detection with nearly every user interaction. In order to know if the view should be rendered again, Angular accesses the new updated value, compares it with the old one and makes the decision. As your application grows, it will include a lot of expressions, and having a change detection cycle on each one of them will cause a performance problem.

We can optimize things if we create a ‘dumb’ component with a certain attribute to handle the change detection cycles. This component relies only on non specific input data and in that way, we can tell Angular only to run change detection when an input changes or when we manually trigger it. When a reference type is immutable, every time the object is being updated, the reference on the stack memory will have to change. Now we can have a simple reference check on the object between the memory address and the stack. If the memory address has changed, then we check all the values. This will skip change detection in that component.

We need to keep in mind that primitive types such as numbers, booleans, strings, etc are passed by value. Objects, arrays and functions are also passed by value, but the value is a copy of a reference.

> You can look for more details on that [here](https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0).

And now we will see two examples of how this is implemented.

#### Example: _ChangeDetectionStrategy.Default_

**You don’t have to specify changeDetection type, it will be ‘ChangeDetectionStrategy.Default’ by default.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*CmTLsaZ6lBFG2nLr23UEnw.gif)
_Default change detection_

![Image](https://cdn-media-1.freecodecamp.org/images/0*M2e8BlgCZ2xEY51A)
_Photo by [Unsplash](https://unsplash.com/@timmossholder?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Tim Mossholder</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### ChangeDetectionStrategy.OnPush

In order to use the OnPush change detection, we need to modify the child component from the first example.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2H5bcmDVupujYig-KKUNTQ.gif)
_OnPush change detection_

### Minimize DOM manipulations

If you have some list of data that was retrieved from some server and you need to show it, you are probably using the Angular directive, [**_ngFor_**](https://angular.io/api/common/NgForOf)**_._** Angular will create a new template for you for each item in that list.

If at some point some of the data has been changed, Angular can’t really know that and will replace the whole list, instead of just the items that were changed. In order to improve that, Angular provide us with the `trackBy` function.`trackBy` takes a function which has two arguments: `index` and `[item](https://angular.io/api/core/IterableChangeRecord#item)`. If `trackBy` is given, Angular tracks changes by the return value of the function.

Syntax:

Most common use is just to return the index itself or item.id as a unique identifier for the item: `trackByFn(index, item){ return item.id; }`.

With that, Angular can track which items have been added or removed according to the unique identifier and create or destroy only the things that were changed.

### Avoid using methods in your template

While it is very convenient to use methods in Angular templates, Angular will recalculate them on each change detection. For larger lists it will affect rendering time and the application may even get stuck due to huge memory consumption. In the following example, Angular will run `getNumberOfCars` on each change detection cycle (ie upon adding a new row).

How can we handle this situation? We can pre-compute the results and then just access the data we have computed. In our example, we can add a new attribute to the person object, vehiclesNumber, which holds in advance the amount of vehicles each person has. The other way to do this is by implementing the method getNumberOfCars as a pure pipe.

According to [Angular pipe documentation](https://angular.io/guide/pipes):

> Angular executes a _pure pipe_ only when it detects a _pure change_ to the input value. A pure change is either a change to a primitive input value (`String`, `Number`, `Boolean`, `Symbol`) or a changed object reference (`Date`, `Array`, `Function`, `Object`).

> Angular ignores changes within (composite) objects.

> This may seem restrictive but it’s also fast. An object reference check is fast — much faster than a deep check for differences — so Angular can quickly determine if it can skip both the pipe execution and a view update.

The pipe will still be executed on each change detection cycle. However, if a pipe is executed more than once with the same parameters, the results of the first execution are returned. Meaning, Angular will cache the results for better performance.

Let’s see an example.

Without a pipe:

![Image](https://cdn-media-1.freecodecamp.org/images/1*E10fN3t0GC2PvG6cvhkhRw.gif)

While with a pipe we will get:

We can see it will recalculate only on the new data, instead of the whole list.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1u5T_iGl9h5uM-TBF5uzYg.gif)

### Use Prod flag in production

It will disable Angular’s development mode, which turns off assertions and other checks within the framework. This will also increase your performance. You can find more details [here](https://angular.io/api/core/enableProdMode).

### Don’t use console.log in production code

console.log prints can really slow down your application, as it takes some time to compute what you want to print. Also, for long information it will also consume some more time for the printing process.

### Don’t forget to unsubscribe from your observables

Your subscription holds a reference to your component instance. If you will not unsubscribe from it, the instance will not be cleared by the garbage collector which will cause a memory leak. You can unsubscribe easily by using `ngOnDestory(){this.subscription.unsubscribe();}`. You can read more about it [here](https://angular.io/guide/observables).

### Final Words

If you run into any issues, feel free to drop me a line at : [_markgrichanik[at]gmail[dot]com_](mailto:markgrichanik@gmail.com).

I would also love to hear any feedback/tips you have while working on large scale applications with Angular.

> If you liked this article, ? away so that others can read it as well

