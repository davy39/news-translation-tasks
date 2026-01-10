---
title: Should data scientists learn JavaScript?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T21:19:52.000Z'
originalURL: https://freecodecamp.org/news/should-data-scientists-learn-javascript-e611d45804b8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*UTtvUYQAa6heAbiq
tags:
- name: careers
  slug: careers
- name: Data Science
  slug: data-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Peter Gleeson

  The pros and cons of using the web’s #1 language for data science

  If you have been following the tech landscape in recent years, you have probably
  noticed at least two things.

  For one, you may have noticed that JavaScript is a very p...'
---

By Peter Gleeson

#### The pros and cons of using the web’s #1 language for data science

If you have been following the tech landscape in recent years, you have probably noticed at least two things.

For one, you may have noticed that [JavaScript is a very popular language](https://insights.stackoverflow.com/survey/2017#technology-programming-languages) these days. It has been growing in popularity ever since [Node.js](https://nodejs.org/en/) allowed JavaScript developers to write server-side code.

More recently, frameworks such as [Electron](https://electronjs.org/), [Cordova](https://cordova.apache.org/) and [React-Native](https://facebook.github.io/react-native/) have enabled JavaScript developers to build native apps across a wide range of platforms.

You’ve probably also noticed there is a lot of excitement surrounding the field of data science, especially machine learning. Recent advances in theory and technology have made this once-esoteric field much more accessible to developers.

You might ask, then, whether they make a natural pairing? Should data scientists consider learning JavaScript?

Most data scientists work with some combination of Python, R and SQL. If you are new to the field, **these are the languages you should master first**.

Data scientists may also specialize in another language such as Scala, or Java. There are [many reasons why these languages are so popular](https://medium.freecodecamp.org/which-languages-should-you-learn-for-data-science-e806ba55a81f).

But relatively few data scientists specialize in JavaScript.

However, given JavaScript’s ubiquity and data science’s popularity, how much could data scientists benefit from learning even the basics of the language? And how about JavaScript developers who want to explore data science?

Let’s start by looking at some important objections, then review some arguments in favour.

#### Against

* **Functionality** — JavaScript just doesn’t have the range of data science packages and inbuilt functionality compared to languages such as R and Python. If you don’t mind reinventing the wheel, this might be less of an issue. But if you need to run more sophisticated analyses, you’ll run out of options pretty quick.
* **Productivity** — Another advantage of Python and R’s extensive ecosystems is there are many guides and how-to’s available for almost any data science task you wish to do. For JavaScript, this is not really the case. You will probably take longer figuring out how to solve a data science problem in JavaScript than you would in Python or R.
* **Multithreading** — It is often helpful to process large data sets or [run simulations in parallel](https://medium.freecodecamp.org/solve-the-unsolvable-with-monte-carlo-methods-294de03c80cd). However, Node.js is not suited for computationally intensive, CPU-bound tasks. For such tasks, languages such as Python, Java or Scala have the upper hand over JS. But, check out [Microsoft’s Napa.js project](https://github.com/Microsoft/napajs#napajs). It provides a multithreaded JavaScript runtime that can complement Node.js.
* **Opportunity cost** — Perhaps the main reason data scientists tend not to learn many languages beyond Python and R is due to ‘[opportunity cost](https://en.wikipedia.org/wiki/Opportunity_cost)’. Every hour spent learning another language is an hour that could have been invested in learning a new Python framework, or another R library. While these languages dominate the data science job market, there is more incentive to learn them. And because data science is such a fast-moving field, there’s always something new to learn.

#### For

* **Visualization** — JavaScript excels at data visualization. Libraries such as [D3.js](https://d3js.org/), [Chart.js](https://www.chartjs.org/), [Plotly.js](https://plot.ly/javascript/) and [many others](https://www.codewall.co.uk/the-best-javascript-data-visualization-charting-libraries/) make powerful data visualization and dashboards really easy to build. Check out [some great D3 examples](https://github.com/d3/d3/wiki/Gallery)!
* **Product integration** — More and more companies are using web technologies with a Node-based stack to build their core product or service. If your role as a data scientist requires you to work closely with product developers, then it cannot hurt to ‘speak’ the same language.
* **ETL** — Data processing pipelines are usually implemented in a general purpose language, like Python, Scala or Java. JavaScript often doesn’t get a look in. However, this might be unfair. Node’s filesystem module ‘fs’ provides a great API which lets you call standard filesystem operations either synchronously or asynchronously. Node also plays along nicely with [MongoDB](https://www.mongodb.com/) and many other popular database systems. The [Streams API makes it very easy to work with streams of large data](https://medium.freecodecamp.org/node-js-streams-everything-you-need-to-know-c9141306be93) — another potential advantage for ETL. As mentioned above, for multithreading and parallel processing, see [Microsoft’s Napa.js project](https://github.com/Microsoft/napajs#napajs).
* **Tensorflow.js** — Who says JS can’t do cool machine learning stuff? Earlier in 2018, [Tensorflow.js was released](https://medium.com/tensorflow/introducing-tensorflow-js-machine-learning-in-javascript-bf3eab376db). This brings machine learning to JavaScript developers — both in the browser and server-side. [Tensorflow](https://www.tensorflow.org/) is a popular machine learning library, developed by Google and made open source in 2015. Gesture recognition, object recognition, music composition… you name it, you can probably have it. The best thing you can do right now is [take a look at some demos](https://github.com/tensorflow/tfjs/blob/master/GALLERY.md).

### Conclusion

So, should data scientists learn JavaScript?

Learning JavaScript won’t harm your resumé. **But don’t learn it as replacement for other languages.**

As a first language, the best advice is to learn one of either Python or R. You should also become comfortable using some database language, such as SQL or MongoDB.

However, once you are familiar with the basics, you may want to specialize further. Perhaps you want to learn [Apache Spark](https://spark.apache.org/) for working with giant, distributed datasets. Or maybe you’d prefer learn another language such as Scala, or MATLAB or Julia.

Why not consider JavaScript? It will prove valuable if you want to specialize in data visualization, or if your role requires you to work closely with a product built using JavaScript or a related technology.

JavaScript’s machine learning capabilities are advancing rapidly. For some use cases, it is perhaps already a strong alternative to the usual data science languages.

Ultimately, the decision is both practical and personal. It depends on which aspects of data science you find most interesting, and what career opportunities excite you most.

But with [current trends](https://magenta.tensorflow.org/demos/), one thing is for sure. Over the coming years, JavaScript will open more doors than it closes.

