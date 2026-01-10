---
title: A simple Git guide and cheat sheet for open source contributors
subtitle: ''
author: Saheed Oladele
co_authors: []
series: null
date: '2019-07-12T17:18:51.000Z'
originalURL: https://freecodecamp.org/news/a-simple-git-guide-and-cheat-sheet-for-open-source-contributors
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca17a740569d1a4ca4ed1.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: GitLab
  slug: gitlab
- name: open source
  slug: open-source
seo_title: null
seo_desc: 'A go-to git cheat sheet for your open source contributions.

  If you’re reading this article, you already know that the benefit of open source
  contribution abounds. You can skip the article and navigate to the end if you’re
  here for the cheat sheet.

  Th...'
---

A go-to git cheat sheet for your open source contributions.

If you’re reading this article, you already know that the benefit of open source contribution abounds. You can skip the article and navigate to the end if you’re here for the cheat sheet.

The common problem faced by aspiring open source contributors is how to take the first step _from fork to pull request_. After reading this article, you should be well equipped with all you need to make your first open source pull request.

Apart from making the process easier for you, the git workflow defined in this piece also makes your contributions look professional. This is especially useful in case you want to add your open source contributions to your portfolio.

### Prerequisites

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-240.png)
_Photo by [Unsplash](https://unsplash.com/@randyfath?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Randy Fath</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

This article assumes you already know the steps to take to contribute to open source. If you don’t know, you may want to read [this article written by Maryna](https://rubygarage.org/blog/how-contribute-to-open-source-projects). This piece also assumes that you’ve already setup Git on your PC. If you haven’t, you may want to check the [setting up Git section of this article](https://help.github.com/en/articles/set-up-git) and do that first.

### Step 1: Fork the project

This is as simple as clicking a button on GitHub. Navigate to the repository of the project you want to contribute to, then click the fork button at the top right corner as illustrated in the picture below.

![Image](https://lh4.googleusercontent.com/4u1uvX1dRTkG0RLXeWqt6N7-Ed2BeNiOfG8KgXsiOAE-quBpq2rDKS2d6dkxyEWbMThVJu4bgeqU9aKO-vhxyj5XULbRxpV0WedoctN0wm_RhgSyzg5ICn4aZUkk99BwBj2ugCBv)

After using the fork button, you’d now have the repository on your GitHub account.

### Step 2: Clone the project to your local machine

This is the simplest part of Git. Navigate to your forked repository (the repository is now one of your GitHub repositories). Follow steps 1 and 2 as shown in the image below to copy the clone address. This address should look like this: `https:[github.com/suretrust.com/freeCodeCamp.git](http://github.com/suretrust.com/freeCodeCamp.git)`

![Image](https://lh5.googleusercontent.com/lyeLwQ6uz-VcEFoQcEGNf5KQiSzaDz1iwefGwi4CAoxuqiOdUPBm_jxVz1GJMgjHYHYkzGIHKb1l7iPdTQ5OIu3WUzK_ouFHHGAruNe-WJVKBsWpPgyLD5EClWnj7kaxsszwFqHB)

Then, clone the project by typing `git clone <the copied address>` into your command terminal as shown below:

`git clone [https://github.com/suretrust/freeCodeCamp.git](https://github.com/suretrust/freeCodeCamp.git)`

### Step 3: Create upstream

The upstream is necessary to keep track of the difference between the forked repository that is on your Git account and the original repository. This is most useful if you want to contribute to a popular repository.

Some repositories merge pull requests hourly or less, so be safe and assume that the forked repository you have will be behind the original repository. 

**Note that the upstream is in the freeCodeCamp repository and not your forked repository.** Follow steps 1 and 2 as shown below to copy the upstream address:

![Image](https://lh6.googleusercontent.com/-fIOwK3jSHRJQrtVdCbGYc_0xFxPt-I22JmCqIom7f5F53iKceawsfju-NBw_wQ5LtRmsk9gJB3qJfA28ujR01lhF8VQKvvercoigfnVUbKNHrgOalp4OXz5CH6tXX46ev7d6Acv)

To create a link to the original repository, copy and paste the following command into your terminal:

`git remote add upstream <upstream address>`

You can use `git pull upstream master` to confirm if there has been any change at the moment (from when you forked the repository to now).

### Step 4: Create the branch you want to work on

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-241.png)
_Photo by [Unsplash](https://unsplash.com/@_zachreiner_?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Zach Reiner</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

It is nice to create a new branch whenever you want to contribute. This illustrates that the branch is only for that contribution you are about to make. It could be as small as fixing a typo or as large as implementing a new feature. Either way, it’s good practice to create a branch.

Another important part of the branch creation is naming. It is pleasing to use a name that a stranger who knows nothing about the repository can easily understand. If you want to add a login feature, for example, you could create a branch called `add-login-feature` or `login-feature`.

To create a branch type the following command into your terminal:

`git checkout -b <your branch name>`

This command will create the branch and navigate into it. If your branch name is login-feature, then you can use the following command:

`git checkout -b login-feature`

_**Then add your contributions. After adding your contribution, move on to Step 5.**_

### Step 5: Git add and commit your contributions

This is quite simple as well. Stage and commit your changes by typing the following into your terminal.

`git add .`

`git commit -m 'Commit message'`

Now, you have the changes staged and committed. What next?

### Step 6: Pull from upstream to the branch

As I explained in step 4, this step is to merge any difference in the upstream into the branch so as to prevent conflicts.

`git pull upstream <branch name>`

This merges the upstream changes into your current branch.

### Step 7: Push to the branch you’re working on

Now, you are almost there. Push your changes to the branch you are working on as shown below:

`git push origin <branch-name>`

### Step 8: Open a pull request

This is the final step for any open source contribution, you are simply saying ‘I have made some changes, would you mind adding it to the project?’.

You open a pull request and if the repository owner or members like what they see, they’ll merge it. Otherwise, they could make changes then merge or request for changes.

To open a pull request, navigate to the forked repository as shown below. You’ll see your last push branch `‘login-feature’`, then click on `‘compare and pull request’`.

![Image](https://lh5.googleusercontent.com/GHcFpgR70pKrxpyhfNDnPRvVluSPF-gz2ICUKv1Q3uxZKEaBcwv32E8Rh7d-5yNS9uvGXWzCcoc22KBbddEOybzP7BkONlKdqXXmFtdcqIm6AU5ebZjAZeFV0iL7PMulwrnT8MnA)

Explain clearly, the changes you made, then open a pull request as shown below:

![Image](https://lh4.googleusercontent.com/4yGQB3_1-2IyGDiOAfNec1yyoMXyvEzUAEcShTx4xf8_DU5vgfhFN0Uihn0A-BZzKGJkeCnjDbQkXT_AKtTCsgAnXK6vDcIWuvWY5ETmUH4MORXT7kgz_4qKVnD2zj1bLcQRTWf1)

  


And that’s it. :) You can now go ahead and contribute like a PRO!

## Git cheat sheet for open source contributors

![Image](https://lh5.googleusercontent.com/ZoVAty5u4vZaFdwBXh2fpsPQMsgW_3qxnt_dCo8Qn5ayk-fdvIZh6D6jSY_GdUhW8yUZvIIaBc_6WoLTyWseX3M8m7yPIzA8f4fL6X_oikH5wRcykopNH1KPI7eEuiz_8-M-jnZm)

  
Peace out and happy contributing!

  

