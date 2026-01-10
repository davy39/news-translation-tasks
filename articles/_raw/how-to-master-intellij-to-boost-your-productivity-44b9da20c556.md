---
title: How to Master IntelliJ to Boost Your Productivity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-05T15:54:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-master-intellij-to-boost-your-productivity-44b9da20c556
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MSm4kz4INUPevAEutrc80Q.jpeg
tags:
- name: coding
  slug: coding
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Jérémy Bardon

  DISCLAMER: This isn’t some free advertising for JetBrains, this is only about a
  developer sharing tips about IntelliJ.

  Without a doubt, the most important developer tool is the development environment
  (called IDE).

  My favourite and t...'
---

By Jérémy Bardon

**DISCLAMER: This isn’t some free advertising for JetBrains, this is only about a developer sharing tips about IntelliJ.**

Without a doubt, the most important developer tool is the development environment (called [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment)).

My favourite and the one I work with every day at work is **IntelliJ** (Ultimate version). In this article, I’ll share with you all the tips and tricks I’ve gathered from my experience and from my colleagues. This might help you master this tool and make your work easier.

Don’t leave if you don’t use IntelliJ or even if you hate it! I bet you can apply many of these tricks to your favourite IDE.

### Table of Contents

* [Convert microservices into modules](https://medium.com/p/44b9da20c556#c484)
* [Have effective code reviews](https://medium.com/p/44b9da20c556#c8d0)
* [Revert multiple commits](https://medium.com/p/44b9da20c556#4bd2)
* [Safety checks for Java devs](https://medium.com/p/44b9da20c556#d7d8)
* [Discuss with your database](https://medium.com/p/44b9da20c556#7ea7)
* Last piece of advice: [run dashboard](https://medium.com/p/44b9da20c556/edit#086e), [marked directories](https://medium.com/p/44b9da20c556#0245), [scratch files](https://medium.com/p/44b9da20c556#9fea), [install plugins](https://medium.com/p/44b9da20c556#a2d4), [overuse shortcuts](https://medium.com/p/44b9da20c556#59a0)

### Convert microservices into modules

If you work on many projects or your project implements a microservice architecture, you have independent projects in many directories.

This means you have to create one IntelliJ project for each project directory. Yet, you can’t have more than one project in a single IntelliJ window.

![Image](https://cdn-media-1.freecodecamp.org/images/ixVdg6rwoneJfniiYDG-4n9hrd5mZ4wR8JGA)
_Prompt if a project is already loaded (File &gt; Open Project)_

Creating modules is the solution. The idea is to create one IntelliJ project with independent modules.

![Image](https://cdn-media-1.freecodecamp.org/images/ZIk1S4P-bVjvAXgo2TKCKDA70ve2hOMsgcO3)
_Create a module from your project directory_

You can manage all modules in the Project Structure window (`File > Project Struct`ure). They’re also accessible by right-clicking on a single module and choosi`ng Open Module Setti`ngs.

### Have effective code reviews

I hope you’re using a version control system such as Git or Subversion. If you aren’t, you should consider learning more about version control systems!

IntelliJ provides a good integration for VCS, especially for code reviews. If your project contains many repositories within your modules, it’s possible to visualize every commit in one place.

First, check if version control knows your directories:

![Image](https://cdn-media-1.freecodecamp.org/images/cLNiqaz8C2OnmPKTM-MXQ5B3Mz5rDWfESHeN)
_File &gt; Settings &gt; Version Control_

Then, go check this tool window:

![Image](https://cdn-media-1.freecodecamp.org/images/4FlaxyN9EhW8vWZEmCChmcJEVAdeKerwGeEv)
_Version Control tool window (Log tab)_

You only have to enable the `Show Root Names` option to see the modules’ names on the left. The **Paths** filter allows you to filter using module names. Useful when you work on projects with a microservice architecture!

The right side of this window shows every modified file from the selected commit. You can click on `Show Diff` to open a new window and visualize modifications for each file.

![Image](https://cdn-media-1.freecodecamp.org/images/LOUR2-HUn1HlLJbMcOrgqvhEkXpuyfkaXAvR)
_Commit content for code reviews_

> If you need to review multiple commits at the same time, select the commits to review (hold the `ctrl` key) and click on `Show Diff`.

### Revert multiple commits

For some reason, you may need to revert a few commits in your project. If you’re not used to doing it, you can get into trouble.

Revert a commit is quite simple: right-click on it and choose revert. Once you eventually fix the conflicts, a commit popup will come up. If you only revert one commit, do as usual without checking the `Amend commit` option.

![Image](https://cdn-media-1.freecodecamp.org/images/dkiCWi7Tue6uRAkkpqW-shr8n4NOM0CcPLBw)
_Commit Changes window (don’t check Amend for the first reverted commit)_

But if you need to revert multiple commits, you have to be a bit more clever. The idea is to create one commit which reverts all commits at once — begin with the most recent to avoid conflicts.

When you revert a commit, you must commit the changes. It means you can’t perform multiple reverts and finally commit the result. My solution is to commit the first revert and then check the **Amend commit** option to squash the other reverts into this first commit.

### Safety checks for Java devs

IntelliJ comes with a lot of features for Java, including Maven integration. It’s highly configurable, but before exploring, you need to check some settings.

* Project SDK _(File > Project Structu_re)
* Java compiler version for each module _(File > Settings > Java Com_piler)
* Maven configuration _(File > Settings >_ Maven)

For Maven configuration, consider checking `Always update snapshots` if you work on microservice architectured projects.

![Image](https://cdn-media-1.freecodecamp.org/images/X3A8LqHWqBqMxqp3kIbwfJadMdptfA21csHq)
_Check Maven configuration_

Don’t forget to also check the **Ignored Files** section to make sure IntelliJ doesn’t ignore your module `pom.xml`. If your module is still not recognized as a Maven project, right click on your `pom.xml` and `Add as Maven Project`.

Sometimes you can compile using the terminal, but IntelliJ finds errors because of the Maven dependencies. To fix that, right click on the module `Maven > Rel`oad and then right click again `to Rebu`ild the module.

### Discuss with your database

I tried some clients to deal with databases, but using IntelliJ is far better when you’re also writing code.

You can explore your database without writing any code using the tree explorer. Then, if you double-click on a table, you can also filter results, perform some CRUD operations, and even export the data in many formats such as SQL, CSV and HTML.

![Image](https://cdn-media-1.freecodecamp.org/images/PeousZe3IFFleZP5Vt46oza2hXqQSb2sCy1m)
_Database table editor_

As you might think, SQL files support [syntax highlighting](https://en.wikipedia.org/wiki/Syntax_highlighting), autocomplete and the ability to run queries from the file. The good part is that you can write multiple queries in your file but only run highlighted queries with `Ctrl + Enter`.

### Last pieces of advice

#### Run dashboard

It’s possible to run your applications from IntelliJ, but you need to create a `Run Configuration` first. Once some process is running you’ll be able to list them all on a dashboard.

![Image](https://cdn-media-1.freecodecamp.org/images/dkbzaArlvNCv-3avb6m8zZvosKYhgmemMwCk)
_Run configuration settings_

To enable the Run Dashboard, open the Run Configuration popup and select `Defaults`. Then, you can add which kind of configuration can appear in your run dashboard.

#### Marked directories

When you do a right-click on a directory, you have the option to mark it as Source, Test, and even exclude it.

It’s useful, because you can hide excluded files in your project and also filter search results so that they don’t display tests _(in scope > Production Fil_es).

#### Scratch files

Creating temporary files is very convenient to test something outside of your project. IntelliJ supports this feature _(shortcut: Ctrl + Alt +Maj + Insert)_ with many kinds of files such as JavaScript and SQL_._ Plugins can help you to run those files. I recommend you to try Quokka which runs JS scratch files.

#### Install plugins

Plenty of plugins exist for IntelliJ — almost every popular framework and language has one. You should install those plugins and check if they help you in your daily work.

For instance, check [Advanced Java Folding](https://medium.com/@andrey_cheptsov/making-java-code-easier-to-read-without-changing-it-adeebd5c36de) which might be interesting for Java developers. You can also set up a particular font to easily distinguish similar characters such as `l 1 I` and `O 0 o`. I’d recommend [Source Code Pro](https://adobe-fonts.github.io/source-code-pro/) and [Hack](https://source-foundry.github.io/Hack/font-specimen.html) which help avoid confusing similar characters.

#### Overuse shortcuts

* `shift + shift` searches everywhere for a file
* `ctrl + shift + E` for recently opened files
* `ctrl + shift + F` searches a text in the path (use the module filter)
* `ctrl + click` jumps to variable/function declaration
* `ctrl + f12` searches variable/function in file
* `alt + F7` lists variable/function usages

Thanks for reading! This was a compilation of tips and tricks I’ve learned with experience and also with help from my colleagues. I hope you found something helpful for your daily work with IntelliJ!

**If you found this article useful, please click on the** ? **button a few times to make others find the article and to show your support! ?**

**Don’t forget to follow me to get notified of my upcoming articles** ?

### Check out my [Other](https://medium.com/@jbardon/latest) Articles

#### ➥ JavaScript

* [React for beginners series](https://medium.freecodecamp.org/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44)
* [How to Improve Your JavaScript Skills by Writing Your Own Web Development Framework](https://medium.freecodecamp.org/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190)
* [Common Mistakes to Avoid While Working with Vue.js](https://medium.freecodecamp.org/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b)

#### ➥ Tips & tricks

* [Stop Painful JavaScript Debug and Embrace Intellij with Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)
* [How To Reduce Enormous JavaScript Bundles Without Effort](https://medium.com/dailyjs/how-to-reduce-enormous-javascript-bundle-without-efforts-59fe37dd4acd)

