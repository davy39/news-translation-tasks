---
title: Windows 10 Start Menu Not Working (Solved)
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-11-06T17:07:32.000Z'
originalURL: https://freecodecamp.org/news/windows-10-start-menu-not-working-solved
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa1226549c47664ed819287.jpg
tags:
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'Windows 10 has come a long way since it was first launched in 2015. Each
  update brings a lot of new features, and Microsoft has embraced the open source
  community in a way that was once thought impossible.

  Still, like with any operating system, there...'
---

Windows 10 has come a long way since it was first launched in 2015. Each update brings a lot of new features, and Microsoft has embraced the open source community in a way that was once thought impossible.

Still, like with any operating system, there are bugs. And one of the more common bugs people running Windows 10 have faced is that the Start Menu suddenly stops working. 

Sometimes the open Start Menu freezes up and is unresponsive, and other times it won’t open at all when you click the Start Menu button.

Whatever specific issue you’re having with the Windows 10 Start Menu, we’ll go over some quick and not so quick fixes in this article.

## How to restart Windows Explorer

Windows Explorer, which is now called File Explorer, is the application you use to browse your file system and open programs and files. But it also controls things like the Start Menu, the taskbar, and other applications.

If you have an issue with the Start Menu, the first thing you can try to do is restart the “Windows Explorer” process in the Task Manager.

To open the Task Manager, press **Ctrl + Alt + Delete**, then click the “Task Manager” button.

Click “More details” to see a full list of open programs and background processes you’re running:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/task-manager-more-details.jpg)

Scroll through the list until you find the “Windows Explorer” process. Then right click on “Windows Explorer” and select “Restart”:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/task-manager-restart-windows-explorer.jpg)

There will be a brief flash while Windows restarts Windows Explorer/Finder, along with the taskbar and Start Menu.

After that, try to open the Start Menu. If it’s still not working normally, try one of the other fixes below.

## How to repair corrupt or missing Windows system files

Sometimes an update goes awry, or you accidentally deleted an important file while digging around the filesystem.

If the Start Menu is still giving you trouble, or other core Windows apps are crashing, then you can try to restore any missing or corrupt Windows system files.

To do this, you'll need to [open the Windows Command Prompt as an administrator](https://www.freecodecamp.org/news/how-to-open-the-command-prompt-in-windows-10/#how-to-open-command-prompt-as-an-administrator) and run the System File Checker program. 

Once you open Command Prompt as an administrator, run the command `sfc /scannow`:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/sfc-scannow.jpg)

System File Checker will start going through all your system files and replace any corrupt or missing files with a cached copy. 

This process can take a little while, so feel free to do something else for 5-10 minutes. Just be careful not to close the window while `sfc` is doing its thing.

Once System File Checker is finished, you'll either see a report of all the files it replaced, or if everything was fine, you'll see a message like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/sfc-scan-complete.jpg)

If System File Checker replaced any corrupt or missing system files, save all of your open work and restart your computer. Once you log back in, try to open the Start Menu to see if that fixed your issues.

**Note:** You could also use Powershell to run the `sfc /scannow` command, but remember that you'll need to open an elevated Powershell terminal.

## How to reset the Start Menu with default Windows 10 apps

The next thing you can try is to reset the Start Menu entirely, along will all the Windows 10 apps that were preinstalled or installed from the Microsoft Store.

To do this, you'll need to open PowerShell as an administrator – Command Prompt won't work for the command you'll run.

There are many ways to open PowerShell, but one of the fastest ways is to use the Run program.

Use the shortcut **Windows Key + R** to open the Run program, enter "powershell", then hold down "Ctrl + Shift" and click the "OK" button:

  


![Image](https://www.freecodecamp.org/news/content/images/2020/11/run-cmd-powershell.jpg)

This should open up a PowerShell terminal with administrative privileges.

In the PowerShell terminal, run the following command:

```
Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}

```

The `Get-AppXPackage` command will attempt to reinstall all the default Windows apps, including the Start Menu and search bar. 

It will also register a manifest file for each program it reinstalls. You don't need to worry about the manifest files, though – it's just something Windows needs to run each program.

Give it 5-10 minutes, and make sure you don't close the PowerShell window until it's finished.

**Note:** You may see some scary looking errors pop up as the `Get-AppXPackage` command is running. Don't worry about them – most are just warnings about why a program can't be reinstalled:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/powershell-get-appxpackage.jpg)

When the `Get-AppXPackage` command is finished, restart your computer, log in, and try to open the Start Menu.

## How to reset your Windows 10 installation

If none of the above methods fixed the Start Menu, the last thing you can try is to do a factory reset of your Windows 10 installation. But keep in mind that this is an "almost-scorched-earth" method, and should only be used as a last resort.

Resetting your Windows 10 installation should keep all of your personal files intact (documents, pictures, videos, and so on), but will uninstall all the other drivers and programs you've installed. Basically this resets your computer to the state it was in when you first turned it on.

Before going any further, make backups of all your important files using a flash drive, external HDD/SSD, and/or an online file host like Google Drive or Dropbox. 

In fact, make two backups. You probably won't need them, but it doesn't hurt.

When you've finished backing up all your files, open a PowerShell terminal – use the shortcut **Windows Key + R**, enter "powershell", then click the "OK" button.

In the PowerShell terminal, run the command `systemreset` to bring up the Windows reset wizard.

Next, click the "Keep my files" button:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/system-reset-keep-my-files.jpg)

Wait a moment while the wizard analyzes your system. Then, you'll see a list of all the programs that'll be removed:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/system-reset-programs-to-be-removed.jpg)

Click the "Next" button, and follow the instructions to reset your Windows 10 installation.

Once you're finished resetting Windows and creating a new user, the Start Menu should be working again.

## "Cortana, open the Start Menu"

So those are all the ways to fix the Windows 10 Start Menu, listed from easiest to hardest.

Did any of these methods work for you? Is there another way to open the Start Menu that I missed? Let me know about it on [Twitter](https://twitter.com/kriskoishigawa).

