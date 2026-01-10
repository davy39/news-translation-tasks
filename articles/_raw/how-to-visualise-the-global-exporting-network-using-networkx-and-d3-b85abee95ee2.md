---
title: How to visualise the Global Exporting Network using NetworkX and D3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-15T23:58:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-visualise-the-global-exporting-network-using-networkx-and-d3-b85abee95ee2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OC42Ul4VREUunK-yojnOyA.png
tags:
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Patrick Ferris

  Data-Driven Documents (D3) is a JavaScript library for building powerful graphics
  to communicate information in datasets. It is also fair to say that for many, myself
  included, it has a non-standard approach to building the graphics...'
---

By Patrick Ferris

Data-Driven Documents (D3) is a JavaScript library for building powerful graphics to communicate information in datasets. It is also fair to say that for many, myself included, it has a non-standard approach to building the graphics. Often the learning curve can feel steep.

In this post we’ll look at using NetworkX — a Python library for exploring graph structures — to do some of the initial data processing for us. Then we’ll add the artistic finishing touches in JavaScript with D3. The full code can be found on my [GitHub](https://github.com/patricoferris/blog-posts/tree/master/Exporting_Dependencies) and an interactive version can be found [here](https://bl.ocks.org/patricoferris/bd646b1122b087cc3ec61de0690625b8/104d0bbfd541851d99d0babdbc0a6f35a6f5a20f).

### The data

I remember when I was first introduced to the [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/), and I loved it. It holds a treasure trove of information about all of the countries in the world. It is just screaming for visualisations of the data to be made. On top of this, it has been converted to different formats on [GitHub](https://github.com/factbook) and — most importantly for us — to JSON.

The data is given per country using their two character ISO encoding. We’ll need the continent each country is in to access the data. First we’ll create that dictionary:

The dictionary makes things a lot simpler when we want to access the URL for each country’s data.

The next step is to define a simple `Country` class to hold the data. While we’re at it, it would improve the visualisation if we could use actual country names — not their two character code — so we can find that information and store it for later use.

And now we’re finally ready to add the exporter information — this method isn’t perfect but it gets a majority of the information.

Don’t worry too much about the `split()` functions on the exporting partners. That’s just cleaning up some of the data so we only get the names and the percentages we want. Check out the GitHub page to see the extra names I had to add for the graph construction to work.

### NetworkX

[NetworkX](https://networkx.github.io/) is a fairly sophisticated Python library for constructing, analysing, and — to a certain extent — exporting graph data structures. It is also really simple to use.

Now that we have the data we want stored in our `Country` objects, the code for creating our directed graph is very simple.

We can also add attributes to our nodes like the degree of the node and the name (not the ISO code). Once we have our data structure we can export it to a JSON format and dump it in a file ready to be used with D3.

### What’s different about D3?

From the outset, Mike Bostock (the founder of D3) wanted to create a “reusable chart.” In his [post](https://bost.ocks.org/mike/chart/) on the subject, he highlights the key goals and missions for the D3 project. These can help us understand the syntactic structure it has.

The first, and **most important**, take-away is that charts should be implementable “as closures with getter-setter methods.” If you’re new to programming you may be confused as to what a [closure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures) is. Don’t worry! The big concept associated with closures is lexical scoping, which sounds a lot scarier than it really is. The basic idea behind it all is nested functions and how the inner function has access to the outer function’s variables.

Take a look at `EXAMPLE 1` in the code below. Here we simply return the inner function, which has access to the arguments passed to the outer function. The variable we declare, `closureOne` , is a function and when we execute it with `closureOne()` we `console.log(config.name)` .

In `EXAMPLE 2`, we declare variables within the scope of the outer function allowing the inner `my` function to have access to it. In the `fullName` function associated with the `my` function — a method — we can **either** set or get the `nameOfPerson` depending on it any arguments are passed. Notice how the developer does not have access to the variable `nameOfPerson` . The developer is forced to use our defined methods to update and access it, providing a level of security to our function.

This method of using closures is how D3 is coded. Take a look at the [line](https://github.com/d3/d3-shape/blob/master/src/line.js) function to see this in action. This [video](https://www.youtube.com/watch?v=-jysK0nlz7A&t=647s) may also shed some light on the topic.

### Programming in D3

Thankfully you **don’t need to be a master of closures and D3** to create a visualisation. In fact, so long as you can copy and paste, you can usually get something running in no time at all thanks to [Mike Bostock’s Blocks](https://bl.ocks.org/mbostock). This site has many open-source examples of building data visualisations in D3. You can use the code to create your own with your data.

To create the network for this tutorial, I used [this example](https://bl.ocks.org/mbostock/4062045). To get it running on screen, all I had to change was the name of the .csv file.

Let’s look at some of the **key lines of code** making this visualisation work, and also the parts I’ve added to hopefully improve it further.

Just before we dive in, Andrew Dunkman wrote a great article helping explain [D3 selection](https://techtime.getharvest.com/blog/understanding-d3-selection-operations) which I recommend reading.

To see the functions we’re calling like `dragstarted` , `scaledSize` , or `mouseOut` , be sure to look at the full code [here](https://github.com/patricoferris/blog-posts/blob/master/Exporting_Dependencies/index.js). As an example, let’s see what’s happening when we click on a node.

### Conclusion

The code is messy, the visualisation isn’t perfect, and there is so much left to discuss and learn.

But that’s beside the point. Hopefully this post has been able to let you get your feet wet with NetworkX and D3 without throwing too much at you. We all have to start somewhere, and this can be your beginning to create insightful and powerful data visualisations.

If you’re stuck wondering what to tackle next, here are a few of suggestions:

* [Mike Bostock’s Towards Reusable Charts](https://bost.ocks.org/mike/chart/) — this is a great example of someone explaining their thought process and then their implementation. This shows how his goals for the project affected his implementation.
* [D3 and React](https://www.smashingmagazine.com/2018/02/react-d3-ecosystem/) — two libraries fighting over the DOM, this is currently what I’m reading about, and seeing what are the best ways to utilise both on a project.
* [Elijah Meeks, Senior Data Visualization Engineer at Netflix](https://medium.com/@Elijah_Meeks/d3-is-not-a-data-visualization-library-67ba549e8520) —any of Elijah Meeks’ posts are a great resource and often shed light on the world of data visualisation.

Thanks for sticking with me to the end. Happy visualising!

