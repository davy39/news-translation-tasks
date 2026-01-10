---
title: How to Translate jQuery Code Into Vanilla JS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:15:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-translate-jquery-code-into-vanilla-js
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa7740569d1a4ca26e2.jpg
tags:
- name: JavaScript
  slug: javascript
- name: jQuery
  slug: jquery
- name: js
  slug: js
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'jQuery was once one of the most popular JS libraries available. It solved
  a lot of problems, like making DOM manipulation and Ajax calls standard across all
  the different browsers, which all handled JavaScript slightly differently.

  A lot of jQuery''s ...'
---

jQuery was once one of the most popular JS libraries available. It solved a lot of problems, like making DOM manipulation and Ajax calls standard across all the different browsers, which all handled JavaScript slightly differently.

A lot of jQuery's once cutting edge features have made it into vanilla JavaScript, so there's no need to load an entire library for just a few functionalities. Given this, it's not uncommon that one of your tasks on the job will be to rewrite jQuery into vanilla JavaScript.

### How to rewrite jQuery into vanilla JS

Imagine you have the following code:

```html
<div class="m1 menu">
    <div id="menu-center">
        <ul>
            <li><a class="active" href="#home">Home</a>

            </li>
            <li><a href="#portfolio">Portfolio</a>

            </li>
            <li><a href="#about">About</a>

            </li>
            <li><a href="#contact">Contact</a>

            </li>
        </ul>
    </div>
</div>
<div id="home"></div>
<div id="portfolio"></div>
<div id="about"></div>
<div id="contact"></div>
```

```css
body, html {
    margin: 0;
    padding: 0;
    height: 100%;
    width: 100%;
}
.menu {
    width: 100%;
    height: 75px;
    background-color: rgba(0, 0, 0, 1);
    position: fixed;
    background-color:rgba(4, 180, 49, 0.6);
    -webkit-transition: all 0.3s ease;
    -moz-transition: all 0.3s ease;
    -o-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
.light-menu {
    width: 100%;
    height: 75px;
    background-color: rgba(255, 255, 255, 1);
    position: fixed;
    background-color:rgba(4, 180, 49, 0.6);
    -webkit-transition: all 0.3s ease;
    -moz-transition: all 0.3s ease;
    -o-transition: all 0.3s ease;
    transition: all 0.3s ease;
}
#menu-center {
    width: 980px;
    height: 75px;
    margin: 0 auto;
}
#menu-center ul {
    margin: 15px 0 0 0;
}
#menu-center ul li {
    list-style: none;
    margin: 0 30px 0 0;
    display: inline;
}
.active {
    font-family:'Droid Sans', serif;
    font-size: 14px;
    color: #fff;
    text-decoration: none;
    line-height: 50px;
}
a {
    font-family:'Droid Sans', serif;
    font-size: 14px;
    color: black;
    text-decoration: none;
    line-height: 50px;
}
#home {
    background-color: grey;
    height: 100%;
    width: 100%;
    overflow: hidden;
    background-image: url(images/home-bg2.png);
}
#portfolio {
    background-image: url(images/portfolio-bg.png);
    height: 100%;
    width: 100%;
}
#about {
    background-color: blue;
    height: 100%;
    width: 100%;
}
#contact {
    background-color: red;
    height: 100%;
    width: 100%;
}
```

```js
$(document).ready(function () {
    $(document).on("scroll", onScroll);
    
    //smoothscroll
    $('a[href^="#"]').on('click', function (e) {
        e.preventDefault();
        $(document).off("scroll");
        
        $('a').each(function () {
            $(this).removeClass('active');
        })
        $(this).addClass('active');
      
        var target = this.hash,
            menu = target;
        $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top+2
        }, 500, 'swing', function () {
            window.location.hash = target;
            $(document).on("scroll", onScroll);
        });
    });
});

function onScroll(event){
    var scrollPos = $(document).scrollTop();
    $('#menu-center a').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
            $('#menu-center ul li a').removeClass("active");
            currLink.addClass("active");
        }
        else{
            currLink.removeClass("active");
        }
    });
}
```

When you scroll down the page, the navbar should change colors as you get to different sections:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Peek-2020-05-25-18-44.gif)

The function that handles this is `onScroll`:

```js
function onScroll(event){
    var scrollPos = $(document).scrollTop();
    /* console.log(scrollPos); */
    $('#menu-center a').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
            $('#menu-center ul li a').removeClass("active");
            currLink.addClass("active");
        }
        else{
            currLink.removeClass("active");
        }
    });
}
```

To translate `onScroll` into vanilla JS, you have a few options.

### Option #1: Use an online compiler

You can use an online tool like Google's [Closure Compiler](https://closure-compiler.appspot.com/) to compress the code and strip out any unnecessary jQuery.

The problem is that you're still essentially left with jQuery code, so the browser would still need to load the library.

### Option #2: Manually translate the code

The best option is to check out resources like [You Don't Need jQuery](https://github.com/nefe/You-Dont-Need-jQuery) and [You Might Not Need jQuery](http://youmightnotneedjquery.com/) before rewriting your jQuery code. You'll be able to find the native JS versions of the most popular jQuery methods, some of which you can use in your own code.

Here's the `onScroll` function in vanilla JS:

```js
function onScroll(event) {
  var sections = [...document.querySelectorAll('#menu-center a')];
  var scrollPos = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop;
  sections.forEach(function(currLink) {
    var val = currLink.getAttribute('href');
    var refElement = document.querySelector(val);
    if (refElement.offsetTop <= scrollPos && (refElement.offsetTop + refElement.offsetHeight > scrollPos)) {
      //document.querySelector('#menu-center ul li a').classList.remove('active');
      currLink.classList.add('active');
    } else {
      currLink.classList.remove('active');
    }
  });
}

document.addEventListener('scroll', onScroll);
```


