---
title: How to show your current Firebase project name on the command line prompt to
  prevent dangerous errors
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-03T21:36:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-show-your-current-firebase-project-name-on-the-command-line-prompt-to-prevent-dangerous-1bfee6293811
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8Yvp2a4vtkb5dWzWXh1qcQ.png
tags:
- name: Bash
  slug: bash
- name: Firebase
  slug: firebase
- name: 'tech '
  slug: tech
- name: terminal
  slug: terminal
- name: zsh
  slug: zsh
seo_title: null
seo_desc: 'By Thang Minh Vu

  When working on a project with multiple stages (development, staging, production),
  developers use the command firebase use to switch between projects. It’s very easy
  to run a command on the production environment instead of the devel...'
---

By Thang Minh Vu

When working on a project with multiple stages (development, staging, production), developers use the command `firebase use` to switch between projects. It’s very easy to run a command on the production environment instead of the development. This is very dangerous.

![Image](https://cdn-media-1.freecodecamp.org/images/eFjsis27Zzr7idxjQLbY6pGoFuXoJaFymGRv)
_Command to switch between firebase project_

**Note**: You can always find the latest script at my [GitHub repository](https://github.com/ittus/firebase-prompt).

Normally, developers only work on the development project. They only switch to production in case of checking or doing a hotfix. There have been a few times when I forgot to switch back to the development project. I accidentally changed the database without thinking that it could impact the actual users.

Digging into the _firebase CLI_, I found that it uses [configstore](https://github.com/yeoman/configstore) to manage local configuration. All config is saved in a JSON file and reads easily. I created a small script which is intended to show the firebase project name on **shell prompt**.

### How to set it up

#### Bash

Add the following script to the end of `~/.bash_profile`:

![Image](https://cdn-media-1.freecodecamp.org/images/vxqUWLsAfgLirG49oRLax03ekT7t5SfgaXYq)
_Add script to ~/.bash_profile_

Then run `source ~/.bash_profile` or open a new terminal window:

![Image](https://cdn-media-1.freecodecamp.org/images/ziaCqfVR0i6tyepr38KBdQ8jnmcdwq7pzHNl)
_Firebase project name is displayed as dev-project, stage-project and prod-project_

#### iTerm2 with oh-my-zsh

[Oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) is a popular open source framework for Zshell. I like it because it has many beautiful terminal themes and many useful plugins.

Here, I will make an example with the _agnoster_ theme:  
Edit `~/.oh-my-zsh/themes/agnoster.zsh-theme`

![Image](https://cdn-media-1.freecodecamp.org/images/RtXGYfMLwplrpQj-BQkXr3M9cMxpRKWuo4z4)
_Script for oh-my-zsh_

and then add `prompt_firebase` to `build_prompt` functions:

![Image](https://cdn-media-1.freecodecamp.org/images/uHVO625HTQdptNI1faRbYW8EZgHVpAEycvh4)
_Change build_promt function_

For the final step, run `source ~/.zshrc` or open a new terminal window:

![Image](https://cdn-media-1.freecodecamp.org/images/CsElxb8a3b4VSJjAqXkyFL-XrwhSXlLEIbuF)
_saas-cs-deploy-taguro-5c55e is displayed as last text in terminal prompt_

I hope this can help you prevent the an unexpected (and bad) situation.

**Note**: You can always find the latest script at my [GitHub repository](https://github.com/ittus/firebase-prompt).

