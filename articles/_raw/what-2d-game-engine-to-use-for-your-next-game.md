---
title: What 2D Game Engine to Use for Your Next Game
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-04T20:47:36.000Z'
originalURL: https://freecodecamp.org/news/what-2d-game-engine-to-use-for-your-next-game
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f9f740569d1a4ca4397.jpg
tags:
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
- name: phaser 3
  slug: phaser-3
- name: React
  slug: react
- name: unity
  slug: unity
seo_title: null
seo_desc: 'By M. S. Farzan

  A few weeks ago, I posted about my experience attempting to make a prototype in
  a bunch of different 2D game engines/frameworks to learn what makes them tick.

  If you''re shopping around for an engine for your next 2D game, this article...'
---

By M. S. Farzan

A few weeks ago, I [posted about my experience](https://www.freecodecamp.org/news/how-i-made-a-2d-prototype-in-different-game-engines/) attempting to make a prototype in a bunch of different 2D game engines/frameworks to learn what makes them tick.

If you're shopping around for an engine for your next 2D game, this article will provide some things to consider that may help in your discernment process.

Do note that I'm not attempting to cover every 2D game engine out there; nor am I positioning one engine or framework over another.  These recommendations are from my personal experience using different engines and frameworks for prototyping.

And if you'd prefer to watch rather than read, I've created a video version of this post (26 minute watch):

%[https://www.youtube.com/watch?v=gtKEkuhsWOs]

## React

At first glance, you might be thinking, "[React](https://reactjs.org/) is a front end framework for making interactive websites. It's not a game engine!" And you'd be mostly correct.

React doesn't provide native support for game development basics, like, for example, 2D physics, but it _does_ handle state extremely well.  If you're already a JavaScript developer and willing to pair React with something like [boardgame.io](https://boardgame.io/) to make a simple 2D game, you could potentially get a prototype up and running pretty quickly.

For all other types of 2D games, you'll want to look elsewhere.

## Unity

[Unity](https://unity.com/) has made itself ubiquitous in the 2D and 3D game development spaces. I'd position it as an excellent 3D game engine, and a serviceable 2D one.

The Unity editor is fairly complex, with a lot of nested menus that take some time to wrap your head around (check out [this article](https://www.freecodecamp.org/news/take-a-tour-of-unity-2d/) for a tour of its 2D features).  If you don't already have a background in C#, which Unity uses for scripting, you'll want to brush up on it prior to learning Unity, as doing so will ease your overall learning curve.

Unity also does a lot of things the "hard way" when it comes to 2D game development, which doesn't _feel_ native compared to other game engines.  Creating a 2D game world in Unity, for example, feels like you're shoehorning a 2D plane into a large 3D space, and things like animation and pixel perfection are more clunky than in other 2D-specific engines.

You can make any type of 2D game with Unity if you're willing to wrestle with the editor and underlying 3D idiosyncrasies. It has extensive community support, and you'll find that working with C# is a delight. Additionally, Unity's Asset Store has all kinds of art and templates for you to download and purchase, but buyer beware: you might spend as much time rewriting someone else's code to fit your project as you would just starting from scratch.

Unity is, in general, free to use, but pricing becomes more complex if you want to use _everything_ it has to offer (see [this page](https://store.unity.com/compare-plans) for more details).

## Godot

[Godot](https://godotengine.org/) is a free and open source 2D and 3D game engine that supports GDScript, C#, and even C++ and Python if you're willing to do a lot of the heavy lifting to make them work.  It supports a node-style workflow and is super lightweight.

If you're a) willing to invest in learning GDScript or b) already super good at C#, C++, or Python, you'll probably be fine in Godot, particularly if you like working with open source software.  If not, you may get easily frustrated, as there isn't nearly as much support for C# or other languages as there is for GDScript.  Still, Godot is a pleasant engine with which to work, and although it may not have the same pedigree and community support as something like Unity, if you're a self-starter you might feel well at home.

## Construct 3

If you just want to make 2D games and don't care about programming language or subscription fees, you'll find [Construct 3](https://www.construct.net/en) to have everything you need to get a demo up and running, and quickly.  All of your work will be done in a browser, using drag-and-drop tools (and custom JavaScript support if you need it).

Don't expect to have a meaningfully productive experience with Construct 3 for free, however.  There's a simple demo that you can try out, but impactful game development with Construct 3 is locked behind a paywall, and a subscription at that.

## Game Maker Studio 2

[Game Maker Studio 2](https://www.yoyogames.com/gamemaker) has a user-friendly editor that supports a proprietary language called, appropriately, Game Maker Language (GML), along with visual scripting.  It also has a lot of tutorials, great community support, and an asset store (which comes with the same caveats as Unity's, above).

The general workflow of Game Maker Studio 2 and doing things like animating sprites, setting up your game world, and so on, are straightforward and intuitive. GML might not be your cup of tea if you're coming from another, more widely-used programming language, and I would _not_ recommend it as your first introduction to learning how to code.  It employs some of the basic concepts of programming, but not important details such as coding best practices or how to write clean code.

Additionally, you can try Game Maker Studio 2 with a free 30-day trial, but will need to pay to continue to use it after that time.

## Phaser 3

If you want to code _everything_ and learn a lot about the JavaScript ecosystem while doing it, check out [Phaser 3](http://phaser.io/) (or wait for Phaser 4, which is [on the way](https://madmimi.com/p/4f5f0f)).

Phaser is a lightweight and powerful JavaScript framework for making 2D games.  Whereas Phaser 2 was extremely well-documented and had excellent community support, Phaser 3 is quite the opposite.  There's good official documentation and a bunch of examples (without much context around them, it must be said), and a dreadfully small amount of tutorials.

Expect to build everything yourself, but if you're looking for ES6 or TypeScript support, or if you _really_ want to polish your skills as a JavaScript developer, you'll be able to go a long way with Phaser 3.

In the interest of fairness, I should mention a two other 2D game engines that have been recommended to me since I started writing on the topic: [LÖVE 2D](https://love2d.org/), which uses Lua, and [MonoGame](http://www.monogame.net/), which supports C#.  I haven't used either of them (or others, such as [PyGame](https://www.pygame.org/)), and can't speak to their usefulness, but they may be worth checking out.

Let me know which 2D game engine you wind up using, and why!

If you enjoyed this article, please consider [checking out my games and books](https://www.nightpathpub.com/), [subscribing to my YouTube channel](https://www.youtube.com/msfarzan?sub_confirmation=1), or [joining the _Entromancy_ Discord](https://discord.gg/RF6k3nB).

**M. S. Farzan, Ph.D.** has written and worked for high-profile video game companies and editorial websites such as Electronic Arts, Perfect World Entertainment, Modus Games, and MMORPG.com, and has served as the Community Manager for games like _Dungeons & Dragons Neverwinter_ and _Mass Effect: Andromeda_. He is the Creative Director and Lead Game Designer of _[Entromancy: A Cyberpunk Fantasy RPG](https://www.entromancy.com/rpg)_ and author of _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Find M. S. Farzan on Twitter [@sominator](http://www.twitter.com/sominator).

