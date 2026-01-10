---
title: How to Use the CSS text-wrap Property to Create Balanced Text Layouts on Your
  Websites
subtitle: ''
author: Azubuike Duru
co_authors: []
series: null
date: '2025-04-14T13:57:22.508Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-text-wrap-property
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744638131989/38357168-abda-4f7b-8c4f-568f64b586df.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Responsive Web Design
  slug: responsive-web-design
seo_title: null
seo_desc: An inconsistent text layout can really ruin the look of your website’s design.
  Maybe a heading has an extra word that wraps to another line, or in a paragraph
  some lines are longer than others. This can leave the whole thing looking messy
  and hard to...
---

An inconsistent text layout can really ruin the look of your website’s design. Maybe a heading has an extra word that wraps to another line, or in a paragraph some lines are longer than others. This can leave the whole thing looking messy and hard to read.

Before now, developers used tags like `<br>` or `<span>` to manually adjust word spacing. But what happens in cases where you also need to consider the responsiveness of the website? Well, the new `text-wrap: balance` property in CSS can now automatically calculate and divide the lines in such a way that every word looks organized and even. Like this:

![Heading before and after applying 'text-wrap: balance' for improved wrapping.](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743742346617_Desktop+-+1-3.png align="left")

In this article, you’ll learn how the `text-wrap` property works and how to use it in your code. You’ll also see a few examples along the way.

Without wasting time, let's get right into it.

### Table of Contents

* [Understanding the Problems](#heading-understanding-the-problems)
    
* [Introducing text-wrap](#heading-introducing-text-wrap)
    
    * [What is text-wrap?](#heading-what-is-text-wrap)
        
    * [Basic Syntax of text-wrap](#heading-basic-syntax-of-text-wrap)
        
* [text-wrap vs. max-width : When to Use Each](#heading-text-wrap-vs-max-width-when-to-use-each)
    
    * [When to Use max-width vs text-wrap](#heading-when-to-use-max-width-vs-text-wrap)
        
    * [Browser Support and Considerations](#heading-browser-support-and-considerations)
        
* [Practical Implementation: Step-by-Step Guide](#heading-practical-implementation-step-by-step-guide)
    
* [Conclusion](#heading-conclusion)
    

## Understanding the Problems

Apart from making words harder to read when your text is unevenly displayed, there are other issues uneven or poorly displayed text can cause on your website as a whole. Some of these are:

* **Responsive Design**: We wouldn't have any issues if we could manually design for every screen size and carefully place and space the lines of our text exactly as we wanted users to read them. Unfortunately, we can't do this, which is why making designs responsive is always crucial. When text adjusts from one screen size to another, lines break, and what looks good on a desktop may look terrible on a tablet view.
    
* **Headings and Short Paragraphs**: Since paragraphs and small blocks of text have many words, there is a high probability of words ending in a very unbalanced way. Often, we see a heading line ending with just one word, forming an awkward shape in the overall design.
    
* **Dynamic Content**: If your website contains dynamic content (such as cards of various sizes, product descriptions, or blog posts), having no `text-wrap` might make your layout break or appear unpredictable.
    

## Introducing `text-wrap`

In the last section, we looked at the problems attributed to uneven text distribution. In this section, you’ll see how `text-wrap` is a game changer in how you organize your text.

Before `text-wrap`, developers relied heavily on `max-width`, `text-align`, or `<br>` to control text lines. The new `text-wrap` CSS property was created to help break text naturally across lines without making it look out of place, preventing the need for trial and error in checking if text fits.

### What is `text-wrap`?

`text-wrap` is a CSS property that can help you adjust and space text automatically, break lines evenly without using the rigid `<br>` tag, and not have to rely on `text-align`, which didn't work on all screen sizes.

With `text-wrap`, your headings and paragraphs are sure to look good. Instead of having some lines that look longer than others, `text-wrap` neatly arranges everything to appear visually appealing.

### Basic Syntax of `text-wrap`

There are two major ways to apply text-wrap to your text. These values are:

`text-wrap: balance`**: (The Smart Heading Balancer)**

This is the smart way of telling the browser to adjust the text evenly, regardless of the screen size.

Code snippet:

```css
h1 {
  text-wrap: balance;
}
```

In this code, the heading text lines will split naturally without any weird short lines.

`text-wrap: pretty;` **(The Smart Paragraph Balancer)**

Just as `text-wrap: balance` works best for headings, `text-wrap: pretty` is the best for styling long paragraphs.

Code snippet:

```css
p{
  text-wrap: pretty;
}
```

The `p` in this code will make sure the paragraphs maintain natural readability.

**Other values include:**

| **Value** | **Description** |
| --- | --- |
| `wrap` | Default state |
| `nowrap` | Prevents text from wrapping to the next line |
| `stable` | Ensures things are kept in place until the content changes itself |

## `text-wrap` vs. `max-width` : When to Use Each

`max-width` was always the go-to option for developers in the past. While this method works in most cases, it won’t stop uneven text distribution. Let's compare it with the new `text-wrap` CSS property so you can know when to use each one.

**Using** `max-width`:

```css
h1 {
  max-width: 400px;
}
```

The `max-width` here forces the heading not to exceed a 400px width. This can be good for controlling short body paragraphs but can cause unevenness for headings when dealing with multiple screen sizes.

**Using** `text-wrap`:

```css
h1 {
  text-wrap: balance;
}
```

Here, the browser dynamically breaks the heading text in a balanced way, preventing any weird-looking single lines.

### When to Use `max-width` vs `text-wrap`

Use `text-wrap: balance` when you want a more natural text read without any weird line breaks.

Use `max-width` when you need to control the text width and don't necessarily care how the lines break.

Use both if you want a more natural read within a confined width limit.

```css
h1 {
  max-width: 500px;
  text-wrap: balance;
}
```

This ensures the heading stays within a 500px limit while maintaining an even text distribution.

### Browser Support and Considerations

Currently, Chrome and Edge are the only main browsers that support the new `text-wrap` property. If you are building a project that should work on browsers like Safari and Firefox, you will need to use traditional text formatting methods like `text-align`, `<br>`, or `max-width` instead.

Fallback snippet:

```css
@supports (text-wrap: balance) {
  h1 {
    text-wrap: balance;
  }
}
```

The `@support` is a pro tip to apply this style to only supported browsers.

## Practical Implementation: Step-by-Step Guide

Now that you’ve seen how important `text-wrap` can be and how to use it, let’s put that knowledge into practise and see real examples, compare the before and after screens of using it (and not), and check how it reacts in responsive designs as well.

### 1\. Applying `text-wrap: balance` to Headings

In this section, we will see how the heading lines in the topic **"How to Use CSS Text Balance: A Simple Trick for Smoother, Cleaner Designs"** will break across different sizes and how it looks when `text-wrap: balance` is applied.

**Without** `text-wrap: balance`:

HTML

```html
<h1 class="title">How to Use CSS Text Balance: A Simple Trick for Smoother, Cleaner Designs</h1>
```

CSS

```css
.title {
  font-size: 2.5rem;
  font-weight: bold;
}
```

Without any special application to the headings, it will just adjust freely.

Result:

![Heading without 'text-wrap: balance', showing uneven wrapping.](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743740541468_Screenshot+2025-04-04+at+5.21.36AM+1.png align="left")

**With** `text-wrap: balance`:

CSS

```css
.title {
  font-size: 2.5rem;
  font-weight: bold;
  text-wrap: balance;
}
```

Now, the browser automatically adjusts the line breaks to ensure a more even distribution.

Result:

![Heading with 'text-wrap: balance', showing smart readable behavior and wrapping](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743740708025_Screenshot+2025-04-04+at+5.24.26AM.png align="left")

### 2\. Using `text-wrap: pretty` on Short Paragraphs

You’ve now seen how `text-wrap: balance` handles headings, so lets also take a look at how it breaks the lines evenly in your text paragraphs. As I mentioned above, the value `pretty` is mostly used for paragraphs or short block of words. Here’s how it works and appears on a block of text.

**Without** `text-wrap: pretty`:

HTML

```html
<p class="subText"> Do you know that inconsistent text layout can ruin the look of your website design? Maybe a heading has an extra word that takes up another line or in a paragraph some lines are longer than others whereby leaving the whole thing looking messed up and hard to read.</p>
```

CSS

```css
.subText {
  font-size: 1.2rem;
  line-height: 1.5;
}
```

In this code, text adjustment will behave normally without any smart contraints.

Result:

![Paragraph without 'text-wrap: pretty', showing uneven wrapping.](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743739991569_Screenshot+2025-04-04+at+5.11.08AM.png align="left")

**With** `text-wrap: pretty`:

CSS

```css
.subText {
  font-size: 1.2rem;
  line-height: 1.5;
  text-wrap: pretty;
}
```

The code above makes the line breaks evenly in a way that it will be easier for someone to read through.

Result:

![Paragraph with 'text-wrap: pretty', showing smart readable behavior and wrapping](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743739834917_Screenshot+2025-04-04+at+5.09.49AM.png align="left")

### How `text-wrap` Works in Responsive Design

When you use `text-wrap` on your text, you need not to worry how it is going to appear on various screen sizes. The below video shows you what I mean by that:

![A gif showing how 'text-wrap' smoothly adjusts on a responsive screen ](https://paper-attachments.dropboxusercontent.com/s_4C8BE890CB3AB8AD50C286E15DBA884FF164212E142B1E75C767C0221DB183E7_1743738297774_ScreenRecording2025-04-04at4.37.18AM-ezgif.com-video-to-gif-converter.gif align="left")

### Using Media Queries for Extra Control

Combine `media-queries` and `text-wrap` to have a great special kind of control on how your text appears on various screens.

```css
h1 {
  font-size: 2.5rem;
  text-wrap: balance;
}

/* On smaller screens, reduce font size and apply text-balancing */
@media (max-width: 600px) {
  h1 {
    font-size: 2rem;
    text-wrap: balance;
  }
}
```

This code ensures your heading text adapts and remains clean across multiple device sizes.

## Conclusion

How text displays is something every good developer should pay attention to. It plays a big role in user experience. By using `text-wrap`, you can ensure that your website layouts don't look messy or difficult to read.

One of the best things about using `text-wrap` in your text formatting is that it just works every time. You don’t need to bother with `<br>` tags, tweak `max-width`, or fight with text alignment.

Even though it's not yet supported by all browsers, adding it to your next project will future-proof your design so it’s always intact and good-looking.
