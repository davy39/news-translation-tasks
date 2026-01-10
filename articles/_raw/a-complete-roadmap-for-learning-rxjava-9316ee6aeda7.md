---
title: A complete roadmap for learning RxJava
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T22:15:55.000Z'
originalURL: https://freecodecamp.org/news/a-complete-roadmap-for-learning-rxjava-9316ee6aeda7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gaQI9yDYH86yIlrLE0tyaQ.png
tags:
- name: Android
  slug: android
- name: Computer Science
  slug: computer-science
- name: mobile app development
  slug: mobile-app-development
- name: rxjava
  slug: rxjava
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By Ayusch Jain


  This article was originally posted here


  I wish someone had written an article like this when I started my learning journey
  with RxJava in 2017. I wish there had been a perfect book or some kind of an online
  school which taught me how...'
---

By Ayusch Jain

> This article was originally posted [here](https://ayusch.com/the-complete-rxjava-roadmap/)

I wish someone had written an article like this when I started my learning journey with RxJava in 2017. I wish there had been a perfect book or some kind of an [online school](http://microverse.org) which taught me how to get started with Rx the right way.

There has been so much hype right now around **RxJava** and Reactive Programming in general. Everyone seems to promote it, but no one seems to have an idea about how a novice programmer who is just starting out with RxJava should go about this journey.

All this has a reason! RxJava has a steep learning curve and there is no one way to master it. Some prefer the docs (which are excellent, by the way), some prefer books about RxJava with some examples, while some crazy ones (including me *facepalm*) commit the mistake of diving right into the code after watching a YouTube video of a talk by Kaushik Gopal on how to get started with RxJava and start refactoring their code.

The last method is absolutely dangerous, and instead of solving your problems with Rx, you’ll just end up creating new ones. So, I suggest that you follow the roadmap given below to get started with RxJava.

While this is by no means the only way to go about it, after having experience of almost 1.5 years with **RxJava** (and still learning), I wish someone had told me these things when I was beginning my journey. If you follow the given roadmap religiously, I can ensure you that you’ll have a strong foundation in RxJava which you can then build upon to unleash its full potential.

I have divided the entire roadmap into four phases:

* **The Discovery**: Say hello to the world of Reactive Programming.
* **The disillusionment**: World ain’t all sunshine and rainbows.
* **Eureka!**
* **Sky’s the limit**

So, let’ get straight into it.

### Phase 1

#### The Discovery: Say hello to the world of Reactive Programming

I could have also titled this phase “The Motivation”, because this is the very initial phase where you’ve heard about **RxJava** from a friend of yours or someone on LinkedIn posted about it or you just happen to stumble upon a piece of code with Observables flying around all over the place.

Whatever the case, when you first go about looking at a piece of **RxJava routine** (even the simplest one), you might be intimidated by all the methods being called one after the other in a single chain. But you’ll notice that the code looks neater than any other you’ve ever seen. And it accomplishes unimaginably complex tasks with simple method chains while you’ve been forming AsynTask and thinking about multiple **Retrofit/Volley** calls in your head.

Tasks such as making multiple API calls one after the other, making API calls and saving into a database and returning a success or a failure etc… are being **accomplished within 20–25 lines of code.** You’ll be intimidated but at the same time inclined to find out what this tool is, and how you can also get started writing such neat code.

**So, in order to get you started here is a list of things I need you to do in this phase:**

I suggest that you **watch this talk by Kaushik Gopal** at least twice (it took me 4 replays to get a hold of it. I had the talk downloaded on my computer) to completeness. According to me, it’s the gold standard of anyone looking to dive into reactive programming.

Kaushik Gopal beautifully explains the nuances of RxJava and provides real-world examples, with a hint of abstraction on the absolute technicalities, easily understandable by any beginner. He divides any RxJava routine into 4 basic constructs (even my article on RxJava: [**Understanding RxJava Basics**](https://disq.us/?url=https%3A%2F%2Fayusch.com%2Funderstanding-rxjava-basics%2F&key=7M4ry_gpESP38RXOsGVmaQ) is inspired by his talk).

Surely on the first attempt, you won’t be able to get a hold of what exactly is an observable and how the observer pattern works. That’s why I suggest that you watch it at least twice.

**Here’s what you should be clear about from this talk (at least):**

* What is an Observable?
* What is a Subscriber?
* How do Observables and Subscribers work together?
* What is an operator (not the specific functionality, but what an operator does)?

Replay it as many times as you want, but you should be absolutely clear about the above 4 questions after you’re done. You can also refer to the text available online along with this video. Don’t move forward unless and until you understand the above nuances clearly else, you’ll end up being more confused than before.

Once you’re done, go ahead and watch this talk by Christina Lee:

Watch this talk once, but I want you to focus especially from **28:20–32:50**. During these 4 minutes, she gives an absolutely beautiful explanation on **what the two most used operators** in any RxJava routine, observeOn() and subscribeOn() do and how they’re used together, using an example.

These operators are together included as one of the main constructs, in the **4 constructs of RxJava** explained by Kaushik Gopal. And believe me, they are really important in your journey with reactive programming and RxJava in general.

**Create a project in Android Studio** (if you are an android developer) or any IDE of your choice and run the exact same code that Christina provides. Once you set that up, you can play around by changing the order of observeOn and subscribeOn and see how they behave. Try adding multiples of these and see who dominates and what’s the output. You’ll get a good grasp on the functions of these operators once you do this exercise.

> **Don’ts**: YouTube would recommend multiple talks on RxJava by **Jake Wharton**, but I highly suggest that you ignore those for the time being. Those talks can get really intimidating after some time and you’ll most likely drop off somewhere in between and maybe even give up on RxJava altogether. So, stay away from them for the time being.

### Phase 2

#### The Disillusionment: the world ain’t all sunshine and rainbows

This phase could also be named “The Struggle”. This is the phase where you need to start getting your hands dirty by writing some actual RxJava code.

**I’d suggest that you start by making some API calls with RxJava and I’ve already published a post for this exact same purpose: [Networking with Retrofit-RxJava-MVP Architecture](https://ayusch.com/networking-with-retrofit-rxjava-mvp/)**

Understand what’s going on here. You’ve probably already made some API calls in your Android Development journey using Retrofit/Volley. But this article will explain how to put them together properly in order to get separation of concerns and make your code more modular and ultimately easy to understand and scale at some later stage.

It also includes the use of MVP Pattern which is really simple but you can omit that if it gets too technical. Just **focus on creating the Adapter, the API service interface, and the UserTask**. Rest assured that it’s all just simple Android code. You can invoke UserTask from anywhere and get the result in a callback.

Once you’ve done this, you’ll get a gist of what it’s like to work with RxJava.

Next, you should develop an app yourselves which involves networking. You could you the fakeJson web service/make a twitter client/consume a rotten tomatoes API, or anything which involves networking. You’ll find out how different operators such as **Map** and **FlatMap** come in handy while transforming your observables into something of your requirement.

As you do that, you’ll start feeling more confident with RxJava routines and observe that most of the code is the same across these applications. Of course, there will be different operators used and a difference in your models. But the overall gist is somewhat similar.

Now you’re ready for **Phase 3** and getting to that Eureka moment ?

### Phase 3

#### Eureka!

This is the phase where you’ll get out of your comfort zone and start exploring what RxJava can do for your **Android** app rather than just networking. This is where you’ll learn about the art of state management with RxJava and how you can Rxify almost everything in your code. In this section, I’ll push you to start State Management with RxJava.

This is also the point where you are ready to watch all of **Jake Wharton’s** talks on RxJava. Actually, this will be your task in this phase, but first, let’s understand what is state management.

**What is state management?**

Let’s think of an **example**. Say, you have a simple login/signup application where you ask the user for their username and password and when they click a button, you sign them in/direct to a signup page.

Now as soon as the user enters his details and clicks the submit button, a loader is shown while the app sends the data to a backend service and waits for the response. We can say that currently, our app is in an “inProgress” state.

As the result is returned, the app reverts back to the “**Idle**” state.

To elaborate further, let’s talk about the submit button. When the text fields are empty, i.e. the user hasn’t entered anything yet, then the button should be disabled. So, “disabled” becomes a state of the button. When the user has entered the info and the fields are validated, the button should be in “enabled” state.

So, you see, everything you see on the screen, exists in a particular state. Right from that button, to the progress bar, everything is in a particular state.

**All’s good but what to do now?**

Here’s what I want you to do.

**Start** by watching this talk about state management by Jake Wharton:

This talk is for **advanced** developers and I had to watch it at least 10 times to wrap my head around what was going on. But watching a video alone won’t make you a pro at RxJava. You’ll need to state manage your applications using RxJava.

To practice with state management, I’d suggest picking up any simple idea/one single screen and start state managing it with RxJava. For example, if your app includes a login/signup screen, you can perform its state management using RxJava as mentioned above.

**Here are a couple of ideas for you:**

* **Develop a login/registration app**. After the user logs in, consume the Rotten Tomatoes API. Allow a search functionality so the user can search for movies according to his liking. In all of this, the progress bars and the animations must be states which would be managed within RxJava streams. Rx would also be used for making API calls.
* **Check out [this](https://github.com/kaushikgopal/RxJava-Android-Samples) repository** by Kaushik Gopal which includes an example of form validation with RxJava. Clone it, and try and understand the code. Once you’re comfortable, start implementing it yourself. Think of what all states you could add to it to increase the complexity. For example, a checkbox to reveal the password.

You’ll definitely get your Eureka moment in this phase where you realize the vast potential of RxJava and how you can possibly do anything with it and make your code neater.

### Phase 4

#### Sky’s the limit

I’ll leave this section blank for you. Now it’s up to you to tell me about all the creative ways you’ve used **RxJava** in your code and how RxJava has made your life easier than before. One thing I’ve noticed as I’ve started writing these blogs is that these have definitely helped me become a better Android developer as I’m accountable for everything I post.

In this post, I’ve shared everything that worked for me and what I think will work for you. If you have any suggestions, let me know in the comments section below. I urge you to share your learnings with everyone and help each other grow and become better engineers.

Like what you read? Don’t forget to share this post on [**Facebook**](https://www.facebook.com/AndroidVille), **Whatsapp**, and **LinkedIn**.

You can follow me on [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain), and [Instagram](https://www.instagram.com/androidville/) where I **answer** questions related to **Mobile Development, especially Android and Flutter**.

**If you want to stay updated with all the latest articles, subscribe to the weekly newsletter by entering your email address in the form on the top right section of this page.**

