---
title: How to Use Font Awesome v5.7.2 with HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:14:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-font-awesome-v5-7-2-with-html
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa9740569d1a4ca26f1.jpg
tags:
- name: fonts
  slug: fonts
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
- name: typography
  slug: typography
seo_title: null
seo_desc: 'Font Awesome is one of the most popular ways to add icons to your site.
  But what if you add the CDN to the <head> element of your page and all you see are
  black rectangles?


  Here are a couple of things to keep in mind when you add Font Awesome to you...'
---

Font Awesome is one of the most popular ways to add icons to your site. But what if you add the CDN to the `<head>` element of your page and all you see are black rectangles?

![Image](https://www.freecodecamp.org/news/content/images/2020/05/6f22c59bffe7f1b87fed6d58092f69d53e3bbd15.png)

Here are a couple of things to keep in mind when you add Font Awesome to your next project.

### Add the link to the head

Imagine you have the following HTML:

```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="testing.css">
	<link rel="stylesheet" type="text/css" href="css/all.css">
	<meta name="viewport" content="width=device-width, initial-scale=1 user-scalable=no">
</head>
<body>
	<i class="fab fa-github-square"><a href="https://github.com/willyblackkeez" id="profile-link"></a></i>
	<i class="fab fa-facebook"></i>
</body>
</html>
```

Like other CDNs, you need to add a `<link>` element to the `<head>`. For Font Awesome 5.7.2, it'll look something like this: 

`<link rel="stylesheet" href="//use.fontawesome.com/releases/v5.0.7/css/all.css">`

### Online vs local

If you run the following code in a web based editor like CodePen or CodeSandbox, the following code renders icons properly:

```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
    <link rel="stylesheet" href="//use.fontawesome.com/releases/v5.0.7/css/all.css">
	<link rel="stylesheet" type="text/css" href="testing.css">
	<link rel="stylesheet" type="text/css" href="css/all.css">
	<meta name="viewport" content="width=device-width, initial-scale=1 user-scalable=no">
</head>
<body>
	<i class="fab fa-github-square"><a href="https://github.com/willyblackkeez" id="profile-link"></a></i>
	<i class="fab fa-facebook"></i>
</body>
</html>
```

But if you try to open the page locally in a browser, you'll still see the black rectangles instead of the icons:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/6f22c59bffe7f1b87fed6d58092f69d53e3bbd15-1.png)

Take another look at the `href` in the `<link>` element above. Do you see it?

The problem is that, when you load the page from your local file system, the browser is trying to find the Font Awesome CSS file at the root of the file system. 

To get things working online and locally, make sure to add the URL scheme (HTTP, or better, HTTPS) to the `href`:

`<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.7/css/all.css">`

### What's going on here?

When you leave off the URL scheme (`href="//use.fontawesome..."`), then the browser uses the same URL scheme the page was loaded with.

So if you run the page locally by running the HTML file in a browser, the `href` assumes the Font Awesome CSS is also a file that is also saved locally (`file:`).

Just make sure the `href` attributes for your `<link>` elements all point to the full URL, including the URL scheme, and you should be good to go.

