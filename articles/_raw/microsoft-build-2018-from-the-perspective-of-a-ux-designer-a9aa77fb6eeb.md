---
title: Microsoft Build 2018 from the perspective of a UX designer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T18:46:03.000Z'
originalURL: https://freecodecamp.org/news/microsoft-build-2018-from-the-perspective-of-a-ux-designer-a9aa77fb6eeb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KUVkepN4MnBioPAqGhRCdg.png
tags:
- name: Fluent Design
  slug: fluent-design
- name: Microsoft
  slug: microsoft
- name: technology
  slug: technology
- name: ux design
  slug: ux-design
- name: Windows
  slug: windows
seo_title: null
seo_desc: "By Samuele Dassatti\nI recently attended Microsoft Build 2018 in Seattle,\
  \ because one of my apps was nominated for Design Innovator of the Year at the Windows\
  \ Developer Awards.   \nDuring the three-day conference, the Redmond giant detailed,\
  \ among othe..."
---

By Samuele Dassatti

I recently attended Microsoft Build 2018 in Seattle, because one of my apps was nominated for Design Innovator of the Year at the Windows Developer Awards.   
   
During the three-day conference, the Redmond giant detailed, among other things, what’s next for the Fluent Design System. This is the design language announced at last year’s Build, upon which Microsoft hopes to build the UI of Windows and its apps.

Here are the most important announcements relative to the future of user experience design on the Windows platform.

### Fluent all the things

One of the biggest trends from a UI perspective that I saw was Microsoft’s willingness to make the new design language available to the greatest number of developers possible, regardless of their framework of choice.  
   
We can summarize this strategy with three elements: **UWP XAML Islands**, the **Windows UI library** and **Fluent Design Web** (although just briefly teased). Let’s look at each one a little more closely.

### UWP XAML Islands

![Image](https://cdn-media-1.freecodecamp.org/images/y7eSHuzFbLdkk7o7arOBwEsSEfD0CzqH8zs3)

So, what are UWP XAML Islands? They are part of a new homonymous library that allows WinForms, WPF, and Win32 applications to feature UI elements that, up to this point, have been limited to UWP applications.   
   
This means that developers will be able to start gradually modernizing their applications’ UIs by integrating “islands” (the name finally makes sense) of XAML UI elements.

These islands could be a limited area of the UI or an entire window, thus allowing developers to keep the code-behind of a Windows legacy app while modernizing its appearance to increase user engagement and to make the application feel more consistent with the rest of the OS.

> A XAML Island is just a standard UWP control or even a complete UWP UI that is seamlessly composed inside of any other UI framework. […] It just works.

> Kevin Gallo, head of the Windows Developer Platform, at Microsoft Build 2018

### The Windows UI library

The core concept of the Windows UI library (or WinUI, as many Microsoft representatives referred to it) is very similar to that of the UWP XAML Islands. However, its purpose is very different.

Islands focuses on bringing UWP XAML controls on legacy application. On the other hand, WinUI would allow developers to leverage the versatility of XAML control that’s natively available only on the latest versions of Windows on every release of the OS (starting from the Anniversary Update, also known as version 1607).  
   
As you may expect, there’s been limited excitement for this new feature, since new Windows updates usually reach almost every Windows device in just a few months. But anyway, it is neat to have this feature.

![Image](https://cdn-media-1.freecodecamp.org/images/WrUMtrNigImCQTnQs5PHA2qbwZf82K1WeSXe)
_The WinUI library means that you can leverage the latest APIs in your app while reaching almost 10% more customers. The chart is based on the data from the AdDuplex report of April 2018_

### Fluent Design Web

If this is the first time you heard about this despite having closely followed the Build conference, don’t worry. The project was briefly teased in a Q&A session after a presentation about Progressive Web Apps and, at the time of writing, there has been no official confirmation.  
   
So here is what we know about it: Microsoft is trying to push its design system as not just being limited to the Windows platform. This is part of an effort by Microsoft to help web developers make their PWAs feel more native to the OS.

By the way, if you are interested in learning how to make your web app feel native, I suggest reading [this article](https://medium.freecodecamp.org/how-you-can-develop-progressive-web-apps-that-feel-native-5110fbbcbf4b).

### Expanding the Fluent toolkit

A key announcement at this year’s Build conference was the introduction of new windowing APIs for UWP apps. In particular, companion windows were finally introduced. I say “finally,” because this will allow the main window of the application to move some of its UI elements on smaller windows that follow the main one. This will make it possible for developers to build more complex apps for the Universal Windows Platform.

Another welcome addition was the new design principles applied to context menus. Not only will they be highlighted by a drop shadow that will render differently based on its position on the Z axis, but they are also subject to light dismiss (that is, the ability to dismiss them by just clicking outside). This will be represented by the use of the iconic acrylic effect.

I really hope that these subtle design changes will improve productivity for UWP users across the board.

![Image](https://cdn-media-1.freecodecamp.org/images/unmsLg6YtQsd8DCWXCmuK7ryMIzlRrzGAESq)
_An example of the new design of context menus_

### Making Fluent Design a multi-device, multi-sense experience

![Image](https://cdn-media-1.freecodecamp.org/images/cVxpVgVN3ZPasgS7Dz6ZgqL4uewSKNbaJfi3)
_The timeline of Microsoft Launcher is the first example of how Microsoft is trying to expand its design language beyond Windows_

During the second keynote, one of the first products to be mentioned by Joe Belfiore was the Microsoft Launcher for Android. The focus on such a product, which would have been unthinkable just a couple of years ago, highlights how Microsoft is serious about taking the Fluent Design System to other platforms. This also further strengthens Satya Nadella’s vision of the Microsoft experience being a multi-device, multi-sense one.  
   
The other key announcement regarding the universal nature of the design system was the new standard of density. It goes from the wide, touch-friendly rectangles of Metro to a healthy middle that allows users to see more details without sacrificing the usability on touch devices. Microsoft also showed an even denser standard, optimized for desktop-first and business apps.

### Wrapping up

Nothing particularly mind blowing design-wise was introduced. But the announcements from Build 2018 show a design system that, although lacking in certain fields it’s relatively young, is headed in the right direction. I think this is the case because Microsoft is focusing on making it truly universal and more versatile than ever before.  
   
I hope this article helped you understand the direction in which the Fluent Design System is headed and, if you have any thoughts about the recent announcements, I’ll be happy to read your responses.

