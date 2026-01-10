---
title: The tradeoffs of CSS-in-JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T13:40:18.000Z'
originalURL: https://freecodecamp.org/news/the-tradeoffs-of-css-in-js-bee5cf926fdb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Y-OFV7iQafRToGdyhAf8yQ.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Oleg Isonen

  Recently I wrote a higher level overview of CSS-in-JS, mostly talking about the
  problems this approach is trying to solve. Library authors rarely invest time into
  describing the tradeoffs of their solution. Sometimes it’s because they ...'
---

By Oleg Isonen

Recently I wrote a higher level [overview of CSS-in-JS](https://medium.com/@oleg008/what-is-actually-css-in-js-f2f529a2757), mostly talking about the problems this approach is trying to solve. Library authors rarely invest time into describing the tradeoffs of their solution. Sometimes it’s because they are too biased, and sometimes they just don’t know how the users apply the tool. So this is an attempt to describe the tradeoffs I have seen so far. I think it is important to mention that I am the author of [JSS](https://cssinjs.org/), so I should be considered biased.

### Social impact

There is a layer of people who work on the web platform and don’t know any JavaScript. Those people are getting paid to write HTML and CSS. CSS-in-JS has made a huge impact on the developers' workflow. A truly transformative change can never be done without some people being left behind. I don’t know if CSS-in-JS has to be the only way, but the mass adoption is a clear sign of problems with using CSS in modern applications.

A big part of the problem is our inability to communicate accurately the use cases where CSS-in-JS shines and how to use it properly for a task. Many CSS-in-JS enthusiasts have been successful at promoting the tech, but not many critics talked about the tradeoffs in a constructive manner, without taking cheap swings at the tools. As a result, we left many tradeoffs hidden and didn’t make a strong effort to provide the explanation and workarounds.

**CSS-in-JS is an attempt to make complex use cases easier to handle, so don’t push it where it is not needed!**

### Runtime cost

When CSS is generated from JavaScript at runtime, in the browser, there is an inherent overhead. Runtime overhead varies from library to library. [This](http://necolas.github.io/react-native-web/benchmarks/) is a good generic benchmark, but be sure to make your own tests. Major differences at runtime appear depending on the need to have a full CSS parsing of template strings, amount of optimizations, dynamic styles implementation details, hashing algorithm and framework integrations cost.*

Besides the potential runtime overhead, you need to consider 4 different bundling strategies, because some CSS-in-JS libraries support multiple strategies and it is up to the user to apply them. *

### Strategy 1: Runtime generation only

Runtime CSS generation is a technique that generates a CSS string in JavaScript and then injects that string using a style tag into the document. This technique produces a Style Sheet, NOT inline styles.

The tradeoff of runtime generation is the inability to provide styled content at the early stage, as the document starts loading. This approach usually fits for applications without content that can be useful immediately. Usually, such applications require user interactions before they can really become useful to a user. Often such applications work with content that is so dynamic that it becomes outdated as soon as you load it, so you need to establish an update pipeline early on, for example, Twitter. In addition, when a user is logged-in, there is no need to provide HTML for SEO.

If the interaction requires JavaScript, the bundle needs to be loaded before the app is ready. For example, you can show the contents of a default channel when loading Slack in the document, but it is likely that the user will want to change the channel right after that. So if you loaded the initial contents just to throw them away immediately.

Perceived performance of such applications can be improved with placeholders and other tricks to let the application feel more instant than it actually is. Such applications are usually data heavy anyways, so they won’t be useful as quickly as an article.

### Strategy 2: Runtime generation with Critical CSS

Critical CSS is the minimal amount of CSS that is required to style the page in its initial state. It’s rendered using a style tag in the head of the document. This technique is widely used with and without CSS-in-JS. In both cases, you are likely to double load the CSS rules, once as part of the Critical CSS and once as part of the JavaScript or CSS bundle. The size of Critical CSS can be quite large depending on the amount of the content. Usually, the document won’t be cached.

Without Critical CSS, a static content-heavy single page application with runtime CSS-in-JS will have to show placeholders instead of content. This is bad because it could have been useful to a user much earlier, improving the accessibility on low-end devices and for low-bandwidth connections.

With critical CSS, runtime CSS generation can be done at a later stage, without blocking the UI in the initial phase. Be warned though, on low-end mobile devices, which are approximately 5+ years old, CSS generation from JavaScript can have a negative impact on performance. It strongly depends on the amount of CSS being generated and the library used, so it can’t be generalized.

The tradeoff of this strategy is the cost of Critical CSS extraction and the cost of runtime CSS generation.

### Strategy 3: Build-time extraction only

This strategy is the default one on the web without CSS-in-JS. Some CSS-in-JS libraries allow you to extract static CSS at build time.* In this case, no runtime overhead is involved, CSS is rendered on the page using a link tag. The cost of the CSS generation is paid once ahead of time.

There are 2 major tradeoffs here:

1. You can’t use some of the dynamic APIs CSS-in-JS offers at runtime, because you have no access to the state. Often you still can’t use CSS custom properties, because they are not supported in every browser and cannot be polyfilled at build time by nature. In this case, you will have to do workarounds for dynamic theming and state-based styling.*
2. Without Critical CSS and with an empty cache, you will block the first paint, until your CSS bundle gets loaded. A link element in the head of the document blocks the rendering of HTML.
3. Non-deterministic specificity with page based bundle splitting in single page applications.*

### Strategy 4: Build-time extraction with Critical CSS

This strategy is also not unique to CSS-in-JS. Full static extraction with critical CSS delivers the best performance when working with a more static application. This approach still has the aforementioned tradeoffs of a static CSS, except that the blocking link tag can be moved to the bottom of the document.

**There are 4 main CSS rendering strategies. Only 2 of them are specific to CSS-in-JS and none of them apply to all libraries.**

### Accessibility

CSS-in-JS can decrease accessibility when used in the wrong way. This will happen when a largely static content site is implemented without Critical CSS extraction so that HTML can’t be painted before the JavaScript bundle is loaded and evaluated. This can also happen when a huge CSS file is rendered using a blocking link tag in the head of the document, which is the most popular current problem with the traditional embedding and not specific to CSS-in-JS.

Developers need to take responsibility for accessibility. There is still a strong misguided idea that an unstable internet connection is a problem of economically weak countries. We tend to forget that we have connectivity issues every single day when we enter an underground rail system or a large building. A stable cable-free mobile connection is a myth. It's not even easy to have a stable WiFi connection, for example, a 2.4 GHz WI-FI network can get interference from a microwave oven!

### The cost of Critical CSS with Server-side Rendering

To get Critical CSS extraction for CSS-in-JS, we need SSR. SSR is a process of generating the final HTML for a given state of an application on the server. In fact, it can be quite a complex and expensive process. It requires a certain amount of CPU cycles on the server for each HTTP request.

CSS-in-JS usually leverages the fact that it is hooked into the HTML rendering pipeline.* It knows what HTML was rendered and what CSS it needs so that it is able to produce the absolute minimal amount of it. Critical CSS adds additional overhead to HTML rendering on the server because that CSS also needs to be compiled into a final CSS string. In some scenarios, it is hard or even impossible to cache on the server though.

### Rendering black box

You need to be aware of how a CSS-in-JS library you are using is rendering your CSS. For example, people are often not aware of how Styled Components and Emotion implement dynamic styles. Dynamic styles is a syntax which allows the usage of JavaScript functions inside of your styles declaration. Those functions accept props and return a CSS block.

In order to keep the source order specificity consistent, both above named libraries generate a new CSS rule if it contains a dynamic declaration and the component updates with new props. To demonstrate what I mean, I created [this sandbox](https://codesandbox.io/s/1rm705jnlq). In [JSS](https://cssinjs.org/) we decided to take a different tradeoff, which allows us to update the dynamic properties without generating new CSS rules.*

### Steep learning curve

For people who are familiar with CSS, but are new to JavaScript, the initial amount of work to get up to speed with CSS-in-JS might be quite large.

You don’t need to be a professional JavaScript developer to write CSS-in-JS, up until the point where complex logic gets involved. We can’t generalize the complexity of styling, as it really depends on the use case. In cases where CSS-in-JS gets complex, it is likely that the implementation with vanilla CSS would be even more complex.

For basic CSS-in-JS styling, one needs to know how to declare variables, how to use template strings, and interpolate JavaScript values. If object-notation is used, one needs to know how to work with JavaScript objects and the library-specific object-based syntax. If dynamic styling is involved, one needs to know how to use JavaScript functions and conditionals.

Overall there is a learning curve, we can’t deny it. This learning curve is usually not much bigger, though, than learning Sass. In fact, I created this [egghead course](https://egghead.io/courses/convert-scss-sass-to-css-in-js) to demonstrate this.

### No interoperability

Most CSS-in-JS libs are not interoperable. This means that styles written using one library can’t be rendered using a different library. Practically it means you can’t switch your entire application easily from one implementation to another. It also means that you can’t easily share your UI on NPM without bringing your CSS-in-JS library of choice into the consumer's bundle unless you have a build-time static extraction for your CSS.

We have started to work on the [ISTF format](https://github.com/cssinjs/istf-spec) that is supposed to fix this problem, but unfortunately we haven’t had time yet to get it to a production-ready state.*

I think sharing reusable framework agnostic UI components in the public domain is still a generally hard-to-solve problem.

### Security risks

It is possible to introduce security leaks with CSS-in-JS. Like with any client-side applications, you need to escape user input before rendering it, always.

[This article](https://reactarmory.com/answers/how-can-i-use-css-in-js-securely) will give you more insight and some defacing examples.

### Unreadable class names

Some people still think it is important that we keep meaningful readable class names on the web. Currently, many CSS-in-JS libraries provide meaningful class names based on the declaration name or component name in development mode. Some of them even let you customize the class name generator function.

In production mode though, most of them generate shorter names for a smaller payload. This is a tradeoff the user of the library has to make and customize the library if needed.

### Conclusion

Tradeoffs exist, and I probably didn’t even mention all of them. But most of them don’t universally apply to all CSS-in-JS. They depend on which library you use and how you use it.

* It will take a dedicated article to explain this sentence. Let me know on Twitter ([@oleg008](https://twitter.com/oleg008)) about which one you would like to read more.

