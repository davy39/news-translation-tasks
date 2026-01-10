---
title: Transparent Taskbar – How to Make a Task Bar Transparent in Windows 10 PC
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-01-26T00:11:44.000Z'
originalURL: https://freecodecamp.org/news/transparent-taskbar-how-to-make-a-task-bar-transparent-in-windows-10-pc-2
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/task-bar.png
tags:
- name: how-to
  slug: how-to
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'Making your Windows taskbar transparent is a pretty cool thing to do. It
  looks great, and it''s one of the few ways you can personalize your taskbar.

  Some resources about this topic require you to install different software to accomplish
  it. But in th...'
---

Making your Windows taskbar transparent is a pretty cool thing to do. It looks great, and it's one of the few ways you can personalize your taskbar.

Some resources about this topic require you to install different software to accomplish it. But in this tutorial we'll see how to make the taskbar completely transparent without any installations.

## How to Make your Windows Taskbar Transparent

### Step 1 - Use the Run command to open the Registry Editor program

The Run command allows you to open various programs on your PC by typing their name. The program we will be using is called Registry Editor.

To use the Run command, you can use the shortcut **Win + R** (Windows button + R) or you can **right click** on the Windows icon and click on "Run".

![Image](https://www.freecodecamp.org/news/content/images/2022/01/run-command.png)

### **Step 2 - Type regedit**

After clicking on Run, a window should pop up where you can type in the name of a program you would like to open. Type "regedit" and press OK. This will open the Registry Editor.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/regedit.png)

After clicking OK, the window below should pop up:

![Image](https://www.freecodecamp.org/news/content/images/2022/01/registry.png)

### **Step 3 - Navigate through folders**

The first folder to expand is the `HKEY_CURRENT_USER` folder. Scroll down and expand the `SOFTWARE` folder. 

After that, locate the `Microsoft` folder and expand it as well. Next, scroll all the way down and expand the `Windows` folder. 

In the `Windows` folder, expand the `CurrentVersion` folder followed by expanding the `Explorer` folder. Lastly, click on the `Advanced` folder. 

If you found the steps above confusing, then you can use this path as a guide:

```
Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Advanced
```

Pasting the path above and hitting enter should automatically bring you to our current location.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/paths.png)

### **Step 4 - Create a new file**

Right click and hover above the "New" option.

Then click on **DWORD (32-bit) Value**:

![Image](https://www.freecodecamp.org/news/content/images/2022/01/new.png)

After clicking on **DWORD (32-bit) Value**, you will see a space where you are supposed to type in the new file. Name the file `TaskbarAcrylicOpacity`. After you have created the file, double click on it and set the **value data** input to 0 (zero) and click OK.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/value-data.png)

### **Step 5 - Enable transparency effects**

Go to Desktop and right click. Click on personalize.

Click on the "Colors" tab, and toggle Transparency effects to **`On`**:

![Image](https://www.freecodecamp.org/news/content/images/2022/01/personalize.png)

After this, you should have a transparent taskbar. 

If the last step does not work for you, then go on with next steps.

### **Step 6 - Restart Windows Explorer using Task Manager**

Before opening task manager, make sure that your File Explorer is already running. Then follow these steps: 

* Right click on taskbar.
* Click on Task Manager.
* Right click on File Explorer under Apps.
* Click on Restart

![Image](https://www.freecodecamp.org/news/content/images/2022/01/restart.png)

After completing the last step, you should have a completely transparent taskbar.

## Conclusion

In this tutorial, we made our taskbar transparent without installing any software in Windows 10. I hope this works for you.

Thank you for reading!

