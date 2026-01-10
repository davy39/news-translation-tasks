---
title: How to Use the CSS Box Model and Style SVG Images
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-03T17:29:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-box-model-and-style-svg-images
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-tiger-lily-4483610--1-.jpg
tags:
- name: CSS
  slug: css
- name: SVG
  slug: svg
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "By Njoku Samson Ebere\nEvery programmer who wants to write clean CSS and\
  \ build great user interfaces should understand the CSS Box Model. \nBefore I understood\
  \ the foundations of CSS, I would often write unnecessary styles for margins and\
  \ padding.   \nC..."
---

By Njoku Samson Ebere

Every programmer who wants to write clean CSS and build great user interfaces should understand the CSS **Box Model**. 

Before I understood the foundations of CSS, I would often write unnecessary styles for **margins** and **padding**.   
  
CSS Box Model forms the basis for styling any element on a website. So understanding the concept will help you target HTML elements and write fewer lines of code that are clean and easy to maintain.  
  
This article will teach how to target the properties of any HTML element and apply the right style. You will also learn what SVG images are and how to style them.

## What is the CSS Box Model?

The CSS Box Model is the relationship between an **HTML element** and the spaces around it – its **padding, border,** and **margin**.

* Padding is the space that surrounds a given HTML element
* The border is the space that surrounds the padding
* Margin is the space that surrounds the border

In other words, the **padding** surrounds the HTML element, the **border** encloses the padding, and the **margin** houses the border. The image below illustrates it all:

![Image](https://dev-to-uploads.s3.amazonaws.com/i/jsm663u6fvzpq4b5buzr.jpg)
_CSS Box Model Illustration_

Now, enough of the theory – let's translate the diagram into code.

## Let's Code

%[https://www.youtube.com/watch?v=BWIpVT-QHbA&t=12s]

You can get your starter code [here](https://github.com/EBEREGIT/box-model-tutorial/tree/starter-code) by cloning the repo.  
  
Otherwise you'll need to create a new HTML file and copy the following code into the file (if you don't want to clone the repo or don't know how to use Git).

```
<!DOCTYPE html>
<html>
  <head>
    <title>Box Model Tutorial</title>
    <style>
    </style>
  </head>
  <body>
    <img src="https://www.w3schools.com/howto/img_avatar2.png" />
  </body>
</html>
```

The code above is a basic HTML boiler plate. It contains a `title` and an `img` element. I got the image from [w3schools](https://www.w3schools.com/).

Load the file in a browser, and you should get the following result:

![Image](https://dev-to-uploads.s3.amazonaws.com/i/0qm111t5yctvgkks36ea.JPG)
_Preview with margin_

Notice that the image came with a default space around it. That is the default margin. Let's remove it.   
  
Enter the following CSS into the `style` tag of your HTML file:

```
   body{
     margin: 0;
   }
```

This code removes all the margins around the image. Notice that there is no longer a space between the edges of the browser and the content in the image below.

![Image](https://dev-to-uploads.s3.amazonaws.com/i/ruru86w57zd4k512kv2o.JPG)
_Preview without margin_

Now let's get down to the main business.  
  
Add a border with the following code:

```
  img{
    border: 5px solid red;
  }
```

This code adds a red border around the content. The border's width is 5 pixels.

![Image](https://dev-to-uploads.s3.amazonaws.com/i/plb3mv3dxg4oju57ok1r.JPG)
_Preview with border_

And add some padding with the code below:

```
  img{
    border: 5px solid red;
    padding: 20px;
  }
```

The code above now creates a space between the content and the border. That space is called **padding.** It is 20 pixels wide.

![Image](https://dev-to-uploads.s3.amazonaws.com/i/01zjji5x4ypu18rpo5u9.JPG)
_Preview with padding_

Type the following code to add a margin:

```
  img{
    border: 5px solid red;
    padding: 20px;
    margin: 20px;
  }
```

You will recall that we removed the margin when we set the margin to 0px. The code above now adds our custom margin that is 20 pixels wide. It creates a space between the red border and the browser edges.

![Image](https://dev-to-uploads.s3.amazonaws.com/i/7aowqpgt6or44ivtzz0y.JPG)
_Preview with border_

You can get the code for this section [here](https://github.com/EBEREGIT/box-model-tutorial) or copy the code below:

```
<!DOCTYPE html>
<html>
  <head>
    <title>Box Model Tutorial</title>
    <style>
        body{
            margin: 0;
        }

        img{
            border: 5px solid red;
            padding: 20px;
            margin: 20px;
        }
    </style>
  </head>
  <body>
    <img src="https://www.w3schools.com/howto/img_avatar2.png" />
  </body>
</html>
```

The project is live here – [https://eberegit.github.io/box-model-tutorial/](https://eberegit.github.io/box-model-tutorial/).  
  
YESSSS! We did it. We made it!

## How to Style SVG Images

Now that you understand how the CSS box model works, let's try styling an important HTML element – an SVG. It is a bit different from other elements but the principles are the same.

[SVG images](https://en.wikipedia.org/wiki/Scalable_Vector_Graphics) are lightweight resources that can help speed up your applications. This section will help you look at SVGs from a friendly perspective and build better applications.  
  
SVG files consist of elements such as the `<g>` and `<path>` elements. You do not have to memorize them. You can inspect the SVG image in your browser to see the different parts and how you can target the element you want.  
  
These elements have a `border` (represented as **stroke**) and `background-color` (**fill**) attributes. We will be looking into those in a bit.  
  
You can download the SVG image for this tutorial [here](https://freesvg.org/volleyball-player-caricature). And you can get the starter project [here](https://github.com/EBEREGIT/styling-svg-images/tree/starter-project).  
  
In the starter project, I have gone ahead and:

1. Added the downloaded `SVG` file to the project directory.
2. Created an `index.html` file.
3. Copied and pasted the SVG code from the SVG file into the `index.html` file.
4. Created a `style.css` file with the following code to `center` all contents:

```
body{
    text-align: center;
}
```

If you run the project in a browser, you should have the following output:

![Image](https://dev-to-uploads.s3.amazonaws.com/i/l55mafu2iaj3xpcsrd3q.JPG)
_Starter Project_

## How to Style the SVG Image

### Make the Image Responsive

Change the `width` and `height` properties of the SVG element to 50% and 100vh, respectively, in the `index.html` file to make the image responsive like so:

```
<svg
        version="1.1"
        id="volleyball"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        x="0px"
        y="0px"
        width="50%"
        height="100vh"
        viewBox="0 -0.5 167 267"
        enable-background="new 0 -0.5 167 267"
        xml:space="preserve"
      >

      ...

</svg>
```

Now, your output should be like this:

![Image](https://dev-to-uploads.s3.amazonaws.com/i/y326rifv946zsphrabtq.JPG)
_The image now takes up the whole page and it is responsive too_

Looking sharp, let's move on!

### How to Change the Border Color

The SVG image we are using in this tutorial contains a `<g>` element, `<path>` element, and `<circle>` element.  
  
We will target the whole `path` and `circle` at once and give them `border-colors` and `width` with the following code:

```
path{
    stroke: red;
    stroke-width: 2px;
}

circle{
    stroke: darkblue;
}
```

Check if your output matches mine below:

![Image](https://dev-to-uploads.s3.amazonaws.com/i/sa8p8g8815lm6u2hb5fy.JPG)
_Stroke Added_

Notice that we changed the `path`'s border color to `red` with a reduced `width`. Then we changed the `circle`'s border color to dark blue. How Awesome!

### How to Change the Background

We could change the background color for the `paths` and `circles` as we did with the `border`, but let's do something different. We are going to give each `path` and `circle` different background colors.  
  
Each `path` and `circle` has a unique `id`.  
  
Let's add the following code to our `styles.css` file to give the `path` and `circle` different background colors with the following code:

```
#torso{
    fill: blue;
}

#left_leg{
    fill: green;
}

#left_arm{
    fill: indigo;
}

#right_arm{
    fill: yellow;
}

#ball{
    fill: hotpink;
}

#head{
    fill: olive;
}
```

I now have a clown-like volleyball player:

![Image](https://dev-to-uploads.s3.amazonaws.com/i/6yrdytn4p7hzm3qib64k.JPG)
_Fill Added_

If your clown looks like mine, then let's proceed...

### How to Add a Hover Attribute

To add a hover property, add the following code to the `styles.css` file:

```
path:hover{
    stroke: black;
    stroke-width: 10px;
}

circle:hover{
    stroke: black;
    stroke-width: 10px;
}
```

My output is the GIF image you see below:

![Image](https://dev-to-uploads.s3.amazonaws.com/i/arr2k0echobmtrgo01ro.gif)
_Hover added_

  
With the clown looking that way, let's do one more thing.

### How to Add Achor Tags

Now we're going to wrap each `path` and `circle` with an anchor tag.  
  
Give the `anchor` tag a `title` (represented as `xlink:title`) and a href (as `xlink:href`) attribute in the following manner:

```
<a xlink:title="a title" xlink:href="a url">
  <path> codes here </path>
</a>

<a xlink:title="a title" xlink:href="a url">
  <circle> codes here </circle>
</a>
```

Go ahead and use any `title` and `URL` of your choice. I added my social media profiles and other websites I built. Checkout mine below:  


![Image](https://paper-attachments.dropboxusercontent.com/s_D592C23061BDAFBA9E611AEDC8048F685A5679FCF2C57746CD5AE80A3DAD15B0_1680184339979_ezgif.com-video-to-gif.gif)
_Final Result_

  
Apart from changing the stroke width, we can see `labels`, and each part of the `image` is linked to a different website.  
  
The `xlink:title` and `xlink:href` attributes add a `label` and `URL` individually.  
  
All codes for this section is [here](https://github.com/EBEREGIT/styling-svg-images). The project is live [here](https://eberegit.github.io/styling-svg-images/)  
  
**YOU ROCK!**

## Conclusion

CSS gets a bit easier when you understand the basics. This article aimed to teach them to you.   
  
You have learned the difference between **margin** and **padding**. You also saw how they are related. Once you understand this, moving elements around the page becomes easy. In all, use padding to move an element within its container or axis and use a margin to create space between elements.  
  
I enjoyed dissecting that SVG image with you. You now know how to work with any SVG image that comes your way. They might differ, but the principle is understanding how their elements are named. Then you can target those elements in your styling.  
  
Try out more SVG images and see how they come out.

