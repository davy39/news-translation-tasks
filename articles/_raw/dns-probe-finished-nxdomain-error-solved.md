---
title: dns_probe_finished_nxdomain Error [Solved]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-20T15:39:02.000Z'
originalURL: https://freecodecamp.org/news/dns-probe-finished-nxdomain-error-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/earth-931552_1920.jpg
tags:
- name: Google Chrome
  slug: chrome
- name: error
  slug: error
seo_title: null
seo_desc: 'If you are a regular Google Chrome user, then you might have encountered
  the error “dns_probe_finished_nxdomain” before. It is usually accompanied by “This
  site can’t be reached”.


  This error is associated with the Domain Name System (DNS) server and...'
---

If you are a regular Google Chrome user, then you might have encountered the error “dns_probe_finished_nxdomain” before. It is usually accompanied by “This site can’t be reached”.
![ss1-5](https://www.freecodecamp.org/news/content/images/2022/04/ss1-5.png)

This error is associated with the Domain Name System (DNS) server and can occur due to misconfiguration in the DNS server, an unresponsive server, or a yet-to-be-propagated DNS of a website.  

The “nxdomain” in the error means you’re trying to access a “non-existent domain”.

In other browsers, the “dns_probe_finished_nxdomain” error could present itself in another way. On Microsoft Edge, it could appear as “Hmm…can’t reach this page”, and on Firefox, it usually appears as “Hmm. We’re having trouble finding that site”.

Fixing this error in order to restore your internet connectivity is not an uphill task. And so in this article, I’m going to show you 4 ways to fix it.

## What We'll Cover Here
- [Disable your Antivirus and VPN](#heading-fix-1-disable-your-antivirus-and-vpn)
- [Flush, Release,and Renew your DNS Cache](#heading-fix-2-flush-release-and-renew-your-dns-cache)
  - [Flush your Google Chrome Browser Cache](#youshouldalsoconsiderflushingchromesdns)) 
- [Restart your Router or Modem](#heading-fix-3-restart-your-router-or-modem)
- [Manually Change your DNS Server](#heading-fix-4-manually-change-your-dns-server)
  - [Change your Google Chrome Browser DNS Server](#heading-you-can-also-change-the-dns-server-of-the-google-chrome-browser-in-particular) 
- [Conclusion](#heading-conclusion)

## Fix 1 – Disable Your Antivirus and VPN
Antivirus programs are notorious for interfering with apps and stopping them from working the right way.

VPNs, on the other hand, can block some websites, while some other websites don't work well with them.

If you are getting the “dns_probe_finished_nxdomain” error, consider disabling your Antivirus and turning off your VPN, then check to make sure you can access the internet again. 

If you are able to access the internet after disabling your antivirus program and turning off your VPN, then this is the reason you’re getting the error. 

If you are on Windows 10, you can disable Windows Security by following the steps below:
**Step 1**: Open the Task Manager by pressing `ALT` + `SHIFT` + `ESC` on your keyboard.

**Step 2**: Click on the Startup tab.

**Step 3**: Locate your Antivirus Program in the list, right-click on it, and select "Disable".
![ss3-4](https://www.freecodecamp.org/news/content/images/2022/04/ss3-4.png)

Try to access the internet again to see if the error isn't shown anymore. If this fails to fix the error, keep reading and try other fixes in this article.

## Fix 2 – Flush, Release, and Renew your DNS Cache
The DNS cache saves the IP addresses of websites you visited in order to speed up load time when you try to visit the same sites.

Flushing, releasing, and renewing the DNS cache can fix the “dns_probe_finished_nxdomain” error because the processes removes invalid IP configurations and outdated information in the DNS cache.

To flush, release, and renew your computer’s DNS on Windows, follow the steps highlighted below:
**Step 1**: Hit the `WIN` button on your keyboard and search for "cmd". Then select "Run as Administrator" on the right.

**Step 2**: Enter and execute the following commands one after the other:
- `ipconfig /flushdns`
- `ipconfig /release`
- `ipconfig /renew
![ss4-3](https://www.freecodecamp.org/news/content/images/2022/04/ss4-3.png)

### You should also consider flushing Chrome’s DNS.

To flush Chrome's DNS, all you need to do is type `chrome://net-internals/#dns` in the address bar and hit `ENTER`. Then click “Clear host cache”:
![flushChromeDNS-1](https://www.freecodecamp.org/news/content/images/2022/04/flushChromeDNS-1.png)
 
After flushing your computer's DNS along with Chrome's, restart your computer and check to see if you don’t get the error anymore.

## Fix 3 – Restart your Router or Modem
If you access the internet through a router or modem, restarting it could help you get rid of the “dns_probe_finished_nxdomain” error. 

This is because turning off and then turning on a router or modem clears the cache of IP addresses, which could fix the error in the long run.

To restart your router or modem, locate the power button and long-press to turn it off, then long-press again to turn it on.

## Fix 4 – Manually Change your DNS Server 
If any of the fixes above fail to work for you, you should consider changing your DNS server address as it is one of the most reliable ways to fix the “dns_probe_finished_nxdomain” error.

By default, a DNS server address is provided by your internet service provider, but using this default DNS is not always secure. And it could be the reason you are getting the “dns_probe_finished_nxdomain” error.

You can change your DNS server to one of the free ones provided by the likes of Google and Cloudflare.

The steps below show you how to change your DNS server to Google: 
**Step 1**: Right-click on Start and select “Network Connections”:
![ss5-3](https://www.freecodecamp.org/news/content/images/2022/04/ss5-3.png)

**Step 2**: Scroll down and select “Change adapter options”:
![ss6-3](https://www.freecodecamp.org/news/content/images/2022/04/ss6-3.png)

**Step 3**: In the pop-up that appears, right-click on the network you are connected to and select “Properties”:
![ss7-2](https://www.freecodecamp.org/news/content/images/2022/04/ss7-2.png)

**Step 4**: In another pop-up that appears, double-click on “Internet Protocol Version 4 (TCP/IPv4)”:
![ss8-2](https://www.freecodecamp.org/news/content/images/2022/04/ss8-2.png)

**Step 5**: Another pop-up will appear. This time around, select the radio button that says “Use the following DNS server addresses”:
![ss9-2](https://www.freecodecamp.org/news/content/images/2022/04/ss9-2.png)

**Step 6**: Enter 8.8.8.8 for “Preferred DNS server” and 8.8.4.4 for “Alternate DNS server”. This is the free DNS server provided by Google.
![ss10-2](https://www.freecodecamp.org/news/content/images/2022/04/ss10-2.png)

**Step 7**: Click “Ok”, and “Ok” once again. 

**N.B.**: If your computer is configured to use IPv6 instead of IPv4, then in step 4, you should choose “Internet Protocol Version 6 (TCP/IPv6)” instead of “Internet Protocol Version 4 (TCP/IPv4)”. Then enter `2001:4860:4860::8888` for the preferred DNS server and `2001:4860:4860::8844` for the alternative DNS server.

### You can also change the DNS server of the Google Chrome browser in particular.

To do this, head over to your chrome browser, type `chrome://settings/security` in the address bar and hit `ENTER`.
![ss2-6](https://www.freecodecamp.org/news/content/images/2022/04/ss2-6.png)

On the page that appears, scroll down, click on “Custom”, and select “Google (Public DNS)”:
![ss3-5](https://www.freecodecamp.org/news/content/images/2022/04/ss3-5.png)

After doing all this, check to see if your internet connection is restored.

## Conclusion
As you can see in this article, resolving the “dns_probe_finished_nxdomain” error is not difficult because there are several ways you can fix it. This article discussed 4 of those ways.

If one of the fixes fails to resolve the error for you, then you should check out any of the rest. As for me, I experienced this error not long ago and what fixed it for me was changing my DNS server – [Fix 4](#heading-fix-4-manually-change-your-dns-server).

Thank you for reading.


