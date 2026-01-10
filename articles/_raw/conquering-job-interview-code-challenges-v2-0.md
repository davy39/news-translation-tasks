---
title: 'How to conquer job interview code challenges v2.0: creating a front-end web
  app'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-19T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/conquering-job-interview-code-challenges-v2-0
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/lou-levit-B4op5oZ4x5Q-unsplash.jpg
tags:
- name: challenge
  slug: challenge
- name: code challenge
  slug: code-challenge
- name: coding challenge
  slug: coding-challenge
- name: coding interview
  slug: coding-interview
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: Job Hunting
  slug: job-hunting
- name: Job Interview
  slug: job-interview
- name: learn to code
  slug: learn-to-code
- name: learning to code
  slug: learning-to-code
seo_title: null
seo_desc: 'By Jonathan Sexton

  As many of you know, I landed my first developer job at the end of June and I thought
  it would be great to use the challenge I was given as the subject of today''s article.

  It is important to note that I used React to build my proje...'
---

By Jonathan Sexton

As many of you know, I [landed my first developer job](https://jonathansexton.me/blog/landing-my-first-development-job-what-a-crazy-journey/) at the end of June and I thought it would be great to use the challenge I was given as the subject of today's article.

It is important to note that I used React to build my project, but this could have been completed with any front end framework or 'vanilla JavaScript'.

Below is a list of topics we'll go over:

* Accessing the [Quip Automation API](https://quip.com/dev/automation/documentation#token-endpoint)
* Creating spreadsheets/documents with the Quip API
* Installing and using the [Axios](https://github.com/axios/axios) library (this is optional and you can make API requests without it but I like the syntax)
* Using [qs package](https://www.npmjs.com/package/qs) to stringify requests (this is not a requirement but I wanted to try something new and if it didn't work I always had the fallback of knowing Axios will stringify my requests by default)
* Making [POST](https://en.wikipedia.org/wiki/POST_(HTTP)) and [GET](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods) requests

For context, here is a snippet of the requirements as I received them:

"_Create a front-end web app that interacts with the Quip API in the following ways:_

* _Create a spreadsheet (bonus points to import data into the newly created spreadsheet)._
* _By import data, I mean upload an Excel spreadsheet, or copy and paste data into Quip spreadsheet._
* _Export a Quip spreadsheet to .xlsx_
* _Download (backup) a folder/multiple documents._

_Create the UI for the page in whatever way you see fit (buttons, dialog boxes, etc)._"

I was a little worried when I read the requirements as I wasn't exactly sure where to begin. So, I dug into the API docs and started soaking up information. Thankfully, no time limit was given to me but I wanted to be done with this as soon as possible to see where I stood in the interview process.

To start, I designed a prototype of the finished product in Figma so I'd have a road map to go off of. This is not a required step, but it does make your project building experience run much smoother.

Alright, let's dig in!

## Getting Started

I built my Nav, Footer, and Content components so I'd have a solid foundation for my app.

Each of these components return some basic JSX and there isn't much to them (If you'd like to see the code for each you can check out the project's [GitHub repo](https://github.com/JS-goose/gibson-code-challenge)).

I decided the majority of the requests would be split between the _`App.js`_ and _`CenterContent.js`_ files.

For reference, here is my project structure:

![react code showing a project structure](https://jonathansexton.me/blog/wp-content/uploads/2019/08/image.png)
_My project structure_

You'll see me reference POST and GET requests throughout this post.  If you aren't familiar with those now is a good time to do some research on those.  I'll be honest in that I wasn't 100% on them when starting this project and had to go through some resources myself.

In a nutshell, a POST request is when we ask the server to **_accept_** some incoming data (that we are sending) - in our case that data comes in the form of creating a new spreadsheet file.

A GET request is when we ask the server to **_send_** us data from a specified resource on the server.

I used the [Insomnia REST Client](https://insomnia.rest/) to help debug issues with my requests. I'm working on a beginner's guide for it so stay tuned for that!

## Using the Quip API

If you're like me, you've never heard of the Quip API and had no idea what it does. At its core, Quip is an automation tool that allows you to integrate with tools like [SalesForce](https://www.salesforce.com/) to make your sales team more collaborative.

For our purposes, we will be using it to create Excel spreadsheets on my Quip account (if you want to replicate this project you'll need to create a Quip account - it is free to do so).

You'll also need to create a personal developer token in order to make requests. You can do that [here](https://quip.com/dev/token) (requires an account). Once you have your token, keep it in a safe spot because we'll be making use of it soon.

To start, I installed Axios into my project by running `npm install axios` and then I import it into the files where I need to make my requests with `import axios from "axios";`

![a code snippet of react import statements](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-1.png)
_My import statements for required packages_

## Authentication

Before making any kind of requests to the server, I needed to authenticate with my credentials. I decided to put this in the `App.js` file inside a `componentDidMount` [lifecycle method](https://reactjs.org/docs/state-and-lifecycle.html) so it would load every time the page loads:

![some react code showing an authentication call to an outside API](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-4.png)
_My authentication function_

So I built my function, I called my function and for a moment thought all is well, until I ran into this dreaded error:

```
"Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at $websiteName"
```

Noooooooo!!! The dreaded [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors) monster rears it's mighty head!  (CORS is actually a useful intermediary between me and the server but can be annoying to deal with if you've never seen this error before).  

_*Side note - if you've never seen this error before don't worry!  I still don't fully understand it but I know enough to debug it. If you get stuck, check out the link above for some helpful info or look below for a quick work around.*_

An easy way to get around this is to use a proxy like the [CORS Anywhere](https://cors-anywhere.herokuapp.com/) free resource. Essentially, place this link `https://cors-anywhere.herokuapp.com/` in front of your end point URL and it'll resolve the problem, for now.

This handy tool will allow you to make your requests **_while developing on localhost_**. If I were you, I would do some research before using this approach in production. Full disclaimer, I don't know enough about this little trick to tell you if it's safe to use in production or not.

So, after some tweaking of the authentication function I got the desired result to log to the console. Time to move on to making requests!

## Making Requests

Now that my authentication is working, we're ready to make some requests. I knew I was going to make a POST request whenever I wanted to create a new document and that I also wanted to tie that action to the click of a button. So, below is my POST function:

![a POST function call to an outside API](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-3.png)
_My POST function_

You'll notice this is where our `qs` package I mentioned at the beginning of this article comes into play. I'm not an expert but from what I gleaned after reading the docs on it, this package turns my request into a string to be sent to the server. If you prefer not to use this package that's no problem as `Axios` will do this by default. I know that  `qs` offers more than just stringifying data but I'm unfamiliar with the full range of its capabilities.

Now, I want this function to fire when clicking a button. Thus, a basic button came to life!

![some react code for a simple button](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-5-1024x96.png)
_A simple React button with an on click method_

My POST function has been built, my button has been built, and the method tied to it.  It's time to cross my fingers and see what my function spat out into the console:

![a console log statement from an outside API call](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-6.png)
_The result of my server request - it works!_

At this point I'm over the moon! I'm beyond excited that I've gotten this API call to not only work but to return something as well. Now the real test...does this show up as a new spreadsheet on my Quip account?

![a quip account showing the creating of a spreadsheet](https://jonathansexton.me/blog/wp-content/uploads/2019/07/image-7.png)

I have the console statement and the confirmation from my Quip account showing that I have successfully created a new spreadsheet - this is awesome!  I'm ecstatic and I literally jumped out of my chair and yelled "YEEEEEEESSSSSS!!!" once I got both of these.

That feeling of getting something to work after struggling with it is like nothing else I've experienced in my professional life.  I tell myself that I have to keep riding this wave of enthusiasm and elation so I push on to the next item on the list.

## Import Data Into the Newly Created Spreadsheet

I had some great ideas for this section of the "assignment" but at this point it has been almost two weeks since I started this project and I'm anxious that the interviewer will have forgotten about it (i.e. me) or is getting impatient with me.

So, I scrap those grand plans and opt for something of a more simple nature so I can get this project turned in ASAP.

I built a small function to at least attach to the upload button so that I would have some type of functionality for it. At it's core, this function waits until a file has been uploaded, sets the state to the first element in the event target array, then creates headers based off of that information, with the eventual goal being it posts to my Quip account with that information.

However, you can tell by the comment at the top of this function block that I was unable to get it to work properly. However, I did not have time (at least I thought I didn't) to dig deep into this problem and get it fixed.

![a snippet of react code showing an upload function](https://jonathansexton.me/blog/wp-content/uploads/2019/08/image-3.png)
_My import function that never quite worked properly :)_

At this point, I've been working on this project after work and at night for over two weeks. I decide that it's time to turn it in without the other parts working (import, export, and downloading data).

## The Final Touches

I know my project is unfinished and I'm beating myself up pretty hard about it. But, as an added bonus I decide that I'm going to design something in [Figma](https://www.figma.com/) as an added touch to help my chances of getting a call back.

Here is the finished product modeled off of their current colors/font/theme:

![a react app showing database table data](https://jonathansexton.me/blog/wp-content/uploads/2019/08/image-4-1024x731.png)

## And That's A Wrap

With my project not finished but at a stopping point, I'm feeling not so good about my progress and my timing but I package everything up and throw it on GitHub. I throw in the above image and schedule an e-mail to go out the next morning at 9AM to the interviewer.  
  
I waited nearly 2 days with bated breath hoping to get some type of call back - something. It finally came as I was driving into work. The interviewer had gotten my project and wanted me to come in for another meeting with his lead developer.

I was terrified and excited all at the same time because I was thinking they wanted to bring me in to make fun of my code or to ask me what the hell I was thinking when I built this monstrosity. But that wasn't the case at all. I ended up getting a job offer from this project!

If you'd like the whole story about that, it can be found in my previous blog [post about landing my first developer job.](https://jonathansexton.me/blog/landing-my-first-development-job-what-a-crazy-journey/)

I hope you've found some value out of this post. If you have let me know on [Twitter](https://twitter.com/jj_goose) or any of the other platforms I post on :D

Also, I cross post most of my articles on great platforms like [Dev.to](https://dev.to/jsgoose) and [Medium](https://medium.com/@joncsexton) so you can find my work there as well!

While you’re here why not sign up for my **Newsletter** –  you can do that at the top right of the page on my [blog](https://jonathansexton.me/blog). I promise I’ll never  spam your inbox and your information will not be shared with  anyone/site. I like to occasionally send out interesting resources I find, articles about web development, and a list of my newest posts.

Have an awesome day filled with love, joy, and coding!

