---
title: How to use AI to play Sonic the Hedgehog. It’s NEAT!
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-02T16:28:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-ai-to-play-sonic-the-hedgehog-its-neat-9d862a2aef98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RYknGhjxRw8arZlI-_ib4A.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: gaming
  slug: gaming
- name: Machine Learning
  slug: machine-learning
- name: Reinforcement Learning
  slug: reinforcement-learning
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Vedant Gupta

  Generation after generation, humans have adapted to become more fit with our surroundings.
  We started off as primates living in a world of eat or be eaten. Eventually we evolved
  into who we are today, reflecting modern society. Throug...'
---

By Vedant Gupta

Generation after generation, humans have adapted to become more fit with our surroundings. We started off as primates living in a world of eat or be eaten. Eventually we evolved into who we are today, reflecting modern society. Through the process of evolution we become smarter. We are able to work better with our environment and accomplish what we need to.

The concept of learning through evolution can also be applied to Artificial Intelligence. We can train AIs to perform certain tasks using NEAT, Neuroevolution of Augmented Topologies. Simply put, NEAT is an algorithm which takes a batch of AIs (genomes) attempting to accomplish a given task. The top performing AIs “breed” to create the next generation. This process continues until we have a generation which is capable of completing what it needs to.

![Image](https://cdn-media-1.freecodecamp.org/images/kB3DscigQ-nDtQhS5em32jfdsFdAKp236CXt)
_Clip of AI playing STH_

NEAT is amazing because it eliminates the need for pre-existing data required to train our AIs. Using the power of NEAT and OpenAI’s Gym Retro I trained an AI to play Sonic the Hedgehog for the SEGA Genesis. Let’s learn how!

### A NEAT Neural Network (Python Implementation)

#### GitHub Repository

[**Vedant-Gupta523/sonicNEAT**](https://github.com/Vedant-Gupta523/sonicNEAT)  
[_Contribute to Vedant-Gupta523/sonicNEAT development by creating an account on GitHub._github.com](https://github.com/Vedant-Gupta523/sonicNEAT)

**Note:** All of the code in this article and the repo above is a slightly modified version of Lucas Thompson's Sonic AI Bot Using Open-AI and NEAT [YouTube tutorials](https://www.freecodecamp.org/news/how-to-use-ai-to-play-sonic-the-hedgehog-its-neat-9d862a2aef98/Sonic%20AI%20Bot%20Using%20Open-AI%20and%20NEAT%20Tutorial) and [code](https://gitlab.com/lucasrthompson/Sonic-Bot-In-OpenAI-and-NEAT).

#### Understanding OpenAI Gym

If you are not already familiar with OpenAI Gym, look through the terminology below. They will be used frequently throughout the article.

**agent —** The AI player. In this case it will be Sonic.

**environment —** The complete surroundings of the agent. The game environment.

**action —** Something the agent has the option of doing (i.e. move left, move right, jump, do nothing).

**step —** Performing 1 action.

**state —** A frame of the environment. The current situation the AI is in.

**observation —** What the AI observes from the environment.

**fitness —** How well our AI is performing.

**done —** When the AI has completed its task or can’t continue any further.

#### Installing Dependencies

Below are GitHub links for OpenAI and NEAT with installation instructions.

**OpenAI**: [https://github.com/openai/retro](https://github.com/openai/retro)

**NEAT**:[https://github.com/CodeReclaimers/neat-python](https://github.com/CodeReclaimers/neat-python)

**Pip install** libraries such as cv2, numpy, pickle etc.

#### Import libraries and set environment

To start, we need to import all of the modules we will use:

```py
import retro
import numpy as np
import cv2
import neat
import pickle
```

We will also define our environment, consisting of the game and the state:

```py
env = retro.make(game = "SonicTheHedgehog-Genesis", state = "GreenHillZone.Act1")
```

In order to train an AI to play Sonic the Hedgehog, you will need the game’s ROM (game file). The simplest way to get it is by purchasing the game off of [Steam](https://store.steampowered.com/app/71113/Sonic_The_Hedgehog/) for $5. You could also find free find downloads of the ROM online, however it is illegal, so don’t do this.

In the OpenAI repository at **retro/retro/data/stable/** you will find a folder for Sonic the Hedgehog Genesis. Place the game’s ROM here and make sure it is called rom.md. This folder also contains .state files. You can choose one and set the state parameter equal to it. I chose GreenHillZone Act 1 since it is the very first level of the game.

#### Understanding data.json and scenario.json

In the Sonic the Hedgehog folder you will have these two files:

**data.json**

```json
{
  "info": {
    "act": {
      "address": 16776721,
      "type": "|u1"
    },
    "level_end_bonus": {
      "address": 16775126,
      "type": "|u1"
    },
    "lives": {
      "address": 16776722,
      "type": "|u1"
    },
    "rings": {
      "address": 16776736,
      "type": ">u2"
    },
    "score": {
      "address": 16776742,
      "type": ">u4"
    },
    "screen_x": {
      "address": 16774912,
      "type": ">u2"
    },
    "screen_x_end": {
      "address": 16774954,
      "type": ">u2"
    },
    "screen_y": {
      "address": 16774916,
      "type": ">u2"
    },
    "x": {
      "address": 16764936,
      "type": ">i2"
    },
    "y": {
      "address": 16764940,
      "type": ">u2"
    },
    "zone": {
      "address": 16776720,
      "type": "|u1"
    }
  }
}
```

**scenario.json**

```py
{
  "done": {
    "variables": {
      "lives": {
        "op": "zero"
      }
    }
  },
  "reward": {
    "variables": {
      "x": {
        "reward": 10.0
      }
    }
  }
}
```

Both these files contain important information pertaining to the game and its training.

As it sounds, the data.json file contains information/data on different game specific variables (i.e. Sonic’s x-position, number of lives he has, etc.).

The scenario.json file allows us to perform actions in sync with the values of the data variables. For example we can reward Sonic 10.0 every time his x-position increases. We could also set our done condition to true when Sonic’s lives hit 0.

#### Understanding NEAT feedforward configuration

The config-feedforward file can be found in my GitHub repository linked above. It acts like a settings menu to set up our training. To point out a few simple settings:

```py
fitness_threshold     = 10000 # How fit we want Sonic to become
pop_size              = 20 # How many Sonics per generation
num_inputs            = 1120 # Number of inputs into our model
num_outputs           = 12 # 12 buttons on Genesis controller
```

There are tons of settings you can experiment with to see how it effects your AI’s training! To learn more about NEAT and the different settings in the feedfoward configuration, I would highly recommend reading the documentation [here](https://neat-python.readthedocs.io/en/latest/)

#### Putting it all together: Creating the Training File

**Setting up configuration**

Our feedforward configuration is defined and stored in the variable config.

```py
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config-feedforward')
```

**Creating a function to evaluate each genome**

We start by creating the function, eval_genomes, which will evaluate our genomes (a genome could be compared to 1 Sonic in a population of Sonics). For each genome we reset the environment and take a random action

```py
for genome_id, genome in genomes:
        ob = env.reset()
        ac = env.action_space.sample()
```

We will also record the game environment’s length and width and color. We divide the length and width by 8.

```py
inx, iny, inc = env.observation_space.shape
inx = int(inx/8)
iny = int(iny/8)
```

We create a [recurrent neural network](https://searchenterpriseai.techtarget.com/definition/recurrent-neural-networks) (RNN) using the NEAT library and input the genome and our chosen configuration.

```py
net = neat.nn.recurrent.RecurrentNetwork.create(genome, config)
```

Finally, we define a few variables: current_max_fitness (the highest fitness in the current population), fitness_current (the current fitness of the genome), frame (the frame count), counter (to count the number of steps our agent takes), xpos (the x-position of Sonic), and done (whether or not we have reached our fitness goal).

```py
current_max_fitness = 0
fitness_current = 0
frame = 0
counter = 0
xpos = 0
done = False
```

While we have not reached our done requirement, we need to run the environment, increment our frame counter, and shape our observation to mimic that of the game (still for each genome).

```py
env.render()
frame += 1
ob = cv2.resize(ob, (inx, iny))
ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
ob = np.reshape(ob, (inx,iny))
```

We will take our observation and put it in a one-dimensional array, so that our RNN can understand it. We receive our output by feeding this array to our RNN.

```py
imgarray = []
imgarray = np.ndarray.flatten(ob)
nnOutput = net.activate(imgarray)
```

Using the output from the RNN our AI takes a step. From this step we can extract fresh information: a new observation, a reward, whether or not we have reached our done requirement, and information on variables in our data.json (info).

```py
ob, rew, done, info = env.step(nnOutput)
```

At this point we need to evaluate our genome’s fitness and whether or not it has met the done requirement.

We look at our “x” variable from data.json and check if it has surpassed the length of the level. If it has, we will increase our fitness by our fitness threshold signifying we are done.

```py
xpos = info['x']
            
if xpos >= 10000:
        fitness_current += 10000
        done = True
```

Otherwise, we will increase our current fitness by the reward we earned from performing the step. We also check if we have a new highest fitness and adjust the value of our current_max_fitness accordingly.

```py
fitness_current += rew

if fitness_current > current_max_fitness:
        current_max_fitness = fitness_current
        counter = 0
else:
        counter += 1
```

Lastly, we check if we are done or if our genome has taken 250 steps. If so, we print information on the genome which was simulated. Otherwise we keep looping until one of the two requirements has been satisfied.

```py
if done or counter == 250:
        done = True
        print(genome_id, fitness_current)
                
genome.fitness = fitness_current
```

**Defining the population, printing training stats, and more**

The absolute last thing we need to do is define our population, print out statistics from our training, save checkpoints (in case you want to pause and resume training), and pickle our winning genome.

```py
p = neat.Population(config)

p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)
p.add_reporter(neat.Checkpointer(1))

winner = p.run(eval_genomes)

with open('winner.pkl', 'wb') as output:
    pickle.dump(winner, output, 1)
```

All that’s left is the matter of running the program and watching Sonic slowly learn how to beat the level!

![Image](https://cdn-media-1.freecodecamp.org/images/caPrOTLL9OmL9C2V3BLMmUYtx1g0ckxZF1wu)

![Image](https://cdn-media-1.freecodecamp.org/images/FsO5NOjcc5S9cQiDjO56TbQLlOQIzFfdwmwc)
_Earlier generation vs Later generation_

**To see all of the code put together check out the Training.py file in my GitHub repository.**

#### Bonus: Parallel Training

If you have a multi-core CPU you can run multiple training simulations at once, exponentially increasing the rate at which you can train your AI! Although I will not go through the specifics on how to do this in this article, I highly suggest you check the **sonicTraning.py** implementation in my GitHub repository.

### Conclusion

That’s all there is to it! With a few adjustments, this framework is applicable to any game for the NES, SNES, SEGA Genesis, and more. If you have any questions or you just want to say hello, feel free to email me at vedantgupta523[at]gmail[dot]com ?

Also, be sure to check out Lucas Thompson's Sonic AI Bot Using Open-AI and NEAT [YouTube tutorials](https://www.freecodecamp.org/news/how-to-use-ai-to-play-sonic-the-hedgehog-its-neat-9d862a2aef98/Sonic%20AI%20Bot%20Using%20Open-AI%20and%20NEAT%20Tutorial) and [code](https://gitlab.com/lucasrthompson/Sonic-Bot-In-OpenAI-and-NEAT) to see what originally inspired this article.

### Key Takeaways

1. **Neuroevolution of Augmenting Topologies (NEAT)** is an algorithm used to train AI to perform certain tasks. It is modeled after genetic evolution.
2. **NEAT** eliminates the need for pre-existing data when training AI.
3. The process of implementing **OpenAI** and **NEAT** using Python to train an AI to play any game.

