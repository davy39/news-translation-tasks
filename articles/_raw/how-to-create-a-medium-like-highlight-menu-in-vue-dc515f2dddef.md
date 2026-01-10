---
title: How to Create a Medium-Like Highlight Menu in Vue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T17:57:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-medium-like-highlight-menu-in-vue-dc515f2dddef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gL6zqT6rsqYsl8-evfS2vg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Taha Shashtari

  A cool feature in Medium is the highlight menu that pops up when you select some
  text. This menu contains buttons that allow you to perform certain actions on the
  selected text like highlight and share.

  If you like this feature and ...'
---

By Taha Shashtari

A cool feature in [Medium](https://medium.com/) is the highlight menu that pops up when you select some text. This menu contains buttons that allow you to perform certain actions on the selected text like highlight and share.

If you like this feature and you want to have it in your site, I’m going to show you how to create a reusable component that enables this behavior on the text it contains.

You can try a live demo on CodePen:

_View the CodePen [here](https://codepen.io/tahazsh/pen/WYywXW)._

### Creating a new project with Vue CLI 3

With Vue CLI 3 [instant prototyping](https://cli.vuejs.org/guide/prototyping.html#vue-serve), we can rapidly run a Vue app with just a single `*.vue` file.

Note that this is only used for creating prototypes, not for production.

First, make sure that you have this installed globally:

`npm install -g @vue/cli-service-global`

In this app, we’ll only need two files: _App.vue_ and _Highlightable.vue_.

_Highlightable.vue_ is our reusable highlight menu component. And _App.vue_ is the main page component.

Create both files in any directory you want; then, run `vue serve` on _App.vue_.

```
vue serve App.vue
```

### Implementing App.vue

In _App.vue_, we'll add two paragraphs. One that can be highlighted, and one that can't.

We’ll also import and use _Highlightable.vue_ before even creating it. (This is helpful to see how we're going to use it.)

Here’s how it should look in the end:

```
<template>  <div class="app">    <highlightable      @share="onShare"      @highlight="onHighlight"    >      <p>        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet at debitis deserunt, optio rem eaque obcaecati non possimus nisi assumenda architecto exercitationem dolore quo praesentium, deleniti reiciendis sed ab nihil!      </p>    </highlightable>    <p>      <strong>This paragraph can't be highlighted.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Labore ipsam repellat, fugiat aut ex incidunt ut quisquam quasi consequatur ducimus quo in, cum soluta eos dolores tempore unde voluptate modi.    <;/p&gt;  </div></template&gt;<script>import Highlightable from './Highlightable'export default {  components: { Highlightable },  methods: {    onShare (text) {      console.log('share:', text)    },    onHighlight (text) {      console.log('highlight:', text)    }  }}</script><style scoped>* {  box-sizing: border-box;}.app {  width: 800px;  margin: 40px auto;  padding: 10px;  font-family: Verdana;  color: #333;  width: 100%;}p {  line-height: 1.5;}</style>
```

As you can see above, we're handling two events from _Highlightable_. These two events are the actions of the buttons in the highlight menu. These are just examples. You can change them to whatever you want.

### Implementing Highlightable.vue

The template section consists of two parts: the menu element with buttons and `<slo`t/> to display the text.

Let’s start with this code in the _template_:

```
<template>  <div>    <div      v-show="showMenu"      class="menu"    >      <span class="item">        Share      </span>      <span class="item">        Highlight      </span>      <!-- You can add more buttons here -->    </div>    <!-- The insterted text should be displayed here -->    <slot/>  </div></template>
```

Note that we're using `showMenu`, which we haven't created yet, to determine if we should display the menu.

Now let's move to the styling part.

Add the following CSS to `<sty`le> section:

```
&lt;style scoped>.menu {  height: 30px;  padding: 5px 10px;  background: #333;  border-radius: 3px;  position: absolute;  top: 0;  left: 0;  transform: translate(-50%, -100%);  transition: 0.2s all;  display: flex;  justify-content: center;  align-items: center;}.menu:after {  content: '';  position: absolute;  left: 50%;  bottom: -5px;  transform: translateX(-50%);  width: 0;  height: 0;  border-left: 6px solid transparent;  border-right: 6px solid transparent;  border-top: 6px solid #333;}.item {  color: #FFF;  cursor: pointer;}.item:hover {  color: #1199ff;}.item + .item {  margin-left: 10px;}&lt;/style>
```

Nothing is too complex here. `.menu` is for the highlight menu. `menu:after` is for the little triangle (arrow) in the bottom center of the menu.

One important thing to note here is that `.menu` has an `absolute` position. We need this to position it above the selected text.

Finally, let's move to the `<scri`pt> section.

Let's start with the _data_.

```
export default {  data () {    return {      x: 0,      y: 0,      showMenu: false,      selectedText: ''    }  }}
```

* `x` and `y` are for positioning the menu.
* `showMenu` to show/hide the menu.
* `selectedText` will contain the actual content of the selected text.

Now, let's move to _computed_.

```
computed: {  highlightableEl () {    return this.$slots.default[0].elm  }}
```

We only have a single computed property that returns the element used in the slot section of _Highlightable_. In our example, it would be the `<`;p> tag be`tween <highlightable><`/highlightable>.

Then, let's add `mounted` and `beforeDestroy` hook functions.

```
mounted () {  window.addEventListener('mouseup', this.onMouseup)},beforeDestroy () {  window.removeEventListener('mouseup', this.onMouseup)}
```

We use these to listen for `mouseup` event, which we handle inside `onMouseup` method.

Now, let's create `onMouseup` method.

```
methods: {  onMouseup () {    const selection = window.getSelection()    const selectionRange = selection.getRangeAt(0)    // startNode is the element that the selection starts in    const startNode = selectionRange.startContainer.parentNode    // endNode is the element that the selection ends in    const endNode = selectionRange.endContainer.parentNode    // if the selected text is not part of the highlightableEl (i.e. <p>)    // OR    // if startNode !== endNode (i.e. the user selected multiple paragraphs)    // Then    // Don't show the menu (this selection is invalid)    if (!startNode.isSameNode(this.highlightableEl) || !startNode.isSameNode(endNode)) {      this.showMenu = false      return    }    // Get the x, y, and width of the selection    const { x, y, width } = selectionRange.getBoundingClientRect()    // If width === 0 (i.e. no selection)    // Then, hide the menu    if (!width) {      this.showMenu = false      return    }    // Finally, if the selection is valid,    // set the position of the menu element,    // set selectedText to content of the selection    // then, show the menu    this.x = x + (width / 2)    this.y = y + window.scrollY - 10    this.selectedText = selection.toString()    this.showMenu = true  }}
```

Now let's update the template of _Highlightable.vue_ to reflect the new changes.

```
<template>  <div>    <div      v-show="showMenu"      class="menu"      :style="{        left: `${x}px`,        top: `${y}px`      }"      @mousedown.prevent=""    >      <span        class="item"        @mousedown.prevent="handleAction('share')"      >        Share      </span>      <span        class="item"        @mousedown.prevent="handleAction('highlight')"      >        Highlight      </span>      <!-- You can add more buttons here -->    </div>    <!-- The insterted text should be displayed here -->    <slot/>  </div></template>
```

The changes are:

* Applied the positions to the menu element.
* Added `@mousedown.prevent=""` to the menu element to prevent the menu from closing when clicking inside it.
* Added `@mousedown.prevent="handleAction('share')"` on share button to handle the clicked action. The same is for the highlight action.

Note that we're using `mousedown` event instead of `click` to prevent the text from getting unselected — which would cause the menu to close.

The last thing we have to do is add the `handleAction` method.

```
handleAction (action) {  this.$emit(action, this.selectedText)}
```

This method emits the `action` event and passes the selected text along with it. (We used this event in _App.vue_, remember?)

With that, we're done! Now you have a reusable component that you can use to show a highlight menu for the selected text, just like Medium does.

_Thanks for reading! By the way, I’m writing a book on how to build a complete single-page application from scratch using Vue. Check out the book’s landing page if you’re interested in learning more about what the book will cover:_

![Image](https://cdn-media-1.freecodecamp.org/images/1*L2FgqLU76lIbry3RZYFY8g.png)

