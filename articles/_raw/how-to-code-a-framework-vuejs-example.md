---
title: How to Code a Framework – the  First Lines of Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-25T21:38:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-a-framework-vuejs-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-hans-middendorp-9092855.jpg
tags:
- name: framework
  slug: framework
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By Fabio Pacific

  Have you ever wondered how frameworks are built? A couple of weeks ago I was writing
  an article and asked myself, what''s the first line of code Evan You wrote to build
  Vue.js?

  Well, thanks to Git and Evan You pushing Vue''s code to Gi...'
---

By Fabio Pacific

Have you ever wondered how frameworks are built? A couple of weeks ago I was writing an article and asked myself, what's the first line of code Evan You wrote to build Vue.js?

Well, thanks to Git and Evan You pushing Vue's code to GitHub, I have been able to travel back in time, like Marty McFly with his DeLorean time machine. But I went nine years back, to 2013, and "watched" Evan writing his code. 

![Delorean time machine](https://www.freecodecamp.org/news/content/images/2022/05/217316-Back_to_the_Future-DeLorean-time_travel-car-movies-smoke.jpg)
_Photo by wallup.net_

## What's the goal of this article?

I am writing this article to show you what's behind a popular tool like Vuejs and what could be the starting point for building something like it. Specifically, we'll look at what was Evan's You starting point.

We will learn from Vue's creator by looking at the source code of his oldest commits. We'll examine what he wrote to make the first implementation of a Vue application and how he wrote the logic in plain JavaScript to make the mustache syntax work.

### What is Mustache syntax? 
Well, if you are wondering what the hack is mustach syntax, let me explain. It is a basic form of data binding used by Vuejs to interpolate text inside a template. 

From the vue documentation:

> Vue.js uses an HTML-based template syntax that allows you to declaratively bind the rendered DOM to the underlying Vue instance’s data. The most basic form of data binding is text interpolation using the “Mustache” syntax (double curly braces):

`<span>Message: {{ msg }}</span>`

> The mustache tag will be replaced with the value of the msg property on the corresponding data object. It will also be updated whenever the data object’s msg property changes.

Ok, now that you know what that is, in the next section I'll answer your next question...

## What will I learn after reading this article?

Ok fair enough, you want to know why should you read this article and what will you learn from it.

If you are either a seasoned Vuejs developer or just at the beginning of your journey, you will learn how everything started for a popular tool like Vue. 

You will also learn how to hunt for a specific feature of a framework, browse old GitHub commits, and understand how you can apply plain JavaScript knowledge to start building the first features of one of the most popular frameworks of our time. 

In the next section we will start exploring the Vue.js repository. We will look at the fist and second commits to understand what files were created for the initial setup of the framework. 

This will help us find the feature that we are looking for (mustache syntax) and figure out also how the first Vue application was made.

## Exploring Vue's Oldest Commits

Alright, let's get started. If you want to follow me on this time traveling journey, hit this [link](https://github.com/vuejs/vue/commits/0.6.0?after=218557cdec830a629252f4a9e2643973dc1f1d2d+349&branch=0.6.0&qualified_name=refs%2Ftags%2F0.6.0). There, you'll find the Vuejs repository tagged 0.6.0. We are interested in its first and second commits.

I have downloaded a copy of the source code locally, precisely the source code of the second commit. Let's browse the code.

%[https://youtu.be/jDeze8rA7cA]

## The Folder Structure
The project structure in the second commit is fairly simple. Apart from a bunch of configuration files for jshing, grund, GitHub and the two JSON files, we can see three folders:

- test
- src
- explorations

The last one is an addition Evan made. The exploration folder wasn't there on the first commit. And it is in there that the actual creation of Vue.js started to take place.

We will come back here later in the article, but before that let's look at the fist commit to find Evan's fist lines of code. Spolier: everything starts with a test.


## The First Vue Test Case

The first lines of code are, I believe, those written in the test.js file. This is where Evan used the Mocha library to write Vue's first test case and set up the tests framework in the first commit named [initial setup](https://github.com/vuejs/vue/commits/0.6.0?after=218557cdec830a629252f4a9e2643973dc1f1d2d+349&branch=0.6.0&qualified_name=refs%2Ftags%2F0.6.0).

Why is this relevant? Well, we are not just hunting for a specific feature but we also want to understand what's the starting point for building a tool like Vuejs. 

Do you start by writing the implementation? Or do you write a basic test case just to set everything up so that you can write proper tests when you have an idea of what you want to implement? 

Well, below you have your answer!

Let's check the code of the test/test.js file:

```js
var Element = require('element')

describe('Element', function () {
    it('should have a variable', function () {
        assert.equal(Element, 123)
    })
})
```

On the first line, there is a `require` statement to import an element class that will be defined somewhere later on in the code. Imagine this as the ancestor of the Vue class.

Next, the Mocha `describe` function is set to provide a general context.
Within it, an `it` function is called to write the actual test case that checks if the imported `Element` class is equal to `123`, which it does using the method `assert.equal()`.

To run the tests we will have to install all dependencies `npm i` and run the Grunt tasks. But since most of the libraries used are deprecated we won't do that (and this is also not the goal of this article and video).

In the next section, we will explore the second commit aiming to reach our goals – find the first implementation of Vue.js, and understand how the mustache syntax works.

To do that, we need to look at the second commit's source code, which is the one I have downloaded and am exploring on VSCode (if you are following the video as well).

Here is the [direct link](https://github.com/vuejs/vue/tree/871ed9126639c9128c18bb2f19e6afd42c0c5ad9).

## The First Vue Application

In Vue, everything we do is done inside a Vue application, which is bound to an istance of the Vue class. So, we first need to find the first implementation of this class and in there we will find the logic behind the mustache syntax.

Ok, we need to look inside the explorations folder – here is where the magic happens.

The main file is called `getset-revitis-style.html`, and here we can see all the logic of the first Vue application (which you can find in the body tag) and its first implementation (which you can find in the `script` tag). 

I made a copy of the entire file and placed everything inside an index.html file so we can mess around with the code, add some console logs, and explore how it works. 

Let's serve the file using `serve -s`. (To run this command you will need to install an npm package. Just type in the terminal `npm install -g serve`.)

In the body tag we can see the Vue app, in `div` with an `id` of `test`. Today we either define our app inside a root element with an id of `app` or `root`, but at the time it started with a test div.

```html

 <div id="test">
   <p>{{msg}}</p>
   <p>{{msg}}</p>
   <p>{{msg}}</p>
   <p>{{what}}</p>
   <p>{{hey}}</p>
  </div>
```

Inside the test `div` we can see the double mustache syntax. Cool! This is the first time it was used, but how does it work? 

In the next section we will explore the first Vue class and look for the logic to make this `{{msg}}` work.

## The First Vue Instance

Ok, we found the firt usage of this syntax, but we are not done yet. We want to know how it works, remember? So, let's look in the script tag where we will find the logic of the first Vue class. 

Evan created a class called `Element` – remember that we are nine years back in time, and ES6 isn't a thing until 2015.

The class declaration is written using `function Element () {}`. This is the ancestor class of what we know today as the Vue instance that we instantiate by doing `new Vue()`.

```js

function Element (id, initData) {
  // The first implementation is in here
}
```

Next, the first Vue instance is created by instantiating the Element class:

```js

var app = new Element('test', {
  msg: 'hello'
})

```

The class expects an `id` and an `initData`. These are passed to the instance as the `test` value and as an object `{}` with a property called `msg`. This is our first implementation of the options object.

Ok, we are getting there. Now that we know how the class was implemented and instantiated, let's look inside to find how the double mustache syntax was implemented.

## How the Mustache Syntax Works

Here we are. The next code block will show us the syntax secrets. This is what we have been aiming to understand, the article's goal. 

After this you will be able to understand what's behind this syntax and even edit and replace it with your own.

You could do something like `[[msg]]` and maybe call it the double box syntax. 🤓 

The code below is used to make the double mustache syntax work. In between there is more code that is responsible for how data are bound. 

```js
var bindingMark = 'data-element-binding' // <-- data binding mark 

function Element (id, initData) {
// The first implementation is in here
  var self = this,
  el = self.el = document.getElementById(id)
  //console.log(self.el)
  
  bindings = {} // the internal copy
  data = self.data = {} // the external interface
  content = el.innerHTML.replace(/\{\{(.*)\}\}/g, markToken)

  el.innerHTML = content


  // ....

  function markToken(match, variable) {
    console.log(match) // <-- LOG match = {{msg}}
    console.log(variable) // <-- LOG captured group as variable = msg
    //console.log(bindings)
    bindings[variable] = {}
    //console.log(bindings)

    console.log('<span ' + bindingMark + '="' + variable + '"></span>')
    return '<span ' + bindingMark + '="' + variable + '"></span>'
  }

  // ...
}
```


I have added a couple console logs to figure out what's inside two key parameters (`match` and `variables`) and what the `markToken` method returns.

Inside the script tag the fist line is a variable `var bindingMark = 'data-element-binding'`. This variable will be used as a data attribute and will replace the contents of the curly brackets using the replace method with a regular expression `el.innerHTML.replace(/\{\{(.*)\}\}/g, markToken)`. 

Yes, you got it right – behind this syntax there is plain JavaScript and specifically one of the oldest methods built in the language.

`string.replace()` is a string method that accepts two parameters:

- the regular expression
- a callback function  

Check the result of the regex using a site like <regex101.com> to see what matches the regex `\{\{(.*)\}\}`.

When the callback function `markToken` is called, we have access to the match and the captured group, respectively used as parameters called `match` and `variables`.

You can see these two parameter values using the console logs I added in the source code.

Inside the `markToken` method, the first line after the console logs is `bindings[variable] = {}`. This is an internal copy of the data that will be used later for the data binings feature of the framework. 

For each match, it sets a new property in the `bindings` object as an empty object. For instance, if we have `{{msg}}` a new property called `binginds[msg] = {}` will be created.

Finally, the return statement builds a `span` element that uses the value of the `bindingMark` variable as a data attribute, `data-element-binding`
and assigns to it the `variable` parameter as property.

So, instead of `{{mess}}` the following string `'<span ' + bindingMark + '="' + variable + '"></span>'` is created. The result is the following code:

```html
<span data-element-binding="msg"></span>
```

The Vue code is still at its early stages. The implementation of the mustache syntax works alongside data bingind that is not yet fully implemented at this point of the framework.

## Conclusion

In this article, we discovered the first steps Evan You took to build Vue.js. This is a raw implementation of the framework, and we have seen only a small bit of its code. But it can help us figure out how one of the framework features worked. And hey, things always start small to grow over time.

Let me know if you liked this kind of content. Reach out to me if you want to know what's behind a different feature of Vuejs. 

You can also consider subscribing to my [YouTube channel](https://www.youtube.com/channel/UCTuFYi0pTsR9tOaO4qjV_pQ).

And you can follow me on [Twitter](https://twitter.com/Fab_Sky_Walker) and [Linkedin](https://www.linkedin.com/in/fabio-pacifici-com/).


