---
title: Git Squash Commits – Squashing the Last N Commits into One Commit
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-22T23:16:43.000Z'
originalURL: https://freecodecamp.org/news/git-squash-commits
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/squashCommits.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: null
seo_desc: "If you are working on a project and trying to implement a new feature,\
  \ you might commit your code a few times to test things out. This lets you see how\
  \ the code works or looks. \nWhile doing this, things might get messy because you\
  \ now have several co..."
---

If you are working on a project and trying to implement a new feature, you might commit your code a few times to test things out. This lets you see how the code works or looks. 

While doing this, things might get messy because you now have several commits, even for things that aren’t necessary. 

Because of this, you might want to combine all those commits into a single commit. This process is called **commit squashing**.

In this article, I’ll show you how commit squashing works in Git so you can combine several messy or unecessary commits into one commit without losing your changes.


## How to Squash Commits in Git with Interactive Rebase
In this process, you will grab all the commits with the `git rebase` command with the `i` flag and put them together with `squash`. Apart from squashing, the command also allows you to drop commits, reword commit messages, and add new files.

I have these commits I would like to combine into one:

![Screenshot-2023-03-22-at-11.10.52](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.10.52.png)

Note that I have two branches – `main` and `new-feature`. I want to squash all the commits in the `new-feature` branch into one commit.

I could see those commits because I ran the command `git log --oneline`. They are also on GitHub already:

![Screenshot-2023-03-22-at-11.11.23](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.11.23.png)

The first thing you need to do is to tell Git how far back you want to rebase. So if you want to squash all those commits in the `new-feature` branch together, you need to go back 6 commits.

To do that run this command:

```bash
git rebase -i HEAD~6
```

This will open up your editor of choice for Git. The default is Vim, but in my case, it is VS Code. This is what the editor looks like:

![Screenshot-2023-03-22-at-11.28.12](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.28.12.png)

Now, you need to replace all those `pick` with `squash` (or simply `s`) apart from the first one.

**Note:** `pick` or `p` will only use those commits, but `squash` or `s` will use them and combine them all together.

The first commit is the one you will combine them into without losing your changes.

After doing that, save the file and close it. Git will open up another editor where you can see the new commit message it generates for you:

![Screenshot-2023-03-22-at-11.36.02](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.36.02.png)

You can get rid of all of them and add your custom message:

![Screenshot-2023-03-22-at-11.37.45](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.37.45.png)

Or you can leave it as is. If you add a new commit message, save the file and close it.

After doing that, you should see a success message in the terminal. 

Check your Git log again by running `git log --oneline` and you should see all the commits have been combined:

![Screenshot-2023-03-22-at-11.41.21](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.41.21.png)

Remember that the new commit message is "Ready to deploy". If you push your branch to Git, you'll see one commit message too:

![Screenshot-2023-03-22-at-11.43.07](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.43.07.png)


## How to Squash Commits in Git with the `merge` Command and `--squash` Flag
You can also combine multiple commits into one when you’re about to merge branches.

This helps clean up the incoming branch of redundant commits. The downside of this approach is that you don’t have much control as you do with `rebase`.

To do this, I’m going to undo the squashing I did in the last step by running `git reset --hard HEAD@{7}`.

Running `git log --oneline` again, I can see all the commits once more:

![Screenshot-2023-03-22-at-11.54.06](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.54.06.png)

I pushed the branch to GitHub again, so I can see those commits there too:

![Screenshot-2023-03-22-at-11.56.32](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-11.56.32.png)

Now, to do the squashing with the `git merge` command, I’m going to switch to the main branch by running `git switch main`.

To merge the `new-feature` branch to `main` and squash the commits there, I’ll use the `git merge` command with the `--squash` flag:

```bash
git merge --squash new-feature
```

If you run `git log --oneline` at this point, you won't have any commit on the `new-feature` branch yet:

![Screenshot-2023-03-22-at-12.00.25](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.00.25.png)

But if you run `git status`, you will see changes and files you need to commit:

![Screenshot-2023-03-22-at-12.01.11](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.01.11.png)

If you’re using VS Code, you will also see the Git tab indicating that you have some changes to commit:

![Screenshot-2023-03-22-at-12.02.24](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.02.24.png)

Now, commit the files with a suitable message. After that, run `git log --oneline` and you’ll see your new commit message:

![Screenshot-2023-03-22-at-12.04.33](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.04.33.png)

After pushing to main, creating a pull request on GitHub, and merging it, this is what I see in the `main` branch:

![Screenshot-2023-03-22-at-12.09.12](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-22-at-12.09.12.png)


## Conclusion
This article showed you how to squash multiple commits into one commit in two different ways. No matter the option you choose, the end goal of combining the commits gets met.

If you want to have more control, you can use the `rebase` with `i` flag option. But if you don’t want to go through that process, you can squash the commits while you merge. Just be aware that with that option, you need to commit your changes again.

Thank you for reading. If you find this article helpful, share it with your friends and family.


