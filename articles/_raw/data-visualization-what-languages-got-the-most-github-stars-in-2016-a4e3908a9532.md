---
title: Which languages got the most GitHub stars in 2016?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-16T17:29:09.000Z'
originalURL: https://freecodecamp.org/news/data-visualization-what-languages-got-the-most-github-stars-in-2016-a4e3908a9532
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-hRBr9wXEoFe_3TuTpuDVA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Jose Aguinaga

  A few weeks ago I decided to build an application to find which programming languages
  I star the most in GitHub.

  Why? Because lately I had been starring projects about Machine Learning, Data Science,
  and Artificial Intelligence. I wa...'
---

By Jose Aguinaga

A few weeks ago I decided to build an application to find which programming languages I star the most in GitHub.

Why? Because lately I had been starring projects about **Machine Learning, Data Science,** and **Artificial Intelligence.** I wanted to see whether my increased interest would show up in my starred projects timeline in any way. And what better way to discover this by using a little bit of Data Science on its own?

The experiment consisted in obtaining the information from GitHub, cleaning it up, and displaying it in a visualization. To try it yourself, go to the following webpage.

[**What languages got the most GitHub stars in 2016?**](https://starred.jjperezaguinaga.com/)  
[_A streamgraph of github starred languages on 2016._starred.jjperezaguinaga.com](https://starred.jjperezaguinaga.com/)

After trying it yourself, give me a moment to explain how it works and show you some interesting examples.

### Retrieving and analyzing the data

For better or worse, GitHub doesn’t provide an easy way to consume this information. You need to go through all your starred projects on [github.com](https://github.com/jjperezaguinaga?tab=stars), then click through many pages to find them all. Depending in how many repositories you have starred, it would take you a few minutes before you can see all the projects across a specific timespan.

The good news are that GitHub has a [starring activity API](https://developer.github.com/v3/activity/starring/), which I then used to write a JavaScript utility to fetch all my starred projects through the year. GitHub allows you to pass a flag to see the date when you first starred a project, which let me get only the projects I starred in 2016.

With the data retrieved, I proceeded to filter it based on the language GitHub has assigned to them. [Ramda](http://ramdajs.com/) was particularly useful to map and reduce this data.

Then, to visualize this information, I decided to display the frequency of each repository programming language through a chart known as a [_streamgraph_](https://en.wikipedia.org/wiki/Streamgraph)_._ Aggregating each language instance per month, I could see the increase and decrease of interest over time.

![Image](https://cdn-media-1.freecodecamp.org/images/mSp-YanfncIQV-QgEP9ERSpsGLFvqYSOwYt7)
_A streamgraph of my starred projects in 2016 aggregated by language and distributed per month. GitHub sometimes will be unable to decide over a specific language for a project, and will give **null** instead._

As we can see in the graph, I starred **142 projects** in 2016. There were more than 15 languages across my starred repositories, but I’m only displaying the top 7, as the frequency per language drops after this number. The top language is JavaScript, which doesn’t surprise me, as I work as a Front-End Engineer on a daily basis.

The second and third programming languages are **Python** and **Go,** which most likely relate to projects about artificial intelligence / deep learning I mentioned earlier. Python made sense, since it was recently considered [the most popular language for Machine Learning](https://www.ibm.com/developerworks/community/blogs/jfp/entry/What_Language_Is_Best_For_Machine_Learning_And_Data_Science?lang=en).

### Everyone gets a graph.

As part of the development of the tool, I tested the application with other developers. This produced a series of interesting graphs.

The following is a list of a few famous developers, grouped by the languages they’ve starred the most.

#### Javascript Developers

![Image](https://cdn-media-1.freecodecamp.org/images/UQpYL0aoitvNqxcOkbjSQYDYCrPOmN3dDnI-)
_[Addy Osmani](undefined" rel="noopener" target="_blank" title=") — Google Web Platform Engineer_

![Image](https://cdn-media-1.freecodecamp.org/images/EMz3T7QrysKajc5DJYiTTivCKLMH5BwZRaKg)
_[Paul Irish](undefined" rel="noopener" target="_blank" title=") — Chrome Dev Tools Engineer_

![Image](https://cdn-media-1.freecodecamp.org/images/ExICtXhMOdoOXMOlgplXX1J7MMHDT-E29Shl)
_[Eric Elliott](undefined" rel="noopener" target="_blank" title=") — Javascript Developer_

![Image](https://cdn-media-1.freecodecamp.org/images/AcsyJGT2XWqFiw4HrPeMotvyqLVvispuBOk4)
_[Sindre Sorhus](undefined" rel="noopener" target="_blank" title=") — Disguised unicorn_

![Image](https://cdn-media-1.freecodecamp.org/images/5YQ-WFc89RtC9AjveOxw2XZKWvGf2sl720Bn)
_[John Resig](undefined" rel="noopener" target="_blank" title=") — Staff Engineer at Khan Academy and creator of jQuery_

![Image](https://cdn-media-1.freecodecamp.org/images/m3DS7IOoKkFf3ckfgcrRq88lgkte4YoZidb5)
_[Dan Abramov](undefined" rel="noopener" target="_blank" title=") —Facebook Engineer, Co-author of Redux, Create React App and React.js_

![Image](https://cdn-media-1.freecodecamp.org/images/NpZZHANKaTtHuGq9OZBTbhUHzBfQ7Bs9dtAo)
_[Ben Alpert](https://github.com/spicyj" rel="noopener" target="_blank" title=") — Facebook Engineer, React.js Contributor_

#### Golang Developers

![Image](https://cdn-media-1.freecodecamp.org/images/MN3igg-z5QlxNlD16JwA3kD8DMt4vyryiqVW)
_[TJ Holowaychuk](undefined" rel="noopener" target="_blank" title=") — Founder of Apex.sh, Javascript and Golang Developer_

![Image](https://cdn-media-1.freecodecamp.org/images/THcSt1hkg-pWGXz22Dv3XQFCfRsb8JBHvGB6)
_[Jessie Frazzelle](https://twitter.com/jessfraz" rel="noopener" target="_blank" title=") — Everything containers_

![Image](https://cdn-media-1.freecodecamp.org/images/letMN4s0Z7H9JX05FhRsYXF9hVb-P8wbUTwH)
_[Josh Baker](undefined" rel="noopener" target="_blank" title=") — Makes a killer goulash_

![Image](https://cdn-media-1.freecodecamp.org/images/d-T1bJOrS2IQnk0J4dSRciE5Sk8LfwcWqmWo)
_[aarti](https://github.com/aarti" rel="noopener" target="_blank" title=") — Exercism.io contributor_

#### Python Developers

![Image](https://cdn-media-1.freecodecamp.org/images/L-zwvoLMN-Z75MRsA2Fu8dqIbLw98BrEfo28)
_[Thaddee Tyl](undefined" rel="noopener" target="_blank" title=") — He saw some code_

![Image](https://cdn-media-1.freecodecamp.org/images/9eOLVdUA4zl0mCL-qHKrqhVe-FaQuQjEb5q7)
_[John Washam](undefined" rel="noopener" target="_blank" title=") — Future Google Engineer_

![Image](https://cdn-media-1.freecodecamp.org/images/Qu8zbkRm3pamo4rMY4kGcGl9uOIritD84rjm)
_[Geimfari](undefined" rel="noopener" target="_blank" title=") — Pythonista, Erlanger, Cosmonaut_

![Image](https://cdn-media-1.freecodecamp.org/images/o6x0Hp927aOLyKNvmRamf4nLHfu4FeUORk2V)
_[Nam Vu](undefined" rel="noopener" target="_blank" title=") — Future Machine Learning Engineer_

#### Swift,R

![Image](https://cdn-media-1.freecodecamp.org/images/ofo9qk48jvS8fkLlzcLzy57qXvdzNbBqXKj4)
_[Luke Zhao](https://github.com/lkzhao" rel="noopener" target="_blank" title=") — iOS Developer_

![Image](https://cdn-media-1.freecodecamp.org/images/8enRlEKgyO6Wostjo3R71sqVSnz05jIvCabg)
_[Jennifer Bryan](https://github.com/jennybc" rel="noopener" target="_blank" title=") — Professor at UBC_

### The thing about data

I had a lot of fun from this experiment, and learned two important lessons:

* **Data can be beautiful**. Not everything needs to have a deep meaning in order to be interesting. For instance, the cover for this article is the product of overlapping a series of _streamgraphs_ from various datasets. I liked it so much I even [copyrighted](https://blockai.com/c/e1jLAq) it.
* **Our data identify us.** Given enough starred projects, the chances of having two individuals with the exact same starred repositories at the exact same time are negligible*. Thus, if we analyze the starring patterns on a developer, we could identify them by seeing their data. This is an example of [Behavioral Analytics](http://dl.acm.org/citation.cfm?id=2971707&dl=ACM&coll=DL&CFID=716696458&CFTOKEN=32651178), used in the past to [identify users by mobile app usage](http://dl.acm.org/citation.cfm?id=2971707&dl=ACM&coll=DL&CFID=716696458&CFTOKEN=32651178).

By the end of this experiment, I’m was more interested in exploring the usages of Data Visualization and Machine Learning than before**. I’ll continue to expand my knowledge in the area to create more experiments like this in the future.

### Please do try this at home

If you’re curious about the code, you can see it on Github.

[**jjperezaguinaga/github-patterns**](https://github.com/jjperezaguinaga/github-patterns)  
[_github-patterns - ? What languages got the most GitHub stars in 2016?g_ithub.com](https://github.com/jjperezaguinaga/github-patterns)

Bear in mind the code is very dirty, so errors might occur (for example, the GitHub rate limit timeout error isn’t caught), so don’t take it as a reference for any real production projects. Feel free to [change, expand or fork the code](https://github.com/jjperezaguinaga/github-patterns) as you wish.

_*Not negligible, but very unlikely. A person would need to star the same project at the same second to share the same pattern. There are 31557600 seconds in an astronomical year and are around [20M](https://octoverse.github.com/) repositories in GitHub by the end of 2016, and around 5.8M active users in GitHub. You tell me what are the odds of two people with 10 starred projects to have the same pattern._

_**Udacity released this weekend [a new nanodegree about Deep Learning foundations](https://www.udacity.com/course/deep-learning-nanodegree-foundation--nd101). I’ve enrolled myself and will post an overview after I finish it._

