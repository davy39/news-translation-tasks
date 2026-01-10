---
title: I figured out a way to hack any of Facebook’s 2 billion accounts, and they
  paid me a $15,000 bounty…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-09T11:41:36.000Z'
originalURL: https://freecodecamp.org/news/responsible-disclosure-how-i-could-have-hacked-all-facebook-accounts-f47c0252ae4d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YxD3C1C9qLsIGG4pqLv7ig.jpeg
tags:
- name: Facebook
  slug: facebook
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By AppSecure

  I am publishing this with the permission of Facebook under the responsible disclosure
  policy. They have fixed this vulnerability.

  This post is about a simple vulnerability I discovered on Facebook which I could
  have used to hack into oth...'
---

By AppSecure

I am publishing this with the permission of Facebook under the responsible disclosure policy. They have fixed this vulnerability.

This post is about a simple vulnerability I discovered on Facebook which I could have used to hack into other users’ Facebook accounts easily and without any user interaction.

This gave me full access to other users account by setting a new password. I was able to view messages, their credit/debit cards stored under their payment section, personal photos, and other private information.

Facebook acknowledged the issue promptly, fixed it, and rewarded me with a US $15,000 bounty based on the severity and impact of this vulnerability.

### How the hack worked

Whenever a user Forgets their password on Facebook, they have an option to reset the password by entering their phone number and email address on [https://www.facebook.com/login/identify?ctx=recover&lwv=110](https://www.facebook.com/login/identify?ctx=recover&lwv=110&__mref=message).

Facebook will then send a 6 digit code to this phone number or email address which the user has to enter in order to set a new password.

I tried to brute force the 6 digit code on [www.facebook.com](http://www.facebook.com/?__mref=message) and was blocked after 10–12 invalid attempts.

Then I looked out for the same issue on beta.facebook.com and mbasic.beta.facebook.com. Interestingly, rate limiting was missing from forgot password endpoint.

I tried to take over my own account (as per Facebook’s policy, you should not do any harm any other users’ accounts) and was successful in setting a new password for my account. I could then use this same password to log into my own hacked account.

### A proof of concept video of the hack

As you can see in the video, I was able to set a new password for the user by brute forcing the code which was sent to their email address and phone number.

### **Vulnerable request**

`POST /recover/as/code/ HTTP/1.1`

`Host: beta.facebook.com`

`lsd=AVoywo13&n=XXXXX`

Brute forcing the “n” successfully allowed me to set new password for any Facebook user.

### **Disclosure Timeline**

Feb 22nd, 2016 : Report sent to Facebook team.

Feb 23rd, 2016 : Verified the fix from my end.

March 2nd, 2016 : Bounty of $15,000 awarded by Facebook

