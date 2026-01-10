---
title: How to Make a Windows 10 USB Using Your Mac - Build a Bootable ISO From Your
  Mac's Terminal
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2019-09-25T17:07:13.000Z'
originalURL: https://freecodecamp.org/news/how-make-a-windows-10-usb-using-your-mac-build-a-bootable-iso-from-your-macs-terminal
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca043740569d1a4ca4791.jpg
tags:
- name: mac
  slug: mac
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'Most new PCs don''t come with DVD drives anymore. So it can be a pain to
  install Windows on a new computer.

  Luckily, Microsoft makes a tool that you can use to install Windows from a USB storage
  drive (or "thumbdrive" as they are often called).

  But wh...'
---

Most new PCs don't come with DVD drives anymore. So it can be a pain to install Windows on a new computer.

Luckily, Microsoft makes a tool that you can use to install Windows from a USB storage drive (or "thumbdrive" as they are often called).

But what if you don't have a second PC for setting up that USB storage drive in the first place?

In this tutorial we'll show you how you can set this up from a Mac.

# Step 1: Download the Windows 10 ISO file

You can download the ISO file straight from Microsoft. That's right - everything we're going to do here is 100% legal and sanctioned by Microsoft.

You can download Windows 10 directly from Microsoft for free using [this link](https://www.microsoft.com/en-us/software-download/windows10). If you visit the link using a Windows device, you'll be redirected to the [Windows Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows10%20) like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-106.png)

If you visit the same link from a non-Windows device, such as a Mac or a Linux device or any smartphone, you'll land on the official ISO download page:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-28-at-23-44-48-Download-Windows-10-Disc-Image--ISO-File--2.png)

Select your desired edition from that drop-down and hit _Confirm_.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-28-at-23-44-48-Download-Windows-10-Disc-Image--ISO-File--1.png)

At this time, Windows 10 (multi-edition ISO) was the only one available. Once you've confirmed your edition, you'll get another drop-down that lets you pick a language. Pick the one you want and hit the _Confirm_ button.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-28-at-23-47-47-Download-Windows-10-Disc-Image--ISO-File--1.png)

Once you've confirmed your language, you'll get two download links, one for the 64-bit edition, and the other one for the 32-bit edition. Both links are valid for 24 hours and the page will also show when they expire.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot-2022-02-28-at-23-48-22-Download-Windows-10-Disc-Image--ISO-File--1.png)

If you don't know how to decide between 64-bit and 32-bit, here's what you should do. If you have a processor that supports 64-bit architecture and you have more than 4GB of RAM, go with the 64-bit one. 32-bit operating systems have a 4GB RAM limit.

To figure out whether your processor supports 64-bit architecture or not, head over to a website like [WikiChip](https://en.wikichip.org/wiki/WikiChip), and search for your processor model.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/image-107.png)

As you can see in the screenshot above, my Ryzen 5 3600 supports 64-bit architecture. I also have 16GB of RAM which is a lot more than 4GB, so I'll go for the 64-bit edition.

# Step 2: Insert your USB storage drive into your Mac

The ISO file is only about 5 gigabytes, but I recommend you use a USB drive with at least 16 gigabytes of space just in case Windows needs more space during the installation process.

I bought a 32 gigabyte USB drive at Walmart for only $3, so this shouldn't be very expensive.

Stick your USB drive into your Mac. Then open your terminal. You can do this using MacOS Spotlight by pressing both the ⌘ and Space bar at the same time, then typing "terminal" and hitting enter.

Don't be intimidated by the command line interface. I'm going to tell you exactly which commands to enter.

# Step 3: Use the diskutil command to identify which disk your USB drive is mounted on

Open Mac Spotlight using the ⌘ + space keyboard shortcut. Then type the word "terminal" and select Terminal from the dropdown list.

Paste the following command into your terminal and hit enter:

`diskutil list`

You will see output like this (note - your Mac's terminal may be black text on a white background if you haven't customized it).

![Image](https://www.freecodecamp.org/news/content/images/2019/09/default_-_default_freeCodeCamp_-_-zsh_-_130-33.png)

Copy the text I point to here. It will probably be something like

`/dev/disk2`.

# Step 4: Format your USB Drive to work with Windows

Next format your USB drive to Windows FAT32 format. This is a format that Windows 10 will recognize.

Note that you should replace the `disk2` with the name of the your drive from step 3 if it wasn't `disk2`. (It may be `disk3` or `disk4`). 

Run this command using the correct disk number for your USB:

`diskutil eraseDisk MS-DOS "WIN10" GPT /dev/disk2`

Then you'll see terminal output like this.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/default_-_default_freeCodeCamp_-_-zsh_-_130-33-1.png)

This will probably only take about 20 seconds on a newer computer, but may take longer on an older computer.

Note that for some hardware, you may instead need to run this command, which uses the MBR format for partitioning instead of GPT. Come back and try this command if step 7 fails, then redo steps 5, 6, and 7:

```
diskutil eraseDisk MS-DOS "WIN10" MBR /dev/disk2
```

# Step 5: Use `hdiutil` to mount the Windows 10 folder and prepare it for transfer.

Now we're going to prep our downloaded ISO file so we can copy it over to our USB drive.

You will need to check where your downloaded Windows 10 ISO file is and use that. But your file is probably located in your `~/Downloads` folder with a name of `Win10_1903_V1_English_x64.iso`.

`hdiutil mount ~/Downloads/Win10_1903_V1_English_x64.iso`

# Step 6: Copy the Windows 10 ISO over to your USB Drive

**Update April 2020:** One of the files in the Windows 10 ISO – install.wim – is now too large to copy over to a FAT-32 formatted USB drive. So I'll show you how to copy it over separately.

Thank you to [@alexlubbock](https://twitter.com/alexlubbock) for coming up with this workaround.

First run this command to copy over everything but that file:

`rsync -vha --exclude=sources/install.wim /Volumes/CCCOMA_X64FRE_EN-US_DV9/* /Volumes/WIN10`

Then run this command to install Homebrew (if you don't have it installed on your Mac yet):

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Then use Homebrew to install a tool called wimlib with this terminal command:

`brew install wimlib`

Then go ahead and create the directory that you're going to write the files into:

`mkdir /Volumes/WIN10/sources`

Then run this command. Note that this process may take several hours, you may see 0% progress until it finishes. Don't abort it. It will use wimlib to split the install.wim file into 2 files less than 4 GB each (I use 3.8 GB in the following command), then copy them over to your USB:

`wimlib-imagex split /Volumes/CCCOMA_X64FRE_EN-US_DV9/sources/install.wim /Volumes/WIN10/sources/install.swm 3800`

Once that's done, you can eject your USB from your Mac inside Finder. Note that Windows will automatically rejoin these files later when you're installing.

# Step 7: Put your USB into your new PC and start loading Windows

Congratulations - your computer now should boot directly from your USB drive. If it doesn't, you may need to check your new PC's BIOS and change the boot order to boot from your USB drive.

Windows will pop up a screen and start the installation process. 

Enjoy your new PC, and your newly-installed copy of Windows.

