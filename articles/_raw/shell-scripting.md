---
title: Shell scripting
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-07T18:16:00.000Z'
originalURL: https://freecodecamp.org/news/shell-scripting
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e14740569d1a4ca3b3b.jpg
tags:
- name: command line
  slug: command-line
- name: shell script
  slug: shell-script
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: In the command line, a shell script is an executable file that contains
  a set of instructions that the shell will execute. Its main purpose is to reduce
  a set of instructions (or commands) in just one file. Also it can handle some logic
  because it’s ...
---

In the command line, a shell script is an executable file that contains a set of instructions that the shell will execute. Its main purpose is to reduce a set of instructions (or commands) in just one file. Also it can handle some logic because it’s a programming language.

## **How to create it**

Create the file:

```bash
$ touch myscript.sh
```

Add a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) at the start of the file. The Shebang line is responsible for letting the command interpreter know which interpreter the shell script will be run with:

```bash
$ echo "#!/bin/bash" > myscript.sh
# or
$ your-desired-editor myscript.sh
# write at the first line #!/bin/bash
```

Add some commands:

```bash
$ echo "echo Hello World!" >> myscript.sh
```

Give the file _execution_ mode:

```bash
$ chmod +x myscript.sh
```

Execute it!

```bash
$ ./myscript.sh
Hello World!
```

More info about shell-scripting can be found [here](https://www.shellscript.sh/)

## More info on shell scripting and Linux:

* [A beginner's guide to surviving in the Linux shell](https://www.freecodecamp.org/news/a-beginners-guide-to-surviving-in-the-linux-shell-cda0f5a0698c/)
* [Basic Linux commands to know](https://guide.freecodecamp.org/linux/basic-linux-commands)
* [Shell scripting tricks](https://www.freecodecamp.org/news/functional-and-flexible-shell-scripting-tricks-a2d693be2dd4/)


