---
title: Pulling the little squid with Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T19:46:17.000Z'
originalURL: https://freecodecamp.org/news/pulling-the-little-squid-with-git-bc074476433b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XTKufkr__czE7CF_VUGIMw.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Iago Rodrigues

  Have you ever changed something directly in your project’s repository? Have you
  ever merged a branch into master? Then wanted to pull the changes to your local
  repository and had some trouble with it?

  If you don’t know what the mean...'
---

By Iago Rodrigues

Have you ever changed something directly in your project’s repository? Have you ever merged a branch into master? Then wanted to pull the changes to your local repository and had some trouble with it?

If you don’t know what the meaning of “pulling a repository” is, you are in the right place. Do want a cup of coffee?

### A brief intro

In this article, we are going to cover the different events that might occur when you pull commits which are ahead of your local ones.

By “ahead of yours,” I mean commits that exist on your remote repository (the one on GitHub servers). These commits do not exist on your local repository (the one on your machine).

So, let’s get some hot coffee — I offered one to you — and let’s figure these things out.

For the sake of the learning, let’s create a repository on GitHub with no files added — we’ll cover this later. You can name it whatever you want.

Now we can go to a directory in our machine to clone our project. If we haven’t yet created a directory which serves as our Hub, we can create one so we can store our projects from GitHub. Pick odds or evens to decide about it.

If you don’t know what I’m talking about, please check [this article](https://medium.freecodecamp.org/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba) out.

Now, let’s check out the events which can occur when we need to `git pull`.

### Pulling when we don’t have local changes

That’s the easiest situation. This happens when we have created the remote repo and added some files which we don’t have locally yet. We also don’t have changes on our local repo.

Ok. First, let’s go to the folder created when we cloned the project. It has the same name.

It’s time to create some files on GitHub. On our project’s page, create a README file. Easy peasy!

On our computer, let’s open CMD or any terminal application (like cmder) and type in `git pull origin master.` You’ll see the magic happening.

![Image](https://cdn-media-1.freecodecamp.org/images/2K5RaCUk7rZolYY8Z5z7-VBl6DytGbqtLuEP)
_Pulling without local changes._

Now we have those changes locally too. Pretty cool, right?

### Pulling when we have local changes which weren’t committed yet

Awesome. Let’s create some files. You can open up your local project folder on your favorite code editor. I recommend using [VSCode](https://code.visualstudio.com/) though.

With that, create a .`gitignore` file and add some stuff there.

![Image](https://cdn-media-1.freecodecamp.org/images/Ae6zrXTktQT2jwd9bk5uk6jQcoyviB19-pMK)
_Creating a local .gitignore file._

Now we have local changes, but we didn’t commit these changes. We are not going to do this yet.

Let’s head to our remote repository. Create another file there. It can be a LICENSE.md. Do as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/tLr1vGeHXPAAU1YhnrfrbbCUYNHcQTIvxXnZ)

1. Type in LICENSE on the input.
2. Click on **choose a license template**.

![Image](https://cdn-media-1.freecodecamp.org/images/junhzv57ioV9K7TsQYdWsPK3IUfuuEgBtOOU)
_Creating a LICENSE file._

On the next page, choose **MIT License** and click on **Review and Submit**. Feel free to read the license if you want to.

Your file should look like the one in the picture now, with your GitHub name, of course.

Now we can commit this. Head down the page and click on **Commit new file**. Make sure the first option is selected.

![Image](https://cdn-media-1.freecodecamp.org/images/TDjiHa9txi1YZbmhgXpGPdnZJhmWT4barFmy)

You can leave the fields empty (it uses the same text of the placeholder) or type something else if you want.

So far we have changed both remotely and locally. However, we haven’t committed our local changes. Leave it like that.

Let’s pull the changes and see what happens?

![Image](https://cdn-media-1.freecodecamp.org/images/SbqBazR5L5rsFxeoZfsSfW8dDt1J4kSUeQto)
_Pulling remote changes when we also have uncommitted local changes._

Cool! We could pull without problems. This happens because we changed different files. Further on we’ll see what happens when we modify the same file. Hang on in there!

### Pulling when we have local commits which weren’t pushed yet

Ok. Now, let’s commit those local changes. If you type `git status` you’ll see that we have an **untracked** file. That means we didn’t add the file and Git isn’t tracking it.

So, let’s add and commit the file. Don’t `git push` yet!

![Image](https://cdn-media-1.freecodecamp.org/images/JTqpt9wiBl0BzhvGHpxpJjcDqryVL91pi5pu)
_Committing local changes._

Let’s add another change to the remote repo and commit it as well. It could be an `index.html` file.

If you type `git status` you’ll see that our local and remote repo has diverged. They both have 1 (one) different commit.

![Image](https://cdn-media-1.freecodecamp.org/images/DYuIo8wyl6fHY6aXeazKsTOAZEjoxKuE-mKi)
_Diverged commits on both repos._

Let’s try to pull those changes now and see the status.

![Image](https://cdn-media-1.freecodecamp.org/images/7qjDaxbt-gO1P64uK6u22WbNzPJDqWwH5rHg)

Look at that! Git pulled the changes recursively on the remote repository and merged them automatically into our local commit stack. So, we are safe to pull changes this way too.

#### What if we have changes on the same file?

Nice. We saw that when we change different files, we can use `git pull` without problems.

However, what happens when we change the same file on both repositories?

Before we continue, we should do `git push origin master` on the local modifications that we made earlier. This way we don’t have any modifications, and we are equal with the remote one.

We can now modify something. Let’s say, modify the README file locally and commit the changes. Don’t push it yet.

Go to the remote README file and modify it too. Commit it.

We are in the “same” situation as before, with one different commit on each side.

If you try to `git pull` the remote one, this is what we see:

![Image](https://cdn-media-1.freecodecamp.org/images/U7PCDo4Uidp1O3u9F2KuGKMjJRQhqrQ3Ki2A)
_Pulling diverged commits on the same file._

![Image](https://cdn-media-1.freecodecamp.org/images/ZfMX05KfWzblDyI6oyxL62D9vCrARsuwIG9H)

Git will try to merge the changes automatically, but since we have different changes on the same file, it fails.

We have to merge the remote commits into our local ones manually, so that we can continue our work.

First, we have to fix the conflicts on the file. If you are using VSCode, we can go to the **Source Control** tab and handle this there.

![Image](https://cdn-media-1.freecodecamp.org/images/L67xfS6-UYxx-xujc4PMyXRZ-vBgOcwnhi-r)
_Handling conflicts on VScode_

This is very simple here. **Accept the current changes** means we accept only the remote changes. **Accept the incoming changes** means we accept only our local changes. We can also accept both changes with the **accept the both changes** option.

With that, we can add and commit the file. If we check the status now, we see that we are 2 commits ahead of the remote repository. That means we successfully **merged** the file.

We can now push it and check the modified file on GitHub.

Phew! Eh?! This one gave us a bit of work. But it isn’t rocket science, right?

Praise the sun ☀️my friend. Now we are going to work.

### What if we already have a project to send to GitHub and a remote repo with stuff in it?

Ok! That’s a long question. But it’s an important one. It’s another situation that we need to look into.

Let’s say we have installed a template with some code. A [template](https://github.com/vuejs-templates) in the dev world is a set of pre-made code which we can use to jump-start our project and mold it to our way.

So, now we have a directory with some code, and we are going to `git init` this folder so Git can start to listen to our changes.

Cool. Now, we want to send this project to GitHub. Pretty simple, right? Just need to create a remote repository. But, let’s say we created this repo and we added a readme, license, index.html and a .gitignore file.

Hmmm … we didn’t pay attention that our template has already put those same files on our local repository.

So if we try to pull, we have the same problem as before — different changes on both sides.

For the sake of the article, let’s say we are going to pull these changes anyway. But before we handle this, we should link our local project to the one on GitHub.

Run the following code: `git remote add origin <github's project li`nk>

The **GitHub’s project link** is the same one that we use to clone the repository. If you don’t know what that is, please read [this article](https://medium.freecodecamp.org/how-you-can-learn-git-and-github-while-youre-learning-to-code-7a592ea287ba?source=activity---post_recommended).

Ok. Now that we did that, we can start to pull and push some stuff. But if we try to pull the changes now, you know what happens, right?

![Image](https://cdn-media-1.freecodecamp.org/images/IeVwSPmPniKFqoHv7aHFAoK-eEgjETo4q8XJ)

This is pretty simple to workaround. Just add and commit our local changes. As this is our first local commit, we can do this:

```
git add --allgit commit -m "first commit"
```

With that, we can try to pull again. Keep in mind that we should use `git pull origin master` as it’s the first pull that we are doing on this repository.

We should get the following message:

![Image](https://cdn-media-1.freecodecamp.org/images/bGp82lzUrVEMiaLMwt1Yjz0n7spkVxkEMsj4)

We can’t pull the changes, because Git doesn’t want to. ? ? Great! Thank you, Git!!! ?

To solve this, we need to merge the files. But we have a much more efficient way. Run the code `git rebase origin/master` .

We receive the following message:

![Image](https://cdn-media-1.freecodecamp.org/images/OewthvVVeubJFduxbdTnBVdMesvgpdtOI5Rl)
_Running git rebase._

Rebasing is pretty awesome. It’s a better alternative to `git merge` . It does the same thing but in a better way. You can find more about it [here](https://git-scm.com/book/pt-br/v1/Ramifica%C3%A7%C3%A3o-Branching-no-Git-Rebasing), but don’t worry too much. In later articles, I’ll explain this.

We must resolve the conflicts now. We can go to VSCode to do that.

![Image](https://cdn-media-1.freecodecamp.org/images/EOztFE2j4VPI9rA9dQNLSQ3gNVQLVTvacR4a)

Pay attention to a couple of things in here.

First, the files that have conflicts are the ones under the **merge changes** tab.

Second, when we ran `git rebase` it added again all of our files to the staging phase— the same stage we are at after running `git add` — but the ones with conflicts.

Third, on the bottom left bar of VSCode, we can see a series of numbers. Well, **git rebase** created this branch. Don’t worry, though. We will get back to the **master** in a second.

Ok. Now that we resolved the conflicts, we can add the files. If you want to avoid the conflicts, you can remove the files but I don’t think that’s a good way to solve this. Unless you don’t need them.

We can add more than one file with this command: `git add .gitignore index.html README.md` .

After that, we are going to rebase the remote commits with our local ones. We can accomplish this with the command `git rebase --continue`.

![Image](https://cdn-media-1.freecodecamp.org/images/uti5MpL2fURrhCUGKJMk7Vh1M3Jv3vcUWORN)
_Adding the resolved conflicts and rebasing the commits._

Now all the commits on the remote repository are merged or rebased with our local commits. We are also back to the master branch.

We can check the commits with `git log` .

![Image](https://cdn-media-1.freecodecamp.org/images/afoDMA6PHO8X8obLUbYpTeE87IE38f8syi15)
_Checking the log with all the commits rebased._

Pretty cool, right? These are the events we can encounter when pulling changes from remote repositories on GitHub.

Well, that is it for now, guys. I hope this article helped you in some way.

I plan to do a series of articles for beginners regarding Git and GitHub. So stay tuned for more.

See you next time. Peace! ✌️ ✌️ ✌️

I’m Iago Rodrigues, Brazilian from Belem, Para. I’m an Information Systems student, a software developer intern, and a freelancer. I’m at the beginning of my career and just wanted to share some knowledge that I’ve acquired with you.

You can follow me on social media. Always a pleasure to help where I can.

[**Iago Rodrigues - Estágio Analista de Software - W3 Automação e Sistemas | LinkedIn**](https://www.linkedin.com/in/iago-rodrigues/)  
[_View Iago Rodrigues' profile on LinkedIn, the world's largest professional community. Iago has 3 jobs listed on their…_www.linkedin.com](https://www.linkedin.com/in/iago-rodrigues/)[**Iago Rodrigues (@iagokv) | Twitter**](https://twitter.com/iagokv)  
[_The latest Tweets from Iago Rodrigues (@iagokv). Front-End Developer | Vue.js padawan | Noob on life. Belém, Brasil_twitter.com](https://twitter.com/iagokv)

Yeah! I know. My twitter photo is something …

