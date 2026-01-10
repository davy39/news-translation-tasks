---
title: 'Learn Vue: a 3-minute interactive Vue JS tutorial'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-19T01:41:12.000Z'
originalURL: https://freecodecamp.org/news/learn-basic-vue-js-crash-course-guide-vue-tutorial-e3da361c635
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S9ztlTg2A3gvRxPfUg3jTQ.png
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  Vue.js is a JavaScript library for building user interfaces. Last year, it started
  to become quite popular among web developers. It’s lightweight, relatively easy
  to learn, and powerful.

  In the three minutes that Medium says it w...'
---

By Per Harald Borgen

Vue.js is a JavaScript library for building user interfaces. Last year, it started to become quite popular among web developers. It’s lightweight, relatively easy to learn, and powerful.

In the three minutes that Medium says it will take you to read this article, you’ll be equipped to start building basic Vue apps. With each segment, I’ve also included an interactive [Scrimba](https://scrimba.com/p/pXKqta?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_in_3_minutes) screencast, where you can watch me explain the concepts and play around with the code yourself.

Let’s jump into it.

### Template syntax and data

At the core of Vue.js is a straightforward template syntax which looks like this:

```vue
<div id="myApp">  
    {{ message }}  
</div>

```

Pair that with the following JavaScript snippet:

```js
var myApp = new Vue({  
   el: '#myApp',  
   data: {  
       message: 'Hello world!'  
   }  
})

```

And it’ll result in _Hello world!_ being rendered on the page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8H9M0L0bYLUo8j0GqbwFFA.png)

The `el: #myApp` part tells Vue to render the app inside the DOM element with the id of _myApp._ The `data` object is where you place you the data you want to use in your app. We’ve added only one key here, `message`, which we’re referencing to in our HTML like this: `{{ message }}`.

Vue takes care of linking the `data` object to the DOM, so if the data changes, the page will be updated as well.

This is called declarative rendering. You simply specify _what_ you want to update, and Vue takes care of _how_ to do it.

You can change the data can by doing this:

```js
myApp.message = 'Some new value';

```

Here is a screencast which explains this exact concept:

### Directives

The next concept you’ll need to learn is directives. Directives are HTML attributes that are prefixed with `v-`, which indicates that they apply reactive behavior to the rendered DOM.

Let’s say we only want to render something if a condition is true, and hide it if it’s false. Then we’ll use `v-if`.

In the HTML, it looks like this.

```vue
<div id="app">  
    <p v-if="seen">Now you see me</p>  
</div>

```

And some JavaScript:

```js
var app = new Vue({  
    el: '#app',  
    data: {  
        seen: true  
    }  
})

```

This will result in rendering out the _Now you see me_ paragraph if `seen` in `data` is **true.** To hide the paragraph, you can set `seen` to **false,** like this:

`app.seen = false;`

Here is a screencast explaining the same concept:

There are many other directives, like `v-for`, `v-on,` `v-bind` and `v-model`.

### Handling user input

Another core directive you need to learn is `v-on`. It will hook up an event listener to the DOM element, so that you can handle user input. You specify the type of event after the colon. So `v-on:click` will listen for clicks.

```vue
<div id="app">  
    <button v-on:click="myClickHandler">Click me!</button>  
</div>

```

`myClickHandler` refers to the key with the same name in the `methods` object. Needless to say, that’s the object where you place your app’s methods. You can have as many methods as you want.

```js
var app = new Vue({  
    el: '#app',  
    methods: {  
        myClickHandler: function () {  
            console.log('button clicked!');  
        }  
    }  
})

```

This will result in _button clicked_ being logged to the console when clicking the button.

Here is a screencast explaining the concept:

### Tying it all together

Now let’s create an example where we’re using both `data` and `methods`, tying together what we’ve learned up until now.

```vue
<div id="app">  
    <p>{{ message }}</p>  
    <button v-on:click="changeMessage">Click me!</button>  
</div>

```

And the JavaScript:

```js
var app = new Vue({  
    el: '#app',  
    data: {  
        message: 'Start message'  
    },  
    methods: {  
        changeMessage: function () {  
            this.message = 'The message has changed!'  
        }  
    }  
})

```

Initially, it’ll display out _Start message_ on the page, however after the click it’ll display _This message has changed_ instead.

The `this`  keyword refers to the Vue instance, the one we’ve called `app`. It is on this instance that our data lives, so we can refer to the `message` data through `this.message`.

[Check out this screencast explaining the concept.](https://scrimba.com/p/playlist-38/cast-1933?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_in_3_minutes)

And by that, you should know enough Vue.js to get started creating simple apps.

In the next tutorial, you’ll learn how to create Vue components. So be sure to follow this publication if you liked this article.

