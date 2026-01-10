---
title: How to create a responsive sliding menu
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-14T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-responsive-sliding-menu-97b90852a455
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_qfdprsLd9bgo4VB1gTWyA.gif
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Prashant Yadav

  I run a blog named learnersbucket.com where I write about ES6, Data structures,
  and Algorithms to help others crack coding interviews. Follow me on Twitter for
  regular updates.

  When I was designing my blog with a mobile-first approa...'
---

By Prashant Yadav

I run a blog named [learnersbucket.com](https://learnersbucket.com/) where I write about [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), [Data structures](https://learnersbucket.com/tutorials/topics/data-structures/), and [Algorithms](https://learnersbucket.com/examples/topics/algorithms/) to help others crack coding interviews. Follow me on [Twitter](https://twitter.com/LearnersBucket) for regular updates.

When I was designing my blog with a mobile-first approach, I decided to keep my sidebar navigation menu separate at the bottom right. There is no need for a sticky header and the user can read everything in full height.

This is the simple version of how my mobile menu looks.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_qfdprsLd9bgo4VB1gTWyA.gif)
_Sliding Sidebar Navigation Menu_

Here is how you can create your own responsive sidebar navigation menu.

### Overview

Before we move on to designing the menu, let us imagine what components we need.

* A hamburger ? button which will s**how/**h**ide** the sliding menu.
* Animation on the hamburger button to represent the current state of the menu.
* A side navigation menu.

As the side navigation menu will toggle on the click of the hamburger menu, we can keep them together in a single container.

### Dependencies

I like to use jQuery for [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) manipulation as it reduces the amount of code I need to write.

### Hamburger button

#### HTML structure

There is a simple trick to creating a hamburger menu.

We are going to use a `<d`iv> w`ith a .ham`burger class to create the hamburger button wrapper. Then we will place `three` <span>s to create the layers of the hamburger.

### Designing the hamburger button

Now that the HTML structure for our button is ready, we need to design it to make it look like a hamburger. While designing, we need to keep in mind that we have to provide the animation for open & close when the user clicks on it.

As we are creating a fixed dimension hamburger button, we are going to provide fixed dimensions to the wrapper.

* We have created a fixed parent `.hamburger{position:fixed}` to place it wherever we want on the screen.
* Then we have designed all the `<sp`an>s as small rectangular boxes `with position:ab`solute.
* As we need to show three different strips we have changed the top position of the 2nd span `.hamburger > span:nth-child(2){ top: 16px`; } & 3rd sp`an .hamburger > span:nth-child(3){ top: 2`7px; }.
* We have also provided `transition: all .25s ease-in-out;` to all the spans so that the change of their properties should be smooth.

### Opening & Closing hamburger button with jQuery

Whenever the hamburger button is clicked it will toggle an `open` class to it. We can now use this class to add the opening & closing effect.

`.hamburger.open > span:nth-child(2){ transform: translateX(-100%); opacity:` 0;} will slide the middle strip of the hamburger to the left and make it transparent.

`.hamburger.open > span:nth-child(1){ transform: rotateZ(45deg); top:16px`; } `& .hamburger.open > span:nth-child(2){ transform: rotateZ(-45deg); top:1`6px; } will bring the first and last span to the same top position and rotate them to make an X.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wV23krL_L1ewHBrk.gif)
_Hamburger Button_

Kudos ? we have our hamburger ? button ready, so let us create the side navigation now.

### Responsive side navigation menu

#### HTML structure

We will create a simple navigation menu.

We used a `nav` element for creating the navigation menu and placed the links in `ul`.

### Designing the navigation menu

I have created a full-screen side menu, you can change the dimensions according to your need. We are using `&`gt; selector to avoid overwriting the style of other elements.

Now we have our navigation menu and hamburger button ready, so we can wrap them inside a wrapper to make them functional.

### Sliding navigation menu

#### HTML structure

We have placed the hamburger button and navigation menu inside the `.mobile-menu` wrapper.

### Designing the sliding navigation menu

We have updated the design a little by providing some property of the `.hamburger` to `.mobile-menu` making it fixed and made `.hamburger` relative to keep the `<sp`an> design the same.

As there can be multiple `nav`s, we have updated all the selectors `.mobile-menu >` nav as well to make sure we are pointing to the required elements only.

### Making sidebar menu functional with jQuery

We now add our `.open` class to the `.mobile-menu` so that we can handle both the hamburger button and the sliding menu with a single change.

Our CSS for the animation is also updated accordingly.

Well done ??? we covered everything.

Check out the working demo here

### Conclusion

This post was about a simple sliding menu. I tried to break it into different components so that you can use them independently.

Thank you for having patience while reading this. If you learned something new today then give some ?. Also, share it with your friends so that they can learn something new too.

That’s it, follow me on [Twitter](https://twitter.com/LearnersBucket) for knowledge sharing. I write about [ES6](https://learnersbucket.com/tutorials/es6/es6-intro/), Nodejs, [Data structures](https://learnersbucket.com/tutorials/topics/data-structures/) & [Algorithms](https://learnersbucket.com/examples/topics/algorithms/) and full stack web development with JavaScript.

_Originally published at [learnersbucket.com](https://learnersbucket.com/examples/html/how-to-create-responsive-sidebar-menu/) on April 14, 2019._

