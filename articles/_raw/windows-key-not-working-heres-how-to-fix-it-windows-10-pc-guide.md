---
title: Windows Key Not Working? Here's How to Fix It [Windows 10 PC Guide]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-11-05T17:29:22.000Z'
originalURL: https://freecodecamp.org/news/windows-key-not-working-heres-how-to-fix-it-windows-10-pc-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/photo-1530133532239-eda6f53fcf0f.jpeg
tags:
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: "On your Windows machine, the Windows key launches the Start menu, and from\
  \ there you can access anything on your computer. \nWhen you press it in combination\
  \ with other keys, it also acts as a useful shortcut to utilities you don't get\
  \ easily through ..."
---

On your Windows machine, the Windows key launches the Start menu, and from there you can access anything on your computer. 

When you press it in combination with other keys, it also acts as a useful shortcut to utilities you don't get easily through your computer's graphic user interface (GUI).

But what if you discover that your Windows key isn't working when you press it? This could be caused by several issues such as hardware, drivers, game mode, mechanical damage, and several other reasons.

If you have this issue, you've come to the right place. Because in this detailed guide, I will show you several ways to fix a Windows key that stops working.

## How to Fix Your Windows Key by Turning Off Game Mode

Windows 10 is optimized for games with game mode, but this can sometimes cause keyboard malfunctions and some keys might stop working. So, disabling game mode can make your Windows key work again.

### How to disable game mode:

**Step 1**: Click on Start to launch the start menu, then the gear icon to open up settings.
![ss-1-4](https://www.freecodecamp.org/news/content/images/2021/11/ss-1-4.jpg)

**Step 2**: Within the menu options, select "Gaming".
![ss-2-4](https://www.freecodecamp.org/news/content/images/2021/11/ss-2-4.jpg)

**Step 3**: Click on the game mode tab and make sure Game mode is toggled off.
![ss-3-4](https://www.freecodecamp.org/news/content/images/2021/11/ss-3-4.jpg)

Some Logitech keyboards have keys for turning on and off game mode. 
![gamemode](https://www.freecodecamp.org/news/content/images/2021/11/gamemode.png)

This does not optimize your computer for games but it disables some keys not used for playing games, such as the Windows key.

If you use one of these keyboards, make sure game mode is turned off right on it.

## How to Fix Your Windows Key by Turning off the Windows Lock Key

Just like Caps lock and Num lock, some keyboards have a Windows lock key which toggles the Windows key on and off. 

If your Windows key is not working, check your keyboard for this key and make sure it is not turned on.

If you are not sure whether your keyboard has the Windows lock key or not, search Google for your keyboard model.
 
## How to Fix your Windows Key by Turning off Filter Keys 

Filter keys are a Windows 10 accessibility feature that ignores multiple key presses. This might be interfering with your keyboard's Windows key, so turning it off might fix the issue.

To turn off filter keys, follow the steps below:

**Step 1**: Launch the Control Panel by clicking on start and searching for "control panel". Then press `ENTER` or click the first search result.
![ss-4-4](https://www.freecodecamp.org/news/content/images/2021/11/ss-4-4.jpg)

**Step 2**: Click on Ease of Access.
![ss-5-4](https://www.freecodecamp.org/news/content/images/2021/11/ss-5-4.jpg)

**Step 3**: Click on the link that says "Change how your keyboard works".
![ss-6-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-6-3.jpg)

**Step 4**: Uncheck the "Turn off filter keys" checkbox.

**Step 5**: Click “Apply”, then “Ok”.
![ss-7](https://www.freecodecamp.org/news/content/images/2021/11/ss-7.jpg)

## How to Fix your Windows Key by Turning off Sticky Keys

Sticky Keys are another Windows 10 accessibility feature that helps people who can't press multiple keyboard keys efficiently use their keyboards. 

This feature might interfere with the Windows key too, so turning it off could solve the issue of your Windows key not working.

**Step 1**: Click on Start and search for "control panel", then choose "Control Panel". 
![ss-4-5](https://www.freecodecamp.org/news/content/images/2021/11/ss-4-5.jpg)

**Step 2**: Select Ease of Access.
![ss-5-4](https://www.freecodecamp.org/news/content/images/2021/11/ss-5-4.jpg)

**Step 3**: Click on the "Change how your keyboard works" link.
![ss-6-3](https://www.freecodecamp.org/news/content/images/2021/11/ss-6-3.jpg)

**Step 4**: Uncheck "Turn on Sticky Keys".

**Step 5**: Make sure the “Apply” button turns off by clicking it, then click “Ok”.
![ss-8-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-8-1.jpg)

## How to Fix your Windows Key by Updating Keyboard Drivers

If your computer has an outdated or corrupt driver, this could cause your keyboard's Windows key to not work. So updating the driver, or uninstalling and reinstalling it, could end up fixing the issue.

**Step 1**: Click on Start on your desktop, search for "device manager", then click on the first [and possibly the only] search result.
![ss-9](https://www.freecodecamp.org/news/content/images/2021/11/ss-9.jpg)

**Step 2**: Expand the keyboard section.
![ss-10-1](https://www.freecodecamp.org/news/content/images/2021/11/ss-10-1.jpg)

**Step 3**: Right-click on the keyboard you're using and click on "Update driver".
![ss-12](https://www.freecodecamp.org/news/content/images/2021/11/ss-12.jpg)

**Step 4**: Choose "Search automatically for drivers". Your computer will now search online for driver updates and install them.
![ss-13](https://www.freecodecamp.org/news/content/images/2021/11/ss-13.jpg)

## How to Fix your Windows Key by Performing an SFC Scan in the Command Line

You can use the system file scan to fix a lot of issues on your Windows 10 computer, including a keyboard issue like the Windows key not working.

**Step 1**: Click on Start (Windows logo) on your desktop and search for "cmd".

**Step 2**: Don’t just select the "Command Prompt" search result, click on “Run as administrator” on the right.
![ss-14](https://www.freecodecamp.org/news/content/images/2021/11/ss-14.jpg)

**Step 3**: Paste in this command `sfc /scannow `, then hit `ENTER`.   
![ss-15](https://www.freecodecamp.org/news/content/images/2021/11/ss-15.png)

**Step 4**: The scan might take a while. Wait for it to complete, then restart your computer.
![ss-16](https://www.freecodecamp.org/news/content/images/2021/11/ss-16.png)

## How to Fix your Windows Key Using a PowerShell Command

Just like the Command Prompt, PowerShell is a command-line app that lets you run scripts and commands which directly communicate with your computer. 

**Step 1**: Click on Start and search for "powershell". Then hit `ENTER` to open up the first search result, which should be Windows PowerShell.
![ss-17](https://www.freecodecamp.org/news/content/images/2021/11/ss-17.jpg)

**Step 2**: Paste the following command to the PowerShell and hit `ENTER`: `Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation) AppXManifest.xml"}`

![ss-18](https://www.freecodecamp.org/news/content/images/2021/11/ss-18.png)

Don't bother about the errors. It does the job.

**Step 3**: Restart your computer.

## Conclusion

This article took you through several ways you can fix your Windows key when it's not opening up the Start menu or executing your desired shortcuts.

If one of these fixes fails to work, you have several other options to try out. 

Just be careful with the fixes that have to do with the command line. The commands directly interfere with your computer's OS, and so they could have a lasting effect on your computer.

I hope this article helps you fix a Windows key that's not working. If you find the article helpful, make sure you share it with your friends and family.

Thank you for reading.





