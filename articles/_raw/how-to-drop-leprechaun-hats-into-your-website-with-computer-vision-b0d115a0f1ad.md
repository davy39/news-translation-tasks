---
title: how to drop LEPRECHAUN-HATS into your website with COMPUTER VISION
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-07T20:56:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-drop-leprechaun-hats-into-your-website-with-computer-vision-b0d115a0f1ad
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kfqTx__agnemI2s0kRd3rw.gif
tags:
- name: Computer Vision
  slug: computer-vision
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Shen Huang

  Automatically leprechaun-hat people on your website for St. Patrick’s Day.


  !!! — WARNING — !!!

  Giving a person a green hat can be considered OFFENSIVE to some Chinese people,
  as it has the same meaning as cheating in a relationship. So...'
---

By Shen Huang

#### Automatically leprechaun-hat people on your website for St. Patrick’s Day.

> **!!! — WARNING — !!!**

> Giving a person a green hat can be considered [**OFFENSIVE**](https://mspoweruser.com/microsoft-removes-green-hat-from-vs-2019-installer-after-offending-users-in-china/) to some Chinese people, as it has the same meaning as cheating in a relationship. So use this **CAREFULLY** when you are serving a Chinese user base.

> **!!! — WARNING — !!!**

In this tutorial, we will go over how to drop a leprechaun hat onto your website images that contain people. The process will be done through the aid of some **Computer Vision** frameworks, so it will be the same amount of work even if you have millions of portraits to go through. A demo can be found [**here**](https://shenhuang.github.io/demo_projects/tracking.js-master/TEAM%20MEMBERS%20_%20Teamwebsite.html) thanks to the permission from my teammates.

This tutorial is for more advanced audiences. I am assuming you can figure out a lot of the fundamentals on your own. I have also made some tutorials for total beginners, which I have attached in the end as links.

![Image](https://cdn-media-1.freecodecamp.org/images/oKTeBIcRIikaGpEVv0zWVOjoUNVQU43ms4XW)
_Leprechaun Hats Fall on top of Heads in Portraits_

### 1. Initial Setup

Before we start this tutorial, we need to first perform some setup.

First of all, we are using **tracking.js** to help us in this project, and therefore, we need to download and extract the necessary files for **tracking.js** from [**here**](https://github.com/eduardolundgren/tracking.js/archive/master.zip).

For this tutorial, we start with a template website I snatched from our team **WiX** which is a **Content Management System (CMS)** allowing you to build websites with much less effort. The template can be downloaded from [**here**](https://github.com/shenhuang/shenhuang.github.io/raw/master/tracking.js-master/site_template.zip). Extract the files into the “tracking.js-master” folder from previous step.

In order to make everything work, we also need a server. We will be using a simple Python server for this tutorial. In case you do not have Python or Homebrew (which helps to install Python), you can use the following bash commands to install them.

Installing Homebrew:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Installing Python:

```
brew install python
```

Now that everything is ready, we will run the command below under our “tracking.js-master” to start the Python server.

```
python -m SimpleHTTPServer
```

To test, go to this [**link**](http://localhost:8000/examples/face_hello_world.html) of your local host to see an example page. You should also be able to view the extracted example page from [**here**](http://localhost:8000/TEAM%20MEMBERS%20_%20Teamwebsite.html). And that is all you have to do for the setup.

![Image](https://cdn-media-1.freecodecamp.org/images/E3njCktFKMne4zqeC-1t6ljhser9k4Ay8Xhx)
_Setting up a simple Python server._

### 2. Creating the hat

Different from my other tutorials, we will be using an online image for this tutorial rather than trying to recreate everything with **CSS**.

I found a leprechaun hat from **kisspng** and it can be found [**here**](https://github.com/shenhuang/shenhuang.github.io/raw/master/tracking.js-master/leprechaunhat_kisspng.png). Save the image to the root folder of our website. By appending the following code to the end above the `</ht`ml>, we should be able to view the image in our example website after save and reload.

```
<body>
  <img id = "hat" class = "leprechaunhat" src = "./leprechaunhat_kisspng.png" >
</body>
```

![Image](https://cdn-media-1.freecodecamp.org/images/FDncTXccdZYyRY8TG3fF1jaCjtMHsI9WyQEa)
_Hat Image Appended to the Bottom of the Website_

Now we have to design a drop animation with CSS, and put the code above the hat declaration. The code basically allows the hat to drop down and then shake a little bit.

```html
<style>
 @keyframes shake {
  0% {
   transform : translateY(-30px);
  }
  40% {
   transform : rotate(10deg);
  }
  60% {
   transform : rotate(-10deg);
  }
  80% {
   transform : rotate(10deg);
  }
  100% {
   transform : rotate(0deg);
  }
 }
 .leprechaunhat {
  animation : shake 1s ease-in;
 }
</style>
```

![Image](https://cdn-media-1.freecodecamp.org/images/niLdZDtnM566OnXKvebFQ-kC96UrllOgVuQv)
_Hat drop animation._

### 3. Drop hats onto portraits

Now we will go over dropping hats precisely onto portraits. First we have to reference the JavaScript files from “tracking.js” with the following code.

```html
<script src = "build/tracking-min.js" type = "text/javascript" ></script>
<script src = "build/data/face-min.js" type = "text/javascript" ></script>
```

The code provides us a `Tracker` class which we can feed images into. Then we can listen for a response indicating a rectangle outlining the faces inside the image.

![Image](https://cdn-media-1.freecodecamp.org/images/19eUYAEHlwvb6ycxU58Xv1ZnIWQoV--GvHDZ)
_Tracker Explained_

We start by defining a function that executes when the page is loaded. This function can be attached to anywhere else if necessary. The `yOffsetValue` is an offset aligning the hat into a more appropriate position.

```js
const yOffsetValue = 10;
window.onload = function() {
};
```

Inside, we define our hat creation function, allowing it to create hats with arbitrary sizes and positions.

```js
function placeHat(x, y, w, h, image, count) {
 hats[count] = hat.cloneNode(true);
 hats[count].style.display = "inline";
 hats[count].style.position = "absolute";
 hats[count].style.left = x + "px";
 hats[count].style.top = y + "px";
 hats[count].style.width = w + "px";
 hats[count].style.height = h + "px";
 image.parentNode.parentNode.appendChild(hats[count]);
}
```

We should also twist our image declaration script a little bit to make it hide the image, as we are now showing it with JavaScript.

```html
<img id = "hat" class = "leprechaunhat" src = "./leprechaunhat_kisspng.png" style = "display : none" >
```

Then we add the following code to create the hats on top of faces, with the size matching the face.

```js
var hat = document.getElementById("hat");
var images = document.getElementsByTagName('img');
var trackers = [];
var hats = [];
for(i = 0; i < images.length; i++)
{
 (function(img)
 {
  trackers[i] = new tracking.ObjectTracker('face');
  tracking.track(img, trackers[i]);
  trackers[i].on('track', function(event) {
   event.data.forEach(function(rect) {
    var bcr = img.getBoundingClientRect();
    placeHat(rect.x, rect.y + yOffsetValue - rect.height, rect.width, rect.height, img, i);
   });
  });
 })(images[i]);
}
```

Now, while our Python server is still running, calling the following address should show us leprechaun hats dropping onto portraits.

```
http://localhost:8000/TEAM%20MEMBERS%20_%20Teamwebsite.html
```

![Image](https://cdn-media-1.freecodecamp.org/images/3lHrFCf6hT-qFaANYfSA7kyK9KzSS9BYG-N8)
_Leprechaun hat drop demo_

Congratulations! You just learned how to drop leprechaun hats onto all the portraits on a website with computer vision. Wish you, your friends, and your audiences a great St. Patricks Day!!!

### In the end

I have linked some of previous guides below on similar projects. I believe there are certain trends in front end design. Despite the newly emerging .js frameworks and ES updates, Computer Animations and Artificial Intelligence can do wonders in the future for front end, improving user experience with elegancy and efficiency.

**Beginner:**

* [how to fill your website with lovely VALENTINES HEARTS](https://medium.com/front-end-weekly/how-to-fill-your-website-with-lovely-valentines-hearts-d30fe66d58eb)
* [how to add some FIREWORKS to your website](https://medium.com/front-end-weekly/how-to-add-some-fireworks-to-your-website-18b594b06cca)
* [how to add some BUBBLES to your website](https://medium.com/front-end-weekly/how-to-add-some-bubbles-to-your-website-8c51b8b72944)

**Advanced:**

* [how to create beautiful LANTERNS that ARRANGE THEMSELVES into words](https://medium.freecodecamp.org/how-to-create-beautiful-lanterns-that-arrange-themselves-into-words-da01ae98238)

I am passionate about coding and would love to learn new stuff. I believe knowledge can make the world a better place and therefore am self-motivated to share. Let me know if you are interested in reading anything in particular.

If you are looking for the source code of this project, they can be found [**here**](https://github.com/shenhuang/shenhuang.github.io/tree/master/tracking.js-master). Thanks again for my teammates who allowed me to use their portraits for this project and **be wary before using this on a website with a Chinese user base**.

