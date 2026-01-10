---
title: Learn Svelte in 5 Minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-08T20:49:08.000Z'
originalURL: https://freecodecamp.org/news/learn-svelte-in-5-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-06-at-16.10.39.png
tags:
- name: framework
  slug: framework
- name: JavaScript
  slug: javascript
- name: Svelte
  slug: svelte
seo_title: null
seo_desc: "By Leanne Rybintsev\nThis article gives you a lightning-speed overview\
  \ of Svelte - a Javascript framework which lets you write less code, use no virtual\
  \ DOM, and create truly reactive apps. \nAs if that's not enough, Svelte is super-intuitive\
  \ too! Buil..."
---

By Leanne Rybintsev

This article gives you a lightning-speed overview of Svelte - a Javascript framework which lets you write less code, use no virtual DOM, and create truly reactive apps. 

As if that's not enough, Svelte is super-intuitive too! Built with developers in mind, it is designed to make coding easier, bug-squashing quicker, and a developer's work life generally happier. 

If that sounds right up your street, then read on!

While 5 minutes won't be enough to teach you Svelte in depth, it does allow for a solid overview of the basics, including:

- Components
- Importing and Exporting
- Templating
- Event handling
- Event dispatching
- Reactivity

If you want to find out more about Svelte after reading this article, check out [the full course](https://scrimba.com/course/glearnsvelte?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article) over on Scrimba. There, you'll learn about even more Svelte features and have the chance to road test your new skills with a bunch of interactive challenges. 

For now, let's get started on the basics!

## Components

[![DOM displaying Svelte component](https://dev-to-uploads.s3.amazonaws.com/i/e8ej7929dpa3u9tzsm0u.png)](https://scrimba.com/p/pG6X6UG/cNDg9yHB?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article)
*(Click the image to access the course.)*

First, we'll take a look at how to build a Svelte component, which can contain three parts; `<script>`, which contains Javascript, `<style>`, which contains CSS and the HTML, which uses the JS from the `<script>` tag. 

```js
<script>
    let say = 'hi';
</script>

<style>
    div {
        color: red;
    }
</style>

<div>
    Say: {say}
</div>
``` 
**Note:** The bare minimum needed for a Svelte component is the HTML, so the app will still work without the `<script>` and `<style>` tags.

## Importing and Exporting

One big benefit of using frameworks is the ability to modularise code by splitting it into separate components. Components are then imported into the main app using `import` keyword: 

```js
  import Face from './Face.svelte';
```

Unlike with other frameworks, the `export` keyword is not required to use a component elsewhere in an app. Instead, it is used to pass parameters, or props, from parent elements to their children. 

For example, we can set a size prop with a default size in our component:
```js
<script>
    export let size = 1;
</script>

<div style="font-size: {size}em">=)</div>
```

This allows us to easily adjust the size of the imported component over in our `App.svelte` file: 
```js
<script>
    import Face from './Face.svelte';
</script>

<Face size="4" />
<Face size="10" />
<Face />
```
The various sizes appear on the DOM as follows:

[![component imported with various sizes using props](https://dev-to-uploads.s3.amazonaws.com/i/3aecnw1qq3xpcck19agr.png)](https://scrimba.com/p/pG6X6UG/cbDNVncg?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article)
*(Click the image to access the course.)*

Head over to [the course on Scrimba](https://scrimba.com/p/pG6X6UG/cbDNVncg?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article) to view and play around with the full code. 

## Templating

The Svelte [templating syntax](https://scrimba.com/p/pG6X6UG/cMZrQds2?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article) is a great feature which lets us add if statements and for loops to our HTML.

The syntax for an if statement looks like this:
```js
<Container>
    {#if say}
        <div>
            Hi!
        </div>
    
    {/if}
</Container>
```

While a for loop is as follows:
```js
{#each [2,1,0] as faceIndex}
        <Face index={faceIndex} />
    {/each}
```

## Event handling
To allow the user to interact with our app, we need event handlers. In [this scrim](https://scrimba.com/p/pG6X6UG/caZ3J6U3?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article), we see how to add a simple `on:click` to a `<button>` to show our app's header:
```js
<button on:click={() => {showHeader = true}}>show</button>
```
And what a header it is..!
[![header made visible on the DOM with an event handler](https://dev-to-uploads.s3.amazonaws.com/i/czgdba1dpkzu552kq2hq.png)](https://scrimba.com/p/pG6X6UG/caZ3J6U3?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article)
*(Click the image to access the course.)*

There is a gotcha with this, though - it only works with the native HTML `<button>` tag and not imported components called `<Button>`. 

Luckily, we can work around this by using **event forwarding**, i.e. adding an `on:click` to the native `<button>` tag in its component file:
```js
<button on:click>
        <slot></slot>
</button>
```

## Event dispatching

[![Hide and show buttons created with event dispatcher](https://dev-to-uploads.s3.amazonaws.com/i/w203a2wxgn1brk5ss6i4.png)](https://scrimba.com/p/pG6X6UG/cD4bKDuD?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article)
*(Click the image to access the course.)*
Event dispatching is a great feature of Svelte which increases code usability by allowing us to use the same element for more than one action.

In [this scrim](https://scrimba.com/p/pG6X6UG/cD4bKDuD?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article), we learn how to use one `<Button>` component to both show and hide an element. 

We create an event dispatcher in the `<Button>` component file like this:
```js
<script>
    import {createEventDispatcher} from 'svelte';
    const dispatch = createEventDispatcher();    
</script>
```
We then add the dispatcher to our native HTML `<button>` like this:
```js
<button on:click={() => dispatch('show')}>
    Show
</button>
<button on:click={() => dispatch('hide')}>
    Hide
</button>
```
Lastly, we declare the button's functionality options in the `App.svelte` file as follows: 
```js
<Buttons on:show={() => {showHeader = true}} on:hide={() => {showHeader = false}} />
```
We can refactor this by passing values up through the dispatch using the event variable (`e`). In this case, the `<Button>` in our `App.svelte` file looks like this:
```js
<Buttons on:click={(e) => {showHeader = e.detail}} />
```
While the native HTML `<button>`s in our component file look like this:
```js
<button on:click={() => dispatch('click', true)}>
    Show
</button>
<button on:click={() => dispatch('click', false)}>
    Hide
</button>
```

## Reactivity
If you want a piece of code to rerun every time its associated variable is updated, then Svelte's unique feature, [the reactive statement](https://scrimba.com/p/pG6X6UG/caZ3yBAB?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article), is for you. We declare a reactive statement with `$:` as follows: 
```js
let score = 0;
    $: smileySays = 'Hi there, your score is: ' + score;
```

It's also possible to run if statements inside reactive statements. The code to do so looks like this:
```js
let score = 0;
    $: smileySays = 'Hi there, your score is: ' + score;
    $: if (score < -4) smileySays = 'Wow your score is low!'
```

That's about all the features we can cram into our 5-minute tour of Svelte. I hope you found it useful and are inspired to try out the framework for yourself and test your new-found skills. 

Don't forget to check out the full course [over at Scrimba](https://scrimba.com/course/glearnsvelte?utm_source=dev.to&utm_medium=referral&utm_campaign=glearnsvelte_5_minute_article) to find out about even more Svelte features and give the coding challenges a try.

Wherever your coding journey takes you next, happy learning :) 



