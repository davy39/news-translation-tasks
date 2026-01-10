---
title: How to avoid committing junk
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-21T21:47:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-committing-junk-dae1277c1433
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ti1Iue11tP3DoOoVDFLZMg.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'By Yoel Zeldes

  In the development process, every developer writes stuff they don’t intend to commit
  and push to the remote server, things like debug prints. It happens to all of us
  every now and then: we forget to remove this temporary stuff before c...'
---

By Yoel Zeldes

In the development process, every developer writes stuff they don’t intend to commit and push to the remote server, things like debug prints. It happens to all of us every now and then: we forget to remove this temporary stuff before committing…

I solved this somewhat embarrassing situation using a simple approach: to every line I don’t want to accidentally commit, I add the magic characters sequence `xxx`. This sequence can be in any part of the line: inside a comment, as a variable name, as a function name, you name it. A few usage examples:

* debug print: `print 'xxx reached this line'`.
* variable used for debugging: `xxx_counter = 0`.
* temporary function: `def xxx_print_debug_info():`.
* TODO which must be attended before committing: `#TODO: don't forget to refactor this function xxx`.

I implemented it using Git hooks. A hook is Git’s mechanism to fire off custom scripts when certain important actions occur. I used the pre-commit hook for validating the commit’s content.

Just create a file with the name `<YOUR-REPO-FOLDER>/.git/hooks/pre-`commit with the following content:

```
#!/bin/sh
```

```
marks=xxx,aaamarksRegex=`echo "($marks)" | sed -r 's/,/|/g'`marksMessage=`echo "$marks" | sed -r 's/,/ or /g'`if git diff --staged | egrep -q "^\+.*$marksRegex"; then    echo "you forgot to remove a line containing $marksMessage!"    echo "you can forcefully commit using \"commit -n\""    exit 1fi
```

1. `marks` contains the characters sequences which are not allowed to be committed.
2. `git diff --staged` shows the changes which will be committed. The changes are passed to a regular expression that searches for any forbidden mark (using `egrep`).
3. If a forbidden mark is found, the script exits with an error code, causing the commit to fail.

You want to bypass the hook? Execute`commit -n`. This can be useful when you want to commit a binary file such as an image, which may contain a forbidden mark.

Any tricks you’ve implemented in your daily git workflow? Share your magic in the comments :)

_This post was originally posted by me at [www.anotherdatum.com](http://www.anotherdatum.com)._

