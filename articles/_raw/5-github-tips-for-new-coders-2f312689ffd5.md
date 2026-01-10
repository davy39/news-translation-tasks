---
title: 5 GitHub tips for new coders
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-20T21:59:49.000Z'
originalURL: https://freecodecamp.org/news/5-github-tips-for-new-coders-2f312689ffd5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zJqp4FDnH00116rssJbdeg.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Alyson La

  This October I celebrated my 5 year anniversary working at GitHub. ? 5 years ago,
  I was an enthusiastic accountant (like straight nerd — my former twitter handle
  was @taxaly) who knew nothing about code, let alone about using Git and Git...'
---

By Alyson La

This October I celebrated my 5 year anniversary working at GitHub. ? 5 years ago, I was an enthusiastic accountant (like straight nerd — my former twitter handle was @taxaly) who knew nothing about code, let alone about using Git and GitHub.

Now I’m an enthusiastic Data Scientist who knows a handful of things about coding using Git & GitHub. It’s partially thanks to learning these technologies that I made this rewarding career switch.

But even working at GitHub, learning Git and GitHub were hard! As it’s own form of an open source contribution, I wanted to share with other folks new to coding my top 5 tips for using GitHub.

### **Tip #1: Change your default text editor associated with Git**

For many people, the default text editor when using Git from the terminal is VIM. VIM can be a terrible, scary thing for the new or casual hacker. Or even for veteran hackers or [@haacked](https://twitter.com/haacked) himself.

If you ever find yourself with a merge conflict (and you will, see tip #4), you’ll get kicked out to VIM to fix the conflict and then you’ll need to know the specific VIM commands to edit the doc and want to cry. For more than a year I had a sticky note on my monitor at work as a reminder of the basic VIM commands like `i` (to edit) and `:wq` (to save and quit). To avoid the potential tears, you could just change the default text editor.

In order to change your text editor to Atom, Sublime, or TextMate, follow the instructions in this [GitHub Help](https://help.github.com/articles/associating-text-editors-with-git/).

While you are at it, you should also make sure your shortcuts are set up so you can open files in your preferred text editor directly from the terminal using `subl .` or `atom .`Check out [these docs](http://flight-manual.atom.io/getting-started/sections/atom-basics/#opening-modifying-and-saving-files) for setting up Atom access from your terminal and [these docs](http://www.sublimetext.com/docs/2/osx_command_line.html) for setting up Sublime.

### Tip #2: **Change your dotfiles**

I didn’t learn about dotfiles until I was hacking and using Git & GitHub for multiple years. I’m still bummed that I didn’t know about this sooner!

Dotfiles allow you to customize your terminal prompt so you can see what git branch you are on & if you have uncommited changes. IT’S GENIUS! I got [my dotfiles](https://github.com/alysonla/dotfiles) from a co-worker ([John Nunemaker](https://www.freecodecamp.org/news/5-github-tips-for-new-coders-2f312689ffd5/undefined)) but if you search GitHub for ‘dotfiles’ you’ll find loads of options.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nLOXZnYWV-CopD55vREPXA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*0UPvjS69Z925qDx_1RJ68Q.jpeg)
_dotfiles for the win!_

### Tip #3: **Install Hub**

[Hub](https://github.com/github/hub) is a command line tool that makes it easier to use GitHub. Often I will be working on a repository in my terminal but want to see issues or pull requests on GitHub. So I’ll open a browser tab, then get distracted by email/twitter/a puppy — and ten minutes later, get around to typing in the GitHub repository url.

By typing `hub browse` in the terminal, it will auto-magically open the url of the repository directly in your browser for distraction free GitHub-ing. Boom.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zJqp4FDnH00116rssJbdeg.png)
_Nash the Octodog_

### Tip #4: **Practice merge conflicts**

This is where I admit that I’m sometimes a quitter. Specifically when it comes to merge conflicts. I cannot remember the number of times that I’ve abandoned a project or pull request because I hit a merge conflict.

They scared me, the docs on how to fix them scared me, and then I was in VIM and wanted to quit forever (see tip #1).

Then I realized I needed to face my fear so I started a practice repository, created a merge conflict **on purpose**, and [walked through the documentation](https://github.com/blog/2293-resolve-simple-merge-conflicts-on-github) or watched a YouTube video on how to fix merge conflicts. I did that a few times. Also now you can [fix simple merge conflicts](https://github.com/blog/2293-resolve-simple-merge-conflicts-on-github) in the GitHub User Interface so that’s been handy.

Today when I hit a merge conflict, I am slightly less scared and calmly make my way deleting the carrots, knowing that thanks to version control, I can’t mess things up too much.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DKRDKuXmj0b7x6L2bsz4bQ.gif)
_Practice._

### **Tip #5: Make a GitHub Page**

A GitHub page is a personal or project based website that GitHub will host for free! It always helps to have an actual project to push up to GitHub to practice your Git and GitHub skills.

Make a simple website using HTML, CSS, and JavaScript from a coding tutorial then follow the steps to host it on GitHub [here](https://pages.github.com/) or you can check out [this](https://www.youtube.com/watch?v=rRGrT0wsJxI) video I made a while back with step by step instructions. Or try the super easy [Fork and Go](https://github.com/jlord/forkngo) method.

Last, I’m gonna sneak in a 6th maybe obvious tip which is — **take a Git and Github class or tutorial**!

Here are a few that are worth checking out:

* Git-it: [https://github.com/jlord/git-it-electron](https://github.com/jlord/git-it-electron)
* freeCodeCamp videos: [https://youtu.be/vR-y_2zWrIE](https://youtu.be/vR-y_2zWrIE)
* GitHub Training: [https://services.github.com/on-demand/resources/](https://services.github.com/on-demand/resources/)
* Git Cheatsheet — [http://ohshitgit.com/](http://ohshitgit.com/)

I hope this list of tips was helpful and if you have any other tips that you found helpful in your journey to learn Git and GitHub, I’d love to hear them! ❤

