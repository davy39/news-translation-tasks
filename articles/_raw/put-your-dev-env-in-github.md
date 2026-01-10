---
title: Please, Everyone, Put Your Entire Development Environment in Github
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-13T15:00:00.000Z'
originalURL: https://freecodecamp.org/news/put-your-dev-env-in-github
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/put-dev-env-in-the-cloud.png
tags:
- name: Docker
  slug: docker
- name: GitHub
  slug: github
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'By Burke Holland

  Stop me if this sounds familiar...

  You want to get started with a new framework/runtime. So you install said framework/runtime.

  Then you open up the terminal and....command not found. Heavy sigh.

  You revisit the docs which suggest th...'
---

By Burke Holland

Stop me if this sounds familiar...

You want to get started with a new framework/runtime. So you install said framework/runtime.

Then you open up the terminal and....command not found. Heavy sigh.

You revisit the docs which suggest that you have make some changes to your profile settings. Which you aren't sure how to do so you go to StackOverflow, where you find an answer from "user92902399" which _looks_ like it could be legit (who knows), so you copy and paste that into your terminal and hope to god it doesn't erase your hard drive and email the president your internet history.

Now the runtime command works. But it fails. The error is cryptic.

Back to Google.

This time there is no clear answer on StackOverflow despite several people having a similar issue. You find a Github issue that looks like it might be related. Somewhere in the middle of a mass of people saying "Thanks this works!" and "This doesn't work at all!" someone uses the word "Python".

You check your Python version and sure enough, this framework/runtime doesn't support the one you have installed. You are just about to downgrade it when you realize that the last time you even looked in the general direction of your Python install it took you a day to get it working again and you still aren't sure how you did it.

You know what, this new framework/runtime probably isn't that good. It's definitely not worth all this trouble. Oh look! A blog post about how you should never use ternary statements. What were you working on before? Who cares.

A little too close to home? This is what it's like to try and set up a new project, framework or runtime. Every time. This is part of the reason why every developer has at one point in time looked up at someone blankly mid-Cheeto and said, "it works on my machine".

## Works on All Machines

The root problem is that in order for code to work, there is an entire environment which has to also be configured correctly. This is a hard problem to solve. What we need is a way to isolate the development environment and then ship it with the code so that it works on all machines. And we need to do that without having to ship an entire operating system.

The key lies in the word "isolate". As it turns out, we do have a way to isolate and ship entire environments. It's called, "Docker". You can create a container with any configuration and then ship that to anyone else. All you need now is a way to develop in that container like it was your local machine.

You can.

In this article, I'm going to show you how you can use a few configuration files to box up and ship your entire development environment minus your bad taste in dubstep. 

This is all thanks to the new [Dev Containers extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers&WT.mc_id=freecodecamp-blog-buhollan).

Note: The Dev Containers extension was previously named Remote-Containers. While the screenshots below show the older Remote-Containers extension name, all of the instructions should work the same way similarly with the new Dev Containers name.

## VS Code and Dev Containers

The basic concept behind [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers&WT.mc_id=freecodecamp-blog-buhollan) is that you specify a Dockerfile which in turn specifies all of the necessary dependencies and configuration steps to get the correct development environment setup. VS Code will then spin up that container, install a little server in it and then connect back to your VS Code instance. What this means is that you are now developing inside of a pre-configured environment. But to you, it's just VS Code.

To show you how this works, I'm going to create a container in which to develop the backend API of a project that I worked on called, theurlist.com. The backend of this project is written in C# and runs on [Azure Functions](https://code.visualstudio.com/tutorials/functions-extension/getting-started?WT.mc_id=freecodecamp-blog-buhollan). In order to run it locally, you would have to install the [.NET Core runtime](https://dotnet.microsoft.com/download?WT.mc_id=freecodecamp-blog-buhollan), [Azure Functions CLI](https://github.com/Azure/azure-functions-core-tools) and the [Azure Functions VS Code extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions&WT.mc_id=freecodecamp-blog-buhollan). 

The first step is to install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers&WT.mc_id=freecodecamp-blog-buhollan). This will add a little icon to the bottom-left corner of your VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-90.png)

You're also going to need to have Docker installed. Docker containers don't run very well if you don't have Docker. You can download the Community Edition [here](https://docs.docker.com/install/).

With the extension installed, I need to add the proper configuration files to this project. Namely a "Dockerfile" which specifies the container that the project will be loaded in. The extension comes with a bunch of preconfigured environments. To add one to the project, open the Command Palette and select "Dev Containers: Add Development Container Configuration Files" 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-91.png)

This project uses Azure Functions and C#, so I'll select that container definition.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-92.png)

As soon as I do that, VS Code is going to add a ".deployment" folder with "Dockerfile" and a "devcontainer.json" file inside. It's also going to immediately ask if I want to re-open the project in a container. I'm gonna say no and have VS Code chill out for just a minute while we look at these files.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-93.png)

First let's look at the "Dockerfile" file. File file file.

### Dockerfile Configuration

The "Dockerfile" specifies what will be in the container. If I open it up, you can see that there's quite a bit in there. It's a tad verbose. But we can parse out the important bits.

The first thing it does is pull in the latest version of the .NET Core SDK.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-94.png)

Then it installs some utilities in the container. Specifically, it installs...

* Git (Source Control)
* procps (process inspection utility)
* curl (HTTP utility)
* apt-transport-https (HTTPS utility)
* gnupg2 (An encryption tool)
* lsb-release (Prints specific Linux information)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-95.png)

All of this is to create an environment that has every obscure tool that a developer may need to run this project and be able to check it in and out of source control.

Then it installs the Azure Functions Core Tools. It configures all of the necessary repository locations before the install. These are all things a developer would have to do themselves before they can even run this project.

The other file in the ".devcontainer" folder is the "devcontainer.json" file.

### The devcontainer.json file

This file specifies some additional settings for the remote development environment. Specifically....

1. It specifies the "Dockerfile" should be used to build the container

2. It makes sure that port "7071" is forwarded from the container so it can be accessed at "localhost:7071". This is the port Azure Functions runs on locally.

3. It specifies any extensions that should be installed in the container. Since you aren't really using VS Code locally, your extensions aren't all installed automatically. Specifying them in this file makes sure they are there when the project is opened.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-96.png)

And with that, we can open the Command Palette and select "Dev Containers: Reopen folder in container".

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-98.png)

VS Code will reload and set about building the container for this project.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-100.png)

The first time it does this, it takes a minute or two because the base images have to be pulled and built. After it's done the first time, subsequent loads are much faster as the image already exists on your machine.

In the case of this project, once the container is built, VS Code sets about restoring the C# dependencies which is done with the C# Extension that was included in the "devcontainer.json" config file.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-105.png)

When it's all finished, I can run this project just by pressing F5. And just like that the app is up and running.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-110.png)

Think of what we would have had to do to get this setup locally...

1. Install .NET Core
2. Install Functions Core Tools
3. Install VS Code Functions Extension
4. Install VS Code C# Extension

With Dev Containers, none of that is required. We can configure and ship an entire development environment in **two text files**.

### Please, Put Your Development Environment in Github

So here's my humble plea: instead of outlining 15 steps in a Github README for configuring your project to run, **put your entire development environment in Github**.  That means checking in that ".devcontainers" folder. If a developer using your project doesn't have VS Code or the Dev Containers extension, nothing happens. You can't lose.

I'm excited because I feel like the days of configuration hell are nearing an end. And besides, think of all the people we'll save from dogmatic articles about ternary statements.

### More On Development With Containers

* [Developing inside a container](https://code.visualstudio.com/docs/remote/containers?WT.mc_id=freecodecamp-blog-buhollan)
* [VS Code Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers&WT.mc_id=freecodecamp-blog-buhollan)
* [Advanced Container Configuration](https://code.visualstudio.com/docs/remote/containers-advanced?WT.mc_id=freecodecamp-blog-buhollan) 

