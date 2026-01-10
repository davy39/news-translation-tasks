---
title: 'Introducing Modulz: The Next Step in Visual Coding'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-30T17:00:40.000Z'
originalURL: https://freecodecamp.org/news/help-us-kickstart-modulz-5751775ed435
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yEyqO_xgbUTXLJwydZalyA.png
tags:
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Colm Tuite

  Modulz is a visual code editor for designing and building digital products — without
  writing code. Last week, we launched our Kickstarter campaign.

  In The Design Tool Dilemma, Design Tools are Running Out of Track and How to Construct
  a...'
---

By Colm Tuite

Modulz is a visual code editor for designing and building digital products — without writing code. Last week, we launched our [Kickstarter campaign](https://www.kickstarter.com/projects/stephenhaney/modulzthe-next-step-in-visual-coding?ref=user_menu).

In [The Design Tool Dilemma](https://medium.freecodecamp.org/the-design-tool-dilemma-225541c4ad1d), [Design Tools are Running Out of Track](https://medium.freecodecamp.org/design-tools-are-running-out-of-track-94f21b6ae939) and [How to Construct a Design System](https://medium.freecodecamp.org/how-to-construct-a-design-system-864adbf2a117), I wrote extensively about how our current crop of design tools are not well suited to UI design.

The amazing response to those posts has inspired [Modulz](https://www.modulz.app/): a new breed of design tool which exports production-ready components.

### What is Modulz and how is it useful?

On the surface, Modulz looks familiar. You organise your layers in the left sidebar, apply styles from the right sidebar and watch your design come together on the canvas. But Modulz is _way_ more powerful than that.

#### Interactive states

Rather than drawing static shapes, you’re working with interactive components. Styling each state individually. Adding component variants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ek43HeyRCa1IHueakqZtvQ.gif)
_Styling a mouseover state in Modulz_

#### Code export

You can export production-ready components. We’re starting with React and styled-components. Soon, we’ll add support for other CSS-in-JS libraries like emotion and styled-jsx. Then, Tailwind and vanilla HTML/CSS. In the future, we hope to add support for Vue, Preact and other component-based libraries.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4NRu-Z_n-456sBLcyRyfOQ.gif)
_The code export UI in Modulz_

#### Design systems

Modulz goes much further than color swatches. Define a complete design system including font sizes, spacing, colors, shadows etc, then reuse them to style your components. Tweak a style in your theme and it updates across your entire project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X1c-BleXR-cFv4kdghuWHQ.gif)
_Modulz Theme screen for defining your design system._

#### Design Linting

You can automate design tasks with Modulz design linting feature. Modulz can programmatically suggest improvements to things like color contrast, line length and cross-browser performance issues.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lOEwKUwLS8EmQ_a4DF8Yzw.gif)
_Design linting in Modulz_

Here’s what people are saying about Modulz so far:

> “State is (almost) everything in UI design. Yet no design app that I’ve seen has it baked in. We’re all jumping through hoops for a damn hover state! Go back Modulz for the mental health of designers worldwide.” — [Eric Pitcock](https://twitter.com/ericpitcock/status/1054867293878931456)

> “I ❤ Sketch, but there is no *great* tool for translating product designs into code. The Modulz approach is interesting: instead of pixel-perfection, the app creates responsive, interactive designs that export to React.”—[Leanne Bathurst](https://twitter.com/leannewdesign/status/1053695747709784065)

> “This really has some ground-breaking ideas!”—[Henrik Juhl](https://twitter.com/yesyesdk/status/1054698376388923397)

> “I am loving the Modulz #CloseTheGap slogan. Why bridge a gap when you can get rid of the gap all together? Fill that gap in!”—[Jina Anne](https://twitter.com/jina/status/1054429034942091264)

> “This looks incredibly promising, excited to see how this turns out.”—[Dianne Alongsagay](https://twitter.com/diannealonsagay/status/1053102155995918336)

> “Design system built in — brilliant! This could finally be the design tool we’ve been waiting for. Happy to be a supporter!”—[Aparajita Fishman](https://twitter.com/aparajita1327/status/1053031871183912960)

> “Excited to be an alpha backer on this project. Hope to see these guys succeed in what they’re doing. Take a look.”—[Brice Gramm](https://twitter.com/bricegramm/status/1053046033087901697)

> “This new visual coding tool looks amazing. It fills a gap no like no other tool I’ve seen.”—[Douglas Bonneville](https://twitter.com/dbonneville/status/1052921955849052161)

> “Drop everything right now and go back Modulz on Kickstarter. A tool that exports production-ready components in React is a dream I have been chasing forever.”—[Abdus Salam](https://twitter.com/mrabdussalam/status/1052870962931257344)

> “My world was blown this morning watching your video. I’ll definitely be backing”—[Amanda Lucas](https://twitter.com/amandalucasirl/status/1052844547368091648)

> “Finally, somebody solved the biggest problem in UI design”—[Ugur Akdemir](https://twitter.com/urakdemir/status/1052716029946855424)

> “Stop everything you’re doing and go back Modulz”—[Steve Schoger](https://twitter.com/steveschoger/status/1052707745131126789)

> “Backed! This needs to happen!”—[Vlad Magdalin](https://twitter.com/callmevlad/status/1052665080641245184)

### Plans for the future

We have huge ambitions for Modulz. The features we highlighted here are just the first step.

Later next year, we’re planning to introduce team features including component import, so product teams can design with their existing component libraries.

As the platform matures, the end-game is to support seamless transfer of code between Modulz and text editors. Developers editing the code manually, inside a text editor. Designers editing that same code visually, inside Modulz.

On top of that, plans for more general features include:

* Support for more CSS-in-JS libraries like emotion, styled-jsx etc.
* Support for exporting to vanilla HTML/CSS
* Export component data to JSON
* Export your theme to utility CSS frameworks like Tailwind
* Wider code library support (Vue.js, Preact, React Native etc.)
* Remote device preview / mirroring
* Offline mode (Modulz is a progressive web app)
* Prototyping—state-based interactions, screen transitions etc.
* Massive library of components, templates, icons, illustrations etc.

Ultimately, we want to fix the disconnect between product teams. To help designers collaborate better with developers, without code.

To encourage more inclusive digital products by automating accessibility.

To reduce bottlenecks by building modern tools which empower whole teams to work on their end products.

To get everyone working on the same product. Together.

### The team

![Image](https://cdn-media-1.freecodecamp.org/images/1*iz3e7IT5bohE562k3nhF6Q.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CcHkAScUrXXwO_SAYmek0g.jpeg)
_Our faces_

#### Colm Tuite

Based in Dublin, Colm handles product design and front-end dev. For the past four years, Colm has worked on design tooling. He previously founded [Plexi](http://www.plexi.io/), another design tool. You can find him on [Twitter](https://twitter.com/colmtuite), [Dribbble](https://dribbble.com/ColmTuite) and his [site](https://www.colmtuite.com/).

#### Stephen Haney

Based in Seattle, Stephen handles back-end dev and JavaScript engineering. Stephen has over 15 years experience with many Fortune 500 companies and has authored two books on game dev. Find him on [Twitter](https://twitter.com/sdothaney) and [Github](https://github.com/StephenHaney).

### How you can help

We’ve been working full-time on Modulz for four months. We already have a lot of the core product complete. But Modulz is a complex product and we have big plans for it.

We’ve received some support from InVision and [Adobe](https://theblog.adobe.com/the-new-adobe-xd-ecosystem-supercharging-design-workflows-with-third-party-plugins/?scid=7a935a97-5362-4d51-888d-b443ed2e5174&mv=social&mv2=owned_social). But we need all the help we can get.

To thank you for your support, we’re offering [unlimited, lifetime access to Modulz on Kickstarter](https://www.kickstarter.com/projects/stephenhaney/modulzthe-next-step-in-visual-coding?ref=user_menu). There’s also a cool goodie bag full of high-quality icons, templates and assets! It would mean _so much_ to us if you would consider supporting our work.

For more info, check out Modulz [website](https://www.modulz.app/), [Twitter](https://twitter.com/Modulz) and [Spectrum](https://spectrum.chat/modulz).

Thanks everyone ❤️

