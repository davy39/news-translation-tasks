---
title: 502 Bad Gateway Error [Solved]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-22T00:45:26.000Z'
originalURL: https://freecodecamp.org/news/502-bad-gateway-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/502.png
tags:
- name: error handling
  slug: error-handling
seo_title: null
seo_desc: 'You can get a 502 bad gateway error when there''s a problem with the server
  of the website you are trying to connect to.


  In more technical terms, the “502” in the error is an HTTP status code which indicates
  that one server received an invalid respon...'
---

You can get a 502 bad gateway error when there's a problem with the server of the website you are trying to connect to.
![502-error](https://www.freecodecamp.org/news/content/images/2022/04/502-error.png)

In more technical terms, the “502” in the error is an HTTP status code which indicates that one server received an invalid response from another server. 

There are other categories of 500 errors including:
- 501 – Not Implemented, 
- 503 – Service Unavailable
- 504 – Gateway Timeout
- 505 – HTTP Version not supported
And many more.

The causes of the 502 bad gateway error include an overloaded server, an error in the code, and yet-to-be-propagated domain names. So the error is often caused by the server of a website and not by you as the user. 

But sometimes, the browser might show this error due to past-due updates, ad-blockers, browser extensions and plugins, or even DNS server problems.

In this article, I will show you 5 ways you can fix the 502 bad gateway error so you can access the internet again.

## Fix 1: Refresh the Page
Many server errors are only temporary, not permanent, and 502 bad gateway is no exception. 

If you’re getting this error, the first thing you should do is refresh the page after a couple of minutes and see if the website loads up again. 

To refresh Google Chrome, click on the refresh button in the top-left corner:
![ss1-6](https://www.freecodecamp.org/news/content/images/2022/04/ss1-6.png)

Edge also provides the same refresh button in the same position:
![ss2-7](https://www.freecodecamp.org/news/content/images/2022/04/ss2-7.png)

If refreshing fails to work, wait a couple of minutes and try again. If the error persists, then proceed to the other fixes in this article.

## Fix 2: Try to Access the Website on another Device
Your own device – whether it's a computer or phone – could be the reason you’re getting the 502 bad gateway error. In addition, your internet connection source – router or modem – could be the culprit.

Since this could be the cause, try to access the website on another device or switch your internet connection source.

You can also reboot your devices – computer, mobile phone, router, and modem.

## Fix 3: Switch to another Browser
Since the cause of the 502 bad gateway error could be due to an outdated browser or ad blockers, you should consider changing to a different browser and see if the error persists. 

For example, if you use the Windows operating system and you’re trying to access the website with Chrome and you're getting the 502 bad gateway error, switch to Edge and vice versa. If you are on Mac and you’re getting the error on Chrome, then consider switching to Safari and vice versa.  

If you have Mozilla Firefox installed on your computer, you can also switch to it too. You might get a different experience as it is not built on the same Chromium engine Edge and Google Chrome are built on.

If the website loads up in another browser, then you might need to update the initial browser, reinstall it, or check your extensions and ad blockers.

## Fix 4: Clear your Browser Cache
You might be getting the 502 bad gateway error because your browser stored outdated information about the website you’re trying to visit. So, clearing your browser cache could fix the error.

### To clear your Chrome browser cache, follow the steps below
**Step 1**: Click the 3 vertical dots on the top right corner:
![ss3-6](https://www.freecodecamp.org/news/content/images/2022/04/ss3-6.png)

**Step 2**: Hover on More tools and select Clear browsing data:
![ss4-4](https://www.freecodecamp.org/news/content/images/2022/04/ss4-4.png)

**Step 3**: Make sure you select "Cached images and files" as part of the data to clear, then click on the "Clear data" button:
![ss5-4](https://www.freecodecamp.org/news/content/images/2022/04/ss5-4.png)

### To clear your Microsoft Edge cache, follow the steps below
**Step 1**: Click on the 3 horizontal dots on the top-right corner:
![ss6-4](https://www.freecodecamp.org/news/content/images/2022/04/ss6-4.png)

**Step 2**: Select Settings:
![ss7-3](https://www.freecodecamp.org/news/content/images/2022/04/ss7-3.png)

**Step 3**: Click on "Privacy, search, and services”.

**Step 4**: Under, “Clear browsing data”, click on the “Choose what to clear" button:
![ss8-3](https://www.freecodecamp.org/news/content/images/2022/04/ss8-3.png)

**Step 5**: Make sure cached images and files are selected, then select “Clear now”:
![ss9-3](https://www.freecodecamp.org/news/content/images/2022/04/ss9-3.png)

## Fix 5: Flush your DNS Cache
DNS problems could be the reason you keep getting the 502 bad gateway error while trying to visit a website. So flushing your DNS cache could be a solution.

### To flush your DNS cache on Windows 10, follow the steps below:
**Step 1**: Click on Start, type “cmd”, then select “Run as Administrator” on the right:
![cmd-admin-1](https://www.freecodecamp.org/news/content/images/2022/04/cmd-admin-1.jpg)

**Step 2**: Type in “ipconfig /flushdns” and hit `ENTER`.
You should get a response that the DNS cache has been flushed, like the one below:
![ss10-3](https://www.freecodecamp.org/news/content/images/2022/04/ss10-3.png)

This means all caches will be cleared and websites will be loaded freshly for you.

### If you use Chrome, it has its own DNS cache
To flush Chrome’s DNS, type `chrome://net-internals/#dns` in the address bar and hit `ENTER`, then click “Clear host cache”:
![ss11-2](https://www.freecodecamp.org/news/content/images/2022/04/ss11-2.png)

### If you use Edge, it has its own DNS cache too

To flush Edge’s DNS, type `edge://net-internals/#dns` in the address bar and hit `ENTER`, then click “Clear host cache”:
![ss12-1](https://www.freecodecamp.org/news/content/images/2022/04/ss12-1.png)

## Conclusion
While it is unlikely for the 502 error to come from the user-side (as it’s a server-related error), you can still try some fixes on your end as the user. That’s why I wrote this article to show you how you can fix the error from your end.

Thank you for reading.


