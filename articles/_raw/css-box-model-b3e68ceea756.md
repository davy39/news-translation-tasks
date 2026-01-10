---
title: Unboxing the basics of the CSS Box Model
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-14T21:12:27.000Z'
originalURL: https://freecodecamp.org/news/css-box-model-b3e68ceea756
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1ch1pHZSb3YDog3PlZ7oFQ.jpeg
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Bryan Smith

  Understanding the CSS Box Model is crucial in being able to master how elements
  are laid out on a page. In the most basic of terms, the Box Model is as follows:
  margin, border, padding and content. But what does that all mean? How do t...'
---

By Bryan Smith

Understanding the CSS Box Model is crucial in being able to master how elements are laid out on a page. In the most basic of terms, the Box Model is as follows: margin, border, padding and content. But what does that all mean? How do these words work together?

_Welp._

In this week’s post we’ll jump right into it and have you feeling like a Box Model Master. Styling elements and giving them proper spacing left and right (and top and bottom…get it? Because you are arranging your elements on the page ?…sorry for the bad jokes).

Take a peek at this visual break down provided by the Chrome Console:

![Image](https://cdn-media-1.freecodecamp.org/images/0*fL7IZ5XJwHsQth-a.png)
_You can see this visual by right-clicking your page in Chrome (or your browser of choice), clicking Inspect to open the developer console, selecting the Styles tab and then scrolling down to the very bottom._

You can see that each part of the Box Model is labeled for you except content — that’s the blue box in the very middle. Let’s break down how each part works and the unique differences between them.

### Margin

You can think of the margin as a buffer for your element. Want a little space around your element? That is what margin is there for. Let’s imagine you have a cold. You should (hopefully) be staying away from people so you don’t spread it around. You need some margin around you. Take a look at this image to further illustrate:

![Image](https://cdn-media-1.freecodecamp.org/images/0*oN7zT5zI3B4lfjED.png)

Notice how your friends are all spread out from you and you’re surrounded by orange? That is margin in action. You remain the same size but there is a no-entry zone for all things around you. Same thing goes for elements on your page. Margin will give you space around your element and keep things separated. To put it simply, margin will put invisible spacing around your element without directly affecting its size. In this example we’ve made it orange to give you a visual cue of where it stands in relation to the content (a sick you in this case).

### Border

Border is the second property from outside edge of your element. Border, as you may have guessed, is used to define a visual edge to your element. Border will increase the presentational size of your element or the part that is visually seen on the screen. There can still be margin involved, but it will be on the outside edge of the border. Lets take another look at you being sick, but this time with a little border involved:

![Image](https://cdn-media-1.freecodecamp.org/images/0*0SJmRV2kv6hOH4uw.png)

It looks almost identical to the margin demo before, except there is now a black box around it. That is our border. One thing to remember is that our content (the sick emoji) is now the size of the emoji plus the border on each side.

Okay, enough of the sick emoji. Let’s talk about padding.

### Padding

Padding is the third item from the outside edge. And, like the margin and border before it, is totally optional. The biggest thing to keep in mind when trying to find the difference between margin and padding is that padding WILL increase the presentational size of your element.

Let’s imagine your grandmother is sending you a birthday gift. She packs it up and sends it off in the mail. Now, being that your grandmother doesn’t want your present to get ruined while being sent to you, she really adds to the packaging. Here is a visual for what I mean:

![Image](https://cdn-media-1.freecodecamp.org/images/0*4BcD7TiSsoCxd2fo.png)

You receive the gift and assume that grandma went all out and got you a 60 inch TV.

Wrong.

She just added some padding (see what I did there?) to the box that made it take up more space and appear bigger.

Let me give you a relevant coding example. You create a `<d`iv> that is 100px wide by 100px tall. You add 10px of padding to each edge, and now `that` <div> is 120px wide by 120px tall because of the added padding on each side. Keep that in mind as you are laying out the elements of your page.

### Content

Content, content, content. This is what our page is made of. Content is how you initially describe it in your CSS or its natural height if you are using an image. You created a `<d`iv> that is 50px wide by 300px tall? That is how much real estate on your screen it will take if it isn't altered by any of the above parts of the Box Model. Content is the present your Grandma gave you, it is the sick emoji.

### Box Sizing

I would be remiss if I didn’t mention `box-sizing: border-box` right now. I don't want to dive too deep into the specifics of it, but there is a CSS property called `box-sizing` that defaults to `content-box` for its value. Take a look at this CodePen to demonstrate. The children have no respect of the parent container, extending out of it.

And now with the power that is `box-sizing: border-box`:

The children are now contained inside of the parent (and probably doing their chores and coming home by curfew). The CSS is exactly the same in each demo, except for one small addition to the second one:

```
*, *:before, *:after {   box-sizing: border-box; }
```

These three lines of code are telling every element on our page to calculate their width and height with border and padding added to it, whereas the first demo was a free wheelin’ mess that didn’t respect anyone or anything. The padding and border were added to the width and flowed outside of the parent container.

### Wrapping it all up

The box model is fundamental to understanding how things will lay out on your page. Hopefully, you now have a great understanding of how the Box Model works and how you can use it to your advantage. I also hope this means no more typing “margin: 10px;…[wait for page changes…delete, delete, delete] padding: 10px…”.

_Originally published at [www.frontamentals.com](https://www.frontamentals.com/css-box-model)._

