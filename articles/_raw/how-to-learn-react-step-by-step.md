---
title: How to Learn React in 2024 – A Step-by-Step Guide
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2024-01-04T21:48:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-learn-react-step-by-step
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/learn-react-2024-4.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'There''s never been a better time to learn React than in 2024.

  In this comprehensive guide, I''ll show you how I would go from knowing nothing
  about React to becoming a job-ready, junior React developer in 3 to 6 months.

  Keep in mind that becoming a sk...'
---

There's never been a better time to learn React than in 2024.

In this comprehensive guide, I'll show you how I would go from knowing nothing about React to becoming a job-ready, junior React developer in 3 to 6 months.

Keep in mind that becoming a skilled developer is not a race. This is just the path I personally would choose to learn React from front to back as quickly and efficiently as possible.

This guide assumes that you have about 3-4 hours of undistracted time a day to dedicate to learning and practicing React. Feel free to adjust this guide to your particular circumstances and goals.

## 📖 Weeks 1-2: Explore the New React Docs

If you're just getting started with React, the ideal resource throughout your journey is not a course or a book. It's the entirely free React documentation at [react.dev](https://react.dev).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-03-at-10.25.59-PM.png)
_A sample page from the new React documentation_

The React docs were rewritten in 2023. They are the official source for all things React, whether it's simple or complex topics.

Not only are the React docs a great way to become familiar with React, but it's also the most complete resource online to learn React from front to back.

**What To Do:**

* Try to read (and understand) the first 10 articles of the React docs.
* Get familiar with the core React concepts: elements, components, JSX, passing data with props, rendering, and lists.

If you encounter any especially difficult concepts, try asking ChatGPT for a simpler explanation.

The new React docs also include interactive code sandboxes, meaning you can play with the React code in their examples within the browser.

## 🤔 Do I Need to Learn JavaScript First?

You might be asking whether you need to fully learn JavaScript before you dive into React.

In 2024, I would personally say, **no, you don't really need to.**

There are just a handful of JavaScript basics that you're going to need to utilize in any React app.

These include simple data types like strings, numbers, and booleans, as well as complex ones like objects and arrays, plus functions and asynchronous operations with promises. That's about it. [Here's an overview](https://www.freecodecamp.org/news/javascript-concepts-you-should-know-before-learning-react/) of some of those concepts to know before diving into React.

Everything else can be learned as you encounter it. So no, you don't have to spend months learning JavaScript in its entirety before you dive into React.

## 💻 Week 3: Run a React Project on Your Computer

At this point, you need to do one crucial thing before building a React app.

You simply need to learn how to create a React project from scratch and run the project in development on your computer. That's it.

**What To Do:**

* Set aside a week to learn the entire process of creating, installing, and running a React project on your local machine.
* The React documentation [has a complete guide](https://react.dev/learn/installation) for this that you can dig into.

It takes some time to get used to this process, but this is important because you will primarily be working here: out of a React project folder on your computer.

Spend some time setting up and getting comfortable with your code editor, which is likely going to be **Visual Studio Code**. Then see how to create a React project using **Vite**.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-03-at-10.27.10-PM.png)
_Visual Studio Code: the most popular React code editor_

There are many ways to create React projects. But, I would highly recommend using Vite instead of Create React App. CRA is now outdated in 2024, and at this point, you shouldn't be creating projects with Next.js.

Finally, you want to get comfortable opening and running basic commands in your terminal, whether it's the integrated terminal in Visual Studio Code or your computer's terminal or command line.

If you have extra time, take a look at how to use Git and GitHub to see how to push any changes you make to your code. It's essential to keep track of these changes using a version control system like Git when you're working with a team.

If you have trouble with this step, remember that you can also create and code React apps in your browser using tools like **CodeSandbox** or **StackBlitz**. Not every **project** needs to be created as a folder on your computer.

## 🧱 Weeks 4-6: Build Static React Projects

Now that you have a basic grasp of what React is and how it can be used to build user interfaces, start building simple ones.

Before you start making fully functional applications, you need to focus on building the shell of it using React elements, components, and CSS for styling.

**What To Do:**

* Take a look at websites you use every day and see if you can build a part of it (a button, a navbar, a hero section, and so on)
* It doesn't have to be a complete page – just start with a simple part. Write it as a separate component.
* Recreate the component so that it looks close to the original in appearance (with the help of CSS).
* As you feel more confident, try putting these components together into a more complete user interface.

You can follow this process using simple React elements. You'll learn how to take those elements and break them into components so that they can be reused. After that, you can try to make it dynamic using data passed with props.

At this stage, I'd highly recommend getting comfortable with using CSS in React. You can use a simple stylesheet or something like **Tailwind CSS**, which is very popular.

Try not to use a component library because there is ultimately no way of avoiding CSS as a frontend developer. You need it to create attractive interfaces.

This stage of building static pages with React is also a good chance to learn the basics of **[semantic HTML](https://www.freecodecamp.org/news/semantic-html-alternatives-to-using-divs/)**. If you don't know what that is, there are plenty of articles that will show you how to properly structure your HTML tags so that it's not an confusing pyramid of divs.

## 🛠️ Weeks 7-10: Build Dynamic React Projects

After making static React projects, your goal is to make small, but functional React projects that perform a simple task.

**What To Do:**

* Try to make 10+ mini dynamic apps that perform a simple task using state and events.
* They should be small, and take no longer than a day to make, such as a calculator, a video player, a todo list, an image carousel, a quote generator, and so on.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-2024-01-03-at-10.28.23-PM.png)
_An example intermediate React project: a shopping list app_

What makes these projects intermediate exactly? In short, these projects should function more like real-world applications as compared to the basic, static ones. They should take user input, meaning handle events and manage data with React state.

You should make projects that use **side effects** as well. This usually involves requesting data from an external data source with the **Fetch API**.

During this stage, you should become comfortable working with the **basic React hooks**: useState, useEffect, and at times useRef, useContext, and maybe useReducer.

Don't worry too much about performance-related hooks like useCallback and useMemo. These should be used sparingly.

Try to build as many mini apps as you can (I would recommend at least 10), but don't spend more than a day at the most building any particular project. Build one, or if you can't, move on to the next one.

If you need any ideas, [I have a complete article](https://www.freecodecamp.org/news/react-projects-for-beginners-easy-ideas-with-code/) that shows you a ton of React beginner projects that you can do within a day.

This period of time is very important for getting comfortable with using React and writing React-specific code as compared to just plain HTML (technically JSX) and CSS.

## 🧑‍💻 Weeks 11-14: Build Your Developer Portfolio

This final stage of building projects should come after you feel that most intermediate projects have become a little too simple.

When you start feeling confident in building mini React projects, that's a sign that it's a good time to push yourself towards more advanced projects.

**What To Do:**

* Pick a larger, much more ambitious React project that you really want to make over the course of a longer period of time (like a month)
* Highlight this project on your developer portfolio and describe what skills and tools you used to build it.

An advanced project might be a mini clone of a larger application such as a YouTube clone where users can sign in, upload videos, and share them with friends.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/youtube-3-4.png)
_An example portfolio project: a mini YouTube clone_

Keep in mind that React is used to build major applications that you use every single day, like TikTok, Twitch, Hulu, Notion, and more. So think big when you are picking what portfolio projects to make.

These more advanced projects should take a much longer period of time, and that's a good thing. They should be a **passion project** – something that you really are interested in building with React, and excites you to make.

Along the way, you're going to be learning a lot of things that you didn't know before. You're going to need to research (for example, in our YouTube sample project):

* How to upload media with React
* How to authenticate users using some kind of authentication service, whether free or paid
* What library is best for playing videos in a React project

All on top of many smaller decisions that you'll figure out along way.

This last stage should really challenge you as a developer. And what you ultimately build over the course of a month or more is a perfect addition to your developer portfolio.

Your developer portfolio should be one or more projects that represent your proficiency with React. It's going to show to your potential employer what you can bring to the job.

Once you've got a functioning project that you're proud of, you feel like you understand core React concepts pretty well, and you know how to problem-solve while coding, you should be in a good position to start applying for junior developer positions with React.

## 🏆 Become a Professional React Developer

Looking for the ultimate resource to learn React from start to finish?

✨ **[Introducing: The React Bootcamp](https://www.thereactbootcamp.com)**

The bootcamp features every resource you need to succeed with React, including:

* 🎬 200+ in-depth videos
* 🕹️ 100+ hands-on React challenges
* 🛠️ 5+ real-world portfolio projects
* 📚 10+ essential React cheatsheets
* 🥾 A complete Next.js bootcamp
* 🖼️ A complete series of animated videos

Click below to try the React Bootcamp for yourself!

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)  
_Click to get started_

