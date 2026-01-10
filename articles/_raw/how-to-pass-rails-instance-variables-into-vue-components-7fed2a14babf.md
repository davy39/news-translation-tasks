---
title: How to pass Rails instance variables into Vue components
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T09:54:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-pass-rails-instance-variables-into-vue-components-7fed2a14babf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5FJEL2CTeSHvTBsCJd0YFQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Rails
  slug: rails
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Gareth Fuller

  I’m currently working with a legacy Rails application. We are slowly transitioning
  the front-end from Rails views to a Vue application.

  As part of this transition, we have some elements that we want to turn into global
  Vue components...'
---

By Gareth Fuller

I’m currently working with a legacy Rails application. We are slowly transitioning the front-end from Rails views to a Vue application.

As part of this transition, we have some elements that we want to turn into global Vue components. We want to be able to use these components within our existing Rails views and within a Vue application without having to customize each component to handle both situations.

Before I share my solution to this problem, here is an example single file Vue component that we want to be able to use in both scenarios (Rails view and Vue Application):

```
// Payments.vue
```

```
<template lang="html">  <div id="payments>    <div class="payment" v-for="payment in payments>      {{ payment.amount }}    </div>  </div></template>
```

```
<script>export default {  name: 'payments'
```

```
  props: {    payments: { type: Array }  }}</script>
```

```
<style lang="scss" scoped></style>
```

From within a Vue app, this is a straightforward component to use, right? For example:

```
// app/javascript/App.vue
```

```
<template lang="html">  <div id="app>    <payments :payments="payments" />  </div></template>
```

```
<script>import Payments from './Payments.vue'
```

```
export default {  name: 'app',
```

```
  components: { Payments },
```

```
  data () {    return {      payments: [        { amount: 123.00 },        { amount: 124.00 }      ]    }  }</script>
```

```
<style lang="scss" scoped></style>
```

But what about using it in a Rails view?

### Solution

So a solution for using the _Payments.vue_ component in Rails looks like this:

```
// app/views/payments/index.haml
```

```
.global-comp  = content_tag 'comp-wrapper', nil, data: { component: 'payments', props: { payments: @payments } }.to_json
```

Let’s break this element down.

`.global-comp` is a div (with class “global-comp”) for mounting a super simple Vue instance. This Vue instance gives us a wrapper component to use called _CompWrapper.vue_ (we’ll get to what CompWrapper is for in a minute).

Here is the Vue instance mounted to `.global-comp`:

```
// app/javascript/packs/global_comp.js
```

```
import Vue from 'vue/dist/vue.esm'import CompWrapper from './CompWrapper'
```

```
document.addEventListener('DOMContentLoaded', () => {  const app = new Vue({    components: { CompWrapper }  }).$mount('.global-comp')})
```

All this does is make the component (_CompWrapper.vue_) available to us within a div with the class `global-comp`.

If you are using [Webpacker](https://github.com/rails/webpacker) with Rails, you will need to include this pack within your layout somewhere before the closing body tag. For example:

```
// app/views/layouts/application.haml
```

```
...
```

```
= javascript_pack_tag "global_comp"
```

#### CompWrapper.vue

This is the fun part. _CompWrapper.vue_ allows us to pass:

1. The name of the component we want to use, for example, “payments”
2. The props we want to pass to it

The whole purpose of this wrapper component is to allow us to pass Rails instance variables like `@payments` into our components as props without having to handle this from within each component like _Payments.vue._

So here is _CompWrapper.vue_:

```
// app/javascript/CompWrapper.vue
```

```
<template lang="html">  <component :is="data.component" v-bind="data.props"></component></template>
```

```
<script>import * as components from './components'
```

```
export default {  name: 'comp-wrapper',
```

```
  components,
```

```
  data () {    return {      data: {}    }  },
```

```
  created() {    this.data = JSON.parse(this.$attrs.data)  }}</script>
```

```
<style lang="scss" scoped></style>
```

The first thing the CompWrapper component is doing is taking the data attributes you set on the element in the Rails view, parsing the JSON, and setting an internal Vue data attribute with the parsed data:

```
created() {  this.data = JSON.parse(this.$attrs.data)}
```

with `this.data` set we can then use it to select the component we want to use and pass it the props we provided in our Rails view using a Vue dynamic component:

```
<component :is="data.component" v-bind="data.props"></component>
```

And that’s it!

We can now use Vue components as they’re meant to be used, but from within our rails views. ?

