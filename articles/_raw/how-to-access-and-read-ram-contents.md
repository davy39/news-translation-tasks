---
title: What is RAM? How to Access Your Computer's RAM and Read the Contents
subtitle: ''
author: Gursimar Singh
co_authors: []
series: null
date: '2023-04-24T19:31:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-access-and-read-ram-contents
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/ram-article.png
tags:
- name: Computer Science
  slug: computer-science
- name: hardware
  slug: hardware
seo_title: null
seo_desc: "This article is a comprehensive guide on how to read the contents of your\
  \ computer's RAM. \nRandom Access Memory (RAM) is a crucial component of any computer\
  \ system, and it is responsible for temporarily storing data that is required by\
  \ the system to ..."
---

This article is a comprehensive guide on how to read the contents of your computer's RAM. 

Random Access Memory (RAM) is a crucial component of any computer system, and it is responsible for temporarily storing data that is required by the system to carry out its functions. But the contents of RAM can be quite volatile, and they are usually lost when the system is shut down.

One way to preserve the contents of RAM is by performing a RAM dump, which is a process of copying the contents of RAM onto a storage device, such as a hard drive. You can analyze the RAM dump, and the data contained within it can provide valuable insights into the system's state at the time the dump was taken.

In this article, I will walk you through the process of reading the contents of RAM, as well as explain what a RAM dump is and how it can be useful in analyzing a computer system. I will also provide you with step-by-step instructions on how to perform a RAM dump and how to analyze the resulting data.

## Why Read RAM Data?

Reading data from the disc is something you might be familiar with doing. But can we also read data straight from the RAM, where the most essential information is stored?

As developers, we can investigate the space complexity and delve further into the RAM to understand what is going on.

Accessing and reading the contents of RAM can be useful in a variety of scenarios. One common use case is for troubleshooting and diagnosing issues with a computer system. By examining the contents of RAM, you can gain insights into the state of the system at a particular point in time. 

For example, if your computer suddenly crashes, examining the contents of RAM can help you identify the cause of the crash.

Another use case is for forensic analysis. When investigating a computer system for evidence of wrongdoing, examining the contents of RAM can provide valuable insights into the activities that were being carried out on the system. 

For example, a security professional may use RAM analysis to determine whether a particular process was running on the system or to identify files that were recently accessed.

In addition, accessing and reading the contents of RAM can also be useful for software developers and researchers. By analyzing the data stored in RAM, developers can gain insights into the performance of their software and identify potential issues or bottlenecks. Researchers can also use RAM analysis to study the behavior of malware or to develop new security tools and techniques.

Overall, accessing and reading the contents of RAM can be useful for troubleshooting, forensic analysis, software development, and research. It provides a valuable way to gain insights into the inner workings of a computer system and can help identify issues and potential security threats.

Before we move further into the specifics, let's take a short look at the nomenclature. This may be common knowledge, but you'll need to understand the terminology as you go through this guide, so it's worth a review.

## What is RAM?

There's a physical hardware device called RAM (which stands for Random Access Memory): the physical memory, a CPU, a hard disk, and other physical components.

On top of this, we have the operating system. The operating system is always in conversation with the piece of hardware known as the "kernel" – and this is one of the most critical aspects of this software.

If we consider things from the user's point of view, we initially log in to the operating system so that we can carry out our tasks, the majority of which include executing applications.

### What is the Kernel?

A kernel is a fundamental portion of an operating system that accepts the instructions from the user with the aid of the program we run behind the scenes. This may happen regardless of the program that we run behind the scenes.

Everything that has to be computed is handled by the central processing unit (CPU), but whatever we do and however we manage the services provided by the CPU, the data, instructions, code, and program must all go via the random access memory (RAM).

This implies that the results of anything we do with the data at any given moment in time will be available on top of the memory. If you are a programmer and you're constructing some kind of data structure, this indicates that all of the data will live on top of the RAM.

We can directly go to the RAM and see how the data structures have been created and how they align, and we can see how the space complexity works there.

For instance, if we are discussing any web browser, such as Chrome, there may have been security flaws generated in an application. So the most effective method is to navigate to the RAM and investigate how the data has been operating.

Let's say you open any secure website in Chrome (or any browser), like gmail.com. Any information you enter into Gmail, including your username and password, is sent over the internet to a server run by Google. That data has been fully encrypted, and it will be challenging, if not impossible, to crack the password.

But in order to enter your password, you likely use a computer with a keyboard attached to it. After that, some programs will encrypt the data and send it to the internet. This means that initially, your data was present in the RAM.

First, the password is standard data, and the password goes and lands on the top of the RAM. Then, some programs will encrypt the data and send it to the internet. If you can access the RAM, you can examine it to determine whether or not your password has been encrypted. And this process is pretty straightforward.

Let's look at an example to see how this works. We'll pretend that "a" is a variable and "9" is the data. When we execute the program, this data loads onto the RAM. When the program ends, the data from the RAM will be gone, although nobody has proven it yet. But this is the case, and we can prove it with a little investigation.

So how can we check whether or not this data is still present in the RAM after the application has finished running if it was loaded at the very top of the memory?

Well, the RAM will be cleared of these contents shortly. A "RAM dump" is the process of capturing all of the RAM. This demonstrates the actual form in which the entire data set is made accessible and loaded onto the RAM for the first time. And you'll learn how to capture or extract the data from memory next.

In order to accomplish this, you'll need some form of software. As a result, the goal of this program is to travel further into the memory. It will go into memory and retrieve all of the stored data from memory before continuing.

### What is LiME?

The Linux memory extractor, sometimes referred to as LiME, is a powerful piece of software. It's what you use to extract the memory from Linux. This piece of software is also known as the driver, also referred to as the module. This is because RAM is a device, which complicates things further.

We need some form of driver to access the device so we can try to read the contents of it. LiME is an example of a driver, and if you're familiar with Linux you may know that in order to make any driver function, you need to load that driver with the assistance of the kernel.

Within the context of Linux, a driver is also referred to as a module. So LiME is a Linux kernel module. We have access to what is known as a kernel loadable module, which allows us to install the module on the operating system.

We have covered enough background. Now, let's look at how we can extract the contents of the RAM. We'll go through the process step-by-step in a hands-on way.

## **Setup** and **Installations**

So, the only thing we need is the LiME driver. Here's the link to download this particular module: [https://github.com/gursimarsm/LiME]( https://github.com/gursimarsm/LiME).

Now, boot up your Linux system (I use RedHat Enterprise Linux). You can use the **`free -h`** command to check the amount of RAM memory that's being used, that's available, and other details. Mine looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-186.png)
_Output from running the `free -m` command_

To access RAM, we need some software where the kernel can load some extra modules. In our case, the module name is LiME. So, the software we install are called “**kernel-devel**”, and “**kernel-headers**”. These two pieces of software are what we need to install in order to perform our subsequent actions, that is to use the LiME module.

If you want to install the software, you should have "yum" configured. For context, **yum** is a command you can use to install the software in the RedHat Linux operating system. I'll demo how to configure it in the appendix for reference.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-187.png)
_Installation_

So, now that you've installed that software, you need one more piece of software because you have to download some drivers from GitHub. So, now you need to install Git if you don't already have it. You can do this using the command **`yum install git`**. You also need to configure your account so that you can work with it.

```bash
# git config --global user.name "Your Name" 

# git config --global user.email "you@example.com"  
```

I shared the repository above. It's a loadable kernel module (LKM). It lets you acquire the entire memory from your Linux operating system or any kind of language operating system (including Android devices because Android is based on Linux as well).

You can download the module using the `**# g**it clone**** [**https://github.com/gursimar**sm**/LiME**](https://github.com/gursimarsm/LiME)` command.

After downloading that, you need to move into the directory of the software. You'll find multiple folders there. But, to run the main code, you need to move to the "src" directory.

In this directory, you'll find multiple programs based on the C language. So, in order to make use of the files, you'll need to compile them. To do that, you can use the **`make`** command. Install that like this:

```bash
# yum install make 

# yum install gcc       
```

In the directory /LiME/src/, run the **`make`** command to compile the entire code.

If you encounter an error, it might be because we are using the latest version of LiME, and it comes with a new feature called orc metadata generate. To implement this feature, you have to install one more thing that's part of LiME called **`elfutils-libelf-devel`**. You can do that using yum like you can see below:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-188.png)
_How to install **`elfutils-libelf-devel`**_

After that's done, if we now run the `make` command it will ask the GCC compiler to compile the entire code. After the compilation, it will create one final object file called the kernel object file, and that is the final module in LiME.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-189.png)
_Output_

You can find this file in the same directory by using the **`ls`** command.

## **How to Use the Module**

With this module, the kernel now has the capability to capture or read the entire RAM. By default, we can't read the entire RAM in one go, but now because of the LiME module, we can.

To learn more about the LiME module, you can use the **`modinfo`** command. Type `modinfo` along with `lime`. This will show you some more details like where the file is available, and it also displays all the modules or drivers that come with some kind of extra parameters. Every parameter has some benefits.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-190.png)
_modinfo_

Here we are going to use two parameters which are very important: `path` and `format`.

`path` means when we read the entire RAM, we have to store the data of the RAM in some file. So, to specify the destination file we would like to create, we have to give that particular information over here.

The next parameter, `format`, specifies the format in which we want to read the RAM data. So, in this case, we want to read the format of the RAM as it is. The data stored in the RAM is mostly in binary, and we want to read the entire data in that binary format only and capture it in its raw form.

So, the format will be raw and stored in the file wherever we give the path.

Finally, it's time to read the data from the RAM. So, let's come to the main command that will help us start reading the entire RAM.

### Demonstration

Type in your password for your Gmail account in Chrome for this demonstration. This will help you learn how to capture the data from the RAM and also if your password is encrypted.

To verify these two things, move to the command prompt and check if the data is still on the RAM. You'll have to load a particular module using the command **`insmod`**. This will help you insert the module.

Copy the complete path of the module and paste it along with the `insmod` command.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-191.png)
_`insmod` command_

This module will get loaded with the help of the kernel. The module will start capturing the entire data from the RAM and it'll store it in a file, for example, myram.data

It will also load the entire memory dump or RAM dump into this file and which format we want to capture. So, the format will be the raw format.

We'll use these two parameters (don't worry about this for now). We need only two parameters to perform, and now as soon as we hit this command, whatever data we have will be captured and stored in this particular file. This command typically takes a few seconds, depending on the CPU speed and the amount of data we have in the RAM.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-192.png)
_Command_

### How to read the data

Now, we have this file myram.data and the entire data of the RAM is stored in this file. Because we captured this data in the raw format, the data is going to be in binary. If we try to read this data from this file directly, as human beings, we can't read it even if we try it with the initial lines using the head command to read some of the top 10 lines.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-193.png)
_Output_

So, we can use the “cat” command, which will read the entire data. But, again, the same thing is going to happen – it will read the entire data, but the data will be displayed in the binary format. Then we need to use the pipe function with this command and combine it with another new command called `strings`:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-194.png)
_Command_

String is a command that will convert the data into regular text in a human-readable format.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-195.png)
_Output_

The list will go on and on. You can interrupt it using **Ctl+C**.

Right now, it won't mean much seeing and reading the entire data. We know some data that are there on the RAM is the password called mywebpasswordgmail. So, just to confirm that this data is available on the RAM we can use one more pipe along with the `grep` command. The grep command helps us sort the data.

```bash
cat /myram.data | strings | grep mywebpasswordgmail 
```

Now, we are searching for this string in the entire data. It will convert the data into regular text, and wherever that particular string shows up, grep will grab that line and let us start searching, then show us this data.

So, as you can see from this simple example, whatever you type on your keyboard can also go into the RAM – even if it's your password or any kind of secure site you are surfing, your data is there on the RAM. It doesn't matter what program you run. If you type using the keyboard everything will load on the RAM and can be extracted. This is called the memory dump.

LiME provides us with many other powerful capabilities. Right now, we are capturing the data directly from the system where we perform the actions. But we can also run LiME on the system and it can capture the data in real-time and send the data over the network to another computer.

What does this mean? Think of it this way: for example, somebody opens a website and they're typing something in real-time. This entire message is being transmitted in real-time to another computer.

We're not talking about key loggers, we are just talking about the RAM. Whatever is happening when any program is running, the database is storing some data. Programs are reading data from other parts of the hard disk. And whatever is happening on the RAM can be captured in real-time by the system and sent over the network to other computers.

# Conclusion

We’ve finally come to the end of this article. I hope you've enjoyed it and have learned something new.

I’m always open to suggestions and discussions on [LinkedIn](https://www.linkedin.com/in/gursimarsm). Hit me up with direct messages.

If you’ve enjoyed my writing and want to keep me motivated, consider leaving starts on [GitHub](https://github.com/gursimarsm) and endorse me for relevant skills on [LinkedIn](https://www.linkedin.com/in/gursimarsm).

Till the next one, stay safe and keep learning.

