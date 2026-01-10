---
title: Angular 6 and its new features — explained in three minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-16T15:11:00.000Z'
originalURL: https://freecodecamp.org/news/angular-what-is-the-new-briefly-e6837348dd3a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AdGD1-LO1avzx5hNJFQoZQ.png
tags:
- name: Angular
  slug: angular
- name: angular6
  slug: angular6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Said Hayani

  Angular has come out with some amazing new features in version 6.0.0, especially
  in Angular-cli. Now, with Angular 6, you can easily update your old packages, create
  native web elements using Angular Elements, and many other things. Le...'
---

By Said Hayani

[Angular](https://angular.io) has come out with some amazing new features in [version 6.0.0](https://angular.io/), especially in Angular-cli. Now, with Angular 6, you can easily update your old packages, create native web elements using Angular Elements, and many other things. Let’s take a look!

### ng add

![Image](https://cdn-media-1.freecodecamp.org/images/1*u8BWLIWdkabEzp0QSmMUgg.png)

`**ng add**` is a new command in Angular-cli that helps you install and download new packages in your angular apps. It works the same as npm, but it doesn’t replace it.

### ng update

![Image](https://cdn-media-1.freecodecamp.org/images/1*mxQPMNmblN_8t_ky1r5G8w.png)

`**ng update**` is a new Angular-cli command too. It’s used to update and upgrade your packages. It’s really helpful, for example, when you want to upgrade from Angular 5 to Angular 6, or any other package in your Angular app.

### Declaring the providers inside the service itself

Before this update, you had to the declare the providers array in `**app.module.ts**`

Now with Angular 6, you can provide your service inside the supervisor itself by putting the `**providedIn:root**` property within the "`**@injectable"**` **decorator.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*3Huej4et-8LIfrAEhzY3pQ.png)

### Use ng-template instead of template directive

You can use `**ng-template**` to render the HTML instead of the `**template**` tag in the new version of Angular. `**ng-template**` is an Angular element, and it works when it is used with a [structural directive](https://angular.io/guide/structural-directives) such as `***ngFor**` and `***ngIf**`

![Image](https://cdn-media-1.freecodecamp.org/images/1*6RjvjuP6weX0bPrYBbjQ8Q.png)

### Angular elements

Angular 6 introduced us to Angular elements. You’re able to render your Angular elements as native web elements, and they’re interpreted as trusted HTML elements.

You can add Angular elements by running the command below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*u8BWLIWdkabEzp0QSmMUgg.png)

Import `**createCustomElement**` in your component.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YP2ej1AXVAO9GURmbGnFcQ.png)

Then create your customized element!

![Image](https://cdn-media-1.freecodecamp.org/images/1*F1WAYYCRzJSyfr8PSWsMRg.png)

`**MyElemComponent.ts**`

![Image](https://cdn-media-1.freecodecamp.org/images/1*S4Ib01DNgO67jh_-habKmQ.png)

The result:

![Image](https://cdn-media-1.freecodecamp.org/images/1*lgl-OcKiFKVLF7A9KdrImA.png)

**Note:** you have to implement the `**DomSanitizer**` method from `@angular/platform-browser` to make your custom element a trusted HTML tag .

You can learn more about Angular elements [here](https://angular.io/guide/elements)

### Upgrading to RxJS 6.0.0

Angular 6 uses the latest version of Rxjs library. Now you can enjoy the newest features of RxJS 6 in your Angular app :)

### Wrapping Up

Angular itself doesn’t have many groundbreaking changes in the Angular core, but Angular-cli is really exciting. The Angular team is focusing more on performance, building PWAs easily, providing a good environment to work in which to work with Angular in an easy way.

You can find me on [Twitter](https://twitter.com/SaidHYN).



> By the way, I’ve recently worked with a strong group of software engineers for one of my mobile applications. The organization was great, and the product was delivered very quickly, much faster than other firms and freelancers I’ve worked with, and I think I can honestly recommend them for other projects out there. Shoot me an email if you want to get in touch — [said@devsdata.com](mailto:said@devsdata.com).

