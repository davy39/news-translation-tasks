---
title: Windows vs MacOS vs Linux – Operating System Handbook
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-04-12T20:14:34.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-operating-systems
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/artiom-vallat-mx9axbKqKW8-unsplash.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Computer Science
  slug: computer-science
- name: Linux
  slug: linux
- name: mac
  slug: mac
- name: software development
  slug: software-development
- name: Windows
  slug: windows
seo_title: null
seo_desc: 'Hi everyone! In this handbook I''m going to give a brief introduction to
  operating systems and compare the three main OSs that are out there nowadays.

  First we''re going to review what an OS is and little history about them. Then,
  we''ll review the main...'
---

Hi everyone! In this handbook I'm going to give a brief introduction to operating systems and compare the three main OSs that are out there nowadays.

First we're going to review what an OS is and little history about them. Then, we'll review the main features and differences of the most popular operating systems (Windows, Mac, and GNU/Linux).

The idea here is to explore their history, how and by whom they were developed, their business models, and their pros and cons. This will give you a better idea of how they work and which one to choose.

I'm going to share facts as well as my personal opinions about this subject. So keep in mind some of the things I mention here will be based on my own experience and analysis of the topic.

I'll also provide a lot of additional articles/videos you can take a look at in case you'd like to dive into a particular subject.

Without further ado, let's go!

## Table of Contents

* [What is an Operating System?](#heading-what-is-an-operating-system)
    
* [A Bit of History of Operating Systems](#heading-a-bit-of-history-of-operating-systems)
    
* [The Three Main OSs](#heading-the-three-main-oss)
    
    * [Windows Operating System](#heading-windows-operating-system)
        
    * [MacOS](#heading-macos)
        
    * [GNU/Linux](#heading-gnulinux)
        
        * [Debian](#heading-debian)
            
        * [Ubuntu](#heading-ubuntu)
            
        * [Mint](#heading-mint)
            
        * [Fedora](#heading-fedora)
            
        * [Red hat Enterprise Linux](#heading-red-hat-enterprise-linux)
            
        * [Arch Linux](#heading-arch-linux)
            
* [Windows vs Mac vs Linux – OS Comparison](#heading-windows-vs-mac-vs-linux-os-comparison)
    
    * [File systems](#heading-file-systems)
        
    * [Shells](#heading-shells)
        
    * [Package managers](#heading-package-managers)
        
    * [Cost](#heading-cost)
        
    * [Software compatibility](#heading-software-compatibility)
        
    * [Hardware quality and compatibility](#heading-hardware-quality-and-compatibility)
        
    * [Ease of use](#heading-ease-of-use)
        
    * [Security and stability](#heading-security-and-stability)
        
    * [Community and culture](#heading-community-and-culture)
        
* [Which Operating System to Choose](#heading-which-operating-system-to-choose)
    

## What is an Operating System?

According to [Wikipedia](https://en.wikipedia.org/wiki/Operating_system#Examples),

> "An operating system (OS) is software system that manages computer hardware, software resources, and provides common services for computer programs".

You can think about an OS as an "intermediary" program that stands between your computer and all other programs you run on it. It will manage crucial basic tasks such as file management, memory management, process management, input-output management, and controlling peripheral devices.

OSs were created to simplify the use of computers. Nowadays any given program can worry only about executing its core features and leave all basic system functionalities to the OS. But things weren't always like this...

## A Bit of History of Operating Systems

![an9zgv0_700b](https://www.freecodecamp.org/news/content/images/2022/04/an9zgv0_700b.jpg align="left")

In the old days (1940's-50's) programs were written to run on specific machines. That means a program could run on one and only one computer model.

If you wanted to execute the same program on a different computer model, programmers would need to write the whole program again because the hardware was configured in a different way. There was no layer of abstraction between the running program and the actual hardware.

Side comment: Do you ever stop and think about the work of a programmer back in those days? Programs were written in punch cards! =O It just blows my mind every time I think about it... It's amazing how low level things were at that time and the progress technology has achieved thanks to those early programmers.

![837755a86e841b0452e12f0786128e02](https://www.freecodecamp.org/news/content/images/2022/04/837755a86e841b0452e12f0786128e02.png align="left")

By the 1960's industry giants such as IBM and AT&T started working on operating systems that could act as a layer of abstraction between hardware and software, which would simplify the implementation of new programs.

The most notorious of these projects was [**Unix**](https://wikipedia.org/wiki/Unix), which was an OS developed in Bell labs at AT&T by developers [Ken Thompson](https://wikipedia.org/wiki/Ken_Thompson) (who's currently working on the development of the Go programming language) and [Dennis Ritchie](https://wikipedia.org/wiki/Dennis_Ritchie) (who also created the C programming language. Freaking coding legends, yup.).

![ken-thompson-dennis-ritchie-111013](https://www.freecodecamp.org/news/content/images/2022/04/ken-thompson-dennis-ritchie-111013.jpg align="left")

Unix was hugely successful and inspired the creation of many other OSs with very similar characteristics. Those later on had a big influence on GNU/Linux and MacOS, which we're going to review in a sec.

By the 1980's, computers performance, accessibility, size, and price had improved to a point where the general public could buy them and use them for personal tasks. This made OSs shift from corporate-specific functions to general usage. And this takes us to the modern age...

> If you're interested in a more detailed explanation of how OSs work and their history, here's [a great video](https://www.youtube.com/watch?v=26QPDBe-NB8) about it. This channel has an incredible crash course series about computer science too, I definetely recommend it! ;)

# The Three Main OSs

In the modern days, when speaking about personal desktop/laptop computers, the three most used operating systems are Microsoft Windows (with around 80% market share), Apple MacOS (with around 15% market share), and GNU/Linux based OSs (with around 3% market share).

Regarding servers, around 80% run GNU/Linux and 20% run Windows. And talking about mobile devices, around 75% run Android (which uses the Linux kernel) and 25% run IOs (which is Apple's mobile OS).

We're going to briefly review each of them individually and later on compare all of them to identify their differences.

## Windows Operating System

![516094c7ed4e0--1-](https://www.freecodecamp.org/news/content/images/2022/04/516094c7ed4e0--1-.jpeg align="left")

Windows' ancestor is [MS-DOS](https://wikipedia.org/wiki/MS-DOS), a text-based OS Microsoft released in 1981.

MS-DOS was developed to be compatible with IBM PCs and it was very successful. But to make it more accessible to the general public, it needed a GUI, and that's what Microsoft shipped in 1985 with [Windows](https://wikipedia.org/wiki/Microsoft_Windows) 1.0.

Since then, Windows has released many versions, like 95, 98, XP, Vista and so on... And has made itself the most widely used operating system worldwide.

Windows accessibility and the fact that it comes pre-installed in most personal computers (thanks to commercial agreements) have made this OS the most popular one to this day.

[Here's a cool video](https://www.youtube.com/watch?v=hAJm6RYTIro) that summarizes Windows history in just 3 minutes.

And if you're interested in knowing more about the history of Microsoft, here's another [cool video about it](https://www.youtube.com/watch?v=JmtPWvT1vp8).

Regarding its business model, I'd say Windows strategy is to flood the market and make its system as accessible and easy to use as possible. Their primary target customer is the general user, so not much particular importance is given to customization, security, or performance.

Windows is just the default OS for most people. It's the first one they get to know and it allows the user to easily run daily tasks (internet browsing, gaming, office work) without much config at all.

Windows is a private piece of software, meaning its source code isn't publicly available. Only Microsoft has access to it.

At first, users had to pay if they wanted to buy a copy of Windows OS or upgrade their Windows version. But with their latest releases, Windows has adopted a freemium model. Under this business model, the user can access most of the software functionalities for free and only needs to pay to access particular features.

The key to understanding this shift is to understand that Microsoft has a hugely diversified portfolio of businesses (Xbox - in Gaming, Azure - in cloud platforms, LinkedIn - in social networks, Bing - in search engines, GitHub... just to name a few). By making Windows free, they keep flooding the market and make it even easier for people to adopt it as the default OS.

Another thing to keep in mind is that Windows shows advertisements within the operating system. So it can be thought as an advertising platform as well.

Yet another cool video explaining this move [here](https://www.youtube.com/watch?v=AYaRzp--xyk).

And a bizarre/funny/tiny-bit-scary [example of Microsoft's old school marketing style](https://www.youtube.com/watch?v=EtuDS0ntaJY).

## MacOS

![How-do-I-plug-a-USB-stick-into-this--2000-Macbook-meme-7242](https://www.freecodecamp.org/news/content/images/2022/04/How-do-I-plug-a-USB-stick-into-this--2000-Macbook-meme-7242.png align="left")

MacOS (previously called OS X) is a line of operating systems created by Apple. It comes pre-installed on all Macintosh computers, or Macs. The first version of it was released in 1984 and it was the first OS for personal computers to come with a built-in GUI.

MacOS is built on top of a UNIX-like OS, which is why this MacOS shares many common characteristics with GNU/Linux-derived ones.

In my opinion, Apple's business model is mainly based on differentiation and exclusivity. Unlike Microsoft, Apple makes both the hardware and software of their products, and Apple's software runs only on their own machines.

Apple has positioned itself as a top-tier manufacturer within the technology market, aiming to offer its customers high quality hardware and software, for a considerably higher price than most of the competition.

Exclusivity is promoted as a perk to users too, selling the idea of being part of a select group of people when owning an Apple product.

The fact that you can't run any software you want in their hardware, and that you can't install their software anywhere else than a Mac machine is part of the same idea. You need to buy the whole package if you want to be part of the group.

Apple makes most of its software and hardware differently and many times incompatible with others. Unlike Microsoft, whose idea is to make the product as widely available and easy to get to as possible, Apple aims to make their products top quality but pricey and incompatible with other hardware.

Another great marketing move by Apple has been their ability to profit on the hugely charismatic and influential personalities of people like [Steve Jobs](https://wikipedia.org/wiki/Steve_Jobs). They have taken advantage of his position and trajectory as an industry leader, innovator, and somehow "rebel", to implicitly translate those same values to their products.

Take a look at these ads to know what I mean:

* [Think different ad](https://www.youtube.com/watch?v=5sMBhDv4sik)
    
* [1984 ad](https://www.youtube.com/watch?v=VtvjbmoDx-I)
    

If you're interested in knowing more about the history of MacOS, [here's a video about it](https://www.youtube.com/watch?v=c77lU0Rhq8k).

## GNU/Linux

GNU/Linux is the base of many open-source OSs. Unlike the examples we've just seen, GNU/Linux isn't a full operating system, but a set of programs/utilities and a kernel that many open-source OSs share.

Let's review each part separately.

[GNU](https://wikipedia.org/wiki/GNU) is a huge collection of programs and utilities that was started by [Richard Stallman](https://wikipedia.org/wiki/Richard_Stallman).

![EInHz4EWkAQYthk](https://www.freecodecamp.org/news/content/images/2022/04/EInHz4EWkAQYthk.jpg align="left")

The GNU project was started in 1983 with the idea of developing a free UNIX-like OS (UNIX was property of AT&T so it wasn't available for free). Stallman started developing programs and utilities necessary for the OS, but one key piece was missing – the kernel.

The [kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system)) is the heart of any OS. It's the piece of software that interacts the closest with the hardware and the rest of the OS sits on top of it. The Kernel is responsible for low-level tasks such as disk management, memory management, task management, and so on.

By 1991, a student from Helsinki university named [Linus Torvalds](https://es.wikipedia.org/wiki/Linus_Torvalds) started developing a Kernel for a UNIX-like OS.

![linus-torvalds](https://www.freecodecamp.org/news/content/images/2022/04/linus-torvalds.jpg align="left")

In the following years, both projects started to interact and were joined together to form a solid base that any OS could use.

The key here is that both projects are open-source, and completely free software. This means:

* Anyone is free to run the program, for any purpose.
    
* Anyone is free to study how the program works, and change it to make it do what they wish.
    
* Anyone is free to redistribute copies of the original software.
    
* Anyone is free to distribute copies of modified versions of the software.
    

To better understand the free software movement, [listen to this TED talk by Richard](https://www.youtube.com/watch?v=Ag1AKIl_2GM).

And then watch Richard speak Spanish and [sing a song about free software](https://www.youtube.com/watch?v=9sJUDx7iEJw) (you gotta love this guy...).

The approach Stallman and Torvalds took in the development of GNU/Linux is radically different to the examples we've seen and to what the industry was used to up to that point.

Making GNU/Linux free was not only the right thing to do from its developers' points of view – it was also an excellent choice from the software quality point of view. This is because thousands of developers and companies around the world choose to collaborate for free in order to improve the system.

Some of the GNU/Linux distributions are known to be the most secure and stable OSs out there. They're used in key spheres such as banking, finance, government, and military.

A big part of this is thanks to the open-source model behind GNU/Linux, and that thousands of people around the world are able to review the code, fix bugs, and propose improvements constantly.

These two videos by the Linux foundation explain [how Linux was born](https://www.youtube.com/watch?v=5ocq6_3-nEw) and [how it currently operates](https://www.youtube.com/watch?v=yVpbFMhOAwE).

As mentioned, GNU/Linux serves as the base for many other OSs. These OSs are called "distributions" or "distros" within the Linux world. All have in common that they're based on the same kernel and set of utilities. They can be thought of as "flavors" of Linux.

There's not much of a difference between certain distros, but others have distinctions worth mentioning. Let's quickly review the most used distros in order to better understand this:

### Debian

Debian is an OS that contains only free, open-source software. Debian was started in 1993 and is still going strong and releasing new versions. Debian is known mainly for its stability and security, which makes it more conservative and "slow" when it comes to new releases.

### Ubuntu

Ubuntu is the most widely used GNU/Linux distro. It was created to take the core parts of Debian and improve on them more quickly. It also has a bigger focus on user friendliness and accessibility, which probably makes it the best option for someone coming from Windows or MacOS background.

Ubuntu normally offers releases every six months, with a more stable LTS (long term support) release every two years. Ubuntu is run by a company called [Canonical](https://canonical.com/).

### Mint

Mint is a distro built on top of Ubuntu. Originally it was loved by many because it included media codecs and proprietary software that Ubuntu didn’t include.

### Fedora

Fedora is a distro that focuses strongly on free software. Fedora is sponsored by a company called [Red Hat](https://es.wikipedia.org/wiki/Red_Hat), which at the same time is owned by [IBM](https://www.ibm.com/).

### Red hat Enterprise Linux

Red Hat Enterprise Linux is a commercial Linux distro managed by a company called Red Hat, which is listed on the Nasdaq. The OS is used mainly for servers and corporations. It’s based on the open-source Fedora project, but designed to be a stable platform with long-term support.

Red Hat uses trademark law to prevent Red Hat Enterprise Linux software from being redistributed. However, the core software is free and open-source.

### Arch Linux

Arch is possibly the most hard-core Linux distro. It's very lightweight, flexible and minimal. With Arch, the user is completely in charge of configuring the system. The purpose of Arch is not to be mainstream. It's meant for users that have deep understanding of how a computer and an OS work, or are at least interested in learning.

You can learn more about Arch and how much you can customize it [in this in-depth handbook](https://www.freecodecamp.org/news/how-to-install-arch-linux/).

Here's a [great video](https://www.youtube.com/watch?v=ShcR4Zfc6Dw) that quickly summarizes the history of GNU/Linux and goes through the characteristics of the main distros. Fireship is another awesome channel I recommend. ;)

Regarding GNU/Linux business model, well they're not a business to start off. Both Linux and the Free software foundation (the organization behind GNU) are NGOs that operate thanks to donations.

Linux, for example, makes money through Platinum, Gold, Silver and Individual memberships.

Companies like Microsoft, Google, Facebook, Cisco, Fujitsu, HPE, Huawei, IBM, Intel, Oracle, Qualcomm and Samsung are all active contributors to the Linux foundation. This makes sense for companies because they all benefit from the knowledge and technology generated by Linux, and their donations may be tax deductible, too.

Regarding the distros, some of them are completely free and maintained by volunteers and others are maintained by companies and are free to particular users but commercialized for corporate users. Another business model used is free usage but charging for support for corporate users.

Today, Linux runs on most servers worldwide. It's used on most supercomputers and also on most cellphones (as mentioned above, Android uses the Linux kernel).

On the desktop/laptop side of things, Linux usage isn't nearly as widespread. And that's probably because it's not as widely available by default as Windows, and it's nowhere near as marketed as Mac.

Also, especially back in the day, the learning curve necessary to implement and use Linux was considerably higher than for the other two OS options.

Anyway, this situation has been changing lately as Linux distros put more focus on user-friendliness and it's easier than ever to get computers with Linux distros installed by default.

## Windows vs Mac vs Linux - OS Comparison

OK, besides history, business model, and so on, what are the actual differences for the user when it comes to these three operating systems?

The short answer is not that much, actually. But let's review some differences in these operating systems' design, features, and user experience, and later on I'll give you my opinion on this.

### File systems

The way Windows organizes files is different from the way Mac and GNU/Linux do.

Windows uses "drives". They're usually a C and D drive that store all the computer files, and separate drives for external devices such as CDs, USBs, and so on.

![992219e7-6b1f-4528-93d5-495994b77a5e](https://www.freecodecamp.org/news/content/images/2022/04/992219e7-6b1f-4528-93d5-495994b77a5e.png align="left")

Mac and GNU/Linux have a similar file system that comes from UNIX. In these OSs there are no drives – everything in the computer is considered a file (even external devices) and all files are organized in directories that descend from a single root directory. The directory structure is formed as a tree that has a unique root.

This doesn't necessarily make much of a difference for the end user, but is something to keep in mind if you're used to navigating one type of file system or the other.

### Shells

Both GNU/Linux and Mac have Bash as their default shell, while Windows has its own shell that uses a different syntax.

As developers and avid terminal users, learning Bash is probably the best choice as this knowledge can be more easily translated to all OSs than the Windows shell. Especially taking into account that GNU/Linux runs on most servers worldwide, which is one of the main occasions when you'd need to use the terminal to interact with the computer.

If you'd like to know more about shells and terminal usage, I recently wrote [an article about that](https://www.freecodecamp.org/news/command-line-for-beginners/).

### Package managers

Mac and GNU/Linux come with package managers installed by default. A package manager is a piece of software that allows you to install, update, and uninstall programs from the terminal, just by entering a few commands.

They're super helpful, especially when you're installing and uninstalling things constantly, as it's much more efficient to install programs through package managers than manually.

Mac's package manager is called [homebrew](https://brew.sh/). On GNU/Linux, the default package manager depends on the distro. For example, Ubuntu comes with [APT](https://ubuntu.com/server/docs/package-management), Arch comes with [Pacman](https://wiki.archlinux.org/title/pacman), and so on.

All package managers function in a similar way, but there are some differences in the syntax used for each. It's also important to mention that you can install and run a different package manager than the default.

Windows doesn't come with a default package manager. If you want one, you need to install it first. One of the package managers available for Windows is [Chocolatey](https://docs.chocolatey.org/en-us/).

### Cost

As already mentioned, most GNU/Linux distros are completely free for anyone to use. Windows has a freemium model currently and MacOS runs only on Mac computers, which are quite pricey as you may know.

### Software compatibility

Windows is the most widely used OS, and thanks to that most software is adapted to it. Even though less popular, MacOS is similar to Windows in this regard.

Back in the day, Linux wasn't compatible with many programs out there, but this has started to change recently, especially with the most popular distros like Ubuntu.

### Hardware quality and compatibility

When it comes to hardware, only Apple has direct responsibility for the computers that the OS runs on. And Apple's hardware is some of the best out there.

As a company, Apple is focused on providing top quality products, so their newest computers tend to be the ones with best performance all across the market.

Given that Apple designs and develops both hardware and software, it's possible that the compatibility between the machine and the OS is tuned finer than with Windows or GNU/Linux.

On the Windows and GNU/Linux side, hardware quality is completely up to what the user decides or can afford to buy. The good thing here is that you can install the OS wherever you want.

This is particularly cool when thinking about installing lightweight Linux distros on older computers that can't handle the requirements of bigger and more consuming OSs like Windows.

### Ease of use

Windows and Mac are really simple and user-friendly OSs. Regarding GNU/Linux, it depends on the distro you choose. As mentioned, distros like Ubuntu are practically as easy as Windows or Mac, and others like Arch are intended for advanced computer users.

### Security and stability

Some GNU/Linux distros are considered the most secure and stable ones nowadays. The fact that the code is available to everyone isn't a security threat as you may think at first – but rather it's an advantage. Bugs can be identified and worked on quicker, and when a security breach is identified lots of people can work on it and propose fixes.

Windows, on the other hand, is considered the least secure and stable of the three. Given that it's the most popular OS, most malware is developed to attack Windows OS too.

### Community and culture

If you're interested in learning more about a particular OS, studying how it works, how to modify it and create projects based on it, GNU/Linux is definitely the way to go. It's the only one that has its code available to anyone and its online community is huge.

Even though GNU/Linux isn't as widely used as the other two OSs, I find Linux users are usually people interested in software and technology, and people who like to talk, learn, and share knowledge about it.

Mac has its set of fans too and is particularly popular among creatives (graphical designers, video editors, animators, and so on).

And finally Windows is commonly used by the general user and in corporate environments.

Regarding organization culture, I think it could be interesting to visualize it in the working environment of the people who created this OSs:

* Take a look at [Apple's headquarters](https://www.youtube.com/watch?v=FzcfZyEhOoI)
    
* [Bill Gate's "home office"](https://www.youtube.com/watch?v=ZjyVjU4gkHM)
    
* And [Linux Torvalds home office](https://www.youtube.com/watch?v=jYUZAF3ePFE)
    

> If you'd like to see a more in depth comparison these three OSs, Zach Gollwitzer has a [very good video about this topic](https://www.youtube.com/watch?v=09puF-VKWeI) (another great channel to follow ;)).

## Which Operating System to Choose

I've had the chance to use all three OSs recently, and as I mentioned, I don't think the differences between each of them are THAT big.

In my opinion, Linux is a smart choice because it works great, it's widely used across the tech industry (so all knowledge can be translated to work environments), and if you're interested in learning more about how it works there's a huge community that supports that. And most important of all... it's free!

I mean, if we have one of the best and most widely used pieces of software in human history within our reach and completely for free, why would we pay to get anything else?

Regarding other matters, I think most things you can do on GNU/Linux you can also do on Mac and Windows, at least for most users. It probably wont make a huge difference in your daily life, at least from my perspective.

About hardware, buying a modern Apple computer is almost a guarantee of having a great performing machine (if you can afford it). But if you know a bit about hardware or take the time to investigate around, you can easily find very good choices too for a smaller price.

At the end, I think it's important to know what you're using and know the options out there. As computer users, it's a good idea to be aware of facts and differences, and avoid being distracted by marketing campaigns.

I also don't believe in placing too much judgment or weight in one choice or the other. The fact that someone chooses an open-source OS doesn't make that person smarter or superior that someone who doesn't... Just as owning the latest Mac computer won't make you a better programmer.

Long story short, whatever you choose is fine as long as your system allows you to do what you want.

As always, I hope you enjoyed the article and learned something new. If you want, you can also follow me on [linkedin](https://www.linkedin.com/in/germancocca/) or [twitter](https://twitter.com/CoccaGerman).

Cheers and see you in the next one! =D

![goodbye](https://www.freecodecamp.org/news/content/images/2022/04/goodbye.gif align="left")
