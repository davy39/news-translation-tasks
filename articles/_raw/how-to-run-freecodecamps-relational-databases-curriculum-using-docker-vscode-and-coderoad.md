---
title: Relational Database Course – How to Learn SQL in VSCode Using Docker and freeCodeCamp
subtitle: ''
author: Tom Mondloch
co_authors: []
series: null
date: '2021-09-16T16:17:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-freecodecamps-relational-databases-curriculum-using-docker-vscode-and-coderoad
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/Screen-Shot-2021-09-12-at-9.22.55-PM.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: freeCodeCamp Curriculum
  slug: freecodecamp-curriculum
- name: Relational Database
  slug: relational-database
seo_title: null
seo_desc: 'You can now learn Relational Database concepts and SQL right inside your
  VSCode editor. This tutorial will walk you through how to install it using Docker.

  During this full-length 300-hour course, you will learn to build more than a dozen
  projects. S...'
---

You can now learn Relational Database concepts and SQL right inside your VSCode editor. This tutorial will walk you through how to install it using Docker.

During this full-length 300-hour course, you will learn to build more than a dozen projects. Some of them will involve step-by-step instructions, and others will be open ended, with elaborate test suites.

You will use real developer tools and software like VS Code, PostgreSQL, and the Linux / Unix command line to complete interactive tutorials and build projects.

### What you will learn

* The Linux / Unix Command Line
    
* Relational Databases
    
* SQL and PostgreSQL
    
* Bash and Bash Scripting
    
* Git and GitHub
    
* Nano
    
* And a lot of other concepts and tools
    

This course was made possible by a grant from [Class Central](https://www.classcentral.com/), a search engine and review site for online courses.

## How to install Docker and run the Relational Database Curriculum

Docker will run a container on your computer that has the software and file structure required for these tutorials.

You will be working in that container using VSCode and the Dev Containers extension. Once it's running, the CodeRoad extension will run the tutorials we have created.

### Prerequisites

Before you get started, you need to have a few things installed:

1. The [Docker Engine](https://docs.docker.com/engine/install/)
    
2. [VS Code](https://code.visualstudio.com/download)
    
3. The [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension for VS Code
    
4. [Git](https://git-scm.com/downloads)
    

### How to Run a Project in Docker

Follow these steps to run the docker container and start a tutorial:

1. Clone the RDB Alpha repo to your computer with `git clone https://github.com/freeCodeCamp/rdb-alpha`
    
2. Open a terminal, navigate to the `rdb-alpha` directory, and open VS Code with `code .`
    
3. In VS Code, open the command palette with `Ctrl / Cmd + Shift + P`. Then, enter and run `Dev Containers: Rebuild and Reopen in Container`
    
4. A new VS Code window will open and begin building the Docker image. It will take several minutes to build the first time
    
5. Once the image is finished building, open the command palette again with `Ctrl / Cmd + Shift + P`, enter and run `CodeRoad: Start`. The command won't be available until the extension has finished installing in your container
    
6. In the CodeRoad window, click "Start New Tutorial"
    
7. Click the `URL` tab and enter the URL of the `tutorial.json` file for the project you want to start (ex: https://raw.githubusercontent.com/freeCodeCamp/learn-bash-by-building-a-boilerplate/main/tutorial.json) Full list of available tutorials below.
    
8. Click the "Start" button to start the lessons
    

### How to Restart or Switch Projects

If you restart or switch projects, you will lose your progress on a tutorial you may have started along with any files or folders you may have created.

1. Open the command palette with `Ctrl / Cmd + Shift + P`, enter and run `Dev-Containers: Rebuild Container`
    
2. Wait for VS Code to reopen the reload the container
    
3. Open CodeRoad from the command palette like you did before, click "Start New Tutorial", and enter the URL of the `tutorial.json` file for the project you want to do
    

### Available Courses

Here is a list of tutorials currently available. Open one of them and use its URL, as described in the instructions above, to start it.

* [Learn Bash by Building a Boilerplate](https://raw.githubusercontent.com/freeCodeCamp/learn-bash-by-building-a-boilerplate/main/tutorial.json)
    
* [Learn Relational Databases by Building a Database of Video Game Characters](https://raw.githubusercontent.com/freeCodeCamp/learn-relational-databases-by-building-a-database-of-video-game-characters/main/tutorial.json)
    
* [Celestial Bodies Database](https://raw.githubusercontent.com/freeCodeCamp/learn-celestial-bodies-database/main/tutorial.json)
    
* [Learn Bash Scripting by Building Five Programs](https://raw.githubusercontent.com/freeCodeCamp/learn-bash-scripting-by-building-five-programs/main/tutorial.json)
    
* [Learn SQL by Building a Student Database: Part 1](https://raw.githubusercontent.com/freeCodeCamp/learn-sql-by-building-a-student-database-part-1/main/tutorial.json)
    
* [Learn SQL by Building a Student Database: Part 2](https://raw.githubusercontent.com/freeCodeCamp/learn-sql-by-building-a-student-database-part-2/main/tutorial.json)
    
* [World Cup Database](https://raw.githubusercontent.com/freeCodeCamp/learn-world-cup-database/main/tutorial.json)
    
* [Learn Advanced Bash by Building a Kitty Ipsum Translator](https://raw.githubusercontent.com/freeCodeCamp/learn-advanced-bash-by-building-a-kitty-ipsum-translator/main/tutorial.json)
    
* [Learn Bash and SQL by Building a Bike Rental Shop](https://raw.githubusercontent.com/freeCodeCamp/learn-bash-and-sql-by-building-a-bike-rental-shop/main/tutorial.json)
    
* [Salon Appointment Scheduler](https://raw.githubusercontent.com/freeCodeCamp/learn-salon-appointment-scheduler/main/tutorial.json)
    
* [Learn Nano by Building a Castle](https://raw.githubusercontent.com/freeCodeCamp/learn-nano-by-building-a-castle/main/tutorial.json)
    
* [Learn Git by Building an SQL Reference Object](https://raw.githubusercontent.com/freeCodeCamp/learn-git-by-building-an-sql-reference-object/main/tutorial.json)
    
* [Periodic Table Database](https://raw.githubusercontent.com/freeCodeCamp/learn-periodic-table-database/main/tutorial.json)
    
* [Number Guessing Game](https://raw.githubusercontent.com/freeCodeCamp/learn-number-guessing-game/main/tutorial.json)
    

#### Here's a video of me doing "Learn Bash by Building a Boilerplate" in 13 minutes and 38 seconds:

%[https://www.youtube.com/watch?v=VQmCwzfSM-k] 

## Also, Download the freeCodeCamp Dark Theme for VS Code

If you like the color scheme that these tutorials use, you can download the [freeCodeCamp Dark Theme extension](https://marketplace.visualstudio.com/items?itemName=freeCodeCamp.freecodecamp-dark-vscode-theme) from the Visual Studio Marketplace.

You can [learn more about the Dark Theme here](https://www.freecodecamp.org/news/vs-code-dark-mode-theme/).

## Help us improve these courses by asking questions and giving us feedback

If you have any questions about these new Relational Database courses, get stuck at some point, or just have general feedback about them, you can create a thread on [the freeCodeCamp Forum](https://forum.freecodecamp.org/).

We also have our own Slack-like chat room system where you can ask questions and help contribute to our open source projects. [Join our chat room system](https://chat.freecodecamp.org/home).

Happy Coding.
