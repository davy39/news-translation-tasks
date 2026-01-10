---
title: How contributing to open source made me a better developer — and how you can
  do it, too
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-17T02:19:15.000Z'
originalURL: https://freecodecamp.org/news/how-contributing-to-open-source-made-me-a-better-developer-and-how-you-can-do-the-same-89929cd9f497
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fu2BEgeHB_-QnlbIhJZfJg.jpeg
tags:
- name: GitHub
  slug: github
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Luciano Strika

  So you’ve been learning how to code. You are studying Algorithms and Data Structures.
  You are getting up to date on the latest Frameworks and their quirks. You can already
  smell some code smells, or even design solutions to real pro...'
---

By Luciano Strika

So you’ve been learning how to code. You are studying Algorithms and Data Structures. You are getting up to date on the latest Frameworks and their quirks. You can already smell some code smells, or even design solutions to real problems.

But you haven’t worked in the Software industry yet. Or you’re in your first job and see how everyone’s awesome and full of experience. Yet you feel like you’re the noobest of noobs. Impostor’s syndrome is a thing, and we’ve all been there.

There’s a way to get experience working in real codebases, nailing down the skills a book won’t teach you.

These are some of the things we can experience through Open Source:

* Reading other people’s code
* Understanding complex systems, one piece at a time
* Using versioning software (like git) in a proper way, with clear commit messages, atomic commits, and all those good, juicy practices.

If you’ve read this post’s title, you know where this is going. As a Medium reader, you’ve read many times that contributing to Open Source is awesome. It will teach you a lot, and may even get you noticed by some Big-N recruiter or something. I won’t say all those things are guaranteed, but I can definitely vouch for the first two.

#### My story

Let me tell you a story. When I started my first job, the repositories overwhelmed me. They had thousands of lines of code, they had conventions or lack of them, and the clashing styles. I had only worked on small college assignments. These assignments had 10000 lines tops, written by people I knew, over the span of a month.

I had never seen what a repository could fester into (or thrive into, if well maintained, but this is the industry we’re talking about here) after a couple of years of chaos and `git reset - -hard`‘s.

Learning to navigate that codebase was a skill in and of itself, which I gained after months of practice. But then when I started browsing GitHub, looking for a place to crash (or push), I started seeing how other repositories where organized.

Now, I am by no means an expert. My experience on GitHub so far has mostly been that of what, in some circles, would be called a lurker. I read the code, see what code does, read the issues, and think ‘geez, I wish I had any idea where to start’.

But then something awesome happened: some guy on Reddit posted a small project he had been working on. Not that many lines of code, mostly in Python (my favorite language), and maintained mostly by himself, with the help of a couple more people. I saw my chance and caught it. Studied the code, saw that some of the Python scripts worked perfectly, but they were a bit ugly: bad practices, repetition, really basic stuff the kind of person that actually gets things done may not stop to think about while coding the first draft, but comes to bite you in the leg afterward. So I set out to refactor.

(By the way, that project was [cheat.sh](http://cheat.sh), an interactive, web cheat-sheet for developers. Here’s the G[itHub](https://github.com/chubin/cheat.sh) project. It’s been an awesome project to contribute to, and I’d recommend you to check it out.)

#### A tutorial

Along with this article, I made a tutorial so you can brush up on your git.   
I will assume we’re using a GitHub repo, as that’s what most of you may end up doing in your jobs. For this tutorial, I’ve set up a [**small example repository**](https://github.com/StrikingLoo/contributions-worktable) so you can follow along. Instructions are also present in the README.md file.

Here’s what you’ll have to do on this small assignment:

* Visit the repository’s link, and hit the **fork** button. This will create a copy of the project’s history up until this point under your own profile.
* Make a local directory in your computer
* Add both my project, and the one you created, as remote repositories. In order to do this, open your terminal in the directory you’ve created and use the following command:

```
 git remote add *name* *link* 
```

It’s customary for the name of my project’s link to be ‘_upstream_’, and yours to be ‘_origin_’.

* **Pull** my project:

```
git pull origin master
```

* Add your name to the contributors list in the README.md using your favourite text editor (I like Vim, for instance). Don’t forget to save your changes!
* **commit** the changes:

```
git add . && git commit -m ‘Your awesome message to me here’
```

* Go to your Github account, visit your copy of the project and hit ‘**pull request**’, choosing to merge your master branch with mine.

I promise I will accept requests as soon as I can, probably on the same day… And that’s it! No different to how it would have worked if you were making a big contribution!

#### **Call to action**

Now you have no excuse, go find a project you actually like or care about and add some lines to it! It doesn’t matter if your changes are small, as long as you’re helping and learning through them. My first contribution was correcting a typo in a README.

I am trying new things this year, and writing on Medium has been on my bucket list for a while now.

This was my first ever article, and I will be glad if you give me any feedback or opinions on anything you’ve read.

Also as I am new to Open Source software, please tell me if there’s anything important you feel I’ve missed. Finally, if you’ve already made Open Source contributions, I’d like to hear some stories and opinions. What are the best projects to contribute to, and the ones you’ve liked the most/least? It would be nice if we could compile a list for beginners.

Thanks for reading this far, I’ll see you soon!

_Follow me for more articles about programming and Data Science, and check out my latest (probably better) articles._

