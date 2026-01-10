---
title: Learn How to Manipulate CSS with JavaScript by Coding a Dynamic Picture Frame
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-04T15:27:39.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-manipulate-css-with-javascript-by-coding-a-dynamic-picture-frame
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Box-Model.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Samuel A. Olubiyo\nDOM manipulation can simply be defined as manipulating\
  \ HTML documents (or pages) with JavaScript. \nThe DOM stands for Document Object\
  \ Model that you can visualize as a tree-like structure made up of different HTML\
  \ elements. \nVisu..."
---

By Samuel A. Olubiyo

DOM manipulation can simply be defined as manipulating HTML documents (or pages) with JavaScript. 

The DOM stands for Document Object Model that you can visualize as a tree-like structure made up of different HTML elements. 

Visualizing an HTML document like a tree makes it easy to access its elements and potentially change them. JavaScript helps us to do this.

![The DOM visualized as a tree.](https://www.freecodecamp.org/news/content/images/2022/05/js-dom-model.png)
_The DOM visualized as a tree_

Now, JavaScript is a powerful language, so not only can we manipulate HTML elements with it, but we can also use it to manipulate the CSS properties of any webpage.

In this tutorial, I will teach you how to manipulate the styling of a webpage by building a simple project. 

In this project we will be coding a picture frame using HTML and CSS, then we will use JavaScript to make the picture frame dynamic. Sounds like fun? Let’s begin!

## How to Create the HTML File

Create a folder for this project and name it whatever you please. Then navigate to the folder in your favorite code editor and create a new HTML file. I named mine `box.html`, but you can name yours whatever you like. 

Next, [generate an HTML5 boilerplate](https://www.freecodecamp.org/news/html-starter-template-a-basic-html5-boilerplate-for-index-html/) by pressing the exclamation mark and hitting the enter key.

Within the body tag, create an h1 tag and type the title of this project within it. In my case, I did this:

`<h1>CSS Picture Frame</h1>`

Next, create a div and give it a class of “border” like this:

`<div class = “border”></div>`

Within this div, create another div and give it a class of “padding” like this:

`<div class = “padding”></div>`

Within the “padding” div, create yet another div and give it a class of “content” like this:

`<div class = “content”></div>`

Now, this “content” div is where the picture will be. You have a choice of either using an image or an emoji. I chose to use an emoji, so I did something like this:

`<div class = “content”>&#127856;</div>`

So far, we have created three divs. Together, they should look like this:

```html
<div class="border">
   <div class="padding">
       <div class="content">
            &#127856;
                </div>
           </div>
       </div
```

Immediately beneath the code above, create a new div and give it an Id of “inputs” like this:

`<div id = “inputs”></div>`

Within this “inputs” div create another div with an Id of  “sliders”, because we will be creating sliders within them. 

To create a slider in HTML, simply do something like this:

`<input type="range" name="" id=""  min="10" max="100">`

`<input type = "range">` creates a slider input, and the `min` and `max` attribute are used to specify the minimum and maximum values the slider can have. In this case, the minimum is 10 and the maximum is 100. 

For this project, we need 3 sliders, one for the "border", one for the "padding", and one for the "content", respectively. Give each slider an Id that makes sense or you can just do it like I did mine:

```html
<div id="sliders">
<h3>Border: </h3>
<input type="range" name="" id="border-range"  min="10" max="100">
<h3>Padding: </h3>
<input type="range" name="" id="padding-range" min="10" max="100">
<h3>Content: </h3>
<input type="range" name="" id="content-range" min="10" max="100">
</div>
```

Below the “sliders” div create a new div and give it an Id of “colors”, like this:

`<div id = “colors”></div>`

because we'll be creating color pickers in this div. You can create color pickers by doing this:

`<input type="color" name="" id="">`

We also need 3 color pickers for this project, one each for the “border”, “padding” and “content” div, respectively. So go ahead and create three color pickers within the “colors” div. Your code should look like this:

```html
<div id="colors">
<h3>Border:</h3>
<input type="color" name="" id="border-color">
<h3>Padding</h3>
<input type="color" name="" id="padding-color">
<h3>Content</h3>
<input type="color" name="" id="content-color">
</div>
```

When you view your page in the browser, you should get a result like the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--9--1.png)

The next step is to link the CSS and JavaScript files. If you haven't already, you should create a CSS and JS file and link them to your HTML. In my case, I created a `box.css` and a `box.js` file. Do not forget to:

* Link your CSS file within the head tag of your HTML with the following code: `<link rel="stylesheet" href="box.css">`
* Link your JS file within the body tag at the very bottom of your code, immediately below the last closing div and above the closing body tag like this: `<script src="box.js"></script>`

If you did this successfully, congratulations! The HTML part of this tutorial is now complete. Here is the full HTML code:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Box Model</title>
    <link rel="stylesheet" href="box.css">
</head>
<body>
    <h1>CSS Picture Frame</h1>
        <div class="border">
            <div class="padding">
                <div class="content">
                    &#127856;
                </div>
            </div>
        </div>

        <div id="inputs">
        <div id="sliders">
            <h3>Border: </h3>
            <input type="range" name="" id="border-range"  min="10" max="100">
            <h3>Padding: </h3>
            <input type="range" name="" id="padding-range" min="10" max="100">
            <h3>Content: </h3>
            <input type="range" name="" id="content-range" min="10" max="100"> 
        </div>

            <div id="colors">
                <h3>Border:</h3>
                <input type="color" name="" id="border-color">
                <h3>Padding</h3>
                <input type="color" name="" id="padding-color">
                <h3>Content</h3>
                <input type="color" name="" id="content-color">
            </div>
        </div>
        <script src="box.js"></script>
</body>
</html>
```

## How to Style the Webpage with CSS

Open the CSS file you created and add the following code:

```css
body{
display: flex;
align-items: center;
justify-content: center;
background-color: aquamarine;
flex-direction: column;
}
.border{
background-color: #0b67c4;
padding: 45px;
}
.padding{
background-color: #42b3dd;
padding: 45px;
}
.content{
background-color: #299baf;
padding: 45px;
font-size: 78px;
}
#inputs{
display: flex;
flex-direction: row;
}
#sliders{
margin-right: 30px;
}
```

**Note:** This styling will only work if you used the same Ids and classes I used in the HTML.

Now, let us pay attention to the `.border`, `.padding`, and `.content` styles. You’ll notice that apart from `.content`, they all have two rules namely: `background-color` and `padding`. It is these two rules we'll manipulate with our JavaScript code.

Remember the sliders and color pickers we created in our HTML code? We'll use the sliders to manipulate the padding property of `.border`, `.padding`, and `.content` respectively. And we'll use the color pickers to change the `background-color` property of each of the divs. 

When you refresh your browser, you should have something similar to the screenshot below:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screenshot--2--1.png)

## How to Write the JavaScript

The JS code for this project can be divided into three parts. First, we get the Ids of the sliders and color pickers and store them in variables. Next, we get the classes of the "border", "padding" and "content" divs and also store them in variables. And finally, we attach event listeners to the variables. 

Since we want the sliders to change the padding property of the divs and the color pickers to change their background colors, we use the change event listener to achieve that.

Now it is time to code. First, get the Ids of the sliders like this and store them in variables (keeping in mind the names of the Ids used in the HTML code.):

```js
let borderRange = document.getElementById("border-range")
let paddingRange = document.getElementById("padding-range")
let contentRange = document.getElementById("content-range")
```

Next, get the Ids of the color pickers and store them in variables too, something like this:

```js
let borderColor = document.getElementById("border-color")
let paddingColor = document.getElementById("padding-color")
let contentColor = document.getElementById("content-color")
```

Now get the classes of the border, padding, and content divs using the `querySelector` like this:

```js
let borderBox = document.querySelector(".border")
let paddingBox = document.querySelector(".padding")
let contentBox = document.querySelector(".content")
```

The next step after this is to attach event listeners to each slider and color picker. To make the first slider change the CSS padding property of the border div, we simply use the following code:

```js
borderRange.addEventListener("change", function(){
borderBox.style.padding = borderRange.value + "px"
})
```

Let me explain: The change event listener listens for a change in the slider. The code `borderBox.style.padding` is used to target the padding property of borderBox.

`borderRange.value` gets the value of the slider, and `+  “px”` adds px to whatever this value is. Equating `borderBox.style.padding` to `borderRange.value + “px”` is a way of telling our code to change the padding property of borderBox to whatever value borderRange inputs in pixels anytime we move the slider (that is, the change event is triggered).

Do the same for the padding and content divs like this:

```js
paddingRange.addEventListener("change", function(){
paddingBox.style.padding = paddingRange.value + "px"
})
contentRange.addEventListener("change", function(){
contentBox.style.padding = contentRange.value + "px"
})
```

After doing this, attach event listeners to the color pickers using the same principle – except, in this case, the color values are in hexadecimal, so we do not need to add any units to them. 

Instead of targeting the padding property, we target the `backgroundColor` property instead. (Note: the syntax for background-color in JS is in camel case.)

Your code should look like this:

```js
borderColor.addEventListener("change", function(){
borderBox.style.backgroundColor = borderColor.value
})
paddingColor.addEventListener("change", function(){
paddingBox.style.backgroundColor = paddingColor.value
})
contentColor.addEventListener("change", function(){
contentBox.style.backgroundColor = contentColor.value
})
```

Now, when you refresh your browser, you should be able to change the sizes of the boxes and their colors with the sliders and color pickers. With this code, you can create a picture frame of different sizes and colors.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/sizes-and-colors-examples.jpg)

Here is the full JS code:

```js
let borderRange = document.getElementById("border-range")

let paddingRange = document.getElementById("padding-range")

let contentRange = document.getElementById("content-range")


let borderColor = document.getElementById("border-color")

let paddingColor = document.getElementById("padding-color")

let contentColor = document.getElementById("content-color")


let borderBox = document.querySelector(".border")

let paddingBox = document.querySelector(".padding")

let contentBox = document.querySelector(".content")

borderRange.addEventListener("change", function(){
    borderBox.style.padding = borderRange.value + "px"
    console.log(borderRange.value)
   
})

paddingRange.addEventListener("change", function(){
    paddingBox.style.padding = paddingRange.value + "px"
    console.log(paddingRange.value)
   
})

contentRange.addEventListener("change", function(){
    contentBox.style.padding = contentRange.value + "px"
    console.log(contentRange.value)
})

borderColor.addEventListener("change", function(){
    borderBox.style.backgroundColor = borderColor.value
})


paddingColor.addEventListener("change", function(){
    paddingBox.style.backgroundColor = paddingColor.value
})

contentColor.addEventListener("change", function(){
    contentBox.style.backgroundColor = contentColor.value
})
```

## Conclusion

You can use JavaScript's DOM manipulation techniques to manipulate not just the HTML file but its styling as well. 

The applications of this knowledge are only limited by your imagination. You can create CSS art and effects with this technique with just a little creativity.

You can connect with me on Twitter [at https://www.twitter.com/lordsamdev](https://www.twitter.com/lordsamdev). I tweet about new ideas and projects I'm working on. I would also love to see what you've built by following this tutorial.

Thanks for reading.

