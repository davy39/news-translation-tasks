---
title: Now that you’re not afraid of GIT anymore, here’s how to leverage what you
  know
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T18:10:06.000Z'
originalURL: https://freecodecamp.org/news/now-that-youre-not-afraid-of-git-anymore-here-s-how-to-leverage-what-you-know-11e710c7f37b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8rQSJ7R76i_N0r-LjULBZw.jpeg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Neil Kakkar

  The first part of this series looked at the inner workings of GIT and showed you
  how not to be afraid of working with Git.

  Now that we understand how Git works, let’s get into the meaty stuff: how to leverage
  what we know in our projec...'
---

By Neil Kakkar

[The first part of this series looked at the inner workings of GIT](https://medium.freecodecamp.org/how-not-to-be-afraid-of-git-anymore-fe1da7415286) and showed you how not to be afraid of working with Git.

Now that we understand how Git works, let’s get into the meaty stuff: how to leverage what we know in our projects.

### Merge

Merge _merges_ your code.

Remember how we were following good Git practices, having branches for various features we were working on, and not everything on `master`? There will come a time when you are done with that feature, and will want to include that in your `master`. This is where `merge` comes in. You want to **merge** your branch into master.

There are 2 kinds of merges:

#### Fast forward merge

Coming back to our example from last time:

This is as simple as moving the label for `master` to `the-ending`. Git has no doubt about exactly what needs to be done — since our “tree” had one single linked list of nodes.

```
$ git branch
  master
* the-ending
$ git checkout master
Switched to branch 'master'
$ git merge the-ending
Updating a39b9fd..b300387
Fast-forward
 byeworld | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 byeworld
```

#### Non-Fast Forward Merge

This is the kind of merge where Git doesn’t know what to do. There are some changes on the base branch, and some more on the branch we want to merge, thus resulting in the scary _merge conflicts_!

Here’s the first thing to know about merge conflicts: If you don’t know what’s happening:

```
git merge --abort
```

This will bring you back to the original state, with no side effects. You just aborted the mess you were about to make.

![Image](https://cdn-media-1.freecodecamp.org/images/HAWGpuc2gjD5wYOk9UbaPNorlFq4dXA5FRFU)
_[You don’t want to be Brian?](http://www.quickmeme.com/p/3vzhql" rel="noopener" target="_blank" title=")_

Let’s go step by step now into how to resolve merge conflicts.

```
$ git checkout -b the-middle
Switched to a new branch 'the-middle'
```

In continuing our style, let’s learn via an example. I modify `helloworld` on branch `the-middle`.

```
$ git diff
diff --git a/helloworld b/helloworld
index a042389..e702052 100644
--- a/helloworld
+++ b/helloworld
@@ -1 +1,3 @@
 hello world!
+
+Middle World
```

Add and commit on `the-middle`.

Then, I switch to `master` and modify `helloworld` on master. I add the following:

```
$ git diff --cached
diff --git a/helloworld b/helloworld
index a042389..ac7a733 100644
--- a/helloworld
+++ b/helloworld
@@ -1 +1,3 @@
 hello world!
+
+Master World
```

Do you see why I had to do `git diff --cached` here? If not, ask me below!

Now, it’s time to merge!

```
$ git merge the-middle
Auto-merging helloworld
CONFLICT (content): Merge conflict in helloworld
Automatic merge failed; fix conflicts and then commit the result.
```

When a `merge` fails, here’s what git does: It modifies the file with the merge to show you exactly what it can’t decide about.

```
$ cat helloworld 
hello world!
```

```
$ cat helloworld 
hello world!
<<<<<<< HEAD
Master World
=======
Middle World
>>>>>>> the-middle
```

Does this make sense? The `<<<<< HEAD` part is ours (the base branch) and the `>>>>> the-middle part` is `theirs` (the branch merging into the base branch).

You can simply edit the file to remove the extra stuff added by git, and choose what should go into `helloworld` finally. There are some tools and editor integrations to make this easier, but I think knowing how it works underneath the hood gives you more confidence when you don’t have your favourite editor lying around.

```
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)
Unmerged paths:
  (use "git add <file>..." to mark resolution)
both modified:   helloworld
```

I decided to keep both bits.

```
$ cat helloworld 
hello world!
Master World
Middle World
```

And there you have it:

```
$ git add helloworld 
$ git commit -m "resolve merge conflict"
[master c747e68] resolve merge conflict
```

### Remotes

Since one power of version source control is to save your code in case of disasters — remotes are here to help. A remote is an externally-hosted copy of your git repository. To be more accurate, a remote is an external repository (not necessarily of the same code you have). By external, it could be in a different folder on your system or in the cloud.

#### Clone

Clone _clones_ the repository from remote into your current working directory. This is simply creating a copy of the `.git/` folder, which gives us the entire history and the files needed to populate the working directory.

```
git clone <repository-url>
```

If you haven’t cloned, you probably don’t have a remote. You can create a remote like this:

```
git remote add <name> <url>
```

### Push and Pull

Push and Pull are actions applied on the `remote`.

Push _pushes_ your changes to the remote. So, we are sending the `Index` and corresponding `Objects` from the object-store!

```
git push <name of remote> <name of branch>
```

Pull _pulls_ the code from the remote. Exactly as before, we are copying the `Index` and corresponding `Objects` from the object-store!

```
git pull origin master
```

`origin` is the default name of the remote. And since `master` is the default branch, you can see how the command devolves into the simple name we find everywhere: `git pull origin master`. Now you know better.

### Reset

Reset _resets_ your codebase to a previous version. Reset comes with 3 flags:

`--soft`, `--hard` and `--mixed`.

The beauty of `reset`, is being able to change history. Say you make a mistake with a `commit`, and now your `git log` is all messed up with commits like:

`Bugfix`

`Final BugFix`

`Final Final BugFix`

`God why isn't this working last try bug fix`

If you want to keep your `master` history clean, you want to clean up this commit log.

If you’re sending in a Pull Request where there’s no squashing, they’d expect a clean commit history too!

That’s where `reset` comes in: You could `reset` all your commits and convert them into one single commit: `got stuff done!`

(Please don’t use this as your commit message — follow the best practices!)

Coming back to our example, here’s what I’ve done.

```
$ git log
commit 959781ec78c970d4797c5e938ec154de44d0151b (HEAD -> master)
Author: Neil Kakkar
Date:   Mon Nov 5 07:32:55 2018 +0000
God why isn't this working last final BugFix
commit affa90c0db78999d22c326fdbd6c1d5057228822
Author: Neil Kakkar
Date:   Mon Nov 5 07:32:19 2018 +0000
Final Final BugFix
commit 2e9570cffc0a8206132d75c402d68351eda450bd
Author: Neil Kakkar
Date:   Mon Nov 5 07:31:49 2018 +0000
Final BugFix
commit 4560fc0ec6305d0b7bcfb4be1901438fd126d6d1
Author: Neil Kakkar
Date:   Mon Nov 5 07:31:21 2018 +0000
BugFix
commit c747e6891af419119fd817dc69a2e122084aedae
Merge: 3d01508 fb8b2fc
Author: Neil Kakkar
Date:   Tue Oct 23 07:44:09 2018 +0100
resolve merge conflict
```

Now that the bug is fixed, I want to clean up my history before I push to `master`. This would work well too — when, say, I realise later on that I introduced another bug and need to revert to the previous version. In this case, `c747e689` doesn’t have the best commit message to understand this.

```
$ git reset c747e6891af419119fd817dc69a2e122084aedae
$ git log
commit c747e6891af419119fd817dc69a2e122084aedae (HEAD -> master)
Merge: 3d01508 fb8b2fc
Author: Neil Kakkar
Date:   Tue Oct 23 07:44:09 2018 +0100
resolve merge conflict
```

There, all sorted?

```
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
      clean.txt
nothing added to commit but untracked files present (use "git add" to track)
```

`clean.txt` is the file I had committed for the bug fix. Now, all I have to do is:

```
$ git add clean.txt 
$ git commit -m "fix bug: Unable to clean folder"
[master d8487ca] fix bug: Unable to clean folder
 1 file changed, 4 insertions(+)
 create mode 100644 clean.txt
$ git log
commit d8487ca8b9acfa9666bdf2c6b7fa27b3971bd957 (HEAD -> master)
Author: Neil Kakkar
Date:   Mon Nov 5 07:41:41 2018 +0000
fix bug: Unable to clean folder
commit c747e6891af419119fd817dc69a2e122084aedae
Merge: 3d01508 fb8b2fc
Author: Neil Kakkar
Date:   Tue Oct 23 07:44:09 2018 +0100
resolve merge conflict
```

There, done and dusted. Can you guess now, using the clues from the `log`, the `reset` command syntax and your tech-sense to figure out how it works behind the scenes?

`Reset` cuts off the commit-tree at the specified commit. All labels for that branch — if ahead — are moved back to the specified commit. Do the existing files stay in the object store though? You know how to check that now, Ace.

The files are also removed from the staging area. Now this might be a problem if you have lots of untracked/modified files which you don’t want to add.

How do you do that?

Can you pick up the clue I left in the beginning of this section?

Behaviour flags!

`--soft` keeps all files staged.

```
$ git reset --soft c747e6891af419119fd817dc69a2e122084aedae
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
new file:   clean.txt
```

`--mixed` is the default: Removes all files from staging area too.

`--hard` is hard-core. Deletes files from the object store — and directory as well. Use with extreme caution. There goes my bug fix*. Gone.

```
$ git reset --hard c747e6891af419119fd817dc69a2e122084aedae
HEAD is now at c747e68 resolve merge conflict
$ git status
On branch master
nothing to commit, working tree clean
```

*Well, not completely. Git is amazing. Have you heard of meta-meta data? A redundancy log of what happened in the repository? Yes, of course git keeps it!

```
$ git reflog
c747e68 (HEAD -> master) HEAD@{0}: reset: moving to c747e6891af419119fd817dc69a2e122084aedae
efc6d21 HEAD@{1}: commit: soft reset
c747e68 (HEAD -> master) HEAD@{2}: reset: moving to c747e6891af419119fd817dc69a2e122084aedae
d8487ca HEAD@{3}: commit: fix bug: Unable to clean folder
c747e68 (HEAD -> master) HEAD@{4}: reset: moving to c747e6891af419119fd817dc69a2e122084aedae
959781e HEAD@{5}: commit: God why isn't this working last final BugFix
affa90c HEAD@{6}: commit: Final Final BugFix
2e9570c HEAD@{7}: commit: Final BugFix
4560fc0 HEAD@{8}: commit: BugFix
c747e68 (HEAD -> master) HEAD@{9}: commit (merge): resolve merge conflict
3d01508 HEAD@{10}: commit: add Master World
b300387 (the-ending) HEAD@{11}: checkout: moving from the-middle to master
fb8b2fc (the-middle) HEAD@{12}: commit: add Middle World
b300387 (the-ending) HEAD@{13}: checkout: moving from master to the-middle
b300387 (the-ending) HEAD@{14}: checkout: moving from the-middle to master
b300387 (the-ending) HEAD@{15}: checkout: moving from master to the-middle
b300387 (the-ending) HEAD@{16}: merge the-ending: Fast-forward
a39b9fd HEAD@{17}: checkout: moving from the-ending to master
b300387 (the-ending) HEAD@{18}: checkout: moving from master to the-ending
a39b9fd HEAD@{19}: checkout: moving from the-ending to master
b300387 (the-ending) HEAD@{20}: commit: add byeworld
a39b9fd HEAD@{21}: checkout: moving from master to the-ending
a39b9fd HEAD@{22}: commit (initial): Add helloworld
```

This is everything from the beginning of the example in the previous article. Does this mean I can recover things if I made an awful mistake?

```
$ git checkout d8487ca
Note: checking out 'd8487ca'.
You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.
If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:
git checkout -b <new-branch-name>
HEAD is now at d8487ca... fix bug: Unable to clean folder

$ ls
byeworld clean.txt  helloworld
```

There you have it.

Congratulations, you’re a Git Ninja — Apprentice now.

Is there something more you’d like to know about? Something that confused you about Git? Let me know below! I’ll try explaining it the way I learnt it!

Enjoyed this? [Don’t miss a post again — subscribe to my mailing list!](http://neilkakkar.com/subscribe/)

