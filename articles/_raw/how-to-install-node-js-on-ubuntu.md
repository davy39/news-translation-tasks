---
title: How to Install Node.js on Ubuntu – Node Linux Installation Guide
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-10-20T19:29:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-node-js-on-ubuntu
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/programming-development-technology-work-at-night-2022-01-19-00-14-46-utc-1.jpg
tags:
- name: Linux
  slug: linux
- name: node
  slug: node
- name: Ubuntu
  slug: ubuntu
seo_title: null
seo_desc: "If you are a web developer working on the frontend or the backend, you'll\
  \ want to have Node.js installed on your system. \nBut if you use the typical sudo\
  \ apt install nodejs command, it may install a very old version of Node which can\
  \ be troublesome f..."
---

If you are a web developer working on the frontend or the backend, you'll want to have **Node.js** installed on your system. 

But if you use the typical `sudo apt install nodejs` command, it may install a very old version of Node which can be troublesome for you.

So you'll want to install a specific version, which requires a different command. This will install the LTS (Long-Term Support) version of Node which is useful for devs because it has a longer period for support. 

Today, I am going to show you how you can install the latest LTS version of Node on your Ubuntu operating system. 

This processes will work on any kind of Debian-based Linux operating system (Ubuntu, Mint, Zorin, Debian, Elementary OS, and so on). It'll work whether you are using that as your main operating system, secondary operating system on dual boot, WSL on Windows, or using in a virtual machine (VMware Workstation, VirtualBox, and so on).

## Video Tutorial

I have also created a complete video to show you the process step-by-step. You can watch it here:

%[https://www.youtube.com/watch?v=g4Enhyn1o-4]

At the time of writing this article, the latest LTS version for Node is 18.18.2.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-141242.png)
_Node download page showing current LTS version_

When you install Node following the instructions in this article, it will install the latest LTS version of Nodejs automatically. So you'll be safe without any hassle if you simply follow this article and the accompanying video.

## Update Your Operating System

First, you'll want to ensure that you have installed all the updates beforehand. I like to work in the terminal mostly, so I'll install the updates using the terminal directly. 

For updating to the latest versions of all the relevant packages, use `sudo apt update` in the terminal. Use your password when it asks for that.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-104647.png)
_Updating all relevant packages_

Now use `sudo apt upgrade -y` to upgrade all the upgradable packages.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-120347.png)
_Upgrading all relevant packages_

## Install CURL

We're using the **Node Version Manager (NVM)** here to install Node. There are various advantages when we install Node and npm using the NVM as it also allows us to manage multiple versions of Node.js on our system altogether. 

First, you'll need to install `curl` if it's not installed on your system already. You can install curl by using the command below:

```bash
sudo apt install curl -y
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122355.png)
_Installing CURL_

## How to Install Node.js

Now you'll need to follow these steps in order to ensure that you've installed Node.js successfully on your system.

### Install Node Version Manager (NVM)

Install the Node Version Manager (NVM) by using the following command:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122423.png)
_Installing the Node Version Manager (NVM)_

When you run this specific command, the curl downloads the NVM installation script from that specific URL. Afterward, bash executes the same script for installing NVM.

### Activate NVM

Activate the NVM using the command below:

```bash
source ~/.bashrc
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122517.png)
_Activating the Node Version Manager (NVM)_

### Install the latest LTS version of Node

Install the latest Long Term Support version of Node by using the command below:

```bash
nvm install --lts
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122656.png)
_Command for installing the latest LTS version of Node.js_

It installs the latest version of the LTS release of Node by default. 

### Make the default LTS version as NVM

We have installed the latest LTS version of Node, but we also need to set the default version of NVM so that it gets used by default whenever we need it. You can use the command below to do that. Make sure to change the version to the exact LTS version you have installed on your system just now. 

```bash
nvm alias default 18.18.2
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122842.png)
_Selecting the appropriate Node version as the default version_

If your LTS version is something like `24.1.2` then the command would be like below:

```bash
nvm alias default 24.1.2
```

### Confirm that Node was installed

Use the command below to check whether the default version is the exact version you just installed:

```bash
node -v npm -v
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-122937.png)
_Showing the current version of Node installed_

## How to Set Up the Node.js Environment

After installing Node and NPM, you need to set up the Node environment by creating a new Node project.

Use the command below to create a new directory/folder where you want to test a simple "Hello World" type Node project.

```bash
mkdir my-node-project
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123101.png)
_Creating a new directory/folder to test a simple "Hello World" program on Node_

Navigate to the `my-node-project` directory by using the command below:

```bash
cd my-node-project
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123148.png)
_Changing the directory to enter into that newly created directory/folder_

Initialize the new Node project like this:

```bash
npm init -y
```

This command will create a "package.json" file containing your project's metadata and dependencies. Here is the JSON output:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123304-1.png)
_Initializing npm in the folder_

The JSON output is below:

```json
{
  "name": "my-node-project",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

Now run the setup with the simple command. For this, I am going to create a new file called `app.js` using the **nano** text editor in the terminal.

```bash
sudo nano app.js
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123550.png)
_Opening app.js file in nano_

Once the text editor opens, type the below code:

```bash
console.log("Hello, Node.js from Ubuntu!");
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123710.png)
_Writing a simple console.log code in the app.js file using nano_

Use `Ctrl`+ `O` to save the file. Use `Enter` to save the file as `app.js`:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123831.png)
_Save the app.js file with the newly added line of code_

Use `Ctrl` + `X` to return to the bash terminal again.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-123907.png)
_Returning to the terminal again_

Now, it is time to check the output and see whether it's working or not.

Use the command below:

```bash
node app.js
```

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Screenshot-2023-10-20-124010.png)
_Running the app.js file using Node_

It is working!

We have successfully installed the latest LTS release of Node on our Ubuntu/Debian-based Linux operating system.

Cheers! 🥂

## Conclusion

Thank you so much for reading the entire article till now.

If you have enjoyed the procedures step-by-step, then don't forget to let me know on [Twitter/X](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/).

You can follow me on [GitHub](https://github.com/FahimFBA) as well if you are interested in open source. Make sure to check [my website](https://fahimbinamin.com/) ([https://fahimbinamin.com/](https://fahimbinamin.com/)) as well! 

If you like to watch programming and technology-related videos, then you can check my [YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1), too.

All the best for your programming and development journey. 😊

You can do it! Don't give up, never! ❤️

