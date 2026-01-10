---
title: The 10-minute roadmap to becoming a Junior full stack web developer
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2019-03-15T15:10:24.000Z'
originalURL: https://freecodecamp.org/news/the-10-minute-roadmap-to-becoming-a-junior-full-stack-web-developer-1131d4ffc48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H5_yjO8LxdW-cwkyLTuRBQ.jpeg
tags:
- name: career advice
  slug: career-advice
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'So you have started your journey into the world of web development. But
  what do you learn first? The Internet is overloaded with a wealth of information
  about the millions of different technologies that a web developer can know.

  It’s not hard to see ...'
---

So you have started your journey into the world of web development. But what do you learn first? The Internet is overloaded with a wealth of information about the millions of different technologies that a web developer can know.

It’s not hard to see how confusing and off-putting it all is. As a former junior developer myself, I know the struggle.

This guide has been assembled based on my experience in the industry as a junior developer. This guide is also a summary of things that I, as a team lead, would expect from junior developers.

There is a lot of information here - so grab a drink, get comfortable, and let’s get started!

#### The Must Know’s

Regardless of your pathway and career goals, there are some things that every developer needs to know.

* **Git/Source control** — Every good developer will need to know how to use Git, especially in a team environment. So learn how to clone repos, make commits, create branches, and merge code
* **Debugging** — Frontend, or backend, there will be bugs. Get familiar with the debugging tools for your IDE. Speaking of IDE’s…
* **IDE** — There are many IDE’s you can use, so pick one and get to know it. Your IDE is your best friend, and knowing the shortcuts and tools will make you a better developer. Personally, I recommend using VS Code.
* **Methodologies (Agile/SCRUM/Kanban) —** When operating in a team, the odds are you will be using a product development methodology, so make sure you’re familiar with how they work

### Front-end

![Image](https://cdn-media-1.freecodecamp.org/images/a0a2gn4-IbAt9j6FWCR112Vh96LGKoIQu0cN)

A front-end developer can typically perform the following tasks:

* Implement a design using HTML/CSS
* Interact with the DOM using JavaScript
* Interact with an API using FETCH API or similar

Let’s dive into this in a bit more detail.

#### HTML/CSS

This is the bread and butter of front-end development. HTML is used to position and place elements on a web page, while CSS is used to _style_ those elements.

A junior front-end web developer will be expected to know this stuff really well. It is important to know:

* Using HTML to create a webpage
* Styling elements using CSS
* Different ways to apply CSS to HTML — inline styles, style sheets, etc.

Once you have the basics nailed down, have a look at more advanced features:

* CSS Grid & Flexbox for layouts and easier positioning of elements
* SCSS for making normal CSS more manageable through using variables

Check out [css-tricks.com](https://css-tricks.com/snippets/css/complete-guide-grid/) for a comprehensive guide on CSS. This is one of the best resources out there.

> BONUS TIP - Create a few projects in CSS/HTML to practice. Don’t worry about using JavaScript or API’s just yet, focus **purely** on the CSS/HTML elements.

We’re turning into CSS/HTML experts now! ?

#### Frameworks

The next stage is to get familiar with CSS frameworks. These are basically “out of the box” elements and styles that you can use within your projects. Most companies use these as it saves their developers time as they don’t have to reinvent the wheel. There are a plethora of frameworks, but I suggest you pick one and get familiar with it. They are typically all quite similar and once you are familiar with one, its easy to pick up the rest.

#### Bootstrap

My personal suggestion is to learn **Bootstrap** ([getbootstrap.com](https://getbootstrap.com/)). It’s highly popular and used by a lot of companies.

“Wait, why did I have to learn CSS/HTML from scratch if I can just use a framework?!”

Good question. Yes, there are frameworks, and while a lot of companies use them, you’ll often have to customise things from time to time based on the project. For this, you’ll need to know the basics.

#### Responsive Designs

These days it’s important to take the many mobile devices into consideration when creating front-end designs. Fortunately for us, the CSS frameworks we have talked about so far (Bootstrap, CSS Grid, Flexbox etc) makes creating responsive designs really easy.

* **Media Queries.** As well as knowing how to use CSS to create responsive designs, you will need to understand how to use **media queries** to define how elements should look for different screen sizes.
* **Avoid using pixels for sizes.** I would suggest using **rem** units over pixels. An image with a width of 100px, will always have a width of 100px regardless of the screen size. Try to use units such as **rem**, **vh**, and **vw**, to achieve responsive designs.

> **BONUS TIP** - Often you need to develop an app that uses both mobile and larger screens. Focus on mobile first when creating designs, and add the media queries for the larger screens after.

#### JavaScript

JavaScript is the programming language of the web. If you want to be a successful front-end developer, you need to know JavaScript. And really know it. Yes there are frameworks, but just like we learned the basics of HTML and CSS before getting into the frameworks, we’ll do the same here. This will make you a better developer in the long run. As frameworks come and go, the core elements of the language will remain the same.

At the very minimal, as a junior developer you will need to to know:

* Objects, functions, conditionals, loops and operators
* Modules
* Arrays (including how to manipulate them)
* Retrieving data from an API using FETCH API
* Manipulating the DOM and using Events
* Async/Await (More an optional advanced topic, but really impressive if you know it)
* JSON
* ES6+
* Testing (Jest, Enzyme, Chai, etc.)

A junior developer isn’t expected to know _everything_ on these topics, but the more you know, better. Once you can create a _basic web app without tutorials,_ you can be sure that you know JavaScript.

If you really want to become an expert in JavaScript, fully understand the language and standout from the crowd, some great resources to learn the more advanced JavaScript topics are:

* [eloquentjavascript.net](http://eloquentjavascript.net/)
* [freeCodeCamp.org](https://www.chrisblakely.dev/the-10-minute-road-map-to-becoming-a-junior-full-stack-web-developer/freeCodeCamp.org)
* [github.com/getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS)

Not only do these resources teach you JavaScript, but you’ll also learn a lot about programming concepts in general. Seriously, if you learn the resources in the resources above, you’ll be a really kick-ass junior developer - some seniors I’ve meant don’t know this stuff!

Some project ideas:

* Create a Super Mario game (you’ll learn JavaScript, manipulating the DOM, and using events)
* Create a dashboard showing some stats which are pulled from an API. e.g, a Twitter dashboard, a GitHub dashboard or anything you like (you’ll learn to work with APIs and JSON)
* Don’t worry about how things look here. Focus on learning JavaScript, not the CSS/HTML. You can always make it look nice later if you want!

#### JS Frameworks

There are many JS frameworks, pick one and learn it well. The popular ones at the moment are **Angular.js**, **React.js**, and **Vue.js**. These are all solid choices and aren’t going anywhere soon. Personally, I recommend React.js, but you can try others and see which you prefer.

Quick note — If you’ve learned the basics of JavaScript and have a solid foundation, learning frameworks should be a piece of cake! Regardless of what framework you choose, make sure to know it well.

**You do not need to know them all,** it looks more impressive if you know one framework REALLY well, as opposed to having minor knowledge of multiple different frameworks.

#### React

It has huge backing from **Facebook**, massive online community and is the most popular in the industry at the minute.

If you followed the steps above and learned a bit of JavaScript, then picking up a React shouldn’t be too difficult. As a junior developer, you want to make sure you have a handle on the core concepts of React:

* Understand that React is based around components, and how components work
* Using State & Props within your components
* JSX and how to use it to render HTML elements on a webpage
* How and when components re-render
* Using React hooks
* NPM, Webpack and Babel

> **BONUS TIP** — Again, as a junior developer you won’t be expected to know React inside out. So to practice the skills outlined above, try creating a few projects:

* Rebuild some of your previous JavaScript projects to use React
* Create a **calculator app** (A good one to practice state management, as a lot of user actions will need to update state. Hint: Try using React Hooks)
* Create your own, **Twitter**, **GitHub**, or **News feed**. Use the public API’s to get the data, and display this within your app.
* Again, don’t worry about making your app perfect, or making it look super sexy. Focus on making it work, and focus on learning the React concepts.

#### State Management (e.g Redux)

Once you have the core concepts of React nailed down, the next step is to understand **Redux**. Redux is basically a state management framework, that heavily compliments React. Think of it as a front-end database that holds the state of your web application in one, easy to manage place.

There are a-lot of moving parts to Redux, so don’t worry if you feel overwhelmed (I’m still learning the in’s and out!). You will only need to know Redux when working with large enterprise scale web apps. Focus on understanding the fundamentals and state management using React.

There are a number of tools available to help you with debugging React/Redux (part of the reason why I love it)

* [React Dev Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en)
* [Redux Dev Tools](https://github.com/zalmoxisus/redux-devtools-extension)

#### Web Browsers

As a front-end developer, it’s important to know your way around web browsers. Chrome, Firefox and Edge are the main ones. You’ll need to have a basic idea around:

* Debugging tools (e.g Chrome Developer Tools)
* Working with the storage methods (local storage, session storage, cookies)
* Browser features — the biggest pain of web development is developing with browser support in mind. Keep an eye on [**whatwebcando.today**](https://whatwebcando.today/) to make sure your code supports the necessary browsers.

#### Deployment & Hosting

A front-end developer should know how to deploy and host a web app. This is good for your portfolios, knowledge, and generally getting a job. I recommend using a managed service (i.e, let someone else do the heavy lifting for you) such as

* GitHub Pages
* Heruko
* Netlify
* Digital Ocean
* AWS
* Firebase

Personally I recommend **Netlify** or **Heroku**. It makes it super easy to deploy and host apps through the UI. Each of these services provides a free tier, so it shouldn’t cost you much to run. The downside to these services is that they don’t give you the _finer access_ that some developers would need, such as email services, SSH or FTP. If you don’t know what these are, you probably don’t need them so the simple service will do just fine.

If you decide to go super-fancy and host some of your projects on a custom domain (like `<yourname&g`t;.com), I reco**mmend Name**Cheap for domain names. Again, really easy to use and the domains are, well, cheap. ?

### Back-end

![Image](https://cdn-media-1.freecodecamp.org/images/xDVVuZJUUqhk28LTGvkKagi7BKTrMKHR77K1)

In a nutshell, this is where the data from the front-end is saved. For example, when a user creates a Tweet, this goes through the server, and is saved in the database.

A back-end developer can typically perform the following tasks:

* Create API’s that the front-end will use (typically by returning JSON)
* Write the business logic and validation logic
* Integrations with 3rd party APIs
* Save and read data from a database

#### Programming Languages

There are many programming languages you can choose from. Like millions of them. But don’t worry, the main ones are:

* Java
* C#
* Python
* Node.js (Not technically a language, more a runtime that let’s you run JavaScript on the server)
* Go
* PHP (only if you’re interested in WordPress development)

Again, my advice is to pick one and learn it well. I suggest using **Node.js**, as you are already in the mindset of learning JavaScript. Node.js makes it really easy to create REST API’s, which is one of the main tasks a junior developer will be expected to do.

Whichever language you choose, make sure you know the following;

* Creating API’s
* Language basics (creating functions, using conditionals, operators, variables, etc)
* How to connect to a database
* How to query a database
* Package management
* Writing tests

If you decided to learn Node.js, a lot of this will be familiar to you. **Do not try and learn them all!** As a junior developer, you will not need to. Choose the language that best fits your goals (if it’s web development, any of them will do) and focus on it and learn it well. Of course, if you’re curious about other languages (Node.js and Python are quite different) then feel free to satisfy your curiosity and play around with them.

#### REST API & JSON

Creating a good REST API is one of the main jobs for a back-end developer. You will need to know:

* The different verbs and what they are used for
* How to create a good response
* How to handle requests
* Authenticating requests
* How to document your API

**REST API’s** are the bridge between back-end and front-end development, so make sure you understand how they work.

**JSON** is the main language used to transfer data over a REST API. Data is represented as _Objects and Arrays._ Again, if you’ve learned JavaScript or front-end development using the steps outlined about, this will look familiar to you.

#### Databases & DevOps

![Image](https://cdn-media-1.freecodecamp.org/images/z1aN6gbVKd8vKlXHCQgvoheoUDH2FJvR3iva)

This is pretty much the infrastructure side of web development. I wouldn’t say that heavy knowledge of this stuff is a requirement for a junior developer. I’d almost suggest the opposite, and say you only really need to know this stuff in depth if you are looking to get into the field of DevOps. The broad area’s you need to know are:

* How to manage a database
* The different platforms for hosting (AWS, Azure, Google etc)
* CICD and tools such as Jenkins, GitLab etc
* Logging and monitoring

Depending on your team or company, there may be other teams or people to manage this. It is still an interesting and impressive set of skills to have, so if you are curious and have some spare time, learning some database and DevOp’s skills will go a long way.

### Advanced Topics

![Image](https://cdn-media-1.freecodecamp.org/images/gT62Q5jgzsdlcZnzN-QFNO9vT8RBsQndSXt5)

Below are some advanced topics I recommend once you have mastered the above. There is plenty to learn already, so I won’t go into much detail here, but feel free to skip/skim this section for now and come back later.

#### Authentication using JWT/OAuth

This is a common approach in industry that authenticates and authorises users (e.g. login).

More info at: [https://oauth.net/2/](https://oauth.net/2/)

#### Design Patterns

Design patterns are _common solutions to common problems_. Learning design patterns will make it easier to solve problems and inevitably a better developer.

* More info (Java example): [github.com/iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns)
* More info(JavaScript): [github.com/fbeline/Design-Patterns-JS](https://github.com/fbeline/Design-Patterns-JS)

> **BONUS TIP** — There are many design patterns, so don’t try and learn them all at once. Instead, _get familiar with them_, and when you encounter a problem as part of a project, see what design patterns are available for you to use.

#### Progressive Web App’s and Mobile development

**Progressive web apps** are essentially web apps that run like native apps on a users phone. Pretty cool right? Check them out if you have times.

More info at: [developers.google.com/web/progressive-web-apps/](https://developers.google.com/web/progressive-web-apps/)

Other options include:

**React Native** — lets you write React code that gets compiled to Android/IOS

**Flutter** — similar to React Native, only uses the Dart programming language

This is rendering front-end code on the server side, which is they returned and displayed to the browser. An advanced topic, that has its own merits such as SEO & speed benefits.

More info at: [medium.freecodecamp.org/demystifying-reacts-server-side-render-de335d408fe4](https://medium.freecodecamp.org/demystifying-reacts-server-side-render-de335d408fe4)

#### Using the command line (SSH/Bash etc)

Sometimes, you’ll need to use the command line when a GUI is not available. At a very basic level, you’ll need to know how to:

* How to connect to a server using SSH
* Navigate around using commands (cd, ls, and so on)
* Edit files using vim (or similar. Heres a cheat sheet [vim.rtorr.com](https://vim.rtorr.com/))

Thanks for reading!

To get the latest guides and courses for junior developers straight to your inbox, make sure to join the mailing list at [www.chrisblakely.dev](https://www.chrisblakely.dev/#signup)

_Originally published at [www.chrisblakely.dev](https://www.chrisblakely.dev/the-10-minute-road-map-to-becoming-a-junior-full-stack-web-developer/) on March 15, 2019._

