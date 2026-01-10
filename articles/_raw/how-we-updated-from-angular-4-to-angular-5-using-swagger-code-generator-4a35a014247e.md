---
title: How we updated from Angular 4 to Angular 5 using swagger code generator
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T18:05:47.000Z'
originalURL: https://freecodecamp.org/news/how-we-updated-from-angular-4-to-angular-5-using-swagger-code-generator-4a35a014247e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c5MXOqXBhsy0nVXEdP89og.png
tags:
- name: Angular
  slug: angular
- name: coding
  slug: coding
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Mark Grichanik

  As a full stack developer in an enterprise company, I had the opportunity to update
  our client side to Angular 5. The process itself is not simple and there are many
  things to take into account. In this article, I’ve outlined the ne...'
---

By Mark Grichanik

As a full stack developer in an enterprise company, I had the opportunity to update our client side to **Angular 5**. The process itself is not simple and there are many things to take into account. In this article, I’ve outlined the necessary steps needed to update your Angular version with ease and simplicity.

> _According to the Angular team, it is ill-advised to update from version 4 to 6 directly. That is why this article will focus on updating to version 5._

> Just as a heads up, the Angular team promises that updating from Angular 6 and further will be lighter and easier to handle.

### Prerequisites

Make sure you are using the latest swagger version. Angular 5 deprecates OpaqueToken and it now uses InjectionToken instead.

OpaqueToken is a unique and immutable value which allows developers to avoid collisions of DI token id’s. [InjectionToken](https://angular.io/api/core/InjectionToken)<T> is a parametrized and type-safe versio[n of ‘Opaqu](https://github.com/angular/angular/commit/d169c2434e3b5cd5991e38ffd8904e0919f11788)eToken’.

> _We use swagger-codegen-maven-plugin, version 2.2.2. Because of the aforementioned issue, we had to upgrade to 2.3.1._

> Inside maven pom.xml file we had to change language attribute of swagger yml from ‘typescript-angular2’ to ‘typescript-angular’ which should support all angular versions from now on.

With Swagger 2.2.2 the BASE_PATH is generated as:

As opposed to Swagger 2.3.1, which is supported by Angular 5:

Take note that there is another major difference between the Swagger versions in regard to the generated file. For example, if we had a dogResource.java file that contains all kinds of REST calls, **Swagger 2.2.2** will generate dogApi.ts. Whereas **Swagger 2.3.1**, will generate it as a service. Meaning, dog.service.ts.

> _After upgrading to the latest swagger version, you must refactor your imports to use dog.service.ts instead of dogApi.ts._

![Image](https://cdn-media-1.freecodecamp.org/images/0*KHF_L94Z1iOA6jxA)
_by [Unsplash](https://unsplash.com/@bruno_nascimento?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Bruno Nascimento</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Let’s Begin

Our server side is written in Java while our client side is written using Angular 4. We are using [swagger](https://github.com/swagger-api/swagger-codegen) that creates a yaml file that uses [OpenApi](https://www.openapis.org/) specification.

_It’s a standard interface to RESTful APIs which allows understanding of the capabilities of the service without access to source code. ([https://swagger.io/specification/](https://swagger.io/specification/))._

Next, we generate Typescript files (containing objects and APIs) from the original yaml file. You can play with their generator [here](https://editor.swagger.io/).

**_STEP 1:_** Update your node and npm to the latest versions . We used npm 6.1 with node 10.0. You can download them from [here](https://nodejs.org/en/).

**_STEP 2_**: Update your package.json file using:

### Upgrading NgRx And Needed Refactoring

It is not mandatory to use NgRx, but I highly suggest it. If you are not using NgRx, you can skip to the next step.

> The NgRx team created a very useful migration [guide](https://github.com/ngrx/platform/blob/master/MIGRATION.md). They really describe step by step what modifications are needed to be done in order to have a successful migration

In version 5, the ‘payload’ property in Action Interface has been removed because it was a source of type-safety issues.

The NgRx team suggests to create a new class for each action that you have, and pass the payload as an input to the constructor of that class.

We’ve decided to make the transition easier by creating our own Action interface called, **_ActionWithPayload,_** which extends the regular Action interface. ActionWithPayload extends the newer interface, but retains the older payload attribute.

Also we noticed that we can’t use observable$.select and we must wrap it with the ‘pipe’ operation:

### Fixing Unit Tests

In order to use the new store mechanism, you need to create a mocked store class:

In order to use it within a test, do the following:

Store will be a mocked instance of the provided state! We can mimic all kinds of states with that!

### Final Words

Although it may seem daunting at first, the steps I have outlined are straightforward and not very complicated. If you run into any issues, feel free to drop me a line at : [_markgrichanik[at]gmail[dot]com_](mailto:markgrichanik@gmail.com).

I would also love to hear any feedback you have while upgrading Angular applications with Swagger and NgRx.

> If you liked this article, ? away so that others can read it as well

