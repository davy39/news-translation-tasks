---
title: Common Causes of Invalid HTML Syntax – and How to Fix Them
subtitle: ''
author: Christine Belzie
co_authors: []
series: null
date: '2023-04-18T16:51:50.000Z'
originalURL: https://freecodecamp.org/news/invalid-html-syntax-examples-and-fixes
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Blog-post-cover-for-FCC---2-Revised-.png
tags:
- name: coding
  slug: coding
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "Remember those treehouses that we had as children and how the wood would\
  \ wear, tear, and eventually collapse because we just would not stop jumping around\
  \ inside it?  \nWell that's kind of like HTML. This markup language is like the\
  \ wood to your codin..."
---

Remember those treehouses that we had as children and how the wood would wear, tear, and eventually collapse because we just would not stop jumping around inside it?  

Well that's kind of like HTML. This markup language is like the wood to your coding project. If it’s invalid, your solution will collapse. 

Now don’t fret. In this article, I'll give you some tips to help you make sure that your HTML is error-free as you build your coding solution.

![Dwight from the Office is getting ready to code ](https://www.freecodecamp.org/news/content/images/2023/04/dwight.gif)
_You heard Dwight. Let's do this! :)_

## Common Causes of Invalid HTML Syntax

Before you go and start investigating for unclean code like Sherlock Holmes (the [Benedict Cumberbatch version](https://www.imdb.com/title/tt1475582/) to be exact 😉), let’s briefly meet some examples of syntax that can ruin your HTML file:

1. Improper nesting of HTML elements

![Screenshot of a code snippet zooming in on the line <b></b> ](https://www.freecodecamp.org/news/content/images/2023/04/example-of-improper-nesting-tag.jpeg)
_"HUH?" indeed_

2.  Deprecated HTML tags 

![Screenshot pointing to the <center> tag, a deprecated HTML element from the Google search's code. ](https://www.freecodecamp.org/news/content/images/2023/04/deprecated-HTML.jpg)
_Interesting choice 😏_

3.   Missing tags 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/missing-html-tag.png)
_Oh closing tag, where are you?_

Now that you've met the culprits, let’s figure out how to catch them before they mess up your HTML file and destroy your coding project.   


![Young Alfred from "Gotham" saying "Let's do this"](https://www.freecodecamp.org/news/content/images/2023/04/alfred-3.gif)
_Sir yes sir!_

###   
Improper Nesting of HTML Elements 

To briefly review, nesting occurs when an HTML element is inside another HTML element.

```html
<p>Coded by <a class="profile-link" href="<https://github.com/CBID2>" target="_blank"><em>Christine Belzie</em></a></p>

```

Now a nested element becomes evil – I mean improperly nested – when you place an HTML element inside the wrong area of the other element, like this:

```html
<a class="profile-link" href="<https://github.com/CBID2>" target="_blank"><em>Christine Belzie<p>Coded by </p></em></a>

```

The code above would be considered invalid because the <p> tag is not related to the <a> tag and the <p> tag is not related to <em> tag. As a result, you get an unorganized paragraph.

%[https://codepen.io/CB_ID2/pen/WNawGVw]

To replace the improperly nested element, I highly recommend doing what I like to call the Sandwich Model. It entails stacking the head and closing tags of styling HTML elements within the primary tags, kind of like how you stack up all your toppings and fillings between two slices of your favorite bread.

```html
<bread> <topping> </topping> <filling> </filling> </bread>
```

Now if you think improperly nested tags were evil, wait until you see the next villain.

![Daughter from "Bob's Burgers" gives an evil laugh while flames erupt in the background](https://www.freecodecamp.org/news/content/images/2023/04/evil-laugh.gif)
_Muahaha! 😈_

### Deprecated HTML Tags

Simply put, deprecated HTML tags are basically when you use HTML elements that the tech industry has decided should no longer be used. Here's an example:

```html
<center>
  <figcaption id="img-caption">Rihanna performs on stage in San Siro Stadium for Anti World Tour 2016. </figcaption>
</center>

```

In the code snippet above, I used the <center> tag, Now, will the code snippet above fulfill its task? Of course. See the output below:

%[https://codepen.io/CB_ID2/pen/LYgZXOE]

But it’s considered invalid since it is [no longer used](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/center), which can cause your project to not function in the best way possible. 

It’s like wearing like wearing platform shoes from the 70s when everyone else is wearing Yeezy’s, Sketchers, or Converse.

![Yellow platform shoes walking down the stairs](https://www.freecodecamp.org/news/content/images/2023/04/platform-shoes.gif)
_To quote Pauly D from "Jersey Shore", "What are those?!"_

The best way to fix deprecated HTML tags is to refer to websites, blogs, and other sources to stay updated on the latest versions of the code. Let’s give the snippet I mentioned a makeover:

```html
<figcaption id="img-caption">Rihanna performs on stage in San Siro Stadium for Anti World Tour 2016. </figcaption>

```

```css
figcaption{
	max-width:100%;
	  height: auto;
	display:flex;
	justify-content: center;
	 font-family: 'Montserrat', sans-serif;
	
  }

```

 To center the <figcaption> element, I used the CSS Flexbox method: "justify-content" and viola:

%[https://codepen.io/CB_ID2/pen/jOerQzK]

See how pretty the snippet looks now? When your code looks good, your project operates well, too. To stay updated on HTML, [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML), in my opinion, is a great source because they always let the readers know when certain tags are out of date.

Now hold on, we’re not out of the woods yet, there’s still one more invalid syntax that we have to meet.

![Ren from the "Ren and Stimpy Show" is sweating in fear](https://www.freecodecamp.org/news/content/images/2023/04/nervous.gif)
_Don't be scared...yet! 😈_

### Missing Closing Tags 

You know how you use to scoff and roll your eyes whenever your writing instructor took points from your essay for having a few misspelled words or a missing period? Well, they were on to something – because the same idea applies to your HTML file. 

A common issue you might run into is missing closing tags. Let's see what that looks like.

```html
<div class="user-info">
<h3 id="user-name">Victor Crest<span class="age">26</span></h3>


```

If one of your code lines is like the code snippet above, your HTML file will break, causing your project to not look so great like in the output below:

%[https://codepen.io/CB_ID2/pen/qBJNQQO]

 Think of it like a missing tire in your car (or whatever vehicle you use to transport yourself). Without it, you would be driving like this:

![Kramer from "Seinfeld" is driving an uncontrollable truck.](https://www.freecodecamp.org/news/content/images/2023/04/crazy-driving.gif)
_Hang in there buddy!_

To fix this error, I highly recommend using the sandwich method that I mentioned before. 

```html
<div class="user-info">
<h3 id="user-name">Victor Crest<span class="age">26</span></h3>
</div>

```

As you can see in the code above, we've added our closing `<div>` tag, causing the snippet to now look like this:

%[https://codepen.io/CB_ID2/pen/jOerQXv]

See how improved the code looks now? Remember, think of a line of code like a sandwich. When one slice of bread (or in this case, a closing tag) is missing, your masterpiece falls apart, leaving you angry, sad, and sometimes hungry. 

![A pudgy rubs its stomach in sadness while saying "I'M SO HUNGRY"](https://www.freecodecamp.org/news/content/images/2023/04/penguin.gif)
_So sorry penguin!_

## Wrapping Up

There you have it! Three common types of invalid syntax to look out for in your HTML file. 

Remember, this file is the foundation of your coding projects, so Happy HTML file = Happy project! 😊

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-131.png)
_Glad to know that we agree with each other._

### Credits

* Ben Mckenzie Fox GIF by [Gotham](https://giphy.com/gifs/gotham-fox-3o7abuqxszgO6pFb3i)
* Can't Touch This High Heels GIF by [BrownSugarApp](https://giphy.com/gifs/brownsugarapp-fashion-get-l3vR1JnogyxKm0SGs)
* Closing Tag image from "How to Easily Find Missing Closing Tags in HTML (with Coda 2)" article on [Clicks Nathan](https://clicknathan.com/web-design/easily-find-missing-closing-html-tag/)
* Dwight Office Tv GIF by [The Office](https://giphy.com/gifs/BpGWitbFZflfSUYuZ9)
* Driving Michael Richards GIF by [Seinfield GIFs](https://giphy.com/gifs/crazy-seinfeld-9NTfxeLPpgRUI)
* Fox Tv Fire GIF by [Bob's Burgers](https://giphy.com/gifs/bobs-burgers-fox-bobs-burgers-tv-3o72FfM5HJydzafgUE)
* Oh Yeah Yes GIF by [Mauro Gatti](https://giphy.com/gifs/cool-ok-sure-l41lUjUgLLwWrz20w)
* Ren And Stimpy Reaction GIF by [Giphy](https://giphy.com/gifs/scared-nervous-ren-and-stimpy-y9X0F8VgTkmU8)
* Sad Nft GIF by [Pudgy Penguins](https://media.giphy.com/media/MSqUXNDStq8V3Qc9OM/giphy.gif)
* Screenshot of Google from the  "Why does Google use the deprecated HTML tag still?"discussion forum on [Reddit](https://twitter.com/davedbase/status/1647012417841365001?s=46)
* Screenshot of improper nested tag from "How is the DOM Affected by Improperly Nested HTML Elements?" article by Louis Lazrus on [Impressive Webs](https://www.impressivewebs.com/dom-improperly-nested/)

