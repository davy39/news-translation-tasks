---
title: How to Use Git Cherry Pick and Avoid Duplicate Commits
subtitle: ''
author: Christine Belzie
co_authors: []
series: null
date: '2024-01-03T21:33:29.000Z'
originalURL: https://freecodecamp.org/news/git-cherry-pick-avoid-duplicate-commits
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/blog-cover-for-git-cherry-pick.png
tags:
- name: Git
  slug: git
- name: open source
  slug: open-source
seo_title: null
seo_desc: "Imagine a beautiful cherry tree full of sweet, red, round fruit hanging\
  \ on lush, glistening branches. But imagine if those cherries grew so quickly that\
  \ the branches started bending, overlapping, and breaking...sounds chaotic right?\
  \ \nThis is what can..."
---

Imagine a beautiful cherry tree full of sweet, red, round fruit hanging on lush, glistening branches. But imagine if those cherries grew so quickly that the branches started bending, overlapping, and breaking...sounds chaotic right? 

This is what can happen if you don't use Git's `cherry-pick` command properly in open source projects. Similarly to hand-picking the finest cherries and putting them in a basket, this command allows you to move individual commits from one branch into another.

It great for when you're collaborating with someone else on an open source project because it saves you the trouble of having to merge entire branches. 

Now as powerful and awesome as the Git `cherry-pick` command is, it can create duplicate commits, making it difficult for open source maintainers to update their project's codebase or solve bugs. 

Scared? Fear not, my fellow open source contributor. I have some strategies that you can use to prevent duplicates when cherry-picking commits.

## Strategy 1: Use the `--no commit` Option

This option is one of the most common methods to prevent duplicate commits. It copies the changes from a branch but it won’t create a new commit, which can be very helpful if you’re working on a contribution with another person. Let’s see it in action.

### Step 1: Pick your Cherry (commit)

After you pick the open source project you and your partner are working on, go to their fork and click on the **Commits** tab. 

![Image](https://www.freecodecamp.org/news/content/images/2023/12/commits-1.png)
_Screenshot of a Pull Request's tab. The Commits section is highlighted with a orange oval_

From there, pick the commit that you want to put on your Pull Request by clicking on its SHA number. 

![Image](https://www.freecodecamp.org/news/content/images/2023/12/commit-sha.png)
_Screenshot of commit history. The SHA number is shown on the right, highlighted in a green oval._

As you can see in the image, the SHA number is a unique id that contains the following information about a commit:

* The type of changes made
* When the changes were made
* The contributor who made the changes

After that, paste your chosen commit's SHA number in the following command:

```git
git cherry-pick --no-commit <commit SHA number> 
```

### Step 2: Check for Spots and Plant 

After running the `--no-commit` command, now it's time to inspect your picked commit. You can do this by doing the following commands:

* `git diff` :  This command shows you all the lines added, deleted, or modified by the cherry-picked commit. Here’s how it would look if someone was making a translation contribution:

```git
git diff 2f410g1
diff --git a/01-intro.md b/01-intro.md
index 1234567890123456789012345678901234567890..0000000000000000000000000000000000000000
--- a/01-intro.md
+++ b/01-intro.md
@@ -1,3 +1,4 @@
- Hello, everyone!
+ Bonjour, tout moun!
- Welcome to our course!
+ [Placeholder for French intro]
+ Bonjour, amis!


```

* `git show commit SHA` : With this version of the `git show` command, you'll see the name of the contributor, date of their commit, their email, and the list of changes they have made. If we were to take the SHA number from the previous example and used this command, here's how the output would look:

```git
git show 2f410g1 (Frenchify intro and materials!)
Author: John (johnseed@example.com)
Date:   2023-12-18 18:07:15 -0500

Bonjour, le monde!  Time to add French translations to our intro and course materials.

* **01-intro.md:** Warm welcome and placeholder for the French translation.
* **materials.md:** Module descriptions replaced with [placeholders] for French versions.

... and other exciting French changes in 4 more files!
```

Now that you've picked your method of inspection, go to your files to make the changes and create a commit message as shown below.

```git
git commit -m <"message">
```

From there, push the changes into your Pull Request's branch.

Now, `—no—commit` is not the only strategy you can use to prevent duplicate commits. Let’s look another one.

## Strategy 2: Make Some Changes With `--edit`

If you know the edits that you want to make in the commit you picked, then the `--edit` command is for you. Here it is in action:

```git
git cherry-pick -e 2f450g1
diff --git a/docs/content/pets.md b/docs/content/pets.md
index abcdef12..34567890 100644
--- a/docs/content/pets.md
+++ a/docs/content/pets.md
@@ -1,4 +1,5 @@
 # Pets
 
 This is a file about pets.
+New content added about pets.
 
 ## Different types of pets
# Continue cherry picking process
git cherry-pick --continue
# Change commit message
git commit -m "feat: add section"
```

As shown in the code snippet, we initiated an interactive cherry-pick of a commit containing changes to the `pets.md` file. During the cherry-picking process, you may make direct edits to the file, including adding new content and changing the heading. From there, we created a new commit message and pushed the changes to our branch. 

## Start Picking 

There it is folks – strategies to help you avoid duplicate commits when cherry-picking. 

Using this command effectively not only makes it easier for you to work on collaborative contributions, but also keeps your commit history clean. 

If you want to learn more about cherry-picking commits and want to put those skills to use, check out [this guide by Atlassian](https://www.atlassian.com/git/tutorials/cherry-pick?source=post_page-----708ad5950460--------------------------------) and this [course by OpenSauced](https://intro.opensauced.pizza/#/). Also, check out [BioDrop](https://www.biodrop.io/CBID2) to view my other technical content and connect with me.

### Credits 

Image of commit history from _[How to fix the order of commits in GitHub Pull Requests](https://andrewlock.net/how-to-fix-the-order-of-commits-in-github-pull-requests/)_ by Andrew Lock 

