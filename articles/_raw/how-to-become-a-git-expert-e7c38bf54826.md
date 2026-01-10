---
title: How to become a Git expert
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T22:55:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-become-a-git-expert-e7c38bf54826
coverImage: https://cdn-media-1.freecodecamp.org/images/0*tJq8RS_Uv3R9s56E
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Aditya Sridhar

  I made a mistake in my commit, how do I fix it ?

  My commit history is a mess, how do I make it neater?

  If you have ever had the above questions, then this post is for you. This post covers
  a list of topics which will make you a Git ...'
---

By Aditya Sridhar

I made a mistake in my commit, how do I fix it ?

My commit history is a mess, how do I make it neater?

If you have ever had the above questions, then this post is for you. This post covers a list of topics which will make you a Git expert.

If you do not know Git basics, [click here](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61) to check out my blog on Git basics. It is necessary that you know basics of Git to make the best use of this article.

### I made a mistake in my commit. What should I do?

![Image](https://cdn-media-1.freecodecamp.org/images/57nEHwVjqEC1a-ULvcaNS0dmO0uFsBQDUFk0)
_“broken ceramic plate on floor” by [Unsplash](https://unsplash.com/@chuttersnap?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">chuttersnap</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Scenario 1

Let’s say that you have committed a bunch of files and realised that the commit message you entered is actually not clear. Now you want to change the commit message. In order to do this you can use `git commit --amend`

```bash
git commit --amend -m "New commit message"
```

#### Scenario 2

Let’s say that you wanted to commit six files but, by mistake, you end up committing only five files. You may think that you can create a new commit and add the 6th file to that commit.

There is nothing wrong with this approach. But, to maintain a neat commit history, wouldn’t it be nicer if you could actually somehow add this file to your previous commit itself? This can be done through `git commit --amend` as well:

```bash
git add file6
git commit --amend --no-edit
```

`--no-edit` means that the commit message does not change.

#### Scenario 3

Whenever you do a commit in Git, the commit has an author name and author email tied to it. Generally, when you set up Git for the first time, you set up the author name and email. You don’t need to worry about the author details for every commit.

That said, it’s possible that for a particular project you want to use a different email ID. You need to configure the email id for that project with the command:

```bash
git config user.email "your email id"
```

Let’s say that you forgot to configure the email and already did your first commit. `Amend` can be used to change the author of your previous commit as well. The author of the commit can be changed using the following command:

```bash
git commit --amend --author "Author Name <Author Email>"
```

#### **Point to note**

Use the `amend` command **only** in your local repository. Using `amend` for the remote repository can create a lot of confusion.

### My Commit history is a mess. How do I handle it?

Let’s say that you are working on a piece of code. You know that the code is going to take approximately ten days to complete. Within those ten days, the other developers will also be committing code to the remote repository.

It is a **good practise** to keep your local repository code up-to-date with the code in the remote repository. This avoids a lot of merge conflicts later when you raise a pull request. So you decide that you will pull the changes from the remote repository once every two days.

Every time you pull the code from the remote repository to the local repository a new merge commit is created in your local repository. This means that your local commit history is going to have a lot of merge commits which can make things look confusing to the reviewer.

![Image](https://cdn-media-1.freecodecamp.org/images/Kf0bCgSdXtM1PJTZwn1FJ5-xPxJa7a3aSRZQ)
_Here is how the commit history would look in your local repository._

#### How do you make the commit history look neater?

This is where **rebase** comes to the rescue.

#### What is rebasing?

Let me explain this through an example.

![Image](https://cdn-media-1.freecodecamp.org/images/HeXMQ3fwvXGfqiBCQJpYCRmzMTGkObShA4NS)
_This diagram shows the commits in the release branch and your feature branch_

1. The Release branch has three commits: Rcommit1, Rcommit2, and Rcommit3.
2. You created your Feature branch from the Release branch when it had only one commit, which is Rcommit1.
3. You have added two commits to the Feature branch. They are Fcommit1 and Fcommit2.
4. Your goal is to get the commits from the Release branch into your Feature branch.
5. You are going to use rebase to do this.
6. Let the name of the Release branch be **release** and the name of the Feature branch be **feature**.
7. Rebasing can be done using the following commands:

```bash
git checkout feature
git rebase release
```

#### Rebasing

While rebasing, your goal is to ensure the Feature branch gets the latest code from the Release branch.

Rebasing tries to add each commit, one by one, and checks for conflicts. Does that sound confusing?

Let me explain with the help of a diagram.

This shows what rebasing actually does internally:

![Image](https://cdn-media-1.freecodecamp.org/images/iGgX4jvJOB8Gc2n8T1WSh8VpWEZqd1CoL2g3)

#### Step 1

1. The moment you run the command, the Feature branch is pointed to the head of Release branch.
2. Now the Feature branch has three commits: Rcommit1, Rcommit2, and Rcommit3.
3. You may be wondering what happened to Fcommit1 and Fcommit2.
4. The commits are still there and will be used in the steps below.

#### **Step 2**

1. Now Git tries to add Fcommit1 to the Feature branch.
2. If there is no conflict Fcommit1 is added after Rcommit3
3. If there is a conflict, Git will notify you, and you will have to resolve the conflict manually. After the conflict is resolved use the following commands to continue rebasing

```bash
git add fixedfile
git rebase --continue
```

#### **Step 3**

1. Once Fcommit1 is added, Git will try to add Fcommit2.
2. Again, if there is no conflict Fcommit2 is added after Fcommit1 and the rebase is successful.
3. If there is a conflict, Git will notify you, and you will have to resolve it manually. Use the same commands mentioned in Step 2 after resolving conflicts
4. After the entire rebase is done, you will notice that the Feature branch has Rcommit1, Rcommit2, Rcommit3 , Fcommit1, and Fcommit2.

#### Points to note

1. Both Rebase and Merge are useful in Git. One is not better than the other.
2. In the case of a merge you will have a merge commit. In the case of a rebase there is no extra commit like a merge commit.
3. One best practise is to use the commands at different points. Use rebase when you are updating your local code repository with the latest code from the remote repository. Use merge when you are dealing with pull requests to merge the Feature branch back with the Release or Master branch.
4. Using Rebase alters the commit history ( it makes it neater) . But that being said, altering the commit history has it’s risks. So ensure you never use rebase on a code that is there in the remote repository. Always use rebase only to alter the commit history of your local repo code.
5. If rebase is done to a remote repository it can create a lot of confusion since other developers will not recognise the new history.
6. Also if rebase is done on the remote repository, it can create issues when other developers try to pull the latest code from remote repository. So I repeat again, always use rebase only for the local repository ?

### Congrats ?

You are now a Git expert ?

In this post you have learnt about:

* amending commits
* rebase

Both of these are very useful concepts. Go explore the world of Git to learn even more.

### About the author

I love technology and follow the advancements in the field. I also like helping others with my technology knowledge.

Feel free to connect with me on my LinkedIn account [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

You can also follow me on twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

My Website: [https://adityasridhar.com/](https://adityasridhar.com/)

### Other Posts by Me

[Best Practises while using Git](https://adityasridhar.com/posts/how-you-can-go-wrong-with-git)

[An introduction to Git](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61)

[How to use Git efficiently](https://medium.freecodecamp.org/how-to-use-git-efficiently-54320a236369)

