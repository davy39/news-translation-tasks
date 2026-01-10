---
title: Introducing WebSlides
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-09T10:28:22.000Z'
originalURL: https://freecodecamp.org/news/introducing-webslides-fa7a9e37ff97
coverImage: https://cdn-media-1.freecodecamp.org/images/1*v1zc80z1gh6n9eKrDNZF9A.png
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: open source
  slug: open-source
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By José Luis Antúnez

  Everyone loves stories. People share content that makes them feel inspired. We need
  stories to know we’re not alone.

  Slide decks are an excellent way to tell these stories. And there are already plenty
  of great tools out there fo...'
---

By José Luis Antúnez

Everyone loves stories. People share content that makes them feel inspired. We need stories to know we’re not alone.

Slide decks are an excellent way to tell these stories. And there are already plenty of great tools out there for this like Powerpoint and Keynote.

But nobody loves HTML presentations. Literally, no one. “I love HTML presentations” returns [zero results](https://www.google.es/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#newwindow=1&q=%22I+love+HTML+presentations%22&search_plus_one=form) in Google search. ?

I’m a designer and developer who works all day on top of the giant platform that is the web. It always felt awkward and old-fashion for me to load up a separate program on my computer and use Powerpoint and Keynote — with their strange proprietary formats — then have to email it to someone.

So I built [WebSlides](https://webslides.tv).

WebSlides are all about **telling a story, then sharing it in a beautiful way:** hypertext, clean markup, and lovely CSS as narrative elements.

![Image](https://cdn-media-1.freecodecamp.org/images/WNgHPuzDIzudaRmfUGlM-7M8p9LWZQkFuCN7)

Designing in WebSlides can be just as fast as with Powerpoint. You can get by with a basic understanding of HTML and CSS. Just choose a [demo](https://webslides.tv/demos) and customize it in minutes.

Designers, developers, marketers, and journalists now have a web-native presentation tool with:

* Quick navigation keyboard shortcuts such (and both horizontal and vertical sliding).
* Permalinks that take you directly to a specific slide.
* A slide counter.
* [+40 components](https://webslides.tv/demos/components) including covers, cards, quotes, and forms
* A wide variety of backgrounds: colors, gradients, images, and videos.
* Flexible blocks with auto-fill and equal height.
* 500+ SVG icons thanks to Font Awesome

![Image](https://cdn-media-1.freecodecamp.org/images/XwUc3TQQQPPG6xrkIbG9pIiQP-R0i2n2yI4m)
_Demos: [Keynote](https://webslides.tv/demos/landings" rel="noopener" target="_blank" title="">Landings</a> · <a href="https://webslides.tv/demos/portfolios" rel="noopener" target="_blank" title="">Portfolios</a> · <a href="https://webslides.tv/demos/keynote" rel="noopener" target="_blank" title=")._

### Code Poetry

Here’s some [HTML source code](https://webslides.tv) that shows you how it’s done. This code is clean, scalable, and well-documented. It uses intuitive markup with [popular naming conventions](https://webslides.tv/demos/classes). **There’s no need to overuse classes or nesting**.

Each parent `_<secti_`on> i`n the #web`slides element is an individual slide:

```
<article id="webslides"&gt;  <!-- Slide 1 -->  <section>    <h1>Design for trust</h1>  &lt;/section>  <!-- Slide 2 -->  <section class="bg-primary aligncenter">    <div class="wrap">      <;h2>.wrap = container 1200px</h2>    </div>  </section></article>
```

### **Designing with purpose**

WebSlides is free and [open source](https://github.com/jlantunez/webslides). I built it because we need a platform for beautiful storytelling. Let’s look at what is happening:

* [Medium](https://medium.com) = Beautiful articles.
* [Typeform](http://typeform.com) = Beautiful forms.
* [WebSlides](https://webslides.tv) = Beautiful presentations and longforms.

![Image](https://cdn-media-1.freecodecamp.org/images/RYGMgnNiCJN8U5ScGXqiPzFuzncQHH10Paww)
_Demo: [Why WebSlides?](https://webslides.tv/demos/why-webslides" rel="noopener" target="_blank" title=") — Good karma._

I welcome [pull requests to WebSlides](https://github.com/jlantunez/webslides/issues) so we can keep improving and expanding this tool.

Please share this post to anyone you think might be interested in using this tool. I’ll look forward to reading your comments. Feel free to [email me](mailto:jlantunez@gmail.com) if you have any questions.

_Special thanks to [Luis Sacristán](https://twitter.com/luissacristan) and [Jenn Schiffer](http://twitter.com/jennschiffer) ([SimpleSlides](https://github.com/jennschiffer/SimpleSlides) was a revelation)._ ? Y_ou can also follow updates on T[witter,](https://twitter.com/webslides) D[ribbble,](http://dribbble.com/tags/webslides) and G[ithub.](https://github.com/jlantunez/webslides)_

