---
title: The relationship between HTML, CSS and JavaScript explained by building a city
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-09T04:04:25.000Z'
originalURL: https://freecodecamp.org/news/the-relationship-between-html-css-and-javascript-explained-by-building-a-city-a73a69c6343
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4jvOC7UafUwx4f1xEWMQiA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever visited a walkable city like New York, then you can understand
  the way that HTML, CSS and JavaScript work together.

  When you start learning web development, you can usually try a series of basic challenges
  on the p...'
---

By Kevin Kononenko

**If you have ever visited a walkable city like New York, then you can understand the way that HTML, CSS** and **JavaScript work together.**

When you start learning web development, you can usually try a series of basic challenges on the principles of HTML, CSS and JavaScript. However, each challenge happens in a sandbox environment, and does not test you on multiple languages at once.

For example, an “Intro to JavaScript” tutorial will usually focus on fundamentals like loops and ‘if’ statements, rather than using JavaScript alongside HTML.

After you get through these preliminary exercises, you reach the point where you need to set up your first full website. Even if this is a single-page, personal site that you never intend to release, you still face a series of new challenges like:

1. How do I connect the three different types of files?
2. After I connect them, how will they work together?
3. How do I test all of this on my own computer?

After thinking about this for awhile, I realized that these pieces work together in the same way that cities can still function. This applies even when businesses are constantly moving in or going out of business, or real estate developers are remaking certain neighborhoods.

So, I am going to show how you can set up your first development environment with these three pieces. In order to understand this tutorial, you just need to know the basic parts of HTML, CSS and JavaScript.

Even if you have not written any code in your life, you still will be able to understand how to link the three languages.

### The differences between HTML, CSS and JavaScript

Let’s imagine that you are in charge of planning the layout of a new neighborhood in the city. This neighborhood will have some residential buildings, some eateries, a bank branch, and a mall.

![Image](https://cdn-media-1.freecodecamp.org/images/0*87frx07SsrDA4UZl)
_Our neighborhood’s layout_

This might seem one-dimensional. In other words, each building is just a point on a map, with no nuance. But when you dig a little deeper, you can see that each building actually has three parts you can change:

1. The structure of the building itself
2. The interior and exterior decoration of the building
3. The actual functions that visitors can perform in each building

This corresponds to the three different types of files that you can use in your first website.

An **HTML file** contains the structure of the page itself. It is kind of like the structure of the building.

A **CSS file** contains the styling of the page. It allows you to change colors, positioning and more. It is kind of like the design of the building itself.

A **JavaScript file** determines the dynamic and interactive elements on the page. It determines what happens when users click, hover, or type within certain elements. This is kind of like the functionality of the building.

Let’s take the example of one of the houses. A house has two bedrooms, two bathrooms, and two stories. That is the HTML of the building.

It is made of brick and has a solid wood door. That corresponds to the CSS of the building.

What can you do within the house? You can eat, sleep, make meals… anything that you do at home, really! That is the JavaScript of the building.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3GaOb3tSGoZe4DjTZg9VXQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*5GAPClpa09DmNcCslMA23Q.png)

### An example of a basic file directory

Since each of these three languages serves a different purpose, web developers generally use separate files for each one. This idea is called “[separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)” — each file should have a different function within the site as a whole.

Although you could technically include all the code in one HTML file, that will eventually lead to repetitive code as you grow your site.

Let’s look at the code needed to create one complete house. All three files must be in the same **directory** — a folder on your computer. In this case, let’s call the folder _house_. In our house folder, we will have one file of each type. I will call the main HTML file _index_, the main CSS file _styles_, and the main JavaScript file _scripts_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YZOpTO65ASByn5i29VDmRQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*18ZU8N-2YsccoCU8z9uWOw.png)

Now we can cover the way that files become linked in code.

Our HTML file actually has three separate sections:

1. The `<he`ad>, where you can include metadata and links to services like Google Fonts.
2. The `<bo`dy>, where you include the actual HTML elements.
3. The `<scri`pt> tags, which can link to Google Analytics and JavaScript files

Right now, all three files are contained within one folder, so the file paths are pretty simple within the HTML file.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pOBUVpf8jG1SMvlv7R4E9g.png)

The `<li`nk> tag will allow you to create a separate stylesheet to use with all brick houses usin_g the style_s.css file.

And the `<scri`pt> tag allows you to create a set of functions that would apply to any type of home i_n the scri_pts.js file.

### Scenario 1: a new pizza chain moves in (CSS file change)

Let’s look at a real-world example. Imagine that in this neighborhood, one of the buildings is a pizza shop called Neighborhood Pizza (great name). But, Neighborhood Pizza is struggling, and Domino’s (a huge pizza chain) decides to buy the property and serve the neighborhood instead.

![Image](https://cdn-media-1.freecodecamp.org/images/0*HM67ZGkZ913HLLqu)

Do you know what this would mean in terms of code?

Well, let’s think through each of the three pieces.

1. The structure of the building is the same. It’s still the same pizza place. That is the HTML.
2. The functionality of the building is the same. It still exists in order to serve pizza, and when customers come in, that is the only thing they expect. That is the JavaScript.
3. But the styling and branding of the building is different! That means the CSS is new.

So, we have now created a new CSS file (let’s call it _Dominos.css_). We need to create a folder called _pizza_ to show we are talking about a pizza place now, and substitute _dominos.css_ for the old _styles.css_ file.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cbrhmfv7aXM-LkfrfL2JUQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*1YOCfrsFIWq-bJRYioaaFQ.png)

### Scenario 2: a new apartment building

Here’s another example. Let’s say your neighborhood is undergoing some [gentrification](https://en.wikipedia.org/wiki/Gentrification). That means wealthier residents are moving in, and more expensive housing is being built. Some real estate developers decide to buy up a lot with a house on it, demolish the house, and put in some fancy apartments.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_PA4fk1-hIzyQRc2)

Let’s think about what that would mean in terms of our file system.

1. The functionality is the same thing. It’s still a home. That means JavaScript is the same.
2. The CSS must be different because there is no way that an apartment building can be styled in the same way as a house!
3. And the HTML file must be different, because the two buildings have completely different structures.

Let’s call the new building _apartment.html_, and the new CSS will be _fancy.css_. Since we have an entirely new HTML file, we are not simply linking up a new CSS file. The entire page is different. And it also links to a new CSS file.

![Image](https://cdn-media-1.freecodecamp.org/images/1*T8leHgkgP-X8L_wcsM2kCQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*aKoiZBHRCzjLCPp6weEwWA.png)

The CSS and JavaScript files simply modify the HTML. They need to be referenced in the HTML file in order to be loaded. That is why, in the diagram above, the folder itself is the same. But the HTML file and the code that links it to the other files are different.

### Creating a file directory with multiple folders

So far, we have covered just one type of building at a time. But that’s kind of like a website with just one page — very unusual. Even a personal website might have an “About” page, a “Portfolio” page, and so on. So what happens when there are multiple buildings? How can you structure your file directory?

Let’s say that your neighborhood has a bank, a mall and a pizza place. That’s kind of like a website with three pages. Each one is an HTML file with a CSS file and JavaScript file linked to it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nXl1p_RnKNh3_iOD7fPXhw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*tUpDr4vgMsncf2XgHRv5Yg.jpeg)

But, notice how we did not use three subfolders within a greater neighborhood folder! Although we certainly could have done that, many front-end developers like to create a separate _scripts_ folder for all JS files, and a _styles_ folder for all CSS files.

As your site grows, you will find that some pieces of CSS and JavaScript are reuseable, and can be linked to multiple HTML files. The scripts and styles folders allow you to organize your efforts and reduce redundant code.

In our example, you can order a greasy slice of pizza in both a mall AND a pizza shop. So, you might expect that both would share one JavaScript file, but also have unique functionality in their own individual JavaScript files.

Anyways, here is a potential layout of the whole file directory.

![Image](https://cdn-media-1.freecodecamp.org/images/0*6ADmIY53-wQGVP9M)

Notice how the HTML files and folders are the same level of depth within the greater _neighborhood_ folder. In order to reference files that are within folders at the same level, you need to start your filepath with the folder name instead of a file name. So, if you wanted to reference the _bank.css_ file from within bank.html, you would use `scripts/bank.css` as the file path.

### Get the latest tutorials

Did you enjoy this tutorial? Give it a “clap” and let me know in the comments. Or, get my latest web development explanations by signing up for my newsletter:

