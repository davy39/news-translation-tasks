---
title: Apple Safe Browsing Explained - Why Apple sends your data to Google and Tencent
  and how to turn it off
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-10-15T15:53:18.000Z'
originalURL: https://freecodecamp.org/news/apple-safe-browsing-explained-why-apple-sends-your-data-to-google-and-tencent-and-how-to-turn-it-off
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ff0740569d1a4ca459d.jpg
tags:
- name: iOS
  slug: ios
- name: Security
  slug: security
seo_title: null
seo_desc: If you use Safari on certain versions of iOS, then your IP address is being
  sent to Google or Tencent by default. Tencent is the Chinese equivalent of Facebook,
  who owns the popular WeChat mobile app. Tencent also works closely with the Chinese
  gover...
---

If you use Safari on certain versions of iOS, then your IP address is being sent to Google or Tencent by default. Tencent is the Chinese equivalent of Facebook, who owns the popular WeChat mobile app. Tencent also works closely with the Chinese government. It is possible to stop your data from being sent to these companies.

Devices send data to Tencent if the region code is set to mainland China. All other devices send data to Google.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-59.png)
_Notification on iPhone that your data will be sent to Google and Tencent._

Here is what an Apple spokesperson said about this feature in a statement to _The Register_:

> Apple protects user privacy and safeguards your data with Safari Fraudulent Website Warning, a security feature that flags websites known to be malicious in nature.

> When the feature is enabled, Safari checks the website URL against lists of known websites and displays a warning if the URL the user is visiting is suspected of fraudulent conduct like phishing. To accomplish this task, Safari receives a list of websites known to be malicious from Google, and for devices with their region code set to mainland China, it receives a list from Tencent.

> The actual URL of a website you visit is never shared with a safe browsing provider and the feature can be turned off.

While the actual URL you visit is not shared, your IP address is shared. Your IP address can reveal your general location and other details about you. It is shared in order to determine if the website you are visiting is a fraudulent site.

This data is being shared automatically by a lot of people. Safari has a U.S. market share of over 50% since it is the default browser on iOS devices.

Also, even if you use a third-party browser on your iOS device, your data may be still sent to Google and Tencent. When you view a web page from inside an app, the pages open inside a version of the Safari browser. Since many apps open Safari from within the app, it is almost impossible to avoid Safari.

To stop your IP address from being sent to Google and Tencent, you must disable the "Fraudulent Website Warning". Keep in mind that disabling this feature can make you more vulnerable to accessing fraudulent websites.

Here is how to disable the "Fraudulent Website Warning" in iOS:

1. In iOS settings, select "Safari".
2. Scroll down a bit and toggle "Fraudulent Website Warning" to the off position.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-60.png)
_How to disable sending data to Google and Tencent._

### What is "Safe Browsing"?

The "Fraudulent Website Warning" service uses Google Safe Browsing and Tencent Safe Browsing. This is a service originally developed by Google. Users sometimes come across malicious sites and phishing pages. Google has a big list of these sites and created "safe browsing" to help notify users when the site they are accessing could be malicious.

Here is how Google provides this service, called the "Update API", according to cryptography researcher [Matthew Green](https://blog.cryptographyengineering.com/2019/10/13/dear-apple-safe-browsing-might-not-be-that-safe/):

> 1. Google first computes the SHA256 _hash_ of each unsafe URL in its database, and truncates each hash down to a 32-bit prefix to save space.

> 2. Google sends the database of truncated hashes down to your browser.

> 3. Each time you visit a URL, your browser hashes it and checks if its 32-bit prefix is contained in your local database.

> 4. If the prefix is found in the browser’s local copy, your browser now sends the prefix to Google’s servers, which ship back a list of all _full_ 256-bit hashes of the matching URLs, so your browser can check for an exact match.

Presumably, the same method is used by Tencent in China. But instead of the hashed prefix being sent to Google, it is sent to Tencent. 

This process should be secure since the actual URLs you visit are not sent over, just a hashed version of the URL. However, some security researchers have pointed out that by analyzing the hundreds of hashed URLs sent to this service by a single user, it could be possible to de-anonymize that user.

Safari isn't the only browser using Google Safe Browsing. The Google Chrome, Firefox, Vivaldi, and GNOME Web browsers use the Google Safe Browsing service. So if you don't want your data sent to Google, choose a browser not on that list or disable the service within the browser settings.

Many people believe that it is worth sharing their IP addresses with Google and/or Tencent to get more protection from malicious sites. You have to decide for yourself if it is worth the risk.

