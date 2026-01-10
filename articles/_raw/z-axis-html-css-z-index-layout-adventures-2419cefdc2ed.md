---
title: 'HTML/CSS: Z-axis Adventures'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-04-05T20:17:29.000Z'
originalURL: https://freecodecamp.org/news/z-axis-html-css-z-index-layout-adventures-2419cefdc2ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4sV2vVFkeY-A9ZIZh_AUtw.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Daniel Robinson

  Let’s jump straight to exploration and adventure.

  We start with three circles: each is a div filled in with “█” characters (ink blotches),
  so we can study the ordering of a divs contents separate from backgrounds and borders.
  The s...'
---

By Daniel Robinson

Let’s jump straight to exploration and adventure.

We start with three circles: each is a div filled in with “█” characters (ink blotches), so we can study the ordering of a divs contents separate from backgrounds and borders. The starting HTML looks like:

```
<body> <div id=”one” class=”circle”> ██████<br/>██████<br/>██████<br/>██████<br/>██████ </div> <div id=”two” class=”circle”> ██████<br/>██████<br/>██████<br/>██████<br/>██████ </div> <div id=”three” class=”circle”> ██████<br/>██████<br/>██████<br/>██████<br/>██████ </div></body>
```

And the CSS:

```
.circle { width: 72px; height: 72px; overflow: hidden; line-height: 16px; border-radius: 100%; box-sizing: border-box;}
```

```
#one { margin-left: 27px; color: red;}
```

```
#two { margin-top: -36px; color: blue;}
```

```
#three { margin-top: -72px; margin-left: 56px; color: green;}
```

This HTML/CSS produces the first image above. Three circles overlapping in the order they were defined. Good. Let’s add some borders:

```
div {   border: 6px solid black;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/bpgUMIsMOCbHV4e2FSrl2IwwtqoKp4-i2rBk)
_Borders are at the back with the contents stacked in the front._

Perhaps this surprises you. The borders are behind even though the contents stay in front. Are the borders stacked as well? A touch of colour:

```
#two {  border-color: grey;}
```

```
#three {  border-color: white;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/KQgZWKWh3mXCB8gl2wV69W8kGMPqS08qmz4c)
_The border stack order is the same as the content stack order, but independent._

Yes, the order of divs in the HTML decides the order of the borders with respect to each other, and the contents with respect to each other, but the order between borders and contents is: borders go behind contents.

Here are plunkers for the examples so far: [start](https://plnkr.co/edit/osQgt6?p=preview), [black borders](https://plnkr.co/edit/THwgYG?p=preview), [colored borders](https://plnkr.co/edit/ZHSxBZ?p=preview).

So far, the three div’s have had the default type of positioning: static. Let’s “position” them (full code in the [plunker](https://plnkr.co/edit/REXUce?p=preview)):

```
div {   border: 6px solid black;   position: relative;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/9f-qY5FHhEEfEp6M8oxvDTkHclby8lZ8Bzj4)
_Just when you’d gotten your head around borders being ‘separate’?_

Ok, so ‘positioned’ elements (position value ≠ static) get stacked together: contents, borders and all. Next experiment! ([plunker](https://plnkr.co/edit/REXUce?p=preview)):

```
div {   border: 6px solid black;}
```

```
#one { position: relative; /* just position the first div */}
```

![Image](https://cdn-media-1.freecodecamp.org/images/yn6jdF08eBLiaIVPrlM70vEpFFKFNKDzDZgx)
_Red circle is ‘positioned’, the others are not. Positioned elements are the ‘highest’._

Right, so positioned elements go in front of un-positioned elements. Ordering solely based on layout properties has a number of cases. Here’s another ([plunker](https://plnkr.co/edit/vpp2zN?p=preview)):

```
#one { margin-left: 24px; color: red;}
```

```
#two { margin-top: -36px; margin-right: -20px; border-color: grey; color: blue; float: left;  /* the important part */}
```

```
#three { margin-top: -36px; border-color: white; color :green;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/jwcYwP4FX8mW-5TqgF4mVWvfHGAU9jK5vlQG)

Here, the blue circle has been floated left, the other two circles are un-positioned. Both div two’s border and its contents sit together between the other circles respective borders and contents. A floated element acts much like a positioned element, where it’s border and contents are positioned together, except it is not on top.

Let’s skip the content+border act for a moment and take a look at nested HTML. [This codepen](http://codepen.io/designerzone/pen/YXVwGm) jumps us forward nicely.

```
<div class=”black”></div><div class=”gray”>  <div class=”lime”></div> <div class=”yellow”></div> </div><div class=”blue”></div>
```

```
(The CSS solely set’s background colours, box sizes, and margins)
```

![Image](https://cdn-media-1.freecodecamp.org/images/21zKGf0Xt5T1vdRc89prt2pZvTlY8bheJVe2)

As one might expect, nested HTML creates stacking with respect to the parent element.

Let’s focus on the nested portion — reintroducing borders and contents, but also throw in backgrounds to the mix. I will explain the diagram below but see the [plunker](https://plnkr.co/edit/rbKxnq?p=preview) for the complete HTML/CSS:

![Image](https://cdn-media-1.freecodecamp.org/images/v4Zgb92swTz69uupPWM8F3Ghl-TZBUcqu9JK)

Our circle divs from before have become nested squares. The yellow is the background of the outer div, and the crimson on the bottom right is the background of the inner inner div (div three).

The second div has no background. Overflow is allowed. In a nested context with no-positioning, the borders are at the back in nest order.

We also see that the backgrounds are sent to the back with them and are also in nest order: the crimson is behind the blue but above the yellow.

The first line of green chars has been removed to show you this effect. If we add positioning to this, we get a similar effect as we did with the circles — all this border/background sinking goes away ([plunker](https://plnkr.co/edit/zChij4?p=preview)):

```
div {  position: relative;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/Kh4k0qpf4wWXzpm8P2m8by7I8SYlbHToB35r)

In a nested context with positioning, children go above parents: borders, backgrounds, contents and all.

If we combine all of the cases so far, we can generate most of the element ordering scenarios with just positions, floats & HTML structure. Well, that is, at least visually. What about when it comes to event capturing? Consider the following:

```
<div id="one"></div><div id="two"></div><div id="three"></div>
```

```
div {  /* all divs overlap 100% */  position: absolute;   top: 0;  bottom: 0;  left: 0;  right: 0;   background-color: white;}
```

```
#three {   background-color: lightblue;}
```

```
document.getElementById(‘one’)  .addEventListener(‘mouseover’,logTarget)
```

```
document.getElementById(‘two’)  .addEventListener(‘mouseover’,logTarget)
```

```
document.getElementById(‘three’)  .addEventListener(‘mouseover’,logTarget)
```

```
function logTarget(e){   console.log(e.target);}
```

If you move your mouse into the browser window, what _mouseover_ events do you expect will fire?

What about if we update the HTML like follows?

```
<div id="one">  <div id="two">   <div id="three"></div>  </div></div>
```

Yes. Exactly. With the in-series HTML you get one event. With the nested you get three*. Despite the fact that visually, the colored third div completely covers the other two divs in each case, for event capturing it doesn’t in the nested case. See the plunkers [here](https://plnkr.co/edit/Y7SMTtHqm2lga0to5g84?p=preview) and [here](https://plnkr.co/edit/Rvb0zaEvCCQO87BRdjeb?p=preview).

*Three events with a target of the third div — it’s still on top, so the mouseover event target applies to it.

So far we’ve explored the natural stacking order — the order purely as defined by HTML structure and standard layout properties such as position and float.

We’ve seen that for element contents floated < un-positioned < positioned. However un-positioned elements have their borders/backgrounds ordered right at the back, while floated and positioned elements bring theirs along for the ride. We’ve also considered ordering both visually and with respect to event capturing.

What about breaking out of the natural stacking order using z-index?

The CSS z-index property affects positioned elements. We have seen that positioned elements come to the front and bring along all their borders and backgrounds, but other than that they were ordered in the order they were defined in HTML. The z-index simply provides a way of breaking out of that HTML ordering context. So the obvious first example ([plunker](https://plnkr.co/edit/EPHDqI?p=preview)):

```
div { width: 80px; height: 80px; position: relative; line-height: 16px; box-sizing: border-box;}
```

```
#one { background-color: red; z-index: 1;}
```

```
#two { background-color: blue; top: -80px;}
```

```
<body>  <div id=”one”></div>  <div id=”two"></div></body>
```

![Image](https://cdn-media-1.freecodecamp.org/images/wowe4g8Y5H0GDN5lH9rOarha8KnGOqPH7FsN)
_We’d normally see the blue box since it was defined second, but the red one has a z-index of 1;_

Next, it is similar with the nested case, except you must apply a negative to the child element (we’ll take a look at why shortly) for the same ([plunker](https://plnkr.co/edit/UQmeiD?p=preview)):

```
.box { position: relative; width: 80px; height: 80px;}
```

```
#one { background-color: red;}
```

```
#two { background-color: blue; z-index: -1;} 
```

```
<div id="one" class="box">  <div id="two" class="box"></div></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/HwOiJR7sZH1l2TwRrDGvUuSmYmgkzf51vAXu)
_#two has been sunk behind #one_

If we add a z-index to the parent as well though:

```
#one { background-color: red;  z-index: 1;}
```

```
#two { background-color: blue; z-index: -1;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/MTxbJXh1a6ZHR-kn-CqQJgixV-TD2eA-SRBE)
_Erm huh?_

The child’s z-index is “ignored” in this case. This may become clearer with this example ([plunker](https://plnkr.co/edit/9WpdxB?p=preview)):

```
.box { position: absolute; width: 80px; height: 80px;}
```

```
#one { background-color: red; z-index: 2;}
```

```
#two { height: 60px; width: 60px; background-color: green; z-index: 1;}
```

```
#three {  background-color: blue;}
```

```
<div id=”one” class=”box”> <div id=”two” class=”box”></div> <div id=”three” class=”box”></div></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/XIKrwN3m-LxcLV6c7lqkQCNA1N2Fl5TKeasL)

The nesting with the use of the z-index creates a new stacking context. So #one is at ‘2’ with respect to it’s sibling elements, while #two & #three are at ‘1’ and ‘0’ respectively with respect to each other, inside #one.

This can cause confusion in situations like so ([plunker](https://plnkr.co/edit/e27KLU?p=preview)):

```
.box { position: absolute; width: 80px; height: 80px;}
```

```
#one { background-color: red; z-index: 2;}
```

```
#two { width: 100px; position: relative; z-index: 4;}
```

```
#three {  margin-top: 80px; background-color: blue; z-index: 2;}  <div id="one" class="box">  <div id="two" class="box">    Text inside two    Text inside two    Text inside two    Text inside two    Text inside two    Text inside two    Text inside two    Text inside two  </div></div><div id="three" class="box"></div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/4OYl73Te9hvQjp9oq6xnyM8wyOYUBaUDdRY1)

Despite the text inside two having a z-index of 4, it is still behind the blue square which has a z-index of 2. Why? Because it is a z-index of 4, inside a stacking context which has a z-index 0f 2. Then because the third div is defined after the first div and is at z-index 2 also, it goes on top. Of course, if we tweak it to have a z-index to 1 it goes underneath([plunker](https://plnkr.co/edit/3LsRJv?p=preview)):

```
#three {  margin-top: 80px; background-color: blue; z-index: 1;  /* was 2, now 1 */}
```

![Image](https://cdn-media-1.freecodecamp.org/images/v6LalxTUbug41Oj8PixY5ZtRAulZCBmoBkmm)

Z-index isn’t the only property to create a new context on the parent. Opacity is another :

```
#one { background-color: red; opacity: 0.99;}
```

```
#two { width: 100px; position: relative; z-index: 1;}
```

```
#three {  margin-top: 80px; background-color: blue;}
```

```
(same HTML as above)
```

![Image](https://cdn-media-1.freecodecamp.org/images/4Mj-28L8aqjJbzjk-Vv2wfpgb8ZFRpvc3jhK)

At this point, [http://philipwalton.com/articles/what-no-one-told-you-about-z-index/](http://philipwalton.com/articles/what-no-one-told-you-about-z-index/) should start to be quite clear.

[https://www.smashingmagazine.com/2009/09/the-z-index-css-property-a-comprehensive-look/](https://www.smashingmagazine.com/2009/09/the-z-index-css-property-a-comprehensive-look/) is also a good read.

Because there is such a massive interplay of rules going on, stack order can get a little unwieldy, but it is true what that first article says: the rules aren’t that hard to understand, they just aren’t necessarily what one might expect.

The creation of new stack contexts is something that a developer must work with to get the desired outcome in vertical stacking situations.

I hope you’ve had an adventure scrolling up and down the layers of this article.

