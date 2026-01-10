---
title: MePage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-11-08T08:50:43.000Z'
originalURL: https://freecodecamp.org/news/mepage-8b10e260d73
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6z_QTQc5m385kAYhsjlt2w.jpeg
tags:
- name: CSS
  slug: css
- name: marketing
  slug: marketing
- name: portfolio
  slug: portfolio
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Divya Mistry

  A Single-page Destination on the Web

  After going through some front-end development tutorials on Free Code Camp, I decided
  to try my hands at this simple Zipline challenge of creating a portfolio page. I’ll
  refer to this single-page d...'
---

By Divya Mistry

#### A Single-page Destination on the Web

After going through some front-end development tutorials on [Free Code Camp](https://www.freecodecamp.org/news/mepage-8b10e260d73/undefined), I decided to try my hands at this simple [Zipline challenge](http://www.freecodecamp.com/challenges/zipline-build-a-personal-portfolio-webpage) of creating a portfolio page. I’ll refer to this single-page destination as a _MePage_ for the purpose of this post.

We’ll do this as a two-step process. First we’ll create a page using [CodePen](http://codepen.io/) to iterate our design and the code, and then optionally we’ll [push](https://help.github.com/articles/pushing-to-a-remote/) it to [Github Pages](https://pages.github.com) when we are satisfied with the results. Do keep in mind that all of this can be done independent of Codepen and Github Pages.

With that in mind, here we go.

### CodePen

![Image](https://cdn-media-1.freecodecamp.org/images/1*fjd-3vkg7STzTTAUM5DNqw.png)
_codepen.io Homepage_

CodePen provides an easy way to test your front-end development ideas. You can create a set of web pages to learn and/or show-off your web development skills there, and share it with the world. We’ll use it to build a single-page personal site (i.e. a _MePage_) where the visitor can learn about you, your social media presence, and get your contact information.

Step 1: Create a [+New Pen](http://codepen.io/pen/).

Step 2: In the HTML box, write the following. This shows the general structure of the MePage.

```
<body>  <!-- navigation bar -->  <!-- header text -->  <!-- social icons -->  <!-- inspirational quote -->  <!-- about me -->  <!-- contact me --></body>
```

Step 3: We’ll utilize Bootstrap for our site. Let’s include that for our use. Click on the gear icon on the top-left corner of the CSS block. In the CSS settings window, click on the Quick-add drop-down menu, and select Bootstrap.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o4wtaxwaN7_MdL2LUdjNZw.png)
_Add Bootstrap using Quick-add in CSS settings_

While we are at it, let’s also add jQuery and Bootstrap JavaScript libraries to help with interactivity of the menu based navbar. To do this, go to the JavaScript settings page, and Quick-add the jQuery and Bootstrap libraries.

Now we start filling in the various parts of the page.

Step 4: Let’s first create the navigation bar. We’ll utilize the Bootstrap’s [fixed-top navigation](http://getbootstrap.com/examples/navbar-fixed-top/) bar for this.

_Although not necessary, you can read the nitty-gritty details about Bootstrap navbar [here](http://getbootstrap.com/components/#navbar). This will help you customize the navbar later on._

* Create a <nav> element and a container <div> in the <body>. This is where the navbar contents will go.

```
<!-- navigation bar -->  <nav class="navbar navbar-default navbar-fixed-top">    <div class="container">      <!-- contents of navigation -->      <!-- Add the next bit of code here -->    </div>  </nav>
```

* We can also utilize the responsive design for navigation menu when the web page is being viewed on smaller screens. The following code will show the contents of navigation items in a collapsible menu on smaller screens. We’ll also show a Brand Name or a Logo as well. I have chosen to keep my own name as a brand name here.

```
<div class="navbar-header">  <button type="button" class="navbar-toggle collapsed"            data-toggle="collapse" data-target="#navbar"            aria-expanded="false" aria-controls="navbar">
```

```
    <!-- add the toggle button with 3 horizontal lines/bars -->    <span class="sr-only">Toggle navigation</span>    <span class="icon-bar"></span>    <span class="icon-bar"></span>    <span class="icon-bar"></span>  </button>  <a class="navbar-brand" href="#">Divya Mistry</a></div><!-- Add the next bit of code here -->
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*qKoRflAv-BX7nfxjkSjeiw.png)
_Navigation bar starting to shape up._

* Next we pick the navigation items for the navbar. For this exercise, we’ll create a _Home_ link to go jump to the default view, an _About_ link to jump to the “about me” section, and a _Contact_ link to jump to thecontact information. These could all be different pages; however, we’ll use the magic of in-page bookmarks and Bootstrap to keep everything in a single-page and jump around the relevant sections. Add the following code where indicated in the previous code chunk.

```
<div class="navbar-collapse collapse" id="navbar">  <!-- add items to the nav bar -->  <ul class="nav navbar-nav navbar-right">    <li><a href="#">Home</a></li>    <li><a href="#about-me">About</a></li>    <li><a href="#contact-me">Contact</a></li>  </ul></div><!-- Add the next bit of code here -->
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*VHDcqdUOcjNnh-u2cLIBrQ.png)
_Navigation bar ready._

We are done with the navigation bar now. You’ll notice that we have anchored the _About_ and _Contact_ links to #about-me and #contact-me references, but they do nothing if you click on the link. Let’s create those along with some basic structure of our page.

```
<div class="container">  <div class="row text-center">    <!-- header text -->    <!-- ADD the header text bit of code HERE -->    <!-- social icons -->    <!-- ADD the Social buttons bit of code HERE -->    <!-- inspirational quote -->    <!-- ADD the inspirational quote bit of code HERE -->  </div>  <div class="row text-center" id="about-me">    <!-- about me -->    <!-- ADD the About text bit of code HERE -->  </div>  <div class="row text-center" id="contact-me">    <!-- contact me -->    <!-- ADD the Contact text bit of code HERE -->  </div></div>
```

Let’s start filling in the various sections. Add the following lines of code where indicated with <!_-- ADD the … HERE -_-> comments in HTML code above.

* Header text

```
<div class="col-xs-12">  <!-- name title -->  <h1>Divya Mistry</h1>  <h4>I *will* bioinformatics you</h1>  <hr></div>
```

* Social icons

```
<div class="col-xs-12">  <!-- social buttons -->  <a class="btn btn-default" href="https://twitter.com/divyamistry" target="_blank">Twitter</a>  <a class="btn btn-default" href="https://linkedin.com/in/divyamistry" target="_blank">LinkedIn</a>  <a class="btn btn-default" href="https://github.com/divyamistry" target="_blank">Github</a></div>
```

* Inspirational quote

```
<div class="col-xs-12">  <blockquote class="blockquote-reverse my-quote">    <p>The fool doth think he is wise, but the wise man knows himself to be a fool.</p>    <footer>William Shakespeare in <cite title="India">As You Like It</cite></footer>  </blockquote></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*vDRQEOqSDYC9NhmgYlGdZw.png)
_Content of the main page section._

You’ll notice that a part of the title is cutoff, and the quote doesn’t look quite prominent or aligned. We’ll fix that in a minute. Let’s continue adding the details to remaining sections of the page.

* About me section. We’ll add a description on left side, and a photograph on the right.

```
<div class="col-xs-6"> <!-- About me - description -->  <p class="lead">Consumer and Producer of Sciencey S#!t.</p>  <p>I am a student of Bioinformatics and Computational Biology. I like making science easier to use and understand. When I'm not in lab/office, I am at home listening to Bollywood tunes.</p></div><div class="col-xs-6"> <!-- About me - photo -->  <img class="img-rounded" height="250px" alt="Divya's face" src="https://lh3.googleusercontent.com/kQABk1XZ1HLRrtfkZA9tZH8WDmLgDqWIG44v-IVASL65N1hWX30"></div>
```

* Contact me

```
<div class="col-xs-6"> <!-- contact me photo -->  <img class="img-rounded" src="https://openclipart.org/image/150px/svg_to_png/98293/1290715998.png" alt="Contact Me"></div><div class="col-xs-6"> <!-- contact me text -->  <address>    <strong>Divya Mistry</strong><br>    My Street Address<br>    Unit 001<br>    Ames, IA 50011<br>    <abbr title="Phone number">515-555-0144</abbr>  </address></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*hwSjqh2su5swE8sduMLk7A.png)
_All the content added. We still need to fix the spacing._

* Footer. _Ah! I leave this for your exercise. Try to read the Bootstrap documentation and create your own footer. Here’s one idea: add a simple_ <d_iv> element and provide your own copyright_ note.

Step 5: Let’s modify the spacing and some look-and-feel to make the page look cleaner. We’ll jump into the CSS now.

* Lower the body such that the contents are not hidden behind the navigation bar. Bootstrap [recommends around 70px](http://getbootstrap.com/components/#navbar-fixed-top) for this. I like using the [em](https://en.wikipedia.org/wiki/Em_%28typography%29) units for [various reasons](http://www.w3.org/Style/Examples/007/units.en.html#font-size).

```
/* Lower the main text below the navigation bar */body { padding-top: 3em; }
```

* Right now, all the sections are too close together. Let’s separate them to give plenty of spacing in between. You can play around with this padding to your liking. I prefer around a typical laptop screen vertical size of 768px.

```
/* each row should be a big screen in itself */.row { height: 768px; }
```

* Let’s make the Shakespeare quote a lot more prominent on the screen.

```
/* Spacing above quote */.my-quote { margin-top: 5em; }
```

```
/* Quote text font, size, and color */.my-quote>p {   font-family: "Lora", serif;   font-size: 3em;   color: #aaa;}
```

```
/* Quote attribution font size and color */.my-quote>footer { font-size: 1em; color: #bbb; }
```

You’ll notice that I have chosen the [Lora](https://www.google.com/fonts/specimen/Lora) font-family for my quote. This font is available via Google Fonts. To use it, all you have to do is go to your HTML settings (click on the gear icon on top-left corner of the HTML editor), and add the following line in the **Stuff for <he**ad> text box.

```
<link href='https://fonts.googleapis.com/css?family=Lora:400italic' rel='stylesheet' type='text/css'>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*uNnc8LmFoEwkVtP005lDmQ.png)
_Adding Google Fonts stylesheet to &lt;head&gt;._

* Finally, let’s give both information sections some padding space at the top so that when we jump to them, the navigation bar does not hide the content.

```
/* for each of the sections of the page */#about-me { padding-top: 6em; }#contact-me { padding-top: 6em; }
```

_Note that this padding is necessary in spite of the padding of the <body> element, because the in-line bookmark anchors are referenced to the top of the browser window view port where <body> starts, and not relative to where the content inside the body sec_tion starts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-o-kQB6Nr13Ha-yKJgiROg.png)
_CSS updated to correct the spacing and alignments._

Step 6: Make any CSS modifications you would like for the footer. I decided to present a slightly smaller text.

Here is my [resulting CodePen](http://codepen.io/anon/pen/wKYqMW) based on this exercise. You can add background images to the body and all the sections to give it a [nice visual effect](http://codepen.io/ThiagoFerreir4/full/eNMxEp).

### Github Pages

![Image](https://cdn-media-1.freecodecamp.org/images/1*UP16Y8izJ8IASnBfd-ZG-g.png)

Github provides a great way to [host static pages](https://pages.github.com/) for yourself and for your projects. I decided to create a [Github user Page](http://divyamistry.github.io/) using the results of this exercise. The code is available in [this repository](https://github.com/divyamistry/divyamistry.github.io). Feel free to fork the repository.

_There are several good tutorials to teach you how Github works. If you are unfamiliar with [git](https://www.atlassian.com/git/) and [Github](https://try.github.io/levels/1/challenges/1), give them a go. It’s a skill worth learning._

![Image](https://cdn-media-1.freecodecamp.org/images/1*eAdEAIWlpYgrfTXUuaOqIg.png)
_My Github Page using this tutorial._

### Final words

Hope you liked this exercise, and were able to make your own MePage. Comment here with your CodePen or Github URL to show your results. If you ended up modifying this, and made your own version of an awesome MePage, please share that too. I would love to see that. And finally, if you want to stay in touch, [@divyamistry](https://twitter.com/divyamistry) is a great way to holler.

