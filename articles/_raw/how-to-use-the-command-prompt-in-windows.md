---
title: How to Open and Use the Command Prompt in Windows
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T23:22:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-command-prompt-in-windows
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d74740569d1a4ca37da.jpg
tags:
- name: command line
  slug: command-line
- name: toothbrush
  slug: toothbrush
- name: Windows
  slug: windows
seo_title: null
seo_desc: "Getting started\nWindows, MacOS and Linux have command line interfaces.\
  \ Windows’ default command line is the command prompt. The command prompt allows\
  \ users to use their computer without pointing and clicking with a mouse. \nThe\
  \ command prompt is a bla..."
---

# **Getting started**

Windows, MacOS and Linux have command line interfaces. Windows’ default command line is the command prompt. The command prompt allows users to use their computer without pointing and clicking with a mouse. 

The command prompt is a black screen where users type commands to use their computer. The same tasks that can be done by pointing and clicking with a mouse can also be done with the command prompt. The difference is that many tasks such as creating folders and deleting files can be done faster in the command prompt. 

Also, it allows users to configure their computer and run programs that they otherwise could not do by pointing and clicking.

## **Opening the Command Prompt**

To access the command prompt, click the windows start menu on the Desktop tool bar (you can also press the windows button on your keyboard) and type `cmd` and hit `enter`. The command prompt will appear, it will display some text like to following below:

```text
C:\Users\YourUserName>
```

## **Navigating Directories (Moving through folders)**

`C:\Users\YourUserName` is called your current working directory (directory is another way to say folder). It is like a street address that tells you where you are on your computer. 

The current working directory can be a guide as you navigate through your computer. On the right of the `>` we can type `cd`, which stands for Change Directory, and the name of a directory that you want to navigate to. In this case we will type `Documents`. Enter `cd Documents` and your current working directory should look like the following:

```text
C:\Users\YourUserName\Documents>
```

To go back one directory type and enter `cd..`. Your current working directory should return to this:

```text
C:\Users\YourUserName>
```

With the `cd` and `cd ..` commands you can move back and forth through directories. This might seem very basic at first but as you learn more commands the command prompt will become a very useful and efficient tool.

## **Here is a list of common commands:**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-18-at-3.25.08-PM.png)

## **Usage Examples:**

#### **Making a Directory**

```text
mkdir name_of_the_directory_you_want_to_make
```

#### **Getting Info on a Command**

```text
your_command /?
```

#### **Deleting a File and Contents**

```text
rm /s name_of_directory_you_want_to_delete
```

## **Useful tips:**

* The command `Ipconfig` shows your computer’s ip address
* If you type part of a directory’s name and hit the `tab` key the command prompt will autocomplete it and if you hit the `tab` key repeatedly it will cycle through directories that start with the same letter
* You can use other shells or tools such as git bash or cmder to add more commands and functionality to your command prompt
* Some tasks require you to run the command prompt as an administrator you clicking the windows button and typing `cmd admin` and hit the `enter` key
* If you know the path to a file or directory can type `cd PATH_TO_YOUR_DIRECTORY` instead of changing directories several times to get to a directory or file
* When you hit the up arrow key your previously entered command will appear and if you hit it repeatedly it will cycle through all of your previously entered commands

