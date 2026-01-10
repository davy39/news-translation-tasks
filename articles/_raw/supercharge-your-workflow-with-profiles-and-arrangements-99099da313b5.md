---
title: Supercharge your workflow with profiles and arrangements
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T14:24:05.000Z'
originalURL: https://freecodecamp.org/news/supercharge-your-workflow-with-profiles-and-arrangements-99099da313b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PU7wwmX3JaTa6CcDKvSwpA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Marcus Wood

  If you’ve ever had to manage multiple projects, keeping up with the command line
  can be cumbersome. Here are a couple of hot tips on how juggle multiple projects
  that will save you a ton of time.

  If you’re using the regular Mac Termina...'
---

By Marcus Wood

If you’ve ever had to manage multiple projects, keeping up with the command line can be cumbersome. Here are a couple of hot tips on how juggle multiple projects that will save you a ton of time.

If you’re using the regular Mac Terminal, I highly recommend switching over to [iTerm2](https://www.iterm2.com/) (it’s just better). More on why in a bit.

#### SSH Aliases

Sometimes, you need to SSH into a server somewhere. Sometimes you have twenty different servers you’d like to SSH into. Remembering where they live and what they’re called can be a pain.

To save time, create aliases for each server in under a minute. Here’s how:

```
// Open a terminal windownano ~/.ssh/config
```

```
// Fill in the following to create an aliasHost <Name you want to assign>  Hostname <Where you want to ssh>  User <User you want to login as>  IdentityFile ~/.ssh/<pem file you want to use>
```

```
//Exit and save the filectrl + xyenter
```

```
// Now instead of doing this to connectssh -i "<pem file>" <user>@<hostname>
```

```
// You can do thisssh name-you-assigned
```

#### iTerm2 Profiles and Arrangements

Profiles are great and have changed my daily workflow. Sometimes your terminal looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*doLyDCyaaDRpKmByae3DWA.png)
_Which one did I want again? ?_

The problem is, you don’t know which window you want to click. You also don’t want to close out windows, because then you’ll have to open a new window, navigate back to the correct directory, and remember the copy pasta to make it go.

With profiles and window arrangements, you don’t have to worry about any of that.

There’s a quick video walk through below if you get lost on any of these steps.

A profile enables you to open a new command line window in a certain directory and run commands automatically. Let’s make one!

First, close all open command line windows in iTerm, and start with a new command line window. Next, you’ll want to navigate to “Profiles” in the Menubar and click “Open Profiles…”

![Image](https://cdn-media-1.freecodecamp.org/images/1*dMLCZZID5N8XRNu2DGyrLw.png)
_You should see something like this_

Now click “Edit Profiles…” which should bring you here:

![Image](https://cdn-media-1.freecodecamp.org/images/1*CBAfmdNNCcrQYrkZ_FLDlw.png)
_Gamebyrd and Mongod are some profiles I made so don’t worry if you don’t see them_

Click the + sign at the bottom left side to create a new profile. Make sure to give it a name and update the directory to be the the root of your project.

If you want to run commands when this profile is opened, add them in the “Send text at start:” field. One of my favorite recipes is to open up the project in my code editor and build it for development.

```
// Separate commands with a semi-colonatom .; preact watch
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ht3-GXIzPXeGDxeF_IPRyA.png)
_Make sure to click the Directory radio button_

Exiting out of the window will save your changes (there’s no button to do this).

Next up, we need to test it out. Click on “Profiles” in the Menubar and select the profile you made to make sure it works. If you run into any issues, make sure your directory path is correct and that your commands are separated correctly.

Once all that works, it’s time to create a window arrangement to easily launch the newly made profile. **Make sure you don’t have any lingering terminal windows open when you do this step or they’ll be saved as part of the arrangement.**

In a new terminal window, click on the profile you just made. If it opens in a new tab make sure to close the “Default” tab. Navigate to the “Window” tab in the Menubar and select “Save Window Arrangement.” Give it a name and click ok. You’re good to go!

Now all of your terminal windows will be named. They’ll automatically remember the commands you need to start each project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8y6dJLmDB93veUvHtBTc4w.png)
_??????_

#### Wrapping Things Up

After the first time you do so, you’ll be able to create new profiles and arrangements with ease. You can also combine multiple profiles into an arrangement, use tabbed terminal windows to run multiple parts of a project, and much more.

Was this helpful? If so, please clap on the story and let me know what else you’d like to know about my development process or tips on mastering the command line.

_My name is Marcus Wood. I am the founder of Caldera, a full-service digital agency focusing on web applications._

