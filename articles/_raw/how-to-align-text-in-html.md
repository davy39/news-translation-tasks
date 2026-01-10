---
title: How to Align Text in HTML – Text-align, Center, and Justified Example
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-22T16:02:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-align-text-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--8-.png
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: null
seo_desc: 'Text is essential on web pages, as it tells your users what your web page
  is all about.

  When you add text to your web page, it dictates the direction and feel of your web
  page based on your language.

  For example, by default, English moves from left t...'
---

Text is essential on web pages, as it tells your users what your web page is all about.

When you add text to your web page, it dictates the direction and feel of your web page based on your language.

For example, by default, English moves from left to right (LTR), while Arabic moves from right to left (RTL).

But most times, you won't want all your text to remain in only one position of your screen or container. You will want some to be in the center, some to the left, and others to the right. You might even want the text to fill up your page or container.

This is similar to what you do when editing texts in Microsoft Word or Google Docs, using the left align, right align, center, and justify buttons.

You can also do the same on your web pages using code.

## How to Align Text to Center Before HTML5

Before the introduction of HTML5, developers performed specific styling with HTML tags. For example, you could use the center tag to align your text to the center, but in HTML4, this tag got depreciated. Although this may still work with some major browsers, it might get dropped at any point.

Here's what it looks like:

```html
<center>
  <h1> Welcome to freeCodeCamp </h1>

  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.

    Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>

  <h3>How we work</h3>

  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>
</center>
```

This will output all our text in the center of the page or whatever container it is applied to:

![](https://paper-attachments.dropbox.com/s_1FCD88D32AEADC1D26B97285FE174892A040B3C1BC2D3128B4E56D61375B2EDB_1663883648627_image.png align="left")

But now that we have HTML5, we don't use this method anymore. Remember that it's essential to always handle all stylings with CSS. You should use HTML only to add markup to your web page.

## How to Align Text in HTML5

With CSS, you have many options that you can use to align your text. The major CSS property that works well with text alignment is the `text-align` property. You use this property to specify the **horizontal** alignment of text in an element.

Suppose you have some text on your web page, for example:

```html
<h1> Welcome to freeCodeCamp </h1>

<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.

  Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>

<h3>How we work</h3>

<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>
```

You can use the `text-align` property to move the text to the left, right, center, or even justify your content, so it fills the element or web page **horizontally**.

```css
// Syntax

text-align: start;
text-align: end;
text-align: left;
text-align: right;
text-align: center;
text-align: justify;
```

If you want to align the entire text on your web page, you can apply this property to any tag containing the text, such as the div tag, heading, paragraph, or body tag.

Before seeing an example, let’s explore the available options/values for this property.

* `start`: This is based on the direction. When the direction is left-to-right, `start` would mean `left`. If the direction is right-to-left, then `start` would mean `right`.
    
* `end`: This is also based on the direction. When the direction is left-to-right, then `end` would mean right. If the direction is right-to-left, then `end` would mean left.
    
* `left`: You use this to align the texts to the `left` edge of the page or container.
    
* `right`: You use this to align the texts to the `right` edge of the page or container.
    
* `center`: You use this to align the texts to the perfect `center` of the page or container.
    
* `justify`: You use this to adjust the text content to touch the left and right edges of your page or container.
    

The general syntax would be:

```css
selector {
  text-align: value;
}
```

### How to align text to the left

You might need to switch the alignment of your text to the left if it is originally on the right side. You do this by targeting the selector and using the `text-align` property alongside `left` as its value.

```html
// HTML
<p> Welcome to freeCodeCamp </p>

// CSS
p {
  text-align: left;
}
```

For example, if you have your content from the right of your screen using the RTL direction:

```html
<html dir="rtl">
  <body>
    <h1> Welcome to freeCodeCamp </h1>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.
      
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>
      
      <h3>How we work</h3>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>
  </body>
</html>
```

This will output:

![](https://paper-attachments.dropbox.com/s_1FCD88D32AEADC1D26B97285FE174892A040B3C1BC2D3128B4E56D61375B2EDB_1663885469001_image.png align="left")

You can style the body tag to align the page's text to the `left`:

```css
body{
  text-align: left;
}
```

### How to align text to the right

By default, your web page or content in the container and other elements start from the left. You might want to align this content to the right, which is accessible using the `text-align` property with a value `right`.

```html
// HTML
<p> Welcome to freeCodeCamp </p>

// CSS
p {
  text-align: right;
}
```

### How to align text to the center

Instead of using the `center` tag to move our text content to the center, you can now use the `text-align` property alongside the `center` value to move your text to the center.

```html
// HTML
<p> Welcome to freeCodeCamp </p>

// CSS
p {
  text-align: center;
}
```

### How to justify text

If you know how to use any text-based tool like Microsoft Word or Google Docs, or tools like Photoshop, Figma, and many more that handle content, you will know how the justify text icon works.

You use it to help your text go up to the edges of a page/container rather than having some unnecessary uneven spaces at the end.

This is not always obvious, but when you take a deep look at the edges, you'll notice the difference, which makes more sense when you have so much text and longer paragraphs.

![](https://paper-attachments.dropbox.com/s_1FCD88D32AEADC1D26B97285FE174892A040B3C1BC2D3128B4E56D61375B2EDB_1663887493952_Untitled.drawio+12.png align="left")

You do this by using the `text-align` property alongside `justify` as its value:

```html
// HTML
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto, inventore. Culpa, rerum neque. Necessitatibus quod velit vitae unde sed? Expedita consequuntur ea quis reiciendis nobis distinctio quod deserunt doloremque in.</p>

// CSS
p {
  text-align: center;
}
```

## Wrapping Up

In this article, you have learned how to align the text of your HTML web page using `text-align` CSS property.

You can learn more via other similar articles that have been published on freeCodeCamp:

* [CSS Text Align – Centered, Justified, Right Aligned Text Style Example](https://www.freecodecamp.org/news/css-text-align-centered-justified-right-aligned-text-style-example/)
    
* [Text Align in CSS – How to Align Text in Center with HTML](https://www.freecodecamp.org/news/text-align-in-css-how-to-align-text-in-center-with-html/)
    

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
