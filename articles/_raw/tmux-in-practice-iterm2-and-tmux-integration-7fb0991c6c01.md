---
title: 'tmux in practice: iTerm2 and tmux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T00:01:18.000Z'
originalURL: https://freecodecamp.org/news/tmux-in-practice-iterm2-and-tmux-integration-7fb0991c6c01
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gGNWXlll62GCAM55hbldbw.png
tags:
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Alexey Samoshkin

  Benefits and drawbacks of using iterm2 vs tmux locally. How to set up iTerm2 profile
  to override key mappings to trigger analogue tmux actions

  This is 2nd part of “tmux in practice” post series.


  tmux experience inside full-screen...'
---

By Alexey Samoshkin

#### Benefits and drawbacks of using iterm2 vs tmux locally. How to set up iTerm2 profile to override key mappings to trigger analogue tmux actions

This is 2nd part of “[tmux in practice](https://medium.com/@alexeysamoshkin/tmux-in-practice-series-of-posts-ae34f16cfab0)” post series.

![Image](https://cdn-media-1.freecodecamp.org/images/ENolmODK64FDqsCG3HlDAmw2YW8IGOP5KDL-)
_tmux experience inside full-screen iTerm with 2 remote sessions nested in a local one_

So you’re using iTerm2 terminal emulator on OSX. And you’ve heard about tmux, and decided to give it a try. Google here, Google there, after a while you grasp concepts like terminal multiplexing, windows, pane splitting, and understand tmux usage on remote machines to persist session state and survive abrupt disconnections.

At some point of time, you might wondering about tmux usage locally.

> “Given iTerm already can create multiple virtual windows inside a single ‘physical’ window, can split, swap and resize panes, do I really need to use tmux on my local machine instead of iTerm?”

When I was learning tmux, I had been returning to same question again and again. It was not clear without some practice. So I’ve decided to give it a try, and today I can share benefits and drawbacks with you.

### iTerm2 vs tmux on local machine: benefits and drawbacks

#### **Benefits:**

* **Named windows.** Similar to tabs in iTerm, but you can give them a name
* **A status line with system-wide information.** Includes CPU, memory, online/offline status, battery, user, host, and date time.
* Having status line and set of named windows inside it, I can turn iTerm to full-screen mode. This which allows me to work in **a distraction-free environment** and also get extra 3 rows. These previously were taken by OSX menu bar, iTerm window frame and iTerm tabs row.
* **Monitor window for activity or silence.** When I run a long-running command in one pane, I can switch to another pane and be notified when no more output appears in previous pane for some interval  
iTerm has [something similar](https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration), but it’s only about notifying you when execution returns to command prompt, and requires installing extra [shell integration](https://iterm2.com/documentation-shell-integration.html)
* **Redefined panes layouts.** Even-horizontal, even-vertical, main-horizontal, main-vertical and tiled
* **Ability to switch between several per-project local tmux sessions** to easily switch context
* If you’re using tmux both locally and on remote machine, you’d get **the same familiar terminal environment**
* When you’re using tmux, you rely on iTerm2 unique features much less  
This makes it **easier to migrate to a different terminal emulator**, be it on same OS or another one (Linux)

#### **Drawbacks:**

* **tmux maintains it’s own scrollback buffer.** It’s more difficult to access it and copy text than in iTerm (just scroll and select with mouse)
* **If you copy text in tmux, it’s stored in tmux own buffer, and not shared with your OS clipboard by default.** To be 100% correct, sharing with system clipboard works in iTerm2, but just because it supports OSC 52 ANSI escape sequences that let application such as tmux to access and store data in clipboard. iTerm2 is a special case. Just try to copy text in tmux running in OSX default Terminal, which does not support OSC52
* If you’re already accustomed to iTerm keybindings, **you need to learn and switch to tmux keybindings**, which are cumbersome. Instead of single keystroke like ⌘⌥->, you need two keystoke`s: pre`fix followed by another key, mapped to specific tmux action.

Personally, I decided to go ahead with tmux and its features, and rely less on iTerm2 specific features. Indeed, right now I’m using iTerm just as a tunnel to tmux ?

**Issues with scrollback buffer and integration with OS clipboard are highly vital**, **that** **you can even decide to give up adopting tmux.** We’ll address these topics in my future posts.

### Override iTerm key mappings to trigger tmux action

Today, let’s see how we can use familiar iTerm keybindings while working in tmux environment. The idea is to map keystrokes in iTerm to trigger tmux actions.

The easy way would be just to go to `.tmux.conf` and map tmux actions to those keybindings. For example, to resize pane in iTerm, we use “`^⌘↑`”, let’s map the same keystroke in tmux in somewhat naive way:

```
bind ^⌘↑ resize-pane -U
```

However, the code above will not work because you cannot use ⌘ in tmux keybindings, and SHIFT usage is also very limited. And even it that was possible, iTerm would intercept that keystroke before.

Instead we setup new iTerm profile, and override key mappings to send pre-configured sequences of bytes, that will trigger corresponding action in tmux.

![Image](https://cdn-media-1.freecodecamp.org/images/OTGL8jqmLb6EK9cMaxorINKrWAqffH0Aqgpe)
_Creating dedicated profile and override key mappings_

For example, when “`^⌘↑`” pressed, sequence of bytes `0x01 0x1b 0x5b 0x31 0x3b 0x35 0x41` is sent through the terminal to the running tmux instance. It interprets them as `C-a C-↑` keybinding and triggers `resize-pane -U` according to our `.tmux.conf` configuration.

So how you can get those hex codes? Use `showkey`, `od` or `hexdump` commands to view binary representation of key presses from keyboard:

```
$ showkey -aPress any keys - Ctrl-D will terminate this program
```

```
^A        1 0001 0x01^[[1;5A  27 0033 0x1b         91 0133 0x5b         49 0061 0x31         59 0073 0x3b         53 0065 0x35         65 0101 0x41
```

**Note**: `showkey` is not available on OSX, but you can always SSH on Linux remote machine and use it ?. If it sounds like a huge overhead, just use o`d` or h`exdump.`

```
$ od -t x1
```

```
^A^[[1;5A   // press C-a C-↑ on your keyboar0000000 01 1b 5b 31 3b 35 410000007
```

You can remap whatever key in this way, but I do this only for most common, which have analogue action in tmux.

By the end of the day, I can create new tmux panes using `⌘D` and `⌘⇧D`, select panes using `⌘⌥→ , ^`Tab to switch to most recently used window, `⌘⇧`Enter to zoom pane, `^⌘←` to resize pane to the left, `⌘[` to select previous pane, `⌘W` to kill current pane, and so forth. So, I don’t need to fight against my muscle memory for most common actions.

For all other actions without correspondence I still use tmux way:`C-a` prefix followed by action key. If you’re curious about complete list of such keybindings, and how all this works in action, check out my [tmux-config](https://github.com/samoshkin/tmux-config#key-bindings) repository.

Also, I’ve found predefined layouts to be very useful: even-horizontal, even-vertical, main-horizontal, main-vertical, tiled. I usually work in main-vertical layout, and need to swap secondary pane with main forth and back. This is so common, that I decide to setup a keybinding both in tmux `(prefix \)` and iTerm `(⌘\)`.

```
# Swap panes back and forth with 1st pane# When in main-(horizontal|vertical) layouts, the biggest/widest panel is always @1bind \ if '[ #{pane_index} -eq 1 ]' \  'swap-pane -s "!"' \  'select-pane -t:.1 ; swap-pane -d -t 1 -s "!"'
```

As an extra step, you can setup this new iTerm profile as default, and tell it to jump into tmux session right at the start.

![Image](https://cdn-media-1.freecodecamp.org/images/ma0knlzOuYXJfroPYHaj-VpEyfXeQ7iGizg3)

And don’t forget to run you iTerm2 in full screen mode. It’s worth it.

### Native integration between iTerm2 and tmux

There is an [integration between iTerm2 and tmux](https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration) powered by iTerm that you might be interesting in.

The idea is that iTerm still handles window and pane management, maintain scrollback buffers, copy/paste as usual, but all windows are backed by tmux session under the hood. It’s tmux session indeed, but abstracted and encapsulated by familiar iTerm environment for you. You can close iTerm, open it back and reattach to previous session, without state lost.

However, it makes little sense for local environment (only useful in case of an iTerm crash which is an extremely rare event). Personally, I don’t like this approach, because it hides me from the fact I’m using tmux, and exposes only those most common tmux features, which have analogues in iTerm (create window, split pane, resize window/pane, close session).

### Resources and links

Tmuxintegration · Wiki · George Nachman / iterm2 · GitLab — [https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration](https://gitlab.com/gnachman/iterm2/wikis/TmuxIntegration)

iTerm2 keymaps for tmux — Dan Lowe — [http://tangledhelix.com/blog/2012/04/28/iterm2-keymaps-for-tmux/](http://tangledhelix.com/blog/2012/04/28/iterm2-keymaps-for-tmux/)

Auto-Starting Tmux in iTerm2 — Sašo Matejina — Medium — [https://medium.com/@sasom/auto-starting-tmux-in-iterm2-4276182d452a](https://medium.com/@sasom/auto-starting-tmux-in-iterm2-4276182d452a)

samoshkin/tmux-config: Tmux configuration, that supercharges your tmux to build cozy and cool terminal environment — [https://github.com/samoshkin/tmux-config](https://github.com/samoshkin/tmux-config)

