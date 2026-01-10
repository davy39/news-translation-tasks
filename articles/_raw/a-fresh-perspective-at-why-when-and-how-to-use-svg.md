---
title: 'Why You Should Use SVG Images: How to Animate Your SVGs and Make Them Lightning
  Fast'
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2019-11-26T14:51:07.000Z'
originalURL: https://freecodecamp.org/news/a-fresh-perspective-at-why-when-and-how-to-use-svg
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/svg.png
tags:
- name: 100Days100Projects
  slug: 100days100projects
- name: Design
  slug: design
- name: SVG
  slug: svg
seo_title: null
seo_desc: 'Why Are We Using SVG?

  The web development sector is growing at a rapid pace, and SVG (scalable vector
  graphics) images are becoming more popular. As vector images, SVGs are composed
  of mathematical equations that define the positioning and color of l...'
---

## **Why Are We Using SVG?**

The web development sector is growing at a rapid pace, and SVG (scalable vector graphics) images are becoming more popular. As vector images, SVGs are composed of mathematical equations that define the positioning and color of lines and curves which make up graphic shapes and text in XML format. SVGs are used for icons, logos, graphic designs, and fonts.

Using SVGs is an easy choice once you consider the advantages they offer. For a client, you get superb quality on any device. For us as developers, there are even more reasons to use SVG. 

Let's discuss some of the benefits of SVG now.

### **1. Text-based format**

SVG elements contain text, which greatly improves the accessibility of a website. But the main advantage is that this text is indexed by search engines. And a user can find an SVG file via Google.

### **2. Scalability**

The quality of SVG images does not depend on the resolution. Unlike images of other formats or icon fonts, SVGs look perfectly sharp on any device with any screen size. Scalability also means that if you use the same image throughout the website but in different sizes, you use a single SVG. You do not have to create multiple copies of it as in the case of PNG. Instead, you embed the same image and define the size of it directly in SVG code.

![Scalability](https://images.ctfassets.net/6xhdtf1foerq/u6zLw9HQVb8DpDR1rhvHp/a5e491c95b5261e47e1c28098b2a2422/Copy_of_2.7_billion_people_use_smartphones__1_-min.png?fm=png&q=85&w=1000)

### **3. High performance**

If you prioritize performance, you should use SVG. With SVG, there is no need for an HTTP request to load in an image file. The page loads faster as it has no files to download. Faster loading time translates into better webpage performance and higher search engine ranking. In turn, it improves user experience.

### **4. Small file size**

The size of simple SVG files is defined by the colors, layers, gradients, effects, and masks that it contains. The size of a PNG or any other raster graphics file is defined by the number of pixels that it consists of. The larger a PNG image is, the heavier it gets in size. This is not the case for SVG icons, though. Also, SVGs can be optimized, and I will tell how later in this article.

![SVG file size](https://images.ctfassets.net/6xhdtf1foerq/6TEDo4rR558facWlrHZjlT/ab71bf067cf14098d65c602eac3d5735/Copy_of_2.7_billion_people_use_smartphones__2_-min.png?fm=png&q=85&w=1000)

### **5. Numerous editing and animating opportunities**

Unlike raster images, vector images can be edited both in special vector drawing programs and directly in a text editor. You can also edit colors or sizes of SVG icons directly via CSS. As for animating SVGs, it can be done with the help of SMIL, Web Animations API, ​WebGL, or CSS animation. Scroll down to learn more about CSS animation of SVG images.

### **6. Integration with HTML, XHTML, and CSS**

SVG was designed “to integrate with and extend other prominent open Web platform technologies, such as X/HTML, CSS, and Javascript”, according to [<ins>W3C</ins>](https://dev.w3.org/SVG/proposals/svg-html/svg-html-proposal.html). So, unlike different image formats, this format can be easily integrated with other documents and technologies.

### **7. W3C Document Object Model support**

There is growing community support for SVG. The [<ins>World Wide Web Consortium</ins>](https://www.w3.org/) (W3C) has always claimed that the Internet cannot do without vector images. This organization basically [<ins>created the SVG format</ins>](https://www.w3.org/2002/04/svg11-pressrelease), and they actively support it nowadays.

## **What Are the Inconveniences of SVG?**

The large number of small parts makes the use of the SVG format irrational. The more parts an image consists of, the heavier it grows in size.

For example, [<ins>here</ins>](https://www.amcharts.com/svg-maps/?map=usa) are two SVG maps of the United States. The second one is slightly more detailed than the first one. But the higher level of detail cost almost a fivefold increase in file size – 33 KB compared to 147 KB. If this map was not monochromatic, the increase would be much greater.

![SVG maps](https://images.ctfassets.net/6xhdtf1foerq/4xg76fiYHZzxpSxDXW9uFp/4f5161cd3efc5dd2ea0d9578388498f0/Copy_of_2.7_billion_people_use_smartphones__3_-min.png?fm=png&q=85&w=1000)

If the picture is linear and contains a few colors – SVG is a solution. However, if the details matter and there are a lot of them, PNG or JPEG may be more suitable.

Also note that SVG cannot be used for photographs. If you use a photograph on your website, SVG is not the best option. You definitely should go with a raster image format.

## **How to Optimize SVG Images**

When rendering a vector format, we have to write some extra SVG code. The end result should be optimized using different services. Most often, for optimizing SVG, I use a <ins>[Node.js](https://keenethics.com/services-web-development-node)</ins> tool [<ins>SVGO</ins>](https://github.com/svg/svgo). It is quite easy to use, and there is no need to upload the images to other websites.

![Example of SVG optimization using SVGO](https://images.ctfassets.net/6xhdtf1foerq/7m9UpCpPW7GNLR9tXAvTca/4c804519c3dd110b650977f72785453a/0_8YcO63_4ajXq0qEb.)
_Example of SVG optimization using SVGO_

## **How to Animate SVG**

SVG graphics on the web can be animated in a number of ways:

1. SMIL, which is the native SVG animation specification
2. Web Animations API, which is a native JavaScript API allowing you to create more complex sequential animations without loading any external scripts
3. ​WebGL
4. CSS animation

Let’s consider the last one.

**CSS animation** is used in order to avoid overloading your service with big libraries for animating icons and loaders.

To see the example of SVG check the [<ins>animated yolk</ins>](http://jsfiddle.net/yd3c81bg/9/embedded/html,css,result), the graphic design of which was initially drawn in Sketch.

![SVG gif](https://images.ctfassets.net/6xhdtf1foerq/7JTBd4pwJJwKYmqgTSwScv/525b6d4e42c53c35961706390802bc5e/ezgif.com-crop.gif)

As you can see here, I use Keyframe Animation Syntax for animation. It is implemented by setting the initial position of an element by id (0%), transition (50%) and final position (100%). To achieve smooth animation, initial and final values are equal.

Here are some **benefits** of using the CSS approach to SVG animation:

1. You do not need an external library.
2. Preprocessors (like Sass or Less) allow you to create variables.
3. You can use onAnimationEnd and some other animation hooks with native JavaScript.
4. This approach is easy to use for responsive web design development because you can modify your animation with media queries.

The **downsides** of using CSS animation are the following:

1. You cannot produce some complex physics effects, which would make the animation more realistic.
2. A lot of recalculation needs to be done if you adjust timing.
3. CSS and SVG graphics on mobile sometimes require strange hacks.

## **For Example**

Still, we can make some interesting projects with the help of simple and trivial CSS animation. For example, I have made a simple game-video using HTML, CSS, and a little bit of JavaScript. All the SVGs were drawn in Sketch. The objective of this game is to save the princess. In any situation, just click. You can find the project at my [<ins>GitHub</ins>](https://github.com/maryna-yanul/duck-the-princess/).

## **To Wrap Up**

SVGs are a great image format to go with. They are scalable, lightweight, text-based, and efficient. They are easy to edit, animate, and integrate. Importantly, they are supported by almost any browser except Internet Explorer 8 and Android 2.3.

While learning to work with scalable vector graphics images may take you some time, it is an investment that will pay off considering the benefits of SVG.

## Do you have an idea for a software project?

My company KeenEthics is a team of experienced [web application developers](https://keenethics.com/services-web-development). In case you need a free estimate of a similar project, feel free to [get in touch](https://keenethics.com/contacts?activeForm=estimate)_._

You can read more of similar articles on my Keen Blog. Allow me to suggest you read [The Value of User Testing](https://keenethics.com/blog/the-value-of-user-testing) or [7 Cases When You Should Not Use Docker](https://www.freecodecamp.org/news/7-cases-when-not-to-use-docker/). 

## P.S.

Also, I would like to say "thank you" to [Maryna Yanul](https://www.linkedin.com/in/yanul/) for coauthoring this article as well as the readers for making it to the end!

The original article posted on KeenEthics blog can be found here: [A Fresh Perspective at Why, When, and How to Use SVG](https://keenethics.com/blog/1478674800000-svg-animation-scalable-vector-graphics).

