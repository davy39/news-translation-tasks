---
title: How to Format a USB Drive to FAT32 on Windows 10
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-10-16T06:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-format-a-usb-drive-to-fat32-on-windows-10
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa4f2e749c47664ed81ae62.jpg
tags:
- name: storage
  slug: storage
- name: usb
  slug: usb
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'If you need to format a USB flash drive, HDD, SDD, or some other form of
  storage to FAT32, you''ve come to the right place.

  In this article we''ll go over what a file system is, the FAT32 standard, and several
  ways to format a storage device to FAT32 o...'
---

If you need to format a USB flash drive, HDD, SDD, or some other form of storage to FAT32, you've come to the right place.

In this article we'll go over what a file system is, the FAT32 standard, and several ways to format a storage device to FAT32 on Windows 10.

## What's a file system?

A file system is a standardized way of organizing data on a computer storage device like a flash drive or HDD. 

A file system divides a storage device into virtual compartments, almost like a wall of post office boxes, and keeps track of all the information that gets stored in each box.

Some of the most common file system formats for portable storage devices are FAT32, NTFS, and ExFAT.

## FAT32 compared to other formats

Of those three common formats, FAT32 is the oldest and most widely supported. Every major operating system will allow you to read and write from a USB flash drive that's formatted to FAT32.

Meanwhile, macOS can only read NTFS drives, and you would need to install third-party software to write back to the drive.

However, though FAT32 is well supported, its maximum drive and file size is severely limited when compared to newer formats like NTFS and ExFAT:

|  | Max drive size | Max file size | Windows | macOS | Linux |
| --- | --- | --- | --- | --- | --- | 
| FAT32 | 32 GB (Windows), up to 16TB (Other OSs) | 4 GB | Read/Write |  Read/Write |  Read/Write |
| NTFS | 8 PB* | 16 EB** | Read/Write |  Read |  Read/Write |
| ExFAT | 128 PB* | 16 EB** |  Read/Write |  Read/Write |  Read/Write |
\* 1 petabyte is about 1 thousand terabytes
\*\* 1 exabyte is about 1 million terabytes

Note that the maximum drive and file size of NTFS and ExFAT is so large that there's basically no limit. (But it would be nice to have a 128 PB USB drive, wouldn't it?)

On the other hand, FAT32's max file size of 4 GB is almost nothing now that phones can record 4K videos. Also, it's a little more difficult to format a drive larger than 32 GB to FAT32 on Windows 10.

These days, the only reason why you'd choose to format a drive to FAT32 is for compatibility. For example, if you need to boot up an old computer, maybe with a different operating system, and backup some of its files. But you'd need to be sure that none of those files are greater than 4 GB.

If you're sure you want to go with FAT32, here's how to format a storage drive on Windows 10.

**Important note:** Before you format a drive, make sure that you backup all of your important files. In fact, make two backups, and keep one on a remote service like Google Drive or Dropbox.

Formatting a drive will delete all of the data that's currently on it.

## How to use Windows File Explorer to format a USB drive to FAT32

A quick note about this method: it only works on USB flash drives that are less that 32 GB. If your USB drive is larger than 32 GB, check out one of the later methods.

With that out of the way, plug your USB drive into your computer and open Windows File Explorer.

Next, right-click on the drive on the left hand side of the File Explorer window and click "Format":

![Selecting the "Format" option in Windows File Explorer ](https://www.freecodecamp.org/news/content/images/2020/11/windows-file-explorer-format.jpg)

In the window that pops up, ensure that "FAT32" is selected. Also, feel free to rename the USB drive whatever you'd like:

![The Windows Format popup window](https://www.freecodecamp.org/news/content/images/2020/11/windows-format-window.jpg)

You can leave the rest of the options alone. Just click start to format your drive.

Once it's done, your USB drive should be formatted to use the FAT32 file system.

To double check this, open File Explorer, right click on your USB drive, and click "Properties".

A window will pop up and you should see that the file system is now FAT32:

![An open drive properties window to double check the format](https://www.freecodecamp.org/news/content/images/2020/11/drive-properties.jpg)

## How to use Rufus to format a USB drive to FAT32

If your USB drive is larger than 32 GB, you'll need to use a third-party program like [Rufus](https://rufus.ie/) to format it. 

There are lots of other programs that can format USB drives, but Rufus is really small and portable. This means you can stick Rufus right on a USB drive, plug it into any Windows computer, and format other drives on the go.

After you download Rufus, double click on the `.exe` file to start the application.

Make sure your USB drive is selected. Then, click the "Boot selection" dropdown and select "Non bootable":

![Selecting the "Non bootable" option in Rufus](https://www.freecodecamp.org/news/content/images/2020/11/rufus-boot-selection.jpg)

Next, click the "File system" dropdown and select "FAT32".

Also, feel free to change the name of your USB drive under "Volume label":

![Selecting the file system and changing the volume label in Rufus](https://www.freecodecamp.org/news/content/images/2020/11/rufus-file-system-and-volume-label.jpg)

Then, click the "Start" button to format your drive. After a few seconds it'll be formatted to FAT32.

## How to use PowerShell to format a USB drive to FAT32

While this method works with drives larger than 32 GB, it's really slow – even formatting a 32 GB drive can take up to an hour depending on your computer.

But, if you aren't able to use the previous two methods for some reason, this will work in a pinch.

First, click on the Windows Search Bar and type in "powershell". Then, click "Run as administrator" to launch PowerShell with elevated privileges:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/powershell-as-administrator.jpg)

In the PowerShell terminal, enter the following command:

`format /FS:FAT32 DRIVE_LETTER:`

Use the File Explorer to double check your drive letter. My drive letter was D, so I entered `format /FS:FAT32 D:`.

Press Enter, make sure your USB drive is plugged in, and press the Enter key again to start the process:

![Using PowerShell to run the format command](https://www.freecodecamp.org/news/content/images/2020/11/image-33.png)

Then go run some errands or something – it will take awhile.

Once the `format` command is finished, your drive should be formatted to FAT32.

## In closing

Now you should be able to format a USB drive of any size to FAT32 on Windows 10. And with just a little modification, any of these methods can be used to format your drive to another file system like NTFS or ExFAT.

Now get out there and format all your USB drives. (But only after you backup everything important!)

Was this helpful? Is there a better method that you know of? [Tweet](https://twitter.com/kriskoishigawa) at me and let me know how you format things on Windows 10.

