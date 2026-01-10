---
title: Learn How to Use JavaScript Arrays by Building an iPhone Product Page
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-22T00:10:02.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-arrays-by-building-product-page
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-caleb-oquendo-9667337-min-1--1.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
seo_title: null
seo_desc: 'By Samuel A. Olubiyo

  I had the idea for this tutorial while browsing the official iPhone website. Apple
  is known for its great products and impeccable design, and if you spend enough time
  checking out its website, you can learn a thing or two about b...'
---

By Samuel A. Olubiyo

I had the idea for this tutorial while browsing the official iPhone website. Apple is known for its great products and impeccable design, and if you spend enough time checking out its website, you can learn a thing or two about branding and great design. 

One of the things that caught my attention while browsing the iPhone 13 product page is the feature where the user can select a phone color from a choice of 3 or 4 colors. You do this by clicking a button of the corresponding color and the phone's color will change. 

When I wrote this, I didn't know how Apple achieved this – but to demonstrate my knowledge of JavaScript arrays, I decided to build a simple version of an iPhone product page. It would have buttons that could change the color of the phone when clicked. 

After building the page (and it worked) I realized that this might not be the technique Apple used after all. (I'll share why I think so in the concluding part of this tutorial.) Still, it's a fun project and way to learn about arrays in JS.

Here's what we'll cover:

* How to set up the HTML
* How to set up the CSS
* How to set up the JavaScript

This tutorial assumes you have a bit of knowledge of DOM manipulation with JavaScript, HTML, and CSS. A lot of things will make more sense if you do. 

I’ll also, try my best to explain every piece of the code in detail as much as I can. With that said, let’s get going.

## How to Set Up the HTML

Before you begin, download images of 3 or 4 iPhones of different colors from the internet. You can find such images on the iPhone website or phone review sites.

Make sure the images you download have transparent backgrounds, are of the same size and the same kind, (that is, if one image has the back camera showing, all images must be like this – but of different colors and the same size.). 

Once you have your images, save them in a folder and name the folder **images.** By this point, you should have created a main folder for this project. If you haven’t you can do that now. Name your folder whatever you please but make sure the images folder you created earlier is in the main folder.

Now that your folders are ready it is time to start coding. In your favorite code editor (mine is VSCode) navigate to the main folder you created earlier and create a new HTML file. I named mine phone.html but you can name yours whatever you like. 

To save time, I used an emmet function to generate an HTML boilerplate – just press an exclamation mark and hit enter.

In the body tag, create a main div and give it a class “main” like this:

```html
<div class="main">
</div>
```

Within this main div, create another div and give it an Id of “phone” like this:

```html
<div id="phone">
</div>
```

Now, within the "phone" div, create an h3 tag and enter: "I Love iPhones" or you can replace 'Love' with an emoji. In my case, I did something like this:

`<h3>I &hearts; iPhones</h3>`

Below this h3 tag, create another div and give it an id of “phoneshow” like this:

`<div id="phoneShow"></div>`

Leave this div empty, but below it create yet another div and give it an Id of “buttons”. Within this div, create 4 span tags to represent the 4 buttons – that is, if you downloaded 4 iPhone images. 

Within each span tag, create a button tag and give each button a different id corresponding to the color of the phone images. Here is an example:

```html
<div id="buttons">
<span><button id="black"></button></span>
<span><button id="blue"></button></span>
<span><button id="pink"></button></span>
<span><button id="starlight"></button></span>
</div>
```

After doing this, you are almost done with the HTML part of this tutorial. All that is left is linking the CSS and JavaScript files. 

If you haven't created a CSS and JavaScript file yet, now would be a good time to do so. In my case, I created a phone.css and a phone.js file. Next, link the CSS file within the head tag like this:

`<link rel ="stylesheet" href = "phone.css">`

Now, link your JavaScript file below the last closing div tag and just above the closing body tag with this code:

`<script src = "phone.js"></script>`

After you have done this, your HTML code is complete.

## How to Set Up the CSS

The CSS code for this project is pretty simple. Style the body, the “main” div, the “phone” div, the “phoneshow” div, the “buttons” div and the buttons like this:

```css
body{
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
background-color: rgb(255, 255, 255)
}

.main{
display: flex;
flex-direction: row;
flex-wrap: wrap;
align-items: center;
justify-content: center;
background-color: #ffff;
border-radius: 10px;
}

#phone{
display: flex;
flex-direction: column;
margin-bottom: 5px;
flex-wrap: nowrap;
align-items: center;
justify-content: center;
background-color: rgb(255, 255, 255);
border-radius: 10px;
}

#phoneShow{
display: flex;
flex-direction: row;
flex-wrap: wrap;
align-items: center;
justify-content: center;
background-color: #ffff;
border-radius: 10px;
}

#buttons{
display: flex;
flex-direction: row;
}

button{
margin-right: 10px;
border-radius: 50%;
padding: 15px;
border: none;
}
```

Note: `#buttons` is different from `buttons`. While the former is a div, the latter is the button element – hence the lack of a selector in front of it. Border-radius: 50%; will make the buttons completely round.

This CSS code uses Flexbox.

Give each button a different background color by styling their different Ids based on the color of the iPhone images you downloaded. Here is an example:

```css
#black{
background-color: black;
}
```

```css
#blue{
background-color: blue;
}
```

```css
#pink{
background-color: pink;
}
```

```css
#starlight{
background-color: silver;
}
```

After doing this, you can preview your progress in the browser. You should see 4 round buttons of different colors, centered on the page.

## How to Set Up the JavaScript

This is the most important part of this tutorial. So far, you've created the basic structure and styling of the page. But to display and change the images of the phone on the page, the magic happens here.

First, create an array of the directories of the images you downloaded at the beginning of this tutorial. Remember the images folder from earlier? What you need to do is to store the relative path of each image in the folder inside an array in string form. Like this:

```js
const phoneImages = ["images/Black.png", "images/Blue.png", "images/Pink.png", "images/Starlight.png"]
```

(Assuming your images are saved as Black.png, Blue.png, and so on.)

Next, get the Id of the div where the phone images will appear. For this tutorial, the phones will appear in the “phoneshow” div from earlier. Store the gotten Id in a variable like this:

`let phoneCont = document.getElementById("phoneshow")`

Next, get the Ids of all the buttons and store them in variables, here is an example:

`let black=document.getElementById("black")`

`let blue=document.getElementById("blue")`

`let pink=document.getElementById("pink")`

`let starlight=document.getElementById("starlight")`

After doing this, it is time to make an iPhone image appear. To do this, create a variable called “defaultImgItems” because for the page to function, there should be a default image on the page that the user can switch from. 

You can use the following code to do this:

```js
let defaultImgItems =`<img src= "${phoneImages.at(0)}">`
```

Let me explain:

Using backticks `` enables us to insert HTML code within our JavaScript. In this case, I want an image tag embedded in the variable `defaultImgItems`. The source is the first item in the phoneImages array. You can access it by the `at()` method.

To display the image in the selected div just use the code below:

`phoneCont.innerHTML = defaultImgItems`

`phoneCont` is the variable you stored the div with Id of “phoneshow” earlier. If you refresh the page in the browser, you should see the first iPhone image in the `phoneImages` array displayed. 

After you have done this, create similar variables for the other three colors like this:

```js
let blueImgItems=`<img src= "${phoneImages.at(1)}">`
let pinkImgItems=`<img src= "${phoneImages.at(2)}">`
let starImgItems=`<img src= "${phoneImages.at(3)}">`
```

(These variables are for the second, third, and fourth items in the `phoneImages` array.)

### How to make the buttons work

If you have done this successfully, the next step is to make the buttons functional. The buttons should be able to change the iPhone color to the corresponding color of the buttons – that is the blue-button should display a blue iPhone and so on.

To achieve this, attach event listeners to the buttons and make them change the `innerHTML` properties of phoneCont. Like this:

```js
black.addEventListener("click", function(){
phoneCont.innerHTML=defaultImgItems
})
```

The code above will make the black button, when clicked to display a black iPhone. The remaining code snippets are as follows:

```js
blue.addEventListener("click", function(){
phoneCont.innerHTML = blueImgItems
})

pink.addEventListener("click", function(){
phoneCont.innerHTML = pinkImgItems
})

starlight.addEventListener("click", function(){
phoneCont.innerHTML = starImgItems
})
```

After doing these, refresh your browser and click each button in turn. The iPhone Images should change with each click.

## Conclusion:

In this tutorial, you learned a practical use of arrays in real-world projects. You also learned how to access array items using the .at() method.

At the beginning of this tutorial, I mentioned that I did not think Apple used this method to build their iPhone product page. This is because when you load the page created with this tutorial and click each button in turn, the iPhone images do not change smoothly – rather they seem to jump. Only after all the buttons have been clicked do the images change smoothly when you click a new button. Still, I hope this tutorial has been beneficial to you.

You can connect with me on Twitter for updates on what I'm working on or any new ideas that pop into my head at https://[www.twitter.com/lordsamdev](http://www.twitter.com/lordsamdev). You can also let me know what you think about the code in this tutorial – I am open to your ideas.

Thanks for reading!

