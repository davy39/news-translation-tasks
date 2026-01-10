---
title: CSS Font Color – How to Style Text in HTML
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-01T17:27:17.000Z'
originalURL: https://freecodecamp.org/news/css-font-color-how-to-style-text-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Cssfontcolor.png
tags:
- name: colors
  slug: colors
- name: CSS
  slug: css
- name: fonts
  slug: fonts
- name: HTML
  slug: html
seo_title: null
seo_desc: 'Setting text color on a website you''re building might be confusing at
  first. But in this article, you''ll learn how to do it.

  How to Set Text Color in HTML

  In CSS, the background-color property is pretty straightforward for setting the
  background colo...'
---

Setting text color on a website you're building might be confusing at first. But in this article, you'll learn how to do it.

## How to Set Text Color in HTML

In CSS, the `background-color` property is pretty straightforward for setting the background color of anything. 

So what if you want to set the foreground color of something on the page? Especially text, which under normal conditions you wouldn't want to set a background color for. 

There's no `foreground-color` property in CSS, so what makes this possible is the `color` property.

In this article, I will walk you through how to set the color of text using the color property. We'll also look at the various ways it takes values.

The color property takes values in 4 different ways: named color, hexadecimal color, RGB color, and HSL color. Let's look at each one now.

## Named Colors

As the name implies, you bring in the color property and apply the value by naming the color you want. This may be red, green, blue, orange, crimson, cyan, or any other named color. There are around 147 named colors recognized by browsers. 

The basic syntax looks like this:

```css 
element {
    color: colorName
}
```

```html
<p>freeCodeCamp</p>
```

```css
 p {
     color: crimson;
}
```

![named-color](https://www.freecodecamp.org/news/content/images/2021/09/named-color.png)

## Hexadecimal Colors (or just Hex Colors)

Hex values are used to represent colors with a total of 6 characters. They start with the pound/number sign (#), then any number from 0 to 9, and finally any letter from A to F.

The first 2 values stand for red, the next two stand for green, and the last 2 represent blue. With hex values, there's no limit to the shades of colors you can use.

```html
<p>freeCodeCamp</p>
```

```css
 p {
    color: #dc143c;
 }
```

## RGB Colors

RGB stands for red, green, and blue. With RGB colosr, you specify the color in terms of how much red, green, and blue you want. All three are expressed with numbers between 0 and 255.

There is a type of RGB called `rgba`. The extra ‘a’ stands for alpha, which lets you specify the opacity of the color. It takes a value from 0.0 to 1.0 – 0.0 means 0% opacity, 0.5 means 50% opacity, and 1.0 means 100% opacity.

The basic syntax is `rgba(amountOfRed, amountOfGreen, amountOfBlue, alpha)`. 

You can limit it to `rgba(amountOfRed, amountOfGreen, amountOfBlue)` if you don't want an alpha value.

Here's the syntax for the regular RGB values:

```html
<p>freeCodeCamp</p>
```

```css
 p {
   color: rgb(220, 20, 60);
 }
```

![rgb-color](https://www.freecodecamp.org/news/content/images/2021/09/rgb-color.png)

And here it is demonstrating the alpha value in action with 50% (0.5) opacity:

```css
p {
    color: rgb(219, 20, 60, 0.5);
}
```

![rgb-fifty-percent-opacity](https://www.freecodecamp.org/news/content/images/2021/09/rgb-fifty-percent-opacity.png)

## HSL Colors

HSL stands for hue, saturation, and lightness. It is another way of specifying color for text (and anything else that takes color) in CSS. 

- Hue represents the color wheel in 360°. So, 0° is red, 120° is green and 240° is blue. 
- Saturation is the amount of gray in the color, expressed as a percentage. 0% is the shade of gray and 100% is the color itself.
- Lightness is the amount of darkness and lightness in the color expressed as a percentage. 0% is black and 100% is white.

Just like the RGB colors, you can also set the opacity of the color. So, there's also hsla.

The full basic syntax is `hsl(colorDegree, saturationPercentage, lightnessPercentage, alpha)`. You can limit it to `hsl(colorDegree, saturationPercentage, lightnessPercentage)` in case you don't want an alpha value.

```html
<p>freeCodeCamp</p>
```

```css
 p {
   color: hsl(348, 83%, 47%);
 }
```

![hsl-color](https://www.freecodecamp.org/news/content/images/2021/09/hsl-color.png)

You can apply a particular opacity to the hsl color like this:

```css
 p {
   color: hsla(348, 83%, 47%, 0.5);
  }
```

![hsl-fifty-percent-opacity-1](https://www.freecodecamp.org/news/content/images/2021/09/hsl-fifty-percent-opacity-1.png)

## Should You Use Named Colors, Hex Colors, RGB Colors, or HSL Colors to Assign Colors?

One of the wonderful things about CSS is that there are multiple ways of doing the same thing. You've seen this by applying colors to text. 

Since you can apply colors in 4 different ways, you must be wondering which is the best to use.

When you use named colors, you're kind of limited in how far you can go in applying different shades of colors. Red, green, blue, yellow, or any other named color has a lot of variations you won't get access to with named colors. You'll only have access to around 147 predefined colors recognized by browsers.

Hexadecimal colors are very dynamic. They are the most commonly used among developers because your limit is your creativity. With hex colors, you can use various shades and even use a color no one has ever used.

RGB colors are as dynamic as hex colors. Apart from being able to specify how much red, green, and blue you want from 0 to 255, you can also set how transparent you want the color to be with the extra alpha value.

HSL is the most dynamic of all. You get to specify the exact color you want in degrees from 0 to 360 within the color wheel, set how saturated and dark you want it to be in percentages, and also set an opacity from 0.0 to 1.0.

So really, it's up to you and your use case – and just how creative or specific you want to get.

## Conclusion

Applying colors to text helps make your website more attractive to visitors. The right color combo can also help your content become more readable too. 

In this article, you have learned how to apply colors to text with the 4 different kinds of values you can use with the color property.

Thank you for reading, and keep coding.




