---
title: “tmux in practice” series of posts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-27T14:27:33.000Z'
originalURL: https://freecodecamp.org/news/tmux-in-practice-series-of-posts-ae34f16cfab0
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb240740569d1a4cac0c7.jpg
tags:
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Alexey Samoshkin

  Explore tmux and its tough questions and tricks, including features, nested sessions,
  scrollback buffer, clipboard integration, and iTerm2 integration.

  I just finished my writings on tmux topic.

  There are several topics I’ve cover...'
---

By Alexey Samoshkin

#### Explore tmux and its tough questions and tricks, including features, nested sessions, scrollback buffer, clipboard integration, and iTerm2 integration.

I just finished my writings on tmux topic.

There are several topics I’ve covered so far. This post’s goal is to be an index page to all parts of “tmux in practice” series. Happy reading:

**Part 1.** [Tmux in practice: explores local and nested remote tmux sessions](https://medium.com/@alexeysamoshkin/tmux-in-practice-local-and-nested-remote-tmux-sessions-4f7ba5db8795). It also discusses tmux features in general, their relevance for local and remote scenarios, and how to setup and configure tmux to support nested sessions.

**Part 2.** [tmux in practice: iTerm2 and tmux integration](https://medium.com/@alexeysamoshkin/tmux-in-practice-iterm2-and-tmux-integration-7fb0991c6c01) includes benefits and drawbacks of using iterm2 vs tmux locally. It shows how to set up iTerm2 profile to override key mappings to trigger analogue tmux actions.

**Part 3.** [tmux in practice: scrollback buffer](https://medium.com/@alexeysamoshkin/tmux-in-practice-scrollback-buffer-47d5ffa71c93). Explores the difference between terminal and tmux scrollback buffers. Shows how to tweak copy mode, scroll, and mouse selection tmux behavior.

**Part 4.** [tmux in practice: integration with system clipboard](https://medium.com/@alexeysamoshkin/tmux-in-practice-integration-with-system-clipboard-bcd72c62ff7b). Builds a bridge between the tmux copy buffer and system clipboard, to store selected text on OSX or Linux system clipboard in a way that addresses both local and remote usage scenarios.

**Part 5.** [tmux in practice: copy text from remote session using SSH remote tunnel and systemd service](https://medium.com/@alexeysamoshkin/tmux-in-practice-copy-text-from-remote-session-using-ssh-remote-tunnel-and-systemd-service-dd3c51bca1fa). Yet another way to copy text from remote session into local clipboard.

Everything discussed here you can see in action by checking my tmux Configuration project on Github: [tmux-config](https://github.com/samoshkin/tmux-config)

