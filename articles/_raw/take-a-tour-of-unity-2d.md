---
title: Learn Unity 2D and Platformer Basics with this Overview
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-17T21:33:36.000Z'
originalURL: https://freecodecamp.org/news/take-a-tour-of-unity-2d
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9f41740569d1a4ca419d.jpg
tags:
- name: C
  slug: c
- name: Game Development
  slug: game-development
- name: learn to code
  slug: learn-to-code
- name: unity
  slug: unity
seo_title: null
seo_desc: 'By M. S. Farzan

  If you''re shopping around for a 2D game engine, you''ve undoubtedly come across
  Unity. Dipping your toe into Unity''s editor can be overwhelming if you haven''t
  had a good overview of where all of the tools live, particularly if it''s als...'
---

By M. S. Farzan

If you're shopping around for a 2D game engine, you've undoubtedly come across [Unity](https://unity.com/). Dipping your toe into Unity's editor can be overwhelming if you haven't had a good overview of where all of the tools live, particularly if it's also your first time using C# to write scripts.

In this article, I'll give you a tour of Unity's 2D features with an overview of what tools you'll need to create a platformer - or any kind of 2D game - and where to find them in the editor!

If you're considering Unity among other 2D game engines, take a look at [this article](https://www.freecodecamp.org/news/what-2d-game-engine-to-use-for-your-next-game/) for some options.

And if you'd prefer a visual tour of Unity, check out this video instead (28 minute watch):

%[https://youtu.be/w2hxVVnbEFA]

In this overview, we'll be using the [Warped City Unity Assets Pack](https://assetstore.unity.com/packages/2d/environments/warped-city-assets-pack-138128) by [Ansimuz](https://assetstore.unity.com/publishers/18720).

## Overview

On first glance, Unity's editor will look familiar if you've used another "all-in-one" game engine, but if it's your initial entrée into game development, it might be overwhelming.  Moreover, if you don't already have some experience working in C#, I _highly recommend_ doing some tutorials using [Microsoft's .NET](https://dotnet.microsoft.com/learn) or similar.  Unity has a relatively steep learning curve, and if you can come to it with some basic proficiency with C#, you'll have an easier onboarding experience.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Unity-1.png)

A lot of your time will be spent in the hierarchy (1), which allows you to keep track of all of your game objects in a given "scene," which is a specific portion of your game (like your "Start" menu or a particular game world in your platformer).  With it, you can nest objects under others, manage your cameras and canvasses, and navigate through all of the game objects you've created.

You'll want to keep organized in your project tab (2), which acts as a file system that you can structure as you see fit.  One best practice, for example, is to collect all of your assets in one folder, animations in another, scripts in yet another, and so forth.  You can also click over to the console tab if you've instructed Unity to log stuff under circumstances that you dictate.

When clicking on a game object, either in the hierarchy or project tab, you'll be greeted with more details in the inspector (3).  These details will depend on what kind of object you've clicked, and what you've _attached_ to that game object.  If you've created an empty game object, for example, there won't be much there.  But if you've made a player character that has a a sprite attached, along with an animation controller, rigidbody2d to manage physics, collider2d to manage collisions, and a script to manage user input and interactivity, all of these will appear in the inspector for you to tinker with.

The rest of the real estate within the editor is taken up by the scene itself (4), which is where you'll build your game world, drop in objects and triggers, and go about your game designing.  You can click over to the game tab to see what your game actually looks like when played (and play it by hitting the "play" button), or check out the Asset Store from the safety of your Unity client.

## Where to Find Things Like the Animator

If you've read [any of my writing about game engines](https://www.freecodecamp.org/news/what-2d-game-engine-to-use-for-your-next-game/), you've heard me whinge about Unity's 2D support being shoehorned into a 3D environment, and about how difficult it can be to locate the tools you need to get your work done.

Let's just say that some things are difficult to accomplish in Unity compared to other 2D game engines, but they're all still possible.  If you're attempting to access the animator, for example, you'll need to select the Window > Animation > Animator, which is _different_ from the location of the animations that you'll painstakingly create and save in your project tab.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Unity-2.png)

Similarly, if you want to access Physics 2D settings, by all means, click on Edit > Project Settings, which are _different_ from your personal preferences, located under Edit > Preferences.  And if you're looking to tinker with builds, you'll want to go to File > Build Settings.

Similarly, if you just want to create a plain ol' game object, head to GameObject > Create Empty (or 2D Object if you know what you're looking for).  If, conversely, you're trying to add a rigidbody to an existing game object, you'll need to go to Component > Physics 2D > Rigidbody 2D (or click "Add Component" in the inspector when you have the game object selected in the hierarchy).

I think it's clear by this point that finding the things that you'll need to get your work done can be complicated, nested as they are within different menus.  It doesn't help that some of the tools themselves, such as the animator, are clunky compared to their counterparts in other 2D game engines, but once you get a handle on how they work, you'll find them to be perfectly serviceable.

## Visual Studio and C# Scripting

Unity supports C# for writing scripts, and you can pair it with Visual Studio for a relatively painless integrated development environment.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Unity-3.png)

Scripts are easily accessible through the editor, and you'll have to attach them to your game objects to make your game do pretty much anything.  One fun feature is to declare a public variable in a script - say, an integer called "jumpSpeed" - and then attach that script to a game object in the inspector.  You'll see that variable exposed in the Unity editor, and can change it on the fly while your game is running to see how your changes work in action.

## Prefabs

Finally, Unity leverages the use of what they call "prefabs" to streamline your workflow.  In essence, a prefab is a type of reusable object that you've created so that you can drop it in your game world again and again without the need for repeat customization.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Unity-4.png)

Let's say that you create a monster in your top-down 2D adventure game as an empty game object, then attach a sprite, rigidbody2d, collider2d, animations, and a controller script.  You can drag that monster into your project tab to make it a prefab, which allows you to use it again and again in your game world without having to go through the whole process every time.

Unity has several more features that support 2D game development, some of which I cover in the video above, and it would do to watch a few tutorials on specific aspects of the editor if you're considering using it for your next game.  I'd particularly recommend brushing up on C# before tackling the editor itself, as doing so will provide for a more gentle learning curve.

Hope this overview is helpful for your next game!

If you enjoyed this article, please consider [checking out my games and books](https://www.nightpathpub.com/), [subscribing to my YouTube channel](https://www.youtube.com/msfarzan?sub_confirmation=1), or [joining the _Entromancy_ Discord](https://discord.gg/RF6k3nB).

**M. S. Farzan, Ph.D.** has written and worked for high-profile video game companies and editorial websites such as Electronic Arts, Perfect World Entertainment, Modus Games, and MMORPG.com, and has served as the Community Manager for games like _Dungeons & Dragons Neverwinter_ and _Mass Effect: Andromeda_. He is the Creative Director and Lead Game Designer of _[Entromancy: A Cyberpunk Fantasy RPG](https://www.entromancy.com/rpg)_ and author of _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Find M. S. Farzan on Twitter [@sominator](http://www.twitter.com/sominator).

