---
title: How to get started with CentOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-05T16:13:42.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-centos-15eac7215c99
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bIzsWHmJ6nun5bayHe3LKg.png
tags:
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: servers
  slug: servers
- name: System administration
  slug: system-administration
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Krasimir Vatchinsky

  You can download CentOS versions here.

  CentOS or Community Enterprise OS is an open source distribution based on RHEL or
  Red Hat Enterprise Linux. This is available only if you’ve bought the support package.
  Moreover, all RHEL ...'
---

By Krasimir Vatchinsky

You can download CentOS versions [_here_](https://wiki.centos.org/Download)_._

CentOS or Community Enterprise OS is an open source distribution based on RHEL or Red Hat Enterprise Linux. This is available only if you’ve bought the support package. Moreover, all RHEL packages are fully compatible with CentOS, providing a robust, stable and easy to manage platform, ensuring the highest level of operational security for free.

CentOS is binary compatible with RHEL out of the box and is the preferred platform for server installations. One of the most valuable parts of CentOS is the long support cycle. While the release support cycles for Fedora, for example, last up to 13 months, CentOS releases provide support for up to 7 years. That makes it extremely dependable and reliable.

Furthermore, the CentOS community project is expanding their availability over a large array of platforms like Google, Amazon AWS and others. It’s also available in generic cloud-init enabled images.

To learn more about CentOS visit [the CentOS Project here](https://www.centos.org/).

#### Versions

![Image](https://cdn-media-1.freecodecamp.org/images/FexWtcAsU02omlWN2zMjEBD-S9O4KYaNDnv2)

#### Examples

Let’s go through some detailed instructions on getting CentOS 7 installation and basic set up going.

1. Download the latest [CentOS .ISO](https://www.centos.org/download/)
2. After downloading the last version of CentOS using the above links or using the official CentOS download page, burn it to a DVD or create a bootable USB stick using LiveUSB Creator called [Unetbootin](https://unetbootin.github.io/).
3. After you have created the installer bootable media, place your DVD/USB into your system appropriate drive, start the computer, select your bootable unit, and the first CentOS 7 prompt should appear. At the prompt choose Install CentOS 7 and press the [Enter] key.

![Image](https://cdn-media-1.freecodecamp.org/images/rk-uJQssZewGXgFP9sIRmUHGpHjUEIpz0ee2)

4. The system will start loading media installer and a Welcome screen should appear. Select your Installation Process Language — that will assist you through the entire installation procedure — and click on Continue.

![Image](https://cdn-media-1.freecodecamp.org/images/21CN30c3nOpSCAb9XSlWJncObEl5fyqAIQEr)

![Image](https://cdn-media-1.freecodecamp.org/images/IIAp4gYwhWdcRvg0KP8de6Y7ivhgiZJ4SXvH)

5. In the next step, the present screen prompt is Installation Summary. It contains a lot of options to fully customize your system. The first thing you may want to setup is your time settings. Click on Date & Time and select your server’s physical location from the provided map and hit the upper Done button to apply that configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/zPoewuybibFqlg79nqCcDjEtKE1lxAi8RqXj)

![Image](https://cdn-media-1.freecodecamp.org/images/udVF8vI0FuFqP8uFY-fXGeXIHcyVUYZcEmQg)

6. Next, choose your Language Support and Keyboard settings. Choose your main and extra language for your system, and when you’re finished, hit Done.

![Image](https://cdn-media-1.freecodecamp.org/images/GNUOD3cBf0HukL0AdEFSaslfAXDfihcOeJxt)

![Image](https://cdn-media-1.freecodecamp.org/images/0SOMnkOxnmkG4DSwnogamdTSlEOC45QFi23m)

7. In the same way, choose your Keyboard Layout by hitting the plus button and test your keyboard configuration using the right input filed. After you’ve finish setting up your keyboard, you can use any key combination for switching between keyboards. In my case I am using Alt+Ctrl. After selecting your desired key combination, press Done again to apply changes and go back to the main screen on Installation Summary.

![Image](https://cdn-media-1.freecodecamp.org/images/YI7FkWgL8h9QTXALMgCCvqxrKgZarWNFh5gn)

![Image](https://cdn-media-1.freecodecamp.org/images/r0NDr-cIq3UyaXoa0y3qgmE7EhiMLj8DZRS4)

![Image](https://cdn-media-1.freecodecamp.org/images/yPi-j4-sjLXe4ShqPpR-bnKWwY2wO-keP5mv)

![Image](https://cdn-media-1.freecodecamp.org/images/aXcgQKMdphnhNTLzTcWWWt7B-3bduQ3b4AXm)

8. Now we can add LANGUAGE SUPPORT if you don’t want to use English. Click on “LANGUAGE SUPPORT” to open the dialog.

![Image](https://cdn-media-1.freecodecamp.org/images/caxBvCvaLqNJYHbuqCEnWz4SlzHcnjJWbSHN)

9. By default, CentOS comes with the English language preinstalled, but we can add more languages easily. In my case, I am adding Deutsch German with Deutsch (Deutschland) as the additional language. Press Done after your selection.

![Image](https://cdn-media-1.freecodecamp.org/images/p69eRIErcsIn7g1AMpUQskZ2gCN2hnpzxAI5)

10. In the next step, you can customize your installation by using other Installation Sources than your local DVD/USB media, such as a network locations using HTTP, HTTPS, FTP or NFS protocols. You can even add some additional repositories, but use this method only if you know what you’re doing. So leave the default Auto-detected installation media and hit Done to continue.

![Image](https://cdn-media-1.freecodecamp.org/images/TOxIxWtUUaU6dck4gKzc2d5VPzbFaWbH7XP0)

![Image](https://cdn-media-1.freecodecamp.org/images/5SagBXBx6G402fzVKdcQgKJXJ3vRqFv9j3Rr)

11. Next you can choose your system installation software. In this step, CentOS offers a lot of Server and Desktop platform environments that you can choose from. But if you want a high degree of customization, especially if you are going to use CentOS 7 to run as a server platform, then I suggest Minimal Install with Compatibility Libraries as Addons. This will install a minimal basic system software and later you can add other packages as your needs require using:

![Image](https://cdn-media-1.freecodecamp.org/images/aiPGfy0I85i73SC5EYBucyDGslreAYyBUvai)

![Image](https://cdn-media-1.freecodecamp.org/images/9VBciZwESM-gjiXOUsLz-88I7H9fLs1GghwC)

![Image](https://cdn-media-1.freecodecamp.org/images/w4QVnApDtJTm1jcMIFnQ8z-Z7ZW68jdjXMxB)

12. Now it’s time to partition your hard-drive. Click on Installation Destination menu, select your disk, and choose the one you want. I will configure partitioning. Read more about what partition to choose [here](https://www.centos.org/docs/5/html/Installation_Guide-en-US/s1-diskpartitioning-x86.html).

![Image](https://cdn-media-1.freecodecamp.org/images/enMF4gpceUHqdwSWDhP6-n0Zvyb0122RP8NQ)

![Image](https://cdn-media-1.freecodecamp.org/images/7nKmF4m-peDAaJT-pJz7F4EvKAzW1fYbHIQX)

13. On the next screen, choose LVM (Logical Volume Manager) as partition layout and then click on Click here to create them automatically. This option will create three system partitions using XFS filesystem, automatically redistributing your hard-disk space and gathering all LVS into one big Volume Group named “centos”. 11.

* /boot — Non LVM
* /(root) — LVM
* Swap — LVM

![Image](https://cdn-media-1.freecodecamp.org/images/N-pKNTOCYDUvsQjB7N5O8H2JV02iw08ODO93)

![Image](https://cdn-media-1.freecodecamp.org/images/U7obhodVkpI38y4oV19VUrC4WU59fYo65s2H)

14. If you are not pleased with the default partition layout created automatically by the installer, you can completely add, modify, or resize your partition scheme. When you finish hit the Done button and Accept Changes on the Summary of Changes prompt.

![Image](https://cdn-media-1.freecodecamp.org/images/fyZ3sVKHOs8pN77NHqcRDfwpYpuyyF4xlzsJ)

NOTE: For those users who have hard-disks more than 2TB in size, the installer automatically will convert the partition table to GPT. But if you wish to use GPT table on smaller disks than 2TB, then you should use the argument inst.gpt to the installer boot command line in order to change the default behavior.

15. The next step is to set your system hostname and enable networking. Click on Network & Hostname label and type your system FQDN (Fully Qualified Domain Name) in the Hostname field, then enable your Network interface, switching the top Ethernet button to ON. If you have a functional DHCP server on your network, then it will automatically configure all your network settings for enabled NIC, which should appear under your active interface.

![Image](https://cdn-media-1.freecodecamp.org/images/aJaSFWrR0OhcclQfctFmPeShvAb4CrK-yJfO)

![Image](https://cdn-media-1.freecodecamp.org/images/6JGzTjzo0weuiVyPoGWOYzRRsh1Rl6C5GcHF)

16. If your system is a server, it’s better to set static network configuration on Ethernet NIC by clicking on the Configure button and adding all your static interface settings like in the screenshot below. When you’re finished, hit Save, disable and enable the Ethernet card by switching the button to OFF and ON, and then hit Done to apply the settings and go back to the main menu.

Otherwise:

![Image](https://cdn-media-1.freecodecamp.org/images/LSvNkE3Tc2i7Fa2q1DDT6YCtJ3C0WQpEam8G)

![Image](https://cdn-media-1.freecodecamp.org/images/j44d6AGcV6OTDbjZOMx8MY8eFGVt4c5QDYOp)

![Image](https://cdn-media-1.freecodecamp.org/images/xNSaSz1Fe3lQ9dZHBqTha5Y4kciBIxVDs7R2)

17. Add the entries for Address, Netmask and Gateway as per your static IP environment. In my case I am using the Address 192.168.1.100, Netmask 255.255.255.0, Gateway 192.168.1.1 and DNS servers 8.8.8.8 8.8.4.4. These values may vary according to your network environment. After that press Save.

IMPORTANT: If you do not have an IPv6 internet connection, then set IPv6 from auto to ignore on the IPv6 tab. Otherwise you won’t be able to reach the internet from this server on IPv4, as CentOS seems to ignore the correct IPv4 setup then and uses IPv6 instead which fails.

![Image](https://cdn-media-1.freecodecamp.org/images/zIVn34DFeRZBICltiKeJ6ZoLae4c2pN45Xdp)

18. Next, we have to turn the connection ON as shown in the screenshot below. After, press Done.

![Image](https://cdn-media-1.freecodecamp.org/images/ZnGNcnOiXpdvvpMya2dRhJ4CaOY8pSRYLnaJ)

19. Now it’s time to start the installation process by choosing Begin Installation and setting up a strong password for the root account.

![Image](https://cdn-media-1.freecodecamp.org/images/ea3kScov6z01BRxr4jOLM4NRJccCxUS3EDqN)

20. The installation process will start now and you will get a small blue progress bar in the next windows. Now we have to set the ROOT PASSWORD and add a new non-root user in the USER CREATION option. I will first go for root password.

![Image](https://cdn-media-1.freecodecamp.org/images/c5h9dW9aqyasoNX9aDwfInjkU5xnPGq4QAu2)

21. Enter a secure password of your choice and press Done.

![Image](https://cdn-media-1.freecodecamp.org/images/2Ky7QzNMLccBT5QPLSqGbav50VsK3cH4JmBI)

22. Next we will go for USER CREATION.

![Image](https://cdn-media-1.freecodecamp.org/images/GeveORGJo-scuJeD1Z25sxVDSeNNeAN7Npr-)

23. Next I will create a user. In my case I used the Full name “Administrator” and Username “administrator”. Check the option Require the password to use this account and then press Done. Of course you can use any value as per your choice.

![Image](https://cdn-media-1.freecodecamp.org/images/3sGgDLaj28eqO4yvWYHgANUkwZn-kXz10LmY)

24. Press Finish. Have patience and wait for the completion of the setup.

![Image](https://cdn-media-1.freecodecamp.org/images/n8Qxnk5BdvJRkM6sntmR62uC4eV8GiNK7dFk)

25. After completion of the installation, it will ask to reboot the server, just press Finish configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/rTWWi5rPGgTBBjTN8vI6uInYwTqD9nhcb2Yy)

26. The server reboots and will request your username and password afterwards.

![Image](https://cdn-media-1.freecodecamp.org/images/yQwZNdAYh2gDJ3cxbDzEiVFGQYnzz412Q3j8)

Congratulations! You have now installed last version of CentOS on your brand new machine. Remove any installation media and reboot your computer so you can login to your new minimal CentOS 7 environment and perform other system tasks, such as update you system and install other useful software needed to run day to day tasks.

Now we are ready to do login with the user that we just created above or we can use the root credentials.

First Login on CentOS. Login as root user to the server so we can do some final installation steps.

The first one is to install all available updates with yum.

![Image](https://cdn-media-1.freecodecamp.org/images/yjaMZ33oDpbtjB21GtAnE-yh3GHkhHuZsEOp)

Confirm with “y” to proceed with the installation of the updates. I will install two command line editors to be able to edit configuration files on the shell:

![Image](https://cdn-media-1.freecodecamp.org/images/eRLKdk7Ha3KRU3fgjZF847V9wIiHhxTpXqnO)

#### Network Configuration

CentOS 7.2 minimal don’t come pre-installed with the ifconfig command, so we will install it as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/slhBMQEUoqGJkgEDUQOW-3rxa3WZCA7PD-V3)

If you want to change or see the network configuration file, just edit the file:

![Image](https://cdn-media-1.freecodecamp.org/images/OliVYcSJvGNYWk9mDB5zqtMExcggQG5SqzbM)

It will be like this when you configured a static IP address:

![Image](https://cdn-media-1.freecodecamp.org/images/pofxOfE9lJnMwr4nIKs0AOyORp4k-r1eUMBI)

![Image](https://cdn-media-1.freecodecamp.org/images/CNjWloceJVc8vHVn9BaiqeZ5c1hEhoYw7WuN)

Change the values if required.

Note: The above DEVICE name may vary, so please check the equivalent file in the directory /etc/sysconfig/network-scripts.

#### Adjust /etc/hosts

Adjust the file /etc/hosts as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/9f52fds4U3nqAdcQtDp5tv98MDuQ6nm09m3q)

Make the values like this:

![Image](https://cdn-media-1.freecodecamp.org/images/4G8Ve0NTRP1Jx6fVcVNx6a7HGIGRiAVK02Hm)

Congratulations! Now we have basic minimal CentOS 7 server setup.

Now you may prefer to use GUI instead, here is a variety of flavors you could choose from:

#### Installing GNOME-Desktop:

Install GNOME Desktop Environment by entering the following:

![Image](https://cdn-media-1.freecodecamp.org/images/8xrxZk0240pPvx-yslBxJXZih9jrhfOPaksU)

To start the GUI, enter after finishing installation:

![Image](https://cdn-media-1.freecodecamp.org/images/cZPdsALzVpA5DYKoToQ2lgMG7FDBftKHJgGY)

![Image](https://cdn-media-1.freecodecamp.org/images/8O5W1tTbW4-caJbSU9qQxqIM5RaUfugFt6BJ)

#### How to use GNOME Shell

The default GNOME Desktop of CentOS 7 starts with classic mode, but if you’d like to use GNOME Shell, set it like this:

Option A: If you start GNOME with **startx**, set it like this:

![Image](https://cdn-media-1.freecodecamp.org/images/UGFEuBeOA5TeYZZlPE-E2iOZBJmXvjjrfFYn)

Option B: set the system graphical login systemctl set-default graphical.target and reboot the system. After the system starts:

1. Click the button which is located next to the “Sign In” button.
2. Select “GNOME” on the list. (The default is GNOME Classic)
3. Click “Sign In” and log in with GNOME Shell.

![Image](https://cdn-media-1.freecodecamp.org/images/N2icRiFgBxnYEXUUu8cHdfVTGPo-yGzHhlAU)

GNOME shell starts like this:

![Image](https://cdn-media-1.freecodecamp.org/images/oiqDsqZuANvGUG2XEpJU8M9LJbaEhfBTcrAV)

#### Installing KDE-Desktop:

Install KDE Desktop Environment by entering

![Image](https://cdn-media-1.freecodecamp.org/images/8EKvkfyxykrD7ESdx-NTZqLn1-XoAHUxqB0t)

Input a command like below after finishing the installation:

![Image](https://cdn-media-1.freecodecamp.org/images/BM7BB8s7TzICeeeYJyhw9H2XeBU5BmXcEAfb)

KDE Desktop Environment starts like this:

![Image](https://cdn-media-1.freecodecamp.org/images/vLim8XR1-vl7DP2Nzbk7GPe34X7PNLjx4KcR)

#### Installing MATE Desktop Environment:

Install MATE Desktop Environment by entering this:

![Image](https://cdn-media-1.freecodecamp.org/images/KQGWjK2f5QL-ESkHT71foneUyytOZgC76THw)

Input a command like below after finishing the installation:

![Image](https://cdn-media-1.freecodecamp.org/images/S-9RT00AC-D0EyVaqdsQMYbH9G1CMKf5imSZ)

MATE Desktop Environment starts:

![Image](https://cdn-media-1.freecodecamp.org/images/6bLYOa7ktDIkJ5-nJ7BK9mQifjizzOZK47ir)

#### Installing Xfce Desktop Environment:

Install Xfce Desktop Environment by entering this:

![Image](https://cdn-media-1.freecodecamp.org/images/eajRi-cVLawzVkihC8nTDZNGXKjdEISEnn6Y)

Input a command like below after finishing the installation:

![Image](https://cdn-media-1.freecodecamp.org/images/nvqLmB2PqwYamPW3KOfIRf4mIKvohyGzwbgv)

Xfce Desktop Environment starts like this:

![Image](https://cdn-media-1.freecodecamp.org/images/3916tM9oz0pGpYNGX5H1EfjvA93F4aSQ33qf)

#### OTHER WAY TO DO IT:

Rather than make use of the hacking of a startx command into a .xinitrc file, it’s probably better to tell Systemd that you want to boot into a graphical GUI vs. the terminal.

To accomplish this simply do the following:

![Image](https://cdn-media-1.freecodecamp.org/images/clCHZwiwW12IxLg8F-1eV8MMpwww250wx8Fn)

Then simply reboot.

The last bit will associate the runlevel 5 target as your default with respect to Systemd.

#### Doing it with Systemd

You can also use Systemd to accomplish this. This is arguably the better method, since you’re managing the state of the system directly through Systemd and its CLIs.

You can see what your current default target is:

![Image](https://cdn-media-1.freecodecamp.org/images/GAMQwC7zZTIyvWWjnOwCxOBII0f9ZJFo6NpV)

And then change it to graphical:

![Image](https://cdn-media-1.freecodecamp.org/images/MRK-LDaeKfDAPHrq1UiP3aG6USYtZYMp0c8Z)

![Image](https://cdn-media-1.freecodecamp.org/images/Q3WkBqFK0D7pAQCU0Kzure2BqDw5cSoA24tC)

#### Targets

In Systemd the targets runlevel5.target and graphical.target are identical. So too are runlevel2.target and multi-user.target.

![Image](https://cdn-media-1.freecodecamp.org/images/04fnoUaIaChUTVk1gI5bpdWueeHe9j6Z4AZx)

#### RHEL / CentOS Linux Install Core Development Tools Automake, Gcc (C/C++), Perl, Python & Debuggers

Q. How do I install all developer tools such as GNU GCC C/C++ compilers, make and others, after installing CentOS or RHEL or Fedora Linux from a shell prompt?

You need to install ‘Development Tools’ group on RHEL/CentOS/Fedora/Scientific/Red Hat Enterprise Linux. These tools include core development tools such as automake, gcc, perl, python, and debuggers which are required to compile software and build new rpms:

1. flex
2. gcc c/c++ compiler
3. redhat-rpm-config
4. strace
5. rpm-build
6. make
7. pkgconfig
8. gettext
9. automake
10. strace64
11. gdb
12. bison
13. libtool
14. autoconf
15. gcc-c++ compiler
16. binutils and all dependencies.

#### Installation:

Open the terminal or login over ssh session and type the following command as a root user:

![Image](https://cdn-media-1.freecodecamp.org/images/FBV3oXITAW4NDKmUlCSnqKRHkrpFxOsywEOa)

Sample outputs that follow:

![Image](https://cdn-media-1.freecodecamp.org/images/eJlL3KG2asfbT7-KjJODLskpBeLTsgNbcCRt)

Now you can compile and use any application on your system.

#### **Installation Verification**

To display Gnu gcc/c/c++ compiler version type:

![Image](https://cdn-media-1.freecodecamp.org/images/gCh9plzh1fFHqRAxIN41R2Z024dgm-3uUICK)

Sample outputs:

![Image](https://cdn-media-1.freecodecamp.org/images/f3COT3u-Xb8zvgnrNGVvH-7rpiPqZenBdivq)

#### How do I list all currently running services in Fedora / RHEL / CentOS Linux server?

There are various ways and tools to find and list all running services under Fedora / RHEL / CentOS Linux systems.

![Image](https://cdn-media-1.freecodecamp.org/images/sR1j7IEftLUJcf3l8eA09lFf4QuW31Na3dbE)

The syntax is as follows for CentOS/RHEL 6.x and older (pre systemd):

![Image](https://cdn-media-1.freecodecamp.org/images/34duN-gDwYU8Voox68o0OWpyO0lcROokMeN6)

Print the status of any service. To print the status of apache (httpd) service:

![Image](https://cdn-media-1.freecodecamp.org/images/hrg5zAjTRW789CRAM0kLPpoEdJi4VCqdf2re)

List all known services (configured via SysV):

![Image](https://cdn-media-1.freecodecamp.org/images/zdMHiLpBgWw-7wcHU4rtNePnTWydgPGwNVSY)

List services and their open ports:

![Image](https://cdn-media-1.freecodecamp.org/images/ONlXfdtpMuQThom-1TXCwogvZLW-CxvJsZSu)

Turn on / off service:

![Image](https://cdn-media-1.freecodecamp.org/images/9zwxQTHcBo1W4-bYkTdLRYkRqlxbgiwH30Fo)

**ntsysv** is a simple interface for configuring runlevel services which are also configurable through **chkconfig**. By default, it configures the current runlevel. Just type **ntsysv** and select the service you want to run.

#### A note about RHEL/CentOS 7.x with systemd

If you are using systemd based distro such as Fedora Linux v22/23/24 or RHEL/CentOS Linux 7.x+, try the following command to list running services using the systemctl command. It controls the systemd system and service manager.

To list systemd services on CentOS/RHEL 7.x+ use the following.

The syntax is:

![Image](https://cdn-media-1.freecodecamp.org/images/HMgfPY4TiCQZt5VqkAeVnOA6wzKA0tHb7fnM)

To list all services:

![Image](https://cdn-media-1.freecodecamp.org/images/4X-Q7tJMtViVrTXOg1118N4RQSxK8fIIsG8q)

Sample outputs:

![Image](https://cdn-media-1.freecodecamp.org/images/8HHdKMxQvr1tP9gfoT3K602qrD3FkQ-RpAU2)

The above image shows List all units installed on the CentOS /RHEL 7 systemd based system, along with their current states.

To view processes associated with a particular service (cgroup), you can use the systemd-cgtop command. Like the top command, systemd-cgtop lists running processes based on their services:

![Image](https://cdn-media-1.freecodecamp.org/images/cnQkMU558eEjH4IQ7NY546voU0Q079Aj5iOp)

Sample outputs:

![Image](https://cdn-media-1.freecodecamp.org/images/vOiJ6B9pCEt3sT5CrOGbkiIGf5UoSdQ7xv42)

To list SysV services only on CentOS/RHEL 7.x+ use (does not include native systemd services):

![Image](https://cdn-media-1.freecodecamp.org/images/C6mSxcdwt6RdEjfLwbP0XmdjJBv7UrKEjr33)

Sample outputs:

![Image](https://cdn-media-1.freecodecamp.org/images/psYt44SaI963eoYVsBCFSCEFGyERv4H3V2nC)

#### FIREWALL HOW TO:

Learn how to set up the firewall [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-oncentos-7).

**References**

* [CentOS Documentation](https://wiki.centos.org/Documentation)
* [CentOS Release Notes](https://wiki.centos.org/Manuals/ReleaseNotes/CentOS7)
* [Install Gnome GUI on CentOS 7 / RHEL 7](https://linuxconfig.org/how-to-install-gui-gnome-on-centos-7-linux-system)
* [Working with SYSTEMD Targets](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-managing_services_with_systemd-targets)

**Documentation How To guide for CentOS**

[CentOS version 7](https://docs.centos.org/en-US/docs/)

CentOS 7 is fully based on RedHat’s detailed documentation. Examples and system administration guides are located here: [CentOS 7 full documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/)

[_Originally published by Krasimir Vatchinsky in Archived Stack Overflow Documentation — RIP Tutorial_](https://riptutorial.com/centos/topic/7640/getting-started-with-centos)

