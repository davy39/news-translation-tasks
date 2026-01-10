---
title: Learn to Code RPG – A Visual Novel Video Game Where you Learn Computer Science
  Concepts
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-12-22T17:23:00.000Z'
originalURL: https://freecodecamp.org/news/learn-to-code-rpg
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Splash-Art.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: Game Development
  slug: game-development
- name: GameDev
  slug: gamedev
- name: Python
  slug: python
seo_title: null
seo_desc: 'Hi, everybody – Lynn here. It''s my great pleasure to announce the launch
  of Learn to Code RPG, a project we''ve been developing in secret for the past eight
  months.

  Learn to Code RPG is an interactive visual novel game where you will teach yourself
  to...'
---

Hi, everybody – Lynn here. It's my great pleasure to announce the launch of **Learn to Code RPG,** a project we've been developing in secret for the past eight months.

**Learn to Code RPG** is an interactive visual novel game where you will teach yourself to code, make friends in the tech industry, and pursue your dream of becoming a developer. 🎯

The game features:

* Hours of gameplay 🎮
    
* Original art and music 🎨
    
* 600+ Computer Science quiz questions 📚
    
* 50+ Easter Eggs you can discover 🚀
    
* 6 different endings 👀
    
* Friendly characters and an adorable cat 🐱
    
* Minigames! 👾
    

This is a first release and we hope to add more content to it in the future. Future releases will have more **characters, scenarios, side quests, art, music,** and, yes, **minigames**. (CS quiz speed run and survival mode, anyone?) We are also planning to localize it into different languages. 🌎 The sky is the limit here. ✈️

## You can download it and play it for free on [itch.io](https://freecodecamp.itch.io/learn-to-code-rpg).

If you'd like to learn more about the game itself, my development process, and so on, read on. This is a very visual devlog (our game is a Visual Novel for a reason) and I'm sure you will enjoy it.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/img_1-1.png align="left")

*Learn to Code RPG – A game where you role play learning to code*

## Where It All Started

Let's start with a bit of background about me.

I've always loved story-rich video games since I was little. 🧒🏻

My interest in game development inspired me to major in Computer Science in college. In June 2021, I graduated from the University of Chicago with a joint Bachelor's and Master's degree in Computer Science.

In July 2021, as I was planning my move to San Francisco to start my career as a software developer, Quincy reached out to me about this game idea.

> A game where you learn to code, make friends, explore the tech culture, and eventually break into the tech industry. 🎯

Although I dabble in game development engines like Unity and Ren'Py and have created small passion projects in my own time, this would be my first time building a game from the ground up, on a (mostly) one-person team. That is to say, I was a little overwhelmed by this opportunity to make my game development dream come true. 🤯

Well, you know the saying: If you’re offered a seat on a rocket ship 🚀, don’t ask what seat!

So I said yes and dove right in.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-18-at-12.56.15.png align="left")

*Who am I to turn down an offer from CupcakeCPU? 🧁*

## From Zero to Hero: How to Build A Game In Four Months

### The Story

The story idea was pretty clear from the beginning: The hero/heroine makes the decision to learn to code, conquers obstacles along the journey, meets allies and mentors, and eventually gets to the grand prize – a shiny developer job.

I started with the classic writing framework of [The Hero's Journey](https://en.wikipedia.org/wiki/Hero%27s_journey), or, the 17-stage monomyth.

(Since I started working on this game, time and again I wish I'd taken at least one creative writing class in college. 😅)

Here's a glimpse into my outline for the first and the third stage out of the 17 stages, straight from my Google Doc:

<table><tbody><tr><td colspan="1" rowspan="1"><p>1. The Call to Adventure</p></td><td colspan="1" rowspan="1"><p>the first stage of the hero’s journey often presents to the audience the current (and sometimes rather mundane) existence of the protagonist.</p></td><td colspan="1" rowspan="1"><p><strong>Main Character (abbreviated MC) </strong>graduates and moves back with her parents. She isn’t really sure what her career is going to look like so she spends her days working gigs and browsing job openings. She has applied to some sales and consulting jobs but they turned her down.</p></td></tr></tbody></table>

<table><tbody><tr><td colspan="1" rowspan="1"><p>3. Supernatural Aid</p></td><td colspan="1" rowspan="1"><p>in this stage of the journey, the protagonist seeks out a sage-like figure and possibly gains a special item or skill in the process.</p></td><td colspan="1" rowspan="1"><p><strong>Annika, </strong>MC’s best friend in college, calls MC one day. Annika is excited because she just got an entry-level web dev role, after spending 6 months to brush up her rusty CS skills (from auditing a few CS classes in college). Annika asks about how MC is doing; is delighted that MC is also considering learning to code; and encourages MC that she can do it if she has the right study method and resources.<br>Annika introduces MC to the resource she uses.</p></td></tr></tbody></table>

### The Characters

Including the main character which the player controls, we have four major characters in the game:

* The main character, **Lydia**, a recent graduate from college. (In future releases of the game we may be able to present a few different main characters the player can choose from.)
    
* **Annika**, the main character's college best friend
    
* **Marco**, who becomes the main character's mentor
    
* **Layla**, the main character's onboarding buddy at her first dev job
    

I started designing the characters by collecting images on Pinterest. Then Quincy and I commissioned an artist online to create the character sprites and splash image.

In the images below, you can see the Pinterest character inspirations (copyright belongs to their original artists) and the final design side-by-side.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled265_20211217211947.PNG align="left")

*Lydia inspiration art + final character card*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled265_20211217212148.PNG align="left")

*Annika inspiration art + final character card*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled265_20211217211928.PNG align="left")

*Layla inspiration art + final character card*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled265_20211217211832.PNG align="left")

*Marco inspiration art + final character card*

Now that we have the main cast, what else do we need to add more character depth to **Lydia**, so that she is not sitting in her room alone all day long grinding code? Maybe she could use a cat in her room? 🐱

And enter **Mint**, Lydia's cat. (Art by me as a makeshift artist so that our artist could focus on the characters. Digital art 🎨 is my second biggest hobby after game dev.)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/mint.gif align="left")

*Mint says hi!*

### The Graphics

With the character graphics done, you may think that concludes the bulk of the graphics. But not so fast! A visual novel is, as its name suggests, visual, and so it needs a lot more graphics to tell an appealing story.

For example, in this image below, besides the character sprites, there is the background image and some GUI components like the textbox.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-18-at-12.40.00.png align="left")

*Basic graphic components: GUI, character sprites, background*

To create the background images, I applied special effect filters to stock images to add a watercolor-like texture. This way, the color scheme of our characters blends perfectly into that of the background.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Untitled266_20211217213638.PNG align="left")

*Top: stock image. Bottom: with filters*

To illustrate the passage of time in a single day, I changed the lighting of the background images by applying color manipulation programmatically. (Check out [our GitHub repo](https://github.com/freeCodeCamp/LearnToCodeRPG) if you are interested in the implementation details!)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/color.png align="left")

*Four modes of lightning*

For a motivation boost, whenever I feel like procrastinating, I switch my creative gears and doodle miscellaneous items that show up throughout the game. 🤣

And that's how we got in-game cookies, toast, pizza, fried chicken, and more!

![Image](https://www.freecodecamp.org/news/content/images/2021/12/ezgif.com-gif-maker-7-.gif align="left")

*Yummy!*

### The Code

I used the game engine that I'm most familiar with, [the Ren'Py Visual Novel Engine](https://www.renpy.org/). I reused a lot of code from my old passion projects – for example, [blinking character sprites](https://gist.github.com/RuolinZheng08/b845f416ebda5b02ebc6b62379105564) and [a rhythm minigame](https://github.com/RuolinZheng08/renpy-rhythm).

![Image](https://www.freecodecamp.org/news/content/images/2021/12/blink2.gif align="left")

*Blinking characters 😉*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-17-at-19.33.39-1.png align="left")

*Rhythm Minigame. Can you get a perfect score?*

I also incorporated some open-source Ren'Py code like [the code for kinetic text tags](https://wattson.itch.io/kinetic-text-tags) and [the code for feather icon text.](https://tacoen.itch.io/feather-icon)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/awesome.gif align="left")

*Kinetic text tag, which can be turned off for accessibility*

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-17-at-22.05.37.png align="left")

*Feather icons are awesome for creating crisp, simplistic GUI*

I will refrain from diving into the codebase here (because I won't know when to stop then 😆). Just know that it's a lot of code, both for the logic and the GUI. See the Ren'Py Lint report below.

Phew... Can we now move on to something more visual?

```pgsql
Ren'Py 7.4.8.1895 lint report, generated at: Fri Dec 17 22:11:43 2021
Statistics:
The game contains 1,335 dialogue blocks, containing 15,390 words and 85,105 characters, for an average of 11.5 words and 64 characters per block.
The game contains 40 menus, 20 images, and 49 screens.
```

### The Progress-Tracker

Even a one-person project needs a project manager, so why not be my own project manager?

I used Trello to track my process and collaborate with others. I even color-coded labels for different categories of tasks, like *coding, UI/UX, writing,* and so on as shown in the image below on the first card in the **Backlog** column.

And wow, isn't that a long scroll of tasks done? 😤

![Image](https://www.freecodecamp.org/news/content/images/2021/12/trello.gif align="left")

*My Trello board*

Everything in the **TODO** and **Doing** column is moved to **Done**, and that brings us to...

## My Takeaway

Hooray! After eight months (four months of the idea brewing, plus four months of intense coding, writing, and art making), we present to you **Learn to Code RPG. 🥳**

In four in-game months, **Lydia** has grown from *an aspiring engineer* into *an engineer with a dev job*. 🎯

In four real-world months, I've grown from **an aspiring game developer** into **a game developer who's actually built a game.** 👾

Naturally here comes the million-dollar question: What's my takeaway from this entire process?

Well, like any creative process, game development isn't easy. I'm extremely fortunate to have a team supporting me: our artist Noa who created the character art, Quincy who created the awesome original music tracks, and proofreaders and playtesters from the freeCodeCamp staff.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-17-at-22.26.07.png align="left")

*My GitHub contributions tell apart the days when I code vs. the days when I brainstorm or write or draw 🤪*

I've grown both in terms of technical skills (by finding creative ways to build things in Ren'Py), non-technical skills (by acting as my own project manager), and more (by managing expectations, overcoming imposter syndrome, and seeking a work-life balance).

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-18-at-12.33.25.png align="left")

*Do you know what imposter syndrome is? 👻 You bet I do!*

It was by no means an easy ride, but the outcome is worth every second of hard work. More importantly, I look forward to you playing the game and providing feedback so that I can make the game better in future releases.

I hope you enjoy playing **Learn to Code RPG** as much as I've enjoyed creating it! 🙌

## Learn to Code RPG Links

You can find the game on itch.io here:

%[https://freecodecamp.itch.io/learn-to-code-rpg] 

[And here's the GitHub repo with all the code](https://github.com/freeCodeCamp/LearnToCodeRPG).

You can also watch the Game Trailer on YouTube and share it with your friends:

%[https://www.youtube.com/watch?v=vLK4fOeiIEk] 

Want to see what the game is like? Check out the [Let's Play with Ania and Lynn](https://www.youtube.com/watch?v=b_IDdQzPRR4).

%[https://www.youtube.com/watch?v=b_IDdQzPRR4] 

And [here's the official press kit for the game](https://www.freecodecamp.org/news/learn-to-code-rpg-press-kit/).

If you are interested in building a Visual Novel Game yourself, check out this article of mine:

%[https://www.freecodecamp.org/news/use-python-to-create-a-visual-novel/]
