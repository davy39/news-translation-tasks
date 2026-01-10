---
title: How to Install Java on Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-03-03T18:07:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-java-on-windows
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/fCC-Cover-Image.jpg
tags:
- name: Java
  slug: java
- name: Windows
  slug: windows
seo_title: null
seo_desc: "If you want to run any Java program on your Windows PC, you won't be able\
  \ to do it without installing the Java Development Kit (JDK for short). \nThe JDK\
  \ also contains the Java Runtime Environment (or JRE) which is the core of a Java\
  \ program. \nIf you ..."
---

If you want to run any Java program on your Windows PC, you won't be able to do it without installing the Java Development Kit (JDK for short). 

The JDK also contains the Java Runtime Environment (or JRE) which is the core of a Java program. 

If you are a beginner trying to learn how to run Java programs in your Windows operating system, then you might face difficulties installing Java correctly on your computer. But fear not! I will cover everything you need to know to prepare your Windows computer fully for running Java programs.

I will be using Windows 11 in this article, but the same method is applicable for the other versions of the Windows operating system as well.

## Download Java from Oracle

If you are wondering why we download Java from Oracle, then the following excerpt from [Wikipedia](https://en.wikipedia.org/wiki/Oracle_Corporation) will help:

> Java is a set of computer software and specifications developed by James Gosling at Sun Microsystems, which was later acquired by the Oracle Corporation, that provides a system for developing application software and deploying it in a cross-platform computing environment.

We download the official JDK directly from the official website of Oracle. So, go to their website: [https://www.oracle.com/](https://www.oracle.com/).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--13--1.png)

You might get this type of prompt to remind you to go to the country closer to you so that you can get a better downloading speed. As I am from Bangladesh, so it is suggesting that I visit Oracle Bangladesh. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--14-.png)

You can select the country closer to you to get a better download speed, but if you do not want that and just download from the global site instead, that's fine, too. You will get the exact installer file from there as well.

Then the website might reloaded itself.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--17-.png)

Click on **Products**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--18-.png)

Then click **Java**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--19-.png)

It will take us to the product page of Java.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--21-.png)

Click **Download Java**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--21--1.png)

Then you will get the download page.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--22-.png)

Simply scroll down a little until you get the OS (Operating System) selection tab.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--23-.png)

Since you want to install Java on your Windows computer, simply click **Windows**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--24-.png)

Then Click **x64 Installer**. You will get a prompt to download the installer file.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--25-.png)

Download the executable file. You'll need to wait a little while for it to complete the downloading process.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--26-.png)

## How to Install Java

After downloading the file, you will get an executable file like below:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--27-.png)

Simply double-click on that file. An installation wizard will appear.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--28-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--29-.png)

Click `**Next>**`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--30-.png)

We will use the default directory. So click `**Next>**`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--31-.png)

Finish the installation process.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--32-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--33-.png)

After finishing the installation, click **Close** to close the installation wizard.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--35-.png)

## How to Add the Directory to the Path of the Environment Variable

Open the file explorer.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--36-.png)

Go to the directory where you have installed the installer earlier. In this case, the default directory is always the **C drive.** 

After going into the C drive, go into the **Program Files** folder.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--38-.png)

Go in to the Java folder.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--39-.png)

Go into the `**jdk-17.0.2**` folder. Here, `**17.0.2**` represents the JDK version. In your case, the version might be different as the JDK will get updated in the future, but the process is exactly the same.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--40-.png)

Go into the **bin** folder. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--41-.png)

The binary files are kept here.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--42-.png)

We need to copy the directory path (directory address) of this folder.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--43-.png)

Simply copy the address using your mouse, or you can use the shortcut `Ctrl` + `A` for selecting all, and then use `Ctrl` + `C` for copying the directory.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--44-.png)

Go to the **Control Panel**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--45-.png)

Go to **System and Security**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--47-.png)

Click **System**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--49-.png)

Click **Advanced System Settings**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--51-.png)

**Alternatively**, you can hop into the Advanced System Settings by simply searching that from your taskbar.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot-2022-03-03-103840.png)

Click Environment Variables.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--53-.png)

Select the Path and click Edit.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--55-.png)

Click New.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--58-.png)

A blank box will appear.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--59--1.png)

Paste the directory path. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--60-.png)

You can use the shortcut keys `Ctrl` + `V` for that as well.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--61-.png)

Click OK.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--62-.png)

Click OK.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--64-.png)

Click OK.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--65-.png)

## How to Check if Java Was Installed Successfully

Open the terminal (CMD or PowerShell).

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--66-.png)

Check the Java version using `java --version`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--68-.png)

If it provides the version you have just installed, then you are good to go!

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--69-.png)

Alternatively, you can simply run some Java code to check whether it is working or not. For now, I will execute a simple Hello World code in Java. I used notepad for now, but you can use any text editor you want.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--70-.png)

Compile your Java code using `javac file_name_with_extension`. Then run the class file using `java file_name_without_extension`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--71-.png)

Wow! Everything is working perfectly. Your Windows machine is ready to execute any Java programs now.

I have also [published a video](https://youtu.be/jGuh6IV-5Vw) on my [English YouTube channel](https://www.youtube.com/channel/UCG97GCUifMS2Vm28tgXQi0Q) where I walk you through all of the processes mentioned above. You can also check that out here:

%[https://www.youtube.com/watch?v=jGuh6IV-5Vw]

## Conclusion

I hope this article helps you install Java on your Windows operating machine. 

If you want to know how to install C and C++ compilers for your Windows operating system, [then you can check this article](https://www.freecodecamp.org/news/how-to-install-c-and-cpp-compiler-on-windows/).

If you want to know how to install Python on your windows, [then you can check this article](https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/).

Thanks for reading the entire article. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!

