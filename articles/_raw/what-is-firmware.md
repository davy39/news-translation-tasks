---
title: What is Firmware? Definition and Examples
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2022-04-21T18:40:08.000Z'
originalURL: https://freecodecamp.org/news/what-is-firmware
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/postimage.png
tags:
- name: firmware
  slug: firmware
- name: hardware
  slug: hardware
- name: software
  slug: software
seo_title: null
seo_desc: 'Did you know that firmware is literally everywhere? It might be strange
  to think about – but it''s just as common as hardware and software.

  In fact, it is thanks to firmware that:


  Printers work

  Defibrillators work

  Car radios works

  and more …


  Based o...'
---

Did you know that firmware is literally everywhere? It might be strange to think about – but it's just as common as hardware and software.

In fact, it is thanks to firmware that:

* Printers work
* Defibrillators work
* Car radios works
* and more …

Based on the examples above, you probably already have some idea of what firmware is. But you don't have a clear definition of it.

In order to truly understand what firmware is, we must first understand software, then hardware, and finally we can jump into firmware.

In this tutorial, I'll explain each topic with an analogy. By doing so, everyone can understand.

It doesn't matter if you're just getting into technology!

With that, I would like to make sure that everyone understands what software, hardware, and firmware is. I will not elaborate on the technical terms.

### In this article we will explore:

* What exactly is software?
* What exactly is hardware?
* What exactly is firmware?

## What is Software?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/book.jpeg)
_Photo by [**Pexels**](https://www.pexels.com/@kubra-dogu-80605500?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener">**Kübra Doğu**</a> from <a href="https://www.pexels.com/photo/food-wood-dawn-coffee-9222655/?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener)_

Imagine, if you will, that you have no idea what to make for dinner today.

Luckily, you find an old cookbook you have and decide to cook one of the recipes in it.

The cookbook has many recipes. Each of these recipes has its own instructions.

In the **cookbook**, a **recipe** can be seen as a **set of steps** (or instructions) that together make a **meal**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/cooking-instruction.jpg)
_Photo by [Luis Quintero on Pexels](https://www.pexels.com/photo/open-bible-2294878/)_

You can also create your own meals based on your experience in cooking many different recipes, right?

Software is no different.

**Software programs** can be seen as a **set of instructions** that work together to form a **program**.

```assembly
 global  _main
    extern  _printf

    section .text
_main:
    push    message
    call    _printf
    add     esp, 4
    ret
message:
    db  'Hello, World', 10, 0
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/HelloWorld.asm.png)

Then, applications are a big sets of instructions that perform specific tasks.

Operating systems are big sets of instructions that coordinate software and hardware resources.

* Cookbook = software
* Dinner cookbook = type of software (application or operating system)
* Recipe = program

You need a recipe to make dinner. You must follow each step in the cookbook to create a recipe.

Once you have completed all the steps, your dinner is ready.

You need software to accomplish a particular task. A computer has to follow all instructions for the software to function. 

Therefore, the software is running either while the instructions are being followed or after they have been completed.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/recipie---cooking-instructions.png)

## What is Hardware?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/food.jpeg)
_Photo by [**Pexels**](https://www.pexels.com/@elevate?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener">**ELEVATE**</a> from <a href="https://www.pexels.com/photo/chef-preparing-vegetable-dish-on-tree-slab-1267320/?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener)_

In order to make dinner, you need a series of steps from the cookbook that tell you how to make a particular meal.

You also need various tools to cook with - like pots and pans, knives, and the food itself. This is like hardware.

So a cookbook gives you instructions that allow you to cook.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/cooking-process-1.png)

For hardware to work, it needs software (a set of instructions) to tell it what to do.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/CPU-process-2.png)

Software then, gives instructions to hardware that lets it work.

* Meal prep tools = hardware
* Recipe = software

Without software, you can't make hardware work.

Without a recipe, you won't know what to do with your various tools and ingredients to make a meal.

Like hardware without software, you can also eat a meal with just uncooked food. Gross.

In the same way that there are various types of meals, there are also various types of computer hardware.

For example:

* CPU
* RAM
* GPU
* and so much more…

![Image](https://www.freecodecamp.org/news/content/images/2022/04/comparason-of-processes.png)
_Comparison of processes_

## What is Firmware?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/dessert.jpeg)
_Photo by [**Pexels**](https://www.pexels.com/@ella-olsson-572949?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener">**Ella Olsson**</a> from <a href="https://www.pexels.com/photo/close-up-photo-of-chocolate-mousse-3026810/?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener)_

A program is a set of instructions read by a computer.

Let's say you just want to make a snack or dessert. You probably don't need as many ingredients as when making a dinner for your family, right?

Let's say you want software that runs on a microwave. You don't need all the hardware the computer has to make the microwave work, right? You just need that specific to making the microwave work.

Or say you want software running on a printer. You don't need all the hardware the computer has to make the printer work right? Just the software for the printer.

* Microwave software = firmware
* Printers software = firmware

So this means that firmware is nothing more than software, but in a hardware device. Not in a computer.

Firmware lets very specific hardware complete very specific tasks.

## Wrapping up

Thanks for reading! Now you know more about:

* Software
* Hardware
* Firmware

Microprocessor photo by **[Pok Rie](https://www.pexels.com/@pok-rie-33563?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)** from **[Pexels](https://www.pexels.com/photo/dell-motherboard-and-central-processing-unit-1432675/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)** 

