---
title: Angular Upgrades That Will Improve Your Developer Experience
subtitle: ''
author: Brenda Chepkorir
co_authors: []
series: null
date: '2023-05-17T23:40:59.000Z'
originalURL: https://freecodecamp.org/news/angular-upgrades-to-improve-developer-experience
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-thisisengineering-3861958.jpg
tags:
- name: Angular
  slug: angular
seo_title: null
seo_desc: "When we talk about the Developer Experience, we're referring to the level\
  \ of difficulty a developer faces when completing essential tasks. \nFactors like\
  \ the complexity of a development framework or the absence of syntactic sugar in\
  \ a programming lang..."
---

When we talk about the [Developer Experience](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/), we're referring to the level of difficulty a developer faces when completing essential tasks. 

Factors like the complexity of a development framework or the absence of [syntactic sugar](https://www.techopedia.com/definition/10212/syntactic-sugar) in a programming language can negatively impact it.

A robust modern framework can be complex. But Angular wouldn’t be so beloved if it didn't get easier to use with each new version. 

Versions 14, 15, and 16 have many improvements that you may not know about and may want to take advantage of when you're migrating from one version to the next. 

These improvements include:

* succinct tree-shakable error messages
* template auto-magic
* required inputs
* page title in route options
* component-bound route data
* CLI completion

Let's look at each of these features in more depth so you can use them in your Angular applications.

## Succinct [Tree-Shakable](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking) Error Messages

Now, tree-shaking mostly gets rid of unused code from a bundle. In this instance, it refers to the trimming of runtime error messages in production. 

Runtime error messages and codes in Angular are not new. What is new are the less verbose production error messages. 

In version 14, instead of long messages, you get their related error codes. And you can quickly look up these codes in the [Angular documentation](https://angular.io/errors) for debugging. You can view the longer detailed messages in development for further debugging.

## [Template](https://angular.io/guide/template-syntax) Auto-Magic

In version 16, template self-closing tags help developers forgo the need to add closing tags to component selectors in templates. This is similar to the ubiquitous `input` HTML element that doesn't need a closing tag. For example: 

```html
<!--Before-->

<app-root></app-root>

<!--After-->

<app-root />
```

Furthermore, upgrades to the Angular language service in version 16 make automatic imports of standalone pipes and components in templates possible. Like automatic class imports within components. Most code editors, like VS Code, [use language services](https://code.visualstudio.com/docs/editor/intellisense#_intellisense-features) to support automatic imports through _quick fixes_.

In addition, version 14 introduced an additional template compiler option, [a TypeScript configuration](https://angular.io/guide/angular-compiler-options), called `[extendedDiagnostics](https://angular.io/extended-diagnostics)` to supplement template insights. This configuration helps the compiler find common template pitfalls like an optional chain when a value will never be `null`. If it is `null`, it’s either a bug or a mis-typed value. 

These types of syntax errors are usually harder to spot since they don't always break the application.

## Required [Inputs](https://angular.io/api/core/Input)

Inputs in Angular are vital in data-sharing from parent to child components. They specify what values are being passed to the child. Version 16 introduced [required](https://angular.io/api/core/Input#required) inputs to help developers remember to pass these data when using child components. 

Missing data assigned to required inputs will trigger compile-time errors.

```typescript
export class ChildComponent {
	@Input({ required: true }) someList: unknown[];
}
```

```html
<!--In parent template-->

<child-one  /> <!--triggers compile-time error-->

<child-one [someList]="list" /> <!--no compile-time error-->
```

Perhaps further updates to required inputs may help delay rendering child components while the data is still `falsy`. 

## Page Title in Route Options

Page titles are important. Even more so for the [Accessiblity Tree](https://web.dev/the-accessibility-tree/). You can see them in the pages’ browser tabs, like headings. The Accessibility Tree is the [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) that Accessibility tools, like screen readers, use to navigate through the web page.

Page titles summarize content for users which is useful for navigation. It can be easy to forget to set them, especially if setting them seems a little counterintuitive in development.

Version 14 introduced a `title` option to the `[Route](https://angular.io/api/router/Route)` interface  which you can  use to configure application routes. This allows each route to set its own page title. In addition, this option can be configured as a `string` or a function that resolves to a string for more dynamic titles.

```typescript
const appRoutes: Route[] = [
{
    path: '/customers',
    component: CustomersComponent,
    title: 'Customers',
    children: [{
    	path: ':id/customer',
    	component: CustomerComponent,
        title: (route: ActivatedRouteSnapshot, state: 	RouterStateSnapshot) => this.getRouteTitleForCustomer()
  	}]
}
];
```

## Component-Bound Route Data

While inputs have always been used for data-sharing between components in parent-child relationships, you can also use them for data-sharing between routed components in version 16.

Some application routing scenarios require passing data, like IDs, to components being routed to. This was possible through use of the injectable `[ActivatedRoute](https://angular.io/api/router/ActivatedRoute)` class in the components needing the data.

Developers can now get these data in through the components’ inputs, whether it's from the route resolvers or path and query parameters. These data values get tied to component inputs with matching names. So, a `customerId` data value from the route will correspond to a `customerId` input in the component. 

```typescript
export class CustomerComponent {
	@Input() customerId: string;
}

```

```typescript
const appRoutes: Route[] = [
{
    path: '/customers',
    component: CustomersComponent,
    title: 'Customers',
    children: [{
    	path: ':id/customer',
    	component: CustomerComponent,
        title: 'Customer',
        resolve: { customerId: (route: ActivatedRouteSnapshot, state: 	RouterStateSnapshot) => this.getCustomerId()
  		}
  	}]
}
];
```

Be sure to [enable component binding through the router](https://angular.io/guide/router#getting-route-information).

## [CLI Completion](https://angular.io/cli/completion)

As for [imperative coders](https://dev.to/ruizb/declarative-vs-imperative-4a7l) and terminal lovers, version 14 brought command auto-completion through `ng completion`. This allows developers to get quick intuitive references for commands and their applicable options with a `tab` key press in the terminal. This makes using the CLI easier and faster.

## Wrapping Up

The latest Angular versions 14, 15, and 16 contain many more requested changes that not only boost the Developer Experience, but also address many framework issues. 

The [Angular Blog](https://blog.angular.io/) and the [documentation](https://angular.io/docs) provide more details about all these changes with specific examples.

