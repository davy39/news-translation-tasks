---
title: How to implement a simple title change application using Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-27T14:31:48.000Z'
originalURL: https://freecodecamp.org/news/implement-a-simple-title-change-website-using-vue-js-7492e049af7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zyNSb0UXhP8TfxYbj-GNWg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By Anoob Bava

  Vue.js is a progressive JavaScript framework. It has a lot of features including
  components, rendering, and routing. The Vue vs React argument is competitive in
  nature. They both have pros and cons in their field.

  I created a simple Jav...'
---

By Anoob Bava

Vue.js is a progressive JavaScript framework. It has a lot of features including components, rendering, and routing. The Vue vs React argument is competitive in nature. They both have pros and cons in their field.

I created a simple JavaScript application in Vue using a CDN (content delivery network). The application has a title which will convert to upper case on clicking a button. I know it is a simple application. But we can learn many simple things through it, like:

* CDN for Vue
* Vue objects
* linking an attribute to the Vue Object
* defining a data property
* defining a method using Vue
* calling the Vue method via listeners

Okay, let's get our hands dirty!

I am a big fan of diving the method to chunks, so we will follow the same approach here.

1. Create an HTML file and link Vue via CDN.
2. Create a Vue object.
3. Link HTML template to the Vue object.
4. Create a data property.
5. Create a method in the Vue object.
6. Change the data when clicking a button.

#### 1. Create an HTML file and link Vue via CDN

Initially create a file called **index.html.** It is our core player. The index.html file contains both the HTML template part and the Vue object.

I am using Visual Studio Code here.

![Image](https://cdn-media-1.freecodecamp.org/images/Vne3w5FAeTV7vb9-Vs4IKCNltCqYeirJ-LDP)

Now add the CDN to the index.html. We can use either the development or production version. But it will be good to use the development version for warning and errors. The entry for the development version of the CDN currently is:

```
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

#### 2. Create a Vue object

Now what we need to create is the Vue object inside the index.html file. It is created under the script tag <script></script>.

It can be created by:

```
new Vue();
```

The whole syntax is below:

```
<script>new Vue({el: ,
```

```
data: {
```

```
},
```

```
methods: {
```

```
}
```

```
});</script>
```

`new Vue` is an instance of Vue. We can access properties like el, data, methods etc to be with Vue. Properties will be explained below.

#### 3. Link the HTML template to the Vue object

As we know Vue has a property called the “el”. This property links the HTML template to the Vue object. In order to do that, all the HTML templates have to be under a single div with an id. For this demo, we can use an id of `app`. We have added the following to the index.html file:

```
<div id='app'>
```

```
<h3> Welcome to title changer</h3>
```

```
</div>
```

Now, add the app id to the Vue object.

```
new Vue({
```

```
el: '#app',
```

```
});
```

So the link will be a success.

#### 4. Create a data property

Now we do not want the header “Welcome to title changer” to be static text. We need to be able to display the value from the Vue data property. To do that, Vue has a built-in property called “data.” We need to register that here and use the name in the HTML like below:

```
new Vue({
```

```
el: '#app',
```

```
data: {
```

```
tile: 'Welcome to title changer'
```

```
},
```

```
});
```

Now in the `<`h3> tag can be updated with the double curly braces like interpolation in Ruby. The value will be:

```
{{title}}
```

![Image](https://cdn-media-1.freecodecamp.org/images/SG2hAWsjA7L39a56BTzsmt6c7NM7vCowW-i9)

#### 5. Create a method in Vue object

Vue has a built-in property called the “methods”. This property will support the methods to be declared inside the Vue objects.

We can use ES6 syntax also. Let me explain them both here.

```
methods: {
```

```
  changeTitle: function() {
```

```
      this.title = this.title.toUpperCase();
```

```
      return this.title;
```

```
   }
```

```
}
```

The ES6 format is:

```
methods: {
```

```
    changeTitle() {
```

```
        this.title = this.title.toUpperCase();
```

```
        return this.title;
```

```
    }
```

```
}
```

`toUpperCase()` is simply a JavaScript method which will convert a string to capital letters. An important point to be noted here is, we can access the data property using the `this` keyword. So the value which is declared in the data property can be accessed using `this` in the methods.

#### 6. Change the data when clicking a button

Now, what we do is simply call the method on clicking a button. Simple as that.

To do that, we need to create a button tag.

```
<button>click to change to upcase</button>
```

To link the button to the method, we need to use an event handler when clicking the button. Vue provides a built-in listener called `**v-on**`**.**

Here is the syntax:

```
v-on:click="call Action or Method"
```

We can combine with:

```
<button v-on:click="changeTitle">click to change to upcase</button>
```

Or **we can use a short-hand syntax like below:**

```
<button @click="changeTitle">click to change to upcase</button>
```

That’s it. All done

Before clicking the button, the HTML heading is below:

![Image](https://cdn-media-1.freecodecamp.org/images/wrxsJfTfPdMx7khAWwAdvtJHj98kOvXbnGv6)

After clicking, it is converted to upper case.

![Image](https://cdn-media-1.freecodecamp.org/images/l7mtoWPLJJdMNRTxP9yBGwJVTp7zBFJQeTfA)

That’s all. Comment if you have any issues or questions. I have attached the Repo details below.

[github link](https://github.com/anoobbava/title_changer). I will update with some advanced features in Vue in the coming lessons.

