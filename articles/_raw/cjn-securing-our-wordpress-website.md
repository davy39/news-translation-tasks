---
title: Securing our WordPress Website
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-20T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/cjn-securing-our-wordpress-website
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/SSL-Certificate-https-1.jpg
tags:
- name: '#ssl'
  slug: hash-ssl
- name: '#wordpress'
  slug: hash-wordpress
- name: '#hosting'
  slug: hash-hosting
seo_title: null
seo_desc: 'By Clark Jason Ngo

  First step looking for free SSL

  Search for “hostgator free ssl”:

  HostGator Free SSL " HostGator.com Support Portal_We have progressively and methodically
  gone through the HostGator cPanel servers to ensure the free SSL certificates...'
---

By Clark Jason Ngo

# First step looking for free SSL

Search for “hostgator free ssl”:

[**HostGator Free SSL " HostGator.com Support Portal**](https://support.hostgator.com/articles/ssl-certificates/hostgator-free-ssl)  
[_We have progressively and methodically gone through the HostGator cPanel servers to ensure the free SSL certificates…_support.hostgator.com](https://support.hostgator.com/articles/ssl-certificates/hostgator-free-ssl)

Then i got a WordPress plugin suggestion for SSL:

[**Really Simple SSL**](https://wordpress.org/plugins/really-simple-ssl/)  
[_No setup required! You only need an SSL certificate, and this plugin will do the rest._wordpress.org](https://wordpress.org/plugins/really-simple-ssl/)

I went ahead and logged in as admin in our WordPress site.

Installed and activated the Really Simple SSL plugin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l82QH0ls5ERIOqTBGWPgTQ.png)

Upon checking the **lock** icon in the web address. it said “content not secure”.

i inspected the WordPress website and had a warning of **Mixed Content** from the background image we have.

It looked something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*_-JFxND1MBIL0ySeTnvmHw.png)

I Googled for “fixing Mixed Content”:

[**Preventing Mixed Content | Web Fundamentals | Google Developers**](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/fixing-mixed-content)  
[_Finding and fixing mixed content is an important task, but it can be time-consuming. This guide discusses some tools…_developers.google.com](https://developers.google.com/web/fundamentals/security/prevent-mixed-content/fixing-mixed-content)

I found fix **Mixed Content** problem by removing the background image and re-uploading the same image.

Some images were not fixed by re-uploading images right away.

It was complaining that an image was uploaded unsecurely (in an http).

I followed option 1 on this guide: [https://managewp.com/blog/wordpress-ssl-settings-and-how-to-resolve-mixed-content-warnings](https://managewp.com/blog/wordpress-ssl-settings-and-how-to-resolve-mixed-content-warnings)

### Option 1: Forcing All Pages to HTTPS

![Image](https://cdn-media-1.freecodecamp.org/images/1*Me0yLoTfqvYz9lzXqAbdAA.png)

After that, i re-uploaded the images.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hIs4N8RQ2YKf1p1gOw0pdQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NKfT_aw-JG4U6xVRZJEPKw.png)

Thanks for reading!

## Update. I recently updated an SSL certificate for a WordPress website hosted in GoDaddy.



1) I googled "buy godaddy ssl"

2) I followed this link [https://www.godaddy.com/web-security/ssl-certificate](https://www.godaddy.com/web-security/ssl-certificate)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-163.png)

3) It redirected me to the my billing page and I click buy

4) Go to My Products page and redeem your SSL

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-164.png)

5) Click on Managed WordPress, choose the Website you want the SSL installed and click Manage

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-165.png)

6) Click Install. Once installation is successful it should show Enabled.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-166.png)

7) Check your Website. It should now have a Lock icon, meaning it is secured. =)

%[https://www.youtube.com/watch?v=QJ8CkBMIvro&fbclid=IwAR2sBDELfC8ci-lfRU3VXcsjYgYn_qMy2ClxLGuZelJclqY6PfIXDZCbibY]

[**Clark Jason Ngo - Graduate Teaching Assistant - Technology Institute - City University of Seattle |…**](https://www.linkedin.com/in/clarkngo/)  
[_View Clark Jason Ngo's profile on LinkedIn, the world's largest professional community. Clark Jason has 9 jobs listed…_www.linkedin.com](https://www.linkedin.com/in/clarkngo/)  

