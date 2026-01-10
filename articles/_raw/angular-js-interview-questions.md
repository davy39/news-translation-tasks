---
title: AngularJS Interview Questions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T20:49:00.000Z'
originalURL: https://freecodecamp.org/news/angular-js-interview-questions
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df9740569d1a4ca3aa8.jpg
tags:
- name: Angular
  slug: angularjs
- name: interview questions
  slug: interview-questions
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'Here’s a list of the concepts that are frequently asked about in AngularJS
  interviews.


  What is AngularJS?

  What is the Model View Controller (MVC)?

  Two way data binding

  What is dependency injection and how does it work?

  What is $scope in AngularJS?

  W...'
---

Here’s a list of the concepts that are frequently asked about in AngularJS interviews.

* What is AngularJS?
* What is the Model View Controller (MVC)?
* Two way data binding
* What is dependency injection and how does it work?
* What is $scope in AngularJS?
* What is $rootScope in AngularJS?
* How to implement routing in Angular?
* Explain directives
* How can we create a custom directive in Angular?
* Explain difference bewteen service and factory
* Explain $q service, deferred and promises

# **Example Questions and Answers**

### Question: List out the Directives in AngularJS? 

Answer: ngBind, ngModel, ngClass, ngApp, ngInit, ngRepeat

### Question: What is $scope in AngularJS? 

Answer: $scope in AngularJS is an object which refers to an application model. It is an object that binds view (DOM element) with the controller. In controller, model data is accessed via $scope object. As we know, AngularJS supports the MV* pattern, $scope object becomes the model of MV*.

### Question: What is a SPA (Single page application) in AngularJS? 

Answer: Single-Page Applications (SPAs) are web applications that load a single HTML page and dynamically update that page as the user interacts with the app. 

SPAs use AJAX and HTML to create fluid and responsive web apps, without constant page reloads. However, this means much of the work happens on the client side, in JavaScript. 

A single HTML page here means UI response page from the server. The source can be ASP, ASP.NET, ASP.NET MVC, JSP and so on. 

A single-page web application, however, is delivered as one page to the browser and typically does not require the page to be reloaded as the user navigates to various parts of the application. This results in faster navigation, more efficient network transfers, and better overall performance for the end user.

### Question: What is routing in AngularJS? 

Answer: Routing is a core feature in AngularJS. This feature is useful in building SPAs (Single Page Applications) with multiple views. In SPAs, all views are different HTML files and we use Routing to load different parts of the application. It’s helpful to divide the application logically and make it manageable. In other words, Routing helps us to divide our application into logical views and bind them with different controllers.

### Question: Explain ng-repeat directive. 

Answer: The ng-repeat directive is the most used AngularJS Directive feature. It iterates over a collection of items and creates DOM elements. It constantly monitors the source of data to re-render a template in response to change.

### Question: What is the difference between ng-If and ng-show/ng-hide. 

Answer: The ng-If directive only renders DOM element if the condition is true. Whereas ng-show/ng-hide directive renders the DOM element but changes the class of ng-hide/ng-show to maintain visibility of the element on the page.

### Question: How do you cancel a timeout with AngularJs? 

Answer: $timeout is AngularJs’ wrapper for window.setTimeout, you cancel a timeout applying the function:

```text
$timeout.cancel(function (){
  // write your code.
});
```

### Question: What is Dependency Injection? 

Answer: Dependency Injection (DI) is a software design pattern that deals with how components get ahold of their dependencies. 

The AngularJS injector subsystem is in charge of creating components, resolving their dependencies, and providing them to other components as requested.

### Question : Explain the ng-App directive. 

Answer: The ng-app directive starts an AngularJS Application. It defines the root element. It automatically initializes or bootstraps the application when web page containing the AngularJS Application is loaded. It is also used to load various AngularJS modules in AngularJS Applications.

### Question: Explain the ng-init directive 

Answer: The ng-init directive initializes an AngularJS Application's data. It is used to put values to the variables to be used in the application. 

For example, in the below code we have initialized an array of countries using JSON syntax to define the array of countries.

```html
<div ng-app = "" ng-init = "countries = [{locale:'en-US',name:'United States'}, {locale:'en-GB',name:'United Kingdom'}, {locale:'en-FR',name:'France'}]">
   ...
</div>
```

### Question: How do you share data between controllers? 

Answer: Create an AngularJS service that will hold the data and inject it inside of the controllers. Using a service is the cleanest, fastest and easiest way to test. 

However, there are couple of other ways to implement data sharing between controllers, like:

* Using events
* Using $parent, nextSibling, controllerAs, and so on to directly access the controllers
* Using the $rootScope to add the data on (not a good practice)

### Question: What is the difference between the ng-if and ng-show/hide directives? 

Answer: ng-if will only create and display the DOM element when its condition is true. If the condition is false or changes to false it will not create or destroy the created one. 

ng-show/hide will always generate the DOM element but it will apply the CSS display property based on the evaluation of the condition.

## More info on AngularJS:

* [Angular vs AngularJS](https://www.freecodecamp.org/news/angular-vs-angularjs/)
* [The best Angular and AngularJS tutorials](https://www.freecodecamp.org/news/best-angular-tutorial-angularjs/)


