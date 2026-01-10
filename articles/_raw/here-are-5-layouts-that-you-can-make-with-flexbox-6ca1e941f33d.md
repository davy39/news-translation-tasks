---
title: Here are 5 Layouts That You Can Make With FlexBox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-04T21:20:15.000Z'
originalURL: https://freecodecamp.org/news/here-are-5-layouts-that-you-can-make-with-flexbox-6ca1e941f33d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*V54N2Latawo69ZaS7hqJQw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jennifer Bland

  The CSS Flexible Box Layout — Flexbox — provides a simple solution to the design
  and layout problems designers and developers have faced with CSS. Let me show you
  how to use it to generate some common layouts and challenges that you...'
---

By Jennifer Bland

The CSS Flexible Box Layout — Flexbox — provides a simple solution to the design and layout problems designers and developers have faced with CSS. Let me show you how to use it to generate some common layouts and challenges that you will face in designing a responsive website design.

I assume you already know the basis of Flexbox. If not there are many documents teaching you about Flexbox. I would recommend [Understanding Flexbox: Everything you need to know](https://medium.freecodecamp.org/understanding-flexbox-everything-you-need-to-know-b4013d4dc9af).

### **Here is What We Will Be Making**

In this article, I am going to show you how to make 7 different layouts using FlexBox.

1. Navigation
2. Center image on screen
3. Responsive website layout
4. AddOn for input fields
5. 3 column layout

### Get The Code

All of the examples that I am going to show can be [downloaded from my GitHub account](https://github.com/ratracegrad/made-with-flexbox). The code for every example is just html and css. I have created a master homepage that provides a link to every example that we are going to cover.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sZPnR9WDlMBBSJCViFbdJw.png)

### Navigation

Every website has a navigation. Using Flexbox you can create a navigation that has your company name on the left and menu items on the right.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o_I7a9CVkOmJNIgQeaLVhg.png)

To accomplish this layout in CSS, you would have to use floats to get some content to appear on the left and the rest of the content to appear on the right.

With FlexBox you have to specify a flex container that contains the navigation. The company name on the left is a flex item within this container.

The menu items on the right are their own flex container with a <ul> containing all the menu items.

Here is the html for the navigation:

Here is the CSS for the navigation:

### Center Image on Screen

Many websites include a full size image. Usually this image contains text that is centered on the screen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jtv2bxTy4-k9e2U1e49OhA.png)

The challenge is styling the image so that it fits full page regardless of whether you are viewing this on a wide screen monitor, laptop, tablet or phone and have the CSS remain centered on the screen. Flexbox makes it easy to do this. To mimic text centered on the screen I have included a button

Here is the html to center an image on the screen:

Here is the css to center an image on the screen:

### Responsive Website Layout

Almost every website has the same layout which contains a navigation across the top and a footer at the bottom. In between there are 3 columns consisting or a right and left sidebar and the main content area. Generally the main content area takes up 60% of the width of the screen and the two sidebars are allocated 20% of the screen each.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uxPAuHEcsoHORMpwH57_Lg.png)

The challenge for creating a responsive website is having the footer stay at the bottom of the page regardless of how much content is displayed. The content area should scroll if there is more than can be displayed on the page.

Here is the html for the responsive website layout:

Here is the css code for the responsive website layout:

### AddOn for Input Field

To improve your user experience, many designers prefer to put images or text in their input fields. This provides the user with directions on what should be included in the field.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-pcENc5u6jl3ajF90EMiew.png)

With traditional CSS that was very challenging and required you to use a table format to insert something before or after an input field. With Flexbox it is much easier.

Here is the html code for the addon for input fields:

Here is the css code for addon for input field:

### 3 Column Layout

It is very common for websites to include a 3 column layout on the screen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vDAqFQfCkc6KBXErK7TG9g.png)

Here is the html for a 3 column layout:

Here is the css for the 3 column layout:

### More Articles

Thanks for reading my article. If you like it, please click on clap icon below so that others will find the article. Here are some more of my articles that you might be interested in:

[Think outside the box with CSS shape-outside](https://medium.com/@ratracegrad/mastering-css-series-shape-outside-44d626270b25)  
[7 Things I learned in my journey from coding bootcamp to Senior Developer](https://codeburst.io/7-things-i-learned-in-my-journey-from-coding-bootcamp-to-senior-developer-645ab7c2fea0)  
[Why Company Culture is Important to Your Career as a Software Engineer](https://medium.freecodecamp.org/why-company-culture-is-important-to-your-career-as-a-software-engineer-5a590bc44621)

