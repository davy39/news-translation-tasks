---
title: Your Connection is Not Private Error – How to Fix in Chrome
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-07T16:03:17.000Z'
originalURL: https://freecodecamp.org/news/your-connection-is-not-private-error-how-to-fix-in-chrome
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/castle-1290860_1280.jpg
tags:
- name: browser
  slug: browser
- name: Google Chrome
  slug: chrome
- name: privacy
  slug: privacy
- name: SSL
  slug: ssl
seo_title: null
seo_desc: 'If you log on to a website and your browser shows the “Your connection
  is not private” error, the browser is trying to warn you to stay off the website.


  In that case, the browser has run a check on the SSL (secure socket layer) certificate
  and found...'
---

If you log on to a website and your browser shows the “Your connection is not private” error, the browser is trying to warn you to stay off the website.
![Annotation-2022-07-06-111823-1](https://www.freecodecamp.org/news/content/images/2022/07/Annotation-2022-07-06-111823-1.png)

In that case, the browser has run a check on the SSL (secure socket layer) certificate and found a problem with it – the SSL could have expired or might not have been installed at all.

In some cases, the problem could be because of your browser and not the website. So, in this article, I will show you how to fix the “Your connection is not private” error on a Chrome browser.

## What We'll Cover
- [How to Fix the “Your connection is not private” Error on a Chrome Browser](#heading-how-to-fix-the-your-connection-is-not-private-error-on-a-chrome-browser)
 - [Reload the Web Page](#heading-reload-the-web-page) 
 - [Clear Chrome’s Cache](#heading-clear-chromes-cache)
 - [Make Sure your Computer’s Date and Time are Correct](#heading-make-sure-your-computers-date-and-time-are-correct)
 - [Disable your Antivirus and VPN](#heading-disable-your-antivirus-and-vpn)
- [Final Thoughts](#heading-final-thoughts)

## How to Fix the “Your connection is not private” Error on a Chrome Browser


### Reload the Web Page

The first thing I would advise you do is to reload the page.

Reloading the web page is the old trick everyone tries if there is a problem with that web page. 

In addition, there are chances that SSL-related work is going on with the website, so if you wait a while and reload the page, the issue could disappear.

If reloading doesn’t fix the issue for you, proceed to other solutions in this article.


### Clear Chrome’s Cache

The SSL data of the website in your Chrome browser cache might have expired. So if you clear the cache, the error may go away.

Follow the steps below to clear your Chrome browser cache:

**Step 1**: Click the 3 vertical dots on the top-right corner and select Settings:
![ss10-1](https://www.freecodecamp.org/news/content/images/2022/07/ss10-1.png)

**Step 2**: Click the “Privacy and Security” tab on the left sidebar and select “Clear browsing data”:
![ss11-1](https://www.freecodecamp.org/news/content/images/2022/07/ss11-1.png)

**Step 3**: Select Cache and Cookies, then click “Clear data”:
![ss12-1](https://www.freecodecamp.org/news/content/images/2022/07/ss12-1.png)


### Make Sure your Computer’s Date and Time are Correct

If your computer clock is behind or ahead, your browser will show you a “Your connection is not secure” error.

These days, the error message has become more accurate in Chrome:
![Annotation-2022-06-06-072807](https://www.freecodecamp.org/news/content/images/2022/07/Annotation-2022-06-06-072807.png)

In this case, you should set your date and time to the correct one and make it automatic, so nothing readjusts it again:
![ss](https://www.freecodecamp.org/news/content/images/2022/07/ss.png)
 

### Disable your Antivirus and VPN

Some Antivirus programs with SSL scanning features can make your browser show the “Your connection is not private” error if they detect any irregularity with the SSL certificate of a website.

In the same vein, a VPN (virtual private network) conceals your IP address and other information. The problem is that the privacy a VPN gives you could have a negative effect on some sites' SSL.

Due to this, you should consider disabling your antivirus and VPN programs, at least temporarily, to see if that fixes the error.


## Final Thoughts

Other fixes that might get rid of the “Your connection is not private” error for you include:
- Trying to access the web page in incognito mode. In Chrome, you can open an incognito tab by pressing `CTRL` + `SHIFT` + `N`.
- Restarting your Router
- Restarting your computer
- Updating your OS

If all the fixes fail to work, the problem could be from the website. This means there is a problem with the website’s SSL certificate. So, try to contact the site admin. 

If you find no admin to contact, you should stay off that website and make sure you don’t share sensitive information with the site.

If you’re a site admin and your users complain about this error, I wrote [an article on how you can restore your site’s SSL](https://www.freecodecamp.org/news/an-ssl-error-has-occurred-how-to-fix-certificate-verification-error/#howtofixsslerrorasasiteowner).


