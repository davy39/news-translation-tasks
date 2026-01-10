---
title: Angular Authentication made easy with Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-07T23:30:08.000Z'
originalURL: https://freecodecamp.org/news/angular-2-authentication-made-easy-with-firebase-246c282d9ef8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oOBXowI2IO9eCTcxP1BT-Q.jpeg
tags:
- name: angular2
  slug: angular2
- name: Firebase
  slug: firebase
- name: JavaScript
  slug: javascript
- name: Security
  slug: security
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Wassim Chegham


  UPDATE: The code in this article has been updated to Angular Final. We also assume
  that you’re using the latest Angular CLI.


  Any serious Web application requires some sort of authentication feature. In this
  blog post, we’ll set up...'
---

By Wassim Chegham

> UPDATE: The code in this article has been updated to Angular Final. We also assume that you’re using the latest Angular CLI.

Any serious Web application requires some sort of authentication feature. In this blog post, we’ll set up this feature for an Angular application using Firebase, thanks to the official [AngularFire2](https://github.com/angular/angularfire2) library.

### Create a new Firebase project

Before using Firebase with our application, we need to create a new project in our [Firebase developer console](https://console.firebase.google.com/):

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZzoMPcmlDgYRLCQgAFiU8Q.png)
_Firebase Developer Console_

To use the Firebase Authentication feature, we need to enable the **sign-in providers** we want to use in our project. In our case, we’re going to use Google, Facebook, Twitter and Github to log in our users.

You can find the Authentication page in: Your App → Auth → SIGN-IN METHOD:

![Image](https://cdn-media-1.freecodecamp.org/images/1*wfIpVAzDOEVFUJR2UjUp5g.png)

Some providers, such as Facebook, Twitter and Github, require you to provide an **App/Client/API ID** and **App/Client/API secret** keys, and use the given **OAuth URI** as the redirect URI:

![Image](https://cdn-media-1.freecodecamp.org/images/1*cmB2uiqwESrHHwKo1RVkgA.png)

In order to obtain this information, you will need to create one application for each provider using your developer account of each service (Github, Facebook and Twitter).

### Configure your services

![Image](https://cdn-media-1.freecodecamp.org/images/1*M372rrSgYuiwgODlftxKDQ.png)
_Github Application Settings_

For Github, go to your [developer settings](https://github.com/settings/developers), and [register](https://github.com/settings/applications/new) a new application.

Use your application **Client ID** and **Client Secret** in your Firebase configuration page.

You also need to fill in the **Authorization callback URL** using the **OAuth URI** from Firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UsjnM5koHUhanSlGXYR6Yg.png)
_Twitter Application Settings_

For Twitter, go to your [Application Management settings](https://apps.twitter.com/), and [create a new](https://apps.twitter.com/app/new) application.

Use your application **API key** and **API Secret** in your Firebase configuration page.

You also need to fill in the **Callback URL** (in the Settings tab) using the **OAuth URI** from Firebase.

![Image](https://cdn-media-1.freecodecamp.org/images/1*blTSqtexKVeShcVPDMHKaw.png)
_Facebook Developer Console_

Finally, for Facebook, go to your [developer apps](https://developers.facebook.com/apps/) home page, and click on the “Add New App” green button at the upper-right corner.

Use your **App ID** and **App Secret** in your Firebase configuration page.

You also need to add a new Web platform. Click on **+Add platform** at the bottom of the page—and fill in the Site URL with the redirect URI from Firebase (i.e. **OAuth URI**).

Now you are ready to use Google, Twitter, Github and Facebook as your authentication providers for your web application.

### Use AngularFire in your application

For the next step, I’m going to use an Angular application I scaffolded thanks to the [official Angular CLI](https://github.com/angular/angular-cli).

In this application, I’m going to use the Authentication providers we just set up in the previous step.

Here’s what the application looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*wmQDx_-Q87Gr-nu9iFRXGg.png)

Clicking on a button will call a specific provider, authenticate the user, and get their information:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zgPhCyiM1Z93aWXD-u3__g.png)
_User logged in using github.com_

#### Install and setup angularfire2

First things first, we need to install the _firebase_ and _angularfire2_ libraries:

```
$ npm install angularfire2 firebase --save
```

Then we need to install _Firebase_ types:

```
$ npm install @types/firebase
```

And add those types to your **src/tsconfig.json** file:

```
{  "compilerOptions": {    "declaration": false,    "emitDecoratorMetadata": true,    "experimentalDecorators": true,    "lib": ["es6", "dom"],    "mapRoot": "./",    "module": "es6",    "moduleResolution": "node",    "outDir": "../dist/out-tsc",    "sourceMap": true,    "target": "es5",    "typeRoots": [      "../node_modules/@types"    ],    "types": [      "jasmine",      "firebase",      "node"    ]  }}
```

A more detailed setup process is described in [the official docs](https://github.com/angular/angularfire2/blob/master/docs/1-install-and-setup.md).

#### Configure _AngularFire_ for your Application

In order to use Firebase with Angular, we need to provide some configuration for the AngularFire services.

Let’s start with the default Firebase configuration which looks like this:

```
defaultFirebase({  apiKey: "AIzaSyCk3weREVFpOIN6pL_QVVNFRl3C3keMIRU",  authDomain: "angular2-auth.firebaseapp.com",  databaseURL: "https://angular2-auth.firebaseio.com",  storageBucket: "angular2-auth.appspot.com"})
```

_Note: Don’t worry about this exposed **apiKey**. This key is only used to identify the different services of your project: a kind of project identifier._

You can get your Firebase **apiKey**, **projectId, databaseName,** and **bucket ID** from your application dashboard.

Click on the **WEB SETUP** button in the top-right corner:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qzOQlZJtR6U9luzBDaVwrw.png)

Next, for our use case, we want to provide a default authentication method:

```
firebaseAuthConfig({  method: AuthMethods.Popup})
```

Here, we choose to use a **Popup** to allow the user to log in. We could also use a Redirect method like this:

```
firebaseAuthConfig({  method: AuthMethods.Redirect})
```

Let’s now create a _CoreModule_ in **src/app/core.module.ts** where we will put our configuration. It is best practice to group core dependencies in a separate NgModule named [CoreModule](https://angular.io/docs/ts/latest/guide/ngmodule.html#!#core-module). Here is an example of such module:

```
import { BrowserModule } from '@angular/platform-browser';import { HttpModule } from '@angular/http';import { NgModule } from '@angular/core';import { FormsModule } from '@angular/forms';import {   AngularFireModule,   AuthMethods,   AuthProviders } from "angularfire2";
```

```
const firebaseConfig = {  apiKey: "AIzaSyCk3weREVFpOIN6pL_QVVNFRl3C3keMIRU",  authDomain: "angular2-auth.firebaseapp.com",  databaseURL: "https://angular2-auth.firebaseio.com",  storageBucket: "angular2-auth.appspot.com"};
```

```
@NgModule({  imports: [    BrowserModule,    FormsModule,    HttpModule,    AngularFireModule.initializeApp(firebaseConfig,{      provider: AuthProviders.Google,      method: AuthMethods.Popup    })  ],  exports: [    BrowserModule,  ]})export class CoreModule {}
```

#### Using it in your components

Now we’re finally ready to implement the authentication feature for our Angular application.

We need to inject the **AngularFire** service in the component’s constructor:

```
import { Component } from '@angular/core';import { AngularFire, AuthProviders } from 'angularfire2';
```

```
@Component({  moduleId: module.id,  selector: 'app-root',  templateUrl: 'app.component.html',  styleUrls: ['app.component.css']})export class AppComponent {  user = {};
```

```
  constructor(    public af: AngularFire  ) {    this.af.auth.subscribe(user => {      if(user) {        // user logged in        this.user = user;      }      else {        // user not logged in        this.user = {};      }    });  }}
```

> In a real world application, you would create a separate service that handles authentication. Think [SRP](https://en.wikipedia.org/wiki/Single_responsibility_principle) and [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). But for this tutorial, we will keep it simple.

The **AngularFire** service gives us the **auth** property which implements the Observable API. So that means we need to subscribe to this **auth** property in order to get the authentication state. A **_NULL_** value means the user is not logged in.

Let’s add a couple of buttons in the component’s view:

```
<button md-raised-button (click)="login()">  <img width="30" src="google-logo.png" />Use My Google Account</button><button md-raised-button (click)="logout()">  Logout</button>
```

We will use those buttons to log in and log out, using the Google provider as an example.

In **_app.component.ts_**, we need to implement the **_login()_** _and **logout()**_ methods:

```
login() {  this.af.auth.login({    provider: AuthProviders.Google  });} logout() {  this.af.auth.logout();}
```

To log a user in, we call the **this.af.auth.login()** method using the Google provider, and **this.af.auth.logout()** to log a user out.

The **AngulareFire login()** usually needs an authentication method. In our case, it will use the default method (i.e. **AuthMethods.Popup)** we set up in the bootstrap phase.

If you need to override the authentication method when calling the **login()** method, just provide a new auth configuration:

```
login() {  this.af.auth.login({    provider: AuthProviders.Google,    method: AuthMethods.Redirect  });}
```

Once everything is setup and working correctly, we can inspect the **_user_** object containing all the user’s session tokens sent by Google (the authentication provider):

![Image](https://cdn-media-1.freecodecamp.org/images/1*mQcUhIAo_anodDNp_Z0tnQ.png)

You can get the user’s information such the **displayName** and the **photoURL** form the **auth.provideData** entry.

That’s it! Your users can now log in using their Google accounts.

You can add Github and Facebook in much the same way.

See the complete working application [hosted on Firebase](https://angular2-auth.firebaseapp.com) or read the complete source code [on Github](https://github.com/manekinekko/angular-firebase-authentication).

> NOTE: I’m in the process of migration this repo to Angular final ([see branch](https://github.com/manekinekko/angular-firebase-authentication/tree/migration-to-angular-2.0.0)). This process is pending because of [this issue](https://github.com/manekinekko/angular-firebase-authentication/issues/3) in AngularFire2.

[**manekinekko/angular-firebase-authentication**](https://github.com/manekinekko/angular-firebase-authentication)  
[_angular-firebase-authentication - An angular demoing Firebase Authentication providers_github.com](https://github.com/manekinekko/angular-firebase-authentication)

### Tips & References

_Follow [@manekinekko](https://twitter.com/manekinekko) to learn more about the web platform._

