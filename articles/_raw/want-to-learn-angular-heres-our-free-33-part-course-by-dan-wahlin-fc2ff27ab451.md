---
title: Learn Angular in this free 33-part course by Angular-expert Dan Wahlin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-16T05:34:57.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-angular-heres-our-free-33-part-course-by-dan-wahlin-fc2ff27ab451
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SaVwtG8cWgCh1WFYsIa2Fw.png
tags:
- name: Angular
  slug: angular
- name: Angular
  slug: angularjs
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  According to the Stack Overflow developer survey 2018, Angular is one of the most
  popular frameworks/libraries among professional developers. So learning it increases
  your chances of getting a job as a web developer significantly...'
---

By Per Harald Borgen

According to the [Stack Overflow developer survey 2018](https://insights.stackoverflow.com/survey/2018/#most-popular-technologies)**,** Angular is one of the most popular frameworks/libraries among professional developers. So learning it increases your chances of getting a job as a web developer significantly.

That’s why we’ve teamed up with one of the most renowned experts on the framework, and created a [free Angular course](https://scrimba.com/g/gyourfirstangularapp?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gyourfirstangularapp_launch_article) at Scrimba.

Instructor [Dan Wahlin](https://twitter.com/DanWahlin) is a Google Developer Expert who’s provided training, architecture, and development services for some of the biggest corporations in the industry and created some of the most popular training courses on Udemy and Pluralsight. He’s also a regular speaker at developer conferences around the world.

[In this course](https://scrimba.com/g/gyourfirstangularapp?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gyourfirstangularapp_launch_article), Dan guides you through creating your very first Angular app using TypeScript. By completing the course you’ll add valuable skills to your toolbelt.

Now let’s have a look at how the course is structured!

### Part #1: Course overview

![Image](https://cdn-media-1.freecodecamp.org/images/1*mHUNNtNB1aF6s1juYuJ7Jw.png)

In the introductory video, Dan gives an overview of the course, key aspects of Angular, and how the course is laid out. He also tells you a little bit about his background, so that you are familiar with him before jumping into the code of your new app.

### Part #2: Application Overview

In this part, Dan gives us a glimpse into the app we’re going to build. It is designed to allow us to focus on the key building blocks of Angular. By creating an app to display customer data and their orders, we will hone in on the key aspects of Angular, such as Components, Modules, Services and Routing. Also, during the course, we will learn about great features every app has, like sorting and filtering.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_bYYJCud9vhxaSSvKmqH6Q.png)

### Part #3: Angular CLI

In this part we learn the basics of using the Angular CLI (command-line interface) tool and walk through the basic commands:

```sh
ng --version  
ng --help  
ng new my-app-name  
ng generate [component | directive | pipe | service | class | interface | enum | guard]  
ng build   
ng serve  
ng lint   
ng tests

```

For example, `ng --new my-app-name` will create a new blank Angular app for us and we can use `ng -generate` to create parts of our app.

`ng build` will build everything for us, and `ng serve -o` will even start a development server as well as open a browser window for us to view our app in.

### Part #4: Project Files Overview

In this video of the course, Dan gives a basic overview of the CLI command for generating a blank Angular app and gives a quick overview of the configuration files like `tslint`, `tsconfig` and `protractor` in our app folder.

### Part #5: The Big Picture

Here we learn a useful abstraction that Components are similar to Lego blocks — we build up components and then use them to stick together to make an app. We also get a quick refresher on JavaScript language family and learn where TypeScripts fits in.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s2TcwSmQM7_BAA25NC3lVQ.png)

Dan gives us a good mental model to use for thinking about our code while working with Angular so we can imagine where it all fits in.

### Part #6: Components & Modules — Overview

Not abstracted away, the diagram for Angular code might look like this.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OTT4yeJg6630S2I43WRGxg.png)

Components are made up of code and HTML template and it can have a selector, so we can call it in our HTML.

```html
<appcomponent></appcomponent>

```

Every Component consists of:

![Image](https://cdn-media-1.freecodecamp.org/images/1*-12cVJ5V8OG1SBWI4hraSg.png)

Dan then explains what each of the parts is and how they fit in the Angular way of developing components. One of the great things about Angular is that it’s very predictable. Once you learn how to create your first component you’re well on your way to creating additional components.

### Part #7: Components & Modules — App Component

In this part of the course, we look at a `HelloWorld` component.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYiWpdm6Aqf4PmcbHdSXGg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*wproObAyLBo-EOBM-r3P8A.png)

Dan breaks down every aspect of the component for us and explains how it’s used and how our component is processed by Angular, how it’s added to `app.module` and ultimately how it’s rendered on our screens.

We learn that `selector: 'app-root'` is what allows us to later call the component from our HTML using `<app-root></app-root>`

We also have a sneak peek at data binding which we’ll learn more about in later chapters.

### Part #8: Components & Modules — App Module

In this screencast, we spend more time learning about the inner workings of `app.module` which we touched on in the previous cast and learn about `NgModule` and `BrowserModule`.

### Part #9: Components & Modules — Adding a Customers Component

In this cast, Dan gives us some tips on creating components using the CLI and then shows how to create components manually. We learn how to structure a component further expanding on our knowledge from Part #6.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C2YJ7m1pbHjXSHC0Fv0baQ.png)

Now we bring in some data to mimic our API and learn about how modules help us keep our code organized and easier to re-use.

### Part #10: Components & Modules — Adding a Customers List component

In this part, we create a `customers-list.component` which is an HTML table to display our list of customers. We quickly register in `customers.module` and use the`<app-customers-list></app-customers-list>` selector to display our empty table.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CeqVsl_JlKtnPXzgSVismQ.png)

Next step would be to populate the table with some data.

### Part #11: Components & Modules — Adding a Filter Textbox Component

Before we add some data to our table, Dan shows us how to add a `filter-textbox.component` to our table and we reinforce the Angular way of creating a component, registering it in a module and using it in our HTML with selectors.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b9SgU3SuhQINc87r56DDwg.png)

### Part #12: Components & Modules — Adding a Shared Module and Interfaces

In this section, Dan talks about using `shared.module` — a module where we put components or other features that we want to share throughout our app, not just in `customers`.

We also have a quick refresher on TypeScript interfaces and how they can be used in Angular applications to provide better code help and enhance productivity.

```ts
export interface ICustomer {  
    id: number;  
    name: string;  
    city: string;  
    orderTotal?: number;  
    customerSince: any;  
}

```

### Part #13: Data Binding — Data Binding Overview

In this chapter we learn about data binding, learn a few techniques and see how to add data binding to our application.

We usually bind data in our templates. Data binding comes into play when a component gets our data and hooks it into a template. We can get data into a template using `Property Binding`, and handle user events and get data out of a template using `Event Binding`. Angular provides a robust and clean way to add data binding in templates that’s quick and easy to remember.

Dan provides us with a handy slide to remember syntax required…

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ft7Mj_TaGsUJ4GRdmJNGPQ.png)

…and some on Angular directives, for example, `ngFor`, used to loop through items in a collection and get some properties from the items, and `ngIf` to add and remove an HTML element from the DOM.

### Part #14: Data Binding — Getting Started with Data Binding

In this cast we play around with `Property Binding` and `Event Binding` to better understand how they work in Angular, using the knowledge from the previous chapter.

Dan shows how we can use the `[hidden]` property to display an `h1` element dynamically:

```html
<h1 [hidden]="!isVisible">{{ title }}</h1>

```

And to bind DOM events such as click:

```html
<button (click)="changeVisibility()">Show/Hide</button>

```

### Part #15: Data Binding — Directives and Interpolation

Here we have a look at Interpolation. The rationale is that we need to get data from each customer to generate a table row in a table from Part #10.

This is the part when things start coming together: we use directive `ngFor` to loop through each customer in `filteredCustomers` and interpolate data from a customer into a table row. We learn a few tricks about rendering data conditionally using `ngIf`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xMU7cyyy5ooxLJPBct0PEw.png)

In the end we get a pretty looking table!

![Image](https://cdn-media-1.freecodecamp.org/images/1*BO_isrPNvKI9u80bXLOnyA.png)

### Part #16: Data Binding — Event Binding

`Event Binding` is crucial when we need to handle an event, like a mouse move or a click. In this screencast, Dan guides us through adding functionality to sort the data in our table. We will start on it in this chapter and finish it when we get to the Services part of our course.

We create a placeholder event handler in our `customer-list.component`:

```ts
sort(prop: string) {  
     // A sorter service will handle the sorting  
}

```

Add binding in `customers-list.component.html`:

```html
<tr>  
    <th (click)="sort('name')">Name</th>  
    <th (click)="sort('city')">City</th>  
    <th (click)="sort('orderTotal')">Order Total</th>  
</tr>

```

### Part #17: Data Binding — Input Properties

We have some data in a `people` array in our `customers.component` and we need to pass it into our `filteredCustomers` array in `customers-list.component`, effectively passing data from a parent component to a child.

For that we will use Angular’s `Input` property which relies on a decorator named Input():

```ts
@Input() get customers(): ICustomer[] {  
    return this._customers  
}

set customers(value: ICustomer[]) {  
     if (value) {  
     this.filteredCustomers = this._customers = value;  
     this.calculateOrders();  
     }  
}

```

And bind to it in our parent component template to pass data from parent to child (app-customers-list in this case):

```html
<app-customers-list [customers]="people"></app-customers-list>

```

### Part #18: Data Binding — Working with Pipes

Wow! We’ve done quite well so far!

![Image](https://cdn-media-1.freecodecamp.org/images/1*v51xQi5Ard63tF0-0dd-2Q.png)

There are a few things which might look a bit odd — “john” is lowercase and we have no “$” symbol to display currency in which we have our orders.

This is really the way we have our data, so we could just go and update it directly, or we can use a built-in Angular feature called Pipes to update it for us!

Some of the simplest pipes look like this:

```ts
{{ cust.name | uppercase }} // renders JOHN  
{{ cust.name | titlecase }} // renders John

```

But sometimes you might want to have your own custom pipe and Dan shows us how to build a custom `capitalize` pipe (note that Angular includes one called `titlecase` — but we’re learning here!) and how to wire it up to use in our application.

### Part #19: Data Binding — Adding Filtering

In this cast, Dan walks us through adding functionality to our `filter-textbox.component` from Part #11

We learn more about Angular `Output` and `EventEmitter` properties, create our filter event handler and bind it to our filter textbox:

```html
<filter-textbox (changed)="filter($event)"></filter-textbox>

```

And there we go, we can now filter on our customers’ names!

![Image](https://cdn-media-1.freecodecamp.org/images/1*8oM5-CM9n7Ic46M4l4IS8w.png)

### Part #20: Services and Http — Services Overview

In this chapter, we look at Angular Services. One of Angular’s strong points is that it’s a complete framework that provides built-in support for managing state and objects through services. We saw services in the diagram earlier. Since we don’t want components to know how to do too much, we’ll rely on services to communicate with the server, perform client-side validation or calculations, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OTT4yeJg6630S2I43WRGxg.png)

Components should focus on presenting data and handling user events. When additional functionality needs to be performed they should delegate to services to provide for a more maintainable application and better code reuse.

That’s exactly what Service does — some reusable functionality for the app which should not be of any component’s concern.

Luckily, Dan get us covered with a handy slide to keep in mind.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dzy9aUGQUu_RXuQ3Wx6RDg.png)

### Part #21: Services and Http — Creating and Providing a Service

From a chapter earlier we have seen an import of `Injectible` which is a decorator that allows for something called Dependency Injection or DI for short (another powerful feature built-into Angular).

We’ll use DI to access an `HttpClient` service which we will use to communicate with a RESTful service. We will be adding HttpClient to a constructor of our `data.service` and `@Injectible()` decorator will make DI possible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6sbs_J-0b6_SH1XqpB7k-g.png)

### Part #22: Services and Http — Calling the Server with HttpClient

In this cast, Dan introduces Observables from `RxJS` — reactive extensions for JavaScript, which is not a part of Angular but is included in all Angular projects by default.

We will be using Observables to deal with asynchronous code. In a nutshell, it allows us to start an operation and then subscribe to data that is returned. Once the data comes back from the server, the subscription ends and we can unsubscribe.

Dan discusses the necessary code to call the server and then subscribe to the response using RxJS piping and operators.

Here’s an example of how we can get Orders:

![Image](https://cdn-media-1.freecodecamp.org/images/1*LZp4nkmFIm4MGJAhQFU4sA.png)

### Part #23: Services and Http — Injecting a Service into a Component

Now that we have a way to get the data, we need to inject the service into one of our components. We can now change `this.people` in `customers.component` from being hardcoded to call a service and get data that way.

We need to bring our `data.service` to `app.module` and then in `customers.component` we can:

```ts
import { DataService } from '../core/data.service';

```

Now we can inject our `DataService` straight into our component’s constructor:

```ts
constructor(private dataService: DataService) {}

```

### Part #24: Services and Http — Subscribing to an Observable

Now we can use our injected `dataService`, call `getCustomers()` and subscribe to our `Observable<ICustomer[]>` to get the data.

Which is pretty straightforward:

```ts
ngOnInit() {  
    this.title = 'Customers';  
    this.dataService.getCustomers()  
        .subscribe((customers: ICustomer[]) =>  
        this.people = customers);

```

Now we have one last service to look at — `SorterService`

### Part #25: Services and Http — Using a SorterService

Currently, if we click on our column headers nothing would happen.

Dan handily provided a prewritten service for us, which we can use, so in this chapter, we will practice bringing in service into our components, in this case, `customers-list.component`.

As with other services we need to import it:

```ts
import { SorterService } from '../../core/sorter.service';

```

Then we inject `SorterService` into our constructor:

```ts
constructor(private sorterService: SorterService) {}

```

Dependency injection makes it extremely easy to access reusable code such as the sorter or data services.

Lastly, we use it in our `sort()` function:

```ts
sort(prop: string) {  
    this.sorterService.sort(this.filteredCustomers, prop);  
}

```

### Part #26: Routing — Routing Overview

This chapter will introduce Routing, which is an essential part of modern applications. As you’re building an Angular app, you want to show different components as the user interacts with it. In our case, when a user clicks on a Customer, we might want to show them Orders. Routing is one way to very neatly achieve this.

Routes are used to hook a specific URL to a component and in the next few chapters, we will be focusing on the top part of our Angular diagram.

![Image](https://cdn-media-1.freecodecamp.org/images/1*og4k_DGep_esiA5I1ALgzg.png)

A super great part of routing is that if a user bookmarks a specific URL, it will bring them back to a specific component and there is no need for complex show/hide logic.

### Part #27: Routing — Creating a Routing Module with Routes

We begin with a familiar module-container routine and create a `app-routing.module`.

A main focus of the `app-routing.module` is to define the routes in an array:

```ts
const routes: Routes = [  
    { path: '', pathMatch: 'full', redirectTo: '/customers'},  
    { path: '**', redirectTo: '/customers' }  
];

```

Three key properties of `routes` are:

* `path` — where your user goes, so `path: ''` would be the root of your app. `path: '**'` is a wild card match. It is usually placed last and it’s there to cover cases for any route that is not specified in `routes`
* `pathMatch` — how exactly should the route match for a specific component to be displayed
* `redirectTo` — when a path is matched, this is where we send the user. In our case, we send them to `/customers`.

### Part #28: Routing — Using Router Outlet

In order to use Routing in Angular in our `app.component` template we replace `<app-customers></app-customers>` with `<router-outlet></router-outlet>`. Ultimately, this is just a way to say: ‘Hey, this is where a component will go when we hit our route’.

When we hit a route, then a component associated with that route will magically appear in the place of `<router-outlet></router-outlet>`.

### Part #29: Routing — Adding a Customers Routing Module and Routes

In this chapter, Dan brings all the things together and we connect a `/customer` route to `customers.component`.

First, we create a`customers-routing.module` and point our route from part #28 to `customers.component` like so:

```ts
const routes: Routes = [  
    { path: 'customers', component: CustomersComponent }  
];

```

And now when we type “customers” **in the Scrimba browser address bar** we get our `customers.component`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*drUS_faas9AzJIvfW-EKxg.png)

### Part #30: Routing — Adding an Orders Component with Routes

In this clip, we’re going to quickly review how we’ve done routing to display customers, and now it’s time for routing to display their orders.

There’s a little catch though. When we click on a customer we need to display order data related to that customer. So we need to pass some dynamic data into our routing.

We can achieve this by passing a `route parameter` in our `orders-routing.module` like so:

```ts
const routes: Routes = [  
    { path: 'orders/:id', component: OrdersComponent}  
];

```

Note the `/:id` syntax. In routing the `:` symbol indicates that the value after it will be dynamically replaced and `id` is just a variable, so it can be anything like `:country` or `:book`.

### Part #31: Routing — Accessing Route Parameters

In the previous screencast we saw how to create `orders/:id` route and now `orders.component` needs to somehow grab that `id` and display customer related orders. To do that we need to access the `id` route parameter.

One way of doing it would be:

```ts
let id = this.route.paramMap.get('id');

```

The benefit of this way is that we can subscribe to `paramMap` and get notified when any of the data in `id` changes. But we only need it once.

We can use `snapshot` for that:

```ts
let id = this.route.snapshot.paramMap.get('id')

```

`snapshot` just takes a kind of an instant picture of your URL and gives it to you, which perfect as that’s what we need in this situation.

But now we have a problem. Our `id` is a string, but to get an order from our `DataService` it needs to be a number. We can convert it with `parseInt()`, but Dan teaches us a neat `+` trick:

```ts
let id = +this.route.snapshot.paramMap.get('id')

```

Now we can call `DataService` to get the order and render it to `orders.component`.

### Part #32: Routing — Linking to Routes with the routerLink Directive

The last thing we want to do is to add a link on a customer’s name, so we can click it to see their orders.

In part #28 we’ve added `<router-outlet></router-outlet` and now we just need to tell our app that we want to display `orders.component` when we navigate to `/orders/:id`.

We can do it by adding a link to our customer’s name in `customers-list.component.html` in a row where we’re mapping all the data to be displayed. We already have our customer object there, so we can just pass `id` to our route.

```html
<a [routerLink]="['/orders', cust.id]">  
    {{ cust.name | capitalize }}  
</a>

```

Now we can see orders!

![Image](https://cdn-media-1.freecodecamp.org/images/1*M3o56Z9ikhkMt6tLbndzdQ.png)

But hey, how do we get back? We could click ‘Back’ button on the browser, but it’s much nicer to have an app link for that, now that we know routing. Let’s add it to `customers-list.component.html` at the very bottom.

```html
<a routerLink="/customers">View All Customers</a>

```

### Part #33: Course Summary

Very well done, we have our app now!

We can wrap up and have a quick recap of things done. Don’t forget to watch the actual screencast of the course, as Dan is a great teacher so you will have lots of fun following the process alongside him!

Thank you, Dan!

![Image](https://cdn-media-1.freecodecamp.org/images/1*TwvG-32iqImuHarf1HKUQg.png)

If you’re interested in keeping up on front-end and back-end technologies make sure to [follow Dan on Twitter](https://twitter.com/danwahlin)! 

Happy coding!

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gyourfirstangularapp_launch_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gyourfirstangularapp_launch_article)_

