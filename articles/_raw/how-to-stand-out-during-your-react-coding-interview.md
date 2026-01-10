---
title: React Coding Interview – How to Stand Out and Ace the Challenges
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-20T18:20:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-stand-out-during-your-react-coding-interview
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/reactinterview.png
tags:
- name: coding interview
  slug: coding-interview
- name: Interview tips
  slug: interview-tips
- name: Job Interview
  slug: job-interview
- name: React
  slug: react
seo_title: null
seo_desc: 'By Iva Kop

  As a React developer, I have gone through my fair share of front-end coding interviews.
  Recently, I had the opportunity to experience the process from the other side –
  as an interviewer. Here is what I''ve learned.

  Coding interview usually ...'
---

By Iva Kop

As a React developer, I have gone through my fair share of front-end coding interviews. Recently, I had the opportunity to experience the process from the other side – as an interviewer. Here is what I've learned.

Coding interview usually involve a multi-step process where interviewers assess everything from basic technical knowledge to culture fit. Every step of that process is important and should not be underestimated. Prepare for all of it and prepare well.

But there is one thing that is at the core of (almost) every React interview.

Inevitably, at some point, you have to build a React app.

# The App Assignment

Here is a short list of real app assignments I had to complete for my own React interviews over the years:

* **Support Desk app** – an app to display a list of support desk employees and their contact information.
* **Video app** – an app where, given a YouTube video URL, it displays it on the page. Users can comment on it.
* **Projects app** – an app to display a list of on-going projects that users can subscribe to and follow.
* **Articles app** – an app to display a list of articles where users can leave nested comments for each one.

These assignments are, in many ways, very similar to each other. The reason is that they are assessing the same set of basic React skills. Which skills are those? Let's break them down.

## Interview Skill #1 – How to Build UIs with React

A primary job of a React developer is to build and structure React components in a meaningful way. 

The assignments above are meant to test your ability to write code in a modular and reusable way while creating abstractions at the right level. 

The main goal is for your app to work well. But, as a front-end developer, you are also expected to build UIs that look good, too.

Most of the time, the assignment will come with a concrete design you'll need to follow. If that is the case, it's important to stick closely to it. 

But if you believe that there is a good reason to deviate, don't hesitate to do so. Just be prepared to explain why your solution is better.

If there is no design available, the interviewer is probably interested in understanding if you can create sensible UIs on your own. Although this could be more challenging, it also gives you the opportunity to show you are able to make conscious choices when it comes to the front-end.

**Tip:** It is easy to assume that the expectation is that you have to build all components from scratch. Using a third party component library might feel like cheating in an interview context. But it is not! 

Make sure to ask in advance what is expected. Taking advantage of component libraries like [MaterialUI](https://material-ui.com/) or [ChakraUI](https://chakra-ui.com/)  is a huge time saver during interview assignments and will allow you to focus on more interesting parts of the app.

## Interview Skill #2 – State Management in React

Another important challenge when it comes to building React apps is state management. There is a myriad of ways to go about this depending on your concrete use case and goals. Check out [my article](https://blog.whereisthemouse.com/how-to-think-about-react-state-management) on the topic if you are curious to learn more.

Whatever approach you choose, what is important during as interview assignment is to show the interviewer that you understand and are able to reason about state management. 

Your solution needs to make sense without being overly complex or convoluted. Be prepared to explain and defend your choices.

**Tip:** It is a good idea to match your state management solution to the one used by the company your are interviewing for. 

Do they use Redux? Then don't hesitate to include Redux in your project. Are they into state machines? Then xState is your friend, and so on. Make sure to ask the interviewer in advance what they would like to see implemented in your project.

## Interview Skill #3 – Data-fetching in React

As a front-end developer, normally you won't be expected to build your own back-end. But the assignment you are given will probably involve some form of data-fetching – likely either through a mock API of some kind or just a JSON file with the necessary data.

This part of the assignment is meant to test if you, as a front-end developer, know how to talk to the back-end. Can you get, display and update the data you receive from the back-end correctly? Do you understand how API requests work? 

In a more advanced setting, there might be a conversation about data-fetching architecture, data state management, and front-end caching.

**Tip:** Make an effort to implement a semi-realistic data-fetching mechanism in your app. In you are given a JSON file, don't just directly import the data in your components. Instead, use `fetch` or another more advanced (preferably async) approach to get it so that you are able to demonstrate your deeper understanding.

## Interview Skill #4 – Routing in React

A lot of the time, creating a React project is synonymous with a single page application. So it is possible that the assignment involves implementing a routing solution. 

Here the goal is to demonstrate that you understand the basics of client-side routing and are able to structure your app around it.

**Tip:** Avoid creating your own client-side routing implementation, unless explicitly required. Opting for [React Router](https://reactrouter.com/) or [Reach Router](https://reach.tech/router/) is a perfectly acceptable choice.

# How to Stand Out in a React Interview

Getting a solid grasp on the basics discussed above is a must and it's a good start to earn points during an interview assignment. But to truly stand out, you have to go a step further.

Here is how.

## Understand Your Setup

Most of the time you can get away with using toolchains like Create React App (or similar) when building a React project for an interview. This will help you get started and save time. 

In fact, it is important to use those tools in order to spend your time on meaningful development rather than setup. 

But it's also important to understand and be able to explain the basic tooling you are using. During a React interview, expect to be asked questions about [Webpack](https://webpack.js.org/) and [Babel](https://babeljs.io/), for example.

But what can really give you an edge is if you not only understand but are able to enhance your existing setup. One idea would be to add a linter ([eslint](https://eslint.org/)) and a formatter ([prettier](https://prettier.io/)) to your app. This shows that you really care about code quality and consistency.

Another would be to go even further and setup pre-commit hooks ([husky](https://github.com/typicode/husky)) that lint and format your code with each commit. Crazy, I know!

These tools take minutes to setup but can seem like an impressive extra step in the eyes on an interviewer.

## Test Your Code

Very few assignments will explicitly state that tests are required. For this reason, many developers assume tests are not part of the task and completely ignore them. This is wrong!

Most of the time, an interviewer will be impressed to see that you understand the importance of testing your code. It is a very easy but powerful way to set yourself apart. 

It is not necessary to have a test for every single line of code in your project. Several strategically selected tests covering the more complicated logic should do the trick just fine.

## Don't Ignore Responsiveness

Here is another aspect of your React assignment that is not explicitly mentioned most of the time – responsiveness. 

Even if you are given a design at the beginning of the task, almost always it will not be a responsive one. It is up to you care enough about responsiveness to figure it out on your own.

Same as testing, most developers will just ignore responsiveness. Which is good news for you – it gives you the opportunity to shine!

There is no need for the implementation to be perfect and work flawlessly on every screen and device. The mere fact that this is something you though about in your development process should be enough to score you some major points.

## Improve Accessibility

Accessibility is a huge concern for most modern web products. Taking even minor steps to improve the accessibility of your project, like adding `alt` text to your images, for example, can leave a really good impression.

Accessibility is also another reason why you might want to choose a third-party component library when building your assignment. Most components in these libraries are accessible out of the box.

Making your project as accessible as possible can truly make you stand out in an interview. But what is more, accessibility should be (and is becoming) the norm in web development. Make sure your future employer knows you understand that.

## Details Matter

Everything in your code should tell the interviewer you are a competent developer – from basics like the way you name and structure your code to minor details like commit messages. 

Given that these assignments are usually done under time constraints, it is tempting to just ignore these seemingly unimportant aspects. But getting them right can meaningfully set you apart.

Hopefully this article is useful for your next React interview. Let me know how it goes!

[Follow me](https://twitter.com/iva_kop) on Twitter for more tech content.

