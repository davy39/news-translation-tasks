---
title: How you can go wrong with Git — and what to do instead.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-14T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-go-wrong-with-git-and-what-to-do-instead-d80eeeff1d95
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Tj_DgrXII8u5E1sv
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

  I am not able to commit to the remote repository, let me do a force push.

  Let me run rebase on the remote repository, to make the commit history neater.

  Let me amend my previous commit which is in the remote repository.

  The points m...'
---

By Aditya Sridhar

I am not able to commit to the remote repository, let me do a force push.

Let me run rebase on the remote repository, to make the commit history neater.

Let me amend my previous commit which is in the remote repository.

**The points mentioned above are some of the things to avoid doing in Git.**

In my previous posts I covered [Git basics](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61) and [Git amend and rebase](https://medium.freecodecamp.org/how-to-become-a-git-expert-e7c38bf54826). Click on the links to know more about them.

Git has amazing features and is very helpful for developers. But mistakes still happen while using Git. Here I will be mentioning some of the **things to avoid** while using Git and also **explain why** you should avoid them.

### Force push to remote repository

![Image](https://cdn-media-1.freecodecamp.org/images/vxvEY0Py6Tt3Jsfqcw3H5BSMdGC2qpuA2TqD)
_Photo by [Unsplash](https://unsplash.com/@timmossholder?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Tim Mossholder</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Let’s say two developers are working on a single branch. Developer 2 is a beginner to Git.

1. Developer 1 has finished their changes and pushed the code to the remote repository.
2. Now Developer 2 has finished their changes, but is unable to push the code to the remote repository.
3. Developer 2 does a quick google search and finds out about force push command and uses it. The command is `git push -f`
4. Developer 1 checks the remote repository only to find out the code they wrote has completely disappeared.

**This is because force push overrides the code in the remote repository and, hence, the existing code in remote repository gets lost.**

#### Ideal way of handling this scenario

Developer 2 needs to pull the latest code changes from the remote repository and rebase the code changes into the local repository. Once the rebase is done successfully, Developer 2 can push the code into the Remote repository. **Here we are talking about rebase from remote to local repo in the same branch.**

**Avoid force push** unless absolutely necessary. Use it only as a last resort if there is no other way to handle a situation. But remember that force push will override the code in the remote repository.

In fact if you are using a user interface like source tree, by default force push is disabled. You will have to manually enable it to use it.

Also if the right [Git workflows](https://medium.freecodecamp.org/how-to-use-git-efficiently-54320a236369) are used, each developer will have their own feature branches, and such a scenario would not even occur.

### Trying to rebase the remote repository

![Image](https://cdn-media-1.freecodecamp.org/images/YYrwWwrW0Le9w89HoybfYPLmJ5JpmwwzABOG)
_“green, red, and white high voltage circuit breaker” by [Unsplash](https://unsplash.com/@benhershey?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Ben Hershey</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Let’s say two developers are working on a feature branch.

1. Developer 1 has done a bunch of commits and pushed it to the remote feature branch.
2. Developer 2 takes the latest changes from the remote feature branch into the local feature branch.
3. Developer 2 adds a bunch of commits to the local feature branch.
4. But Developer 2 also wants to ensure that the latest changes from the release branch are rebased into the feature repository. So Developer 2 rebases the release branch onto the local feature branch. **This is the rebase done from remote to local repo of different branches**.
5. Now Developer 2 tries to push the code to the remote feature branch. Git won’t allow you since the commit history has changed. So Developer 2 would do a force push.
6. Now, when Developer 1 wants to pull the latest code from the remote feature branch, it is a tough job since the commit history has changed. So Developer 1 will need to take care of a lot of code conflicts — even redundant code conflicts which were already taken care of by Developer 2.

**Rebasing the remote repository will alter the commit history and will create issues when other developers try to pull the latest code from the remote repository.**

#### Ideal way of handling this scenario

The ideal way of handling this situation is to always rebase **only** the local repository. None of the commits in the local repo should have already been pushed to the remote repo.

If any of the commits have already been pushed to the remote feature branch, then its better to do a merge with the release branch rather than a rebase since merge would not alter the commit history.

Also if the right Git workflows are used, only one person would work on one feature branch, and this issue would not even occur.

If only one person works on the feature branch and a rebase is done on the remote feature branch, then there is no issue — no other developers are pulling code from the same remote feature branch. But it is best to avoid rebasing a remote repository.

**Rebase is a very powerful feature, but use it carefully.**

### Amending commits in the remote repository

![Image](https://cdn-media-1.freecodecamp.org/images/gq1Wo6a6yVlzmaudBN6xO6Vs65fZ7EkiYukn)
_“broken ceramic plate on floor” by [Unsplash](https://unsplash.com/@chuttersnap?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">chuttersnap</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Let’s say two developers are working on a feature branch.

1. Developer 1 has done a commit and pushed it to the remote feature branch. Lets call this “commit old.”
2. Developer 2 pulls the latest code from the remote feature branch into the local feature branch
3. Developer 2 is working on the code in the local repository and has not pushed any code to the remote repository yet.
4. Developer 1 realises there was a mistake in the commit, and amends the commit in the local repo. Let’s call this “commit new.”
5. Developer 1 tries to push the amended commit to the remote feature branch. But Git would not allow this since there is a change in commit history. So Developer 1 does a force push.
6. Now, when Developer 2 wants to pull the latest code from the remote feature branch, Git will notice the difference in commit histories and create a merge commit. When Developer 2 goes over the commit history in the local repo, Developer 2 will notice both “commit new” and “commit old”. This destroys the whole point of amending a commit.
7. Even if Developer 2 does a rebase from remote branch to the local branch, “commit old” will still be present in Developer 2’s local. So it will still be a part of the commit history.

**Amending a commit changes the commit history. So amending a commit in the remote repository will create confusion when other developers try to pull the latest code from the remote repository**

#### Ideal way of handling this scenario

Best practise is to amend commits only in the local repository. Once the commit is there in the remote repository, it is best not to do any amends.

Also, if the right Git workflows are used, only one person would work on one feature branch and this issue would not even occur. In this case, amending a remote repository would not create any issues, since no other developers are pulling code from the same remote feature branch.

### Hard reset

![Image](https://cdn-media-1.freecodecamp.org/images/6JofEPRTTXtI2CQJvVYxKtSnV3NtdyL9TbBZ)
_“clear hour glass beside pink flowers” by [Unsplash](https://unsplash.com/@nate_dumlao?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Nathan Dumlao</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

1. Hard reset is done by using `git reset --hard`
2. There are other types of reset as well like`--soft` and `--mixed` which are not as dangerous as hard reset

Let’s say Developer 1 is working on a feature branch and has done five commits in the local repo.

1. Also, Developer 1 is currently working on two files which are not yet committed.
2. If Developer 1 runs `git reset --hard <commit4hash>` the following things will happen.
3. The latest commit in feature branch will now be commit4 and commit5 is lost.
4. The two uncommited files which Developer 1 was working on are also lost

Commit5 is still there internally in Git but the reference to it is lost. We can get the commit5 back using `git reflog`. But, that being said, it is still very risky to use hard reset.

**Be very careful when you are using reset commands in Git. You may have to use reset in some scenarios, but evaluate the situation completely before going ahead with hard reset.**

### How to know the bad practises while using Git

![Image](https://cdn-media-1.freecodecamp.org/images/sa54At5X8hjGOHKzP2owlBAfmMuhkjIdpzOy)
_“question mark neon signage” by [Unsplash](https://unsplash.com/@emilymorter?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Emily Morter</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

The list I have mentioned above does not cover everything. It just lists out some of the things that can go wrong while using Git.

So how do you know in general what to avoid while using Git?

1. One common thing you would have observed in the above list is that issues occur when multiple people work on the same branch. So using the right Git workflows would ensure only one person works on one feature branch at a time. The release branch would be handled by the tech lead or a senior developer. This workflow can prevent some major issues from happening.
2. One other common thing you would observe is the use of force push everywhere. Git, by default, ensures that you cannot do any destructive change in the remote repository. But force push overrides the default behaviour of Git.
3. So, whenever you are in a position where you may need to use force push, use it only as a last resort. Also evaluate if there is any other way of achieving what you want without using force push.
4. Any operation which alters the commit history in the remote repository can be dangerous. Alter the commit history only in your local repository. But even in the local repository be careful while using hard reset.
5. Using Git workflows may be overkill in very tiny projects. In these projects multiple developers will work on the same branch. But, before doing any major change in the remote repository, it is better to evaluate once if this will impact the other developers.

Hopefully this post gave some ideas about what can go wrong in Git and how to avoid it. ?

### About the author

I love technology and follow the advancements in the field. I also like helping others with my technology knowledge.

Feel free to connect with me on my LinkedIn account [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

You can also follow me on twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

My website: [https://adityasridhar.com/](https://adityasridhar.com/)

### Other posts by me

[An introduction to Git](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61)

[How to use Git efficiently](https://medium.freecodecamp.org/how-to-use-git-efficiently-54320a236369)

[How to become a git expert](https://medium.freecodecamp.org/how-to-become-a-git-expert-e7c38bf54826)

Originally published at [adityasridhar.com](https://adityasridhar.com/posts/how-you-can-go-wrong-with-git)

