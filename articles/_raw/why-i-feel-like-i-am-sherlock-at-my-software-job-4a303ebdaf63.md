---
title: I feel like Sherlock, if he were a developer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-30T08:16:07.000Z'
originalURL: https://freecodecamp.org/news/why-i-feel-like-i-am-sherlock-at-my-software-job-4a303ebdaf63
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-CNoGje_a2x2Nziq0pru-w.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By DHARA DOSHI

  It’s a normal day at work. My boss assigned me an issue that I know nothing about.
  And I’m supposed to solve it as fast as possible.

  Somewhere in a massive project is a piece of code that keeps crashing. To me, it
  feels as electrifying...'
---

By DHARA DOSHI

It’s a normal day at work. My boss assigned me an issue that I know nothing about. And I’m supposed to solve it as fast as possible.

Somewhere in a massive project is a piece of code that keeps crashing. To me, it feels as electrifying as a murder mystery.

Luckily for me, debugging and investigation go hand in hand.

Welcome to the crime scene!

There are clues. Some obvious suspicions. Some finger prints.

But nothing definite.

I track down the usual suspects, but they lead me nowhere.

> “There is nothing more deceptive than an obvious fact.”   
> ― [**Arthur Conan Doyle**](https://www.goodreads.com/author/show/2448.Arthur_Conan_Doyle) **in [The Boscombe Valley Mystery](https://www.goodreads.com/work/quotes/1214700)**

I call for the help of my equivalent of a Dr. Watson: my [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment).

I place a few breakpoints. I add a few watches.

I brainstorm a little more.

I play back the crime scene again and again, investigating the facts.

Skimming the stack trace, I get a flash of insight that helps me narrow my search.

I feel a shot of elation as I go into a function, and add a specific breakpoint.

And a few moments later, I emerge from my state of concentration, having solved the bug.

You want to know what the problem was?

If you know some basic C, take a look at this block of code, and see if you can find a clue as to what went wrong:

```
FILE *fd;char *filename="models/";strcat(filename,"bullet");strcat(filename,".h3d");if( (fd = fopen(filename,"r"))==NULL ){    printf("\nFile or Directory not found");    return;}
```

All right, drum roll… here’s the cause of the problem:

It was a [segmentation fault](https://en.wikipedia.org/wiki/Segmentation_fault). Plain and simple.

```
char *filename="models/"; // This is a string literal stored in read-only memory
```

```
When we use strcat to append to "filename", it is undefined behavior because we aren't allowed to write to that read-only memory.
```

So how did I solve it?

I allocated a memory buffer big enough to store the full path of the file.

```
char filename[256]; // Alternatively you can allocate dynamically strcpy(filename, "models/");strcat(filename,"bullet");strcat(filename,".h3d");
```

Now you see how I can’t help being Sherlock-ed now.

Stay tuned for the next mystery!

[**Subscribe to my Medium posts**](https://powered.by.rabbut.com/p/Ntce?c=0)  
[_Enter your email to receive updates from me._powered.by.rabbut.com](https://powered.by.rabbut.com/p/Ntce?c=0)

