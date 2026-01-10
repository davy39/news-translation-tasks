---
title: How to Install C and C++ Compilers on Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2022-02-22T18:04:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-c-and-cpp-compiler-on-windows
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/banner_freeCodeCamp.png
tags:
- name: C++
  slug: c-2
- name: c programming
  slug: c-programming
- name: compilers
  slug: compilers
seo_title: null
seo_desc: "If you want to run C or C++ programs in your Windows operating system,\
  \ then you need to have the right compilers. \nThe MinGW compiler is a well known\
  \ and widely used software for installing GCC and G++ compilers for the C and C++\
  \ programming language..."
---

If you want to run C or C++ programs in your Windows operating system, then you need to have the right compilers. 

The MinGW compiler is a well known and widely used software for installing GCC and G++ compilers for the C and C++ programming languages. 

But many devs face difficulties when installing the compiler, so I am going to show you all the steps to do so in this article with screenshots to help you get it done. 

I will be using Windows 11, but the same process is applicable for all other Windows operating systems unless you are using Windows XP (You need to change some steps in Windows XP).

If you'd like to watch the video I made on this topic as well, here it is:

%[https://www.youtube.com/watch?v=c7FjV8Gwk_M]

## Install MSYS2

Firstly we need to download an executable file from MSYS2. Go to the official website of MSYS2: [https://www.msys2.org/](https://www.msys2.org/). The website looks like below as of today.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--8-.png)

Scroll down a little bit until you find the download button for the executable file.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--9-.png)

Simply click on the installer button and save the installer file in any place you want.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--10--1.png)

Finish downloading the executable file. It should not take much time depending on your internet speed.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--11-.png)

After downloading the file, we will get this executable file.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--12-.png)

Double click on the executable file. Then click `Next`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--13-.png)

Keep the name as it is, and click `Next`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--14--1.png)

Keep all this as it is, and click `Next`.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--15-.png)

Give it some time to finish the installation process.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--16-.png)

If you keep the checkmark, then the MSYS2 terminal will open once you click `Finish`. 

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--17-.png)

I prefer to do it this way, but if you want to do the remaining tasks later, then you need to open the terminal by yourself from the start menu. 

In that case, you have to click the start button > Search for `MSYS2` and click on the terminal like in the following picture:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--26-.png)

Let me assume that we have opened the **MSYS2 MSYS** terminal successfully.

Apply the command `pacman -Syu` to update the package database and the base packages.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--19-.png)

Type `Y` and press the enter key if you get this type of installation prompt.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--20-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--21-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--22-.png)

Type `Y` and press the enter key.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--23-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--24-.png)

The terminal will be closed. We have to open the terminal manually and update the rest of the packages.

Click the start button.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--25-.png)

Search the folder named **MSYS2 64bit**. Click on the folder to expand and get the terminal. Open the terminal by clicking **MSYS2 MSYS**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--26--1.png)

Update the rest of the packages by applying the command, `pacman -Su`. You might need to apply the command `pacman -Sy` if the terminal tells you to do that.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--27-.png)

If you get any installation prompt, then you need to type `Y` or `y` and press the enter key.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--28-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--29-.png)

Wait a little to finish the installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--30-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--31-.png)

Close the window after finishing the installation.

## Install the GCC and G++ Compilers

Click the start button. Find the **MSYS2 64bit** folder. Click on that folder to expand it.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--32-.png)

If you are using a **64 bit** operating system like I am, then we need to use the **MSYS2 MinGW x64** terminal. Click on the terminal to open that.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--33-.png)

⚠️ But, if you are using a **32 bit** operating system, then you have to use the **MSYS2 MinGW x86** terminal. Then, you need to open that terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--34-.png)

As I am using a **64 bit** operating system, I have opened the terminal for 64 bit. Apply the command `pacman -S mingw-w64-x86_64-gcc` to install the compilers.

⚠️ If you are using a **32 bit** operating system, then you have to apply the command `pacman -S mingw-w64-i686-gcc` in your 32 bit terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--35-.png)

Wait for a little while.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--36-.png)

Type `Y` or `y` and press the enter key if you get the installation prompts.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--37-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--38-.png)

Give it some time to finish the installation process.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--39-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--39--1.png)

You've now finished installing the compilers.

## How to Install the Debugger

If you are using a **64 bit** operating system like I am, then you have to apply the command `pacman -S mingw-w64-x86_64-gdb`.

⚠️ If you are using a **32 bit** operating system, then you have to apply the command `pacman -S mingw-w64-i686-gdb` in your 32 bit terminal.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--41-.png)

If you get any installation prompt, then simply type `Y` or `y` and press the enter key.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--42-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--38--1.png)

Give it some time to finish the installation.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--44-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--45-.png)

You can close the terminal.

## How to Add the Directory to the Path of the Environment Variables

Open the file explorer.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--46-.png)

I am assuming that you have installed the MSYS into the default directory like I have. If you used custom directories, then you need to go to the directory where you installed it.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--47-.png)

If you are using a 64 bit operating system like I am, then go to the **mingw64** folder.

⚠️ If you are using a 32 bit operating system, then go to the **mingw32** folder.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--48-.png)

We have to go to the binary folder now. Go to the **bin** folder.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--49-.png)

⚠️ If you are using a 32 bit operating system, then you have to go into your **mingw32** folder > **bin** folder.

Copy the directory.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--51-.png)

⚠️ If you are using a 32 bit operating system, and you also installed the MSYS2 in the default directory, then your directory should be like the following:

```
C:\msys64\mingw32\bin
```

Open the **Advanced System Settings**. You can do that in many ways. A simple way is to simply click the start button and search for it like the below screenshot.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--52-.png)

Click **Environment Variables** from the Advanced tab.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--54-.png)

Click on **Path** and select that. Then click **Edit**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--57-.png)

A window will appear as below:

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--58-.png)

Click **New**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--59-.png)

A blank box will appear.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--60-.png)

Paste the directory here.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--61-.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--62-.png)

Click **OK**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--63-.png)

Click **OK**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--65-.png)

Click **OK**.

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--66-.png)

If you want to get all the steps in a video, then you can watch [this video](https://www.youtube.com/watch?v=0HD0pqVtsmw) as well.

## Check the Install

Now it is time to check whether we have successfully installed all of the above or not.

Open the terminal / PowerShell / CMD and apply the commands serially:

For checking the **GCC** version:

```powershell
gcc --version
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--68-.png)

For checking the **G++** version:

```powershell
g++ --version
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--69-.png)

For checking the **GDB** version:

```powershell
gdb --version
```

![Image](https://www.freecodecamp.org/news/content/images/2022/02/Screenshot--70-.png)

## Conclusion

I hope this article helps you install your compilers on the Windows operating system for C and C++ programs. 

Thanks for reading the entire article. If it helps you then you can also check out other articles of mine at [freeCodeCamp](https://www.freecodecamp.org/news/author/fahimbinamin/).

If you want to get in touch with me, then you can do so using [Twitter](https://twitter.com/Fahim_FBA), [LinkedIn](https://www.linkedin.com/in/fahimfba/), and [GitHub](https://github.com/FahimFBA). 

You can also [SUBSCRIBE to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) (Code With FahimFBA) if you want to learn various kinds of programming languages with a lot of practical examples regularly.

If you want to check out my highlights, then you can do so at my [Polywork timeline](https://www.polywork.com/fahimbinamin).

You can also [visit my website](https://fahimbinamin.com/) to learn more about me and what I'm working on.

Thanks a bunch!

