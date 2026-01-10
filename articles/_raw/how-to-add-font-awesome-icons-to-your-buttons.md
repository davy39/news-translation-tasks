---
title: How to Add Font Awesome Icons to Your Buttons
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T19:56:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-font-awesome-icons-to-your-buttons
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e2b740569d1a4ca3bbb.jpg
tags:
- name: Design
  slug: design
- name: fonts
  slug: fonts
seo_title: null
seo_desc: 'Font Awesome is a convenient library of icons. These icons can be vector
  graphics stored in the .svg file format or web fonts.

  These icons are treated just like fonts. You can specify their size using pixels,
  and they will assume the font size of the...'
---

Font Awesome is a convenient library of icons. These icons can be vector graphics stored in the `.svg` file format or web fonts.

These icons are treated just like fonts. You can specify their size using pixels, and they will assume the font size of their parent HTML elements.

## Basic use

To include Font Awesome in your app or page, just add the following code to the `<head>` element at the top of your HTML:

```html
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">
```

The `i` element was originally used to make other elements italic, but is now commonly used for icons. You can add the Font Awesome classes to the `i` element to turn it into an icon, for example:

```html
<i class="fas fa-info-circle"></i>
```

Note that the `span` element is also acceptable for use with icons.

Here's how you add an icon:

```html
<i class="fas fa-thumbs-up"></i>
```

This will produce a simple thumbs up icon:

![Image](https://www.freecodecamp.org/news/content/images/2020/02/thumbs-up.jpg)

And here's how you would insert that icon onto a button:

```html
<button>
  <i class="fas fa-thumbs-up"></i> Like
</button>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/thumbs-up-btn.jpg)

Notice that there are two parts to using an icon, the _style prefix_ and the _icon name_. In the example above, the style prefix and icon name are `fas` and `fa-thumbs-up`, respectively.

Font Awesome offers the following style prefixes:

| Style  | Style Prefix | Plan Type |
| --- | --- | --- |
| Solid | `fas` | Free |
| Regular | `far` | Pro |
| Light | `fal` | Pro |
| Duotone | `fad` | Pro |
| Brands | `fab` | Free |

Brand icons are often submitted by the company itself, and are useful for building things like buttons for social authentication or payment. These icons include Twitter, Facebook, Spotify, Apple, and even freeCodeCamp:

```html
<i class="fab fa-free-code-camp"></i>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/fcc-fa-icon.jpg)

While you'll only have access to solid and brand icons under the free plan, there are still many ways to style them.

## Styling Font Awesome icons

For simple applications, you could use inline styles:

```html
<span style="font-size: 3em; color: Tomato;">
  <i class="fas fa-thumbs-up"></i>
</span>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/styled-thumbs-up.jpg)

For sizing, you could also use Font Awesome's built in keywords:

```html
<i class="fas fa-thumbs-up fa-xs"></i>
<i class="fas fa-thumbs-up fa-sm"></i>
<i class="fas fa-thumbs-up fa-lg"></i>
<i class="fas fa-thumbs-up fa-2x"></i>
<i class="fas fa-thumbs-up fa-3x"></i>
<i class="fas fa-thumbs-up fa-5x"></i>
<i class="fas fa-thumbs-up fa-7x"></i>
<i class="fas fa-thumbs-up fa-10x"></i>
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/sizing-keywords.jpg)

An important thing to remember is that FA icons inherit the `font-size` of the parent container. This means that the icons scale with any text that might be used with them, which keeps the design consistent.

For example, say you want to create several buttons. The default size for the buttons is quite small, so you write some CSS to increase the size of the buttons, along with the text and icons within them:

```html
<button>
  <i class="fas fa-thumbs-up"></i> Like
</button>

<button>
  <i class="fas fa-thumbs-down"></i> Dislike
</button>

<button>
  <i class="fas fa-share"></i> Share
</button>
```

```css
button {
  font-size: 1.5em;
  margin: 5px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/buttons-ex.jpg)

You can also adjust an icon's size directly by targeting the icon itself and adjusting its `font-size`.

Font Awesome is, well, awesome! As the most popular icon toolkits, it's easy to include and use in all of your projects. Now go on icon up all the things.

### More Information

* [Font Awesome docs](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use)
* [All available Font Awesome icons](https://fontawesome.com/icons)

