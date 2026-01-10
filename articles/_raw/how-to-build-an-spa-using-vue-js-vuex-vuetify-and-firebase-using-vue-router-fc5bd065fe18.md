---
title: 'How to build an SPA using Vue.js, Vuex, Vuetify, and Firebase: using Vue Router'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-24T17:28:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-spa-using-vue-js-vuex-vuetify-and-firebase-using-vue-router-fc5bd065fe18
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_oxBC3QDl02cB2MDOzGXZg.png
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: vue
  slug: vue
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By Jennifer Bland

  Part 2: learn how to use Vue Router with your SPA


  Meal Prep application

  Learn how to create a meal delivery website using Vue.js, Vuex, Vue Router, and
  Firebase.

  This is part two of my four-part series on building a Vue application...'
---

By Jennifer Bland

#### Part 2: learn how to use Vue Router with your SPA

![Image](https://cdn-media-1.freecodecamp.org/images/E1pvqQ1jnZas610gycuziZk7Tu8KaK6uygz8)
_Meal Prep application_

Learn how to create a meal delivery website using Vue.js, Vuex, Vue Router, and Firebase.

This is part two of my four-part series on building a Vue application. Here is a list of all the parts:

[Part 1: Installing Vue and Building an SPA using Vuetify and Vue Router](https://medium.freecodecamp.org/how-to-build-a-single-page-application-using-vue-js-vuex-vuetify-and-firebase-838b40721a07)

[Part 2: Using Vue Router](https://medium.com/p/fc5bd065fe18)

[Part 3: Using Vuex and accessing API](https://medium.com/p/f8036aa464ad)

[Part 4: Using Firebase for Authentication](https://medium.com/p/d9932d1e4365)

### Recap

In the first part of this series, we created our Vue application using the Vue CLI. Also, we added Vuetify to the app. I am using Vuetify for styling the app. I will also take advantage of the many UI components that it offers.

After getting everything installed, we styled the home page of our application.

### Using Vue Router

Vue router provides the navigation for our application. When you click on the _SIGN IN_ button, it will redirect you to the page to login. When you click the _MENU_ button, it will redirect you to the page that shows the available meal plans.

The `router.js` file contains the configuration for routing. Open that file. In that file, you will see two routes. One that displays the Home.vue component when you hit `‘/’` route. The other displays the about.vue component when you hit the route ‘about’.

We will need to create routes for every page in our application. Our application will need the following routes:

* /
* /menu
* /sign-in
* /join

When we used the Vue CLI to create out the app, we selected to install Vue Router. By default, this created routes for ‘/’ which is home and ‘/about’ for the about page. In part 4 we will use the about page to show all the recipes the user has ordered.

We need to add three new routes to the routes array. After adding these new routes, this is what our `router.js` file looks like:

```
import Vue from 'vue';import Router from 'vue-router';import Home from './views/Home.vue';
```

```
Vue.use(Router);
```

```
export default new Router({    mode: 'history',    base: process.env.BASE_URL,    routes: [        {            path: '/',            name: 'home',            component: Home        },        {            path: '/about',            name: 'about',            component: () =&gt; import('./views/About.vue')        },        {            path: '/menu',            name: 'menu',            component: () => import('./views/Menu.vue')        },        {            path: '/sign-in',            name: 'signin',            component: () =&gt; import('./views/Signin.vue')        },        {            path: '/join',            name: 'join',            component: () => import('./views/Join.vue')        }    ]});
```

#### View vs Components

In our first lesson, we created several new Vue components. I placed these components inside the components folder. For these three new components, we will not create them inside the components folder. Instead, we will put them inside the views folder. The reason is that anything that is hit using a URL like `/menu` belongs in the views folder. Everything else should be in the components folder.

#### Creating new Views

We need to create new views for each of the three new routes. In the views folder create the following three files:

* Menu.vue
* Signin.vue
* Join.vue

Inside each of the files add a <v-container> with a <v-layout>. Inside the layout have an <h1> tag with the name of the page.

Here is the `Menu.vue` file:

```
<template>    <v-container fluid>        <v-layout>            <h1>Menu Page</h1>        </v-layout>    </v-container></template>
```

```
<script>export default {    name: 'Menu'};</script>
```

```
<style scoped></style>
```

Here is the `signin.vue` file:

```
<template>    <v-container fluid>        <v-layout>            <h1>Signin Page</h1>        </v-layout>    </v-container></template>
```

```
<script>export default {    name: 'Signin'};</script>
```

```
<style scoped></style>
```

Here is the `Join.vue` file:

```
<template>    <v-container fluid>        <v-layout>            <h1>Join Page</h1>        </v-layout>    </v-container></template>
```

```
<script>export default {    name: 'Join'};</script>
```

```
<style scoped></style>
```

#### Making the Menu Items Clickable

In our <v-toolbar> menu we have four items that a user can click. They are:

* Menu
* Profile
* Sign In
* Join

We want to configure each of these so that when a user clicks on them it will take them to the appropriate page. Open up the AppNavigation.vue file. In the <v-toolbar> section find the <v-btn> for the Menu. All we need t`o do is ad`d to="/menu". We will do this for all four entries, but make sure we specify the correct route that we def`ined in t`he router.js file.

We don’t have a menu option to return to the home page. We can fix this by making the app name redirect to the home page. But the title is not a button, so adding `to="/menu"` will not work. Vue Router provides the option to surround a link with `<router-link to=”`/”>. We will do this for our app title.

Here is what my AppNavigation looks like now:

```
<template>    <span>        <v-navigation-drawer app v-model="drawer" class="brown lighten-2" dark disable-resize-watcher>            <v-list>                <template v-for="(item, index) in items">                    <v-list-tile :key="index">                        <v-list-tile-content>                            {{item.title}}                        </v-list-tile-content>                    <;/v-list-tile>                    <v-divider :key="`divider-${index}`"></v-divider>                </template>            </v-list>        </v-navigation-drawer>        <v-toolbar app color="brown darken-4" dark>            <v-toolbar-side-icon class="hidden-md-and-up" @click="drawer = !drawer"></v-toolbar-side-icon>            <v-spacer class="hidden-md-and-up"></v-spacer>            <router-link to="/"&gt;                <v-toolbar-title to="/">{{appTitle}}</v-toolbar-title>;            </router-link>            <v-btn flat class="hidden-sm-and-down" to="/menu">Menu</v-btn>            <v-spacer class="hidden-sm-and-down"></v-spacer>            <v-btn flat class="hidden-sm-and-down" to="/sign-in">SIGN IN</v-btn>            <v-btn color="brown lighten-3" class="hidden-sm-and-down" to="/join">JOIN</v-btn>        </v-toolbar>    </span></template>
```

```
<script>export default {    name: 'AppNavigation',    data() {        return {            appTitle: 'Meal Prep',            drawer: false,            items: [                { title: 'Menu' },                { title: 'Profile' },                 { title: 'Sign In' },                { title: 'Join' }            ]        };    }};</script>
```

```
<style scoped></style>
```

When we do this, we have a slight problem with our app title in the menu. It has changed from being white text to being blue text with an underline. This is the default styling for an anchor tag. We can overcome this by adding the following style:

```
a {    color: white;    text-decoration: none;}
```

Now we are back to where we were. If you click on all the items on the menu, they will redirect you to the appropriate page. We only have a slight problem with the About.vue file. This file displays the contents differently. So that we have consistency, update the About.vue file to be this:

```
<template>    <v-container fluid>        <v-layout>            <h1>About Page</h1>        </v-layout>    </v-container></template>
```

```
<script>export default {    name: 'About'};</script>
```

```
<style scoped></style>
```

### Get the Code

Even though this is a 4-part series, you can get the [finished code in my GitHub account.](https://github.com/ratracegrad/meal-prep) Please help me out and **star the repo** when you get the code.

### Summary

In this part of this series, you have learned:

* how Vue Router works
* how to load new routes
* how to setup menu to load each page

### What’s Next

In the next part of this series, we will cover using Firebase for Authentication. Vuex allows you to provide “state” within your application. We will be signing up for access to a recipe API. From that API we will be getting recipes to display to users for our menu page.

If you enjoyed this article please clap for it. If you think somebody else would benefit from this article please share it with them.

If you have any questions or find anything wrong with the code, please leave a comment. If there are other topics you would like for me to write about, please leave a comment.

#### More Articles

Here are some other articles I have written that you might want to read.

[**Want a job in Tech? Here is how to use the top online marketplace for job seekers to get that job.**](https://medium.freecodecamp.org/want-a-job-in-tech-here-is-how-to-use-the-top-online-marketplace-for-job-seekers-to-get-that-job-878391456a2)  
[_LinkedIn is the world’s largest talent pool with 3 million active job listings. Let me show you how you can tap into…_medium.freecodecamp.org](https://medium.freecodecamp.org/want-a-job-in-tech-here-is-how-to-use-the-top-online-marketplace-for-job-seekers-to-get-that-job-878391456a2)[**Instantiation Patterns in JavaScript**](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)  
[_Instantiation patterns are ways to create something in JavaScript. JavaScript provides four different methods to create…_medium.com](https://medium.com/dailyjs/instantiation-patterns-in-javascript-8fdcf69e8f9b)[**Contributing to Open Source isn’t that hard: my journey to contributing to the Node.js project**](https://medium.freecodecamp.org/contributing-to-open-source-is-not-hard-here-is-my-journey-to-contributing-to-nodejs-d10760e31194)  
[_As a developer, you should consider contributing to open source software. Many of your potential employers will look…_medium.freecodecamp.org](https://medium.freecodecamp.org/contributing-to-open-source-is-not-hard-here-is-my-journey-to-contributing-to-nodejs-d10760e31194)

[**Follow Me On Twitter!**](https://twitter.com/ratracegrad)

