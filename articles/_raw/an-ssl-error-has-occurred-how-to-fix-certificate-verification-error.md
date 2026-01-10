---
title: An SSL Error Has Occurred – How to Fix Certificate Verification Error
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-07-06T17:51:46.000Z'
originalURL: https://freecodecamp.org/news/an-ssl-error-has-occurred-how-to-fix-certificate-verification-error
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/ssl.png
tags:
- name: Application Security
  slug: application-security
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: SSL
  slug: ssl
- name: Windows
  slug: windows
seo_title: null
seo_desc: 'If you’re surfing the net and an SSL error occurs on a website you''re
  trying to visit, your browser will warn you by showing you an error messages or
  signal.

  This error is mostly caused by an expired or bad SSL certificate. It also occurs
  when the br...'
---

If you’re surfing the net and an SSL error occurs on a website you're trying to visit, your browser will warn you by showing you an error messages or signal.

This error is mostly caused by an expired or bad SSL certificate. It also occurs when the browser can’t verify the legitimacy of a website’s SSL certificate.

That error message could be a giant one like this:
![Annotation-2022-07-06-111823](https://www.freecodecamp.org/news/content/images/2022/07/Annotation-2022-07-06-111823.png)

The browser could also show you a signal in the address bar like this: 
![ss1-1](https://www.freecodecamp.org/news/content/images/2022/07/ss1-1.png)

In this article, I will show you what an SSL certificate is. I will also show you how to fix SSL errors as a site owner and as a user.

## What We'll Cover
- [What is SSL and Why is it Used?](#heading-what-is-ssl-and-why-is-it-used)
- [How to Fix SSL Error as a Site Owner](#heading-how-to-fix-ssl-error-as-a-site-owner)
 - [Purchase an SSL Certificate](#heading-purchase-an-ssl-certificate)
 - [Make sure you Turn on SSL on your Website](#heading-make-sure-you-turn-on-ssl-on-your-website)
 - [If your website is hosted on Github pages…](#heading-if-your-website-is-hosted-on-github-pages)
 - [If your website is hosted on Netlify…](#heading-if-your-website-is-hosted-on-netlify)
 - [If your website is a WordPress website…](#heading-if-your-website-is-a-wordpress-website)
 - [Contact your Hosting Provider](#heading-contact-your-hosting-provider)
- [How to Fix SSL Error as a User](#heading-how-to-fix-ssl-error-as-a-user)
 - [Make Sure your Date and Time are Correct ](#heading-make-sure-your-date-and-time-are-correct)
 - [Clear Saved SSLs on your Computer](#heading-clear-saved-ssls-on-your-computer)
 - [Clear your Browser’s Cache and Cookies](#heading-clear-your-browsers-cache-and-cookies)
- [Final Thoughts](#heading-final-thoughts)
## What is SSL and Why is it Used?

SSL stands for secure socket layer. It is the international standard security technology for keeping the sharing of information safe between a website and its users.

In the Chrome browser, when a website has a valid SSL, a locked padlock is shown in the address bar – indicating that any information the user shares with that website is encrypted.
![ss2-1](https://www.freecodecamp.org/news/content/images/2022/07/ss2-1.png)

## How to Fix SSL Error as a Site Owner

If you are a site owner and your users are complaining that your website shows SSL errors, you can fix the issue with any of the methods explained below:

### Purchase an SSL Certificate

If your website doesn’t have an SSL certificate installed, any modern browser your user is using will alert them your site is not secure.

In this case, you should purchase an SSL certificate from any of the providers out there.

By the way, you can buy an SSL certificate from companies that sell domain names. You can also buy an SSL from [Sectigo](https://sectigo.com/) or [SSLs](https://www.ssls.com/).


### Make sure you Turn on SSL on your Website

If you’ve purchased and installed an SSL but your website still shows SSL errors, it could happen because you unknowingly didn’t turn on SSL.


### If your website is hosted on Github pages…

**Step 1**: Navigate to your site repo and click Settings:
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/07/ss3-1.png)

**Step 2**: Click on Pages on the left sidebar:
![ss4-1](https://www.freecodecamp.org/news/content/images/2022/07/ss4-1.png)

**Step 3**: Tick “Enforce HTTPS”:
![ss5-1](https://www.freecodecamp.org/news/content/images/2022/07/ss5-1.png)

This is required for sites using GitHub’s default domain (example.github.io). 

Even if you’re using a custom domain, make sure that box is ticked.


### If your website is hosted on Netlify…

**Step 1**: Click on the site with an SSL error:
![ss6-1](https://www.freecodecamp.org/news/content/images/2022/07/ss6-1.png)

**Step 2**: Click on “Site Settings”:
![ss7-1](https://www.freecodecamp.org/news/content/images/2022/07/ss7-1.png)

**Step 3**: Click “Domain Management”, and then HTTPS on the left sidebar. Make sure there’s the message “Your site has HTTPS enabled”.
![ss8-1](https://www.freecodecamp.org/news/content/images/2022/07/ss8-1.png)


### If your website is a WordPress website…
If you have a WordPress website with an SSL error, install the [Force SSL plugin](https://wordpress.org/plugins/wp-force-ssl/) on your website
![ss9-1](https://www.freecodecamp.org/news/content/images/2022/07/ss9-1.png)

### Contact your Hosting Provider

If every method discussed above fails to work for you, then you should contact the customer service of your hosting provider.


## How to Fix SSL Error as a User

If you visit a website and you’re getting any SSL-related errors, there are some things you can do as a user. That’s because the problem is not always caused by the website – as long as an SSL certificate is installed on the website.


### Make Sure your Date and Time are Correct 

If your computer’s date and time are ahead or behind, the browser might show an SSL-related error. 

This is because SSLs have expiration dates. So, when your computer’s date and time are behind or ahead, the check your browser runs to see if the SSL certificate of that website is valid will fail.  

In this case, the browser will suggest that you change your date and time.


### Clear Saved SSLs on your Computer

Clearing the SSL certificates stored by your computer can fix the issue for you. 

When next you visit that website with the SSL error, your browser will run another check to revalidate the SSL installed on that website.

To clear the SSLs, hit the Windows button on your keyboard, search for “Internet Options” and click the Internet Options search result:
![ss13](https://www.freecodecamp.org/news/content/images/2022/07/ss13.png)

Switch to the content tab and click “Clear SSL state”:
![ss14](https://www.freecodecamp.org/news/content/images/2022/07/ss14.png)


### Clear your Browser’s Cache and Cookies

The SSL info of a website in your browser’s cache and cookies might have expired, so if you clear both records, it could fix the issue for you.

To clear Chrome’s cache and cookies, click the 3 vertical dots on the top-right corner and select Settings:
![ss10](https://www.freecodecamp.org/news/content/images/2022/07/ss10.png)

Switch to the Privacy and Security tab on the left sidebar and select “Clear browsing data”:
![ss11](https://www.freecodecamp.org/news/content/images/2022/07/ss11.png)

Select Cache and Cookies, then click “Clear data”:
![ss12](https://www.freecodecamp.org/news/content/images/2022/07/ss12.png)

If you’re using another browser that is not Chrome, clear the browser’s cache and cookies.


## Final Thoughts

As a web administrator or owner, it's very important to make sure SSL is installed and properly working on your website. Otherwise, it might not just affect your website alone, but also your business.

If you’re a user, too, make sure any website you’re visiting shows the padlock icon on the address bar. If that’s not the case, make sure you don’t share sensitive information like card details and passwords with the website.

Thank you for reading.



