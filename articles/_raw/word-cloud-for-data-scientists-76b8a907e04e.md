---
title: An easy way to make word clouds for data scientists
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T05:24:33.000Z'
originalURL: https://freecodecamp.org/news/word-cloud-for-data-scientists-76b8a907e04e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HYtC28uzCWtTK2r_cR_3CA.png
tags:
- name: Data Science
  slug: data-science
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: text mining
  slug: text-mining
- name: visualization
  slug: visualization
seo_title: null
seo_desc: 'By Kavita Ganesan

  About a year ago, I looked high and low for a Python word cloud library that I could
  use from within my Jupyter notebook. I needed it to be flexible enough to use counts
  or tfidf when needed or just accept a set of words and corresp...'
---

By Kavita Ganesan

About a year ago, I looked high and low for a Python word cloud library that I could use from within my Jupyter notebook. I needed it to be flexible enough to use `counts` or `tfidf` when needed or just accept a set of words and corresponding weights.

I was a bit surprised that something like that did not already exist within libraries like `plotly`. All I wanted to do was to get a quick understanding of my text data and word vectors. I thought that was probably not too much to ask…

Here I am a year later, using my own [word_cloud](https://github.com/kavgan/word_cloud) visualization library. Its not the prettiest or the most sophisticated, but it works for most cases. I decided to share it, so that others could use it as well. After [installation](https://github.com/kavgan/word_cloud), here are a few ways you can use it.

#### Generate word clouds with a single text document

This example show examples of how you can generate word clouds with just one document. While the colors can be randomized, in this example, the colors are based on the default color settings.

By default, the words are weighted by word counts unless you explicitly ask for tfidf weighting. Tfidf weighting makes sense only if you have a lot of documents to start with.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HYtC28uzCWtTK2r_cR_3CA.png)
_word cloud based on a single document_

#### Generate word clouds from multiple documents

Let’s say you have 100 documents from one news category, and you just want to see what the common mentions are.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lKQBi3n4OfjawldVtXrU5g.png)
_word cloud based on multiple documents_

#### Generate word clouds from existing weights

Let’s say you have a set of words with corresponding weights, and you just want to visualize it. All you need to do is make sure that the weights are normalized between [0 - 1].

![Image](https://cdn-media-1.freecodecamp.org/images/1*NyGmBmZ4OOiOPLir9h4doA.png)
_word cloud from existing weights_

Hope you find this useful! Please feel free to propose changes to prettify the output - just open a pull request with your changes.

### Links

* [See my Jupyter notebook with code examples](https://colab.research.google.com/drive/1AkdUKEFmaYom77r6KPh18jdQrplIQbKQ)
* [Start using word_cloud library](https://github.com/kavgan/word_cloud)

