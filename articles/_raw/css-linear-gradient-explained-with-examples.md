---
title: CSS Linear Gradient Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-linear-gradient-explained-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cfc740569d1a4ca3543.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'In a linear gradient, the colors flow in a single direction, for example
  from left to right, top to bottom, or any angle you choose.


  A linear gradient with two color stops

  Syntax

  To create a linear gradient you must define at least two color stops. ...'
---

In a linear gradient, the colors flow in a single direction, for example from left to right, top to bottom, or any angle you choose.

![A gradient with Two colour stops](https://cdn.discordapp.com/attachments/261391445074771978/371707961422118912/image.png)
_A linear gradient with two color stops_

## Syntax

To create a linear gradient you must define at least two color stops. They are the colors the transitions are created among. It is declared on either the **background** or **background-image** properties.

```text
background: linear-gradient(direction, colour-stop1, colour-stop2, ...);
```

If no direction is specified, the default transition is top to bottom.

## Examples

### Top to bottom:

```text
background: linear-gradient(red, yellow);
```

![Top to Bottom](https://cdn.discordapp.com/attachments/261391445074771978/371702268803809301/image.png)

**Left To** r**ight:**

To make it left to right, you add an additional parameter at the beginning of the `linear-gradient()` starting with the word **to** which indicates the direction:

```text
background: linear-gradient(to right, red , yellow);
```

![Left to Right](https://cdn.discordapp.com/attachments/261391445074771978/371702990161051648/image.png)

**Diagonal** gradients**:**

You can also transition a gradient diagonally by specifying the horizontal and vertical starting positions, for example, top-left, or bottom-right.

Here’s a sample for a gradient starting from the top-left:

```text
 background: linear-gradient(to bottom right, red, yellow);
```

![Top-left](https://cdn.discordapp.com/attachments/261391445074771978/371705382105776128/image.png)

### **Using angles to specify the direction of the gradient**

You can also use angles, to be more accurate in specifying the direction of the gradient:

```text
background: linear-gradient(angle, colour-stop1, colour-stop2);
```

The angle is specified as an angle between a horizontal line and the gradient line.

```text
background: linear-gradient(90deg, red, yellow);
```

![90 degrees](https://cdn.discordapp.com/attachments/261391445074771978/371710718698848256/image.png)

### **Using more than two colors**

You’re not limited to just two colors – you can use as many comma separated colors as you want.

```text
background: linear-gradient(red, yellow, green); 
```

![A gradient with 3 colour stops](https://cdn.discordapp.com/attachments/261391445074771978/371706534591201281/image.png)

You can also use other color syntaxes like RGB or hex codes to specify the colors.

### **Hard color stops**

You can not only use gradients to transition with fading colors, but you can also use it to change from one solid color to another solid color instantly:

```text
background: linear-gradient(to right,red 15%, yellow 15%);
```

![Hard colour stops](https://cdn.discordapp.com/attachments/261391445074771978/371716730046775318/image.png)

## More information:

* [The CSS Handbook: a handy guide to CSS for developers](https://www.freecodecamp.org/news/the-css-handbook-a-handy-guide-to-css-for-developers-b56695917d11/)

