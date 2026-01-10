---
title: 'ABS 1.2: background commands & the ability to import files'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T19:13:17.000Z'
originalURL: https://freecodecamp.org/news/abs-1-2-background-commands-the-ability-to-import-files-e5d1e046cb35
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ph8ChGDlQ8vqoWTp.png
tags:
- name: Bash
  slug: bash
- name: General Programming
  slug: programming
- name: Scripting
  slug: scripting
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Alex Nadalin

  ABS is a programming language that puts together the productivity of bash scripts
  with the elegance of high-level languages such as Python or Ruby. It lets you issue
  system commands by simply wrapping them in backticks (very similar t...'
---

By Alex Nadalin

[ABS](https://www.abs-lang.org/) is a programming language that puts together the productivity of bash scripts with the elegance of high-level languages such as Python or Ruby. It lets you issue system commands by simply wrapping them in backticks (very similar to how you would do it in Bash) and lets you use their output with clear and concise syntax.

This is, for example, a script that would try to issue a `curl` command, and exit if the server at `example.org` would not reply within 10 seconds:

![Image](https://cdn-media-1.freecodecamp.org/images/dSVYyySoZGbfUcDXgDVHZ674fUKRRG5GGL8n)

A few weeks ago the [ABS team](https://github.com/abs-lang/abs) managed to pull together a new minor release of the language, [1.2.0](https://github.com/abs-lang/abs/releases/tag/1.2.0), which includes loads of interesting features — let’s get to them!

### ~/.absrc

ABS will now look for a default `~/.absrc` file to preload every time you run a script. This is especially useful if you’d like to dump “base” functions you’re likely to re-use across scripts in a common place. Your `.absrc` could look like:

```
tenth = f(x) {   return x / 10 }
```

so that in any other abs script you can `tenth(x)`.

### ~/.abs_history

We also introduced an history file in order to be able to repeat commands easily when using the ABS repl. This is, by default, located at `~/.abs_history` and gets synced every time you close a repl session:

```
$ absHello alex, welcome to the ABS (1.2.0) programming language!Type 'quit' when you're done, 'help' if you get lost!⧐  `sleep 1`
```

```
⧐  quitAdios!$ tail ~/.abs_history`sleep 1`
```

### require(file)

A big one here: you can now **require external files** through `require(path/to/file.abs )`.

This is a stepping stone that allows creating base libraries that can be re-used across ABS scripts, and organizes ABS code a tad better.

### Background commands

Another big feature here: you can now issue “background” commands that won’t block your ABS script (these commands are executed within a [Goroutine](https://tour.golang.org/concurrency/1)).

A background command differs from a regular one simply because it employs an `&` at the end of the command itself — let’s see them in action:

```
`sleep 10`echo("Hello world!") # This will be printed after 10s
```

```
`sleep 10 &`echo("Hello world!") # This will be printed immediately
```

You can check whether a background command is done with the `.done` property:

```
cmd = `sleep 10 &`cmd.done # falsewait(10000)cmd.done # true
```

and we’ve added the `wait()` function if you need to block until the command is done:

```
cmd = `sleep 10 &`cmd.wait() # The script will be blocked for 10secho("Hello world!")
```

### Misc

A few more features that made it into this release:

* number functions such as `floor`, `round` and `ceil`
* `cd()`, which switches the `cwd` of a script
* you can play around with your prompt by setting the environment variables `ABS_PROMPT_LIVE_PREFIX=true` and `ABS_PROMPT_PREFIX=templated_string`. The templated string can use `{dir}`, `{user}`, `{host}` that will be replaced on-the-fly. For further info, have a look at the sample [.absrc](https://github.com/abs-lang/abs/blob/d1e92899ed0d6b3abb7a0a3fc6ec18d13dbe3ff2/tests/test-absrc.abs) file

### Bugfixes

As usual, we managed to fix some minor bugs along the way:

* fixed a few random panics when calling built-in functions without enough arguments ([#193](https://github.com/abs-lang/abs/pull/193))
* windows commands are now using cmd.exe rather than bash, as bash might not be available on the system ([#180](https://github.com/abs-lang/abs/pull/180))
* better error messages when parsing “invalid” numbers ([#182](https://github.com/abs-lang/abs/pull/182))
* the ABS installer was not working with wget 1.20.1 ([#178](https://github.com/abs-lang/abs/pull/178))
* the ABS parser now supports numbers in scientific notation (eg. 8.366100560806463e-7, [#174](https://github.com/abs-lang/abs/pull/174))
* errors on built-in functions would not report the correct error line / column numbers ([#168](https://github.com/abs-lang/abs/pull/168))

### Now what?

Install ABS with a simple one-liner:

```
bash <(curl https://www.abs-lang.org/installer.sh)
```

…and start scripting like it’s 2019!

PS: Again, many thanks to [Erich](https://github.com/ntwrick), who’s been taking a larger role as the weeks went by. Without him, many of the stuff included in 1.2 wouldn’t be possible!

PPS: [1.3.0 is already well underway](https://github.com/abs-lang/abs/milestone/10) — expect it at some point in April. We’ll be introducing extremely interesting features such as the ability to kill background commands, so it’s going to be an exciting release!

_Originally published at [odino.org](https://odino.org/abs-1-dot-2-background-commands-and-the-ability-to-import-files/) (21st March 2019)._  
_You can follow me on [Twitter](https://twitter.com/_odino_) — rants are welcome!_ ?

