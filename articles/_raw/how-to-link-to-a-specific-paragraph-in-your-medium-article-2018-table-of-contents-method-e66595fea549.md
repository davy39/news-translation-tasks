---
title: How to link to a specific paragraph in your Medium article (Table of Contents
  method)
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2018-02-22T20:47:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-link-to-a-specific-paragraph-in-your-medium-article-2018-table-of-contents-method-e66595fea549
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UCdiE5IGAlQt8YJ-vKWv1A.png
tags: []
seo_title: null
seo_desc: 'Update Feb 26, 2018: a member of the freeCodeCamp community just built
  a tool that makes this process extremely convenient. Instead of using the method
  I describe in this article, I recommend you just use his website.


  A screenshot from mediumtoc.com...'
---

**Update Feb 26, 2018**: a member of the freeCodeCamp community just built a tool that makes this process extremely convenient. Instead of using the method I describe in this article, I recommend you just [use his website](https://www.mediumtoc.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/gIWQ-TirKtcVt91mqai-UHzE0aBbNBiUYZkM align="left")

*A screenshot from* [*mediumtoc.com*](https://www.mediumtoc.com/)

I’m going to show you how you can make a nice hyper-linked Table of Contents for your Medium articles. Here’s what this will look like in your Medium article:

![Image](https://cdn-media-1.freecodecamp.org/images/2eyEr6YvptG9w1PAfp1jNJfq1OCrN68dKnqO align="left")

Each of these links will jump to a specific part of the article. This is a major usability improvement for your readers. Especially if your article is long enough to require multiple reading sessions to finish.

On the [freeCodeCamp Medium publication](https://medium.freecodecamp.org), we frequently publish articles that are 20 minute reads, 40 minute reads, even 60 minute reads. And we find these Table of Contents to be super helpful.

Note that the technique I share here in this article has mixed results on mobile devices. So here’s hoping Medium formally adds this feature in the future.

### Proof that this works

By clicking [this link](https://medium.com/p/e66595fea549#ddca), you will be transported right back to this exact part of this article.

### So here’s how you do this.

Each heading on Medium is its own HTML element, with its own `id`.

To get the `id` of the heading, you need to right-click on it, then click “inspect.”

This will open your browser’s developer tools. Here’s what this looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/wjuRelJMIPs2ShBj8LjFTv8Jzrfy2XRe64BE align="left")

Now you just need to get the 4-digit hexadecimal code associated with that HTML element. In this case, the `id` of the “Hello, World!” heading is `48f5`.

Now you can use that code to make a special link that will link directly to that heading. These links follow this structure:

`https://medium.com/p/[article ID]#[4-digit hexadecimal code]`

* The **article ID** is the 12-digit hexadecimal code for the Medium article. One of these codes is in every Medium URL. For example, the article ID for this article you’re reading is `e66595fea549`. Go ahead — check the address bar of your browser and you should see this code in the URL. This code is the universal identifier for your article and it will never change — even if you change the headline for your article or publish it in a Medium publication.
    
* The **4-digit hexadecimal code** is the code you got from the developer tools (in this case, `48f5`).
    

Here’s the URL I used earlier to link back to my “proof that this works” section:

```javascript
https://medium.com/p/e66595fea549#ddca
```

### Let’s build a table of contents!

Here’s that table of contents I showed you earlier. Each of these will link to a different section of the same article:

#### Table of Contents

* [Disclaimers](https://medium.com/p/1c96572a1401#0239)
    
* [Seven bridges of Königsberg](https://medium.com/p/1c96572a1401#48f5)
    
* [Intro to Graph representation and binary trees (Airbnb example)](https://medium.com/p/1c96572a1401#0374)
    
* [Graph representation: outro](https://medium.com/p/1c96572a1401#fb0c)
    
* [Twitter example: tweet delivery problem](https://medium.com/p/1c96572a1401#0cd4)
    
* [Graph Algorithms: intro](https://medium.com/p/1c96572a1401#fb0c)
    
* [Netflix and Amazon: inverted index example](https://medium.com/p/1c96572a1401#cdde)
    
* [Traversals: DFS and BFS](https://medium.com/p/1c96572a1401#45f6)
    
* [Uber and the shortest path problem (Dijkstra’s algorithm)](https://medium.com/p/1c96572a1401#aa4d)
    

### A Chrome Extension to make this process easier

In response to this article, [Cadu de Castro Alves](https://www.freecodecamp.org/news/how-to-link-to-a-specific-paragraph-in-your-medium-article-2018-table-of-contents-method-e66595fea549/undefined) [created a Chrome extension](https://github.com/castroalves/medium-anchor-url-generator) that makes extracting the IDs from different paragraphs an more straight-forward process.

### That’s all. Have fun, and happy writing!

If you found this article helpful, you should [follow me on Twitter](https://www.twitter.com/ossia). I only tweet about programming and technology, and I won’t waste your time :)
