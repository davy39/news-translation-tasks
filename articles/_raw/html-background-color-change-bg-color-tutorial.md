---
title: HTML Background Color – Change BG Color Tutorial
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-12T17:30:49.000Z'
originalURL: https://freecodecamp.org/news/html-background-color-change-bg-color-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--7-.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: null
seo_desc: 'When you''re building web pages, you always want to create unique layouts.
  You want your web page to be appealing to your users and not jarring to the eye.

  And to help do that, you can choose background and text colors that blend well and
  complement e...'
---

When you're building web pages, you always want to create unique layouts. You want your web page to be appealing to your users and not jarring to the eye.

And to help do that, you can choose background and text colors that blend well and complement each other.

By default, you will notice that your web page has a transparent background color, which you can change to any color you want.

For example, you might want to create a dark mode feature on your web page so that the background has a dark color while the text has a light color. This help readers avoid harsh colors that can affect their eyes.

In this article, you will learn how to change the background color of your web pages with HTML and CSS.

## How We Used to Change Background Color

In the past, before the introduction of HTML5, some basic styling was handled by HTML.

For example, when you wanted to change the background color of your page, you could've easily added the `bgcolor` attribute in the opening body tag and set it to the value of your preferred color. This could be its hex code or the name.

```html
<body bgcolor="grey">

// Or

<body bgcolor="#808080">
```

However, this attribute was depreciated when HTML5 was introduced. It’s now replaced by a better alternative, the CSS `background-color` property. This makes sense because HTML is a markup language, not a styling language. When dealing with styling, it is best to use CSS.

In case you are in a rush to see how you can change the background color of your web page, divs, and other elements, then here it is:

```html
// Using inline CSS
<body style="background-color: value;"> 
  // ... 
</body>

// Using internal/external CSS
selector {
  background-color: value;
}
```

Let's say you have time to spare. Let's quickly get started.

## How to Change Background Color in HTML

You can use the CSS background-color property to change the color of your web pages. This property works like every other CSS property, meaning you can make use of it to style your page in three ways:

* within your HTML tags (inline styling),
    
* within a style tag in the head tag (internal styling),
    
* or in a dedicated CSS file (external styling).
    

Depending on your preference, you will set the `background-color` property to a color name, a hex code, an RGB value, or even an HSL value. You can use this property to style not only the body of your web page but also divs, headings, tables and lots more.

Check out the following example in CodePen:

%[https://codepen.io/olawanlejoel/pen/BaxKLdd] 

<iframe height="300" style="width:100%" src="https://codepen.io/olawanlejoel/embed/BaxKLdd?default-tab=html%2Cresult">
  See the Pen <a href="https://codepen.io/olawanlejoel/pen/BaxKLdd">
  Background-color</a> by Olawanle Joel (<a href="https://codepen.io/olawanlejoel">@olawanlejoel</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

## How to Change Background Color in HTML With Inline CSS

Inline CSS allows you to apply styles directly to your HTML elements. This means you are putting CSS into an HTML tag directly. You do this with the style attribute, which holds all the styles you wish to apply to your HTML tag.

```html
<body style="...">
  // ...
</body>
```

You will use the CSS background-color property alongside your preferred color value:

```html
// Color Name Value
<body style="background-color: skyblue">
  // Hex Value
  <div style="background-color: #87CEEB">
    // RGB Value
    <h1 style="background-color: rgb(135,206,235)">
      // ...
    </h1>

    // HSL Value
    <span style="background-color: hsl(197, 71%, 73%)">
      // ...
    </span>
  </div>
</body>
```

## How to Change Background Color in HTML With Internal/External CSS

The best way to style web pages is external styling, but you can always use internal styling when you only have a few lines of styles.

Both internal and external make use of the same approach: they both use selectors to add styling to HTML elements.

For internal styling, all styles are added to your HTML file within the `<style>` tag. This style tag is placed within the `<head>` tag as seen below:

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      selector {
        background-color: value;
      }
    </style>
  </head>

  // ...

</html>
```

For external styling, all you have to do is add the CSS styling to your CSS file using the general syntax:

```css
selector {
  background-color: value;
}
```

The selector can either be your HTML tag or maybe a `class` or an `ID`. For example:

```html
// HTML
<div> 
  <h1> Welcome to freeCodeCamp! </h1>
</div>

// CSS
div {
  background-color: skyblue;
}
```

Or you could use a `class`:

```html
// HTML
<div class="container"> 
  <h1> Welcome to freeCodeCamp! </h1>
</div>

// CSS
.container {
  background-color: skyblue;
}
```

Or you could use an `id`:

```html
// HTML
<div id="container"> 
  <h1> Welcome to freeCodeCamp! </h1>
</div>

// CSS
#container {
  background-color: skyblue;
}
```

**Note:** As you have seen earlier, with inline CSS, you can use the color name, Hex code, RGB value, and HSL value with both internal or external styling.

## Wrapping Up

In this article, you have learned how to change the background color of HTML element’s using the CSS background-color property. You also learned how developers did it before the introduction of HTML5 with the `bgcolor` attribute.

It is essential to remember that styling your HTML elements with internal or external is always preferable to inline styling because it provides more flexibility. For example, instead of adding similar inline styles to all your `<div>` tag elements, you can use a single CSS `class` for them.

Inline styles are not considered best practices because they result in a lot of repetition - you cannot reuse the styles elsewhere. To learn more, you can read [my article on Inline Style in HTML](https://www.freecodecamp.org/news/inline-style-in-html/). You can also learn how to [change text size](https://www.freecodecamp.org/news/how-to-change-text-size-in-html/) in this article, and how to change [text color](https://www.freecodecamp.org/news/how-to-change-text-color-in-html/) in this article.

I hope this tutorial gives you the knowledge to change the color of your HTML text to make it look better.

Have fun coding!
