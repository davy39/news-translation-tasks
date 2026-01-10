---
title: HTML Font – CSS Font Family Example (Serif and Sans Serif Characters)
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-26T22:15:30.000Z'
originalURL: https://freecodecamp.org/news/html-font-css-font-family-example-serif-and-sans-serif-characters
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/brett-jordan-M9NVqELEtHU-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: fonts
  slug: fonts
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Choosing the right font is an important first step in making your website
  usable and accessible.

  How text is formatted affects how readable your designs and webpages are.

  You can modify how your HTML text appears in many ways using CSS. You can selec...'
---

Choosing the right font is an important first step in making your website usable and accessible.

How text is formatted affects how readable your designs and webpages are.

You can modify how your HTML text appears in many ways using CSS. You can select the type of font you want to use, whether it's bold or not, how big it is, and you can even change the color and add different spacing or decorations to it.

In this article, we'll go over the differences between the two most popular font types, Serif and Sans Serif.

In addition, we'll cover the syntax and how to use the `font-family` property so that with the help of CSS, you can choose and then use different fonts in your web design projects.

Let's get started!

## Typeface Terminology

First, let's discuss some of the most common and frequently used font types that modern browsers support.


### The Serif font type

Serif fonts are characterised by the little extra fine details on the ends of the letters.

![Screenshot-2021-08-13-at-4.34.15-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-4.34.15-PM.png)

At the end of the main strokes of characters, there are small flourish strokes called *serifs*.


![Screenshot-2021-08-13-at-4.38.02-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-4.38.02-PM.jpeg)

Serif fonts are traditionally used widely in print as they are considered readable for lengthy passages of text. But they don't always display well on screens.

Serif fonts are considered to be among the most classic, elegant, and traditional fonts you can use.

### The Sans-Serif font type

This type of font creates a clean design look, while at the same time being very readable and clear.

![Screenshot-2021-08-13-at-4.35.04-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-4.35.04-PM.png)

This font type  has straight ends on each letter and there are no strokes at the edges, making the characters look sharp and flat and with clean lines.

![Screenshot-2021-08-13-at-4.38.14-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-4.38.14-PM.jpeg)

Sans-serif fonts are considered modern, minimalistic, contemporary and a bit more readable choice for high resolution computer screens.

### The Monospace font type

With this font type, every letter has the same fixed width and letters are equally spaced apart. 

With the previous font types we've discussed so far, each letter has a different width.

So, with the monospace typeface, all letters have the same width. This makes text align nicely and makes it easy to follow, giving designs a clean appearance and mechanical feel.

![Screenshot-2021-08-13-at-5.29.11-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-5.29.11-PM.png)

There are two more generic font types available, `fantasy` and `cursive`, but the most widely used fonts are the ones mentioned above.

## How to choose a font for your website – font names

Now that we've covered the basics of font terms and descriptions, its time to look at the many different font styles within each family.

Some common styles within each font family are listed below:

### Serif Fonts

- Georgia
- Times
- Times New Roman
- Bodoni
- Garamond
- Palatino
- ITC Clearface
- Plantin
- Freight Text
- Didot
- American Typewriter

### Sans-Serif Fonts

- Arial
- Verdana
- Helvetica
- Geneva
- Tahoma
- Trebuchet MS
- Open Sans
- Liberation Sans
- Impact

### Monospace Fonts

- Courier
- MS Courier New
- Monaco
- Lucinda Console
- Andalé Mono
- Menlo
- Consolas

## How to use the `font-family` property

In CSS, the `font-family` property defines a specific font for an element and how its text content will look and be rendered.

The syntax for the `font-family` property is:

```CSS
element {
font-family: value;
}
```

We write the propepty `font-family` followed by a colon `:`, a space, a `value`, and finally end the specification with a semicolon `;`.

We have to set the property we want to target and assign the value we want.


## How to set a CSS font

Say we have the HTML below:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>CSS Fonts</title>
</head>
<body>
    <h1>HTML Font – CSS Font Family </h1>
    <p>I am a paragraph</p>
</body>
</html>
```


Without any style applied and without explicitely setting a value to the `font-family` property, browsers display headings and paragraphs in the font of their own choosing. 

The default, standard font used in Google Chrome is `Times New Roman`, a serif font.

The result looks like this:

![Screenshot-2021-08-13-at-7.03.34-PM](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-13-at-7.03.34-PM.png)

There are a few ways to set a different typeface and specify the font we want.

When choosing a typeface – that is the `value` part – it's worth mentioning that sites use a limited set of typefaces. They'll grab fonts that are already installed on the user's computer.

A browser will display a font only if its already installed on a user's computer.

So let's see the ways in which you can set a font in CSS.

### How to use a generic font-family name

In this case, the names are keywords and include one of the font categories mentioned earlier (serif, sans-serif, monospace).

It would look something like this:

 ```CSS
 p {
  font-family: serif;
  }
```

This sets the font to a generic serif font.

### How to use a specific font-family name

```CSS
p {
 font-family: Times,serif;
 }
```

This rule sets `Times` as the desired font and then `serif` as the generic fallback option, in case the first option is not installed on the user's computer.

If the name contains any white space, you need to enclose it in quotation marks.

```CSS
p {
font-family: "Courier New",monospace;
}
```

This sets the font to `Courier New` and adds `monospace` as a backup.

If we're specifying a font other than one of the generic names (like serif, sans-serif) we need to give the browser a fallback.

### How to use a font-stack 

In this case, the `font-family` property has multiple values.

It is a prioritized, comma-separated list of font family names you can apply to text, indicating that all the fonts are alternatives. This makes for maximum browser and operating system compatability.

The list is prioritized from left to right, from highest to lowest priority.

```css
p { 
  font-family: "Lucida Console", Courier, monospace;
}
```

By applying more than one font-family name, you create an order of preference. We start with the font we want first.

If a user doesn't have the first option installed on their computer or if it isn't supported by the browser, the browser moves on to the second font and  uses that one. If that font is also not available it moves to the third one, and so on.

We can list as many fonts as we wish, but best practice is to list three to four.

If all else fails, there will always be a generic font listed at the end as a last option-fallback mechanism.

From the group listed, the browser has to support *at least* one option and the generic name guarantees that something in the desired font-family will be rendered.


```CSS
p {
 font-family: Georgia, "Times New Roman", Times, serif;
```

The fonts you list are known as a *font stack*. 

The browser will first look for `Georgia`. If it is installed, the browser will display that font. Overwise it will look for `Times New Roman`. If that also isn't available, it will resort to displaying the generic default `serif` family font.

## Conclusion

In this article, we went over the different font families and gave some examples of the different styles within each family.

We also went over the `font-family` property and the three different ways to set a font in CSS.

If you want to learn more about HTML and CSS and the different modern techniques used, freeCodeCamp has a free certification on [Responsive Web Design](https://www.freecodecamp.org/learn/responsive-web-design/).

You'll start from the absolute basics and go up through Flexbox, CSS Grid, and how to make websites resonsive. These are essential skills to have for digital design and front-end web development.

In the end, you'll build 5 projects, including a portfolio site where you can show off the other projects you've built if you want.

Thanks for reading and happy learning.



