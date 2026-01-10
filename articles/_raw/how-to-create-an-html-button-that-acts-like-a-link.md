---
title: How to Create an HTML Button That Acts Like a Link
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T22:05:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-html-button-that-acts-like-a-link
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e4f740569d1a4ca3c6e.jpg
tags:
- name: HTML
  slug: html
seo_title: null
seo_desc: 'Sometimes you may want to use a button to link to another page or website
  rather than to submit a form or something like that. This is fairly simple to do
  and can be achieved in several ways.

  How to Create an HTML Button Using the Button Tag in an A ...'
---

Sometimes you may want to use a button to link to another page or website rather than to submit a form or something like that. This is fairly simple to do and can be achieved in several ways.

## How to Create an HTML Button Using the Button Tag in an A Tag

One way is to simply wrap your `<button>` tag in an `<a>` tag:

```html
<a href='https://www.freecodecamp.org/'><button>Link To freeCodeCamp</button></a>
```

This transforms your entire button into a link.

## How To Turn a Link Into a Button with CSS

A second option is to create your link as you normally would with your `<a>` tag and then style it via CSS:

```html
<a href='https://www.freecodecamp.org/'>Link To freeCodeCamp</a>
```

Once you’ve created your link, you can the use CSS to make it look like a button. For instance, you could add a border, a background color, some styles for when the user is hovering the link.

You can [read more about styling links with CSS here](https://www.freecodecamp.org/news/a-quick-guide-to-styling-buttons-using-css-f64d4f96337f/).

## How to Put a Button inside a Form Using HTML

Another way to add a button is to wrap an `input` inside `form` tags. Specify the desired target URL in the form action attribute.

```html
<form action="http://google.com">
    <input type="submit" value="Go to Google" />
</form>
```

I hope you've found tutorial helpful. Happy coding.

