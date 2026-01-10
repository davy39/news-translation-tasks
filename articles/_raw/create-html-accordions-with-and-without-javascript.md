---
title: How to Create HTML Accordion Elements With and Without JavaScript
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-11-30T19:10:31.000Z'
originalURL: https://freecodecamp.org/news/create-html-accordions-with-and-without-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/accordion-1.png
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Accordion elements are very handy for displaying topic titles and expandable
  details below them when you click the title.

  In this article, I''ll walk you through creating an FAQ section with some expandable
  accordion elements.

  I''ll show you how to do ...'
---

Accordion elements are very handy for displaying topic titles and expandable details below them when you click the title.

In this article, I'll walk you through creating an FAQ section with some expandable accordion elements.

I'll show you how to do this without any JavaScript, and then we'll add a bit of JavaScript to make it even better.

I've also made a video tutorial of the whole process here:

%[https://youtu.be/NYleh6wzDRE]

## How to Make an Accordion Using <details>

HTML has a disclosure element called `<details>` that can be in one of two states: open and closed. When opened, the information within the element is displayed. When closed, only the `<summary>` information is displayed.

This is an extremely easy version of the "accordion", although it's arguably not a true accordion by itself. When using `<details>`, more than one of the panels may be open at any one time – and because there's no JavaScript yet, panels will remain open until you click them again to close them.

Still, this is a quick and easy way to get an accordion-like element up and running. If you only need a few and aren't picky about functionality, this may be all you're looking for.

Here's what a basic example looks like. The `<summary>` is visible until clicked, at which point the rest of the content is displayed below it.

```html
<!-- With just <details> -->
<section>
    <h2>Accordion using details</h2>
    <details open>
        <summary>Who is Eamonn?</summary>
        A guy from TN who makes content on the internet.
    </details>
    <details>
        <summary>What kind of content does he make?</summary>
        He focuses on productivity tips using coding and spreadsheets. He makes <a href="https://youtube.com/@eamonncottrell">YouTube</a> videos and writes articles on freeCodeCamp, <a href="https://www.linkedin.com/in/eamonncottrell/">LinkedIn</a> and his <a href="https://got-sheet.beehiiv.com/">personal newsletter</a>.
    </details>
    <details>
        <summary>What does he do for fun?</summary>
        Hangs out with his wife and four kids, and runs ultramarathons.
    </details>
</section>
```

We can also have the first details panel open by default by simply including the open command: `<details open>`. 

Here's what that will look like with only a sprinkling of CSS:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/image-92.png)
_screenshot of HTML accordion made with &lt;details&gt; only_

This is a great start, but we can go further. A little bit of JavaScript will go a long way👇

## How to Add JavaScript to an Accordion Element

Let's make another section with three more `<details>` elements. And let's add a `class = "withJS"` to each one so we can do some different things to them for comparison's sake.

```html
<!-- With JavaScript -->
<section>
    <h2>Accordion with some JavaScript added</h2>
    <details  open>
        <summary class="withJS">What's the difference?</summary>
        We're adding JavaScript to these three.
    </details>
    <details >
        <summary class="withJS">Why add JavaScript?</summary>
        We can make it so only one panel can be open at a time.
    </details>
    <details >
        <summary class="withJS">Try clicking each of these</summary>
        See how one closes as soon as the other opens?.
    </details>
</section>
```

To keep things tidy and in one file, we can add a `<script>` tag at the bottom of our `<body>`. 

First, select all of the summary elements with the `.withJS` class by using `document.querySelectorAll()`:

```javascript
const summaries = document.querySelectorAll(".withJS")
```

Then add a click event listener to each of them:

```javascript
summaries.forEach(e=>{
    e.addEventListener('click',openCloseDetails)
})
```

This will run the function `openCloseDetails` every time one of these summary elements is clicked.

It won't do anything except give us an error until we declare that function, though...so, let's do that next.

Within the `<script>` after the `forEach` loop, let's have the `openCloseDetails()` function loop through those summaries again. This time, we want to modify the `open` status on the `<details>` element.

Remember how we have this setup: The first `<details>` element is set to `open` by default, and the others are closed.

We need a way to toggle the clicked element from open to closed, and close any previously `open` element when we click a new one.

To do this, we'll set a variable for the `<details>` element of each of the `<summary>` elements by setting it equal to `e.parentNode` in the `forEach` loop. 

```javascript
let details = e.parentNode;
```

The parentNode is the element directly preceding the current element. Since the `<summary>` elements are within the `<details>` elements, the `parentNode` for the `<summary>` elements will be the `<details>`.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/clearly.gif)
_gif of woman saying, "clearly"_

From there, we check if that `<details>` is NOT `this.parentNode`. If it's not, then we'll remove the `open` attribute.

The native functionality of the `<details>` elements will open the clicked one, we just needed to make sure all the other ones close.

Here's the code. It's not complicated, but it may take a second to wrap your head around the logic:

```javascript
summaries.forEach(e =>{
    let details = e.parentNode;
    if(details != this.parentNode){
        details.removeAttribute('open')
    }
```

And that's it. Now when we click each `<details>` the other ones automatically close:

![Image](https://www.freecodecamp.org/news/content/images/2023/11/accordion-gif.gif)
_gif of html accordion in action_

Here is the entire HTML file for your reference:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accordion</title>
</head>
<body>
    <style>
        body{
            background: rgb(255, 255, 230);
            color: #444;
        }
        details{
            font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
            margin-bottom: 5px;
            padding: 0.5em 0.5em 0;
        }
        details[open]{
            padding: 0.5em;
        }
        summary{
            font-weight: bold;
            margin: -0.5em -0.5em 0;
            padding: 0.5em;
            cursor: pointer;
        }
        details[open] summary{
            margin-bottom: 0.5em;
        }
    </style>
    
    <h1>Accordions</h1>

    <!-- With just <details> -->

    <section>
        <h2>Accordion using details</h2>
        <details open>
            <summary>Who is Eamonn?</summary>
            A guy from TN who makes content on the internet.
        </details>
        <details>
            <summary>What kind of content does he make?</summary>
            He focuses on productivity tips using coding and spreadsheets. He makes <a href="https://youtube.com/@eamonncottrell">YouTube</a> videos and writes articles on freeCodeCamp, <a href="https://www.linkedin.com/in/eamonncottrell/">LinkedIn</a> and his <a href="https://got-sheet.beehiiv.com/">personal newsletter</a>.
        </details>
        <details>
            <summary>What does he do for fun?</summary>
            Hangs out with his wife and four kids, and runs ultramarathons.
        </details>
    </section>
    

    <!-- With JavaScript -->
    <section>
        <h2>Accordion with some JavaScript added</h2>
        <details  open>
            <summary class="withJS">What's the difference?</summary>
            We're adding JavaScript to these three.
        </details>
        <details >
            <summary class="withJS">Why add JavaScript?</summary>
            We can make it so only one panel can be open at a time.
        </details>
        <details >
            <summary class="withJS">Try clicking each of these</summary>
            See how one closes as soon as the other opens?.
        </details>
    </section>
    
    <script>
        const summaries = document.querySelectorAll(`.withJS`)
        summaries.forEach(e=>{
            e.addEventListener('click',openCloseDetails)
        })

        function openCloseDetails(){
            summaries.forEach(e =>{
                let details = e.parentNode;
                if(details != this.parentNode){
                details.removeAttribute('open')
            }
            })
        }
    </script>
</body>
</html>
```

## Thanks for Reading

I hope this was useful for you!

Come follow me on YouTube: [https://www.youtube.com/@eamonncottrell](https://www.youtube.com/@eamonncottrell) 

And sign up for my coding & spreadsheet newsletter: [https://got-sheet.beehiiv.com/](https://got-sheet.beehiiv.com/)

Have a great one!

