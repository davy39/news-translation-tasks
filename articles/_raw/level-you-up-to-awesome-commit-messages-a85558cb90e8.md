---
title: How to make your commit messages awesome and keep your team happy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T23:22:17.000Z'
originalURL: https://freecodecamp.org/news/level-you-up-to-awesome-commit-messages-a85558cb90e8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D3L--z7Mx3-LqL9o6sbUgQ.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Bruno

  Commit messages are important means of communication between team members


  What matters most in team software development is communication. Commit messages
  are important means of communication between team members: its past and its future.

  W...'
---

By Bruno

#### Commit messages are important means of communication between team members

![Image](https://cdn-media-1.freecodecamp.org/images/KTwUWqoJVaLxvcNiUMaOupwuWnCGoMkyODUR)

What matters most in team software development is communication. Commit messages are important means of communication between team members: its past and its future.

When analysing the code or debugging, we all have questions like:

* Why is this _if_ here?
* Who forgot to update the branch?
* What impact has this change had?
* How can this change ever fix or improve the code?

To this end, [git-blame](https://git-scm.com/docs/git-blame) allows us to discover which revision was the last to change the file. But just knowing that is not good enough. Would be helpful to actually read the commit message to understand what really happened there.

We need to read the message to experience the real value of a good commit message, and be motivated to write them.

#### Some best practices

So, if the majority of your Git commits so far have been created with something like `git commit -m "9000 — Bug fixes issue"` then next time try this guideline:

> Never use the `-m <m`sg&`gt; / --message`=<msg&`gt; flag t`o git commit.

It gives you a poor mindset right off the bat as you will feel that you have to fit your commit message into the terminal command, and makes the commit feel more like a one-off argument than a page in history.

> The first line should always be [50 characters or less](https://commit.style) and it should be followed by a blank line.

Write an imperative tense: “Fix bug”. [_Add |Fix | Remove| Update| Refactor_] Consistent wording makes it easier to mentally process a list of commits.

> 72-character wrapped longer description.

Often a subject by itself is sufficient. When it’s not, add a blank line (this is important) followed by one or more paragraphs hard wrapped to 72 characters.

Those paragraphs should explain:

**Why is this change necessary?**

This answer explains what to expect in the commit, allowing them to more easily identify and point out unrelated changes.

**How does it address the issue?**

Describe, at a high level, what was done to affect change. If your change is obvious, you may be able to omit addressing this question.

**What side effects does this change have?**

This is the most important question to answer, as it can point out problems where you are making too many changes in one commit or branch. One or two bullet points for related changes may be okay, but five or six are likely indicators of a commit that is doing too many things.

```
# 50-character subject line## 72-character wrapped longer description. This should answer:## * Why was this change necessary?# * How does it address the problem?# * Are there any side effects?## Include a link to the ticket, if any.
```

#### How to make your life easier

It’s a lot to remember, but you can set up a commit message template by using the `commit.template`

Configure Git to use a template file (for example, `.gitmessage`), then create the template file with Vim:

```
git config --global commit.template ~/.gitmessagevim ~/.gitmessage
```

When we run `git commit` without the `-m` message flag, the editor will open our helpful template ready to go:

```
# [Add/Fix/Remove/Update/Refactor/Document] [summary]# Why is it necessary? (Bug fix, feature, improvements?)-# How does the change address the issue? -# What side effects does this change have?-# Include a link to the ticket, if any.
```

Commented lines are not included in the final message. Simply fill in the blank lines with text and bullet points under the prompts.

Issue trackers in GitHub and Bitbucket both recognise the keywords `close`, `fix`, and `resolve` followed immediately by the issue or pull request number.

I think Linus would be very happy if we didn’t use `git commit -m "Fix bug"` in a public repository ever again :)

You can simple search in git log for a issue number, for example, with `git log --grep=JIRA-1234`

You can also use plugins like `vim-fugitive` for _vim_ or `git lens` for _vs code_ to quickly access to git commit messages.

#### Closing thoughts

Creating clean Git commits says a lot about you and may be a primary way that people interact with you over projects.

With a little practice, you can make your commit habits an even better reflection of your best work — work that is evidently created with care and pride.

Your future you, and your team, will thank you for your forethought and verbosity when they run `git blame` to see why that conditional is there.

_If you enjoyed this article please clap, recommend and share._

