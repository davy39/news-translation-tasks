---
title: Designing beautiful mobile apps from scratch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-26T18:24:40.000Z'
originalURL: https://freecodecamp.org/news/designing-beautiful-mobile-apps-from-scratch-1a3441ebd604
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c8TfejOHg-KLM4wOsr37Jg.png
tags:
- name: Apps
  slug: apps-tag
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Harshita Arora

  I started learning graphic design when I was 13. I learned to design websites from
  online courses and used to play around with Photoshop and Affinity Designer all
  day. That experience taught me how to think like a designer.

  I’ve bee...'
---

By Harshita Arora

I started learning graphic design when I was 13. I learned to design websites from online courses and used to play around with Photoshop and Affinity Designer all day. That experience taught me how to think like a designer.

I’ve been designing and developing apps for almost a year now. I attended a program at MIT where I worked with a team to develop [Universeat](http://universeatyapp.com/)y. Two months ago, I started working on a new app, [Crypto Price Tracker](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8), which I launched recently on 28th January.

In this post, I’ll share the step-by-step design process I follow along with examples of the app I worked on. This should help anyone who wants to learn or improve upon their digital design skills. Design is not all about knowing how to use design software, and this post won’t teach you how to use it. There’s hundreds of good quality tutorials online to learn. Design is also about understanding your product inside out, its features and functionality, and designing while keeping the end-user in mind. That’s what this post is meant to teach.

**Design Process**:

1. Create a user-flow diagram for each screen.
2. Create/draw wireframes.
3. Choose design patterns and colour palettes.
4. Create mock-ups.
5. Create an animated app prototype and ask people to test it and provide feedback.
6. Give final touch ups to the mock-ups to have the final screens all ready to begin coding.

Let’s start!

### **User-Flow Diagram**

The first step is to figure out the features you want in your app. Once you’ve got your ideas, design a user-flow diagram. A user-flow diagram is a very high level representation of a user’s journey through your app/website.

Usually, a user flow diagram is made up of 3 types of shapes.

* Rectangles are used to represent screens.
* Diamonds are used to represent decisions (For example, tapping the login button, swiping to the left, zooming in).
* Arrows link up screens and decisions together.

User-flow diagrams are super helpful because they give a good logical idea of how the app would function.

Here’s a user-flow diagram I drew when I started out working on the design of my app.

![Image](https://cdn-media-1.freecodecamp.org/images/sQTKDXA1ocHyurFP1Xvzy0fOabE9bqu9TR7k)
_User-flow diagram for the Main Interface._

### **Wireframes**

Once you’ve completed the user-flow diagrams for each screen and designed user journeys, you’ll begin working on wireframing all the screens. Wireframes are essentially low-fidelity representations of how your app will look. Essentially a sketch or an outline of where images, labels, buttons, and stuff will go, with their layout and positioning. A rough sketch of how your app will work.

I use printed templates from [UI Stencils](https://www.uistencils.com/blogs/news/ui-stencils-drafting-templates) for drawing the wireframes. It saves time and gives a nice canvas to draw on and make notes.

Here’s an example wireframe.

![Image](https://cdn-media-1.freecodecamp.org/images/pMB5oT19AL3Cx02O3Ut6qc8QMGotOZO2SrHd)
_Wireframe for the Main Interface._

After sketching the wireframes, you can use an app called [Pop](https://itunes.apple.com/us/app/pop-prototyping-on-paper/id555647796?mt=8) and take a pic of all your drawings using the app and have a prototype by linking up all the screens through buttons.

### **Design Patterns and Colour Palettes**

This is my favourite part. It’s like window-shopping. Lots of design patterns and colour palettes to choose from. I go about picking the ones I like and experimenting with them.

The best platforms to find design patterns are [Mobile Patterns](http://mobile-patterns.com/) and [Pttrns](https://pttrns.com/). And to find good colour palettes, go to [Color Hunt](http://colorhunt.co/).

### **Mock-ups**

This is when you finally move on to using design software. A mock-up in the design sense is a high-fidelity representation of your design. It’s almost like you went into this app in the future and you took some screenshots from it. It should look realistic and pretty much like the real thing.

There are design software and tools for creating mock-ups. I use Affinity designer. The most commonly used tool for iOS design is [Sketch](https://sketchapp.com/).

Here’s an example of some of the early designs of my app.

![Image](https://cdn-media-1.freecodecamp.org/images/dcKdLyb87k6pV3u7B9eQsoiqh2HWmmA7KmuW)
_Bringing the pencil drawing to pixels!_

I experimented more with various colour palettes.

![Image](https://cdn-media-1.freecodecamp.org/images/6tYeMeNm6LFTHRBdXXToUY8isV4XmwbnkK5u)

I shared the initial mockups with my friends for their feedback. A lot of people seemed to like the gold gradient and black scheme.

Be willing to take feedback and experiment with new suggestions! You’ll find amazing ideas come from your users when you talk to them, not when you frantically scroll through Dribbble or Behance.

So I redesigned the mock-up and removed the background graphs because generating them was a technically time-consuming process and they reduced readability. This is what the redesigned mock-up looked like.

![Image](https://cdn-media-1.freecodecamp.org/images/-cGRDrYKax41rdeUDC9q39udfYrVliFJ4SMX)
_Gold gradient with black surprisingly looks good!_

I was pretty satisfied with the colour scheme, icons on the tab bar, and overall layout. I went ahead and designed the rest of the screens following the same design guidelines. It was a long, but surely fun process!

Once all of my screens were ready, I put together a prototype in Adobe XD and asked a few friends to experiment and give feedback.

After final touches and such, this is what my final design looks like.

![Image](https://cdn-media-1.freecodecamp.org/images/WbFarZPetpzDnI4c9pfdVxSrClRjC5vb17XN)
_The Main Interface!_

After all the screens were completed, I imported them into Xcode and began coding the app.

That’s it! I hope this post will help you get started with app design or help you become a better designer. And if you like my app, you can download it [here](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8).

I’m ending the post with one of my favourite quotes about design.

> “Design is not just what it looks like and feels like. Design is how it works”   
> -Steve Jobs

