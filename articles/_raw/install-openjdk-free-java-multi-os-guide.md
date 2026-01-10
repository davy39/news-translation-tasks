---
title: How to Install OpenJDK (Free Java) – Multi OS Guide
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-19T20:52:44.000Z'
originalURL: https://freecodecamp.org/news/install-openjdk-free-java-multi-os-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-simon-berger-1323550.jpg
tags:
- name: Java
  slug: java
- name: open source
  slug: open-source
seo_title: null
seo_desc: 'By Otavio Ehrenberger

  In a nutshell, there are two coexisting branches of Java: the proprietary, closed-source
  Oracle Java and the community-maintained open-source OpenJDK.

  OpenJDK is licensed under GPL-2.0, and it consists of a Java Virtual Machine ...'
---

By Otavio Ehrenberger

In a nutshell, there are two coexisting branches of Java: the proprietary, closed-source Oracle Java and the community-maintained [open-source OpenJDK](https://github.com/openjdk/jdk).

OpenJDK is licensed under [GPL-2.0](https://github.com/openjdk/jdk/blob/master/LICENSE), and it consists of a Java Virtual Machine and a java-bytecode compiler. Since this is the easier and cheaper way, it's the one we're going to be using in this tutorial.

Here, you'll learn how to install OpenJDK on Windows, Mac, and Linux in a few different ways.

# How to Install OpenJDK

## Very Easy Semi-Automatic Mode – for Windows and macOS

Keep in mind that this will require administrator access.

If you are in a hurry and just want a plug-and-play install with an easy uninstaller and automatic setup, that's fine – I won't judge. :) 

Head over to the community-driven, [Eclipse Foundation-supported](https://blog.adoptopenjdk.net/2021/03/transition-to-eclipse-an-update/) [Adopt Open JDK](https://adoptopenjdk.net/) website to get the link for your installer (if you are in doubt, just go with OpenJDK 11 LTS on HotSpot JVM).

Also, Eclipse is the main open-source Java IDE in case you didn't know.

You'll be redirected to a page with a list of install links. Look for your OS, choose the packaged installer (`.msi` for Windows or `.pkg` for macOS) and download it. **Remember to install ALL features**, as it won't work out of the box if you don't allow the installer to set JAVA_HOME. Then run it and voilà! You're done.

## Very Easy Semi-Automatic Mode – for Linux

This method also needs admin access, of course.

First, remember to run this command:

`sudo apt-get update`

Your OS will very likely have its own OpenJDK package available in the repository manager. 

For Ubuntu/Debian, the package names are usually named like `openjdk-<version_number>-jre-headless`. For example:

`sudo apt install openjdk-8-jre-headless # installs for java 8`  
or  
`sudo apt install openjdk-13-jre-headless # installs for java 13`

That's it, the open-source community saves the day again.

## Still Pretty Easy, Mostly Manual Mode – for Windows, macOS, and Linux

You can get your compressed OpenJDK from a number of different vendors such as Microsoft, Red Hat, Intel or anyone offering their fork of OpenJDK. They might even offer their own installer file. But to keep it simple we're using [Adopt Open JDK](https://adoptopenjdk.net/) once again.

Select your preferred version and JVM ( OpenJDK 11 LTS on HotSpot JVM if you are unsure) and download the compressed JDK.

Why would you choose this option over the much easier methods just described above? Maybe you don't have administrator rights on your current machine or maybe you are setting up your own strategy to manage multiple Java versions. I don't know, but it has its use cases.

### Steps for Windows

1. Store the extracted files in the Directory Tree

First, extract the zip file into a folder (`C:\Program Files\OpenJDK` would be the [educated choice](https://www.makeuseof.com/tag/default-windows-files-folders/). Note that `\OpenJDK` was manually added). It will create the folder for the JDK installation, with `\bin` as one of its sub-directories.

You will need Administrator privileges to extract the zip file to this location.

If you cannot use Administrator rights for any reason, extract it to a location under your user space, such as `C:\Users\%YOUR_USERNAME%\OpenJDK`.

2.  Open Environment Variables

Open the Control Panel > System & Security > System > Advanced System Settings (it'll be under 'Device Specifications in Windows 10+).

In the System Properties window, select the Advanced tab, then Environment Variables.

3.   Set JAVA_HOME:

Under System Variables, click New. Enter the variable name as JAVA_HOME. Enter the variable value as the installation path of the JDK (appending the `\bin` sub-folder at the end of the path). Mine was `C:\Program Files\OpenJDK\OpenJDK11U-jdk_x64_windows_hotspot_11.0.15_10\jdk-11.0.15+10\bin`.

Click OK and Apply Changes. If you are doing this process as a non-admin, choose `User Variables` instead.

4.   Add the binary executables to PATH:

Stay in the Environment Variables window. Click on the variable named `Path` (either for System or User, depending on your choice in the last section).

You'll see a list of stuff. These are the executables you have access from your CLI (like Windows Terminal, Command Prompt, or Poweshell).

Click on 'New' at the top-right corner and add `%JAVA_HOME%` as a variable.

Click OK and Apply Changes.

5.   Test Installation

Open a Command Line Interface. Type `java -version`. If the output was the version, all was OK, congrats!

If it wasn't, restart your computer and try again. If it still isn't working, double-check this tutorial, try to read your JAVA_HOME path, and see if it points to the the bin folder within the downloaded folder's path.

### Steps for Linux/macOS:

1. Store the extracted files in the Directory Tree:

Then, extract the compressed file appropriate to your OS. In case you can't or don't want to use admin permissions, extract it somewhere in your user space (like `~/.openjdk`).

If you want a more conventional location, extract it to `/usr/local/`, which is where software manually installed by the user conventionally goes in POSIX systems.

My command (for Linux) was this one: `sudo tar -xf OpenJDK11U-jdk_x64_linux_hotspot_11.0.16.1_1.tar.gz -C /usr/local`.

2.   Set JAVA_HOME and add it to PATH:

Set JAVA_HOME to where you extracted your OpenJDK installation. Point it to the OpenJDK directory, not to its `/bin` subfolder, as JAVA_HOME will not only be used to determine the executables' location.

This should be located in your shell initialization file. For example, let's suppose These are the two last lines of my `~/.zshrc` file:

```
   export JAVA_HOME="/usr/local/jdk-11.0.16.1+1"
   export PATH="$JAVA_HOME/bin:$PATH"

```

3.   Verify Installation

Now, refresh your shell by either sourcing the init file or opening another tab/window.

You can check installation with `java -version`. If no errors are displayed, congratulations! Time to do some Java'ing.

## Wrapping Up

And that's it! Now you should have OpenJDK installed and ready to use on your machine. Thanks for reading.

