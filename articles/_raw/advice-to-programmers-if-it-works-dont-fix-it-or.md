---
title: If the code works, don't fix it... Or maybe do? When to refactor your code
  and when to leave it alone.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-30T18:51:06.000Z'
originalURL: https://freecodecamp.org/news/advice-to-programmers-if-it-works-dont-fix-it-or
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/1_ShTnBApvIxNlKjTItTAAiw.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: software development
  slug: software-development
- name: web
  slug: web
seo_title: null
seo_desc: 'By Huseyin Polat Yuruk

  Imagine software that you work on. It was written by programmers before you joined
  the team and the software works properly. There are some bugs that need to be fixed
  but it does what it’s supposed to do. Nothing else. This is ...'
---

By Huseyin Polat Yuruk

Imagine software that you work on. It was written by programmers before you joined the team and the software works properly. There are some bugs that need to be fixed but it does what it’s supposed to do. Nothing else. This is what others see from outside of the code–software that solves customers’ problems and works as expected.

But what about the code? What about the programmers? What do they think about their software?

As one of the programmers that built this software, you see totally different things from inside the code. 

First things first, you think the code base is so big. You know certainly that this software could have been written with much less code while still providing the same functionality. The code base seems so complex to you. You know that the code could have been written in a better, simpler, and more well-structured way. 

Adding new features or implementing something new is hard and painful because you have to consider the other parts that are connected to each other. The modules are not loosely coupled, so making changes takes too much time. And what about debugging? Finding bugs and fixing them takes too much time as well.

Besides the bad design and ugly code, the software works properly and the customers are happy. Now you are at the crossroads. There are two possible ways for you: one way tells you that you should follow the old engineering adage, “If it works, don’t fix it.” The other one that tells you that you should do some refactoring to make your job easier while working on your code base so that you have more readable and understandable code. 

Which way would you prefer? Would you follow the old engineering adage “If it works, don’t fix it?”

## Two different programmer mindsets

The answer to that question can be simple. But before explaining the appropriate answer, I want to introduce you to two different programmer’s mindsets when it comes to fixing bad code that works properly.

The first mindset believes in the old engineering adage: “**If it works, don’t fix it.**” To them, their code style doesn’t matter. They are result-driven programmers. It can be complex, badly structured code, completely opposite of important programming principles, but they don’t care about how well the code is written. They just care about what it does. 

So to these programmers, fixing badly written code is a waste of time. It just works. Why should they touch it?! And besides, there is a big risk of introducing new bugs while fixing the bad code. So what will they do? They will not touch the code and continue following the old engineering adage.

On the other hand, the other programmers who see the code as artwork will be uncomfortable with that kind of situation. They will feel disgusted while reading badly written code. They will try to fix each piece of code in the project because they care about code style a lot, and every piece of code in their project should be treated as art. 

They are too obsessive about their code style. Even if other programmers write well-structured code, they will try to change that code to make it suitable to their own style. So basically they don’t follow the old “if it works, don’t fix it” adage. They will fix everything according to their own mindset. In the end, it doesn’t matter to them if it works or not.

## What would be the best solution that works for you?

Find the parts of code that you work on actively and fix these parts to make them more understandable and readable. Don’t touch other parts if they work as expected and they are bug-free. 

Why is this core so important? The core parts of your software are the parts you will work on the most. You will read these parts more often and will make changes in them more often than the rest. If there is a need for adding additional functionalities or implementing new features, they will be connected directly to the core. 

Most of the bugs will be introduced from this core, which means you will spend most of your time debugging these parts. Remember the [80/20 rule (Pareto Principle)](https://en.wikipedia.org/wiki/Pareto_principle), **“20 percent of the code has 80 percent of the errors. Find them, fix them!”**

What about the other parts?

Those parts are the ones that you will rarely work on. They are bug-free. They were written maybe even months or years ago and they work as expected. They might be written in an ugly way, even though they could have been written in a simpler, more readable and understandable way. This doesn’t mean that you have to fix them too. God knows when you will have to read them or change them again. So these parts can stay as they are. Forget about them. No need to fix them. You can spend your time working on more important stuff.

## Why is fixing core parts so important even if they work as expected?

If you want to serve your customers for many years, you should have a maintainable product. A maintainable product means that making changes is not a struggle. Debugging and fixing bugs shouldn’t take too much time and adding new features should also be easy. So as a result, your programmers are happy and your customers are happy, too.

As [Martin Fowler](https://martinfowler.com/) said in his [Refactoring book](https://www.amazon.com/Refactoring-Improving-Existing-Addison-Wesley-Signature/dp/0134757599/ref=pd_sbs_14_img_0/147-2543130-6817650?_encoding=UTF8&pd_rd_i=0134757599&pd_rd_r=3126d0ac-cc44-40ab-874c-dd6a2817a30a&pd_rd_w=NxgDY&pd_rd_wg=nvdiq&pf_rd_p=5cfcfe89-300f-47d2-b1ad-a4e27203a02a&pf_rd_r=AB27YQ6VJP9RM58D8HBD&psc=1&refRID=AB27YQ6VJP9RM58D8HBD):

> “When you think about programmers, most of us will think that they spend most of their time writing code. Actually, this is quite a small fraction. Programmers spend most of their time reading the code and debugging it. Every programmer can tell a story of a bug that took a whole day (or more) to find. Fixing the bug is usually pretty quick, but finding it is a nightmare.”

The more well-written code you have, the easier it is to understand the code. The more understandable your code is, the easier your job is.

That is the reason why not following the old engineering adage (if it works, don’t fix it) for the core parts of your software is an important decision you can make.

