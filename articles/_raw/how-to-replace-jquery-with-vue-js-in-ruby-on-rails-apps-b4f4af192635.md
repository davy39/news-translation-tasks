---
title: How to replace jQuery with Vue.js in Ruby on Rails apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T19:21:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-replace-jquery-with-vue-js-in-ruby-on-rails-apps-b4f4af192635
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VIrASrMWiySHstjaQwF4GA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Igor Petrov

  If you are a Ruby on Rails developer and have been for several years, you’re probably
  used to using jQuery as the default option for developing the front end. Several
  versions ago, core Rails developers offered it as a standard, and in...'
---

By Igor Petrov

If you are a **Ruby on Rails** developer and have been for several years, you’re probably used to using **jQuery** as the default option for developing the front end. Several versions ago, core **Rails** developers offered it as a standard, and in time it became the standard. **jQuery** was the #1 **JavaScript** library, and it was very convenient to use it.

Since then, quite a bit of time has passed, but **jQuery** is still the default option. Now, however, you need something different because of the growing complexity of client-side code. You might try React, Angular.js, or Vue.js, but you can only use one of these easily while making the smallest effort to integrate it into an existing or new app.

I used **jQuery** for a long time and it became a habit: if you start a new **Rails** app, **jQuery** is already there. You’re already familiar with it, and so you start to use it immediately.

Several years ago, I discovered that I liked **Angular 1,** because it was very simple to start with. But it still had redundant setup with app initializing, writing controllers, and injecting dependencies.

This is great for architecting your app in with an MVC (MVVM) approach.

But let’s say you have an existing app with a lot of **jQuery** DOM manipulation code, and you want to start replacing this mess with something more supportable. Something like the following (which could be optimized, of course — but this is for the sake of example):

```
$(document).ready(function(){
```

```
   ...   $('#some-radio-button1').on('click', function(){     if ($(this).is(':checked')) {       // removing "active" classes, hiding some blocks       // showing related block
```

```
     } else {
```

```
       // opposite of above     }   });
```

```
});
```

### Why Vue.js?

So why do I recommend replacing **jQuery** code with **Vue.js**? Because **Vue.js** is not just useful for writing complex **JavaScript** apps. You can also use it just for one simple task, like DOM manipulation. If this is all you need, it would be a good idea to go with **Vue**. And you can go further with it if you need to solve more complex tasks like routing, state management, and so on.

So, if you already have a project with a lot of **jQuery** code and you would like to get rid of those messy event handlers, you should definitely give **Vue.js** a try.

#### Getting started

If you are an old-school RoR developer and still manage assets via **Sprockets**, then just download and put `vue.js` to your `vendor/assets/javascripts` folder.

Next, require it from your main **JavaScript** manifest file (for example, `application.js` ):

```
//= require jquery//= require jquery_ujs//= require bootstrap//= require vue
```

Then you need to instantiate a **Vue** instance and attach it to some element in your **HTML** code. For this purpose, you could create a separate `vue_app.js` (or .coffee) file inside `app/assets/javascripts`:

```
window.vueApp = new Vue  el: '.off-canvas-container'  data:    ...
```

That’s it, now you can use **Vue.js**!

### Going further

Now you can add data to your **Vue** instance `data` section and write some handlers in the `methods` section. But it’s better to use a core **Vue.js** unit: components.

The easiest way to continue with **Vue.js** is to use your existing **Rails** views and wrap some pieces of **HTML** into components. Let’s take a look how to achieve this.

For example, I have `app/views/sellers/print_labels/new.html.erb` and some **jQuery** code associated with this page:

![Image](https://cdn-media-1.freecodecamp.org/images/oby6k46mOkZzmsrhymr5Z3AMPwop2tCmKNiW)

![Image](https://cdn-media-1.freecodecamp.org/images/YDQsGEOpcQdAEpWCJQaJVPWKjkzUQbbwKCFx)

This is a shipping address form with inputs disabled by default. Once the user clicks the “pencil” icon, form fields will turn into accessible inputs and the “Save” button will be shown. Once “Save” is clicked, the form gets returned to its original state.

To replace this **jQuery** code with a simple **Vue.js** components, I’m creating `app/assets/javascripts/components/print_labels.coffee` with something like the following (but don’t forget to require your `components` folder from `application.js`):

```
Vue.component 'print-labels',  data: ->    isEditingAddress: false
```

And then I use it in my **Rails** view:

![Image](https://cdn-media-1.freecodecamp.org/images/83yq--rKhJDGBRFhsqy8LHTbZ3G2FRrG3Zcp)

Several things to notice:

* If you want to keep the component template inside Rails views or partials, you should use the `inline-template` option.
* `v-cloak` option is needed to display the component after it has been initialized and rendered
* We use `@click` for attaching `onclick` event handlers (you can extract complex code to the component `methods`)

Now we can get rid of the **jQuery** code because we’ve replaced it with a small **Vue.js** component (with just one data variable!).

Now it’s your turn! Go ahead with this approach, and I hope you’ll find yourself happy with **Vue.js** soon.

_If you liked this post, please click on_ ✋ _to spread the word._

