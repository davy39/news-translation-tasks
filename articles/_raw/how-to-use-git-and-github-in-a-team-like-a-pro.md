---
title: How to Use Git and GitHub in a Team like a Pro – Featuring Harry and Hermione
  🧙
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-07T18:13:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-and-github-in-a-team-like-a-pro
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Frame-17---freeCodeCamp.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: teamwork
  slug: teamwork
- name: version control
  slug: version-control
seo_title: null
seo_desc: 'By Damian Demasi

  In this tutorial, you will learn how to work in a team with a central repository
  on GitHub. You will work on issues, commits, pull requests, code reviews, and more.

  I don''t consider myself an expert on Git, but I have learned a lot a...'
---

By Damian Demasi

In this tutorial, you will learn how to work in a team with a central repository on GitHub. You will work on issues, commits, pull requests, code reviews, and more.

I don't consider myself an expert on Git, but I have learned a lot about it in my first month working as a software developer. 

I wrote this tutorial to share how Git is used in professional environments. Bear in mind that there is not just a single way of using Git – so this is just one approach, and it may differ from what you see in your professional career.

A good read to start working with Git workflows is this [Comparing Workflows](https://www.atlassian.com/git/tutorials/comparing-workflows) tutorial.

## **The Project**

Harry and Hermione had the great idea of building a SaaS app to allow people to build their own potions online and share them with the rest of the world. They named it **Potionfy**, and this will be their first start-up.

![Image](https://media.giphy.com/media/BttC0fsMuGXVS/giphy.gif)

They decided to use GitHub as the central repository in which all their work was going to be stored. They chose React and Ruby on Rails as the app technology stack.

## **The Team**

Potionfy will be bootstrapped by Harry and Hermione themselves by using their savings. They will work their home garage and they expect to have an MVP ready in 4 weeks.

Let's see how they will work together in building the SaaS product and the obstacles they will have to overcome in doing so.

## **Initial Project Setup**

This project will use two fictional team members – Harry and Hermione – with two separate GitHub accounts. So you may want to start creating two accounts on GitHub for this.

Bonus: in order to simplify things, if you have a Gmail account you can use your Gmail address with a plus and a string after the first part of it, and all email communications will be centralised in one account, like so:

```
my_email_address+harry@gmail.com
my_email_address+hermione@gmail.com

```

More on this [here](https://support.google.com/a/users/answer/9308648?hl=en).

### Step 1: How to create two different GitHub accounts

In order to follow along with this tutorial, you'll need two different GitHub accounts. I chose to create two, but you can just use your own and create another one. Here is how my set-up looks:

![Harry and Hermione GitHub accounts](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o8n5im9orxfgn5cf19ch.png)

### Step 2: How to set up your local development environment

We are going to use a local development environment and set up Git on it. I decided to use a virtual machine running Linux, but you can use your own environment (I just want to avoid any kind of configuration problem with Git).

We have to make sure Git is installed in our system:

```
git --version

```

This command should return the version of Git that is installed in your system. In my case, my virtual Ubuntu didn't have it installed, so I ran:

```
sudo apt install git

```

### Step 3: teamwork considerations

Harry will be the one working locally in our development environment, and Hermione will choose to work directly on GitHub by using an online VSCode (more on this later).

## **How to Get Started Working on the Project**

### Step 1: How to create the repository and build the team (for free)

Hermione is the leader of the team, as she is more experienced in coding, so she has decided to create a new repository to host the code for the SaaS product. 

To create the repository, she simply used the GitHub web interface and clicked on the `Repositories` tab, and then on the `New` button. She named the repository `potionfy` and she added a short description and a `Readme.md` file.

![Potionfy repository](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/92a2v6z1asks9og4pows.png)

After the repository was created, she invited Harry to work on it. To do so, she clicked on the `Settings` tab in the `potionfy` repository, then in the `Manage access` option, and finally in the `Add people` button.

![Add people to the repository](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3veijbtrpirpxpx5qivl.png)

By entering Harry's GitHub username (or email address) in the pop-up window and clicking on the `Add Harry(...) to this repository`, she managed to send the invitation to Harry.

![Inviting Harry](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6o5mdaunh0wnbwil28c4.png)

A couple of seconds later, Harry received the invitation to his email:

![Invitation email](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/82utres034fp4hmpvkta.png)

He accepted it, and by doing so, both team members were ready to start working on their project.

**NOTE:** In case the invitation link does not work (as in my case), Harry needs to go to Hermione's GitHub profile, click on the `potionfy` repository, and accept the invitation there:

![Accepting invitation (part 1)](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/71u7wj0v3cicwnpinbhw.png)

![Accepting invitation (part 2)](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d4d69vm27g19jo6kcvbv.png)

### Step 2: How to create a file

Hermione started the project by creating the initial file the Potionfy SaaS product will use: `index.html`. 

In order to do so, she created the file using the GitHub web interface by positioning herself in the repository and clicking on the `Add file` > `Create new file` buttons.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2gdlz27zm8k8cpziv7be.png)

Then she added the name of the file, its content, and a meaningful commit message. After clicking on the `Commit new file` button, the file was created on the repository.

![Creating a file](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/si7jxizohz7adle8rtr0.png)

### Step 3: How to create an issue and work on it

Hermione needs to move on to work on the marketing related to Potionfy launch, so she told Harry to add a simple landing message to the `index.html` file. So, she proceeded to create an **issue** in the repository by clicking on the `Issues` tab and clicking on the `New issue` button.

![New issue](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rasnvg01wtaxt35p4oa8.png)

![New issue description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mgf8tpr35i1dbzpnno2l.png)

After the issue was created, Harry took a look at it (also by going to the `issues` tab in the Potionfy repository) and let Hermione know that he will be working on it by leaving a comment and assigning the issue to himself.

![Issue assignment](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6n6z1xfed0iy71y3nkpa.png)

By working with this dynamic, the team will know who is working on what.

### Step 4: How to set up the local development environment

In order to work on the project's `index.html` file, Harry chose to work locally, so he needed to clone the `potionfy` repository in his development environment (the Linux virtual machine).

The first thing he had to do was set up the SSH keys to work with GitHub. He followed GitHub's [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) tutorial to do so. He then added the key to his GitHub account, following the [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) tutorial.

Then, Harry opened Hermione's repository on GitHub and copied the link to clone it:

![Cloning repository](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vj9me394xsugdav4wouh.png)

Now in his local development environment, he created a new directory in which all his work would be centralised:

```
$ mkdir ~/development
$ cd ~/development

```

Finally, he cloned the repository by typing `git clone` and pasting the code he just copied from GitHub (which is the _address_ of the repository):

```
$ git clone git@github.com:Hermione-Colo-Codes/potionfy.git

```

In this way, he now has a local copy of the repository and he is ready to start working on it.

```
$ ll
total 12
drwxrwxr-x  3 parallels parallels 4096 Nov 17 07:34 ./
drwxr-xr-x 23 parallels parallels 4096 Nov 17 07:33 ../
drwxrwxr-x  3 parallels parallels 4096 Nov 17 07:34 potionfy/

```

### GitHub workflow

In order to work on a repository, this is the workflow GitHub recommends:

1. Create a branch
2. Make changes
3. Create a pull request
4. Address review comments
5. Merge your pull request
6. Delete your branch

For more information about this, you can read [this document](https://docs.github.com/en/get-started/quickstart/github-flow).

#### Step 1: Create a branch

As it is a good practice not to work on the master branch directly, Harry created a new branch related to the issue on which he will be working. 

He chose to do this on the GitHub repository, but he could have done the same in his local environment using Git commands.

He chose a meaningful name and prefixed the name with the number of the related issue (which is `1`, in this case).

![Creating a branch](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f6yne1wb24kctulcw654.png)

More information about how to create a branch on GitHub can be [found here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository).

#### Step 2: Work on the branch locally

After the branch was created, Harry started working on it.

##### `git pull`

The first thing he did was a `pull` of the whole repository so he could see the branch in his local development environment.

```bash
~/development/potionfy$ git pull
Warning: Permanently added the ECDSA host key for IP address '13.237.44.5' to the list of known hosts.
From github.com:Hermione-Colo-Codes/potionfy
 * [new branch]      1-add-landing-message -> origin/1-add-landing-message
Already up to date.

```

##### `git checkout`

With the new branch in his environment, he switched to it by using the `git checkout <name_of_branch>` command. After doing so, he ensured he was working in the correct branch with the `git branch` command.

```bash
~/development/potionfy$ git checkout 1-add-landing-message 
Branch '1-add-landing-message' set up to track remote branch '1-add-landing-message' from 'origin'.
Switched to a new branch '1-add-landing-message'

~/development/potionfy$ git branch
* 1-add-landing-message
  main

```

##### Solve the issue

Harry started working on solving the issue. In order to do so, he opened the `index.html` file and added a `h1` header to it.

![Making changes to the file](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1rhinjvy8z4ouozekolm.png)

After the changes were made, he saw how Git reacted to this change.

```bash
~/development/potionfy$ git status
On branch 1-add-landing-message
Your branch is up to date with 'origin/1-add-landing-message'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   index.html

no changes added to commit (use "git add" and/or "git commit -a")
parallels@parallels-Parallels-Virtual-Platform:~/development/potionfy$

```

He then added the file to the staging area with the `git add` command and committed the change with the `git commit` command.

```bash
~/development/potionfy$ git add -A

~/development/potionfy$ git commit -m "Add landing message. #1"

~/development/potionfy$ git status

```

Note how the commit message also includes the id of the issue, which in this case is `#1`.

##### Push to the repository

The next step Harry needs to do is to push the changes to the repository.

```bash
~/development/potionfy$ git push

```

![Pushing changes](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/spgnh14xpr1wnqlis2k3.png)

##### Create a pull request

Harry then clicked on the `Compare and pull request` button in the GitHub repository (making sure his branch was selected in the branch left drop-down menu).

![Pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9nsmrf4fbqloojq41tk0.png)

This pull request will be analysed by Hermione and she will decide if it can be merged to the master branch or not.

### Quick recap so far

Up to this point in the tutorial, we learned how Harry and Hermione decided to build a SaaS app to allow people to build their own potions online and share them with the rest of the world. They named it **Potionfy**.

Hermione created a remote repository, then an `issue` to address the task of building a landing page, and how Harry worked on that `issue` locally and created a `pull request` once he finished working on it.

Now, we are going to see:

* how Hermione reviews Harry's code,
* how the code is merged on the master branch,
* the decision of using a `develop` branch,
* how the team works in the develop branch and merges changes into main,
* and how the team solves merge conflicts.

![Image](https://media.giphy.com/media/VwUquCGtIatGg/giphy.gif)

## **How to Do Code Reviews**

### Step 1: How to create a code review

Hermione has finished with her marketing and promotion tasks, and she now has time to review Harry's code. 

In order to do so, she opens the GitHub repository and clicks on the `Pull requests` tab to find Harry's pull request.

![First pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qytmh2qm30u2tfxfdc1p.png)

After clicking on it, she then clicks on the `Commits` tab, and finally in Harry's last commit (this is just one way of accessing the files modified on the pull request).

![Reviewing code](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zr6b36csbr9btula3rh9.png)

She is not entirely convinced about the `<h1>` code, so she clicks on the plus icon that appears when she hovers that line of code, and writes a comment to Harry. Finally, she clicks on the `Start a review` button.

![Comment on the code](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2ws8b6hfmuo9kqmun15q.png)

As she has no other comments about the code, she now clicks on the `Review changes` button to make the review visible to the rest of the team.

![Making a review](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hybyz2iwa71gsqbztvum.png)

You can find more information about making reviews in this [Reviewing proposed changes in a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request) article.

### Step 2: How to address the review and create a code change

Harry checks his pull request and finds a new conversation there: Hermione's review.

![Working on the review](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pklnu1xdc1wmvf2mkl0f.png)

Harry answers Hermione's comment and clicks on the `Resolve conversation` button.

![Solving conversation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ofalfmz3ukitvnng7yha.png)

Now that the conversation is resolved, Hermione can submit the review indicating that **there are requested changes** so Harry can actually work on them.

![Submitting review](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/reok6k1teor9ho43vltv.png)

**Note:** this is just one version of the review process in GitHub, and it can differ from the actual way your team chooses to handle them.

Harry checks the pull request again and finds that it has `Changes requested`.

![Changes requested](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6rz496wfrvxdesf0ij75.png)

### Step 3: How to implement the changes

As Harry likes to work locally, he continues working on the branch he had created in order to implement the code changes.

```bash
$ git checkout 1-add-landing-message

```

Once he is sure he is working on the correct branch, he makes the changes in the `index.html` file.

![Implementing changes](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/no7pmw3pck2cpgi3nl5n.png)

**Note:** for simplicity sake, we are not creating a separate CSS file here.

Once Harry finishes tweaking the code, he stages the changes, commits them (making sure to include the `id` of the issue because he is still working on it), and pushes them to GitHub.

```bash
$ git add -A

$ git commit -m "Add colour and remove text. #1"

$ git push

```

### Step 4: How to merge the pull request

Now it's Hermione's turn. She goes to the pull request and finds a new commit: the one Harry did and pushed to GitHub.

![New commit](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4n6yso4pn6rfkdj0xioj.png)

She then clicks on the `Files changed` tab and finds the ones that she suggested implemented on the `index.html` file.

![Changes in the file](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tmudklpfre4op0afjem3.png)

As she is satisfied with the changes, she proceeds to approve them by clicking on the `Review changes` button and selecting the `Approve` option.

![Approving changes](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/c7soa00zfq791oa50b9j.png)

Harry sees that his pull request was approved by Hermione, and he proceeds to merge it into the main branch of the project.

![Merging pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6hdjyzbh1vxpyhf9joy0.png)

He decided not to delete the branch, as he wants to leave it there for future reference (although it would be a good idea to delete it).

As Hermione is satisfied with how the issue was solved, she proceeds to close it by going to the `Issues` tab and clicking on the `Close issue` button.

![Closing issue](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/reqhbp9nrmvzxj46d9ms.png)

If you want to see a graphical representation of the whole process up to this point, you can click on the `Insights` tab and then on the `Network` option. You will be able to actually see how the branching and merging were performed.

![Graphical representation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u87v2ie8y93dq8ielyuq.png)

## **How to Use a `develop` Branch in Git**

When working with real projects, merging changes into the main branch like you saw up to this point is not recommended. 

Instead of working directly with the `main` branch (often called `production`), you will be working with a `develop` branch. You will be branching issues out of that `develop` branch and merging them back into the `develop` branch. 

Once a group of issues have been solved, that `develop` branch will be merged into the `main` (or `production`) branch, usually denoting a version change in the app.

![Develop branch](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/94wbcj99uvf39ax8f3ab.png)

Hermione is aware of this, and now that the landing page is live and accessible to customers, she decided to preserve that _production environment_ and work on a development branch. 

In order to do so, she creates a `develop` branch out of the `main` one, so she and Harry can work on that branch without impacting the production environment.

![Creating a develop branch](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d7okjo7adstn9af3rymu.png)

## **How to Handle Merge Conflicts in Git**

Hermione wants to add a new feature to the landing page: a form to capture clients' emails. In order to do so, she creates a new issue.

![New issue](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4v5lyxbk8a18fjvet99o.png)

Once the issue is created, Harry decides to start working on it. To do so, **he branches out from the `develop` branch** (by selecting that branch on the GitHub interface) a new one called `3-email-form` (including the issue number at the front to make it clear how this branch will relate to the issues).

![New issue branch from develop](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/km1xvg06alcri2d3q2uk.png)

He then pulls that branch locally and starts working on it.

```bash
$ git pull

$ git checkout 3-form

```

Harry decides to include a simple form into the `index.html` file:

```html
<form action="mailto:hermione@potionfy.com" method="post" enctype="text/plain">
Name:<br>
    <input type="text" name="name"><br>
    E-mail:<br>
    <input type="text" name="mail"><br>
    <input type="submit" value="Send">
    <input type="reset" value="Reset">
</form>

```

**Note:** This code is just to exemplify how Harry is working on a file and it's not how this type of form could actually be built.

Harry stages and commits his changes locally using the `Contact form. #3` message.

```bash
$ git add -A

$ git commit -m "Contact form. #3"

$ git push

```

![Image](https://media.giphy.com/media/7Yif3ae99ksCc/giphy.gif)

Before Harry could create a new pull request, Hermione decides to build a placeholder for the form on the `index.html` file on her own. In order to do so, **she creates a new branch** out of `develop` called `3-email-form-placeholder`.

![Hermione's branch](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vtqld9mij5mxoj56qx4r.png)

To work on the `index.html` file, she uses the GitHub online code editor (basically, a VSCode for the web). In order to open it, she just presses the `.` key on her keyboard and the GitHub page is transformed into a VSCode interface (like magic 😉).

![VSCode online](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/agznz5qsohwq8w7xh4xx.png)

She then proceeds to add the following code to the file:

```html
<form action="mailto:harry@potionfy.com" method="post" enctype="text/plain">

</form>

```

After saving the file, she commits the changes right there on her browser window by using VSCode's graphical interface:

![Committing changes](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/26bow6vevor0j2bz3g1e.png)

Once the commit is complete, she opens GitHub again and decides to create her own pull request and merge her changes to the `develop` branch.

![Creating a pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4ucvh19hp86eh6vwth49.png)

![Merging changes to develop](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/s5p2ldzkvch67ziutdw5.png)

![Image](https://media.giphy.com/media/OUwzqE4ZOk5Bm/source.gif)

On the other hand, Harry also decides to create a `pull request` to merge his changes into the `develop` branch.

![Harry's pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/slmwjb3s1z263tnbhvye.png)

At this point, GitHub lets him know that his pull request won't be able to merge automatically to the `develop` branch.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xvyambidieetr4u3puhi.png)

Harry supposes that his branch is no longer reflecting the state of the `develop` branch and that the `develop` branch has changed because someone else merged changes affecting the `index.html` file on which he was working on. Nevertheless, he proceeds to create a pull request.

What he sees next is GitHub's way of letting him know that there is a conflict affecting the file he modified. He proceeds to click on the `Resolve conflicts` button.

![A conflict](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gtxo3qpizp3gfcfpeo14.png)

He can now see that the `index.html` indeed was modified, and the changes made to that file are affecting the lines he himself modified.

![Conflicting changes](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bdg7jgxt3zcrwbn6p66h.png)

For more information about solving conflicts, you can read the [Resolving a merge conflict on GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github) article.

Harry proceeds to modify the file directly on the GitHub site to remove the conflicting changes and then clicks on the `Mark as resolved` button.

![Solving conflict](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9ijk9wdc6aenfwbzrt8z.png)

Once the conflict is marked as resolved, he clicks on the `Commit merge` button.

![Commit merge](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cp87juwh255hou1kipgv.png)

Finally, his branch was conflict-free and he can merge his pull request (assuming Hermione reviewed his code and approved it, just as she did earlier).

![Merging pull request](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7m3lr63hu68nv0xdk15i.png)

Conflicts ofter arise when teammates are working on different branches that affect a common file. A great way to prevent merge conflicts is to do a `pull` request on the `develop` branch, merge that updated `develop` branch into the branch you are working on, and then do a `push` followed by a `pull request`.

```bash
$ git branch
x-my-branch # This is an example name

$ git checkout develop

$ git pull

$ git checkout x-my-branch

$ git merge develop

# You make some changes on the files of the x-my-branch branch

$ git add -A

$ git commit -m "<a message>"

$ git push

```

## **Final Thoughts**

After working on their landing page, Harry and Hermione managed to get lots of email addresses from potential customers and continued developing their MVP. They managed to get funding from a local venture capital firm, and they are now in the process of hiring other developers to launch Potionfy to the public. 

I'm sure they would love to take a look at your resume to consider you for a position in their company, so good luck!

![Image](https://media.giphy.com/media/gbErpwcLlizvi/giphy.gif)

🗞 If you enjoyed this article, you may like other articles I publish. The best way to know about them would be by [**subscribing to my newsletter**](https://mailchi.mp/22b236f812b1/subscribe-to-newsletter).

🐦 You can follow and contact me on my [**Twitter**](https://twitter.com/DamianDemasi) account.

Cheers!

Damian.-

