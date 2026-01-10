---
title: HTML New Line – How to Add a Line Break with the BR Tag
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-12T18:00:31.000Z'
originalURL: https://freecodecamp.org/news/html-new-line-how-to-add-a-line-break-with-the-br-tag
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/line-break.png
tags:
- name: Accessibility
  slug: accessibility
- name: HTML
  slug: html
seo_title: null
seo_desc: 'By Dillion Megida

  In this article, I''ll explain what line breaks are and show you how to create them
  in HTML.

  What is a Line Break?

  A line break, as the name implies, is a break in line 😅. A line break in HTML is
  a point where a line ends horizontal...'
---

By Dillion Megida

In this article, I'll explain what line breaks are and show you how to create them in HTML.

## What is a Line Break?

A line break, as the name implies, is a break in line 😅. A line break in HTML is a point where a line ends horizontally, and the next line starts on a new line.

In HTML, when you write a string like this:

```html
<p>
    Hello, I am
    trying to create a
    new line
</p>
```

The whitespaces (the tab space before "Hello", the space between "am" and "trying", "a" and "new") will be ignored. The result on the screen will appear like this:

```txt
Hello, I am trying to create a new line
```

One way to fix this (though it's not very effective) is to create three `<p>` tags like this:

```html
<p>Hello, I am</p>
<p>trying to create a</p>
<p>new line</p>
```

This will result in the following:

```txt
Hello, I am
trying to create a
new line
```

Because `p` tags create `block` elements, they occupy the entire horizontal space and the next element goes to the next line – as you can see from the result above.

This solution is not effective because you have created three paragraphs. In cases where a screen reader is to interpret this, it will read it as three paragraphs instead of a single sentence. This can affect web accessibility.

So how do you add a line break for an inline element?


## How to Add a Line Break in HTML

HTML has tags for numerous purposes, including to create line breaks. You can use the `br` tag in HTML to add line breaks. It can go between inline elements to break the elements into multiple parts.

Here is an example of a paragraph with the `br` tag:

```html
<p>
    Hello, I am
    <br />
    trying to create a
    <br />
    new line
</p>
```

The `br` tag is a **void element** that doesn't have a closing tag. Instead, it is a self-closing tag.

The above code results in this:

```txt
Hello, I am
trying to create a
new line
```

You can use this tag for other forms of inline elements like links. For example, look at this code:

```html
<div>
    <a href="https://google.com">Google</a>
    <a href="https://twitter.com">Twitter</a>
</div>
```

Anchor tags, `a`, are inline elements, so instead of the second link showing on the next line, it shows in the same line like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-50.png)

You can use the `br` tag between the links to break the first link line:

```html
<div>
    <a href="https://google.com">Google</a>
    <br />
    <a href="https://twitter.com">Twitter</a>
</div>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-51.png)

## Conclusion

The `br` tag in HTML starts the next element on a new line, similar to the carriage return `\n` in strings.

Instead of using block elements for putting elements in new lines, you can use the line break tag: `br`. 

In cases like sentences, using the `br` tag serves as a visual line break and doesn't affect accessibility. Screen readers will read the sentence as it is without pause.


