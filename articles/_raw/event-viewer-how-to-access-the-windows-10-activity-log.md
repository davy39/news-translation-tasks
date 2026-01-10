---
title: Event Viewer – How to Access the Windows 10 Activity Log
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-10-19T16:33:26.000Z'
originalURL: https://freecodecamp.org/news/event-viewer-how-to-access-the-windows-10-activity-log
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/eventViewer-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Windows 10
  slug: windows-10
seo_title: null
seo_desc: 'The Windows 10 Event Viewer is an app that shows a log detailing information
  about significant events on your computer. This information includes automatically
  downloaded updates, errors, and warnings.

  In this article, you''ll learn what the event vie...'
---

The Windows 10 Event Viewer is an app that shows a log detailing information about significant events on your computer. This information includes automatically downloaded updates, errors, and warnings.

In this article, you'll learn what the event viewer is, the different logs it has, and most importantly, how to access it on a Windows 10 computer.

## What is the Event Viewer? 

Each program you open on your Windows 10 computer sends a notification to a particular activity log in the Event Viewer. 

All other activity such as OS changes, security updates, driver quirks, hardware failure, and so on are also posted to a particular log. So you can think of the event viewer as a database that records every activity on your computer.

With the event viewer, you can troubleshoot different Windows and application issues.

If you explore the event viewer in-depth, you will see different information, warnings, and plenty of errors. Don’t freak out – this is normal. Even the best-maintained computers show plenty of errors and warnings.

## How to Access the Windows 10 Activity Log

There are 3 main ways you can gain access to the event viewer on Windows 10 – via the Start menu, Run dialogue, and the command line. 

### How to Access the Windows 10 Activity Log through the Start Menu

**Step 1**: Click on Start or press the WIN (Windows) key on your keyboard
**Step 2**: Search for “Event Viewer”
**Step 3**: Click on the first search result or press `ENTER`
![ss-1-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-1-5.jpg)

You will be greeted with this page:
![ss-2-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-2-1.png)

### How to Access the Windows 10 Activity Log through the Run Dialogue

**Step 1**: Right-click on Start (Windows log) and select “Run”, or press `WIN` (Windows key) + `R` on your keyboard
![ss-3-4](https://www.freecodecamp.org/news/content/images/2021/10/ss-3-4.jpg)

**Step 2**: Type in “eventvwr” to the editor and click “Ok” or hit `ENTER`
![ss-4-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-4-5.jpg)
![ss-5-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-5-5.png)

### How to Access the Windows 10 Activity Log through the Command Prompt

**Step 1**: Click on Start (Windows logo) and search for “cmd”
**Step 2**: Hit Enter or click on the first search result (should be the command prompt) to launch the command prompt
![ss-6-3](https://www.freecodecamp.org/news/content/images/2021/10/ss-6-3.jpg)

**Step 3**: Type in “eventvwr” and hit `ENTER`
![ss-7-2](https://www.freecodecamp.org/news/content/images/2021/10/ss-7-2.png)
![ss-8-2](https://www.freecodecamp.org/news/content/images/2021/10/ss-8-2.png)

## Event Viewer Activity Logs

When you open the event viewer to see your computer's activity logs, you are automatically shown the Event Viewer (Local) tab. But this might not contain the details you need, as it's just a page you are greeted with when you open the Event Viewer. 

There is lots more to the Event Viewer than this. 

### The Administrative Events Log

You can expand the Custom Views tab to see your computer’s administrative events, like this:
![ss-9](https://www.freecodecamp.org/news/content/images/2021/10/ss-9.png)

### The Windows Activity Logs

You can also expand the Windows Logs to show various activities such as:
- Application Events: Information, errors, and warning reports of program activities 
![ss-10](https://www.freecodecamp.org/news/content/images/2021/10/ss-10.png)

- Security Events: This shows the results of various security actions. They are called audits and each of them can be a success or a failure
![ss-11](https://www.freecodecamp.org/news/content/images/2021/10/ss-11.png)

- Setup Event: this has to do with domain controllers, which is a server that verifies users on computer networks. You shouldn’t worry about them day-to-day.
![ss-12](https://www.freecodecamp.org/news/content/images/2021/10/ss-12.png)

- System Events: these are reports from system files detailing the errors they have encountered
![ss-13-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-13-1.png)

- Forwarded Events: these are sent to your computer from other computers in the same network. They help you keep track of the event logs of other computers in the same newtwork. 
![ss-14-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-14-1.png)

In addition, there are the Application and Service logs, which show hardware and Internet Explorer activities, alongside Microsoft Office apps activities.

You can double click on an error to check its properties, and look up the event ID of the error online. This can help you discover more information on the error so you can fix it if you need to.
![ss-15](https://www.freecodecamp.org/news/content/images/2021/10/ss-15.png)

## Conclusion

In this article, you learned about the Windows 10 Event Viewer, which is a very powerful tool Windows users should know how to use. 

Apart from viewing various activity logs, it also helps you be aware of what's happening on your computer.

Thank you for reading. If you consider this article helpful, please share it with your friends and family.


