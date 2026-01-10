---
title: HTML Bold Text Tutorial – How to Use the <b> Tag
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-03-18T23:16:44.000Z'
originalURL: https://freecodecamp.org/news/html-bold-text-tutorial-how-to-use-the-b-tag
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6051c3af28094f59be25734b.jpg
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In this article, we are going to learn how to use the <b> tag and how it
  differs from the <strong> tag.

  What is the (bold) tag in HTML?

  The <b> tag is used to to make a portion of the text bold without carrying any special
  importance. Here is an exam...'
---

In this article, we are going to learn how to use the `<b>` tag and how it differs from the `<strong>` tag.

## What is the **(bold) tag in HTML?**

**The** `<b>` tag is used to to make a portion of the text bold without carrying any special importance. Here is an example using the `<b>` tag.

```html
<p>This is an example of <b>bold text.</b></p>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/bold-text.png align="left")

**According to the** [**HTML Living Standard**](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-b-element)**, the** `<b>` tag can be used with the following examples:

> **key words in a document abstract, product names in a review, actionable words in interactive text-driven software, or an article lede.**

### **Here's an example of using for a product name in a review**

```html
<p>The <b>Sennheiser IE 300 Headphones</b> fit well in your ears and have an incredible sound.</p>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/headphones-bold-text-1.png align="left")

**The** `<b>` tag is meant to bring the user's attention to a span of text. It is not supposed to carry any importance or convey a tone of urgency or seriousness.

**This would be an incorrect use of the** `<b>` tag.

```html
<p><b>WARNING!!</b> This area is dangerous.</p>
```

**The appropriate tag for this situation would be the** `<strong>` tag because it conveys a sense of seriousness.

## **Differences between the tag and tag in HTML**

**When I first started learning HTML, I thought that the** `<b>` tag and `<strong>` tag were the same thing. Part of the confusion is that they both have the same default boldface styling in most browsers.

**One key difference is that** `<strong>` tags should be used when the text has strong importance, or a sense of urgency or seriousness. `<b>` tags, on the other hand, should be used to bring attention to a span of text without increased importance.

**This example of the** `<strong>` tag tells the user what list item should be read first and that it holds more importance than the other two list items.

```html
<p>To do list for Monday:</p>
<ul>
    <li><p><strong>Pay rent.</strong></p></li>
    <li><p>Start term paper.</p></li>
    <li><p>Go grocery shopping.</p></li>
</ul>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/to-do-list-.png align="left")

**Another key difference is that** `<b>` tags should not be used in headings and captions whereas `<strong>` tags can.

**Here is an example using the** `<strong>` tag to place importance on the title of the chapter.

```html
<h1>Chapter 5: <strong>The Battle</strong></h1>
```

## **How to Use the Class Attribute with Tags in HTML**

**It is common to add a class attribute in the** `<b>` tag to add more semantic meaning.

**If you have a series of sentences, you can add a class like this** `<b class="lead">` to the first `<p>` tag and that will mark it as the lead sentence.

```html
<article>
    <h2>A young boy reunites with birth mother</h2>
    <p><b class="lead">A six year old boy unexpectedly meets his birth mother at the local grocery store.</b></p>
    <p>A young boy and his grandfather were shopping at the grocery store, when a young woman approached them from behind.</p>
    [...]
</article>
```

## **Should you use the tag for styling text in HTML?**

**In HTML 5, it is not appropriate to use the** `<b>` tag for styling text. The preferred styling method is to use the CSS `font-weight` property.

### **Example using the keyword of bold**

```html
 <p class="demo-para">I am using CSS to make the text bold.</p>
```

```css
.demo-para {
  font-weight: bold;
}
```

### **Example using numeric values**

```css
.demo-para {
  font-weight: 700;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/03/using-font-weight.png align="left")

## **Conclusion**

**While,** `<b>` tags and `<strong>` tags might look similar in the browser, they do have different meanings. It is important to know the difference between the two so you can use them appropriately.

`<b>` tags are used to bring attention to a span of text but hold no special importance. `<strong>` tags on the other hand, should be used if the text conveys a sense of importance, seriousness, or urgency.

**I hope you enjoyed this article and learned about when to use** `<b>` tags.
