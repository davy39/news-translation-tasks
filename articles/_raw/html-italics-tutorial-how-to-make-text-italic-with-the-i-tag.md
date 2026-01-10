---
title: HTML Italics Tutorial – How to Make Text Italic with the <i> tag
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-03-22T23:21:42.000Z'
originalURL: https://freecodecamp.org/news/html-italics-tutorial-how-to-make-text-italic-with-the-i-tag
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6053020b28094f59be257c71.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: style
  slug: style
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "In this article, we are going to learn about how to use the <i> tag and\
  \ how it differs from the <em> tag. \nIn previous versions of HTML, the <i> tag\
  \ was used to display text in italics. But in HTML 5, the definition has changed.\
  \ We are going to explo..."
---

In this article, we are going to learn about how to use the `<i>` tag and how it differs from the `<em>` tag. 

In previous versions of HTML, the `<i>` tag was used to display text in italics. But in HTML 5, the definition has changed. We are going to explore that new definition and learn about other ways to style text in italics using CSS.  

## What is the <i> tag? 

The `<i>` tag, or Idiomatic Text element, is a span of text that represents a change in mood or quality of text. This text is displayed in italics. 

Let's look at a few reasons why you might want to use the `<i>` tag.  

### Using the <i> tag to mark phrases in a different language

You can use the `<i>` tag to mark a span of text in a different language. This example italicizes a latin phrase.  

```html
<p>Stacy just got a tattoo of the phrase <i>Audentes fortuna iuvat</i> which means "Fortune favors the bold".</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/latin-phrase-tattoo.png)

You can also use the `lang` attribute in the `<i>` tag to represent phrases that are in a different language than their surrounding text. 

```html
<p>The first phrase that Matt learned in Italian is <i lang="it">Vorrei una birra</i>, which translates to "I'd like a beer".</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/lang-atrribute.png)

### Using the <i> tag to show someone's thoughts

You can also use the `<i>` tag to highlight a person's inner thoughts. 

```html
<p>After Ben met his girlfriend's parents he thought to himself, <i>I really hope they liked me</i>.</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/ben-story.png)

### Using the <i> tag for the name of a ship

If you wanted to use the name of a ship, then you can wrap that name in `<i>` tags. 

```html
<p>The <i>USS Arizona</i> was a United States Navy battleship built in the 1910's.</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/uss-arizona.png)

### Using the <i> tag for taxonomic descriptions

According to the [Convention of Biological Diversity](https://www.cbd.int/gti/taxonomy.shtml), 

> Taxonomy is the science of naming, describing and classifying organisms and includes all plants, animals and microorganisms of the world. 

This would be an example of using the the `<i>` tag for the term _Felis catus_. 

```html
<p>Another term for the domestic cat would be <i>Felis catus</i>.</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/cat-term.png)

## **Differences between the <i> tag and <em> tag in HTML**

You might think that the `<i>` and `<em>` tags have the same meaning because they look the same in the browser. But the two tags hold different meanings from each other. 

The `<em>` tag, or emphasis element, should be used when you want to place an emphasis on a word or span of text. 

Here is an example using the `<em>` tag.

```html
 <p>Quit being a baby and just <em>do</em> it already!</p>

```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/em-example.png)

Humans and screen readers would place verbal stress on the word "do". This differs from the `<i>` tag where there was no extra emphasis placed on the text. 

## Should you use the <i> tag for styling? 

You should not use the `<i>` tag for styling purposes. If you want to style text in italics, then you should use the CSS `font-style` property. 

```html
<p class="demo-para">I am using CSS to style this text in italics.</p>

```

```css
.demo-para {
  font-style: italic;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/css-italics.png)

## Should you use the <i> or <span> tag for icons?

Over the years, there has been debate about whether it is "correct" to use `<i>` tags or `<span>` tags for adding icons to your website. 

Some will argue that there is nothing wrong with it and it is pretty common practice, while others think it is a misuse of the `<i>` tag and you should use the `<span>` tag instead. 

Here is a response from [Font Awesome](https://fontawesome.com/how-to-use/on-the-web/referencing-icons/basic-use) regarding the use of the `<i>` for its icons:

> We like the `<i>` tag for brevity and because most folks use `<em></em>` for emphasized/italicized semantic text these days. If that’s not your cup of tea, using a `<span>` is more semantically correct.

My goal is not to make you choose one side over the other in this debate, but rather make you aware of this ongoing discussion. 

## Conclusion

The `<i>` tag is a span of text that represents a change in mood or quality of text. If you want to place emphasis on text, then the appropriate tag would be the `<em>` tag.

The `<i>` tag should not be used for styling purposes. The correct way to style text in italics is to use the CSS `font-style` property.

I hope you enjoyed this article and learned about when to use `<i>` tag.

  






 




