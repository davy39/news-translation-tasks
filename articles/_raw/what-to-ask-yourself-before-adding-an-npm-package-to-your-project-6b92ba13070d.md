---
title: What to ask yourself before adding an NPM package to your project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-05T18:09:22.000Z'
originalURL: https://freecodecamp.org/news/what-to-ask-yourself-before-adding-an-npm-package-to-your-project-6b92ba13070d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*40Etz3IOkChZ_RdoNcil3A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: open source
  slug: open-source
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Jacob Worrel

  One of the greatest things about being a JavaScript developer today is the ability
  to leverage its incredibly rich ecosystem. With almost a million packages on the
  NPM registry, it’s not uncommon to reach for an off-the-shelf solution...'
---

By Jacob Worrel

One of the greatest things about being a JavaScript developer today is the ability to leverage its incredibly rich ecosystem. With almost a **million** packages on the NPM registry, it’s not uncommon to reach for an off-the-shelf solution when facing a commonly solved problem. The less time you spend reinventing the wheel, the more you can focus on the larger problem at hand.

That being said, not all open source is created equal and it’s probably a good idea to do your homework before taking the leap and depending on someone else’s code. Here are some basic questions you should ask yourself before adding a new NPM package to your project, and the tools you can use to answer them.

### TL;DR

The following questions are based on my experience as a JavaScript developer and are by no means exhaustive. If you think anything’s missing, please feel free to let me know in the comments!

**How popular is it?** Look at weekly downloads on NPM & stars on Github.

**How mature is it?** Look at the date of the first published version on NPM and the number of open issues vs. closed issues on Github.

**Is it actively maintained?** Look at the commit history and the [Commits](https://github.com/expressjs/express/graphs/commit-activity) and [Code Frequency](https://github.com/expressjs/express/graphs/code-frequency) charts (under the Insights tab) on Github. Check the “last published” date on NPM.

**How big is it?** Check bundle size on [Bundlephobia](https://bundlephobia.com/).

**Does it have test coverage?** Check for coverage badges on NPM/Github. Open up the test files.

### How popular is it?

![Image](https://cdn-media-1.freecodecamp.org/images/ipdckGNlq1pIHne7aM65st7F3LI9A1XVazOr)
_Popularity of CSS-in-JS libraries by NPM downloads, courtesy of [npmcharts](https://npmcharts.com/" rel="noopener" target="_blank" title=")._

Popularity is probably the first thing most people want to know when looking around for an open source package to solve their problem — more specifically, how many stars it has on Github and how many weekly downloads it’s getting on NPM.

And while these two metrics might give you a pulse on how much traction a project has within the community, you should definitely take these numbers with a grain of salt. Keep in mind that a Github star is basically the equivalent to a “like” on social media sites and a lot of developers will dish these out like candy. I’m guilty of this myself, and just because I’ve starred a repo doesn’t mean I’ve checked for code quality and given it my full endorsement.

When it comes to downloads, even NPM admits their stats are “[naive by design](https://blog.npmjs.org/post/92574016600/numeric-precision-matters-how-npm-download-counts)” since they include downloads by automated build servers, mirrors and bots. Still, you have to start somewhere so you might as well get this question out of the way. Just be aware this is probably the least important (and often the most misleading!) factor, so make sure to do your due diligence and definitely don’t stop there.

### How mature is it?

![Image](https://cdn-media-1.freecodecamp.org/images/tZzWTv2iChpcSd3AgNunYVE6cezc9a4kRIvc)
_A healthy number of open vs. closed issues is a good indicator of how mature a project is._

If you’ve heard of the [80/20 rule](https://swreflections.blogspot.com/2013/11/applying-8020-rule-in-software.html), you’re probably familiar with the concept that the first 80% of code is typically done in 20% of the time, and the remaining 20% takes the other 80% of the time. This is because it’s usually easy to get something up and running, but handling all the edge cases, fixing unforeseen bugs and dealing with performance and scale is often the most challenging part of writing stable software. This is why you ideally only want to use open source that has been battle tested and has withstood the test of time.

The first thing to check is when a package was first published. Go to the project’s NPM page, click on the Versions tab to get the full history of every release and scroll down to the very bottom. A long history with lots of releases is usually a good sign since it means the project has been iterated on over time.

The next and probably best indicator of a mature project is the number of open and closed issues on Github. It’s usually a good idea to look at these two numbers together since one doesn’t really mean all that much without the other. A high number of open issues isn’t necessarily a bad thing if the number of closed issues is even higher. To give you some frame of reference, as of this writing, [React](https://github.com/facebook/react/issues) has about 400 open issues but more than 6500 closed. [Node.js](https://github.com/nodejs/node/issues) has around 600 open issues and almost 9000 closed.

There’s no magic ratio but beware of any project with a high number of open issues relative to how many issues have been closed. On the flip side, a low number of open issues isn’t necessarily a good thing if the number of closed issues is low as well. This likely means it hasn’t been used very much and is still in an early stage of development.

### Is it actively maintained?

![Image](https://cdn-media-1.freecodecamp.org/images/0lyma8THIp-zVYm3kAZmyxbnzHh7gX3ojNkf)
_The insights tab on Github_

Unless, a project is already very mature and not adding new features, or does something relatively small in scope, it’s important that it’s actively maintained. Remember the 80/20 rule? The only way software goes from new and experimental to stable and mature is through active maintenance, meaning regular bug fixes and added enhancements.

In my experience, the best way to check for this is by looking at the commit history on the project’s master branch. First, click on the number of commits on the project’s Github page and check when the last commit was merged to master. This date doesn’t mean very much by itself but it’s an important piece of the overall picture.

If you’re like me and you prefer to see this kind of data visualized, click on the insights tab, where you can glean all sorts of information about the repo. I could probably write an entire blog post about this feature alone, so all I’m going to say is, if you haven’t used this yet, stop reading, go to your favorite open source project’s Github page and start playing around with it.

I particularly like the [Commits](https://github.com/expressjs/express/graphs/commit-activity) and [Code Frequency](https://github.com/expressjs/express/graphs/code-frequency) graphs since they tell me at a glance how much the project is being worked on. Remember though, just because there aren’t a lot of recent commits doesn’t mean the code can’t be trusted. On the contrary, this is sometimes a sign of maturity — in the screenshot above, the code frequency chart for Express is a great visualization for what a mature project looks like.

Last but not least, I find it useful to know when a new version was last published on NPM, which is included in the hero stats on a project’s NPM page. This gives me a general sense as to how often the maintainers are actually scheduling releases, versus just committing code.

### How big is it?

![Image](https://cdn-media-1.freecodecamp.org/images/rG7TrFGwBkJWXUwo--WIqZCV1FYfVh70KaqN)
_A breakdown of d3’s NPM module on [Bundlephobia](https://bundlephobia.com/" rel="noopener" target="_blank" title=")._

No one likes a bloated bundle. And while it’s easy to keep adding node modules to a project, this can come at a [cost](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4). Minification, compression, and code splitting helps a lot, but at the end of day, it all boils down to how much JavaScript you’re sending to the client.

My go to resource for this is [Bundlephobia](https://bundlephobia.com/), a wonderful site that not only shows you the bundle size of an NPM package, but all sorts of other fancy things. Pictured above, you can see the estimated download time on slow networks, the evolution of the bundle size over the course of different versions, and the composition of dependencies. It will also tell you if the package is optimized to leverage tree-shaking with modern bundlers like Webpack, and even suggests similar modules, with stats comparing how they stack up size-wise!

Ideally, you want to use modules with a small size and a low number of dependencies, if any. Of course, size is relative so make sure you’re comparing apples to apples — if you’re looking at a charting library, for example, make sure you’re comparing it to other charting libraries (which tend to be on the bigger end of the spectrum).

### Does it have test coverage?

![Image](https://cdn-media-1.freecodecamp.org/images/RLyKPuibGV878fVuLCqackTNSNIwShpczNJb)
_A testing library with no test coverage…?_

This may seem obvious but always, always, always check for test coverage. Code you can’t test is code you can’t trust.

Nowadays, it’s much easier to get a high level picture of coverage thanks to tools like [Coveralls](https://coveralls.io/) and [Codecov](https://codecov.io/)— which track coverage over time and provide authors with shiny badges they can proudly display on their Github and NPM pages. Bear in mind though that test coverage tools only check how much code executed during tests and can be [misleading](http://www.developintelligence.com/blog/2017/11/why-test-coverage-shouldnt-trust/) at times. If you really want to get down into the nitty-gritty, there’s no substitute for opening up the test files and reading through the test specs.

### And of course…

#### Does It Follow Semantic Versioning?

Semantic versioning is a way for open source authors to communicate — via the version number — with consumers of their software about what kind of changes a new release includes. It ensures you know when breaking changes are introduced and therefore remain in control of your code despite depending on other modules. More on semantic versioning [here](https://semver.org/).

#### What’s the License?

If you were around during the whole [React license debacle](https://medium.freecodecamp.org/facebook-just-changed-the-license-on-react-heres-a-2-minute-explanation-why-5878478913b2), you probably learned it’s a good idea to check the license before you start using any open source software, lest some seemingly benevolent organization tries to pull a fast one on you. You can find them in the source code, usually in the project’s root directory. Look for permissive licenses like the [MIT license](https://en.wikipedia.org/wiki/MIT_License), which basically allows you to do whatever you want except sue the author. More on licenses [here](https://medium.com/shakuro/software-licenses-explained-77f4f18ebeb1).

### That’s right, read the source code!

While the questions discussed above are a good way to get a glimpse of the overall health of an NPM package, the best way to determine code quality on any project is by actually taking a look at the source code. Of course, this takes considerably more time than perusing through a project’s NPM / Github / Bundlephobia pages so you’re unlikely to do this for every dependency. However, it will likely pay off if the module is critical to your app. It might even save you from a major headache later on if you discover some deal breaker that otherwise might have gone unnoticed.

### Note on 3rd party UI components

If you’re using a component-driven front end framework like React, Vue or Angular, chances are you have some 3rd party UI component in your `package.json` dependencies. And while all the questions raised in this post still apply, UI components require some additional scrutiny, which I plan on addressing in a future post, so stay tuned!

