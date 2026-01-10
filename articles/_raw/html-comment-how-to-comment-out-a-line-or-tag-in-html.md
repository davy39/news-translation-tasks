---
title: HTML Comment – How to Comment Out a Line or Tag in HTML
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-29T17:03:35.000Z'
originalURL: https://freecodecamp.org/news/html-comment-how-to-comment-out-a-line-or-tag-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/pexels-pixabay-268351.jpg
tags:
- name: best practices
  slug: best-practices
- name: HTML
  slug: html
seo_title: null
seo_desc: 'In this article, you''ll learn how to add single and multi-line comments
  to your HTML documents.

  You''ll also see why comments are considered a good practice when writing HTML code.

  Let''s get started!

  The HTML Comment Tag

  The general syntax for an HTML...'
---

In this article, you'll learn how to add single and multi-line comments to your HTML documents.

You'll also see why comments are considered a good practice when writing HTML code.

Let's get started!

## The HTML Comment Tag

The general syntax for an HTML comment looks like this:

```html
<!-- I am a comment! -->
```

Comments in HTML start with `<!--` and end with `-->`. 

Don't forget the exclamation mark at the start of the tag! But you don't need to add it at the end.

The tag surrounds any text or other HTML tag you want to comment out.

## When to Use HTML Comments

HTML comments don't get displayed in the browser. This means that any comments you add to your HTML source code will not be shown when the document gets rendered in a web browser. 

That being said, keep in mind that anyone can view the source code of practically every website published on the Internet by going to `View -> Developer -> View Source` – and this also includes all comments! 

So your comments will be visible for others to see if you make the HTML document public and they choose to look at the source code.

Writing comments is helpful and it's a good practice to follow when writing source code. Comments help you document and communicate about your code and thought process to yourself (and others). It also reminds you what you were thinking/doing when you come back to a project after months of not working on it.

Comments also help you communicate with other developers who are working on the project with you. Your comments can clearly explain to them why you added certain lines of code. 


## How to Write Single-Line Comments in HTML

A single-line comment only spans one line. As mentioned earlier, that line will not get displayed in the browser.

Use a single-line comment when you want to explain and clarify the purpose behind the code that follows it or when you want to add reminders to yourself like so:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- Add the navbar here -->
    <h2>About me</h2>
    <p>I am learning to code with freeCodeCamp.</p>
    <p>I am going through each and every one of their awesome and super helpful  certifications. </p>
    <p>I am on my way to becoming a fullstack web developer!</p>
    <h3>Work Experience</h3>
</body>
</html>
```

Single-line comments are also helpful when you want to make clear where a tag ends. This comes in handy in a long and complex HTML document where a lot is going on and you may get confused as to where a closing tag is situated.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <section class="contact">
    </section> <!--closing tag of contact section is here-->
</body>
</html>
```

## How to Write Inline Comments in HTML

You can also add comments in the middle of a sentence or line of code. 

Only the text inside the `<!-- -->` will be commented out, and the rest of the text inside the tag won't be affected.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>I am <!--going to be--> a web developer</p>
</body>
</html>
```

## How to Write Multi-Line Comments in HTML

Comments can also span multiple lines, using the exact same syntax you've seen so far.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>I am  a web developer</p>
    <!--This is going to be my portfolio.
    It will show off the projects that I'm most proud of.
    I could go on and on about what I want to add
    because I am writing a multi-line comment here-->
</body>
</html>
```

## How to Comment Out a Tag in HTML

So what if you want to comment out a tag in HTML?

You wrap the tag you've selected in `<!-- -->`, like so:

```html

!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>My portfolio page</h2>
    <h3>freeCodeCamp certification projects</h3>
    <!-- <section class="hero">
    </section>  -->
    <h2>About Me</h2>
</body>
</html>
```

Commenting out tags helps with debugging.

When something isn't working the way it's supposed to or they way you intended it to, start commenting out individual tags one by one. This lets you test them and see which one is causing the issue. 

## Keyboard Shortcut for Adding HTML Comments

There are shortcuts you can use for adding comments – and you'll probably end up using them a lot. The shortcut is `Command /` for Mac users or `Control /` for Windows and Linux users.

To add a single-line comment, just hold down the combo of keys shown above inside the code editor. Then the whole line you're on will be commented out. Just keep in mind that since everything will be commented out on that line, this only works for single-line comments. You'll need to add inline comments manually.

For adding multi-line comments, select and highlight all the text or tags you want to comment out and hold down the two keys shown previously. Each line you selected will now have a comment.

## Conclusion

And there you have it – now you know how and why to use comments in HTML!

Learn more about HTML by watching the following videos on freeCodeCamp's YouTube channel:

- [HTML Tutorial - Website Crash Course for Beginners ](https://www.youtube.com/watch?v=916GWv2Qs08)
- [HTML Full Course - Build a Website Tutorial](https://www.youtube.com/watch?v=pQN-pnXPaVg)

freeCodeCamp also offers a free, project-based certification on [Responsive Web Design](https://www.freecodecamp.org/learn/responsive-web-design/).

It is ideal for complete beginners and assumes no previous knowledge. You'll start from the absolute necessary basics and build your skills as you progress. In the end, you'll complete five projects.

Thanks for reading and happy learning :)


