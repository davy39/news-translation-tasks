---
title: The Periodic Table of Australian Startups Built With CSS Grid ??
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-13T19:55:28.000Z'
originalURL: https://freecodecamp.org/news/the-periodic-table-of-australian-startups-4ab76b79ee34
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yhblHz6Wa1PcKUX4c3QggQ.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Shooting Unicorns

  This month the two derp developers at Shooting Unicorns embarked on their journey
  to learn CSS Grid by building a periodic table. As a little tribute to working in
  corporate for 5 years and recently bidding farewell to join the s...'
---

By Shooting Unicorns

This month the two derp developers at [Shooting Unicorns](https://shooting-unicorns.com) embarked on their journey to learn CSS Grid by building a periodic table. As a little tribute to working in corporate for 5 years and recently bidding farewell to join the startup life, the derps believed that sharing corporate buzzwords would be the perfect project.

1. Put it on the blockchain
2. Disruptive technology
3. We’re an agile company
4. Bleeding edge technology
5. It’s in the cloud
6. Our designs are human-centric
7. Digital transformation
8. Thought leadership
9. Big data and analytics
10. 360-degree view
11. Bespoke designs
12. It’s IoT enabled
13. Creating synergies
14. Breaking down the silos
15. Real-time automation
16. … ?

But little did they know that there are actually a total of 118 elements in a periodic table. It soon became apparent to them that coming up with that many corporate buzzwords was going to be tougher than learning CSS Grid itself. No doubt, the corporate world is littered with thousands upon thousands of buzzwords, but unfortunately for the duo, recalling any more than 7 plus or minus 2 items would be deemed a very difficult task.

![Image](https://cdn-media-1.freecodecamp.org/images/xSQ7fXrbp8pQeuhnKwuYACkhOZzvEgtRD7Nk)

Now they are left with no choice but to do what they do best… last minute pivoting! ?

And thus… [The Periodic Table of Australian Startups](https://startups.shooting-unicorns.com) was made instead! Or as they like to call it, the Completely Selective Startup Grid (CSS Grid) (◔_◔)

### The Idea

In all seriousness, we were inspired by [Deck](http://www.hi.agency/deck/), a presentation deck developed without using any Javascript which really inspired us to try it out.

![Image](https://cdn-media-1.freecodecamp.org/images/yntoXwQCEDWkGtV6Qd7kDu9SaaXBeXFia31C)

It is arguably the most powerful layout system available in CSS and allowed us to handle both columns and rows, making it multi-dimensional. We got super excited that day and really wanted to do our very own [Shooting Unicorns](https://shooting-unicorns.com)Deck, but for some reason we settled on doing a periodic table instead ??.

We guess one reason would be that while the deck looks really cool, getting it to look pretty would have taken a huge chunk of time away from learning CSS grid itself. You can check out the Deck’s source code [here](http://provide.smashingmagazine.com/css-grid-challenge/deck-css-grid-template.zip?_ga=2.45532898.732059500.1519294938-1524689586.1519294938).

#### Therefore in the last two weeks…

We followed what we believed to be the secret recipe and figured out the layout of the grid using…

![Image](https://cdn-media-1.freecodecamp.org/images/XYH4DLH45utbfKvHEG1skHgOZKoizbWMnuwS)

To determine how many boxes the grid needed to be, we needed to think in terms of rows and columns, factoring in the blanks as well.

A periodic table has 118 elements. So if our math hasn’t failed us, to get our grid to look like one would require 18 columns and 9 rows making it a total of 162 boxes.

Our first iteration of the periodic table was as follows:

```
.firstElement {   grid-row: 1 / span 1;   grid-column: 1 / span 1;}
```

```
.secondElement {   grid-row: 2 / span 1;   grid-column: 1 / span 1;}
```

```
...nthElement{}
```

As you can imagine, after a while we eventually made 118 classes just to show the periodic table.… hmmm ?. Surely, there is a cleaner and more maintainable way to do this right? Therefore, we decided to not take matters into our own hands, and followed the example h[ere.](https://codepen.io/dudleystorey/pen/rmWMXY/)

We discovered that CSS grid uses magical layout algorithms which can determine the flow of the grid. If we don’t specify the direction of flow (using grid-auto-flow), then it will fill all columns in a row first before going to the next.

Round two. We deleted the original CSS code and started again. This time we were smarter. You can refer to the rest of this article following our source code [**here**](https://github.com/shooting-unicorns/the-periodic-table-of-australian-startups)**.**

![Image](https://cdn-media-1.freecodecamp.org/images/4hUYozPfP7dQS-VF0Bmx1yfYBtCwjZYpJCcq)

Firstly, let’s take a look at the first row of the periodic table. The first element is automatically placed in row 1, column 1. By default, the second element will be placed in row 1, column 2, but that’s not what we want. Following the diagram, to place it in the 18th column, we can do it like so:

```
.itemInEighteenthColumn {   grid-column-start: 18;}
```

So, to get the next element in the second column, we just tell CSS to place it in row 2 column 1 right?

```
.thirdElement {   grid-column-start: 1;   grid-row-start: 2;}
```

That is one way, but in CSS grid, specifying a grid-column-start on a child element will automatically create that many numbers of columns. So in this case, we said that the second element should start at column 18, so our grid would contain 18 columns. Any element after that would flow to the next row.

![Image](https://cdn-media-1.freecodecamp.org/images/NLwWeR-UQXFH2uB4eBgpep7RxaVVZxIc9UXb)

The same concept goes for the third element in the second row. We set the grid column start to row 13 to create that gap.

```
.secondRowThirdElement {   grid-column-start: 13;}
```

This makes all the columns before row 13 blank, and the rest of the elements would assume their normal flow starting from 13 through to 18. The same goes for the next row after that:

```
.secondRowThirdElement, .thirdRowThirdElement {   grid-column-start: 13;}
```

The only special case we had to cater for were the last two rows on the bottom, which required specific grid properties. The reason for this is that those elements weren’t the last few elements in our HTML, so they would end up misplaced in the rows above. To get those elements on row 8 and 9, we need to explicitly state the grid-row-start property to those individual elements (it is required to add those classes to each individual element in the HTML):

```
.row-8 {   grid-row-start: 8;}
```

```
.row-9 {   grid-row-start: 9;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/07-ihShFAeTkGeRHOkrfV9Ceeoxt0KvRysii)
_Result after setting .row-8 and .row-9_

And with this CSS Grid magic, we got our first periodic table.

![Image](https://cdn-media-1.freecodecamp.org/images/RxBFT9R2dHly4c37Svl8cNy4R0SYda5HSl2H)

#### Scripts

It would have taken way too much effort to manually copy and paste startup data into an HTML file. To get the job done, we created Python scripts to convert CSV into JSON and then from JSON into HTML. Here is a snippet of how we generated the HTML (not the best, but it worked nonetheless):

```
import json
```

```
with open('./startups.json') as startup_data:with open('./startups.html', 'w+') as f:
```

```
d = json.load(startup_data)   for startup in d:   name = startup['name']   city = startup['city']   founded = startup['founded']   description = startup['description']      htmlString= "\   <div class=\"startup-detail-container %s\"> \n\   <div class=\"startup-em\"></div>\n\   <div class=\"name\">%s</div>\n\   <div class=\"description\">%s</div>\n\   </div>\n\n"%(city.lower(), name, description)   f.write(htmlString.encode('utf-8'))
```

There were additional scripts that were used to clean and add extra information to the existing data, but we won’t bore you with the details.

#### The rest of the puzzle

From here on out, the rest was pushing pixels and playing around with colors. We initially went with the Shooting Unicorns color scheme, but as colorful as it looks, the theme seemed a bit ‘un-themed’.

![Image](https://cdn-media-1.freecodecamp.org/images/r7PQ0SXP5U9hJVy3dEsG3lc5y7DLHc1iQGrP)

Many days later… we eventually settled on none other than the colors from our terminal… because… developers.

![Image](https://cdn-media-1.freecodecamp.org/images/Qyc7Jp5DotCQPayiNIAxX-aJnEEFxEW8bhOQ)
_**Live version [here](https://startups.shooting-unicorns.com" rel="noopener" target="_blank" title=")**_

We’re still very new to CSS, but we hope this project will at least inspire or help others to do the same thing. If you haven’t seen our code yet, you can check out our repo [**here**](https://github.com/shooting-unicorns/the-periodic-table-of-australian-startups)**.** We would also love to get any feedback on how we could improve the current codebase, too. Please feel free to share your thoughts below or even raise a pull request!

#### What’s Next? ?

Each month [Shooting Unicorns](https://www.freecodecamp.org/news/the-periodic-table-of-australian-startups-4ab76b79ee34/undefined) will ship a passion project while learning a different technology. For January, it was a React project called [Hustle Club](https://hustle.shooting-unicorns.com), a platform that helps people find the perfect accelerator in beautiful Australia.

In March, we’ll be sharing everything we learned in Swift wrapped up in a little bow. You’ll see exactly how we hacked our way from startups through to enterprises!

**Stay tuned and until next time, happy hacking!**

Amount of times pivoted: 100% ✌️

