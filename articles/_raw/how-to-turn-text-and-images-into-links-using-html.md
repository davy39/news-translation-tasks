---
title: HTML Link – How to Turn an Image into a Link and Nest Links Inside Paragraphs
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-06-06T13:52:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-turn-text-and-images-into-links-using-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/markus-spiske--dbOrdtrR1A-unsplash.jpg
tags:
- name: HTML
  slug: html
seo_title: null
seo_desc: 'There will be times where you will want to nest links inside paragraphs
  or turn an image into a link. But how do you go about doing that in HTML?

  In this article, I will show you how to nest links inside paragraphs and how to
  turn an image into a lin...'
---

  
There will be times where you will want to nest links inside paragraphs or turn an image into a link. But how do you go about doing that in HTML?

In this article, I will show you how to nest links inside paragraphs and how to turn an image into a link using code examples.

## **How to nest anchor tags inside paragraph tags**

If you want to include links inside your paragraphs, then you can nest anchor tags inside the paragraph tags.

In this first example we have the text "I love freeCodeCamp".

```html
<p>I love freeCodeCamp</p>
```

If I wanted to turn the word freeCodeCamp into a link, then I would wrap it inside a set of anchor tags.

```html
<p>I love <a href="https://www.freecodecamp.org/">freeCodeCamp</a></p>
```

We can also add the `target="_blank"` attribute to have that link open up in a new tab.

```html
<p>I love <a target="_blank" href="https://www.freecodecamp.org/">freeCodeCamp</a></p>
```

When you hover your mouse over the word freeCodeCamp, you will notice that it is a link you can now click on which will direct you to the website.

%[https://codepen.io/jessica-wilkins/pen/BaYVREm]

Nesting links inside paragraph tags is helpful when you want to direct your users to additional information concerning the main content on the page.

In this next example, I have a paragraph talking about the courses available at freeCodeCamp.

```html
<p>I started learning how to code using freeCodeCamp. I really enjoyed their Responsive Web Design course. I am looking forward to starting the JavaScript course soon.</p>
```

I want to first turn the word freeCodeCamp into a link to direct people to the website.

```html
<p>I started learning how to code using  <a href="https://www.freecodecamp.org/">freeCodeCamp</a>. I really enjoyed  their Responsive Web Design course. I am looking forward to starting the  JavaScript course soon.</p>
```

Now I am going to add another link for "Responsive Web Design course" which will direct people to the project-based curriculum.

```html
<p>I started learning how to code using  <a href="https://www.freecodecamp.org/">freeCodeCamp</a>. I really enjoyed  their  <a href="https://www.freecodecamp.org/learn/2022/responsive-web-design/">Responsive Web Design course</a>. I am looking forward to starting the JavaScript course soon.</p>
```

Lastly, I am going to add a link for the JavaScript course, which will direct users to the JavaScript curriculum.

```html
<p>I started learning how to code using <a href="https://www.freecodecamp.org/">freeCodeCamp</a>. I really enjoyed their <a href="https://www.freecodecamp.org/learn/2022/responsive-web-design/">Responsive Web Design course</a>. I am looking forward to starting the <a href="https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/">JavaScript course</a> soon.</p>
```

This is what the final result would look like in a web browser:

%[https://codepen.io/jessica-wilkins/pen/ExQRmqY]

## How to turn an image into a link

In HTML, we can use the `<img>` element to add images on the page. In this example, we are adding an image of five cats.

```html
<img  src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"  alt="Five cats looking around a field."/>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-02-at-10.39.02-PM.png)

  
If we wanted to make that image a clickable link, then we can place it inside a set of anchor tags.

```html
<a href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Five cats looking around a field."/></a>
```

We can also add the `target="_blank"` attribute to have that link open up in a new tab.

```html
<a target="_blank" href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Five cats looking around a field." /></a>
```

When you hover your mouse over the image, you will see the cursor pointer indicating that it is a link directing you to an article about cats.

%[https://codepen.io/jessica-wilkins/pen/XWZYRgy?editors=1000]

## **Conclusion**

In this article we learned how to nest anchor tags inside paragraphs and how to turn images into links.

To add links inside paragraphs, we can nest anchor tags inside paragraph tags. 

```html
<p>I love <a href="https://www.freecodecamp.org/">freeCodeCamp</a></p>
```

To turn an image into a link, we can nest an `img` element inside anchor tags.

```html
<a href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Five cats looking around a field."/></a>
```

I hope you enjoyed this article and best of luck on your programming journey.  

