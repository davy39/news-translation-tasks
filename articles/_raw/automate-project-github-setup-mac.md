---
title: How to automate your project and Github repo setup from the command line
subtitle: ''
author: Zubin Pratap
co_authors: []
series: null
date: '2019-08-20T08:59:00.000Z'
originalURL: https://freecodecamp.org/news/automate-project-github-setup-mac
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/octo.png
tags:
- name: automation
  slug: automation
- name: GitHub
  slug: github
- name: Scripting
  slug: scripting
- name: workflow
  slug: workflow
seo_title: null
seo_desc: 'This post comes out of an irritation I faced personally, when I was first
  learning to code - setting up my local repo and syncing with Github.

  I learned by doing projects (often freeCodeCamp ones!). But I needed to make sure
  I didn''t lose my hard wor...'
---

This post comes out of an irritation I faced personally, when I was first learning to code - setting up my local repo and syncing with Github.

I learned by doing projects (often freeCodeCamp ones!). But I needed to make sure I didn't lose my hard work, and that others could see the hard work I was putting in, so every project *had* to go on Github. [The more complete projects I had on Github, the easier it would be for recruiters](https://www.freecodecamp.org/news/learned-to-code-job-ready-and-heres-why/). But the steps required to set up a project, initialise a repo, and sync with Github were really annoying and repetitive, so I decided to solve the problem.

Bad news: this isn't going to be a big, fancy, detailed and technically sexy post. It's going to be very un-sexy.

Good news: you don't need to be a shell scripting god(dess) to do it.

So my typical project setup work flow usually goes like this:

1. Go to my `../projects` folder and run `mkdir project-of-some-name` to create a folder with the name `project-of-some-name`.
    
2. `cd` into that project folder and do `git init` to initialise a local git repo in there.
    
3. run `touch README.MD` to create the `README` file, open it and add some basic descriptions, including links to the resources / tutorials I was implementing in that project. Save the file.
    
4. run `git add .` and then `git commit -m ' ...some initial commit message...`
    
5. open a browser, go to Github, login, create a new (remote) repository, copy the url, return to my terminal, make sure I was in the correct project folder `project-of-some-name`...then run the git scripts needed to set up the remote repo as the 'upstream' repo and connect my local repo to it. Then, finally, I can run a `git push` and my local commit would get pushed up
    
6. lie down and take a nap, exhausted from this repetitive process.
    

Admittedly, this was my process, but I liked to stay organised and always be able to access my projects so I can refer to them.

Since automation is a great way to practice your coding skills, I decided to write a small shell script that automates these horrible and repetitive steps. The script is at the bottom of this post, and be warned - it's not sophisticated or fancy. But it sure gets the job done, and I don't need to log in to Github and fool around will all those steps!

Before you copy the script, you need to know how to run it on your Mac. So below are the steps you need to implement to be able to use the script to automate your setup workflow.

1. I keep my scripts in my root/home folder, in a sub-folder called `scripts`. I suggest you do the same or similar. To get to the root/home folder, in your terminal type `cd ~` because the tilda ( `~` )is the symbol for the home folder. In your Mac Finder app it shows up as the one with a house icon. So all my scripts are stored in `~/scripts`
    
2. This matters because to run a shell script from any directory in the terminal, you have to type out the full path. In my case I have to type out `~/scripts/git-script.sh` to run the script. But we're getting ahead of ourselves.
    
3. copy the code chunk at the bottom of this post and then open a text editor, paste it in and then save it as `[filename].sh`. The `.sh` is the extension for shell scripts. Save the file in the directory you want to save it at - again I recommend `~/scripts` as the folder to save your scripts in.
    
4. Navigate to that folder in your terminal. To be safe run `ls` in the terminal to check that you can see the script is there. If it's not you're in the wrong folder or step 3 didn't successfully complete.
    
5. Make the shell script executable. To do that you type the following in the terminal: `chmod +x <<the-correct-filename.sh>>`. This is the unix way to make a shell script "executable". I'm not confident I fully understand what that means, other than it's needed to make any shell scripts you write executable, so don't ask me and I won't lie to you.
    
6. navigate to your projects folder and make a new folder that you intend to house your project. Effectively, you've got to do this: `mkdir` - create a `project-of-some-name` inside the folder where you keep all your projects. So your project will eventually be placed inside `my-computer/my-projects/project-of-some-name`. `cd` into this folder and then type `pwd` to get the full path. Copy that - you will need to paste it shortly. It should look like `my-computer/my-projects/project-of-some-name`
    
7. open your terminal again, and then type `~/scripts/`&lt;&lt;the-correct-filename.sh&gt;&gt;\`\`. The script runs! You will be guided through some input... The main steps are:
    
    > what do you want to call your Github repo (**don't use spaces-** 'my-awesome-project' is good. Don't use 'my awesome project' as the repo name.
    
    > Enter a description that shows up in the Github repo's description. For this it's safe to use spaces.
    

> Enter the project path you got in step 6, the one that you get after typing `pwd` in the terminal and getting something like `my-computer/my-projects/project-of-some-name`

> enter your Github username (not email address) and then your Github password. Be careful as you type as these values don't show up on the screen.

> ....that's it. The script will set up your git repo locally inside `my-computer/my-projects/project-of-some-name` and then create a `README.MD` (blank) and then commit it locally, then set up a remote repo in Github (log you in via API) etc and then push everything up!

> finally, you will see that the terminal you were interacting with has changed the currently active directory to your project folder. It will now be at `my-computer/my-projects/project-of-some-name` and you can type in `ls` and see the `README.MD` file. If you then type `git status` you will see your local repo's status (the state of your local project) and if you type in `git remote` it will show you the Github url for your project!

Done! Happy Coding!

Annnd.....finally......here is the script! I've commented each step so you can reason your way through it.

```plaintext
# Make executable with chmod +x <<filename.sh>>

CURRENTDIR=${pwd}

# step 1: name of the remote repo. Enter a SINGLE WORD ..or...separate with hyphens
echo "What name do you want to give your remote repo?"
read REPO_NAME

echo "Enter a repo description: "
read DESCRIPTION


# step 2:  the local project folder path
echo "what is the absolute path to your local project directory?"
read PROJECT_PATH

echo "What is your github username?"
read USERNAME

# step 3 : go to path 
cd "$PROJECT_PATH"


# step 4: initialise the repo locally, create blank README, add and commit
git init
touch README.MD
git add README.MD
git commit -m 'initial commit -setup with .sh script'


# step 5 use github API to log the user in
curl -u ${USERNAME} https://api.github.com/user/repos -d "{\"name\": \"${REPO_NAME}\", \"description\": \"${DESCRIPTION}\"}"

#  step 6 add the remote github repo to local repo and push
git remote add origin https://github.com/${USERNAME}/${REPO_NAME}.git
git push --set-upstream origin master

# step 7 change to your project's root directory.
cd "$PROJECT_PATH"

echo "Done. Go to https://github.com/$USERNAME/$REPO_NAME to see." 
echo " *** You're now in your project root. ***"
```

#### Thanks for reading!

If you would like to learn more about my journey into code, check out [episode 53](http://podcast.freecodecamp.org/53-zubin-pratap-from-lawyer-to-developer) of the [freeCodeCamp podcast](http://podcast.freecodecamp.org/), where Quincy (founder of freeCodeCamp) and I share our experiences as career changers that may help you on your journey. You can also access the podcast on [iTunes](https://itunes.apple.com/au/podcast/ep-53-zubin-pratap-from-lawyer-to-developer/id1313660749?i=1000431046274&mt=2), [Stitcher](https://www.stitcher.com/podcast/freecodecamp-podcast/e/59201373?autoplay=true), and [Spotify](https://open.spotify.com/episode/4lG0RGpzriG5vXRMgza05C).

I will also hold a few AMAs and webinars in the coming months. If this is of interest to you please let me know by going [here](http://www.matchfitmastery.com/). And of course, you can also Tweet me at [@ZubinPratap](https://twitter.com/zubinpratap).
