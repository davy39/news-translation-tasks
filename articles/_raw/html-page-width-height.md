---
title: 'HTML vs Body: How to Set Width and Height for Full Page Size'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-17T17:06:50.000Z'
originalURL: https://freecodecamp.org/news/html-page-width-height
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/william-warby-WahfNoqbYnM-unsplash--1-.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Dave Gray\nCSS is difficult but also forgiving. And this forgiveness\
  \ allows us to haphazardly throw styles into our CSS. \nOur page still loads. There\
  \ is no \"crash\". \nWhen it comes to page width and height, do you know what to\
  \ set on the HTML elemen..."
---

By Dave Gray

CSS is difficult but also forgiving. And this forgiveness allows us to haphazardly throw styles into our CSS. 

Our page still loads. There is no "crash". 

When it comes to page width and height, do you know what to set on the HTML element? How about the body element? 

Do you just slap the styles into both elements and hope for the best?

If you do, you're not alone.

The answers to those questions are not intuitive. 

I'm 100% guilty of applying styles to both elements in the past without considering exactly which property should be applied to which element. 🤦‍♂️

It is not uncommon to see CSS properties applied to both the HTML and body elements like this:

```
html, body {
     min-height: 100%;
}
```

## Does It Matter?

Yes, yes it does.

The above style definition creates a problem:

Setting min-height to 100% on both elements does not allow the body element to fill the page like you might expect. If you check the computed style values in dev tools, the body element has a height of zero. 

Meanwhile, the HTML element has a height equal to the visible part of the page in the browser.

Look at the following screenshot from Chrome Dev Tools:

![Image](https://www.freecodecamp.org/news/content/images/2021/02/empty_body.png)
_The body element has a default 8px margin indicated by the bar on top. The height value is 0._

## Why Does This Happen?

Using a percentage as a size value requires the element to reference a parent to base that percentage on. 

The HTML element references the viewport which has a height value equal to the visible viewport height. However, we only set a min-height on the HTML element... NOT a height property value. 

Therefore, the body element has no parent height value to reference when deciding what 100% is equal to.

## And The Problem May Be Hidden

If you started out with enough content to fill the body of the page, you might not have noticed this issue. 

And to make it more difficult to notice, if you set a background-color on both elements or even on just one of them, the viewport is full of that color. This gives the impression the body element is as tall as the viewport.

It's not. It's still at zero.

The image above is taken from a page with the following CSS: 

``` 
html, body {
    min-height: 100%;
}
body { background-color: dodgerblue; }
```

### Reverse-inheritance?

In a strange twist, the HTML element assumes the background-color of the body element if you don't set a separate background-color on the html element. 

## So What is the Ideal Height Setting for a Full Responsive Page?

For years, the answer was the following:

```
html {
    height: 100%;
}
body {
    min-height: 100%;
}
```

This allows the HTML element to reference the parent viewport and have a height value equal to 100% of the viewport value. 

With the HTML element receiving a height value, the min-height value assigned to the body element gives it an initial height that matches the HTML element. 

This also allows the body to to grow taller if the content outgrows the visible page. 

The only drawback is the HTML element does not grow beyond the height of the visible viewport. However, allowing the body element to outgrow the HTML element has been considered acceptable.

## **The Modern Solution is Simplified**

```
body { min-height: 100vh; }
```

This example uses `vh` (viewport height) units to allow the body to set a minimum height value based upon the full height of the viewport. 

Like the previously discussed background-color, if we do not set a height value for the HTML element, it will assume the same value for height that is given to the body element. 

Therefore, this solution avoids the HTML element overflow present in the previous solution and both elements grow with your content! 

The use of `vh` units did cause some mobile browser issues in the past, but [it appears that Chrome and Safari are consistent with viewport units now](https://developers.google.com/web/updates/2016/12/url-bar-resizing).

## Page Height May Cause a Horizontal Scrollbar

Wait, what? 

Shouldn't this say "Page Width"? 

Nope. 

In another strange series of events, your page height may activate the horizontal scrollbar in your browser. 

When your page content grows taller than the viewport height, the vertical scrollbar on the right is activated. This can cause your page to instantly have a horizontal scrollbar as well.

## So What is the Fix?

You may sleep better knowing it starts with a page width setting.

This problem arises when any element - not just the HTML or body element - is set to 100vw (viewport width) units. 

The viewport units do not account for the approximate 10 pixels that the vertical scrollbar takes up. 

Therefore, when the vertical scrollbar activates you also get a horizontal scrollbar.

## How to Set the Page for Full Width

Maybe just don't. 

Not setting a width on the HTML and body elements will default to the full size of the screen. If you do set a width value other than auto, consider utilizing a CSS reset first.

Remember, by default the body element has 8px of margin on all sides. 

A CSS reset removes this. Otherwise, setting the width to 100% before removing the margins will cause the body element to overflow. Here's the CSS reset I use:

```
* { 
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

## How to Set Width to Your Preference

While it may not always be necessary to set a width, I usually do. 

It may simply be a habit.

If you set the width to 100% on the body element you will have a full page width. This is essentially equivalent to not setting a width value and allowing the default.

If you want to use the body element as a smaller container and let the HTML element fill the page, you could set a max-width value on the body. 

Here's an example: 

```
html { background-color: #000; } 
body {
    min-height: 100vh;
    max-width: 400px;
    background-color: papayawhip; 
    margin: 0 auto;
}

## Conclusion

With no height value provided for the HTML element, setting the height and/or min-height of the body element to 100% results in no height (before you add content).

However, with no width value provided for the HTML element, setting the width of the body element to 100% results in full page width.

This can be counterintuitive and confusing. 

For a responsive full page height, set the body element min-height to 100vh.

If you set a page width, choose 100% over 100vw to avoid surprise horizontal scrollbars.

I'll leave you with a tutorial from my YouTube channel demonstrating the CSS height and width settings for an HTML page that is full screen size and grows with the content it contains:

%[https://youtu.be/dpuKVjX6BJ8]

Do you have a different way of setting the CSS width and height that you prefer?

Let me know your method!

