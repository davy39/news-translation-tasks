---
title: How I Developed My First Adventure Game
subtitle: ''
author: Andrea Koutifaris
co_authors: []
series: null
date: '2022-03-09T20:05:24.000Z'
originalURL: https://freecodecamp.org/news/how-i-developed-my-first-game
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/presentazione-new.min.jpg
tags:
- name: Art
  slug: art
- name: C
  slug: c
- name: '#Game Design'
  slug: game-design
- name: Game Development
  slug: game-development
- name: lessons learned
  slug: lessons-learned
- name: technology
  slug: technology
- name: unity
  slug: unity
seo_title: null
seo_desc: 'It''s hard to tell exactly when my journey creating Occulto, a point and
  click adventure game, started. But I have a significant date in mind:

  3 May 2018.

  Here''s one thing that got the ball rolling:


  Luigi: Hello Andrea. Sorry to bother you. I would l...'
---

It's hard to tell exactly when my journey creating Occulto, a point and click adventure game, started. But I have a significant date in mind:

3 May 2018.

Here's one thing that got the ball rolling:

> Luigi: Hello Andrea. Sorry to bother you. I would like to learn how to develop an app. Am I crazy?

> Me (Andrea): Hmm... I don't have your number... who are you?

Reading those two WhatsApp messages now makes me smile. But there are also two other pieces of interesting information:

First, that was May 2018. Now it is 2022... 3 years and some months later, we have published our very first game DEMO. So yes, it took us 3 years to release a demo.

But we are now producing at a steady pace, and in the first months of 2023 we will release the whole game.

That said, if you are planning to develop a game yourself, it won't necessarily take you 4 years…and I have some advice that hopefully will help!

Second, an app – everyone wants to make an app. Do we really need another app? What about a game instead? What I mean is: an adventure game is like a book, you install it, play it, enjoy and eventually uninstall it. It is not yet another app polluting your phone's memory.

Before I start, let me step back and explain what this article is about.

## What We'll Discuss in This Article

This article is about how I (Andrea) and Luigi developed *Occulto*, our first adventure game.

It will cover some technical aspects of the project, as well as how we managed creating and developing it. I'll discuss both psychological and practical parts of the journey.

I'll also provide a shallow comparison between using web technologies (like WebGL) for development vs Unity 2D.

This article consists of:

* A brief story about my passion for Adventure P&C games, and how I ended up developing my own game.
    
* A section about *Occulto*, the game I am developing
    
* A tech section with a comparison between web technologies and Unity 2D
    
* A section about what I learned through the process, along with some advice if you're creating your own game.
    

## How I got Into Adventure Games

Many years ago, a good friend introduced me to [Machinarium](https://amanita-design.net/games/machinarium.html). Machinarium is one of the best adventure games I've ever played.

After I finished it, I felt the need to create my own adventure game. This feeling was not immediate, but grew stronger over time. Eventually it led me to find Luigi and be actually able to create my own indie game.

### First adventure game attempt

![Image](https://www.freecodecamp.org/news/content/images/2021/10/newton-scene.jpeg align="left")

In my first attempt at building a game, I contacted some friends and created a small group of people who were enthusiastic about creating an artistic P&C game.

We managed to create a draft of the first scene (see the illustration above). The idea was to make an apple fall on Newton's head, who is resting under the tree.

I used the [Playn Java framework](https://github.com/playn/playn) to write in Java and export to Android, iOS and web. At the time I was a Java developer. Playn is still an active project, it may be worth considering if you are looking for a Java 2D game framework.

This first attempt didn't last long. We had a dinner all together, and asked two friends to present us with a draft story of the game. And then I didn't get any feedback from the others and the project vanished into nothing.

### Second attempt

![Image](https://www.freecodecamp.org/news/content/images/2021/10/cover-red-moony.min.jpg align="left")

In my second attempt I managed to create four scenes and some game-play among them. But the project failed because I wasn't ready to lead the project. You'll read about that soon.

Below you can see an image of one of the scenes of the game. It was intended to be a modern revisiting of Little Red Riding Hood were wolves were not bad :).

![Image](https://www.freecodecamp.org/news/content/images/2021/10/room.min.jpeg align="left")

## Third and Final Adventure Game Attempt: Occulto

Developing *Occulto* is my 3rd attempt at creating an adventure game – and hopefully this one is successful!

![Image](https://www.freecodecamp.org/news/content/images/2021/10/village-editor.min.jpg align="left")

*Unity Editor: 1° Village*

### Intro to the game

It is a beautiful morning, and Eliot, a young mage apprentice, is going to the studio of his magister for a lesson about magical potions. Something is wrong from the first moment: why isn't the magister opening the door?

Inside the studio everything is a mess, and a note tells Eliot to go to the church in the village. What is going on? Where is the magister?

![Image](https://www.freecodecamp.org/news/content/images/2021/10/studio.jpg align="left")

*2° Magister studio*

Will you help Eliot in his journey to find his magister and regain possession of the powerful forbidden book titled "The never written book" that an evil figure is trying to steal?

The demo consists of four scenes:

![Image](https://www.freecodecamp.org/news/content/images/2021/10/monastery.jpg align="left")

*3° Monastery*

and one secret passage between the monastery and the private studio of a monk.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/secret-passage.jpg align="left")

*4° Secret passage*

Below you can see the last scene of the demo.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/hunckback-studio.jpg align="left")

*5° Monk private studio*

## Tech I Used to Build My Adventure Game

![Image](https://www.freecodecamp.org/news/content/images/2022/03/unity-vs-pixijs.png align="left")

We developed *Occulto* in the beginning using [Pixi.JS](https://pixijs.com/) and HTML. Then, later, I switched to Unity using the 2D features that are now included as default in the editor.

Since this article is quite long, I will not enter in the details of the code. But I will provide a description of the technologies we used and the process of creating the game.

I am planning to write a second article for the technical part.

We are a group of 3 people:

* Myself, Andrea, the developer and project/technical manager. I contribute to the story and game/riddle design as well. I am a software engineer.
    
* Luigi, the wonderful artistic designer who designs and draws the scenes. He is also responsible for the game story and game-play. If you like the illustrations above, then you like Luigi's work :). He graduated in Mathematics.
    
* Antonio is the music and sounds designer. He is a software engineer.
    

Luigi draws the scenes using [Photoshop](https://www.adobe.com/products/photoshop.html) and makes the animations using [After Effects](https://www.adobe.com/products/aftereffects.html). Then he exports everything into images (jpg and png) that I later use to assemble the scenes.

In addition Antonio provides me with the sounds and music for the scenes. We are using mp3 files at the moment, but we are planning to switch to [FMOD](https://www.fmod.com/) in the future.

The game uses FHD (1920x1080) images, and runs also on low end mobile devices. If you want to run on a device with 1 GB of RAM, you need to reduce the amount of FHD images. If you load in memory more than 50/60 FHD images, the game may crash on devices with not enough memory.

In normal Unity memory management, the entire scene is loaded on memory, so you have to pay attention to what you add to the scene.

A simple and classic solution to reduce the memory imprint, is to use sprite sheets for the animations. Most of the time an animation will fit in a 2048x2048 sprite. I use [Texture Packer](https://www.codeandweb.com/texturepacker) to create and import animation sprite sheets in Unity.

In addition I use [ImageMagick](https://imagemagick.org/index.php) [CLI](https://en.wikipedia.org/wiki/Command-line_interface) to trim images with an object inside. My input is a FHD transparent PNG with an object inside placed in the right position. Then I use:

```bash
magick mogrify -trim -verbose *.png > trim.txt
```

to trim the image and get the precise position of the object.

Finally I add the trimmed image to the scene and place it using a script I made that maps the coordinates inside *trim.txt* file to the x,y values of the Unity scene.

By trimming and using sprite-sheets, I solved all memory problems. Also smaller images means lower time when loading a scene. In cheap mobile devices, loading a scene can require like 5 or 6 seconds (whereas in more powerful devices it takes less than a second).

Regarding fps and performance, Unity is good – so basically you don't have to do anything special. You just need to avoid bad design. And pay attention to [time complexity](https://en.wikipedia.org/wiki/Time_complexity). For example, avoid searching for an element on every tick of the game loop.

As I mentioned earlier, I am planning to write a tech article about how I developed the game using Unity 2D. If you are interested, follow me or follow us on one of our social accounts.

### Unity vs WebGL

Even if I used both technologies, I am not an expert (this is my first game). So below I will just list some of the pro and cons of both technologies.

#### Pros of WebGL

* Easy to port everywhere with [Capacitor](https://capacitorjs.com/) or [Electron](https://www.electronjs.org/).
    
* Programmers friendly: [PixiJS](https://pixijs.com/) makes it very easy.
    
* Almost the only working solution if you need a web responsive version.
    
* Continuous integration and delivery to web is very easy, since the output is a bunch of files.
    
* Web development is mature, and you have access to tons of libraries, utilities as well as a web packers, like [Webpack](https://webpack.js.org/).
    
* Collaboration is very easy and mature with Git. There is something about collaboration in Unity, I didn't explore it. I don't know what happens if two people work on the same scene.
    

#### Cons of WebGL

* Slightly lower performances compared to more native frameworks.
    
* Subject to WebViews bugs (which you cannot solve).
    
* It can be difficult for programmers who do not know web development.
    
* WebViews doesn't seem to be ready to perfectly support WebGL. The game wasn't working well on my Neffos, and who knows on which devices it had issues. Maybe WebViews are not yet ready for gaming, but they are definitely ready for HTML and hybrids app.
    

#### Pros of Unity

* Graphical editor: it is easier to visualize/update the scene and fine tuning.
    
* Easy and complete: it has almost everything you need.
    
* Good performance: 60 fps even on low end devices at 1920 x 1080 resolution.
    
* Cross platform, but the WebGL version does not work well on mobile phones.
    
* A lot of indie games are made using Unity. If the Unity team introduces a bug, it will be found very soon.
    

#### Cons of Unity

* Graphical editor: you need a working updated Unity editor in each of the computers you are going to use. With Linux it's not that simple.
    
* [Closed licence](https://store.unity.com/compare-plans) but it has a free tier if you earned up to $100K in the last 12 months.
    
* At the moment the mobile web version is not officially supported.
    
* Linux Unity editor is alpha (and I managed to make it work after many attempts).
    
* Not a lot of helpful info about it: most of the posts I read to find help about a particular topic were low quality or were videos. That's far away from stack overflow quality. But the documentation is well done.
    

Keep in mind that this section is not intended to be an exhaustive comparison between Unity 3D and WebGl frameworks. Depending on your target, one technology could be better than the other.

That said, even if I am a web developer, I must admit that Unity is great for developing a 2D games (and I guess 3D games too).

## What I learned While Building Occulto

![Image](https://www.freecodecamp.org/news/content/images/2022/03/1_zGuG4nFo8O4e0WMoNWVbMA.jpeg align="left")

### Someone needs to lead the project

This is my first insight: if it is you who propose a project to others (a game, an app or whatever), they will assume you will lead the project.

At the time I was thinking that I was just a programmer, and didn't act like a project leader. It won't work if someone doesn't actively follow every person in the project.

### Have the right attitude

It is important to have the right attitude towards people that are participating in the project. You also need to understand if they can be productive.

In this context, "productive" does not have the same meaning it has at work. Productive means "actually able to produce". At work it means how much you produce and how good is your output.

Before I go on, let me tell you a story:

Before embarking on *Occulto* game development, I decided to help a guy develop the interface for his board game. I did it because I thought the game he invented was a good game that had some brilliant parts to it.

In this case I was the developer, and he was leading the project (being the inventor of a game, doesn't unfortunately imply that you are also good as a project leader).

In the beginning everything was good, and I enjoyed developing the game. In addition I was learning React, which I used as the framework to build the game app. (It is a board game, not a classic one, so React was a good choice, and also it had a lot of pages, not just the game page).

Then things started to become weird: he started asking for deadlines, complaining about delays on the development, and asking for features which I thought weren't really useful in the first version of the game.

In the end it didn't work out and I couldn't work well with him, so I blocked all communication. Remember that I worked on his game for free, and I even solved a nasty bug that caused the back end side of the game to stop working.

So, why this story? To tell you that making a game with a bunch of friends is a very different job than what you do at work. Some advice:

* **Don't push people too hard**: if you are making a game for fun, it must be fun. Motivate people and help them. They are working (as you are) for free on a project they believe in.
    
* **Don't act like a boss**: even if you direct and follow every step of the game, people should regard you more as a project manager/team leader than a boss.
    

### Work in your spare time

Being able to be "productive" applies also to you. Are you able to work in your spare time on the game? Can you provide a steady output, without long periods of time away from the project?

This is the first obstacle I encountered in my previous attempts. I wasn't able to provide a constant, timely output and people thought the project was falling apart.

In this case, as a programmer, it is important to integrate the output of your other team members (images, animations and sounds) as soon as possible. People will be more engaged if they see their work quickly integrated in the game. Also the sooner you integrate others' work, the sooner you will find and solve problems.

### Remove as many obstacles as you can

In order to work in your spare time, you have to reduce or remove all the obstacles. These can be physical (slow computer, too small a screen, ...) or psychological. The psychological ones are the most subtle. I will try to list some of them:

**Feeling guilty for not working**: this is hard, and I think is one of the main reasons for quitting. You have to enjoy working on your project. So deadlines, pushing others to produce more, threatening (like "If you don't work enough you are out") do NOT work.

It is better to motivate people and help them understand what's blocking them (or you) to produce some output.

**Obstacles that delays the moment you can actually work**: you may think something like "I'd like to finish that thing I started, I think I can complete it in 10 minutes." Then you think: "But the PC is slow and it will take forever to start... may be tomorrow, now I'll just serf on Instagram".

It is important that when you think you can work a bit on the game, you can actually do it without any delay or obstacle.

**Too tired to work on the game**: indeed you must not overdo it. It is important to find a balance between how much you work and how much you rest. But it is also important to avoid long periods of not working on the game.

I noticed that small actions can help: for example for me it is enough to start the Unity Editor to increase the chances that I'll actually work on the game.

**Share your results with the others**: even though non technical people may not fully understand what you are doing (and vice-versa), it is satisfying to explain that you solved a performance problem, or that you reduced the bundle size, for example.

In fact, in agile methodologies, telling what you did and what your are going to do is one of the main points.

**Persist**. Not everything will be easy. You will have to persist. Even though you are probably making a game because of passion, it is still requires a lot of work and sometimes you have to persevere and overcome problems/blocks. You probably do that all the time at work, you can do it also for your game.

**Not every moment is a moment of pleasure**. Imagine when I discovered that the demo, almost ready to be published, wasn't working on some mobile devices and I had to rewrite everything in Unity. I really had a bad weekend.

But then I manage to change my attitude, start with Unity, and regain pleasure in working on the game.

Fortunately Luigi, my partner in the game, understood it and accepted that we needed to delay the release date of the game demo. While it took a lot of time to write the demo (2 years, if you count from the first commit), it took me 3 months to rewrite it.

### Focus on developing the game

It is extremely important to focus on making the game, and not the framework for the game.

Being a programmer you will probably want to write more code than necessary and use your preferred language. Chose a framework based on your needs (cross platform? 2D or 3D? ...) and try to develop a simple level to understand if you made the right choices.

When you start, you won't necessarily have a clear view of the possible frameworks/technologies available to build a game – and there are a lot. In addition you will be biased towards some languages/features.

About that, I can tell you 2 mistakes I made:

I used PixiJS and HTML technologies at first. As opposite as you may think, I was able to go at 60 fps with FHD (1920x1080) resolution even in medium performance mobile devices.

This is because most of the work is done by WebGL. But at a certain point the game started flickering on my old mobile phone (Neffos X1 Max) when ported to a mobile app using Capacitor (webview). But it was working well on the browser and on the other phones I had. Even on my Motorola Moto G first generation (2013 low end device).

I should have tested earlier on mobile (not just with the browser). Also the game wasn't smooth on the my lower end device Moto G (still it was running near 30 fps).

I decided that I wanted my game to run smoothly even on low end devices, so I switched to Unity 2D. Unity is used by a lot of indie game developers, and C# is quite easy. I didn't try Unreal Engine, because I am too rusty on C++. Now it runs smoothly also on my Moto G (60 FPS).

The second thing that was almost a mistake is that I developed a library to find the shortest path on polygon areas with polygon holes. [Here](https://github.com/Kouty/shortest-path-polygon-area) you can find the JS code (I have ported it to C#, but not yet release on GitHub).

I took me 3 attempts to get it working properly, and a lot of time. Fortunately by the time I started developing *Occulto*, the library was ready and working. Now I can just draw the walkable area and have the main character move inside it, avoiding obstacles (polygon holes).

The fact is that having an algorithm to move things inside a walk-able area is not strictly necessary, and it is better to focus on actually making the game. Other P&C games do not use this feature, they just move characters along predefined paths.

So, before you embark on something that is not strictly necessary for the game, see if you can find something already implemented or if it is really worth it.

### Release a one scene version of the game

After you've chosen the right framework, take a scene, and develop the entire game which will consist on one scene plus a menu and every UI component that is cross scene. It is important to learn everything you need and to find problems as soon as possible.

Also, submit the game for internal testing (not public) to the stores you are going to use. Yes, do everything that's necessary from developing to publishing (privately) the game.

When I published the game demo on iOS, one animation wasn't working. It was working on Android, Desktop, and even on iPhone with the developer build. So yes, you need to test everything as soon as possible, even the process of publishing.

I made the mistake to first develop the whole demo (four scenes, plus menu and some other screens) just to find out that WebGL technology was not the right choice for my game.

## Final Notes

I hope you enjoyed reading this article and found some interesting advice. Maybe I will write another article when I have published the whole game, sharing other insights.

If you are curious about [*Occulto*](https://www.sirioartgames.com/) game, follow us on:

* Twitter: [https://twitter.com/SirioArtGames](https://twitter.com/SirioArtGames)
    
* Instagram: [https://www.instagram.com/sirioartgames](https://www.instagram.com/sirioartgames/)
    
* Our website: [https://www.sirioartgames.com](https://www.sirioartgames.com/)
    

or [try the demo](http://onelink.to/mxsak4): [http://onelink.to/occulto](http://onelink.to/occulto)!
