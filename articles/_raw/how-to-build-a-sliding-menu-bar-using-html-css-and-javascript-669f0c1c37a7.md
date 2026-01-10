---
title: How to build a sliding menu bar using HTML, CSS and JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-18T17:15:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-sliding-menu-bar-using-html-css-and-javascript-669f0c1c37a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*x_Hcn2GhZZoiwhWBSnVGTA.jpeg
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Supriya Shashivasan

  A menu is what you look for when you land at a website. It has options and gives
  you access to everything the website has to offer you. You would definitely say
  it is an important part of a website, right?

  My friend Girish pati...'
---

By Supriya Shashivasan

A menu is what you look for when you land at a website. It has options and gives you access to everything the website has to offer you. You would definitely say it is an important part of a website, right?

My friend [Girish patil](https://www.freecodecamp.org/news/how-to-build-a-sliding-menu-bar-using-html-css-and-javascript-669f0c1c37a7/undefined) and I started a biweekly newsletter for fronted developers this month. The first newsletter features sliding menu bars, and so here I am writing about how we built it.

Before we begin, get a container in place for your whole webpage and design the width and height according to your requirements. Now, inside the container, you have to place a sliding menu. In this article, we’ll explain how to create a left sliding menu.

### Let’s get started

![Image](https://cdn-media-1.freecodecamp.org/images/1*1Jjz_X5KuI7U3Qs-lyKFSw.gif)
_Inspiration !!!! ;)_

The HTML code for the slider is given below. It is a basic bare version.

```
<div class="slider-container">
```

```
<a href="#" class="slider-trigger">   Click here   </a>
```

```
<div class="slider-parent">    <h1>Slider</h1>    <a href="https:/twitter.com/giyaletter">Twitter&lt;/a> <br>    &lt;a href="https:/twitter.com/s_omeal">@Supriya</a> <br>    <a href="https:/twitter.com/g__patil">@Girish</a> <br>   </div>
```

```
</div>
```

An **anchor tag** is used to open the menu when clicked on. This is what triggers the menu to open, so you can see why it’s called **slider-trigger**. The menu component is what lies in the **slider-parent** class.

Now design the menu bar in CSS. Pay attention to the design details.

```
.slider-container {  position: relative; }  .slider-container .slider-parent {    height: 70vh;    max-width: 250px;    width: 100%;    background: #6C7A89;    position: absolute;    left: -250px;    top: 50px;    visibility: hidden;    opacity: 0;    pointer-events: none;    transition: .2s all linear; }   .slider-container .slider-parent.active {      visibility: visible;      pointer-events: inherit;      transition: .2s all ease-in-out;      opacity: 1;      left: 0; }
```

Let’s now break down the above snippet and discuss how it works.

**Maxwidth** defines the maximum width up to which the div can occupy. In a smaller window, it can occupy less that 250px. The div occupies 250px when the window is stretched all the way out on the screen.

At times, the user might look at the website on a much smaller screen, so we want our div to resize accordingly.

Moving on, let’s look at why **left : -250px?** This is done to get that smooth sliding action for the menu. Notice that the value for left is negative, which tells us that the menu starts 250px to the left of the starting position (which is 0). So it is presently not in the visible area.

We don’t want the sliding menu to be seen at all, which is why we add **opacity** and make its **visibility hidden**. Everybody likes animation, and it gives an interesting visual feel. This animation can be done using the **transition** component.

#### YAYYY! The basic slider is done!

![Image](https://cdn-media-1.freecodecamp.org/images/1*UJtn-JxIMOnn6D6jLGqFgw.gif)
_I am sure you will dance better :P_

Now that the basic slider is done, let’s understand what happens when the slider bar is active — that is, when the anchor tag that opens the menu bar is clicked.

Focus on the **active** class in the CSS code given above. Notice that the values for **opacity** and visibility are changed. This change is made to make the slider (which was previously hidden) visible on the screen.

Also, you might wonder: why is it now **left : 0?** Previously, the slider was out of the screen. Now that we want the menu to start at the left side of the screen, we change the value of left to 0.

OH! The animation! Add the **transition** component again so that when the slider is active, it eases in from the left smoothly.

It’s done! You have designed the components, so what is the next step? JavaScript! It’ll put all this into action.

### Adding some JavaScript

```
var sliderTrigger = document.getElementsByClassName("slider-trigger")[0];var slider = document.getElementsByClassName('slider-parent')[0];
```

```
sliderTrigger.addEventListener( "click" , function(el){
```

```
if(slider.classList.contains("active")){  slider.classList.remove("active"); }else{  slider.classList.add("active"); }
```

```
});
```

Let’s look into how JavaScript wraps everything and gets the slider working. We want the slider to open when the anchor tag **slider-trigger** is clicked. So we get that element into a variable **sliderTrigger_._** Later on we get the whole slider element into the variable **slider**. Now, we add an event listener that implements a function when the **sliderTrigger** element is clicked.

```
sliderTrigger.addEventListener( "click" , function(el) {} );
```

The function that is written controls the mechanics of opening and closing the sliding menu bar. Remember that we had an active and a normal **slider-parent** class.

The hack we implement here is to add the active class when the **sliderTrigger** element is clicked, and remove the active class when the same element is clicked again. To do that we use the code given below, to check if the variable contains the class active.

```
slider.classList.contains("active")
```

If the value is true, we remove the class active from the list. What happens then? The sliding menu bar closes. If the value is false, we add the class active to the classlist. Now what happens? Yes, the sliding menu bar is displayed. It is that simple.

```
slider.classList.add("active")
```

```
slider.classList.remove("active")
```

### Voilà it’s done!! Look who is clapping ;)

![Image](https://cdn-media-1.freecodecamp.org/images/1*FPKDw_SRNiaOfjL1fPBBRg.gif)

The working of the same code is shown below in the CodePen.

While this is a basic example, I’m sending out examples of more complex and different types of sliding menu bars in my newsletter.

[Github repo of Giyaletter](https://github.com/girishpatil/giya)

Twitter handle: [Supriya S](https://twitter.com/s_omeal) and [Girish Patil](https://twitter.com/theevilhead)

Thank you. Happy coding :)

Check out products by us:

[paybackhub.com](http://paybackhub.com) and [certhive.com](http://certhive.com)

