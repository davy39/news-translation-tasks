---
title: How to Launch Sublime Text on Windows from Git Bash
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2020-09-08T21:29:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-launch-sublime-text-from-your-terminal
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98cd740569d1a4ca1c23.jpg
tags:
- name: Bash
  slug: bash
- name: Git
  slug: git
- name: terminal
  slug: terminal
seo_title: null
seo_desc: "If you have been trying to figure out how to open the Sublime Text editor\
  \ from your Git bash, then you're in luck. This article will guide you through the\
  \ process with little or no stress. \nIt took me a while to figure out how it's\
  \ done, but now I ca..."
---

If you have been trying to figure out how to open the Sublime Text editor from your Git bash, then you're in luck. This article will guide you through the process with little or no stress. 

It took me a while to figure out how it's done, but now I can share that knowledge with you all in this write up. By the end you will be able to launch Sublime Text from bash.

### Prerequisites:

* Make sure you have [Sublime text editor](https://www.sublimetext.com/3) set up
* Make sure you have [Git](https://git-scm.com/downloads) installed

## Getting started

[Sublime text](https://en.wikipedia.org/wiki/Sublime_Text#:~:text=Sublime%20Text%20is%20a%20shareware,maintained%20under%20free%2Dsoftware%20licenses.) is a source code editor that helps software developers code and edit text or markup. 

It has amazing features such as syntax highlighting, indentation, plugins and packages. All these features help make it easier and more comfortable to work with and contribute to a wide variety of programming language code bases.

Once you've downloaded and installed Sublime, it will be located within the program files as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/sublime-text.PNG)

What we want to do is create an alias for the sublime_text.exe found within the Sublime Text 3 folder. Then when we type the alias into Git bash it auto launches the text editor.

## How to Configure Git Bash with Sublime Alias

To begin configuring Git bash, we first need to open the bash terminal. Then we can proceed to explore various Linux commands in order to complete the configuration process .

First, we need to create a .bashrc file using the **[touch command](https://www.geeksforgeeks.org/touch-command-in-linux-with-examples/)**. It's important that the file be created within the **C:\Users\username\** directory – otherwise you will get a permission denied error. 

I have created the bash file within the specified directory, so mine looks like **C:\Users\larry\.bashrc**.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/touch-1.PNG)

Next we need to edit the **.bashrc file** to include the alias we'll need to launch Sublime text:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vim.PNG)

When we click on enter we will see an interface that looks somewhat like what we have below. Then you need to press `i` to enter the insert mode.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/insert.PNG)

Now you have access and can type into the prompt. So we can add our alias there now, like this:

```
alias subl='C:/Program\ Files/Sublime\ Text\ 3/sublime_text.exe'
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/alias.PNG)

Once we've included that, we can press `esc` to exit insert mode and then `:wq` to save and exit. 

Once we are done with that we can head back to our bash to check if our configuration worked by doing `subl` as shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/sublz.PNG)

Yes, it works! And you can see Sublime Text launch itself. 

I also figured out that if you have a working directory you can force Sublime to open that directory. I will navigate into a code base now and show the difference in the next screenshot:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/vue--app.PNG)

From the screenshot above, Sublime doesn't just launch a blank workspace – it launches with all project folders associated with that project. That's because we added a wildcard to the command. 

I hope with this hack you will be able to setup an alias for Sublime Text. I really appreciate the answers on this stack overflow **[thread](https://stackoverflow.com/a/43431197/9352741)**. It helped me form the knowledge I was able to share in this article . 

