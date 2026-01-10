---
title: How to Remove the Start Text from PowerShell
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-03-22T17:18:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-starting-text-from-powershell
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Artboard-1-1.jpg
tags:
- name: Powershell
  slug: powershell
- name: Windows
  slug: windows
seo_title: null
seo_desc: "If you are using a Windows operating system, you have likely used the latest\
  \ Windows PowerShell at least once. \nWhenever you open PowerShell using Windows\
  \ Terminal, you get a text message inside the terminal which shows the PowerShell\
  \ version, the li..."
---

If you are using a Windows operating system, you have likely used the latest Windows PowerShell at least once. 

Whenever you open PowerShell using Windows Terminal, you get a text message inside the terminal which shows the PowerShell version, the link to download the latest PowerShell, and so on. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--3--1.png)

Sometimes this can be annoying, and you might want to remove that text so that message never appears again. There is a way to do that, and in this article I will show you how you can remove the starting text from the terminal once and for all! ✌️

Firstly, open PowerShell in Windows Terminal. You will get the starting text as usual.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--3--2.png)

Click the drop down button to get the menu under it.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--4-.png)

Go to **Settings**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--5-.png)

You will get an interface like below:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--6-.png)

Click **Open JSON file**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--7-.png)

The JSON fill will be opened in a text editor. For me, it is Notepad – but for you, it might be VS Code or any other text editor you want.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--9-.png)

Scroll down until you find the PowerShell block like below.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--12-.png)

Add `"commandline": "pwsh.exe -nologo",` like below.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--14--1.png)

The command should be like this for the PowerShell block:

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--15-.png)

Then save the file. You can use the shortcut keys `Ctrl` + `S` for this as well.

Click **Save**.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--16-.png)

Close all the tabs.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--17--1.png)

Reopen the terminal and see the magic! 🪄

![Image](https://www.freecodecamp.org/news/content/images/2022/03/Screenshot--19--1.png)

## Conclusion

Thanks for reading the entire article. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!

The banner image has been taken from [storyset](https://storyset.com/worker) (Worker illustrations by Storyset) and modified using Adobe Photoshop.

