---
title: HTML and CSS – Inline Style, External Stylesheet, CSS Code Examples
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-12T18:47:27.000Z'
originalURL: https://freecodecamp.org/news/html-and-css-inline-style-external-stylesheet-css-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Htmlcss.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'When you''re learning about web development, you probably hear about HTML
  and CSS pretty quickly. Well, what are these tools and how do you use them?

  You can think of HTML as the structure and framing of a house. And when you want
  to make that structu...'
---

When you're learning about web development, you probably hear about HTML and CSS pretty quickly. Well, what are these tools and how do you use them?

You can think of HTML as the structure and framing of a house. And when you want to make that structure look good, you add paint, decor, and other features. This decoration is the CSS.

## How Do You Style HTML Code?

HTML stands for hypertext markup language. It is a text-based document designed to be displayed in a browser. To make that texts and other embedded elements contained in the HTML look good, you need to add CSS, or Cascading Style Sheets.

There are 3 different ways you can style your HTML: 
* inline styles, 
* internal styles (also known as embedded CSS), and 
* external stylesheets. 

In this tutorial, we'll explore these three styling methods in as much depth as possible. We'll also look at their pros and cons so you can start using them in your coding projects and choose which one works best for you.

## HTML Template

To make things easier in this tutorial, I have prepared a simple HTML template that we'll style: 

```html
<article>
    <p class="paragraph-one">
      freeCodeCamp is one of the best platforms to learn how to code
    </p>
    <p class="paragraph-two">
      Learning to code is free on freeCodeCamp, that's why they call it
      freeCodeCamp
    </p>
    <p class="paragraph-three">
      freeCodeCamp generates money through donations inorder to pay employees
      and maintain servers.
    </p>
    <p id="paragraph-four">
      If you're generous enough, consider joining others who have been
      donating to freeCodeCamp
    </p>
    <p class="paragraph-five">
      At freeCodeCamp, it's not all about typing on a code editor alone,
      there's a forum like StackOverflow, where you can ask questions about
      your coding problems and get answers from campers alike.
    </p>
</article>
```

![initialPageView](https://www.freecodecamp.org/news/content/images/2021/08/initialPageView.png)

## Inline Styles in HTML

When you use inline styles, you add them directly to the HTML tags with the style attribute. 

For example, in our HTML code, we can assign a color to any of the paragraphs by writing the CSS right inside the opening tag. 

It is also typical to remove the default underline and color assigned to links, so we can do that inside the opening `<a>` tag too.

```html
<article>
   <p
     class="paragraph-one"
     style="color: darkmagenta; font-size: 2rem; text-align: center"
   >
     <a href="freecodecamp.org" style="text-decoration: none; color: crimson"
       >freeCodeCamp</a
     >
     is one of the best platforms to learn how to code
   </p>
   <p class="paragraph-two">
     Learning to code is free on freeCodeCamp, that's why they call it
     freeCodeCamp
   </p>
   <p class="paragraph-three">
     freeCodeCamp generates money through donations inorder to pay employees
     and maintain servers.
   </p>
   <p id="paragraph-four">
     If you're generous enough, consider joining others who have been
     donating to freeCodeCamp
   </p>
   <p class="paragraph-five">
     At freeCodeCamp, it's not all about typing on a code editor alone,
     there's a forum like StackOverflow, where you can ask questions about
     your coding problems and get answers from campers alike.
   </p>
 </article>
```

Can you see that the first paragraph is now less readable? That's one of the downsides of using inline styles, which we'll see below.

Our web page now looks like the screenshot below:

![inlineStyling](https://www.freecodecamp.org/news/content/images/2021/08/inlineStyling.png)

### Pros of Inline Styles

- Good for quick fixes.
- Takes the highest specificity, so it overrides any style set with inline style or external stylesheets.
- You don't need to switch between files or scroll to the head section to modify the CSS
- Browsers always download the HTML, CSS, and JavaScript files before displaying a web page, so with inline CSS there are fewer files to be downloaded.

### Cons of Inline Styles

- Makes the HTML messy, harder to maintain, and less readable.
- Cannot be reused across multiple HTML files
- You can end up overriding internal styles or external stylesheets 
- You have limited styling options


## Internal Styles in HTML

When you use internal styling, you embed the styles right inside the HTML file within the style tag. You usually place them in the head, but it works anywhere, even outside of the opening and closing HTML tags (but don't do that as it's a bad practice).

We can apply some internal styles to our HTML code like this:

```html
<style>
   * {
     padding: 0;
     margin: 0;
     box-sizing: border-box;
 }
 body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
   }

 .paragraph-two {
     font-size: 1.5rem;
      }

 .paragraph-one a {
      text-decoration: none;
      color: crimson;
      font-size: 2rem;
      font-weight: bolder;
     }
 </style>
</head>
 <body>
 <article>
   <p class="paragraph-one">
     <a href="freecodecamp.org">freeCodeCamp</a>
     is one of the best platforms to learn how to code
   </p>
   <p class="paragraph-two">
     Learning to code is free on freeCodeCamp, that's why they call it
     freeCodeCamp
   </p>
   <p class="paragraph-three">
     freeCodeCamp generates money through donations inorder to pay employees
     and maintain servers.
  </p>
   <p id="paragraph-four">
     If you're generous enough, consider joining others who have been
     donating to freeCodeCamp
   </p>
   <p class="paragraph-five">
     At freeCodeCamp, it's not all about typing on a code editor alone,
     there's a forum like StackOverflow, where you can ask questions about
     your coding problems and get answers from campers alike.
   </p>
 </article>
```

You can see that we now have more styling options when we use internal styles. 

### Pros of Internal Styles

- Reduces the number of files browsers need to download
- No switching between files to modify CSS
- More styling options as you can use combinators, class selectors, and id selectors

If you are wondering what combinators are, they are the symbols used to connect different selectors. An example is a space (` `) for selecting the next descendant of an element, such as any paragraph (`p`) that comes after a `div`. 

Class selectors are denoted by a dot (`.`), and id selectors are denoted by a `#`. 

### Cons of Internal Styles

- They cannot be reused across multiple HTML files. To add the same style to another HTML file, you need to include it in the head again
- It increases the HTML file size, which may lead to slower load speeds.

Our web page now looks like this: 
![internalStyling](https://www.freecodecamp.org/news/content/images/2021/08/internalStyling.png)

## External Stylesheets in HTML

This is considered the best way to style your HTML code. External stylesheets are totally separate from the HTML and you place them in a CSS file (with the `.css` extension). 

To use external stylesheets in your HTML, you link them within the head with the link tag. 

The basic syntax of the link tag looks like this:

```html
<link rel="stylesheet" href="path-to-css-file">
```

To style our HTML code, we need to create a CSS file and link it. When linked, our full HTML file now looks like this:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>How to Style HTML</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <article>
      <p class="paragraph-one">
        <a href="freecodecamp.org">freeCodeCamp</a>
        is one of the best platforms to learn how to code
      </p>
      <p class="paragraph-two">
        Learning to code is free on freeCodeCamp, that's why they call it
        freeCodeCamp
      </p>
      <p class="paragraph-three">
        freeCodeCamp generates money through donations inorder to pay employees
        and maintain servers.
      </p>
      <p id="paragraph-four">
        If you're generous enough, consider joining others who have been
        donating to freeCodeCamp
      </p>
      <p class="paragraph-five">
        At freeCodeCamp, it's not all about typing on a code editor alone,
        there's a forum like StackOverflow, where you can ask questions about
        your coding problems and get answers from campers alike.
      </p>
    </article> 
</body>
</html>
```
 
You might be wondering why the path to the CSS file is just `style.css`, which is also the filename. This is because the HTML and CSS files are in the same directory. If you have the stylesheet in another folder, you have to include the folder name before the filename.

Let's apply some stylings to our HTML in our external stylesheet: 

![externalStyling](https://www.freecodecamp.org/news/content/images/2021/08/externalStyling.png)

### Pros of External Stylesheets

- Makes styles reusable across multiple HTML files
- It is easier to maintain
- It is cached by the browser on initial load, making page rendering easier and less time consuming after subsequent page loads
- It can be hosted on a CDN, so bandwidth becomes minimal and it can be easily transported across various regions of the world.

### Cons of External Stylesheets
- It increases the number of files the browser needs to download
- The browser has to make extra HTTP requests per file

## Conclusion

I hope this tutorial has helped you learn the various ways you can style your HTML.

And now you also know the pros and cons of each method, so you can pick the one that is best for you. 

Thanks for reading, and keep coding. 



