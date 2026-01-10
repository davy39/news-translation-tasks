---
title: Inline CSS Guide – How to Style an HTML Tag Directly
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-09T19:43:17.000Z'
originalURL: https://freecodecamp.org/news/inline-css-guide-how-to-style-an-html-tag-directly
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c38740569d1a4ca30c1.jpg
tags:
- name: CSS
  slug: css
- name: frontend
  slug: frontend
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Style Guide
  slug: style-guide
seo_title: null
seo_desc: 'By Amy Haddad

  You’ve written some HTML and now need to style it with CSS. One way is to use inline
  styles, which is what this article is about.

  <p style="color: red; font-size: 20px;">This is my first paragraph.</p>


  Before we jump into the nuances o...'
---

By Amy Haddad

You’ve written some HTML and now need to style it with CSS. One way is to use inline styles, which is what this article is about.

```html
<p style="color: red; font-size: 20px;">This is my first paragraph.</p>
```

Before we jump into the nuances of inline styles—when, why, and how to use them—it’s important to be aware of the other ways to style your HTML. That way, you choose the best option for your code.

Here’s a summary of your options.

### External Stylesheet

Developers typically keep all of their CSS in an external stylesheet. In your HTML file, use the **`<link>`** element to link to your external stylesheet, which contains your CSS.

```html
<head>
    <link rel="stylesheet" href="./index.css">
</head>
```

Inside the file, index.css, we have our CSS rules.

```css
p {
    color: red;
    font-size: 20px;
}
```

### Internal stylesheet

Another option for styling CSS is using an internal stylesheet. This means defining your CSS rules inside the **`<style>`** element in your HTML file.

```html
<head>  
   <style>
       p {
           color: red;
           font-size: 20px;
       }
   </style>
 </head>
```

### Inline Styles

Less frequently, you’ll find yourself reaching for inline styles. But they’re still important to know about because there are certain occasions when they come in handy.

With inline styles, you’ll add the style attribute to an HTML tag followed by your CSS to style an element.

```html
<p style="color: red; font-size: 20px;">This is my first paragraph.</p>
<p>This is my second paragraph.</p>
```

So in our case, the text of the first paragraph is red with a font-size of 20px. The second one, however, remains unchanged.

Let’s take a closer look at how and when to use inline styles. We'll also uncover why only one of our paragraphs is styled.

# What’s an HTML Tag?

With inline styles, you apply CSS to the `style` attribute in the opening HTML tag.

Examples of HTML tags include:

* <body>...</body>
* <h1>...</h1>
* <p>...</p>

Opening and closing tags are often part of the HTML [element](https://developer.mozilla.org/en-US/docs/Glossary/element), which can contain text, data, an image, or nothing at all. 

Here, we have an element of text.

```html
<p>This is my first paragraph.</p>
```

We can use inline styles to style this element by adding the style attribute to the opening tag, followed by CSS property-value pairs.  


```html
<body>
   <p style="color: red; font-size: 20px;">This is my first paragraph.</p>
   <p>This is my second paragraph.</p>
</body>
```

Let’s walk through how we used inline styles.

# How to Use Inline Styles

Add the style attribute to the tag you want to style, followed by an equals sign. Start and end your CSS with double quotation marks.

```html
<p style="....">
```

Add property-value pairs to the style attribute. Add a semicolon after each property-value pair.

```css
color: red; font-size: 20px;
```

So when we put everything together, it looks like this:

```html
<p style="color: red; font-size: 20px;">This is my first paragraph.</p>
```

## Key Points to Know

Unlike internal and external stylesheets, inline styles don’t contain curly braces or line breaks. That is, write your CSS all on the same line when using inline styles.

Also, keep in mind that inline styles _only_ affect the specific element that you add the style attribute with CSS property-value pairs to. 

For example, in the code below _only_ the first paragraph is styled red with a font-size of 20px.

```html
<body>
   <p style="color: red; font-size: 20px;">This is my first paragraph.</p>
   <p>This is my second paragraph.</p>
</body>
```

If we want to style the text of _both_ paragraphs with inline styles, then we need to add CSS to the style attribute to the second `<p>` as well.

```html
<body>
  <p style="color: red; font-size: 20px;">This is my first paragraph.</p>
  <p style="color: red; font-size: 20px;">This is my second paragraph.</p>
</body>
```

However, if we used an external stylesheet, for example, we could easily style _both_ paragraphs without duplicating our code by using a single CSS selector.

```css
p {
    color: red;
    font-size: 20px;
}
```

This brings us to an important topic: when to use and when not to use inline styles.

# When to Use (and when NOT to use) Inline Styles

Say you have an HTML file with ten or more paragraph tags. Can you imagine styling each one individually with inline styles?

Doing so will quickly clutter your code, making it hard to read and maintain. 

Besides, inline styles can introduce specificity issues if you’re also using internal or external stylesheets. 

That’s because inline styles have a [high specificity](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#Understanding_the_cascade). This means they'll override most other rules in internal and external stylesheets, except for the `!important` declaration.

For example, we added inline styles to two paragraph elements. We’ve also added an internal stylesheet.

```html
<html>
  <head>
      <title>My New Webpage</title>
      <style>
       p {
           color: pink;
       }
   </style>
  </head>
 
<body>
   <p style="color: blue;">A blue paragraph.</p>
   <p style="color: blue;">Another blue paragraph.</p>
</body>
</html>
```

The CSS from our inline styles override the CSS in the internal stylesheet. So we end up with two blue paragraphs.

External stylesheets are also much easier to maintain when you or someone else needs to make a change. This is because a style from an external or internal stylesheet can apply to multiple elements, while an inline one must be applied to each element individually. 

For example, say you need to update a style to ten elements. It’s easier to make the change once in an external stylesheet, instead of ten different times in your HTML file.

In general, it’s often best practice to put your CSS into a separate file. That way, your HTML file contains the structure and content of your website, and your CSS file contains your styles. Doing so makes your code easier to read and manage.

However, there are times when it may make sense to use inline styles:

* Add a style and see the change quickly, which can be useful for [testing](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style).
* Use the style attribute in JavaScript to apply styling.

Most of the time you’ll want to use external stylesheets. But you’ll occasionally find yourself using inline styles, most commonly in the above situations. 

_I write about learning to program, and the best ways to go about it on my blog at [amymhaddad.com](https://amymhaddad.com/)._

