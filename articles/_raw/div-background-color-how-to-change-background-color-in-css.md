---
title: Div Background Color – How to Change Background Color in CSS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-03T16:50:46.000Z'
originalURL: https://freecodecamp.org/news/div-background-color-how-to-change-background-color-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/backgroundcolor.png
tags:
- name: colors
  slug: colors
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: null
seo_desc: "If you're working on a web development project, setting a nice background\
  \ color can give the website a more enticing look. \nTo set a background color for\
  \ a div or related element in CSS, you use the background-color property.\nWhile\
  \ setting this backg..."
---

If you're working on a web development project, setting a nice background color can give the website a more enticing look. 

To set a background color for a `div` or related element in CSS, you use the `background-color` property.

While setting this background color, your creativity is your limit as to how far you want to go. 

So in this article, I'm going to show you how you can set this background color.

## How to Set Background Color with Named Colors

With named colors, you can set the background color by bringing in the `background-color` property and assigning it a value expressed in a color name like `red`, `green`, `blue`, and so on.

```css
 div {
      background: green;
    }
```
![ss-1-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-1-1.png)

You can use the following styles to make the web page look better. Just set a width and height for the `div`, so the background-color can take effect:

```css
body {
   display: flex;
   align-items: center;
   justify-content: center;
   height: 100vh;
   background-color: #d3d3d3;
 }

div {
   background: green;
 }
```

Modern browsers recognize around 147 colors, so you're still limited a little. 

## How to Set Background Color with Hexadecimal Colors

With Hexadecimal values, you can set a background color for a `div` or any other element with a total of 6 characters. 

Hex colors start with the hash sign (#), any number from 0 to 9, and finally any letter from A to F.

The first 2 values stand for red, the next two stand for green, and the last 2 represent blue. 

With hex values, you can dive deep into the color wheel and even use colors no one has ever used.

```css
div {
   background: #2ecc71;
 }
```
![ss-2-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-2-1.png)

You can [read more about hex colors here](https://www.freecodecamp.org/news/how-hex-code-colors-work-how-to-choose-colors-without-a-color-picker/).

## How to Set Background Color with RGB Colors

RGB stands for Red Green, and Blue. 

To set the background color with RGB, you specify the amount of red, green, and blue you want with numbers between 0 and 255.
```css
div {
      background: rgb(220, 20, 60);
    }
```
![ss-3](https://www.freecodecamp.org/news/content/images/2022/02/ss-3.png)

RGB also has a variation called RGBA. The last A means alpha and it lets you determine how opaque you want the color to be.

The alpha takes a value from 0.0 to 1.0. 0.0 means 0% opacity, 0.5 means 50% opacity, and 1.0 means 100% opacity.

```css
div {
    background: rgb(220, 20, 60, 0.6);
 }
 ```
![ss-4](https://www.freecodecamp.org/news/content/images/2022/02/ss-4.png)

You can [read more about RGB colors here](https://www.freecodecamp.org/news/rgb-color-html-and-css-guide/).

## How to Set Background Color with HSL Colors

HSL stands for Hue, Saturation, and Lightness. It is the most dynamic within the ways you can specify a background color for a `div` or other elements.  

- **Hue** represents the color wheel in 360°. 0° is red, 120° is green and 240° is blue
- **Saturation** is the amount of gray in the color expressed in percentages. 0% is the shade of gray and 100% is the color itself.
- As the name implies, **lightness** is the amount of darkness and lightness in the color expressed as a percentage. 0% is black and 100% is white.
```css
div {
   background: hsl(16, 100%, 50%);
 }
```
![ss-5](https://www.freecodecamp.org/news/content/images/2022/02/ss-5.png)

## Conclusion
Since you can apply colors in 4 different ways, you must be wondering which one you should use. 

When you use named colors, you're kind of limited in how far you can go in applying different shades of colors. 

Each color like red, green, blue, yellow, or any other color has a lot of variations you won't get access to with named colors. 

You can only access about 147 predefined colors recognized by browsers.
Hexadecimal colors, on the other hand, are very dynamic. They are mostly used among developers, and creativity is the limit. These hex colors allow you to use different shades of the same color.

RGB colors are as dynamic as hexadecimal colors. You can specify the amount of red, green, and blue from 0 to 255, and you can also use the added alpha value to specify the transparency of the color.

HSL is the most dynamic of all of them. You can specify exactly the color from 0 to 360 degrees in the color wheel, set the saturation and darkness as a percentage, and set the opacity to any value between 0.0 and 1.0.  

So deciding which to use between named, hex, RGB and HSL colors depends on you and how creative you want to be and what your project's needs are.

Thank you for reading.


