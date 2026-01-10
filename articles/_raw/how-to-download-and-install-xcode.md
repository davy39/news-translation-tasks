---
title: How to Download Xcode and Install it on Your Mac – and Update it for iOS Development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-30T03:58:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-download-and-install-xcode
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b61740569d1a4ca2b7b.jpg
tags:
- name: mac
  slug: mac
- name: macOS
  slug: macos
seo_title: null
seo_desc: 'By Ai-Lyn Tang

  Xcode is the tool developers use to build apps for the Apple ecosystem – MacOS,
  iOS, and all things Apple.

  This guide will walk you through how to successfully install Xcode onto your Mac,
  from start to finish.

  Here are some handy tips...'
---

By Ai-Lyn Tang

Xcode is the tool developers use to build apps for the Apple ecosystem – MacOS, iOS, and all things Apple.

This guide will walk you through how to successfully install Xcode onto your Mac, from start to finish.

Here are some handy tips to know before you get started:

* Xcode only runs on a mac. If you are on a PC, sadly you won't be able to use Xcode.
* You'll need a good, stable internet connection. The latest version is around 8 gigabytes in size.
* Be sure to have at least 30 gigabytes of free space on your computer. The latest `.xip` file (v11.4.1 at the time of writing) is ~8 gigabytes zipped. When you unzip it, that's another 17 gigabytes. Then you'll need the command line tool, which is yet another 1.5 gigabytes.

## Here's an overview of the steps to install Xcode

1. Download Xcode
2. Install the command line tool
3. Open the new version
4. Delete files

Note that I have listed some Terminal commands in the steps below. These commands can be typed into your present working directory. This means that you don't need to navigate to any particular folder.

If you really want to, you can first type `cd` before typing the commands in the below steps. This will return you back to the home folder.

## Step #1: Download Xcode

There are two ways to do this. For the latest version and a theoretically "easy" installation, you can use the App Store. I don't recommend this option.

I prefer to use the developer site. This comes with the bonus option of being able to download any version you'd like.

### Option #1: Download via the App Store for the latest version (not my preferred option)

In theory, this should be a seamless and pain-free process. But if the installation fails for any reason on the last step, it is very hard to troubleshoot.

There are a few reasons for failure, and no easy way to know which is the underlying cause. If you do encounter a failure, you will need to re-download the entire file again each time you try to fix the failure. As the latest version is 8 gigabytes, I didn't much enjoy this approach.

But if you're feeling brave, here are the steps:

* Open the App Store on your mac
* Sign in
* Search for Xcode
* Click install or update

### Option 2: Download via the Developer site for a specific version (my preferred option)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-258.png)
_A screenshot of [https://developer.apple.com/download/more/](https://developer.apple.com/download/more/)_

1. Head to the "more" section of the [Apple developer website](https://developer.apple.com/download/more/)
2. Sign in with your iTunes account id
3. Type in the version that you'd like, and download the `Xcode_x_x_x.xip` file. Keep in mind that Xcode 11.4.1 is 8 gigabytes, so this will take awhile depending on your internet connection.
4. Once the file is downloaded, click on `.xip` to extract it. Your laptop will extract it to the same folder you downloaded it to. This extraction process is automatic. You don't need to do anything more after you click on the `.xip` file. This step will take a few minutes.
5. [Optional] Once extracted, rename the application to “Xcode11.x.x” if you are using multiple versions.
6. Drag application to the Applications folder
7. [Optional] Set the new Xcode version as the default. Open Terminal and type `sudo xcode-select -switch /Applications/Xcodex.x.x.app` . Replace `x.x.x` with the version number. For example: `Xcode11.4.1.app`. You will need to enter in your computer admin password. I'm pretty sure this will update the default Xcode version for all users on your computer, so best to check with other users first

## Step #2: Install the command line tool (CLT)

If you have multiple users on your computer, you will need to update the CLT for each user.

**Download `.dmg`** 

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-269.png)
_A screenshot of [https://developer.apple.com/download/more/](https://developer.apple.com/download/more/)_

To update the CLT, go to [app developer website](https://idmsa.apple.com/IDMSWebAuth/signin?appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2Fdownload%2Fmore%2F&rv=1) and download the command line tool `.dmg`.

If you have never installed Xcode before, you may be able to update with your Terminal by typing in `xcode-select --install` instead of visiting the developer website.

But if you have an existing version of Xcode installed on your machine, you'll probably see this error: 

```
xcode-select: error: command line tools are already installed, use “Software Update” to install updates
```

This means you'll need to go to the developer website instead.

### Installing the CLT

When the `.dmg` has finished downloaded, double click the file to open it. This will open a little window that looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-271.png)

Double click the box and follow the prompts to install the CLT. It will take a few minutes to complete.

It may ask you at the end of the installation whether you want to move this to the trash bin. When it does this, it's talking about moving the `.dmg` file to the trash bin. Since you should no longer need this file. I always say yes to this.

## Step #3: Open Xcode

Open the Applications folder and open the new version of Xcode. If you renamed Xcode, make sure you open the correct application

Xcode may prompt you to install additional components. Click install. This will take a few minutes.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-273.png)

While it's installing, check that your default Xcode version is the one you just downloaded:

* Open Terminal
* Type `brew config`
* You should see “CLT” and “Xcode” versions, as well as everything else. This should reflect the version that you have just downloaded. In my case, I downloaded Xcode 11.4.1.

```
CLT: 11.4.1.0.1.1586360307
Xcode: 11.4.1 => /Applications/Xcode11.4.1.app/Contents/Developer
```

Once the components are installed, Xcode will launch. You should be able to pick up your old projects and continue where you left off seamlessly*.

_*Note that if you use any proxy tools, such as Charles, you will need to re-install those certificates in your simulator again._

If you encounter any errors while trying to build or run a project, check which device you are trying to launch. The new version may not remember the device you were using before. If so, click on the device and choose "Add additional simulators" from the drop down menu to add the device you want.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-275.png)

## Step #4. Delete the files

If you don't need the older versions of Xcode on your computer, you can uninstall them and get some hard drive space back.

You can also delete the `.xip` file of the version you just downloaded, as well as the `CLT.dmg` file.

That's everything. I hope this has helped you successfully install Xcode. Have fun with it!

