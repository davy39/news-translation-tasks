---
title: Ethical Hacking 101 – How to Set Up Metasploitable on Your Computer
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2024-03-12T12:39:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-metasploitable
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-mati-6330644.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: virtual machine
  slug: virtual-machine
- name: 'VirtualBox '
  slug: virtualbox
seo_title: null
seo_desc: 'Ladies and Gentlemen, welcome to the world of Virtual Machines 🖥️

  So you’ve discovered the world of ethical hacking and you want to try your hands
  on something. Trouble is, doing some ‘practical application’ on the wrong thing
  could get you fined, a...'
---

Ladies and Gentlemen, welcome to the world of Virtual Machines 🖥️

So you’ve discovered the world of ethical hacking and you want to try your hands on something. Trouble is, doing some ‘practical application’ on the wrong thing could get you fined, arrested, and even undesired jail time.

You don’t have to give up your dreams just yet though. There is a legal, ethical way to sharpen your cyber offensive skills: Vulnerable Virtual Machines.

In this tutorial, we’ll take a look at the following:

1. [What is a Virtual Machine?](#heading-what-is-a-virtual-machine)
2. [What is Metasploitable?](#heading-what-is-metasploitable)
3. [How to Set Up Metasploitable](#heading-how-to-set-up-metasploitable)
4. [A Quick Word on Vulnerable VMs](#heading-a-quick-word-on-vulnerable-machines)

So without further ado, let’s jump in.

## What is a Virtual Machine?

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-38.png)
_Virtual Machines ¦ Credit: [Hackersarts](https://www.deviantart.com/hackersarts" rel="noopener noreferrer)_

A Virtual Machine (VM) is an emulation of a computer system. Think of it like a mini disposable environment where you can play around with different operating systems and software. 

On a VM, you can delete critical system files, test software, or even install a virus (not recommended), and nothing will happen to your actual system.

All this is made possible with a hypervisor, a software that takes some of your ‘host’ system’s hardware resources, and makes it available for the ‘guest’ machine. A hypervisor allows you to determine things like how much RAM, storage, and even screens (if you have multiple displays), you want to hand over to the VM.

There are 2 types of hypervisors, namely:

* Type 1 hypervisors
* Type 2 hypervisors

Mind blowing naming scheme, I know.

Type 1 hypervisors run directly on the physical host machine and have direct access to hardware resources. They tend to be used for servers and enterprise-level infrastructure. They are considered more efficient because of their direct access to the host resources. Examples of type 1 hypervisors include Microsoft Hyper-V and VMware ESXi.

Type 2 hypervisors, on the other hand, are installed on the host OS, and manages the hardware resources for the guest. You would find these on personal computers and they make hardware resource management pretty easy for the average user. Examples of type 2 hypervisors are Oracle VirtualBox (my personal favourite 😌) and VMware Workstation.

We’ll be using Oracle VirtualBox, a type 2 hypervisor, for simplicity (and because I don’t have a server randomly lying around the house). Now, let’s find an appropriate vulnerable VM to install.

## What is Metasploitable?

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-39.png)
_A mere box ¦ Credit: [Rostislav Uzunov](https://www.pexels.com/@rostislav/" rel="noopener noreferrer)_

Metasploitable is an ‘intentionally vulnerable virtual machine’ by Rapid7, owners of the popular security project, Metasploit. Note that Metasploitable and Metasploit are two different things entirely. The previous is a VM while the latter is a cyber offense tool (which may or may not be covered in a later article 😉).

VMs, much like any other computer, need to be as secure as possible. Metasploitable does the complete opposite. It comes out of the box with enough vulnerabilities to give the cybersecurity professionals at [CYSED](https://cysed.org) serious nightmares. The VM is a Linux-based system with various ports open, insecure configurations, and outdated software.

Now, let’s figure out how to install it securely on our systems.

## How to Set Up Metasploitable

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-40.png)
_The metasploitable interface ¦ Credit: Author_

Before we go further, you’re going to need a few things:

* An Internet Connection
* A Computer with at least 8 GB RAM and 20 GB free storage
* A flair to be an awesome geek

And with those boxes checked, let’s get started.

To download the VM, head over to Google and type in ‘Metasploitable download’. Click on the first link by [SourceForge](https://sourceforge.net/projects/metasploitable/), and hit download. The file is about 800 megabytes so feel free to pull up an episode of Scooby-Doo while that’s downloading.

You should have a zip file like this once that is done:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-41.png)
_The metasploitable zip file ¦ Credit: Author_

Right-click and hit ‘Extract All…’ to get the VM Disk. You should see some files like this:

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-42.png)
_The zip file contents ¦ Credit: Author_

We’re going to need VirtualBox to install our VM. You can quickly setup VirtualBox using this [tutorial](https://www.freecodecamp.org/news/what-is-a-virtual-machine-and-how-to-setup-a-vm-on-windows-linux-and-mac/) by [Beau Carnes](https://www.freecodecamp.org/news/author/beau/). To import Metasploitable, open VirtualBox and click on ‘New’. Set the following options:

Name: Metasploitable (or whatever you like)

Type: Linux

Version: Other Linux (64-bit)

You don't have to select an ISO image because the OS is already in the virtual hard disk which will be installed as we go along.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-43.png)
_Setting up the VM ¦ Credit: Author_

Click on ‘Next’, which should take you to the hardware section. As mentioned before, a VM is a simulation of the real system, which requires resources like RAM and a Processor. You can change the amount of RAM and logical processors your VM uses. 

Keep in mind that the more resources you allocate to the VM, the less resources you have for your system.

On that note, I would suggest leaving the default hardware settings.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-44.png)
_Deciding how much hardware we need ¦ Credit: Author_

Quick lesson: Your system likely only has 1 physical processor but can have as many as 8 or more logical processors. This is because of something called **hyperthreading**, where a computer basically converts it’s physical cores into multiple smaller virtual ones. Now back to the tutorial.

Click ‘Next’ and you’ll be directed to the ‘Virtual Hard disk’ section. Normally, you’d create a virtual hard disk for your VM but we already have one.

Click on ‘Use an Existing Virtual Hard Disk File’ and hit ‘Add’ at the top right.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-45.png)
_Selecting a Virtual hard disk ¦ Credit: Author_

This will open up File Explorer, where you will proceed to select the ‘Metasploitable.vmdk’ file. Once that is done, Metasploitable should appear under the ‘Not Attached’ list.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-46.png)
_Selecting the Metasploitable hard disk ¦ Credit: Author_

Select it, hit ‘Choose’ and click on ‘Next’. You will be led to a ‘Summary’ section which will give you information about the VM before it is finally setup.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-47.png)
_Putting in the final touches ¦ Credit: Author_

Let’s finish it up by literally hitting ‘Finish’ and you should get a screen like so.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-48.png)
_Metasploitable installed on VirtualBox ¦ Credit: Author_

Congratulations on setting up Metasploitable 🎉. Now you can build your cybersecurity skills without risking a trip to your local prison 😉.

The credentials for the machine are `msfadmin:msfadmin`. Feel free to boot up your Kali machine, ping the machines, and start hacking. Here, I’ll give you a hint: It starts with ‘nmap’ 👁️.

## A Quick Word on Vulnerable Machines

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-49.png)
_A network of sorts ¦ Credit: [AcatXIo](https://pixabay.com/users/acatxio-20233758/" rel="noopener noreferrer)_

Just like a real system, a virtual machine is vulnerable to real world attacks. Try not to leave Metasploitable up when not in use and definitely do not expose it to an untrusted network. 

By default, the VM is set to use NAT (Network Address Translation) which adds a layer of security by isolating it from the external network while providing it access to the internet.

However, this may not be a comprehensive solution. One common alternative is to change the network adapter settings to ‘Host-Only’, which shuts the VM off from the Internet but allows it to communicate with other VMs and the host.

If you’re wondering what the other options are, here is a quick summary for each:

* **NAT:** Shares host network, provides internet access to VM.
* **Bridged Adapter:** VM connects directly to the physical network.
* **Internal Network:** Isolated network for VMs on the same host.
* **Host-Only Adapter:** VMs communicate with host and among themselves.
* **Generic Driver:** Allows using custom, non-standard network drivers.
* **NAT Network:** Similar to NAT but allows defining network properties.
* **Cloud Network:** Experimental feature for cloud-based networking.
* **Not Attached:** No network connection for the virtual machine.

## Conclusion

And now, let’s summarize what you’ve learned in this tutorial:

1. What a Virtual Machine is and how it works
2. What Metasploitable is
3. How to install Metasploitable and any other VM
4. What different network adapters do in VirtualBox

Playing with Metasploitable is a great way to practice offensive cybersecurity skills and the defensive if you want to try and patch it up. [Vulnhub](https://www.vulnhub.com) is a great place to download more virtual machines if you want to move beyond Metasploitable.

You could also use platforms like [TryHackMe](https://tryhackme.com/) and [HackTheBox](https://www.hackthebox.com) which are gamified and make things more fun if you want something a little different.

Good luck and Happy Hacking 🙃

## Resources

1. [Learn more about Cybersecurity in Africa](https://cysed.org)
2. [The Metasploitable Exploitability Guide from Rapid7](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/)

## Acknowledgements

Thanks to [Anuoluwapo Victor](https://www.linkedin.com/in/a-n-u-o/), [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Favour Ojo](https://www.linkedin.com/in/favour-ojo-906883199/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), and my family for the inspiration, support and knowledge used to put this post together. You’re all amazing.

Cover image credit: [Google DeepMind](https://www.pexels.com/@googledeepmind/)

