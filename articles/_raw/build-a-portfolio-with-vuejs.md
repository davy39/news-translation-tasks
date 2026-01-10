---
title: How to Build and Deploy a Portfolio with Vue.js Axios, the GitHub REST API,
  and Netlify
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-12T20:53:20.000Z'
originalURL: https://freecodecamp.org/news/build-a-portfolio-with-vuejs
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/VUE.JS-_-Article-Cover.jpg
tags:
- name: axios
  slug: axios
- name: GitHub
  slug: github
- name: Netlify
  slug: netlify
- name: portfolio
  slug: portfolio
- name: projects
  slug: projects
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: "By Fabio Pacific\nIn this free book, we will build two simple projects\
  \ and deploy them on Netlify. We will use Vue.js as our front-end framework, and\
  \ use different technologies to build our projects. \nIf you follow this tutorial\
  \ to the end, you will b..."
---

By Fabio Pacific

In this free book, we will build two simple projects and deploy them on Netlify. We will use Vue.js as our front-end framework, and use different technologies to build our projects. 

If you follow this tutorial to the end, you will build a simplified version of Twitter and a single page application for a portfolio using the GitHub API.

## What you need to know to follow this tutorial

To follow along, you will need at least some basic knowledge of HTML, CSS, and JavaScript. 

Knowledge of Vue.js isn't required, as you will learn the basics first and then we'll move into building the projects together.

At the end of each section, you'll find that information in video form via a YouTube link/embed. That way you can watch the videos to cement your knowledge of what you just read.

## Table of Contents

* [Introduction](#heading-introduction)
* [How to Install Vue](#heading-how-to-install-vue)
* [How to Create a Vue Instance](#heading-how-to-create-a-vue-instance)
* [How to Work with Templates in Vue](#heading-how-to-work-with-templates-in-vue)
* [Vue Directives](#heading-vue-directives)
* [Methods](#heading-methods-in-vue)
* [Conditionals](#heading-conditionals-in-vue-v-ifv-else-ifv-elsev-show)
* [Loops](#heading-loops-in-vue)
* [How to handle user inputs with events Handling](#heading-how-to-handle-user-input-with-event-handling-v-on-in-vue)
* [Two way model binding (v-model)](#heading-two-way-model-binding-v-model-in-vue)
* [Computed Properties and methods](#heading-computed-properties-and-methods)
* [**Project**: Simple Twitter Clone](#heading-how-to-create-a-simple-twitter-clone)
* [Component basics](#heading-vue-component-basics)
* [Project Update: Simple Twitter clone with components](#heading-how-to-update-your-simpletwitter-project-with-components)
* [Axios and RestAPI](#heading-how-to-perform-api-calls-with-axios)
* [Routing with VueRouter](#heading-how-to-handle-routing-with-vuerouter)
* [**Final Project**: build a Portfolio with VueJS, VueRouter, Axios, GitHub API](#heading-final-project-how-to-build-a-portfolio-with-vuejs-vuerouter-axios-github-api-and-deploy-to-netlify)
* [**Deploy** Continuous deployment with BitBucket and Netlify](#heading-continuos-deployment-with-bitbucket-and-netlify)

## Introduction
VueJS is a JavaScript framework that has become really popular in recent years. 

In this guide, we will start by looking at the fundamentals first, with a quick look at two libraries: VueRouter and Axios. We will use them to build a cool portfolio project at the end.

%[https://youtu.be/CzgP6GamIMc]

Click to view the video on [YouTube](https://youtu.be/CzgP6GamIMc).

## How to Install Vue

You can use Vue in your projects by installing it using a package manager like NPM or by using its CDN. If you've never used Vuejs before, I suggest that you use the CDN, as it will be easier if you want to code along with me. 

Click to view the [Repository](https://bitbucket.org/fbhood/how-to-vuejs/src/master/1-installation/)

Click to view the [YouTube-Video](https://youtu.be/enz0Vi3NuDA) or find it at the end of this section to reinforce what you've learned.

### The Vue CDN
For the CDN, we only need to include the script tag below inside our HTML file:

```html
<!-- Development version for prototyping and learning -->
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue.js"></script>
```
Alternatively, you can use a production-ready script that uses a specific stable release, like this:

```html
<!-- Production version -->
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.12"></script>
```

In production, Vue suggests using the optimized version to replace vue.js with vue.min.js.


There is also an ES Modules-compatible build:
```html
<script type="module">
  import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue.esm.browser.js'
</script>
```

### How to Install Vue via NPM
If you plan to build large scale applications, I recommend installing via NPM like this:

```bash
npm install vue
```

As I said above, we will use the Vue CDN so that anyone can follow this guide. So our final HTML file will look something like this: 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VueJS Tutorial</title>
    
    <!-- vue development version, includes helpful console warnings -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

</head>
<body>



    <script src="./main.js"></script>
</body>
</html>

```

Let's break this code down. First, we've add a basic markup for an HTML file. Then we've included the script tag for the VueJs framework. 

In the end, before closing the body tag, we've added our main.js script where we placed all the JavaScript code for our application. 

Let's now move to the next step and add our first Vue instance inside the main.js file.


%[https://youtu.be/enz0Vi3NuDA]

## How to Create a Vue Instance

Once you've installed Vue or included it via its CDN, you can create a Vue instance. You can do that using the `new Vue()` function. This function accepts an object of options.

If you read the documentation, you will see that the vue instance is often stored inside a variable called `vm`, but you can call it anything you like. I'll call it `app` during this guide.

So now, inside the main.js file you need to create a variable and store in it the Vue instance like so:
```js
let app = new Vue({
    // all options goes here
})
```
The object you pass to the Vue instance is called the options object.
Inside the options object, you can add all the options described in the Vue API reference pages to build our application. 

The options object has properties divided into multiple sections: 
- Data 
- DOM 
- Life Cycle Hooks 
- Assets
- Composition 
- Misc categories 

The first property that you need to build you Vue application is used to connect Vue with a root DOM element. Then you will need some data options to work with.

Let's start by connecting the Vue instance with a root DOM element.

You can click to view the [Repository](https://bitbucket.org/fbhood/how-to-vuejs/src/master/2-create-vue-instance/) here.

And you can click to view the [YouTube-Video](https://youtu.be/gBJaL7Jqh4w) or find it at the end of this section so you can review what you've learned.

### Options/DOM: How to select the root DOM element

The Options/DOM API gives you an `el` property that you can use to select an existing DOM element that Vue will use to mount your application instance. 

The `el` property accepts a string that contains a CSS selector for the element or directly a DOM element.

NOTE: Vue discourages using the body or HTML tags and suggests using a different element as a mounting point.

Let's do it. Inside the body of the index.html file, you need to put the following code:

```html
    <div id="app">
    </div> 
```
Now you have a root element that you can use to connect the Vue instance.
Back inside the main.js file, let's select this element inside the options object. 

You can now use the `el` property to select the element you created with an id of `app`.

```js
let app = new Vue({
    // all options go here
    el: "#app",
})
```

You now have an element to work with. You can move on to the next step and add to the options object the data object.

You can read more about it in the documentation here:[https://vuejs.org/v2/api/#Options-DOM]


### Options/Data: How to add the data object (or function when used in a component)

When a new instance is created, it adds all properties found in its data object to the Vue reactivity system. And when a value in the data object changes, the view will reflect these changes. This is at the base of the VueJS reactivity system. 

To explain it, let's see a practical example.

#### Create a data object
Inside the main.js file you can create a data property that has an object as its value, like so:
```js

let app = new Vue({
    // all options go here
    el: "#app",
    data: {}
})
```
The data object can be defined directly inside the Vue instance like in the code above, or outside the instance like in the code below. 

```js
let dataObject = {}
let app = new Vue({
    // all options go here
    el: "#app",
    data: dataObject
})
```

You can pick the one you like.

#### Add properties to the Data Object
Since VueJs is a JavaScript framework, it's helpful to remember that what you know about JavaScript is still valuable here. 

Vue is just a JavaScript object that has a number of methods and properties that you can use to simplify and speed up your workflow.

Let's add some properties to the data object to see how it works.
```js
// Create a data object
let app = new Vue({
    el:"#app",
    // create a vue instance, add the data property and the dataObject created
    data: {
        alert: "This is an alert message! ",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "grocery shop", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "automation script", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ];
    }
})
```
With the code above, you simply add two properties to the data object: an `alert` property and a  `projects` property. 

The alert property just a string while the projects property is an array of objects. 

Now that you have some data to work with, let's see how you can access and modify their values.

#### Manipulate properties in the data object
You can access and manipulate the properties of a data object using the variable that contains the Vue instance `app`. Then you can reference the properties using dot notation, like `app.alert`. 

In the browser, if you open the console you can see that when you write `app` you get the Vue instance object. So, like any other object with dot notation, you get its properties and methods.

Let's try this out inside the console:
```js
// Access the alert property in the data object
app.alert // This is an alert message!
// update a data property value
app.alert = "This is a new alert message!" 
app.projects
```
The code above does three simple things:
- the first line accesses the `alert` property and prints its content "this is an alert message"
- the second line assigns a new value to the `alert` property with the equals operator
- finally, the third line returns the value of the projects array. 

You can also access the entire data object using the shortcuts $data or _data

Back in the console:
```js
// Access the entrie data object
app.$data // {__ob__: Observer} option 1
app._data // {__ob__: Observer} option 2

```

You can read more about this in the documentation here: [https://vuejs.org/v2/api/#Options-Data]

### Options Data Methods
The Vue instance gives you access to a number of properties and methods.
You can access default methods and properties using the `$` sign. It is used to differentiate Vue defined methods from those defined by the user.

There are a number of instance methods and properties predefined and split into four different categories:

- Instance Properties
- Instance Methods / Data
- Instance Methods / Events
- Instance Methods/life cycle hooks

For instance, with the following code, you can get the `data` and `options` objects or access the `watch` or the `on` methods. 

```js
app.$data // returns the data object
app.$options // returns the options object
app.$watch() // function that watched for changes on the vue instance
app.$on() // listen for a custom event on the vue instance
```

I won't dive deeper into this since it's out of the scope of this guide. But if you are interested and want to learn more, here is the [documentation](https://vuejs.org/v2/api/#Instance-Properties).

### Lifecycle Hooks
Vue gives you access to a series of functions called lifecycle hooks. They allow you to run code at specific stages of the Vue initialization steps.

Inside all lifecycle hooks you have access to their `this` variable that points to the Vue instance. 

You will see how this works in more detail in future sections. But for now this is a short summary of the available hooks and what they let you do:

- beforeCreate (you can run code before the Vue instance is created)
- created (you can run code after the Vue instance is created )
- beforeMount (you can run code before your element is mounted to the DOM)
- mounted (you can run code when the element is mounted to the DOM)
- beforeUpdate (you can run code before values are updated in the DOM)
- updated (you can run code after values in the DOM have been updated)
- beforeDestroy (you can run code before an instance is destroyed)
- destroyed (you can run code when an instance is destroyed)

During the course, we will often use the mounted hook. If you are curious to learn more about this topic, I suggest you look at the diagram in the documentation first. Find the lifecycle Hooks [diagram](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram) here.


%[https://youtu.be/gBJaL7Jqh4w]

## How to Work with Templates in Vue

VueJS uses mustache syntax `{{ }}` to render data from the Vue instance inside the HTML element. 

Using this syntax you can grab properties and methods defined in the Vue instance. The property is then parsed and rendered to the page.

You can click to view the [Repository here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/3-work-with-templates/).

And you can click to view the [YouTube-Video here](https://youtu.be/pDj3SQ8TNzs) here, or find it at the end of this section to review what you've just learned.

### Text Data binding
This is called text data binding. Let's see an example of how you can bind data between the Vue instance and your template file. 

```html

<div id="app">
    <h1>{{ title }}</h1>
</div>
```
The code above has an `h1` tag inside the root element with an id of `app` we defined in the previous chapter. 

Inside the `h1` tag you use the double curly brackets syntax to render onto the page the value of a property in the data object called that you called `title`. 

You don't have a `title` property yet inside your data object, so let's add it.

Inside the main.js file
```js

let app = new Vue({
    el: "#app",
    data: {
        title: "John Doe portfolio",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "grocery shop", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "automation script", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ]
    }
})

```

Now, with the code above you can render the content of the property `title` inside the `h1` tag in your template. The final result will be something like this: 

```html
<h1>John Doe portfolio</h1>
```

However, with this method, you can only pass a string. If you want to use HTML tags inside the string these will not be parsed but instead will be shown as simple strings.

For instance if you assign the following string to the `title` property
```js
    title: "John Doe <span class='badge'>Portfolio</span>"
```
And then try to render it inside our HTML like so:
```html
<h1 class="title">{{title}}</h1>
```
The property `title` will be rendered as a plain string including the HTML tags 
ie. ```John Doe <span class='badge'>Portfolio</span>```

Of course you can parse HTML too.

### How to parse raw HTML
To render a raw HTML element we need to introduce another important Vue concept called directives. 

In this case, you will use the v-html directive inside your HTML tag as an attribute and pass to it the property title. 

When you're using Vue directives, the text inside the quotes is considered a JavaScript expression. This means that it's computed and its result is rendered.  

Let's create a separate property for the title with HTML tags inside so that you can see how both render onto the page. 

```js
let app = new Vue({
    el: "#app",
    data: {
        title: "John Doe Portfolio", 
        titleHTLM : "John Doe <span class='badge'>Portfolio</span>",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "grocery shop", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "automation script", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ]
    }
})

```
Now inside your HTML file, you will use this `{{}}` syntax to render the property `title`. But on the tag where you want to render raw HTML, with the `titleHTML` property, you use the v-html directive instead.

```html
<div id="app">
    <div class="title">{{ title }}</div>
    <div v-html="titleHTML"></div>
</div>
```
Both elements will now render correctly including the second property that has HTML tags inside.

NOTE: Rendering HTML can expose XSS vulnerabilities. Never use this approach on user-provided content.

Now that you know how to render data onto the page, let's dig deeper into directives. 

If you want to read more, visit the documentation 
[here](https://vuejs.org/v2/guide/syntax.html#Using-JavaScript-Expressions).


%[https://youtu.be/pDj3SQ8TNzs]



## Vue Directives 

Inside your HTML files, you can use directives to interact with HTML attributes. A directive applies effects to the DOM when its expression changes. 

You can click to view the [Repository here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/4-Directives/)

And you can click to view the [YouTube-Video here](https://youtu.be/LICvNmhsTEs), or you can find it at the end of this section to review what you've learned.

### The v-bind directive on HTML attributes
So far, you have used the `{{}}` syntax to render something between HTML opening and closing tags. But inside an HTML tag you cannot use the {{ }} syntax. 

So how do you connect an HTML attribute to the Vue instance? You use the v-bind directive instead which lets you access data object properties as you have done before. 

The v-bind directive is one of the directives that take arguments which are specified after the colon. In our case here, what's specified after the colon is the HTML attribute name like id, class, href, src and so on. 

If you need to dynamically assign an attribute like href or even a class, you can bind it with the Vue instance using the v-bind directive. It will then be able to get what's in the options object, like properties in the data object.

Let's see v-bind in action and start connecting the `id` and `class` attributes so you can assign them values dynamically with Vue.

Inside our index.html file:
```html
<div id="app">
    <div v-bind:class="dynamicClass" v-bind:id="dynamicId">Dinamically assign a class and an id to the div</div>
</div>
```
Let's break the code above and see what it's doing. 

First, you have a `div` tag inside the root element. Then you use the v-bind directive on the class and the id attributes. 

Inside the quotes, you specify two properties that later you'll define inside the data object of your Vue instance.

Remember that when using Vue directives the content between quotes is treated as a JavaScript expression.

Let's define these two properties inside the Vue instance.
```js
let app = new Vue({
    el: "#app",
    data: {
        title: "John Doe Portfolio", 
        titleHTLM : "John Doe <span class='badge'>Portfolio</span>",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "grocery shop", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "automation script", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ],
        dynamicId : "projects_section",
        dynamicClass : "projects"
    }
})


```
So you have defined `dinamicId: "projects_section"` and `dynmicClass: "projects"` properties and assigned them two values.

Thanks to the data binding on the attributes, your HTML tag will be rendered as follows (and you can now dynamically change your attributes values and see them change reactively):

```html
<div id="projects_section" class="projects">Dynamically assign a class and an id to the div</div>
```

### V-bind with Boolean values
With attributes using a boolean value, the v-bind directive works differently. It will show the attribute only if the property's value is true. In all other cases, it won't render the attribute and its content. 

For the next example, you will use a button with the disabled attribute.

Inside your root HTML element:
```html
    <div id="app">
        <button v-bind:disabled="disabled">You can't click this button</button>
    </div>
```
Inside a Vue instance:
```js
let app = new Vue({
    el: '#app',
    data: {
    //disabled: false, // wont render the attribute
    //disabled: null, // wont render the attribute
    //disabled: undefined, // wont render the attribute
    disabled: true // renders the attribute
}
})

```

Only if the disabled property is set to true does the attribute become visible and render its property content.
```html
    <button disabled>You can't click this button</button>
```
This is something to keep in mind when working with such attributes.

Another thing to consider is that bindings can include a single JavaScript expression, with some restrictions:
- only expressions are allowed
- only a single expression
- no statements
- no flow control tools, but the ternary operator works.

If you want to read more, visit the documentation 
here:[https://vuejs.org/v2/guide/syntax.html#Using-JavaScript-Expressions]

So far we have seen only two Vue directives, v-html and v-bind. But there are a number of directives available, and here are some more (to list just a few):
- v-html
- v-bind
- v-if
- v-else-if
- v-else
- v-for
- v-on
All directives have a v- prefix, but there is shorthand for v-bind (:) and v-on (@). 

They work in the same way. Here's a quick reference for the v-bind and v-on directives: 
```html
<!-- Long syntax -->
<a v-bind:href="url">Some link</a>
<!-- Shot syntax -->
<a :href="url">Some link</a>
<!-- Long syntax with dynamic arguments -->
<a v-bind:[attribute_name]="url">Some link</a>
<!-- Shot syntax with dynamic arguments -->
<a :[attribute_name]="url">Some link</a>
```
Shorthand for v-on
```html
<!-- Long syntax -->
<a v-on:click="runFunction">Some link</a>
<!-- Shot syntax -->
<a @click="runFunction">Some link</a>
<!-- Long syntax with dynamic arguments -->
<a v-on:[attribute_name]="runFunction">Some link</a>
<!-- Shot syntax with dynamic arguments -->
<a @:[attribute_name]="runFunction">Some link</a>

```
Now let's see what dynamic arguments are and how they work.

### Dynamic arguments in Vue
Directives have been able to have dynamic arguments since Vue 2.6.0. You can use a JavaScript expression in the directive argument if you wrap it inside square brackets.

But there are some restrictions:
- expressions should evaluate to a string
- spaces and quotes are invalid

Let's see a practical example
```html
    <a v-bind:[attribute_name]="url">Visit my Website</a>
```
Inside your data object you can define the directive arguments as if they were properties, where the property value is the name of your HTML attribute like `hef` in the following example:

```js
let app = new Vue({
    el: '#app',
    data: {
        attribute_name: 'href',
        url: 'https://fabiopacifici.com'
    }
})

```
The code above renders the attribute name `href` and its value dynamically when you bind it using the v-bind directive.

The result will be this:  
```htm
<a href="https://fabiopacifici.com">Visit my Website</a>
```

### Dynamic events in Vue
You can apply the same concept to event directives like v-on. This directive does the job of the JavaScript event listener. 

v-on accepts an argument like click, for example `v-on:click="doSomething"`.

To apply the concept of dynamicity, let's create a v-on directive and use the square brackets after it to specify a dynamic event.

Inside the index.html file you will place the following code:
```html
    <div id="app">
        <a v-on:[event_name]="runFunction">Some link</a>
    </div>
```
Let's break down the code above. 

First you have your root element, the `div` with an `id` of `app`. Inside the root element you add an anchor tag `<a>Some link</a>`. 

The anchor tag has a `v-on` directive in it. After the directive you specify a dynamic argument `v-on:[event_name]` where `event_name` will be a property inside your Vue instance that you can change as you need. 

The v-on directive works like any event listener, so between quotes you need to specify the name of the function that you want to run when the event is triggered, therefore `runFunction`.

Now, inside your main.js file:
```js
let app = new Vue({
    el: '#app',
    data: {
    event_name: "click"
    },
    methods: {
        runFunction() {
            console.log("test click function");
        }
    }
})
```
Let's review what the code above does. 

First, you create the Vue instance. Then you add the `event_name` property inside the data object and you assign to it a value of `click`. This is the event you will listen for.

Finally, we said that the v-on directive runs a function when the event is triggered, therefore you need to write a method inside your Vue instance. So inside the methods object, create a new function called `runFunction` that will simply output a message inside the console. 

The power of dynamic events is clear when you replace the value of the `event_name` property with a different event name.


%[https://youtu.be/LICvNmhsTEs]

## Methods in Vue

So far we've learned how to bind data using the v-bind directive inside your template. In the next section, you will learn more directives – but before diving into that, let's quickly talk about how to store your functions. 

You can check out the [Repository here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/5-Methods/) 

And you can see the video version of this section on [YouTube](https://youtu.be/dESmaEvkZ2I) if you want to review what you learn.

Since you are working in a big object, the Vue instance function will take the name of the methods. And as you might guess, the Options object has a property called `methods` where you can store your functions as you do for your data. 

Inside your Vue instance, define a method that you can call anything you like – just remember to use a naming convention that clearly describes your code.

```js

let app = new Vue({
    el: '#app',
    data: {
        firstName: "Fabio",
        lastName: "Pacific" 
    },
    methods: {
        // es6 syntax
        getFullName(){
            return this.firstName + " " + this.lastName;
        }
        // es5 syntax
    /* getFullName: function(){

        } */
    }
});

```
In the code above, you created a method inside the methods object. You called it `getFullName`. Inside a method, you have access to the `this` keyword that refers to the object instance, so you can use it to access from a method the properties stored in the data object.

When you call the method `getFullName` the method will return a single string that contains both the first and the last name. 

Now inside your HTML file, you can simply call the method as you did when you needed to access properties in the data object `{{ getFullName() }}` 

```html
<div>{{ getFullName() }}</div>
```
Now that you know how to create a method and where to put it in the Vue instance, let's move forward and learn more about directives.


%[https://youtu.be/dESmaEvkZ2I]

## Conditionals in Vue (v-if/v-else-if/v-else/v-show)
 
Now it's time to learn more about directives. We will start by looking at how conditionals work in VueJS. The first directive of this section is the `v-if`, which allows you to render blocks of code based on a certain condition. 

You can click to view the [Repository here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/6-Conditionals/]).

And you can click to view the video on [YouTube here](https://youtu.be/VNaCsloA1ZU) or use it to review at the end of the section.

Like the `if-else` statements in vanilla JavaScript, the v-if will check if the returned value of a conditional expression evaluates to true. If so it will render the HTML element and everything you place inside it. 

Since it's a directive, it works on a single element (HTML tag). If you want to extend its behaviour on multiple elements, then you need to wrap them inside a `<template>` tag.

The v-if directive works in the same way as the v-bind directive works: it has access to the properties in the data object and accepts an expression between its quotes. 

If the returned value of the expression or the value of the data property you use evaluates to `true`, then the directive renders the HTML element. Otherwise it doesn't.

Of course, you can check for multiple conditions and end up rendering an element if none of these evaluates to true. You do that using v-if together with the v-else-if and v-else directives.

Let's see a simple example and write some code inside your main.js file to show or hide an element.

The first thing to note is that if you have a property that returns a boolean value, it is enough to use it inside the v-if directive to show/hide an element, like so: 

```html
<h1 v-if="showTitle">{{movieTitle}}</h1>
```
And a vue instance with a showTitle property set to true.
```js

let app = new Vue({
    el: "#app",
    data: {
        movieTitle: 'Shining',
        showTitle: true,
    }
})
```
In such a case, you are saying show the title property only if the value of `showTitle` is `true`. If you change it to false, the title won't show.

You can put a simple expression inside the quotes of a v-if directive that once computed evaluates to a boolean.
```html
<h2 v-if="age >= 18">{{movieTitle}}</h2>

```
Inside your main.js file
```js 
let app = new Vue({
    el: "#app",
    data: {
        movieTitle: 'Shining',
        age: 18,
    }
})
```
In the code above we wrote an expression on the v-if directive that checks if the `age` property is greater than or equal to 18. If the result is true then the `h2` will be shown onto the page.

Now let's move to a more complex example and add another condition using the v-else-if.

#### v-if/v-else-if
In the following example, you will first create a v-if condition similar to the one above – but this time you'll check if the user is over 18 but under 21 using the `&&` operator. 

If true, then you'll show the time with an additional note. If false, and the user is over 21, then we will simply show the title of the movie. 
```html
<h2 v-if="age > 21">{{movieTitle}}</h2>
<h2 v-else-if="age > 18 && age < 21"> {{ movieTitle }} | Watch with an adult</h2>
```
Inside the Vue instance you could have an `age` property. But to make your simple program dynamic, you can instead use a prompt to ask the user their age. 

```js
let userAge = Number(prompt("What's your age?"))
let app = new Vue({
    el: "#app",
    data: {
        movieTitle: 'Shining',
        age: userAge,
    }
})
```
So the code here first asks the user their age, then stores the result as a number inside the variable `userAge`. 

You'll later use the `userAge` variable inside the data object to assign a value to the `age` property so that based on its value you will render one element or the other.

Let's move forward and use the v-else directive to show a different message in case the user is under 18.

#### v-else directive:
The `v-else` directive works differently. You don't have to pass it anything. It simply enters into action when none of the previous conditions evaluate to a true value.

So the new HTML element is fairly simple:

```html
    <div id="app">
        <h2 v-if="age > 21">{{movieTitle}}</h2>
        <h2 v-else-if="age > 18 && age < 21"> {{ movieTitle }} | Watch with an adult</h2>
        <p v-else> Sorry You are too young to see this movie</p>
    </div>

```

Here we have a `p` tag with a v-else directive attached. As you can see, it looks like an attribute without values (like the disabled or required HTML attributes).

Your JavaScript file has not changed.
```js

let userAge = Number(prompt("What's your age?"))
let app = new Vue({
    el: "#app",
    data: {
        movieTitle: 'Shining',
        age: userAge,
    }
})
```

That's all you need to know about conditional rendering to be able to move forward with your first project. But if you want to learn more, here is the documentation: [https://vuejs.org/v2/guide/conditional.html]

You need to learn a few more things before you'll be able to build your first project, which is a simplified Twitter clone. The next topic is about Loops.


%[https://youtu.be/VNaCsloA1ZU]

## Loops in Vue

Let's go back to the previous example and learn how to use the v-for directive to output each project of the array onto the page. 

You can click to view the Repository [here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/7-loops/)

And you can click to view the YouTube-Video [here](https://youtu.be/aViHg80-7Bs), or you can find it at the end of this section to review what you've learned.

For our next task, it would be useful if we could use a loop, and the v-for directive is here to help.

Its syntax doesn't have much in common with a classic `for` loop in JavaScript, but rather with a Python `for in` loop or with the `for in` JavaScript loop used to iterate over objects.

With this directive, you specify the elements of the array and the single element between quotes using the syntax `project in projects`. Here, projects are the property inside the data object that contains an array of objects, and project is the single element of the array. 

You can call this as you like, but keep in mind that what follows the `in` keyword must be an iterable from your data object while what comes before can be anything you like to refer to each element of the iterable. 

In your case, project seems the most appropriate choice since you have an array of projects.

Your JavaScript file will look like this:
```js
let app = new Vue({
    el: "#app",
    data: {
        name: "John Doe",
        title: "Portfolio",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "grocery shop", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "automation script", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ],
        
    }

});
```
Now inside the HTML file, let's use the v-for to render the title of each project.
```html
    <div id="app">
        <h1>{{name}} {{title}}</h1>
        <ul>
            <li v-for="project in projects">{{project.title}}</li>
        </ul>
    </div>
```
In the code above, you used `{{name}} {{title}}` to render the main title for your portfolio. Then you used the v-for directive and specified inside the quests that you want to assign each element of the iteration to a project variable `v-for="project in projects"`.

Now on each iteration, the `project` variable holds an object from which you can retrieve its properties using dot notation like so: `{{ project.title }}`.

One thing to note is that the v-for directive also gives you access to the index of the element at each iteration. You can store it in a variable as you did with the single element you called project. 

To do that, you need to wrap them between parentheses and separate the element and its index with a comma, like so `v-for="(project, index) in projects"`. 

Also, note that when working with objects Vue can show an alert to inform you that the use of a key is recommended. This means that it expects a key to identify each element when it's rendered. 

You can do this using the `key` attribute and bind it, for instance to an id property on the object or to another different property, like so

```html

<div id="app">
    <h1>{{name}} {{title}}</h1>
    <ul>
        <li v-for="project in projects" :key="project.title">{{project.title}}</li>
    </ul>
</div>
```
Here you used the v-bind shorthand directive to bind the key attribute to the project.id property if it exists or to another property if not. 

```js
let app = new Vue({
    el: "#app",
    data: {
        name: "John Doe",
        title: "Portfolio",
        projects: [
            {title: "portfolio", languages: ["HTML", "CSS", "VueJS"]},
            {title: "grocery shop", languages: ["HTML", "CSS", "PHP"]},
            {title: "blog", languages: ["HTML", "CSS", "PHP"]},
            {title: "automation script", languages: ["Python"]},
            {title: "eCommerce", languages: ["HTML", "CSS", "PHP"]},
        ],
        
    }

});

```

v-for can also be used to iterate over objects. In such a case, you have access to the value, the key, and also the index like so `v-for="(value, key, index) in object"` where 'object' is a property in the data object.

If you want to learn more, visit the documentation here: [https://vuejs.org/v2/guide/list.html]

Let's now move on to another important feature of Vue: how to handle user inputs and events. 


%[https://youtu.be/aViHg80-7Bs]



## How to Handle User Input with Event Handling (v-on) in Vue
 
To make the application react to a user's input, Vue provides a straightforward directive called `v-on`. This is one of the directives that accepts arguments, similar to the v-bind directive. 

With such a directive, it's easy to listen for events triggered by a user.

The v-on directive lets you run a function that executes a block of code when the user performs an action, like when they click on a button, hover on an element, or press a specific key on the keyboard.

You can check out the [Repository here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/8-user-inputs-events-handling/).

And you can view the video on [YouTube here](https://youtu.be/9_U1eagqOJY) or at the end of this section to review what you've learned.

### V-on Syntax and Events
There are two types of syntax we can use, the long-form or the short. They're equivalent, so pick the one you prefer. What follows is just a representation of the syntax, and I'll explain it in detail in a minute.

Long syntax: `v-on:EventName='doSomething' `
Shot syntax: `@EventName='doSomething'`

There are many events you can listen to, such as: 
- click
- submit
- mouseover
- mouseenter
- mouseleave
- keyup
- keydown
- keypress

But you can also create custom events (which you will see when you reach the components section).

Let's pick the long-form syntax: `v-on:EventName='doSomething`. I'll explain it more now.

First, you have the directive `v-on`. Then you have an argument that is the event name you want to listen for, like `click`. After that, the `doSomething` can be any method that you have defined inside the methods object of the Vue instance.

This method is like any other function that you define inside a JavaScript object. It can have parameters or not. If it has them, you can call the method and pass parameters to it as usual like this: `doSomething(param, param_2, param3)`. 

You can have something like this `<div v-on:click="likeProject">Like</div>` and when the user clicks on this element, it will trigger a method and run some code to increase a like counter inside a project.

Let's first create the HTML you need for that:
```html
<div class="projects" v-for="(project,index) in projects">
    <h1>{{project.title.toUpperCase()}}</h1>
    <p>Lorem ipsum dolor sit amet.</p>
    <div>Like
        <i class="fas fa-heart fa-lg fa-fw" @click="likeProject(index)">
        </i>
        {{project.likes}}
    </div>
</div>

```
In the code here, first you'll use the v-for directive to loop over the array of projects. Note that you should use the syntax `(project, index) in projects` because you will need to pass the index to the like method that you defined earlier. 

After that, you output some data onto the page (like the project name in uppercase letters) then the description, and a `div` tag with an icon for the likes (remember to add font awesome to get the icon). 

On the heart icon, add the directive v-on using the short syntax `@click="likeProject(index)"` between quotes that you used to invoke your `likeProject(index)` method. Then pass to it the index as a parameter so you can find the current project the user clicked on. 

Finally, you'll render the likes onto the page for the current project using the `{{project.likes}}` syntax.


Now it's time to go in the Vue instance and write your method.
```js

let app = new Vue({
    el:"#app",
    data: {
        projects: [
            {title: "My first project", description: "A simplified Twitter clone", likes: 0},
            {title: "My second project", description: "Projects portfolio with GitHub", likes: 0},
        ]
    },
        methods: {
            likeProject(index){
                const project = this.projects[index]
                project.likes++
                console.log(project.likes)
            }
        
    }
});

```
As I said earlier, you needed to define a method to call when the user clicks on a link. So you create the `likeProject` method, which accepts a parameter that will be the index of the element the user clicked on. 

You can then add a likes property inside your projects array and access it for the current project to increment its value every time the user clicks on your link.


### How to access the original event
If for any reason you need to access the original DOM event, you could have used the special `$event` variable inside the method like this on the v-on directive: `doSomething(param1, param2, $event)`. Let's see an example of that now.

You need to add the special variable in the method call on your v-on directive like so:
```html
<i class="fas fa-heart fa-lg fa-fw" @click="likeProject(index, $event)">
        </i>
```
Then you can access the original event inside your method like so: 
```js
likeProject(index, event){
    console.log(event); // get the original event
    const project = this.projects[index]
    project.likes++
    console.log(project.likes)
}
```

Now that you know how the v-on directive works, let's improve our Likes example and put something more in it. We will use key modifiers in the next example, so let's quickly see what they are and what you can do with them.

### Event Modifiers in Vue
With events, Vue provides access to a number of Event modifiers. They are divided into 4 main groups. You can add these modifiers to a directive to change the way your event behaves. They are like postfix and you can chain them using dot notation. 

Below there is a quick reference.

Categories:
- event modifiers
- key modifiers
- system modifiers keys
- mouse buttons modifiers

Event Modifiers:
.stop
.prevent 
.capture
.self
.once
.passive

Key Modifiers:
You can add these modifiers to the @keyup listener to listen for when these keys are pressed or use them as a combination with the @click event to listen for a click+space, for example. `@click.enter="doSomething"`

.enter
.tab
.delete (captures both “Delete” and “Backspace” keys)
.esc
.space
.up
.down
.left
.right

System modifiers:
With these modifiers, you can trigger mouse or keyboard event listeners when the corresponding key is pressed.
.ctrl 
.alt
.shift
.meta
.exact (allows control of the exact combination of system modifiers needed to trigger an event)

Mouse buttons modifiers:
These modifiers allow you to trigger a mouse event listener if the corresponding mouse button is clicked. 

.left
.right
.middle

If you want to learn more, read the docs [here](https://vuejs.org/v2/guide/events.html#Event-Modifiers).


### How to like a project with key modifiers
In the previous example, you used the v-on:click directive to trigger a mouse event listener that aimed to simulate a like on a project. 

But the user was able to add as many likes they wanted by clicking on the icon. 

In the next example, you will do things a bit differently.
- First, you will prevent the user from adding more than one like to each project,
- Then you will let the user remove a like 
- Finally, you will keep the likes on the page even after the user refreshes the page.

Let's get started. This time you will use mouse button modifiers to listen for clicks. The left mouse button click will trigger the add like behaviour and the right mouse button click will trigger the remove behaviour.

Inside your HTML file: 
```html
<div id="app">
    
    <!-- Users can like a project with a left click and dislike it with right click -->

        <div class="projects" v-for="project in projects">
            <h1>{{project.title.toUpperCase()}}</h1>
            <p>Lorem ipsum dolor sit amet.</p>
            <div>Like 
                <i class="fas fa-heart fa-lg fa-fw" 
                    @click.left="addLike(project)" 
                    @click.right="removeLike(project, $event)">
                </i> 
               {{project.likes}}
            </div>
        </div>


</div>
```

In the code above you have taken what you had before and simply added a left mouse button key modifier to the click event `@click.left`. Then you invoked the `addLike` method. This will make your project like counter increase by one as we have seen before. 

Then you added another event listener to the same element, but this time you used the `.right` mouse button key modifier to listen when the user clicks on our icon using the right button `@click.right="removeLike()"`. 

In the remove like method, you have also passed the special variable $event so that you can use the original event later in your method to prevent its default behaviour and open the contextual menu. 

But we said earlier that you can also chain key modifiers and indeed there is a `.prevent` key modifier that you can use here instead of the `$event` variable. You could do the same like this: `@click.right.prevent="removeLike(project)"` 

Let's see how to structure your main.js file:
 
```js
let app = new Vue({
    el: "#app",
    data: {
        name: "John Doe",
        title: "Portfolio",
        projects: [
            {title: "My first project", description: "A simplified Twitter clone", likes: 0},
            {title: "My second project", description: "Projects portfolio with GitHub", likes: 0},
        ]
    },
    methods: {
        addLike(project){
           console.log(project)  
        },
        removeLike(project, event){
            console.log(project)
            console.log(event)
        }
    }

});
```
So in the data object, you have a `projects` property that is an array of objects. Each object has a likes property that you will increment or decrement depending on what mouse button the user clicks.

Inside the `methods` object, you created the two methods you referenced in your v-on directives `addLike()` and `removeLike()`. For now, you are only logging to the console the project parameter value and the event value. You will implement the logic in a minute.

Let's start with the add likes method – it could look like this:
```js
addLike(project){
    const projectTitle = project.title;
    if(!localStorage.getItem(projectTitle)) {
        project.likes++;
        localStorage.setItem(projectTitle, true);
    }              
}
```
There are a few things going on here. In the first line, you're storing the project title inside the `projectTitle` variable. Then, you said you wanted data to persist if you refresh the page so you are using the `localStorage` API to store information inside the client browser. 

You increment the likes count by one, but you do that depending on a value inside the local storage. 

You can do this by first checking to see if there is a key in the `localStorage` matching your project title, `if(!localStorage.getItem(projectTitle))`. 

If this evaluates to false, then you will run the code inside the if block and first increment the likes `project.likes++`. 

Second, use the `.setItem()` method of the local storage API to set a key-value pair with the project title as the key and a boolean value as its value `localStorage.setItem(projectTitle, true)`.


To put an item in the local storage, you'll use `localStorage.setItem()`. The set item method accepts a key-value pair. Your key will be the title you saved in the variable `projectTitle` and the value will the boolean value `true`.

Now let's see if this works. 

```js
removeLike(project, event){
    event.preventDefault(); // This can be omitted if we use the prevent key modifier
    const projectTitle = project.title;
    if(project.likes > 0 && localStorage.getItem(projectTitle)) {
        project.likes--;
        localStorage.removeItem(projectTitle);
    }
}
```
This function does the opposite of the previous. When the user clicks their right mouse button, the method `removeLikes()` is executed and you do the following:

First things first, you need to prevent its default behaviour. Otherwise when the user right-clicks on the icon, the contextual menu will pop up and we don't want that. So, you'll use the `event.preventDefault()` method on the original event that is represented by the `event` parameter on your method. 

Alternatively, you can omit this if you use the prevent key modifier in the v-on directive `@click.right.prevent="removeLike(project)`.

The next step is to grab the project title. Since you also passed a parameter to the method to represent the current project object `removeLike(project, event)`, you can store the project title in a variable `projectTitle`.

Then you need to make a couple of checks. First, you want to decrement the likes only if its value is greater than zero. Then you want to make sure the project title is in the local storage as a key with a value. 

So, in your condition, you have done both checks `if(project.likes > 0 && localStorage.getItem(projectTitle))`. Now, if both conditions evaluate to true, the code inside the if block can run. 

First you remove the like by decrementing its value `project.likes--`. Then you remove the project title from the local storage using the `removeItem` method and pass to it the key you want to remove (which is the project title `localStorage.removeItem(projectTitle)`).   

To put it all together, you should now have the following code:

```js
let app = new Vue({
    el: "#app",
    data: {
        name: "John Doe",
        title: "Portfolio",
        projects: [
            {title: "My first project", description: "A simplified Twitter clone", likes: 0},
            {title: "My second project", description: "Projects portfolio with GitHub", likes: 0},
        ]
    },
        methods: {
        addLike(project)
        {
            //console.log(project, "like");
            const projectTitle = project.title;
            // check if the current project is not in the local storage
            if(!localStorage.getItem(projectTitle)) {
                // set the item in the storage and increase the likes counter
                project.likes++;
                localStorage.setItem(projectTitle, true);
            }
          
        },
        removeLike(project){ 
            const projectTitle = project.title;
            console.log(project, "dislike");  
            if(project.likes > 0 && Boolean(localStorage.getItem(projectTitle))) {
                project.likes--;
                localStorage.removeItem(projectTitle);
            }
            
        }
    },
    mounted(){
        this.projects.forEach(project => {
            if(localStorage.getItem(project.title) !== null) {
                project.likes = 1; 
            }
        });
    }

});

```

To make the code work, you also need to add a life cycle hook called mounted. This will let you run code when the root element is mounted on the Vue instance. With it, you can check if the localStorage has a key corresponding to your project title and if so, update the value of the likes counter.

And your HTML is still the same:
```html
<div id="app">
    <!-- Users can like a project with a left click and dislike it with right click -->

    <div class="projects" v-for="project in projects">
        <h1>{{project.title.toUpperCase()}}</h1>
        <p>Lorem ipsum dolor sit amet.</p>
        <div>Like 
            <i class="fas fa-heart fa-lg fa-fw" 
                @click.left="addLike(project)" 
                @click.right="removeLike(project, $event)">
            </i> 
            {{project.likes}}
        </div>
    </div>
</div>
```
Remember that you can get rid of the `$event` variable passed to the `removeLike` method by using the event key modifier like so: `@click.right.prevent="removeLike(project)"`


You have learned a lot so far! And now that you have seen key modifiers in action, we can move forward to the next topic: two-way model binding and the v-model directive. Then we'll start building our Twitter clone. 


%[https://youtu.be/9_U1eagqOJY]




## Two Way Model Binding (v-model) in Vue

All right, so far we have seen how to bind properties from the data object to our HTML tags and inside attributes, 
how to loop over a sequence of elements and, how to display conditionally elements onto our template with conditionals. 

We have covered how to define methods inside the methods object so that we can perform more complex operations on our data and, 
we have learned how to work with events using the v-on directive.

In the next section, we will look at how Vue opens a two-way communication channel between a form's input and, a property defined
inside the data object. Then we will use this knowledge to build our first project together.

You can check out the [Repositoy here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/9-two-way-binding/).

And you can view the video on [YouTube here](https://youtu.be/pBUXTUvDRCo) or at the end of the section if you want to review what you've learned.

### How does the v-model directive work?
The v-model is another Vue directive. You can use it out of the box, and it's useful to simplify the way an input tag can communicate 
with a Vue instance's property in the data object. 

It works like all the other directives. The main difference is that when it's implemented, your application will listen for changes 
inside the input with this v-model directive and update the attached property's value immediately inside the data object and vice-versa. 

It is effectively a two-way communication channel between your template and the Vue instance. It's the Vue way to interact with user input and simplify your life as a developer.

Let's look at a straightforward example.

### How to use the v-model on an input tag
First, you need an input tag inside the element you defined as the root element in the Vue instance, the div with an id of `app`. 
```html
<div id="app">
    <h2>What do you want to tweet about today?</h2>
    <input type="text" v-model="tweet" placehoder="What's happening today?">
</div>
```
In the HTML you have an input tag, which has the v-model directive attached to it as an HTML attribute. Anything between quotes is computed as a JavaScript expression, so you write the name of a property `tweet` that you will create inside the Vue data object.

So let's do it.

```js
let app = new Vue({
    el: '#app',
    data: {
        tweet: ""
    }
});
```
So now you have a Vue instance and, in it, you have a data object with a tweet property that has an empty string as its value. 

If you open the console and inspect the Vue element, you can see the two-way data binding in action. 

By changing the value of the tweet property, you will immediately update the value inside the input tag and vice-versa. 

You have this `tweet` property in the data object and you already know how to render its content onto the page. So now you can update your markup and add a paragraph under the input tag to see the value dynamically changing while you type.

```html
<div id="app">
    <h2>What do you want to tweet about today?</h2>
    <input type="text" v-model="tweet" placehoder="What's happening today?">
    <p>{{tweet}}<p>
</div>
```
How cool is that? Now you can see the tweet property changing in real-time as you type. 

That's the two-way data binding. If you change the content of the tweet property directly it will be reflected in your template, too.

If you want to learn more, make sure to read the official [Documentation](https://vuejs.org/v2/guide/forms.html) too.

### How to build a tweet box 
Now, let's raise the bar a little and build something together.

- We will create a simple `textarea` with a submit button, 
- We will display the number of characters the user has left while they are typing so that they can submit the form without exceeding the max number of characters allowed. 
- Like in a tweet, the maximum number of characters will be 200.

#### How to define the initial markup
Now you need to define a markup. So inside our index.html file, write the following code:
```html
<div id="app">
    <h2>What do you want to tweet about today?</h2>
    <form v-on:submit.prevent="submitData">
       <!-- Code here -->

    </form>
    <!-- More code here -->
</div>
```
First you have first created your root element for the Vue instance so that it can monitor the markup and do its magic.

Then you created a form tag with an event listener using the directive v-on, which listens for the submit event and runs a function `submitData` that you still have to create.

You also added the `.prevent` modifier so that the page doesn't refresh when you submit the form.

#### How to define the Vue instance and methods
Let's define our Vue instance and create the `submitData` method so that you can use it later when you need it.
```js

let app = new Vue({
    el: '#app',
    data: {
        // data object props here
    },
    
    methods: {
          submitData(){
             // Code here
        }
    },

});
```

#### How to add a text area and a submit button
Now back to the HTML: let's add the text area inside your form. 

```html
<div id="app">
    <h2>What do you want to tweet about today?</h2>
    <form v-on:submit.prevent="submitData">
       <!-- Code here -->
        <div class="form_group">
            <label for="name">Tweet</label>
            <textarea name="tweet" id="tweet" cols="80" rows="10" v-model="tweet" maxlength="200"></textarea>
            
        </div>

        <button type="submit">Tweet</button>

    </form>
    <!-- More code here -->
</div>

```
Inside the form tag, you create a label and a `textarea` for your tweet box. 
On the `textarea` you use the directive v-model to bind the `textarea` value to a `tweet` property and vice-versa. So now when one changes the other changes, too. 

NOTE: The v-model directive is used on form elements like inputs, text areas, check box, and more.

After the `textarea` you put a button of type submit so that when a user clicks it the form's data are sent to your application's `submitData()` method and you can process them.

#### How to add properties to the Vue instance
Now inside your JavaScript file, you need to create the tweet property in the data object and do something with this information so that you can later show a list of tweets sent. 

We also said that we want to limit the characters to 200 and show an error when they're in excess.

So let's add a few more properties here like:
- `tweet` for the current tweet message that the user inputs in the text area
- `tweets` for the list of tweets
- `max_length` for the characters limit

```js

let app = new Vue({
    el: '#app',
    data: {
        tweets: [],
        tweet: "",
        max_length: 200,  
    },
    
    methods: {
          submitData(){
              /* Handle the tweet */
        }
    },

});
```

So now with the tweets property as an array and using the two-day binding between the tweet property and the `textarea`, you can push all tweets inside the `tweets` array when the user submits the form by triggering the 
`submitData` method.

#### How to implement the character counter
Before implementing the `submitData` method, you can show a character counter while the user types in the textarea. 

Let's implement this feature so the user knows if they can submit the tweet or not.

Back in the HTML file, you can add a div with a couple of span elements and use a v-if directive to check the length of the character. It'll show the counter while the user is within the characters limit, otherwise it'll show an error message.

```html
<div id="app">
    <h2>What do you want to tweet about today?</h2>
    <form v-on:submit.prevent="submitData">
        <div class="form_group">
            <label for="name">Tweet</label>
            <textarea name="tweet" id="tweet" cols="80" rows="10" v-model="tweet"></textarea>        
        </div>

        <button type="submit">Tweet</button>

    </form>
    <!-- Show character limits here -->
    <div>
        <span v-if="tweet.length < max_length"> {{ `Max: ${tweet.length} of ${max_length} characters` }}
        </span>
        <span class="errorMessage" v-else>{{`Max char limit reached! excess chars: ${max_length - tweet.length}`}}</span>
    </div>
    
</div>

```
The code above uses two-way data binding between the tweet property and the `textarea` to find out if the user has reached the character limit that you defined as the `max_lenght` property. 

Since the tweet property is connected to the `textarea`, you can use the `v-if` directive combined with the `tweet.length` and the `max_length` properties to make the comparison. 

Now, every time the user types something in the `textarea`, the string saved in the `tweet` property increases by one character. Then you can use the `.length` property to see how long the whole string is and compare it against your `max_length` property.

You use the directive  `v-if="tweet.length <= max_length"` to make your comparison. When this comparison returns true, the user will see the span tag with its content, the counter. 

Inside the span tag, you used the moustache syntax to show the user the current length of the property `tweet` and the character limit.

```html
<span v-if="tweet.length < max_length"> {{ `Max: ${tweet.length} of ${max_length} characters` }}</span>
```

After the `v-if` directive, a `v-else` directive handles the error message that you show to the user when there are no characters left to use. 

Here the content of the span element shows a message that tells how many characters there are in excess by subtracting the tweet length from the `max_lenght` property.

```html
<span class="errorMessage" v-else>{{`Max char limit reached! excess chars: ${max_length - tweet.length}`}}</span>
```

#### How to submit the form
All that's left is to add the tweet to the list of tweets and show them on the page when the user submits the form.

Let's complete the `submitData` method so that every time it's executed it pushes a new object to the tweets array. 

Inside the methods object the `submitData` methods now looks like this:
```js
 submitData(){
    if (this.tweet.length <= this.max_length) {
        this.tweets.unshift(this.tweet);
        this.tweet = "";
    } 
}

```
The method above first checks if the length of the `tweet` property is less than or equal to the `max_length` property. If the condition evaluates to true, then you can add the `tweet` content to the array using the `unshift` method (which adds it to the beginning of the array).

Finally, you need to clear the value of the `tweet` property. You can do this by assigning to it an empty string again.

NOTE that since you are inside a method, you need to use the `this` keyword to grab properties and eventually methods inside the Vue instance.

#### How to show a list of tweets
Now, you can also show a list of tweets in your template. 

To do that you will use a `v-for` directive and loop over the `tweets` array to show each tweet.

```html
<ul>
    <li v-for="text in tweets">{{text}}</li>
</ul>

```

### Put it all together
The final code now looks like this:

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VueJs v-model</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <!-- Fontawesome CDN -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <!-- VueJS CDN -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12/dist/vue.js"></script>
    <style>

    </style>
</head>

<body>
    <div id="app" class="container">

        <h2>What do you wanna tweet about today</h2>

        <!-- Tweet form -->
        <form v-on:submit.prevent="submitData">

            <div class="form-group">
                <label>Tweet</label>
                <textarea class="form-control" cols="30" rows="5" v-model="tweet"></textarea>
            </div>

            <button type="submit" class="btn btn-primary">Tweet</button>
        </form>

        <!-- Alert the user  -->
        <div class="my-3">
            <span v-if="tweet.length < max_length">
                {{ ` Max: ${tweet.length} of ${max_length} characters` }}
            </span>
            <span class="alert alert-danger" v-else> {{ `Max char limit reached! excess characters: ${max_length -
                tweet.length} ` }}</span>

        </div>

        <!-- Tweets message -->
        <ul>

            <li v-for="tweet in tweets">
                {{tweet}}
            </li>
        </ul>

    </div>

    <script src="./main.js"></script>

</body>

</html>

```
Our final javascript file 

```js 

let app = new Vue({
    el: '#app',
    data: {
        tweet: "",
        tweets: [],
        max_length: 200        
    }, 
    methods: {
        submitData(){
            // Handle the tweet submission
            if(this.tweet.length <= this.max_length){
                this.tweets.unshift(this.tweet);
                this.tweet = "";
            }
        }
    }
})


```

### Improvements you can make

If you take this bit of code from your index.html file, there is something you can do to clean up our code... 

```html
<!-- Show the max char messages -->
<div>
    <span v-if="tweet.length < max_length"> {{ `Max: ${tweet.length} of ${max_length} characters` }}
    </span>
    <span class="errorMessage" v-else>{{`Max char limit reached! excess chars: ${max_length - tweet.length}`}}</span>

</div>
```
To clean this template file, we can follow two approaches that are exactly the same, except that one is cached and the other one isn't. 
- Computed Properties (cached)
- Methods (not cached)

In the next section, we will learn what computed properties are and how they differ from methods.


%[https://youtu.be/pBUXTUvDRCo]




## Computed Properties and methods

You should use computed properties instead of in-template expressions for complex logic that has the scope of changing the presentation of our data, not the data itself. 

If we need to change the data, then you should use methods instead. Computed properties are cached based on their dependencies, meaning that it will re-evaluate only when its dependencies have changed. 

With computed properties, the result of the previously run function is returned if the dependencies have not changed. 

You can view the [repository here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/10-computed-properties/) and watch the video on [YouTube here](https://youtu.be/VxFT6cgTHhw). The video is also listed at the end of this section so you can review what you've learned.

In the following example, we will use computed properties but we could also use methods. Generally speaking, we use computed properties when we have an expensive operation that we want to execute and cache so that the next time we don't have to run it again unless something has changed.  

Let's implement a computed property for the following messages. Our HTML file will now change from this:

```html
<!-- Show the max char messages -->
<div>
    <span v-if="tweet.length < max_length"> {{ `Max: ${tweet.length} of ${max_length} characters` }}
    </span>
    <span class="errorMessage" v-else>{{`Max char limit reached! excess chars: ${max_length - tweet.length}`}}</span>

</div>

```

to this much cleaner version:

```html
<!-- Show the max char messages -->
<div>
    <span v-if="tweet.length < max_length"> {{ maxCharsText }}
    </span>
    <span class="errorMessage" v-else>{{errorMessage}}</span>
    
</div>

```
We have replaced the contents of both spans with two new properties that will be placed as methods inside our computed object.

Now inside our Vue instance, we will create a new object called `computed` where we will define two methods that will return the messages we had before. 

```js
let app = new Vue({
    el: '#app',
    data: {
        tweets: [],
        tweet: "",
        max_length: 200,  
        error: ""
    },
    // Computed Properties
 computed: {
        maxCharsText: function(){
            return `Max: ${this.tweet.length} of ${this.max_length} characters`;
        },
        errorMessage: function(){
            return `Max char limit reached! excess chars: ${this.max_length - this.tweet.length}`
        }
    },
    // Methods
 methods: {
          submitData(){
              if (this.tweet.length <= this.max_length) {
                  this.tweets.unshift(this.tweet);
                  this.tweet = "";
              } 
        }
    },

});

```
The first method `maxCharsText` returns exactly the same string we had before inside our HTML file. The only difference is that we are using the keyword `this` to reference the properties we needed to grab inside the Vue instance `this.tweet.length` and `this.max_length`. 

The second method works in the exact same way and it also uses the keyword `this` to pick the properties defined in the Vue instance `this.max_length` and `this.tweet.length`.


### All together
```html
<div id="app">
    <h2>What do you want to tweet about today?</h2>
    <form v-on:submit.prevent="submitData">
        <div class="form_group">
            <label for="name">Tweet</label>
            <textarea name="tweet" id="tweet" cols="80" rows="10" v-model="tweet"></textarea>

        </div>

        <button type="submit">Next</button>

    </form>

    <div>
        <span v-if="tweet.length < max_length"> {{ maxCharsText }}
        </span>
        <span class="errorMessage" v-else>{{errorMessage}}</span>
       
    </div>
    <ul>
        <li v-for="text in tweets">{{text}}</li>
    </ul>
</div>

```
JavaScript file

```js
let app = new Vue({
    el: '#app',
    data: {
        tweets: [],
        tweet: "",
        max_length: 200,  
        error: ""
    },
    // Computed Properties
 computed: {
        maxCharsText: function(){
            return `Max: ${this.tweet.length} of ${this.max_length} characters`;
        },
        errorMessage: function(){
            return `Max char limit reached! excess chars: ${this.max_length - this.tweet.length}`
        }
    },
    // Methods
 methods: {
          submitData(){
              if (this.tweet.length <= this.max_length) {
                  this.tweets.unshift(this.tweet);
                  this.tweet = "";
              } 
        }
    },

});


```


If we want to use methods instead of computed properties, we can simply move both methods from the `computed` object inside the `methods` object and invoke them with parenthesis inside our HTML file like so:

```html
<div>
    <span v-if="tweet.length < max_length"> {{ maxCharsText() }}
    </span>
    <span class="errorMessage" v-else>{{errorMessage() }}</span>
    
</div>

```
Just remember that computed properties are cached while methods are not. 
If you want to learn more make sure to read the official [documentation](https://vuejs.org/v2/guide/computed.html).

%[https://youtu.be/VxFT6cgTHhw]

## How to Create a Simple Twitter Clone

Now, let's put together everything we've learned so far and and build our very first project. It will be a minimalist and simplified twitter-like web application. 

We want to create a simple application that has some kind of registration form, a box to add new tweets, and a section where we can show all tweets. We also want to be able to remove tweets.

All data must be persistent so that after the page is refreshed the list of tweets is still visible while the registration form will be hidden.

You can watch the video on [YouTube here](https://youtu.be/v1j_bDDd6jI) or at the end of this section if you want to review.

You can also view the repository [here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/11-project-simple-twitter-cone/).

### Define our tasks
Let's break this down into large tasks first. Then we will see what we need to do to complete each one. 
- create a registration form
- create a tweets box form
- create a tweets section

To do our project we need to research what tools we need to use to achieve our goals, so lets put them down:
- VueJS (application logic)
- localStorage (make data persistent)
- font awesome (icons)

This application has no database so we are unable to record multiple users and their tweets. It's just a proof of concept, something we build to use our new knowledge.

### Create the project structure
Now that we know what to do, let's start by creating our project structure and importing the tools we need to complete the first task, the registration form.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple tweetter clone</title>
    <!-- CDN Fontawesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />
    
    <!-- VueJS development version, includes helpful console warnings -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <!-- Style sheet -->
    <link rel="stylesheet" href="style.css">
</head>

<body>
<div id="app">
    <!-- Register an account -->

    <!-- Add a tweet -->

    <!-- Show all tweets -->
    
</div>
<!-- Link our main.js file -->
<script src="./main.js"></script>
</body>

</html>

```

Now that our HTML file is ready, let's create the main.js file and create a Vue instance.

```js

let app = new Vue({
    el: '#app',
    data: {
        
    },
    methods: {
          
    }

});

```

Finally, we need to create a style.css file that we will place for now in the root folder of our project. 

We will use a CSS file that I have already written, and you can download it from [here](https://bitbucket.org/fbhood/simple-tweet-app/src/master/style.css).

OK, our basic structure is ready to go. Inside our HTML file, we have some comments that reflect our 3 main tasks: create a registration form, create an add tweet box and, show a list of tweets. 

Let's start with the first task and simulate a registration form.

### How to simulate a registration form - HTML

Inside the root element `<div id="app"></div>` we need to create a registration form with the following fields: name, email, password, and a submit button. The form is contained in a card so we will wrap everything in a div and assign to it a card class. 

The form won't submit data to a server, but will simply simulate a registration and update some property in the data object of the Vue instance.

We will place the following code inside our HTML file:
```html
<!-- Register an account -->
<div class="card">
    <i class="fab fa-twitter fa-lg fa-fw"></i>
        
    <h2>Create your account</h2>
    <form v-on:submit.prevent="registerAccount">
        <div class="form_group">
            <label for="name">Name</label>
            <input type="text" v-model="name" maxlength="25" required>
        </div>
        <div class="form_group">
            <label for="email">Email</label>
            <input type="email" v-model="email" maxlength="25" required>
        </div>
        <div class="form_group">
            <label for="password">Password</label>
            <input type="password" v-model="password" maxlength="16" required>
        </div>
        <button type="submit">Register</button>
    </form>

</div>
```
Let's break this down. First, the form tag has a `v-on` directive with a `submit` argument so it will listen for a submit event. It also has an event modifier `.prevent` so when we hit the submit button the page doesn't refresh. 

Inside the `v-on` directive there is a method called `registerAccount` that we need to create inside the methods of the Vue instance.

Inside the form, we have the three input fields: name, email, and password with labels. We wrapped each field inside a div with a class of `form_group`. Later we can replicate the style of the Twitter registration fields and show a character counter. 

Each input field has a `v-model` directive that binds the input to its data property. 

### How to simulate a registration form - Vue
Let's move on to the Vue instance to make the binding between the form and the data object properties.

Here we also need a place where we can store the details that the user submits so we will create another property for that. 

Looking at the input fields, we also put a `maxlength` property on them, which is 25 for the name and email and 16 for the password. 

Like we did previously when we learned about the v-model, we can create a property for these limits so that we can use it to show the user how many characters the user has left. 

The Vue instance will look like this:

```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {}
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16
    },
    methods: {
        registerAccount(){
            // record user details
            // add registration to localStorage
            // clear the registration fields

        }
    }

});

```
Let's break this down. First inside the `data:{}` object, we defined an object to store and retrieve the `userData`. Then we added the properties `name`, `email`, and `password` to make the two-way data binding work. 
Finally we added the `max_length` and `max_pass_length` propeties.

### How to show input character counter 
OK, now that we have a binding between the input fields and our properties, we can show a character counter to the user while they're typing. 

This is fairly simple – all there is to do is to show the length of each input property and compare it with the max length properties we have set in the Vue instance.

```html
<div class="form_group">
    <label for="name">Name
        <span> {{ name.length + '/' + max_length }}</span>
    </label>
    <input type="text" v-model="name" :maxlength="max_length" required>
</div>

```
So here we created a string using an in-template expression. We've shown the length of the `name` property and the value of the `max_length` so that while the user types we show something like this: 13/25. 

We've also used a `v-bind` directive on the `maxlength` attribute so that its value is bound to the value of the property we defined in the Vue instance. So in case we want to change it we can do so in one place.

We will do the same for the other fields. 

```html
<form id="register" v-on:submit.prevent="registerAccount">
    <div class="form_group">
        <label for="name">Name
            <span> {{ name.length + '/' + max_length }}</span>
        </label>
        <input type="text" v-model="name" :maxlength="max_length" required>
    </div>
    <div class="form_group">
        <label for="email">Email
            <span> {{ email.length + '/' + max_length }}</span>
        </label>
        <input type="email" v-model="email" :maxlength="max_length" required>
    </div>
    <div class="form_group">
        <label for="password">Password
            <span> {{ password.length + '/' + max_pass_length }}</span>
        </label>
        <input type="password" v-model="password" :maxlength="max_pass_length" required>
    </div>
    <button type="submit">Register</button>

</form>

```

### How to add the logic to the `registerAccount` method
Now it's time to work on the form submission logic. We will simply populate the object stored in the property `userData` when the user submits the form. 

Inside the `registerAccount` method we will add the details the user passes and build our object. 

```js
 registerAccount(){
            // record user details
            this.userData.name = this.name,
            this.userData.email = this.email,
            this.userData.password = this.password
            
            // add registration to localStorage

            // clear the registration fields
            this.name = "";
            this.email = "";
            this.password = "";
        }

```
Here we have taken the value of the properties name, email, and password and assigned them to properties we created in the `userData` object.

This seems fine mostly because we have put on our input fields the `required` attribute – but if we remove it we will be able to submit an empty form, and we don't want that. 

So let's add a very basic form of validation to at least check if the user has typed something inside our form, otherwise we show an error. 

To do this, we need to add an if block inside the method and also an error property to the data object. Our file now looks like this:

```js


let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        error: "",
      
    },  
    methods: {
        registerAccount(){
            if (this.name !== "" && this.email !== "" && this.password !== "" ) 
            {
                this.userData.id = ++this.usersID,
                this.userData.name = this.name,
                this.userData.email = this.email,
                this.userData.password = this.password
                 
            } else {
                this.error = "Complete all the form fields"
            }
        
        /* Add registration data to the local storage */

        
        /* Clear the registration inputs */
        this.name = "";
        this.email = "";
        this.password = "";
        }

    }
    
});

```
Here in the `registerAccount` we've written a conditional that checks if the length of the name property is not empty, if the email property isn't empty, and if the password isn't empty  `this.name !== "" && this.email !== "" && this.password !== ""`. 

If all these checks evaluate to a true value, then we run the code inside the block. Otherwise we run the code in the `else` block that updates the value of the `error` property that we will now use in our template to show the error message. 

We also added a new property `usersID: 0,` that we used inside the if block to assign an id property to the `userData` object, just to make our application more realistic. But of course it is useless, as we will not have a database where we store all user details. We'll just store a single user inside their browser's local storage.

```html
<form id="register" v-on:submit.prevent="registerAccount">
    <div class="form_group">
        <label for="name">Name
            <span> {{ name.length + '/' + max_length }}</span>
        </label>
        <input type="text" v-model="name" :maxlength="max_length" required>
    </div>
    <div class="form_group">
        <label for="email">Email
            <span> {{ email.length + '/' + max_length }}</span>
        </label>
        <input type="email" v-model="email" :maxlength="max_length" required>
    </div>
    <div class="form_group">
        <label for="password">Password
            <span> {{ password.length + '/' + max_pass_length }}</span>
        </label>
        <input type="password" v-model="password" :maxlength="max_pass_length" required>
    </div>
    <button type="submit">Register</button>
</form>


<div v-if="error.length > 0"> {{error}}</div>
```
Now our form is complete and we're also displaying an error message to the user if the required attributes are removed from our markup. 

But our data do not persist and when the page is refreshed –everything's all gone. Let's tackle that using the localStorage API.

Inside our Vue instance, we need to set an item in the local storage. But we also need to save the entire `userData` object so that later we can use its data to display a message to the registered user.

```js
/* Add registration data to the local storage */
localStorage.setItem('simple_tweet_registered', true)
/* Add the whole userData object as JSON string */
localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))

```
Here we use the `setItem` method of the Local Storage API to add an item to the local storage so that later we can use it to check if the user is registered or not. 

Then we also need to store the entire `userData` object as a string. To do that we use the `JSON.stringify` method that will turn the object into a JSON string that can be saved in the localStorage.

Our JS file is now as follows:
```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        error: "",
    },  
    methods: {
        registerAccount(){
            if (this.name !== ""  && this.email !== "" && this.password !== "" ) {
                this.userData.id = ++this.usersID,
                this.userData.name = this.name,
                this.userData.email = this.email,
                this.userData.password = this.password
                 
            } else {
                this.error = "Complete all the form fields"
            }
        
        /* Add registration data to the local storage */
        localStorage.setItem('simple_tweet_registered', true)
        /* Add the whole userData object as JSON string */
        localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))

        
        /* Clear the registration inputs */
        this.name = "";
        this.email = "";
        this.password = "";
        }

    }
    
});

```

Now when the user visits our application page, we need to check inside the browser's local storage to see if there is a key called `simple_tweet_registered`. If there is, we can assume that the user is registered and we can show the next section, the tweet box. Otherwise, we show the registration form. 

We will do that by creating a `registered: false` property in the data object and use it to display or hide the registration form.

```js

data: {
    userData: {},
    usersID: 0,
    name: "",
    email: "",
    password: "",
    max_length: 25,
    max_pass_length: 16,
    error: "",
    registered: false,      
}

```
Wrap the form around a div with a directive `v-if="!registered"` like this:

```html
<div class="register" v-if="!registered">
    // here goes the form
</div>

<div v-else> Tweetbox </div>
```

Our final HTML file now looks like this:

```html
    <div class="card">
        <i class="fab fa-twitter fa-lg fa-fw"></i>
        <!-- Register an account -->
        <div class="register" v-if="!registered">
            <button form="register" type="submit">Register</button>
            <h2>Create your account</h2>
            <form id="register" v-on:submit.prevent="registerAccount">
                <div class="form_group">
                    <label for="name">Name
                        <span> {{ name.length + '/' + max_length }}</span>
                    </label>
                    <input type="text" v-model="name" :maxlength="max_length" required>
                </div>
                <div class="form_group">
                    <label for="email">Email
                        <span> {{ email.length + '/' + max_length }}</span>
                    </label>
                    <input type="email" v-model="email" :maxlength="max_length" required>
                </div>
                <div class="form_group">
                    <label for="password">Password
                        <span> {{ password.length + '/' + max_pass_length }}</span>
                    </label>
                    <input type="password" v-model="password" :maxlength="max_pass_length" required>
                </div>
            </form>


            <div v-if="error.length > 0"> {{error}}</div>
        </div>
        <!-- Add tweet -->
        <div class="tweetBox" v-else>
            <h2>Welcome username_here write your first Tweet</h2>
        </div>

    </div>

```

Now to make this work, we will use the lifecycle hook we created which lets us inject our code when the Vue instance has been created. This is because we want to check this before mounting our root element. 

So let's add a life cycle hook to the Vue instance. We will check if our key is there, and if so we will update the value of the `registered` property to `true`. 

We have also stored the full `userData` object in the local Storage so we can use it to repopulate the `userData` object when the page is refreshed with the details the user submitted.

```js
created(){
    /* Check if the user is registered and set the registered to true */
    if(localStorage.getItem("simple_tweet_registered") === 'true'){
        this.registered = true;
    }
    // repopulate the userData object
     if(localStorage.getItem('simple_tweet_registered_user')) {
            this.userData = JSON.parse(localStorage.getItem('simple_tweet_registered_user'))
        }

}

```
To turn a JSON string back into an object, we can use the `JSON.parse` method.

Now it's all set for the next task – show a tweet form to the user after registration.

Our code so far looks like this:

The main.js file:
```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        error: "",
        registered: false,
    },
    
    methods: {
          registerAccount(){
      
              if (this.name.length > 0 && this.name.length <= this.max_length && this.email !== "" && this.password !== "" ) {
                  
                    this.userData.id = ++this.usersID,
                    this.userData.name = this.name,
                    this.userData.email = this.email,
                    this.userData.password = this.password
                    this.registered=true;
                
                  
                 
              } else {
                  this.error = "Complete all the form fields"
              }
            
            /* Add registration data to the local storage */
            localStorage.setItem('simple_tweet_registered', true)
            /* Add the whole userData object as JSON string */
            localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))
            
            /* Clear the registration inputs */
            this.name = "";
            this.email = "";
            this.password = "";
        }
        
    },
    created(){
        /* Check if the user is registered and set the registered to true */
        if(localStorage.getItem("simple_tweet_registered") === 'true'){
            this.registered = true;
        }
        // repopulate the userData object
        if(localStorage.getItem('simple_tweet_registered_user')) {
            this.userData = JSON.parse(localStorage.getItem('simple_tweet_registered_user'))
        }
       
    }

});

```
And the HTML inside the `app` element:

```html
<div class="card">
    <i class="fab fa-twitter fa-lg fa-fw"></i>
    <!-- Register an account -->
    <div class="register" v-if="!registered">
        <button form="register" type="submit">Register</button>
        <h2>Create your account</h2>
        <form id="register" v-on:submit.prevent="registerAccount">
            <div class="form_group">
                <label for="name">Name
                    <span> {{ name.length + '/' + max_length }}</span>
                </label>
                <input type="text" v-model="name" :maxlength="max_length" required>
            </div>
            <div class="form_group">
                <label for="email">Email
                    <span> {{ email.length + '/' + max_length }}</span>
                </label>
                <input type="email" v-model="email" :maxlength="max_length" required>
            </div>
            <div class="form_group">
                <label for="password">Password
                    <span> {{ password.length + '/' + max_pass_length }}</span>
                </label>
                <input type="password" v-model="password" :maxlength="max_pass_length" required>
            </div>
        </form>


        <div v-if="error.length > 0"> {{error}}</div>
    </div>
    <!-- Add tweet -->
    <div class="tweetBox" v-else>
        <h2>Welcome {{ userData.name }} write your first Tweet</h2>

    </div>

</div>

```
Here in the HTML, since we used the `v-else` on the add tweet section and used the local storage to retrieve the data submitted by the user, we can use an in-template expression to grab the user name so that we can output a welcome message. 

In the next section, we will create a tweet box form so that after the registration the user can write a tweet.

%[https://youtu.be/v1j_bDDd6jI]

### How to create a tweet box form - HTML

Now it's time to build our add tweet form. We did something very similar earlier in this article, but now we will need to store and make the data persistent. This lets us show a list of tweets even when the page refreshes.

```html
<div class="tweetBox" v-else>
    <h2>Welcome {{ userData.name }} write your first Tweet</h2>
    <form v-on:submit.prevent="sendTweet">
        <div class="form_group">
            <label for="tweet">
                Send your tweet
                <span> {{ tweetMsg.length + '/' + max_tweet }}</span>
            </label>
            <textarea name="tweet" id="tweet" cols="30" rows="10" v-model="tweetMsg" maxlength="200"></textarea>
        </div>
        <button type="submit">Tweet</button>
    </form>

</div>
```
This is nothing new to us now. Inside the `tweetBox` element we add a form with the usual v-on directive and a method  `sendTweet` that we will need to define inside the methods object. This will take the tweet and save it somewhere, maybe in a property in the data object.

Inside the form, there is a `textarea` that has a `v-model` directive that binds it to a `tweetMsg` property that we need to create.

Finally, a submit button.

We also have a span inside the tweet label that shows a character counter to the user as we did before in the registration form. 

Here we have a new property `max_tweet` that is used to show the limit and the `tweetMsg.length` is used to show the current number of the characters inserted.

You can watch the video on [YouTube here](https://youtu.be/xFwfrIciFt0) if you want to review what you've learned.

### Create a tweets box form - Vue
Let's go to the Vue instance and add the properties and the `sendTweet` methods.

Our data object now has three more properties, the `max_tweet` set to `200`, the `tweetMsg` that binds to the `textarea`, and a `tweets` array that we will use to store all tweets the user sends.
```js
data: {
    userData: {},
    usersID: 0,
    name: "",
    email: "",
    password: "",
    max_length: 25,
    max_pass_length: 16,
    max_tweet: 200, // max tweets lenght
    error: "",
    registered: false,
    tweetMsg: "", // current tweet
    tweets: [] // list of tweets
}

```
Inside the methods, we have a new method that will be invoked by the v-on directive when the form is submitted:

```js

sendTweet(){
    /* Store the tweet in the tweets property */
    this.tweets.unshift(
        {
            text: this.tweetMsg,
            date: new Date().toLocaleTimeString()
        }

    );
    /* Empty the tweetMsg property */
    this.tweetMsg = "";
    //console.log(this.tweets);

    /* Tranform the object into a string  */
    stringTweets = JSON.stringify(this.tweets)
    //console.log(stringTweets);

    /* Add to the local storage the stringified tweet object */
    localStorage.setItem('simple_tweet_tweets', stringTweets)
},

```

The code above does four things:

- takes the tweets array and adds in it an object to represent a single tweet with text and date properties. To the text property, we assign the value of the `tweetMsg` that is bound with the `textarea`. For the date, we create a new date object with the `new Date().toLocaleTimeString()` method.
- we empty the value of the `tweetMsg`
- we transform the tweets property into a string using the method `JSON.stringify(this.tweets)` 
- Then we add it to the local storage.

Our final main.js file now looks like this:

```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        error: "",
        registered: false,
    },
    
    methods: {
          registerAccount(){
      
              if (this.name.length > 0 && this.name.length <= this.max_length && this.email !== "" && this.password !== "" ) {
                  
                    this.userData.id = ++this.usersID,
                    this.userData.name = this.name,
                    this.userData.email = this.email,
                    this.userData.password = this.password
                    this.registered=true;
                
                  
                 
              } else {
                  this.error = "Complete all the form fields"
              }
            
            /* Add registration data to the local storage */
            localStorage.setItem('simple_tweet_registered', true)
            /* Add the whole userData object as JSON string */
            localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))
            
            /* Clear the registration inputs */
            this.name = "";
            this.email = "";
            this.password = "";
        },
        sendTweet(){
            /* Store the tweet in the tweets property */
            this.tweets.unshift(
                {
                    text: this.tweetMsg,
                    date: new Date().toLocaleTimeString()
                }

            );
            /* Empty the tweetMsg property */
            this.tweetMsg = "";
            //console.log(this.tweets);

            /* Tranform the object into a string  */
            stringTweets = JSON.stringify(this.tweets)
            //console.log(stringTweets);

            /* Add to the local storage the stringified tweet object */
            localStorage.setItem('simple_tweet_tweets', stringTweets)
        },

        
    },
    created(){
        /* Check if the user is registered and set the registered to true */
        if(localStorage.getItem("simple_tweet_registered") === 'true'){
            this.registered = true;
        }
        // repopulate the userData object
        if(localStorage.getItem('simple_tweet_registered_user')) {
            this.userData = JSON.parse(localStorage.getItem('simple_tweet_registered_user'))
        }
       
    }

});

```
Now that we've completed this part, we can show a list of tweets and also handle when the page is refreshed, and the local storage has in it our tweets object. We will need to parse it back and add its content to the `tweets` property to see the list.

Next, we will learn how to show the list of tweets using a v-for directive.

%[https://youtu.be/xFwfrIciFt0]

### How to show a list of tweets - HTML

Inside our root element, add the following code:

```html
 <!-- Show all tweets -->
    <div class="card_tweets">
        <section class="tweets" v-if="tweets.length > 0">
            <h2>Tweets</h2>
            <div class="tweetMsg" v-for="(tweet, index) in tweets">
                <p>
                    {{tweet.text}}
                </p>

                <div class="tweetDate">
                    <i class="fas fa-calendar-alt fa-sm fa-fw"></i>{{tweet.date}}
                </div>
 
            </div>

        </section>
        <div v-else>No tweets to show</div>
    </div>
```

Here we wrap everything in a div with a class `card_tweets`. Then we use a v-if directive inside a child section to check if there are tweets in the `tweets` array `v-if="tweets.length > 0"`. 

Inside this section, we can loop over the tweets array using a `v-for="(tweet, index) in tweets"` directive. After that we use in-template expressions to show the tweet text property `{{tweet.text}}` and the data `{{tweet.date}}`.

After the `section` we can use a `v-else` directive to show a message in case there are no tweets stored inside the tweets array `<div v-else>No tweets to show</div>`. Done. 

Now there's one last thing we need to do, and that is to figure out what to do to remove tweets from the list.

But when the user refreshes the page, everything is gone. So we need to work with the `localStorage` once again to repopulate our tweets array from it before rendering the root element.

Inside the `created` lifecycle hook we will now write some code to parse the tweets and save them back in the `tweets` property:

```js
/* Parse all tweets from the local storage  */
if(localStorage.getItem("simple_tweet_tweets")) {
    console.log("There is a list of tweets");
    this.tweets = JSON.parse(localStorage.getItem('simple_tweet_tweets'))
}else {
    console.log("No tweets here");
}

```

Here we used the `localStorage` API to first check if there was a key called `simple_tweet_tweets`. If so, we grab the tweets property using `this.tweets` and assign to it the content of the `localStorage`. But we parse the string back to `JSON` with `JSON.parse` so we write `this.tweets = JSON.parse(localStorage.getItem('simple_tweet_tweets'))`.

Now everything works. After we refresh the page, the tweets are still there. Let's move on. In the next step, we will add a method to remove tweets from the list.

You can watch the video on [YouTube here](https://youtu.be/3DzBkUHH3bU) or at the end of this section to review what you've learned.

### How to remove tweets
Inside the div that contains the tweet message, we can add another div to show a link and a trash icon. This lets the user click it and remove that tweet. 

```html
<div class="tweet_remove" @click="removeTweet(index)">
    <span class="remove">Delete this tweet <i class="fas fa-trash fa-xs fa-fw"></i></span>
</div>

```
Here we simply used a v-on short syntax directive on the div and invoked a method `removeTweet(index)`, passing to the method the element index so that we know what to remove.

Let's build our `removeTweet` method now:

```js
removeTweet(index){
    let removeIt = confirm("Are you sure you want to remove this tweet?")
    if(removeIt) {
        this.tweets.splice(index, 1);
        /* Remove the item also from the local storage */
        localStorage.simple_tweet_tweets = JSON.stringify(this.tweets)
    }
}

```
This bit of code is pretty straightforward. Our method accepts an index that represents the position of the tweet object in the array obtained from the v-for directive when the method is invoked. 

We then create a variable to ask the user to confirm that they want to delete the tweet. We used the `confirm` function for that. 

If the value of the `removeIt` variable is true, then we execute the code and use `this.tweets.splice(index, 1)` to remove the tweet from the array using its index. 

Finally we update the `localStorage` value by assigning to is the new array using the `localStorage.simple_tweet_tweets = JSON.stringify(this.tweets)`.

### Final Code
Our code is now complete. You can find the final code below or inside the repository here: [https://bitbucket.org/fbhood/simple-tweet-app/src/master/].

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vue 2 Hello World</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <!-- Axios CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.0/axios.min.js"
        integrity="sha512-DZqqY3PiOvTP9HkjIWgjO6ouCbq+dxqWoJZ/Q+zPYNHmlnI2dQnbJ5bxAHpAMw+LXRm4D72EIRXzvcHQtE8/VQ=="
        crossorigin="anonymous"></script>
    <!-- development version, includes helpful console warnings -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
</head>

<body>
<div id="app">
    <div class="card">
        <i class="fab fa-twitter fa-lg fa-fw"></i>
        <!-- Register an account -->
        <div class="register" v-if="!registered">
            <button form="register" type="submit">Register</button>
            <h2>Create your account</h2>
            <form id="register" v-on:submit.prevent="registerAccount">
                <div class="form_group">
                    <label for="name">Name
                        <span> {{ name.length + '/' + max_length }}</span>
                    </label>
                    <input type="text" v-model="name" :maxlength="max_length" required>
                </div>
                <div class="form_group">
                    <label for="email">Email
                        <span> {{ email.length + '/' + max_length }}</span>
                    </label>
                    <input type="email" v-model="email" :maxlength="max_length" required>
                </div>
                <div class="form_group">
                    <label for="password">Password
                        <span> {{ password.length + '/' + max_pass_length }}</span>
                    </label>
                    <input type="password" v-model="password" :maxlength="max_pass_length" required>
                </div>
            </form>


            <div v-if="error.length > 0"> {{error}}</div>
        </div>
        <!-- Add tweet -->
        <div class="tweetBox" v-else>
            <h2>Welcome {{ userData.name }} write your first Tweet</h2>
            <form v-on:submit.prevent="sendTweet">
                <div class="form_group">
                    <label for="tweet">
                        Send your tweet
                        <span> {{ tweetMsg.length + '/' + max_tweet }}</span>
                    </label>
                    <textarea name="tweet" id="tweet" cols="30" rows="10" v-model="tweetMsg" maxlength="200"></textarea>
                </div>
                <button type="submit">Tweet</button>
            </form>

        </div>

    </div>
    <!-- Show all tweets -->
    <div class="card_tweets">
        <section class="tweets" v-if="tweets.length > 0">
            <h2>Tweets</h2>
            <div class="tweetMsg" v-for="(tweet, index) in tweets">
                <p>
                    {{tweet.text}}
                </p>

                <div class="tweetDate">
                    <i class="fas fa-calendar-alt fa-sm fa-fw"></i>{{tweet.date}}
                </div>
                <div class="tweet_remove" @click="removeTweet(index)">
                    <span class="remove">Delete this tweet <i class="fas fa-trash fa-xs fa-fw"></i></span>
                </div>
                
            </div>

        </section>
        <div v-else>No tweets to show</div>
    </div>
</div>
<script src="./main.js"></script>
</body>

</html>

```

JavaScript file

```js

let app = new Vue({
    el: '#app',
    data: {
        userData: {},
        usersID: 0,
        name: "",
        email: "",
        password: "",
        max_length: 25,
        max_pass_length: 16,
        max_tweet: 200,
        error: "",
        registered: false,
        tweetMsg: "",
        tweets: []
    },
    
    methods: {
          registerAccount(){
      
              if (this.name.length > 0 && this.name.length <= this.max_length && this.email !== "" && this.password !== "" ) {
                  
                    this.userData.id = ++this.usersID,
                    this.userData.name = this.name,
                    this.userData.email = this.email,
                    this.userData.password = this.password
                    this.registered=true;
                
                  
                 
              } else {
                  this.error = "Complete all the form fields"
              }
            
            /* Add registration data to the local storage */
            localStorage.setItem('simple_tweet_registered', true)
            /* Add the whole userData object as JSON string */
            localStorage.setItem('simple_tweet_registered_user', JSON.stringify(this.userData))
            
            /* Clear the registration inputs */
            this.name = "";
            this.email = "";
            this.password = "";
        }, 
        sendTweet(){
            this.tweets.unshift(
                {
                    text: this.tweetMsg,
                    date: new Date().toLocaleTimeString()
                }

            );
            this.tweetMsg = "";
            
            //console.log(this.tweets);
            stringTweets = JSON.stringify(this.tweets)
            //console.log(stringTweets);
            localStorage.setItem('simple_tweet_tweets', stringTweets)
        },
        removeTweet(index){
            let removeIt = confirm("Are you sure you want to remove this tweet?")
            if(removeIt) {
                this.tweets.splice(index, 1);
                /* Remove the item also from the local storage */
                localStorage.simple_tweet_tweets = JSON.stringify(this.tweets)
            }
        }
    },
    created(){
        /* Check if the user is registered and set the registered to true */
        if(localStorage.getItem("simple_tweet_registered") === 'true'){
            this.registered = true;
        }

        if(localStorage.getItem('simple_tweet_registered_user')) {
            this.userData = JSON.parse(localStorage.getItem('simple_tweet_registered_user'))
        }
        /* Parse all tweets from the local storage  */
        if(localStorage.getItem("simple_tweet_tweets")) {
            console.log("There is a list of tweets");
            this.tweets = JSON.parse(localStorage.getItem('simple_tweet_tweets'))

        }else {
            console.log("No tweets here");
        }
    }

});

```

We are ready to move forward with our Vue journey. Now it's time to learn about components.

%[https://youtu.be/3DzBkUHH3bU]

## Vue Component Basics

A component is a reusable block of code that represents a specific element on the page.

Every web page and web or mobile application can be divided into components. Starting from the main sections we can further divide these into smaller bits and make sub-components. 

Every component is reusable and is made of dedicated HTML, CSS, and JavaScript code. 

We can use components to organize our code and build complex layouts that are easily maintainable.

Looking at a simple web page, it is usually made of a header, the main content area, and a footer. But each of these three pieces can be sub-divided into smaller parts. 

For instance, a header can have the main navigation menu, a secondary menu, and a hero image. The same is true for the main and footer areas.

You can watch the video on [YouTube here](https://youtu.be/wrqjPka7puo) or at the end of this section to review. You can also view the repository [here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/12-components-basics/).

To get started with components, we first need to learn how to register them, pass them data, and then we need to learn how to use them. Here are some great overviews of these topics to get you started:

- Register a component (https://vuejs.org/v2/guide/components-registration.html)
- How to use Props (https://vuejs.org/v2/guide/components-props.html)
- How to use Slots (https://vuejs.org/v2/guide/components-slots.html)
- How the Data object works inside a component   
- Child Component Events (https://vuejs.org/v2/guide/components-custom-events.html)
- Dynamic Components ( https://vuejs.org/v2/guide/components-dynamic-async.html)


### How to register a component in Vue
To register a component, we need to use the `component` method on the `Vue()` object. After calling this function we need to define a template property with some markup specific to the component. 
```js
Vue.component('component-name', {
    // component properies here
});
```
Every component needs to have a template property at least – without it a component doesn't make much sense.

So the next step is to define a template property and pass to it a string literal with some HTML tag:
```js
Vue.component('test-component', {
    // component properies here
    template: `<p>I am a component</p>`

});
```
Now we can use our component multiple times inside our main HTML file by using its name as it was a standard HTML tag.

```html
<div id="app">
  <test-component></test-component>
</div>

```
However, our component will always render the same content, `I am a component`. Let's make it more useful and, following our tweets example, build a tweet message component.

```js

Vue.component('tweet-message', {
   
    template: `
       <div>
           <p> Tweet text goes here </p>
           <p> Date of the tweet goes here</p>
       </div>
    `
});
```

OK, now that we have the base for our component we need to actually pass data to it.

One thing to notice here is that every component requires a single root element inside the template property. So, since we have two paragraphs, we wrapped them inside a div that will be considered the root element of our component. 

Inside it, we can put whatever we want to build our custom component.

Let's move on to the next step and pass some data to the component.

### How to use props in Vue

Now, given what we've learned so far, we want to pass data to our component as we did previously to bind data between the Vue instance and the markup file via the moustache syntax. 

However, with components things work a bit differently. We use props to create a binding between our component and its template.

The `props` property can be defined as an array or as an object. 
When used as an array, we can specify the properties as strings inside the array and these can later be used inside the component like we usually do. 

When we use an object we can pass the prop as the key and its type as the value. That will help to make sure that the exact data type is passed to our component. 

Let's see an example of that.

Example of props as an Array:
```js
Vue.component('tweet-message', {
    props: ['text', 'date']
    template: `
       <div>
           <p> {{text}} </p>
           <p> {{date}}</p>
       </div>
    `
});

```
Use props as an object where the key is the property and the value is its type:
```js
Vue.component('tweet-message', {
    props: {
        text: String,
        date: String
    }
    template: `
       <div>
           <p> {{text}} </p>
           <p> {{date}}</p>
       </div>
    `
});
```

Once we have defined our properties, we can use them as HTML attributes and pass them the data we want our component to render onto the page. 

For instance, we can use the component above to show a bunch of tweets using our newly created component.

```html
    <!-- Manually pass the data to the tweet message component -->
    <tweet-message text="This is a component" date="25/12/2020"></tweet-message>
    <tweet-message text="This another component" date="26/12/2020"></tweet-message>
    <tweet-message text="This another component" date="27/12/2020"></tweet-message>
    <!-- Pass a javascript expression to the date property of the tweet message component -->
    <tweet-message text="This another component" :date="new Date().toLocaleString()"></tweet-message>
```
The first examples will render the string we passed between quotes. But 
to render the computed result of the new `Date()` instance we will need to use the v-bind directive so that its content is interpreted as JavaScript code.

You can review all this in the docs here: [https://vuejs.org/v2/guide/components-props.html].

### The data property inside components 
So far we have seen that we can bind data by defining properties inside the `data` object on a Vue instance. 

When working with components the data object is not available as an object but as a function. This function can return an object with properties. This will make each component's instance unique and independent from the others.

Following our previous example, let's add a couple of CSS classes to our component.

First, we will edit our component template and bind the class attribute to a data property. Then we will create our data object.

```js
Vue.component('tweet-message', {
    props: {
        text: String,
        date: String
    }
    template: `
       <div :class="tweetBoxWrapper">
           <p> {{text}} </p>
           <p :class="dateClass"> {{date}}</p>
       </div>
    `
});

```
Now our template will look for two data properties, `tweetBoxWrapper` and `dateClass`, that we can later use inside our CSS to add some style to our elements. Let's add the data function now.
 
```js
Vue.component('tweet-message', {
    props: {
        text: String,
        date: String
    }
    template: `
       <div :class="tweetBoxWrapper">
           <p> {{text}} </p>
           <p :class="dateClass"> {{date}}</p>
       </div>
    `,
    data(){
        return {
            // Data properties go here
            tweetBoxWrapper: "tweet-message",
            dateClass: "tweet-date",
        }
    }
});

```
Another thing we can do is to define a data property and use it inside our template, for instance, to dynamically show the current date. We can define a `now` property and use it in the template like we previously did with the `date` property:

```js

Vue.component('tweet-message', {
    props: {
        'text': String,
        
    },
     template: `
       <div :class="tweetBoxWrapper">
           <p> {{text}} </p>
           <p :class="dateClass">{{now}}</p>
           
       </div>
       
    `,
    data(){
        return {
            tweetBoxWrapper: "tweet-message",
            dateClass: "tweet-date",
            now: new Date().toDateString(), // 3 
            
        }
    }

    
});


```
In the example above we have used both `props` and `data`. We can use the prop `text` as an attribute when we use our component ` <tweet-message text="This is a component"></tweet-message>`. The properties we returned in the `data` method are bound to the template and will render the information we specify right there in the data method.

When inside the data method, we need to remember that props defined here are accessible using the `this` keyword.

So if we want to store the value of the text prop inside a property in the data object, we can grab it like this:

```js
Vue.component('tweet-message', {
    props: {
        'text': String,
        
    },
     template: `
       <div :class="tweetBoxWrapper">
           <p> {{text}} </p>
           <p :class="dateClass">{{now}}</p>
           
       </div>
       
    `,
    data(){
        return {
            tweetBoxWrapper: "tweet-message",
            dateClass: "tweet-date",
            now: new Date().toDateString(), 
            message: this.text
        }
    }

    
});
```
Next, we will learn about slots.

### How to use slots
There are situations when we just don't know or want to strictly define what goes inside a component. Or we might want to let the user decide its content when they use our component.

In such cases, we can use slots when we declare the template of our component.

Let's imagine that we have another component that we want to use to divide tweets into different sections.

```js
Vue.component('tweet-section', {
    props: {
        'title': String,
        
    },
     template: `
        <div class="tweet_section">
            <h2>{{title}}</h2>
           <slot></slot>
       </div>  
    `    
});

```
Our new component can be as simple as that, a div with a class `tweet_section`, an `h2` that binds to a prop, and a slot. The slot means that inside our component we can put whatever we want, like nesting other elements and even other components.

```html

<tweet-section title="Latest Tweets">
    <tweet-message text="This is my first tweet"></tweet-message>
    <tweet-message text="This is my second tweet"></tweet-message>
    <tweet-message text="This is my third tweet"></tweet-message>
    <tweet-message text="This is my fourth tweet"></tweet-message>

</tweet-section>
<tweet-section title="Most popular">
    <h3>Trendy in IT</h3>
    <tweet-message text="This is a very popular tweet"></tweet-message>
    <tweet-message text="This is another popular tweet"></tweet-message>
</tweet-section>

```
We've barely scratched the surface here, but with what we know we can already modify our `simple_twitter` application to use components. Along the way, we will also learn how events work inside components.


%[https://youtu.be/wrqjPka7puo]


## How to Update Your Simple_twitter Project with Components

Now that we have a basic understanding of components, we can update the simple Twitter project we built in the previous videos and use components to make our code better.

We need to do a few things to make this happen, and create a component:

 1. We need to decide what component we want to build 
 2. We need to extract the code from the markup and place it in the template property
 3. We need to refactor our code to make the component work.

You can watch the tutorial on [YouTube here](https://youtu.be/HanHyGFC6Sc)
or checkout the repository [here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/13-simple-twitter-components/).


Let's say we want to create a component for the tweet message. 

### How to create the component
Let's create a component for a tweet message like this:
```js
Vue.component('tweet-message',{
    template: ``
});
```
### How to move the tweetMsg element
Then we have to move the `tweetMsg` element inside the  `template` property of our component:
```js

Vue.component('tweet-message',{
    template: `
    <div class="tweetMsg" v-for="(tweet, index) in tweets">
        <p>
            {{ tweet.text}}
        </p>
        <div class="tweetDate">
            <i class="fas fa-calendar fa-sm fa-fw"></i>{{ tweet.date }}
        </div>
        <div class="tweet_remove" @click="removeTweet(index)">
            <span class="remove">Delete this tweet <i class="fas fa-trash fa-sm fa-fw"></i></span>
        </div>
    </div>
    `
});

```
After that, we need to update the template because the v-for directive now is useless. So we will remove it and add it back later when we are ready to use the component.

Given that we will not have a v-for directive at this point, we still want to use the tweet variable to grab the tweet, so we will pass it as a `props`.


```js
Vue.component('tweet-message',{
    props: {
        'tweet': Object,
    },
    template: `
    <div class="tweetMsg">
        <p>
            {{ tweet.text}}
        </p>
        <div class="tweetDate">
            <i class="fas fa-calendar fa-sm fa-fw"></i>{{ tweet.date }}
        </div>
        <div class="tweet_remove" @click="removeTweet(index)">
            <span class="remove">Delete this tweet <i class="fas fa-trash fa-sm fa-fw"></i></span>
        </div>
    </div>
    `
});
```
### How to emit a custom event
There is also an event listener that needs to change to let our application work as expected. 

```html
<div class="tweet_remove" @click="removeTweet(index)">
    <span class="remove">Delete this tweet <i class="fas fa-trash fa-sm fa-fw"></i></span>
</div>
```

The code here `<div class="tweet_remove" @click="removeTweet(index)">` listens to click events so the user can remove a tweet by clicking on it. 

This will need to go, and we need to replace it with a special method of the Vue instance called `$emit()`. Our component instance will need to communicate with the parent instance and tell it that it wants to trigger the remove tweet method.  

To solve this problem, Vue provides a custom events system. It allows us to use the v-on directive to listen not only to native DOM events but also to custom events defined at the component level.

We need to update this line of code: 
```html
<div class="tweet_remove" @click="removeTweet(index)">

```
and change it like so: 
```html
<div class="tweet_remove" @click="$emit('remove-tweet', 'index')">
```

Let's break this down: we keep using the v-on directive in its short form `@`. Then we use the Vue `$emit` method to define a custom event that our component will emit when we click on this element. 

To the `$emit` method we pass two parameters, the first is the name of the custom event `remove-tweet`, and the second is a parameter that we want to pass to the event listener when we use `index`. That will be the index of the element we want to delete. 

So that the parent instance can listen to our event, trigger the `removeTweet` method we defined in the main Vue instance and remove the correct tweet.


### Put it all together
Our final component now looks like this:
```js

Vue.component('tweet-message',{
    props: {
        'tweet': Object,
    },
    template: `
    <div class="tweetMsg">
        <p>
            {{tweet.text}}
        </p>

        <div class="tweetDate">
            <i class="fas fa-calendar-alt fa-sm fa-fw"></i>{{tweet.date}}
        </div>
        <div class="tweet_remove" @click="$emit('remove-tweet', 'index')">
            <span class="remove">Delete this tweet <i class="fas fa-trash fa-xs fa-fw"></i></span>
        </div>
        
    </div>
    `
});

```

And we'll change our index.html file as follows:

```html
<!-- Show all tweets -->
<div class="card_tweets">
    <section class="tweets" v-if="tweets.length > 0">
        <h2>Tweets</h2>
        <tweet-message v-for="(tweet, index) in tweets"  v-bind:tweet="tweet" :key="index" @remove-tweet="removeTweet(index)"></tweet-message>
    </section>
    <div v-else>No tweets to show</div>
</div>
```

Now that we've completed our first project, let's learn how to make an API request and how to use the GitHub API to build our final portfolio.


%[https://youtu.be/HanHyGFC6Sc]

## How to Perform API Calls with Axios

For our next project, I have created a simple but nice design using Figma that we will use to kick start our portfolio.

Our portfolio will use the GitHub's rest API to pull projects and fill out the design. 

You can watch the video on [YouTube here](https://youtu.be/XJEmPr89HA8)
and check out the repository on [BitBucket](https://bitbucket.org/fbhood/how-to-vuejs/src/master/14-axios/).

### What is a REST API?

To quote Wikipedia:

>"A REST API is a software architectural style that enables the requesting system to access and manipulate a textual representation of web resources."

What this means is that our Vue application (the requesting system) will request a textual representation from GitHub of our repositories that we can use later and manipulate to showcase our projects inside our portfolio.

For our final project, we will use a library called Axios that will help us make HTTP requests to the GitHub API. 

We can install Axios inside our project in multiple ways. For our example we will keep things simple and use the CDN. 

There are also other methods you can use to install Axios. The official documentation for Axios is available [here](https://www.npmjs.com/package/axios)
and you can read about how to consume the API in the [documentation here](https://vuejs.org/v2/cookbook/using-axios-to-consume-apis.html#Base-Example).

### How to install Axios via CDN

So let's get started and install Axios via the CDN. We will use the UNPKG CDN and insert a script tag inside our main HTML file. 

This CDN will always provide the most up to date version of Axios. Alternatively, we can also specify a different version number. 

Let's start by inserting the following script in an index.html file that we will use to send our first HTTP request to the GitHub API.


```html
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

Our final HTML file will look like this now:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VueJS / GitHub API</title>
    

</head>
<body>
    <div id="app"> </div>

    <!-- Axios latest version CDN -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

    <!-- VueJS development version -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script src="./main.js"></script>
</body>
</html>

```

The code above is nothing new, but let's look at it piece by piece.

We have a basic HTML structure. Before the closing body tag, we've placed two script tags, one for Axios and one for VueJs. 

In the body, we created a root element for the Vue application that we called `#app`.

Finally, before the end of the body tag, we placed a new script tag that points to the file where we will write our code, the main.js file.

Now we have all the building blocks to make our first API call and request data from the GitHub API.

But before that let's quickly see what an HTTP request actually is and what kind of requests we can make.

### What is an HTTP request?
HTTP stands for Hypertext transfer protocol. It is an application-layer protocol designed for communications between two points:

1. a web client (the browser) 
2. a web server

This protocol allows transmission of data like HTML files and. It defines verbs also known as methods that you can use to perform specific actions on a given resource.

The method or verb that we will use for our project is the `GET` method, that, as you might have guessed, is used to obtain or to get 
a resource from the webserver.

We have also other methods:
- GET (retrieves data)
- POST (sends data)
- PUT (updates the entire representation of the data)
- PATCH (similar to put but used to partially update data)
- DELETE (removes data)

Each of these requests performs a specific action on a resource, but there are also other verbs like the HEAD, OPTIONS, CONNECT, and TRACE.

I won't cover HTTP in detail here as it's out of the scope of this guide. But below there are some links to documentation pages 
related to this topic if you want to find out more. 

I suggest you to read the following at least:

- [HTTP Intro](https://www.freecodecamp.org/news/how-the-internet-works/)
- [HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)


### How to perform a GET request

We will use the GET method to perform get requests from the GitHub API. All data we want to request are publicly accessible (the public repositories of a user), therefore we don't have to authenticate our application. 

But unauthenticated requests are limited. For the scope of this tutorial, this is perfectly fine. If you plan to put this in production then you might want to look at how to make authenticated requests and obtain an API key from GitHub.

GitHub provides clear and in-depth documentation about its Rest API, including a list of resources that you can request along with their endpoints. We will use the "List repositories for a user" resources available [here](https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#list-repositories-for-a-user).

Let's look at the documentation. The first thing we notice is that GitHub gives us a GET endpoint where we can send our HTTP requests `/users/{username}/repos`. 

The placeholder `{username}` needs to be replaced with the actual username of the user we want to request the list of public repositories from.

From the documentation, we also see that there are other parameters that we can use to refine our request. We will use `username` that goes in the path and needs to be a string as described in the parameters table under Type. 

We can also use the `per_page` and `page` parameters to paginate our results.

Let's make the first request and see what we get.

Inside our main.js file, we will create a new Vue instance and add a `mounted` lifecycle hook where we will perform the HTTP request using Axios.

```js
let app = new Vue({
    el:'#app',
    data:{
        projects: [],
        perPage: 20,
        page: 1
    },
    mounted(){
        
         axios
         .get(`https://api.github.com/users/fabiopacifici/repos?per_page=${this.perPage}&page=${this.page}`)
         .then(
            response => {
                console.log(response);
                this.projects = response.data;
            }
        )
        .catch(error=> {console.log(error);})
    }
});
```

Let's break this code down. First, we have created a new Vue instance. Then we used the `el` property and assigned it a root HTML element. 

Then we have defined a `data` object and the properties that we will use later to perform the HTTP request and handle the response.

After the data object, we have defined a lifecycle hook that will use to run our code once the root element has been mounted.

Inside the `mounted` method, it's time to use Axios and perform an HTTP request. 

Axios is a promise-based HTTP client. When we use the get method to request our data from the GitHub API it will return a promise that needs to be handled. 

We do this using the syntax `axios.get()` to perform the request, then we handle its response using the `.then()` method on the promise. 

If our request fails the `.catch()` method will handle the error and, in this case, show the error message on the console.

Promises are out of the scope of this guide, but if you want to learn more, you can check out [this detailed article here](https://www.freecodecamp.org/news/javascript-promise-tutorial-how-to-resolve-or-reject-promises-in-js/).

Inside the `.get()` method we have put the URL including a query string that uses `per_page` and `page` parameters to submit our request. Inside the `.then()` method we handled the response. The response parameter is given to us by the promise and we use an arrow function to handle it.

```js 
response => {
                console.log(response);
                this.projects = response.data;
            }
```

The get method returns a promise. Here we simply handled its `response` with an arrow function where `response` is the return value that we obtained by calling `axios.get()`.

We logged the response object to the console. Then we assigned its content, the `response.data`, to our `projects` property so that we can later retrieve each project and show them onto the page as usual with a `v-for` directive.

### How to show each project 

Now it's time to show our projects inside the portfolio. We can do that with the v-for directive.

The projects property in this case contains an array of objects. Each object has its properties that we can use to populate our template.

```html
<div id='app'>

    <div v-for="project in projects">
        <h2 class="title">{{project.full_name}}</h2>
        
        <div class="author">
            <img width="50px" :src="project.owner.avatar_url" alt="me">
        </div>
        <div class="view">
            <a :href="project.html_url">View</a>
        </div>
    </div>

</div>
```

Here we use the v-for directive to loop over the array of projects.
Now the `project` variable contains an object that represents a single repository from the GitHub account.

Looking at the response object we know that we can grab a number of properties. So we picked `full_name`, the full name for the repository, `owner.avatar_url`, the URL of the profile's avatar, and `html_url` that is the actual URL of our repository. That's all we need for now. 

If we now look at the page we will immediately see all repositories from our account.

Now that we know how to make an HTTP request with Axios and get data from GitHub, we are almost ready to start building our portfolio. 

In the next section, we are going to look at another Vue library called Vue-router that we will use in our final project.


%[https://youtu.be/XJEmPr89HA8]


## How to Handle Routing with VueRouter

Our portfolio will surely have more than one page, so we need a system that understands where to send the user when, for instance, they click a link in the navbar for a specific page. 

For that Vue has an official routing package that can help us do just that and build a single page application.

A single page application is an application that doesn't refresh the page when a user visits a new page so that the user experience is more fluid.

As for Vue and Axios, we need to install this library and we do that via its CDN. But as always, there are also other methods depending on your needs. I just want to keep things simple for now, so let's start by placing the CDN script tag inside the HTML file and learn the basics of this new library.

You can watch the tutorial on [YouTube here](https://youtu.be/T_avTRFAEAg)
and checkout the repository on [BitBucket](https://bitbucket.org/fbhood/how-to-vuejs/src/master/15-routing/).

You can also see the Vue Router Documentation [here](https://router.vuejs.org/installation.html#direct-download-cdn).

### How to install Vue Router via CDN

Let's take our previous example index.html and after the VueJS CDN will point to the router `https://unpkg.com/vue-router@3.4.9/dist/vue-router.js`.

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VueJS / GitHub API</title>
  
</head>
<body>
    <div id="app"> 
        <div v-for="project in projects">
            <h2 class="title">{{project.full_name}}</h2>
            
            <div class="author">
                <img width="50px" :src="project.owner.avatar_url" alt="me">
            </div>
            <div class="view">
                <a :href="project.html_url">View</a>
            </div>
        </div>

    </div>
      <!-- Axios latest version CDN -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>

    <!-- VueJS development version -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    
    <!-- Vue Router CDN -->
    <script src="https://unpkg.com/vue-router@3.4.9/dist/vue-router.js"></script>
    
    <!-- Main scrip file -->
    <script src="./main.js"></script>
</body>
</html>
```

### How to use Vue Router

Now our app has access to the router system and we can add a couple of routes for our application.

We can do so using the `router-link` component provided by the library and its `to` attribute to point the link to a specific page.

```html
<!-- Create a router link using the 'router-link' component and set the path using the 'to' attribute -->
<header>
    <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/projects">Projects</router-link>
    </nav>
</header>

<!-- Render the component for the corresponding route -->
<router-view></router-view>
```

We also used the router-view component that will render a specific component for each route.

Now we need to do something inside our JavaScript file to make this work. 

Let's see the steps we need to take:
- Define route components
- Define routes
- Create a Vue router instance
- Create and mount the Vue root instance.

First, we need to define our components that we'll use from each route to render the content of the page.

We will create two components, one for the home page and one for the projects page.

To simplify the steps, we will keep everything in the same file and refactor later on. 

Let's create the first two basic components to see if the router works:

```js
// Create Route components
const Home = {template: '<div>My Portfolio</div>'} 
const Projects = {template: '<div> Projects </div>'} 
```

Now let's follow the remaining steps and define the routes, create the vue router instance, and create and mount the Vue root instance.

```js

// Define some routes
const routes = [
    {path: '/', component: Home},
    {path: '/projects', component: Projects}
];
// Create the router instance and pass the routes to it
const router = new VueRouter({
routes: routes
});
// Create and mount the root instance.

let app = new Vue({
    router 
}).$mount('#app');

```

That's it. If you visit the homepage you will see two navigation links and the site content will change accordingly.

Let's put it all together and start building our portfolio.

From the previous example in the Axios section, we requested from the GitHub API all public repositories for a user and rendered name, user avatar, and project URL onto the page. 

Let's move some of that logic inside our application that uses routes.

The main changes that we need to make here are:
- move the HTML markup inside the `template` property of the project's component
- move the `data` properties inside the `data` object of the component
- move the code we wrote in the mounted hook inside our component.

The final code looks something like this:
```js
// Define route components

const Home = {template: '<div>My Portfolio</div>'} 
const Projects = {
    
    template: `<div> 
         <div v-for="project in projects">
            <h2 class="title">{{project.full_name}}</h2>
            
            <div class="author">
                <img width="50px" :src="project.owner.avatar_url" alt="me">
            </div>
            <div class="view">
                <a :href="project.html_url">View</a>
            </div>
        </div>
    </div>`,
    data(){
        return {
            projects: [],
            perPage: 20,
            page: 1
        }
    }, 
    mounted(){
        
         axios
         .get(`https://api.github.com/users/fabiopacifici/repos?per_page=${this.perPage}&page=${this.page}`)
         .then(
            response => {
                //console.log(response);
                this.projects = response.data;
            }
        )
        .catch(error=> {console.log(error);})
    }
} 

// Define some routes
const routes = [
    {path: '/', component: Home},
    {path: '/projects', component: Projects}
];
// Create the router instance and pass the routes to it
const router = new VueRouter({
routes: routes
});
// Create and mount the root instance.

let app = new Vue({
    router 
}).$mount('#app');

```


The HTML file remains the same:

```html
<div id='app'>
  <header>
            <nav>
                <router-link to="/">Home</router-link>
                <router-link to="/projects">Projects</router-link>
            </nav>
        </header>

        <router-view></router-view>
</div>

```

Now that we have a base to work with, let's improve it. We will use a design prototype I made using Figma and add some functionalities to our portfolio to make it look nice.

%[https://youtu.be/T_avTRFAEAg]

## Final Project – How to Build a Portfolio with VueJS, VueRouter, Axios, GitHub API and deploy to Netlify 

We are ready to build our final project! For our Vue-folio, we will start from where we left off in the previous section.

We will build a single-page application that has two routes, one for the home page and one for the projects page. 

Below are the building blocks:
- Vuejs 
- Vue router
- Axios
- GitHub rest API
- portfolio design

You can watch this tutorial on [YouTube here](https://youtu.be/I6hQnWQU4rQ) and check out the repository on [BitBucket here](https://bitbucket.org/fbhood/how-to-vuejs/src/master/16-final-project-portfolio/).

### Project structure

To speed things up we will just copy the code we wrote in the previous section.

The project structure will be the following:
```
|-- index.html
|-- assets/
    |-- css/
        |-- style.css
    |-- js/
        |-- main.js
    |-- img/
```

### index.html file
The index.html file is a little different from what we had in the previous section. Here, we will place only the router-view component that is responsible for showing the component matching a given route. 

Then we will place the actual `route-links` inside each component to make sure we have the desired result as per the design.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vuefolio</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100;300;400;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <link rel="stylesheet" href="./assets/css/style.css">
</head>

<body>

    <div id="app">

        <!-- Render the component for the corresponding route -->
        <router-view></router-view>

    </div>
    <footer> © Developed by <a href="https://fabiopacifici.com">Fabio Pacific</a> </footer>
    <!-- Axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <!-- VueJS development version -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <!-- Vue Router -->
    <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>
    <!-- Main Js file -->
    <script src="./assets/js/main.js"></script>
</body>

</html>
```

### style.css file
Since this is not going to be a CSS tutorial, for the CSS part you can simply copy the code from the repository file if you are following along.
```css

    /* Utility Classes */
    .d_none {
        display: none;
    }
    .d_flex {
        display: flex;
    }
    .container {
        max-width: 1170px;
        margin: auto;
    }
    a {
        color: white;
    } 
    a:hover {
        color:#DB5461;
        
    }
    .loading {
        font-size: 2rem;
    }
    /* END Utility Classes */
    /* Components */
    .bio__media {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        text-align: left;
    }
    .bio__media img {
        height: 120px;
    }
    .bio__media__text {
        padding: 1rem;
    }
    .bio__media__text h1{
        font-size: 36px;
        font-weight: 900;
        color: #DB5461;

    }
    .bio__media__text p {
        font-weight: 100;
        font-size: 16px;
        line-height: 1.5rem;
        
    }

    .card__custom {
        position: relative;
        display: flex;
        max-width: 400px;
        height: 300px;
        min-height: 300px;
        padding: 0.5rem;
        margin-bottom: 3rem;
        flex-grow: 1;
        flex-basis: calc(100% /2);
        align-items: center;
        justify-content: space-between;
    }
    .card__custom > .card__custom__text {
        max-width: calc((100% / 3) *2);
        text-align: right;
        height: 80%;
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        overflow: hidden;

    }
    .card__custom__img {
        
        position: absolute;
        width: 70%;
        height: 100%;
        background-image: url(../img/cards_bg_img.svg);
        background-position: center;
        background-repeat: no-repeat;
        background-size: contain;
        display: inline-block;
        z-index: -1;
        left: 60%;
        transform: translateX(-50%);
        border-radius: 85px 0 100px 25px;

    }
    .card_custom__button a, .btn_load_more {
        background: #F1EDEE;
        border: 5px solid #3D5467;
        box-sizing: border-box;
        border-radius: 54px;
        padding: 0.5rem 1rem;
        font-weight: 900;
        color: #3D5467;
    }
    .card_custom__button a:hover, .btn_load_more:hover {
        cursor: pointer;
        background: #324555;
        color: white;
        border-color: #DB5461;
        transition: 1s;
    }
    .card__custom__text h3 {
        text-transform: uppercase;
        font-size: 1.5rem;
    }
    /* END Componenet */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body{
        font-family: 'Raleway', Arial, Helvetica, sans-serif;
        color: white;
        background: linear-gradient(116.82deg, #3D5467 0%, #1A232B 99.99%, #333333 100%);

    }
    a {
    text-decoration: none;   
    }

    /* Home Page */
    main#home {
        width: 100%;
        height: 100vh;
        min-height: 600px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    #home > .about__me {
        text-align: center;
        width: 80%;
        line-height: 1.5rem;
    }
    #home > .about__me > h1 {
        margin: 20px 0 0;
        font-size: 36px;
        font-weight: 900;
        color: #DB5461;
    }
    #home > .about__me > h3 {
        font-size: 28px;
        font-weight: 500;

    }
    #home > .about__me > h1, #home > .about__me > h3  {
        font-style: normal;
        line-height: 42px;
        letter-spacing: 0.115em;

    }
    #home > .about__me p {
        font-weight: 100;
        font-size: 22px;
        padding: 2rem;
    }
    .skills_projects_link {
        position: relative;
    }
    .skills_projects_link > a {
        text-transform: uppercase;
        color: white;
        font-weight: 900;
        font-size: 18px;
        line-height: 21px;

    }
    .skills_projects_link > a:hover {
        color: #DB5461;
        transition: all 0.5s ease-in-out;

    }
    .skills_projects_link > a:hover::after {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        margin: auto;
        text-align: center;
        content: "";
        width: 30px;
        height: 2px;
        background-color: #DB5461;
        transition: background-color 0.5s ease-in-out;

    }

    /* Header */
    #site_header {
        text-align: center;
        padding: 2rem 0;
        justify-content: space-between;
        align-items: center;
    }
    #site_header > h1 {
        text-transform: uppercase;
    }
    nav a {
            color: #e2e2e2;
        text-transform: uppercase;
        font-weight: 900;
    }
    nav a:hover {
        color: #DB5461;
    }
    /* Portfolio Page Section */

    #portfolio {
        margin-top: 4rem;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-around;
    }
    .btn_load_more {

    }
    /* Skills */

    #skills_section {
        margin-top: 4rem;
        min-height: 300px;
        background-image: url(../img/skills_bg.svg);
        background-repeat: no-repeat;
        background-size: contain;
        background-position: top left;
    }
    #skills_section h2 {
        margin-left: 180px;
        font-size: 44px;
        color: #F1EDEE;
        line-height: 2rem;

    }
    #skills_section ul {
        list-style: none;
        margin: 20px 120px;
        display: flex;
        flex-wrap: wrap;

    }
    #skills_section ul  li {
        padding: 1rem;
        margin: 0.5rem;
        background-color: #DB5461;
        border: 5px solid #3D5467;
        border-radius: 35px;
    }



    .avatar {
        width: 30px;
        height: auto;
        border-radius: 50%;
            margin: 0 1rem;

    }




    .card__back {
        display: none;
    }
    .rotate__card {
        transform: rotate3d(360,0,0,180deg);
    }
    /* Site Footer */

    footer {
        text-align: center;
        padding: 2rem 0;
    }



    /* Media Query  */

    @media screen and (max-width: 475px) {
        .card {
            flex-basis: 100%;
            width: 100%;
        }
    }

```

## Main.js file basic structure
Inside the main.js file, we have the core of our single page application. 
Here we will define the route components that need to be rendered for each view/page, the homepage, and projects components. 

Then we will define two routes, one for the homepage and one for the projects page, create a router instance, and pass it to the routes. Finally, we will create a new Vue instance and pass to it the router instance and mount the root HTML element.

Let's start with the route components.

### How to define components for each view
The homepage component is fairly simple. 

```js
// Homepage component
const Home = {
    template: 
    `<main id="home">
        <div class="about__me">
            <img src="./assets/img/avatar.svg" alt="">
            <h1>John Doe</h1>
            <h3>Python Expert</h3>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
    
            <div class="skills_projects_link">
                <router-link to="/projects">Projects/Skills</router-link> 
            </div>
        </div>
    </main>`
}
```
Let's break it down. First, we create a Home constant that will hold the router component object. 

Inside the object, the only thing we will put is the template property with some markup to render our page. The main thing to notice here is the router-link component that will point to the /projects route from the homepage.

Next, let's create a route component for the projects page. We have a lot to do here so for now let's just add some boilerplate code – we will come back to it later and write out step by step all the logic. 

```js
const Projects = {
    template: 
    `<div>
        <h1>Projects</h1>
    </div>`,
    data() { 
        return {
                // Data object here
            }
    },
    methods: {
        // All methods here
    },
    mounted(){  
        // Lifecycle hook      
        
    }
}

```
The Projects route components have a `template` property that so far holds a basic markup that only spit out an `h1` title.

After that there is the component's data method that returns an empty object, then an empty methods object and an empty lifecycle hook.

That's all we need, for now, so let's move on and define the rest of the building blocks, the routes, the router and the Vue instances.


### How to define the routes, router, and Vue instance
Now that we have two components to render on our main pages we can move forward to the next steps:
- define routes
- create the router instance
- create and mount the Vue instance

First, let's define our two routes and link the components.
```js

// Define routes
const routes = [
    {path: '/', component: Home},
    {path: '/projects', component: Projects},
];

```
In the code, we have defined a new constant called routes. In it, we defined two routes as an array of objects. 

Each object has two properties:
- path
- component

The first object is for the homepage. Its path will respond to requests made to our website base URL, like https://fabiopacifici.com/.

Then the component property links this page to the route's component called `Home` that we defined in the previous step. 

The second object is for the projects page. The path responds to requests made to `/projects` and it's linked to the `Projects` route component.

Now that we have our routes:

```js

// create the router instance
const router = new VueRouter({
    routes
})

```
Above we used the ES6 syntax that allows us to just put the name of the variable holding the routes since it is equal to the name of the property that we needed to use. It's actually the same as writing `routes: routes`.

Now, we create a Vue instance. Inject the router instance inside it and finally mount the root element. 

```js

// create and mount the vue instance
const app = new Vue({
    router
}).$mount('#app');
```

Done! We now have everything in place to start building our portfolio and complete the Projects route component.

## How to Build the Main Projects Route Component
We will start working on the data object. Here we need to define properties that will hold all our projects once we fetch data from the git hub API.

### The data object
To keep things easier I have intentionally limited results to 20. If you feel this isn't enough you can change the code as you like. 

You can implement pagination for your results by increasing the page property that will be passed to the query string or return more results per page by increasing the value of the `perPage` property.

```js
data() { 
    return {
        projects: [],
        projectsList: null,
        skills: [],
        projectsCount: 5,
        perPage: 20,
        page: 1,
        loading: true,
        errors: false,
        }
    },
```

As we learned in the section where we used Axios to fetch data from the GitHub REST API, there are a few properties we need to define. 

The component's data function returns an object with a `projects` property where we will store all projects we fetch from GitHub.

Then we add a `projectsList` property that holds only a few projects at a time. We will use this property later to implement a very simple
load more feature in combination with the `projectsCount` property.

Then we have a `skills` property where we will store all languages used to build our projects. 

We'll use the `perPage: 20` and `page: 1` properties to build the query string used to fetch data from GitHub. It will take 20 projects and 
return only the first page of results unless we change these values.

Finally, we have a `loading: true` property that we will use to check if the page is fetching data and an `errors: false` property that shows an error message in case we are unable to connect to the GitHub server.

In the next step, we will start working on all methods required to make our application work.

### The fetch all data method

The first method is the one we will use to fetch data from GitHub.

This method will make the Ajax call to the GitHub rest API using Axios and store the response in a property of the Vue instance:
```js

 fetchData: function(){
            axios
            .get(`https://api.github.com/users/fbhood/repos?per_page=${this.perPage}&page=${this.page}`)
            .then(
                response => {
                    
                    this.projects = response.data;
                    this.projects.forEach(project =>{
                        if (project.language !== null && ! this.skills.includes(project.language)) { 
                            this.skills.push(project.language)
                        };
                    });
                }
            )
            .catch(error=> {
                console.log(error);
                this.errors = true;
            })
            .finally(() => { 
                this.loading = false
                this.getProjects();
            })
        }, 
```

Let's break this down. First, we defined a method called `fetchData: function(){}`. This method uses Axios to make an API call to the
REST API. 

In the `.get()` method we have built the URL also using the properties `perPage` and `page` as part of the query string.

The get method returns a promise so we used the `.then()` method on the promise to handle the response using an arrow function `response => {}`.

Inside the arrow function, we stored the response data inside the projects property of the Vue instance using ` this.projects = response.data;`.

Next, we used a `forEach` loop to iterate over each project and store the language used in the repository as a skill using the code below:

```js
this.projects.forEach(project =>{
    if (project.language !== null && ! this.skills.includes(project.language)) { 
        this.skills.push(project.language)
    };
});
```

We chained a `.catch` method to handle an error in case we are unable to connect to the rest API and fetch data. We will log the error to the
console and update the value of the `errors` property to true so that we can show a custom error message to the user later on. 

Finally, we chained the `.finally()` method that will be executed after the response has been handled. We also updated the `loading` property and set it to false so that we can show the results to the user. 

Inside the `finally` method we can also call a method (that we still have to create) and that we will use to slice the results later. 

Let's build it.

### The get projects method
This method takes a portion of the projects we actually stored in the `projects` property. We can use the `projectsList` property to store the slice and later implement a method to increment them with a show more button.
```js

getProjects: function(){

    this.projectsList = this.projects.slice(0, this.projectsCount);
    return this.projectsList;

},
```
The getProjects method takes a portion of all projects stored in the `projects` property using the array slice method in conjunction with
the property `projectsCount` that is set to five. So it will store in there only the first five results and return them.

To add five more projects to the `projectsList` property we will also need a method that the user can call when he clicks on the load more button. Let's create it.

### The load more projects method
The load more method will first check if the length of the `projects` array is less than or equal to the length of the `projectsList` array. Then, if not, it will increment the value of the `projectsCount` property by five and then take a bigger slice from the `projects` property.

```js

loadMore(){
            
    if(this.projectsList.length <= this.projects.length){
        this.projectsCount += 5;
        this.projectsList = this.projects.slice(0, this.projectsCount)
    }
    

}
```

### Build the template
In the template property of the `Projects` component, we can start with the header section. We'll also put in there two `router-link` components for the pages navigation:

```html
`<div>
        <header id="site_header" class="container d_flex">
            <div class="bio__media">
                <img src="./assets/img/avatar.svg" alt="">
                <div class="bio__media__text">
                    <h1>John Doe</h1>
                    <h3>Python Expert</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
                </div>
            </div>
            <nav>
                <router-link to='/'>Home</router-link>
                <router-link to="/projects">Project</router-link>
                <a href="https://">
                    <i class="fab fa-github fa-lg fa-fw"></i>
                </a>
            </nav>
        </header>

</div>

```
Next, we can continue working on the template and create the main section.
We will put the following markup always in the main template div, right under the header closing tag.

Let's start by placing the main container:

```html
<main class="container">
    <!-- Show an error message if the REST API doensn't work -->
    <!-- Otherwise show  a section for our portfolio projects and skills section-->
</main>
```

Inside the container, let's use the v-if-else directives to show an error message or the projects section:

```html
 <!-- Show Errors if the rest api doesn't work -->
    <div class="error" v-if="errors"> 
        Sorry! It seems we can't fetch data righ now 😥
    </div>
    <!-- Else show the portfolio section -->
    <section id="portfolio" v-else></section>
```
To make the code work, we used the v-if directive and passed to it the `errors` property. This property will be set to `true` if there is an error while we fetch data from GitHub or will be set to `false` if everything is ok. So the v-else directive will render the portfolio section.

Next, we need to show a 'loading...' message while we fetch data. When done we can use the v-for directive to loop over the results. So right in the portfolio section, we will write another v-if-else directive.

```html
<section id="portfolio" v-else>
 <!-- Use a v-if directive to show the loading message -->
        <div class="loading" v-if="loading">😴 Loading ... </div>

        <!-- use a v-for directive to loop over the projectsList array -->
        <div v-for="project in projectsList" class="card__custom" v-else></div>

</section>
```

Here we use the v-if directive `<div class="loading" v-if="loading">😴 Loading ... </div>` to render a loading message. After that the `<div v-for="project in projectsList" class="card__custom" v-else></div>`
has two directives, the v-for directive that we use to loop over the `projectsList` property and a v-else directive that will show this element when we are done fetching data from GitHub.

Now we can use the `project` variable to render all project details in our markup:

```html
<!-- use a v-for directive to loop over the projectsList array -->
<div v-for="project in projectsList" class="card__custom" v-else>
    <div class="card__custom__text">
        <div>
            <!-- Create a custom method to trim the project name so that it doesn't break the design -->
            <h3>{{project.name}}</h3>
            <!-- Create a custom trimmedText to trim the description -->
            <p>{{project.description}}</p>                        
        </div>

        <div class="meta__data d_flex">
            <div class="date">
                <h5>Updated at</h5>
                <div>{{new Date(project.updated_at).toDateString()}}</div>
            </div>
            <img class="avatar" :src="project.owner.avatar_url">

        </div>
    </div>
    <div class="card__custom__img"></div>
    <div class="card_custom__button">
        <a :href="project.html_url" target="_blank">
            Code
        </a>
    </div>

</div>

```
To render the project title and desciption we used the propeties `poject.name` and `project.description`. But the description and the title will break our design unless we trim them at some point. 

Next in the element with class `date` we rendered the poject data in a readable fomat using the ` new Data().toDateString()` method. 

To render the user avatar `<img class="avatar" :src="project.owner.avatar_url">` we used the shortcut for the v-bind diective so that we could use the property `project.owner.avatar_url` to grab the avatar URL. 

Finally, to render a button that once clicked redirects the user to the repository page we bound the `href` attribute to the `project.html_url` property `<a :href="project.html_url" target="_blank">Code</a>`.

Our project card is complete. The next thing we need to do is render a load more button to show more projects. 

We are still working inside the `projects` section. Right after the project card we can write the following markup

```html
<!-- Render a load more button -->
<div style="text-align: center; width:100%" v-if="!loading" >
    <div v-if="projectsList.length < projects.length">
        <button class="btn_load_more" v-on:click="loadMore()">Load More</button>
    </div>
    <div v-else>
        <a href="" target="_blank" rel="noopener noreferrer">Visit My GitHub</a>
    </div>

</div>

```
The v-if directive first checks if the loading property is set to false. 
If so, we'll use another v-if directive to check if the length of property `projectsList` is less than the length of the property `projects`. 

If so, it will show a button that uses a v-on directive to listen for clicks 
`<button class="btn_load_more" v-on:click="loadMore()">Load More</button>` and trigger a `loadMore()` method. Otherwise, we show a link to the GitHub account. 

After this, we can show a list of skills related to all the projects:

```html
<!-- Show a skills section -->
<div id="skills_section">
    <h2>Development Skills</h2>
    <ul class="skills">
        <!-- Loop over the skills property -->
        <li v-for="skill in skills">{{skill}}</li>
    </ul>
</div>

```
Our markup is complete, but we need to improve our code a little as the project title and its description are breaking our design! 

Let's create two methods, one to trim the title and one for the description text.

### The trimText and trimTitle methods
The `trimTitle` method will replace all `-` and `_` with a space, and restrict the number of characters to 12. The `trimText` method instead only reduces the number of characters of the description in excess of 100 characters. 

```js
trimTitle: function(text){
    let title = text.replaceAll("-", " ").replace("_", " ")
    if(title.length > 15) {
        return title.slice(0, 12) + ' ...'
    } return title;

},
trimText: function(text){
    //console.log(text.slice(0, 100));
    if(text.length > 100) {
        return text.slice(0, 100) + ' ...'
    } return text;
},

```

With these two methods, now we can update the markup and use them to make sure nothing breaks the design.

Let's update these two lines that will be changed from this:
```html
<!-- Create a custom method to trim the project name so that it doesn't break the design -->
<h3>{{project.name}}</h3>
<!-- Create a custom trimmedText to trim the description -->
<p>{{project.description}}</p>   
```

To this:
```html
<h3>{{trimedTitle(project.name)}}</h3>
<p>{{trimedText(project.description)}}</p>   
```


Let's put eveything together. The final markup will be the following:

```html
<div>
    <header id="site_header" class="container d_flex">
        <div class="bio__media">
            <img src="./assets/img/avatar.svg" alt="">
            <div class="bio__media__text">
                <h1>John Doe</h1>
                <h3>Python Expert</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
            </div>
        </div>
        <nav>
            <router-link to='/'>Home</router-link>
            <router-link to="/projects">Project</router-link>
            <a href="https://">
                <i class="fab fa-github fa-lg fa-fw"></i>
            </a>
        </nav>
    </header>

        <main class="container">
        <div class="error" v-if="errors"> 
            Sorry! It seems we can't fetch data righ now 😥
        </div>

        <section id="portfolio" v-else>
            <div class="loading" v-if="loading">😴 Loading ... </div>
            <div class="projects" v-else>
                    <div v-for="project in projectsList" class="card__custom" >
                    <div class="card__custom__text">
                        <div>
                            <h3>{{trimedTitle(project.name)}}</h3>
                            <p>{{trimedText(project.description)}}</p>                        
                        </div>
                
                        <div class="meta__data d_flex">
                            <div class="date">
                                <h5>Updated at</h5>
                                <div>{{new Date(project.updated_at).toDateString()}}</div>
                            </div>
                            <img class="avatar" :src="project.owner.avatar_url">
                
                        </div>
                    </div>
                    <div class="card__custom__img"></div>
                    <div class="card_custom__button">
                        <a :href="project.html_url" target="_blank">
                            Code
                        </a>
                    </div>
                
                
                </div>


                <div style="text-align: center; width:100%" v-if="!loading" >
                    <div v-if="projectsList.length < projects.length">
                        <button class="btn_load_more" v-on:click="loadMore()">Load More</button>
                    </div>
                    <div v-else>
                        <a href="" target="_blank" rel="noopener noreferrer">Visit My GitHub</a>
                    </div>

                </div>

                <div id="skills_section">
                    <h2>Development Skills</h2>
                    <ul class="skills">
                        <li v-for="skill in skills">{{skill}}</li>
                    </ul>
                </div>
            </div>
        </section>  
    </main>
</div>

```

There is one last thing to do. Since fetching data from GitHub is very fast we don't really see the loading message. Let's set a timeout and delay it by a few seconds – then you can tune it as you like.

### The mounted lifecycle hook

```
 mounted(){  

        setTimeout(this.fetchData, 3000 );
        
    }
```
Inside the mounted lifecycle hook we used `setTimeout()` and called the `fetchData` method as the first parameter. Then for the second parameter we specified that this method should be executed after 3000 milliseconds (3seconds). 


## Let's see our final code all toghether
Index.html file looks like the following:

```html

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vuefolio</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100;300;400;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.1.1/css/all.css"
        integrity="sha384-O8whS3fhG2OnA5Kas0Y9l3cfpmYjapjI0E4theH4iuMD+pLhbf6JI0jIMfYcK3yZ" crossorigin="anonymous">
    <link rel="stylesheet" href="./assets/css/style.css">
</head>

<body>

    <div id="app">

        <!-- Render the component for the corresponding route -->
        <router-view></router-view>

    </div>
    <footer> © Developed by <a href="https://fabiopacifici.com">Fabio Pacific</a> </footer>
    <!-- Axios -->
    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <!-- VueJS development version -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <!-- Vue Router -->
    <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>
    <!-- Main Js file -->
    <script src="./assets/js/main.js"></script>
</body>

</html>

```

And this is the main.js file:

```js
// Create route components
const Home = {
    template: 
    `<main id="home">
        <div class="about__me">
            <img src="./assets/img/avatar.svg" alt="">
            <h1>John Doe</h1>
            <h3>Python Expert</h3>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
    
            <div class="skills_projects_link"><router-link to="/projects">Projects/Skills</router-link> </div>
        </div>
    </main>`
}
const Projects = {
    template: 
    `<div>
        <header id="site_header" class="container d_flex">
            <div class="bio__media">
                <img src="./assets/img/avatar.svg" alt="">
                <div class="bio__media__text">
                    <h1>John Doe</h1>
                    <h3>Python Expert</h3>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. </p>
                </div>
            </div>
            <nav>
                <router-link to='/'>Home</router-link>
                <router-link to="/projects">Project</router-link>
                <a href="https://">
                    <i class="fab fa-github fa-lg fa-fw"></i>
                </a>
            </nav>
        </header>
    
         <main class="container">
            <div class="error" v-if="errors"> 
                Sorry! It seems we can't fetch data righ now 😥
            </div>

            <section id="portfolio" v-else>
                <div class="loading" v-if="loading">😴 Loading ... </div>
                <div class="projects" v-else>
                     <div v-for="project in projectsList" class="card__custom" >
                        <div class="card__custom__text">
                            <div>
                                <h3>{{trimedTitle(project.name)}}</h3>
                                <p>{{trimedText(project.description)}}</p>                        
                            </div>
                    
                            <div class="meta__data d_flex">
                                <div class="date">
                                    <h5>Updated at</h5>
                                    <div>{{new Date(project.updated_at).toDateString()}}</div>
                                </div>
                                <img class="avatar" :src="project.owner.avatar_url">
                    
                            </div>
                        </div>
                        <div class="card__custom__img"></div>
                        <div class="card_custom__button">
                            <a :href="project.html_url" target="_blank">
                                Code
                            </a>
                        </div>
                    
                    
                    </div>


                    <div style="text-align: center; width:100%" v-if="!loading" >
                        <div v-if="projectsList.length < projects.length">
                            <button class="btn_load_more" v-on:click="loadMore()">Load More</button>
                        </div>
                        <div v-else>
                            <a href="" target="_blank" rel="noopener noreferrer">Visit My GitHub</a>
                        </div>

                    </div>

                    <div id="skills_section">
                        <h2>Development Skills</h2>
                        <ul class="skills">
                            <li v-for="skill in skills">{{skill}}</li>
                        </ul>
                    </div>
                </div>
            </section>
        
           
        </main>
    </div>`,
data() { 
    return {
        data: [],
        projects: [],
        projectsList: null,
        skills: [],
        projectsCount: 5,
        perPage: 20,
        page: 1,
        loading: true,
        errors: false,
        }
    },
    methods: {
        trimedTitle: function(text){
            let title = text.replaceAll("-", " ").replace("_", " ")
            if(title.length > 15) {
                return title.slice(0, 12) + ' ...'
            } return title;
        
        },
        trimedText: function(text){
            //console.log(text.slice(0, 100));
            if(text === null) {
                return 'This project has no description yet!';
            } else if(text.length > 100) {
                return text.slice(0, 100) + ' ...'
            } 
            return text;
        
        },
        getProjects: function(){

            this.projectsList = this.projects.slice(0, this.projectsCount);
            return this.projectsList;
        
        },
        fetchData: function(){
            axios
            .get(`https://api.github.com/users/fbhood/repos?per_page=${this.perPage}&page=${this.page}`)
            .then(
                response => {
                    this.projects = response.data;
                    this.projects.forEach(project =>{
                        if (project.language !== null && ! this.skills.includes(project.language)) { 
                            this.skills.push(project.language)
                        };
                    });
                }
            )
            .catch(error=> {
                console.log(error);
                this.errors = true;
            })
            .finally(() => { 
                this.loading = false
                this.getProjects();
            })
        }, 
        loadMore(){
            
            if(this.projectsList.length <= this.projects.length){
                this.projectsCount += 5;
                this.projectsList = this.projects.slice(0, this.projectsCount)
            }
            
        
        }
        
    },
    mounted(){  

        setTimeout(this.fetchData, 3000 );
        
    }
}

// Define routes
const routes = [
    {path: '/', component: Home},
    {path: '/projects', component: Projects},
];


// create the router instance
const router = new VueRouter({
    routes
})

// create and mount the vue instance
const app = new Vue({
    router
}).$mount('#app');

```

On the CSS side this is what we have:

```css

/* Utility Classes */
.d_none {
    display: none;
}
.d_flex {
    display: flex;
}
.container {
    max-width: 1170px;
    margin: auto;
}
a {
    color: white;
} 
a:hover {
    color:#DB5461;
    
}
.loading {
    font-size: 2rem;
}
/* END Utility Classes */
/* Components */
.bio__media {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    text-align: left;
}
.bio__media img {
    height: 120px;
}
.bio__media__text {
    padding: 1rem;
}
.bio__media__text h1{
    font-size: 36px;
    font-weight: 900;
    color: #DB5461;

}
.bio__media__text p {
    font-weight: 100;
    font-size: 16px;
    line-height: 1.5rem;
    
}

.card__custom {
    position: relative;
    display: flex;
    max-width: 400px;
    height: 300px;
    min-height: 300px;
    padding: 0.5rem;
    margin-bottom: 3rem;
    flex-grow: 1;
    flex-basis: calc(100% /2);
    align-items: center;
    justify-content: space-between;
}
.card__custom > .card__custom__text {
    max-width: calc((100% / 3) *2);
    text-align: right;
    height: 80%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    overflow: hidden;

}
.card__custom__img {
    
    position: absolute;
    width: 70%;
    height: 100%;
    background-image: url(../img/cards_bg_img.svg);
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain;
    display: inline-block;
    z-index: -1;
    left: 60%;
    transform: translateX(-50%);
    border-radius: 85px 0 100px 25px;

}
.card_custom__button a, .btn_load_more {
    background: #F1EDEE;
    border: 5px solid #3D5467;
    box-sizing: border-box;
    border-radius: 54px;
    padding: 0.5rem 1rem;
    font-weight: 900;
    color: #3D5467;
}
.card_custom__button a:hover, .btn_load_more:hover {
    cursor: pointer;
    background: #324555;
    color: white;
    border-color: #DB5461;
    transition: 1s;
}
.card__custom__text h3 {
    text-transform: uppercase;
    font-size: 1.5rem;
}
/* END Componenet */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body{
    font-family: 'Raleway', Arial, Helvetica, sans-serif;
    color: white;
    background: linear-gradient(116.82deg, #3D5467 0%, #1A232B 99.99%, #333333 100%);

}
a {
 text-decoration: none;   
}

/* Home Page */
main#home {
    width: 100%;
    height: 100vh;
    min-height: 600px;
    display: flex;
    justify-content: center;
    align-items: center;
}
#home > .about__me {
    text-align: center;
    width: 80%;
    line-height: 1.5rem;
}
#home > .about__me > h1 {
    margin: 20px 0 0;
    font-size: 36px;
    font-weight: 900;
    color: #DB5461;
}
#home > .about__me > h3 {
    font-size: 28px;
    font-weight: 500;

}
#home > .about__me > h1, #home > .about__me > h3  {
    font-style: normal;
    line-height: 42px;
    letter-spacing: 0.115em;

}
#home > .about__me p {
    font-weight: 100;
    font-size: 22px;
    padding: 2rem;
}
.skills_projects_link {
    position: relative;
}
.skills_projects_link > a {
    text-transform: uppercase;
    color: white;
    font-weight: 900;
    font-size: 18px;
    line-height: 21px;

}
.skills_projects_link > a:hover {
    color: #DB5461;
    transition: all 0.5s ease-in-out;

}
.skills_projects_link > a:hover::after {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    margin: auto;
    text-align: center;
    content: "";
    width: 30px;
    height: 2px;
    background-color: #DB5461;
    transition: background-color 0.5s ease-in-out;

}

/* Header */
#site_header {
    text-align: center;
    padding: 2rem 0;
    justify-content: space-between;
    align-items: center;
}
#site_header > h1 {
    text-transform: uppercase;
}
nav a {
        color: #e2e2e2;
    text-transform: uppercase;
    font-weight: 900;
}
nav a:hover {
    color: #DB5461;
}
/* Portfolio Page Section */

#portfolio {
    margin-top: 4rem;
    
}


#portfolio .projects {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-around;
}
/* Skills */

#skills_section {
    margin-top: 4rem;
    min-height: 300px;
    background-image: url(../img/skills_bg.svg);
    background-repeat: no-repeat;
    background-size: contain;
    background-position: top left;
}
#skills_section h2 {
    margin-left: 180px;
    font-size: 44px;
    color: #F1EDEE;
    line-height: 2rem;

}
#skills_section ul {
    list-style: none;
    margin: 20px 120px;
    display: flex;
    flex-wrap: wrap;

}
#skills_section ul  li {
    padding: 1rem;
    margin: 0.5rem;
    background-color: #DB5461;
    border: 5px solid #3D5467;
    border-radius: 35px;
}



.avatar {
    width: 30px;
    height: 30px;
    border-radius: 50%;
        margin: 0 1rem;

}


.card__back {
    display: none;
}
.rotate__card {
    transform: rotate3d(360,0,0,180deg);
}
/* Site Footer */

footer {
    text-align: center;
    padding: 2rem 0;
}



/* Media Query  */

@media screen and (max-width: 475px) {
    .card {
        flex-basis: 100%;
        width: 100%;
    }
}

```

That's it! We are ready to deply our code to production.


%[https://youtu.be/I6hQnWQU4rQ]

## Continuos Deployment with BitBucket and Netlify

The final step is to deploy our projects so that others can see them. To do that we will use two services:

- BitBucket, a git-based source code repository for hosting (you can use GitHub if you prefer)
- Netlify, a web hosting company that provides hosting for websites that have source code files stored in a Git version control system.

You can watch this final video on [YouTube here](https://youtu.be/BH5I68DzcYQ).

You can also checkout the final repositories on BitBucket: 
- [SimpleTwitter](https://bitbucket.org/fbhood/simple-twitter/src/master/)
- [VuePortfolio](https://bitbucket.org/fbhood/vue-folio/src)


### Create the project folders and copy all files
First, create two folders – one for each project:
- vue-folio
- simple-twitter
then copy all projects files in the related folder.

### Initialize a git repository
Next, we need to initialise the git repository locally.

```
cd vue-folio 
git init
git add .
git commit -m"Initial Commit"
```
You need to execute the commands above in a termial, so you need to have git installed on you system. If you don't, you can read about how to do that [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

With the first command, we navigate to the project folder called `vue-folio`. Then we initialise a git repository, add all files to the staging area, and commit the files.

Repeat the steps above for both projects folders.

### Create a BitBucket or GitHub repository
I assume you already have an account with GitHub o BitBucket. But if you don't, then go over and create one.

Follow the steps in the video to create the repositories and connect them with you local repositories.


### Create an account with Netlify and create a site
You can use Netlify's free plan for private projects, hobby websites, and experiments. It's a perfect fit for our tutorial. 

Follow the steps in the video to deploy your projects there.



%[https://youtu.be/BH5I68DzcYQ]

## What's Next?
In an upcoming tutorial I'll show you also how to test your code, upgrade to Vue3, and more.

### Thank you for reading!

I hope you enjoyed this tutorial and the accompanying videos. If so, please share the article and hit the like button on the videos. You can also enable notifications by clicking on the bell icon to know when my next video is online. 

If you have any questions please just reach out to me. I reply to all YouTube comments. 

Dont forget to subscribe to my YouTube Channel [here](https://youtube.com/channel/UCTuFYi0pTsR9tOaO4qjV_pQ).

