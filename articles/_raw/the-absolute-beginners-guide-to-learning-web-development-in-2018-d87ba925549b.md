---
title: The absolute beginner’s guide to learning web development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T01:44:40.000Z'
originalURL: https://freecodecamp.org/news/the-absolute-beginners-guide-to-learning-web-development-in-2018-d87ba925549b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*48Svhyucz8U4vEbhK8swpg.png
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jessica Chan

  This post was originally published on Coder-Coder.com.

  If you’re a beginner coder, this guide is for you!

  Here is what this guide covers:


  An explanation of the basic areas in web development,


  An overview of programming languages and...'
---

By Jessica Chan

*This post was originally published on* [*Coder-Coder.com*](https://coder-coder.com/learn-web-development/)*.*

If you’re a beginner coder, this guide is for you!

Here is what this guide covers:

* An explanation of the **basic areas** in web development,
    
* An overview of **programming languages and frameworks**,
    
* And **recommended resources** to help you learn.
    

It’s geared for beginners, with helpful links and information to give you a head start into your own research.

Here’s what we’ll be going through.

### Table of Contents

\*Jump links included, so you can skip around if you want!

### [Part 1: We’ll start out with the basics:](#part1)

* **What web development is**: explaining what’s actually happening when you load a website in your browser.
    
* **HTML, CSS, and JavaScript**: the foundation of every website.
    
* Helpful tools: using **code editors and Git**
    
* What’s **front-end** and **back-end**?
    

### [Part 2: Then we’ll get into more intermediate front-end skills:](#part2)

* **Responsive design**: making sure your website looks good on computers, tablets, and phones.
    
* **Grunt, Gulp, and WebPack**: using build tools to do some work for you!
    
* An introduction to **JavaScript front-end frameworks**: React, Vue, and Angular
    

### [Part 3: Followed by back-end skills:](#part3)

* An overview of the most commonly used **back-end languages** and how they stack up.
    
* A quick intro to **databases** and what database languages you should learn.
    
* The basics of setting up a website on a **server**.
    

### [Epilogue: Learning resources](#epilogue)

* A short list of recommended online courses, tutorials, and books.
    

Now, before we go through everything about websites… let’s start with you!

### What’s your ultimate goal in learning to code?

In his book *The 7 Habits of Highly Effective People*, Stephen R. Covey asserts that in order to be successful, you have to “begin with the end in mind.”

Consider your own reasons for getting into coding… What end are you aiming for?

What is your ultimate goal?

Are you looking for a fun hobby, a career change, a flexible job where you can be closer to your family?

**Your entire approach to web development should be centered around achieving this one dream.**

You can even try writing down your goal, and putting it someplace where you will see it everyday, like your bathroom mirror or next to your computer.

As you go through this article, keep your goal in mind, and let that determine what decisions you make: which languages to learn, even how you choose to learn.

With that said, let’s get started with the basics!

![Image](https://cdn-media-1.freecodecamp.org/images/1*wCBlcgi36bFR_JfU1pcp8Q.png align="left")

### Part 1: The basics

This might seem obvious, but I’m going to say it anyway:

**At its core, web development is all about building websites.**

A website may be a simple one page site, or it could be an incredibly complex web application.

If you can view it on the web in a browser, it has to do with web development.

Here is a simple explanation of how websites on the internet work:

1. **Websites** are basically a bunch of files stored on computers called servers.
    
2. **Servers** are computers that are used to host websites, meaning that they store the website files. These servers are connected to the giant network called the World Wide Web (to use 90’s lingo), or the Internet.
    
3. **Browsers** are programs that you run on your computer. They load the website files via your internet connection. Your computer is also known as the **client**, which connects to the **server**.
    

**Further reading**

* [How does the Internet work?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/How_does_the_Internet_work) — Mozilla Developer Network
    
* [What is the difference between webpage, website, web server, and search engine?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Pages_sites_servers_and_search_engines) — Mozilla Developer Network
    

### The 3 components that make up every website

As mentioned above, websites are made up of files, mainly HTML, CSS, and JavaScript files.

Let’s take a closer look at each of them:

#### **HTML or HyperText Markup Language**

HTML is the foundation of all websites. It’s the main file type that is loaded in your browser when you look at a website.

You can actually make a very very basic website just using HTML and no other types of files.

It won’t look very interesting, but that’s the minimum that you need for a website to be a website.

*(If you’re interested in the basics of HTML, you can check out a* [*video/blog tutorial*](https://coder-coder.com/how-to-make-simple-website-html/) *I have about that.)*

#### **CSS or Cascading Style Sheets**

Without CSS, a website will look as aesthetically pleasing as a Word document.

With CSS, you can add colors of all kinds, compelling fonts, and layout the website in pretty much any way you please.

You can even add animations and draw shapes using more advanced CSS.

#### **JavaScript**

JavaScript is a programming language that allows you to interact with elements on the website and to manipulate them.

While CSS adds style to HTML, JavaScript adds interactivity and makes a website more dynamic.

For example, you can use JavaScript to scroll to the top of the page when you click a button, or to build a slideshow with buttons to navigate through the images.

To work with HTML, CSS and JavaScript files, you’ll need to use a program on your computer called a code editor.

Which brings us to the next point:

### Which code editor should you use?

This is a very common question, especially if you’re just starting out.

The best code editor for you will be highly dependent on what kind of code you’re writing.

If you’re doing mainly HTML, CSS, and JavaScript, you could code in Windows Notepad or TextEdit for Macs if you wanted to.

But what would the fun be in that?

Code editor programs like Sublime or VS Code come with a lot of features that just make coding easier.

They allow you to indent multiple lines of text right or left, and can highlight the text in different ways depending on what language the file is in.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JCnyi8HTMhlUNX3Ym16S8A.jpeg align="left")

*Example of syntax highlighting in VS Code*

For back-end languages (we’ll get into those in a later section) you’ll need a more powerful code editor called an IDE (Integrated Development Environment). IDEs have features that allow you to debug and compile (process) your code.

Here are some popular code editors:

![Image](https://cdn-media-1.freecodecamp.org/images/0*z4FzNLD6u884XHFT.png align="left")

[**VS Code**](https://code.visualstudio.com/): This lightweight version of Visual Studio, Microsoft’s main IDE, is only a few years old but it’s gotten incredibly popular, due to its speed, ease of use, and powerful features. VS Code is my personal editor of choice, so I may be rather biased ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*XNya7s0zovmrqiRJ.png align="left")

[**Atom**](https://atom.io/)**:** Created by GitHub and advertised as a “hackable text editor,” Atom is a well-loved editor. One of its main strengths is its customizability. You can install packages and themes that will add features to the program.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Qb5K88ZRZ2d9JP-m.png align="left")

[**Sublime**](https://www.sublimetext.com/): A hugely popular program that has been around for a while. Like Atom, you can install packages and themes, and it also has quick performance. Unlike the other two editors, a Sublime license costs $70 (but it is free to try).

I’d recommend trying some or all of these editors out, for comparison’s sake. Then pick one and stick to it, learning its features and shortcut keys.

### Version control

Now you have your code editor, and you’re starting to write code.

However what happens if you make a mistake in your code, and pressing Ctrl-Z to undo a million times isn’t working for you? What do you do?

The answer, is version control!

**Version control is like having save points for your code files.**

If you think you might be about to make some code changes that could break everything, you can create a new save point (called a commit).

Then if you do break your website, you can revert your code back to the state it was in before.

It can be a lifesaver if you ever make a mistake that you desperately need to undo.

**Version control sounds great! How does it work?**

Using a [version control system](https://www.atlassian.com/git/tutorials/what-is-version-control) (VCS) involves storing your code files and the entire history of changes in what’s called a repository.

Usually you will use one repository per website or project.

Then you store your repository online in what’s known as a **central repository**, and also keep a version on your computer in a **local repository**.

As you make changes on your computer, you can create commits and then push them up to the central repository.

This process allows you to have multiple people working on the same set of code, even changing the same files.

**Git is the most popular VCS right now**

The main version control system nowadays is [Git](https://git-scm.com/). Its main competitor is [Subversion](https://subversion.apache.org/) (SVN), an older system.

But the vast majority of coding bootcamps and tutorials will use Git, so that’s what I’d recommend that you learn.

**Further reading**

* [Quick tutorial on the very basics of using Git](https://try.github.io/levels/1/challenges/1)
    
* [In-depth guide to using GitHub](https://guides.github.com/activities/hello-world/)
    

Now, as we move into explaining the actual languages and frameworks that are used, we’ll be using terms that you’ve probably come across already: **front end and back end**.

### The front end is all about how the website looks, visually.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1ZgqE7dZv3rSaRT2.gif align="left")

\_\[Sarah Maes via GIPHY\](https://giphy.com/sarahmaes/" rel="noopener" target="*blank" title=")*

The front end (or client-side) refers to what is loaded by the user’s browser, also called the client.

This would be the HTML and CSS that we started out talking about. JavaScript was originally just a front-end language, but nowadays you can use JavaScript as your server-side, or back-end, language also.

**Front-end work deals heavily with making the website look good.**

In addition, it also involves making the site behave in a way that makes sense to the user (also called UX or user experience).

If you enjoy tweaking your CSS to make sure the site is pixel perfect, and adding subtle JavaScript animations that help the user along, then you will likely enjoy front-end development.

### The back end is all about functionality and making sure everything works.

While the front end is about the appearance and visual behavior of the website, the back end is about getting everything to work behind the scenes.

If you’re working in back-end development, you’ll be doing tasks like handling requests to the server and database.

Some examples of back-end work would be saving the data when someone fills out a form on the contact page, or retrieving data to display blog posts in a specific category that the user has requested.

Back-end work also may involve setting up the website on a server, handling deployment, and setting up SQL databases.

If the idea of setting up all the functional parts of a website sounds fun to you, you may enjoy back-end work!

### Putting both sides together

The names front-end and back-end came about because the front-end is what you can see in your browser.

And the back-end is the part that you can’t see, but it handles a lot of the heavy lifting and functionality that helps the front-end.

You can think about the front-end as the storefront of a business, the only part that most customers will see. The back-end is like the manufacturing, distribution, and operation centers that help the store run.

Both serve separate functions that are are equally important.

### Front end, back end, or full stack?

In web development, you can focus on just the front end, or just the back end. Or you can deal in both, which is called full stack development.

What you choose to focus on should mainly depend on two things:

* **Your personal preference:** Not everyone likes both front and back end.
    
* **Job availability:** Browse your local job listings and get involved with local coding meetups to get a feel for what types of jobs there are.
    

It’s worth mentioning that if you enjoy both front and back end, being a full stack developer will make you more marketable.

It makes sense — the more technologies you can work with, the more tasks you will be able to perform.

Stack Overflow reported in their [2017 survey of users](https://insights.stackoverflow.com/survey/2017#developer-profile-specific-developer-types) that 63.7% identified as full-stack, 24.4% as back-end, and 11.9% as front-end developers:

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYtHdEZA9xAiq_ys3Z9ArQ.png align="left")

\_Source: \[Stack Overflow 2017 Survey\](https://insights.stackoverflow.com/survey/2017#developer-profile-specific-developer-types" rel="noopener" target="*blank" title=")*

However again, this will be heavily dependent on the company. Some companies may utilize full stack developers, where others split the back and front ends.

Some also have their front-end developers spill over into design, where the developers will design and build the front end of the application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y3XK4wTNDRfVtdBhVD0nlw.png align="left")

### Part 2: Making your front-end skills shine

Once you’ve gotten the basics of HTML, CSS, and JavaScript down, you can start getting into more advanced skills in the front-end.

This section will go through practices and tools that will help you build more marketable skills as a web developer.

### Responsive design is a must in this mobile-friendly world

When websites were first around, there was only one way to view them: on your computer.

Smartphones and mobile data didn’t really exist yet. When making a website you only had to worry about how it looked on your computer.

Now, according to [Statcounter.com](http://gs.statcounter.com/press/mobile-and-tablet-internet-usage-exceeds-desktop-for-first-time-worldwide), more people are using their phones than their desktop computers to browse the internet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LJTR6eQvxIwaQZj4yN4MDQ.png align="left")

So we need to make sure that all our websites work and look good on everything from the biggest monitor to the smallest phone.

This practice is what’s known as **responsive design**. It’s called that because the design can “respond” to any device that is viewing it.

You can test how responsive a website is by manually changing the width of your browser window and seeing how the design looks at large and small widths.

Building a truly responsive website involves a lot of planning in the design phase to consider how everything will look on all devices. And in the web development stage, it involves using media queries to control which CSS properties are being used at specific widths.

### Frameworks can help you build a responsive website quickly

As you might imagine, coding all the CSS of a responsive website takes a lot of work.

If you can’t spare a lot of extra time, you might try using a responsive framework like [Bootstrap](https://getbootstrap.com/) or [Zurb Foundation](https://foundation.zurb.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*q2QUM3sANJz1ez4o0-SVew.png align="left")

\_Example of a page you can create with \[Bootstrap\](https://getbootstrap.com/docs/4.0/examples/" rel="noopener" target="*blank" title=")*

The beauty of these frameworks is that they come pre-packaged with custom CSS and JavaScript. They’ve done a lot of work for you by pre-styling elements like headlines and buttons.

They also come with JavaScript components (essentially little plugins) like modal pop-up windows and navigation bars.

Since you’re using something that’s already been tested, it will make building your website a lot easier. The only caveat is that you shouldn’t become too dependent on frameworks.

**There’s no substitute for knowing how to build a responsive website from scratch.**

**Further reading**

* [Examples of responsive design from Designmodo.com](https://designmodo.com/responsive-design-examples/)
    
* [Responsive Web Design Basics from Google](https://developers.google.com/web/fundamentals/design-and-ux/responsive/)
    
* [Bootstrap 4 tutorial from W3Schools](https://www.w3schools.com/bootstrap4/bootstrap_get_started.asp)
    
* [Zurb Foundation Tutorials](https://foundation.zurb.com/learn/tutorials.html)
    

### Sass will save you time and headaches when writing CSS

Once you’ve gotten the basics of CSS down, I would start to learn [Sass](http://sass-lang.com/), because it is simply awesome.

It’s even in the name! Sass stands for “Syntactically Awesome Style Sheets.” And it’s described on its website as [“an extension of CSS.”](http://sass-lang.com/documentation/file.SASS_REFERENCE.html)

**It makes writing your CSS styles much easier, more intuitive, and faster.**

Don’t get me wrong, CSS is great. But as you get into it, you’ll realize that regular vanilla CSS can get quite tedious. And, if you aren’t super organized in how you write your styles, your CSS styles can quickly become frustratingly tangled.

**What Sass does is give you more power and control.**

Here are a couple examples of how Sass will make your life easier:

* **Mixins**: Instead of copying and pasting the CSS code for certain elements a million times, you can use mixins. They allow you to write a set of styles for an element just once, and reuse as many times as you want.
    
* **Nesting:** Instead of writing all the parent classes of a specific style, you can nest all the children inside the parent’s styles. This also cuts down on a lot of duplicate work.
    

![Image](https://cdn-media-1.freecodecamp.org/images/1*QeU_j0ZkguS_Sqyzc5hJcg.png align="left")

*Here’s an example of using nesting in Sass.*

In short, using Sass will save you time and annoyance. Well worth the effort it takes to learn it!

**Further reading**

* [Getting started with Sass](http://thesassway.com/beginner/getting-started-with-sass-and-compass)
    
* [Sass Basics](http://sass-lang.com/guide)
    

One note: since the browser can’t read Sass files itself, you have to compile your Sass files into CSS.

In order to do this, you’ll have to use something called a build tool and run it on your computer.

Which brings us to the next section….

### What are all these build tools about, anyway?

![Image](https://cdn-media-1.freecodecamp.org/images/1*f5D9s0KsC4sIauxLEz9oUg.png align="left")

You’ve probably heard one or several of the following terms: npm, Webpack, Grunt, Gulp, Bower, Yarn… the list gets pretty long!

These tools are often described as build tools, task runners, task managers, or *“NOW what do I have to install?!”*

### Some tools do your grunt work (pun intended!) for you

Build tools like [Grunt](https://gruntjs.com/), [Gulp](https://gulpjs.com/), and [Webpack](https://webpack.js.org/) are commonly used to do some of the following tasks:

* **Processing** Sass files into CSS
    
* **Concatenating** (combining) multiple CSS files or multiple JavaScript files into one big CSS or JavaScript file.
    
* **Minifying** (compressing) CSS, JavaScript, and even image files
    
* **Automatically refreshing** your browser with the updated CSS or JavaScript code
    

Sure, many of these tasks you could do yourself by hand.

But having to do it over and over again every time you make a small CSS or JavaScript change gets tiring.

### Which build tool should you use?

At the moment, Webpack is taking over the field, but Grunt and Gulp are still in use.

I would definitely learn Webpack, but it couldn’t hurt to learn either Grunt or Gulp (Gulp is faster and seems a bit easier to get up and running).

### Other tools install packages (plugins) for you

![Image](https://cdn-media-1.freecodecamp.org/images/1*g_5-PNq-uB6f1ooeD-7gNA.png align="left")

In addition, in order to accomplish all those tasks, you generally need to download and install plugins or packages.

This is where a tool like [npm](https://www.npmjs.com/) (Node Package Manager), [Bower](https://bower.io/), or [Yarn](https://yarnpkg.com/en/) comes in handy. These are tools that allow you to quickly install packages to your computer by typing commands into your computer’s command line.

They’re tools to get you more tools, basically!

As **npm** is the dominant package manager right now, you should definitely learn how to use it.

**Bower** was one of the first package manager tools, but it’s officially obsolete– the creators of Bower.io now recommend using Yarn.

**Yarn** is a very npm-like tool created by Google, Facebook, and others that [promises to fix](https://scotch.io/tutorials/yarn-package-manager-an-improvement-over-npm) some of the issues that npm has.

While Yarn is in the minority, I’d still recommend checking it out, as it seems to be gaining in popularity.

**Further reading**

* [How to setup Webpack +2.0 from scratch](https://codeburst.io/easy-guide-for-webpack-2-0-from-scratch-fe508a3ce44e)
    
* [Javascript Tooling — The Evolution and Future of JS & Front-end Build Tools](https://blog.qmo.io/javascript-tooling-the-evolution-and-future-of-js-front-end-build-tools/)
    
* [NPM vs Yarn Cheat Sheet](https://shift.infinite.red/npm-vs-yarn-cheat-sheet-8755b092e5cc)
    

### Everyone loves JavaScript frameworks

You’ve probably noticed a lot of JavaScript frameworks, libraries, toolkits, and so on being thrown around… you know, those names that all end in “.JS?”

Let’s first take a step back and define just what a JavaScript framework is.

Depending on whom you talk to, the terms framework, library, and/or toolkit may or may not be interchangeable. ([It’s still under debate.](https://stackoverflow.com/questions/148747/what-is-the-difference-between-a-framework-and-a-library))

But they’re all essentially tools that, surprise surprise, do some of the work for you.

#### A framework is a pre-built structure that you build upon.

Generally speaking, a framework is a system of working parts created by someone else.

To use the framework, you install it to your own website files. Then you work off of that existing structure, adding onto it to accomplish what you want to do.

Using a framework is like buying a bare bones house that comes with all the structural components (foundation, frame, roof), but isn’t totally complete.

You still need to go in and attach the water and electricity, as well as install cabinets, paint the walls, and decorate.

Some examples of JavaScript front-end frameworks are [React](https://reactjs.org/), [Vue](https://vuejs.org/), and [Angular](https://angular.io/).

#### A library is a set of pre-made tools that you add to your own structure.

In comparison, a library is a collection of individual components that you can take and plug in to your own system.

> **This is the main difference between frameworks and libraries:**

> While frameworks are pre-made structures, libraries aren’t a structure in themselves. They provide additional functionality for existing systems.

To continue the home building analogy, you can think of libraries like appliances that you choose to add to your house.

Machines like ovens, showers, and air conditioners all perform a distinct function, but you have to install them into an existing home in order for them to be useful.

One example of a library, using the above categorization, is jQuery.

[jQuery](http://jquery.com/) is a JavaScript library that doesn’t have any kind of structure in itself, but has over [300 different functions](http://api.jquery.com/) that you can use.

**Again, these definitions are not agreed upon by everyone.**

React and jQuery categorize themselves as libraries, and Angular and Vue call themselves frameworks.

However for my own personal understanding, it helps to separate the tools into these two general buckets of frameworks (systems) and libraries (tools).

Which brings us to our next point…

### The big three in JavaScript frameworks: Angular, React, and Vue

![Image](https://cdn-media-1.freecodecamp.org/images/1*8lqOL3IOvK879eu64unZCA.png align="left")

In the early 2010’s there was an explosion of frameworks ending in “.js,” almost a new one every month.

However as we approach 2020, the field has cleared and we’re left with the three big winners: Angular, React, and Vue.

**JavaScript frameworks may have started out as a trend, but they’re definitely here to stay.**

Angular, React, and Vue are all growing, and JavaScript itself is extremely popular right now– [it’s the most used technology](https://insights.stackoverflow.com/survey/2017#most-popular-technologies) for the fifth year running in Stack Overflow’s annual survey.

In addition, Stack Overflow publishes trends of technologies based on how many questions are asked per month.

You can see that Angular has the most volume, and both Angular and React have had pretty steep growth over the past year.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z2fsSGzW1zz8BZwaku8CCg.png align="left")

\_Source: Stack Overflow — \[JavaScript Framework Trends\](https://insights.stackoverflow.com/trends?utm\_source=so-owned&utm\_medium=blog&utm\_campaign=trends&utm\_content=blog-link&tags=angularjs%2Cangular%2Creactjs%2Cvue.js" rel="noopener" target="*blank" title=")*

[The State of JavaScript survey](https://stateofjs.com/2017/front-end/results) shows that React leads in the number of developers who have used it and loved it, while Angular doesn’t seem to be quite as interesting or hold as much desire for reuse.

Vue has a lower amount of actual usage, but is leading the pack in terms of being a technology that developers want to try in the future. So it’s feasible that Vue could become a bigger player in the next couple of years.

However I think all three are sticking around, at least for the next several years.

### TL,DR: Which framework should I learn right now?

It depends– if you’re seeking to land a full-time web developer job, I would browse your local job listings to see which framework seems to get mentioned the most.

If you’re just learning right now without that specific end in mind, Vue is a good place to start for beginners. It’s lightweight and documented quite well.

However, I personally wouldn’t only learn Vue. It would be a good idea to eventually add either React or Angular to your toolbelt, depending on your liking.

**Further reading**

* [Best JavaScript Frameworks, Libraries and Tools to use in 2017](https://www.sitepoint.com/top-javascript-frameworks-libraries-tools-use/)
    
* [The Noob’s Guide to Choosing a JavaScript Framework](https://webdesign.tutsplus.com/tutorials/the-noobs-guide-to-choosing-a-javascript-framework--cms-28538)
    

![Image](https://cdn-media-1.freecodecamp.org/images/1*QXYhx3P_IUMHLyZQniVbVA.png align="left")

### Part 3: Let’s get into the back-end

#### Which language should you learn first?

There are a ton of back-end languages. Many of them have been around for quite a while, some even before the internet existed!

This can make it difficult to choose which language to start out with. To narrow down your choices, I’d recommend applying the following principles to your decision:

* Choose a language that is **learnable**: it has a reasonable learning curve, is well-documented, and/or has a good online support system.
    
* Choose a language that is **relevant** to your eventual career goals.
    
* Choose a language that is **enjoyable**. Learning web development is hard enough — there’s no point in forcing yourself to learn a language that you really don’t like.
    

> **One important thing to keep in mind is that you don’t have to learn every language.**

> In fact, if you’re a beginner I would strongly recommend that you focus on one language first.

**All programming languages share some common principles.**

For example, you can write a “for” loop in JavaScript, PHP, C# and Python.

Once you’ve picked up the fundamental principles of programming in your first language, it will be easier to transfer those concepts into other languages.

I hope this takes off a little pressure from choosing your first back-end language to learn ?

### Let’s take a look at some of the most popular back-end languages.

**Java**

[Java](https://www.oracle.com/java/index.html) is a stable language that is very widely used and has been around a long time. It has held the top spot on the [TIOBE index](https://www.tiobe.com/tiobe-index/) since 2001. (TIOBE is a ranking of programming languages by number of searches.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*HqJzc1ZlB4pBPQgBfXPYWg.png align="left")

\_Source: \[Stackify.com\](https://twitter.com/benjaminputano" rel="noopener" target="\_blank" title=""&gt;Ben Putano on &lt;a href="https://stackify.com/popular-programming-languages-2018/" rel="noopener" target="*blank" title=")*

In addition, Java ranked third in Stack Overflow’s rankings of the [most commonly used languages](https://insights.stackoverflow.com/survey/2017#technology-programming-languages) and has the second-highest [tagged questions](https://stackoverflow.com/tags) on Stack Overflow.

![Image](https://cdn-media-1.freecodecamp.org/images/1*68BlQUD0zRq2YGf__-O2Vg.png align="left")

\_Source: \[Most Common Programming Languages\](https://insights.stackoverflow.com/survey/2017#technology-programming-languages" rel="noopener" target="*blank" title="), Stack Overflow Developer Survey 2017*

Many big tech companies [use Java](https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites) in their websites: Google, YouTube, Facebook, Amazon, and Twitter, among others.

One reason for this is that Java is fast, and can scale up to handle large websites. It’s also a consistent language that allows for easier maintenance for [long-term projects](https://www.upwork.com/hiring/development/the-java-platform/).

Twitter was originally built with Ruby on Rails. But in 2015 they needed to be able to support their huge growth, so they [switched to Scala](https://www.quora.com/Why-did-Twitter-switch-to-a-Java-based-front-end-after-successfully-using-Ruby-on-Rails-with-200-million-users), a language that runs on the Java Virtual Machine.

**C# (C Sharp)**

[C#](https://docs.microsoft.com/en-us/dotnet/csharp/getting-started/introduction-to-the-csharp-language-and-the-net-framework) was created by Microsoft to be a competitor to Java. You can see that C# peaked on Stack Overflow’s Trends in 2009 and has been on the decline ever since.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ddhjNfjMedPiY8QK_6Z6Cw.png align="left")

\_Source: Stack Overflow \[trends for back-end languages\](https://insights.stackoverflow.com/trends?utm\_source=so-owned&utm\_medium=blog&utm\_campaign=trends&utm\_content=blog-link&tags=java%2Cpython%2Cc%23%2Cjavascript%2Cphp%2Cruby%2Cc%2B%2B%2Cnode.js" rel="noopener" target="*blank" title=")*

But I wouldn’t count C# out just yet.

It’s a powerful, object-oriented language that has the third highest number of [Stack Overflow tags](https://stackoverflow.com/tags). It also came in third in Stackify’s [research](https://stackify.com/popular-programming-languages-2018/) into the most in-demand languages in Indeed job listings in December of 2017.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uop6ItxTX3wFkTQnuFZOvA.png align="left")

\_Source: \[Stackify.com\](https://twitter.com/benjaminputano" rel="noopener" target="\_blank" title=""&gt;Ben Putano on &lt;a href="https://stackify.com/popular-programming-languages-2018/" rel="noopener" target="*blank" title=")*

C# is used in a wide variety of applications, such as Windows desktop apps and Android programming.

It’s also used a lot in game development, through the [Unity game engine](https://www.quora.com/What-is-unity-game-engine/answer/Harshal-B-Kolambe). So if you’re interested in Android or game development, C# would be a great option to learn.

**Node.js**

As mentioned earlier, JavaScript has been the most commonly used language reported by Stack Overflow users for the past five years.

A lot of this has to do with [Node.js](https://nodejs.org/en/), which topped their [list](https://insights.stackoverflow.com/survey/2017#technology-frameworks-libraries-and-other-technologies) of frameworks and libraries used the most in 2017.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VOHEKe0YQunX-g6USjpMVg.png align="left")

\_Source: \[Most Common Frameworks and Libraries\](https://insights.stackoverflow.com/survey/2017#technology-frameworks-libraries-and-other-technologies" rel="noopener" target="*blank" title="), Stack Overflow Developer Survey 2017*

Node.js, self-described as a “JavaScript runtime,” is basically JavaScript that runs on the back end.

It was originally meant to serve as a more efficient [alternative](https://www.infoworld.com/article/3210589/node-js/what-is-nodejs-javascript-runtime-explained.html) to the Apache HTTP server. Since its release in 2009, Node.js has steadily increased in usage, due to its fast, lightweight nature.

Node developers often use the [Express](https://expressjs.com/) framework when building web apps. Express.js is a “minimalist web framework” for Node.js.

By using Node and Express on the back end, and Angular or React on the front end, this means that you can be a full stack JavaScript developer.

This stack, or combination of technologies, is very popular at the moment, [especially with startups](https://codingvc.com/which-technologies-do-startups-use-an-exploration-of-angellist-data).

**Python**

[Python](https://www.python.org/) first came onto the scene in 1991 and is a frequent “first language” for many programming students.

Due to its [readability](https://en.wikipedia.org/wiki/Python_\(programming_language\)) and use of English keywords, it’s generally considered an easy language to learn.

There are a couple of Python frameworks that you can use:

* [Django](https://www.djangoproject.com/) (pre-built features, more bells and whistles), and
    
* [Flask](http://flask.pocoo.org/) (more minimal and flexible).
    

Python’s popularity has soared in recent years. As of this writing, it is [ranked #4](https://www.tiobe.com/tiobe-index/) on the TIOBE index.

And in 2017 it was ranked second in the number of pull requests on GitHub, according to their [2017 Year in Review report](https://octoverse.github.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*FK5xi-zleQCUafgucPamlw.png align="left")

\_Source: \[Stackify.com\](https://twitter.com/benjaminputano" rel="noopener" target="\_blank" title=""&gt;Ben Putano on &lt;a href="https://stackify.com/popular-programming-languages-2018/" rel="noopener" target="*blank" title=")*

Stack Overflow [reported](https://stackoverflow.blog/2017/09/14/python-growing-quickly/) last September that data science, machine learning and academic research are largely the reason for this fast growth.

Even if you’re not a data scientist, being able to work with and manipulate data is becoming a useful skill.

As Alexus Strong of Code Academy [writes](http://news.codecademy.com/why-learn-python/):

> “Python is appealing to those of us in non-technical fields because it puts data analysis \[…\] within arm’s reach.”

If you’re curious about data science or machine learning, Python may be a very good bet for you, as these fields will likely expand in the coming years.

**Ruby**

[Ruby](https://en.wikipedia.org/wiki/Ruby_\(programming_language\)) was first released in 1995. It started getting a lot of attention in the early 2000s when the startup [Basecamp](https://basecamp.com/about) invented the framework [Ruby on Rails](http://rubyonrails.org/).

Combined with Ruby’s beginner-friendly syntax and readability, Rails made building web apps very quick and easy.

Ruby on Rails grew in popularity and became the framework of choice for startups. (Codepen.io, GitHub, and [Shopify](https://basecamp.com/about) [all use](https://w3techs.com/technologies/details/pl-ruby/all/all) Ruby on Rails.)

However, Ruby was never one of the heavy hitters. Last year it came in tenth place both in Stack Overflow’s most commonly used language [rankings](https://insights.stackoverflow.com/survey/2017#technology-programming-languages), and the [TIOBE index](https://www.tiobe.com/tiobe-index/).

In addition, Ruby on Rails doesn’t scale very well, leading to those startups eventually switching to other languages when they get really big (like Twitter switching to Java, as we mentioned above).

It may not be topping the rankings, but Ruby could still be a good choice for your first language to learn.

If you’re interested in the startup world or your geographic area has a lot of Ruby jobs, I would consider learning Ruby and Ruby on Rails.

**PHP**

[PHP](http://php.net/manual/en/intro-whatis.php) is a language that a lot of people love to hate.

However, despite the number of Quora questions [asking if PHP is dead](https://www.quora.com/Is-PHP-dead-What-is-the-job-outlook-and-future-of-PHP-in-the-next-five-years), the fact remains that PHP is the most widely used back-end language today.

Research done by [W3Techs.com](https://w3techs.com/technologies/overview/programming_language/all) shows that 83% of all websites use PHP. (The next highest language , ASP.NET, comprises only 14%.)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wsn6WoqlDCLANKqny2TzIw.png align="left")

\_Source: \[W3Techs.com\](https://w3techs.com/technologies/overview/programming\_language/all" rel="noopener" target="*blank" title=")*

Content management systems (CMSs) are a major reason for the large market share of PHP. The [top three CMSs](https://w3techs.com/technologies/overview/content_management/all) — WordPress, Joomla, and Drupal — are all built with PHP.

WordPress itself has the lion’s share of the CMS market, making up [29.5% of all websites](https://w3techs.com/technologies/overview/content_management/all).

If you like working with it, WordPress development may be a good area of focus for customizing websites and building plugins or themes.

In addition to content management systems, PHP has some frameworks that make development easier and quicker. [Laravel](https://laravel.com/), a framework that came out in 2011, is currently the most popular one.

**Further reading**

* [A Beginner’s Guide to Back-End Development (Upwork.com)](https://www.upwork.com/hiring/development/a-beginners-guide-to-back-end-development/)
    
* [Server-side web frameworks (Mozilla Developer Network)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps/Web_frameworks)
    
* [What is the Best Programming Language for Me?](http://www.bestprogramminglanguagefor.me/)
    

### Working with data and databases

![Image](https://cdn-media-1.freecodecamp.org/images/0*tMc9X0KyVDJNRf2Q.gif align="left")

\_Source: \[Sherchle \](https://giphy.com/gifs/art-design-illustration-l0HlN5Y28D9MzzcRy" rel="noopener" target="*blank" title=")via GIPHY*

Databases can seem intimidating if you’re not familiar with them.

However, if you think about it, you’ve probably worked with and used data in your own life at some point.

If you’ve ever used Excel to organize data, or created a chart to track your goals, then you’ve done a similar (albeit much simpler) function that databases do.

### What do I need to learn to use databases?

Fortunately, you don’t need to learn a ton of different languages. The main database language is [SQL](https://en.wikipedia.org/wiki/SQL) (pronounced *sequel*).

SQL (Structured Query Language) was [created](https://www.thebalance.com/what-is-sql-and-uses-2071909) in the 1970s by IBM, and is used in [relational databases](https://en.wikipedia.org/wiki/Relational_database).

The relational model is a way of structuring data into rows and columns (think like an Excel spreadsheet).

Each column is designated for a certain kind of data, and it may require that the data is formatted correctly. And each row, or record, contains a unique ID or key in addition to the column, or field, values.

You can see this below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*axy8IyyF8aiv3NKDQk5QBw.png align="left")

*A simple spreadsheet similar to how data is stored in a table. The Rent column would require numeric values.*

The records are then stored in multiple collections called tables. And a collection of tables (among other things) makes up the entire database schema, or structure.

The main types of SQL database systems are:

* [MySQL](https://www.mysql.com/) (used for PHP and open source applications)
    
* [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-2017) (generally used for .NET applications)
    
* [PostgreSQL](https://www.postgresql.org/) (open source)
    

**NoSQL**

Even though SQL is the dominant type of database, there is another type: NoSQL (i.e. non-SQL). As the name implies, NoSQL databases are in some ways opposite of traditional SQL ones.

[NoSQL](https://en.wikipedia.org/wiki/NoSQL) is not relational, and [doesn’t enforce](https://www.infoworld.com/article/3240644/nosql/what-is-nosql-nosql-databases-explained.html) the same type of structure that SQL does. Instead, you can store any kind of data in a freer, more flexible type of system.

This creates much faster processes and is much better at scaling up for large, complex applications. The downside is that you sacrifice data consistency.

As Craig Buckler of Sitepoint [writes](https://www.sitepoint.com/sql-vs-nosql-differences/):

> NoSQL is more flexible and forgiving, but being able to store any data anywhere can lead to consistency issues.

NoSQL rose in popularity in the 2000s due to large tech companies like Facebook and Amazon needing a fast way to manipulate and store data.

[MongoDB](https://www.mongodb.com/) is the most commonly used NoSQL system. The other top types are Cassandra, Elasticsearch, and Couchbase, according to [Hackernoon](https://hackernoon.com/top-4-nosql-databases-infographic-b6acc389befc).

**SQL vs NoSQL?**

You may run across discussions on whether NoSQL is replacing SQL, or which one is better. The truth is that both types of databases have their strengths and weaknesses.

Like anything else, the right choice will change depending on the project, and the job. Personally, I would recommend learning the basics of both SQL and NoSQL.

**Further reading**

* [History of SQL](https://www.thebalance.com/what-is-sql-and-uses-2071909) — TheBalance.com
    
* [SQLCourse.com](http://www.sqlcourse.com/intro.html) — free online tutorial about SQL
    
* [SQL vs NoSQL Difference](https://medium.com/xplenty-blog/the-sql-vs-nosql-difference-mysql-vs-mongodb-32c9980e67b2) — XplentyBlog
    
* [NoSQL Explained](https://www.mongodb.com/nosql-explained) — MongoDB
    

### Creating websites on servers

![Image](https://cdn-media-1.freecodecamp.org/images/0*zZFtoXHQdZd2pZCC.gif align="left")

As we mentioned at the beginning, servers are simply computers that store website files and other resources like databases.

In order to have a website be accessible publicly on the internet, it needs to be installed on a server.

Here are some of the things that you’ll have to work with in order to create a live website:

#### **Domain name and SSL certificate**

Domain names are the address of the website, like Google.com, Wikipedia.org or Dartmouth.edu.

In order to get one, you’ll have to choose one that is available, then purchase it from a domain name registrar like [Namecheap.com](https://www.namecheap.com/) or [Google Domains](https://domains.google/#/).

These companies register the domains with [ICANN](https://en.wikipedia.org/wiki/ICANN) (Internet Corporation for Assigned Names and Numbers).

ICANN is a centralized organization that oversees and manages the DNS (domain name system) and IP (internet protocol) areas of the global internet.

In addition to the domain name, you should also get an SSL (Secure Sockets Layer) certificate for your domain. SSL will [encrypt the traffic](https://www.digicert.com/ssl/) on your website, which will help protect it from cyber attacks.

#### **Web host server space**

![Image](https://cdn-media-1.freecodecamp.org/images/1*XgwG8TIIqH_6RHDMiOO6ew.jpeg align="left")

Once you have your domain name to *AwesomeStupendousAmazingSite.com*, you’ll need to purchase server space.

There are a few different levels of web hosting plans:

* **Shared servers**: The cheapest option, can range from a few dollars to $12–20 per month. Like it sounds, you share your server space with other website “neighbors.” Upside is the affordability, and downside is slower speeds and possible downtime if you exceed your usage for the month. Popular hosts are [SiteGround](https://www.siteground.com/), [Bluehost](https://www.bluehost.com/), and [WP Engine](https://wpengine.com/).
    
* **Cloud servers:** [Cloud hosting](https://www.interoute.com/what-cloud-hosting) is a relatively new option. It consists of a system of a large number of physical servers whose resources are all shared. Each individual “tenant” is then given a virtual server that pulls resources from the collective pool. This setup allows for more flexibility for bandwidth and can scale up very quickly. One company, [Digital Ocean](https://www.digitalocean.com/), deals exclusively with cloud servers. Pricing depends on your server specs, and can range from a few dollars a month all the way up to almost $1000.
    
* **VPS (Virtual Private Servers):** VPSs are similar to cloud hosting in that each tenant has their own virtual server, and all tenants share one physical server. It’s better than shared hosting because you are allocated your own slice of the server resources. This option is a bit more expensive, between $20–60 per month (according to [BlueHost](https://www.bluehost.com/products/vps)).
    
* **Dedicated servers:** These servers give you one complete physical server all to yourself. As you might imagine, this option is the most powerful but also the most expensive. They often also are managed servers, meaning the company will run maintenance and do other tasks for you. Dedicated hosting will generally run you a couple to a few hundred dollars per month, according to SiteGround pricing.
    

#### **Server setup and maintenance**

Once you have your domain name and server space, you’ll have to set up your site on the server.

This involves directing your domain name to your server’s unique IP address, setting up your website files and database (if necessary), and other configurations.

How much work you have to do will depend on type of server plan you purchased from your web host. The simplest shared plans often come with one-click features that will automatically install WordPress, Drupal, or other sites for you.

Other servers, like Digital Ocean, are very minimal and require you to set everything up manually.

#### **Deploying files to your server**

You might be wondering how you get files from your own computer up to your server. You can accomplish this by using a [protocol](https://en.wikipedia.org/wiki/Communication_protocol), which is basically a method of transporting files or other data to and from a server.

> **Side note:**  
> HTTP, the way that your browser loads websites, is also a protocol– HTTP stands for Hypertext Transfer Protocol.

The most simple way is by using a protocol called [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) (File Transfer Protocol). However it’s not recommended to use FTP anymore, because it is not secure (encrypted).

Nowadays most people use more secure protocols FTPS (FTP over SSL) or SFTP (Secure SHell FTP).

To get FTP/SFTP working, you need to create an account on your server. You’ll then connect to the server using the IP address of the server, and a username and password login for authentication.

In order to transfer files over FTP/SFTP you can use programs like [Filezilla](https://filezilla-project.org/) or [CyberDuck](https://cyberduck.io/). These have a GUI (graphical user interface) that makes it relatively easy to upload and download files to and from your computer and your server.

#### **Deployment tools**

![Image](https://cdn-media-1.freecodecamp.org/images/1*1jvILZIbneS98ISyxfynXQ.jpeg align="left")

As you might imagine, having to manually upload files to your server every time you make one little code change can get tedious. In addition, things can get confusing if multiple people are working on the same file and uploading simultaneously.

Fortunately, you can set up deployments that link into your Git repository.

The deployment tool stores your FTP/SFTP settings, and when you push a change in Git to your master branch, for example, the tool will transfer the files for you. That way you don’t need to remember which files you changed, reducing the number of mistakes you make.

For more complex websites that have a team with several people, there are more advanced deployment tools and systems that you can use to make your deployments more structured.

These systems are beyond the scope of this article, but they include practices such as [continuous integration](https://aws.amazon.com/devops/continuous-integration/).

**Further reading**

* [Domain Name Registration process](https://whois.icann.org/en/domain-name-registration-process) — WHOIS
    
* [8 Popular Types of Web Hosting Services](https://www.thebalance.com/types-of-web-hosting-services-2532072) — TheBalance.com
    
* [6 Best FTP Clients](http://www.wpbeginner.com/showcase/6-best-ftp-clients-for-wordpress-users/) — WP Beginner
    
* [Continuous integration vs. continuous delivery vs. continuous deployment](https://www.atlassian.com/continuous-delivery/ci-vs-ci-vs-cd) — Atlassian
    

### Congrats!!

![Image](https://cdn-media-1.freecodecamp.org/images/0*hDquyfV9gO45z7Vf.gif align="left")

You’ve made it through!

Now before we continue to the resource list, please note that the following section contains some affiliate links. This means I will receive a small commission from the company if you purchase through the link.

It’s an easy way that you can support writing these types of articles, at no extra cost to yourself. (I’ve also included non-affiliate links as well, if you’d prefer to use that.)

### Epilogue: Recommended learning resources

As I’m sure you know, there are a ton of resources that you can use to learn code.

I’ve included some of the most popular and recommended online tutorials, books, and other resources here.

### Complete web development courses

There are a few online courses that cover all or very close to all of the areas of web development.

If you don’t want to jump around and just want to focus on one place to learn everything, I’d recommend one or more of the following:

![Image](https://cdn-media-1.freecodecamp.org/images/1*YPpb4B_k1FehpeRNxDApzw.png align="left")

[**freeCodeCamp**](https://www.freecodecamp.org/) is a non-profit that offers completely free education for aspiring web developers.

Their curriculum is a comprehensive set of courses ranging from front to back end (using Node and Express) and more!

Many people have landed full-time jobs after taking freeCodeCamp. You can also contribute to [open source projects](https://www.freecodecamp.org/nonprofits/) via GitHub.

One of the main perks of freeCodeCamp is that it’s very community-centered, with message boards and Facebook groups, so you’re able to get a lot of support as you learn.

You can read some reviews of freeCodeCamp on [Quora](https://www.quora.com/How-did-Free-Code-Camp-change-your-life) and [Reddit](https://www.reddit.com/r/learnprogramming/comments/4cen3v/a_review_of_freecodecamp_the_first_25_hours_from/).

![Image](https://cdn-media-1.freecodecamp.org/images/0*4nEbzCm3SWCGX_jJ.png align="left")

**Colt Steele’s Web Developer Bootcamp** *(*[*affiliate link*](https://www.udemy.com/the-web-developer-bootcamp/?siteID=T4jMTDexBoM-4eq5n6HlbL7PAfBCL8SWqw&LSNPUBID=T4jMTDexBoM) */* [*non-affiliate link*](https://www.udemy.com/the-web-developer-bootcamp/)*)*

Colt is a former coding bootcamp instructor who wanted to offer a complete bootcamp for a fraction of the price.

He ended up creating one of the most popular and well-rated web developer courses on Udemy, and with good reason.

His course takes you from the basics through full-stack development (using Node and Express as the back-end), with a lot of content and is updated frequently.

You can read [reviews](https://www.udemy.com/the-web-developer-bootcamp/#reviews) of his course on the Udemy page, as well as on a freeCodeCamp [forum post](https://forum.freecodecamp.org/t/the-web-developer-bootcamp-udemy-review/61595/4).

![Image](https://cdn-media-1.freecodecamp.org/images/0*8mRX8qP022AC1ygz.png align="left")

**Udacity** offers both [free courses](https://www.udacity.com/courses/web-development) and paid programs called [Nanodegrees](https://www.udacity.com/nanodegree).

The Nanodegrees build off of the free courses– they are intensive (12 hrs/week) programs where you build portfolio projects and have more community interaction and support.

They’re not cheap, currently $199/mth and it may take you between 6 to 10 hours to complete one.

If you’re interested, here are some reviews of Udacity’s Nanodegree programs on [Quora](https://www.quora.com/Are-Udacity-Nanodegrees-worth-it-for-finding-a-job) and [Hacker News](https://news.ycombinator.com/item?id=9313088), and [Quora answers](https://www.quora.com/What-is-the-difference-between-a-Udacity-nanodegree-degree-program-and-free-courses) about the difference between Udacity’s free courses vs Nanodegree.

### Other resources

![Image](https://cdn-media-1.freecodecamp.org/images/0*4v3jYDpiexq_tDvo.png align="left")

[**Team Treehouse**](https://teamtreehouse.com/tracks) is a very popular website for learning coding. They don’t have free content, but they use a subscription model.

Treehouse offers tiered monthly plans ($25 or $55/mth currently) and you can take unlimited courses.

You can even pause your membership if you want to take a break for a few months, and resume it later when you’re ready.

Aside from individual courses, they also have structured tracks like Java Web Development or Front End Web Development which guide you through a series of selected courses.

![Image](https://cdn-media-1.freecodecamp.org/images/0*eEoOMNC5kTo9Eoas.png align="left")

**Udemy** *(*[*affiliate link*](https://www.udemy.com/courses/development/web-development/?siteID=T4jMTDexBoM-BdAzoxv_nMbWPIUjULEsSg&LSNPUBID=T4jMTDexBoM) */* [*non-affiliate link*](https://www.udemy.com/courses/development/web-development)*)*

Udemy is one of the largest online learning platforms, and has courses not only in coding, but other professional and hobbyist areas.

You pay for each course individually, and they have frequent sales where course are anywhere from $10–20 each.

Of course, due to the large number of courses and instructors, they vary in quality, so you should do research before buying.

I’d recommend checking ratings and reviews both on the Udemy course page and elsewhere online.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ExV7N_TGY8rzoH5B.png align="left")

[**Wes Bos**](http://wesbos.com/courses/) is a web development instructor who has created quite a few very popular courses.

One course I’d definitely check out is **JavaScript30** *(*[*affiliate link*](https://javascript30.com/friend/CODERCODER) */* [*non-affliate link*](https://javascript30.com/)*)*. This is his free 30-day vanilla (meaning no frameworks or libraries) JavaScript coding challenge.

He also has premium courses on React, Node, and more advanced JavaScript on his website.

If you’re curious, here are some reviews of his courses on [Reddit](https://www.reddit.com/r/webdev/comments/69yd1g/wes_bos_learn_node_course_officially_launched/) and the [freeCodeCamp forum](https://forum.freecodecamp.org/t/want-to-learn-node-wes-bos-review/113286/13).

![Image](https://cdn-media-1.freecodecamp.org/images/1*a9ES6TeAXN-VtU7CjVB1MQ.png align="left")

[**Microsoft Virtual Academy**](https://mva.microsoft.com/) **(MVA)** has a collection of free online courses ranging from C# and Python to SQL Server and other areas like game development.

Some of their popular courses are [Introduction to Programming with Python](https://mva.microsoft.com/en-us/training-courses/introduction-to-programming-with-python-8360), [C# Fundamentals](https://mva.microsoft.com/en-US/training-courses/c-fundamentals-for-absolute-beginners-16169) and [SQL Database Fundamentals](https://mva.microsoft.com/en-US/training-courses/sql-database-fundamentals-16944) courses.

Here are a couple reviews of MVA courses on [Reddit](https://www.reddit.com/r/learnprogramming/comments/7kum1x/c_course_on_microsoft_virtual_academy_looks_to_be/) and [LinkedIn](https://www.linkedin.com/pulse/review-microsoft-virtual-academy-database-course-michelle-hoque).

![Image](https://cdn-media-1.freecodecamp.org/images/0*GkbtxAeIvIIUTz0q.png align="left")

[**SoloLearn**](https://www.sololearn.com/) has a unique approach to learning coding: you can learn not only from their website, but on their free mobile apps.

Some of their most popular courses are Python, C++, and Java.

They also have a StackOverflow type of message board that is quite active with questions and discussions.

If you’re curious, you can check out some reviews of SoloLearn on [Reddit](https://www.reddit.com/r/learnprogramming/comments/7tks7h/is_sololearn_a_good_app_for_learning_code/) and [Quora](https://www.quora.com/How-good-are-SoloLearn-courses-for-learning-programming-Do-their-certificates-have-any-credibility-if-mentioned-in-a-resume).

### Books

If you enjoy learning from books, or want some on hand as references, here is a short list of books that I thought would be good for beginners.

Some of them are free and available online for you to read, others are traditional paper books.

![Image](https://cdn-media-1.freecodecamp.org/images/0*O7xUZsT9qn-TGvvu.jpg align="left")

**HTML and CSS by Jon Duckett**  
*(*[*affiliate link*](http://amzn.to/2GNgyFt) */* [*non-affiliate link*](https://www.amazon.com/gp/product/1118008189)*)*

**JavaScript and JQuery by Jon Duckett**  
*(*[*affiliate link*](http://amzn.to/2EZOq1m) */* [*non-affiliate link*](https://www.amazon.com/gp/product/1118531647)*)*

Jon Duckett’s books are quite possibly the most popular books for beginner web developers.

They aren’t just plain textbooks, but are beautifully-designed books that use photos and illustrations to teach coding concepts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kk8_Xc9hFSRWZoYqHX1DVQ.jpeg align="left")

[**The Front-End Developer Handbook**](https://www.gitbook.com/book/frontendmasters/front-end-developer-handbook-2018/details) is a free online book from [Frontend Masters](https://frontendmasters.com/) and written by [Cody Lindley](http://codylindley.com/).

It’s updated yearly and you can think of it as a “state of front-end web development” guide with new information, resources, trends, and tools related to the field.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FIStnBRnDyvqAyayjQzF6A.jpeg align="left")

[**Eloquent JavaScript**](http://eloquentjavascript.net/) is a beginner’s book about programming that focuses on JavaScript.

You can read it for free online on the website, which has a neat console tool where you can write and test the code as you read.

If you want a physical copy, the book is also available on Amazon *(*[*affiliate link*](http://amzn.to/2EVJYof) */* [*non-affiliate link*](https://www.amazon.com/Eloquent-JavaScript-2nd-Ed-Introduction/dp/1593275846)*)*.

### Closing thoughts

Is it possible to teach yourself web development with online resources? I believe the answer is yes.

However it will not be easy at all. Learning and mastering anything is difficult, and learning to code is no different.

With that in mind, if you do want to go down that path, here is some advice:

#### **Stay focused.**

When you’re learning on your own, it can be very tempting to jump around from one tutorial to another. Especially when you start hitting roadblocks.

But this can result in learning very superficially, when you actually need to develop a deeper knowledge of skills.

Try to stick with the course/book that you’re working on, unless you really don’t like it. Fighting through the roadblocks will help you develop a fuller understanding of the material.

And the more seemingly impossible problems you tackle, the more you’ll get used to facing challenges.

#### **Any course is simply the first step in your learning journey.**

Just taking a tutorial or course doesn’t mean that you’ll be a master by the time you finish. You’ll have to learn and practice many times before you really truly “get” it.

Try going through a tutorial a second time, or even learning the same material with a different course or book.

You’ll see how different people explain the same concept, and it may help the knowledge to stick in your brain better.

**And, of course, there is no substitute for practical experience.**

As you learn, try to practice the skills you’re learning about on your own. Build random projects, make a website for free for a friend or a non-profit. The more times you solve a problem, the more you will understand it.

### Thanks for reading!

![Image](https://cdn-media-1.freecodecamp.org/images/0*wDiab2yE-XocbLtC.gif align="left")

I really hope you found this article helpful!

Feel free to leave a comment below with any thoughts or feedback.

#### Want more?

I write web development tutorials on my blog, [Coder-Coder.com](https://coder-coder.com)!

Other blog posts there that you might enjoy:

* [Build a responsive website layout with flexbox](https://coder-coder.com/build-flexbox-website-layout/)
    
* [The best books for learning web development](https://coder-coder.com/best-web-development-books/)
    
* [The best courses to learn web development](https://coder-coder.com/best-web-development-courses/)
    

I also post mini-tips on [Instagram](https://www.instagram.com/thecodercoder/) and coding tutorials on [YouTube](https://www.youtube.com/c/codercodertv).
