---
title: How to Make a Custom Mouse Cursor with CSS and JavaScript
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2022-01-10T16:13:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-custom-mouse-cursor-with-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/salman-hossain-saif-m3xjTe9zl6k-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Have you ever visited a website and been totally blown away by its amazing\
  \ features? One of them might be a cool mouse cursor that is different from the\
  \ regular arrow or pointer cursors you are used to.  \nThis can really improve user\
  \ experience, and ..."
---

Have you ever visited a website and been totally blown away by its amazing features? One of them might be a cool mouse cursor that is different from the regular arrow or pointer cursors you are used to.  

This can really improve user experience, and lately I've been wondering how it works. So I started to do some research and I found out how it is done.

In this article, I will be explaining how to make a custom mouse cursor. By the end of this article you will learn how to make these cursors with two different methods, using CSS and JavaScript. Then you be will ready to vamp up your website with different creative cursors to keep your audience engaged. Ready? Let's dive in.

## Prerequisites

This article is beginner-friendly, but to understand some concepts you should have basic knowledge of:

* HTML
* Basic CSS
* Basic JavaScript

## How to Customize a Mouse Cursor with CSS

Customizing a mouse cursor with CSS is pretty simple, as CSS already has a property to handle this. All we need to do is identify this property and use it. 

As Frontend Engineers we use this property often – it is none other than the almighty `cursor` property. Yes, that property is what gives us the power to make a custom cursor of our choice.

Before we go to a practical example, let's look at the values associated with the CSS `cursor` property. While most developers just use a few important ones, there are more we should look at.

%[https://codepen.io/developeraspire5/pen/XWeBEXo]

From the above code snippet and from the results, you can see and test out different mouse cursors that CSS has by hovering your mouse cursor on each of those boxes containing the name of each CSS `cursor` property value.

Now how do I use CSS to customize a mouse cursor? To use this, you just have to tell CSS what image you intend to use and point the cursor property to the image URL using the `url` value.

```css
body {
  cursor: url('image-path.png'),auto;
}
```

From the code snippet above, you can see I set this on the document body, so it can apply to the cursor no matter where it moves. It has the image specified in `url()`.

The next value of the property is a fallback, just in case the image doesn't load or can not be found maybe due to some internal glitches. I'm sure you wouldn't want your website to be "cursor-less", so adding a fallback is very important. You can also add as many fallback URLs as you can or want.

```css
body {
  cursor: url('image-path.png'), url('image-path-2.svg), 
          url('image-path-3.jpeg'), auto;
}
```

You can also customize the cursor on a particular element or section of your webpage. Below is a CodePen example:

%[https://codepen.io/developeraspire5/pen/GRMBxWN]

That is all there is to customizing cursors in CSS. Now let's see how we can do this is JavaScript.

## How to Make Custom Mouse Cursors with JavaScript

To make this happen with JavaScript, you need to manipulate the DOM to get the desired result. 

First, let's see the HTML:

### The HTML

```html
<div class="cursor rounded"></div>
<div class="cursor pointed"><div>
```

From the code snippet above, I created two `divs` to represent the cursor. The plan is to manipulate these divs from JavaScript so their movement over the webpage is scrolled by the JavaScript `mousemove` event using the X and Y coordinates of the mouse movement. 

Now let's get to the CSS part which will all make sense piece by piece.

### How to style custom cursors with CSS 

```css
body{
  background-color: #1D1E22;
  cursor: none;
}

.rounded{
  width: 30px;
  height: 30px;
  border: 2px solid #fff;
  border-radius: 50%;
}

.pointed{
  width: 7px;
  height: 7px;
  background-color: white;
  border-radius: 50%;
}
```

Taking a look at the CSS code above, I disabled the cursor (remember `cursor:none`?). This will make the cursor go invisible, allowing our custom cursor only to display. 

The `divs` I styled to give them a unique "cursor-like" look. You can absolutely do more with it, maybe add a background image, emoji, stickers and so on provided there are images. Now, let's take a look at the JavaScript

### How to use JavaScript to make the cursor move

```javascript
const cursorRounded = document.querySelector('.rounded');
const cursorPointed = document.querySelector('.pointed');


const moveCursor = (e)=> {
  const mouseY = e.clientY;
  const mouseX = e.clientX;
   
  cursorRounded.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
  
  cursorPointed.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0)`;
 
}

window.addEventListener('mousemove', moveCursor)
```

I added an event listener on the global window object to listen to any mouse movement. When the mouse moves, the `moveCursor` function expression is called and it receives the event object as a parameter. With this parameter I was able to get the X and Y coordinates on the mouse at any point on the page.

I already selected each kind of cursor from the DOM using JavaScript `querySelector`. So all I had to do was move them according to the X and Y coordinates of the mouse by controlling the transform properties on the style with the `translate3d` value. This will enable the divs to move when the mouse moves to any point on the webpage. 

And the backticks you see are called template literals. This enables writing variables easily to append them to strings. The alternative would be to concat the variables to the strings.

Simple, right? That's it!

Below is a CodePen sample and result of the above code snippet:

%[https://codepen.io/developeraspire5/pen/gOGjeZG]

## Which Method Works Best?

Now it's up to you as the developer to choose which method works best for you. You may choose to use CSS if you want to use some pretty emojis or images as a cursor. On the other hand, you might want to use JavaScript so you can customize complex shapes of your choice and animate the cursor's movement.

Either way is fine, as long as you get your desired results and wow all your site's visitors.

I hope you learnt a lot from this article, an d I am looking forward to seeing what you build with this knowledge. 

For more CSS tips, follow me on [Twitter](https://twitter.com/DeveloperAspire).

Thanks for reading, See you next time.

