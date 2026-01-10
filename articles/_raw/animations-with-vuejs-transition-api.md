---
title: How to Build Stunning Animations with the Vue.js Transition API
subtitle: ''
author: Felix Favour Chinemerem
co_authors: []
series: null
date: '2023-10-10T15:28:04.000Z'
originalURL: https://freecodecamp.org/news/animations-with-vuejs-transition-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/supercharged-animations.png
tags:
- name: animations
  slug: animations
- name: api
  slug: api
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: "I’m easily gripped by animations and purposeful motion on the Web – so\
  \ much so that I wrote a whole article on it. \nI’m also a big fan of the Vue.js\
  \ framework, and I’ve been building apps with it for three years.\nSo it was a delightful\
  \ surprise when ..."
---

I’m easily gripped by animations and purposeful motion on the Web – so much so that I wrote a [whole article](https://favourfelix.com/stories/css-and-motion-build-animations-on-the-web/) on it. 

I’m also a big fan of the Vue.js framework, and I’ve been building apps with it for three years.

So it was a delightful surprise when I realized that I could use **only** the Transition API in Vue.js while leveraging my decent CSS skills to animate a component’s enter and exit animations in such a fluid manner.

How fluid, you might ask? Let me show you:

%[https://vimeo.com/872452747]

In this article, we'll build a straightforward movie app with built-in filtering features. By the end, you should have a solid understanding of the `<Transition>` and `<TransitionGroup>` built-in components in Vue.js and how they seamlessly handle enter and exit animations within Vue.js.

## Prerequisites

Hold on! We need a few tools in our toolkit before we dive into this adventure. This article is designed to be a breeze for beginners, but to ensure a smooth ride, here's what you'll need:

* A basic understanding of HTML, CSS, and Javascript.
* A [basic understanding of Transitions and Animations in CSS](https://www.freecodecamp.org/news/css-transition-vs-css-animation-handbook/).
* A [basic knowledge of the Vue.js framework](https://www.freecodecamp.org/news/vue-3-full-course/).
* You can also access the bare movie app without the transitions [here](https://github.com/felixfavour/supercharged-animations-vue), but only if you think it’s the boring part ;)
* Last but not least, some good background music—I’ll let you choose this one yourself, [but there's always freeCodeCamp radio](https://coderadio.freecodecamp.org/).

Ok, now we're ready to get started.

## What is the Transition API?

The Transition API primarily consists of the built-in `<Transition>` and  `<TransitionGroup>` components in Vue.

The `<Transition>` component is used for animating single elements or components. In contrast, the `<TransitionGroup>` is used for animating multiple elements in a list in conjunction with the v-for directive in Vue.

### How to Add Animations with the `<Transition>` Component

The `<Transition>` component is a built-in component that is typically wrapped around any root element or component for animation benefits. The animations are triggered when the inner element or component is shown or hidden using common Vue directives like v-show or v-if.

This component is "built-in" because it does not need to be imported into the template to be functional. It's recognized by the Vue template compiler.

We can try this out by adding a v-show to our `.header-filters` container first and wrapping the container in the `<Transition>` component like below:

```html
<Transition>
  <div v-show="filtersVisible" class="header-filters">
    <input type="search" v-model="searchQuery" placeholder="Search Movies">
    <div class="button-group">
      <button @click="query = ''" :class="{ active: query === '' }">Clear Filters</button>
      <button @click="query = '2021'" :class="{ active: query === '2021' }">2021</button>
      <button @click="query = 'Action'" :class="{ active: query === 'Action' }">Action</button>
    </div>
  </div>
</Transition>

```

We can then wrap up the animation by including styling specifications for the enter and exit animations. If you are familiar with CSS Animations and Transitions, the mode of operation is pretty similar. If you are not, here is a [quick crash course](https://favourfelix.com/stories/css-and-motion-build-animations-on-the-web/).

```css
.v-move,
.v-enter-active,
.v-leave-active {
  transition: 0.3s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
  transform: translateY(10px);
}

```

And now, you should have your fluid animations for single root elements with the `<Transition>` component. 

![Image](https://www.freecodecamp.org/news/content/images/2023/10/ezgif.com-video-to-gif--1-.gif)
_Illustration of the effect of the Transition component when an element is hidden and shown._

What if you want something similar to the video that I shared earlier? Something more mesmerizing? Well, let’s see the `<TransitionGroup>` component.

### How to Add List Animations with the `<TransitionGroup>` Component

The `<TransitionGroup>` component is wrapped around a list to animate the insertion, removal, and change of order of the items that are rendered in this list. This list is typically created with the v-for directive.

Unlike the `<Transition>` component, the elements or components wrapped in the `<TransitionGroup>` component must have unique key attributes.

```html
<TransitionGroup>
  <MovieCard v-for="movie in filteredMovies" :key="movie.title" :movie="movie" />
</TransitionGroup>
```

Aside from the instructions above, the `<TransitionGroup>` component has a similar mode of integration and operation as the `<Transition>` component.

## How to Identify and Name Transitions

A common problem when using `<Transition>` and `<TransitionGroup>` components is having multiple instances of these components in your app and using different enter and exit transitions for specific instances. This is why we name `<Transition>` and `<TransitionGroup>` components.

The `<Transition>` and `<TransitionGroup>` components accept a `name` prop that helps to identify and group transitions.

```html
<TransitionGroup name="list">
  <MovieCard v-for="movie in filteredMovies" :key="movie.title" :movie="movie" />
</TransitionGroup>

```

The `name` prop also determines the class name for styling enter and exit transitions like below:

```css
.list-move,
.list-enter-active,
.list-leave-active {
  transition: 0.3s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(10px);
}


```

Notice that the `name` prop passed in the `<TransitionGroup>` code above is “list”, and it is used as a prefix in the styles for enter and exit transitions in the CSS code above.

## How to Customize Enter and Exit Animations With CSS

In this article, we used the CSS `transition` property to help with subtle enter and exit animations. But the `<Transition>` and `<TransitionGroup>` components also support the `animation` property in CSS for much more complex animations with multiple keyframes.

Here is an example of how we can use the `animation` property in our `<Transition>` component:

### Template

```html
<Transition name="bounce">
  <div v-show="filtersVisible" class="header-filters">
    <input type="search" v-model="searchQuery" placeholder="Search Movies">
    . . .
  </div>
</Transition>


```

### Styles

```css
.bounce-enter-active {
  animation: bounce-in 0.5s;
}
.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.25);
  }
  100% {
    transform: scale(1);
  }
}

```

If the concept of keyframes or the animation property in CSS does not make much sense to you, feel free to [get a quick introduction to animations in CSS](https://favourfelix.com/stories/css-and-motion-build-animations-on-the-web/).

## Purposeful Motion on the Web

In any discussion about web animations and transitions, it's crucial to address the "why" behind them. Why should we include motion on the web, and is it genuinely indispensable?

Motion on the web serves a purpose that extends far beyond mere aesthetics. It's a powerful tool for conveying messages to your users. Whether it's to elevate your storytelling, provide user feedback, or captivate their attention, animations can play a pivotal role in enhancing your users' experience.

Gone are the days when animations were added merely for decorative purposes. In the modern web landscape, every keyframe should be thoughtfully designed with a clear purpose, and the user should always be at the heart of your design decisions.

That being said, make sure not to overuse animations – as too many moving parts can be distracting and actually detract from the user experience. It's all about balance.

## Conclusion

Phew, that was an exciting ride! I hope you enjoyed it. This article shared a lot, and I'm excited to see how you use that information. I would love to know if you built something cool while reading.

Also feel free to look into the official Vue [documentation](https://vuejs.org/guide/built-ins/transition.html) to see what else is possible with the Transition API.

Finally, have fun creating delightful experiences with animation, but always remember CSS animations are only useful to your users when they are purposeful. If you found this article helpful, feel free to connect on [favourfelix.com](http://favourfelix.com/) to see what else I'm up to.

