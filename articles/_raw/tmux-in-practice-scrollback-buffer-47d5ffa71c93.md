---
title: 'tmux in practice: scrollback buffer'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-26T13:50:16.000Z'
originalURL: https://freecodecamp.org/news/tmux-in-practice-scrollback-buffer-47d5ffa71c93
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WOE01gwjsFx-0gGi5KdZfA.gif
tags:
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Alexey Samoshkin

  The difference between terminal and tmux scrollback buffers, and how to tweak copy
  mode, scroll, and mouse selection of tmux behavior.

  This is 3rd part of my tmux in practice article series.

  Usually terminal emulators implement sc...'
---

By Alexey Samoshkin

#### The difference between terminal and tmux scrollback buffers, and how to tweak copy mode, scroll, and mouse selection of tmux behavior.

This is 3rd part of my [tmux in practice](https://medium.com/@alexeysamoshkin/tmux-in-practice-series-of-posts-ae34f16cfab0) article series.

Usually terminal emulators implement scrollback buffer, so you can explore past output, when it moves out of view. tmux, like other full-screen terminal applications like vim, runs in so-called alternate screen buffer of a parent terminal. Alternate buffer has exact width and height dimensions as physical window size.

There are several effects of using alternate buffer:

* Any output, that exceeds visible part of alternate buffer, is lost. As soon as lines go out of view, they are lost. To prevent history loss, tmux implements it’s own “inner” scrollback buffer. The consequence of this is that you cannot work with tmux inner scrollback same as you usually do within your terminal.
* Any output produced inside tmux (the same is true for vim, nano, man, less, and so on) does not spill over into the outer terminal’s scrollback history. When you close your full-screen app, you get back to the same state when you launched the app and don’t see output from inside the app any more.

In practice, if you get used to scroll back using `⌘↑` in your iTerm and if you’re going to do the same inside running tmux session, you will control and scroll the outer iTerm’s scrollback buffer, rather than the tmux’s inner scrollback buffer.

The solution is to use tmux specific controls to access its own scrollback buffer: `Ctrl-b` then `[` to enter copy mode, use `Down/Up` arrows or `PageDown` and `PageUp` keys, `q` or `Enter` to exit copy mode.

Some people who find this annoying — configure tmux scrollback buffer to be allowed to be shown up in parent terminal scrollback buffer — so they can just use familiar scrolling controls. [See this post](https://dan.carley.co/blog/2013/01/11/tmux-scrollback-with-iterm2/). However, this solution is limited to having tmux session with 1 window and 1 pane only. And when you detach/close a tmux session, the parent terminal is polluted with tmux window’s output.

Personally, I use tmux scrollback without hacks above, but tweak it’s configuration to be more friendly and familiar.

First of all, I don’t like `prefix,[` to enter copy mode. I’ve gotten used to `⌘↑` to start scrolling in iTerm, and I’ve added following root keybinding:

```
# trigger copy mode bybind -n M-Up copy-mode
```

Once you’re in copy mode, you can continue pressing`M-Up` to scroll 1 line up. The usual `PageDown` and `PageUp` controls are available to scroll by whole screen, and extra `M-PageDown` and `M-PageUp` to scroll by a half of screen (really convenient).

```
# Scroll up/down by 1 line, half screen, whole screenbind -T copy-mode-vi M-Up              send-keys -X scroll-upbind -T copy-mode-vi M-Down            send-keys -X scroll-downbind -T copy-mode-vi M-PageUp          send-keys -X halfpage-upbind -T copy-mode-vi M-PageDown        send-keys -X halfpage-downbind -T copy-mode-vi PageDown          send-keys -X page-downbind -T copy-mode-vi PageUp            send-keys -X page-up
```

Moreover, even when I’m inside tmux session, I can still continue using `⌘↑` and `⌘↓` to control the inner tmux scrollback buffer, rather that iTerm’s one. It’s possible by using custom iTerm profile with some keybindings overridden to trigger tmux actions. So `⌘↑` pressed in iTerm just sends `M-Up` keystroke to tmux session.

Read my previous part of “tmux in practice” series for more details: [tmux in practice: iTerm2 and tmux integration](https://medium.com/@alexeysamoshkin/tmux-in-practice-iterm2-and-tmux-integration-7fb0991c6c01).

Another tmux’s default I would prefer to change is the mouse wheel scroll. It scrolls by 5 rows, which feels like a big jump. Let’s reduce it to scroll by 2 rows:

```
# When scrolling with mouse wheel, reduce number of scrolled rows per tick to "2" (default is 5)
```

```
bind -T copy-mode-vi WheelUpPane select-pane \; send-keys -X -N 2 scroll-upbind -T copy-mode-vi WheelDownPane select-pane \; send-keys -X -N 2 scroll-down
```

Well, now let’s talk about copying text once you’re in copy mode. I get used to copy text using mouse. Let’s enable mouse support:

```
set -g mouse on
```

By default, when you select text with the mouse in tmux, it get’s copied to buffer, and you’re immediately dropped out of the copy mode. Your current scroll position is reset by the end of the output, and you’re put in a command prompt mode. Let’s see this in action:

![Image](https://cdn-media-1.freecodecamp.org/images/S61DaFvLkDfW6Q2RmmPkZojMHwxrHj-JZZKN)
_Kicked off copy mode on mouse drag end_

As you notice, each time I select text with the mouse, it kicks me off the copy mode. It’s really annoying. Usually when I’m stuck with some task, I tend to select some text here or there just to meditate (it helps me to focus on ?). Or you might want just to select some text to highlight for you colleague sitting next to you.

So let’s tweak this. We don’t want to be kicked off the copy mode. We don’t want the selection cleared on the mouse drag end event. Text from the selection can be copied on the mouse left click afterwards.

```
# Do not copy selection and cancel copy mode on drag end event# Prefer iTerm style selection: select, then mouse click to copy to bufferunbind -T copy-mode-vi MouseDragEnd1Panebind -T copy-mode-vi MouseDown1Pane select-pane \;\  send-keys -X copy-pipe "pbcopy" \;\  send-keys -X clear-selection
```

Let’s check out the result:

![Image](https://cdn-media-1.freecodecamp.org/images/AZl-e1MAfVIJRZjUjW37DGehkURLqVzBWPOj)
_Stay in copy mode and do not clear selection on mouse drag end event_

To access the copy buffer items and paste the most recent item, use `C-p` and `p`:

```
bind p paste-bufferbind C-p choose-buffer
```

That’s it for today. Stay tuned. In the next part of “tmux in practice” series, we’ll talk about clipboard integration, and how to share text copied inside tmux with the system clipboard (both locally and when working remotely, on OSX and Linux).

BTW, you can see all those configuration tweaks in action, just checkout my [tmux-config](https://github.com/samoshkin/tmux-config) repo.

#### Trick

If you want to bypass tmux copy mode altogether and select text via iTerm, just hold `<O`pt> key while dragging you mouse.

### Resources and links

shell — What exactly is scrollback and scrollback buffer? — Unix & Linux Stack Exchange — [https://unix.stackexchange.com/questions/145050/what-exactly-is-scrollback-and-scrollback-buffer](https://unix.stackexchange.com/questions/145050/what-exactly-is-scrollback-and-scrollback-buffer)

tmux scrollback with iTerm2 • dan.carley.co — [https://dan.carley.co/blog/2013/01/11/tmux-scrollback-with-iterm2/](https://dan.carley.co/blog/2013/01/11/tmux-scrollback-with-iterm2/)

tmux copy mouse selected text to clipboard automatically on mouse release — Stack Overflow — [https://stackoverflow.com/questions/36815879/tmux-copy-mouse-selected-text-to-clipboard-automatically-on-mouse-release](https://stackoverflow.com/questions/36815879/tmux-copy-mouse-selected-text-to-clipboard-automatically-on-mouse-release)

keyboard shortcuts — tmux — scroll up/down with shift + page up/down into a pane — Super User — [https://superuser.com/questions/702189/tmux-scroll-up-down-with-shift-page-up-down-into-a-pane](https://superuser.com/questions/702189/tmux-scroll-up-down-with-shift-page-up-down-into-a-pane)

[question/request] copy-mode without automatically selecting a pane? · Issue #1021 · tmux/tmux — [https://github.com/tmux/tmux/issues/1021](https://github.com/tmux/tmux/issues/1021)

ssh — Leaving tmux scrollback in terminal (iTerm2) — Stack Overflow — [https://stackoverflow.com/questions/12865559/leaving-tmux-scrollback-in-terminal-iterm2](https://stackoverflow.com/questions/12865559/leaving-tmux-scrollback-in-terminal-iterm2)

command line — Use terminal scrollbar with tmux — Super User — [https://superuser.com/questions/310251/use-terminal-scrollbar-with-tmux](https://superuser.com/questions/310251/use-terminal-scrollbar-with-tmux)

