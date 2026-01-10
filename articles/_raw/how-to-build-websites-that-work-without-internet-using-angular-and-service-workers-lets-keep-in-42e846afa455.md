---
title: How to build websites that work without internet using Angular & service workers
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-03T16:21:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-websites-that-work-without-internet-using-angular-and-service-workers-lets-keep-in-42e846afa455
coverImage: https://cdn-media-1.freecodecamp.org/images/0*rJj-3GV2wU_Ky6gZ.png
tags:
- name: Angular
  slug: angular
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Tomiwa

  Introduction

  In this article, you will learn the theory of how service workers work. I provide
  a short tutorial to apply that theory to make a website that runs without the internet.
  Finally, I’ll discuss what this means for you and the fut...'
---

By Tomiwa

### Introduction

In this article, you will learn the theory of how service workers work. I provide a short tutorial to apply that theory to make a website that runs without the internet. Finally, I’ll discuss what this means for you and the future of the internet.

I get excited when talking about service workers. I am going to go on a quick rant on the problem this solves and why this is awesome. Then I dive into the theory of how service workers work and why it is awesome. If you want to jump straight to the theory or the tutorial, go to the sections starting with titles **Theory** and **Application** for the code.

This blog post is also available as:

* [Youtube Video](http://bit.ly/pwa-tutorial-video)
* [Slide deck](http://bit.ly/pwa-tutorial-slides)
* [Podcast](https://anchor.fm/tomiwa1a/episodes/How-to-Build-Websites-that-work-without-Internet-Using-Angular--Service-Workers-and-Firebase-e2ccp2)

### Table of Contents

* Websites are Strange
* Theory: How Servicer Workers Work
* Application: Tutorial on How to Build Offline Websites
* Prerequisites
* Installing the Service Worker
* Part 1a: Build The Service Worker
* Service Worker Output
* Part 1b: Testing The Service Worker (#2001441)
* Creating A Mini Server
* Inspecting the Server Requests
* Where are the Files Being Saved?
* Part 2: Saving External Data (Part 1 Git Tag: pwa-tutorial-0.1 )
* Saving External API calls: #8593ada
* Part 3: Notify Users of New Updates (Part 2 Git Tag: pwa-tutorial-0.2)
* Part 4: Deployment (Part 3 Git Tag: pwa-tutorial-0.3)
* Conclusion
* Who Needs Mobile Apps
* The Future of Websites
* Further Reading

### Websites are Strange

I realized something recently that made me truly realize how powerful service workers can be. When I have internet, it feels like there are infinitely many things competing for my attention.

But when I am on a plane for example, and there is no internet connection, the competition for my attention is much less fierce. The three things I can usually do is look through my photos, watch a downloaded movie or read an ebook.

With service-workers, if you are able to deliver an offline web experience for your users, you are able to get their attention in one of those few moments when the competition for it is least fierce.

Let’s start with a simple diagram. What do the two circles in this Venn diagram represent?

![Image](https://cdn-media-1.freecodecamp.org/images/0*E2A3mu1X9dugLi3F)

Let me give you a hint. Amazon, Alibaba, and Facebook are some of the world’s biggest websites, servicing millions of users every day. Here are some stats to put things in context for you:

* Alibaba [$25 billion](https://www.forbes.com/sites/helenwang/2017/11/12/alibabas-singles-day-by-the-numbers-a-record-25-billion-haul/#1a6df2421db1) in sales in one day (singles day)
* [40%](https://www.skyhighnetworks.com/cloud-security-blog/microsoft-azure-closes-iaas-adoption-gap-with-amazon-aws/) of cloud computing clients use Amazon Web Services Including [Apple](https://techcrunch.com/2018/02/27/apple-now-relies-on-google-cloud-platform-and-amazon-s3-for-icloud-data/), Netflix, and CIA
* [2.2 Billion](https://www.statista.com/statistics/264810/number-of-monthly-active-facebook-users-worldwide/) people use Facebook every month, 700 million on Instagram

This is all well and good but there’s just one small problem. Without wifi, their entire websites are completely unusable. Even if you just want to do simple tasks like look at product reviews for items that are already in your shopping cart, you can’t do anything.

Now compare that to sites like [Google Drive](https://www.google.com/drive/) or [Atila.ca](https://atila.ca/). [Atila.ca](http://atila.ca/) doesn’t have a million users but even when you have no internet connection, you can still use the site. Google Drive is another website that does this well. You can actually use Google Drive even without internet. Like how you would use a desktop app like Microsoft Word. Learn something new everyday right?

![Image](https://cdn-media-1.freecodecamp.org/images/0*tcZGksocJwwGM4En)

In the past, it almost seemed like a truism that websites would not work without the internet. Once you realize the potential of service workers, you completely change your perspective on how you think about websites. You begin to imagine the significant user experience improvements we can have on our favorite sites.

Imagine if you are on the subway commuting to work with no internet. You do not even have any cell phone service. But you could still review the product reviews of the items in your Amazon shopping cart. Or you’re on a long plane ride. While your phone is in airplane mode you can read the most popular articles from The New York Times. Or your favorite articles in a list that you chose to save for later.

You can see that the potential is great and it easy to start daydreaming. Let’s get back to reality and dig into the theory of how this is all possible.

### Theory: How Servicer Workers Work

A service worker is a proxy or messenger between your browser and the internet. When your web app asks for resources (images, html files, json API etc.) the service worker gets it for you without needing to ask the internet. In literal terms, it is a Javascript file that gets shipped along with the rest of your app. This file has code that tells your app how to intercept network requests and get it from your network cache.

Typically, when a website is first loaded, the web browser makes a set of requests to the network for the assets that your website needs to run. Typically including:

* html files for content display
* CSS files for styling
* Js files for application logic
* Images and other assets

When your internet is not working, there is no way for the browser to contact the network to retrieve the files necessary for displaying the website. So it fails and you get the infamous “jumping Dinosaur” on Google Chrome.

With service workers. The first time you visit a site, in addition to the usual set of index.html, styles.css, main.js etc. files that get requested, the browser also requests a service worker javascript file from your website. This file then gets downloaded and saved to your browser cache. The serviceworker file then downloads, versions and caches all the files in your application to serve it for later.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DWZmifjCFHNB6cyq)

This has two very important benefits. As is mentioned in the title, this means that even when your internet connection is down, the website will still work. It never actually has to ask the internet for anything. The service worker has all the files you will need.

Conversely, this also means that even if you do have internet, the application will also run faster. On future website loads, instead of making a full round trip to the network to get the application files. It simply retrieves the files from the browser cache and serves it to the user.

### Application: How to Build Offline Websites

#### Prerequisites

Before you start make sure you have the following installed

* [Node.js® and npm](https://nodejs.org/en/download/)
* Make sure you have node 8.X or greater (node -v ) and npm 5.x or greater ( npm -v)
* Globally install [Angular CLI](https://github.com/angular/angular-cli):
* `npm install -g @angular/cli`
* Google Chrome Browser (optional, but recommended)
* Google Account (optional, only if you want to deploy to Firebase)

#### Launch the project

* Go to [https://github.com/atilatech/atila-web-app](https://github.com/atilatech/atila-web-app)
* Clone the [demo.atila.ca](https://demo.atila.ca/) web app from Github: [atila-web-app](https://github.com/atilatech/atila-web-app)
* Check out the pwa-tutorial branch: `git checkout pwa-tutorial`
* Check out the tutorial start commit: `git checkout pwa-tutorial-0.0`
* Install npm modules: `npm install`
* Start the app!: `ng serve -o`

If you get a `No NgModule` error, go to any .ts file and put a space. This is a really strange bug but you can read this [Github issue](https://github.com/angular/angular-cli/issues/9292#issuecomment-360178485) for more information.

#### Installing the Service Worker

In order to install the Service Worker and get access to the various Service Worker objects in our app, we need to do the following.

1. Install the @angular/serviceworker module: npm install @angular/serviceworker
2. This installs an npm package that includes various service worker Javascript objects that we will use in the future steps
3. Tell angular-cli to build project with service worker: ng set apps.0.serviceWorker=true
4. Tell angular CLI to automatically produce a Javascript file that contains the code for the service worker when building project explained in the next step.
5. Configure your service worker in ngsw-config.json
6. This tells your service worker, exactly what files it should be saving and how it should be saving them
7. assetGroups: files that are included as part of the app
8. When the app updates, these resources update as well
9. dataGroups: external resources not versioned with the app
10. Install Mode: What caching strategy to use when first seeing this file
11. UpdateMode: What caching strategy to use when updating the file, after we’ve already installed it
12. Caching strategy
13. Prefetch: Save these files before we even ask for it
14. Lazy: Save these files only after they’ve been requested at least once
15. Add a manifest.json file and reference it in index.html

#### Service Worker Configuration

![Image](https://cdn-media-1.freecodecamp.org/images/0*PZYiuo0W10jQvHmo)

* This tells your service worker exactly what files it should be saving and how it should be saving them:
* assetGroups: files included as part of the app
* When the app updates, these resources update as well
* dataGroups: external resources not versioned with the app
* Install Mode: What caching strategy to use when first seeing this file
* UpdateMode: What caching strategy to use when updating the file, after we’ve already installed it
* Caching strategy
* Prefetch: Save these files before we even ask for it
* Lazy: Save these files only after they’ve been requested at least once
* You can check out the [official angular documentation on servicer worker configuration](https://angular.io/guide/service-worker-config) for more details

#### Manifest.json

```
{"name": "Atila","short_name": "Atila","start_url": "index.html","display": "standalone","icons": [{"src": "assets/img/favicon-bg.png","sizes": "512x512","type": "image/png"}],"background_color": "#194f87","theme_color": "#194f87"}
```

This is what turns your app from a web app to a progressive web app. It allows your web app to be similar to a native mobile. It allows users to install your app to their home screen.

![Image](https://cdn-media-1.freecodecamp.org/images/0*P5myb3EsJHS_bugZ)

#### Register the Service Worker ([#d2b186f](https://github.com/atilatech/atila-web-app/commit/d2b186f1ecc3a0862fcb3bd863643f1d28eac970))

Now we need to actually tell our app that a service worker exists. So we register the service worker module in our app module.

```
// src/app.module.ts
```

```
import {ServiceWorkerModule} from '@angular/service-worker';
```

```
…
```

```
Imports: [
```

```
…,
```

```
ServiceWorkerModule.register('/ngsw-worker.js', {enabled: environment.production}),]
```

Then we register the service worker file if our [browser has service worker support](https://jakearchibald.github.io/isserviceworkerready/) and we are are in production mode.

```
// src/main.ts
```

```
if ('serviceWorker'  in  navigator  && environment.production) {
```

```
console.log("Service Worker in main.ts");
```

```
window.addEventListener('load', () =>; {
```

```
console.log("on page Load Service Worker in main.ts");
```

```
navigator.serviceWorker.register('/ngsw-worker.js', {
```

```
scope: '/',
```

```
})
```

```
.then(registration  =>; {
```

```
console.log("Service Worker registration completed main.ts", registration);
```

```
});
```

```
});
```

### Part 1a: Build The Service Worker

#### Service Worker Output

Next, we will build the project: `ng build --prod`

Let’s take a look at the dist/ folder to see what building an app with service worker looks like.

![Image](https://cdn-media-1.freecodecamp.org/images/0*yK-cyZH5cBDp3spd)

#### Service Worker Output: ngsw.json

Recall that in the previous step we created a file called ngsw-config.json. This file specifies what types of files we wanted our service worker to cache and how we wanted to cache it. When the project gets built, the rules in the ngsw-config.json gets expanded to include exactly what files we will be caching. The ngsw.json file also includes a hash table to index and retrieve the cached files. The hash table also allows us to version our files. We can keep track of what versions of our file is running and if we should get a new version.

![Image](https://cdn-media-1.freecodecamp.org/images/0*gtRBo57N9515LdBC)

![Image](https://cdn-media-1.freecodecamp.org/images/0*xrGnG1j9q-B1ONGy)

#### Service Worker Output: ngsw-worker.js

This file is literally the service worker. We registered it earlier in our main.ts file. It is a plain javascript file. It contains the code and logic for how your service worker registers and caches data to a database. If you’re up for a challenge, try looking through the code and see if you can understand what is happening.

![Image](https://cdn-media-1.freecodecamp.org/images/0*x_osOIZlwST--8Ui)

### Part 1b: Testing The Service Worker ([#2001441](https://github.com/atilatech/atila-web-app/commit/2001441a948f8fc0768c43634020cd927763f812))

#### Creating A Mini Server

* Service workers are used in an offline context. We need a server that can simulate offline environments
* Install [npm http server](https://www.npmjs.com/package/http-server)
* `Npm install http-server@0.11.1 --save-dev`
* Build and Run the server:
* `ng build --prod` (optional)
* `http-server -p 8080 -c-1 dist`

#### Inspecting the Server Requests

* Visit Chrome Network tab in devtools
* Do this before going to localhost!
* Open a new tab
* Right-click somewhere blank on the screen
* Inspect > go to Network Tab
* Open [http://localhost:8080/](http://localhost:8080/)

![Image](https://cdn-media-1.freecodecamp.org/images/0*Oy6aUcTa2mJF4Iil)

Note that there is no wi-fi in the top right. Check the devtools console: The external network resources fail with 504 but our files are successful (200).

#### Where are the Files Being Saved?

Open the application tab in Devtools and you will see the local cache section. This is the “database” where the service workers are saving your files. That there are 2 tables. One which contains the actual resources our app needs. Another hash table with hash keys that point to each file name, as we saw in our ngsw.json file. That’s it! You now have a simple but functional offline first web app. Continue to part 2 for adding more cool features.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OLvJkfQzjwyk5bef)

### Part 2: Saving External Data (Part 1 Git Tag: [pwa-tutorial-0.1](https://github.com/atilatech/atila-web-app/releases/tag/pwa-tutorial-0.1) )

#### Why are None of my APIs Working?

When you try to navigate click on a link, you will notice a server error. Your service worker doesn’t have those APIs in your database, but we can add it. Pop Quiz! If we want to tell our service worker to cache a new type of file where should we put the code to do so:

1. Manifest.json
2. Ngsw-config.json
3. App.module.ts

![Image](https://cdn-media-1.freecodecamp.org/images/0*USs5NfuSBP-nCOjF)

You can see the network requests failing in your dev tools network tab.

#### Saving External API calls: Configuration ([Github Diff](https://github.com/atilatech/atila-web-app/commit/fe3f6aa30a01766d8d487711afd9aded4a0a3f13#diff-4553821adec55b6f464162aab4323c7a))

Now we will configure our ngsw-config.json to cache external API URLs as well. Two caching options:

1. Freshness: Go to the network first, if missing, go to the
2. Performance: Go the cache first, then go to network

#### Saving External API calls: [#8593ada](https://github.com/atilatech/atila-web-app/commit/8f93ada504dd5b0dc210a64a73caee5ffd14927d)

You might need to use a separate URL that allows your app to access it via CORS. We will use a special JSON service to simulate (“mock”) our blog API. We don’t have permission to use official Atila API’s

* Change ScholarshipService.getPaginatedScholarships:
* Go to `src/app/_service/scholarship.service.ts#L47`
* Change: `this.http.post(${this.scholarshipsPreviewUrl}?page=${page}/, form_data)` to: this.http.get(`https://api.myjson.com/bins/dx1dc`)
* Change BlogPostService.getBySlug:
* Go to src/app/_service/blog-post.service.ts#L25
* Change: this.http.get(`${this.blogUrl}blog/${username}/${slug}/`) to: this.http.get(`https://api.myjson.com/bins/v5ow0`)

### Part 3: Notify Users of New Updates (Part 2 Git Tag: [pwa-tutorial-0.2](https://github.com/atilatech/atila-web-app/releases/tag/pwa-tutorial-0.2)))

When a new version is available from the network, the service worker still serves the old version in the cache to save time

* Add your profile to the team page: src/app/team/team.component.ts
* Add your image and some information in the team data array
* If you rebuild the project and restart the server, you’ll notice that your profile doesn’t appear yet.
* We can add a snackbar to notify the user of new updates
* npm install @angular/material@5.1.1 — save (you might already have this)
* Then we create swUpdate to listen for updates from the SW and update if a new version is available.[Github Diff](https://github.com/atilatech/atila-web-app/commit/1c89769)

```
// src/app/app.component.ts    import {SwUpdate} from  "@angular/service-worker";...    Constructor (..., public swUpdate SWUpdate,)...ngOnInit() {
```

```
if (true) {
```

```
// check service worker to see if new version of app is available
```

```
if (this.swUpdate.isEnabled) {
```

```
this.swUpdate.available.subscribe(() =>; {
```

```
const snackBarRef = this.snackBar.open('New version available', 'Load New Version');snackBarRef.onAction().subscribe(
```

```
() =>; {
```

```
location.reload();});			});		}	}}
```

Rebuild and reserve your application

### Part 4: Deployment (Part 3 Git Tag: [pwa-tutorial-0.3](https://github.com/atilatech/atila-web-app/releases/tag/pwa-tutorial-0.3))

#### Deploying to Firebase Hosting

To see the effect of service worker, we should deploy it to a real website. I like Firebase Hosting. You can take a web app from your localhost to a live website in less than 5 minutes with a few simple steps. I’ve been doing this for almost 2 years now and I still get impressed with how easy the process is. Lately, I have also been playing around with [AWS S3 Static website hosting.](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) This is another good alternative you can look into:

#### Deployment Prerequisites:

1. [Create a google account](https://accounts.google.com/SignUp?hl=en)
2. [Create A firebase account](https://firebase.google.com/) and a firebase project
3. install firebase tools globally: `npm install -g firebase-tools@4.2.0`
4. Log in to firebase: `firebase login`
5. Initialize Firebase Repo: `firebase init`
6. Choose the following settings:
7. Choose hosting as the project type
8. Change public folder to dist/
9. Configure as a single page app
10. Overwrite idnex.html? NO
11. Deploy! `Firebase deploy`
12. Visit the URL in the command line output to see your app

That’s it! Congratulations you now have a website that can work without the internet.

### Conclusion

#### Who Needs Mobile Apps

I’ve [written](https://atila.ca/blog/tomiwa/why-we-chose-angular-over-react-and-django-over-ruby-on-rails-for-atila-the-essential-software-startup-techstack) [previously](https://atila.ca/blog/tomiwa/phlock-my-hardware-startup-that-disappeared) about why I strongly believe that startups and companies should design their technology products as progressive web apps instead of mobile apps. My core arguments being:

1. Having to maintain 2 separate Android and IOS codebases is a pain: 2 sets of users, 2 sets of developers, 2 sets of problems. (Things like [Flutter](https://flutter.io/) and [Ionic](https://ionicframework.com/) are cool but I don’t believe they address the fundamental issue of 2 separate codebases.)
2. Most people only use the same 5 apps a day, so convincing them to download another app will be very difficult.
3. Approval and Distribution through the Apple App Store and Google Play Store gatekeepers are not fun.

Some of the core arguments against web apps include things like:

1. Offline accessibility
2. Better user engagement because of push notifications
3. Access to Native hardware features like cameras

With features like service workers, I have just shown how we can enable websites to work offline. [Progressive web apps also enable push notifications](https://developers.google.com/web/fundamentals/codelabs/push-notifications/).

Native hardware features are still the one advantage which mobile apps have, though this [is changing](https://developers.google.com/web/fundamentals/media/capturing-images/). Unless it’s mission critical for your app to have these native features, I strongly encourage startups and companies to consider looking into making their next app a progressive web app.

I think that the future of the internet will see more applications distributed through browsers and URLs than native apps and the app store. In an ironic case of history repeating itself, this is actually a throwback to the advent of the internet in the 90s when companies like Netscape and various “.com startups” were doing very well distributing their software through the web.

#### The Future of Websites

Wouldn’t it be awesome if other sites applied that same philosophy? Imagine if you’re like me and you have an hour plus commute to work every day. Forget about wifi, they don’t even have cellular service on the subway.

Now suppose I want to buy Bluetooth headphones and I want to read some Amazon reviews before I make my decision. Wouldn’t it be awesome if I could cache the product details for the items in my shopping cart and read the reviews on my way to work? Then by the time I get to work, I can just buy the item I want.

Or imagine you’re on the plane for a quick flight from Toronto to Ottawa. You load up the NY Times to catch up on morning news but the site gives the famous “Google dinosaur”. In an ideal world, the NY Times should cache the top 5 most popular articles. This allows users to read the articles and leave comments offline. The comments can be synced when they connect back to the internet.

Google Docs does this best. Google Docs is Microsoft Word, Powerpoint and Excel but better and built for Chrome. You don’t need the internet to use Microsoft Word. Because Google Docs runs in a web browser, you should be able to use Google Docs to access and edit your recent items. Which is exactly what Google Docs does well.

I feel slightly proud of the fact that the great Amazon and NY Times websites need the internet to run. I am humble that little [Atila.ca](http://atila.ca/) runs just fine with and without internet. ;) When the internet is down, you can still see featured scholarships, blog posts and other pieces of content.

Okay, these are mostly #FirstWorldProblems. But another thing that gets me really excited about this technology, is building the internet for the next billion users. For people who have very slow or inconsistent internet connection.

For example, [HospitalRun](http://hospitalrun.io/) is an offline first application. It manages hospitals in the developing world. These are places where intermittent connectivity is a fact of life. It allows records to be carried to remote clinics, where there may be no internet. It then syncs those records when there is. (h/t [jonbellah.com](https://jonbellah.com/articles/offline-first/))

At Atila, one of our projects is increasing access to scholarships for students from developing countries. So it would be awesome if they could seamlessly read sample essays and work on their scholarship applications even if they lived in places with a poor internet connection.

I personally find the idea of service workers and offline-first web applications very fascinating. Simple technologies with the ability to fundamentally change the day to day habits of billions of people are why I chose to study software engineering and why I love this field. I’m really excited to not just see how the future of the internet will unfold but also help build the future of the internet and how we will interact it. The future is already here folks. Thanks for reading.

### Further Reading

* [Angular Official Service Worker Documentation](https://angular.io/guide/service-worker-intro)
* [Angular University: Angular Service Workers](https://blog.angular-university.io/angular-service-worker/)
* [Add Service Worker to Existing Angular App](https://medium.com/@cdeniz/transforming-an-existing-angular-application-into-a-progressive-web-app-d48869ba391f)
* [Angular Firebase — Deploying an Angular App to Firebase](https://angularfirebase.com/lessons/deploying-an-angular-app-to-firebase/)

