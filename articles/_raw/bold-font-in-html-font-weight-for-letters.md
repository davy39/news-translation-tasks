---
title: Bold Font in HTML – Font Weight for Letters
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-31T20:35:21.000Z'
originalURL: https://freecodecamp.org/news/bold-font-in-html-font-weight-for-letters
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/boldfont.png
tags:
- name: fonts
  slug: fonts
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "When you're building a website, you may want to place particular emphasis\
  \ on certain text to let users know that it's important. \nAnd you can do this in\
  \ HTML with various text formatting tags. \nIn this article, I will take you through\
  \ how to emphasiz..."
---

When you're building a website, you may want to place particular emphasis on certain text to let users know that it's important. 

And you can do this in HTML with various text formatting tags. 

In this article, I will take you through how to emphasize certain text by making it bold.

In HTML, there are three major ways that you can use to make text bold. You can use the `<b>` tag, the `<strong>` tag, or you can do it in CSS with the `font-weight` property. Let's look at each method in more detail.

## How to Make Text Bold With the `<b>` Tag in HTML

HTML gives us the `<b>` tag for making text bold. To make text bold with this tag, you need to wrap it around the text like this:

```html
<p><b>This text is bold</b>, but this text is not.</p>
```
![bold-with-b-tag](https://www.freecodecamp.org/news/content/images/2021/08/bold-with-b-tag.png)

As you can see in the image, the tag makes part of the text stand out.

## How to Make Text Bold With the `<strong>` Tag in HTML

With the `<strong>` tag, you are not just making the text bold – you are calling special attention to it. 

`<strong>` also makes text bold just like the `<b>` tag, but there is a slight difference between the two. I'll discuss this later in the article.

Just like the `<b>` tag, you need to wrap the `<strong>` tag around the text to make the text bold with it. 

```html
<p>
   Before paying to learn programming, check out
   <strong>freeCodeCamp</strong>.
</p>
```

![bold-with-strong-tag](https://www.freecodecamp.org/news/content/images/2021/08/bold-with-strong-tag.png)

With the `<strong>` tag, the `freeCodeCamp` text isn’t just bold, it has a semantic meaning and emphasis.


## How to Make Text Bold with the CSS `font-weight` Property

The font-weight property takes `lighter`, `bold`, and `bolder` as values. It also takes numbers from 100 to 900. So, with it, you don't just make text bold, you can also make it lighter than its surrounding text.

To make some text bold with the font-weight weight property, you need to select the text with its class, id (if any), or element and then apply the values you want. Here's how it works:

```html
<p>This is a <span class="lighter">lighter text</span>.</p>

<p>This is a <span class="bold">bold text</span>.</p>

<p>This is a <span class="bolder">bolder text</span>.</p>
```

```css
 .lighter {
    font-weight: lighter;
}

.bold {
    font-weight: bold;
}

.bolder {
    font-weight: bolder;
}
```

![bold-with-fontweight](https://www.freecodecamp.org/news/content/images/2021/08/bold-with-fontweight.png)

## Should You Use `<b>`, `<strong>` or `font-weight` to Make Text Bold?

You might be wondering which to use for making text bold – `<b>`, `<strong>`, or the CSS `font-weight` property. 

You should generally avoid using `<b>` because it's already a style. When you make text bold with the `<b>` tag, you're explicitly telling the browser to make the text bold right from the HTML. 

`<strong>` also makes the text appear bold, but it is semantic. With it, you're not styling from the HTML (which HTML was never meant for originally), but rather you're telling the browser to make the text appear stronger in appearance than other surrounding text.

The CSS `font-weight` property gives you more control over how light or bold the text should be. The values `lighter`, `bold`, and `bolder` are a start, but you can take things a step further by applying numbers/weights like `100` `200`, `300`, `400`, `500`, `600`, `700`, `800`, and `900` as values, which gives different variations of lightness and boldness.

## Conclusion

Bold font helps you place emphasis on certain words in HTML. In this article, you've learned about the 3 different ways you can make text bold, as well as which of them is best to use.

Thank you for reading, and keep coding.


