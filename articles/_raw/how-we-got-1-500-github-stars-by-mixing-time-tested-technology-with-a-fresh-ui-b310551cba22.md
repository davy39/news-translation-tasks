---
title: How we got 1,500 GitHub stars by mixing time-tested technology with a fresh
  UI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-16T06:43:00.000Z'
originalURL: https://freecodecamp.org/news/how-we-got-1-500-github-stars-by-mixing-time-tested-technology-with-a-fresh-ui-b310551cba22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dRitLnbV0KDrtHFtsI2ZzQ.jpeg
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Roman Hotsiy

  Recently we released an open-source tool called GraphQL Voyager. Surprisingly, it
  got to the first page of Hacker News and GitHub trending and gained 1,000+ stars
  in the first few days. As of now it has more than 1,600 stars.

  People l...'
---

By Roman Hotsiy

Recently we released an open-source tool called [GraphQL Voyager](https://github.com/APIs-guru/graphql-voyager). Surprisingly, it got to the first page of Hacker News and GitHub trending and gained 1,000+ stars in the first few days. As of now it has more than [1,600 stars](https://github.com/APIs-guru/graphql-voyager/stargazers).

People loved the slick UI, interactive features, and animations. We used TypeScript, React, Redux, webpack and even PostCSS but this is **NOT** **yet another article about them**. Let’s look under the hood…

### Our backstory

It all started a few months ago. My friend and I (we call ourselves [APIs.guru](https://apis.guru)-s) were looking for an idea for a project around [GraphQL](https://graphql.org/) (a query language for APIs developed by Facebook). After some research, an interesting tool caught our eyes — [GraphQL Visualizer](http://nathanrandal.com/graphql-visualizer/).

![Image](https://cdn-media-1.freecodecamp.org/images/xrsITDwSIv3dVd8gMfx1kOaKP3Cc6Rw0EkQr)
_Output from GraphQL Visualizer_

We wanted to add:

* colors (black and white looked too boring)
* pan-and-zoom
* interactive features like selecting nodes and edges

But after looking at the source code we found a [fatal flaw](http://www.drdobbs.com/windows/a-brief-history-of-windows-programming-r/225701475) in this tool: it used [Graphviz](http://www.graphviz.org/) — a decades old tool written in plain C and compiled to unreadable JavaScript using [Emscripten](https://github.com/kripken/emscripten).

![Image](https://cdn-media-1.freecodecamp.org/images/8tWF9RgASDSh2i-jlgIKWbwMb3fekhX5M9CL)
_Even worse than usual Uglify.js output_

How could we use something from 2000? We are hipsters for God’s sake! ReactJS, D3, webpack, TypeScript, PostCSS — that is what we work with! Not with tools written in old-fashioned C ?.

After a little research, we found the best library for the task— [Cytoscape.js](http://js.cytoscape.org/). It was written in the lovely JavaScript and even supported running CSS-like selectors on the graph itself. What a great result!

After a week of intensive coding, the result was less than satisfying. See for yourself:

![Image](https://cdn-media-1.freecodecamp.org/images/suwBiGVSkhBNW5B9dZMTQQ7UNCTnrQY6HZjf)
_Visualised graph using Cytoscape.js_

And that was without even displaying all that many details on the graph! What a mess!

Although the code was much cleaner, the end-result was much worse compared to the original tool. Completely unusable.

It appeared that there is no way for cytoscape.js to have edges that don’t cross nodes. We tried everything from our toolbox. We googled. We asked on StackOverflow. We even bothered a few SVG gurus we knew. Zero success :(

As a last resort, I even tried to hack cytoscape.js to produce a readable result. A little more research made me give up: apparently, visualizing graphs **is** rocket-science (even when you have a Master’s degree in applied math).

We were defeated…

And then it dawned on us. What if we were to take the output from Graphviz (which is just plain SVG) and sprinkle it with some CSS and JS?

And this did the trick ✨

![Image](https://cdn-media-1.freecodecamp.org/images/nW0lS1sFHqG7xOiU0t0N9mSpTTKMYDOcgwTe)

Much better! And less than a day of coding ?.

Adding a bit of color, a logo, loading animation, a few more useful features and here we are:

![Image](https://cdn-media-1.freecodecamp.org/images/3AwUl3XL7ZuJOXV4HfwdtAy8F-rccxjDFzFa)
_The final result_

Yes, we wrote a few hundred lines of ugly DOM manipulations. Yes, we packed all this mess as a NOT PURE ? React/Redux component. And yes, the Graphviz code is so huge we split it into a separate 2MB file. But it works and nobody cares. 1,600 stars on GitHub confirms this.

**UPDATE:** since the time article was submitted, the project has been adopted by the companies in the field (e.g. Graphcool, Neo4j) and it was featured on GraphQL Europe, so not only 1600 stars confirm that :)

### Lessons learned

> “If I have seen a little further it is by standing on the shoulders of giants.” — Issac Newton

Don’t judge code by it’s age. Especially if it was written by tech giants such as [AT&T Labs](https://en.wikipedia.org/wiki/AT%26T_Labs) (the place where Unix and the C and C++ languages were born).

Unfortunately, we were affected by cognitive bias: old code is bad code. But the truth can be the opposite. The old code is battle-tested by thousands of users in hundreds of different projects. Most of the critical bugs have been fixed, the documentation is complete, there are tons of questions and answers on StackOverflow and Quora.

We live in 2017, and a UI from the 2000’s is definitely not acceptable. But graphs and the mathematics behind them don’t change much.

The same line of thought can be applied to many other domains. So old code should be given a chance, especially since you can always wrap it into a modern-looking UI.

That’s why we see huge potential in [Web Assembly](http://webassembly.org/). It will allow to fuse time-proven algorithm implementations with modern UIs. We’re eager to see the awesome things people will build with it.

### “Emm.. you promised to tell me how to get lots of stars”

Oops… OK. You got me. I wanted to make the title catchy enough.

Below is a checklist of the most important tips & tricks we use for our open-source project:

* Try to use your technology name as a part of your project name (e.g. graphql-something, react-something, etc.) That way your project will have a better rank in GitHub search results for these technologies.
* Your README should catch peoples’ eyes. We added an animated gif to the top of our README so people could immediately understand what our project is about. If it’s a console app — add a gif with the console (here’s an awesome [awesome example](https://github.com/graphcool/graphql-up)).
* More bells and whistles: add badges, add a nice-looking logo, add emojis ? ?
* Set up a demo if possible, and add a link to it in the description field of the repository.

![Image](https://cdn-media-1.freecodecamp.org/images/YTnNgu5HMPJZVAjPeCM3ljlLsxRmDOHuhD3v)

* Again, **set up a demo**! And don’t forget to add link from the demo back to GitHub (we use [GitHub Corners](http://tholman.com/github-corners/)).
* Before posting it to HackerNews/Reddit/etc., gain an initial number of stars (5–10) by posting it to less popular resources, or sharing it with your friends. People are less likely to click “star” on the projects with zero stars.
* Try to gain 30–40 stars in the first day. That way you’re likely to get featured on GitHub trending for your language, which is another source for traffic.
* **Make something useful**.

There are a few other articles about how to promote open-source projects: [here](https://blog.cwrichardkim.com/how-to-get-hundreds-of-stars-on-your-github-project-345b065e20a2#.iudi1mx0q), [here](https://medium.com/@zenorocha/how-did-clipboard-js-get-5000-stars-in-a-few-days-2b2248ba7bd8#.wvvstia5n), and [here](https://medium.com/developer-relations/how-talks-affect-an-open-source-project-e4dd1db81a6d#.ecb0kqb1p).

That’s all folks. If you ever wrapped old code into new shiny UI ? tell your story in the comments below.

