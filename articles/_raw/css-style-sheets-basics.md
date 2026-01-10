---
title: How to Work with CSS Style Sheets – the Basics for Beginners
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-06-30T16:22:07.000Z'
originalURL: https://freecodecamp.org/news/css-style-sheets-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pexels-bibek-ghosh-14553706.jpg
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Using HTML tags like , , and so on can help you organize your web page\
  \ content nicely, but only up to a point. \nHTML-only pages can be pleasant and\
  \ easy to read – which is hugely important – but, after a while, they all do tend\
  \ to look the same. \nCas..."
---

Using HTML tags like <head>, <body>, and so on can help you organize your web page content nicely, but only up to a point. 

HTML-only pages can be pleasant and easy to read – which is hugely important – but, after a while, they all do tend to look the same. 

Cascading style sheets, known universally as CSS, aren't really sheets, and it can take some work to figure out what "cascading" means. But the markup standard adds real power to your web development work. Let's look at some of that CSS magic in action.

This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). If you'd like, you can follow the video version here:

%[https://youtu.be/47Ufb8g8WGc]

## How CSS Works

So what CSS actually does is allow you to separate your _content_ from its _presentation_. HTML handles the content – meaning, the text, images, and other media your users will consume. And CSS adds more sophisticated control over the way that content looks and behaves. 

Beyond managing formatting, CSS also lets you modularize resources across complex websites, providing uniform presentation across multiple web pages. That's because a single CSS document can be referenced by as many web pages as you like.

In fact I remember how, many years ago, in a particularly lazy moment, I once referenced some large, well-known website's CSS document from one of my own small sites. (Don't tell anyone, but it might have belonged to freeCodeCamp.) 

Because I couldn't be bothered to figure out how they produced an effect I liked, I just linked to their code. I'm pretty sure that was completely legal, by the way, but I definitely don't recommend you try it. It'll only be a matter of time before they make some changes to their style sheet that breaks your site.

## How to Add CSS to your HTML

There are two ways to incorporate CSS code. First, you can simply save all your markup to a file using the `.css` extension that's accessible to your `.html` files using a `link rel` tag like this:

```
<link rel="stylesheet" href="/main.css"
```

That example uses the `stylesheet` attribute to point to a CSS file called `main.css` that's in the web root directory on its server.

Alternatively, you can add it between `<style>` tags within the `<head>` section of your HTML. That'll look something like this:

```
<!DOCTYPE html>
<html>
<head>
<style type="text/css">
p {
  color: red;
  text-align: center;
}
/* This is formatting for bullet points: */
ul {
  color: blue;
  text-align: left;
}
</style>
</head>

```

Note how the opening tag has a `type` attribute of `text/css`, although I'm not sure how necessary that is any more. Keeping it there certainly can't hurt, though. 

This CSS has two sections: the first will apply to all `p` (paragraph) elements that might exist in your HTML.

## How to Apply Your CSS

When you look at the above code, you'll see that there are two style definitions within the curly braces: the text color should be red, and the text alignment should be centered:

```css
<style type="text/css">
p {
  color: red;
  text-align: center;
}
```

Notice how each definition ends with a semicolon. That's really important and leaving those out will break stuff. Also notice how we can refer to colors by name. We'll see more examples of that later, but be aware that you can also identify colors by their hexadecimal codes. The hexadecimal code for an attractive shade of red could be `#F5733`.

The next line of our code is just a comment:

```
/* This is formatting for bullet points: */
```

In general, of course, you want this kind of note to make your code more readable and understandable. But I added it here specifically to show you how commenting works in CSS, using a forward slash and an asterisk at the start, and an asterisk and forward slash at the end. HTML-style comments won't work here. 

This next style will apply to any unordered list within your HTML, using blue as the text color and aligning text to the left. 

```
/* This is formatting for bullet points: */
ul {
  color: blue;
  text-align: left;
}
</style>

```

There's a lot more you can do here and, of course, you can apply styles to all kinds of HTML elements. But we've got to start somewhere, right?

The actual HTML is further down in the `<body>` section. To show you how our CSS will work, I've written some text within a regular paragraph, and a couple of bullet points between `<ul>` tags.

```
<body>

<h2>Basic CSS</h2>

<p>This text exists within a regular paragraph.</p>

<ul>
   <li>This is a bullet point
   <li>This is another bullet point
</ul>
</body>
</html>

```

Now pop that code into a text file with a `.html` file extension and open it up in a browser. The colors and the alignment should reflect our preferences. It isn't much, but it is ours:

![Image](https://www.freecodecamp.org/news/content/images/2023/06/fCC_product.png)
_The final product_

## Wrapping Up

We've successfully incorporated CSS code within our HTML and precisely applied CSS styles to our content. Now take a couple of minutes to create something similar for yourself. Make sure you play around with all the values so you completely understand how they work.

_This article comes from [my Complete LPI Web Development Essentials Study Guide course](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257)._ _And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/)_

