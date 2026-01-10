---
title: HTML Line Break – How to Break a Line with the HTML <br> Tag
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-20T17:21:23.000Z'
originalURL: https://freecodecamp.org/news/html-line-break-how-to-break-a-line-with-the-html-br-tag
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/linebreak.png
tags:
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'When you''re writing HTML, you often need to insert line breaks. A line
  break is essential in addresses, poems, or when text exceeds the available browser
  width. If you don''t insert your own line breaks, then the text gets formatted in
  an odd way.

  In ...'
---

When you're writing HTML, you often need to insert line breaks. A line break is essential in addresses, poems, or when text exceeds the available browser width. If you don't insert your own line breaks, then the text gets formatted in an odd way.

In this tutorial, I'm going to show you how to insert line breaks in your HTML code with some "with and without" examples, so you can start using it correctly and format your text better.

## Basic HTML Line Break Syntax

You can insert line breaks in HTML with the `<br>` tag, which is equivalent to a carriage return on a keyboard. 

Be aware that HTML will ignore any line break from a keyboard’s return key.

```html 
<br />
```

If you are wondering why there’s a forward slash in the `<br>` tag above, the slash was important when HTML4 was still widely used. With HTML5, you don’t need to put a slash in it anymore. But both will do the same thing. 

If you are using a code formatter like prettier, it'll always insert the slash when you save or paste even if you don’t put it in there.

## How to Insert Line Breaks in Addresses 

A line break is important when you're writing an address on a letter, for example, in order to format it properly.

### Here's an example of an address without line breaks

An address without line breaks (`<br>` tags) looks like this:

```html
<p>
     The White House, 1600 Pennsylvania Avenue NW Washington, DC 20500, USA.
</p>
```
I have added some CSS code to center everything with Flexbox and make the text a bit bigger:

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    font-size: 3rem;
    max-width: 1000px;
    margin: 0 auto;
}
```

This is how it looks in the browser: 
![address-without-line-breaks](https://www.freecodecamp.org/news/content/images/2021/08/address-without-line-breaks.png)

### Here's an address with line breaks 

And this is how we can add line breaks to properly format our address:

```html
<p>
    The White House <br />
    1600 Pennsylvania Avenue <br />
    NW Washington, DC <br />
    20500 <br />
    USA
</p>
```

It looks like this in the browser: 
 
![address-with-line-breaks](https://www.freecodecamp.org/news/content/images/2021/08/address-with-line-breaks.png) 

## How to Add Line Breaks to Poems

Poems are conventionally written in short breaking sentences in order to create visual hierarchies and format them nicely. 

So, if you want to write a poem in your HTML code, the `<br>` tag makes the formatting process easier for you.

### A poem without line breaks 

```html
<p>
      I dabbled around a lot when I decided to learn to code 
      I went from A to Z with resources 
      When I decided to make my own things 
      I discovered I've been in the old all while 
      So I remained a novice in coding 
      But then I found freeCodeCamp 
      I got my hands on the platform 
      I went from novice to ninja in coding 
     And now I'm a camper for life
</p>
```

It looks like this in the browser: 

![poem-without-line-break](https://www.freecodecamp.org/news/content/images/2021/08/poem-without-line-break.png)

You can see the poem has no visual hierarchy, it is not formatted the right way, and so it is unreadable as a poem. 

### A poem with line breaks 

```html
<p>
      I dabbled around a lot when I decided to learn to code <br />
      I went from A to Z with resources <br />
      When I decided to make my own things <br />
      I discovered I've been in the old all while <br />
      So I remained a novice in coding <br />
      But then I found freeCodeCamp <br />
      I got my hands on the platform <br />
      I went from novice to ninja in coding <br />
      And now I'm a camper for life <br />
</p>
```

I also changed the font size a bit in the CSS:

```css
body {
   display: flex;
   align-items: center;
   justify-content: center;
   height: 100vh;
   font-size: 2.5rem;
   max-width: 1000px;
   margin: 0 auto;
}
```

It now looks like this in the browser:

![poem-with-line-break](https://www.freecodecamp.org/news/content/images/2021/08/poem-with-line-break.png)

You can see that the poem is now more readable and formatted the right way.

**Some valuable advice:** Do not use the `<br>` tag to force a space between block-level elements (`p`, `h1`, `h2`, `h3`, `div`, etc). Instead, use the CSS margin property.

You might be wondering – since the `<br>` tag is an element, is it possible to style it? 

Well, it is possible. But there’s no real practical need to style it since all it does is create a couple of white spaces. 

## Conclusion

I hope this tutorial has given you the background knowledge you need to use the `<br>` tag so you can make your HTML text look better.

Thank you for reading, and keep coding.








