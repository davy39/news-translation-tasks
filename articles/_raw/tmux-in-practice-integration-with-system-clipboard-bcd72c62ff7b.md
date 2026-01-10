---
title: 'tmux in practice: integration with system clipboard'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-27T11:13:55.000Z'
originalURL: https://freecodecamp.org/news/tmux-in-practice-integration-with-system-clipboard-bcd72c62ff7b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gGNWXlll62GCAM55hbldbw.png
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

  How to build a bridge between tmux copy buffer and system clipboard, and to store
  selected text on OSX or Linux system clipboard, in a way that address both local
  and remote usage scenarios

  This is the 4th part of my tmux in pract...'
---

By Alexey Samoshkin

#### How to build a bridge between tmux copy buffer and system clipboard, and to store selected text on OSX or Linux system clipboard, in a way that address both local and remote usage scenarios

This is the 4th part of my [tmux in practice](https://medium.com/@alexeysamoshkin/tmux-in-practice-series-of-posts-ae34f16cfab0) article series.

![Image](https://cdn-media-1.freecodecamp.org/images/hLvVwjePtz6ORxA6S5mKvdVTsoysRvgDtLA7)
_You can copy text from local or remote, or even nested remote session to your system clipboard_

In the [previous part of “tmux in practice”](https://medium.com/@alexeysamoshkin/tmux-in-practice-scrollback-buffer-47d5ffa71c93) series we talked about things like scrollback buffer, copy mode, and slightly touched on the topic of copying text into tmux’s copy buffer.

Sooner or later you’ll realize that whatever you copy in tmux gets stored in tmux’s copy buffer only, but not shared with system clipboard. Copying and pasting are such common operations, that this limitation is itself enough to turn tmux into a useless brick, despite other goodies.

In this post we’ll explore how to build a bridge between the tmux copy buffer and system clipboard, to store copied text on system clipboard, in a way that address both local and remote usage scenarios.

**We’ll discuss following techniques:**

1. OSX only, share text with clipboard using “pbcopy”
2. OSX only, using “reattach-to-user-namespace” wrapper to make pbcopy work properly inside tmux environment
3. Linux only, share text with X selection using `xclip` or `xsel` commands

Techniques above address only local scenarios.   
**To support remote scenarios there are 2 extra methods:**

1. Use the [ANSI OSC 52](https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences) escape [sequence](https://blog.vucica.net/2017/07/what-are-osc-terminal-control-sequences-escape-codes.html) to talk to controlling/parent terminal to manage and store text on a clipboard of a local machine.
2. Setup a local network listener which pipes input to `pbcopy` or `xclip`or `xsel`. Pipe copied selected text from remote machine to a listener on the local machine through SSH remote tunneling. This is rather involved, and I will devote a dedicated post to describe it.

### OSX. pbcopy and pbpaste commands

`pbcopy` and `pbpaste` commands allow you to interact and manipulate system clipboard from command line.

`pbcopy` reads data from `stdin` and stores it in the clipboard. `pbpaste` does the opposite and puts copied text on `stdout`.

The idea is to hook into various tmux commands, that manage to copy text while in copy mode.

Let’s list them:

```
$ tmux -f /dev/null list-keys -T copy-mode-vi
```

```
bind-key -T copy-mode-vi Enter send-keys -X copy-selection-and-cancelbind-key -T copy-mode-vi C-j send-keys -X copy-selection-and-cancelbind-key -T copy-mode-vi D send-keys -X copy-end-of-linebind-key -T copy-mode-vi MouseDragEnd1Pane send-keys -X copy-selection-and-cancelbind-key -T copy-mode-vi A send-keys -X append-selection-and-cancel
```

`copy-selection-and-cancel` and `copy-end-of-line` are special tmux commands which tmux understand when pane is in copy mode. There are two flavors of copy command: `copy-selection` and `copy-pipe`.

Let’s rewrite `Enter` keybinding with copy-pipe command:

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "pbcopy"
```

`copy-pipe` command stores selected text in tmux buffer same to `copy-selection`, plus pipes selected text to the given command `pbcopy`. So we get text stored in two places: the tmux copy buffer and the system clipboard.

### OSX. reattach-to-user-namespace wrapper

So far so good. However, on some versions of OSX, `pbcopy` and `pbpaste` fail to function properly when run under tmux.

Read [more details](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard#interaction-with-tmux) from Chris Johnsen on why it happens:

> tmux uses the daemon(3) library function when starting its server process. In Mac OS X 10.5, Apple changed daemon(3) to move the resulting process from its original bootstrap namespace to the root bootstrap namespace. This means that the tmux server, and its children, will automatically and uncontrollably lose access to what would have been their original bootstrap namespace (i.e. the one that has access to the pasteboard service).

A common solution is to use [reattach-to-user-namespace](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard) wrapper. This allows us to launch a process and have that process be attached to the per-user bootstrap namespace, which makes the program behave as we are expecting. You need to change keybinding properly:

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel “reattach-to-user-namespace pbcopy”
```

Plus, you would need to tell tmux to run your shell (bash, zsh, …) inside a wrapper, by setting `default-command` option:

```
if -b "command -v reattach-to-user-namespace > /dev/null 2>&1" \    "run 'tmux set -g default-command \"exec $(tmux show -gv default-shell) 2>/dev/null & reattach-to-user-namespace -l $(tmux show -gv default-shell)\"'"
```

**Note**: some OSX versions works fine even without this hack (OSX 10.11.5 El Capitan), whereas OSX Sierra users [report this hack is still needed](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard/issues/56).

### Linux. Interact with X selection via xclip and xsel

We can make use of `xclip` or `xsel` commands on Linux to store text in the clipboard, same as `pbcopy` on OSX. On Linux, there are [several kinds of clipboard selections](https://wiki.archlinux.org/index.php/Clipboard) maintained by X server: primary, secondary and clipboard. We only concern with primary and clipboard. Secondary was intended as an alternate to primary.

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "xclip -i -f -selection primary | xclip -i -selection clipboard"
```

Or when using `xsel`:

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "xsel -i --clipboard"
```

[Read here](https://askubuntu.com/questions/705620/xclip-vs-xsel) about comparison of `xclip` vs. `xsel`, if you’re curious. Also, check out [this post on `xclip` usage and examples](https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/). And don’t forget to install one of these utilities, as they might not be a part of your distribution.

### Using ANSI OSC 52 escape sequence to cause terminal to store text in the clipboard

So far we covered only local scenarios. When you SSH to remote machine, and start tmux sessions there, you cannot make use of `pbcopy`, `xclip` or `xsel`, because text will be stored in the remote machine’s clipboard, not in your local one. You need some way to transport copied text to your local machine’s clipboard.

[ANSI escape sequence](https://en.wikipedia.org/wiki/ANSI_escape_code) is a sequence of bytes sent to the terminal that are interleaved with regular printable characters, and are used to control various terminal aspects: such as text colors, cursor position, text effects, clearing screen. The terminal is capable of detecting such controlling sequence of bytes that causes it to trigger specific actions and not print those characters to the output.

The ANSI escape sequence can be detected as they start with `ESC` ASCII character (0x1b hex, 027 decimal, \033 in octal). For example, when the terminal sees the `\033[2A` sequence, it will move the cursor position 2 lines up.

There are [really](http://ascii-table.com/ansi-escape-sequences.php) [a lot](https://www.xfree86.org/4.8.0/ctlseqs.html) of those known sequences. Some of them are the same across different terminal types, while others can vary and be very specific to your terminal emulator. Use`infocmp` command to query `terminfo` database for escape sequences supported by different types of terminals.

Okay great, but how can it help us regarding the clipboard? It turns out that there is a special category of escape sequences: “Operating System Controls” (OSC) and the “OSC 52" escape sequence, which allows applications to interact with the clipboard.

If you’re using iTerm, try to execute following command, and then “`⌘V`” to see contents of system clipboard. Make sure to turn on OSC 52 escape sequence handling: “Preferences -> General -> Applications in terminal may access clipboard”.

```
printf "\033]52;c;$(printf "%s" "blabla" | base64)\a"
```

The conclusion is that we can store text in the system clipboard by sending a specially crafted ANSI escape sequence to our terminal.

Let’s write the shell script `yank.sh`:

```
#!/bin/bash
```

```
set -eu
```

```
# get data either form stdin or from filebuf=$(cat "$@")
```

```
# Get buffer lengthbuflen=$( printf %s "$buf" | wc -c )
```

```
maxlen=74994
```

```
# warn if exceeds maxlenif [ "$buflen" -gt "$maxlen" ]; then   printf "input is %d bytes too long" "$(( buflen - maxlen ))" >&2fi
```

```
# build up OSC 52 ANSI escape sequenceesc="\033]52;c;$( printf %s "$buf" | head -c $maxlen | base64 | tr -d '\r\n' )\a"
```

So, we read text to copy from `stdin`, then check if it’s length exceeds the maximum length of 74994 bytes. If true, we crop it, and finally convert data to base64 and wrap in OSC 52 escape sequence: `\033]53;c;${data_in_base64}\a`

Then let’s wire it with our tmux keybindings. That’s pretty easy: just pipe the selected text to our `yank.sh` script, just as we pipe it to `pbcopy` or `xclip`.

```
yank="~/.tmux/yank.sh"
```

```
bind -T copy-mode-vi Enter send-keys -X copy-pipe-and-cancel "$yank"
```

However, there is one piece left to complete the puzzle. Where should we send the escape sequence? Apparently, just sending it to `stdout` won’t work. The target should be our parent terminal emulator, but we don’t know the right `tty`. So, we’re going to send it to tmux’s active pane `tty`, and tell tmux to further resend it to the parent terminal emulator:

```
# build up OSC 52 ANSI escape sequenceesc="\033]52;c;$( printf %s "$buf" | head -c $maxlen | base64 | tr -d '\r\n' )\a"esc="\033Ptmux;\033$esc\033\\"
```

```
pane_active_tty=$(tmux list-panes -F "#{pane_active} #{pane_tty}" | awk '$1=="1" { print $2 }')
```

```
printf "$esc" > "$pane_active_tty"
```

We use `tmux list-panes` command to query for the active pane and it’s `tty`. We also put our OSC 52 sequence in an additional wrapper escape sequence (Device Control String, ESC P), so tmux unwraps this envelope and passes OSC 52 to parent terminal.

In newer versions of tmux, you can tell tmux to handle interactions with the clipboard for you. See`set-clipboard` tmux option. `on` — tmux will create an inner buffer and attempt to set the terminal clipboard using OSC 52. `external` — do not create a buffer, but still attempt to set the terminal clipboard.

Just make sure it’s either `external` or `on`:

```
set -g set-clipboard on
```

So, if tmux is already capable of this feature, why we need to bother ourselves with manual wiring OSC 52 stuff? That’s because `set-clipboard` does not work when you have a remote tmux session nested in a local one. And it only works in those [terminals which supports OSC 52 escape sequence handling](https://askubuntu.com/questions/621522/use-tmux-set-clipboard-in-gnome-terminal-xterms-disallowedwindowops/621646).

The trick for nested remote sessions is to bypass the remote session and send our OSC 52 escape sequence directly to the local session, so it hits our local terminal emulator (iTerm).

Use `$SSH_TTY` for this purpose:

```
# resolve target terminal to send escape sequence# if we are on remote machine, send directly to SSH_TTY to transport escape sequence# to terminal on local machine, so data lands in clipboard on our local machinepane_active_tty=$(tmux list-panes -F "#{pane_active} #{pane_tty}" | awk '$1=="1" { print $2 }')target_tty="${SSH_TTY:-$pane_active_tty}"
```

```
printf "$esc" > "$target_tty"
```

That’s it. Now we have a completely working solution, be it a local session, remote or both, nested in each other. [Credits to this great post](https://sunaku.github.io/tmux-yank-osc52.html), where I first read about this approach.

The major drawback of using OSC escape sequences,is that despite being declared in spec, only a few terminals support this in practice: iTerm and xterm do, whereas OSX Terminal, Terminator, and Gnome terminal does not. So, an otherwise great solution (especially in remote scenarios, when you cannot just `pipe` to `xclip` or `pbcopy`) lacks wider terminal support.

You might want to [checkout complete version](https://github.com/samoshkin/tmux-config/blob/af2efd9561f41f30c51c9deeeab9451308c4086b/tmux/yank.sh) of `yank.sh` script.

There is yet another solution to support remote scenarios, which is rather crazy, and I’ll describe it in another [dedicated post](https://medium.com/@alexeysamoshkin/tmux-in-practice-copy-text-from-remote-session-using-ssh-remote-tunnel-and-systemd-service-dd3c51bca1fa). The idea is to setup a local network listener which pipes input to `pbcopy` or `xclip`or `xsel;` and pipes copied selected text from a remote machine to a listener on the local machine through SSH remote tunneling. Stay tuned.

### Resources and links

ANSI escape code — Wikipedia — [https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences](https://en.wikipedia.org/wiki/ANSI_escape_code#Escape_sequences)

What are OSC terminal control sequences / escape codes? | ivucica blog — [https://blog.vucica.net/2017/07/what-are-osc-terminal-control-sequences-escape-codes.html](https://blog.vucica.net/2017/07/what-are-osc-terminal-control-sequences-escape-codes.html)

Copying to clipboard from tmux and Vim using OSC 52 — The Terminal Programmer — [https://sunaku.github.io/tmux-yank-osc52.html](https://sunaku.github.io/tmux-yank-osc52.html)

Copy Shell Prompt Output To Linux / UNIX X Clipboard Directly — nixCraft — [https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/](https://www.cyberciti.biz/faq/xclip-linux-insert-files-command-output-intoclipboard/)

software recommendation — ‘xclip’ vs. ‘xsel’ — Ask Ubuntu — [https://askubuntu.com/questions/705620/xclip-vs-xsel](https://askubuntu.com/questions/705620/xclip-vs-xsel)

Everything you need to know about Tmux copy paste · rushiagr — [http://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting/](http://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting/)

macos — Synchronize pasteboard between remote tmux session and local Mac OS pasteboard — Super User — [https://superuser.com/questions/407888/synchronize-pasteboard-between-remote-tmux-session-and-local-mac-os-pasteboard/408374#408374](https://superuser.com/questions/407888/synchronize-pasteboard-between-remote-tmux-session-and-local-mac-os-pasteboard/408374#408374)

linux — Getting Items on the Local Clipboard from a Remote SSH Session — Stack Overflow — [https://stackoverflow.com/questions/1152362/getting-items-on-the-local-clipboard-from-a-remote-ssh-session](https://stackoverflow.com/questions/1152362/getting-items-on-the-local-clipboard-from-a-remote-ssh-session)

Use tmux set-clipboard in gnome-terminal (XTerm’s disallowedWindowOps) — Ask Ubuntu — [https://askubuntu.com/questions/621522/use-tmux-set-clipboard-in-gnome-terminal-xterms-disallowedwindowops/621646](https://askubuntu.com/questions/621522/use-tmux-set-clipboard-in-gnome-terminal-xterms-disallowedwindowops/621646)

