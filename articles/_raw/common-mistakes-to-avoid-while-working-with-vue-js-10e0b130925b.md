---
title: Common mistakes to avoid while working with Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-04T12:22:43.000Z'
originalURL: https://freecodecamp.org/news/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CtOATbW-ewf3UHbrZVi7Iw.jpeg
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jérémy Bardon

  Looking for a front-end framework to try out, I started with React and then tried
  Vue.js.

  Unfortunately, I encountered a lot of issues with Vue.js at the very beginning.
  In this article, I’d like to share a few common issues that you...'
---

By Jérémy Bardon

Looking for a front-end framework to try out, I started with React and then tried Vue.js.

Unfortunately**,** I encountered a lot of issues with Vue.js at the very beginning. In this article, I’d like to share a few common issues that you may have to deal with when working with Vue.js. Some of these issues may seem obvious, but I figured that sharing my experience might help someone.

### Include template compiler

My first issue was a pretty basic one. The first thing to do in order to use Vue.js is to import it. If you follow the [official guide](https://vuejs.org/v2/guide/#Composing-with-Components) and use an inline template for your component, you will get a blank page.

```js
import Vue from 'vue';
var vm = new Vue({
  el: '#vm',
  template: '<div>Hello World</div>',
});
```

Note that this issue doesn’t occur when you define templates with the render function or SFC ([Single File Component](https://vuejs.org/v2/guide/single-file-components.html#ad)).

Actually, there are many [Vue builds](https://vuejs.org/v2/guide/installation.html#Explanation-of-Different-Builds). The default build exported by the NPM package is the **runtime-only build**. It doesn’t bring the template compiler.

For some background information, the template compiler works exactly like [JSX for React](https://reactjs.org/docs/introducing-jsx.html). It replaces template strings with function calls to create a Virtual DOM node.

```js
// #1: import full build in JavaScript file
import Vue from 'vue/dist/vue.js';

// OR #2: make an alias in webpack configuration
config.resolve: {
  alias: { vue: 'vue/dist/vue.js' }
}

// OR #3: use render function directly
var vm = new Vue({
  el: '#vm',
  render: function(createElement) {
    return createElement('div', 'Hello world');
  }
});
```

With SFCs, this issue does not occur. Both **vue-loader** and **vueify** are tools used to handle SFCs. They generates plain JavaScript components using the render function to define the template.

To use string templates in components, use a full Vue.js build.

In summary, to fix this issue, specify the correct build during import, or make an alias for Vue in your bundler configuration.

You should note that using string templates reduces your app performance, because the compilation occurs at runtime.

There are many more ways to define a component template, so [check out this article](https://vuejsdevelopers.com/2017/03/24/vue-js-component-templates/). Also, I recommend using the [render function in Vue instance](https://vuejsdevelopers.com/2017/09/17/vue-js-avoid-dom-templates/).

### Keep property’s reactivity

If you use React, you probably know its reactivity relies on calling the `setState` function to update the value of properties.

Reactivity with Vue.js is a bit different. It’s based on proxying the component properties. [Getter and setter](https://vuejs.org/v2/guide/reactivity.html#How-Changes-Are-Tracked) functions will be overridden and will notify updates to the Virtual DOM.

```js
var vm = new Vue({
  el: '#vm',
  template: `<div>{{ item.count }}<input type="button" value="Click" @click="updateCount"/></div>`,
  data: {
    item: {}
  },
  beforeMount () {
    this.$data.item.count = 0;
  },
  methods: {
    updateCount () {
      // JavaScript object is updated but
      // the component template is not rendered again
      this.$data.item.count++;
    }
  }
});
```

In the code snippet above, the Vue instance has a property called `item` (defined in data). This property contains an empty literal object.

During the component initialization, Vue creates a proxy under the `get` and `set` functions attached to the `item` property. Thus, the framework will watch value changes and eventually react.

However, the `count` property isn’t reactive, because it wasn’t declared at initialization time.

Actually, proxifying only occurs at component initialization time, and the`beforeMount` lifecycle function triggers later.

Besides, the `item` setter isn’t called during `count` definition. So the proxy won’t trigger and the `count` property will have no watch.

```js
beforeMount () {
  // #1: Call parent setter
  // item setter is called so proxifying is propaged
  this.$data.item = {
    count: 0
  };
  
  // OR #2: explicitly ask for watching
  // item.count got its getter and setter proxyfied
  this.$set(this.$data.item, 'count', 0);
  
  // "Short-hand" for:
  Vue.set(this.$data.item, 'count', 0);
}
```

If you keep the `item.count` affectation in `beforeMount`, calling `Vue.set` later won’t create a watch.

The exact same issue also occurs with arrays when using direct affection on unknown indexes. In such cases, you should prefer [array proxifyed functions](https://vuejs.org/v2/guide/list.html#Array-Change-Detection) such as `push` and `slice`.

Also, you can read [this article](https://vuejsdevelopers.com/2017/03/05/vue-js-reactivity/) from the Vue.js Developer’s website.

### Be careful with SFC exports

You can use Vue regularly in JavaScript files, but you can also use [Single File Components](https://vuejs.org/v2/guide/single-file-components.html#ad). It helps to gather JavaScript, HTML, and CSS code in a single file.

With SFCs, the component code is the script tag of a `.vue` file. Still written in JavaScript, it has to export the component.

There are many ways to export a variable/component. Often, we use either direct, named, or default exports. Named exports will prevent users from renaming the component. It will also be eligible for [tree-shaking](https://en.wikipedia.org/wiki/Tree_shaking).

```js
/* File: user.vue */
<template>
  <div>{{ user.name }}</div>
</template>

<script>
  const User = {
    data: () => ({
      user: {
        name: 'John Doe'
      }
    })
  };
  export User; // Not work
  export default User; // Works
</script>

/* File: app.js */
import {User} from 'user.vue'; // Not work
import User from 'user.vue'; // Works (".vue" is required)
```

Using named exports is not compatible with SFCs, be mindful about this!

In summary, exporting a named variable by default might be a good idea. This way, you will get more explicit debug messages.

### Don’t mix SFC components

Putting code, template, and style together is a good idea. Besides, depending on your constraints and opinions, you may want to keep the [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns).

As described in the [Vue documentation](https://vuejs.org/v2/guide/single-file-components.html#What-About-Separation-of-Concerns), it’s compatible with SFC.

Afterward, one idea came to my mind. Use the same JavaScript code and include it in different templates. You may point it as a bad practice, but it keeps things simple.

For instance, a component can have both read-only and read-write mode and keep the same implementation.

```js
/* File: user.js */
const User = {
  data: () => ({
    user: {
      name: 'John Doe'
    }
  })
};
export default User;

/* File: user-read-only.vue */
<template><div>{{ user.name }}</div></template>
<script src="./user.js"></script>

/* File: user-read-write.vue */
<template><input v-model="user.name"/></template>
<script src="./user.js"></script>
```

In this snippet, both read-only and read-write templates use the same JavaScript user component.

Once you import both components, you will figure out that it doesn’t work as expected.

```js
// The last import wins
import UserReadWrite from './user-read-write.vue';
import UserReadOnly from './user-read-only.vue';

Vue.component('UserReadOnly', UserReadOnly);
Vue.component('UserReadWrite', UserReadWrite);

// Renders two times a UserReadOnly
var vm = new Vue({
  el: '#vm',
  template: `<div><UserReadOnly/><UserReadWrite/></div>`
});
```

The component defined in `user.js` can only be used in a single SFC. Otherwise, the last imported SFC which uses it will override the previous.

> SFCs allow splitting code in separate files. But you can’t import thoses files in multiple Vue components.

To make it simple, don’t reuse JavaScript component code in multiple SFC components. The separate code feature is a handy syntax, not a design pattern.

Thanks for reading, hope my experience has been useful to make you avoid the mistakes I made.

**If it was useful, please click on the** ? **button a few times to make others find the article and show your support! ?**

**Don’t forget to follow me to get notified about my upcoming articles** ?

### Check out my [Other](https://medium.com/@jbardon/latest) Articles

#### ➥ JavaScript

* [How to Improve Your JavaScript Skills by Writing Your Own Web Development Framework ?](https://www.freecodecamp.org/news/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190/)
* [Stop Painful JavaScript Debug and Embrace Intellij with Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)

#### ➥ React for beginners series

* [Begin with the first article](https://www.freecodecamp.org/news/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44/)
* [Get the best practices guide](https://www.freecodecamp.org/news/the-beginners-collection-of-powerful-tips-and-tricks-for-react-f2e3833c6f12/)

