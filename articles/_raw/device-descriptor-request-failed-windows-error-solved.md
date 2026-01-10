---
title: Device Descriptor Request Failed – How to Fix Unknown USB Device Error in Windows
  10
subtitle: ''
author: Gavin Lon
co_authors: []
series: null
date: '2022-10-28T23:49:33.000Z'
originalURL: https://freecodecamp.org/news/device-descriptor-request-failed-windows-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Screenshot1.jpg
tags:
- name: error
  slug: error
- name: usb
  slug: usb
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: "Recently my uncle, who lives in Australia, sent my parents, who live in\
  \ South Africa, a flash drive that was full of pictures of our Australian family\
  \ getting up to various Australian activities. \nBut it was very frustrating for\
  \ my poor Mom when her ..."
---

Recently my uncle, who lives in Australia, sent my parents, who live in South Africa, a flash drive that was full of pictures of our Australian family getting up to various Australian activities. 

But it was very frustrating for my poor Mom when her laptop would not recognise the USB device (the flash drive containing the Australian family pictures). 

I have the _privilege_ of being the goto family member when anything goes wrong with something computer related, because I am a computer programmer. This means I must know everything about USB ports, printers, scanners, basically all things computer related….right? 

Well, at the time, I must confess I didn’t have a clue why Windows 10 could not recognise the flash drive. So I did a bit of research. In this particular case the external device (the flash drive) was the offending party. 

It turns out, however, that this “Device Descriptor Request Failed“ issue can occur for many different reasons, some hardware related and others software related. 

In this article I'll cover the possible hardware-related issues first, and then we'll get into the possible software-related issues. With each cause of the “Device Descriptor Request Failed“ error, I’ll take you through the steps you'll need to follow to resolve the issue.

## Possible Causes and Fixes for "Device Descriptor Request Failed" Error

The following seven headings list out what may have caused the “Device Descriptor Request Failed“ issue. In the subsequent sections of this article, I'll give you details on how you might be able to resolve the issue.

* **USB Hardware Fault**
* **Run Hardware and Device Troubleshooter**
* **Update USB Device Driver**
* **Disable Fast Startup**
* **Disable the USB Selective Suspend Setting**
* **Remove USB Device and Scan for Hardware Changes**
* **Update Windows 10**

## USB Hardware Fault

The “Device Descriptor Request Failed” issue may have been caused by a hardware issue. We can easily test that the issue stems from a hardware issue and not an operating system related issue by performing the following checks:

First, plug the relevant device into a different USB port on the same computer. For good measure try a few USB ports. If the relevant device is working when plugged into another USB port, this means that the source of the issue is likely the USB port used when the issue arrises. 

In this case you can simply mark the USB port causing the issue as faulty, and use the USB port that works. You also may wish to replace the offending USB port at some stage.

Second, you can plug the relevant device into a USB port on a different computer. If the device doesn’t work on a different computer, this points to the device itself being the issue. Your only solution in this case may be to repair or replace the device itself.

## Run Hardware and Devices Troubleshooter

Windows provides us with a very convenient facility that you can use for performing troubleshooting. You are able to use this facility to trouble shoot possible hardware issues. 

Follow these steps to use the **Troubleshooter** facility:

* Firstly invoke the “Run” box. You can do this by pressing Windows key + R.
* Enter the following command into the “Run” box: **msdt.exe -id DeviceDiagnostic**

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-235.png)

* Press the **OK** button.
* Select Advanced – and make sure that the “Apply repairs automatically” checkbox is checked. Press the “Next” button and follow the instructions to preform the troubleshooting task.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-236.png)

## Uninstall and Update USB Device Driver

To uninstall the USB device driver we can use the **Device Manager** facility provided by windows. To run **Device Manager**, follow these steps:

* First, invoke the “Run” box. One way to do this is to press **Windows key + R**.
* Enter the following command into the “Run” box: **devmgmt.msc**. Then press the **OK** button.
* Within the tree structure presented in the **Device Manager** dialog box, expand the **Universal Serial Bus controllers** node**.**
* From the expanded list of nodes, select the node marked “Unknown USB Device (Device Descriptor Request Failed)”
* Right click this node and select **Uninstall device** from the context menu presented to you.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-237.png)

* Once the uninstall operation has completed, reboot your computer. This will result in the driver being reinstalled which may also result in your issue being fixed.

## Disable Fast Startup

One possible cause of the “Device Descriptor Request Failed” issue could be from a feature in Windows designed to speed up the boot process of your computer. Sometimes, this “Fast Startup" feature can keep your Operating System from detecting USB devices. 

Luckily we have the ability to turn this feature off. The “Fast Startup” feature is a “nice to have” feature and is it is recommended to have this feather turned on, but it is not an essential feature. 

So to turn off the feature, follow these steps:

* Press Windows Key + R to invoke the “Run” box.
* In the “Run” box type “control” and click the “OK” button to open Control Panel
* In the search box of your Control Panel type “Power options” and then click “Change what the power buttons do”
* Under the heading, “Define power buttons and turn on password protection”, click the link labelled, “Change settings that are currently unavailable”
* Make sure that the “Turn on fast startup (recommended)” checkbox is unchecked. Click the “Save changes” button

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-238.png)

* Restart your computer and see if this possible solution has fixed your USB device issue.

## Disable the USB Selective Suspend Setting

Sometimes the USB port is put into low-power mode when the “USB selective suspend” setting is enabled. This can cause abnormal behaviour when connecting a device to a USB port, which can result in the “Device Descriptor Request Failed” issue occurring. 

We are able to safely disable this feature, and by doing so potentially solve the “Device Descriptor Request Failed” issue. 

To disable the “USB selective suspend” setting, follow these steps.

* Press Windows Key + R to invoke the “Run” box.
* In the “Run” box, type “control” and click the “OK” button to open Control Panel
* In your Control Panel find and click “Power Options”
* Click the “Change plan settings” link
* Click the “Change advanced power settings” link
* Find and expand the “USB settings” node in the tree structure found on the "Advanced settings" tab.
* Expand the “USB selective suspend setting” child node.
* Make sure that “Disabled” is selected in the relevant dropdown list for both ”On battery” and “Plugged in”.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-239.png)

* Click the “Ok” button
* Reboot your computer
* Once your computer has been rebooted, test to see if the “Device Descriptor Request Failed” issue has been resolved.

## Remove USB Device and Scan for Hardware Changes

* Launch **Device Manager** by pressing Windows Key + R to launch the “Run” box, then type  **devmgmt.msc** in the "Run" box and press the “OK” button.
* Unplug the problematic device from the relevant USB port.
* From within the **Device Manager** dialog, click the “Scan for hardware changes” button on the toolbar. You can identify the relevant button by hovering your mouse pointer over the button whereby its tooltip text will display the text “Scan for hardware changes”.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-240.png)

* When the system recognises hardware changes, plug in the relevant USB device and test whether the problem has been fixed

## Update Windows

Installing the latest update for Windows may fix the “Device Descriptor Request Failed” issue. To install the latest windows update you can follow these steps:

* Open the Settings App by pressing Windows key + I
* Click the "Update & Security" option
* Select the “Windows Update” option
* Click the “Check for updates” button

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-241.png)

* Restart Computer and test to see if the “Device Descriptor Request Failed” issue still occurs (change)

## Conclusion

The “Device Descriptor Request Failed” issue can cause a lot of frustration and even heart ache in my poor mother's case where it prevented her from viewing family photos. 

Don’t despair – hopefully this article provides you with an effective remedy for the issue.

