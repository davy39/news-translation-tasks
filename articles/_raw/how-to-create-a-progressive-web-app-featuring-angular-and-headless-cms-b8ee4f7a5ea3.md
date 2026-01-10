---
title: How to create a progressive web app featuring Angular and headless CMS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-17T16:47:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-progressive-web-app-featuring-angular-and-headless-cms-b8ee4f7a5ea3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZBkMjm06K3zeKAuXCL0mkg.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: progressive web app
  slug: progressive-web-app
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ondrej Chrastina

  Have you ever wondered how a headless Content Management System fits in with Progressive
  Web Apps?

  I recently read my colleague Bryan’s story about Progressive Web Apps. The article
  talks about the implementation of a Progressive ...'
---

By Ondrej Chrastina

Have you ever wondered how a headless Content Management System fits in with Progressive Web Apps?

I recently read my colleague [Bryan](https://www.freecodecamp.org/news/how-to-create-a-progressive-web-app-featuring-angular-and-headless-cms-b8ee4f7a5ea3/undefined)’s [story](https://hackernoon.com/creating-a-progressive-web-app-with-a-headless-cms-part-1-85ede9dba59b) about Progressive Web Apps. The article talks about the implementation of a [Progressive Web App](https://developers.google.com/web/progressive-web-apps) (PWA) that lists interesting places stored in the headless CMS.

You could install this app on your device. It uses a service worker to cache the application and data about the points of interest. The application was written in plain JavaScript.

Having written a good share of JavaScript code, I wanted to expand on the concept using more complex frameworks.

I narrowed my choices down to three big players — React, Vue, and Angular. I chose to use Angular, because it has already support for service workers, and I wanted to use [TypeScript](https://www.typescriptlang.org/).

Each step of this tutorial will be accompanied by a link to a GitHub commit. This way, you’ll always be able to see what the code looks like.

To run the app, just download or clone the commit and run `npm install` and `ng serve -o`. The whole code is stored in [one of the branches](https://github.com/Kentico/cloud-sample-angular-pwa-app/commits/v1-introduction).

Let’s get to it!

#### Prerequisites

* [node.js](https://nodejs.org/en/download) v8+
* [Angular CLI](https://www.npmjs.com/package/@angular/cli) v.1.7.4 installed as a global dependency via the npm package manager: `npm install -g @angular/cli`

#### Getting started

First of all, generate a new project. You can easily generate all boilerplate code using the awesome Angular CLI tools. Just navigate to a folder and generate a ready-to-run code:

```bash
ng new cloud-sample-angular-pwa-aps
```

#### Boilerplate configuration

![Image](https://cdn-media-1.freecodecamp.org/images/4Hjiz65hb-1T-nUK-LjuICXRKbymmoBvyx88)
_[Configured boilerplate commit](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/1857f253955e4abf0685222fa958d199648dd6ba" rel="noopener" target="_blank" title=")_

There are a few steps to configure the boilerplate.

The generated code uses plain CSS by default. But, you might want to make your life easier with SCSS. To achieve this, perform these steps:

1. Set `defaults.styleExt` value from `css`to `scss`in the`/.angular-cli.json`configuration file
2. Rename `styles.css` to `styles.scss`
3. Rename `/src/app.component.css` to `/src/app.component.scss`and reflect this renaming in `app.component.ts` in the component declaration atribute’s `styleUrls` property value.

#### **Create some initial** content **for the app**

* Global styles: [/src/styles.scss](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/1857f253955e4abf0685222fa958d199648dd6ba#diff-6a2256f44598ec970b4bd034962e011e)
* Component: [/src/app/app.component.html](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/1857f253955e4abf0685222fa958d199648dd6ba#diff-465e9f13ce23ec4a1e366935273fdbb6) and [/src/app/app.component.scss](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/1857f253955e4abf0685222fa958d199648dd6ba#diff-f4c58ad626d121a4d36442d6696213eb)

Lets have a look!

![Image](https://cdn-media-1.freecodecamp.org/images/Al8CUwqAdD24f1o-Wuw5u4xrLM8HYpSmFaM7)
_Voila, first run of the app._

Just run this command:

```bash
ng serve -o
```

#### Load the data

![Image](https://cdn-media-1.freecodecamp.org/images/4LCfjsHaWVGURtUehLSGhtx2095mR96ExNEr)
_[Data loading commit.](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/00072d54eda9023f6f9176fc6de3ed49b339b602" rel="noopener" target="_blank" title=")_

Let’s finally use the power of Angular. In this section, we will define an [injectable](https://angular.io/guide/dependency-injection) client that allows the app to get [Kentico Cloud](https://kenticocloud.com/) data. I will use the same data source as Bryan used in his article.

First of all, install [Kentico Cloud Delivery SDK](https://github.com/Enngage/KenticoCloudDeliveryTypeScriptSDK) via the following command:

```bash
npm install -P kentico-cloud-delivery-typescript-sdk
```

Then, create a client provider that will be used in dependency injection.

Create a new file in the `/src/app` folder and name it `delivery-client.provider.ts`. This [provider](https://angular.io/guide/dependency-injection#factory-providers) module needs to export an object defining the factory used to create our client. In the code below, you can see the ID of the project in Kentico Cloud where the data is stored.

```ts
import { DeliveryClient, DeliveryClientConfig } from 'kentico-cloud-delivery-typescript-sdk';

export const DeliveryClientFactory = (): DeliveryClient => {
    const projectId = '975bf280-fd91-488c-994c-2f04416e5ee3';
    
    return new DeliveryClient(
        new DeliveryClientConfig(projectId, [])
    );
};

export const DeliveryClientProvider = {
    provide: DeliveryClient,
    useFactory: DeliveryClientFactory,
    deps: []
};
```

Next, edit `app.module.ts`. This is the place where you state which modules are loaded.

```ts
... 
import { DeliveryClientProvider } from './delivery-client.provider';
...

@NgModule({
...
providers: [DeliveryClientProvider]
...
})
```

Now we are ready to use the client in the app component.

We will set up the `app.component.ts` to use the `DeliverClient` that is auto-magically injected as a parameter to the constructor. We’ll also subscribe the component to the client’s observable and we’ll define a corresponding observer action.

```ts
import { Component, OnInit, OnDestroy } from '@angular/core';
import { DeliveryClient, ContentItem } from 'kentico-cloud-delivery-typescript-sdk';
import { Subscription } from 'rxjs/Subscription';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit, OnDestroy {
  dataSubscription: Subscription;
  pointsOfInterest: ContentItem[];
  
constructor(private deliveryClient: DeliveryClient) { }

ngOnInit() {
    this.dataSubscription = this.deliveryClient
      .items<ContentItem>()
      .type('point_of_interest')
      .get()
      .subscribe(response => {
        this.pointsOfInterest = response.items;
      });
  }
  
ngOnDestroy(): void {
    this.dataSubscription.unsubscribe();
  }
}
```

The last step is to display the data from CMS using the Angular `ngFor` directive to iterate through the items and render them.

```html
<header>
    <h2>Pack and Go</h2>
</header>
<main class="main">
    <div class="card" *ngFor="let poi of pointsOfInterest">
        <h2 class="title">{{poi.title.value}}</h2>
        <div class="content" innerHTML="{{poi.description.value}}"></div>
        <a class="map-link" target="_blank" href="http://maps.google.com/?ie=UTF8&amp;hq=&amp;ll={{poi.latitude__decimal_degrees_.value}},{{poi.longitude__decimal_degrees_.value}}&amp;z=16">
           Open the map
        </a>
    </div>
</main>
```

#### Allow adding a shortcut icon

Now, we’ll make the app capable of adding its icon to the desktop or start screen of the device.

![Image](https://cdn-media-1.freecodecamp.org/images/hDtH-KcbAIVk8hyusfrbGV8JaHEd--pLYSbk)

This step is quite easy. It requires us to create a JSON file containing metadata about the app and link it from the `head` tag. The manifest file should point to multiple URLs of icons in various sizes.

We should also list the `manifest.json` file in an assets declaration in the `.angular-cli.json` configuration file.

```json
{
    ...
    apps: {
        assets : [
            ...,
            "manifest.json"
        ],
        ...
    },
    ...
}
```

But, more importantly, link to the `manifest.json` file from `index.html`.

```html
<link rel="manifest" href="manifest.json" />
```

Finally, we’ll create the manifest itself, together with all the icon renditions. Take a look at the link below to see the result.

![Image](https://cdn-media-1.freecodecamp.org/images/jmtJk-647gvGgq-bdjB3ssca-qbgo2QbmR8p)
_[Commit link with the data.](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/abb80401d8775c608b5e554e17da2f7ef1437a42" rel="noopener" target="_blank" title=")_

#### Set up the service worker

The concept of the service worker is what makes PWA apps revolutionary.

Service workers work as a proxy between the client and the internet. Depending on the actual configuration, the service worker can pre-cache the app skeleton (called the ‘app shell’) during the first load. This means that subsequent requests are blazing-fast. The service worker can also silently cache all other application data.

First of all, it is required to install the service worker module to the application.

```bash
npm install -P @angular/service-worker
```

Now enable the service worker in Angular in the `.angular-cli.json` configuration file.

```json
{
    ...
    apps: {
        "serviceWorker": true,
        ...
    },
    ...
}
```

Now, let’s import the service worker module to our app using the `app.module.ts` file.

```ts
...
import { ServiceWorkerModule } from '@angular/service-worker';
...
@NgModule({
  ...
  imports: [
    ...
    ServiceWorkerModule.register('/ngsw-worker.js', { enabled: environment.production })
  ],
  ...
})
˛...
```

The last thing is to configure the caching strategies for the app shell and the data. First we need to create `ngsw-config.json` configuration file under the `/src` folder.

For the app shell, we’ll use the default set up described in the [documentation](https://angular.io/guide/service-worker-getting-started#step-4-create-the-configuration-file-ngsw-configjson). This configuration will pre-fetch `index.html` , the `favicon.ico` , and the app shell, including the linked CSS and JavaScript bundles. Files in `/assets` folder are lazy-loaded.

Requests for the data from Kentico Cloud will use another caching strategy. We will define an API endpoint as a new [data group](https://angular.io/guide/service-worker-config#datagroups) and set the caching to use the [freshness](https://angular.io/guide/service-worker-config#strategy) strategy. In the commit link bellow, you can see the whole content of the configuration file.

![Image](https://cdn-media-1.freecodecamp.org/images/-fdiGKoHlYE2tkUjOZiS7V89pT0d1jjedLkc)
_[Commit link](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/6a5f2b3230f04901c51573124bafce4bd31672e4" rel="noopener" target="_blank" title=")_

Now we are ready to install the app on the device. For instance, in Chrome in Android, you can do so by tapping the ellipsis glyph and choosing “Add to Home screen”.

![Image](https://cdn-media-1.freecodecamp.org/images/NLmY5ZkuUm8267AT-VfDutcekoSzFp6uhGuO)

All right, we’re done. Despite a quick and simple implementation, the app is quite powerful and fast. And we’re free to extend it in various ways, like importing the material design or font icons.

The PWA APIs also allow us to use cool native features such as:

* read device’s sensors
* display push notifications
* and use the device’s cameras.

Our app could also sense when the device transitions from online to offline, and vice versa**.** We could also use the [automatically generated, strongly-typed models of content items](https://www.npmjs.com/package/kentico-cloud-model-generator-utility) from the CMS.

As you can see, creating a PWA in Angular is easy, yet allows us to extend the app much further.

