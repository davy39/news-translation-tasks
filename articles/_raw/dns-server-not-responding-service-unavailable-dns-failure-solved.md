---
title: DNS Server Not Responding – Service Unavailable DNS Failure [Solved]
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-11T15:59:55.000Z'
originalURL: https://freecodecamp.org/news/dns-server-not-responding-service-unavailable-dns-failure-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/binary-g3068c576e_1920.jpg
tags:
- name: dns
  slug: dns
- name: error
  slug: error
- name: internet
  slug: internet
- name: servers
  slug: servers
seo_title: null
seo_desc: "Sometimes, you might suddenly discover that you can’t access the internet\
  \ on your computer because of the error “DNS server not responding”. \nIf you run\
  \ a troubleshooter for the issue, you'll get a message like the below:\n\nIn your\
  \ Chrome browser, you..."
---

Sometimes, you might suddenly discover that you can’t access the internet on your computer because of the error “DNS server not responding”. 

If you run a troubleshooter for the issue, you'll get a message like the below:
![ss1-1](https://www.freecodecamp.org/news/content/images/2022/04/ss1-1.png)

In your Chrome browser, you might also get an error like the one below:
![ss2-2](https://www.freecodecamp.org/news/content/images/2022/04/ss2-2.png)

This is because the Domain Name System (DNS) server is crucial in getting an internet connection on your computer.

As far as websites are concerned, the “DNS server not responding” error could be caused by DNS gaps and a DDoS (Distributed Denial of Service) attack. If this is the problem, you might have to wait for 72 hours for domain gaps to be fixed or the website admins to fix the security issues with the website.

On the user’s end, the “DNS server not responding” error could be caused by numerous reasons such as misconfigured DNS settings and outdated browsers. 

If this is the cause, I will show you 7 ways to fix the error so you can restore your internet connection.

## Table of Contents
- [How Does the DNS System Work?](#heading-how-does-the-dns-system-work)
- [7 Ways to Fix the DNS Server Not Responding Error](#heading-7-ways-to-fix-the-dns-server-not-responding-error)
  - [Solution 1: Switch Browsers](#heading-solution-1-switch-browsers)
  - [Solution 2: Temporarily Disable Your Antivirus](#heading-solution-2-temporarily-disable-your-antivirus)
  - [Solution 3: Restart your Router or Modem](#heading-solution-3-restart-your-router-or-modem)
  - [Solution 4: Flush your DNS Cache](#heading-solution-4-flush-your-dns-cache)
  - [Solution 5: Manually Change your DNS Server](#heading-solution-5-manually-change-your-dns-server)
  - [Solution 6: Update Your Network Adapter Driver](#heading-solution-6-update-your-network-adapter-driver)
  - [Solution 7: Disable IPv6](#heading-solution-7-disable-ipv6)
- [Final Thoughts](#heading-final-thoughts)
## How Does the DNS System Work?

Whenever you try to access a website, like freeCodeCamp.org, you type in the URL like “freecodecamp.org” to the address bar and hit `ENTER`. 

Under the hood, the DNS server looks up the numerical address for freeCodeCamp.org. This numerical address is called an Internet Protocol (IP) address.

Once the browser gets this IP address, the website (freeCodeCamp.org or any other) will be shown to you. If the browser fails to find this address, then you might get the “DNS server not responding” error.

## 7 Ways to Fix the DNS Server Not Responding Error

Now let's go through seven ways you can use to get rid of the “DNS server not responding” error so your internet connection can be restored.

### Solution 1: Switch Browsers

The “DNS server not responding” error could be showing up because of the browser you’re currently using. Some browsers have their own DNS cache and if there’s an issue with the cache, your internet experience on that browser could be negatively affected. 

So, a non-complicated fix is to change to a different browser and see if the error persists. 

For example, if you are using Chrome, switch to Edge if you are on Windows or Safari if you are using Mac. 

If the website loads up in another browser, then you might need to update your other browser or reinstall it.

### Solution 2: Temporarily Disable Your Antivirus

Antivirus programs are notorious for interfering with applications and stopping them from working properly.

If you are getting the “DNS server not responding” error, consider disabling your antivirus program to see if your internet connection works fine. 

If you are able to access the internet after disabling the antivirus, then it is the reason you’re getting the error. 

In this case, you may want to consider getting another antivirus program.

If you are on Windows 10, you can disable Windows Security (AKA Windows Defender) by following the steps below:
**Step 1**: Press `ALT` + `SHIFT` + `ESC` on your keyboard to open the Task Manager

**Step 2**: Switch to the Startup tab

**Step 3**: Locate your Antivirus Program in the list, right-click on it and select "Disable".
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/04/ss3-1.png)

### Solution 3: Restart your Router or Modem

If your internet connection relies on a router or modem, restarting it could help you get rid of the “DNS server not responding” error. 

This is because turning off and then turning on a router or modem clears the cache of IP addresses. This could fix the error in the long run.

To restart your router or modem, locate the power button and long press to turn it off, then turn it on again.

### Solution 4: Flush your DNS Cache

If the “DNS server not responding” error is due to misconfiguration on your device, flushing your DNS is one of the most reliable ways to fix it. This is because the process would remove invalid IP configurations and outdated information in the DNS cache.

To flush your computer’s DNS on Windows, follow the steps highlighted below:

**Step 1**: Hit the `WIN` button on your keyboard and search for "cmd". Then select "Run as Administrator" on the right.

**Step 2**: Enter and execute the following commands one after the other:
- `ipconfig /flushdns`
- `ipconfig /release`
- `ipconfig /renew`
![ss4](https://www.freecodecamp.org/news/content/images/2022/04/ss4.png)

**Step 3**: Restart your computer


### Solution 5: Manually Change your DNS Server

Using the default DNS server of your internet service provider could be the reason you are getting the “DNS server not responding” error.

You can change your DNS server to one of the free ones provided by the likes of Google and Cloudflare.

The steps below show you how to change your DNS server to Google's: 

**Step 1**: Right-click on Start and select “Network Connections”:
![ss5](https://www.freecodecamp.org/news/content/images/2022/04/ss5.png)

**Step 2**: Scroll down and select “Change adapter options”:
![ss6](https://www.freecodecamp.org/news/content/images/2022/04/ss6.png)

**Step 3**: In the pop-up that appears, right-click on the network you are connected to and select “Properties”:
![ss7](https://www.freecodecamp.org/news/content/images/2022/04/ss7.png)

**Step 4**: In the next pop-up that appears, double-click on “Internet Protocol Version 4 (TCP/IPv4)”:
![ss8](https://www.freecodecamp.org/news/content/images/2022/04/ss8.png)

**Step 5**: In the following pop-up that appears, click the radio button that says “Use the following DNS server addresses”:
![ss9](https://www.freecodecamp.org/news/content/images/2022/04/ss9.png)

**Step 6**: Enter 8.8.8.8 for “Preferred DNS server” and 8.8.4.4 for “Alternate DNS server”:
![ss10](https://www.freecodecamp.org/news/content/images/2022/04/ss10.png)

This is the free DNS server provided by Google.

**Step 7**: Click “Ok”, and “Ok” again.

N.B.: If your computer is configured to use IPv6 instead of IPv4, then in step 4, you should choose “Internet Protocol Version 6 (TCP/IPv6)” instead of “Internet Protocol Version 4 (TCP/IPv4)”.


### Solution 6: Update Your Network Adapter Driver

Updating your network adapter driver can fix a lot of technical issues – including the “DNS server not responding” error, since the new driver could include bug fixes.

To update your network adapter driver, you can do it with the steps below:

**Step 1**: Click on Start and select Device Manager.

**Step 2**: Expand Network Adapters.

**Step 3**: Right-click on the affected driver and select Update driver:
![ss11](https://www.freecodecamp.org/news/content/images/2022/04/ss11.png)

**Step 4**: Choose Search automatically for updated driver software:
![ss12](https://www.freecodecamp.org/news/content/images/2022/04/ss12.png)

**Step 5**: Allow your computer to search for a driver online and install it for you. When it is done installing, restart your computer.

### Solution 7: Disable IPv6

If your current network is configured to use IPv4 and IPv6 is turned on on your computer, it could lead to negative interference which could make you get the “DNS server not responding” error.

To disable IPv6, the following steps can help you:

**Step 1**: Right-click on Start and select “Network Connections”:
![ss5](https://www.freecodecamp.org/news/content/images/2022/04/ss5.png)

**Step 2**: Scroll down and select “Change adapter options”:
![ss6](https://www.freecodecamp.org/news/content/images/2022/04/ss6.png)

**Step 3**: In the pop-up that appears, right-click on the network you are connected to and select “Properties”:
![ss7](https://www.freecodecamp.org/news/content/images/2022/04/ss7.png)

**Step 4**: In the next pop-up that appears, uncheck “Internet Protocol Version 6 (TCP/IPv6)”:
![ss13](https://www.freecodecamp.org/news/content/images/2022/04/ss13.png)

**Step 6**: Click “Ok”, and “Ok” again.

## Final Thoughts

The “DNS server not responding” error can be frustrating and disturb your internet experience. But in this article you've learned how to fix it if the error is caused by misconfiguration of DNS from the user’s end. 

I hope one of the solutions to the error explained in this article helps you fix the error.


