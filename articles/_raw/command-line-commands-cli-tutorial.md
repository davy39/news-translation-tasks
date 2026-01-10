---
title: Command Line Commands – CLI Tutorial
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-08-09T15:28:14.000Z'
originalURL: https://freecodecamp.org/news/command-line-commands-cli-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cli.png
tags:
- name: command line
  slug: command-line
- name: Windows
  slug: windows
seo_title: null
seo_desc: 'The Windows command line is one of the most powerful utilities on a Windows
  PC. With it, you can interact with the OS directly and do a lot of things not available
  in the graphical user interface (GUI).

  In this article, I’ll show you 40 commands you ...'
---

The Windows command line is one of the most powerful utilities on a Windows PC. With it, you can interact with the OS directly and do a lot of things not available in the graphical user interface (GUI).

In this article, I’ll show you 40 commands you can use on the Windows command line that can boost your confidence as a Windows user.

**N.B.**: You have to be careful while using the commands I’ll show you. This is because some commands can have a lasting negative or positive effect on your Windows PC until you reset it.

In addition, some of these commands require you to open the command prompt as an admin.
![ss5-1](https://www.freecodecamp.org/news/content/images/2022/08/ss5-1.png)


## Windows Command Line Commands

### ` powershell start cmd -v runAs` – Run the Command Prompt as an Administrator

Entering this command opens another command prompt window as an administrator:
![ss1-1](https://www.freecodecamp.org/news/content/images/2022/08/ss1-1.png)


### `driverquery` – Lists All Installed Drivers

It is important to have access to all drivers because they often cause problems. 

That’s what this command does – it shows you even the drivers you won’t find in the device manager.
![ss2-1](https://www.freecodecamp.org/news/content/images/2022/08/ss2-1.png)


### `chdir` or `cd` – Changes the Current Working Directory to the Specified Directory
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/08/ss3-1.png)


### `systeminfo` – Shows Your PC's Details

If you want to see more detailed information about your system you won’t see in the GUI, this is the command for you.
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/08/ss4-1.png)


### `set` – Shows your PC’s Environment Variables

![ss5-2](https://www.freecodecamp.org/news/content/images/2022/08/ss5-2.png)


### `prompt` – Changes the Default Text Shown before Entering Commands

By default, the command prompt shows the C drive path to your user account. 

You can use the `prompt` command to change that default text with the syntax `prompt prompt_name $G`:
![ss6-1](https://www.freecodecamp.org/news/content/images/2022/08/ss6-1.png)

**N.B**: If you don’t append `$G` to the command, you won’t get the greater than symbol in front of the text.


### `clip` – Copies an Item to the Clipboard
For example, `dir | clip` copies all the content of the present working directory to the clipboard.
![ss7](https://www.freecodecamp.org/news/content/images/2022/08/ss7.png)

You can type `clip /?` and hit `ENTER` to see how to use it.


### `assoc` – Lists Programs and the Extensions They are Associated With
![ss8](https://www.freecodecamp.org/news/content/images/2022/08/ss8.png)


### `title` – Changes the Command Prompt Window Title Using the Format `title window-title-name`

![ss9](https://www.freecodecamp.org/news/content/images/2022/08/ss9.png)


### `fc` – Compares Two Similar Files 

If you are a programmer or writer and you want to quickly see what differs between two files, you can enter this command and then the full path to the two files. For example `fc “file-1-path” “file-2-path”`.
![ss10](https://www.freecodecamp.org/news/content/images/2022/08/ss10.png)

### `cipher` – Wipes Free Space and Encrypts Data

On a PC, deleted files remain accessible to you and other users. So, technically, they are not deleted under the hood. 

You can use the cipher command to wipe the drive clean and encrypt such files.
![ss11](https://www.freecodecamp.org/news/content/images/2022/08/ss11.png)


### `netstat -an` – Shows Open Ports, their IP Addresses and States
![ss12](https://www.freecodecamp.org/news/content/images/2022/08/ss12.png)


### `ping` – Shows a Website IP Address, Lets you Know How Long it Takes to Transmit Data and a Get Response  
![ss13](https://www.freecodecamp.org/news/content/images/2022/08/ss13.png)


### `color` – Changes the Text Color of the Command Prompt
Enter `color attr` to see the colors you can change to:
![ss14](https://www.freecodecamp.org/news/content/images/2022/08/ss14.png)

Entering `color 2` changes the color of the terminal to green:
![ss15](https://www.freecodecamp.org/news/content/images/2022/08/ss15.png) 


### `for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear` – Shows All Wi-Fi Passwords

![ss16](https://www.freecodecamp.org/news/content/images/2022/08/ss16.png) 


### `ipconfig` – Shows Information about PC IP Addresses and Connections

![ss17](https://www.freecodecamp.org/news/content/images/2022/08/ss17.png) 

This command also has extensions such as `ipconfig /release`, `ipconfig /renew`, and `ipconfig /flushdns` which you can use to troubleshoot issues with internet connections.

### `sfc` – System File Checker
This command scans your computer for corrupt files and repairs them. The extension of the command you can use to run a scan is `/scannow`.
![ss18](https://www.freecodecamp.org/news/content/images/2022/08/ss18.png) 


### `powercfg` – Controls Configurable Power Settings
You can use this command with its several extensions to show information about the power state of your PC. 

You can enter `powercfg help` to show those extensions.
![ss19](https://www.freecodecamp.org/news/content/images/2022/08/ss19.png) 

For example, you can use `powercfg /energy` to generate a battery health report.
![ss20](https://www.freecodecamp.org/news/content/images/2022/08/ss20.png) 

The `powercfg /energy` command will generate an HTML file containing the report. You can find the HTML file in `C:\Windows\system32\energy-report.html`.


### `dir` – Lists Items in a Directory
![ss21](https://www.freecodecamp.org/news/content/images/2022/08/ss21.png)


### `del` – Deletes a File 
![ss22](https://www.freecodecamp.org/news/content/images/2022/08/ss22.png)


### ` attrib +h +s +r folder_name ` – Hides a Folder 

You can hide a folder right from the command line by typing in `attrib +h +s +r folder_name` and then pressing `ENTER`.

To show the folder again, execute the command `– attrib -h -s -r folder_name`.
![ss23](https://www.freecodecamp.org/news/content/images/2022/08/ss23.png)


### `start website-address` – Logs on to a Website from the Command Line
![ss24](https://www.freecodecamp.org/news/content/images/2022/08/ss24.png)
![ss25](https://www.freecodecamp.org/news/content/images/2022/08/ss25.png) 


### `tree` – Shows the Tree of the Current Directory or Specified Drive
![ss26](https://www.freecodecamp.org/news/content/images/2022/08/ss26.png) 


### `ver` – Shows the Version of the OS
![ss27](https://www.freecodecamp.org/news/content/images/2022/08/ss27.png)


### `tasklist` – Shows Open Programs

You can do the same thing you do with the task manager with this command:
![ss28](https://www.freecodecamp.org/news/content/images/2022/08/ss28.png)
The next command shows you how to close an open task.


### `taskkill` – Terminates a Running Task

To kill a task, run `taskkill /IM "task.exe" /F`. For example, `taskkill /IM "chrome.exe" /F`:
![ss29](https://www.freecodecamp.org/news/content/images/2022/08/ss29.png) 


### `date` – Shows and Changes the Current Date
![ss30](https://www.freecodecamp.org/news/content/images/2022/08/ss30.png)


### `time` – Shows and Changes the Current Time
![ss31](https://www.freecodecamp.org/news/content/images/2022/08/ss31.png)


### `vol` – Shows the Serial Number and Label Info of the Current Drive
![ss32](https://www.freecodecamp.org/news/content/images/2022/08/ss32.png) 


### `dism` – Runs the Deployment Image Service Management Tool
![ss33](https://www.freecodecamp.org/news/content/images/2022/08/ss33.png) 


### `CTRL + C` – Stops the Execution of a Command 

### `-help` – Provides a Guide to other Commands

For example, `powercfg -help` shows how to use the `powercfg` command
![ss34](https://www.freecodecamp.org/news/content/images/2022/08/ss34.png) 


### `echo` – Shows Custom Messages or Messages from a Script or File
![ss35](https://www.freecodecamp.org/news/content/images/2022/08/ss35.png) 

You can also use the `echo` command to create a file with this syntax `echo file-content > filename.extension`.
![ss36](https://www.freecodecamp.org/news/content/images/2022/08/ss36.png) 


### `mkdir` – Creates a Folder
![ss37](https://www.freecodecamp.org/news/content/images/2022/08/ss37.png)


### `rmdir` – Deletes a Folder
![ss38](https://www.freecodecamp.org/news/content/images/2022/08/ss38.png)

**N.B.:** The folder must be empty for this command to work.


### `more` – Shows More Information or the Content of a File
![ss39](https://www.freecodecamp.org/news/content/images/2022/08/ss39.png) 


### `move` – Moves a File or Folder to a Specified Folder
![ss40](https://www.freecodecamp.org/news/content/images/2022/08/ss40.png)


### `ren` – Renames a File with the Syntax `ren filename.extension new-name.extension`
![ss41-1](https://www.freecodecamp.org/news/content/images/2022/08/ss41-1.png)


### `cls` – Clears the Command Line 

In case you enter several commands and the command line gets clogged up, you can use `cls` to clear all entries and their outputs.
![cls](https://www.freecodecamp.org/news/content/images/2022/08/cls.gif)


### `exit` – Closes the Command Line 


### `shutdown` – Shuts down, Restarts, Hibernates, Sleeps the Computer

You can shut down, restart, hibernate, and sleep your PC from the command line. 

Enter `shutdown` in the command line so you can see the extensions you can use to perform the actions. For example, shutdown /r will restart your computer.
![ss42](https://www.freecodecamp.org/news/content/images/2022/08/ss42.png)


## Conclusion

This article showed you several “unknown-to-many” commands you can use to get access to hidden functionalities on your Windows PC.

Again, you should be careful while working with these commands because they can have a lasting effect on your OS.

If you find the commands helpful, share the article with your friends and family.

In case you know another useful command I did not list, [tell me about it on Twitter](https://twitter.com/Ksound22). I will add it and mention you as the source.


