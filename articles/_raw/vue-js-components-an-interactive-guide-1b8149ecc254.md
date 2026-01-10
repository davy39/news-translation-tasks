---
title: 'Vue Components: An Interactive Vue JS Tutorial'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-17T21:46:52.000Z'
originalURL: https://freecodecamp.org/news/vue-js-components-an-interactive-guide-1b8149ecc254
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ieROYZuCX-w0p9V7UswJbQ.png
tags:
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  In my previous tutorial we learned the basics of Vue.js: the Vue instance, the template
  syntax, data object, directives, methods and more. This was enough to get started
  creating with very basic Vue examples.


  Note: check out thi...'
---

By Per Harald Borgen

In [my previous tutorial](https://medium.freecodecamp.org/learn-basic-vue-js-crash-course-guide-vue-tutorial-e3da361c635) we learned the basics of Vue.js: the Vue instance, the template syntax, data object, directives, methods and more. This was enough to get started creating with very basic Vue examples.

> **Note:** check out [this playlist](https://scrimba.com/playlist/playlist-38?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) if you’re interested in watching all my Vue screencasts.

But if you want to build proper apps with Vue, you’ll need to learn about components. It’s one of the most powerful features of the library.

![Image](https://cdn-media-1.freecodecamp.org/images/lU7kIfogtoKiBbhLmwBSdmeDhUlQUJ0Iyj-J)

Components makes your code more reusable and your markup more readable.

They’ll let you create custom HTML elements, which will behave exactly how you want them to. To create a Vue.js component, do the following:

```vue
Vue.component('my-component', {
  template: '<div>A custom component!</div>'
})

new Vue({
    el: '#app'
})
```

The `template key` is where you write your markup for that component. In the same object you’ll later add more functionalities. You create an **instance** of your component through adding `<my-component></my-co`mponent> in the HTML:

```vue
<div id="app">
      <my-component></my-component>
</div>
```

This will result in the following being rendered on the page:

![Image](https://cdn-media-1.freecodecamp.org/images/wOT9PJkSfHw2lU2c81dIYeOZwGu1rs01bcAi)

Here is a [Scrimba screencast](https://scrimba.com/casts/crNKWHd?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) explaining the same concept. It’s interactive, so you can pause the screencast and edit the code whenever you want.

![Image](https://cdn-media-1.freecodecamp.org/images/uAUTlrqpj7seczMdm9GIFaYMqKLrbP2gaibK)

### Props

The component above doesn’t do much. To make it a bit more usable, let’s add props to it:

```vue
Vue.component('my-component', {
  props: ['message'],
  template: `<div>{{ message }}</div>`,
})
```

Props will enable you to pass data into a component instance from the outside of that component. Or more correctly, pass the data down from a parent.

The `my-component` has one prop called `message`, which it’ll render out. The value of `message` will be defined when we create new instances of this component in the DOM. We can create as many `my-component`’s as we want, and give each of them different props. Thus we’ll be able to re-use our code.

To pass data down as the `message` prop, simply do the following:

```vue
<div id="app">
      <my-component message="Hello from Vue.js!"></my-component>
</div>
```

Now, **Hello from Vue.js!** will be rendered on the page.

But this is still a very static solution, as we’ve hard coded the value of the prop in the HTML. A better solution would be to bind this value to a data source. Then we can change it how we want later on, like based upon user interactions or responses from API’s.

Let’s bind it to the data object on our Vue instance. First we’ll create the data object.

```vue
var app = new Vue({
    el: '#app',
    data: {
      msg: 'Hello from the Vue instance'
    }
})
```

To bind the prop in `my-component` to the `msg` in our Vue instance, we’ll use the `v-bind` directive we learned in the previous article:

```vue
<div id="app">
      <my-component v-bind:message="msg"></my-component>
</div>
```

Now, we can change the data through `app.msg = 'Some new data'` and Vue will take care of updating the DOM with the new data.

> **_Tip:_** _You can remove the `v-bind` from `v-bind:message` and rather use the `:message` shorthand._

Here is a [Scrimba screencast](https://scrimba.com/casts/caPgLTP?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) explaining the concept:

![Image](https://cdn-media-1.freecodecamp.org/images/PJ7UGwbOgARBGkj7JjkCRMmkeges8UAcnR2U)

But what if you want your component to be able to change its `message`? This can’t happen as long as `message` is a prop, as you should never mutate a prop inside a component. If you try to, Vue will give you a warning in the console.

### Data

So we’ll need another way of handling data inside the component. This is where the `data` function comes into play. It will allow your components to handle internal state, which you can change how you wants to.

Component `data` fills the same role as the `data` object in the Vue instance. They’re both places where you’ll hold mutable data. But, component `data` is a **function** and not an **object**.

Let’s jump into the code, to make it less abstract.

```vue
Vue.component('my-component', {
  template: '<div> {{ message }} </div>',
  data: function() {
    return {
      message: 'Hello from Vue data!'
    }
  }
})
```

Here is a [Scrimba screencast](https://scrimba.com/casts/c2LmGU2?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) which explains the concept.

![Image](https://cdn-media-1.freecodecamp.org/images/TwF5iKb1ozpTfkLRX6V9H7AfLwFPClUgco00)

And that’s about it! There are of course many more things to learn about Vue components. But this should be enough for you to start playing around with it on your own.

If you learn something new about Vue, I’d recommend you to pass that knowledge on to others as well. That’s one of the best ways to learn, and the reason that communities like [freeCodeCamp](https://www.freecodecamp.com/) thrive.

So go ahead and write an article (or create a [Scrimba](http://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) screencast) about your what you’ve learned!

