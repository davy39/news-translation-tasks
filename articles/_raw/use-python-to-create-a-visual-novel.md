---
title: How to Make a Visual Novel Game in 10 Minutes – Python Ren'Py Tutorial
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-06-22T16:18:29.000Z'
originalURL: https://freecodecamp.org/news/use-python-to-create-a-visual-novel
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-21-at-14.23.10-1.png
tags:
- name: Game Development
  slug: game-development
- name: Python
  slug: python
seo_title: null
seo_desc: 'Do you have a story idea that you''d like to turn into a novel? How about
  adding visual appeal and interactivity to that novel?

  A Visual Novel might be the game genre you are looking for. And this tutorial is
  here to help set you up in 10 minutes, wit...'
---

Do you have a story idea that you'd like to turn into a novel? How about adding visual appeal and interactivity to that novel?

A [Visual Novel](https://en.wikipedia.org/wiki/Visual_novel) might be the game genre you are looking for. And this tutorial is here to help set you up in 10 minutes, with minimal coding experience required. Let's get started!

## Tool Introduction and Setup

We will be using [the Ren'Py Visual Novel Engine](https://www.renpy.org/), which is built on top of Python 2.7. As Python itself is a scripting language, you will be able to "script" your visual novel project in Ren'Py.

> Since the arrival of Python 3, Python 2.7 has been sunsetted and is no longer actively maintained. Rest assured - Python 2.7 has all the features we need to create an awesome visual novel. Moreover, the newest release of Ren'Py, [Ren'Py SDK 7.4](https://www.renpy.org/release/7.4.0), provides a compatibility mode for Python 3. The developers also express the hope of integrating fully with Python 3 in the next release, Ren'Py 8.0.

### How to Download and Set up Ren'Py

You can download the latest version of Ren'Py for your operating system (Windows, Mac, Linux) on [its official site.](https://www.renpy.org/)

Once you have downloaded and installed Ren'Py, you may open the Ren'Py launcher, select one of the starter projects (Tutorial, The Question) on the left, and click on **Launch Project.**

Check out the **Tutorial** to get a sense of the full power of this engine, or **The Question** to see a very basic visual novel that you can make in 10 minutes.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-21-at-10.51.50.png align="left")

*The Ren'Py Launcher*

## How to Create a New Project in Ren'Py

Let's create a new project. I called mine **Forest Hike🌲**, featuring a simple scene where two kids explore a forest trail.

Pay attention to the resolution you choose: The default is 1280 x 720. When we add images, our background images should also conform to these dimensions.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/foresthike.gif align="left")

### How to Run the Boilerplate Project

Launch the boilerplate project. Press **Start** from the main menu. After two brief lines of dialogue, the script ends and we are brought back to the main menu.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/launch.gif align="left")

*Running the boilerplate project*

## How to Script Our Project

Let's start scripting our game based on the boilerplate.

Text Editors like [Sublime Text](https://www.sublimetext.com/) and [Atom](https://atom.io/) both have syntax highlighting for Ren'Py scripts ending in `.rpy`. Check out [this Sublime Text package](https://packagecontrol.io/packages/Renpy%20Language) and [this Atom package.](https://atom.io/packages/language-renpy)

The two lines of dialogue we saw are located in `script.rpy`. Open that file and its content should look like the following. Just like in Python, lines that start with `#` are comments and won't be evaluated as part of the Ren'Py script. The comments and the code below are pretty self-explanatory.

```pgsql
# Declare characters used by this game
define e = Character("Eileen")


# The game starts here
label start:

    # Show a background
    scene bg room

    # This shows a character sprite
    show eileen happy

    # These display lines of dialogue.
    e "You've created a new Ren'Py game."
    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    return
```

The `label` is used for control flow, which we will cover in the following section.

The `return` statement on the last line is what brought us back to the main menu.

### How to Declare Characters and Add Dialogues

Let's replace the boilerplate character declaration and dialogues with those from our story. Here is how my story goes:

```pgsql
define laura = Character('Laura')
define tom = Character('Tom')

label start:

    laura "Wait up, Tom!"
    laura "Tom!"
    laura "I said wait up!"
    laura "...Tom?"
    tom "Boo!"
    laura "Yikes... not again."
    tom "Are you scared?"
    laura "Not at all."
    laura "Running off like that is dangerous, you know."
    laura "We are in the forest. We could get lost."
    tom "Okay okay mom. I won't do it again."

    return
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/story.gif align="left")

### How to Add Images and Transitions

If you aren't an artist yourself, you may consider looking for assets in the creative commons domain. [itch.io](https://itch.io/), a marketplace for indie games, is a great place to look for assets.

I found [this set of character sprites](https://fuelli.itch.io/free-to-use-character-sprites) for my project. For the background images, I simply applied artistic filters to creative commons pictures, giving real-life pictures a nice watercolor aesthetic.

I put all my images inside `game/images`. Note that it's okay to use whitespaces in the image file names.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screen-Shot-2021-06-21-at-13.23.45.png align="left")

*A conventional way of organizing image assets*

Then we add to `script.rpy` those images as well as some transitions. Ren'Py applies transitions when it sees keywords like `with` and `at`. You can read more about transitions in [Ren'Py's ATL (Animation and Transition Language) docs.](https://www.renpy.org/doc/html/atl.html)

```pgsql
label start:
    scene bg forest day with fade
    show laura angry
    laura "Wait up, Tom!"
    laura "Tom!"
    laura "I said wait up!"
    laura "...Tom?"
    hide laura
    scene bg forest day with vpunch
    show tom happy at right with moveinbottom
    tom "Boo!"
    show laura angry at left with moveinleft
    laura "Yikes... not again."
    tom "Are you scared?"
    laura "Not at all."
    show laura sad
    laura "Running off like that is dangerous, you know."
    laura "We are in the forest. We could get lost."
    tom "Okay okay mom. I won't do it again."

    return
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/images.gif align="left")

With the addition of visuals, our story is coming together nicely.

### How to Add Choices

A game with different branches and endings more than doubles the fun. Adding a choice menu to a Ren'Py script is simple:

```pgsql
menu:
    "Which way should we go?"

    "Left":
        tom "Let's check out the trail on the left!"
    "Right":
        tom "Right is always the right way to go!"
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/choice.gif align="left")

### How to Use Python Variables and Control Flow

We may define Python variables in a Ren'Py script and alter the flow of our story depending on their values. Python statements start with a `$` or an indented `python:` block.

Adding variables to our previous choice menu:

```pgsql
menu:
    "Which way should we go?"

    "Left":
        tom "Let's check out the trail on the left!"
        $ is_lost = True
    "Right":
        tom "Right is always the right way to go!"
        $ is_lost = False
scene bg forest noon with Dissolve(3.0)
scene bg forest dusk with Dissolve(3.0)
show laura sad at left with moveinleft
laura "It's getting late. Are you sure we aren't lost?"
if is_lost:
    show tom sad at right with moveinleft
    tom "I hope not, but I have a bad feeling about this."
else:
    show tom happy at right with moveinleft
    tom "We are fine. Look! There's the end of the trail."
    tom "I'm the best scout around."
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/ezgif.com-gif-maker-2-.gif align="left")

See the end of this post for my handcrafted resources for working with Python in Ren'Py.

### How to Play Music

According to [Ren'Py's Audio docs](https://www.renpy.org/doc/html/audio.html), playing music and sound effects is as easy as the following:

```pgsql
play music "mozart.ogg"
play sound "woof.mp3"
```

### How to Save and Load the Game

Ren'Py has done all the heavy lifting for us and has a built-in save and load system.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/save.gif align="left")

*Saving the game*

![Image](https://www.freecodecamp.org/news/content/images/2021/06/load.gif align="left")

*Loading the game*

### Other Customization You Can Do

Currently in our dialogue, the entire line of text is displayed at once, instead of character by character. We may change the variable `preference.text_cps` (CPS stands for character per second) in `options.rpy` like this.

```pgsql
default preferences.text_cps = 20
```

![Image](https://www.freecodecamp.org/news/content/images/2021/06/cps.gif align="left")

*Setting a custom CPS displays the text one character at a time at a given rate*

There is even more that we can customize in `gui.rpy` (GUI stands for Graphic User Interface, which includes the textbox and menu choice items that we have seen) or `screens.rpy`.

## What Else is Ren'Py Capable of?

Ren'Py's capability extends way beyond displaying text and images. I may go as far as to say that Ren'Py is about as capable and versatile as Python itself.

With the [Pygame](https://www.pygame.org/news) module, it is possible to create complex mini games in Ren'Py. I myself have created and open-sourced a few mini games, including a chess engine that integrates with the Stockfish chess AI as well as a rhythm game engine that automatically generates the beat map for any music file.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/promotion.gif align="left")

*My chess game demo*

![Image](https://www.freecodecamp.org/news/content/images/2021/06/demo-4.gif align="left")

*My rhythm game demo*

%[https://r3dhummingbird.itch.io/renpy-chess-game] 

%[https://r3dhummingbird.itch.io/renpy-rhythm-game] 

## Resources

This tutorial should help get you started with Ren'Py. It's always useful to refer to [the official documentation](https://www.renpy.org/doc/html/) as you learn the more advanced features to add buzz to your project.

I've also created some course material to help you brush up on Python fundamentals and their capabilities in Ren'Py scripts.

%[https://github.com/RuolinZheng08/python-for-renpy-dev] 

%[https://www.udemy.com/course/python-basics-for-renpy-developers/?referralCode=774C55606994052EBFCB] 

Check out my course intro video on YouTube:

%[https://www.youtube.com/watch?v=pQcb_pfIbI0] 

Thanks for reading and have fun telling your story!
