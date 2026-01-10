---
title: How to Uncommit Sensitive Files from Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T20:55:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-uncommit-sensitive-files-from-git
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/IMG_5162.00_00_17_13.Still001-1.jpg
tags:
- name: Git
  slug: git
- name: information security
  slug: information-security
- name: version control
  slug: version-control
seo_title: null
seo_desc: "By Ondrej Polesny\nStage files, add a commit message, push. No – wait!\
  \ Not that file. And now we need to start googling. \nEvery developer has accidentally\
  \ committed sensitive files in the past. So how do we fix the situation and ensure\
  \ it wonʼt happen..."
---

By Ondrej Polesny

Stage files, add a commit message, push. No – wait! Not that file. And now we need to start googling. 

Every developer has accidentally committed sensitive files in the past. So how do we fix the situation and ensure it wonʼt happen again?

In this article, Iʼll explain what to do when you accidentally commit a sensitive file and include the necessary Git commands to adjust the history.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/illustration.png)
_How to uncommit sensitive files from git_

## Damage control

So you accidentally committed a sensitive file. Letʼs call it _.env_. There are two important questions to answer:

* Did you push the commit to a remote repository?
* Is the remote repository public?

### Not pushed yet

If you did not push yet, the situation is not at all critical. You can **return to a previous commit**:

```
git reset HEAD^ --soft
```

Your files will stay in the working copy so that you can fix the sensitive file/info. If you want to **keep the commit and just remove the sensitive file**, do:

```
git rm .env --cached
git commit --amend
```

You can use the `--amend` only on the latest commit. If you managed to add a bunch of commits on top of that, use:

```
git rebase -i HEAD~{how many commits to go back?}
```

This will allow you to fix the faulty commit and it will replay all the remaining commits after the fix so you wonʼt lose them.

### Already pushed

If you did push, there is an important difference between public and private repositories.

If your repository is private and there are no bots or people you donʼt trust with access to it, you can easily amend the last commit using the two commands above. 

If you pushed a bunch of commits on top of the problematic one, you can still use [filter-branch](https://git-scm.com/docs/git-filter-branch) or [BFG repo cleaner](https://rtyley.github.io/bfg-repo-cleaner/) to **remove the sensitive file from git history**:

```
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch .env" --prune-empty --tag-name-filter cat -- --all
```

But keep in mind two important aspects of these changes:

* **You are actually changing the history**  
If there are other people, other branches, other forks, or open pull requests relying on the current state of the repository, you will break them. In those cases, treat the repository as if it was public and avoid changing the history.
* **You need to clear cache**  
You always need to contact the support of your Git storage provider and ask them to clear the cache of your repository. Even though you fixed the problematic commit or rewrote the history, the old commit with the sensitive file stays in the cache. Youʼd need to know its ID to access it, but itʼs still accessible until you clear the cache.

## Do I need to regenerate keys if pushed to a public repository?

In short, yes. If your repository is public or you donʼt think itʼs a safe place for any other reason, you must consider the sensitive information compromised. 

Even if you remove the data from your repository, you canʼt do anything about bots and other forks of the repo. So what are the next steps?

* **Deactivate all keys and/or passwords**  
Do this as the first step. Once you deactivate the keys, sensitive information becomes useless.
* **Adjust gitignore**  
Add all sensitive files to .gitignore to make sure git wonʼt track them.
* **Remove the sensitive file**
* **Commit the fix with a meaningful explanation**  
Donʼt try to hide the mistake. Other collaborators and you in a month will appreciate the explanation of what happened and what this commit fixes.

## Best practices when storing sensitive data in Git

To avoid a situation like this in the future, here are a few tips on storing sensitive data:

### Keep sensitive data in .env file (or similar file on other platforms)

Keep API keys and other sensitive data in a single .env file. That way you wonʼt accidentally commit a new key when the .env file is already excluded from git. 

Another great benefit is that you get access to all keys using a global _process_ variable.

### Use API keys if possible

API keys are easy to generate and deactivate if compromised. If possible, use them and avoid using credentials/passwords.

### Add API keys to your build tool

API keys are usually needed during application builds. Build tools like Netlify allow you to add these keys in the secure areas of their administration. These keys are automatically injected into your app via the global _process_ variable.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify.png)

### Add .env file to gitignore

Make sure Git doesnʼt track files containing sensitive information.

### Provide .env.template file

The template file instructs other collaborators to add the necessary API keys without requiring them to read long docs.

### Do not change the history on remote

Use this as a rule of thumb. If you followed the above rules, you wonʼt need to change the history.

I hope this info helped you to stay on the safe side. Do you have a personal experience with uncommitting or perhaps a good _lesson learned_? [Talk to me on Twitter](https://twitter.com/ondrabus) :-)

