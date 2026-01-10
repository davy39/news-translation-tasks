---
title: Lazy Loading in Angular – A Beginner's Guide to NgModules
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-27T18:17:43.000Z'
originalURL: https://freecodecamp.org/news/lazy-loading-in-angular-intro-to-ngmodules
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/cat-1.jpg
tags:
- name: Angular
  slug: angular
seo_title: null
seo_desc: "By Arjav Dave\nWhat is Lazy Loading?\nLazy loading is the process of loading\
  \ components, modules, or other assets of a website as they're required. \nSince\
  \ Angular creates a SPA (Single Page Application), all of its components are loaded\
  \ at once. This m..."
---

By Arjav Dave

## What is Lazy Loading?

Lazy loading is the process of loading components, modules, or other assets of a website as they're required. 

Since Angular creates a [SPA (Single Page Application)](https://en.wikipedia.org/wiki/Single-page_application#:~:text=From%20Wikipedia%2C%20the%20free%20encyclopedia,browser%20loading%20entire%20new%20pages.), all of its components are loaded at once. This means that a lot of unnecessary libraries or modules might be loaded as well.

For a small application this would be okay. But as the application grows the load time will increase if everything is loaded at once. Lazy loading allows Angular to load components and modules as and when they're needed.

First of all, to understand how lazy loading works in Angular, we need to understand the basic building blocks of the framework: NgModules.

## What are NgModules?

Angular libraries like RouterModule, BrowserModule, and FormsModule are NgModules. [Angular Material](https://material.angular.io/), which is a third party tool, is also a type of NgModule. 

NgModules consist of files and code related to a specific domain or that have a similar set of functionalities.

A typical NgModule file declares components, directives, pipes, and services. It can also import other modules that are needed in the current module.

One of the important advantages of NgModules is that they can be lazy loaded. Let’s have a look at how we can configure lazy loading.

You can [check below](#heading-root-module) to see what a basic NgModule file looks like. 

## How to Create NgModules

In this tutorial, we will create two modules, _Module_ _A_ and _Module B_, which will be lazy loaded. On the main screen we will have two buttons for loading each module lazily.

### Create the Project

Create a new Angular project called _lazy-load-demo_ by executing the below command:

```
ng new lazy-load-demo --routing --style css
code lazy-load-demo
```

Here, we are creating a new project with routing. Secondly, we mention the stylesheet format to CSS. The second command opens your project in VS Code.

<h3 id="root-module">Root Module</h3>

By default, a root module or app module is created under _/src/app_. Below is the NgModule file that's created.

```
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

First, we import all the required modules and components.

After that, the **`@NgModule`** decorator states that the AppModule class is a type of NgModule. The decorator accepts _declarations, imports, providers,_ and _bootstrap._ Here are the descriptions for each of them:

* **declarations**: The components in this module.
* **imports**: The modules that are required by the current module.
* **providers**: The service providers, if any.
* **bootstrap**: The _root_ component that Angular creates and inserts into the `index.html` host web page.

### Main screen

The main screen will have two buttons, **Load Module A** & **Load Module B.** As the name suggests, clicking these buttons will lazily load each module.

For that, replace your _app.component.html_ file with the contents below.

```
<button style="padding: 20px; color: white; background-color: green;" routerLink="a">Load Module A</button>
<button style="padding: 20px; color: white; background-color: blue;" routerLink="b">Load Module B</button>
<router-outlet></router-outlet>
```

Let’s define the modules for routes _a_ & _b_.

### Lazy Loaded Modules

In order to create lazy loaded modules, execute the below commands:

```
ng generate module modulea --route a --module app.module
ng generate module moduleb --route b --module app.module
```

The commands will generate two folders called **modulea** and **moduleb**. Each folder will contain its own _module.ts_, _routing.ts_ and _component_ files.

If you check your _app-routing.module.ts_ you will see the below code for routes:

```
const routes: Routes = [
  { path: 'a', loadChildren: () => import('./modulea/modulea.module').then(m => m.ModuleaModule) },
  { path: 'b', loadChildren: () => import('./moduleb/moduleb.module').then(m => m.ModulebModule) }
];
```

It implies that when route _a_ or _b_ is visited, load their respective modules lazily.

On running the project with **ng serve**, you will see the below screen:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.18.55-PM.png)
_Home Page_

When you click the _Load Module A_ button, you will be routed to page _a_. This is how your screen should look:

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.18.14-PM.png)
_Lazily loaded Module A_

You should see a similar screen that says **moduleb works!** when you click on _Load Module B._

## How to Verify that the Lazy Loading Worked

In order to verify that the files loaded, open the developer tools by pressing F12. After that, visit the _Network_ tab as you can see in the screenshot below. When you refresh the page it will show a few files that were requested.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Network-Tab-1.jpg)
_Network Tab_

Go ahead and clear your list of requests by hitting the clear button as shown in the image below.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.42.21-PM.png)

When you click on the _Load Module A_, you will see a request for _modulea-modulea-module.js_ as in the screenshot below. This verifies that _Module A_ was lazily loaded.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.46.50-PM.png)
_Module A Loaded_

Similarly, when you click _Load Module B_, the _moduleb-moduleb-module.js_ file is loaded. This verifies that Module B was loaded lazily.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/Screenshot-2021-04-25-at-11.47.10-PM.png)
_Module B Loaded_

Now, when you try to click the buttons it will not load these _js_ files again.

## Use Cases for NgModules

As we have seen, it's very easy to create lazy loading modules. There are lots of use cases where they are useful, such as

* Creating a separate module for pre-login vs post-login screens.
* For an e-commerce website, vendor facing vs customer facing screens can belong to separate modules. You can also create a separate module for payment.
* A separate CommonModule which contains shared components, directives, or pipelines is usually created. Directives like _Copy Code_ button, components like _up vote/down vote_ are usually included in a common module.

## Conclusion

For smaller websites, it might not matter much that all the modules are loaded at once. But, as the site grows, it’s helpful to have separate modules which are loaded as needed.

Because of lazy loading, load time for the websites can be reduced drastically. This is specially helpful when you are trying to rank higher for SEO. Even if not, shorter loading times means better user experience.

Are you interested in more tutorials? Check these resources out:

* [Learn TDD with Integration Tests in .NET](https://arjavdave.com/2021/04/14/learn-test-driven-development-with-integration-tests-in-net-5-0/) 
* [How to authenticate & authorise API’s correctly in .NET](https://arjavdave.com/2021/03/31/net-5-setup-authentication-and-authorisation/)
* [Azure Functions & wkhtmltopdf: Convert HTML to PDF](https://arjavdave.com/2021/03/22/azure-functions-wkhtmltopdf/)  
  

