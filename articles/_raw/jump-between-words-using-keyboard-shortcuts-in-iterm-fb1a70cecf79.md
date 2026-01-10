---
title: Jump between words using keyboard shortcuts in iTerm
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2018-01-28T18:49:35.000Z'
originalURL: https://freecodecamp.org/news/jump-between-words-using-keyboard-shortcuts-in-iterm-fb1a70cecf79
coverImage: https://cdn-media-1.freecodecamp.org/images/0*PgviMTnKvX_ivYIG.png
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: iTerm is a great terminal replacement that I like to use. One feature that
  I wanted after my migration from Windows to OS X was the ability to jump between
  words in the command line, and not having to go through the whole line, character
  by character...
---

iTerm is a great terminal replacement that I like to use. One feature that I wanted after my migration from Windows to OS X was the ability to jump between words in the command line, and not having to go through the whole line, character by character.

It turns out that this is quite possible and doesn’t cause much pain and effort on your side. You do not need to pay 1 BTC to Apple to get this working. You only need to make a few keystroke changes in your iTerm preferences and you are done.

In other words, you do not need to install anything else in your OS X. All you have to do is make a few configurations in the iTerm preferences, and you are good to go.

It’s that easy.

Let’s get started.

To make this work for the right option key, you need to set the key modifier to act as an escape sequence.

First, you need to set your left ⌥ key to act as an escape character.

![Image](https://cdn-media-1.freecodecamp.org/images/rdEDhYcmDHmBVijhouwsFatN18kEY6ZD08ST align="left")

After that, you can either change the current shortcut for ⌥ ← or create a new one, in the profile shortcut keys, with the following settings:

* Keyboard Shortcut: ⌥←
    
* Action: Send Escape Sequence
    
* Esc+: b
    

![Image](https://cdn-media-1.freecodecamp.org/images/LqVy4VYF8AHtoeyBTt5FiwraeY3X2IZrQ46j align="left")

Now we need to repeat a similar process for the ⌥→ keyboard shortcut with the following settings:

* Keyboard Shortcut: ⌥→
    
* Action: Send Escape Sequence
    
* Esc+: f
    

That’s all we need to do. After we are done, we may need to restart the iTerm to be able to use the changes that we just made.

Now we can skip entire words on the command line interface by holding down the left ⌥ key and hitting ← or →.

I hope you find this article helpful.

*This article was first published by the author on his* [*blog*](http://www.fatosmorina.com/jump-words-using-keyboard-shortcuts-iterm/)*.*
