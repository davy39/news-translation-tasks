---
title: How to Build Beautiful Page Transitions in Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-11T17:50:09.000Z'
originalURL: https://freecodecamp.org/news/beautiful-page-transitions-in-angular
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/SF.jpeg
tags:
- name: Angular
  slug: angular
- name: animations
  slug: animations
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'By Arjav Dave

  In today’s world, just having a website is not enough. The website needs to have
  a clean UI and it needs to be intuitive. And most importantly, it needs to have
  some sort of interactive element.

  Interactivity keeps users glued to your s...'
---

By Arjav Dave

In today’s world, just having a website is not enough. The website needs to have a clean UI and it needs to be intuitive. And most importantly, it needs to have some sort of interactive element.

Interactivity keeps users glued to your site for longer periods of time. As a result, it increases the chances that users will become customers. Also, longer interaction time leads to a lower bounce rate and a higher ranking on search engines.

One of the most common and basic forms of interaction happens when a user scrolls on your website. But wouldn’t it be quite boring if the user keeps scrolling through your long static page? 

In this tutorial, we will have a look at three basic animations that you can implement on scroll. Parallax, fade, and slide animations are the most popular animations devs use to make scrolling more fun. Let’s see how we can build them for our sites.

Before we move further, here are the end results:

![Parallax animation](https://www.freecodecamp.org/news/content/images/2021/05/1_Ywqe-PW3A-V8B5mvJmlpVg.gif)
_Parallax ([View Demo](https://animations-demo-ffcb4.web.app/parallax" class="cd il" rel="noopener" style="box-sizing: inherit; color: inherit; text-decoration: underline; -webkit-tap-highlight-color: transparent;))_

![Fade animation](https://www.freecodecamp.org/news/content/images/2021/05/1_cZYvFm4F9EZXCyfpv1Rnwg.gif)
_Fade ([View Demo](https://animations-demo-ffcb4.web.app/fade" class="cd il" rel="noopener" style="box-sizing: inherit; color: inherit; text-decoration: underline; -webkit-tap-highlight-color: transparent;))_

![Slide animation](https://www.freecodecamp.org/news/content/images/2021/05/1_-thdCqzqVWw9o0oTk-lN0g.gif)
_Slide ([View Demo](https://animations-demo-ffcb4.web.app/slide" class="cd il" rel="noopener" style="box-sizing: inherit; color: inherit; text-decoration: underline; -webkit-tap-highlight-color: transparent;))_

# Project Setup

## Prerequisites

We will be using Angular 11 to create our project. And we'll use VS Code as our IDE.

In order to build the animations, we are going to use the fabulous [Green Sock Animation Platform (gsap)](https://greensock.com/gsap/). It’s one of the best JavaScript animation libraries out there.

## Create the project

Create an Angular project by entering the command below. _Make sure to enable routing when_ it asks you_._

```
ng new animations --style css
code animations
```

This will create a new project named _animations_ with the style format as CSS. Next, it will open the project in VS Code. 

Now let’s install gsap. In your VS Code terminal, enter the command below:

```
npm install --save gsap @types/gsap
```

This will install the gsap library and the typing files via `@types/gsap`.

Lastly, let’s create three components. Enter the commands below:

```
ng g c parallax
ng g c fade
ng g c slide
```

## How to set up the routes

Let’s create three separate routes: `/parallax`, `/fade`, and `/scroll`. Open your `app-routing.module.ts` and add the routes as below:

<script src="https://gist.github.com/shenanigan/a48aa865eb07ae94044e5e4c29ddaf9a.js"></script>

# How to Create Parallax Animation

Since we have now set up the project, let’s start with parallax animation.

When you create page animations, you typically use sections. So, open your `parallax.component.html` file and paste in the code below:

<script src="https://gist.github.com/shenanigan/9441fd03f71c4b2569c7d47aedc13b9d.js"></script>

Let’s add some styling to these sections. Since we are going to use sections in all three components, we will add styling to the common `styles.css` file. 

Open your `styles.css` file and paste in the CSS below:

<script src="https://gist.github.com/shenanigan/dca657f450b032f5fc59a61f286f169d.js"></script>

In the above code, we are making the height and width of the section equal to the viewport’s height and width. Second, we are aligning the content in the center of the section. Lastly, we are setting the font style for how we want to display the text.

Since the `bg` class used in `parallax.component.html` is specific to parallax, we will define its properties in `parallax.component.css`_._ Open that file and paste in the CSS below:

<script src="https://gist.github.com/shenanigan/af0cd6f8452fef800e511aa22a0d9790.js"></script>

In order to set the parallax animation, we need to add some TypeScript code. So, open your `parallax.component.ts` file and add the code below in your `ngOnInit` function:

<script src="https://gist.github.com/shenanigan/d5cf12a6dd47f7fbef4f26f346f12312.js"></script>

I have added inline comments to help you understand the code. Message me if you need further explanation.

Finally, add the imports below at the top of your TS file so that you don’t get any compile-time errors:

```
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/all';
```

That’s it! You can now visit [http://localhost:4200/parallax](http://localhost:4200/parallax) to see the beautiful animation.

# How to Create Fade Animation

For the fade animation, open the `fade.component.html` file and paste in the HTML code below:

<script src="https://gist.github.com/shenanigan/d7cea722e1f9a7ce73143810bb6e894f.js"></script>

In the `fade.component.css`, paste in the CSS below:

<script src="https://gist.github.com/shenanigan/f8d15983a7a263af72f2b2addf71f151.js"></script>

We are going to display only one section at a time. So we will hide all sections except the first one. Also, since we are not moving the sections along with the scroll, we'll mark its position as fixed.

Let’s add the animation code to make the other sections visible on scroll. Open the `fade.component.ts` file and paste in the following code:

<script src="https://gist.github.com/shenanigan/0fadba01528dc3e0d3636522a5f13adc.js"></script>

I have added inline comments so as to make the code self-explanatory. For any clarifications, please let me know.

Visit [http://localhost:4200/fade](http://localhost:4200/parallax) to see the smooth fading animation as you scroll.

# How to Create Slide Animation

This is typically the easiest of the lot to understand and implement. 

Open your `slide.component.html` file and paste in the code below. It’s similar to `fade.component.html`, except the class is removed from the first section.

<script src="https://gist.github.com/shenanigan/6a68e1b4cc35ba04809fa6d118bf098c.js"></script>

We don't need to add any CSS. 

Next, open the `slide.component.ts` file and add the code below:

<script src="https://gist.github.com/shenanigan/f958d7d662ffe821e3c0431bfb5b27bf.js"></script>

Again, I have added the inline comments for a better understanding of the code. For any queries, just reach out to me.

Open [http://localhost:4200/slide](http://localhost:4200/slide) to see a mesmerizing slide animation as you scroll.

# Conclusion

Animations add a lot of value to your site, and they help keep your users engaged. As with all things, don't go overboard and use animations in moderation. Don’t clutter or mess up the website with heavy images and funky animations. Keep It Simple & Keep It Subtle (KIS & KIS).

In this tutorial, we saw how to add simple parallax, fade, and slide animations for page sections. 

Lastly, a great thanks to [Lorem Picsum](https://picsum.photos/) for providing such great photos.

If you liked this article, you might also like the below articles:

* [Lazy Loading Modules in Angular](https://betterprogramming.pub/lazy-loading-in-angular-a-beginners-guide-c09d09738d08)
* [.NET 5: How to Authenticate & Authorise API's correctly](https://itnext.io/net-5-how-to-authenticate-authorise-apis-correctly-34b09d132d84)
* [Learn TDD with Integration Tests in .NET 5.0](https://itnext.io/learn-tdd-with-integration-tests-in-net-5-0-937f126e7220)

_Note: You can find the whole project_ [_on GitHub_](https://github.com/shenanigan/animations-demo)_._

  

