---
title: 'An intro to Git Aliases: a faster way of working with Git'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-06T20:10:40.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-git-aliases-a-faster-way-of-working-with-git-b1eda81c7747
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LmBD9OaRAJPnBYBoZwyZMw.jpeg
tags:
- name: Git
  slug: git
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Boudhayan Biswas

  As developers, we know Git very well, as it is a very important part of our daily
  activity. Software developers use it all the time. We can not spend a day without
  interacting with Git. We can run Git from the terminal or use some...'
---

By Boudhayan Biswas

As developers, we know **Git** very well, as it is a very important part of our daily activity. Software developers use it all the time. We can not spend a day without interacting with Git. We can run Git from the terminal or use some third party tools like Sourcetree.

But there are some terminal fans who always love to run Git from the terminal only. So for them, it is sometimes difficult to remember and write those long commands. Ohh no buddy!! It is very much a boring and time-consuming task to write long commands all the time ???.

So what should we do now???

Okay, we should start looking for a shortcut for those long long commands.?‍?‍?‍

Look what we found: **Git Alias**. It has come as the rescuer for all.

We all likely know what an alias is — it means a **false name or nickname**.

So using **git alias**, we can assign a nickname to a long git command. This is perfect. ?

Now let’s try to find a place where we can write these nicknames.

_Searching ? Searching ?Searching ?…_

_Yes, **_bash_profile_** is the place where we can write them._

#### _How to open bash_profile ?_

_From Terminal, we can easily open **_bash_profile_** by using the following command:_

_`vim ~/.bash_profile`_

_Now enter into insert mode in your **_vim editor_** by tapping `i` from the keyboard.✓_

#### _Create your first alias in bash_profile:_

_The first program we use to write in any programming language is a **Hello World**_ program. Let’s not break this tradition — we are going to write our very first **alias** with a simple **hello** command.

_Open **_bash_profile_**, and write the following line:_

_`alias hello="echo Hello Boudhayan!! How are you?"`_

_It says that we have created an **alias** named **hello**_ and assigns the right-hand side as the command to execute. So whenever we write **hello** in the terminal, it should execute the command assigned to it.

_Save the changes and reload the **_bash_profile_** by using the following command:_

_`source ~/.bash_profile`_

_Now if we type `hello` in the terminal, it prints `Hello Boudhayan!! How are you?`_

![Image](https://cdn-media-1.freecodecamp.org/images/1*S7sKAFEQuZellxzd1G9L3w.png)

_Awesome!! ???_

_So we have learned how to create an alias command in **_bash_profile_**._

_If we look closely, then we can relate to it. We can find some similarities with the _variable declaration_ in any language. Yes, we already know about that, right?_

#### _Coming to the main topic_

_Now let’s create some git aliases to make our daily life easier and faster.?_

_`git clone`_

_We use this command for cloning a remote repository to a local system._

_Though it’s a short command, we want to start learning git aliases by making it even shorter.?‍_

_Just like above, open bash_profile, write the below line and reload **_bash_profile_**. See the magic.☄️_

_`alias gc="git clone"`_

_So from now on, for cloning a repository, we do not need to write this:_

_`git clone <remote repository url>`_

_instead, we will use the below command for cloning purposes:_

_`gc <remote repository url>`_

_Boom!! Your remote repository is successfully cloned into your local system.???_

#### _Create some more aliases_

_We push our local commits to the development or master branch by using the below commands:_

_`git push origin develop`_  
_`git push origin master`_

_Now, we can write shorter version like below:_

_`alias gpd="git push origin develop"`_  
_`alias gpm="git push origin master"`_

_So from now, we will use_ gpd and gpm to push local commits to the development and master branch respectively.

_?????? Hurrah!! We have made it.??????_

_I have created some more git aliases which can be really useful in our programming life. Check them out:_

#### _Shell Function:_

_We can also use the **shell function** to declare more complex_ git aliases. But to start with this, we need to know how to write a shell function.?

_It is very easy to write a **shell function**_ which is like a normal **C** function.?

```
function function_name() {         
  command1         
  command2         
  .......         
  commandn
}
```

_Now let’s try this. This function will create a directory in the current path and then immediately move into that directory. We know the below commands already to make it happen:_

_`mkdir <directory_name>`_  
_`cd <directory_name>`_

_We can compress those two commands by creating a simple function in **_bash_profile_** like below:_

_`function mdm() {`_  
   _`mkdir -p $1   #here $1 is the first parameter to the function.`_  
   _`cd $1`_  
_`}`_

_Now reload the **_bash_profile_** source once and run the following:_

_`mdm test`_

_It will create a directory named **test** in the current path and move to that directory. Cool!!?_

#### _Advanced Git Aliases_

_To push the code in the remote branch, we need to make a commit with some message. Only then we can push to a branch. So basically this is a combination of two commands (commit and push). But we want to try the same with a single one-line command by writing a shell function for this. ?_

_We can easily do this by writing a simple shell function. Open **_bash_profile_** and write the following the function:_

_`function gcp() {`_  
      _`git commit -am "$1" && git push`_   
_`}`_

_Reload the **_bash_profile_** once and use the command like below:_

_`gcp "initial commit"`_

_Cool!! From now we can use this **gcp** command to commit and push in one shot.?_

_In a development or feature branch, all the team members push their changes almost every day. So sometimes it is very difficult to find a particular commit among all the commits._

_To easily handle this type of situation, we can write a function which will search the commit logs for a particular message and return the commit._

_To do this, we will write a function like below:_

_`function gfc() {`_  
         _`git log --all --grep="$1"`_  
_`}`_

_Occasionally if we want to search for a commit by the commit message, then we can do it by using `gfc`:_

_`gfc "<commit message>"`_

#### _Conclusion:_

_So we have learned how to use shortcuts for git commands._

_May these aliases and functions save you from writing those long git commands and make your life easy and smooth. You can add your own aliases, functions and make modifications to them — no one’s permission is required except **_bash_**.???_

_**??? Cheers!!! Thank you for reading!! ???**_

