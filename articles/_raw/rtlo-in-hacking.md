---
title: What is RTLO in Hacking? How to Use Right-to-Left Override and Defend Against
  it
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2023-02-28T00:36:36.000Z'
originalURL: https://freecodecamp.org/news/rtlo-in-hacking
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/image-249-1.png
tags:
- name: Ethical Hacking
  slug: ethical-hacking
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: null
seo_desc: 'Let’s play a lovely game of hide your malware in plain sight. 🐴

  Malicious hackers look for all kinds of underhanded tricks to make everyday users
  victims as a result of common mistakes. They might get someone to click the wrong
  link, open the wrong ...'
---

Let’s play a lovely game of hide your malware in plain sight. 🐴

Malicious hackers look for all kinds of underhanded tricks to make everyday users victims as a result of common mistakes. They might get someone to click the wrong link, open the wrong website, or execute the wrong program.

Most times, it’s easy to identify a suspicious file by the following:

1. The icon does not match the name
2. The extension seems incorrect
3. The file is noticeably bigger or smaller than its proposed file type (Imagine an image of 50mb 🤯)

But would you be suspicious of a file like this?

![image-248](https://www.freecodecamp.org/news/content/images/2023/02/image-248.png)
_A totally non-suspicious file | Credit: Mercury_

Nothing out of the ordinary right? Seems like your average word document. Let’s take a closer look at things.

![image-250](https://www.freecodecamp.org/news/content/images/2023/02/image-250.png)
_Properties of the file | Credit: Mercury_

In this tutorial, you’ll learn:

1. What Right-To-Left Override is
2. How to use it to hide file extensions
3. How to detect if it was used on a file
4. Mitigations

**Friendly Disclaimer**: This is simply for educational purposes only and is written solely to protect individuals, businesses, and organisations from threat actors. If you still wish to use this in any other way, that's your choice...just get ready for a lovely trip to jail…for a long time. 🙂

And with that intro, let’s jump in 🙃

## **What is Right-To-Left Override?**

![image-252](https://www.freecodecamp.org/news/content/images/2023/02/image-252.png)
_When nothing goes right, go left | Credit: [Wallpaperflare.com](http://wallpaperflare.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

Right-To-Left Override (RTO or RTLO) is a Unicode non-printing character used to write languages read in the right-to-left manner. It takes the input and literally just flips the text the other way round. Such languages include Hebrew, Arabic, Aramaic, and Urdu.

You can find the character in the character map in both Windows and Linux using the code [202E].

![image-253](https://www.freecodecamp.org/news/content/images/2023/02/image-253.png)
_Character map | Credit: Mercury_

Below is a demonstration of how it is used:

![image-254](https://www.freecodecamp.org/news/content/images/2023/02/4.2---RTLO-demonstration.gif)
_RTLO Demonstration | Credit: Mercury_

As you may see, the two statements typed are the exact same thing, except that the one below is written in the inverse because the RTLO character was inserted before typing it.

## **How RTLO Can Be a Malicious Tool**

Perhaps at first glance this character looks innocent enough. What’s the harm in flipping some text anyway? The answer: File extensions.

![image-255](https://www.freecodecamp.org/news/content/images/2023/02/image-255.png)
_A Chrome installer as an installer and word document | Credit: Mercury_

Below are some hacks carried out in the past using this technique:

1. **Telegram**: In 2018, Kaspersky reported in [a blogpost on Securelist](https://securelist.com/zero-day-vulnerability-in-telegram/83800/) that Russian cybercriminals exploited RTLO gaps in the wild on Telegram Windows Clients. As demonstrated in the article, this allowed the criminals to install cryptominers or RATs when a user opened what seemed to be a harmless file ⛏️.
2. **Scarlet Mimic**: In 2016, Unit 42 from Palo Alto Networks released a report on the tactics of a threat group known as Scarlet Mimic. The group is commonly known for targeting minority activists. According to [the report](https://unit42.paloaltonetworks.com/scarlet-mimic-years-long-espionage-targets-minority-activists/), one of the groups common tactics included using RTLO characters to mask the actual file extensions of self-extracting archives (SFX/SEA)🎭.
3. **Famous Messaging apps**: In 2022, Bleeping computer released a [news article](https://www.bleepingcomputer.com/news/security/url-rendering-trick-enabled-whatsapp-signal-imessage-phishing/) about phishing techniques on messaging and email platforms using RTLO. Platforms such as iMessage, WhatsApp, Signal, and Facebook Messenger (I wonder who uses the last one 🤨) were vulnerable to such tactics. It allowed an attacker to inject an RTLO character in between two links. On the left was a legitimate domain such as ([google.com](http://google.com/)) and on the right was a malicious one. This made it appear as one link and if a user clicked on the left side, they were safe. However, if they clicked on the right side, they were not.
4. **PLEAD**: In 2017, Trend Micro released [an article](https://www.trendmicro.com/en_us/research/17/f/following-trail-blacktech-cyber-espionage-campaigns.html) on three campaigns performed by a threat group known as BlackTech. One of these campaigns was named PLEAD, which focused on information theft and was targeted at the Taiwanese government and organisations. According to the article, spear-phishing emails were used to deliver and install a backdoor. The notable part of this attack was that the installers where disguised as documents using RTLO characters and decoy documents were also added to trick users 📄.
5. **Apple’s OS X**: Despite being common in Windows, this technique could be used to target Mac users. In 2013, [a blogpost](https://archive.f-secure.com/weblog/archives/00002576.html) by F-Secure Labs revealed that RTLO was used to disguise a relatively mild Mac malware in the wild. However, the malware screams ‘I’m a virus!’ due to the fact that OS X shows the real file extension and when run, the file quarantine notification is written backwards (Nice one Apple 😉🍎).

## **How to Hide a Potentially Malicious File**

![image-256](https://www.freecodecamp.org/news/content/images/2023/02/image-256.png)
_A Guy Fawkes Mask | Credit: [Wallpaperflare.com](http://wallpaperflare.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

RTLO can be used in any attack that leverages tricking the user about written text. As we saw in the above hacks, links, email attachments and executable scripts and files are the most common attack vectors.

But this tutorial will focus on locally hosted files because it gives the basic idea and its variations can be used to carry out other attacks.

There are two steps to the process:

1. Insert the RTLO character in the file name
2. Change the file icon

The file icon needs to be changed to mimic the fake extension to make it easier to trick a user.

Below are the prerequisites for the procedure:

1. An executable or script – The payload
2. A file icon – Part of the bait
3. Resource hacker – To change the file icon

The file icon could be in .exe, .dll, .res, or .ico format. You can download some from [here](https://icon-icons.com/). And now, let the chaos begin ⚠️.

### **Step 1 – Insert the RTLO character**

Choose a file of your liking and open it in Windows Explorer. Open the Character Map app on Windows and check the ‘Advanced View’ box. In the ‘Go to Unicode’ option, type in 202E. Hit the ‘Select’ and ‘Copy’ buttons respectively and go to the file you want to modify.

![image-257](https://www.freecodecamp.org/news/content/images/2023/02/6---RTLO-demonstration.gif)
_Selecting the Right-To-Left Override Character | Credit: Mercury_

Here is the tricky part 🎃. When typing with the RTLO character, it types from right-to-left. This can be confusing when trying to rename the file. If you want to rename a file after injecting the character, spell it backwards.

For example, if you want to write the extension ‘.pdf’, you have to type it as ‘fdp.’ It takes some time getting used to but it's easy after a few tries.

![image-258](https://www.freecodecamp.org/news/content/images/2023/02/7---RTLO-demonstration.gif)
_Short renaming demonstration | Credit: Mercury_

In File Explorer, check the option to show file extensions. Go to the file, right-click and hit rename. Change the name to whatever you want but make sure not to ever edit the extension itself so the file works as intended❗.

Set the cursor just before the extension name. Paste the RTLO character. You will observe it seems like nothing happened but that’s how it is supposed to look. Next type in ‘xcod’ to get ‘docx’ and hit enter.

![image-259](https://www.freecodecamp.org/news/content/images/2023/02/8---Gif-of-renaming.gif)
_Renaming the target file | Credit: Mercury_

### **Step 2 – Change the Icon**

Now for the final part of our amazing trick – changing the icon 🪄. Download and install a software called resource hacker. Open it and hit Ctrl + O. Next, select your target program. There’s a lot of information here that we can edit, but we just want to focus on the icon.

![image-260](https://www.freecodecamp.org/news/content/images/2023/02/image-260.png)
_Resource Hacker | Credit: Mercury_

Hit Ctrl+R to open the replace window and click on the ‘Open file with new icon’ button.

In the Explorer, select the file icon you wish to replace on the program and hit the ‘Replace’ button.

Lastly, hit Ctrl+S to save the file. If you have an Antivirus, you might want to temporarily switch it off before saving the file.

![image-261](https://www.freecodecamp.org/news/content/images/2023/02/Untitled.gif)
_Using Resource Hacker to change the icon | Credit: Mercury_

![image-262](https://www.freecodecamp.org/news/content/images/2023/02/image-262.png)
_A totally non-suspicious file | Credit: Mercury_

Neat, isn’t it? Let’s look at how to avoid falling for this trick.

## **Mitigations**

![image-263](https://www.freecodecamp.org/news/content/images/2023/02/image-263.png)
_Online Security | Credit: [Wallpaperflare.com](http://wallpaperflare.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

Since it abuses system features, almost any regular user or tech geek would fall for this hack. So how can you avoid it? Here are some tips:

### **Never open a file or link of unknown origin**

Never underestimate the power of basic cyber hygiene. Don’t click random links, or open files that you have no clue where they came from or who sent them.

### **Set file extensions to be shown**

A file name that hides its extension is much more easily noticed to be fishy when file extensions are on.

Be cautious if you notice that just before the extension, the file ends with common file extensions written backwards. For example, ‘infoexe.pdf’ will be obvious. However, some are less obvious like ‘infosbv.png' which could be a Visual Basic script (.vbs). A file named ‘Samsung_Galaxy_tab.png’ could be a batch file (.bat).

### **Install and keep Antivirus software up to date**

In case you have fallen for such, this could be your last line of defense. An appropriate antivirus will take note if a script or executable file with malicious actions has been executed and will quarantine or delete it.

I mean, a $20 yearly subscription sounds better than over $200 down the drain for nothing 💀.

### **Apply best practices**

For the more sophisticated IT people in organisations, implementation of best practices such as Network traffic analysis, firewalls, use of intrusion detection and prevention systems and network segmentation are your best bet.

## **Conclusion**

Let’s summarise what you’ve learned:

1. How to use RTLO characters to manipulate text
2. How to change application icons using Resource Hacker
3. How to identify text manipulated with RTLO characters

Initially it’s hard to identify files modified like this. I encourage you to play around with different file names and extensions and see what you get. This will also train you to identify files that are not what they seem.

Remember, **this is strictly for educational purposes**. And with that, we have come to the end of this article. As I always say, Happy Hacking! 🙃

## **Resources**

1. [Other ways to change an app icon](https://www.wikihow.com/Change-the-Icon-for-an-Exe-File)
2. [More ways to use RTLO](http://blog.sevagas.com/?Bypass-Defender-and-other-thoughts-on-Unicode-RTLO-attacks)

## **Acknowledgements**

Thanks to [Anuoluwapo Victor](https://twitter.com/Anuoluwap__o?t=4Cv6VR2c2_wK5HLXwbvXCQ&s=09), [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Favour Ojo](https://www.linkedin.com/in/favour-ojo-906883199/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), and my family for the inspiration, support and knowledge used to put this post together. You all inspire me daily.

Cover image credit: The Kelpies | Jamie McInall

