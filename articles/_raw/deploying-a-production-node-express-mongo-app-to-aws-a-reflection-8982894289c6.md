---
title: Deploying a production Node/Express Mongo App to AWS — A Reflection
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-25T10:51:35.000Z'
originalURL: https://freecodecamp.org/news/deploying-a-production-node-express-mongo-app-to-aws-a-reflection-8982894289c6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8Seydglu0RAQqkvQ7kIGCQ.jpeg
tags:
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jared Nutt

  Lessons learned deploying a production web application in AWS

  Background

  This is not a code-based tutorial. It consists of all the things I wish I knew before
  I started the project and the steps I took that worked out pretty well. It fo...'
---

By Jared Nutt

#### Lessons learned deploying a production web application in AWS

### Background

This is not a code-based tutorial. It consists of all the things I wish I knew before I started the project and the steps I took that worked out pretty well. It follows the development of a production Node.js web application created with the Express framework that was deployed onto Amazon Web Services (AWS).

The full-scale tutorial is available [here](https://medium.freecodecamp.org/how-to-deploy-a-node-js-app-to-the-aws-elastic-beanstalk-f150899ed977).

# Developing a plan is crucial

There are entire books about developing plans, so I’m not going to elaborate upon that here. Just have one, whatever it is.

# You never allot yourself enough time

It didn’t seem to matter how simple or complex a task was. I never estimated the time a given task would take correctly. I imagine that as I do more of these, I will get better at estimating time frames.

Something that can help with this is to set a realistic timeline that gives yourself enough buffer to adjust if necessary.

# Deploy to the Server from the very beginning

There’s an old dev saying that goes something like, “Always develop in an environment that is the same as your deployment environment.” This is why things like Virtual Environments exist. This is sage advice.

Right now, it’s so easy to just grab a generator (such as [express generator](https://www.npmjs.com/package/express-generator) or [create-react-app](https://www.npmjs.com/package/create-react-app)), `yarn install` and write all our code locally. This is great for a development, but what I learned on the last project is if you wait for deployment until the end, you’ll be surprised at the number of things that “should work” but don’t.

For this project I chose to incrementally deploy the application while I built it. It made sure that what I was building was going to work on the environment I would be deploying it on. Also, it saved a ton of time when the actual deployment time came.

# Communication with the client is key

I do most of my work by myself, so sometimes I find that a solution I’ve come up with doesn’t always make sense to the person who is going to use it. It’s incredibly important to get client buy-in. In fact, if you can manage to get them to come up with the idea, they will **love** it, I promise. Nothing makes a human happier than being listened to.

## Aside - I got lucky with a REALLY good client

This isn’t so much a lesson, so much as a reminder of how important it is that you pick your clients. I know this sounds impossible, and frankly when you’re first starting out, it is very hard to be picky about your jobs. However, I’ve accepted jobs before that turned into nightmares because I ignored the signs.

Phrases like, “We need it ASAP” are a good indicator that the client is going to undervalue your worth.

# Plan for Failure

![Image](https://cdn-media-1.freecodecamp.org/images/1*CY8CSJcXBrmMZjuZ0SKU7w.png?q=20)
_Bugs are Inevitable_

I think sometimes we look at established apps like Facebook or Instagram and try to reach that goal with our Version 1.0 apps. This is impossible for two reasons:

1. Proper growth of an app requires user input. Do you think Instagram had a plan to add stories in their 1.0 version? Of course not, they waited for Snapchat to do it first then copied them. ?
2. If you wait until it’s perfect, it will never be finished.

What I’m getting at is, do the best you can, but don’t get hung up on writing the perfect function. Make it work, and improve as you go.

Also, knowing that things will fail, make sure you are handling your errors correctly. The user needs to know if something goes wrong, even if they can’t do anything about it.

# The Importance of User Testing

Do **NOT** send the client a link and say, “Go check this out,” if you are planning on leaving your computer anytime soon. I made the mistake of doing that and then was bombarded with messages within an hour, while I was trying to eat lunch. Unless of course you enjoy bugs with your sushi.Not always the solution.

It may be obvious to you, but that doesn’t mean it’s obvious to anyone else. A lot of the little things that became bugs were because of a bad UX or UI. I took for granted that I knew exactly what needed to happen because I wrote the thing. I’m not saying that you can plan for everything, but be aware that you will need to adjust some of your layouts so everyone will know what you want them to do.

I originally only allotted two weeks for beta testing. One to test, one to fix. This is not enough time. I ended up having a week of beta testing part one, a week of cleanup, and then another week of beta testing, followed by another week of cleanup.

# Don’t get attached to the product

This ideal is driven by my graphic design background. If we stick to a design because we really like it, we will ignore all user feedback (what really matters) and never change. It is the same with building an app.

Creating something out of nothing is, as the name implies, a creative act. You are making a lot of decisions about how you think a user will interact with the thing you are building. Don’t think you know better than the user — you don’t.

# Have fun

There’s no reason why you can’t enjoy the thing you’re doing. That’s not to say it won’t be incredibly frustrating, but try and enjoy it as much as you can.

# Learn something

Deadlines are deadlines, but if you can incorporate one new thing into your stack, do it. You’ll be a much better developer afterwards.

My biggest challenge for this project was AWS. I spent a ton of hours getting to know AWS. But now I have that notch on my belt for the next job. It would have been so easy to just deploy it to Heroku and call it a day, but that’s not the best option for a number of reasons.

# Push for that MVP

At the time of this writing, I still have about 20 open issues on the project. Expecting to finish every single item for version 1.0 is unrealistic. Always push for the minimum viable product (MVP) initially. Prioritization is key to determining what really matters in a project.

**Example:** One of the open issues I have is that the padding is not right on the navigation. Is this a breaking issue? No. Can it wait until all the core features are done to fix it? Yes.

So, I haven’t fixed it yet. However, I’ve expressed this to the client and they are OK with it.

# Things I will do differently next time

## Unit Testing

I hadn’t done anything with testing before this project, so I didn’t do unit testing for this project. Huge mistake. I ended up having to integrate tests after I had already built the thing.

Unit testing helps with the following:

1. Every time I added a new feature or changed something, I had to test everything **manually**. Not good.
2. It maintains a level of functionality and also allows you to realize some shortcomings of your code. Purposely writing tests that will fail helps identity issues within the code.

I highly suggest the TDD course by [FunFunFunction](https://www.youtube.com/watch?v=Eu35xM76kKY) to get started.

**Small aside:** If you use the express generator, it doesn’t export the server.

If you want to test the server with Mocha, you have to export it at the end of the `bin/www` file.module.exports = server;

## Get a more in depth look at each feature from the beginning

I made a list of all the features when I started, but I didn’t do a deep dive up front to see how I was actually going to implement them. If I had done this, I probably could have estimated my time better.

# Little things I learned

## You can access the camera with an HTML input — Welcome to 2018

However, this doesn’t work over non-secure pages in iOS.

## File upload and resize is a pain

The tutorial I went through showed the method for saving locally, however I wanted to leverage AWS S3. To be honest, the method I have setup is not ideal, so hopefully I can address this better in the future.

## AWS doesn’t let you create SSL Certificates if you are a new account

As it turns out, AWS is pretty picky about new accounts. The customer service rep said it was to prevent new accounts from racking up huge bills, which I guess makes sense. Either way it’s pretty annoying when you are trying to launch an app and you can’t get your SSL Cert sorted.

**Side note:** if you use AWS for hosting, their certificate manager is amazingly easy.

## Mongo Database hosting

I chose [mLab](http://mlab.com/) to host my mongo database for a number of reasons:

1. I wanted backups without having to handle backups. mLab does that for you.
2. I didn’t want to spend a ton of money (or rather I didn’t want my client to spend a ton of money). They cost $10 per gigabyte.
3. Also, they allow hosting on AWS. So in my mind that will be faster. I doubt it, but it’s the thought that counts, right?

## Prettier

Prettier is a life saver. However, it often fights with my ESLint. For one thing, it always removes my parentheses around single param functions. Meaning: `(var) => {}`

vs

`var => {}`

## Illustrator kept creating favicons that were 1000 x 1001 pixels

Turns out if you don’t arrange the art boards to the pixel grid, it will throw it off. Using the auto arrange art boards feature will solve that issue. More info [here](https://www.reddit.com/r/AdobeIllustrator/comments/3dqadd/1_pixel_off_when_exporting_artboards_to_png/).

# Building for failure is important

The further along I got with other people using the app, the more I had to adjust my database and views. That meant breaking things that used to work.

It’s hard to plan for everything but I got into the habit of expecting there to be no data and handling it.

**Example:** I changed how I was storing images. It was in a field called ‘documentation’. When I switched how I was storing it I also changed it in the view, but that broke the older entries.

I solved this by first checking to see if there was anything at all. And if there was, run some logic.

# Summary

This isn’t everything I learned, but hopefully some of it is useful to someone. If you have questions, hit me up.

I can’t share the code for this project due to it being for a client. However, I’m happy to expand on any of the things in this article if you have questions.

**Happy Codin**g!

