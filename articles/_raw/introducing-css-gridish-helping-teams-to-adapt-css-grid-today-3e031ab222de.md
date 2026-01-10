---
title: 'Introducing CSS Gridish: An Open Source Tool to Help Your Team Adapt CSS Grid
  Today'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-23T14:18:07.000Z'
originalURL: https://freecodecamp.org/news/introducing-css-gridish-helping-teams-to-adapt-css-grid-today-3e031ab222de
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JobvUFgnKW070EmCAmLpIg.gif
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: open source
  slug: open-source
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By James Y Rauhut

  Today, I’m excited to introduce a new open-source tool from IBM called CSS Gridish!

  CSS Gridish takes design specs of your product’s grid and builds out several resources
  for your team to use:


  A sketch file with artboards and grid/...'
---

By James Y Rauhut

Today, I’m excited to introduce a new open-source tool from IBM called [CSS Gridish](https://github.com/ibm/css-gridish)!

CSS Gridish takes design specs of your product’s grid and builds out several resources for your team to use:

* A sketch file with artboards and grid/layout settings for designers
* CSS/SCSS code using CSS Grid with a CSS Flexbox fallback for developers
* A [Google Chrome extension](https://chrome.google.com/webstore/detail/ebhcneoilkamaddhlphlehojpcooobgc) for anyone to check a webpage’s alignment

The goal is to help teams adapt CSS Grid sooner, and to enable more complex layouts. To show how versatile the tool is, here are some example grids from [Bootstrap](https://github.com/IBM/css-gridish/tree/master/examples/bootstrap), [Carbon Design System](https://github.com/IBM/css-gridish/tree/master/examples/carbon), and [Material Design](https://github.com/IBM/css-gridish/tree/master/examples/material).

### Why IBM’s Developers Made This

The new CSS Grid spec is wonderful for web design. Now, designers can place as much care into the y-axis as they have the x-axis in the past. Projects [left](https://slack.engineering/rebuilding-slack-com-b124c405c193) and [right](https://open.nytimes.com/bootstrap-to-css-grid-87b3f5f830e4) are starting to document their transition to CSS Grid.

A lot of IBM teams are eager to use CSS Grid, but face a couple of blockers to overcome. CSS Gridish helps by addressing these blockers.

![Image](https://cdn-media-1.freecodecamp.org/images/Ui9S0UFPRKRi50UBf0pzqBCiscncZK4vZpuA)
_The top screenshot is a page loading on Chrome using CSS Grid. The bottom screenshot is the same page on IE 11 using CSS Flexbox. ([Source](https://ibm.github.io/css-gridish/examples/material/example.html" rel="noopener" target="_blank" title="))_

#### Browser Compatibility

CSS Grid currently has great browser support (~75%). Yet, a lot of products still need to serve the remaining browsers. For example, ibm.com still receives 10% of its traffic from Internet Explorer. It takes a lot of extra work to support those older browsers.

While CSS Gridish always builds `yourGrid.css` that uses CSS Grid, it also builds a file we call `yourGrid-legacy.css`. This legacy file still only serves CSS Grid code if a browser supports it. If the browser does not support CSS Grid, the user gets served a flexbox fallback. Add the extra classes for `yourGrid-legacy.css` and you have added backwards compatibility!

What do you do if you do not need to support older browsers anymore? All it takes is a switch to `yourGrid.css` to shave precious kilobytes off the experience.

#### Bridging Design and Code

Great tools have emerged that create a single source of truth for design and code like [React Sketchapp](https://github.com/airbnb/react-sketchapp) and [Lona](https://github.com/airbnb/Lona). These tools ensure that designers and developers are making with the same components.

![Image](https://cdn-media-1.freecodecamp.org/images/dvsiIMI7i-5Qk9JyfLXaVKtYOUtPTwxLV-Xc)
_Use the [Chrome extension](https://chrome.google.com/webstore/detail/css-gridish/ebhcneoilkamaddhlphlehojpcooobgc" rel="noopener" target="_blank" title=") for CSS Gridish to review webpages with the same grid and layout settings on your Sketch artboards._

We hope to bring that same team unity to the grid. The artboards for Sketch and code for web development generate from the same config file. While the grid config file is not flawless, we want CSS Gridish to spark a conversation about grid standards in similar tools.

Additionally, it is easy for design details to get lost in the transition to development. So that’s why we have built a Google Chrome extension to review your coded work. The Chrome extension can be set to your team’s grid config file to view the same grid and layout from the Sketch file with the same shortcuts(CTRL+G and CTRL+L). Developers enjoy using the extension with the Sketch file they are implementing open. Designers love reviewing coded webpages with it.

#### Respecting the Entire Page

Using CSS Grid, a developer can follow the grid design when starting at the first layer of HTML. But things get more difficult when the developer has to work inside of different sections and other nodes. This is because `display: subgrid` is still gaining [browser support.](https://caniuse.com/#feat=css-display-contents)

CSS Gridish works around this by relying on viewport width units instead of relative percentage units. You can embed as many `.yourGrid-grid` elements inside each other, but still respect the columns and rows of the page. The only downside we have found to this is that browsers treat the `vw` unit differently with scrollbars. This can be circumvented with margin on your grid.

### How It Works

The only input CSS Gridish needs is one json file called `css-gridish.json`. The file accepts your grid design specs and options for where/how the outputted files are saved. For now, CSS Gridish makes a couple of assumptions about your grid design:

* The outside gutters are half the size of inside gutters
* Your main columns are fluid instead of fixed widths

**Tip:** For the best results in Sketch, we recommend you make your grid breakpoints, margin, and gutter divisible by the row height.

![Image](https://cdn-media-1.freecodecamp.org/images/WNtMemAeOorDqjE9u12JyFZu3NVHEMcPK7r8)
_While the grid’s designer specifies the dimensions in red (plus number of columns), a developer is provided with the helpful values in blue._

CSS Gridish is then ran in a command line with just `npx css-gridish`. You should then see a folder with all of the files for your team to use your grid! The great thing about CSS Gridish is that it makes it pretty easy for first-time CSS Grid users. After users learn the classes detailed in the documentation, they will typically use only two rules:

```
.myElement {    grid-column: 1 / span 4; // Span four columns from first row    grid-row: 4 / span 8; // Span eight rows from fourth row}
```

The flexbox fallback code works similar to most grid frameworks with recognizable BEM class naming.

By default, the code works with fluid columns and fixed rows. It also allows for vice-versa with helpful modifier classes. You will use the fluid row class to create shapes like squares that scale with the user’s screen width.

One gotcha when using CSS Gridish code is that we do not utilize the CSS Grid’s gap property for gutters. Instead, there are padding classes that are half a gutter size that you apply to respect the gutter. This is due to the inability to ignore gaps for situations like background colors and full-sized media. Hopefully the next version of the CSS Grid spec will resolve this.

### The Future

CSS Gridish aims to get more products to adopt CSS Grid sooner, and to make the transition easier for users and teams.

In the long-term, we hope this encourages an idea called two-dimensional component libraries. The industry has had a strong era of component libraries that fill the width the users place a component in. Now with CSS Grid, we can create components that also fill the height they are placed in. This provides more creative possibilities to those making a design system and more flexibility to the teams that use it.

For the meantime, please use and contribute back to CSS Gridish. There is much more work to be done!

If it helps you out, please leave [CSS Gridish](https://github.com/ibm/css-gridish) a star!

James Y Rauhut ([@seejamescode](https://twitter.com/seejamescode)) is an ATX Designer working for IBM Design. He loves to code, research, and try his best for God. The above article is personal and does not necessarily represent IBM’s positions, strategies or opinions.

Special thanks to [Hayley Hughes](https://twitter.com/hayhughes) for the discotastic logo. Also, the following people were a big help to the project itself: [Trevor Wong](https://github.com/electrostaticfleece), Daniel Kuehn, [Seth Johnson](https://twitter.com/sethrrr), Chiu-Ping Chiu, [Jen Downs](https://github.com/jendowns), [Josh Black](https://twitter.com/__joshblack), [Jessica Tremblay](https://twitter.com/poofichu), [Maranda Bodas](https://twitter.com/Maranda_Bodas), [Wonil Suh](http://www.wonilsuh.com/), [Quincy Larson](https://twitter.com/ossia), and the whole FED@IBM community

