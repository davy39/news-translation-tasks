---
title: Improve your team’s development workflow with Githooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-15T16:06:01.000Z'
originalURL: https://freecodecamp.org/news/improve-development-workflow-of-your-team-with-githooks-9cda15377c3b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*fzif-QPdioernqbi
tags:
- name: Git
  slug: git
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: workflow
  slug: workflow
seo_title: null
seo_desc: 'By Daniel Deutsch

  Every product that is developed by more than one programmer needs to have some guidelines
  to harmonize the workflow.

  A standardized software development workflow between programmers allows, for example:


  faster engineering, since ea...'
---

By Daniel Deutsch

Every product that is developed by more than one programmer needs to have some guidelines to harmonize the workflow.

A standardized software development workflow between programmers allows, for example:

* faster engineering, since each developer can rely on a habitual activity
* fewer errors, as the workflow itself shall be structured in a way to avoid some mistakes
* easy integration of new members
* improved log of history

One very easy to use feature are “[Githooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)”(if you are using Git for version control).

In this article I want to show how easy it actually is to set up a few workflow guidelines with Githooks. This will allow your team to be on one page when developing software.

### Table of Contents

* [Why Githooks?](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#why-githooks)
* [GitFlow and Checkout, Commit, Push](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#gitflow-and-checkout-commit-push)
* [Post-checkout](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#post-checkout)
* [Commit-msg](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#commit-msg)
* [Pre-push](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#pre-push)
* [“Enforce” the hooks](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#%22enforce%22-the-hooks)
* [Fix one common problem](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#fix-one-common-problem)
* [Thanks](https://github.com/Createdd/Writing/blob/master/2018/articles/Githooks.md#thanks)

### Why Githooks?

Githooks are, as the word suggests, a hook for [Git](https://git-scm.com/) commands. Intuitively this makes sense. With Git you are essentially managing the workflow of a piece of software. Every Branch is a part of the whole piece. Every Commit is a building block of a Branch.

So in order to standardize quality in software development, one must standardize actions in the building process of the product.

There are many Git commands that can be hooked for setting standards. Remember, there are quite a few:

* applypatch-msg
* pre-applypatch
* post-applypatch
* pre-commit
* prepare-commit-msg
* commit-msg
* post-commit
* pre-rebase
* post-checkout
* post-merge
* pre-receive
* pre-push
* update
* post-update
* pre-auto-gc
* post-rewrite

To establish an improved workflow you don’t have to use all of them. Focus on the few important ones. In my experience so far, those are:

* commit-msg/pre-commit
* post-checkout
* pre-push

Let me explain why.

### GitFlow and Checkout, Commit, Push

Using Git as version control system allows to set a workflow. I do this using the [GitFlow method](https://datasift.github.io/gitflow/IntroducingGitFlow.html).

![Image](https://cdn-media-1.freecodecamp.org/images/0*f-3vMJcoDjKLJ3RJ)

It is basically to develop a piece of software where each feature is represented by a branch.

In the following examples I will always check naming with Regex tests or execute another script.

### Post-checkout

The increased importance of a branch allows for the first hook on “post-checkout”. It is triggered after a new branch is created with Git.

Often a naming convention is applied to make branches comparable and understand their use for the whole product.

You can create a simple shell script like this to ensure naming:

### Commit-msg

In web development there are multiple libraries that help with setting up a hook for committing. Often they are not necessary, as simple scripts can be written by yourself as well.

See validation of a git message for example:

### Pre-push

“Git push” is the process of “sharing” your branch with the team. It is often the last step before opening a pull-request for a merge with the main branch.

This is a good time to check other guidelines like “linting” of the code, or if all tests are passing.

An example for executing another script could be:

### “Enforce” the hooks

Another step is to actually enforce those hooks.

In JavaScript and NPM/Yarn package managers there is a “postinstall” script already built in. It allows for the execution of a script after the installing process. But what exactly should be executed?

Create your own install script! Like:

### Fix one common problem

One issue that kept me guessing for a while was that Git hooks are NOT executable by default. This means that they need to be made executable with

`chmod +x <pathToHo`ok>

See StackOverflow discussion [here](https://stackoverflow.com/questions/8598639/why-is-my-git-pre-commit-hook-not-executable-by-default).

### Thanks

I hope that this will help some of you to align the workflow of your development team and make everyone’s lives much easier. :-)

Thanks for reading my article! Feel free to leave any feedback!

Daniel is a software developer, a LL.M. student in business law, and organizer of tech-related events in Vienna. His current personal learning efforts focus on machine learning.

Connect on:

* [LinkedIn](https://www.linkedin.com/in/createdd)
* [Github](https://github.com/Createdd)
* [Medium](https://medium.com/@ddcreationstudi)
* [Twitter](https://twitter.com/_createdd)
* [Steemit](https://steemit.com/@createdd)
* [Hashnode](https://hashnode.com/@DDCreationStudio)

