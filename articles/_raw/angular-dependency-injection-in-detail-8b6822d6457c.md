---
title: An introduction to Angular dependency injection
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T21:14:06.000Z'
originalURL: https://freecodecamp.org/news/angular-dependency-injection-in-detail-8b6822d6457c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xQW9Spiz8U0tNEuX_m2blw.jpeg
tags:
- name: Angular
  slug: angular
- name: dependency injection
  slug: dependency-injection
seo_title: null
seo_desc: 'By Neeraj Dana

  In this article, we will see how the dependency injection of Angular works internally.
  Suppose we have a component named appcomponent which has a basic and simple structure
  as follows:

  import { Component, OnInit } from "@angular/core";...'
---

By Neeraj Dana

In this article, we will see how the dependency injection of Angular works internally. Suppose we have a component named appcomponent which has a basic and simple structure as follows:

```
import { Component, OnInit } from "@angular/core";@Component({  selector: "my-root",  templateUrl: "app.component.html",  styleUrls: ["app.component.css"]})export class AppComponent implements OnInit {  ngOnInit(): void {      }}
```

And we have a service class named GreetingService with a function in it `sayHello` which has a name as a parameter and returns the name with “Hello” in front of it.

```
export class GreetingService{  sayHello(name){    return `Hello ${name}` ;  }}
```

There are two ways to use the service class in the component: first, we can manually create an instance of the service in the component (this is the wrong way and is never recommended).

And the other way is to let Angular create the instance of our service and pass that instance to our component internally. This is the common and recommended way to do it.

#### Injecting our service in the Angular dependency injection system

```
Import {Component} from '@angular/core';Import {GreetingService} from '. /greetingService';
```

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ]})export class AppComponent  {
```

```
constructor(private greetingService : GreetingService){   console.log(this.greetingService.sayHello());  }}
```

Now if you run this project, you will get the error “No provider for GreetingService!”

![Image](https://cdn-media-1.freecodecamp.org/images/PA66RsT3fdnjttQROpVulvpDU6QGWfYoCxyl)

So, basically Angular is complaining that it did not find any provider for creating an instance of the greeting service or it does not know how to create an instance. In order to let the framework know how the instance should be created, we have to pass a provider object to the providers property in the component decorator shown below:

```
import { Component } from '@angular/core';import {GreetingService} from './greetingService';
```

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[{      }]})export class AppComponent  {
```

```
constructor(private greetingService : GreetingService){   console.log(this.greetingService.sayHello());  }  }
```

In this provider object, we have many properties so let us understand them one by one.

#### Custom Factory

use factory: this will tell the framework which factory will be used while creating the object of the service. In our case, we don’t have any factory so let’s create one.

The factory will be a function which will be responsible for creating and returning the object of the service.

```
export function greetingFactory(){   return  new GreetingService()};
```

```
Or more short way
```

```
export const greetingFactory= () =>  new GreetingService ();
```

#### Custom Injection Token

The next thing is to create a property whose value will be an Injection Token instance. Using this property, the framework will uniquely identify our service and will inject the right instance of the service.

```
var greetingTokken = new InjectionToken<GreetingService>("GREET_TOKEN");
```

So in the above snippet, we are creating an instance of the InjectionToken class and it is generic. In our case, the GreetingService instance will be injected when someone asks for the injection with name greetingToken.

So far now our code will look like this:

```
import { Component ,InjectionToken} from '@angular/core';import {GreetingService} from './greetingService';
```

```
export const greetingTokken = new InjectionToken<GreetingService>("GREET_TOKEN");export const greetingFactory=()=>  new GreetingService();@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[{    provide  : greetingTokken,    useFactory : greetingFactory,     }]})export class AppComponent  {
```

```
constructor(private greetingService : GreetingService){   console.log(this.greetingService.sayHello());  }  name = 'Angular';}
```

But then also we will have the same error:

![Image](https://cdn-media-1.freecodecamp.org/images/yOKshbzOHxjiPigdOXBK8p-IUkH7wOc8wnf8)

This is because in the constructor, where we are asking for the instance of our service, we have to tell it the unique string of our injection token that is `greetingToken`.

So let’s update our code:

```
export class AppComponent  {
```

```
constructor(@Inject(greetingTokken) private greetingService : GreetingService){   console.log(this.greetingService.sayHello('Neeraj'));  }  name = 'Angular';}
```

and now we will have the result that allows us to successfully pass a service from Angular dependency injection.

![Image](https://cdn-media-1.freecodecamp.org/images/Z0y7nt8qPli6OdjGSse2dEhxJV11Mk-yQ4kz)

Now let us assume you have some nested dependencies like this:

```
import{DomSanitizer} from '@angular/platform-browser';
```

```
export class GreetingService{  constructor (private domSanitizer:DomSanitizer){      }  sayHello(name){    return `Hello ${name}`  }}
```

So, in this case, we have to pass one more property to the provider’s object (that is deps) which is the array of all the dependencies:

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[{    provide  : greetingTokken,    useFactory : greetingFactory,    deps:[DomSanitizer]     }]})export class AppComponent  {
```

```
constructor(@Inject(greetingTokken) private greetingService : GreetingService  ){   console.log(this.greetingService.sayHello('Neeraj'));  }  name = 'Angular';}
```

> **_Up until now, whatever we have done has only been for learning purposes. It is not recommended to create manual providers until there is a need._**

So this is all the hard work done by Angular behind the scenes for us. We don’t have to do all this for registering our service. We can actually reduce the code, and instead of passing the factory and token manually, we can ask the framework to do this for us in that case.

The provide property, which is the injection token, will be the name of the service and Angular will internally create an injection token and factory for us.

We have to pass one more property (use-class) which tells the framework which class we need to use:

```
import { Component ,InjectionToken,Inject} from '@angular/core';
```

```
import {GreetingService} from './greetingService';
```

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[{    provide  : GreetingService,    useClass :GreetingService     }]})export class AppComponent  {
```

```
constructor( private greetingService : GreetingService  ){   console.log(this.greetingService.sayHello('Neeraj'));  }  name = 'Angular';}
```

So now our code looks much cleaner and we can further reduce it by just passing the name of the service. Then Angular under the hood will create the provide object, the factory, and the injection token for us and make the instance available to us when needed.

```
import { Component } from '@angular/core';
```

```
import {GreetingService} from './greetingService';
```

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[GreetingService]})export class AppComponent  {
```

```
constructor( private greetingService : GreetingService  ){   console.log(this.greetingService.sayHello('Neeraj'));  }  name = 'Angular';}
```

So in the end, our code looks very familiar. Now in the future, whenever you create a service, you know exactly what steps are involved to get that instance available.

If you like this article follow me to get more of this kind of stuff.

![Image](https://cdn-media-1.freecodecamp.org/images/GHJHXu-n2p6nfjIZmNgTMyNt-MBPTvPRLTkt)

Visit [Smartcodehub](https://www.smartcodehub.com/)

