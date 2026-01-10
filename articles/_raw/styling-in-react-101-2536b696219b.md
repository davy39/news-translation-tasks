---
title: How to make your apps pretty with styling in React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-26T19:02:03.000Z'
originalURL: https://freecodecamp.org/news/styling-in-react-101-2536b696219b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*INQOqFg9aha-aEJbqhXQUw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: null
seo_desc: 'By Vinh Le

  When it comes to styling in React, there are just so many ways and choices of technologies
  to beautify your web app. Nonetheless, based on my personal experience, it really
  depends on the UI requirements of your app to decide which to go w...'
---

By Vinh Le

When it comes to styling in React, there are just so many ways and choices of technologies to beautify your web app. Nonetheless, based on my personal experience, it really depends on the UI requirements of your app to decide which to go with.

### Is it too easy?

If you stop here and say: “It is easy! Just Google to find out top React UI libraries, pick one of them, and you’re good to go”, then you perhaps have not gone through painful experiences configuring pre-styled components in those libraries.

The more time you work on something, the more familiar you are and the less time you need to spend troubleshooting. Styling in React is not an exception. However, it truly requires a decent amount of time, at least for me as a self-taught developer, to be able to make a wise choice.

Therefore, my main purposes on this article is to quickly introduce best React styling alternatives and more importantly, try to further elaborate to you when you should use which.

### Why styling?

![Image](https://cdn-media-1.freecodecamp.org/images/p247brEV3QCLUH97LtMsI0w7YhhekP5ZyfTd)
_Aesthetics ? Functionalities ? Or both?_

Another dead simple question, isn’t it? Well, if I alter that question a tiny bit: “Why learn styling right when you start learning React?”, it might perhaps activate your thought flow.

If you are a newcomer to React ecosystem, your very first tutorials probably teach you how to start a project, show you how to manage states and handle props. Styling is merely mentioned in the first sections of online courses and therefore minimally used in your very first apps.

Before I sound over-serious to you, let me tell you that “It is entirely fine.” There is absolutely nothing wrong with how you are doing. On the other hand, it is even better if you put styling aside at the beginning to focus more on logic and functionalities of the app.

However, if you do care about the aesthetics of your work from the very beginning, then you are probably not totally satisfied with your functional but minimally styled app.

Okay, enough words. Let me summarize the benefits of styling your app, either from your very first “Hello world” or a project that you are in the middle of:

* **Beautiful user interface at start** — remember why React exists? To help us create dynamic UI. A more polished user interface contributes to a better user experience. As a result, if we put ourselves in the users’ shoes, we simply realize that appealing design is an imperative part of a user-friendly application.
* **Good development environment** — especially when you are working on your side project. If a good design makes you enjoy using it, you will perhaps have more inspiration for developing an app with a design-first approach. Again, this comes from the aesthetic sides of things. If you are the one who just want it to work, this might not be applicable for you.
* **Avoidance of styling overwhelm later on** — imagine when you have worked on a project for a while and suddenly look back to think about how much you are going to need to do styling. If it is just a sandbox project, then it’s perhaps fine. But if your app requires multiple layers of containers and elements, and responsiveness is a must, then it would be quite a big amount of work ahead.

**Then what should I use to make my React app look good?**

![Image](https://cdn-media-1.freecodecamp.org/images/S28rjd2vX8bKPhxNO1m1JpYO9QvorQtJ-3lK)
_You already got an idea, let’s now consider alternatives_

### Inline styling

This approach is the easiest way to start as it requires non-configuration and you can instantly see the result. However, even if you are familiar with CSS, be aware of typos as they might cause you headaches:

```
<div style={{ width: 50, height: 50, background: '#000'}}>    I am a square box with black background</div>
```

#### **Takeaways**

* Inline styling is done by the **style property** in any DOM element, it has an **object** type, in which **key** is a normal CSS property, and **value** is the equivalent CSS value.
* Because there is no dash like many CSS properties, you should notice capitalization such as: `backgroundColor`, `backgroundImage`, `textAlign`, and `flexDirection`.
* It is more well-organized when you define a distinctive variable storing all styling logic:

```
const styles = {  alertMessage: { color: 'red' },  ... // other styling rule};...
```

```
<span style={styles.alertMessage}>Unknown error</span>
```

* You can do conditional styling. For example:

```
<span    style={{ color: this.state.isWarning ? ‘red’ : ‘black’  }}>   Let’s see if I am a warning </span>. </span>
```

#### Pros

* Easy to apply, non-configuration.

#### Cons

* Your JavaScript files will get messier and longer when your project gets more complex. One way to do it is to define style variables in an external JavaScript file and import them back. However, this does requires an extra step and becomes more difficult to use compared with following styling methods below.
* Lower speed of development caused by app’s reloading. If you use tools like create-react-app, your app will hot-reload every time you make changes. Otherwise, you have to manually reload your page to see changes. Therefore, depending on the complexity of your app, it will take a gradually longer amount of time just for re-rendering.

#### When to use?

When you first started learning React would be the most appropriate time to pick up this approach. Besides, if your project is small or you just want to apply some minor styling on top of your app. Responsiveness, for instance, is not really critical. Then inline styling is good to go.

### CSS

Okay, no more weird CSS-in-JS. Here is original CSS that you’ve loved :), only a simple configuration before you start:

* Create your CSS file and import it into a JavaScript file:

```
import ‘./App.css’;
```

* Add className to the element that you want to apply a style to:

```
<p className=’warning-message’>Warning</p>
```

Notice that it is now **className**, not normal **class** — just a typical React thingy.

* Followed by your styling rules:

```
App.css.warning-message { color: red;}
```

* Conditional styling by setting equivalent class name:

```
<p   className={this.state.warning ? ’warning-message’ : ‘normal-message’}>Warning</p>
```

#### Pros

* Write CSS rules that you’re familiar with, less risk of making typos.
* Benefits from CSS features such as variables and media queries.
* Well-organized project structure.
* **Higher development speed** — this is perhaps the most enjoyable upside that I’ve experienced in development. When you make changes in your CSS files, your app will not be re-rendered. Therefore, it will take a second for your updates to display on the screen. The bigger and more complex your app is, the more pleasure you will feel saving those unnecessary reloading time.

#### Cons

* Missing features compared to SCSS, which I will dive into right after this.

#### When to use?

You can use CSS from the beginning, regardless of your app’s size. As it is almost zero-configuration and CSS is perhaps familiar with many, it is easy to quickly start.

If your app is getting bigger and having an even more complex design system, consider checking benefits of SCSS over CSS.

Nonetheless, keep in mind that you’ll be totally fine with pure CSS. SCSS is not really a game-changer that offers you all benefits that you would not get out of CSS. Recently, brand new features like variables are coming to minimize the gap between CSS and its preprocessors. Besides, if you have not used SCSS before, it will does take some times to familiarize with it.

### SCSS

This is perhaps my go-to choice for React styling. It takes all familiarity and benefits of CSS plus a number of very useful features to make a great package. If you are not familiar with SCSS, they have awesome [docs](https://sass-lang.com/guide) for you to check out.

In order to make use of SCSS in your React app, it does require a few configurations, though. If you are using create-react-app, this [guideline](https://medium.com/@oreofeolurin/configuring-scss-with-react-create-react-app-1f563f862724) might be helpful for you.

Next, let me show you the benefits of SCSS that makes it a superior choice compared with normal CSS.

#### Nesting

When your project gets bigger, the chance is highly likely that your CSS files are going to be full of class names. Things get even more daunting when your design consists of nested blocks, containers and elements. Finding a particular class name somewhere in a hundreds-line file is thus tiring and time-consuming. Here is where nesting comes in handy:

```
App.scss.intro-container {  h1 { font-size: 20px };  .nested-child {    display: block;    p {      margin: 0;    }  }}
```

With this structure, for instance, you want to change style of a child element inside your intro container. All you need to do right now is to find its class name, which is `intro-container` in this case. Then all styles of its children could be found inside it. Much easier, isn’t it?

#### Mixins

One of the greatest benefits that mixins bring to the table is to define breakpoints in media queries. Let’s take a look at this example:

```
_mixins.scss
```

```
// define breakpoint for mobile device  @mixin bp-mobile {    @media only screen and (min-device-width: 320px) and (max-device-width: 480px) {      @content;    }  }
```

Back in the main SCSS file:

```
App.scss
```

```
body {  width: 60%; margin: 0 auto;  @include bp-mobile {    width: 90%;  }}
```

Compared to:

```
App.css
```

```
// set width of the body to 90% only in mobile devicesbody {  width: 60%; margin: 0 auto;}...@media only screen and (min-device-width: 320px) and (max-device-width: 480px) {  body {    @include bp-mobile {      width: 90%;    }  }}
```

I believe that it is much more natural and easier in SCSS. As when you apply styling rules for one element, you have a clear view of how it looks in other viewports. Therefore, changes and adjustments are made directly without the burden of scrolling up in CSS as people normally define media queries at the end of CSS file.

#### Inheritance

This is extremely helpful in making your code [DRY](https://en.wikipedia.org/wiki/Don't_repeat_yourself). Let’s say if you want to apply similar background and border for 2 buttons, except one of them has red text color and the other has blue one:

```
// define common rules%button-common {  background: #fff;  border: 1px solid gray;  border-radius: 3px;}
```

```
.button-red {  @extend %button-common; color: ‘red’;}
```

```
.button-blue {  @extend %button-common; color: ‘blue’;}
```

Let’s summarize pros and cons of SCSS:

#### Pros

* Basically all pros from CSS plus distinctive features that make people love SCSS.

#### Cons

* Requires configuration to use.
* Does take a certain amount of time to learn for folks who are not familiar with SCSS.

### React UI Libraries

Thanks to the thriving of the open-source community, there are awesome React UI libraries that you can take into use in your projects. Excellent resources are [MaterialUI](https://github.com/mui-org/material-ui), [React-Bootstrap](https://github.com/react-bootstrap/react-bootstrap)… to name but a few.

Let’s take MaterialUI, one of the most popular libraries, as a demo:

#### Installation

```
npm install @material-ui/core
```

In order to use this, you have to rely heavily on its documentation, which is drafted nicely and designed in, well, the Google material way. However, if you look at a code sample for its components, it is kind of daunting. My way is to just import the component that you want to use, notice some important props, and customize it later.

Let’s say if we want to create a button:

```
App.js
```

```
import { Button } from ‘@material-ui/core’;...
```

```
<Button  color=’primary’  onClick={() => console.log(‘clicked’)}  fullWidth> View </Button>
```

Boom! A button with label “View”, blue color, having a width value equal to the one of its parent container, appears nicely on the screen.

Just like this, you can pretty much get use of all components in the library. The advantage of using it is an apparently polished and modern material design. If you want to create a component on your own, it will perhaps take a good amount of work and your final result might not even look as good as pre-styled components.

#### So why don’t we just all use this?

First of all, if making it appear on the screen seems to be super easy, customizing and making it perfectly fit into your design system is absolutely not an easy task.

One way to customize those components is to override its style, most of the time through style prop. Another way is to give it a class name, and write its own style by CSS. In this case, if your CSS is totally valid but your component does not change at all, remember to put `!important` after your rules.

#### So when would you use React UI libraries?

If you are working on a side project which is small, libraries like MaterialUI are nice to use. As you’ll only have to focus on the JavaScript side of things and still have a pretty nice-looking app.

However, when you plan to make a complex app with nested layers of UI, do notice that sometimes it might be even faster to create your own reusable components than try to customize pre-styled ones. In my personal experience, if you really need particular components where they are so difficult to style or make them behave like what you wish, then you take them into use. Otherwise, it is better to create your own and take full advantage of your control over them.

So, here they are, popular ways to style in React. Of course, there are still many other great libraries and hacks out there. Please share yours down bellow in the comment section. As the React community is growing bigger and bigger, we can expect an even increasing number of “rising stars”.

Furthermore, awesome maintainers and developers of current open-source libraries will only try to make their solutions better, more polished, and easier to use. Those all signify a bright future ahead :)

#### Thanks for reading!

#### Say hello on Social Media: [Facebook](https://www.facebook.com/VinhLee95), [Twitter](https://mobile.twitter.com/vinhle95), [LinkedIn](https://www.linkedin.com/in/vinhlee95/), or my [personal site](http://vinhlee.com/).

#### Stay tuned for upcoming tech blogs ? ? ?

#### See you soon!

