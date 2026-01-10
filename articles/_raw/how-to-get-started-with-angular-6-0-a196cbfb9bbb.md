---
title: How to get started with Angular 6.0
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-06T16:16:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-angular-6-0-a196cbfb9bbb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mmxWHaqZZtNMs_ggYnx8hg.jpeg
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Visual Studio Code
  slug: visual-studio-code
seo_title: null
seo_desc: 'By Ankit Sharma

  Learn what’s new and build an app

  Angular has released its latest version, Angular 6.0. In this article, we will understand
  the new features of Angular 6.0 and also set up a new project with the help of Angular
  CLI 6.0 and Visual Stud...'
---

By Ankit Sharma

#### Learn what’s new and build an app

Angular has released its latest version, Angular 6.0. In this article, we will understand the new features of Angular 6.0 and also set up a new project with the help of Angular CLI 6.0 and Visual Studio Code.

### What’s new in Angular 6.0?

#### ng update

A new CLI command that will update your project dependencies to their latest versions.

#### ng add

Another new CLI command that makes adding new capabilities to your project easier.

#### Angular Elements

This is a new feature that allows us to compile Angular components to native web components which we can use in our Angular app.

#### <template> element is deprecated

You can’t use <template> anymore inside of your component templates. You need to use <ng-template> instead.

#### Library support

Angular CLI now has the support for creating and building libraries. To create a library project within your CLI workspace, run the following command: ng generate library <name> (for example: ng generate library my-demo-lib)

#### Angular Material Starter Components

If you run “ng add @angular/material” to add material to an existing application, you will also be able to generate 3 new starter components:

* **Material Sidenav**  
 A starter component including a toolbar with the app name and the side navigation
* **Material Dashboard**  
 A starter dashboard component containing a dynamic grid list of cards
* **Material Data Table**  
 A starter data table component that is pre-configured with a datasource for sorting and pagination

#### Workspace support

Angular CLI now has support for workspaces containing multiple projects, such as multiple applications and/or libraries.

#### The “.angular-cli.json” file has been deprecated

Angular projects will now use “angular.json” instead of “.angular-cli.json” for build and project configuration.

#### Use RxJS V6

Angular 6 will also allow us to use RxJS V6 with our application.

#### Tree Shakable Providers

Angular 6.0 allows us to bundle services into the code base in modules where they are injected. This will help us to make our application smaller.

For example: Earlier, we used to reference our services as below.

```
// In app.module.ts    @NgModule({    ...    providers: [MyService]  })  export class AppModule {}    // In myservice.ts     import { Injectable } from '@angular/core';    @Injectable()  export class MyService {    constructor() { }  }
```

This approach will still work, but Angular 6.0 provides a new and easier alternative to this. We no longer need to add references in our NgModule. We can inject the reference directly into the service. Therefore, we can use the service as below:

```
// In myservice.ts    import { Injectable } from '@angular/core';    @Injectable({    providedIn: 'root',  })  export class MyService {    constructor() { }  }
```

Those are the new features/improvements in the latest release of Angular. Let’s move on and create our first application using Angular 6.0.

### Prerequisites

* Install the latest version of Node.js from [here](https://nodejs.org/en/download/)
* Install Visual Studio Code from [here](https://code.visualstudio.com/)

Installing Node.js will also install npm on your machine. After installing Node.js, open the command prompt and run the following set of commands to check the version of Node and npm installed on your machine.

Refer to the below image:

![Image](https://cdn-media-1.freecodecamp.org/images/PpLMXyOskr9A5wpHDndRTG8IkvpRvJ6H9DVb)

Now that we’ve installed Node and npm, the next step is to install Angular CLI. Run the following command in a command window. This will install Angular 6.0 CLI globally on your machine.

![Image](https://cdn-media-1.freecodecamp.org/images/rskMSFRtqxuqxXA80OYMwHVhnR-3AGrxDsS5)

Open VS Code and navigate to View >> Integrated Terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/-bJC4pD8YZXAZdB2h6ez7WjmdZWcS0D5IpMo)

This will open a terminal window in VS Code.

Type the following sequence of commands in the terminal window. These commands will create a directory with the name “_ng6Demo_” and then create an Angular application with the name “_ng6App_” inside that directory.

* mkdir ng6Demo
* cd ng6Demo
* ng new ng6App

![Image](https://cdn-media-1.freecodecamp.org/images/n7ub05-40gA8P9HxCosSWJDoy5PyYSA0kHoA)

There we go — we have created our first Angular 6 application using VS Code and Angular CLI. Now run the following command to open the project.

Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/hcwLxqSELFiSmKaGJ9Wbjmlmtm4ThL1ZpNVU)

This will open the code file of our application in a new VS Code window. You can see the following file structure in Solution Explorer.

![Image](https://cdn-media-1.freecodecamp.org/images/m8PPvMTg1DzehHavw-zrEx16BuG-RIQ5jMSy)

Notice that the folder structure is a little bit different from the older version of Angular. We have a new “angular.json” file instead of the old “.angular-cli.json” file. This config file will still serve the same task as before, but the schema has changed a bit.

Open the package.json file and you can observe that we have the latest Angular 6.0.0 packages installed in our project.

```
{    "name": "ng6-app",    "version": "0.0.0",    "scripts": {      "ng": "ng",      "start": "ng serve",      "build": "ng build",      "test": "ng test",      "lint": "ng lint",      "e2e": "ng e2e"    },    "private": true,    "dependencies": {      "@angular/animations": "^6.0.0",      "@angular/common": "^6.0.0",      "@angular/compiler": "^6.0.0",      "@angular/core": "^6.0.0",      "@angular/forms": "^6.0.0",      "@angular/http": "^6.0.0",      "@angular/platform-browser": "^6.0.0",      "@angular/platform-browser-dynamic": "^6.0.0",      "@angular/router": "^6.0.0",      "core-js": "^2.5.4",      "rxjs": "^6.0.0",      "zone.js": "^0.8.26"    },    "devDependencies": {      "@angular/compiler-cli": "^6.0.0",      "@angular-devkit/build-angular": "~0.6.0",      "typescript": "~2.7.2",      "@angular/cli": "~6.0.0",      "@angular/language-service": "^6.0.0",      "@types/jasmine": "~2.8.6",      "@types/jasminewd2": "~2.0.3",      "@types/node": "~8.9.4",      "codelyzer": "~4.2.1",      "jasmine-core": "~2.99.1",      "jasmine-spec-reporter": "~4.2.1",      "karma": "~1.7.1",      "karma-chrome-launcher": "~2.2.0",      "karma-coverage-istanbul-reporter": "~1.4.2",      "karma-jasmine": "~1.1.1",      "karma-jasmine-html-reporter": "^0.2.2",      "protractor": "~5.3.0",      "ts-node": "~5.0.1",      "tslint": "~5.9.1"    }  }
```

The name of our Angular application is _ng6app_ which is inside _ng6demo_ directory.

So, we will first navigate to our application using the below commands.

And then we use the following command to start the web server.

![Image](https://cdn-media-1.freecodecamp.org/images/aERCZwSg9S74d2ZxBtQxwx50kL2IRfmJjSYy)

After running this command, you can see that it is asking to open [_http://localhost:4200_](http://localhost:4200) in your browser. So, open any browser on your machine and navigate to this URL. Now, you can see the following page.

![Image](https://cdn-media-1.freecodecamp.org/images/IjRPyX7l6pOcgmXtT3ml1WSYRFU09uhDrGAD)

Now we will try to change the welcome text on the screen. Navigate to _/src/app/app.component.ts_ file and replace the code with the below code.

```
import { Component } from '@angular/core';    @Component({    selector: 'app-root',    templateUrl: './app.component.html',    styleUrls: ['./app.component.css']  })  export class AppComponent {    title = 'Csharp Corner';  }
```

Now open the browser, you can see that the web page has been updated with new welcome message “Welcome to Csharp Corner!”

![Image](https://cdn-media-1.freecodecamp.org/images/c5mAy0iqq0fAlCVSgceh51pMHuH7OEoreQXN)

In this article we learned about the new features of Angular 6.0. We have installed the Angular 6.0 CLI and created our first Angular 6.0 application with the help of Visual Studio Code. We have also customized the welcome message on the webpage.

You can also find this article at [C# Corner](https://www.c-sharpcorner.com/article/getting-started-with-angular-6/).

You can check my other articles on Angular [here](http://ankitsharmablogs.com/category/angular/)

Originally published at [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)

