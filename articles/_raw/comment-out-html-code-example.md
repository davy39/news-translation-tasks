---
title: Comment out HTML – Code Example
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-28T23:26:26.000Z'
originalURL: https://freecodecamp.org/news/comment-out-html-code-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/arrow-g4f0266a9e_1280.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Adding comments in your code is a good practice, as it makes your code
  more readable and understandable.

  Comments don’t run because they are ignored by compilers and interpreters.

  In this article, I will show you how you can comment out your HTML cod...'
---

Adding comments in your code is a good practice, as it makes your code more readable and understandable.

Comments don’t run because they are ignored by compilers and interpreters.

In this article, I will show you how you can comment out your HTML code, so you can help yourself and team members understand what you're doing with it.

## How to Comment Out HTML Code

Unlike other programming languages which have different symbols for making multi-line and single line comments, you make both multi-line and single line comments with the same symbols in HTML.

To comment out HTML code, use the less than symbol (`<`) followed by an exclamation mark (`!`), 2 hyphens (`--`), the comment, 2 hyphens again (`--`), and greater than symbol (`>`).

The syntax for commenting out HTML looks like this:

```html
<!-- comments here -->
```

You can use this for single line comments:
```html
    <!-- This is a single line comment -->
    <section class="about" id="about">
      <h3>Watch the Jabs</h3>
      <p>
        Our primary objective is to bring live boxing matches to fans all around
        the world
      </p>

      <h3>Its not About the Fights Alone!</h3>
      <p>
        We also air documentaries specially made for the greats, lifestyle of
        boxers, news, and more.
      </p>
    </section>
```

You can also use it for multi-line comments: 

```html
    <section class="about" id="about">
      <h3>Watch the Jabs</h3>
      <p>
        Our primary objective is to bring live boxing matches to fans all around
        the world
      </p>
      <!-- This is a 
        multi-line 
        comment -->
      <h3>Its not About the Fights Alone!</h3>
      <p>
        We also air documentaries specially made for the greats, lifestyle of
        boxers, news, and more.
      </p>
    </section>
```

You can also insert the comment anywhere you want as long as it is not within a tag: 

```html
    <section class="about" id="about">
      <h3>Watch the Jabs</h3>
      <p>
        Our primary objective is to bring live boxing matches to fans all around
        the world
      </p>
      <h3>Its not About the Fights Alone!</h3>
      <p>
        We also air
        <!-- This is a comment within some text -->
        documentaries specially made for the greats, lifestyle of boxers, news,
        and more.
      </p>
    </section>
```

And there you have it – now you can comment your HTML code correctly and safely.

Thank you for reading.


