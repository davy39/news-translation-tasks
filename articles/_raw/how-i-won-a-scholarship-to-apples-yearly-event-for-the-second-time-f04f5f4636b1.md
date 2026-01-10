---
title: How I won a scholarship to Apple’s yearly event for the second time
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-02T15:55:46.000Z'
originalURL: https://freecodecamp.org/news/how-i-won-a-scholarship-to-apples-yearly-event-for-the-second-time-f04f5f4636b1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*c3bEXoh-PxEi-XHYr6yeNw.png
tags:
- name: Design
  slug: design
- name: Life lessons
  slug: life-lessons
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Renan Magagnin

  Introduction

  This article describes the process behind Mindblower, a game that was one of the
  selected submissions for the WWDC19 Scholarship. It is now available on the AppStore
  and GitHub.

  WWDC Scholarships reward students from al...'
---

By Renan Magagnin

### Introduction

This article describes the process behind _Mindblower_, a game that was one of the selected submissions for the _WWDC19 Scholarship_. It is now available on the [AppStore](https://itunes.apple.com/us/app/mindblower-the-game/id1460079689) and [GitHub](https://github.com/RenanMagagnin/mindblower-wwdc19).

[_WWDC Scholarships_](https://developer.apple.com/wwdc19/scholarships/) reward students from all over the world with the opportunity to attend Apple’s yearly event. Developers selected for a scholarship receive a WWDC ticket, lodging for the conference, and one year of membership in the _Apple Developer Program_ free of charge.

I was a student at the Apple Developer Academy and this was my second time winning the scholarship — my project from last year can be found [here](https://github.com/renanmagagnin/orbs-wwdc18). I was incredibly excited with the news and thought I would share the process behind the game that allowed me to receive this opportunity once more.

In _Mindblower_, the objective is to blow minds. To achieve this, the player shoots sticky grenades which are affected by vector fields. The core loop is to analyse each level, come up with a plan, and shoot precisely.

### The Idea

The inspiration came from the combination of being intrigued by the optimizations in [_Frost_](https://www.youtube.com/watch?v=Ry7VFcDNUMA), one of the winners of the _Apple Design Awards 2018_, and [videos about vector fields by _3Blue1Brown_](https://www.youtube.com/watch?v=rB83DpBJQsE).

The idea was to optimize the movement of a large number of entities by using vector field equations to determine their velocity.

![Image](https://cdn-media-1.freecodecamp.org/images/JOyhTe5ksoTskTMY5XJ8uhSQikslIGUqQE0j)
_An early prototype simulating a vortex vector field affecting small entities_

### Game Concept

The prototype shown above proved that this could, indeed, be the base mechanic for the game. Now, it was time to come up with the main elements that would allow for interesting gameplay:

* **Slingshot:** Allows the player to shoot balls by determining their initial velocity, given the fixed position of the slingshot.
* **Objective:** Upon contact with at least one ball, registers that the stage is complete.
* **Obstacle vector fields:** These exist in an attempt to prevent the player from achieving the goal.
* **Inverters:** Upon contact with a ball, rotate the orientation of every vector field in the stage by 180º degrees.
* **Portals:** Exist in pairs and any ball that enters through one portal, comes out the other.

![Image](https://cdn-media-1.freecodecamp.org/images/p6ZrWG2RbP4nVAPkcdTa9wMdA1S5ovLznkQM)
_An early version of the game with a functional slingshot, some different vector fields and the objective_

### Level Design

The next step was to create stages that, in an interesting way, would progressively introduce the game elements and get increasingly challenging.

To achieve this, there was a lot of experimenting with vector field equations to find the ones that would fit the game. Then, combinations of these vector fields and the other game elements gave shape to the stages in the final version of the game.

![Image](https://cdn-media-1.freecodecamp.org/images/T6n0p35kWGg3cBW21bB7hIsi8FyhNhvaGDOk)
_Mockup of the stages, which gradually introduce all game elements before combining them all in the final stage_

### Implementation

Since, at this point, the idea was well defined and the stages were already planned, it was easy to identify what systems would be required and what they would need to support. It also became clear that the key part would be to facilitate the construction of stages.

With this in mind, vector fields were engineered to support customisation of their acceleration equation, shape, strength, colour and transparency.

This allowed for different stages to be created in a rather elegant and easy way — supporting even multiple slingshots or objectives. It also avoided the repetition of code and achieved all the compositions present in the stages planned for the final game.

### Design

The graphics were created with Sketch and SpriteKit particles. The intention was to follow the neon theme of _WWDC19_ and take literally the phrase from Apple:

> _“Write code. Blow minds.”_

The core loop made up by a slingshot shooting balls at a larger ball that represented the objective was upgraded. Now, a neon bow shot sticky grenades at a mind to be blown. This was not only more visually appealing, but also more intuitive.

![Image](https://cdn-media-1.freecodecamp.org/images/zyEC7uBvpM-iccPFxMebHlobcUjZMGMfjrAf)

And, in order to make success more satisfying, it was important to focus on its core part: the explosion.

![Image](https://cdn-media-1.freecodecamp.org/images/jAbQA0hNX4mRqOtbAa1YHrBIKGOs1c9prddU)

This result was achieved using four different particles and several SKActions to programmatically create the bounce on contact and the pieces of the head flying everywhere (which were exported as 9 different assets).

As a final touch, it was also important to — with animations — make the neon lights feel real. To get this right, it took much observation of references on the internet and A LOT of fadeTo(alpha) and wait(forDuration) SKActions in the code.

![Image](https://cdn-media-1.freecodecamp.org/images/aVnc2jMDXi7MeJZWqINkVRPlDWLBsI5MbKKd)

### Audio

The audio was made from a mix between online sources and some sound effects created on Garageband. For the implementation, SpriteKit actions and the AVFoundation framework were used.

The background music used is [Paradise by Juno Dreams](https://www.youtube.com/watch?v=Iedf8baVdDM) and was found in the awesome [mixtape by NewRetroWave](https://www.youtube.com/watch?v=yV_MsBiTVsc&t) on Youtube. It just fit the theme and the game so well.

### Adapting to the PlaygroundBook Format

Since the game was made entirely with Spritekit, the transition was almost stress-free, only requiring the classic requirement of marking almost everything in the code as _public_.

The last step was to provide an instructions page in the playground book. The goal was to have it contain only the necessary instructions, while also keeping it as concise as possible, in order to keep the focus on the game.

### Conclusion

In retrospect, I believe that what contributed most to the quality of the final result were the following:

1. **Being curious:** Interesting ideas can come from anything. For me, it was when I asked myself: “How did the people from [Frost](https://www.youtube.com/watch?v=Ry7VFcDNUMA) do that? How would _I_ do that?”
2. **Coming up with a plan:** Validating the idea before even thinking about the implementation was crucial. Having a clear idea of the end goal made identifying the best approaches way easier.
3. **Creating for people:** Have the experience of the player/user be your number one priority. Revolve every decision around it.

Thank you very much for reading. If you have any questions, suggestions or comments, feel free write them in the comment section below or send them to me directly, I will be glad to answer.

