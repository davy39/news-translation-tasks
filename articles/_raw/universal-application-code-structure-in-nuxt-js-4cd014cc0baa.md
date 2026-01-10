---
title: Universal application code structure in Nuxt.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-15T02:50:30.000Z'
originalURL: https://freecodecamp.org/news/universal-application-code-structure-in-nuxt-js-4cd014cc0baa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lwIEF0F3eDlMKR1hKZic7Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: vue
  slug: vue
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By Krutie Patel

  A brief summary of source code structure in Nuxt.js

  Are you new to the Nuxt.js framework and totally overwhelmed by the number of folders
  it comes with? Are you also surprised that most of them are empty with just the
  readme file in t...'
---

By Krutie Patel

#### A brief summary of source code structure in Nuxt.js

Are you new to the Nuxt.js framework and totally overwhelmed by the number of folders it comes with? Are you also surprised that most of them are empty with just the readme file in them? Well, that’s where I was little over a year ago. Since then, I’ve always wanted to learn and document the magic that each folder brought into the Nuxt project.

And now, after implementing a few projects with this framework, I have documented my understanding of how these folders work together to bring the server-rendered Vue application to life.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lwIEF0F3eDlMKR1hKZic7Q.jpeg)

The diagram above is based on [Vue SSR guide](https://ssr.vuejs.org/guide/structure.html#introducing-a-build-step), and extended with Nuxt.js in mind. At a glance, you see different folders in _Your universal application code_ section, and how the code is then, packaged by Nuxt and bundled by Webpack.

This article is neither tutorial nor complete guide to Nuxt SSR. It rather shows what goes into universal application.

Although you see modules, serverMiddleware, and plugins at the top of the diagram, let’s start with _Store_ first.

### Vuex Store (/store)

Nuxt comes pre-packaged with Vuex, but it’s not activated unless you make a Vuex store in the _/store_ directory and create the store.

This is very special directory for any data-driven project. This is where you can create a data-store, as well as define the _nuxtServerInit_ action. This happens to be the very first lifecycle hook as well!

```
const createStore = () => {  return new Vuex.Store({     ...  })}
```

When the user initially accesses your application, this helps fill/update the store. It also maintains the state of your data throughout the application.

### Route Middleware (/middleware)

There are three different kinds of route middleware available in Nuxt. They are all defined in one central location — in the _/middleware_ directory.

From here, you can use them in the following ways:

* Global middleware — (entry via Nuxt config and affects all routes)

```
// nuxt.config.js 
```

```
export default {  router: {    middleware: 'authenticated'  },}
```

* Layout middleware (entry via layouts and affects group of matching routes, i.e. certain pages only to be viewed/accessed by authenticated users)

```
// layouts/default.vue
```

```
export default {  middleware: 'authenticated-basic-plan-user'}
```

* Page middleware (entry via page component and affects single route)

```
// pages/index.vue
```

```
export default {   middleware: 'subscribed'}
```

The middleware above are dealt in this exact order — meaning, their priorities are non-negotiable. So you must think through and plan your application carefully to get the most use out of them.

### Vue Components

There are three directories where _.vue_ files are created in a Nuxt project.

#### **1. Page components ? (/pages)**

This is the most important directory of all that houses application views and routes. Vue.js components created here are directly converted into application routes.

The real power of page components lies in dynamic routes. You can use them to generate SEO friendly and data-oriented URLs. Dynamic routes are generated based on your directory structure under _/pages._

In addition, Nuxt adds three special methods on page components which aren’t available anywhere else. They are _validate()_, _asyncData()_ & _fetch()_.

```
// pages/index.vue 
```

```
export default {
```

```
  validate() {     // validates dynamic URL parameters     // verifies the availability of the data  },   asyncData() {     // sets component data  },
```

```
  fetch() {    // doesn't set component data, but     // fetches further contextual data  }
```

```
}
```

#### **2. Layout components (/layouts)**

Layout components power the structural aspects of your application. Common components found on all pages are created here (like main menu, secondary menu, header, footer, etc.). They’re located in the _/layouts_ directory.

You can be as creative as you want here, after all they are Vue.js components. Don’t forget to add _<nux_t/> in the main content area of the layout.

```
<template>  &lt;div>     <nuxt/>  </div></template>
```

Incorporate _route-middleware_ and _store data-state_ with the layout component to build perfect _who-sees-what_ features for any number of user-types with varied scenarios. You can achieve a bit more than just with a custom user interface.

#### **3. Vue.js components (/components)**

These are regular, but versatile Vue components. They are created under the _/components_ directory. They are not supercharged with special methods like Page components.

But they allow you to structure and organize your business logic. They also hide heavy markup from **page** and **layout** components. This makes your codebase more manageable.

Now look closely — can you see the partial folder structure in this Nuxt lifecycle diagram?  
**Hint:** Store (nuxtServerInit), Route Middleware and Page components (validate, asyncData & fetch methods)

### Assets

#### **Webpacked assets (/assets)**

Assets such as JavaScript files, custom fonts, and CSS files are processed by Webpack using specific loaders (css-loader, file-loader, url-loader etc) depending upon file types. For example, if you write your CSS in _.scss_ or _.less_ format then Webpack will process these files using a specific loader and output compiled _.css_ file that can be used by the browser.

You can even customize your _nuxt.config.js_ to instruct Webpack to minify and optimize images in the assets folder as a part of your build process. After Webpack processes the files, it attaches hash-code — _for example, index.4258e3668a44556dd767.js_ — to the processed items which helps in long-term caching of dynamic assets and cache-busting.

#### **Static assets (/static)**

For the assets that will not change, you can safely put them in the _static_ folder. Webpack ignores the static folder and will not process anything in there.

### Modules, serverMiddleware and plugins

They are all defined (by their path) in Nuxt configuration. They are accessible globally within the Nuxt application.

#### **Modules (/modules)**

A fresh Nuxt application is pre-packaged with Vue, Vue Router, Vuex, Vue Server Rendered and Vue Meta by default.

But you may wonder, what about features like Sitemap, Google Analytics, Progressive Web Apps, or more? If you’re thinking of using modules, then yes, you are right, this is where the power of Nuxt modules come into play.

#### **serverMiddleware (i.e. /api)**

serverMiddleware can be considered an extension point for your application. They are special because they have access to the underlying instance of the connect framework.

Since Nuxt uses **connect** to deliver the application, it allows custom functions to be hooked into the underlying request pipeline as middleware.

You can use serverMiddleware to:

* Create an API endpoint to connect to external applications.
* Create an API endpoint to send email to users from your Nuxt application.
* Access and modify the request in any way, even before it reaches Nuxt.

Note that you don’t have any pre-populated empty folders for serverMiddleware and modules. You create them when needed.

#### **Plugins (/plugins)**

You can make your existing Vue mixins, filters, or directives work harder just by converting them into Nuxt plugins. You place them in the _/plugins_ directory that comes with a fresh Nuxt installation.

But most of the time, you will end up adding external packages or Vue libraries as Nuxt plugins. You incorporate them in Nuxt by simply using _Vue.use()_ syntax. Some of the staple plugins I always end up using in my Nuxt implementation are Vue Bootstrap, form validation, font-awesome icon-set and axios.

That’s not the end of plugins. You can write custom plugins and add them in the application root. They are available globally in your Nuxt application. This is my personal favorite way of adding custom GreenSock or Scroll-Magic transitions into the project, and using them in the Vue _(/components)_ and Page _(/pages)_ components.

#### High-level overview of modules, serverMiddleware and plugins

### Package, bundle and deliver

Once you have the desired features in place, you build your application using _npm run build._ Nuxt packages your application.

As shown in the diagram below, _index.js_ is the main entry point, which imports _app.js_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5K1HLp5zxlKfwlM7X2BdZw.jpeg)
_Nuxt packages your code — Webpack bundles and delivers your code_

_App.js_ defines the root Vue instance. If you look closely in _.nuxt/App.js_, it’s nothing but a Vue component.

Once this root Vue instance is defined, client entry (_client.js_) creates a new instance based on it and mounts it to the DOM element. End-users see a fresh instance of an app in their browsers. While server entry (_server.js_) creates a new app instance for each request.

And finally, Webpack bundles your app so that the code runs on both the client and server side. The server bundle renders the server side, and the client bundle hydrates static HTML markup in the browser. It turns it into a dynamic DOM that can react to client-side data changes.

Nuxt does this all out of the box for us, so you don’t have to write this setup manually. Lots of complexity goes into the last two steps — packaging and bundling. But Nuxt hides all of it from you. You can concentrate on the application code that eventually delivers the final application.

### Conclusion

I hope this higher level overview of the application code structure takes you one step further in your learning journey of the Nuxt framework.

This is one of many alternate perspectives to help you make sense of how everything fits together in a Nuxt application.

For me personally, this little exercise helps me:

* map out the requirements of the project against out-of-the-box Nuxt features
* list relevant community modules & plugins that are already available, and
* pick out the remaining/complex bits that require custom development.

#### **Diagrams links with high-res versions of the diagrams used above**

1. [Nuxt Js lifecycle hooks](http://bit.ly/2xv6PDV)
2. [Understanding modules, serverMiddleware and plugins](http://bit.ly/2sHNieo)
3. [Universal application code in Nuxt.js](http://bit.ly/2MFl23s)

Feel free to reach out with comments, feedback or even a suggestion for new diagram ideas you would like to see — in the comment section below.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IslxntaSDwDHfcKEieqDng.jpeg)
_[https://www.pariksha.io/](https://www.pariksha.io/" rel="noopener" target="_blank" title=")_

If you’re new to Nuxt, then you may want to check out my earlier article on this topic “[Why Nuxt Js is the perfect framework for your landing page?](https://codeburst.io/why-nuxt-js-is-perfect-framework-for-your-landing-page-53e214649b88) That will give you deeper insight in the nitty-gritty of developing applications with Nuxt.

### Are you Nuxt yet?

![Image](https://cdn-media-1.freecodecamp.org/images/1*xV6a7Pxle-OrI10wcbCCeQ.jpeg)

When [@_achopin](https://twitter.com/_achopin) asked at the [@vuejsamsterdam](https://twitter.com/vuejsamsterdam), “Are you Nuxt?” I thought, hey… I am Nuxt.

And I created these [Nuxt stickers](https://www.etsy.com/au/shop/CrewShopDesigns) — professionally printed by Moo Printing and ready to be shipped if you’re interested. Alternatively, you can order them on [RedBubble](https://www.redbubble.com/people/krutie?asc=u) as well.

