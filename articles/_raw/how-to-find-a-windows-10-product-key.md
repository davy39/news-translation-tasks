---
title: How to Find a Windows 10 Product Key
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-11-10T06:26:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-find-a-windows-10-product-key
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc8850349c47664ed8290dd.jpg
tags:
- name: Windows
  slug: windows
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'If you''re having trouble finding your Windows 10 product key, we''ve got
  you covered.

  In this quick tutorial we''ll go over what a Windows product key is, and I''ll share
  several ways to find the product key on modern Windows machines.

  What''s a Windows ...'
---

If you're having trouble finding your Windows 10 product key, we've got you covered.

In this quick tutorial we'll go over what a Windows product key is, and I'll share several ways to find the product key on modern Windows machines.

## What's a Windows 10 product key?

A Windows product key or license is a 25 digit code used to activate your installation of Windows.

Back in the day, all you had to do to find your Windows product key was look for a sticker somewhere on the machine.

Usually you could find the sticker on the side of a desktop PC, or stuck to the bottom of a laptop:

![Picture of a Windows 7 product key sticker](https://www.freecodecamp.org/news/content/images/2020/12/windows-7-product-key-sticker.jpg)
_An old-school Windows product key sticker – [Source](https://answers.microsoft.com/en-us/windows/forum/windows_10-win_licensing/how-to-find-your-windows-product-key/f032f08f-f114-46f6-ab81-b28004dd43a0)_

Or if you bought a physical copy of Windows, your product key would be included somewhere in the box:

![Image](https://www.freecodecamp.org/news/content/images/2020/12/windows-10-physical-product-key.png)
_A Windows 10 product key label - [Source](https://answers.microsoft.com/en-us/windows/forum/windows_10-win_licensing/how-to-find-your-windows-product-key/f032f08f-f114-46f6-ab81-b28004dd43a0)_

These days, if you buy a Windows 10 Home or Pro from the Microsoft Store or another online retailer like Amazon, it'll include a digital copy of your product key.

But if your computer is relatively new and came with Windows preinstalled, you might be wondering how to find your key – there's likely no sticker on the machine, and the computer manufacturer probably didn't include one in the box.

Whether you installed and activated Windows yourself, or it came preinstalled, your product key is stored in the [BIOS](https://www.freecodecamp.org/news/uefi-vs-bios/). This makes it really easy if you ever want to reinstall or upgrade Windows – there's no sticker on the machine that could get damaged, and no small label to lose.

Still, there are times when you might need your product key, like if you want to transfer a Windows Home or Pro license to another machine.

Whatever the reason, here are a few ways to get your Windows 10 product key.

## How to get your Windows 10 product key with the Command Prompt

If you want to get your product key from Windows, the easiest way is to do that is through the Windows Command Prompt.

First, press the Windows key, search for "cmd", and click on "Run as administrator":

![Screenshot of opening the command prompt as an administrator](https://www.freecodecamp.org/news/content/images/2020/12/open-admin-command-prompt.jpg)

Then, run the following command: 

```
wmic path softwarelicensingservice get OA3xOriginalProductKey
```

After that, you'll see your Windows 10 product key:

![Output of the wmic command listed above](https://www.freecodecamp.org/news/content/images/2020/12/wmic-output.jpg)

Alternatively, you can run this command in the Command Prompt terminal:

```
powershell "(Get-WmiObject -query ‘select * from SoftwareLicensingService’).OA3xOriginalProductKey"
```

![Output of the powershell command listed above](https://www.freecodecamp.org/news/content/images/2020/12/powershell-output.jpg)

Both of these commands attempt to read your Windows product key from something called the OA3 BIOS marker. In other words, they may only work if Windows came preinstalled, and not if you built the machine yourself and installed/activated Windows.

If your product key isn't saved to your BIOS/UEFI for some reason, then these commands will either throw an error or return an empty string. In this case, or if you prefer a GUI, give the next method a try.

## How to get your Windows 10 product key with a third-party program

There are a few tools out there like [Belarc Advisor](https://www.belarc.com/products_belarc_advisor) or [Magical Jelly Bean KeyFinder](https://www.magicaljellybean.com/keyfinder/) that can detect your Windows product key.

We'll use Magical Jelly Bean KeyFinder for this tutorial because, well – come on, that name, right?

All you have to do is download and install Magical Jelly Bean KeyFinder. Then open the KeyFinder program to see your product key:

![Screenshot of the Windows product key in Magical Jellybean KeyFinder](https://www.freecodecamp.org/news/content/images/2020/12/magical-jellybean-keyfinder.jpg)

Once you've copied your product key somewhere safe, feel free to uninstall Magical Jelly Bean KeyFinder.

So those are some quick ways to find your Windows 10 product key.

Did any of these methods or programs work for you? Did you find another way to get your product key? Let me know over on [Twitter](https://twitter.com/home).

