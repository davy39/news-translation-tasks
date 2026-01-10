---
title: 'Makefiles 101: how to use make as a task automation tool'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-21T18:23:11.000Z'
originalURL: https://freecodecamp.org/news/makefiles-101-how-to-use-make-as-a-task-automation-tool-69d2ccc3f25e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aOVtsK7VBpDnR71WlBuHOg.jpeg
tags:
- name: automation
  slug: automation
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Alex Nadalin

  It seems like developers are afraid of using make as they associate it with the
  painful experience of compiling things from scratch — the dreaded ./configure &&
  make && make install.

  Part of this fear is due to the description of what...'
---

By Alex Nadalin

It seems like developers are afraid of using `make` as they associate it with the painful experience of compiling things from scratch — the dreaded `./configure && make && make install`.

Part of this fear is due to the description of what [make(1)](https://linux.die.net/man/1/make) does:

> _The purpose of the make utility is to determine automatically which pieces of a large program need to be recompiled, and issue the commands to recompile them._

> **_Free Software Foundation_** [The Linux Man Pages](https://linux.die.net/man/1/make)

Not everyone is aware that make can easily be used to manage tasks in your projects. In this article, I’d like to share a brief introduction to how [Makefiles help me automate some tasks](https://github.com/odino/mssqldump/blob/master/Makefile) in my day to day activities. This brief guide will focus on using make as an automation tool for tasks rather than a tool for compiling code.

### Executing tasks

Let’s start by simply creating a `Makefile`, and defining a task to run:

```
task:
  date
```

If you run `make task` you will bump into the following error:

```
/tmp ᐅ make task
Makefile:2: *** missing separator.  Stop.
```

And that’s because Makefiles use tabs to indent code. Let’s update our example by using tabs rather than spaces and… Voilà.

```
/tmp ᐅ make task
date
Fri Jun 15 08:34:15 +04 2018
```

What kind of sorcery is this? Well, `make` understood you wanted to run the section `task` of your makefile, and ran the code (`date`) within that section in a shell, outputting both the command and its output. If you want to skip outputting the command that’s being executed, you can simply prefix it with an `@` sign:

```
task:
  @date
```

Running the make command again:

```
/tmp ᐅ make task
Fri Jun 15 08:34:15 +04 2018
```

The first task in a `Makefile` is the **default** one, meaning that we can run `make` without any arguments:

```
/tmp ᐅ make       
Fri Jun 15 08:37:11 +04 2018
```

### Running additional tasks

You can add additional tasks in your `Makefile` and call them with `make $TASK`:

```
task:
  @date
some:
  sleep 1
  echo "Slept"
thing:
  cal
```

Running the make command again:

```
/tmp ᐅ make thing
cal
     June 2018        
Su Mo Tu We Th Fr Sa  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30
```

### Running tasks in a specific order

A lot of times you will want to execute a task before the current one. Think of it as `before` or `after` hooks in your automated tests. This can be done by specifying a list of tasks right after your task’s name:

```
task: thing some
  @date
...
```

Running the make command again:

```
/tmp ᐅ make task
cal
     June 2018        
Su Mo Tu We Th Fr Sa  
                1  2  
 3  4  5  6  7  8  9  
10 11 12 13 14 15 16  
17 18 19 20 21 22 23  
24 25 26 27 28 29 30

sleep 1
echo "Slept"
Slept
Fri Jun 15 08:40:23 +04 2018
```

### Using variables with make

Defining and using variables is fairly straightforward:

```
VAR=123

print_var:
        echo ${VAR}
...
```

Running the make command again:

```
/tmp ᐅ make print_var    
echo 123
123
```

But watch out, as your shell variables won’t work out of the box:

```
print_user:
        echo $USER
```

Running the make command again:

```
/tmp ᐅ make print_user   
echo SER
SER
```

You’ll will need to escape them with either `${VAR}` or `$$VAR`.

Passing flags is also a bit different from what you might be used to. They’re positioned as flags but use the same syntax as environment variables:

```
print_foo:
  echo $$FOO
```

Running the make command again:

```
/tmp ᐅ make print_foo
echo $FOO

/tmp ᐅ make print_foo FOO=bar
echo $FOO
bar
```

### Make and the shell

```
5.3.1 Choosing the Shell
------------------------

The program used as the shell is taken from the variable `SHELL'.  If this variable is not set in your makefile, the program `/bin/sh' is used as the shell.
```

Make will use `sh` to execute code in a task. This means that some stuff might not work, as you’re probably using some syntax that’s specific to bash. In order to switch, you can simply specify the `SHELL` variable. In our case, we would want to use `SHELL:=/bin/bash`.

As seen before, sometimes you will need to use a quirky, custom syntax to get a regular shell command to work in `make`. Just like variables need to be escaped with a `$$` or `${...}`, you will need to use `shell` when using [command substitution](http://tldp.org/LDP/abs/html/commandsub.html):

```
subshell:
  echo $(shell echo ${USER})
```

Running the make command again:

```
/tmp ᐅ make subshell
echo alex
alex
```

Don’t believe me? Try removing the `shell` instruction. Here’s what you’re going to get:

```
/tmp ᐅ make subshell
echo
```

### Conclusion

There’s so much more `make` can do, and so many more quirky things you might need to find out to decrease the WPS (WTF per second) when working with it. 😄

That doesn’t negate the fact that `make` is an extremely helpful tool that allows us to automate workflows with ease (without having to setup very complicated pipelines) by writing tab-separated lines with a bunch of shell commands instead.

_Originally published at [odino.org](https://odino.org/makefile-101/) (15th June 2018)._  
_You can follow me on [Twitter](https://twitter.com/_odino_) - rants are welcome!_ 😉

