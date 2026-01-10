---
title: Angular Views, Routing, and NgModules Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T21:22:00.000Z'
originalURL: https://freecodecamp.org/news/angular-vs-angularjs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e1f740569d1a4ca3b6e.jpg
tags:
- name: Angular
  slug: angular
- name: Angular
  slug: angularjs
seo_title: null
seo_desc: "Angular vs AngularJS\nAngularJS (versions 1.x) is a JavaScript-based open\
  \ source framework. It is cross platform and is used to develop Single Page Web\
  \ Application (SPWA). \nAngularJS implements the MVC pattern to separate the logic,\
  \ presentation, and ..."
---

## Angular vs AngularJS

AngularJS (versions 1.x) is a JavaScript-based open source framework. It is cross platform and is used to develop Single Page Web Application (SPWA). 

AngularJS implements the MVC pattern to separate the logic, presentation, and data components. It also uses dependency injection to make use of server-side services in client side applications.

Angular (versions 2.x and up) is a Typescript-based open source framework used to develop front-end web applications. Angular has the following features like generics, static-typing, dynamic loading, and also some ES6 features.

## **Version History**

Google released the initial version of AngularJS on October 20,2010. The first stable release of AngularJS was on December 18, 2017 of version 1.6.8. 

The Angular 2.0 release took place on September 22 2014 at the ng-Europe conference. 

After some modifications, Angular 4.0 was released in December 2016. Angular 4 is backward compatible with Angular 2.0. The HttpClient library is one of the new features of Angular 4.0. 

Angular 5 release was on November 1, 2017. Support for progressive web apps (PWAs)  was one of the improvements to Angular 4.0. 

And finally, Angular 6 was released in May 2018. The latest stable version is [6.1.9](https://blog.angular.io/angular-v6-1-now-available-typescript-2-9-scroll-positioning-and-more-9f1c03007bb6)

## How to install it

We can add Angular either by referencing the sources available or downloading the framework.

### Link To Source

AngularJS: We can add AngularJS (Angular 1.x versions) by referencing the Content Delivery Network from Google.

```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js"></script> 
```

Download/install: We can download the framework with npm, Bower, or composer

**Angular**JS **1.x**:

npm

```shell
npm install angular
```

Then add a `<script>` to your `index.html`:

```html
<script src="/node_modules/angular/angular.js"></script>
```

bower

```shell
bower install angular
```

Then add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular/angular.js"></script>
```

**Angular:**

For more information regarding the documentation, refer to the official site of [AngularJS](https://docs.angularjs.org/api).

You can install **Angular 2.x** and other versions by following the steps from the official documentation of [Angular](https://angular.io/guide/quickstart).

Now let's learn a bit more about Angular, shall we?

# **Introduction**

Views offer a necessary layer of abstraction. They keep Angular independent of platform specific utilities. As a cross-platform technology, Angular uses its views to connect with the platform.

For every element in Angular’s template HTML, there is a corresponding view. Angular recommends interacting with the platforms through these views. While direct manipulation is still possible, Angular warns against it. Angular offers its own application programming interface (API) to replace the native manipulations.

Shunning views for platform-specific API has its consequences. When developing Angular in a web browser, elements exist in two places: the DOM and the view. Messing only with the DOM does not impact the view.

Since Angular does not interface with the platform, this creates a discontinuity. Views should mirror the platform one-to-one. Otherwise Angular wastes resources managing elements that mismatch it. This is terrible in the event of deleted elements.

These sorts of discrepancies make views appear unnecessary. Never forget that Angular is a universal development platform above all. Views are a necessary abstraction for this end.

By adhering to views, Angular applications will function across all supported development platforms. Platforms include the Web, Android, and Apple iOS.

#### **Note**

From here-on, this article assumes a web browser environment. Feel free to mentally replace the DOM with something more applicable to your preferred platform.

## What are Views?

Views are almost like their own virtual DOM. Each view contains a reference to a corresponding section of the DOM. Inside a view are nodes that mirror what is in the this section. Angular assigns one view node per DOM element. Each node holds a reference to a matching element.

When Angular checks for changes, it checks the views. Angular avoids the DOM under the hood. The views reference the DOM on its behalf. Other mechanisms are in place to ensure that view changes render to the DOM. Conversely, changes to the DOM do not affect the views.

Again, views are common across all development platforms besides the DOM. Even if developing for one platform, views are still considered best practice. They guarantee Angular has a correct interpretation of the DOM.

Views may not exist on third-party libraries. Direct DOM manipulation is an escape hatch for this kind of scenario. Granted, do not expect the application to function cross-platform.

### Types of Views

There are two main types of views: embedded and host.

There also exists view containers. They hold embedded and host views and are often referred to as simple “views”.

Every `@Component` class registers a view container (view) with Angular. New components generate a custom selector targeting a certain DOM element. The view attaches to that element wherever it appears. Angular now knows the component exists looking at the view model.

Host views attach to components created dynamically with factories. Factories provide a blueprint for view instantiation. That way the application can instantiate the component’s host view during runtime. A host view attaches to a component’s wrapper per its instantiation. This view stores data describing conventional component capabilities.

`<ng-template></ng-template>` is a akin to the HTML5 `<template></template>` element. Angular’s `ng-template` works with embedded views. These views do not attach to DOM elements unlike host views. They are identical to host views in that they both types exist inside of view containers.

Keep in mind, `ng-template` is not a DOM element. It gets commented out later leaving nothing but the embedded view nodes behind.

The difference depends on input data; embedded views store no component data. They store a series of elements as nodes comprising its template. The template makes up all the innerHTML of `ng-template`. Each element within the embedded view is its own separate view node.

### Host Views and Containers

Host views _host_ dynamic components. View containers (views) attach automatically to elements already in the template. Views can attach to any element beyond what is unique to component classes.

Think of the traditional method of component generation. It begins by creating a class, decorating it with `@Component`, and filling in metadata. This approach occurs for any pre-defined component element of the template.

Try using the Angular command-line interface (CLI) command: `ng generate component [name-of-component]`. It yields the following.

```typescript
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-example',
  templateUrl: './example.component.html',
  styleUrls: ['./example.component.css']
})
export class ExampleComponent implements OnInit {
  constructor() { }

  ngOnInit() { }
}
```

This creates the component with the selector `app-example`. This attaches a view container to `<app-example></app-example>` in the template. If this were the root of the application, its view would encapsulate all other views. The root view marks the beginning of the application from Angular’s perspective.

Creating components dynamically and registering them in the Angular view model takes a few extra steps. Structural directives help manage dynamic content (`*ngIf, *ngFor, and *ngSwitch…`). Directives do not scale to bigger applications however. Too many structural directives complicates the template.

This is where instantiating components from existing class logic comes in handy. These components need to create a host view that can insert into the view model. Host views holds data for components so that Angular recognizes their structural purpose.

### Host Views Continued

Every component has a class definition. Yet JavaScript does not support classes. Classes are syntactic sugar. They produce functions containing component factories instead.

Factories act as blueprints for host views. They build views to interface with Angular on behalf of their components. Host views attach to DOM elements. Technically any element is OK but the most common target is `<ng-component></ng-component>`.

A view container (view) for holding views must first exist. `<ng-container></ng-container>` is a great place to attach a view container. View containers are the same type of views that also apply to template class elements.

A few helpers and references from `@angular/core` provide the other needed utilities. The following example puts it all together.

```typescript
// another.component.ts

import { Component } from '@angular/core';

@Component({
  template: `
  <h1>Another Component Content</h1>
  <h3>Dynamically Generated!</h3>
  `
})
export class AnotherComponent { }
```

```typescript
// example.component.ts

import { AfterViewInit, Component, ViewChild,
ViewContainerRef, ComponentFactoryResolver } from '@angular/core';
import { AnotherComponent } from './another.component';

@Component({
  selector: 'app-example',
  template: `
  <h1>Application Content</h1>
  <ng-container #container></ng-container>
  <h3>End of Application</h3>
  `,
  entryComponents: [ AnotherComponent ]
})
export class ExampleComponent implements AfterViewInit {
  @ViewChild("container", { read: ViewContainerRef }) ctr: ViewContainerRef;

  constructor(private resolve: ComponentFactoryResolver) { }

  ngAfterViewInit() {
    const factory = this.resolve.resolveComponentFactory(AnotherComponent);
    this.ctr.createComponent(factory);
  }
}
```

Assume AnotherComponent and ExampleComponent are both declared under the same module. AnotherComponent is a simple class component dynamically added into ExampleComponent’s view. ExampleComponent’s `entryComponents` metadata must contain AnotherComponent for [bootstrapping](https://angular.io/guide/bootstrapping).

While ExampleComponent is a part of the template, AnotherComponent remains detached. It dynamically renders into the template from ExampleComponent.

There are two view containers present: `<app-example></app-example>` and `<ng-container></ng-container>`. The host view for this example will insert into `ng-container`.

The `AfterViewInit` lifecycle hook fires after the `@ViewChild` queries complete. Using the _template reference variable_ `#container`, the `@ViewChild` references `ng-container` as `ctr`.

`ViewContainerRef` is the type of reference for view containers (views). `ViewContainerRef` references a view that supports the insertion of other views. `ViewContainerRef` contains more methods for managing its contained views.

Through dependency injection, the constructor instantiates an instance of Angular’s `ComponentFactoryResolver` service. This service extracts the the factory function (host view blueprint) of AnotherComponent.

The single argument of `createComponent` requires a factory. The `createComponent` function derives from `ViewContainerRef`. It instantiates AnotherComponent under a host view derived from the component’s factory.

The host view then inserts into the view container. `<ng-component></ng-component>` wraps the component inside of the view container. It has attached to it the aforementioned host view. `ng-component` is the host view’s connection with the DOM.

There are other ways create a host view dynamically from a component. Other ways often [focus on optimization](https://blog.angularindepth.com/working-with-dom-in-angular-unexpected-consequences-and-optimization-techniques-682ac09f6866).

The `ViewContainerRef` holds a powerful API. It can manage any number of views either host or embedded within its view. The API includes view operations such as insert, move, and delete. This lets you manipulate the DOM through Angular’s view model. This is best practice so that Angular and the DOM match each other.

### Embedded Views

Note: embedded views attach to other views no added input. Host views attach to a DOM element with input data from its host view describing it as a component.

Structural directives create an [`ng-template` surrounding a chunk of HTML content](https://angular.io/guide/structural-directives#the-asterisk--prefix). The directive’s host element has a view container attached. This make it so that the content can conditionally render into its intended layout.

The `ng-template` holds embedded view nodes representing each element within its innerHTML. `ng-template` is by no means a DOM element. It comments itself out. The tags define the extend of its embedded view.

### Embedded Views Continued

Instantiating an embedded view requires no external resources beyond its own reference. The `@ViewChild` query can fetch that.

With the template reference, calling `createEmbeddedView` from it does the trick. The innerHTML of the reference becomes its own embedded view instance.

In the next example, `<ng-container></ng-container>` is a view container. `ng-container` gets commented out during compilation just like `ng-template`. Thus it provides an outlet for inserting the embedded view while keeping the DOM lean.

The embedded view template inserts at the layout location of `ng-container`. This newly inserted view has no additional view encapsulation besides the view container. Remember how that differs from host views (host views attach to their `ng-component` element wrapper).

```typescript
import { Component, AfterViewInit, ViewChild,
ViewContainerRef, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-example',
  template: `
  <h1>Application Content</h1>
  <ng-container #container></ng-container> <!-- embed view here -->
  <h3>End of Application</h3>

  <ng-template #template>
    <h1>Template Content</h1>
    <h3>Dynamically Generated!</h3>
  </ng-template>
  `
})
export class ExampleComponent implements AfterViewInit {
  @ViewChild("template", { read: TemplateRef }) tpl: TemplateRef<any>;
  @ViewChild("container", { read: ViewContainerRef }) ctr: ViewContainerRef;

  constructor() { }

  ngAfterViewInit() {
    const view =  this.tpl.createEmbeddedView(null);
    this.ctr.insert(view);
  }
}
```

`@ViewChild` queries for the _template reference variable_ `#template`. This provides a template reference of type `TemplateRef`. `TemplateRef` holds the `createEmbeddedView` function. It instantiates the template as an embedded view.

The single argument of `createEmbeddedView` is for context. If you wanted to pass in additional metadata, you could do it here as an object. The fields should match up with the `ng-template` attributes (`let-[context-field-key-name]=“value”`). Passing `null` indicates no extra metadata is necessary.

A second `@ViewChild` query provides a reference to `ng-container` as a `ViewContainerRef`. Embedded views only attach to other views, never the DOM. The `ViewContainerRef` references the view that takes in the embedded view.

An embedded view may also insert into the component view of `<app-example></app-example>`. This approach positions the view at the very end of ExampleComponent’s view. In this example however, we want the content to show up in the very middle where `ng-container` sits.

The `ViewContainerRef` `insert` function _inserts_ the embedded view into the `ng-container`. The view content shows ups in the intended location right in the middle of ExampleComponent’s view.

## Conclusion

Manipulating the DOM with platform specific methods is not recommended. Creating and managing a tight set of views keeps Angular and the DOM on the same page. Updating the views informs Angular of the current state of the DOM. Updates to the views also carry over into what the DOM displays.

Angular provides a flexible API for view interaction. Developing platform independent applications is possible thanks to this level of abstraction. Of course, the temptation to fallback on platform dependent strategies persists. Unless you have a very good reason not to, try to stick with the views API Angular provides. This will yield predictable results across all platforms.

# **Routing in Angular**

Routing is essential. Many modern web applications host too much information for one page. Users should not have to scroll through an entire application’s worth of content either. An application needs to split itself into distinguishable sections.

Users prioritize necessary information. Routing helps them find the application section with such information. Any other information useful to other users may exist on an entirely separate route. With routing, both users can find what they need quickly. Irrelevant details stay obscured behind irrelevant routes.

Routing excels at sorting and restricting access to application data. Sensitive data should never display to unauthorized users. Between every route the application may intervene. It can examine a user’s session for authentication purposes. This examination determines what the route renders if it should render at all. Routing gives developers the perfect chance to verify a user before proceeding.

Creating a list of routes promotes organization as well. In terms of development, it keeps the developer thinking in distinguishable sections. Users benefit from this too, but more-so developers when navigating the application code. A list of programmatic routers paints an accurate model of the application’s front end.

As for Angular, routing takes up its own entire library within the framework. All modern front-end frameworks support routing, and Angular is no different. Routing happens from the client-side using either hash or location routing. Both styles allow the client to manage its own routes. No additional assistance from the server is necessary past the initial request.

The web browser rarely refreshes using client-side routing. Web browser utilities such as bookmarks, history, and the address bar still work despite no refreshing. This makes for a slick routing experience that does not mess up the browser. No more jumpy page reloads while routing to a different page.

Angular adds on a layer of abstraction over the core technologies used for routing. This article intends to explain this abstraction. There exists two routing strategies in Angular: path location and hash. This article focuses on the path location strategy since its the default option.

Plus, path location may deprecate hash routing following the full release of [Angular Universal](https://universal.angular.io/). Regardless, the two strategies are very similar in implementation. Learning one learns the other. Time to get started!

## RouterModule Setup

Routing utilities export with `RouterModule` available from `@angular/router`. It is not part of the core library since not all applications require routing. The most conventional way to introduce routing is as its own [feature module](https://angular.io/guide/feature-modules).

As route complexity grows, having it as its own module will promote the root module’s simplicity. Keeping it stupid simple without compromising functionality constitutes good design for modules.

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AComponent } from '../../components/a/a.component';
import { BComponent } from '../../components/b/b.component';

// an array of soon-to-be routes!
const routes: Routes = [];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
```

`.forRoot(...)` is a class function available from the RouterModule class. The function accepts an array of `Route` objects as `Routes`. `.forRoot(...)` configures routes for eager-loading while its alternative `.forChild(...)` configures for lazy-loading.

Eager-loading meaning the routes load their content into the application from the get-go. Lazy-loading happens on-demand. The focus of this article is eager-loading. It is the default approach for loading in an application. The RouterModule class definition looks something like the next block of code.

```typescript
@NgModule({
  // … lots of metadata ...
})
export class RouterModule {
  forRoot(routes: Routes) {
    // … configuration for eagerly loaded routes …
  }

  forChild(routes: Routes) {
    // … configuration for lazily loaded routes …
  }
}
```

Do not worry about the configuration details the example omits with comments. Having a general understanding will do for now.

Notice how AppRoutingModule imports the RouterModule while also exporting it. This makes sense given AppRoutingModule is a feature module. It imports into the root module as a feature module. It exposes RouterModule directives, interfaces, and services to the root component tree.

This explains why AppRoutingModule must export RouterModule. It does so for the sake of the root module’s underlying component tree. It needs access to those routing utilities!

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AComponent } from './components/a/a.component';
import { BComponent } from './components/b/b.component';
import { AppRoutingModule } from './modules/app-routing/app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    AComponent,
    BComponent
  ],
  imports: [
    AppRoutingModule, // routing feature module
    BrowserModule
  ],
  providers: [],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
```

The AppRoutingModule token imports from the very top. Its token inserts into the root module’s imports array. The root component tree may now utilize the RouterModule library. That includes its directives, interfaces, and services as already mentioned. Big thanks goes to AppRoutingModule for exporting RouterModule!

The RouterModule utilities will come in handy for the root’s components. The basic HTML for AppComponent makes use of one directive: `router-outlet`.

```html
<!-- app.component.html -->

<ul>
  <!-- routerLink(s) here -->
</ul>
<router-outlet></router-outlet>
<!-- routed content appends here (AFTER THE ELEMENT, NOT IN IT!) -->
```

`routerLink` is an attribute directive of RouterModule. It will attach to each element of `<ul></ul>` once the routes are setup. `router-outlet` is a component directive with interesting behavior. It acts more as a marker for displaying routed content. Routed content results from navigation to a specific route. Usually that means a single component as configured in AppRoutingModule

The routed content renders right after `<router-outlet></router-outlet>`. Nothing renders inside of it. This does not make too much of a considerable difference. That said, do not expect `router-outlet` to behave like a container for routed content. It is merely a marker for appending routed content to the Document Object Model (DOM).

## Basic Routing

The previous section establishes the basic setup for routing. Before actual routing can happen, a few more things must be addressed

The first question to address is what routes will this application consume? Well, there are two components: AComponent and BComponent. Each one should have its own route. They can render from AppComponent’s `router-outlet` depending on the current route location.

The route location (or path) defines what appends to a [website’s origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin) (e.g. [http://localhost:4200](http://localhost:4200/)) through a series of slashes (`/`).

```typescript
// … same imports from before …

const routes: Routes = [
  {
    path: 'A',
    component: AComponent
  },
  {
    path: 'B',
    component: BComponent
  }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
```

`http://localhost:4200/A` renders AComponent from AppComponent’s `router-outlet`. `http://localhost:4200/B` renders BComponent. You need a way to route to these locations without using the address bar though. An application should not rely upon a web browser’s address bar for navigation.

_The global CSS (Cascading Style-sheets) supplements the HTML below it. An application’s router link ought to have a pleasant appearance. This CSS applies to all other examples too._

```css
/* global styles.css */

ul li {
  cursor: pointer;
  display: inline-block;
  padding: 20px;
  margin: 5px;
  background-color: whitesmoke;
  border-radius: 5px;
  border: 1px solid black;
}

ul li:hover {
  background-color: lightgrey;
}
```

```html
<!-- app.component.html -->

<ul>
  <li routerLink="/A">Go to A!</li>
  <li routerLink="/B">Go to B!</li>
</ul>
<router-outlet></router-outlet>
```

This is basic routing! Clicking either of the routerLink elments routes the web address. It reassigns it without refreshing the web browser. Angular’s `Router` maps the routed address to the `Routes` configured in AppRoutingModule. It matches the address to the `path` property of a single `Route` object within the array. First match always wins, so match-all routes should lie at the very end of the `Routes` array.

Match-all routes prevent the application from crashing if it cannot match the current route. This can happen from the address bar where the user may type in any route. For this, Angular provides a wildcard path value `**` that accepts all routes. This route usually renders a PageNotFoundComponent component displaying “Error 404: Page not found”.

```typescript
// … PageNotFoundComponent imported along with everything else …

const routes: Routes = [
  {
    path: 'A',
    component: AComponent
  },
  {
    path: 'B',
    component: BComponent
  },
  {
    path: '',
    redirectTo: 'A',
    pathMatch: 'full'
  },
  {
    path: '**',
    component: PageNotFoundComponent
  }
];
```

The `Route` object containing `redirectTo` keeps the PageNotFoundComponent from rendering as a result of `http://localhost:4200`. This is the applications home route. To fix this, `redirectTo` reroutes the home route to `http://localhost:4200/A`. `http://localhost:4200/A` indirectly becomes the application’s new home route.

The `pathMatch: 'full'` tells the `Route` object to match against the home route (`http://localhost:4200`). It matches the empty path.

These two new `Route` objects go at the end of the array since first match wins. The last array element (`path: '**'`) always matches, so it goes last.

There is one last thing worth addressing before moving on. How does the user know where he or she is in the application relative to the current route? Sure there may be content specific to the route, but how is user supposed to make that connection? There should be some form of highlighting applied to the routerLinks. That way, the user will know which route is active for the given web page.

This is an easy fix. When you click a `routerLink` element, Angular’s `Router` assigns _focus_ to it. This focus can trigger certain styles which provide useful feedback to the user. The `routerLinkActive` directive can track this focus for the developer.

```html
<!-- app.component.html -->

<ul>
  <li routerLink="/A" routerLinkActive="active">Go to A!</li>
  <li routerLink="/B" routerLinkActive="active">Go to B!</li>
</ul>
<router-outlet></router-outlet>
```

The right assignment of `routerLinkActive` represents a string of classes. This example portrays only one class (`.active`), but any number of space-delimited classes may apply. When the `Router` assigns _focus_ to a routerLink, the space-delimited classes apply to the host element. When the focus shifts away, the classes get removed automatically.

```css
/* global styles.css */

.active {
  background-color: lightgrey !important;
}
```

Users can now easily recognize how the current route and the page content coincide. `lightgrey` highlighting applies to the routerLink matching the current route. `!important` ensures the highlighting overrides inline stylings.

## Parameterized Routes

Routes do not have to be completely hard-coded. They can contain dynamic variables referenceable from the component corresponding the `Route` object. These variables are declared as parameters when writing the route’s path.

Route parameters are either optional or mandatory for matching a particular `Route`. It depends on how a route writes its parameters. Two strategies exist: matrix and traditional parameterization.

Traditional parameterization begins from the `Routes` array configured in AppRoutingModule.

```typescript
const routes: Routes = [
  // … other routes …
  {
    path: 'B',
    component: BComponent
  },
  {
    path: 'B/:parameter',
    component: BComponent
  },
  // … other routes …
];
```

Focus on the two BComponent routes. Parameterization will eventually occur in both routes.

Traditional parameterization occurs in the second BComponent `Route`. `B/:parameter` contains the `parameter` parameter as indicated with the `:`. Whatever follows the colon marks the parameter’s name. The `parameter` parameter is necessary for the second BComponent `Route` to match.

`parameter` reads in the value of whatever gets passed into the route. Routing to `http://localhost:4200/B/randomValue` will assign `parameter` the value of `randomValue`. This value can include anything besides another `/`. For example, `http://localhost:4200/B/randomValue/blahBlah` will not trigger the second BComponent `Route`. The PageNotFoundComponent renders instead.

BComponent can reference route parameters from its component class. Both approaches to parameterization (matrix and traditional) yield the same results in BComponent. Before seeing BComponent, examine the matrix form of parameterization below.

```typescript
// app.component.ts

import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  constructor(private router: Router) { }

  routeMatrixParam(value: string) {
    if (value)
      this.router.navigate(['B', { parameter: value }]); // matrix parameter
    else
      this.router.navigate(['B']);
  }

  routeAddressParam(value: string) {
    this.router.navigate(['B', value]);
  }
}
```

Angular’s dependency injection system provides an instantiation of the `Router`. This lets the component programmatically route. The `.navigate(...)` function accepts an array of values that resolves to a _routable_ path. Something like `.navigate(['path', 'to', 'something'])` resolves to `http://localhost:4200/path/to/something`. `.navigate(...)` adds path-delimiting `/` marks when normalizing the array into a _routable_ path.

The second form of parameterization occurs in `routeMatrixParam(...)`. See this line of code: `this.router.navigate(['B', { parameter: value }])`. This form of `parameter` is a matrix parameter. Its value is optional for the first BComponent `Route` to match (`/B`). The `Route` matches regardless of the parameter’s presence in the path.

The `routeAddressParam(...)` resolves a route that matches the `http://localhost:4200/B/randomValue` parameterization approach. This traditional strategy needs a parameter to match the second BComponent route (`B/:parameter`).

The matrix strategy concerns `routeMatrixParam(...)`. With or without a matrix parameter in its path, the first BComponent route still matches. The `parameter` parameter passes to BComponent just like with the traditional approach.

To make full sense of the above code, here is the corresponding template HTML.

```html
// app.component.html

<ul>
  <li routerLink="/A">Go to A!</li>
  <li>
    <input #matrixInput>
    <button (click)="routeMatrixParam(matrixInput.value)">Matrix!</button>
  </li>
  <li>
    <input #paramInput>
    <button (click)="routeAddressParam(paramInput.value)">Param!</button>
  </li>
</ul>
<router-outlet></router-outlet>
```

In the template, values are accepted as text input. The input injects it into the route path as a parameter. Two separate sets of boxes exist for each parameterization strategy (traditional and matrix). With all the pieces coming together, it is time to examine the BComponent component class.

```typescript
// b.component.ts

import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-b',
  template: `
  <p>Route param: {{ currParam }}</p>
  `
})
export class BComponent implements OnInit {
  currParam: string = "";

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.params.subscribe((param: ParamMap) => {
      this.currParam = param['parameter'];
    });
  }
}
```

BComponent results from either of two BComponent routes in AppRoutingModule. `ActivatedRoute` instantiates into a set of useful information pertaining to the current route. That is, the route that caused BComponent to render. `ActivatedRoute` instantiates via dependency injection targeting the class constructor.

The `.params` field of `ActivatedRoute.params` returns an `Observable` which emits the route parameters. Notice how the two different parameterization approaches result in the `parameter` parameter. The returned `Observable` emits it as a key-value pair inside of a `ParamMap` object.

Between the two parameterization approaches, the `parameter` parameter resolved identically. The value emits from `ActivatedRoute.params` despite the approach to parameterization.

The address bar distinguishes the final results of each approach. Matrix parameterization (optional for `Route` match) yields the address: `http://localhost:4200/B;parameter=randomValue`. Traditional parameterization (required for `Route` match) yields: `http://localhost:4200/B/randomValue`.

Either way, the same BComponent results. The actual difference: a different BComponent `Route` matches. This entirely depends upon the parameterization strategy. The matrix approach ensures parameters are optional for `Route` matching. The traditional approach requires them.

## Nested Routes

`Routes` may form a hierarchy. In the DOM, this involves one parent `router-outlet` rendering at least one child `router-outlet`. In the address bar, it looks like this: `http://localhost/parentRoutes/childRoutes`. In the `Routes` configuration, the `children: []` property denotes a `Route` object as having nested (child) routes.

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { NestComponent } from '../../components/nest/nest.component';
import { AComponent } from '../../components/nest/a/a.component';
import { BComponent } from '../../components/nest/b/b.component';

const routes: Routes = [
  {
    path: 'nest',
    component: NestComponent,
    children: [
      { path: 'A', component: AComponent },
      { path: 'B', component: BComponent }
    ]
  }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule { }
```

```typescript
// nest.component.ts

import { Component } from '@angular/core';

@Component({
  selector: 'app-nest',
  template: `
  <ul>
    <li routerLink="./A">Go to A!</li>
    <li routerLink="./B">Go to B!</li>
  </ul>
  <router-outlet></router-outlet>
  `
})
export class NestComponent { }
```

NestComponent renders a `router-outlet` after rendering itself from another root-level `router-outlet` in AppComponent. The `router-outlet` of NestComponent’s template may render either AComponent (`/nest/A`) or BComponent (`/nest/B`).

The AppRoutingModule reflects this nesting in NestComponent’s `Route` object. The `children: []` field holds an array of `Route` objects. These `Route` object may also nest routes in their `children: []` fields. This can continue for however many layers of nested routes. The above example shows two layers of nesting.

Each `routerLink` contains a `./` as compared to `/`. The `.` ensures that the routerLink appends to the route path. The routerLink completely replaces the path otherwise. After routing to `/nest`, `.` expands into `/nest`.

This is useful for routing to either `/nest/A` or `/nest/B` from the `.nest` route. `A` and `B` constitute nested routes of `/nest`. Routing to `/A` or `/B` returns PageNotFound. `/nest` must prepend the two routes.

Take a look at the AppComponent containing the root-level `router-outlet` in its template. AppComponent is the first layer of nesting while NestComponent is the second.

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
  <ul>
    <li routerLink="/nest">Go to nested routes!</li>
    <li routerLink="/">Back out of the nested routes!</li>
  </ul>
  <router-outlet></router-outlet>
  `
})
export class AppComponent { }
```

Inside the nest `Route` object, the `children: []` contains two more nested routes. They result in AComponent and BComponent when routing from `/nest` as previously discussed. These components are very simple for the sake of demonstration. `<li routerLink="/">...</li>` lets you navigate out of the nest routes to reset the example by navigating to the home route.

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-a',
  template: `
  <p>a works!</p>
  `
})
export class AComponent { }
```

```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-b',
  template: `
  <p>b works!</p>
  `
})
export class BComponent { }
```

The `children: []` array accepts `Route` object as elements. `children: []` can apply to any of these elements as well. The children of these elements can continue nesting. This pattern may continue for however many layers of nesting. Insert a `router-outlet` into the template for every layer of nested routing.

Routing techniques apply regardless of a `Route` object’s level of nesting. The parameterization techniques differ in only one aspect. Child routes can only access their parent’s parameters via `ActivatedRoute.parent.params`. `ActivatedRoute.params` targets the same level of nested routes. This excludes parent-level routes and their parameters.

`Route` guards are especially suited for nested routing. One `Route` object can restrict access to all its nested (child) routes.

## Guarded Routes

Web applications often consist of public and private data. Both types of data tend to have their own pages with _guarded_ routes. These routes allow/restrict access depending on the user’s privileges. Unauthorized users may interact with a guarded route. The route should block the user if he or she attempts to access its routed content.

Angular provides a bundle of authentication guards that can attach to any route. These methods trigger automatically depending on how the user interacts with the guarded route.

* `canActivate(...)` - fires when the user attempts to access a route
* `canActivateChild(...)` - fires when the user attempts to access a route’s nested (child) routes
* `canDeactivate(...)` - fires when the user attempts to leave a route

Angular’s guard methods are available from `@angular/router`. To help them authenticate, they may optionally receive a few parameters. Such parameters do not inject via dependency injection. Under the hood, each value gets passed in as an argument to the invoked guard method.

* `ActivatedRouteSnapshot` - available to all three
* `RouterStateSnapshot` - available to all three
* `Component` - available to `canDeactivate(...)`

`ActivatedRouteSnapshot` provides access to the route parameters of the guarded route. `RouterStateSnapshot` exposes the URL (uniform resource locator) web address matching the route. `Component` references the component rendered by the route.

To guard a route, a class implementing the guard methods needs to first exist as a service. The service can inject into AppRoutingModule to guard its `Routes`. The token value for the service may inject into any one `Route` object.

```typescript
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthService } from '../../services/auth.service';
import { UserService } from '../../services/user.service';

import { PrivateNestComponent } from '../../components/private-nest/private-nest.component';
import { PrivateAComponent } from '../../components/private-nest/private-a/private-a.component';
import { PrivateBComponent } from '../../components/private-nest/private-b/private-b.component';

const routes: Routes = [
  {
    path: 'private-nest',
    component: PrivateNestComponent,
    canActivate: [ AuthService ], // !!!
    canActivateChild: [ AuthService ], // !!!
    canDeactivate: [ AuthService ], // !!!
    children: [
      { path: 'private-A', component: PrivateAComponent },
      { path: 'private-B', component: PrivateBComponent }
    ]
  }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ],
  providers: [
    AuthService,
    UserService
  ]
})
export class AppRoutingModule { }
```

`canActivate`, `canActivateChild`, and `canDeactivate` implement from AuthService. The service implementation will be shown shortly alongside the UserService implementation.

UserService provides the information needed to authenticate a user. The AuthService guard method implementations perform the authentication. AppRoutingModule must include the two services into its providers array. This is so the module’s injector knows how to instantiate them.

Nested routes exist off of the `/private-nest` path. The `Route` object for `/private-nest` contains a few more new fields. Their names should look familiar as they mirror their corresponding guard methods.

Each field fires its namesake’s method implementation inside of the service when triggered. Any number of services can populate this array too. The method implementation of each service gets tested. They must return a boolean value or an `Observable` that emits a boolean value.

See the AuthService and UserService implementations below.

```typescript
// user.service.ts

import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

class TheUser {
  constructor(public isLoggedIn: boolean = false) { }

  toggleLogin() {
    this.isLoggedIn = true;
  }

  toggleLogout() {
    this.isLoggedIn = false;
  }
}

const globalUser = new TheUser();

@Injectable({
  providedIn: 'root'
})
export class UserService {
  theUser: TheUser = globalUser;

  constructor(private router: Router) { }

  get isLoggedIn() {
    return this.theUser.isLoggedIn;
  }

  login() {
    this.theUser.toggleLogin();
  }

  logout() {
    this.theUser.toggleLogout();
    this.router.navigate(['/']);
  }
}
```

The same instance of `TheUser` gets passed with each instantiation of UserService. `TheUser` provides access to `isLoggedIn` determining the user’s login status. Two other public methods let the UserService toggle the value of `isLoggedIn`. This is so the user can log in and out.

You can think of `TheUser` as a global instance. `UserService` is a instantiable interface that configures this global. Changes to `TheUser` from one `UserService` instantiation apply to every other `UserService` instance. `UserService` implements into AuthService to provide access to `isLoggedIn` of `TheUser` for authentication.

```typescript
import { Component, Injectable } from '@angular/core';
import { CanActivate, CanActivateChild, CanDeactivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

import { UserService } from './user.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService implements CanActivate, CanActivateChild, CanDeactivate<Component> {
  constructor(private user: UserService) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    if (this.user.isLoggedIn)
      return true;
    else
      return false;
  }

  canActivateChild(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    return this.canActivate(route, state);
  }

  canDeactivate(component: Component, route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    if (!this.user.isLoggedIn || window.confirm('Leave the nest?'))
      return true;
    else
      return false;
  }
}
```

AuthService implements every guard method imported from `@angular/router`. Each guard method maps to a corresponding field in the PrivateNestComponent’s `Route` object. An instance of UserService instantiates from the AuthService constructor. AuthService determines if a user may proceed using `isLoggedIn` exposed by UserService.

Returning `false` from a guard instructs the route to block the user from routing. A return value of `true` lets the user proceed to his route destination. If more than one service authenticates, they all must return true to permit access. `canActivateChild` guards the child routes of PrivateNestComponent. This guard method accounts for users bypassing PrivateNestComponent through the address bar.

Guard method parameters pass in automatically upon invocation. While the example does not make use of them, they do supply useful information from the route. The developer can use this information to help authenticate the user.

AppComponent also instantiates UserService for direct use in its template. The UserService instantiation of AppComponent and AuthService reference the same user class (`TheUser`).

```typescript
import { Component } from '@angular/core';

import { UserService } from './services/user.service';

@Component({
  selector: 'app-root',
  template: `
  <ul>
    <li routerLink="/private-nest">Enter the secret nest!</li>
    <li routerLink="/">Leave the secret nest!</li>
    <li *ngIf="user.isLoggedIn"><button (click)="user.logout()">LOGOUT</button></li>
    <li *ngIf="!user.isLoggedIn"><button (click)="user.login()">LOGIN</button></li>
  </ul>
  <router-outlet></router-outlet>
  `
})
export class AppComponent {
  constructor(private user: UserService) { }
}
```

UserService handles all the logic for AppComponent. AppComponent mostly concerns its template. A UserService does instantiate as `user` from the class constructor. `user` data determines the template’s functionality.

## Conclusions

Routing strikes a fine balance between organizing and restricting sections of the application. A smaller application such as a blog or tribute page may not require any routing. Even then, including a little bit of hash routing could not hurt. A user may only want to reference part of the page after all.

Angular applies its own routing library built on top of the HTML5 [history API](https://developer.mozilla.org/en-US/docs/Web/API/History_API). This API omits hash routing to instead use the `pushState(...)` and `replaceState(...)` methods. They change the web address URL without refreshing the page. The default path location routing strategy in Angular works this way. Setting `RouterModule.forRoot(routes, { useHash: true })` enables hash routing if preferred.

This article focused on the default path location strategy. Regardless of the strategy, many routing utilities are available to route an application. The `RouterModule` exposes these utilities through its exports. Basic, parameterized, nested, and guarded routes are all possible utilizing RouterModule.

# **NgModules**

Angular applications begin from the root NgModule. Angular manages an application’s dependencies through its module system comprised of NgModules. Alongside plain JavaScript modules, NgModules ensure code modularity and encapsulation.

Modules also provide a top-most level of organizing code. Each NgModule sections off its own chunk of code as the root. This module provides top-to-bottom encapsulation for its code. The entire block of code can then export to any other module. In this sense, NgModules act like gatekeepers to their own code blocks.

Angular’s documented utilities come from NgModules authored by Angular. No utility is available unless the NgModule that declares it gets included into the root. These utilities must also export from their host module so that importers can use them. This form of encapsulation empowers the developer to produce his or her own NgModules within the same file-system.

Plus, it makes sense to know why the Angular CLI (command-line interface) imports `BrowserModule` from `@angular/core`. This happens whenever a new app generates using the CLI command: `ng new [name-of-app]`.

Understanding the point of the implementation may suffice in most cases. However, understanding how the implementation wires itself to the root is even better. It all happens automatically by importing `BrowserModule` into the root.

### NgModule Decorator

Angular defines its modules by decorating a generic class. The `@NgModule` decorator indicates the class’ modular purpose to Angular. An NgModule class consolidates root dependencies accessible/instantiable from the module’s scope. ‘Scope’ meaning anything originating from the module’s metadata.

```typescript
import { NgModule } from '@angular/core';

@NgModule({
  // … metadata …
})
export class AppModule { }
```

### NgModule Metadata

The CLI generated root NgModule includes the following metadata fields. These fields provide configuration to the code block upon which the NgModule presides.

* `declarations: []`
* `imports: []`
* `providers: []`
* `bootstrap: []`

### Declarations

The declarations array includes all components, directives, or pipes hosted by an NgModule. They are private to the module unless explicitly exported inside its metadata. Given this use-case, components, directives, and pipes are nicknamed ‘declarables’. An NgModule must declare a declarable uniquely. The declarable cannot declare twice in separate NgModules. An error gets thrown otherwise. See the below example.

```typescript
import { NgModule } from '@angular/core';
import { TwoComponent } from './components/two.component.ts';

@NgModule({
  declarations: [ TwoComponent ]
})
export class TwoModule { }

@NgModule({
  imports: [ TwoModule ],
  declarations: [ TwoComponent ]
})
export class OneModule { }
```

Angular throws an error for the sake of NgModule encapsulation. Declarables are private to the NgModule that declares them by default. If multiple NgModules need a certain declarable, they should import the declaring NgModule. This NgModule must then export the desired declarable so that the other NgModules can use it.

```typescript
import { NgModule } from '@angular/core';
import { TwoComponent } from './components/two.component.ts';

@NgModule({
  declarations: [ TwoComponent ],
  exports: [ TwoComponent ]
})
export class TwoModule { }

@NgModule({
  imports: [ TwoModule ] // this module can now use TwoComponent
})
export class OneModule { }
```

The above example will not throw an error. TwoComponent has been uniquely declared between the two NgModules. OneModule also has access to TwoComponent since it imports TwoModule. TwoModule in turn exports the TwoComponent for external use.

### Imports

The imports array only accepts NgModules. This array does not accept declarables, services, or anything else besides other NgModules. Importing a module provides access to what declarable the module publicizes.

This explains why importing `BrowserModule` provides access to its various utilities. Each declarable utility declared in `BrowserModule` exports from its metadata. Upon importing `BrowserModule`, those exported declarables become available to the importing NgModule. Services do not export at all since they lack the same encapsulation.

### Providers

The lack of service encapsulation might seem odd given the encapsulation of declarables. Remember that services go into the providers array separate from declarations or exports.

When Angular compiles, it flattens the root NgModule and its imports into one module. Services group together in a single providers array hosted by the merged NgModule. Declarables maintain their encapsulation through a set of compile-time flags.

If NgModule providers contain matching token values, the importing root module takes precedence. Past that, the last NgModule imported takes precedence. See the next example. Pay special attention to the NgModule importing the other two. Recognize how that affects the precedence of the provided service.

```typescript
import { NgModule } from '@angular/core';

@NgModule({
  providers: [ AwesomeService ], // 1st precedence + importing module
  imports: [
    BModule,
    CModule
  ]
})
export class AModule { }

@NgModule({
  providers: [ AwesomeService ]  // 3rd precedence + first import
})
export class BModule { }

@NgModule({
  providers: [ AwesomeService ]  // 2nd precedence + last import
})
export class CModule { }
```

Instantiating AwesomeService from within AModule’s scope results in an AwesomeService instance as provided in AModule’s metadata. If AModule’s providers omitted this service, the AwesomeService of CModule would take precedence. So and so forth for BModule if CModule’s providers omitted AwesomeService.

## Bootstrap

The bootstrap array accepts components. For each component of the Array, Angular inserts the component as its own root of the `index.html` file. The CLI-generated root NgModule of an application will always have this field.

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [ AppComponent ],
  imports: [ BrowserModule ],
  providers: [],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
```

AppComponent’s element will inject into the base-level HTML of the app (`index.html`). The rest of the component tree unfolds from there. The scope of the overarching NgModule covers this entire tree plus any others injected from the bootstrap array. The array usually contains only one element. This one component represents the module as a single element and its underlying tree.

## NgModules vs JavaScript Modules

You have seen Angular and JavaScript modules working together in the previous examples. The top-most `import..from` statements constitute the JavaScript module system. The file locations of each statement’s target must export a class, variable, or function matching the request. `import { TARGET } from './path/to/exported/target'`.

In JavaScript, modules are file-separated. Files import using the `import..from` keywords as just mentioned. NgModules, on the other hand, are class-separated and decorated with `@NgModule`. And so, many Angular modules can exist in a single file. This cannot happen with JavaScript since a file defines a module.

Granted, conventions say that each `@NgModule` decorated class should have its own file. Even so, know that files do not constitute their own modules in Angular. Classes decorated with `@NgModule` create that distinction.

JavaScript modules provide token references to `@NgModule` metadata. This happens at the top of a file hosting a NgModule class. NgModule uses these tokens inside of its metadata fields (declarables, imports, providers, etc). The only reason `@NgModule` can decorate a class in the first place is because JavaScript imports it from the top of the file.

```typescript
// JavaScript module system provides tokens
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { AppService } from './app.service';
// Javascript module system is strict about where it imports. It can only import at the top of files.

// Angular NgModule uses those tokens in its metadata settings
@NgModule({ // import { NgModule } from '@angular/core';
  declarations: [
    AppComponent // import { AppComponent } from './app.component';
  ],
  imports: [
    BrowserModule // import { BrowserModule } from '@angular/platform-browser';
  ],
  providers: [
    AppService // import { AppService } from './app.service';
  ],
  bootstrap: [
    AppComponent // import { AppComponent } from './app.component';
  ]
})
export class AppModule { }
// JavaScript module system exports the class. Other modules can now import AppModule.
```

The above example does not introduce anything new. The focus here is on the comments explaining how the two modular systems work together. JavaScript provides token references while NgModule uses those token to encapsulate and configure its underlying block of code.

### Feature Modules

Applications grow overtime. Scaling them properly requires application organization. A solid system for this will make further development much easier.

In Angular, schematics ensure purpose-driven sections of code remain distinguishable. Beyond the sub-NgModule schematics, there are the NgModules themselves. They are a type of schematic too. They stand above the rest in the list of schematics excluding the application itself.

The root module should not stand alone once an application starts to scale. Feature modules include any NgModule used alongside the root NgModule. You can think of the root module as having the `bootstrap: []` metadata field. Feature application ensure the root module does not oversaturate its metadata.

Feature modules isolate a section of code on behalf of any importing module. They can handle whole application sections independently. This means it could be used in any application whose root module imports the feature module. This tactic saves developers time and effort over the course of multiple applications! It keeps the application’s root NgModule lean as well.

In the root NgModule of an app, adding a feature module’s token into the root’s `imports` array does the trick. Whatever the feature module exports or provides becomes available to the root.

```typescript
// ./awesome.module.ts

import { NgModule } from '@angular/core';
import { AwesomePipe } from './awesome/pipes/awesome.pipe';
import { AwesomeComponent } from './awesome/components/awesome.component';
import { AwesomeDirective } from './awesome/directives/awesome.directive';

@NgModule({
  exports: [
    AwesomePipe,
    AwesomeComponent,
    AwesomeDirective
  ]
  declarations: [
    AwesomePipe,
    AwesomeComponent,
    AwesomeDirective
  ]
})
export class AwesomeModule { }
```

```typescript
// ./app.module.ts

import { AwesomeModule } from './awesome.module';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    AwesomeModule,
    BrowserModule
  ],
  providers: [],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
```

```typescript
// ./app.component.ts

import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
  <!-- AwesomeDirective -->
  <h1 appAwesome>This element mutates as per the directive logic of appAwesome.</h1>

  <!-- AwesomePipe -->
  <p>Generic output: {{ componentData | awesome }}</p>

  <section>
    <!-- AwesomeComponent -->
    <app-awesome></app-awesome>
  </section>
  `
})
export class AppComponent {
  componentData: string = "Lots of transformable data!";
}
```

`<app-awesome></app-awesome>` (component), `awesome` (pipe), and `appAwesome` (directive) are exclusive to AwesomeModule. Had it not exported these declarables or AppModule neglected to add AwesomeModule to its imports, then AwesomeModule’s declarables would not have been usable by AppComponent’s template. AwesomeModule is a feature module to the root NgModule AppModule.

Angular provides some its own modules that supplement the root upon their importation. This is due to these feature modules exporting what they create.

### Static module methods

Sometimes modules provide the option to be configured with a custom config object. This is achieved by leveraging static methods inside the module class.

An example of this approach is the `RoutingModule` which provides a `.forRoot(...)` method directly on the module.

To define your own static module method you add it to the module class using the `static` keyword. The return type has to be `ModuleWithProviders`.

```ts
// configureable.module.ts

import { AwesomeModule } from './awesome.module';
import { ConfigureableService, CUSTOM_CONFIG_TOKEN, Config } from './configurable.service';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


@NgModule({
  imports: [
    AwesomeModule,
    BrowserModule
  ],
  providers: [
    ConfigureableService
  ]
})
export class ConfigureableModule { 
  static forRoot(config: Config): ModuleWithProviders {
    return {
        ngModule: ConfigureableModule,
        providers: [
            ConfigureableService,
            {
                provide: CUSTOM_CONFIG_TOKEN,
                useValue: config
            }
        ]
    };
  }
}
```

```ts
// configureable.service.ts

import { Inject, Injectable, InjectionToken } from '@angular/core';

export const CUSTOM_CONFIG_TOKEN: InjectionToken<string> = new InjectionToken('customConfig');

export interface Config {
  url: string
}

@Injectable()
export class ConfigureableService {
  constructor(
    @Inject(CUSTOM_CONFIG_TOKEN) private config: Config
  )
}
```

Notice that the object the `forRoot(...)` method returns is almost identical to the `NgModule` config.

The `forRoot(...)` method accepts a custom config object that the user can provide when importing the module.

```ts
imports: [
  ...
  ConfigureableModule.forRoot({ url: 'http://localhost' }),
  ...
]
```

The config is then provided using a custom `InjectionToken` called `CUSTOM_CONFIG_TOKEN` and injected in the `ConfigureableService`. The `ConfigureableModule` should be imported only once using the `forRoot(...)` method. This provides the `CUSTOM_CONFIG_TOKEN` with the custom config. All other modules should import the `ConfigureableModule` without the `forRoot(...)` method.

## NgModule Examples from Angular

Angular provides a variety of modules importable from `@angular`. Two of the most commonly imported modules are `CommonModule` and `HttpClientModule`.

`CommonModule` is actually a subset of `BrowserModule`. Both provide access to the `*ngIf` and `*ngFor` structural directives. `BrowserModule` includes a platform-specific installation for the web browser. `CommonModule` omits this installation. The `BrowserModule` should import into the root NgModule of a web application. `CommonModule` provides `*ngIf` and `*ngFor` to feature modules not requiring a platform installation.

`HttpClientModule` provides the `HttpClient` service. Remember that services go in the providers array of the `@NgModule` metadata. They are not declarable. During compilation, every NgModule gets consolidated into one single module. Services are not encapsulated unlike declarables. They are all instantiable through the root injector located alongside the merged NgModule.

Back to the point. Like any other service, `HttpClient` instantiates into a class through its constructor via dependency injection (DI). Using DI, the root injector injects an instance of `HttpClient` into the constructor. This service lets developers make HTTP requests with the service’s implementation.

The `HttpClient` implementation includes into the `HttpClientModule` providers array. As long as the root NgModule imports `HttpClientModule`, `HttpClient` will instantiate from inside the root’s scope as expected.

## Conclusion

Chances are you may have already taken advantage of Angular’s NgModules. Angular makes it very easy to throw a module into the root NgModule’s imports array. Utilities are often exported from the imported module’s metadata. Hence why its utilities suddenly become available upon importation within the root NgModule.

NgModules work closely with plain JavaScript modules. One provides token while one uses them for configuration. Their teamwork results in a robust, modular system unique to the Angular framework. It provides a new layer of organization above all other schematics excluding the application.

Hopefully this article furthers your understanding of NgModules. Angular can leverage this system even further for some of the more exotic use-cases. 

