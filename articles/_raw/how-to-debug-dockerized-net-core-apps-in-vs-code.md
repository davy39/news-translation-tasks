---
title: How to Debug Dockerized .NET Core Apps in VS Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-08T15:34:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-debug-dockerized-net-core-apps-in-vs-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/debug_dockerized_dotnet_core_apps-1.png
tags:
- name: debugging
  slug: debugging
- name: Docker
  slug: docker
- name: .NET
  slug: net
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'By Haseeb Ahmed

  I recently switched to VS Code for development of a dockerized .NET core app. But
  I then realized that there weren''t many up-to-date articles about debugging dockerized
  .NET core applications in VS Code.


  Source: GIPHY

  So, here I am, ...'
---

By Haseeb Ahmed

I recently switched to VS Code for development of a dockerized .NET core app. But I then realized that there weren't many up-to-date articles about debugging dockerized .NET core applications in VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-217.png)
_Source: GIPHY_

So, here I am, writing this article. I hope that it'll help others like myself in debugging their dockerized .NET core applications in VS Code. 

In this article we will discuss the following:

1. VS Code extensions for Docker
2. VS Code launch configurations
3. How to debug .NET core apps on your local Docker

# VS Code Extensions for Docker

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-218.png)

Although no extension is really required (for you hardcore minimalists) to debug containerzied .NET core applications, I'd still recommend that you install the [Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) by Microsoft. It will make it easy to create, manage, and debug containerized applications from right within VS Code. 

Honestly, ever since I've started using the extension, I don't use the Docker Desktop anymore.

# VS Code Launch Configurations

Now, in order to debug dockerized .NET Core applications, we will need to create a VS code launch configuration. 

In this section, I'll talk about two sorts of launch configurations: one for docker run and the other for docker compose. 

Later on, we'll also look into the final launch configurations and understand them so that we know what we're doing.

## Docker Run Launch Configuration

If you installed the Docker extension by Microsoft, this should be easy.

First, press "Ctrl + P" in VS code and type in `> Docker:`

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-221.png)

Next, select "Docker: Initialize for Docker Debugging".

Then select ".NET: ASP.NET Core" as your application platform. Select "Linux" as your operating system.

And voilà! You should now have a "Docker .NET Core Launch" launch configuration.

Note that Docker extension will want to overwrite your existing dockerfile. If you don't let it, it won't create the launch configurations. I'd recommend that you backup your dockerfile, let the extension overwrite it, and then restore your original file.

## Docker Compose Launch Configurations

Now we all know that real-life applications are never that simple! You would probably have a DB container, an app container, and a few other containers all connected together via a docker-compose configuration. 

If that is the case, here is how you'll create your launch configurations.

First, open your workspace in VS Code. If you already have existing launch configurations, you can skip the next part.

Next, press "Ctrl + Shift + D" to switch to the "Run & Debug Tab".

Click on "create a launch.json file" and choose ".NET 5+ and .NET Core" (This will create a basic launch configuration for running your application without Docker).

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-222.png)

Now, while your launch.json file is open, click on Add Configuration button in the bottom right corner of the editor.

Select "Docker: .NET Core Attach (Preview)" from the opened dropdown.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-229.png)

It should have added a new configuration called "Docker: .NET Core Attach (Preview)".

Voilà! Now you're ready to debug your dockerized .NET Core application in VS Code.

## How to Understand Launch Configurations

Before we start debugging our application, let's look into the launch configurations a bit closer to understand how they work. 

There should be two files in the .vscode folder, in the root of your workspace. 

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "docker-build",
            "label": "docker-build: debug",
            "dependsOn": [
                "build"
            ],
            "dockerBuild": {
                "tag": "webapi:dev",
                "target": "base",
                "dockerfile": "${workspaceFolder}/src/Dockerfile",
                "context": "${workspaceFolder}",
                "pull": true
            },
            "netCore": {
                "appProject": "${workspaceFolder}/src/webapi.csproj"
            }
        },
        {
            "type": "docker-run",
            "label": "docker-run: debug",
            "dependsOn": [
                "docker-build: debug"
            ],
            "dockerRun": {},
            "netCore": {
                "appProject": "${workspaceFolder}/src/webapi.csproj",
                "enableDebugging": true
            }
        }
    ]
}
```

First, let's take a look at the tasks.json file. This file has list of tasks that might be required by some of the launch configurations to launch the application properly.

The task we want to look at is "docker-run: debug". This is the task called when you launch using the "Docker .NET Core Launch" configuration (as we'll see later).

This task has three properties that we need to understand:

* netCore.appProject: This property is .NET Core app-specific and just points to the project file of your app.
* netCore.enableDebugging: This is another .NET Core app-specific property which tells VS code to launch the app with debugging capabilities.
* dependsOn: This is a generic property that defines if a task depends on other tasks for its execution.

Secondly, we need to understand what the "docker-build: debug" task does. 

In addition to the netCore and dependsOn properties, it has a dockerBuild object that controls the `docker build` command which is run by VS Code to launch a docker run app. 

Properties of the dockerBuild object are quite similar to the arguments that you pass to the `docker build` command.

You can read about all the dockerBuild object properties [here](https://code.visualstudio.com/docs/containers/reference#_dockerbuild-object-properties) and tasks in general [here](https://code.visualstudio.com/docs/editor/tasks).

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Docker .NET Core Attach",
      "type": "docker",
      "request": "attach",
      "platform": "netCore",
      "sourceFileMap": {
        "/src": "${workspaceFolder}/src"
      }
    },
    {
      "name": "Docker .NET Core Launch",
      "type": "docker",
      "request": "launch",
      "preLaunchTask": "docker-run: debug",
      "netCore": {
        "appProject": "${workspaceFolder}/src/webapi.csproj"
      }
    }
  ]
}
```

Now, let's take a look at the launch.json file where all the launch configurations live. 

While most of these properties are standard, the one we care about is "sourceFileMap" in the "Docker .NET Core Attach" configuration. 

In order to debug .NET Core applications that were built on a machine other than the VS Code machine (in this case a Docker), VS Code needs to understand how-to map your current workspace to the build machine hierarchy. 

For example, if my project was built from the "/src" folder in Linux, this property will tell VS Code to replace "/src" with "${workspaceFolder}/src" in all the filepaths. In case this mapping is incorrect, VS Code will hit the breakpoint but will give an error that the file (being debugged) does not exist.

You can read more about launch.json properties in detail over [here](https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes).

# How to Debug .NET Core Apps on Your Local Docker

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-230.png)

## Docker Run

Now that we have the launch configurations figured out, this should be easy! Just follow the steps below.

First, press "Ctrl + Shift + D" to switch to the "Run & Debug Tab".

Then choose "Docker .NET Core Launch" and press the green play icon to debug.

## Docker Compose

Debugging a Docker Compose container is slightly different. You'll have to make sure that your Docker Compose containers are already running before you attach the VS Code debugger. 

Once they are up, follow these steps:

First, press "Ctrl + Shift + D" to switch to the "Run & Debug Tab".

Then choose "Docker: .NET Core Attach (Preview)" and press the green play icon to debug.

That is, it! I hope you found this helpful. If you have any questions or are confused about anything, you can reach out to me or you can check out the sample project on [GitHub](https://github.com/thehaseebahmed/vscode-dotnet-docker-debug).

Happy Coding!

This article is a part of my [coding series](https://blog.thehaseebahmed.com/series/coding). You may find other useful articles for your daily development there as well.

