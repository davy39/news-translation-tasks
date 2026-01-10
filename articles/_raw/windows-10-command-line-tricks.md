---
title: 14 Windows 10 Command Line Tricks that Give You More Control Over Your PC
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-12-16T16:37:46.000Z'
originalURL: https://freecodecamp.org/news/windows-10-command-line-tricks
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/cmdtricks.png
tags:
- name: command line
  slug: command-line
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: "Windows 10 has an incredible Graphics User Interface (GUI) that will often\
  \ be enough for you to get things done. \nBut if your inner Oliver Twist wants more,\
  \ then you should start learning about the Command Line. \nWith the command prompt,\
  \ you get acce..."
---

Windows 10 has an incredible Graphics User Interface (GUI) that will often be enough for you to get things done. 

But if your inner [Oliver Twist](https://en.wikipedia.org/wiki/Oliver_Twist) wants more, then you should start learning about the Command Line. 

With the command prompt, you get access to features that are not available in the GUI and you get to interact directly with your Windows 10 operating system.

In this article, I’m going to show you 14 command line tips and tricks that'll help you feel like a superhero while using your computer and that will surely impress your friends as well.

Be aware that you should be very careful while executing commands in the command prompt because any command you execute might have a lasting effect on your computer.

Make sure you read until the end because I’m going to show you how to see the password of every Wi-Fi that has ever been connected to your computer.

## Table of Contents

- [How to Open the Command Prompt in any Folder](#heading-1-how-to-open-the-command-prompt-in-any-folder)
- [How to Create a Secure Folder with the Command Prompt](#heading-2-how-to-create-a-secure-folder-with-the-command-prompt)
- [How to Run the Command Prompt as an Administrator](#heading-3-how-to-run-the-command-prompt-as-an-administrator)
- [How to Encrypt Files with the Command Prompt](#heading-4-how-to-encrypt-files-with-the-command-prompt)
- [How to Hide a Folder with the Command Prompt](#heading-5-how-to-hide-a-folder-with-the-command-prompt)
- [How to Change the Background Color and Font Color of the Command Prompt](#heading-6-how-to-change-the-background-color-and-font-color-of-the-command-prompt)
- [How to Change the Title of the Command Prompt Window](#heading-7-how-to-change-the-title-of-the-command-prompt-window)
- [How to Change the Prompt Text of the Command Prompt](#heading-8-how-to-change-the-prompt-text-of-the-command-prompt)
- [How to Change the Font Size of the Command Prompt Texts](#heading-9-how-to-change-the-font-size-of-the-command-prompt-texts)
- [How to Generate Battery Health Report with the Command Prompt](#heading-10-how-to-generate-battery-health-report-with-the-command-prompt)
- [How to Log on to a Website from the Command Prompt](#heading-11-how-to-log-on-to-a-website-from-the-command-prompt)
- [How to Check the IP Address of a Website with the Command Prompt](#heading-12-how-to-see-the-ip-address-of-a-website-with-the-command-prompt)
- [How to Show All Wi-Fi Passwords with the Command Prompt](#heading-13-how-to-show-all-wi-fi-passwords-with-the-command-prompt)
- [How to Shut Down Your Computer With the Command Prompt](#heading-14-how-to-shut-down-your-computer-with-the-command-prompt)


## 1. How to Open the Command Prompt in any Folder

Not everyone wants the hassle of navigating around folders in the command line.

If you are one of those people like I am, you can open the folder directly in the command prompt by typing “cmd” in the folder address bar and then hitting `ENTER`
![open-cmd](https://www.freecodecamp.org/news/content/images/2021/12/open-cmd.gif)

There you go!

## 2. How to Create a Secure Folder with the Command Prompt

For privacy reasons, you might want to create a folder that cannot be edited, moved, copied, or deleted by any random person that gets access to your computer.

To do this, navigate to the directory where you want to create this folder or open the command prompt directly in it with the first tip in this article. Then execute the command – `md aux\`.
![ss-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-1.png)

This will create a folder named “aux”. It cannot be deleted, edited, moved, or copied. 

If you check and you can’t find the folder, refresh the directory in which you created the folder.
![ss-2-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-2-2.png)

So, what if you want to delete this folder? You can’t do that with the GUI, so you need to do it in the command line. Execute the command –`rd aux\` – to delete the folder. Make sure the files in the folder are backed up.

## 3. How to Run the Command Prompt as an Administrator

Sometimes, you might need administrative privileges when you don’t have access to the GUI. 

To get these, type in `powershell "start cmd -v runAs` and hit `ENTER`. Select Yes in the next prompt and it'll open a new window of the command prompt with administrative privileges.
![ss-3-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-3-2.png)

## 4. How to Encrypt Files with the Command Prompt

If you're not the only one who uses your Windows 10 computer and you want your files inaccessible to other users, you can encrypt the files by navigating to the folder where the files are located and typing in `Cipher /E`.
![ss-4-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-4-1.png)

Any other user apart from you will be unable to open the files.

## 5. How to Hide a Folder with the Command Prompt

So, what if you want to hide a folder? You can do that by typing in `attrib +h +s +r folder_name` and then hitting `ENTER`.

To show the folder again, execute the command – `attrib -h -s -r folder_name`.
![ss-5-3](https://www.freecodecamp.org/news/content/images/2021/12/ss-5-3.png)

## 6. How to Change the Background Color and Font Color of the Command Prompt

If the old-school black and white colors of the command line look boring to you, you can change them to your desired color scheme.

To do this, launch the command prompt and run `color -help`. This will show you available colors represented by numbers and alphabets. You can change the background and font colors to.
![ss-7](https://www.freecodecamp.org/news/content/images/2021/12/ss-7.png)

To change the colors properly, run `color background_color_number font_color_number`. For example, `color 02` leaves the background color black and changes the font color to green.

![ss-6-3](https://www.freecodecamp.org/news/content/images/2021/12/ss-6-3.png)

## 7. How to Change the Title of the Command Prompt Window

The title of an opened command prompt window doesn’t need to stay as the default – you can change it.

To do this, type in `title window_title_name`.
![ss-8-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-8-2.jpg)

## 8. How to Change the Prompt Text of the Command Prompt

The text that appears before you type your commands might not be attractive enough for you. For me, it isn’t, so I've changed it. 

To change the prompt text, type in `prompt prompt_name $G` and hit `ENTER`.
The “$G” in front of the specified prompt name will append the greater than (>) symbol for you, so you can know where your command starts – a better UX for you, by you!
![ss-9](https://www.freecodecamp.org/news/content/images/2021/12/ss-9.jpg)

## 9. How to Change the Font Size of the Command Prompt Texts

If the default font size of the command prompt is too small for your eyes, you can change it. You don’t even need to run a command for this.

**Step 1**: Right-click on the command prompt window and select “properties”.
![ss-10-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-10-1.jpg)

**Step 2**: Switch to the font tab and select your desired font size, then click “Ok”.
![ss-11-2](https://www.freecodecamp.org/news/content/images/2021/12/ss-11-2.jpg)

## 10. How to Generate Battery Health Report with the Command Prompt

With this, you get to know the state of your laptop battery and what to do to improve it. In fact, this is my favorite thing that the command prompt lets me do. 

To generate a battery health report, make sure you are running the command prompt as an administrator. Then enter the command `powercfg/energy` and hit `ENTER`.
![ss-12](https://www.freecodecamp.org/news/content/images/2021/12/ss-12.png)

An HTML file you can open with the browser will be generated for you in 60 seconds. 
You can locate the HTML file in `C:\Windows\system32\energy-report.html`.

## 11. How to Log on to a Website from the Command Prompt 

You can open a website from the command prompt by typing in `start www.website_name.com` and then hitting `ENTER`. Then the website will open in your default browser.
![ss-13](https://www.freecodecamp.org/news/content/images/2021/12/ss-13.png)

![ss-14-1](https://www.freecodecamp.org/news/content/images/2021/12/ss-14-1.png)

Note that you must append “www” before the domain name, otherwise, it doesn’t work.

## 12. How to see the IP Address of a Website with the Command Prompt

You can check the IP address of any website by typing `ping www.website_name.com` and then hitting `ENTER`.
![ss-15](https://www.freecodecamp.org/news/content/images/2021/12/ss-15.png)

Note that you must append “www” before the domain name, otherwise, it doesn’t work.

## 13. How to Show All Wi-Fi Passwords with the Command Prompt

You can check the password of your current WiFi connection with the GUI. But the command prompt also shows the passwords of every WiFi that has ever connected with your computer.

To check the passwords, run the command – `for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear` and hit `ENTER`.

You can find the key right in front of “Key content”.
![ss-16](https://www.freecodecamp.org/news/content/images/2021/12/ss-16.jpg)

I blurred out the key, as some of my neighbors read my freeCodeCamp articles. :)

## 14. How to Shut Down Your Computer With the Command Prompt

Now that you’ve learned about 11 helpful commands that'll make you feel like a boss, here's one more: shut down or restart your computer with the command prompt.

To shut down your computer with the command prompt, run the command `shutdown -s`. 
To restart your computer, enter `shutdown -r` and hit `ENTER`.

To set a countdown for when your computer will shut down, enter `shutdown /s /t time_in_seconds` and hit `ENTER`.
![ss-17](https://www.freecodecamp.org/news/content/images/2021/12/ss-17.png)

To set a countdown and an alert message for when your computer will shut down, enter `shutdown /s /t time_in_seconds /c “alert_message” ` and hit `ENTER`.
![ss-18](https://www.freecodecamp.org/news/content/images/2021/12/ss-18.png)

Thank you for reading this article. If you find it helpful, please share with your friends and family.


