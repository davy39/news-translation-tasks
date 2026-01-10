---
title: How to Change Text Color in HTML – Font Style Tutorial
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-12T20:45:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-text-color-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--6-.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
seo_title: null
seo_desc: 'Text plays a significant role on our web pages. This is because it helps
  users learn what the web page is all about and what they can do there.

  When you add text to your web pages, this text defaults to a black color. But sometimes
  you will want to c...'
---

Text plays a significant role on our web pages. This is because it helps users learn what the web page is all about and what they can do there.

When you add text to your web pages, this text defaults to a black color. But sometimes you will want to change the text color to be more personalized.

For example, suppose you have a darker color as the background of your website. In that case, you'll want to make the text color a lighter, brighter color to improve your website’s readability and accessibility.

In this article, you will learn how to change the color of your text in HTML. We'll look at various methods, and we'll discuss which method is best.

## How to Change Text Color Before HTML5

Before the introduction of HTML5, you'd use `<font>` to add text to websites. This tag takes the `color` attribute, which accepts the color as a name or hex code value:

```html
<font color="#9900FF"> Welcome to freeCodeCamp. </font>

// Or

<font color="green"> Welcome to freeCodeCamp. </font>
```

This tag got depreciated when HTML5 was introduced. This makes sense because HTML is a markup language, not a styling language. When dealing with any type of styling, it is best to use CSS, which has the primary function of styling.

This means for you to add color to your web pages, you need to make use of CSS.

In case you are in a rush to see how you can change the color of your text, then here it is:

```html
// Using inline CSS
<h1 style="color: value;"> Welcome to freeCodeCamp! </h1>

// Using internal/external CSS
selector {
    color: value;
}
```

Suppose you are not in a rush. Let's briefly dive right in.

## How to Change Text Color in HTML

You can use the CSS color property to change the text color. This property accepts color values like Hex codes, RGB, HSL, or color names.

For example, if you want to change the text color to sky blue, you can make use of the name `skyblue`, the hex code `#87CEEB`, the RGB decimal code `rgb(135,206,235)`, or the HSL value `hsl(197, 71%, 73%)`.

There are three ways you can change the color of your text with CSS. These are using inline, internal, or external styling.

### How to Change Text Color in HTML With Inline CSS

Inline CSS allows you to apply styles directly to your HTML elements. This means you are putting CSS into an HTML tag directly.

You can use the style attribute, which holds all the styles you wish to apply to this tag.

```html
<p style="...">Welcome to freeCodeCamp!</p>
```

You will use the CSS color property alongside your preferred color value:

```html
// Color Name Value
<p style="color: skyblue">Welcome to freeCodeCamp!</p>

// Hex Value
<p style="color: #87CEEB">Welcome to freeCodeCamp!</p>

// RGB Value
<p style="color: rgb(135,206,235)">Welcome to freeCodeCamp!</p>

// HSL Value
<p style="color: hsl(197, 71%, 73%)">Welcome to freeCodeCamp!</p>
```

But inline styling isn't the greatest option if your apps get bigger and more complex. So let's look at what you can do instead.

### How to Change Text Color in HTML With Internal or External CSS

Another preferred way to change the color of your text is to use either internal or external styling. These two are quite similar since both use a selector.

For internal styling, you do it within your HTML file's `<head>` tag. In the `<head>` tag, you will add the `<style>` tag and place all your CSS stylings there as seen below:

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      selector {
        color: value;
      }
    </style>
  </head>

  // ...

</html>
```

While for external styling, all you have to do is add the CSS styling to your CSS file using the general syntax:

```css
selector {
  color: value;
}
```

The selector can either be your HTML tag or maybe a `class` or an `ID`. For example:

```html
// HTML
<p> Welcome to freeCodeCamp! </p>

// CSS
p {
  color: skyblue;
}
```

Or you could use a `class`:

```html
// HTML
<p class="my-paragraph" > Welcome to freeCodeCamp! </p>

// CSS
.my-paragraph {
   color: skyblue;
}
```

Or you could use an `id`:

```html
// HTML
<p id="my-paragraph" > Welcome to freeCodeCamp! </p>

// CSS
#my-paragraph {
   color: skyblue;
}
```

**Note:** As you have seen earlier, with inline CSS, you can use the color name, Hex code, RGB value, and HSL value with internal or external styling.

## Wrapping Up

In this article, you have learned how to change an HTML element's font/text color using CSS. You also learned how developers did it before the introduction of HTML5 with the `<font>` tag and color attributes.

Also, keep in mind that styling your HTML elements with internal or external styling is always preferable to inline styling. This is because it provides more flexibility.

For example, instead of adding similar inline styles to all your `<p>` tag elements, you can use a single CSS `class` for all of them.

Inline styles are not considered best practices because they result in a lot of repetition - you cannot reuse the styles elsewhere. To learn more, you can read [my article on Inline Style in HTML](https://www.freecodecamp.org/news/inline-style-in-html/). You can also learn how to change [text size](https://www.freecodecamp.org/news/how-to-change-text-size-in-html/) in this article and [background color](https://www.freecodecamp.org/news/html-background-color-change-bg-color-tutorial/) in this article.

I hope this tutorial gives you the knowledge to change the color of your HTML text to make it look better.

Have fun coding!

Embark on a journey of learning! [Browse 200+ expert articles on web development](https://joelolawanle.com/contents). Check out [my blog](https://joelolawanle.com/posts) for more captivating content from me.
