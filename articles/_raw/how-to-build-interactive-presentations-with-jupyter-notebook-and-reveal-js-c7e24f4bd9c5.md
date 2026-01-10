---
title: How you can ditch PowerPoint and build better slides with Jupyter and Reveal.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-10T00:33:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-interactive-presentations-with-jupyter-notebook-and-reveal-js-c7e24f4bd9c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MvyDoOEprAO-lbSuInyA0w.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Dat Tran

  In this article, I will introduce jupyter2slides — a little side project of mine
  that lets you easily create beautiful and interactive presentation slides using
  Jupyter Notebook and reveal.js.

  Here’s what it looks like:


  _[http://interact...'
---

By Dat Tran

In this article, I will introduce [jupyter2slides](https://github.com/datitran/jupyter2slides) — a little side project of mine that lets you easily create beautiful and interactive presentation slides using [Jupyter](http://jupyter.org/) Notebook and [reveal.js](http://lab.hakim.se/reveal-js/#/).

Here’s what it looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*8Hmu8ZyI3NJJWvVEWZlWAg.gif)
_[http://interactive-slides.cfapps.io/](http://interactive-slides.cfapps.io/#/" rel="noopener" target="_blank" title=")_

And this is the corresponding PDF, generated with [DeckTape](https://github.com/astefanutti/decktape):

### My motivation for building this

Microsoft PowerPoint is cool. It’s like a Swiss Army knife for consultants, and you can make beautiful slides with it.

When it comes to code, though, PowerPoint sucks. The solution is to use reveal.js. You can use markdown to highlight code, and it’s responsive. But like [LaTeX](https://www.latex-project.org/), it can be tedious.

Another way to use reveal.js is through Jupyter which offers many advantages:

* In-browser editing for code with automatic syntax highlighting, indentation, and tab completion
* Ability to run code with the results of computations attached to the code which generated them (literate programming)
* Supports [Markdown](https://en.wikipedia.org/wiki/Markdown) and many media formats such as HTML, LaTex, audio, and images
* Supports interactive widgets to manipulate and visualize data
* Uses tools from the [PyData stack](https://www.numfocus.org/) like Matplotlib, Numpy, and Bokeh as well as others like [Plotly](https://plot.ly/) and [Folium](https://folium.readthedocs.io/en/latest/)

To use reveal.js with Jupyter, you create a notebook and use [nbconvert](http://nbconvert.readthedocs.io/en/stable/) to get reveal.js slides as well. But the standard design is boring:

![Image](https://cdn-media-1.freecodecamp.org/images/1*kq3-BczjCXej2BMu-u4Qyw.png)
_Check out [IPython Slides Viewer](http://slideviewer.herokuapp.com/" rel="noopener" target="_blank" title=") for some other “default” examples._

### My solution

I’ve worked on a project that lets you generate beautiful presentation slides. The entire code is on [my GitHub repo](https://github.com/datitran/jupyter2slides). Under the hood, it still uses `nbconvert`with reveal.js, but I extended it by:

* Adding a customized theme which has a cleaner design
* Enabling the [title footer plugin](https://github.com/e-gor/Reveal.js-Title-Footer) by default
* Enabling slide numbers by default
* Adding a Jupyter notebook template with examples like cover and divider slides, markdown syntax, and more
* Making it easier to push the presentation to [Cloud Foundry](https://www.cloudfoundry.org/) by using [Flask](http://flask.pocoo.org/) and the Python buildpack
* Including the option to export slides to PDF using [DeckTape](https://github.com/astefanutti/decktape)

### How to get started

To create your own presentation, clone the [repo on GitHub](https://github.com/datitran/jupyter2slides) and go through its readme.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WEgwvN_yuy0-gsgAAmIKIw.gif)
_Clone the [repo](https://github.com/datitran/jupyter2slides" rel="noopener" target="_blank" title=") to get started._

I hope this project will be of use for you in the future. I look forward to seeing others use this template at conferences like [PyData](https://pydata.org/). I welcome any feedback to improve the slide designs and others’ contributes to the code base.

If you found this article useful, give me a high five ?? so others can find it too, and share it with your friends. Follow me here on Medium (Da[t Tran)](https://medium.com/@datitran) or on Twitter (@d[atitran)](https://twitter.com/datitran) to stay up-to-date with my work. Thanks for reading!

