---
title: 'Intro to Advanced Actor-Critic Methods: Reinforcement Learning Course'
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2021-07-30T22:20:15.000Z'
originalURL: https://freecodecamp.org/news/intro-to-advanced-actor-critic-methods-reinforcement-learning-course
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/activecritic.png
tags:
- name: Reinforcement Learning
  slug: reinforcement-learning
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Actor-Critic Methods are very useful reinforcement learning techniques.

  Actor-critic methods are most useful for applications in robotics as they allow
  software to output continuous, rather than discrete actions. This enables control
  of electric moto...'
---

Actor-Critic Methods are very useful reinforcement learning techniques.

Actor-critic methods are most useful for applications in robotics as they allow software to output continuous, rather than discrete actions. This enables control of electric motors to actuate movement in robotic systems, at the expense of increased computational complexity.

We just released a comprehensive course on Actor-Critic methods on the freeCodeCamp.org YouTube channel.

Dr. Tabor developed this course. He is a physicist and former semiconductor engineer who is now a data scientist.

The basic idea behind actor-critic methods is that there are two deep neural networks. The actor network approximates the agent’s policy: a probability distribution that tells us the probability of selecting a (continuous) action given some state of the environment. The critic network approximates the value function: the agent’s estimate of future rewards that follow the current state. These two networks interact to shift the policy towards more profitable states, where profitability is determined by interacting with the environment.

This requires no prior knowledge of how our environment works, or any input regarding rules of the game. All we have to do is let the algorithm interact with the environment and watch as it learns. 

This course also incorporate some useful innovations from deep Q learning, such as the use of experience replay buffers and target networks. This increases stability and robustness of the learned policies, so that our agent are able to learn effective policies for navigating the Open AI gym environments.

Here are the algorithms covered in this course:

* Actor Critic
* Deep Deterministic Policy Gradients (DDPG)
* Twin Delayed Deep Deterministic Policy Gradients (TD3)
* Proximal Policy Optimization (PPO)
* Soft Actor Critic (SAC)
* Asynchronous Advantage Actor Critic (A3C)

Watch the full course below or on [the freeCodeCamp.org YouTube channel](https://youtu.be/K2qjAixgLqk) (6-hour watch).

%[https://youtu.be/K2qjAixgLqk]


