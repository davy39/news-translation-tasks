---
title: An introduction to visual automata-based programming in Rosmaro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T13:53:42.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-visual-automata-based-programming-in-rosmaro-100dae8eb969
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wYiiltn59DLXuTckakv8rg.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Łukasz Makuch

  To do automata-based programming is to program with states and transitions. States
  correspond to different behaviors. Transitions are named after events and describe
  how those behaviors change.

  The easiest way to think about this is ...'
---

By Łukasz Makuch

To do automata-based programming is to program with states and transitions. States correspond to different behaviors. Transitions are named after events and describe how those behaviors change.

The easiest way to think about this is a directed graph. Here’s an example of a cursed prince:

![Image](https://cdn-media-1.freecodecamp.org/images/1*cxViPSuy4F9OJtQXcRAd0Q.png)
_A very simlpe, directed graph_

It may be either a _Prince_ or a _Frog_. The _Prince_ eating a pizza is an event which causes a transition from the _Prince_ state to the _Frog_ state.

I’m going to show you how to do (visual) automata-based programming in Rosmaro.

[Rosmaro](https://rosmaro.js.org) is a JavaScript library which allows you to build stateful objects.

An object is stateful when two identical method calls may produce different results.

Here’s an example:

```
> model.introduceYourself(); 'I am The Prince of Rosmaro!'
```

```
> model.eat({dish: 'yakisoba'}); undefined
```

```
> model.introduceYourself();'I am The Prince of Rosmaro!'
```

```
> model.eat({dish: 'pizza'});undefined
```

```
> model.introduceYourself();'Ribbit! Ribbit!'
```

Another great example of stateful objects is a Graphical User Interface. Think of an ATM. You can look twice at its screen and see different messages and fields. Your eyes are the same. The way you look at the screen hasn’t changed. It’s the state of the ATM that changed. Maybe you selected some option by clicking a button, or maybe some timer kicked in. Something caused a transition from one state to another.

Below are few examples of front-end applications built using visual automata-based programming.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wSe8QRkF9KCFWrK4l4gn6g.gif)
_The codebase of [this To-Do application](https://github.com/lukaszmakuch/bool-less-todo" rel="noopener" target="_blank" title=") consists of no boolean values._

![Image](https://cdn-media-1.freecodecamp.org/images/1*73H1rmEcexjfg3o-BB2SRA.gif)
_[This wizard](https://github.com/lukaszmakuch/Rosmaro-React-example-Bunny-App" rel="noopener" target="_blank" title=") has two paths. There’s no IF for that._

The Rosmaro way of building stateful objects is to **combine a drawn graph with some written code**.

The graph shows all the possible behaviors and what makes them change. The fact that it’s drawn using a visual editor makes it a visual programming tool.

Each behavior is expressed as a bunch of pure functions. A function may return some result as well as a request to follow an arrow.

Rosmaro stores the whole state of a model in a pluggable storage mechanism. It may be everything from a plain-old JavaScript object to a NoSQL database. It also uses pessimistic locking to prevent going into an inconsistent state.

The example I want to show you concerns a prince who turns into a frog when he eats a pizza.

First, open the [Rosmaro editor](https://rosmaro.js.org/editor/). Then, click the _LOAD_ button to start a new project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UKxKP4zIYv0UaMXt0C2S4Q.png)

Add the main graph.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ahW-cir31VYEJ9cejGyUsg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*C2aMW6A9Z7rxwLll0nE8Hw.png)

Click _NEW NODE_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kMlmPurzTdi02OryTx1rGg.png)

Add a local node called _Prince_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wcyKGVD0HjXTHp2gJ6e7xQ.png)

Then, add a local node called _Frog_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*riJxknEZaHyt2bblanzuoQ.png)

Put your mouse cursor over the _start_ entry point and draw an arrow to the _Prince_ node. Then, draw an arrow from the _Prince_ to the _Frog_ and call it _ate pizza_. Finally, click _ADD NODE_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ny2w0wNxp8I4wQ3uKMLpkw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GuMz85fYAj4N6KZtinbYSA.png)

Add a leaf called _Prince_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NfV-0-geNWNNok4n6GyRRw.png)

Then, add a leaf called _Frog_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GaWnKZe4G6ezzQGCHzsVjQ.png)

To complete the main graph, associate local nodes with the recently added leaves.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6nIgD-hbb8wS8hbF6S8OJA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CR5ZvCLP8GsC4VLgN8sylA.png)

The graph is ready. Click the button called _GENERATE CODE_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*atgBQ9GnIjRBfNyc6CM_5w.png)

It’s time to write some JavaScript. First, you need to get all the dependencies.

```
npm i rosmaro rosmaro-in-memory-storage rosmaro-process-wide-lock --save
```

Then, you need to import and call them.

The generated graph may be either imported as a JSON file, or pasted directly into the code. To keep this example as simple as possible, I suggest pasting it into the code.

A frog is certainly a simpler creature than a prince. Implementing its behavior is easy. Every time we ask the frog to introduce itself, it says “Ribbit! Ribbit!”

The prince not only introduces himself, but also pays attention to the things he eats. He may eat a yakisoba and everything is fine. But as soon as he eats a pizza, he follows the arrow called _ate pizza_.

It’s time to put the handlers all together.

The model is ready. Here’s the complete code:

Identical calls to the _introduceYourself_ method return different values. The returned value depends on events which occurred in the past. It proves that the _model_ object is stateful.

The [code of The Cursed Prince](https://github.com/lukaszmakuch/cursed-prince) is on GitHub. It makes use of only basic Rosmaro features. When working on real apps, you’ll want to use more advanced techniques. Some of them include subgraphs, dynamic orthogonal regions, and the context object.

You can learn more about Rosmaro from its [official documentation](https://rosmaro.js.org/doc/).

