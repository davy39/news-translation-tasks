---
title: How to Stay GDPR Compliant with Access Logs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-08T16:24:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-stay-gdpr-compliant-with-access-logs
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/privacy.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: '#gdpr'
  slug: gdpr
- name: privacy
  slug: privacy
seo_title: null
seo_desc: 'By Yuli Stremovsky

  Privacy is a complicated topic. A well-known method used to save application logs
  turned out to be tricky with the new privacy regulations. In fact, new regulations
  define an IP address as a personal identifier. Like other user ide...'
---

By Yuli Stremovsky

Privacy is a complicated topic. A well-known method used to save application logs turned out to be tricky with the new privacy regulations. In fact, new regulations define an IP address as a personal identifier. Like other user identifiers, it should be treated with caution.

In this article, I will cover a few methods to make your logging privacy-friendly. 

First, I will teach you basic **GDPR terms**: **PII** and **forget-me user right**. After that, we will cover methods to make web or application server logs GDPR ready. 

Then I will talk about an open-source product I am developing called **[Databunker](http://databunker.org/)** and how it helps. **Databunker** is a Swiss army knife tool for storing personal records.

## Some GDPR-related terms

### What is Personal Identifiable Information?

GDPR defines the concept of **PII** or **Personal Identifiable Information**. This can be any information that helps to identify a person. 

For example, it can be a user name, address, telephone number, email address, or SSN. It can also be a weak identity, like browser information, IP address, session cookie name. 

Like in triangulation, a combination of weak identities can lead us to a user. Strong and weak user identities are all considered **PII**.

The **GDPR** introduces the right for individuals to have their personal data erased. Your user or customer can send you an email asking you to remove their records. You have one month to respond to this request.

### What does a forget-me request mean for log files?

Deleting user data from the database is easy. You have SQL for that. Deleting user PII from the log file is the tricky part. 

You might have different servers generating logs and you might feed logs to different cloud services. This might complicate how you perform record deletion. 

In this article I will cover smarter methods to make your logging privacy-compliant.

### Introduction to Databunker

But first, let me give you a bit more information about what **Databunker** is and how it works since we'll be discussing it in some of these methods below.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/databunker-solution.png)

**Databunker** is a GDPR compliant user store service for Web and mobile apps. It works as a backend application service. This product is a combination of several software concepts merged together. It provides secure PII storage and privacy by design out of the box:

* A Personal Identifiable Information (PII) storage and vault
* Secure session storage for web applications
* Privacy portal for customers
* Application backend server
* DPO management tool
* Tokenization service
* Secret sauce

Project website: [https://databunker.org/](https://databunker.org/)

Full working Node.js example with Passport.js is available here: [https://github.com/securitybunker/databunker-nodejs-example](https://github.com/securitybunker/databunker-nodejs-example)

## Method 1: Use an automatic log retention period

You have **one month** to respond to a **user forget-me request**. This actually means that you have one month to filter your log files from all user-related records – for example, filter out user IP addresses. 

Or you can limit the log retention period just to one month. All older log entries will get removed. This way you do not need to do anything besides a one-time configuration of the log retention period.

## Method 2: Use pseudonymization to resolve any log compliance issues

GDPR discusses the concept of **pseudonymization**. This method will be based on the usage of the pseudonymization term. From the [GDPR Article 4(5)](https://gdpr-info.eu/art-4-gdpr/):

> _‘pseudonymisation’ means the processing of personal data in such a manner that the personal data can no longer be attributed to a specific data subject without the use of additional information, provided that such additional information is kept separately and is subject to technical and organisational measures to ensure that the personal data are not attributed to an identified or identifiable natural person..._

You can keep personal data in a separate database, for example in **Databunker**. When you receive a user's **forget-me request**, you will delete the user's personal data from **Databunker**, **leaving the log files unchanged**.

To make our life even easier, we can print a user session and user token in each log line.

You can take a look at [this example](https://github.com/securitybunker/databunker-nodejs-example) for reference:

> ::ffff:141.226.198.55 - - [02/Jan/2021:18:42:54 +0000] "GET /user/me HTTP/1.1" 304 - "http://my-dev-site/user/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36" **"b994fdbf-694e-4289-b8db-04d8049da2e8" "1f587eb7-eaaa-1629-c108-b707d99798da"**

This is different from a regular web server log by the addition of two custom variables at the end of the log line.

**"B994fdbf-694e-4289-b8db-04d8049da2e8**" is the session token generated by the Databunker session library.

**"1f587eb7-eaaa-1629-c108-b707d99798da"** is a user token of the logged-in user. It is the user token generated upon user creation in Databunker.

## Method 3: Solution for high-security environments

This method includes partial encryption of the log events. PII found in the log events will be grouped together and encrypted. The initial setup will include one time generation of the log-entry password for each user. This password for example can be saved in the user profile stored in **Databunker**.

As we need to know who the record owner is (to decrypt the record), we need to save the user id together with encrypted PII. So, another level of encryption will be used with a generic password.

For user identified log events, PII will be encrypted twice. The first time the data will be encrypted using the user's log-entry password. The second time, it'll be encrypted with the default password to hide the identified user id.

For identified users:

```
const piiPayload = JSON.stringify({ClientIP, BrowserUserAgent, SessionID});
coast piiEncrypted = Encrypt(UserPassword, piiPayload);
const linePayload = JSON.stringify({UserToken, data: btoa(piiEncrypted)});
const encrypted = Encrypt(GenericPassword, linePayload);
```

If the user is unknown, only one level of encryption can be used:

```
const piiPayload = JSON.stringify({ClientIP, BrowserUserAgent, SessionID});
const encrypted = Encrypt(GenericPassword, piiPayload);
```

When you get a user's forget-me request, you can remove the user's log-entry password and their profile stored in **[Databunker](http://databunker.org/)**. This will make user log entries unrecoverable. This is completely ok and satisfies GDPR requirements. So extra actions to remove anything from logs files are not required.

## Summary

With the right architecture, you can make your logging privacy compliant. It is not complicated. You can use **Databunker** or roll your own solution. 

Whatever you choose is much better than completely ignoring this issue and manually removing user records from log files.

### Free takeaway

I run a privacy training for startup founders and architects. It is [available completely for FREE here](https://basebunker.com/).

### About the author

Yuli Stremovsky is a world-class software and security architect. Founder of [PrivacyBunker.io](https://privacybunker.io/) and [DataBunker.org](http://databunker.org/) privacy products. Former Checkpoint, and RSA Security employee. An expert in marrying technological solutions with privacy.

  


  


  


  


  


  

