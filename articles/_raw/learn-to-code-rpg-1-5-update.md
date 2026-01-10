---
title: Learn to Code RPG Version 1.5 is Now Playable with Hours of New Gameplay
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2022-12-23T02:43:43.000Z'
originalURL: https://freecodecamp.org/news/learn-to-code-rpg-1-5-update
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/splash-2-lowres-1.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: Game Development
  slug: game-development
- name: GameDev
  slug: gamedev
- name: learning to code
  slug: learning-to-code
- name: Python
  slug: python
seo_title: null
seo_desc: 'Hello from the Learn to Code RPG dev team! We are Lynn, KayLa, and Nielda.
  And we''ve been hard at work building out new adventures for our characters.

  I''m excited to announce the launch of Learn to Code RPG v1.5, a year after the
  launch of Learn to C...'
---

Hello from the Learn to Code RPG dev team! We are Lynn, KayLa, and Nielda. And we've been hard at work building out new adventures for our characters.

I'm excited to announce the launch of **Learn to Code RPG v1.5**, a year after the launch of Learn to Code RPG v1. (Fun fact: we're calling it v1.5 instead of v2 because we have grand plans for v2, which we plan to release in early 2023.)

## What is Learn to Code RPG?

**Learn to Code RPG** is an interactive visual novel game where you will teach yourself to code, make friends in the tech industry, and pursue your dream of working as a developer. 🎯

The game features:

* Hours of gameplay 🎮
    
* Original art and music 🎨
    
* 1,000+ Computer Science quiz questions 📚
    
* 50+ achievements you can unlock 🏆
    
* 6 different endings 👀
    
* 10+ characters you can make friends with, and an adorable cat 🐱
    
* Minigames 👾
    
* A renown system, a money system, and fun items you can buy for your cat and to customize your room 🏠
    

## Learn to Code RPG v1.5 Game Trailer

You can also watch the game trailer below and share the YouTube video with your friends:

%[https://www.youtube.com/watch?v=vDfcMD99Kdg] 

## You can download the game and play it for free. It's available for PC, Mac, and Linux on [itch.io](https://freecodecamp.itch.io/learn-to-code-rpg). And on Android from the [Google Play Store](https://play.google.com/store/apps/details?id=org.freecodecamp.learntocoderpg&hl=en_US&gl=US&pli=1).

If you'd like to learn more about the game itself and the development process, read on.

We'll walk you through the story, characters, graphics, and code. I'm sure you'll enjoy it. And it may even inspire you to code your own video game.

## How LearnToCodeRPG Went From v1 to v1.5

### The Team

When Lynn created v1, she was working solo on the game, juggling writing, coding, and some asset creation.

With this release, to give Lynn more time to focus on coding, KayLa took care of the writing. Nielda helped brainstorm features and create art assets.

Want to see a teamwork showcase? Here's one for the item shop. After purchasing furniture from the shop, the player will see the furniture in their room.

* Lynn programmed the shop, the items, and the room customization
    
* KayLa and Nielda came up with ideas for the items
    
* KayLa wrote fun flavor text for the items
    
* Nielda created all the assets – the room and the items – by tracing over 3D assets and applying textures over them
    

![Image](https://www.freecodecamp.org/news/content/images/2022/12/room.gif align="left")

### The Learn to Code RPG Main Story

In v1 (or what we call the Prologue), the story started as our protagonist, Lydia, decided to get a job in the tech industry. She needed to learn to code, make friends in the industry, find mentors, tackle technical interviews, and eventually arrive at her goal – a shiny new developer job.

Building from the Prologue story, in v1.5 (or what we call Arc I) Lydia starts working as a full-stack developer. She now needs to interact with her new colleagues on a day-to-day basis and react to events that arise.

She will be faced with all the things a real-world software engineer faces – changes in project requirements, communicating with project managers, learning from senior developers, and so on.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-20-at-18.37.09.png align="left")

*Does this look like a familiar scene from working in tech to you?*

Outside of work, Lydia can also go hang out at Hacker Space with friends she made back when she was first learning to code.

At Hacker Space, Lydia might run into old acquaintances who are also looking for a job. She can decide whether or not to give them a referral.

She can also give back to the community by mentoring high school students with their projects.

There is never a shortage of fun things to do at Hacker Space. 😄

![Image](https://www.freecodecamp.org/news/content/images/2022/12/itch2.png align="left")

### The Characters

To give the characters more depth, we brainstormed using the character card format shown below. Here's the character card for Lydia:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screen-Shot-2022-12-20-at-19.46.02.png align="left")

Lydia meets many new colleagues in this arc and our character list has been greatly expanded.

When designing the characters, sometimes our artist Noa will experiment with hair color and style variations until we land on a design that we are happy with:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/mala-3.jpg align="left")

*Mala's different designs. Which is your favorite?*

Here's also a sneak peek into one of the many characters and their many expressions:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/darius-4.jpg align="left")

*Darius's many faces*

Of course, everyone's favorite, Mint the kitty, is still the key emotional support for this story arc. 🐱

![Image](https://www.freecodecamp.org/news/content/images/2022/12/mint_small.gif align="left")

### The Graphics

Now moving on to other graphics besides character sprite art. Just like in v1, we again created background images by applying a watercolor-like filter to real-world images.

Since a lot of story takes place at the company Lydia is working at, we also tried to find stock images that are coherent in color scheme, like the ones below:

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Untitled-design.png align="left")

*Background images for the company Lydia's working at*

### The Code

Just like in v1, I used the game engine that I'm most familiar with, [the Ren'Py Visual Novel Engine](https://www.renpy.org/).

During this year of development, a really exciting piece of news for the Ren'Py community is that Ren'Py 8 now supports Python 3. This is exciting to me.

Compared to Python 2.7 (which we used in Ren'Py 7.4 when we developed Learn to Code RPG v1), Python 3 brings in a lot of new features that positively impact our development.

This also means that I had to spend a little time to migrate from Python 2.7 to Python 3 in our project. (It was a small Git commit, trust me 🤓).

Now some exciting stats – Ren'Py's built-in linter is perfect for gathering stats for comparisons between v1 and v1.5:

```pgsql
# v1
Ren'Py 7.4.8.1895 lint report, generated at: Fri Dec 17 22:11:43 2021
Statistics:
The game contains 1,335 dialogue blocks, containing 15,390 words and 85,105 characters, for an average of 11.5 words and 64 characters per block.
The game contains 40 menus, 20 images, and 49 screens.

# v1.5
Ren'Py 8.0.3.22090809 lint report, generated at: Tue Dec 20 19:22:05 2022
Statistics:
The game contains 3,339 dialogue blocks, containing 41,214 words and 220,501
characters, for an average of 12.3 words and 66 characters per block.
The game contains 68 menus, 19 images, and 51 screens.
```

From the stats we can see that we've nearly tripled the story content. Woohoo! 🤩

## Next Steps for LearnToCodeRPG: From v1.5 to v2

Hooray! After a whole year of development, we've taken v1 to new heights and are now presenting you with **Learn to Code RPG v1.5**.

What's more exciting: we are only just getting started. Just as Quincy always likes to say, the sky is the limit. ✈️

Here are some things you can look forward to in v2, or even sooner, between v1.5 and v2:

* 🌎 Localization: All the text in v1 has been fully translated into Portuguese, and we have an active community working on translating the game into other world languages. You can help too, by starting [here](https://contribute.freecodecamp.org/#/how-to-translate-files?id=translate-the-learntocode-rpg).
    
* 🎭 More story and characters (shhh... we have 10+ characters planned and some drawn already)
    
* 📚 Expanded bank of quiz questions and spaced repetition to help you learn more efficiently.
    
* 💻 Auto-update from inside the game so that you can stay up-to-date with the latest bug fixes, features, and storylines.
    
* ... and more on our holiday wishlists! 🎁
    

Last but not least, we hope you enjoy playing this game as much as we enjoyed developing it! 🥳

### Links

You can find the game on itch.io here:

%[https://freecodecamp.itch.io/learn-to-code-rpg] 

And here's the GitHub repo with all the code:

%[https://github.com/freeCodeCamp/LearnToCodeRPG] 

If you haven't read about how v1 of the game took shape, here's an article for you:

%[https://www.freecodecamp.org/news/learn-to-code-rpg/] 

And here's the official press kit for the game:

%[https://www.freecodecamp.org/news/learn-to-code-rpg-press-kit/] 

If you are interested in building a Visual Novel Game yourself, check out this article of mine:

%[https://www.freecodecamp.org/news/use-python-to-create-a-visual-novel/] 

We hope you enjoy learning what it's like to work in tech by playing the Learn to Code RPG. 🧑‍💻
