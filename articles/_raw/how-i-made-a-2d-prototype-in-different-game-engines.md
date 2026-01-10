---
title: I attempted to make the same 2D game prototype in React, Unity, Godot, Construct,
  Game Maker, and Phaser. Here's what I found.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-11T16:17:31.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-a-2d-prototype-in-different-game-engines
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/EntromancyHB_Logo_COLOR.jpg
tags:
- name: phaser 3
  slug: phaser-3
- name: C
  slug: c
- name: construct 3
  slug: construct-3
- name: Game Development
  slug: game-development
- name: game-maker-2
  slug: game-maker-2
- name: Godot
  slug: godot
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: unity
  slug: unity
seo_title: null
seo_desc: 'By M. S. Farzan

  I''m a tabletop game developer. In designing a new card game, I decided to build
  a digital prototype to help me run simulations and easily share a proof of concept
  with collaborators.

  I have some background in JavaScript and C#, and I ...'
---

By M. S. Farzan

I'm a tabletop game developer. In designing a new card game, I decided to build a digital prototype to help me run simulations and easily share a proof of concept with collaborators.

I have some background in JavaScript and C#, and I set out as many do: by spending an inordinate amount of time in "what framework should I use" threads and reading documentation without actually making anything. 

Flash forward many months, and I've now spent more time working in (and wrestling with) React, Unity, Godot, Construct 3, Game Maker Studio 2, and Phaser 3, in an attempt to understand what makes them tick.

Admittedly, I think I've spent _way more_ time in each of them than necessary to make my little game, and I probably could have just stuck with the first one and blundered my way through the prototype. I'm hoping the below info will be helpful for anyone else who is shopping around for an engine or framework.

Bunch of caveats: I'm not attempting to sell one engine or framework over the others, and I'm also not suggesting that one or any of these frameworks will work for your game better than another. I'm also not comparing pricing, back end functionality, or platform deployment. So depending on your requirements, the below information might be of differing value to you.

Additionally, this experience is based on development for a 2D card game, so I won't be discussing 3D engines, physics, etc.

You can also **skip to the bottom for the TL;DR.**

%[https://www.youtube.com/watch?v=gtKEkuhsWOs]

## The Prototype

My game, _Entromancy: Hacker Battles_, is a competitive cyberpunk card game with TCG-light mechanics. You can read more on our [website](https://www.entromancy.com) or watch how it's meant to be played in [this video](https://www.entromancy.com/single-post/2019/09/26/Get-a-Sneak-Peek-at-Entromancy-Hacker-Battles). But suffice it to say that, as a card game, it requires a potential digital framework to support basic things like state management, UI, drag-and-drop UX, and back end hooks for implementing multiplayer.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/HackerBattles_Card-Mockup.png)

Given these requirements, I explored the following frameworks and engines to see which one would be most suitable for making my game...instead of actually _making_ the game (I'm happy to say that now that I've settled on a framework, I'm making a lot more progress). 

You can access a playable version [here](https://sominator.github.io/hacker-battles/), and although the game is further along than the live prototype would suggest, this version is pretty stable (in Chrome at least).

## React

Having already built a character generator prototype in [React](https://reactjs.org/) for a [tabletop RPG I designed](https://www.entromancy.com/rpg), I thought a natural step would be to give the framework a spin for the card game. I found state management to be a breeze (it's what React _does_, after all), whereas implementing simple drag-and-drop functionality for cards proved to be a nightmare.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/React_Native_Logo.png)

There are some libraries out there that can help with basic drag-and-drop (e.g. [React DnD](https://react-dnd.github.io/react-dnd/about)), but I found that with a card game, I needed a more elegant solution for dropzones, as Hacker Battles is very specific about which cards can be played where, and when.

This experience led me to check out [boardgame.io](https://boardgame.io/), which can work in tandem with React. But this ultimately required me to learn another framework on top of an existing framework, which was less than ideal for my purposes.

## Unity

Out of general interest, I had spent a lot of time in [Unity](https://unity.com) doing tutorials and learning how to use the editor before attempting to remake the card game prototype with it. The asset store is a great resource, and there's so much documentation, official and unofficial, out there that I was confident I could find an answer to any issue I might encounter.

My experience with Unity thus far has been a mixed bag. I really enjoy working in C#, and anything code-related has been a relatively pain-free experience. However, Unity is very specific about its implementation and can feel counter-intuitive at times.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1280px-Unity_Technologies_logo.svg.png)

The editor, on the other hand, is a bear to work with. To harness Unity's full potential, you need to spend a good long while wrestling with the UI to understand where everything is and how to use it. It's also desperately behind the times with 2D game development, clearly attempting to flatten a primarily 3D engine into a 2D plane, with mixed results.

To be fair, I quite enjoy working in the Unity editor, clunky as it is. But if you're looking for a 2D game engine, your quality of life will be a lot higher elsewhere (watch a video on Unity's animation system or achieving pixel perfection and you'll see what I mean). 

Ultimately, Unity's handling of the 2D space is a bit more complex than I need for my prototype, but I will return to it for other types of games.

Also, a sidebar that might be useful to some: I was initially extremely excited about the asset store, with the idea that I could purchase a card game template that would make the development process that much easier for me. It didn't work out. Most of them were MTG/Hearthstone/etc. clones that would require just as much development time on my part to restructure them for my card game as it would to just start from scratch. <shrug>

## Godot 

My first thought upon encountering [Godot](https://godotengine.org) was: "open source game engine that supports C#? Sign me up!" Then I downloaded it, worked through a couple of basic tutorials, and had it crash on build. Hurm.

Several Google searches, reinstalls, and hairs pulled later, I figured out it had something to do with my version of VS Build (I think?), which led me down a separate rabbit hole. I knew from experience that other engines - Unity chief among them - could cause game-breaking issues completely outside of your own code, but this was an annoying hurdle that likely colored the rest of my experience with Godot.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Godot_logo.svg)

In terms of the editor, I quite liked Godot's node-based implementation, which I actually found counter-intuitive coming from Unity's prefabs, but eventually warmed to. I'd actually go as far as to say that its 2D functionality is _better_ than Unity's, but it's missing the community, asset store (see sidebar above), and especially, the documentation that Unity has. If you're intending in working in C# with Godot, for example, be prepared to look for answers in the engine's custom GDScript and then translating them to C#.

I have heard, however, of people experiencing great success with Godot while using GDScript, so if you're willing to invest the time to learn it you might enjoy what Godot has to offer.

## Construct 3 

In the caveats that I listed above, I mentioned that I'm not including pricing as a point of discussion. Still, I feel like I need to bring it up with [Construct 3](https://construct.net/), as it turned out to be impactful in my experience. 

Unlike the other game engines listed here, which are, for the most part, free to use (Game Maker Studio 2 has a 30-day free trial), the vast majority of Construct's functionality is behind a pay wall, and a subscription fee at that. Ugh.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Construct_3_Logo.svg)

I really, _really_ like the cut of Construct's jib for simple 2D games. The editor feels a bit like an upgrade from MS Paint, but it handles sprite and object management really well, and is just plain easy to use. I don't love that it uses a "visual scripting" style, but they've recently added the feature of writing plain old JavaScript and it seems to more or less work.

I was able to spin up a very rudimentary architecture for the prototype in a brief amount of time before closing the Construct 3 demo (which runs in a browser)...and then trying it all again later with a new demo. I feel like, at least for this card game, I could do a lot with Construct 3, but I'm just not willing to pay $99/year (or more, as a business) for a prototype.

## Game Maker Studio 2

YoYo Games has clearly done a lot of work to make [Game Maker Studio 2](https://www.yoyogames.com/gamemaker) accessible and easily navigable, and it shows. Of all of the engines that I've used for this project, I like the GMS editor the most. For a small project, it's easy to find your way around and go about your business. I suspect, however, that a larger project might get out of hand pretty quickly.

This might be influenced by Game Maker Studio's proprietary language, GML (although GMS 2 supports visual scripting, which I did not use). It works, but if you're coming to it from another OOP language (or, truly, any other widely used language), you might scratch your head at the implementation or figuring out how to do some things. If you're a beginner or willing to spend time figuring out how GMS _wants_ you to use GML, you'll probably be fine.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/download.png)

I experienced some quirkiness with Game Maker Studio's drag-and-drop functionality - namely, mouse pointer detection upon dragging is a little wonky and requires some scaffolding to make work correctly. 

I think - and this is totally personal preference and laziness on my part - that if GMS offered the ability to use another, non-proprietary programming language, I would spend the time to do more damage here. I'm all for leveling up multiple skills while working, whereas spending the time to become an expert in the GMS editor _and_ GML without being able to easily apply that knowledge elsewhere doesn't seem worthwhile.

Still, it's a pretty workable 2D editor, and although the community support may not be on par with Unity's, it's still pretty good.  Beware, also, that once your free trial is up, you'll have to pay to continue using Game Maker Studio 2.

## Phaser 3

[Phaser](https://www.freecodecamp.org/news/how-i-made-a-2d-prototype-in-different-game-engines/phaser%20io) is a lightweight, open-source JavaScript game framework. There are some Phaser IDEs around, but if you're of the sort that wants to work primarily in code, you might wind up here, using Atom, Sublime, or your favorite editor.

Phaser 2 was and is widely used and well-documented with a ton of tutorials to draw upon. Phaser 3 is the opposite. It has a comparatively high learning curve for beginners, with a bunch of examples and not a lot of context around them. 

A lot of the tutorials out there support Phaser 2, and while the learning is transferable, the code is not. Additionally, the devs [recently announced that they'll be moving support to Phaser 4](https://madmimi.com/p/4f5f0f) (and TypeScript rather than ES6), which is not great if you've spent time working in Phaser 3.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Phaser_-game_framework-_logo.png)

If you're not a professional programmer (I'm not) and up-to-speed with ES6 classes and JavaScript best practices (I wasn't), you might become quickly frustrated with Phaser's lack of handholding and having to set up your own IDE and work flow (I was). 

However, I've found it to be a powerful, lightweight framework that does a lot of things in a much more streamlined fashion than other game engines. Drag-and-drop functionality for the card game has been a relative breeze, and the ability to separate card types into classes (sort of like Unity's prefabs) has compartmentalized some of the cognitive load that this kind of game requires.

If you're a front end developer, you might like or be comfortable with hard coding pixel coordinates for everything, but sheesh, is this painstaking work. Additionally, if you're not up-to-speed on everything JavaScript, you'll most likely be searching for answers in non-Phaser circles and then applying them to your project, which has its own benefit, I suppose.

One other note in case it's not clear: Phaser 3 _does_ have quite a bit of official documentation and examples, but it _doesn't_ have the community or Stack Overflow answers that a lot of other game engines enjoy. If you run into an issue or can't figure something out, you'll have to figure out your own solution or post your question on the Phaser Discord server, which has been helpful in my experience.

## Conclusion 

Given all of the above, the prototype I've stuck with and continue to iterate upon is the one I've built with Phaser 3. I realize that this may be anti-climactic, as Phaser isn't inherently "better" than the other frameworks and engines at 2D game development (except for, perhaps, React, which isn't trying to be a competitor in the digital game space).

Phaser does, however, seem to handle drag-and-drop and game loop management for _Hacker Battles_ more smoothly, and for my purposes, that's important. I also enjoy that using Phaser is requiring me to invest more heavily in the JavaScript ecosystem(s) and communities, but I'm interested in doing that anyway so it feels like a bonus. 

If you're more of the "what can I use to build something quickly and not care about the context in which the engine is situated" type, YMMV.

## TL;DR

**React:** great for front end development. Wouldn't use it for games, particularly drag-and-drop.

**Unity:** you can make any type of 2D game if you're willing to wrestle with the editor and underlying 3D idiosyncrasies. Great community support, and C# is awesome. Asset store exists, but may not be useful for your purposes.

**Godot:** open source and supports GDScript, C#, even C++ and Python if you're willing to do a lot of the heavy lifting. Good 2D implications but not nearly as much community support as something like Unity. Also, my experience was buggy.

**Construct 3:** really easy to use, high barrier to entry because of the subscription paywall. Visual scripting may get on your nerves if you're looking to use or learn code, although there is now some JavaScript support.

**Game Maker Studio 2:** user-friendly editor with good community support. GML or visual scripting might not be your cup of tea if you're coming from another more popular programming language, but hey, when in Rome. Also, requires payment after a 30-day free trial.

**Phaser 3:** expect to code everything, and do a lot of searching to figure out how to make things work. It's working for me for this particular game and prototype, but Phaser 4 is on the way, so there's that.

I hope this post is useful in your own search and discernment process. I'd love to hear about your own experience(s), too, with any of these frameworks/engines or others!

If you enjoyed this article, please consider [checking out my games and books](https://www.nightpathpub.com/), [subscribing to my YouTube channel](https://www.youtube.com/msfarzan?sub_confirmation=1), or [joining the _Entromancy_ Discord](https://discord.gg/RF6k3nB).

**M. S. Farzan, Ph.D.** has written and worked for high-profile video game companies and editorial websites such as Electronic Arts, Perfect World Entertainment, Modus Games, and MMORPG.com, and has served as the Community Manager for games like _Dungeons & Dragons Neverwinter_ and _Mass Effect: Andromeda_. He is the Creative Director and Lead Game Designer of _[Entromancy: A Cyberpunk Fantasy RPG](https://www.entromancy.com/rpg)_ and author of _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Find M. S. Farzan on Twitter [@sominator](http://www.twitter.com/sominator).

