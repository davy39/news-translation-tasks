---
title: How to Understand and Solve Conflicts in Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-24T18:55:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-merge-conflicts-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/header-image@1000x420.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'By Tobias Günther

  There it is, the word that every developer hates to see: conflict. 😱 There''s just
  no way around the occasional merge conflict when working with Git (or other version
  control systems).

  But when speaking with developers, I often hear...'
---

By Tobias Günther

There it is, the word that every developer hates to see: **conflict.** 😱 There's just no way around the occasional merge conflict when working with Git (or other version control systems).

But when speaking with developers, I often hear that there's a sense of _anxiety_ or _discomfort_ around the topic of merge conflicts. 

Handling conflicts often remains a dark, mysterious place: a situation where things are badly broken and it's unclear how to get out of it (without making things worse).

While it's true that merge conflicts are an unavoidable part of a developer's life, the discomfort in these situations is fully optional. 

My intention with this article is to bring some clarity to this topic: how and when conflicts typically occur, what they actually are, and how to solve - or undo - them.

When you properly understand these things, you'll be able to deal with merge conflicts in a much more relaxed and confident way. 😍

## How and When Conflicts Occur

The name already says it: "merge conflicts" can occur in the process of integrating commits from a different source.

Keep in mind, though, that "integration" is not limited to only "merging branches". It can also happen when rebasing or interactive rebasing, when performing a cherry-pick or a pull, or even when reapplying a Stash. 

All of these actions perform some kind of integration - and that's when merge conflicts can happen.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/situations-where-conflicts-can-happen-1.png)

But of course, these actions don't result in a merge conflict _every time_ (thank God!). Ideally, you should find yourself in these situations only rarely. _But when exactly do conflicts occur?_

Actually, Git's merging capabilities are one of its greatest advantages: merging branches works effortlessly most of the time, because Git is usually able to figure things out on its own. 

But there are situations where **contradictory changes** were made - and where technology simply _cannot_ decide what's right or wrong. These situations simply require a decision from a human being.

The true classic is when the _exact same line of code_ was changed in two commits, on two different branches. Git has no way of knowing which change you prefer! 🤔

There are some other, similar situations - for example when a file was _modified_ in one branch and _deleted_ in another one - but they are a bit less common.

The [**"Tower" Git desktop GUI**](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=understand-and-solve-conflicts), for example, has a nice way of visualizing these kinds of situations:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tower-conflict-wizard-1.png)

## How to Know When a Conflict Has Occurred

Don't worry: Git will tell you very clearly when a conflict has happened. 😉  

First, it will let you know _immediately in the situation_, for example when a merge or rebase fails due to a conflict:

```git on cli
$ git merge develop
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
CONFLICT (modify/delete): error.html deleted in HEAD and modified in develop. Version develop of error.html left in tree.
Automatic merge failed; fix conflicts and then commit the result.
```

As you can see from the above example, when I tried to perform a merge, I created a merge conflict - and Git communicates the problem very clearly and promptly:

* A conflict in the file "index.html" occurred.
* Another conflict in the file "error.html" occurred.
* And finally, because of the conflicts, the merge operation failed.

These are the situations where we have to dig into the code and see what has to be done.

In the unlikely event that you have overlooked these warning messages when the conflict happened, Git additionally informs you whenever you run `git status`:

```git on cli
$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add/rm <file>..." as appropriate to mark resolution)
	deleted by us:   error.html
	both modified:   index.html
```

In other words: don't worry about _not noticing_ merge conflicts. Git makes sure you can't overlook them.

## How to Undo a Conflict in Git and Start Over

Merge conflicts come with a certain air of urgency. And rightfully so: you'll have to deal with them before you can go on with your work. 

But although ignoring them is not an option, "dealing with merge conflicts" doesn't necessarily mean you have to resolve them. **Undoing** them is also possible!

This might be worth repeating: **you always have the option to undo a merge conflict and return to the state before.** This is true even when you've already started resolving the conflicted files and find yourself in a dead end. 

In these situations, it's great to keep in mind that you can always start over and return to a clean state before the conflict even happened.

For this purpose, most commands come with an `--abort` option, for example `git merge --abort` and `git rebase --abort`:

```git on cli
$ git merge --abort
$ git status
On branch main
nothing to commit, working tree clean
```

This should give you the confidence that **you really cannot mess up.** You can always abort, return to a clean state, and start over.

## What Conflicts Really Look Like in Git

Now, safe in the knowledge that nothing can break, let's see what a conflict _really looks like_ under the hood. This will demystify those little buggers and, at the same time, help you lose respect for them and gain confidence in yourself.

As an example, let's look at the contents of the (currently conflicted) "index.html" file in an editor:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/contents-of-conflicted-file-1.png)

Git was kind enough to mark the problem area in the file, enclosing it in `<<<<<<< HEAD` and `>>>>>>> [other/branch/name]`. The content that comes after the first marker originates from our current working branch. Finally, a line with `=======` characters separates the two conflicting changes.

## How to Solve a Conflict in Git

Our job as developers now is to clean up these lines: after we're finished, the file has to look exactly as we want it to look. 

It might be necessary to talk to the teammate who wrote the "other" changes and decide which code is actually correct. Maybe it's ours, maybe it's theirs - or maybe a mixture between the two.

This process - cleaning up the file and making sure it contains what we actually want - doesn't have to involve any magic. You can do this simply by opening your text editor or IDE and starting to making your changes.

Often, however, you'll find that this is not the most efficient way. That's when dedicated tools can save time and effort:

* **Git GUI Tools:** Some of the graphical user interfaces for Git can be helpful when solving conflicts. The [**Tower Git GUI**](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=understand-and-solve-conflicts), for example, offers a dedicated "Conflict Wizard" that helps visualize and solve the situation:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tower-conflict-wizard-in-action-1.gif)

* **Dedicated Merge Tools:** For more complicated conflicts, it can be great to have a dedicated "Diff & Merge Tool" at hand. You can configure your tool of choice using the "git config" command. (Consult your tool's documentation for detailed instructions.) Then, in case of a conflict, you can invoke it by simply typing `git mergetool`. As an example, here's a screenshot of "[**Kaleidoscope**](https://www.kaleidoscopeapp.com)" on macOS:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/merge-conflict-in-gui-1.jpg)

After cleaning up the file - either manually or in a Git GUI or Merge Tool - we have to commit this like any other change:

* By using `git add <filename>` on the (previously) conflicted file, we inform Git that the conflict has been solved.
* When all conflicts have been solved and added to the Staging Area, you need to complete the resolution by creating a regular commit.

## How to Become More Confident and Productive

Many years ago, when I started using version control, merge conflicts regularly freaked me out: I was afraid that, finally, I had managed to break things for good. 😩 

Only when I took the time to truly understand what was going on under the hood was I able to deal with conflicts confidently and efficiently.

The same was true, for example, when dealing with mistakes: only once I learned **how to undo mistakes with Git** was I able to become more confident and productive in my work. 

I highly recommend taking a look at the free "[**First Aid Kit for Git**](https://www.git-tower.com/learn/git/first-aid-kit?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=understand-and-solve-conflicts)", a collection of short videos about how to undo and recover from mistakes with Git.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/first-aid-kit-3.png)

Have fun becoming a better programmer!

## About the Author

[Tobias Günther](https://twitter.com/gntr) is the CEO of [Tower](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=understand-and-solve-conflicts), the popular Git desktop client that helps more than 100,000 developers around the world to be more productive with Git.

