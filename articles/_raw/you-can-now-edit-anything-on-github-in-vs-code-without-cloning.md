---
title: How to Open Any Repo in VS Code Without Cloning It
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-15T16:06:54.000Z'
originalURL: https://freecodecamp.org/news/you-can-now-edit-anything-on-github-in-vs-code-without-cloning
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/window.jpg
tags:
- name: Productivity
  slug: productivity
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: "By Burke Holland\nYou can now open anything (that you have access to) on\
  \ GitHub directly from VS Code with the official Remote Repositories extension.\
  \ \nAnd I do mean directly. That means no clone. No download. No looking at your\
  \ dev folder and wonderi..."
---

By Burke Holland

You can now open anything (that you have access to) on GitHub directly from VS Code with the official [Remote Repositories extension](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub&WT.mc_id=devcloud-18509-cxa). 

And I do mean _directly_. That means no clone. No download. No looking at your dev folder and wondering why on earth you structured your projects this way and OMG SO MUCH REGRET.

Listen, it's ok. Nobody is happy with how they have cluttered up their once pristine dev environment. Inside my "c:\dev" folder is an entire season of [Hoarders](https://www.aetv.com/shows/hoarders) and no, I'm not going to delete that jQuery project. I might need it some day.

Let's look at how the new Remote Repositories extension for VS Code lets you casually interact with any project on GitHub without having to clone a thing.

## How to Install the Remote Repositories Extension

First, you'll need to install GitHub's [Remote Repositories extension](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub&WT.mc_id=devcloud-18509-cxa) for Visual Studio Code.

%[https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub&WT.mc_id=devcloud-18509-cxa]

To open a GitHub repo, click on the green indicator in the lower left-hand corner of VS Code. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-64.png)

You'll see a new option for "Open Remote Repository". 

If you have other Remote extensions for VS Code installed, you'll see a lot more options in this list, so just search for the right one. 

You can also get to this option from the Command Palette if clicking on things with a mouse is too much trouble. I see you VIM people.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-65.png)

You can paste in the URL to a GitHub repo if you happen to just have that hanging around on your clipboard (weird) OR you can browse GitHub by selecting "Open Repository from GitHub". The third option lets you open a Pull Request branch so you can ~~pretend to~~ thoroughly review it.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-66.png)

VS Code will reopen and you'll see that repository just like you were working with it locally. But you're not. You're looking at it _on_ GitHub _through_ the window of VS Code.

You'll notice disclaimers about "some features" not being available and that you are in "Restricted Mode".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-145.png)

This is part of the new Trusted Workspace settings in VS Code. 

%[https://code.visualstudio.com/docs/editor/workspace-trust?WT.mc_id=devcloud-30876-buhollan]

By default, VS Code now turns off Tasks, debugging, some workspaces settings and any extensions that might try and execute something the first time you open a folder. You have to tell VS Code that it's cool, you know and trust this code and you're 100% sure it's not going to [shutdown your oil pipeline](https://www.nytimes.com/2021/05/08/us/politics/cyberattack-colonial-pipeline.html). 

Ok – so scary security warnings dismissed, what can we do here?

## How to Work with a Remote Repository

You have full editing capabilities with a big difference being that you don't have to save anything. Your changes are just saved as you go. 

They aren't automatically committed to GitHub. In order for the changes to be saved to the repo, you'd have to commit them from the source control view. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-68.png)

You don't have to push them because you are already on GitHub. A commit is a commit – no push required. This is the same as if you were editing the file directly on GitHub. Because you essentially are.

As far as the editing goes, you get much of what you would expect in  VS Code.

Language specific intellisense works. For instance, if  you started writing a `fetch`, VS Code will help you with that because it knows about `fetch`.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-69.png)

But you do not get the intellisense on project files that VS Code gives you when it runs your project locally. 

For instance – locally, VS Code knows about `useEffect` which comes from the `react` import. It knows this because it's inspecting the import which is a node module. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-34.png)

But with Remote Repositories, we're looking directly at GitHub and the node_modules folder never ever gets pushed to GitHub unless you are me 10 years ago. So there is no intellisense for `useEffect` because that code doesn't actually exist in the repo.

You can use things like Emmet to compose HTML and you get the nice split screen Markdown preview that you probably love like I do.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-35.png)

You can also use "Find" and "Find in Files". 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-37.png)

Many things that work locally work the same way when connected to a project directly on GitHub, but some do not. Which is the vaguest thing anyone has ever written on the internet, but understanding how this all works will shed some light on what you can reasonably expect.

## How It Works

VS Code has a [file system provider API](https://github.com/microsoft/vscode/blob/dc8bd9cd7e5231745549ac6218266c63271f48cd/src/vs/vscode.d.ts#L7038) that has been around for some time. What this API does is provide a mechanism to consume an API as if it were a physical file. In this case, the Remote Repositories extension is consuming and mapping the GitHub API to a "Virtual Workspace" in VS Code.

This means that any extension that is trying to work with physical files is not going to work **until the** **extension author updates their extension to use the Virtual File System API**. Which means that things that don't work today might work in the future as extensions are updated.

So what can you expect to work? Themes, key bindings, snippets and grammar extensions. These types of extension typically don't execute any code, so you know they aren't trying to work with files which means it's safe (internet safe) to assume they'll work in Remote Repositories.

But some things won't ever work because you need local file access to do them. 

A prime example of this is Prettier. Prettier is a CLI tool that alters your local files by reformatting your code. Since there is no local file access, it doesn't currently work with Remote Repositories. So nobody is going to change those double quotes to singles automatically or put that semicolon back. Or remove it. I want out of this paragraph.

In fact, you can't _run_ a Remote Repositories project at all. If you open the terminal while connected to a Remote Repository, it will be there. But it won't have any access to this project. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-70.png)

Which is legit because the project doesn't actually exist on your machine. So how do you get a terminal if you find you actually do want to run the code you are working with, or just upgrade your editing experience to full-blown VS Code?

## How to Switch to Full VS Code

> "Continue on my wayward son" - [some band from the 70's](https://www.youtube.com/watch?v=2X_2IdybTV0)

If you click in that green bottom left-hand part of the Status Bar that says "GitHub" right now, you'll see an option to "Continue Working On".

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-71.png)

This option will let you either clone the project locally, or open it in a GitHub Codespace. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-72.png)

If you're in the Codespaces Beta (_[request access here](https://github.com/features/codespaces)_), you can open the repo in a Codespace. This is VS Code running in the browser, but backed by a compute environment where you can run anything just like it was on your desktop. This works because VS Code was originally designed to be a web app. True story.

Or clone it locally! Crack open that `c:\Users\you\Documents\GitHub` folder that you regret choosing to put all  your projects in because now your "Documents" folder is being backed up to OneDrive and it's got 900 terabytes of node_modules in it. Well - now it's got 920. 

![Image](https://www.freecodecamp.org/news/content/images/2021/06/image-77.png)
_Credit: Some brilliant soul. Please comment and take credit for this work of genius._

## Cool. But Why?

The natural question you should be asking yourself right now is, "Very cool! But why do I need this?"

Excellent question. You are preceptive and people like you.

Consider the following scenarios...

* **You want to browse a GitHub repo and look at the code.** GitHub is a great site, but it's not the best way to quickly jump through files and examine a project. You really need an editor for that and Remote Repositories cuts out the cumbersome and often bandwidth intensive step of cloning simply to look at code.
* **You want to make a quick update.** While you would almost always do heavy coding locally, you might want to pop into a repo and make a quick change without having to sync your local environment. README's come to mind, but this could be any sort of small change.
* **You are working on Markdown.** If you're working on documentation, README's or other Markdown in GitHub, there's no need to clone the repo locally anymore to do that. Unless you are running a local server to preview that Markdown, using the built-in preview is a much faster way to pound out 5K words about your API.
* **You want to review a PR.** Seems self explanatory. 

## Get More Remote

Now that you have Remote Repositories, you can clean out that dev folder. Just right-click and delete something. See how good that feels? 

Remote Repositories is one of several ways to do "Remote" development with VS Code. Check out these other options to use VS Code to connect to almost anything. 

* [Dev Containers](https://code.visualstudio.com/docs/remote/containers?WT.mc_id=devcloud-30876-buhollan) - Use a Docker container as a full-featured development environment with 
* [Remote SSH](https://code.visualstudio.com/docs/remote/ssh?WT.mc_id=devcloud-30876-buhollan) - Open a remote folder in VS Code on any remote machine over an SSH connection
* [Remote WSL](https://code.visualstudio.com/docs/remote/wsl?WT.mc_id=devcloud-30876-buhollan) - To use your WSL as the full-time backing runtime environment in VS Code.

