---
title: How to Secure Mobile Apps – A Mobile App Security Checklist
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-02T23:18:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-mobile-apps
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/mobile-app-security.jpg
tags:
- name: Application Security
  slug: application-security
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: "By Roger James\nSecurity has always been a major concern for businesses.\
  \ And this concern is even greater when it comes to mobile apps. \nToday every business\
  \ has a mobile app to connect more easily with their customers. And if that business\
  \ does not t..."
---

By Roger James

Security has always been a major concern for businesses. And this concern is even greater when it comes to mobile apps. 

Today every business has a mobile app to connect more easily with their customers. And if that business does not take proper security protections it can put their brand at risk.

Mobile devices span multiple operating systems and, given the distributed nature of components, mobile app security often experiences problems.

I hope your business is properly secured and you are just looking for a mobile app security checklist for the future. If that's the case, good for you – being a business owner means you must take care of mobile app security. 

**But according to a [survey](https://www.pixelcrayons.com/blog/mobile-app-stats/?utm_source=freecodecamp&utm_medium=mobile%2Bapp%2Bdevelopment_sk&utm_campaign=website), more than 75% of mobile applications will fail basic security tests.**

Many employees download apps from app stores and use mobile applications that can access enterprise assets or perform business functions. And unfortunately, these applications have little or no security assurances. They are exposed to attacks and violations of enterprise security policies all the time.

I know that nobody wants to be a part of this failure. That is why you need to follow a proper mobile app security checklist.

## Enforce Strong Authentication

To prevent unauthorised access and password guessing attacks, you should implement multi-factor authentication. The three main factors for authentication are

* something that a user knows, such as a password or PIN
* something the user has, such as a mobile device
* or something the user is, such as a fingerprint.

Combining password-based authentication with a client certificate, device ID, or one-time password significantly reduces the risk of unauthorised access. You can also implement time-of-day and location-based restrictions to prevent fraud.

## Encrypt Mobile Communications

With threats like snooping and man-in-the-middle attacks over WiFi and cellular networks, IT should make sure that all communications between mobile apps and app servers are encrypted. 

Strong encryption that leverages 4096-bit SSL keys and session-based key exchanges can prevent even the most determined hackers from decrypting communications.

Besides encrypting traffic, IT should confirm that data at rest—the sensitive data stored on users' phones—is also encrypted. For ultra-sensitive data, IT might want to prevent data from ever being downloaded to the end user device at all.

## Patch App and Operating System Vulnerabilities

Recent Android and iOS vulnerabilities such as [Stagefright](https://play.google.com/store/apps/details?id=com.zimperium.stagefrightdetector&hl=en_IN) and [XcodeGhost](https://www.macrumors.com/2015/09/20/xcodeghost-chinese-malware-faq/) have exposed mobile users to attack. 

In addition to mobile OS flaws, IT must contend with a never-ending succession of app updates and fixes. 

To protect mobile users from attack, IT should check mobile devices and ensure that the latest patches and updates have been applied.

## Protect Against Device Theft

Every year, millions of mobile devices are lost or stolen. To ensure sensitive data does not end up in the wrong hands, IT should provide a way to remotely wipe sensitive data Or—better yet—make sure data is never stored on mobile devices in the first place.

For employee-owned devices, IT should lock or wipe corporate information while leaving personal apps and files intact. When the device is found or replaced, IT should be able to quickly restore users’ apps and data.

## Scan Mobile Apps for Malware

Eliminate malware and adware by testing apps for malicious behaviour. Malware can be detected using virtual sandboxing or signature-based scanning tools. For mobile workspace or virtual mobile solutions, perform malware scans on the server.

## Protect app data on your device

Make sure developers are not storing any sensitive data on their devices. If you must store data on device for some reason, first make sure it's encrypted/protected. And then only store it in files, data stores, and databases.

If you use the latest encryption technologies, you can get a higher level of security.

## Secure the Platform

Your platform should be properly secured and controlled. This process consists of detecting [jailbroken phones](https://www.scribd.com/document/226019655/IOS-Application-Security-Part-24-Jailbreak-Detection-and-Evasion) and preventing access to other services when needed. 

## Prevent Data Leaks

To avoid data leaks while still allowing users to install personal apps on their mobile devices, IT must separate business apps from personal apps. 

Creating secure mobile workspaces helps prevent malware from accessing corporate apps and stops users from copying, saving, or distributing sensitive data.

### For ironclad data leak prevention of confidential data:

* Control clipboard access to prevent copy and paste functions
* Block screen captures
* Prevent users from downloading confidential files to their phone or saving files on file sharing sites or connected devices or drives.
* Watermark sensitive files with users’ usernames and timestamps

## Optimise Data Caching‌‌

Did you know that mobile devices usually store cached data in order to enhance an app's performance? This is a major cause of security issues because those apps and devices become more vulnerable and it is relatively easy for attackers to breach and decrypt the cached data. This often results stolen user data.

You can require a password to access the application in case the nature of your data is extremely sensitive. This will help reduce vulnerabilities associated with cached data. ‌‌

After that, set up an automatic process that wipes cached data whenever the device gets restarted. This helps reduce the cache and mitigate security concerns.

## Isolate Application Information‌‌

You need to separate all information accessed through a mobile device from a user’s data. And this process of isolating information requires a few levels of protection around enterprise-deployed apps. This way corporate data will be separated from the employee’s private data as well as the consumer-facing application. ‌‌

This process of isolating data should increase your customers' satisfaction and productivity, all while making sure they're compliant with your security rules. 

Using a container-based model can help you out in this case. Security is often more strict and won't compromise at any level of transmission. This ultimately helps eliminate the risk of corporate data loss. ‌‌‌‌‌‌‌‌

## Final words‌‌

Before setting up your business – or even if you are already running one – try to implement this mobile app security checklists. It'll help you protect your business from any fraud or loss. ‌‌

I know that security is a major concern and can't simply be resolved by going through a few steps. If you need some help, contact any [mobile app development company](https://www.pixelcrayons.com/mobile-app-development/?utm_source=freecodecamp&utm_medium=mobile%2Bapp%2Bdevelopment_sk&utm_campaign=website) which can guide you through the process.

