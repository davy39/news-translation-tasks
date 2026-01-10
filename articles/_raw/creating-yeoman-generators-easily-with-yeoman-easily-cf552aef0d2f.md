---
title: Creating Yeoman generators easily with yeoman-easily
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-01T16:44:51.000Z'
originalURL: https://freecodecamp.org/news/creating-yeoman-generators-easily-with-yeoman-easily-cf552aef0d2f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*80vnFUltjdnV38Owrjr95g.png
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
- name: yeoman
  slug: yeoman
seo_title: null
seo_desc: 'By Krist Wongsuphasawat

  I’ve used Yeoman to start many of my projects. It’s an amazing web scaffolding tool.

  But after creating my own generators several times, I saw the repetitive tasks,
  somewhat lengthy code, and part of the generator code that co...'
---

By Krist Wongsuphasawat

I’ve used [Yeoman](http://yeoman.io/) to start many of my projects. It’s an amazing web scaffolding tool.

But after creating my own generators several times, I saw the repetitive tasks, somewhat lengthy code, and part of the generator code that confused me every time.

At one point, I ended up hacking a small utility that I kept copying over and over from project to project. I spent a weekend organizing it and adding several more features to take care of repetitive tasks.

### And yeoman-easily was born.

[yeoman-easily](https://github.com/kristw/yeoman-easily) helps with the following tasks when creating a generator with Yeoman:

#### Advantage #1: Confirmation

Often you would like to ask for user confirmation before proceeding. The first code block below shows how to write this with plain Yeoman. The second code block shows how to write it with the help of yeoman-easily.

With yeoman-easily, you can ask for confirmation before proceeding in one line. `easily.confirmBeforeStart(message)` then `easily.checkForConfirmation()` returns the result.

#### **Advantage #2: Prompting**

Handling results from the prompt, then choosing which prompt to display used to be complicated.

* `this.prompt()` returns a promise which needs to be handled to obtain the answers and store them. The answers are commonly stored into `this.props`. This block of code has to be written again and again.
* A parent generator often passes the parameters to the child generator via options. From what I have seen, many generators will hide the prompts for fields that are present in the options. (Yes, you have to write code to check that.) Then combine answers from prompts and options into `this.props`.

For convenience, yeoman-easily:

* Handles storing user’s answers from the prompts into `this.props`. Just call `easily.prompt(prompts)` instead of `this.prompt(prompts)`
* Can automatically skip a prompt if an option with the same name is present. It will also copy the value of existing `this.options[field]` into `this.props[field]`.
* Can register common prompts via `easily.learnPrompts(prompts)` and allow looking up prompts by name while calling `easily.prompt()`. This can save a lot of time if you create multiple generators that ask similar questions.

#### **Advantage #3: Composing**

Yeoman generator can call (`composeWith`) another generator from another package or local subgenerator, but the current syntax for doing so is somewhat long. I am still not sure what the _local_ field means.

yeoman-easily simplifies the syntax to `easily.composeWithLocal(name, namespace, options)` and `easily.composeWithExternal(package, namespace, options)`.

#### **Advantage #4: File handling**

Yeoman provides flexible APIs for file handling to cover many scenarios. But it takes a few lines to perform common task such as copying a file from the template directory to the destination directory. A function for bulk copying also exists, but it’s discouraged.

To address the above issues, yeoman-easily:

* Provides I/O functions that wraps `this.fs.xxx` and also resolves _template_ and _destination_ directory for common cases (from template to destination). These functions include `read`, `write`, `writeJSON`, `extendJSON`, `exists`, `copy`, and `copyTemplate`. I have a full list in my [API documentation](https://github.com/kristw/yeoman-easily/blob/master/docs/api.md).
* Provides functions for mass copying both static and dynamic files based on glob pattern. See `easily.copyFiles(…)` in the example below.

#### Advantage #5: Method chaining

yeoman-easily was created with chaining in mind and support method chaining for fluent coding.

### Putting it all together

Here’s an example that demonstrates all of these advantages together into one generator:

The yeoman-easily package is now available on npm. Visit the [github repo](https://github.com/kristw/yeoman-easily) for more details, [API documentation](https://github.com/kristw/yeoman-easily/blob/master/docs/api.md) and examples. I welcome your pull requests and bug reports.

