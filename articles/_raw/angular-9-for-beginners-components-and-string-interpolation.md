---
title: Angular 9 for Beginners - Components and String Interpolation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-29T22:23:33.000Z'
originalURL: https://freecodecamp.org/news/angular-9-for-beginners-components-and-string-interpolation
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/Copy-of-Copy-of-Travel-Photography-1.png
tags:
- name: Angular
  slug: angular
- name: Angular 9
  slug: angular-9
seo_title: null
seo_desc: 'By Cem Eygi

  In modern web development, many developers prefer to build the UI of a website in
  a component-based way. It''s also supported by all modern frameworks. Understanding
  how components work and how to use them is a big step in learning Angular...'
---

By Cem Eygi

In modern web development, many developers prefer to build the UI of a website in a component-based way. It's also supported by all modern frameworks. Understanding how components work and how to use them is a big step in learning Angular.

In this post, you're going to learn about Angular components, how to create and use a component in a project, and what string interpolation is. I will also be covering other important features of Angular in my upcoming articles:

* **Part 1:** [How to install your first App with the Angular CLI](https://www.freecodecamp.org/news/angular-9-for-beginners-how-to-install-your-first-app-with-angular-cli/) 
* **Part 2:** Angular Components and String Interpolation **(you’re here)**
* **Part 3**: [Angular Directives & Pipes](https://youtu.be/3-eJ-A9rFEU)
* **Part 4:** [One-Way Data Binding in Angular](https://youtu.be/x_vtX3vvE8k) 
* **Part 5:** [Angular Two-Way Data Binding with ngModel](https://youtu.be/bKfbzpANUFE)

**If you prefer, you can also watch the video version:**

%[https://youtu.be/wXmw0FxjmTc]

## What is a Component?

Components are the most basic building blocks of an Angular application. We can think of components like LEGO pieces. We create a component once but can use them many times as we need in different parts of the project.

An Angular component is made of 3 main parts:

* HTML Template —View
* TypeScript File — Model
* CSS File — Styling

### Why do we need Components?

Using components is beneficial in many ways. Components divide the UI into smaller views and render data. A component should not be involved in tasks like making HTTP requests, service operations, routing, and so on. This approach keeps the code clean and separates the view from other parts (see [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)). 

Another important reason is that components divide the code into smaller, reusable pieces. Otherwise, we would have to include endless lines of code in a single HTML file, which makes the code much harder to maintain.

## Creating Our First Angular Component

Now let's create our first component. The short way to create a component is by using Angular CLI:

```
ng g c component-name
```

This command creates a brand new component with its own files (HTML, CSS, and TypeScript) and registers it to the App Module automatically:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Ekran-Resmi-2020-04-29-10.59.14.png)
_The App Module_

> **Note:** In Angular, we need to register every necessary service, component, and module to a module file.

Now let's take a closer look at the component model (TypeScript Component File):

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Ekran-Resmi-2020-04-29-10.57.59.png)
_Inside the App Component_

This is actually a TypeScript class but to define it as a component:

* First of all, we need to import **Component** from the **@angular/core** library, so we can use the component decorator
* The **@Component** decorator marks the class as a component and allows us to add the following metadata
* The **selector** is for calling the component later as an HTML tag: `<app-root> </app-root>`
* **TemplateUrl** is the path where the HTML View of the component is.
* **S**tyle URLs**** (can be more than 1) is where the styling files of the component are.
* Finally, we **export** the class (component) so that we can call it inside the **app.module** or other places in the project later.

### What is String Interpolation?

One of the most common questions people ask about Angular is what that curly braces syntax is. Components render data, but data can change in time, so it needs to be dynamic. 

We use curly braces inside other curly braces to render dynamic data: `{{ data }}` and this representation is called string interpolation. You can see the example in the video version above.

## Wrap Up

One of the biggest steps of learning Angular is to know how to create components and use them efficiently. I hope you find this post helpful. In the next part, we are going to take a look at the Angular Directives like ng-if, ng-for, ng-class, and more. Stay tuned :)

**If you want to learn more about Web Development,** **feel free to** [**follow me on Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)**!**

Thank you for reading!

