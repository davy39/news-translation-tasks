---
title: Git Log Command Explained
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T00:20:00.000Z'
originalURL: https://freecodecamp.org/news/git-log-command
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dfc740569d1a4ca3abd.jpg
tags:
- name: Git
  slug: git
seo_title: null
seo_desc: 'What does git log do?

  The git log command displays all of the commits in a repository’s history.

  By default, the command displays each commit’s:


  Secure Hash Algorithm (SHA)

  author

  date

  commit message


  Navigating Git Log

  Git uses the Less terminal pa...'
---

## **What does git log do?**

The `git log` command displays all of the commits in a repository’s history.

By default, the command displays each commit’s:

* Secure Hash Algorithm (SHA)
* author
* date
* commit message

## Navigating Git Log

Git uses the Less terminal pager to page through the commit history. You can navigate it with the following commands:

* to scroll down by one line, use j or ↓
* to scroll up by one line, use k or ↑
* to scroll down by one page, use the spacebar or the Page Down button
* to scroll up by one page, use b or the Page Up button
* to quit the log, use q

## Git Log Flags

You can customize the information presented by `git log` using flags.

### --oneline

`git log --oneline`

The `--oneline` flag causes `git log` to display

* one commit per line
* the first seven characters of the SHA
* the commit message

### --stat

`git log --stat`

The `--stat` flag causes `git log` to display

* the files that were modified in each commit
* the number of lines added or removed
* a summary line with the total number of files and lines changed

### --patch or -p

`git log --patch`

or, the shorter version

`git log -p`

The `--patch` flag causes `git log` to display

* the files that you modified
* the location of the lines that you added or removed
* the specific changes that you made

## View specified number of commits by author

To view a specified number of commits by an author to the current repo (optionally in a prettified format), the following command can be used

`git log --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" -n {NUMBER_OF_COMMITS} --author="{AUTHOR_NAME}" --all`

### Start at a specific commit

To start `git log` at a specific commit, add the SHA:

`git log 7752b22`

This will display the commit with the SHA 7752b22 and all of the commits made before that commit. You can combine this with any of the other flags.

### --graph

`git log --graph`

The `--graph` flag enables you to view your `git log` as a graph. To make things things interesting, you can combine this command with `--oneline` option you learned from above.

`git log --graph --oneline`

The output would be similar to,

```text
* 64e6db0 Update index.md
* b592012 Update Python articles (#5030)
* ecbf9d3 Add latest version and remove duplicate link (#8860)
* 7e3934b Add hint for Compose React Components (#8705)
* 99b7758 Added more frameworks (#8842)
* c4e6a84 Add hint for "Create a Component with Composition" (#8704)
*   907b004 Merge branch 'master' of github.com:freeCodeCamp/guide
|\  
| * 275b6d1 Update index.md
* |   cb74308 Merge branch 'dogb3rt-patch-3'
|\ \  
| |/  
|/|   
| *   98015b6 fix merge conflicts after folder renaming
| |\  
|/ /  
| * fa83460 Update index.md
* | 6afb3b5 rename illegally formatted folder name (#8762)
* | 64b1fe4 CSS3: border-radius property (#8803)
```

One of the benefit of using this command is that it enables you to get a overview of how commits have merged and how the git history was created.

There are may other options you could use in combination with `--graph`. Couple of them are `--decorate` and `--all`. Make sure to try these out too. And you can refer to the [documentation](https://git-scm.com/docs/git-log) for more helpful info.

### More Information:

* [Git Basics - Viewing the Commit History](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History)
* [Git Log](https://git-scm.com/docs/git-log)

## **Other Resources on Git** 

* [Git Checkout](https://www.freecodecamp.org/news/git-checkout-explained/)
* [Git Commit](https://www.freecodecamp.org/news/git-commit-command-explained/)
* [Git Stash](https://www.freecodecamp.org/news/git-stash-explained/)
* [Git Branch](https://www.freecodecamp.org/news/git-delete-branch-how-to-remove-a-local-or-remote-branch/)

