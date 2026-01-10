---
title: CLI Shells – A Brief History of Human-Computer Interfaces
subtitle: ''
author: Chidiadi Anyanwu
co_authors: []
series: null
date: '2023-07-18T16:45:23.000Z'
originalURL: https://freecodecamp.org/news/shells-a-history-of-human-computer-interfaces
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Evernote-cli-geeknote.png
tags:
- name: cli
  slug: cli
- name: command line
  slug: command-line
- name: Computer Science
  slug: computer-science
- name: shell
  slug: shell
seo_title: null
seo_desc: 'By Chidiadi Anyanwu

  A computer is basically a piece of electronic circuitry that performs tasks as instructed
  by its users.

  But for a human to interact with this hardware, they must really know and understand
  how it works. The person must also know t...'
---

By Chidiadi Anyanwu

A computer is basically a piece of electronic circuitry that performs tasks as instructed by its users.

But for a human to interact with this hardware, they must really know and understand how it works. The person must also know the order in which to give the computer various tasks to produce a meaningful result.

But most of us don't know these things. What happened?

In this article, we're going to look at:

* The history of early computing
    
* How operating systems were developed
    
* Modern operating systems
    
* The development of kernels and shells
    
* The history of shells
    
* Why CLI tools are still important
    

## The Early Days of Computers

In the 1800's, computers were mostly used to work on large amounts of numerical data. They were basically programmable calculators the size of small factories.

The data they worked on were also very physical. They were manually fed as punched cards into the machine's card readers. The computers were then programmed by physically rewiring cables, plugboards, and switches to determine what operations would be carried out on the input data. Some of the computers even processed logic through partially mechanical means.

Plugboards allowed you write (or wire) a program and store it so when you needed that program, you'd remove the current plugboard and install a new one. The output of the programs were printed out by line printers, saved on tapes, or punched on cards.

These programming and memory technologies were used in many forms of technological designs.

For example, the Enigma machine which was used to scramble letters and encipher top secret military and diplomatic communication had a plugboard you would rewire to change settings.

The IBM International Daily Dial Attendance Recorder also counted and recorded staff attendance on punched cards. These were more special-purpose equipment.

## Early Operating Systems

The first-ever speech synthesis was done in 1962 on an IBM 704, a computer without an operating system.

At the time of the first computers, nobody ever thought of operating systems. People wrote their programs in machine language (or wired them on plugboards) and ran them. There was no way to run two programs at the same time or perform error detection/correction. Your program ran until it either crashed or completed.

![Picture of a man and a woman operating the IBM 704 in 1957.](https://www.freecodecamp.org/news/content/images/2023/07/IBM_Electronic_Data_Processing_Machine_-_GPN-2000-001881-IBM-704.jpg align="left")

*IBM 704 computer with two operators in 1957*

Initially, computers didn't ship with any software. Later on, IBM included FORTRAN and COBOL compilers in their mainframes. Then came 'resident monitors,' the precursor to operating systems. They literally got the name because they were software that resided in the company's memory and monitored tasks. They basically performed tasks like cleaning up after programs and helping to sequence jobs on the computers.

The first operating systems were made by computer owners who were tired of under-utilizing their computers. They didn't want to have to wait for a program to complete before they manually loaded in another set of data and programs.

One of these early operating systems was the Input/Output System of General Motors and North American Aviation (GM-NAA I/O). Its main aim was to execute the next program automatically after the current one was finished (batch processing). It was created in 1956, and is known as the first-ever working operating system.

IBM later modified one of its customer's operating systems and distributed it as IBSYS. Then, IBM thought that it wasn't good for different computers to have different (machine language) instruction sets, so they stopped all production and started a new line called System/360.

With this, they aimed to build just one operating system for all their computers. It didn't quite go as planned, so they ended up with a family of operating systems, OS/360.

OS/360 included features like time-sharing, error detection/correction, and device management, which are all features implemented in modern operating systems. The OS/360 was introduced in 1964 and was in use until 1977.

Early time-sharing technologies enabled multiple people to access the same mainframe from their different terminals at once. The first computer terminals were teletypewriters (or teletypes). Teletypes were developed around the 1830's but weren't used as computer terminals until the 1970's.

## Modern Operating Systems

The MULTiplexed Information and Computing Service (MULTICS) operating system was initially developed for General Electric's 645 mainframe, and later Honeywell's mainframes when they bought over GE's computer division.

It was jointly developed in 1964 by GE, MIT, and Bell Labs, mainly as a successor to the Compatible Time-Sharing System (CTSS).

It came with a lot of new ideas to the computing world like access control, dynamic linking, support for ASCII, and dynamic reconfiguration.

Dynamic reconfiguration allowed the operators to remove and add memories and CPUs without logging out or disrupting users. With the advent of the Compatible Time-Sharing System (CTSS), computers were looked at as a utility.

The idea was that computers were too big and expensive and could be used by only one person at a time. But what if that expensive hardware could be used more efficiently by allowing more than one person to use them at the same time? That way, the computer could become a public utility, accessed from home with terminals.

With a public utility, you need to be able to carry out maintenance on different components without disrupting the service. That was the usefulness of dynamic reconfiguration.

That idea of computers becoming a public utility seems to have lived on with the use of servers, and now, cloud computing.

At a point, MULTICS didn't work out and the companies went their separate ways. Ken Thompson, one of the programmers, later described MULTICS as 'over-designed,' 'overbuilt,' and close to unusable. In an interview with Peter Seibel, he said that the things he liked enough to take from it were the hierarchical filesystem and the shell.

He later went on to create the UNIX operating system with Dennis Ritchie.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Timeline-Computers.png align="left")

## The Development of Kernels and Shells

One of the major features of the UNIX operating system was the splitting of the operating system into shell and kernel. The OS kernel was then meant to handle all the system calls, while the shell was used to access the system's services without exposing the inner workings of the operating system.

This concept was first introduced by French computer scientist Louis Pouzin in 1965. He also coined the term shell. This is how he described it in a document titled, [The SHELL: A Global Tool for Calling and Chaining Procedures in the System](https://people.csail.mit.edu/saltzer/Multics/Multics-Documents/MDN/MDN-4.pdf).

> We may envision a common procedure called automatically by the supervisor whenever a user types in some message at his console . . . we shall refer to that procedure as the "SHELL".

![Louis Pouzin Shell Document Definitionpng](https://www.freecodecamp.org/news/content/images/2023/07/Louis-Pouzin-Shell-Document-Definition.png align="left")

*Louis Pouzin's Document on Shells*

According to the document, when the user types in a command, the supervisor initiates a new stack to save the command, then calls the shell with the command as an argument.

He also envisioned a future where people created their own shells and used them without having to meddle with the underlying structure of the shell.

> "An important facility is that the SHELL being itself a common procedure may be replaced by a private one supplied by the user. On that way, not only a particular procedure can be replaced on user's choice, but all conventions about typing commands may be tailor-made to user's wishes just by providing his own SHELL."

This idea was first implemented in MULTICS, and is one of the only things Ken Thompson admitted to liking enough to take from the project.

Now, in modern operating systems, the shell is the software that lets you communicate with the operating system, and access the OS services which are things like program execution, file management, and I/O management. It could be a command-line shell (CLI) or it could be a graphical user interface (GUI).

The kernel is the part that handles all the system calls, manages computer resources like memory, CPU, and storage, and handles timesharing between processes.

## History of CLI Shells

Shells as we know them now really began with UNIX, and one of the first was the Thompson shell.

### Thompson Shell (1971)

Ken Thompson, of course, went on to create his own shell. It was a simple command interpreter, not designed for scripting. It introduced the &lt; &gt; symbols for redirecting the input or output of a command, and the | symbol for piping.

### C Shell (1978)

The C Shell (or csh) was created by Bill Joy and enabled scripting. The objective was to create a command language that looked more like the C programming language.

### Bourne Shell (1979)

Stephen Bourne started work on the Bourne Shell in 1976 as a replacement for the Thompson Shell. It was intended as a scripting language. One of the major goals was to enable using scripts as filters.

### Korn Shell (1983)

Developed by David Korn, the Korn Shell was based on source code from the Bourne Shell, and attempted to integrate the features of C Shell and Bourne Shell. It is [POSIX.2](https://en.wikipedia.org/wiki/POSIX) compliant.

### Bourne Again SHell aka BASH (1989)

BASH was written by Brian Fox in 1989 and released under the GNU license as a free and open-source version of the Bourne Shell.

It was one of the first programs Linus Torvalds ported to Linux and is the default shell for most Linux distributions. It was built for scripting and is [POSIX](https://en.wikipedia.org/wiki/POSIX) compliant.

### Z Shell (1990)

The Z Shell (or Zsh) was created by Paul Falstad as an extended and improved Bourne Shell. The name was derived from the name of a teaching assistant at Paul's university named Zhong Shao.

It also enables scripting and is aesthetically superior to Bash. It supports plugins and extensions, auto-completion, and some other globing capabilities that are unavailable in Bash.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Timeline-Shells-1.png align="left")

There are many other popular shells used today, but I'm not going to talk about them.

All these shells mentioned did not apply to Windows (until recently). Windows had two command-line shells: Command Prompt (cmd) and PowerShell. The PowerShell was created as an extension to Command Prompt. It supports cmdlets, scripting, piping, and many more features.

Then in 2019, that changed with Windows Terminal, a new terminal emulator for Windows that can run Bash on what is called Windows Subsystem for Linux (WSL). It also supports Command Prompt, PowerShell, and Azure Cloud shell out-of-the-box.

## Why Are These CLI Tools Important When We Have Graphical User Interfaces (GUIs)?

You may wonder why we would take the pains to go through this whole evolution and yet still love to use CLI tools and shells. What's so interesting about typing commands into terminals?

The first and most compelling reason is that CLI tools are lightweight because they're text-based. In cases where you have servers and other devices where you need to optimize the use of resources, it's not very wise to use up most of the resources to run GUI interfaces.

Using the CLI can also provide you with a great deal of flexibility and speed that you won't get with a GUI. For example, you may want to search for all the images in a folder with 1000 files and rename them in a certain order. Doing that with your GUI will be time-consuming and maybe frustrating. With the CLI, you can just type a few commands.

Scripts are another important feature. Sometimes, there are tasks you want to carry out multiple times and you don't want to have to navigate through menus all the time or even type commands multiple times. You can write scripts that you run to automatically carry out the tasks repetitively.

In cases where you have to access devices remotely, like web servers or network devices, the CLI is also the most favoured method. Also, for some tasks, it's just easier to do them with a few commands than using your GUI—updating your apps on Linux for example.

## Wrapping Up

We've really come a long way from purely mechanical computers to purely electronic computers. The way we interact with computers has changed over the decades, but command-line interfaces aren't going anywhere soon.

Thanks for reading. I hope you enjoyed this article. You can [connect with me on LinkedIn.](https://www.linkedin.com/in/chidiadi-anyanwu)
