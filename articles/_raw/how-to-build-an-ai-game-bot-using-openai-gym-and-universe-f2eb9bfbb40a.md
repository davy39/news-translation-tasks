---
title: 'Day 22: How to build an AI Game Bot using OpenAI Gym and Universe'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-10T15:54:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-ai-game-bot-using-openai-gym-and-universe-f2eb9bfbb40a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hyjwsHNsORWJngVh5uKx8g.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: bots
  slug: bots
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Harini Janakiraman

  Let’s face it, AI is everywhere. A face-off battle is unfolding between Elon Musk
  and Mark Zuckerberg on the future of AI. There are some that demonize it. And some
  whose utopian views claim that AI could almost be God-like in h...'
---

By Harini Janakiraman

Let’s face it, AI is everywhere. A [face-off battle](https://www.recode.net/2017/7/25/16026184/mark-zuckerberg-artificial-intelligence-elon-musk-ai-argument-twitter) is unfolding between Elon Musk and Mark Zuckerberg on the future of AI. There are some that demonize it. And some whose utopian views claim that AI could almost be God-like in helping humanity. Whichever side your views tilt, AI is here to stay.

> “With artificial intelligence, we are summoning the demon.” — Elon Musk

> “Fearing a rise of killer robots is like worrying about overpopulation on Mars.” — Andrew Ng

If you’re excited to dive right in and tinker with AI, then games are a great place to start. They have been the go-to testbed for AI. But before jumping in, here’s a little bit of history on how game programming has evolved through time.

### The History of Game Programming

Game programmers used to use heuristic if-then-else type decisions to make educated guesses. We saw this in the earliest arcade videos games such as Pong and PacMan. This trend was the norm for a very long time. But game developers can only predict so many scenarios and edge cases so your bot doesn’t run in circles!

Game developers then tried to mimic how humans would play a game, and modeled human intelligence in a game bot.

The team at DeepMind did this by generalizing and modeling intelligence to solve any Atari game thrown at it. The game bot used deep learning neural networks that would have no game-specific knowledge. They beat the game based on the pixels they saw on screen and their knowledge of the game controls. However, parts of DeepMind are still not open-sourced as Google uses it to beat competition.

### The Democratization of AI

To avoid concentrating the incredible power of AI in the hands of a few, Elon Musk founded [OpenAI](https://openai.com/). It seeks to democratize AI by making it accessible to all. Today we shall explore OpenAI Gym and the recently released Universe, which is built on top of Gym.

[OpenAI Gym](https://gym.openai.com/) provides a simple interface for interacting with and managing any arbitrary dynamic environment. [OpenAI Universe](https://universe.openai.com/) is a platform that lets you build a bot and test it out.

There are thousands of environments. They range from classic Atari games, Minecraft, and Grand Theft Auto, to [protein fold simulations](https://fold.it/portal/) that can cure cancer. You can create a bot and run it in any environment using only a few lines of Python code. This is too awesome not to try!

### Project (1 Hour)

We are going to build an AI Game Bot that uses the “Reinforcement Learning” technique. I’ll explain that later. It will autonomously play against and beat the Atari game Neon Race Car (you can select any game you want). We will build this game bot using OpenAI’s Gym and Universe libraries.

#### Step 1: Installation

Ensure you have Python installed, or install it using Homebrew. You can download a dedicated Python IDE like PyCharm or iPython notebook. I like to keep it simple and use Sublime. Finally, install Gym, Universe and other required libraries using pip.

```
// Install python using brewbrew install python3// Install the required OpenAI librariespip3 install gympip3 install numpy incrementalbrew install golang libjpeg-turbo pip install universe
```

Everything in Universe (the environments) runs as containers inside Docker. In case you don’t have it already, install and run Docker from [here](https://docs.docker.com/docker-for-mac/).

#### Step 2: Code the Game Bot

The Game Bot is coded in Python, so we start by importing the only two dependencies needed: Gym and Universe.

```
import gymimport universe
```

For this Game Bot, let’s use my favorite childhood game, Neon Race Cars, as the test environment. You can find a complete list of other environment/games you can choose from [here](https://universe.openai.com/envs).

Universe lets you run as many environments as you want in parallel. But for this project, we will use only one.

```
env = gym.make(‘flashgames.NeonRace-v0’)env.configure(remotes=1) # creates a local docker container
```

#### **Reinforcement Learning**

Now we add the game bot logic that uses the reinforcement learning technique. This technique observes the game’s previous state and reward (such as the pixels seen on the screen or the game score). It then comes up with an action to perform on the environment.

The goal is to make its next observation better (in our case — to maximize the game score). This action is chosen and performed by an agent (Game Bot) with the intention of maximizing the score. It’s then applied on the environment. The environment records the resulting state and reward based on whether the action was beneficial or not (did it win the game?).

![Image](https://cdn-media-1.freecodecamp.org/images/Ca1muYeNrBcXtwx9qzvPtzD6Quq-63T4b45I)

Now we can retrieve the list of observations for each environment initialized using the env.reset() method.

```
observation_n = env.reset()
```

The observation here is an environment-specific object. It represents what was observed, such as the raw pixel data on the screen or the game status/score.

The next step is to create a game agent using an infinite loop, which continuously performs some action based on the observation. In our bot, let’s define a single action of repeatedly pressing the up arrow (Silly bot! Feel free to evolve it to a complex one…). Action here is defined by the event type (KeyEvent), the control key (Up Arrow), and setting it to true for all observation that the agent sees.

```
while True:action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]
```

We then use the `env.step()` method to use the action to move forward one time step. This is a very basic implementation of reinforced learning.

```
 observation_n, reward_n, done_n, info = env.step(action_n)
```

The step method here returns four variables:

1. `observation_n`: Observations of the environment
2. `reward_n`: If your action was beneficial or not: +1/-1
3. `done_n`: Indicates if the game is over or not: Yes/No
4. `info`: Additional info such as performance and latency for debugging purposes

You can run this action simultaneously for all the environments in which you’re training your bot. Use the env.render() method to start the bot.

```
env.render()
```

Now you have the Game Bot ready to compete with the environment. The complete code for this basic bot as well as an advanced version is available in my Github repo [here](https://github.com/harinij/100DaysOfCode/tree/master/Day%20022%20-%20AI%20GameBot%20using%20Universe).

#### **Step 3: Run the Game Bot**

Now for the fun part: ensure Docker is running and run the bot. See it in action beating other cars or failing to do so. If it fails, keep tweaking your bot to make it beat intelligence!

```
python gamebot.py
```

![Image](https://cdn-media-1.freecodecamp.org/images/6lGP8Q22XzPi5aSnBcKidzRyP-AkplbGZHuo)

![Image](https://cdn-media-1.freecodecamp.org/images/deBMJ8LmSX5uZuZyQ2FkAZi4DJC7iKdiQCTx)
_Crash and burrrn! #Basic_

Keep tinkering with AI and eventually you can unlock God Mode! #100DaysOfCode

![Image](https://cdn-media-1.freecodecamp.org/images/EbRss6eo08UYIvzBcLMVjRrjoh0q0a78D2yh)

_If you enjoyed this, please clap **? s**o others can see it as well! Follow me on Twitter @[H**ariniLabs**](https://twitter.com/harinilabs) or M[**edium**](https://medium.com/@harinilabs) to get the latest updates on other stories or just to say Hi :)_

_PS: Sign up for my newsletter [**here**](http://harinilabs.com/womenintech.html) to be the first to get fresh new content and it’s filled with a dose of inspiration from the world of #[**WomenInTech**](http://harinilabs.com/womenintech.html) and yes men can signup too!_

